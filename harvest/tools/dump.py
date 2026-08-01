#!/usr/bin/env python3
"""Dump full post + comment tree for given Reddit thread ids from the local archive cache."""
import json, sys, datetime

OUT = "/workspace/harvest/raw/_reddit_cache"
posts = {p["id"]: p for p in json.load(open(f"{OUT}/posts.json"))}
threads = json.load(open(f"{OUT}/thread_comments.json"))


def ts(x):
    return datetime.datetime.fromtimestamp(x or 0, datetime.UTC).strftime("%Y-%m-%d")


for pid in sys.argv[1:]:
    p = posts.get(pid, {})
    print("#" * 110)
    print(f"r/{p.get('subreddit')} | {ts(p.get('created_utc'))} | u/{p.get('author')} | "
          f"https://www.reddit.com/r/{p.get('subreddit')}/comments/{pid}/")
    print("TITLE:", p.get("title"))
    print("BODY:", (p.get("selftext") or "").strip()[:2000])
    for c in sorted(threads.get(pid, []), key=lambda x: x.get("created_utc") or 0):
        if c.get("author") in ("AutoModerator", "quant-ModTeam", "FinancialCareers-ModTeam"):
            continue
        b = (c.get("body") or "").strip()
        if not b:
            continue
        print(f"--- u/{c.get('author')} {ts(c.get('created_utc'))} [{c.get('id')}]")
        print(b[:2200])
