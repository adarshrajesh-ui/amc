#!/usr/bin/env python3
"""Harvest Tier-A firm interview recalls from the Arctic Shift Reddit archive.

reddit.com 403s every direct request from this box, but the Arctic Shift archive
mirrors post/comment bodies verbatim and is reachable, so quotes taken from it are
the real Reddit text even though the permalink can't be re-fetched here.
The API rate-limits aggressively ("Timeout. Maybe slow down a bit"), hence the pacing.
"""
import json
import os
import re
import subprocess
import sys
import time
import urllib.parse

API = "https://arctic-shift.photon-reddit.com/api"
CACHE = "/workspace/harvest/.arctic_cache"
os.makedirs(CACHE, exist_ok=True)

SUBS = ["quant", "quantfinance", "FinancialCareers", "csMajors", "cscareerquestions",
        "leetcode", "internships"]

KEYWORDS = ["HRT", "Hudson River", "Jump Trading", "DRW", "Five Rings", "Akuna",
            "Old Mission", "Two Sigma", "DE Shaw", "D.E. Shaw"]

PAUSE = 2.5


def get(path, **params):
    params.setdefault("limit", 100)
    url = "%s/%s?%s" % (API, path, urllib.parse.urlencode(params))
    key = re.sub(r"[^A-Za-z0-9]+", "_", url)[:180]
    p = os.path.join(CACHE, key + ".json")
    if os.path.exists(p):
        try:
            return json.load(open(p, encoding="utf-8")).get("data") or []
        except Exception:
            pass
    delay = PAUSE
    for attempt in range(5):
        time.sleep(delay)
        r = subprocess.run(["curl", "-s", "--max-time", "70", url], capture_output=True)
        try:
            d = json.loads(r.stdout.decode("utf-8", errors="replace"))
        except Exception:
            delay = min(delay * 2, 40)
            continue
        err = d.get("error") or ""
        if err:
            if "slow down" in err.lower() or "timeout" in err.lower():
                delay = min(delay * 2, 40)
                continue
            return []          # genuine bad-parameter / unknown-sub error
        open(p, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False))
        return d.get("data") or []
    return []


def main():
    out = {}
    done = 0
    plan = [(s, k, path, f) for s in SUBS for k in KEYWORDS
            for path, f in (("comments/search", "body"),
                            ("posts/search", "selftext"))]
    for sub, kw, path, field in plan:
        for o in get(path, subreddit=sub, **{field: kw}):
            oid = o.get("id")
            if oid and oid not in out:
                o["_sub"], o["_kw"] = sub, kw
                out[oid] = o
        done += 1
        sys.stderr.write("\r%4d/%d %-18s %-14s objs=%d" % (done, len(plan), sub, kw, len(out)))
        sys.stderr.flush()
        if done % 25 == 0:
            json.dump(list(out.values()),
                      open("/workspace/harvest/raw/_tiera_reddit/arctic_tiera.json", "w",
                           encoding="utf-8"), ensure_ascii=False)
    sys.stderr.write("\n")
    dst = "/workspace/harvest/raw/_tiera_reddit/arctic_tiera.json"
    json.dump(list(out.values()), open(dst, "w", encoding="utf-8"), ensure_ascii=False)
    print("saved %d objects -> %s" % (len(out), dst))


if __name__ == "__main__":
    main()
