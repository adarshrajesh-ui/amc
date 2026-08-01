#!/usr/bin/env python3
"""Print the readable text of a cached page, so quotes can be copied from the exact
bytes the verifier will see. Usage: pagetext.py <url-or-cache-file> [grep-regex]"""
import html
import os
import re
import sys

CACHE = "/workspace/harvest/.verify_cache"


def slug(u):
    return re.sub(r"[^A-Za-z0-9]+", "_", u)[:150]


def clean(raw):
    raw = re.sub(r"(?is)<(script|style|noscript|svg)[^>]*>.*?</\1>", " ", raw)
    raw = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</li>|</h[1-6]>|</tr>", "\n", raw)
    raw = re.sub(r"(?s)<[^>]+>", " ", raw)
    raw = html.unescape(raw)
    raw = re.sub(r"[ \t\u00a0]+", " ", raw)
    raw = re.sub(r"\n[ \t]+", "\n", raw)
    raw = re.sub(r"\n{3,}", "\n\n", raw)
    return raw.strip()


def load(arg):
    p = arg if os.path.exists(arg) else os.path.join(CACHE, slug(arg) + ".txt")
    if not os.path.exists(p):
        sys.exit("no cache for %s (looked at %s)" % (arg, p))
    raw = open(p, encoding="utf-8", errors="replace").read()
    return clean(raw) if "<" in raw[:2000] else raw


def main():
    txt = load(sys.argv[1])
    if len(sys.argv) > 2:
        pat = re.compile(sys.argv[2], re.I)
        lines = txt.split("\n")
        hit = {i for i, l in enumerate(lines) if pat.search(l)}
        show = sorted({j for i in hit for j in range(max(0, i - 3), min(len(lines), i + 6))})
        prev = -2
        for i in show:
            if i != prev + 1:
                print("---")
            print(lines[i])
            prev = i
    else:
        print(txt)


if __name__ == "__main__":
    main()
