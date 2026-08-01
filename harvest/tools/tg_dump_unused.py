#!/usr/bin/env python3
"""Dump readable text of fetched t.me message pages that no record cites yet."""
import html
import json
import os
import re

TG_BLOCKS = re.compile(
    r'<div class="(?:tgme_widget_message_text[^"]*|link_preview_title|link_preview_description)"'
    r'[^>]*>(.*?)</div>', re.S)
DATE = re.compile(r'<time[^>]*datetime="([^"]+)"')


def strip_html(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S)
    s = re.sub(r'<br\s*/?>', '\n', s)
    s = re.sub(r'<[^>]+>', '\n', s)
    s = html.unescape(s)
    s = re.sub(r'[ \t\u00a0]+', ' ', s)
    return re.sub(r'\n{2,}', '\n', s).strip()


used = set()
for line in open('raw/chat_and_archive.jsonl', encoding='utf-8'):
    m = re.match(r'https://t\.me/usinterview/(\d+)$', json.loads(line)['source_url'])
    if m:
        used.add(m.group(1))

for f in sorted(os.listdir('raw/pages/tgmsg'), key=lambda x: int(x[:-5])):
    mid = f[:-5]
    if mid in used:
        continue
    raw = open(f'raw/pages/tgmsg/{f}', encoding='utf-8', errors='replace').read()
    d = DATE.findall(raw)
    print('=' * 70)
    print(f'### t.me/usinterview/{mid}   date={d[0] if d else "?"}')
    for b in TG_BLOCKS.findall(raw):
        t = strip_html(b)
        if t:
            print(t)
    print()
