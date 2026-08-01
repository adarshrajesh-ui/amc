#!/usr/bin/env python3
"""Second archive pass: math/puzzle help subs where candidates repost OA questions verbatim."""
import json, os, sys, time, urllib.parse, urllib.request

BASE = "https://arctic-shift.photon-reddit.com/api"
OUT = "/workspace/harvest/raw/_reddit_cache"
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
            with urllib.request.urlopen(req, timeout=180) as r:
                body = r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            try:
                body = e.read().decode("utf-8", "replace")
            except Exception:
                body = ""
        except Exception as e:
            sys.stderr.write(f"  net{i} {e}\n")
            time.sleep(7 + 7 * i)
            continue
        try:
            data = json.loads(body)
        except Exception:
            time.sleep(7 + 7 * i)
            continue
        if data.get("error"):
            time.sleep(8 + 8 * i)
            continue
        return data.get("data") or []
    return None


SUBS = ["quant", "FinancialCareers", "cscareerquestions",
        "askmath", "probabilitytheory", "learnmath", "mathematics", "statistics",
        "AskStatistics", "puzzles", "riddles", "HomeworkHelp", "cheatatmathhomework",
        "math", "quantfinance", "csMajors", "cscareerquestionsuk", "UKJobs",
        "quantitative", "brainteasers", "GAMETHEORY", "poker", "options",
        "algotrading", "highfreqtrading", "Optiver", "janestreet", "OMSCS",
        "UIUC", "berkeley", "uwaterloo", "cmu", "nyu", "unimelb", "UNSW",
        "trinitycollegedublin", "ucd", "ireland", "AusFinance", "Sydney",
        "cambridge_uni", "Oxforduni", "imperialcollege", "columbia", "Cornell",
        "gatech", "UTAustin", "mit", "UPenn", "Purdue", "UBC"]
TERMS = ["SIG", "Susquehanna"]
CORE_EXTRA = ["SIG OA", "SIG interview", "SIG superday", "SIG intern", "SIG trading",
              "Susquehanna interview", "Susquehanna OA", "Susquehanna intern",
              "SIG assessment", "SIG discovery", "SIG quant", "SIG phone",
              "SIG final round", "SIG trading game", "SIG market making"]
CORE = {"quant", "FinancialCareers", "cscareerquestions"}

posts = {p["id"]: p for p in json.load(open(f"{OUT}/posts.json"))}
try:
    done = set(json.load(open(f"{OUT}/done2.json")))
except Exception:
    done = set()

for sub in SUBS:
    for term in (TERMS + CORE_EXTRA if sub in CORE else TERMS):
        key = f"{sub}|{term}"
        if key in done:
            continue
        r = get("posts/search", {"subreddit": sub, "query": term, "limit": 100})
        if r is None:
            sys.stderr.write(f"[fail] {key}\n")
            continue
        new = 0
        for p in r:
            if p["id"] not in posts:
                new += 1
            posts[p["id"]] = p
        done.add(key)
        with open(f"{OUT}/posts.json", "w") as f:
            json.dump(list(posts.values()), f)
        with open(f"{OUT}/done2.json", "w") as f:
            json.dump(sorted(done), f)
        sys.stderr.write(f"[ok] r/{sub} '{term}' n={len(r)} new={new} total={len(posts)}\n")

print("TOTAL", len(posts))
