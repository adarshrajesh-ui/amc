#!/usr/bin/env python3
"""Extract post bodies from archived 1point3acres (Discuz, GBK) thread HTML."""
import html
import re
import sys


def load(path: str) -> str:
    data = open(path, 'rb').read()
    for enc in ('gbk', 'gb18030', 'utf-8'):
        try:
            return data.decode(enc)
        except UnicodeDecodeError:
            continue
    return data.decode('gb18030', errors='replace')


def clean(b: str) -> str:
    b = re.sub(r'<script.*?</script>', '', b, flags=re.S)
    b = re.sub(r'<br\s*/?>', '\n', b)
    b = re.sub(r'</(p|div|tr|li|h\d)>', '\n', b)
    b = re.sub(r'<[^>]+>', '', b)
    b = html.unescape(b)
    return re.sub(r'\n{3,}', '\n\n', b).strip()


for path in sys.argv[1:]:
    raw = load(path)
    print('#' * 25, path)
    t = re.findall(r'<title>(.*?)</title>', raw, re.S)
    print('TITLE:', t[0].strip() if t else '?')
    d = re.findall(r'class="authi"[^>]*>.*?<em[^>]*>(.*?)</em>', raw, re.S)
    print('DATES:', [re.sub(r'<[^>]+>', '', x).strip() for x in d][:6])
    for i, b in enumerate(re.findall(r'<td class="t_f"[^>]*>(.*?)</td>', raw, re.S)):
        print(f'--- body {i} ---')
        print(clean(b))
    print()
