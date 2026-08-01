#!/usr/bin/env python3
"""Looser sweep: any cached Reddit comment/post that reads like it is describing an
actual SIG assessment/interview question, rather than generic advice."""
import json, re, sys, datetime

OUT = "/workspace/harvest/raw/_reddit_cache"
posts = {p["id"]: p for p in json.load(open(f"{OUT}/posts.json"))}
threads = json.load(open(f"{OUT}/thread_comments.json"))

SIG = re.compile(r"\b(sig|sig's|susquehanna)\b", re.I)
# first-person / recall markers
RECALL = re.compile(
    r"(i (was |got |had |remember|recall|did|took|just took)|they asked|asked me|"
    r"was asked|one (of the )?question|the question|last question|first question|"
    r"there (was|were) a|i think i|from what i remember|in the (oa|test|assessment)|"
    r"on the (oa|test|assessment)|q\d+|question \d+)", re.I)
# question-shaped content
SHAPE = re.compile(
    r"(probability|expected (value|number|payoff|return|sum)|\bEV\b|combinator|"
    r"permutation|how many ways|dice|die\b|coin|cards?\b|deck|spinner|frog|marble|ball|"
    r"urn|bayes|markov|sequence|market|bid|ask|quote|brain ?teaser|puzzle|liar|"
    r"paths?\b|grid|horses|poker)", re.I)
NOISE = re.compile(r"^(AutoModerator|quant-ModTeam|FinancialCareers-ModTeam)$")

rows = []
seen = set()
for pid, cs in threads.items():
    p = posts.get(pid, {})
    ptitle = p.get("title", "")
    psub = p.get("subreddit", "")
    ptext = ptitle + " " + (p.get("selftext") or "")
    for c in cs:
        a = c.get("author") or ""
        if NOISE.match(a):
            continue
        b = (c.get("body") or "").strip()
        if len(b) < 25 or b in ("[removed]", "[deleted]"):
            continue
        if not (SIG.search(b) or SIG.search(ptext)):
            continue
        if not SHAPE.search(b):
            continue
        if not RECALL.search(b):
            continue
        k = b[:120]
        if k in seen:
            continue
        seen.add(k)
        rows.append((c.get("created_utc") or 0, psub, pid, ptitle, a, c.get("id"), b))

# also scan post bodies themselves
for pid, p in posts.items():
    b = (p.get("selftext") or "").strip()
    t = p.get("title") or ""
    if len(b) < 25 or b in ("[removed]", "[deleted]"):
        continue
    if not SIG.search(t + " " + b):
        continue
    if not (SHAPE.search(b) and RECALL.search(b)):
        continue
    k = b[:120]
    if k in seen:
        continue
    seen.add(k)
    rows.append((p.get("created_utc") or 0, p.get("subreddit"), pid, "[POST] " + t,
                 p.get("author"), "", b))

rows.sort(key=lambda x: -x[0])
sys.stderr.write(f"hits {len(rows)}\n")
for cu, sub, pid, title, a, cid, b in rows:
    d = datetime.datetime.fromtimestamp(cu, datetime.UTC).strftime("%Y-%m-%d")
    url = (f"https://www.reddit.com/r/{sub}/comments/{pid}/_/{cid}/" if cid
           else f"https://www.reddit.com/r/{sub}/comments/{pid}/")
    print("=" * 108)
    print(f"{d} | r/{sub} | u/{a} | {url}")
    print(f"THREAD: {title}")
    print(b[:2600])
