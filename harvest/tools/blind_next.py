#!/usr/bin/env python3
"""Read a cached teamblind thread out of its Next.js payload rather than its JSON-LD.

blind_comments.py parses the schema.org DiscussionForumPosting block, but Blind only
mirrors part of the tree there — replies whose author is a "company page" user get
dropped, which silently lost real recalls. The __NEXT_DATA__ payload carries every
comment with content/contentRaw, writedAt and the poster's companyName, so parse that
instead. The payload is a JSON string nested inside JSON, hence the double unescaping.

Usage: blind_next.py <url-or-cache-file> [grep-regex]
"""
import json
import os
import re
import sys

CACHE = "/workspace/harvest/.verify_cache"


def slug(u):
    return re.sub(r"[^A-Za-z0-9]+", "_", u)[:150]


"""Only comment/post records carry contentRaw next to content; requiring it keeps the
scan off the page's <meta content="..."> tags."""
BODY = re.compile(r'"content":"((?:[^"\\]|\\.)*)","contentRaw":')
DATE = re.compile(r'"writedAt":"([^"]*)"')
FIRM = re.compile(r'"companyName":"([^"]*)"')


def entries(raw):
    """Every {content, writedAt, companyName} record in the page, in page order.

    Blind emits the fields in no fixed order, so pair each body with the nearest
    writedAt behind it and the nearest companyName ahead of it rather than trying to
    match one rigid record shape.
    """
    out, seen = [], set()
    # The payload is JSON serialised into a JS string, so its quotes arrive backslashed;
    # scan both the raw bytes and a once-unescaped copy.
    for text in (raw, raw.replace('\\"', '"')):
        for m in BODY.finditer(text):
            try:
                body = json.loads('"%s"' % m.group(1).replace("\n", "\\n"))
            except Exception:
                body = m.group(1)
            body = body.strip()
            if len(body) < 12 or body[:120] in seen:
                continue
            seen.add(body[:120])
            before, after = text[max(0, m.start() - 3000):m.start()], text[m.end():m.end() + 3000]
            d = DATE.findall(before)
            c = FIRM.findall(after)
            out.append({"content": body, "date": d[-1] if d else "?",
                        "company": c[0] if c else "?"})
    return out


def main():
    arg = sys.argv[1]
    pat = re.compile(sys.argv[2], re.I) if len(sys.argv) > 2 else None
    p = arg if os.path.exists(arg) else os.path.join(CACHE, slug(arg) + ".txt")
    raw = open(p, encoding="utf-8", errors="replace").read()
    rows = entries(raw)
    for r in rows:
        if pat and not pat.search(r["content"]):
            continue
        print("\n[%s] %s" % (r["date"], r["company"]))
        print("    " + r["content"][:2000].replace("\n", "\n    "))
    print("\n[%d distinct entries]" % len(rows), file=sys.stderr)


if __name__ == "__main__":
    main()
