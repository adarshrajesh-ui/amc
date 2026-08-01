#!/usr/bin/env python3
"""Re-sweep the (grown) Reddit cache for SIG assessment content, excluding anything
whose comment/post id is already cited in the shard JSONL."""
import json, re, sys, datetime

OUT = "/workspace/harvest/raw/_reddit_cache"
JSONL = "/workspace/harvest/raw/sig_qt_english_forums.jsonl"

posts = {p["id"]: p for p in json.load(open(f"{OUT}/posts.json"))}
threads = {}
for _f in ("thread_comments.json", "thread_comments3.json"):
    try:
        threads.update(json.load(open(f"{OUT}/{_f}")))
    except FileNotFoundError:
        pass

used = set()
for line in open(JSONL):
    u = json.loads(line)["source_url"]
    for part in u.rstrip("/").split("/"):
        if part:
            used.add(part)

SIG = re.compile(r"\b(sig|sig's|susquehanna)\b", re.I)
RECALL = re.compile(
    r"(i (was |got |had |remember|recall|did|took|just took|have)|they asked|asked me|"
    r"was asked|one (of the )?question|the question|last question|first question|"
    r"there (was|were) a|from what i remember|in the (oa|test|assessment)|"
    r"on the (oa|test|assessment)|q\d+|question \d+|my (oa|interview|superday|final)|"
    r"the (oa|test|assessment|superday|final round) (was|had|consisted))", re.I)
SHAPE = re.compile(
    r"(probability|expected (value|number|payoff|return|sum)|\bEV\b|combinator|"
    r"permutation|how many ways|dice|die\b|coin|cards?\b|deck|spinner|frog|marble|ball|"
    r"urn|bayes|markov|sequence|market ?mak|bid|ask|quote|brain ?teaser|puzzle|liar|"
    r"paths?\b|grid|horses|poker|widget|cookie|painting|calculus|logic)", re.I)
NOISE = re.compile(r"^(AutoModerator|quant-ModTeam|FinancialCareers-ModTeam)$")

rows = []
seen = set()
for pid, cs in threads.items():
    p = posts.get(pid, {})
    ptext = (p.get("title") or "") + " " + (p.get("selftext") or "")
    for c in cs:
        if NOISE.match(c.get("author") or ""):
            continue
        if c.get("id") in used:
            continue
        b = (c.get("body") or "").strip()
        if len(b) < 25 or b in ("[removed]", "[deleted]"):
            continue
        if not (SIG.search(b) or SIG.search(ptext)):
            continue
        if not (SHAPE.search(b) and RECALL.search(b)):
            continue
        k = b[:120]
        if k in seen:
            continue
        seen.add(k)
        rows.append((c.get("created_utc") or 0, p.get("subreddit"), pid,
                     p.get("title"), c.get("author"), c.get("id"), b))

for pid, p in posts.items():
    if pid in used:
        continue
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
    print("=" * 104)
    print(f"{d} | r/{sub} | u/{a} | {url}")
    print(f"THREAD: {title}")
    print(b[:2200])
