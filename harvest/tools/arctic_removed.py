#!/usr/bin/env python3
"""Find target-firm assessment recall posts that are gone from reddit.com but whose
bodies survive in the Arctic Shift mirror.

r/quant and r/quantfinance automod-remove nearly every OA/interview thread, so the
archive copy is frequently the only readable version left.
"""
import json
import os
import re
import subprocess
import sys
import time
import urllib.parse

API = 'https://arctic-shift.photon-reddit.com/api'
CACHE = '/workspace/harvest/.arctic_chat'
os.makedirs(CACHE, exist_ok=True)
PAUSE = 3.0

SUBS = ['quant', 'quantfinance', 'FinancialCareers', 'csMajors', 'leetcode',
        'cscareerquestions', 'internships', 'quantfinancecareers']
FIRMS = ['SIG', 'Susquehanna', 'Jane Street', 'Citadel', 'Optiver', 'IMC', 'HRT',
         'Hudson River', 'Jump Trading', 'DRW', 'Five Rings', 'Akuna', 'Two Sigma',
         'DE Shaw']


def get(path, **params):
    params.setdefault('limit', 100)
    url = '%s/%s?%s' % (API, path, urllib.parse.urlencode(params))
    key = re.sub(r'[^A-Za-z0-9]+', '_', url)[:170]
    p = os.path.join(CACHE, key + '.json')
    if os.path.exists(p):
        try:
            return json.load(open(p, encoding='utf-8')).get('data') or []
        except Exception:
            pass
    delay = PAUSE
    for _ in range(5):
        time.sleep(delay)
        r = subprocess.run(['curl', '-s', '--max-time', '80', url], capture_output=True)
        try:
            d = json.loads(r.stdout.decode('utf-8', errors='replace'))
        except Exception:
            delay = min(delay * 2, 45)
            continue
        err = d.get('error') or ''
        if err:
            if 'slow down' in err.lower() or 'timeout' in err.lower():
                delay = min(delay * 2, 45)
                continue
            return []
        open(p, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False))
        return d.get('data') or []
    return []


def main():
    found = {}
    plan = [(s, f) for s in SUBS for f in FIRMS]
    for i, (sub, firm) in enumerate(plan):
        for o in get('posts/search', subreddit=sub, title=firm):
            body = (o.get('selftext') or '').strip()
            if len(body) < 60 or body in ('[removed]', '[deleted]'):
                continue
            found[o['id']] = o
        sys.stderr.write('\r%3d/%d %-22s %-14s kept=%d' % (i + 1, len(plan), sub, firm, len(found)))
        sys.stderr.flush()
    sys.stderr.write('\n')
    dst = '/workspace/harvest/raw/_chat_arctic/arctic_posts.json'
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    json.dump(list(found.values()), open(dst, 'w', encoding='utf-8'), ensure_ascii=False)
    print('saved %d posts with intact bodies -> %s' % (len(found), dst))


if __name__ == '__main__':
    main()
