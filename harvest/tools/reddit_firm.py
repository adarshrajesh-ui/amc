#!/usr/bin/env python3
"""Per-firm sweep over every cached post AND comment, with a looser gate than the
first scan so the non-Akuna firms are not crowded out by ranking.

Usage: reddit_firm.py <FirmKey> [limit] [offset]
"""
import glob
import json
import os
import re
import sys

CDIR = "/workspace/harvest/.reddit_threads"
PCACHE = "/workspace/harvest/.reddit_cache"

FIRMS = {
    "HRT": r"hudson\s*river|(?<![a-z])hrt(?![a-z])",
    "Jump": r"jump\s*trading",
    "DRW": r"(?<![a-z])drw(?![a-z])",
    "FiveRings": r"five\s*rings|fiverings",
    "Akuna": r"akuna",
    "OldMission": r"old\s*mission",
    "TwoSigma": r"two\s*sigma|twosigma",
    "DEShaw": r"d\.?\s*e\.?\s*shaw|deshaw",
}

RECALL = re.compile(
    r"(they asked|asked me|was asked|i got asked|question was|questions were|"
    r"first question|second question|third question|i had to|they gave|gave us|"
    r"my oa|the oa|the test was|oa consisted|i remember|the problem was|"
    r"i was given|they had me|round was|interview was|it was a|consisted of)", re.I)
# vendor / self-promo tells: these are hard rejects
VENDOR = re.compile(r"interviews?\.chat|prepfully|interviewquery|tryexponent|jobtestprep|"
                    r"quantblueprint|tradermath|tradinginterview|everythingquant|"
                    r"theinterviewden|my team built|a tool (i|we) built|dm me for|"
                    r"check out my|our platform|QuantGrind", re.I)


def iter_items():
    posts = json.load(open(os.path.join(CDIR, "_posts.json"), encoding="utf-8"))
    for rid, pa in posts.items():
        yield ("post", rid, pa, pa.get("title") or "", pa.get("selftext") or "",
               pa.get("author"), pa.get("created_utc"), pa)
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
            yield ("comment", rid, pa, pa.get("title") or "", c.get("body") or "",
                   c.get("author"), c.get("created_utc"), pa)
    # also posts that were never comment-fetched
    for p in glob.glob(os.path.join(PCACHE, "*.json")):
        try:
            d = json.load(open(p, encoding="utf-8"))
        except Exception:
            continue
        for row in (d.get("data") or []):
            if row.get("selftext") is None:
                continue
            yield ("post", row.get("id"), row, row.get("title") or "",
                   row.get("selftext") or "", row.get("author"),
                   row.get("created_utc"), row)


def main():
    key = sys.argv[1]
    rx = re.compile(FIRMS[key], re.I)
    lim = int(sys.argv[2]) if len(sys.argv) > 2 else 15
    off = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    seen, out = set(), []
    for kind, rid, pa, title, body, author, ts, raw in iter_items():
        if len(body) < 60:
            continue
        h = hash(body[:400])
        if h in seen:
            continue
        seen.add(h)
        ctx = title + "\n" + body
        if not rx.search(ctx):
            continue
        if VENDOR.search(body):
            continue
        if not RECALL.search(body):
            continue
        score = 3 * len(RECALL.findall(body)) + (2 if rx.search(body) else 0)
        out.append((score, kind, rid, pa, title, body, author, ts))
    out.sort(key=lambda x: -x[0])
    print("%s: %d candidates" % (key, len(out)), file=sys.stderr)
    for score, kind, rid, pa, title, body, author, ts in out[off:off + lim]:
        print("\n" + "=" * 96)
        print("[%s] score=%d r/%s u/%s ts=%s" % (kind, score, pa.get("subreddit"), author, ts))
        print("POST: %s" % title[:105])
        print("LINK: https://www.reddit.com%s" % (pa.get("permalink") or ""))
        print("-" * 96)
        print(body[:1700])


if __name__ == "__main__":
    main()
