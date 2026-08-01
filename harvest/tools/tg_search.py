#!/usr/bin/env python3
"""Search a public Telegram channel's web preview and report which hits are new."""
import html
import json
import os
import re
import subprocess
import sys
import time
import urllib.parse

UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/120.0 Safari/537.36')
CH = sys.argv[1]
OUT = f'raw/pages/tgsearch_{CH}'
os.makedirs(OUT, exist_ok=True)

have = {f[:-5] for f in os.listdir('raw/pages/tgmsg')} if os.path.isdir('raw/pages/tgmsg') else set()
seen = {}
for q in [l.strip() for l in open(sys.argv[2]) if l.strip()]:
    url = f'https://t.me/s/{CH}?q={urllib.parse.quote(q)}'
    path = os.path.join(OUT, re.sub(r'[^A-Za-z0-9]+', '_', q)[:40] + '.html')
    subprocess.run(['curl', '-sL', '-m', '45', '-A', UA, '-o', path, url], capture_output=True)
    raw = open(path, encoding='utf-8', errors='replace').read()
    ids = re.findall(rf'data-post="{CH}/(\d+)"', raw)
    new = [i for i in dict.fromkeys(ids) if i not in have]
    print(f'{q:34s} hits={len(set(ids)):3d} new={len(new):3d} {" ".join(new[:25])}', flush=True)
    for i in ids:
        seen[i] = q
    time.sleep(2)

json.dump(seen, open(f'{OUT}/_ids.json', 'w'), indent=0)
print('total distinct ids:', len(seen), ' new:', len(set(seen) - have))
