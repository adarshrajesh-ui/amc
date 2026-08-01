#!/usr/bin/env python3
"""Sweep the Arctic Shift mirror for reddit posts whose TITLE looks like a recall post.

r/quantfinance in particular is full of "<firm> interview question" posts; many are images of
the actual prompt and many have since been removed by moderators. reddit.com 403s this machine,
so the mirror is the only way in.
"""
import json
import os
import re
import subprocess
import sys
import time
import urllib.parse

API = 'https://arctic-shift.photon-reddit.com/api'
CACHE = '.arctic_title'
os.makedirs(CACHE, exist_ok=True)


def get(path, **params):
    url = '%s/%s?%s' % (API, path, urllib.parse.urlencode(params))
    p = os.path.join(CACHE, re.sub(r'[^A-Za-z0-9]+', '_', url)[:170] + '.json')
    if os.path.exists(p):
        try:
            return json.load(open(p, encoding='utf-8')).get('data') or []
        except Exception:
            pass
    delay = 2.5
    for _ in range(5):
        time.sleep(delay)
        r = subprocess.run(['curl', '-s', '--max-time', '90', url], capture_output=True)
        try:
            d = json.loads(r.stdout.decode('utf-8', errors='replace'))
        except Exception:
            delay = min(delay * 2, 40)
            continue
        if d.get('error'):
            delay = min(delay * 2, 40)
            continue
        open(p, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False))
        return d.get('data') or []
    return []


SUBS = ['quantfinance', 'quant', 'FinancialCareers', 'csMajors', 'cscareerquestions',
        'quantfinancecareers', 'algotrading']
TITLES = ['interview question', 'oa question', 'online assessment', 'interview questions',
          'superday', 'trading game', 'phone interview', 'first round', 'mental math',
          'interview experience', 'oa', 'assessment']

if sys.argv[1] == 'sweep':
    seen = {}
    for sub in SUBS:
        for t in TITLES:
            d = get('posts/search', subreddit=sub, title=t, limit=100)
            for o in d:
                seen[o['id']] = o
            sys.stderr.write(f'{sub}/{t!r} -> +{len(d)} total={len(seen)}\n')
            sys.stderr.flush()
    json.dump(list(seen.values()), open(f'{CACHE}/_posts.json', 'w'), ensure_ascii=False)
    print('total distinct posts:', len(seen))

elif sys.argv[1] == 'report':
    posts = json.load(open(f'{CACHE}/_posts.json', encoding='utf-8'))
    FIRM = re.compile(r'\b(SIG|Susquehanna|Jane\s*Street|Citadel|Optiver|IMC|HRT|Hudson\s*River|'
                      r'Jump\s*Trading|DRW|Five\s*Rings|Akuna|Two\s*Sigma|D\.?\s*E\.?\s*Shaw|'
                      r'DEShaw)\b', re.I)
    img_only = '--img' in sys.argv
    n = 0
    for o in sorted(posts, key=lambda x: -(x.get('created_utc') or 0)):
        blob = o['title'] + '\n' + (o.get('selftext') or '')
        if not FIRM.search(blob):
            continue
        u = o.get('url') or ''
        isimg = bool(re.search(r'(i\.redd\.it|imgur|preview\.redd\.it)', u))
        if img_only and not isimg:
            continue
        n += 1
        print('=' * 78)
        print(f"### {o['id']}  r/{o['subreddit']}  u/{o.get('author')}  score={o.get('score')} "
              f"cmts={o.get('num_comments')} removed={o.get('removed_by_category')} "
              f"utc={o.get('created_utc')}")
        print('TITLE:', o['title'])
        if isimg:
            print('IMAGE:', u)
        body = (o.get('selftext') or '').strip()
        if body:
            print('BODY:', body[:1200])
        print()
    print(f'# {n} firm-named posts of {len(posts)}', file=sys.stderr)
