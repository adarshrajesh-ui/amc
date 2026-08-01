#!/usr/bin/env python3
"""Stage 2 only: pull full comment trees for the Reddit threads already discovered.

Stage 1's breadth sweep is far slower than its marginal value once the big career subs
are covered, and the actual question recalls live in comments, so this runs the link_id
lookups directly against whatever posts.json already holds.
"""
import json, os, sys, time, urllib.error, urllib.parse, urllib.request

BASE = "https://arctic-shift.photon-reddit.com/api"
OUT = "/workspace/harvest/raw/_tiera_reddit"
LAST = [0.0]
GAP = 2.0


def load(name, default):
    try:
        with open(f"{OUT}/{name}") as f:
            return json.load(f)
    except Exception:
        return default


def get(path, params, tries=4):
    params = dict(params, sort="desc")
    url = f"{BASE}/{path}?{urllib.parse.urlencode(params)}"
    for i in range(tries):
        d = time.time() - LAST[0]
        if d < GAP:
            time.sleep(GAP - d)
        LAST[0] = time.time()
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "quant-research-harvest/1.0"})
            with urllib.request.urlopen(req, timeout=120) as r:
                body = r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            try:
                body = e.read().decode("utf-8", "replace")
            except Exception:
                body = ""
        except Exception as e:
            sys.stderr.write(f"  net{i} {e}\n")
            time.sleep(4 + 4 * i)
            continue
        try:
            data = json.loads(body)
        except Exception:
            time.sleep(4 + 4 * i)
            continue
        err = str(data.get("error") or "")
        if err:
            if "Timeout" in err or "slow down" in err:
                time.sleep(3 + 4 * i)
                continue
            return None
        return data.get("data") or []
    return None


posts = {p["id"]: p for p in load("posts.json", [])}
comments = {c["id"]: c for c in load("comments.json", [])}
done = set(load("done2.json", []))

KEY = ("jane street", "janestreet", "citadel", "optiver", "imc trading",
       "imc ", " imc")
HINT = ("oa", "assessment", "interview", "intern", "test", "round", "question",
        "superday", "hackerrank", "codesignal", "probability", "market",
        "mental math", "sequences", "game", "brainteaser", "brain teaser")

cands = []
for p in posts.values():
    title = (p.get("title") or "")
    blob = (title + " " + (p.get("selftext") or "")).casefold()
    if not any(k in blob for k in KEY):
        continue
    score = sum(1 for h in HINT if h in blob) + 3 * sum(1 for h in HINT if h in title.casefold())
    score += min(int(p.get("num_comments") or 0) // 8, 10)
    if any(k in title.casefold() for k in KEY):
        score += 6
    cands.append((-score, p["id"]))
cands.sort()
sys.stderr.write(f"=== {len(cands)} candidate threads ===\n")


def save():
    with open(f"{OUT}/comments.json", "w") as f:
        json.dump(list(comments.values()), f)
    with open(f"{OUT}/done2.json", "w") as f:
        json.dump(sorted(done), f)


for n, (_, pid) in enumerate(cands):
    key = f"cmts|{pid}"
    if key in done:
        continue
    r = get("comments/search", {"link_id": "t3_" + pid, "limit": 100})
    if r is None:
        sys.stderr.write(f"[cfail {n}] {pid}\n")
        continue
    for x in r:
        comments[x["id"]] = x
    done.add(key)
    if n % 10 == 0:
        sys.stderr.write(f"[c {n}/{len(cands)}] C={len(comments)}\n")
        save()

save()
print("TOTAL comments", len(comments))
