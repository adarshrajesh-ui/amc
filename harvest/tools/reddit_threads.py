#!/usr/bin/env python3
"""Dump whole threads whose TITLE names a shard firm.

Ranking individual comments kept surfacing "which of these 27 firms is easiest"
list posts, because they mention every firm at once. Titles are a much better
filter: a thread called "five rings qt intern first round" is about exactly one
firm, and its replies are the recalls worth reading.

Usage: reddit_threads.py <FirmKey> [max_threads] [offset]
"""
import glob
import json
import os
import re
import sys

CDIR = "/workspace/harvest/.reddit_threads"

FIRMS = {
    "HRT": r"hudson\s*river|(?<![a-z])hrt(?![a-z])",
    "Jump": r"jump\s*trading|(?<![a-z])jump(?![a-z])",
    "DRW": r"(?<![a-z])drw(?![a-z])",
    "FiveRings": r"five\s*rings|fiverings|five-rings",
    "Akuna": r"akuna",
    "OldMission": r"old\s*mission|(?<![a-z])omc(?![a-z])",
    "TwoSigma": r"two\s*sigma|twosigma|(?<![a-z])2\s*sigma(?![a-z])",
    "DEShaw": r"d\.?\s*e\.?\s*shaw|deshaw",
}
INTERVIEWY = re.compile(
    r"\b(oa|interview|assessment|screen|round|superday|onsite|on-site|codepair|"
    r"hackerrank|codesignal|test|intern|internship|offer|process|final|phone)\b", re.I)
VENDOR = re.compile(r"interviews?\.chat|prepfully|interviewquery|tryexponent|jobtestprep|"
                    r"quantblueprint|tradermath|tradinginterview|everythingquant|"
                    r"theinterviewden|my team built|a tool (i|we) built|QuantGrind", re.I)


def main():
    key = sys.argv[1]
    rx = re.compile(FIRMS[key], re.I)
    maxn = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    off = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    posts = json.load(open(os.path.join(CDIR, "_posts.json"), encoding="utf-8"))

    hits = []
    for rid, pa in posts.items():
        title = pa.get("title") or ""
        if not rx.search(title) or not INTERVIEWY.search(title):
            continue
        cf = os.path.join(CDIR, rid + ".json")
        rows = []
        if os.path.exists(cf):
            try:
                rows = json.load(open(cf, encoding="utf-8")).get("data") or []
            except Exception:
                rows = []
        body = pa.get("selftext") or ""
        useful = [c for c in rows
                  if len(c.get("body") or "") > 45
                  and not (c.get("body") or "").startswith("[")
                  and not VENDOR.search(c.get("body") or "")]
        hits.append((len(useful) + (2 if len(body) > 200 else 0), rid, pa, body, useful))
    hits.sort(key=lambda x: -x[0])
    print("%s: %d titled threads" % (key, len(hits)), file=sys.stderr)
    for _, rid, pa, body, useful in hits[off:off + maxn]:
        print("\n" + "#" * 96)
        print("THREAD r/%s  %s" % (pa.get("subreddit"), pa.get("title")))
        print("LINK   https://www.reddit.com%s" % (pa.get("permalink") or ""))
        print("OP     u/%s  ts=%s" % (pa.get("author"), pa.get("created_utc")))
        if body.strip():
            print("-" * 96)
            print(body[:1300])
        for c in useful[:14]:
            print("-" * 96)
            print("  u/%s ts=%s score=%s" % (c.get("author"), c.get("created_utc"), c.get("score")))
            print("  " + (c.get("body") or "")[:1200].replace("\n", "\n  "))


if __name__ == "__main__":
    main()
