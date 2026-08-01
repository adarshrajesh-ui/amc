#!/usr/bin/env python3
"""Extract post bodies from archived 1point3acres (Discuz, GBK) thread HTML.

Discuz post bodies live in <td class="t_f" id="postmessage_N">...</td>, but posts
frequently contain nested tables, so the closing tag must be found by tracking
<td>/</td> depth rather than by a non-greedy regex.
"""
import gzip
import html
import re
import sys

OPEN = re.compile(r'<td\b[^>]*class="t_f"[^>]*>')
TD = re.compile(r'<(/?)td\b', re.I)


def load(path: str) -> str:
    data = open(path, 'rb').read()
    if data[:2] == b'\x1f\x8b':
        data = gzip.decompress(data)
    for enc in ('gbk', 'gb18030', 'utf-8'):
        try:
            return data.decode(enc)
        except UnicodeDecodeError:
            continue
    return data.decode('gb18030', errors='replace')


def body_at(s: str, start: int) -> str:
    depth = 1
    i = start
    while depth and i < len(s):
        m = TD.search(s, i)
        if not m:
            break
        depth += -1 if m.group(1) else 1
        i = m.end()
    return s[start:m.start() if m else len(s)]


def clean(b: str) -> str:
    b = re.sub(r'<script.*?</script>', '', b, flags=re.S)
    b = re.sub(r'<style.*?</style>', '', b, flags=re.S)
    b = re.sub(r'<br\s*/?>', '\n', b)
    b = re.sub(r'</(p|div|tr|li|h\d|td|th|table)>', '\n', b)
    b = re.sub(r'<[^>]+>', '', b)
    b = html.unescape(b)
    b = re.sub(r'[ \t]+', ' ', b)
    return re.sub(r'\n{3,}', '\n\n', b).strip()


def bodies(path: str):
    s = load(path)
    out = []
    for m in OPEN.finditer(s):
        out.append(clean(body_at(s, m.end())))
    return s, out


if __name__ == '__main__':
    for path in sys.argv[1:]:
        s, bs = bodies(path)
        t = re.findall(r'<title>(.*?)</title>', s, re.S)
        print('#' * 25, path)
        print('TITLE:', html.unescape(t[0]).strip() if t else '?')
        d = re.findall(r'class="authi"[^>]*>.*?<em[^>]*>(.*?)</em>', s, re.S)
        print('DATES:', [re.sub(r'<[^>]+>', '', x).strip() for x in d][:8])
        for i, b in enumerate(bs):
            print(f'--- body {i} ---')
            print(b)
        print()
