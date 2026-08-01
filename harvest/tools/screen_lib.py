#!/usr/bin/env python3
"""Shared fetch/cache helpers for the Reddit provenance screen.

Reddit HTML and its own .json endpoints are Cloudflare-walled from this host, so
every lookup goes through the Arctic Shift mirror, which also retains bodies that
moderators removed on live reddit.
"""
import json
import os
import re
import subprocess
import time
import urllib.parse

API = 'https://arctic-shift.photon-reddit.com/api'
CACHE = '/workspace/harvest/.screen_cache'
os.makedirs(CACHE, exist_ok=True)


def _key(url):
    return os.path.join(CACHE, re.sub(r'[^A-Za-z0-9]+', '_', url)[:180] + '.json')


def get(path, **params):
    """GET an Arctic Shift endpoint, caching the parsed `data` list on disk."""
    url = '%s/%s?%s' % (API, path, urllib.parse.urlencode(params))
    p = _key(url)
    if os.path.exists(p):
        try:
            return json.load(open(p, encoding='utf-8')).get('data')
        except Exception:
            pass
    delay = 1.5
    for attempt in range(5):
        time.sleep(delay)
        r = subprocess.run(['curl', '-s', '--max-time', '90', url], capture_output=True)
        try:
            d = json.loads(r.stdout.decode('utf-8', errors='replace'))
        except Exception:
            delay = min(delay * 2, 45)
            continue
        if isinstance(d, dict) and d.get('error'):
            e = str(d['error']).lower()
            if 'slow down' in e or 'timeout' in e or 'too many' in e:
                delay = min(delay * 2, 45)
                continue
            json.dump({'data': None, 'error': d['error']}, open(p, 'w'))
            return None
        if isinstance(d, dict) and 'data' in d:
            json.dump(d, open(p, 'w'))
            return d['data']
        delay = min(delay * 2, 45)
    return None


POST_RE = re.compile(r'/comments/([a-z0-9]{4,10})(?:/[^/]*(?:/([a-z0-9]{5,10}))?)?', re.I)


def parse_url(u):
    """-> (post_id, comment_id|None). Handles /r/x/comments/<pid>/<slug>/<cid>/ forms."""
    u = u.split('?')[0].rstrip('/')
    m = POST_RE.search(u)
    if not m:
        return None, None
    pid, cid = m.group(1), m.group(2)
    if cid and cid.lower() in ('comment', 'comments'):
        cid = None
    return pid, cid
