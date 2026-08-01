#!/usr/bin/env python3
"""Fetch the r/quant 'Weekly Megathread: Education, Early Career and Hiring/Interview
Advice' comment trees. These are where the subreddit's moderators send every OA and
interview question, so SIG recalls end up in threads whose titles never say SIG."""
import json, re, sys, time, urllib.parse, urllib.request

BASE = "https://arctic-shift.photon-reddit.com/api"
OUT = "/workspace/harvest/raw/_reddit_cache"
STORE = f"{OUT}/mega_comments.json"
LAST = [0.0]
GAP = 6.5


def get(params, tries=6):
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
            time.sleep(8 + 8 * i)
            continue
        try:
            data = json.loads(body)
        except Exception:
            time.sleep(8 + 8 * i)
            continue
        if str(data.get("error") or ""):
            time.sleep(10 + 10 * i)
            continue
        return data.get("data") or []
    return None


posts = json.load(open(f"{OUT}/mega_posts.json"))
cand = [p for p in posts
        if p.get("subreddit") in ("quant", "FinancialCareers", "csMajors")
        and re.search(r"(megathread|weekly)", p.get("title") or "", re.I)
        and re.search(r"(hiring|interview|career|education|advice|weekly)",
                      p.get("title") or "", re.I)
        and (p.get("num_comments") or 0) >= 2]
cand.sort(key=lambda p: -(p.get("created_utc") or 0))
sys.stderr.write(f"targets: {len(cand)}\n")

try:
    store = json.load(open(STORE))
except Exception:
    store = {}

SIG = re.compile(r"\b(sig|susquehanna)\b", re.I)
total_hits = 0
for n, p in enumerate(cand):
    pid = p["id"]
    if pid in store:
        continue
    r = get({"link_id": pid, "limit": 100})
    if r is None:
        sys.stderr.write(f"[fail] {pid}\n")
        continue
    store[pid] = r
    with open(STORE, "w") as f:
        json.dump(store, f)
    hits = sum(1 for c in r if SIG.search(c.get("body") or ""))
    total_hits += hits
    flag = "  <<< SIG" if hits else ""
    sys.stderr.write(f"[{n}/{len(cand)}] {pid} r/{p.get('subreddit')} n={len(r)} "
                     f"sig={hits} cum={total_hits}{flag}\n")

print("done", len(store), "sig hits", total_hits)
