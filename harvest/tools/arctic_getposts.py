#!/usr/bin/env python3
"""Fetch specific reddit posts by id from the Arctic Shift mirror."""
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
    p = os.path.join(CACHE, re.sub(r'[^A-Za-z0-9]+', '_', url)[:170] + '.json')
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


ids = sys.argv[1:]
out = get('posts/ids', ids=','.join(ids))
json.dump(out, open(f'{CACHE}/_qposts.json', 'w'), ensure_ascii=False)
for o in out:
    print('=' * 78)
    print(f"### {o['id']}  r/{o['subreddit']}  u/{o.get('author')}  "
          f"score={o.get('score')}  removed={o.get('removed_by_category')}")
    print('URL: https://www.reddit.com' + o['permalink'])
    print('TITLE:', o['title'])
    print('URLFIELD:', o.get('url'))
    print('BODY:', (o.get('selftext') or '')[:1500])
    print()
