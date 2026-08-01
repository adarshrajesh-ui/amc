#!/usr/bin/env python3
"""Pull every comment of each cached post that mentions a shard firm.

On reddit the submission is usually the question ("anyone done the HRT OA?") and
the recall is in the replies, so the post-level sweep on its own systematically
misses the evidence. Arctic Shift will return a whole thread by link_id, which is
cheap and exact.
"""
import glob
import json
import os
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor

CACHE = "/workspace/harvest/.reddit_cache"
CDIR = "/workspace/harvest/.reddit_threads"
os.makedirs(CDIR, exist_ok=True)
API = "https://arctic-shift.photon-reddit.com/api/comments/search"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/122 Safari/537.36"

FIRMRE = re.compile(
    r"hudson\s*river|(?<![a-z])hrt(?![a-z])|jump\s*trading|(?<![a-z])drw(?![a-z])|"
    r"five\s*rings|fiverings|akuna|old\s*mission|two\s*sigma|twosigma|"
    r"d\.?\s*e\.?\s*shaw|deshaw", re.I)


def posts():
    seen = {}
    for p in glob.glob(os.path.join(CACHE, "*.json")):
        try:
            d = json.load(open(p, encoding="utf-8"))
        except Exception:
            continue
        for row in (d.get("data") or []):
            # posts carry selftext; comments carry body
            if row.get("selftext") is None:
                continue
            rid = row.get("id")
            blob = (row.get("title") or "") + " " + (row.get("selftext") or "")
            if rid and rid not in seen and FIRMRE.search(blob):
                seen[rid] = row
    return seen


def fetch(rid):
    out = os.path.join(CDIR, rid + ".json")
    if os.path.exists(out):
        return rid, -1
    url = "%s?link_id=t3_%s&limit=100" % (API, rid)
    for attempt in range(4):
        try:
            raw = subprocess.run(["curl", "-s", "--max-time", "60", "--compressed", "-A", UA, url],
                                 capture_output=True, timeout=70).stdout
            d = json.loads(raw.decode("utf-8", "replace"))
        except Exception:
            time.sleep(2 + 3 * attempt)
            continue
        if d.get("data") is not None:
            open(out, "wb").write(raw)
            return rid, len(d["data"])
        time.sleep(2 + 3 * attempt)
    return rid, 0


def main():
    ps = posts()
    print("%d firm-mentioning posts" % len(ps), file=sys.stderr)
    tot = 0
    with ThreadPoolExecutor(max_workers=8) as ex:
        for rid, n in ex.map(fetch, list(ps)):
            if n > 0:
                tot += n
    print("fetched %d new comments across %d threads" % (tot, len(ps)))
    json.dump({k: {"title": v.get("title"), "subreddit": v.get("subreddit"),
                   "permalink": v.get("permalink"), "author": v.get("author"),
                   "created_utc": v.get("created_utc"), "selftext": v.get("selftext")}
               for k, v in ps.items()},
              open(os.path.join(CDIR, "_posts.json"), "w", encoding="utf-8"),
              ensure_ascii=False)


if __name__ == "__main__":
    main()
