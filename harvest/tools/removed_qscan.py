#!/usr/bin/env python3
"""Surface firm-named recall posts that reddit.com no longer serves but the mirror still holds.

The pool is tools/arctic_removed.py's 1,878 title-matched posts whose selftext survived.
A post counts as recovered-from-archive when removed_by_category is set (automod filter,
moderator removal, deleted-by-author) — reddit.com renders those as [removed] while the
Arctic Shift mirror keeps the body it ingested before removal.
"""
import json
import re
import sys

FIRM = re.compile(r'\b(SIG|Susquehanna|Jane\s*Street|Citadel|Optiver|IMC|HRT|Hudson\s*River|'
                  r'Jump\s*Trading|DRW|Five\s*Rings|Akuna|Two\s*Sigma|D\.?\s*E\.?\s*Shaw)\b', re.I)
Q = re.compile(
    r'(they asked|i (was|got) asked|asked me to|the question was|questions? were|first question|'
    r'expected value|probability that|make a market|implement (a|an|the)|write a function|'
    r'brainteaser|mental math|the oa (was|had|is|consisted)|oa consisted|sequences?\b|'
    r'\bwhat is the (probability|expected|chance|fair)|\byou (are given|have|roll|flip|draw|pick)|'
    r'\bfair (coin|die|dice)\b|\bhow many\b|\bdeck of cards\b|\bcoin flips?\b|zap|'
    r'\bnumber ?logic\b|\border ?book|\bintervals?\b|\bmarket mak)', re.I)

posts = json.load(open('raw/_chat_arctic/arctic_posts.json', encoding='utf-8'))
mode = sys.argv[1] if len(sys.argv) > 1 else 'removed'
n = 0
for p in sorted(posts, key=lambda x: x.get('created_utc', 0), reverse=True):
    body = (p.get('selftext') or '').strip()
    rbc = p.get('removed_by_category')
    if mode == 'removed' and not rbc:
        continue
    if not FIRM.search(p.get('title', '') + ' ' + body):
        continue
    if not Q.search(body):
        continue
    n += 1
    print('=' * 78)
    print(f"### {p['id']}  r/{p['subreddit']}  u/{p.get('author')}  removed_by={rbc}  "
          f"score={p.get('score')}  utc={p.get('created_utc')}")
    print('TITLE:', p.get('title'))
    print('URL: https://www.reddit.com' + (p.get('permalink') or ''))
    print(body[:2600])
    print()
print(f'# matched {n} of {len(posts)}', file=sys.stderr)
