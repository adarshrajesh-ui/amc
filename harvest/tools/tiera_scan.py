#!/usr/bin/env python3
"""Rank cached Reddit posts+comments by how likely they are to contain an actual
question recall, and print them with permalinks for manual transcription.

Scoring is deliberately crude: firm name present, plus recall vocabulary, plus signals
that the author is describing their own sitting ("I was asked", "they asked me"). The
point is ordering, not classification -- every candidate is read by hand before it
becomes a record.
"""
import json, re, sys

D = "/workspace/harvest/raw/_tiera_reddit"
posts = json.load(open(f"{D}/posts.json"))
try:
    comments = json.load(open(f"{D}/comments.json"))
except Exception:
    comments = []

FIRMS = {
    "Jane Street": (r"\bjane\s*street\b", r"\bJS\b"),
    "Optiver": (r"\boptiver\b",),
    "Citadel": (r"\bcitadel\b", r"\bcitsec\b"),
    "IMC Trading": (r"\bIMC\b",),
}
FIRST_PERSON = re.compile(
    r"\b(i was asked|they asked me|i got asked|my oa|i had (?:the|an|my)|"
    r"the question was|first question|second question|one question|asked me to|"
    r"i did the|i took the|the oa was|the test was|i interviewed|during my)\b", re.I)
RECALL = re.compile(
    r"\b(oa|online assessment|hackerrank|codesignal|superday|final round|"
    r"first round|phone screen|mental math|sequences|market mak|estimath|"
    r"brain ?teaser|probability|expected value|trading game|zetamac|"
    r"80 in 8|80 questions)\b", re.I)
QUESTIONY = re.compile(
    r"(what(?:'s| is) the (?:probability|expected|ev)|how many|"
    r"you (?:roll|flip|draw|have|are given)|make a market|"
    r"\bdice\b|\bcoin\b|\burn\b|\bmarbles?\b|\bdeck of cards\b)", re.I)

want = sys.argv[1] if len(sys.argv) > 1 else None
minscore = int(sys.argv[2]) if len(sys.argv) > 2 else 5

rows = []
for c in comments:
    body = c.get("body") or ""
    if len(body) < 60:
        continue
    for firm, pats in FIRMS.items():
        if not any(re.search(p, body) for p in pats):
            continue
        if want and firm != want:
            continue
        s = 0
        s += 4 * len(FIRST_PERSON.findall(body))
        s += 2 * len(set(m.lower() for m in RECALL.findall(body)))
        s += 3 * len(set(m.lower() for m in QUESTIONY.findall(body)))
        if s >= minscore:
            rows.append((s, firm, "c", c.get("permalink") or "", c.get("author"),
                         c.get("created_utc"), body))
        break

for p in posts:
    body = (p.get("title") or "") + "\n" + (p.get("selftext") or "")
    if len(body) < 60:
        continue
    for firm, pats in FIRMS.items():
        if not any(re.search(pt, body) for pt in pats):
            continue
        if want and firm != want:
            continue
        s = 0
        s += 4 * len(FIRST_PERSON.findall(body))
        s += 2 * len(set(m.lower() for m in RECALL.findall(body)))
        s += 3 * len(set(m.lower() for m in QUESTIONY.findall(body)))
        if s >= minscore:
            rows.append((s, firm, "p", p.get("permalink") or "", p.get("author"),
                         p.get("created_utc"), body))
        break

rows.sort(key=lambda r: -r[0])
import datetime
print(f"### {len(rows)} candidates (posts={len(posts)} comments={len(comments)})\n")
for s, firm, kind, perma, author, ts, body in rows[:int(sys.argv[3]) if len(sys.argv) > 3 else 40]:
    try:
        d = datetime.datetime.utcfromtimestamp(int(ts)).strftime("%Y-%m-%d")
    except Exception:
        d = "?"
    print(f"===== score={s} {firm} {kind} {d} u/{author}")
    print(f"https://www.reddit.com{perma}")
    print(body[:2200])
    print()
