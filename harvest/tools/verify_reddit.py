#!/usr/bin/env python3
"""Verify reddit source_quotes against the Arctic Shift bytes actually fetched.

verify_quotes.py can only mark reddit records UNCHECKABLE, since reddit.com
refuses this host. This is the substitute gate: it asserts each quote appears
verbatim in the archived post/comment corpus under .reddit_threads and
.reddit_cache, which is the text those records were read from.
"""
import glob
import json
import os
import re
import sys

CDIR = "/workspace/harvest/.reddit_threads"
PCACHE = "/workspace/harvest/.reddit_cache"


def corpus():
    out = []
    posts = json.load(open(os.path.join(CDIR, "_posts.json"), encoding="utf-8"))
    for pa in posts.values():
        out.append((pa.get("title") or "") + " " + (pa.get("selftext") or ""))
    for p in glob.glob(os.path.join(CDIR, "*.json")):
        if p.endswith("_posts.json"):
            continue
        try:
            rows = json.load(open(p, encoding="utf-8")).get("data") or []
        except Exception:
            continue
        out.extend(c.get("body") or "" for c in rows)
    for p in glob.glob(os.path.join(PCACHE, "*.json")):
        try:
            d = json.load(open(p, encoding="utf-8"))
        except Exception:
            continue
        for r in (d.get("data") or []):
            out.append((r.get("title") or "") + " " + (r.get("selftext") or r.get("body") or ""))
    return out


def norm(s):
    return re.sub(r"\s+", " ", s).strip().lower()


def main(paths):
    big = " || ".join(norm(b) for b in corpus())
    ok = bad = 0
    for path in paths:
        for line in open(path, encoding="utf-8"):
            line = line.strip()
            if not line:
                continue
            o = json.loads(line)
            if "reddit.com" not in o["source_url"]:
                continue
            if norm(o["source_quote"]) in big:
                ok += 1
            else:
                bad += 1
                print("MISSING %s | %s" % (o["firm"], o["source_quote"][:110]))
    print("archive-verified %d, missing %d" % (ok, bad))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
