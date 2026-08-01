#!/usr/bin/env python3
"""Sweep the Arctic Shift Reddit archive for Tier-A firm mentions.

reddit.com itself 403s this box and pullpush.io is behind Cloudflare, but
arctic-shift.photon-reddit.com answers. Its full-text search refuses to run
unscoped ("'body' query parameter requires one of: author, subreddit, ..."),
so every query is (subreddit x term) and the subreddit list is what does the
recall work here.

Phase 1 writes post hits to .reddit_cache; phase 2 pulls every comment of the
posts that survive triage, since the actual "they asked me X" text is almost
always a comment rather than the submission body.
"""
import json
import os
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

CACHE = "/workspace/harvest/.reddit_cache"
API = "https://arctic-shift.photon-reddit.com/api"
os.makedirs(CACHE, exist_ok=True)

SUBS = [
    "quant", "quantfinance", "FinancialCareers", "csMajors", "leetcode",
    "cscareerquestions", "cscareerquestionsEU", "developersIndia", "algotrading",
    "Trading", "internships", "intern", "EngineeringStudents", "UIUC", "uwaterloo",
    "berkeley", "cmu", "gatech", "nyu", "Purdue", "UTAustin", "jobs", "statistics",
    "datascience", "MachineLearning", "quantitative", "highfreqtrading", "options",
    "Daytrading", "financialmodelling", "GetEmployed", "csharp", "cpp", "cpp_questions",
    "compsci", "OMSCS", "MSFinance", "MathHelp", "learnmath", "probabilitytheory",
    "AskStatistics", "quantitativefinance", "Bogleheads", "SecurityAnalysis",
    "UBC", "McGill", "Cornell", "mit", "Stanford", "UPenn", "columbia", "uofm",
    "UniversityOfLondon", "cambridge_uni", "Oxforduni", "unimelb", "usyd", "UNSW",
    "Sydney", "AusFinance", "singapore", "hongkong", "London", "chicago",
    "financialindependence", "wallstreetbets", "investing", "CFA", "actuary",
]

TERMS = [
    "Akuna", "Hudson River Trading", "HRT", "Jump Trading", "DRW", "Five Rings",
    "Old Mission", "Two Sigma", "DE Shaw", "D.E. Shaw", "Shaw",
]

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/122 Safari/537.36")


def slug(s):
    return re.sub(r"[^A-Za-z0-9]+", "_", s)[:170]


def get(url, key, force=False):
    path = os.path.join(CACHE, key + ".json")
    if os.path.exists(path) and os.path.getsize(path) > 2 and not force:
        try:
            return json.load(open(path, encoding="utf-8"))
        except Exception:
            pass
    try:
        out = subprocess.run(
            ["curl", "-s", "--max-time", "50", "--compressed", "-A", UA, url],
            capture_output=True, timeout=60).stdout.decode("utf-8", "replace")
        d = json.loads(out)
    except Exception as e:
        return {"data": None, "error": str(e)}
    if d.get("data") is not None:
        open(path, "w", encoding="utf-8").write(out)
    return d


def q(s):
    from urllib.parse import quote
    return quote(str(s), safe="")


def search_posts(sub, term, field):
    url = "%s/posts/search?subreddit=%s&%s=%s&limit=100" % (API, q(sub), field, q(term))
    d = get(url, "p_%s_%s_%s" % (slug(sub), field, slug(term)))
    return d.get("data") or []


def search_comments(sub, term):
    url = "%s/comments/search?subreddit=%s&body=%s&limit=100" % (API, q(sub), q(term))
    d = get(url, "c_%s_%s" % (slug(sub), slug(term)))
    return d.get("data") or []


def phase1():
    jobs = []
    for sub in SUBS:
        for term in TERMS:
            jobs.append(("title", sub, term))
            jobs.append(("selftext", sub, term))
            jobs.append(("body", sub, term))

    hits = {}
    done = [0]

    def run(j):
        kind, sub, term = j
        try:
            rows = search_comments(sub, term) if kind == "body" else search_posts(sub, term, kind)
        except Exception:
            rows = []
        done[0] += 1
        if done[0] % 100 == 0:
            print("  ...%d/%d" % (done[0], len(jobs)), file=sys.stderr, flush=True)
        return (kind, sub, term, len(rows))

    with ThreadPoolExecutor(max_workers=12) as ex:
        for kind, sub, term, n in ex.map(run, jobs):
            if n:
                hits[(sub, term, kind)] = n
    tot = sum(hits.values())
    print("phase1: %d/%d queries returned rows, %d total rows" % (len(hits), len(jobs), tot))
    bysub = {}
    for (sub, term, kind), n in hits.items():
        bysub[sub] = bysub.get(sub, 0) + n
    for s, n in sorted(bysub.items(), key=lambda x: -x[1])[:40]:
        print("  %-24s %d" % (s, n))


if __name__ == "__main__":
    phase1()
