#!/usr/bin/env python3
"""Extract post body + comments from archived reddit HTML (old and new layouts)."""
import gzip
import html
import re
import sys


def load(path: str) -> str:
    d = open(path, 'rb').read()
    if d[:2] == b'\x1f\x8b':
        d = gzip.decompress(d)
    return d.decode('utf-8', errors='replace')


def clean(b: str) -> str:
    b = re.sub(r'<script.*?</script>', ' ', b, flags=re.S)
    b = re.sub(r'<style.*?</style>', ' ', b, flags=re.S)
    b = re.sub(r'<br\s*/?>', '\n', b)
    b = re.sub(r'</(p|div|li|h\d|blockquote)>', '\n', b)
    b = re.sub(r'<[^>]+>', '', b)
    b = html.unescape(b)
    b = re.sub(r'[ \t]+', ' ', b)
    return re.sub(r'\n{3,}', '\n\n', b).strip()


def blocks(s: str):
    out = []
    # old.reddit / www.reddit desktop classic
    for m in re.finditer(r'<div class="md">(.*?)</div>\s*</div>', s, re.S):
        out.append(clean(m.group(1)))
    # new reddit shreddit / rtjson
    for m in re.finditer(r'<div[^>]+id="t[13]_[a-z0-9]+-post-rtjson-content"[^>]*>(.*?)</div>\s*</div>',
                         s, re.S):
        out.append(clean(m.group(1)))
    for m in re.finditer(r'<div[^>]*slot="(?:text-body|comment)"[^>]*>(.*?)</div>\s*</div>', s, re.S):
        out.append(clean(m.group(1)))
    seen, uniq = set(), []
    for b in out:
        if b and b not in seen:
            seen.add(b)
            uniq.append(b)
    return uniq


if __name__ == '__main__':
    for p in sys.argv[1:]:
        s = load(p)
        t = re.findall(r'<title>(.*?)</title>', s, re.S)
        print('#' * 30, p)
        print('TITLE:', html.unescape(re.sub(r'<[^>]+>', '', t[0])).strip() if t else '?',
              ' bytes=', len(s))
        bs = blocks(s)
        print(f'BLOCKS={len(bs)}')
        for i, b in enumerate(bs):
            print(f'--- {i} ---')
            print(b[:2500])
        print()
