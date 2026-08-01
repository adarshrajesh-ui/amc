#!/usr/bin/env python3
"""Nowcoder harvester.

nowcoder.com/search is client-rendered so plain curl returns an empty body, which
is why earlier passes could only reach permalinks someone had already named. But
the page's backing API, POST gw-c.nowcoder.com/api/sparta/pc/search, answers this
box with JSON and carries the post bodies inline. This walks that API over every
firm x Chinese-jargon term pair, then resolves each hit to its permalink so the
quote can be verified against a static URL rather than a search page.

Two content shapes come back:
  rc_type 207 -> data.contentData  -> https://www.nowcoder.com/discuss/<id>
  rc_type 201 -> data.momentData   -> https://www.nowcoder.com/feed/main/detail/<uuid>
"""
import json
import os
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor

CACHE = "/workspace/harvest/.nc_cache"
OUT = "/workspace/harvest/.nc_cache/_index.json"
API = "https://gw-c.nowcoder.com/api/sparta/pc/search"
os.makedirs(CACHE, exist_ok=True)
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/122 Safari/537.36")

FIRMS = ["Akuna", "akuna capital", "HRT", "Hudson River", "hudson river trading",
         "Jump Trading", "jump 量化", "DRW", "Five Rings", "fiverings", "Old Mission",
         "Two Sigma", "twosigma", "德劭", "DE Shaw", "D.E.Shaw", "deshaw", "两西格玛"]
SUFFIX = ["", " 面经", " 笔试", " OA", " 实习", " 量化", " 笔经", " 面试", " 真题"]


def post(query, page):
    key = os.path.join(CACHE, "s_%s_%d.json" % (re.sub(r"[^A-Za-z0-9\u4e00-\u9fff]+", "_", query)[:60], page))
    if os.path.exists(key) and os.path.getsize(key) > 100:
        try:
            return json.load(open(key, encoding="utf-8"))
        except Exception:
            pass
    body = json.dumps({"query": query, "type": "all", "page": page, "pageSize": 20},
                      ensure_ascii=False)
    for attempt in range(3):
        try:
            out = subprocess.run(
                ["curl", "-s", "--max-time", "40", "-X", "POST", API,
                 "-H", "Content-Type: application/json", "-A", UA,
                 "-H", "Referer: https://www.nowcoder.com/", "--data-binary", "@-"],
                input=body.encode("utf-8"), capture_output=True, timeout=50).stdout
            d = json.loads(out.decode("utf-8", "replace"))
            if d.get("success"):
                open(key, "wb").write(out)
                return d
        except Exception:
            pass
        time.sleep(1.5 * (attempt + 1))
    return {}


def harvest():
    queries = []
    for f in FIRMS:
        for s in SUFFIX:
            queries.append((f + s).strip())
    queries = list(dict.fromkeys(queries))
    print("%d queries" % len(queries), file=sys.stderr)

    found = {}

    def run(query):
        rows = []
        d = post(query, 1)
        data = d.get("data") or {}
        tp = min(int(data.get("totalPage") or 0), 5)
        rows.extend(data.get("records") or [])
        for p in range(2, tp + 1):
            d2 = post(query, p)
            rows.extend((d2.get("data") or {}).get("records") or [])
        return query, rows

    with ThreadPoolExecutor(max_workers=6) as ex:
        for query, rows in ex.map(run, queries):
            n = 0
            for r in rows:
                d = r.get("data") or {}
                cd = d.get("contentData") or d.get("momentData")
                if not cd:
                    continue
                cid = str(cd.get("id") or "")
                uuid = cd.get("uuid") or ""
                if r.get("rc_type") == 207 or d.get("contentType") == 250:
                    url = "https://www.nowcoder.com/discuss/%s" % cid
                else:
                    url = "https://www.nowcoder.com/feed/main/detail/%s" % uuid
                title = cd.get("title") or ""
                content = cd.get("content") or ""
                ub = d.get("userBrief") or {}
                key = url
                if key not in found:
                    found[key] = {
                        "url": url, "id": cid, "uuid": uuid, "title": title,
                        "content": content, "queries": [],
                        "author": ub.get("nickname"), "edu": ub.get("authDisplayInfo"),
                        "views": (d.get("frequencyData") or {}).get("viewCnt"),
                    }
                    n += 1
                found[key]["queries"].append(query)
            print("  %-28s %3d rows %3d new" % (query, len(rows), n), file=sys.stderr)

    json.dump(found, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("\n%d distinct nowcoder posts -> %s" % (len(found), OUT))
    # quick relevance triage so the fetch phase is not blind
    FIRMPAT = re.compile(r"akuna|hrt|hudson\s*river|jump|drw|five\s*rings|fiverings|"
                         r"old\s*mission|two\s*sigma|twosigma|德劭|d\.?e\.?\s*shaw|deshaw",
                         re.I)
    hot = [v for v in found.values() if FIRMPAT.search(v["title"] + " " + v["content"])]
    print("%d mention a shard firm in title/body" % len(hot))
    for v in sorted(hot, key=lambda x: -(x["views"] or 0))[:30]:
        print("  %-7s %s | %s" % (v["views"], v["url"], v["title"][:60]))


if __name__ == "__main__":
    harvest()
