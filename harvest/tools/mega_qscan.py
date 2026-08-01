#!/usr/bin/env python3
"""Surface r/quant + r/quantfinance megathread comments that state an actual assessment question.

reddit.com returns 403 to this machine, so these 2,235 comments — pulled whole-thread from the
Arctic Shift mirror by tools/arctic_mega3.py — are readable only through the mirror. Deleted
comments keep their body in the mirror, which is the point of the exercise.
"""
import json
import re
import sys

FIRM = re.compile(r'\b(SIG|Susquehanna|Jane\s*Street|\bJS\b|Citadel|Optiver|IMC|HRT|Hudson\s*River|'
                  r'Jump\s*Trading|\bJump\b|DRW|Five\s*Rings|Akuna|Two\s*Sigma|D\.?\s*E\.?\s*Shaw|'
                  r'DEShaw|deshaw)\b', re.I)
# Signals that the comment reproduces a prompt rather than talking about the process.
Q = re.compile(
    r'(asked (me|us|him|her)?\s*(to|the|this|a|about)|the question (was|is)|questions? (were|was):|'
    r'\bwhat(\'s| is| was) the (probability|expected|chance|ev\b|edge|fair)|'
    r'\bexpected (value|number|payoff)\b|\byou (are given|have|roll|flip|draw|pick)\b|'
    r'\bgiven (a|an|the|two|three|n|\d)\b|\bfair (coin|die|dice)\b|\bhow many\b|'
    r'\bimplement\b|\bwrite a (function|program|script)\b|\bmake a market\b|\bbid[/-]ask\b|'
    r'\bmarket mak(e|ing) on\b|\bprobability that\b|\bdeck of cards\b|\bcoin flips?\b|'
    r'\bdice\b|\bbrainteaser was\b|\bpuzzle was\b|\bthey ask\b|\bthey asked\b)', re.I)

data = json.load(open('.arctic_mega/_comments.json', encoding='utf-8'))
mode = sys.argv[1] if len(sys.argv) > 1 else 'q'
n = 0
for c in sorted(data, key=lambda x: x.get('created_utc', 0)):
    b = (c.get('body') or '').strip()
    if b in ('', '[removed]', '[deleted]') or len(b) < 60:
        continue
    if mode == 'q' and not (FIRM.search(b) and Q.search(b)):
        continue
    if mode == 'firm' and not FIRM.search(b):
        continue
    n += 1
    print('=' * 78)
    print(f"### {c['id']}  r/{c['subreddit']}  author={c.get('author')}  "
          f"score={c.get('score')}  utc={c.get('created_utc')}")
    print('URL: https://www.reddit.com' + (c.get('permalink') or ''))
    print(b[:3000])
    print()
print(f'# matched {n} of {len(data)}', file=sys.stderr)
