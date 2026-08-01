#!/usr/bin/env python3
"""Third route: Wayback Machine. archive.org rate-limits this host hard, so back off aggressively."""
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from indep_check import norm, longest_common_prefix_frac, strip_html  # noqa: E402

CACHE = "/workspace/harvest/.indep_cache"
os.makedirs(CACHE, exist_ok=True)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
BASE_SLEEP = 20


def _get(url, timeout=45):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    return urllib.request.urlopen(req, timeout=timeout).read().decode("utf-8", "replace")


def polite(url, tries=4):
    delay = BASE_SLEEP
    for i in range(tries):
        try:
            body = _get(url)
            time.sleep(BASE_SLEEP)
            return body
        except urllib.error.HTTPError as e:
            if e.code in (429, 503, 502, 500):
                time.sleep(delay)
                delay = min(delay * 2, 180)
                continue
            return f"__HTTP_{e.code}__"
        except Exception as e:
            time.sleep(delay)
            delay = min(delay * 2, 180)
            last = f"__ERR_{type(e).__name__}__"
    return locals().get("last", "__GAVE_UP__")


def snapshots(url):
    q = urllib.parse.quote(url, safe="")
    body = polite(f"https://web.archive.org/cdx/search/cdx?url={q}&output=json&limit=40&filter=statuscode:200&collapse=timestamp:6")
    if body.startswith("__"):
        return [], body
    try:
        rows = json.loads(body)
    except Exception:
        return [], "__BAD_CDX__"
    return [r[1] for r in rows[1:]], "ok"


def main():
    sample = json.load(open("/workspace/harvest/reports/_sample45.json"))["sample"]
    order = sys.argv[1:]
    rank = {rid: i for i, rid in enumerate(order)}
    sample = sorted((s for s in sample if s["id"] in rank), key=lambda s: rank[s["id"]])
    out = {}
    for s in sample:
        url = s["source_url"]
        stamps, note = snapshots(url)
        print(f"### {s['id']} {url}\n    snapshots={len(stamps)} {stamps[:6]} note={note}", flush=True)
        best = (0.0, 0, None)
        for ts in stamps[-6:][::-1]:
            key = os.path.join(CACHE, "wb_" + hashlib.sha1((ts + url).encode()).hexdigest() + ".txt")
            if os.path.exists(key):
                page = open(key, encoding="utf-8", errors="replace").read()
            else:
                page = polite(f"https://web.archive.org/web/{ts}id_/{url}")
                if not page.startswith("__"):
                    open(key, "w", encoding="utf-8").write(page)
            if page.startswith("__"):
                print(f"    {ts}: {page}", flush=True)
                continue
            txt = strip_html(page)
            frac, n = longest_common_prefix_frac(s["source_quote"], txt)
            print(f"    {ts}: {len(page)}B  prefix={frac:.1%} ({n}/{len(norm(s['source_quote']))})", flush=True)
            if frac > best[0]:
                best = (frac, n, ts)
            if frac >= 1.0:
                break
        out[s["id"]] = {"url": url, "best_frac": best[0], "chars": best[1], "ts": best[2], "n_snapshots": len(stamps)}
        json.dump(out, open("/workspace/harvest/reports/_wayback_probe.json", "w"), indent=1)
    print("WAYBACK_DONE")


if __name__ == "__main__":
    main()
