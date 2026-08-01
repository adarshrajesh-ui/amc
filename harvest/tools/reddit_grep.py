#!/usr/bin/env python3
"""Sentence-level grep over every cached reddit post and comment.

Prints only the matching sentence plus one neighbour, with the permalink, so a
lot of ground can be covered without dumping whole threads. Usage:

    reddit_grep.py <firm-regex> <content-regex> [limit]
"""
import glob
import json
import os
import re
import sys

CDIR = "/workspace/harvest/.reddit_threads"
PCACHE = "/workspace/harvest/.reddit_cache"
VENDOR = re.compile(r"interviews?\.chat|prepfully|interviewquery|tryexponent|jobtestprep|"
                    r"quantblueprint|tradermath|tradinginterview|everythingquant|"
                    r"theinterviewden|my team built|a tool (i|we) built|QuantGrind", re.I)


def items():
    posts = json.load(open(os.path.join(CDIR, "_posts.json"), encoding="utf-8"))
    for rid, pa in posts.items():
        yield (pa.get("title") or "") + "\n" + (pa.get("selftext") or ""), pa, pa.get("author"), pa.get("created_utc"), "post"
    for p in glob.glob(os.path.join(CDIR, "*.json")):
        rid = os.path.basename(p)[:-5]
        if rid == "_posts":
            continue
        pa = posts.get(rid, {})
        try:
            rows = json.load(open(p, encoding="utf-8")).get("data") or []
        except Exception:
            continue
        for c in rows:
            yield (c.get("body") or ""), pa, c.get("author"), c.get("created_utc"), "comment"
    for p in glob.glob(os.path.join(PCACHE, "*.json")):
        try:
            d = json.load(open(p, encoding="utf-8"))
        except Exception:
            continue
        for row in (d.get("data") or []):
            txt = (row.get("title") or "") + "\n" + (row.get("selftext") or row.get("body") or "")
            yield txt, row, row.get("author"), row.get("created_utc"), "raw"


def main():
    firm = re.compile(sys.argv[1], re.I)
    cont = re.compile(sys.argv[2], re.I)
    lim = int(sys.argv[3]) if len(sys.argv) > 3 else 30
    seen, n = set(), 0
    for text, pa, author, ts, kind in items():
        if not text or VENDOR.search(text):
            continue
        if not firm.search(text) or not cont.search(text):
            continue
        sents = re.split(r"(?<=[.!?\n])\s+", text)
        for i, s in enumerate(sents):
            if not cont.search(s):
                continue
            window = " ".join(sents[max(0, i - 2):i + 2])
            if not firm.search(window):
                continue
            k = hash(s[:180])
            if k in seen:
                continue
            seen.add(k)
            n += 1
            print("\n--- u/%s ts=%s [%s] https://www.reddit.com%s"
                  % (author, ts, kind, pa.get("permalink") or ""))
            print("    " + window[:900].replace("\n", " "))
            if n >= lim:
                return


if __name__ == "__main__":
    main()
