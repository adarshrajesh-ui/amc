#!/usr/bin/env python3
"""Pull every comment of named reddit threads from the Arctic Shift mirror.

The recall posts themselves usually only ask "what should I expect"; the answers — which is
where actual question text appears — are in the replies. comments/search?link_id= returns a
whole thread in one call and is far more reliable than the mirror's free-text comment search.
"""
import json
import os
import re
import subprocess
import sys
import time
import urllib.parse

API = 'https://arctic-shift.photon-reddit.com/api'
CACHE = '.arctic_thr'
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
    for _ in range(4):
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


ids = [x.strip() for x in open(sys.argv[1]) if x.strip() and not x.startswith('#')]
allc = {}
for i, pid in enumerate(ids):
    cs = get('comments/search', link_id='t3_' + pid, limit=100)
    for c in cs:
        allc[c['id']] = c
    sys.stderr.write(f'\r{i+1}/{len(ids)} {pid} +{len(cs):3d} total={len(allc)}   ')
    sys.stderr.flush()
sys.stderr.write('\n')
json.dump(list(allc.values()), open(f'{CACHE}/_cmts.json', 'w'), ensure_ascii=False)
print('comments pulled:', len(allc))
