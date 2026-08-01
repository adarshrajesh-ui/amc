#!/usr/bin/env python3
"""Surface Reddit comments/posts that plausibly contain a real SIG assessment question."""
import json, re, sys, datetime

OUT = "/workspace/harvest/raw/_reddit_cache"
posts = {p["id"]: p for p in json.load(open(f"{OUT}/posts.json"))}
try:
    threads = json.load(open(f"{OUT}/thread_comments.json"))
except Exception:
    threads = {}

SIG_CTX = re.compile(r"\b(sig|susquehanna)\b", re.I)
QUESTION = re.compile(
    r"(expected (value|number|payoff|profit)|probability (that|of)|what('s| is) the probability|"
    r"make a market|market on |quote a |bid.{0,12}ask|"
    r"asked me|they asked|one question|a question (was|about)|first question|"
    r"the question was|i (got|had) (a|an) question|i remember|"
    r"roll(ing)? (a|two|three|the) dice|die\b|coin flip|flip(ping)? (a|two) coin|"
    r"deck of cards|\bEV\b|brain ?teaser|sequence|"
    r"n\)?\s*=|how many ways|combinatoric|bayes|markov)", re.I)
NOISE = re.compile(r"^(AutoModerator|quant-ModTeam)$")

rows = []
for pid, cs in threads.items():
    p = posts.get(pid, {})
    ptitle = p.get("title", "")
    psub = p.get("subreddit", "")
    for c in cs:
        a = c.get("author") or ""
        if NOISE.match(a):
            continue
        b = (c.get("body") or "").strip()
        if len(b) < 40:
            continue
        if not QUESTION.search(b):
            continue
        ctx = b + " " + ptitle
        if not SIG_CTX.search(ctx):
            continue
        rows.append((c.get("created_utc") or 0, psub, pid, ptitle, a, c.get("id"), b))

rows.sort(key=lambda x: -x[0])
sys.stderr.write(f"hits {len(rows)}\n")
for cu, sub, pid, title, a, cid, b in rows:
    d = datetime.datetime.fromtimestamp(cu, datetime.UTC).strftime("%Y-%m-%d")
    print("=" * 110)
    print(f"{d} | r/{sub} | u/{a} | https://www.reddit.com/r/{sub}/comments/{pid}/_/{cid}/")
    print(f"THREAD: {title}")
    print(b[:2500])
