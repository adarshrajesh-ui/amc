#!/usr/bin/env python3
"""Scan every cached teamblind thread (post + JSON-LD comment tree) for recalls.

Usage: blind_scan.py <FirmKey> [limit] [offset]
"""
import glob
import os
import re
import sys

sys.path.insert(0, "/workspace/harvest/tools")
from blind_comments import blocks, walk  # noqa: E402

CACHE = "/workspace/harvest/.verify_cache"

FIRMS = {
    "HRT": r"hudson\s*river|(?<![a-z])hrt(?![a-z])",
    "Jump": r"jump\s*trading",
    "DRW": r"(?<![a-z])drw(?![a-z])",
    "FiveRings": r"five\s*rings|fiverings",
    "Akuna": r"akuna",
    "OldMission": r"old\s*mission",
    "TwoSigma": r"two\s*sigma|twosigma",
    "DEShaw": r"d\.?\s*e\.?\s*shaw|deshaw|desco",
}
RECALL = re.compile(
    r"(they asked|asked me|was asked|i got asked|question was|questions were|"
    r"first question|second question|i had to|they gave|my oa|the oa|"
    r"onsite was|round was|screen was|interview was|consisted of|i remember)", re.I)
CONCRETE = re.compile(
    r"(probability|expected value|\bev\b|market mak|brainteas|dice|coin|cards?|"
    r"estimate|combinator|regression|markov|bayes|binary search|dynamic programming|"
    r"\bdp\b|linked list|order book|\bheap\b|mental math|std::|template|virtual|"
    r"mutex|cache|latency|lock|thread|pointer|leetcode|hackerrank|lc \w+|"
    r"sql|pandas|matrix|graph|tree|sort)", re.I)
VENDOR = re.compile(r"interviews?\.chat|prepfully|interviewquery|tryexponent|jobtestprep|"
                    r"quantblueprint|tradermath|tradinginterview|my team built|"
                    r"a tool (i|we) built|dm me to buy|selling", re.I)


def main():
    key = sys.argv[1]
    rx = re.compile(FIRMS[key], re.I)
    lim = int(sys.argv[2]) if len(sys.argv) > 2 else 12
    off = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    hits, seen = [], set()
    for f in glob.glob(os.path.join(CACHE, "https_www_teamblind_com_post_*.txt")):
        raw = open(f, encoding="utf-8", errors="replace").read()
        url = "https://www.teamblind.com/post/" + os.path.basename(f)[:-4].split("_post_")[1].replace("_", "-")
        ents = []
        for b in blocks(raw):
            walk(b, 0, ents)
        if not ents:
            continue
        page = " ".join(e[3] for e in ents)
        if not rx.search(page):
            continue
        for depth, who, date, txt in ents:
            if len(txt) < 55 or VENDOR.search(txt):
                continue
            k = txt[:130]
            if k in seen:
                continue
            seen.add(k)
            if not RECALL.search(txt):
                continue
            s = 3 * len(RECALL.findall(txt)) + len(set(x.lower() for x in CONCRETE.findall(txt)))
            if not rx.search(txt) and not rx.search(ents[0][3]):
                continue
            if s < 4:
                continue
            hits.append((s, url, who, date, depth, txt, ents[0][3][:90]))
    hits.sort(key=lambda x: -x[0])
    print("%s: %d candidates" % (key, len(hits)), file=sys.stderr)
    for s, url, who, date, depth, txt, title in hits[off:off + lim]:
        print("\n" + "=" * 96)
        print("score=%d %s [%s] %s depth=%d" % (s, url, date, who, depth))
        print("OP: %s" % title.replace("\n", " "))
        print("-" * 96)
        print(txt[:1600])


if __name__ == "__main__":
    main()
