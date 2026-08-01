#!/usr/bin/env python3
"""Fetch full comment trees for SIG-relevant Reddit threads from the Arctic Shift archive."""
import json, os, re, sys, time, urllib.parse, urllib.request

BASE = "https://arctic-shift.photon-reddit.com/api"
OUT = "/workspace/harvest/raw/_reddit_cache"
LAST = [0.0]
GAP = 6.0


def get(path, params, tries=5):
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
            time.sleep(6 + 6 * i)
            continue
        try:
            data = json.loads(body)
        except Exception:
            time.sleep(6 + 6 * i)
            continue
        err = str(data.get("error") or "")
        if err:
            time.sleep(8 + 8 * i)
            continue
        return data.get("data") or []
    return None


posts = json.load(open(f"{OUT}/posts.json"))
SIG = re.compile(r"\b(sig|susquehanna|sig's)\b", re.I)
RELEVANT = re.compile(
    r"(OA\b|online assessment|assessment|interview|superday|super ?day|discovery|"
    r"phone screen|recruiter|round|test\b|quiz|prep|question|trading game|"
    r"market making|mental math|intern)", re.I)

PRIORITY = {
    "1gr8l9m", "1n8p8dl", "1mk0za3", "qp1feq", "arlq4z", "dosx14", "1gqjsqn",
    "1nhrzy0", "1t36ww8", "1s6769o", "n18odo", "cu0v9i", "1pe37u6", "1rdmucn",
    "1r0le5a", "1si5ffr", "1pywbwr", "1u4g7cs", "kxc4oo", "10chmq3", "i4ckc2",
    "bvh8fc", "qzezzs", "1t83nef", "1rak5kp", "buobnv",
}

cand = []
for p in posts:
    t = p.get("title") or ""
    b = p.get("selftext") or ""
    if p["id"] not in PRIORITY:
        if not SIG.search(t + " " + b):
            continue
        if not RELEVANT.search(t + " " + b):
            continue
    if (p.get("num_comments") or 0) < 1:
        continue
    score = 100 if p["id"] in PRIORITY else 0
    if SIG.search(t):
        score += 10
    if re.search(r"(OA\b|assessment|interview|superday|super ?day|round|question|test\b|"
                 r"quiz|prep|discovery|math)", t, re.I):
        score += 12
    if re.search(r"(trad(er|ing)|quant|QT\b|intern|market mak|poker|probabilit)", t, re.I):
        score += 8
    if re.search(r"(software|SWE|developer|dev\b|coding|engineer|equity research|"
                 r"growth equity|private equity|sports)", t, re.I):
        score -= 14
    score += min(int(p.get("num_comments") or 0), 80) / 8.0
    cand.append((score, p.get("created_utc") or 0, p["id"], t, p.get("subreddit")))

cand.sort(key=lambda x: (-x[0], -x[1]))
sys.stderr.write(f"candidates: {len(cand)}\n")

try:
    store = json.load(open(f"{OUT}/thread_comments.json"))
except Exception:
    store = {}

for n, (sc, cu, pid, title, sub) in enumerate(cand):
    if pid in store:
        continue
    r = get("comments/search", {"link_id": pid, "limit": 100})
    if r is None:
        sys.stderr.write(f"[fail] {pid} {title[:60]}\n")
        continue
    store[pid] = r
    with open(f"{OUT}/thread_comments.json", "w") as f:
        json.dump(store, f)
    sys.stderr.write(f"[{n}/{len(cand)}] {pid} r/{sub} n={len(r)} :: {title[:70]}\n")

print("threads fetched", len(store))
