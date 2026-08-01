#!/usr/bin/env python3
"""Pull the comment tree out of a cached teamblind page.

Blind renders only the opening post into HTML; the replies ship inside the
page's schema.org JSON-LD DiscussionForumPosting block, which carries `text`,
`datePublished` and `author.identifier` per comment and nests replies under
`comment`. A tag-stripping reader therefore shows none of them, which is why an
earlier pass could only quote opening posts.

Usage: blind_comments.py <url-or-cache-file> [grep-regex]
"""
import json
import os
import re
import sys

CACHE = "/workspace/harvest/.verify_cache"


def slug(u):
    return re.sub(r"[^A-Za-z0-9]+", "_", u)[:150]


def blocks(raw):
    """Yield every parsed application/ld+json object on the page."""
    for m in re.finditer(r'<script[^>]+application/ld\+json[^>]*>(.*?)</script>', raw, re.S):
        try:
            yield json.loads(m.group(1))
        except Exception:
            continue


def walk(node, depth, out):
    if isinstance(node, list):
        for x in node:
            walk(x, depth, out)
        return
    if not isinstance(node, dict):
        return
    txt = node.get("text") or node.get("articleBody")
    if txt:
        au = (node.get("author") or {})
        out.append((depth, au.get("identifier") or au.get("name") or "?",
                    (node.get("datePublished") or "")[:10], txt.strip()))
    for x in (node.get("comment") or []):
        walk(x, depth + 1, out)


def main():
    arg = sys.argv[1]
    pat = re.compile(sys.argv[2], re.I) if len(sys.argv) > 2 else None
    p = arg if os.path.exists(arg) else os.path.join(CACHE, slug(arg) + ".txt")
    raw = open(p, encoding="utf-8", errors="replace").read()
    out = []
    for b in blocks(raw):
        walk(b, 0, out)
    seen, n = set(), 0
    for depth, who, date, txt in out:
        k = txt[:120]
        if k in seen:
            continue
        seen.add(k)
        n += 1
        if pat and not pat.search(txt):
            continue
        print("\n%s[%s] %s  %s" % ("  " * depth, date, who, "(OP)" if depth == 0 else ""))
        print("%s    %s" % ("  " * depth, txt[:1500].replace("\n", "\n" + "  " * depth + "    ")))
    print("\n[%d distinct entries]" % n, file=sys.stderr)


if __name__ == "__main__":
    main()
