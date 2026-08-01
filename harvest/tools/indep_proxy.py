#!/usr/bin/env python3
"""Second network path for the Cloudflare-blocked hosts: r.jina.ai text extraction.

Caches each page under .indep_cache/ so re-runs cost nothing.
"""
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from indep_check import norm, longest_common_prefix_frac  # noqa: E402

CACHE = "/workspace/harvest/.indep_cache"
os.makedirs(CACHE, exist_ok=True)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"


def fetch(url, tries=3):
    key = os.path.join(CACHE, hashlib.sha1(url.encode()).hexdigest() + ".txt")
    if os.path.exists(key) and os.path.getsize(key) > 200:
        return open(key, encoding="utf-8", errors="replace").read()
    last = ""
    for i in range(tries):
        try:
            req = urllib.request.Request("https://r.jina.ai/" + url, headers={"User-Agent": UA})
            body = urllib.request.urlopen(req, timeout=75).read().decode("utf-8", "replace")
            if len(body) > 1500 and "Just a moment" not in body[:600]:
                open(key, "w", encoding="utf-8").write(body)
                time.sleep(62)
                return body
            last = "SHORT:" + body[:200]
        except urllib.error.HTTPError as e:
            last = f"HTTP {e.code}"
            if e.code in (401, 402, 451):
                break
        except Exception as e:
            last = f"{type(e).__name__}: {e}"
        time.sleep(45)
    return "__FETCH_FAILED__ " + last


def main():
    sample = json.load(open("/workspace/harvest/reports/_sample45.json"))["sample"]
    order = sys.argv[1:]
    if order:
        rank = {rid: i for i, rid in enumerate(order)}
        sample = sorted((s for s in sample if s["id"] in rank), key=lambda s: rank[s["id"]])
    for s in sample:
        body = fetch(s["source_url"])
        if body.startswith("__FETCH_FAILED__"):
            print(f"{s['id']}  {s['source_type']:14s} FETCH_FAILED {body[:90]}\n  {s['source_url']}\n")
            time.sleep(3)
            continue
        frac, n = longest_common_prefix_frac(s["source_quote"], body)
        nq = norm(s["source_quote"])
        print(f"{s['id']}  {s['source_type']:14s} page={len(body)}B  prefix={frac:.1%} ({n}/{len(nq)})")
        print(f"  {s['source_url']}")
        if frac < 1.0:
            print(f"  matched : ...{nq[max(0, n - 80):n]!r}")
            print(f"  diverges: {nq[n:n + 100]!r}")
        print()
        sys.stdout.flush()


if __name__ == "__main__":
    main()
