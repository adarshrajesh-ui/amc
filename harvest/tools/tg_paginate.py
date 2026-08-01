#!/usr/bin/env python3
"""Walk a public Telegram channel's ?q= search backwards with before= pagination.

t.me/s/<ch>?q=<term> only shows one page; adding &before=<msgid> pages further back. Looping
that until no new ids appear gives the full firm-hashtag history of the channel instead of the
most recent page only.
"""
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
OUT = f'raw/pages/tgpage_{CH}'
os.makedirs(OUT, exist_ok=True)

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


def fetch(term, before=None):
    # Telegram only honours before= when it precedes q= in the query string.
    q = urllib.parse.urlencode({'q': term} if before is None else {'before': before, 'q': term})
    url = f'https://t.me/s/{CH}?{q}'
    key = re.sub(r'[^A-Za-z0-9]+', '_', f'{term}_{before}')[:80] + '.html'
    p = os.path.join(OUT, key)
    if not os.path.exists(p):
        subprocess.run(['curl', '-sL', '-m', '45', '-A', UA, '-o', p, url], capture_output=True)
        time.sleep(1.5)
    return open(p, encoding='utf-8', errors='replace').read(), url


store = {}
sfile = f'{OUT}/_texts.json'
if os.path.exists(sfile):
    store = json.load(open(sfile, encoding='utf-8'))

terms = [l.strip() for l in open(sys.argv[2]) if l.strip()]
MAXPAGES = int(sys.argv[3]) if len(sys.argv) > 3 else 12

for term in terms:
    before = None
    for page in range(MAXPAGES):
        raw, url = fetch(term, before)
        ids = []
        for w in WRAP.findall(raw):
            m = POST.search(w)
            if not m:
                continue
            mid = m.group(1)
            ids.append(int(mid))
            if mid not in store:
                d = DATE.findall(w)
                txt = '\n'.join(x for x in (strip(b) for b in BLK.findall(w)) if x)
                store[mid] = {'date': d[0][:10] if d else '?', 'text': txt, 'q': term}
        if not ids:
            break
        lo = min(ids)
        if before is not None and lo >= before:
            break
        before = lo
    sys.stderr.write(f'{term:26s} store={len(store)}\n')
    sys.stderr.flush()
    json.dump(store, open(sfile, 'w'), ensure_ascii=False, indent=0)

print('total distinct messages held:', len(store))
