#!/usr/bin/env python3
"""Fetch Wayback snapshots for a list of reddit thread slugs, slowly and with backoff."""
import os
import re
import subprocess
import sys
import time

UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/120.0 Safari/537.36')
OUT = 'raw/pages/wayback'
os.makedirs(OUT, exist_ok=True)


def cdx(url):
    """Return list of (timestamp, statuscode) snapshots for exactly this url."""
    api = (f'https://web.archive.org/cdx/search/cdx?url={url}'
           f'&fl=timestamp,statuscode&limit=200')
    for attempt in range(4):
        p = subprocess.run(['curl', '-s', '-m', '90', '-A', UA, api],
                           capture_output=True, text=True)
        if p.returncode == 0 and 'Too Many Requests' not in p.stdout:
            rows = [l.split() for l in p.stdout.strip().splitlines() if l.strip()]
            return [(r[0], r[1] if len(r) > 1 else '?') for r in rows]
        time.sleep(20 * (attempt + 1))
    return []


def snap(ts, url, path):
    if os.path.exists(path) and os.path.getsize(path) > 5000:
        return 'cached'
    wb = f'https://web.archive.org/web/{ts}id_/{url}'
    for attempt in range(4):
        p = subprocess.run(['curl', '-sL', '-m', '150', '-A', UA, '-o', path,
                            '-w', '%{http_code}', wb], capture_output=True, text=True)
        code = p.stdout.strip()
        if code == '200' and os.path.getsize(path) > 5000:
            return code
        time.sleep(25 * (attempt + 1))
    return code


for slug in [l.strip() for l in open(sys.argv[1]) if l.strip()]:
    key = re.sub(r'[^a-z0-9]+', '_', slug.split('/comments/')[1]).strip('_')[:60]
    snaps = cdx('https://' + slug)
    ok = [s for s in snaps if s[1] == '200']
    print(f'{slug}  snaps={len(snaps)} ok={len(ok)}', flush=True)
    time.sleep(6)
    if not ok:
        continue
    picks = {ok[0][0]}
    if len(ok) > 1:
        picks.add(ok[-1][0])
    for ts in sorted(picks):
        path = f'{OUT}/{key}__{ts}.html'
        r = snap(ts, 'https://' + slug, path)
        size = os.path.getsize(path) if os.path.exists(path) else 0
        print(f'    {ts} -> {r} ({size}B)', flush=True)
        time.sleep(8)
