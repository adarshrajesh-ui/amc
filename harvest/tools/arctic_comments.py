#!/usr/bin/env python3
"""Search the Arctic Shift reddit mirror for COMMENTS that quote assessment questions.

r/quant funnels all OA/interview talk into weekly megathreads and automod-removes
standalone threads, so the recall that exists lives in comment bodies. Comment bodies
removed by moderators on live reddit are still readable in the mirror.
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

QUERIES = [
    ('quant', 'SIG OA'), ('quant', 'Optiver OA'), ('quant', 'Jane Street OA'),
    ('quant', 'Citadel OA'), ('quant', 'IMC OA'), ('quant', 'HRT OA'),
    ('quant', 'Jump OA'), ('quant', 'DRW OA'), ('quant', 'Akuna OA'),
    ('quant', 'Five Rings'), ('quant', 'Two Sigma OA'),
    ('quantfinance', 'SIG OA'), ('quantfinance', 'Optiver OA'),
    ('quantfinance', 'Jane Street OA'), ('quantfinance', 'Citadel OA'),
    ('quantfinance', 'IMC OA'), ('quantfinance', 'HRT OA'),
    ('quantfinance', 'DRW OA'), ('quantfinance', 'Akuna OA'),
    ('quantfinance', 'Five Rings'), ('quantfinance', 'Jump Trading OA'),
    ('quantfinance', 'Two Sigma OA'), ('quantfinance', 'Susquehanna'),
    ('quant', 'they asked me'), ('quantfinance', 'they asked me'),
    ('quantfinance', 'the question was'), ('quant', 'the question was'),
    ('quantfinance', 'one of the questions'), ('quant', 'one of the questions'),
    ('quantfinance', 'my superday'), ('quantfinance', 'interview question I got'),
]


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
    delay = 3.0
    for _ in range(4):
        time.sleep(delay)
        r = subprocess.run(['curl', '-s', '--max-time', '80', url], capture_output=True)
        try:
            d = json.loads(r.stdout.decode('utf-8', errors='replace'))
        except Exception:
            delay = min(delay * 2, 40)
            continue
        if d.get('error'):
            if 'slow down' in d['error'].lower() or 'timeout' in d['error'].lower():
                delay = min(delay * 2, 40)
                continue
            return []
        open(p, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False))
        return d.get('data') or []
    return []


def main():
    out = {}
    for i, (sub, q) in enumerate(QUERIES):
        for o in get('comments/search', subreddit=sub, body=q):
            out[o['id']] = o
        sys.stderr.write('\r%2d/%d %-14s %-24s n=%d' % (i + 1, len(QUERIES), sub, q, len(out)))
        sys.stderr.flush()
    sys.stderr.write('\n')
    dst = '/workspace/harvest/raw/_chat_arctic/comments.json'
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    json.dump(list(out.values()), open(dst, 'w', encoding='utf-8'), ensure_ascii=False)
    print('saved %d comments -> %s' % (len(out), dst))


if __name__ == '__main__':
    main()
