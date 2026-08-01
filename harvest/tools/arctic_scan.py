#!/usr/bin/env python3
"""Scan whatever Arctic Shift responses are cached and surface posts that actually
contain assessment questions (as opposed to career chatter)."""
import glob
import json
import re
import sys

FIRMS = {
    'SIG': r'\bSIG\b|Susquehanna', 'Jane Street': r'Jane\s*Street',
    'Citadel': r'Citadel', 'Optiver': r'Optiver', 'IMC': r'\bIMC\b',
    'HRT': r'\bHRT\b|Hudson River', 'Jump Trading': r'Jump\s*Trading',
    'DRW': r'\bDRW\b', 'Five Rings': r'Five\s*Rings', 'Akuna': r'Akuna',
    'Two Sigma': r'Two\s*Sigma', 'D. E. Shaw': r'D\.?\s*E\.?\s*Shaw',
}
# wording that signals an actual problem statement rather than "how do I prepare"
QSIG = re.compile(
    r'(what is the probability|expected value of|compute the|you (are|have) given|'
    r'suppose (that )?(you|there|we)|find the (number|probability|expected|minimum|maximum)|'
    r'a fair (coin|die|dice)|roll(ed|s|ing)? (a|two|three|\d) dic?e|'
    r'flip(s|ped|ping)? (a|two|\d+) coins?|urn|marbles?|'
    r'the question (was|is)|asked me to|the problem (was|is)|one of the questions)', re.I)
STOP = re.compile(r'^\s*(\[removed\]|\[deleted\])\s*$')


def main():
    seen = {}
    for p in glob.glob('/workspace/harvest/.arctic_chat/*.json'):
        try:
            d = json.load(open(p, encoding='utf-8'))
        except Exception:
            continue
        for o in d.get('data') or []:
            body = (o.get('selftext') or '').strip()
            if not body or STOP.match(body) or len(body) < 80:
                continue
            seen[o['id']] = o
    rows = []
    for o in seen.values():
        blob = (o.get('title') or '') + '\n' + o['selftext']
        firms = [f for f, pat in FIRMS.items() if re.search(pat, blob)]
        if not firms:
            continue
        hits = QSIG.findall(blob)
        rows.append((len(hits), o, firms))
    rows.sort(key=lambda r: -r[0])
    print(f'posts with intact bodies mentioning a target firm: {len(rows)}')
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 25
    for score, o, firms in rows[:n]:
        print('=' * 100)
        print(f"[{score}] r/{o['subreddit']}  {o.get('created_utc')}  {firms}")
        print(f"https://reddit.com/comments/{o['id']}   removed_by={o.get('removed_by_category')}")
        print('TITLE:', o.get('title'))
        print(o['selftext'][:1800])


if __name__ == '__main__':
    main()
