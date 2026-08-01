#!/usr/bin/env python3
"""Surface reddit thread comments that reproduce an assessment question.

Input is .arctic_thr/_cmts.json — every comment of the 141 firm-named recall threads found by
the title/question sweep, pulled from the Arctic Shift mirror because reddit.com 403s this box.
The recall posts themselves nearly always just ask "what should I expect"; when an actual
question surfaces it is in a reply, often from someone who has already sat the round.
"""
import json
import re
import sys

FIRM = re.compile(r'\b(SIG|Susquehanna|Jane\s*Street|Citadel|Optiver|IMC|HRT|Hudson\s*River|'
                  r'Jump\s*Trading|DRW|Five\s*Rings|Akuna|Two\s*Sigma|D\.?\s*E\.?\s*Shaw)\b', re.I)
Q = re.compile(
    r'(they asked|i (was|got) asked|asked me to|the question was|questions were|'
    r'\bwhat(\'s| is| was) the (probability|expected|chance|ev\b|fair value)|'
    r'\bexpected (value|number|payoff)\b|\byou (are given|have|roll|flip|draw|pick)\b|'
    r'\bgiven (a|an|the|two|three|n|\d)\b|\bfair (coin|die|dice)\b|\bhow many\b|'
    r'\bimplement (a|an|the)\b|\bwrite a (function|program|class)\b|\bmake a market\b|'
    r'\bprobability (that|of)\b|\bdeck of cards\b|\bcoin flips?\b|\bbrainteaser\b|'
    r'\bleetcode \d|\blc \d|\bfirst question\b|\bsecond question\b|\bone question\b)', re.I)

data = json.load(open('.arctic_thr/_cmts.json', encoding='utf-8'))
strict = '--strict' in sys.argv
n = 0
for c in sorted(data, key=lambda x: x.get('created_utc', 0)):
    b = (c.get('body') or '').strip()
    if b in ('', '[removed]', '[deleted]') or len(b) < 50:
        continue
    if not Q.search(b):
        continue
    if strict and not FIRM.search(b):
        continue
    n += 1
    print('=' * 78)
    print(f"### {c['id']}  r/{c['subreddit']}  u/{c.get('author')}  score={c.get('score')} "
          f"utc={c.get('created_utc')}")
    print('URL: https://www.reddit.com' + (c.get('permalink') or ''))
    print(b[:2200])
    print()
print(f'# matched {n} of {len(data)}', file=sys.stderr)
