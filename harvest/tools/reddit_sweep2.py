#!/usr/bin/env python3
"""Second Reddit pass.

The first pass counted a 422 "Timeout. Maybe slow down a bit" as an empty result,
which silently wrote off every large subreddit (csMajors, cscareerquestions,
internships...). Arctic Shift will run the same full-text query happily if the
scan is bounded, so this re-runs the misses one year-window at a time with a real
backoff, and only declares a (sub, term) pair empty once every window has come
back 200.
"""
import json
import os
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import quote

CACHE = "/workspace/harvest/.reddit_cache"
API = "https://arctic-shift.photon-reddit.com/api"
os.makedirs(CACHE, exist_ok=True)
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/122 Safari/537.36"

SUBS = ["csMajors", "cscareerquestions", "internships", "developersIndia", "leetcode",
        "cscareerquestionsEU", "algotrading", "options", "Trading", "datascience",
        "statistics", "MachineLearning", "compsci", "UIUC", "uwaterloo", "berkeley",
        "cmu", "gatech", "nyu", "Purdue", "jobs", "EngineeringStudents", "intern",
        "quant", "quantfinance", "FinancialCareers"]

TERMS = ["Akuna", "Hudson River Trading", "Jump Trading", "DRW", "Five Rings",
         "Old Mission", "Two Sigma", "DE Shaw", "HRT"]

WINDOWS = [("%d-01-01" % y, "%d-01-01" % (y + 1)) for y in range(2016, 2027)]


def slug(s):
    return re.sub(r"[^A-Za-z0-9]+", "_", s)[:170]


def fetch(url, key):
    path = os.path.join(CACHE, key + ".json")
    if os.path.exists(path):
        try:
            return json.load(open(path, encoding="utf-8")).get("data") or []
        except Exception:
            pass
    for attempt in range(5):
        try:
            out = subprocess.run(["curl", "-s", "--max-time", "70", "--compressed",
                                  "-A", UA, url], capture_output=True, timeout=80).stdout
            d = json.loads(out.decode("utf-8", "replace"))
        except Exception:
            time.sleep(2 + 3 * attempt)
            continue
        if d.get("data") is not None:
            open(path, "wb").write(out)
            return d["data"]
        if "imeout" in str(d.get("error", "")) or "low down" in str(d.get("error", "")):
            time.sleep(3 + 4 * attempt)
            continue
        return []
    return []


def main():
    jobs = []
    for sub in SUBS:
        for term in TERMS:
            for a, b in WINDOWS:
                jobs.append((sub, term, a, b))
    print("%d windowed jobs" % len(jobs), file=sys.stderr)
    done = [0]
    total = [0]

    def run(j):
        sub, term, a, b = j
        n = 0
        for field, ep in (("selftext", "posts"), ("title", "posts"), ("body", "comments")):
            url = ("%s/%s/search?subreddit=%s&%s=%s&after=%s&before=%s&limit=100"
                   % (API, ep, quote(sub), field, quote(term), a, b))
            rows = fetch(url, "w_%s_%s_%s_%s" % (slug(sub), field, slug(term), a[:4]))
            n += len(rows)
        done[0] += 1
        total[0] += n
        if done[0] % 150 == 0:
            print("  %d/%d  rows=%d" % (done[0], len(jobs), total[0]), file=sys.stderr, flush=True)
        return n

    with ThreadPoolExecutor(max_workers=8) as ex:
        list(ex.map(run, jobs))
    print("pass2 rows: %d" % total[0])


if __name__ == "__main__":
    main()
