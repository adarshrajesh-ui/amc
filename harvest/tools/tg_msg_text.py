#!/usr/bin/env python3
"""Print clean verbatim text blocks from single-message t.me embed pages."""
import glob
import html
import os
import re
import sys

BLOCKS = re.compile(
    r'<div class="(tgme_widget_message_text[^"]*|link_preview_title|link_preview_description)"[^>]*>(.*?)</div>',
    re.S,
)
TIME_RE = re.compile(r'<time[^>]*datetime="([^"]+)"')


def clean(s: str) -> str:
    s = re.sub(r'<br\s*/?>', '\n', s)
    s = re.sub(r'<[^>]+>', '', s)
    return html.unescape(s).strip()


for path in sorted(sys.argv[1:] or glob.glob('raw/pages/tgmsg/*.html')):
    raw = open(path, encoding='utf-8', errors='replace').read()
    mid = os.path.basename(path).replace('.html', '')
    t = TIME_RE.findall(raw)
    print(f'==== https://t.me/usinterview/{mid}   {t[-1] if t else "?"}')
    for kind, body in BLOCKS.findall(raw):
        print(f'  [{kind}] {clean(body)!r}')
    print()
