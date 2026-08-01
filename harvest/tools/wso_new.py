#!/usr/bin/env python3
"""Show WSO interview entries whose question text is not yet represented in the
Tier-A JSONL, so the new pagination pages can be mined without re-adding duplicates."""
import glob
import json
import re
import sys

PARTS = "/workspace/harvest/raw/_tier_a_parts/p*.jsonl"


def norm(s):
    s = re.sub(r"\s+", " ", (s or "").lower())
    return re.sub(r"[^a-z0-9\u4e00-\u9fff ]", "", s)


def main():
    have = []
    for p in glob.glob(PARTS):
        for line in open(p, encoding="utf-8"):
            line = line.strip()
            if line:
                o = json.loads(line)
                have.append(norm(o["question_text"]))
    havejoin = " || ".join(have)
    recs = json.load(open("/tmp/wso_all.json", encoding="utf-8"))
    want = sys.argv[1] if len(sys.argv) > 1 else ""
    shown = 0
    for r in recs:
        if want and want.lower() not in r["firm"].lower():
            continue
        q = r["questions"].strip()
        if len(q) < 40:
            continue
        # An entry counts as covered if a decent-length chunk of it is already stored.
        probe = norm(q)[:70]
        if probe and probe in havejoin:
            continue
        shown += 1
        print("=" * 100)
        print("[%d] %s | %s | Interviewed: %s | Submitted: %s | %s" %
              (shown, r["firm"], r["heading"], r["interviewed"], r["submitted"], r["outcome"]))
        print(r["url"])
        print("--narr--", r["narrative"][:900].replace("\n", " "))
        print("--Q--")
        print(q[:1500])
    print("\n%d uncaptured entries" % shown, file=sys.stderr)


if __name__ == "__main__":
    main()
