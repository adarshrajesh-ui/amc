#!/usr/bin/env python3
"""Crawl the Arctic Shift Reddit archive for SIG/Susquehanna assessment recall posts+comments.

Resumable: keeps a done-list so re-runs only fetch what is still missing.
"""
import json, os, sys, time, urllib.parse, urllib.request

BASE = "https://arctic-shift.photon-reddit.com/api"
OUT = "/workspace/harvest/raw/_reddit_cache"
os.makedirs(OUT, exist_ok=True)
LAST = [0.0]
GAP = 11.0


def load(name, default):
    try:
        with open(f"{OUT}/{name}") as f:
            return json.load(f)
    except Exception:
        return default


def get(path, params, tries=8):
    """Return list on success, None on hard failure (bad sub / exhausted retries)."""
    url = f"{BASE}/{path}?{urllib.parse.urlencode(params)}"
    for i in range(tries):
        d = time.time() - LAST[0]
        if d < GAP:
            time.sleep(GAP - d)
        LAST[0] = time.time()
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "quant-research-harvest/1.0"})
            with urllib.request.urlopen(req, timeout=180) as r:
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
        err = str(data.get("error") or "")
        if err:
            if "Timeout" in err or "slow down" in err:
                time.sleep(10 + 10 * i)
                continue
            sys.stderr.write(f"  ERR {err} :: {params}\n")
            return None
        return data.get("data") or []
    sys.stderr.write(f"  EXHAUSTED :: {params}\n")
    return None


CORE = ["quant", "FinancialCareers", "csMajors", "cscareerquestions",
        "highfreqtrading", "algotrading", "quantitativefinance",
        "cscareerquestionsuk", "options", "poker"]
EXTRA = ["leetcode", "cscareerquestionsEU", "UIUC", "berkeley", "uwaterloo",
         "cmu", "nyu", "UBC", "unimelb", "UNSW", "Purdue", "gatech", "UTAustin",
         "mit", "Cornell", "UPenn", "cambridge_uni", "Oxforduni",
         "imperialcollege", "trinitycollegedublin", "ucd", "ireland",
         "AusFinance", "Sydney", "melbourne", "HongKong", "singapore",
         "columbia", "Northwestern", "ucla", "Stanford", "mathematics",
         "statistics", "AskStatistics", "actuary", "Trading", "Daytrading"]

POST_TERMS = ["SIG", "Susquehanna", "SIG OA", "SIG interview", "SIG superday",
              "Susquehanna interview", "Susquehanna internship", "SIG trading",
              "SIG intern", "Susquehanna trading"]
COMMENT_TERMS = ["Susquehanna", "SIG OA", "SIG interview", "SIG superday",
                 "Susquehanna OA", "SIG trading", "SIG intern", "Susquehanna intern"]

posts = {p["id"]: p for p in load("posts.json", [])}
comments = {c["id"]: c for c in load("comments_bodysearch.json", [])}
done = set(load("done.json", []))


def save():
    with open(f"{OUT}/posts.json", "w") as f:
        json.dump(list(posts.values()), f)
    with open(f"{OUT}/comments_bodysearch.json", "w") as f:
        json.dump(list(comments.values()), f)
    with open(f"{OUT}/done.json", "w") as f:
        json.dump(sorted(done), f)


jobs = []
for sub in CORE:
    for term in COMMENT_TERMS:
        jobs.append(("comments/search", sub, term))
for sub in CORE + EXTRA:
    for term in (POST_TERMS if sub in CORE else ["SIG", "Susquehanna"]):
        jobs.append(("posts/search", sub, term))
for sub in EXTRA:
    for term in ["Susquehanna", "SIG OA"]:
        jobs.append(("comments/search", sub, term))

for n, (path, sub, term) in enumerate(jobs):
    key = f"{path}|{sub}|{term}"
    if key in done:
        continue
    field = "query" if path.startswith("posts") else "body"
    r = get(path, {"subreddit": sub, field: term, "limit": 100})
    if r is None:
        sys.stderr.write(f"[fail {n}/{len(jobs)}] {key}\n")
        continue
    tgt = posts if path.startswith("posts") else comments
    for x in r:
        tgt[x["id"]] = x
    done.add(key)
    sys.stderr.write(f"[ok {n}/{len(jobs)}] {key} n={len(r)} P={len(posts)} C={len(comments)}\n")
    save()

save()
print("TOTAL", len(posts), len(comments))
