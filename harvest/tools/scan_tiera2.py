#!/usr/bin/env python3
"""Second pass over the Reddit archive: keep only text that recalls a SPECIFIC
question at a specific Tier-A firm, and drop prep-guide / resource-list posts."""
import glob
import json
import re
import sys

FIRMS = {
    'HRT': r'\bHRT\b|Hudson\s*River',
    'Jump Trading': r'Jump\s*Trading',
    'DRW': r'\bDRW\b',
    'Five Rings': r'Five\s*Rings|5\s*Rings',
    'Akuna Capital': r'Akuna',
    'Old Mission Capital': r'Old\s*Mission',
    'Two Sigma': r'Two\s*Sigma',
    'D. E. Shaw': r'D\.?\s*E\.?\s*Shaw|DE\s*Shaw|DEShaw',
}

# A recalled question almost always carries one of these.
RECALL = re.compile(
    r'(they asked me|I was asked|got asked|asked me (?:to|about|for|a|the|how|what|why)|'
    r'the question was|questions were|first question|second question|third question|'
    r'one question|the OA (?:was|had|consisted|is)|OA had|my OA|the problems? was|'
    r'the problems? were|I got (?:a|an|the|two|three|\d)|they gave me|'
    r'asked (?:me )?(?:some|a bunch of|a few|several)|'
    r'the (?:first|second|final|last) round (?:was|had|consisted))', re.I)

# Concrete question content: numbers, math nouns, or an actual interrogative.
CONCRETE = re.compile(
    r'(probability|expected value|expected number|dice|die\b|coin|deck|cards|'
    r'urn|marble|random variable|distribution|variance|market mak|'
    r'bid.{0,10}ask|EV of|combinatoric|permutation|binary search|dynamic programming|'
    r'linked list|hash ?map|segment tree|graph|matrix|regression|'
    r'brownian|martingale|option|call\b|put\b|delta|gamma|vega|'
    r'estimate how many|how many|what.{0,5}s the (?:chance|probability|expected))', re.I)

# Prep-guide / resource-dump tells.
GUIDE = re.compile(
    r'(green book|heard on the street|comprehensive guide|resources in one place|'
    r'ultimate guide|here.{0,3}s everything|# Background:|Practice Platforms|'
    r'quant research of the week|SSRN|recommended books|reading list|'
    r'my top recommendation|non-negotiable)', re.I)

STOP = re.compile(r'^\s*(\[removed\]|\[deleted\])\s*$')


def load_all():
    seen = {}
    for pat in ('/workspace/harvest/raw/_tiera_reddit/*.json',
                '/workspace/harvest/.arctic_cache/*.json',
                '/workspace/harvest/.arctic_chat/*.json',
                '/workspace/harvest/raw/_reddit_cache/*.json'):
        for p in glob.glob(pat):
            try:
                d = json.load(open(p, encoding='utf-8'))
            except Exception:
                continue
            objs = d.get('data') if isinstance(d, dict) else d
            if not isinstance(objs, list):
                continue
            for o in objs:
                if isinstance(o, dict) and o.get('id'):
                    seen.setdefault(o['id'], o)
    return seen


def text_of(o):
    return ((o.get('title') or '') + '\n' + (o.get('body') or o.get('selftext') or '')).strip()


def main():
    seen = load_all()
    sys.stderr.write('loaded %d\n' % len(seen))
    rows = []
    for o in seen.values():
        blob = text_of(o)
        if len(blob) < 80 or STOP.match(blob) or GUIDE.search(blob):
            continue
        firms = [f for f, pat in FIRMS.items() if re.search(pat, blob)]
        if not firms:
            continue
        if not RECALL.search(blob):
            continue
        nc = len(CONCRETE.findall(blob))
        if nc == 0:
            continue
        # Prefer text where the firm name sits near the recall verb.
        prox = 0
        for f, pat in FIRMS.items():
            for m in re.finditer(pat, blob):
                w = blob[max(0, m.start() - 400):m.end() + 700]
                if RECALL.search(w) and CONCRETE.search(w):
                    prox += 1
        rows.append((prox * 3 + nc, prox, nc, o, firms))
    rows.sort(key=lambda r: -r[0])
    sys.stderr.write('candidates: %d\n' % len(rows))
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    off = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    for score, prox, nc, o, firms in rows[off:off + n]:
        print('=' * 100)
        pid = (o.get('link_id') or '').replace('t3_', '')
        kind = 'comment' if o.get('body') else 'post'
        url = ('https://www.reddit.com/r/%s/comments/%s/comment/%s/'
               % (o.get('subreddit'), pid, o['id']) if kind == 'comment'
               else 'https://www.reddit.com/r/%s/comments/%s/' % (o.get('subreddit'), o['id']))
        print('[%d prox=%d c=%d] %s r/%s utc=%s %s' %
              (score, prox, nc, kind, o.get('subreddit'), o.get('created_utc'), firms))
        print(url)
        print(text_of(o)[:3000])


if __name__ == '__main__':
    main()
