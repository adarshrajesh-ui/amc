#!/usr/bin/env python3
"""Pull each cited commenter's own Reddit history and surface anything that states the
level of the SIG application they were describing."""
import json
import os
import re
import subprocess
import sys
import time

CACHE = '/workspace/harvest/.siglvl_cache/authors'
os.makedirs(CACHE, exist_ok=True)
API = 'https://arctic-shift.photon-reddit.com/api'
LEVEL = re.compile(
    r'(intern(ship)?s?\b|summer\s*20\d\d|penultimate|placement|sophomore|'
    r'senior year|senior in|final year|undergrad|graduat|new.?grad|full.?time|'
    r'\bFT\b|\bNG\b|campus|PhD|master|class of|return offer)', re.I)
SIG = re.compile(r'(sig\b|susquehanna)', re.I)


def get(url, key):
    path = os.path.join(CACHE, key + '.json')
    if os.path.exists(path) and os.path.getsize(path) > 40:
        try:
            return json.load(open(path))
        except Exception:
            pass
    for attempt in range(3):
        p = subprocess.run(['curl', '-s', '-m', '90', url], capture_output=True, text=True)
        try:
            data = json.loads(p.stdout)
        except Exception:
            time.sleep(10 * (attempt + 1))
            continue
        if isinstance(data, dict) and 'data' in data:
            json.dump(data, open(path, 'w'))
            return data
        time.sleep(10 * (attempt + 1))
    return {'data': []}


for author in [l.strip() for l in open(sys.argv[1]) if l.strip()]:
    cm = get(f'{API}/comments/search?author={author}&limit=100', f'c_{author}')
    time.sleep(1.5)
    ps = get(f'{API}/posts/search?author={author}&limit=100', f'p_{author}')
    time.sleep(1.5)
    items = [('C', c.get('created_utc'), c.get('subreddit'), c.get('body') or '')
             for c in (cm.get('data') or [])]
    items += [('P', p.get('created_utc'), p.get('subreddit'),
               (p.get('title') or '') + ' || ' + (p.get('selftext') or ''))
              for p in (ps.get('data') or [])]
    hits = [(k, t, s, b) for k, t, s, b in items if LEVEL.search(b) and SIG.search(b)]
    print(f'=== u/{author}  items={len(items)}  sig+level hits={len(hits)}', flush=True)
    for k, t, s, b in sorted(hits, key=lambda x: x[1] or 0):
        ts = time.strftime('%Y-%m-%d', time.gmtime(t)) if t else '?'
        print(f'   [{k} {ts} r/{s}] {b[:600]}'.replace('\n', ' '))
