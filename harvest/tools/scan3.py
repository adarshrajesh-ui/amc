#!/usr/bin/env python3
"""Tightest sweep: inside SIG-titled threads only, surface any comment that states
numbers alongside probability/game language - i.e. plausibly an actual question."""
import json, re, sys, datetime

OUT = "/workspace/harvest/raw/_reddit_cache"
posts = {p["id"]: p for p in json.load(open(f"{OUT}/posts.json"))}
threads = json.load(open(f"{OUT}/thread_comments.json"))

SIGT = re.compile(r"\b(sig|susquehanna)\b", re.I)
NUM = re.compile(r"\d")
GAME = re.compile(
    r"(probability|expected|\bEV\b|dice|die\b|coin|card|deck|spinner|frog|marble|urn|"
    r"bayes|markov|sequence|combinator|permutation|paths?\b|grid|horses|poker|"
    r"market|bid|ask|quote|liar|truth|cookie|widget|painting|box|ball)", re.I)
NOISE = re.compile(r"^(AutoModerator|quant-ModTeam|FinancialCareers-ModTeam)$")

rows = []
for pid, cs in threads.items():
    p = posts.get(pid, {})
    t = p.get("title", "")
    if not SIGT.search(t):
        continue
    for c in cs:
        if NOISE.match(c.get("author") or ""):
            continue
        b = (c.get("body") or "").strip()
        if len(b) < 30 or b in ("[removed]", "[deleted]"):
            continue
        if not (NUM.search(b) and GAME.search(b)):
            continue
        rows.append((c.get("created_utc") or 0, p.get("subreddit"), pid, t,
                     c.get("author"), c.get("id"), b))

rows.sort(key=lambda x: -x[0])
sys.stderr.write(f"hits {len(rows)}\n")
for cu, sub, pid, title, a, cid, b in rows:
    d = datetime.datetime.fromtimestamp(cu, datetime.UTC).strftime("%Y-%m-%d")
    print("=" * 100)
    print(f"{d} | r/{sub} | u/{a} | https://www.reddit.com/r/{sub}/comments/{pid}/_/{cid}/")
    print(f"THREAD: {title}")
    print(b[:1800])
