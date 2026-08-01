#!/usr/bin/env python3
"""Scan the per-thread comment cache for replies that reproduce an assessment question.

Reads .arctic_thr2/*.json directly rather than the merged dump so it can be run while the
pull is still in flight. Drops AutoModerator boilerplate and anything already cited in the
JSONL.
"""
import json
import os
import re
import sys

FIRM = re.compile(r'\b(SIG|Susquehanna|Jane\s*Street|Citadel|Optiver|IMC|HRT|Hudson\s*River|'
                  r'Jump\s*Trading|DRW|Five\s*Rings|Akuna|Two\s*Sigma|D\.?\s*E\.?\s*Shaw)\b', re.I)
Q = re.compile(
    r'(\bwhat(\'s| is| was) the (probability|expected|chance|fair|ev\b)|'
    r'\bexpected (value|number|payoff|profit)\b|\byou (are given|roll|flip|draw|pick)\b|'
    r'\bfair (coin|die|dice)\b|\bdeck of cards\b|\bcoin flips?\b|\bmake a market\b|'
    r'\bthe question was\b|\bthey asked me to\b|\bfirst question was\b|\bimplement a\b|'
    r'\bwrite a function\b|\bgiven an array\b|\bgiven a string\b|\bthe sequence was\b)', re.I)

seen = set()
for l in open('raw/chat_and_archive.jsonl', encoding='utf-8'):
    m = re.search(r'/comments/[a-z0-9]+/[^/]*/([a-z0-9]+)/', json.loads(l)['source_url'])
    if m:
        seen.add(m.group(1))

rows = {}
for fn in os.listdir('.arctic_thr2'):
    if not fn.endswith('.json') or fn.startswith('_'):
        continue
    try:
        d = json.load(open('.arctic_thr2/' + fn, encoding='utf-8'))
    except Exception:
        continue
    for c in d.get('data') or []:
        rows[c['id']] = c

n = 0
for c in sorted(rows.values(), key=lambda x: x.get('created_utc', 0), reverse=True):
    b = (c.get('body') or '').strip()
    if (c.get('author') == 'AutoModerator' or c['id'] in seen or len(b) < 60
            or b in ('[removed]', '[deleted]')):
        continue
    if not (Q.search(b) and FIRM.search(b)):
        continue
    n += 1
    print('=' * 76)
    print(f"### {c['id']} r/{c['subreddit']} u/{c.get('author')} score={c.get('score')} "
          f"utc={c.get('created_utc')}")
    print('URL: https://www.reddit.com' + (c.get('permalink') or ''))
    print(b[:2000])
    print()
print(f'# matched {n} of {len(rows)} cached comments', file=sys.stderr)
