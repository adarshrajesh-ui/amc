#!/usr/bin/env python3
"""Scan the downloaded Arctic Shift comment/post dumps for Tier-A firm recalls.

Tier A here = HRT, Jump, DRW, Five Rings, Akuna, Old Mission, Two Sigma, D. E. Shaw.
Reddit itself 403s this box, so the archive body text is the only way to read these.
"""
import glob
import json
import re
import sys

FIRMS = {
    'HRT': r'\bHRT\b|Hudson\s*River',
    'Jump Trading': r'Jump\s*Trading|\bJump\b',
    'DRW': r'\bDRW\b',
    'Five Rings': r'Five\s*Rings|5\s*Rings',
    'Akuna Capital': r'Akuna',
    'Old Mission Capital': r'Old\s*Mission',
    'Two Sigma': r'Two\s*Sigma|2\s*Sigma',
    'D. E. Shaw': r'D\.?\s*E\.?\s*Shaw|DE\s*Shaw|DEShaw',
}

# Wording that signals an actual problem statement / recalled question.
QSIG = re.compile(
    r'(what(?:\'s| is| was) the probability|expected value|expected number|'
    r'compute the|you are given|you have \d|suppose (?:that )?(?:you|there|we)|'
    r'find the (?:number|probability|expected|minimum|maximum|smallest|largest)|'
    r'a fair (?:coin|die|dice)|roll(?:ed|s|ing)? (?:a|two|three|\d) dic?e|'
    r'flip(?:s|ped|ping)? (?:a|two|\d+) coins?|\burn\b|marbles?|deck of cards|'
    r'the question (?:was|is)|asked me to|they asked me|the problem (?:was|is)|'
    r'one of the questions|first question|second question|the questions were|'
    r'market mak|brain\s?teaser|estimate how many|how many .{0,40}\?|'
    r'OA (?:had|was|consisted|question)|got asked|leetcode (?:hard|medium)|'
    r'asked about|interview question)', re.I)

# Wording that signals it is a first-person recall, not speculation.
FIRSTP = re.compile(
    r'\bI (?:had|did|got|was asked|interviewed|took|applied|received)|'
    r'\bmy (?:OA|interview|onsite|superday|first round|final round|phone screen)|'
    r'\bthey asked me|\bI remember|\bwhen I interviewed', re.I)

STOP = re.compile(r'^\s*(\[removed\]|\[deleted\])\s*$')


def load_all():
    seen = {}
    paths = []
    paths += glob.glob('/workspace/harvest/raw/_tiera_reddit/*.json')
    paths += glob.glob('/workspace/harvest/.arctic_cache/*.json')
    paths += glob.glob('/workspace/harvest/.arctic_chat/*.json')
    paths += glob.glob('/workspace/harvest/raw/_reddit_cache/*.json')
    for p in paths:
        try:
            d = json.load(open(p, encoding='utf-8'))
        except Exception:
            continue
        objs = d.get('data') if isinstance(d, dict) else d
        if not isinstance(objs, list):
            continue
        for o in objs:
            if not isinstance(o, dict):
                continue
            oid = o.get('id')
            if oid:
                seen.setdefault(oid, o)
    return seen


def text_of(o):
    t = (o.get('title') or '')
    b = (o.get('body') or o.get('selftext') or '')
    return (t + '\n' + b).strip()


def main():
    seen = load_all()
    sys.stderr.write('loaded %d objects\n' % len(seen))
    rows = []
    for o in seen.values():
        blob = text_of(o)
        if len(blob) < 60 or STOP.match(blob):
            continue
        firms = [f for f, pat in FIRMS.items() if re.search(pat, blob)]
        if not firms:
            continue
        qh = len(QSIG.findall(blob))
        fp = len(FIRSTP.findall(blob))
        if qh == 0:
            continue
        rows.append((qh * 2 + fp, qh, fp, o, firms))
    rows.sort(key=lambda r: -r[0])
    sys.stderr.write('candidates: %d\n' % len(rows))
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    off = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    for score, qh, fp, o, firms in rows[off:off + n]:
        print('=' * 100)
        pid = o.get('link_id', '').replace('t3_', '')
        kind = 'comment' if o.get('body') else 'post'
        url = ('https://www.reddit.com/r/%s/comments/%s/_/%s/' % (o.get('subreddit'), pid, o['id'])
               if kind == 'comment' else
               'https://www.reddit.com/r/%s/comments/%s/' % (o.get('subreddit'), o['id']))
        print('[%d q=%d fp=%d] %s r/%s utc=%s %s' % (score, qh, fp, kind, o.get('subreddit'),
                                                     o.get('created_utc'), firms))
        print(url)
        if o.get('title'):
            print('TITLE:', o['title'])
        print(text_of(o)[:2500])


if __name__ == '__main__':
    main()
