#!/usr/bin/env python3
"""Scan the cached Arctic Shift results for first-person question recalls.

Two-stage: rank every cached post/comment by how much it looks like someone
saying what they were actually asked, then print the winners with enough context
to judge. Nothing here writes records -- the records get written by hand from the
printed text, so the quote in the deliverable is the text I actually read.
"""
import glob
import json
import os
import re
import sys

CACHE = "/workspace/harvest/.reddit_cache"

FIRMS = {
    "Hudson River Trading": r"hudson\s*river|(?<![a-z])hrt(?![a-z])",
    "Jump Trading": r"jump\s*trading|(?<![a-z])jump(?![a-z])",
    "DRW": r"(?<![a-z])drw(?![a-z])",
    "Five Rings": r"five\s*rings|fiverings",
    "Akuna Capital": r"akuna",
    "Old Mission Capital": r"old\s*mission",
    "Two Sigma": r"two\s*sigma|twosigma",
    "D. E. Shaw": r"d\.?\s*e\.?\s*shaw|deshaw",
}
FIRMRE = {k: re.compile(v, re.I) for k, v in FIRMS.items()}

# phrases that mark a recall rather than speculation or career chat
RECALL = re.compile(
    r"\b(they asked|asked me|was asked|i got asked|i was asked|the question was|"
    r"first question|second question|one question|the questions were|"
    r"i had to|they gave me|gave us|the oa was|oa was|my oa|the test was|"
    r"the problem was|the prompt was|interview was|round was|they had me)\b", re.I)
QUESTIONY = re.compile(
    r"\b(probability|expected value|\bev\b|market mak|brainteaser|brain teaser|dice|coin|"
    r"cards?|deck|estimate|combinatoric|permutation|regression|markov|bayes|"
    r"binary search|dynamic programming|\bdp\b|linked list|order book|heap|"
    r"segment tree|leetcode|hackerrank|codesignal|mental math|sequence)\b", re.I)
NOISE = re.compile(r"^\s*(\[removed\]|\[deleted\]|)\s*$")


def load_all():
    seen = {}
    for p in glob.glob(os.path.join(CACHE, "*.json")):
        try:
            d = json.load(open(p, encoding="utf-8"))
        except Exception:
            continue
        for row in (d.get("data") or []):
            rid = row.get("id")
            if rid and rid not in seen:
                seen[rid] = row
    return list(seen.values())


def textof(row):
    return ((row.get("title") or "") + "\n" + (row.get("selftext") or row.get("body") or "")).strip()


def permalink(row):
    pl = row.get("permalink") or ""
    if pl:
        return "https://www.reddit.com" + pl
    lid = (row.get("link_id") or "").replace("t3_", "")
    return "https://www.reddit.com/comments/%s/_/%s" % (lid, row.get("id"))


def main():
    rows = load_all()
    print("%d unique cached reddit items" % len(rows), file=sys.stderr)
    scored = []
    for r in rows:
        t = textof(r)
        if len(t) < 60 or NOISE.match(t):
            continue
        firms = [f for f, rx in FIRMRE.items() if rx.search(t)]
        if not firms:
            continue
        s = 0
        s += 3 * len(RECALL.findall(t))
        s += 1 * len(set(QUESTIONY.findall(t.lower())))
        if s < 3:
            continue
        scored.append((s, firms, r, t))
    scored.sort(key=lambda x: -x[0])
    print("%d scored candidates" % len(scored), file=sys.stderr)
    lim = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    off = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    for s, firms, r, t in scored[off:off + lim]:
        print("\n" + "=" * 100)
        print("score=%d  %s  r/%s  %s" % (s, ",".join(firms), r.get("subreddit"), permalink(r)))
        print("author=%s  created=%s  kind=%s"
              % (r.get("author"), r.get("created_utc"), "post" if r.get("selftext") is not None else "comment"))
        print("-" * 100)
        print(t[:2600])


if __name__ == "__main__":
    main()
