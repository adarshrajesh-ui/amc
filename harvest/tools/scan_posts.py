#!/usr/bin/env python3
"""Rank cached Reddit POST bodies (selftext) by likely recall content.

Comments turned out to be mostly process chatter; the actual "here is what they asked me"
write-ups tend to be the top-level post, which the comment scanner never looked at.
"""
import datetime, json, re, sys

D = "/workspace/harvest/raw/_tiera_reddit"
posts = json.load(open(f"{D}/posts.json"))

FIRMS = [("Jane Street", (r"\bjane\s*street\b",)), ("Optiver", (r"\boptiver\b",)),
         ("Citadel", (r"\bcitadel\b", r"\bcitsec\b")), ("IMC Trading", (r"\bIMC\b",))]
FIRST = re.compile(r"\b(i was asked|they asked me|i got asked|the question was|"
                   r"first question|second question|asked me to|i did the|i took the|"
                   r"the oa was|i just did|i recently did|questions were)\b", re.I)
QY = re.compile(r"(what(?:'s| is| was) the (?:probability|expected|ev|answer)|how many|"
                r"you (?:roll|flip|draw|pick)|make a market|\bdice\b|\bdie\b|\bcoin\b|"
                r"\burn\b|\bmarbles?\b|deck of cards|expected number|\bbulbs?\b)", re.I)
RECALL = re.compile(r"\b(oa|online assessment|hackerrank|codesignal|superday|mental math|"
                    r"sequences|market mak|brain ?teaser|expected value|trading game|"
                    r"zetamac|80 in 8|zap-?n|estimath)\b", re.I)

want = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] else None
mn = int(sys.argv[2]) if len(sys.argv) > 2 else 8
lim = int(sys.argv[3]) if len(sys.argv) > 3 else 25
skip = int(sys.argv[4]) if len(sys.argv) > 4 else 0

def firm_of(t):
    for f, ps in FIRMS:
        if any(re.search(p, t) for p in ps):
            return f
    return None

rows = []
for p in posts:
    st = p.get("selftext") or ""
    ti = p.get("title") or ""
    if len(st) < 120 or st.strip() in ("[deleted]", "[removed]"):
        continue
    f = firm_of(ti) or firm_of(st)
    if not f or (want and f != want):
        continue
    s = 4 * len(FIRST.findall(st)) + 3 * len(set(m.lower() for m in QY.findall(st))) \
        + 2 * len(set(m.lower() for m in RECALL.findall(st)))
    if s >= mn:
        rows.append((s, f, ti, p.get("permalink") or "", p.get("author"),
                     p.get("created_utc"), st))
rows.sort(key=lambda r: -r[0])
print(f"### {len(rows)} post candidates of {len(posts)}\n")
for s, f, ti, perma, au, ts, st in rows[skip:skip + lim]:
    try:
        d = datetime.datetime.fromtimestamp(int(ts), datetime.UTC).strftime("%Y-%m-%d")
    except Exception:
        d = "?"
    print(f"===== score={s} [{f}] {d} u/{au}  {ti[:100]}")
    print(f"https://www.reddit.com{perma}")
    print(st[:2200])
    print()
