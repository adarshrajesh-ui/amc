#!/usr/bin/env python3
"""Scan saved t.me search-result pages: pull each message's own text plus its link-preview
title/description, and surface the ones that name a target firm."""
import html
import json
import os
import re
import sys

DIR = sys.argv[1]
FIRMS = re.compile(
    r'\b(SIG|Susquehanna|Jane\s*Street|Citadel|Optiver|IMC|HRT|Hudson\s*River|Jump|DRW|'
    r'Five\s*Rings|Akuna|Two\s*Sigma|D\.?\s*E\.?\s*Shaw|DEShaw)\b', re.I)
WRAP = re.compile(r'<div class="tgme_widget_message_wrap.*?(?=<div class="tgme_widget_message_wrap|$)',
                  re.S)
POST = re.compile(r'data-post="[^/]+/(\d+)"')
DATE = re.compile(r'datetime="([^"]+)"')
BLK = re.compile(
    r'<div class="(?:tgme_widget_message_text[^"]*|link_preview_title|link_preview_description)"'
    r'[^>]*>(.*?)</div>', re.S)


def strip(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S)
    s = re.sub(r'<br\s*/?>', '\n', s)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = html.unescape(s)
    return re.sub(r'\n{2,}', '\n', re.sub(r'[ \t\u00a0]+', ' ', s)).strip()


seen = {}
for f in sorted(os.listdir(DIR)):
    if not f.endswith('.html'):
        continue
    raw = open(os.path.join(DIR, f), encoding='utf-8', errors='replace').read()
    for w in WRAP.findall(raw):
        pid = POST.search(w)
        if not pid:
            continue
        d = DATE.findall(w)
        txt = '\n'.join(x for x in (strip(b) for b in BLK.findall(w)) if x)
        if pid.group(1) not in seen and txt:
            seen[pid.group(1)] = (d[0][:10] if d else '?', txt)

hits = {k: v for k, v in seen.items() if FIRMS.search(v[1])}
print(f'# messages scanned: {len(seen)}   firm hits: {len(hits)}', file=sys.stderr)
json.dump({k: v[1] for k, v in seen.items()}, open(f'{DIR}/_texts.json', 'w'),
          ensure_ascii=False, indent=0)
for k in sorted(hits, key=int):
    d, t = hits[k]
    print('=' * 72)
    print(f'### t.me/usinterview/{k}  {d}')
    print(t)
    print()
