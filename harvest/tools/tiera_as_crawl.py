#!/usr/bin/env python3
"""Crawl the Arctic Shift Reddit archive for Jane Street / Citadel / Optiver / IMC
assessment-recall posts and comments.

Reddit itself 403s every direct request from this host, but the Arctic Shift mirror
serves the same author-written bodies over a plain JSON API, so recalls can be read in
full rather than guessed at from search snippets.

Two-stage: find candidate threads by title/selftext search, then pull each thread's full
comment tree by link_id. Recalls overwhelmingly live in replies, and a link_id lookup is
a cheap indexed query where an unbounded body regex is not.

The upstream frequently answers 422 "Timeout. Maybe slow down a bit"; that is a
server-side query timeout, not a ban, so it is retried rather than treated as fatal.
Resumable via a done-list.
"""
import json, os, sys, time, urllib.error, urllib.parse, urllib.request

BASE = "https://arctic-shift.photon-reddit.com/api"
OUT = "/workspace/harvest/raw/_tiera_reddit"
os.makedirs(OUT, exist_ok=True)
LAST = [0.0]
GAP = 3.0


def load(name, default):
    try:
        with open(f"{OUT}/{name}") as f:
            return json.load(f)
    except Exception:
        return default


def get(path, params, tries=5):
    params = dict(params)
    params.setdefault("sort", "desc")
    url = f"{BASE}/{path}?{urllib.parse.urlencode(params)}"
    for i in range(tries):
        d = time.time() - LAST[0]
        if d < GAP:
            time.sleep(GAP - d)
        LAST[0] = time.time()
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "quant-research-harvest/1.0"})
            with urllib.request.urlopen(req, timeout=120) as r:
                body = r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            try:
                body = e.read().decode("utf-8", "replace")
            except Exception:
                body = ""
        except Exception as e:
            sys.stderr.write(f"  net{i} {e}\n")
            time.sleep(5 + 5 * i)
            continue
        try:
            data = json.loads(body)
        except Exception:
            time.sleep(5 + 5 * i)
            continue
        err = str(data.get("error") or "")
        if err:
            if "Timeout" in err or "slow down" in err:
                time.sleep(4 + 6 * i)
                continue
            sys.stderr.write(f"  ERR {err} :: {params}\n")
            return None
        return data.get("data") or []
    return None


CORE = ["quant", "FinancialCareers", "csMajors", "cscareerquestions",
        "highfreqtrading", "algotrading", "quantitativefinance",
        "cscareerquestionsuk", "leetcode", "Trading", "options",
        "cscareerquestionsEU", "mathematics", "statistics", "datascience",
        "uwaterloo", "UIUC", "berkeley", "cmu", "nyu", "gatech",
        "Purdue", "mit", "Cornell", "UPenn", "columbia", "ucla",
        "UBC", "unimelb", "UNSW", "AusFinance", "cambridge_uni",
        "Oxforduni", "imperialcollege", "UniUK", "6thForm",
        "Netherlands", "singapore", "HongKong", "developersIndia",
        "Btechtards", "actuary", "poker", "MachineLearning", "OMSCS",
        "Amsterdam", "chicago", "financialmodelling", "quantfinance"]

POST_TERMS = ["Jane Street", "Citadel", "Optiver", "IMC Trading", "IMC"]
DEEP_TERMS = ["Jane Street OA", "Jane Street interview", "Jane Street intern",
              "Citadel OA", "Citadel interview", "Citadel Securities",
              "Optiver OA", "Optiver interview", "Optiver intern",
              "IMC OA", "IMC interview", "IMC intern"]

posts = {p["id"]: p for p in load("posts.json", [])}
comments = {c["id"]: c for c in load("comments.json", [])}
done = set(load("done.json", []))

KEY = ("jane street", "janestreet", "citadel", "optiver", "imc ", " imc",
       "imc trading")
HINT = ("oa", "assessment", "interview", "intern", "test", "round", "question",
        "superday", "hackerrank", "codesignal", "math", "probability", "game")


def save():
    for name, obj in (("posts.json", posts), ("comments.json", comments)):
        with open(f"{OUT}/{name}", "w") as f:
            json.dump(list(obj.values()), f)
    with open(f"{OUT}/done.json", "w") as f:
        json.dump(sorted(done), f)


stage1 = []
for sub in CORE:
    for term in POST_TERMS:
        stage1.append((sub, term))
for sub in CORE[:15]:
    for term in DEEP_TERMS:
        stage1.append((sub, term))

for n, (sub, term) in enumerate(stage1):
    key = f"posts|{sub}|{term}"
    if key in done:
        continue
    r = get("posts/search", {"subreddit": sub, "query": term, "limit": 100})
    if r is None:
        sys.stderr.write(f"[fail {n}/{len(stage1)}] {key}\n")
        continue
    for x in r:
        posts[x["id"]] = x
    done.add(key)
    sys.stderr.write(f"[p {n}/{len(stage1)}] {key} n={len(r)} P={len(posts)}\n")
    if n % 10 == 0:
        save()
save()
sys.stderr.write(f"=== stage1 done, {len(posts)} posts ===\n")

# Stage 2: comment trees, most-relevant threads first so an interrupted run still has
# the threads whose titles promise an actual recall.
cands = []
for p in posts.values():
    blob = ((p.get("title") or "") + " " + (p.get("selftext") or "")).casefold()
    if not any(k in blob for k in KEY):
        continue
    score = sum(1 for h in HINT if h in blob) + 3 * sum(1 for h in HINT if h in (p.get("title") or "").casefold())
    score += min(int(p.get("num_comments") or 0) // 10, 8)
    cands.append((-score, p["id"]))
cands.sort()
sys.stderr.write(f"=== stage2: {len(cands)} candidate threads ===\n")

for n, (_, pid) in enumerate(cands):
    key = f"cmts|{pid}"
    if key in done:
        continue
    r = get("comments/search", {"link_id": "t3_" + pid, "limit": 100})
    if r is None:
        sys.stderr.write(f"[cfail {n}/{len(cands)}] {pid}\n")
        continue
    for x in r:
        comments[x["id"]] = x
    done.add(key)
    sys.stderr.write(f"[c {n}/{len(cands)}] {pid} n={len(r)} C={len(comments)}\n")
    if n % 10 == 0:
        save()

save()
print("TOTAL", len(posts), len(comments))
