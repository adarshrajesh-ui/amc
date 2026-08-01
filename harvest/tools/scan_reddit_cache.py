#!/usr/bin/env python3
"""Scan cached Reddit archive dumps for Tier-A firm interview content."""
import json
import os
import re
import sys

FILES = [
    "/workspace/harvest/raw/_reddit_cache/mega_posts.json",
    "/workspace/harvest/raw/_reddit_cache/mega_comments.json",
    "/workspace/harvest/raw/_reddit_cache/comments_bodysearch.json",
    "/workspace/harvest/raw/_tiera_reddit/posts.json",
    "/workspace/harvest/raw/_tiera_reddit/comments.json",
]

FIRMS = {
    "Hudson River Trading": r"\bHRT\b|Hudson River",
    "Jump Trading": r"Jump Trading|\bJump\b",
    "DRW": r"\bDRW\b",
    "Five Rings": r"Five Rings|FiveRings",
    "Akuna Capital": r"Akuna",
    "Old Mission Capital": r"Old Mission",
    "Two Sigma": r"Two Sigma|TwoSigma",
    "D. E. Shaw": r"D\.?\s?E\.?\s?Shaw|DE Shaw|DEShaw",
}

# Signals that the text recounts an actual question rather than chatter.
QSIG = re.compile(
    r"asked me|they asked|question was|first question|the questions were|OA (?:had|was|consisted)|"
    r"interview was|round was|got asked|expected value|probability that|what'?s the probability|"
    r"how many|estimate the|market mak|brainteaser|brain teaser|dice|coin flip|deck of cards",
    re.I)


def load(p):
    if not os.path.exists(p):
        return []
    try:
        d = json.load(open(p, encoding="utf-8"))
    except Exception:
        return []
    if isinstance(d, dict):
        d = d.get("data", [])
    return d if isinstance(d, list) else []


def text_of(o):
    return " ".join(str(o.get(k) or "") for k in ("title", "selftext", "body"))


def perma(o):
    p = o.get("permalink")
    if p:
        return "https://www.reddit.com" + p
    if o.get("link_id") and o.get("id"):
        return "https://www.reddit.com/comments/%s/_/%s" % (o["link_id"].split("_")[-1], o["id"])
    return "https://www.reddit.com/" + str(o.get("id", ""))


def main():
    want = sys.argv[1] if len(sys.argv) > 1 else None
    seen = set()
    hits = []
    for f in FILES:
        for o in load(f):
            t = text_of(o)
            if len(t) < 60:
                continue
            oid = o.get("id")
            if oid in seen:
                continue
            seen.add(oid)
            for firm, pat in FIRMS.items():
                if want and firm != want:
                    continue
                if re.search(pat, t) and QSIG.search(t):
                    hits.append((firm, o.get("subreddit"), o.get("created_utc"), perma(o), t))
                    break
    hits.sort(key=lambda x: -(x[2] or 0))
    print("TOTAL HITS", len(hits))
    from collections import Counter
    print(Counter(h[0] for h in hits))
    for firm, sub, ts, url, t in hits:
        import datetime
        d = datetime.datetime.utcfromtimestamp(ts).strftime("%Y-%m-%d") if ts else "?"
        print("\n" + "=" * 100)
        print("%s | r/%s | %s | %s" % (firm, sub, d, url))
        print(t[:2600])


if __name__ == "__main__":
    main()
