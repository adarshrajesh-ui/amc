#!/usr/bin/env python3
"""Second sweep of nowcoder's search API with vocabulary the first pass never tried.

nc_search.py paired each firm with the obvious 面经/笔试/OA suffixes and is now
exhausted — 227 posts, 19 with a firm plus recall language, nearly all already mined.
The terms below are the ones a candidate actually types: 网测 and 手撕 for the test
itself, 暑期实习/2026届/校招 for the cycle, 求米 for the beg-for-karma posts that
carry the longest write-ups, and the Chinese nicknames (光速, 两西, 老任务) that never
appear in the Latin-script queries. Firm list also picks up spellings seen in the
wild: HRT 面经 posts often write 哈德逊, Akuna as 奥可纳.

Reuses nc_search.post so the on-disk cache is shared and nothing is re-requested.
"""
import json
import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor

sys.path.insert(0, "/workspace/harvest/tools")
from nc_search import post  # noqa: E402

OUT = "/workspace/harvest/.nc_cache/_index2.json"

FIRMS = ["Akuna", "奥可纳", "HRT", "哈德逊", "Hudson River Trading", "Jump", "光速",
         "DRW", "Five Rings", "五环", "Old Mission", "老任务", "Two Sigma", "两西",
         "两西格玛", "德劭", "DE Shaw", "Citadel Securities 对比 HRT"]
SUFFIX = ["网测", "手撕", "校招", "暑期实习", "2026届", "2025届", "量化交易员",
          "量化研究员", "挂了", "求米", "hackerrank", "codesignal", "题目", "面试题",
          "实习面经", "秋招"]


def main():
    queries = ["%s %s" % (f, s) for f in FIRMS for s in SUFFIX]
    queries = list(dict.fromkeys(queries))
    print("%d queries" % len(queries), file=sys.stderr)
    found = {}

    def run(q):
        rows = []
        d = post(q, 1)
        data = d.get("data") or {}
        rows.extend(data.get("records") or [])
        for p in range(2, min(int(data.get("totalPage") or 0), 3) + 1):
            rows.extend((post(q, p).get("data") or {}).get("records") or [])
        return q, rows

    with ThreadPoolExecutor(max_workers=6) as ex:
        for q, rows in ex.map(run, queries):
            n = 0
            for r in rows:
                d = r.get("data") or {}
                # Company/job result rows carry a list under "data" instead of an object.
                if not isinstance(d, dict):
                    continue
                cd = d.get("contentData") or d.get("momentData")
                if not cd:
                    continue
                cid, uuid = str(cd.get("id") or ""), cd.get("uuid") or ""
                if r.get("rc_type") == 207 or d.get("contentType") == 250:
                    url = "https://www.nowcoder.com/discuss/%s" % cid
                else:
                    url = "https://www.nowcoder.com/feed/main/detail/%s" % uuid
                if url not in found:
                    ub = d.get("userBrief") or {}
                    found[url] = {"url": url, "title": cd.get("title") or "",
                                  "content": cd.get("content") or "", "queries": [],
                                  "author": ub.get("nickname"),
                                  "edu": ub.get("authDisplayInfo"),
                                  "views": (d.get("frequencyData") or {}).get("viewCnt")}
                    n += 1
                found[url]["queries"].append(q)
            print("  %-32s %3d rows %3d new" % (q, len(rows), n), file=sys.stderr)

    json.dump(found, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    FIRMPAT = re.compile(r"akuna|奥可纳|hrt|哈德逊|hudson\s*river|jump|光速|drw|"
                         r"five\s*rings|五环|old\s*mission|老任务|two\s*sigma|两西|"
                         r"德劭|d\.?e\.?\s*shaw|deshaw", re.I)
    hot = [v for v in found.values() if FIRMPAT.search(v["title"] + " " + v["content"])]
    print("\n%d posts, %d name a shard firm" % (len(found), len(hot)))
    for v in sorted(hot, key=lambda x: -(x["views"] or 0)):
        print("  %-7s %s | %s" % (v["views"], v["url"], v["title"][:70]))


if __name__ == "__main__":
    main()
