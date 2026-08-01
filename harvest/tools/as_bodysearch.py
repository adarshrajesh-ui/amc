#!/usr/bin/env python3
"""Comment full-text sweep.

The title-based crawl can only reach threads whose title names SIG. r/quant and
r/FinancialCareers both funnel "how do I pass the OA" traffic into weekly megathreads
with generic titles, so first-person SIG recalls sit inside threads no title search will
ever surface. The archive's comment `body` filter can be scoped to a subreddit, which
reaches them.
"""
import json, sys, time, urllib.parse, urllib.request

BASE = "https://arctic-shift.photon-reddit.com/api"
OUT = "/workspace/harvest/raw/_reddit_cache"
STORE = f"{OUT}/body_comments.json"
LAST = [0.0]
GAP = 9.0


def get(params, tries=7):
    url = f"{BASE}/comments/search?{urllib.parse.urlencode(params)}"
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
            time.sleep(10 + 10 * i)
            continue
        try:
            data = json.loads(body)
        except Exception:
            time.sleep(10 + 10 * i)
            continue
        err = str(data.get("error") or "")
        if err:
            sys.stderr.write(f"  err{i} {err[:70]}\n")
            time.sleep(12 + 12 * i)
            continue
        return data.get("data") or []
    return None


SUBS = ["quant", "FinancialCareers", "cscareerquestions", "csMajors", "quantfinance",
        "algotrading", "askmath", "probabilitytheory", "learnmath", "HomeworkHelp",
        "puzzles", "riddles", "brainteasers", "statistics", "AskStatistics",
        "cscareerquestionsuk", "UKJobs", "ireland", "AusFinance", "uwaterloo",
        "berkeley", "UIUC", "nyu", "cmu", "UPenn", "mit", "Cornell", "columbia",
        "gatech", "unimelb", "UNSW", "trinitycollegedublin", "ucd", "imperialcollege",
        "cambridge_uni", "Oxforduni", "poker", "options", "highfreqtrading"]
TERMS = ["Susquehanna", "SIG OA", "SIG assessment", "SIG interview", "SIG trading",
         "SIG intern", "SIG superday", "SIG phone", "SIG final round"]

try:
    store = json.load(open(STORE))
except Exception:
    store = {}
try:
    done = set(json.load(open(f"{OUT}/body_done.json")))
except Exception:
    done = set()

for sub in SUBS:
    for term in TERMS:
        key = f"{sub}|{term}"
        if key in done:
            continue
        r = get({"subreddit": sub, "body": term, "limit": 100})
        if r is None:
            sys.stderr.write(f"[fail] {key}\n")
            continue
        new = 0
        for c in r:
            if c["id"] not in store:
                new += 1
            store[c["id"]] = c
        done.add(key)
        with open(STORE, "w") as f:
            json.dump(store, f)
        with open(f"{OUT}/body_done.json", "w") as f:
            json.dump(sorted(done), f)
        sys.stderr.write(f"[ok] r/{sub} '{term}' n={len(r)} new={new} total={len(store)}\n")

print("TOTAL", len(store))
