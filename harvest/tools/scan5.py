#!/usr/bin/env python3
"""Final precision sweep over the finished cache.

Earlier passes looked for SIG mentions and then read everything. The cache is now large
enough that this drowns in "how long till they get back to me" traffic, so this pass
demands that a comment in a SIG-titled thread actually *state a problem*: a number or a
quantifier next to probability/game vocabulary, in a sentence that reads as recall
rather than a request for help. Anything already emitted is excluded.
"""
import json, re, sys, datetime

OUT = "/workspace/harvest/raw/_reddit_cache"
JSONL = "/workspace/harvest/raw/sig_qt_english_forums.jsonl"

posts = {}
for f in ("mega_posts.json", "posts.json"):
    try:
        posts.update({p["id"]: p for p in json.load(open(f"{OUT}/{f}"))})
    except FileNotFoundError:
        pass
threads = {}
for f in ("thread_comments.json", "thread_comments3.json", "mega_comments.json"):
    try:
        threads.update(json.load(open(f"{OUT}/{f}")))
    except FileNotFoundError:
        pass

cited = set()
for line in open(JSONL):
    m = re.search(r"/comments/([a-z0-9]+)/(?:_/([a-z0-9]+)/)?", json.loads(line)["source_url"])
    if m:
        cited.add(m.group(1))
        if m.group(2):
            cited.add(m.group(2))

SIG = re.compile(r"\b(sig|susquehanna|susq)\b", re.I)
# Vendors and self-promoting bots that flooded r/quantfinance in 2026.
BOT = re.compile(r"(interviews\.chat|quantgrind|prachub|beyz|tradermath|interviewquery|"
                 r"lifegood4u|financeandquantsociety|oavoservice|quantblueprint|jobtestprep)", re.I)
# Vocabulary that only appears when someone is describing an actual problem.
PROB = re.compile(r"(probabilit|expected value|\bEV\b|combinator|bayes|dice|die\b|coin|card|deck|"
                  r"marbles?|balls?|urn|flip|roll|market mak|two-sided|bid|ask|sequence|"
                  r"brain ?teaser|puzzle|game)", re.I)
# First-person recall, not a request for help.
RECALL = re.compile(r"(i (was |got |had |did |remember|recall)|they asked|i (just )?took|"
                    r"on (my|the) (oa|test|assessment|interview)|one (of the )?question|"
                    r"the question (was|asked)|asked me|there was a)", re.I)
NUM = re.compile(r"\d")

rows = []
for pid, cs in threads.items():
    p = posts.get(pid, {})
    title = p.get("title") or ""
    tsig = bool(SIG.search(title))
    for c in cs:
        b = c.get("body") or ""
        cid = c["id"]
        if cid in cited or pid in cited:
            continue
        if len(b) < 60 or BOT.search(b):
            continue
        if not (tsig or SIG.search(b)):
            continue
        if not (PROB.search(b) and RECALL.search(b) and NUM.search(b)):
            continue
        rows.append((c.get("created_utc", 0), pid, title, c))

rows.sort(reverse=True)
sys.stderr.write(f"hits {len(rows)}\n")
for ts, pid, title, c in rows:
    d = datetime.datetime.fromtimestamp(ts, datetime.UTC).strftime("%Y-%m-%d")
    sub = c.get("subreddit") or posts.get(pid, {}).get("subreddit")
    print("=" * 100)
    print(f"{d} | r/{sub} | u/{c.get('author')} | "
          f"https://www.reddit.com/r/{sub}/comments/{pid}/_/{c['id']}/")
    print(f"THREAD: {title}")
    print(c.get("body"))
