#!/usr/bin/env python3
"""Triage the nowcoder search index down to plausible first-person recalls, then
fetch each survivor's permalink so quotes can be verified against a static page.

Nowcoder's firm-name hits are dominated by recruiting posts (内推 / 招聘 / 汇总 /
薪资), which are not evidence of anything. The filter therefore wants a firm
mention AND an experience signal AND no advertisement tell.
"""
import json
import os
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor

IDX = "/workspace/harvest/.nc_cache/_index.json"
CACHE = "/workspace/harvest/.verify_cache"
os.makedirs(CACHE, exist_ok=True)
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/122 Safari/537.36")

FIRM = re.compile(r"akuna|\bhrt\b|hudson\s*river|jump\s*trading|\bdrw\b|five\s*rings|"
                  r"fiverings|old\s*mission|two\s*sigma|twosigma|德劭|d\.?\s*e\.?\s*shaw|"
                  r"deshaw|两西格玛|光速", re.I)
EXP = re.compile(r"面经|笔经|笔试|面试|一面|二面|三面|终面|onsite|OA\b|网测|手撕|挂了|"
                 r"电面|题目|问了|考了|做题|hackerrank|codesignal", re.I)
AD = re.compile(r"内推码|招聘|投递链接|校招汇总|薪资|岗位职责|简历投递|求职群|内推$|"
                r"官网投递|信息汇总|公司名单|资源整理", re.I)


def slug(u):
    return re.sub(r"[^A-Za-z0-9]+", "_", u)[:150]


def fetch(url):
    out = os.path.join(CACHE, slug(url) + ".txt")
    if os.path.exists(out) and os.path.getsize(out) > 20000:
        return url, os.path.getsize(out), True
    for attempt in range(3):
        try:
            subprocess.run(["curl", "-sL", "--max-time", "40", "--compressed", "-A", UA,
                            url, "-o", out], timeout=50)
        except Exception:
            pass
        if os.path.exists(out) and os.path.getsize(out) > 20000:
            return url, os.path.getsize(out), True
        time.sleep(1.5)
    return url, os.path.getsize(out) if os.path.exists(out) else 0, False


def main():
    idx = json.load(open(IDX, encoding="utf-8"))
    keep = []
    for v in idx.values():
        blob = (v["title"] or "") + " " + (v["content"] or "")
        if not FIRM.search(blob):
            continue
        if AD.search(v["title"] or "") and not EXP.search(v["title"] or ""):
            continue
        if not EXP.search(blob):
            continue
        keep.append(v)
    keep.sort(key=lambda x: -(x["views"] or 0))
    print("%d candidates after triage" % len(keep))

    if "--fetch" in sys.argv:
        ok = 0
        with ThreadPoolExecutor(max_workers=5) as ex:
            for url, sz, good in ex.map(fetch, [k["url"] for k in keep]):
                ok += bool(good)
                print("  %-6s %8d %s" % ("OK" if good else "SMALL", sz, url))
        print("fetched %d/%d" % (ok, len(keep)))

    json.dump(keep, open("/workspace/harvest/.nc_cache/_keep.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    for v in keep:
        print("\n=== %s  (%s views)" % (v["url"], v["views"]))
        print("    T: %s" % (v["title"] or "")[:110])
        print("    B: %s" % re.sub(r"\s+", " ", (v["content"] or ""))[:260])


if __name__ == "__main__":
    main()
