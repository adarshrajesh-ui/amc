#!/usr/bin/env python3
"""Megathread sweep.

r/quant's moderators redirect every "how do I pass the OA / what did they ask" post into
a weekly megathread, so the SIG recalls that survive moderation live inside threads whose
titles never mention SIG. The archive's comment body search is scoped-only and times out
server-side, so the workable route is: find the megathreads by title, pull their whole
comment trees, and grep locally for SIG.
"""
import json, re, sys, time, urllib.parse, urllib.request

BASE = "https://arctic-shift.photon-reddit.com/api"
OUT = "/workspace/harvest/raw/_reddit_cache"
STORE = f"{OUT}/mega_comments.json"
LAST = [0.0]
GAP = 7.0


def get(path, params, tries=6):
    url = f"{BASE}/{path}?{urllib.parse.urlencode(params)}"
    for i in range(tries):
        d = time.time() - LAST[0]
        if d < GAP:
            time.sleep(GAP - d)
        LAST[0] = time.time()
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "quant-research-harvest/1.0"})
            with urllib.request.urlopen(req, timeout=240) as r:
                body = r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            try:
                body = e.read().decode("utf-8", "replace")
            except Exception:
                body = ""
        except Exception as e:
            sys.stderr.write(f"  net{i} {e}\n")
            time.sleep(8 + 8 * i)
            continue
        try:
            data = json.loads(body)
        except Exception:
            time.sleep(8 + 8 * i)
            continue
        if str(data.get("error") or ""):
            time.sleep(10 + 10 * i)
            continue
        return data.get("data") or []
    return None


QUERIES = [
    ("quant", "Megathread"),
    ("quant", "weekly megathread"),
    ("quant", "Education Megathread"),
    ("quant", "Career Megathread"),
    ("quant", "interview megathread"),
    ("FinancialCareers", "Megathread"),
    ("FinancialCareers", "interview thread"),
    ("csMajors", "Megathread"),
    ("cscareerquestions", "interview discussion"),
]

try:
    posts = {p["id"]: p for p in json.load(open(f"{OUT}/mega_posts.json"))}
except Exception:
    posts = {}

for sub, q in QUERIES:
    r = get("posts/search", {"subreddit": sub, "query": q, "limit": 100})
    if r is None:
        sys.stderr.write(f"[fail] r/{sub} '{q}'\n")
        continue
    new = 0
    for p in r:
        if p["id"] not in posts:
            new += 1
        posts[p["id"]] = p
    with open(f"{OUT}/mega_posts.json", "w") as f:
        json.dump(list(posts.values()), f)
    sys.stderr.write(f"[posts] r/{sub} '{q}' n={len(r)} new={new} total={len(posts)}\n")

MEGA = re.compile(r"(megathread|weekly|interview thread|discussion thread)", re.I)
cand = [p for p in posts.values()
        if MEGA.search(p.get("title") or "") and (p.get("num_comments") or 0) >= 3]
cand.sort(key=lambda p: -(p.get("num_comments") or 0))
sys.stderr.write(f"megathreads to fetch: {len(cand)}\n")

try:
    store = json.load(open(STORE))
except Exception:
    store = {}

for n, p in enumerate(cand):
    pid = p["id"]
    if pid in store:
        continue
    r = get("comments/search", {"link_id": pid, "limit": 100})
    if r is None:
        sys.stderr.write(f"[fail] {pid}\n")
        continue
    store[pid] = r
    with open(STORE, "w") as f:
        json.dump(store, f)
    hits = sum(1 for c in r if re.search(r"\b(sig|susquehanna)\b", c.get("body") or "", re.I))
    sys.stderr.write(f"[{n}/{len(cand)}] {pid} r/{p.get('subreddit')} n={len(r)} "
                     f"sig={hits} :: {(p.get('title') or '')[:60]}\n")

print("done", len(store))
