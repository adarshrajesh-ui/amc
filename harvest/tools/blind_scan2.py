#!/usr/bin/env python3
"""Rescan every cached teamblind thread through the Next.js payload parser.

blind_scan.py reads the JSON-LD tree, which drops replies posted from company pages —
that is how the Old Mission SWE OA recall was missed. This pass uses blind_next.entries
so every comment is in scope, and reports the poster's own company alongside the text
because a reply from a peer firm is worth more than one from an onlooker.

Usage: blind_scan2.py <FirmKey|ALL> [limit] [offset]
"""
import glob
import os
import re
import sys

sys.path.insert(0, "/workspace/harvest/tools")
from blind_next import entries  # noqa: E402
from blind_scan import CONCRETE, FIRMS, RECALL, VENDOR  # noqa: E402

CACHE = "/workspace/harvest/.verify_cache"


def url_of(path):
    return ("https://www.teamblind.com/post/"
            + os.path.basename(path)[:-4].split("_post_")[1].replace("_", "-"))


def main():
    key = sys.argv[1]
    keys = list(FIRMS) if key == "ALL" else [key]
    lim = int(sys.argv[2]) if len(sys.argv) > 2 else 12
    off = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    hits, seen = [], set()
    for f in sorted(glob.glob(os.path.join(CACHE, "https_www_teamblind_com_post_*.txt"))):
        raw = open(f, encoding="utf-8", errors="replace").read()
        ents = entries(raw)
        if not ents:
            continue
        page = " ".join(e["content"] for e in ents)
        which = [k for k in keys if re.search(FIRMS[k], page, re.I)]
        if not which:
            continue
        for e in ents:
            txt = e["content"]
            if len(txt) < 45 or VENDOR.search(txt) or txt[:100] in seen:
                continue
            seen.add(txt[:100])
            score = 2 * len(RECALL.findall(txt)) + len(set(CONCRETE.findall(txt.lower())))
            if score < 3:
                continue
            hits.append((score, "/".join(which), url_of(f), e["date"], e["company"], txt))
    hits.sort(key=lambda h: -h[0])
    for score, which, url, date, company, txt in hits[off:off + lim]:
        print("\n=== %d  %s  [%s] poster@%s\n%s\n%s" % (score, which, date, company, url, txt[:1400]))
    print("\n[%d candidates]" % len(hits), file=sys.stderr)


if __name__ == "__main__":
    main()
