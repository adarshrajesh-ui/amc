#!/usr/bin/env python3
"""Rank the fetched reddit comments by how much they look like a question recall.

Scoring is deliberately blunt: a recall verb ("they asked", "the OA was") plus
concrete question vocabulary. Advice posts score low because they talk about
preparation, not about what was on the screen. Prints the parent post title so
each comment can be read in context.
"""
import glob
import json
import os
import re
import sys

CDIR = "/workspace/harvest/.reddit_threads"

FIRMS = {
    "HRT": r"hudson\s*river|(?<![a-z])hrt(?![a-z])",
    "Jump": r"jump\s*trading|(?<![a-z])jump(?![a-z])",
    "DRW": r"(?<![a-z])drw(?![a-z])",
    "FiveRings": r"five\s*rings|fiverings",
    "Akuna": r"akuna",
    "OldMission": r"old\s*mission",
    "TwoSigma": r"two\s*sigma|twosigma",
    "DEShaw": r"d\.?\s*e\.?\s*shaw|deshaw",
}
FIRMRE = {k: re.compile(v, re.I) for k, v in FIRMS.items()}

RECALL = re.compile(
    r"(they asked|asked me|was asked|i got asked|the question was|questions were|"
    r"first question|second question|third question|last question|"
    r"i had to (write|implement|code|find|compute)|they gave me|gave us|"
    r"my oa (was|had)|the oa (was|had|is)|the test (was|had)|oa consisted|"
    r"i remember (the|one|a)|the problem was|the prompt|for me it was|"
    r"i was given|you get (a|an|the)|they had me)", re.I)
CONCRETE = re.compile(
    r"(probability|expected value|\bev\b|market mak|brainteas|dice|coin flip|"
    r"deck of cards|estimate how many|combinator|permutation|regression|markov|"
    r"bayes|binary search|dynamic programming|\bdp\b|linked list|order book|"
    r"\bheap\b|segment tree|mental math|monotonic|prefix sum|two pointer|"
    r"bit manipulation|graph|\btrie\b|sliding window|matrix|interval|"
    r"std::|template|virtual|mutex|cache|latency|zetamac|sequence)", re.I)
STOP = re.compile(r"^\s*(\[removed\]|\[deleted\])\s*$")


def main():
    posts = json.load(open(os.path.join(CDIR, "_posts.json"), encoding="utf-8"))
    out = []
    nc = 0
    for p in glob.glob(os.path.join(CDIR, "*.json")):
        rid = os.path.basename(p)[:-5]
        if rid == "_posts":
            continue
        try:
            rows = json.load(open(p, encoding="utf-8")).get("data") or []
        except Exception:
            continue
        parent = posts.get(rid, {})
        ptitle = parent.get("title") or ""
        for c in rows:
            nc += 1
            body = c.get("body") or ""
            if len(body) < 70 or STOP.match(body):
                continue
            ctx = ptitle + "\n" + body
            firms = [f for f, rx in FIRMRE.items() if rx.search(ctx)]
            if not firms:
                continue
            s = 3 * len(RECALL.findall(body)) + len(set(x.lower() for x in CONCRETE.findall(body)))
            # require the recall verb, otherwise it is speculation or advice
            if not RECALL.search(body) or s < 5:
                continue
            out.append((s, firms, rid, ptitle, c, parent))
    out.sort(key=lambda x: -x[0])
    print("%d comments scanned, %d candidates" % (nc, len(out)), file=sys.stderr)
    lim = int(sys.argv[1]) if len(sys.argv) > 1 else 25
    off = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    for s, firms, rid, ptitle, c, parent in out[off:off + lim]:
        print("\n" + "=" * 100)
        print("score=%d %s r/%s" % (s, ",".join(firms), parent.get("subreddit")))
        print("POST : %s" % ptitle[:110])
        print("LINK : https://www.reddit.com%s" % (parent.get("permalink") or ""))
        print("CMT  : u/%s  %s  id=%s" % (c.get("author"), c.get("created_utc"), c.get("id")))
        print("-" * 100)
        print((c.get("body") or "")[:2200])


if __name__ == "__main__":
    main()
