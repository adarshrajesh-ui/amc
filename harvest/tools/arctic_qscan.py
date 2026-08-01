#!/usr/bin/env python3
"""Surface Arctic-Shift-preserved reddit posts that actually contain an assessment question.

Reddit itself returns 403 to this machine, and r/quant automod-filters most OA threads, so a
post with removed_by_category set but selftext intact is a recall that is gone from reddit.com
and readable only here.
"""
import glob
import json
import re
import sys

Q = re.compile(
    r'(asked (me|us)?\s*(the|this|a)?|the question (was|is)|question asked|'
    r'\bwhat is the (probability|expected|chance)|\bexpected value\b|'
    r'\byou (are given|have|roll|flip|draw)\b|\bgiven (a|an|the|two|three|n)\b|'
    r'\bfair (coin|die|dice)\b|\bhow many\b|\bwhat.s the (probability|ev|edge)\b|'
    r'\bimplement\b|\bwrite a (function|program)\b|\bmake a market\b|\bbid.ask\b)', re.I)
FIRM = re.compile(r'\b(SIG|Susquehanna|Jane\s*Street|Citadel|Optiver|IMC|HRT|Hudson\s*River|'
                  r'Jump|DRW|Five\s*Rings|Akuna|Two\s*Sigma|D\.?\s*E\.?\s*Shaw)\b', re.I)

posts = {}
for f in glob.glob('.arctic_chat/*.json') + glob.glob('.arctic_cache/*.json'):
    try:
        d = json.load(open(f, encoding='utf-8'))
    except Exception:
        continue
    for o in (d.get('data') or []):
        posts[o['id']] = o

removed_only = '--removed' in sys.argv
n = 0
for o in sorted(posts.values(), key=lambda x: x.get('created_utc', 0)):
    body = (o.get('selftext') or '').strip()
    if body in ('', '[removed]', '[deleted]') or len(body) < 80:
        continue
    if removed_only and not o.get('removed_by_category'):
        continue
    blob = o['title'] + '\n' + body
    if not (Q.search(blob) and FIRM.search(blob)):
        continue
    n += 1
    print('=' * 78)
    print(f"### r/{o['subreddit']}  {o['id']}  removed={o.get('removed_by_category')}  "
          f"score={o.get('score')}  comments={o.get('num_comments')}")
    print('URL: https://www.reddit.com' + o['permalink'])
    print('TITLE:', o['title'])
    print(body[:2500])
    print()
print(f'# matched {n}', file=sys.stderr)
