#!/usr/bin/env python3
"""Rank cached Reddit comments by likely recall content, attributing each comment to its
PARENT THREAD's firm.

The first scanner required the firm name inside the comment body, which threw away
almost everything: in a thread titled "Optiver OA" nobody repeats the word Optiver, they
just say "the second section was...". Joining on link_id recovers those.
"""
import datetime, json, re, sys

D = "/workspace/harvest/raw/_tiera_reddit"
posts = {p["id"]: p for p in json.load(open(f"{D}/posts.json"))}
try:
    comments = json.load(open(f"{D}/comments.json"))
except Exception:
    comments = []

FIRMS = [
    ("Jane Street", (r"\bjane\s*street\b", r"\bjanest\b")),
    ("Optiver", (r"\boptiver\b",)),
    ("Citadel", (r"\bcitadel\b", r"\bcitsec\b")),
    ("IMC Trading", (r"\bIMC\b",)),
]
FIRST_PERSON = re.compile(
    r"\b(i was asked|they asked me|i got asked|i had (?:the|an|my|a)|"
    r"the question was|first question|second question|one question|asked me to|"
    r"i did the|i took the|the oa was|the test was|i interviewed|during my|"
    r"my interview|i remember|got the oa|my oa|i just did|i recently did)\b", re.I)
RECALL = re.compile(
    r"\b(oa|online assessment|hackerrank|codesignal|superday|final round|"
    r"first round|phone screen|mental math|sequences|market mak|estimath|"
    r"brain ?teaser|expected value|trading game|zetamac|80 in 8|80 questions|"
    r"zap-?n|number logic|beat the odds)\b", re.I)
QUESTIONY = re.compile(
    r"(what(?:'s| is| was) the (?:probability|expected|ev|answer)|how many|"
    r"you (?:roll|flip|draw|have|are given|pick)|make a market|"
    r"\bdice\b|\bdie\b|\bcoin\b|\burn\b|\bmarbles?\b|\bdeck of cards\b|"
    r"\bbulbs?\b|\bballs?\b|expected number)", re.I)


def firm_of(text):
    for firm, pats in FIRMS:
        if any(re.search(p, text) for p in pats):
            return firm
    return None


def score(body):
    s = 4 * len(FIRST_PERSON.findall(body))
    s += 2 * len(set(m.lower() for m in RECALL.findall(body)))
    s += 3 * len(set(m.lower() for m in QUESTIONY.findall(body)))
    return s


want = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] else None
minscore = int(sys.argv[2]) if len(sys.argv) > 2 else 8
limit = int(sys.argv[3]) if len(sys.argv) > 3 else 30
skip = int(sys.argv[4]) if len(sys.argv) > 4 else 0

rows = []
for c in comments:
    body = c.get("body") or ""
    if len(body) < 80 or body.strip() in ("[deleted]", "[removed]"):
        continue
    lid = (c.get("link_id") or "").replace("t3_", "")
    parent = posts.get(lid) or {}
    ptitle = parent.get("title") or ""
    firm = firm_of(body) or firm_of(ptitle)
    if not firm or (want and firm != want):
        continue
    s = score(body)
    if firm_of(body):
        s += 2
    if s >= minscore:
        rows.append((s, firm, ptitle, c.get("permalink") or "", c.get("author"),
                     c.get("created_utc"), body))

rows.sort(key=lambda r: -r[0])
print(f"### {len(rows)} comment candidates (threads={len(posts)} comments={len(comments)})\n")
for s, firm, ptitle, perma, author, ts, body in rows[skip:skip + limit]:
    try:
        d = datetime.datetime.utcfromtimestamp(int(ts)).strftime("%Y-%m-%d")
    except Exception:
        d = "?"
    print(f"===== score={s} [{firm}] {d} u/{author}  THREAD: {ptitle[:90]}")
    print(f"https://www.reddit.com{perma}")
    print(body[:1800])
    print()
