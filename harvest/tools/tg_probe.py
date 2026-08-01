#!/usr/bin/env python3
"""Probe candidate Telegram handles for a public, web-readable /s/ preview."""
import os
import re
import subprocess
import sys
import time

UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/120.0 Safari/537.36')
OUT = 'raw/pages/tg2'
os.makedirs(OUT, exist_ok=True)

for h in [l.strip() for l in open(sys.argv[1]) if l.strip() and not l.startswith('#')]:
    path = f'{OUT}/probe_{h}.html'
    p = subprocess.run(['curl', '-sL', '-m', '45', '-A', UA, '-o', path, '-w', '%{http_code}',
                        f'https://t.me/s/{h}'], capture_output=True, text=True)
    raw = open(path, encoding='utf-8', errors='replace').read() if os.path.exists(path) else ''
    msgs = len(re.findall(r'tgme_widget_message_wrap', raw))
    title = re.findall(r'<meta property="og:title" content="([^"]*)"', raw)
    desc = re.findall(r'<meta property="og:description" content="([^"]*)"', raw)
    kind = ('READABLE' if msgs else
            ('private/no-preview' if 'tgme_page' in raw or 'preview' in raw.lower() else 'unknown'))
    print(f'{h:28s} http={p.stdout.strip():3s} msgs={msgs:3d} {kind:18s} '
          f'title={title[0][:40] if title else "-"!r} desc={desc[0][:70] if desc else "-"!r}',
          flush=True)
    if not msgs:
        os.remove(path)
    time.sleep(1.5)
