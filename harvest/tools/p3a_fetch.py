#!/usr/bin/env python3
"""Fetch archived 1point3acres threads from the Wayback Machine, slowly, with backoff."""
import os
import subprocess
import sys
import time

UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/120.0 Safari/537.36')
OUT = 'raw/pages/wayback'
os.makedirs(OUT, exist_ok=True)

ts_by_thread = {}
for line in open('raw/cdx/p3a_ok.txt'):
    name, ts = line.split()
    ts_by_thread.setdefault(name, []).append(ts)

wanted = [l.strip() for l in open(sys.argv[1]) if l.strip()]
for name in wanted:
    tid = name.split('-')[1]
    ts = sorted(ts_by_thread.get(name, []))[-1] if ts_by_thread.get(name) else None
    if not ts:
        print(f'{name}: no snapshot', flush=True)
        continue
    path = f'{OUT}/1p3a_{tid}__{ts}.html'
    if os.path.exists(path) and os.path.getsize(path) > 8000:
        print(f'{name}: cached', flush=True)
        continue
    url = f'https://web.archive.org/web/{ts}id_/https://www.1point3acres.com/bbs/{name}'
    for attempt in range(4):
        p = subprocess.run(['curl', '-sL', '-m', '180', '-A', UA, '-o', path, '-w', '%{http_code}',
                            url], capture_output=True, text=True)
        code, size = p.stdout.strip(), (os.path.getsize(path) if os.path.exists(path) else 0)
        if code == '200' and size > 8000:
            break
        time.sleep(30 * (attempt + 1))
    print(f'{name} ts={ts} -> {code} {size}B', flush=True)
    time.sleep(7)
