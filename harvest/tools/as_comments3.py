#!/usr/bin/env python3
"""Third comment pass: SIG-titled threads discovered after the earlier passes built
their candidate lists, ranked so interview/assessment threads go first."""
import json, re, sys, time, urllib.parse, urllib.request

BASE = "https://arctic-shift.photon-reddit.com/api"
OUT = "/workspace/harvest/raw/_reddit_cache"
LAST = [0.0]
GAP = 6.5


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
        if str(data.get("error") or ""):
            time.sleep(8 + 8 * i)
            continue
        return data.get("data") or []
    return None


SIG = re.compile(r"\b(sig|susquehanna|sig's)\b", re.I)
ASSESS = re.compile(r"(OA\b|online assessment|assessment|interview|superday|super ?day|"
                    r"discovery|phone|recruiter|round|test\b|quiz|question|math|"
                    r"trading game|market ?mak|prep)", re.I)
TRADE = re.compile(r"(trad(e|er|ing)|quant|QT\b|intern|poker|probabilit|market)", re.I)
OFFTRACK = re.compile(r"(software|SWE\b|developer|\bdev\b|coding|engineer|equity research|"
                      r"growth equity|private equity|sports|salary|comp\b|pay\b)", re.I)

STORE3 = f"{OUT}/thread_comments3.json"


def load_all():
    """Union of the shared cache and this crawler's own file. Written separately so a
    concurrently running crawler holding a stale in-memory dict cannot clobber it."""
    merged = {}
    for path in (f"{OUT}/thread_comments.json", STORE3):
        try:
            merged.update(json.load(open(path)))
        except Exception:
            pass
    return merged


while True:
    posts = json.load(open(f"{OUT}/posts.json"))
    store = load_all()
    try:
        own = json.load(open(STORE3))
    except Exception:
        own = {}

    cand = []
    for p in posts:
        pid = p["id"]
        if pid in store:
            continue
        if (p.get("num_comments") or 0) < 1:
            continue
        t = p.get("title") or ""
        if not SIG.search(t):
            continue
        s = 0
        if ASSESS.search(t):
            s += 14
        if TRADE.search(t):
            s += 9
        if OFFTRACK.search(t):
            s -= 11
        s += min(int(p.get("num_comments") or 0), 60) / 6.0
        cand.append((s, p.get("created_utc") or 0, pid, t, p.get("subreddit")))
    if not cand:
        break
    cand.sort(key=lambda x: (-x[0], -x[1]))
    sys.stderr.write(f"--- pass over {len(cand)} unfetched SIG-titled threads\n")
    for n, (sc, cu, pid, title, sub) in enumerate(cand):
        if pid in own:
            continue
        r = get("comments/search", {"link_id": pid, "limit": 100})
        if r is None:
            sys.stderr.write(f"[fail] {pid} {title[:60]}\n")
            continue
        own[pid] = r
        with open(STORE3, "w") as f:
            json.dump(own, f)
        sys.stderr.write(f"[{n}/{len(cand)} s={sc:.0f}] {pid} r/{sub} n={len(r)} :: {title[:65]}\n")

print("done")
