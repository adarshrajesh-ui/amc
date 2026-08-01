#!/usr/bin/env python3
"""Paced one-at-a-time proxy fetch + quote comparison.

r.jina.ai allows roughly one request a minute from this host, so the spacing is
deliberate; the cache means an interrupted run resumes for free.
"""
import hashlib
import json
import os
import sys
import time
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from indep_check import norm, longest_common_prefix_frac  # noqa: E402

CACHE = "/workspace/harvest/.indep_cache"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
SPACING = 78


def main():
    sample = {s["id"]: s for s in json.load(open("/workspace/harvest/reports/_sample45.json"))["sample"]}
    ids = sys.argv[1:]
    for k, rid in enumerate(ids):
        s = sample[rid]
        url = s["source_url"]
        key = os.path.join(CACHE, hashlib.sha1(url.encode()).hexdigest() + ".txt")
        body = None
        if os.path.exists(key) and os.path.getsize(key) > 1500:
            body = open(key, encoding="utf-8", errors="replace").read()
        else:
            for attempt in range(2):
                try:
                    req = urllib.request.Request("https://r.jina.ai/" + url, headers={"User-Agent": UA})
                    got = urllib.request.urlopen(req, timeout=90).read().decode("utf-8", "replace")
                    if len(got) > 1500 and "Just a moment" not in got[:800]:
                        open(key, "w", encoding="utf-8").write(got)
                        body = got
                        break
                except Exception as e:
                    print(f"  {rid} attempt{attempt}: {type(e).__name__} {e}", flush=True)
                time.sleep(SPACING)
        if not body:
            print(f"{rid}  FETCH_FAILED  {url}\n", flush=True)
        else:
            frac, n = longest_common_prefix_frac(s["source_quote"], body)
            nq = norm(s["source_quote"])
            print("=" * 95)
            print(f"{rid}  {s['source_type']}  {len(body)}B  match={frac:.1%} ({n}/{len(nq)})")
            print("  " + url)
            if frac < 1:
                print("   matched :", repr(nq[max(0, n - 80):n]))
                print("   diverges:", repr(nq[n:n + 130]))
                print("   remainder found elsewhere on page:", nq[n:n + 40] in norm(body))
            print(flush=True)
        if k < len(ids) - 1:
            time.sleep(SPACING)


if __name__ == "__main__":
    main()
