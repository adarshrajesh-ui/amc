#!/usr/bin/env python3
"""Pull comments from r/quant and r/quantfinance recruiting megathreads.

Standalone OA posts are automod-removed on r/quant, so recall is funnelled into weekly
megathreads. comments/search?link_id= returns a whole thread at once and does not time out
the way the free-text comment search does.
"""
import json
import os
import re
import subprocess
import sys
import time
import urllib.parse

API = 'https://arctic-shift.photon-reddit.com/api'
CACHE = '.arctic_mega'
os.makedirs(CACHE, exist_ok=True)


def get(path, **params):
    url = '%s/%s?%s' % (API, path, urllib.parse.urlencode(params))
    key = re.sub(r'[^A-Za-z0-9]+', '_', url)[:170] + '.json'
    p = os.path.join(CACHE, key)
    if os.path.exists(p):
        try:
            return json.load(open(p, encoding='utf-8')).get('data') or []
        except Exception:
            pass
    delay = 2.0
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


if sys.argv[1] == 'find':
    seen = {}
    for sub in ('quant', 'quantfinance', 'quantfinancecareers'):
        for q in ('megathread', 'weekly', 'recruiting', 'interview'):
            for o in get('posts/search', subreddit=sub, title=q, limit=100):
                if o.get('num_comments', 0) >= 15:
                    seen[o['id']] = o
            sys.stderr.write(f'{sub}/{q} -> {len(seen)}\n')
    out = sorted(seen.values(), key=lambda x: -(x.get('num_comments') or 0))
    json.dump([{k: o.get(k) for k in ('id', 'subreddit', 'title', 'num_comments', 'created_utc',
                                      'permalink')} for o in out],
              open(f'{CACHE}/_threads.json', 'w'), ensure_ascii=False, indent=1)
    for o in out[:40]:
        print(f"{o['id']}  c={o.get('num_comments'):5d}  r/{o['subreddit']:<20} {o['title'][:75]}")
    print('total threads:', len(out))

elif sys.argv[1] == 'pull':
    th = json.load(open(f'{CACHE}/_threads.json', encoding='utf-8'))
    th = [t for t in th if (t.get('num_comments') or 0) >= 25]
    allc = {}
    for i, t in enumerate(th):
        cs = get('comments/search', link_id='t3_' + t['id'], limit=100)
        for c in cs:
            allc[c['id']] = c
        sys.stderr.write(f"\r{i+1}/{len(th)} {t['id']} +{len(cs):3d} total={len(allc)}")
        sys.stderr.flush()
    sys.stderr.write('\n')
    json.dump(list(allc.values()), open(f'{CACHE}/_comments.json', 'w'), ensure_ascii=False)
    print('comments pulled:', len(allc))
