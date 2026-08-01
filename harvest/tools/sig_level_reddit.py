#!/usr/bin/env python3
"""Pull full Reddit threads (post + comments) behind the SIG quant-trader `unknown`
records so the level can be read off the OP's own framing."""
import json
import os
import subprocess
import sys
import time

CACHE = '/workspace/harvest/.siglvl_cache'
os.makedirs(CACHE, exist_ok=True)
API = 'https://arctic-shift.photon-reddit.com/api'


def get(url, key):
    path = os.path.join(CACHE, key + '.json')
    if os.path.exists(path) and os.path.getsize(path) > 40:
        return json.load(open(path))
    for attempt in range(4):
        p = subprocess.run(['curl', '-s', '-m', '90', url], capture_output=True, text=True)
        try:
            data = json.loads(p.stdout)
        except Exception:
            time.sleep(15 * (attempt + 1))
            continue
        if isinstance(data, dict) and 'data' in data:
            json.dump(data, open(path, 'w'))
            return data
        time.sleep(15 * (attempt + 1))
    return {'data': []}


def main():
    ids = [l.strip() for l in open(sys.argv[1]) if l.strip()]
    for tid in ids:
        post = get(f'{API}/posts/ids?ids={tid}', f'post_{tid}')
        time.sleep(2)
        cmts = get(f'{API}/comments/search?link_id=t3_{tid}&limit=100', f'cmts_{tid}')
        time.sleep(2)
        d = post.get('data') or []
        print(f'=== {tid}  post={len(d)} comments={len(cmts.get("data") or [])}', flush=True)
        if d:
            p = d[0]
            print('  SUBREDDIT:', p.get('subreddit'))
            print('  TITLE:', (p.get('title') or '').replace('\n', ' '))
            print('  FLAIR:', p.get('link_flair_text'))
            print('  AUTHOR:', p.get('author'))
            body = (p.get('selftext') or '').replace('\n', ' ')
            print('  SELFTEXT:', body[:1500])


if __name__ == '__main__':
    main()
