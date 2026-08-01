#!/usr/bin/env python3
"""Show what the WSO permalink pages say that the already-mined listing pages did not.

The listing truncates long write-ups, so a permalink can hold several sentences that
never reached the dataset. This prints, per entry, only the sentences whose text is
absent from both the cached listing dumps and every source_quote already recorded —
i.e. the actual new material, so no effort is spent re-reading what is already in.
"""
import glob
import json
import os
import re
import sys

sys.path.insert(0, "/workspace/harvest/tools")
from wso_perm import parse  # noqa: E402

CACHE = "/workspace/harvest/.verify_cache"
DATASET = "/workspace/harvest/raw/tier_a_hrt_jump_drw_others.jsonl"


def norm(s):
    return re.sub(r"\s+", " ", s).strip().lower()


def main():
    want = sys.argv[1] if len(sys.argv) > 1 else ""
    listing = norm(" ".join(
        open(p, encoding="utf-8", errors="replace").read()
        for p in glob.glob(os.path.join(CACHE, "*_company_*_interview.txt"))
        + glob.glob(os.path.join(CACHE, "*_company_*_interview_page_*.txt"))))
    mined = norm(" ".join(json.loads(l)["source_quote"]
                          for l in open(DATASET, encoding="utf-8")))
    shown = 0
    for p in sorted(glob.glob(os.path.join(CACHE, "*_company_*_interview_*.txt"))):
        if "_interview_page_" in p:
            continue
        e = parse(p)
        if not e or (want and want not in e["url"]):
            continue
        fresh = []
        for field in ("narrative", "questions"):
            for sent in re.split(r"(?<=[.?!])\s+|\n", e[field]):
                s = sent.strip()
                if len(s) < 45:
                    continue
                n = norm(s)
                if n in mined:
                    continue
                fresh.append(s + ("" if n in listing else "   [permalink-only]"))
        if not fresh:
            continue
        shown += 1
        print("\n=== %s | %s | %s\n%s" % (e["firm"], e["title"], e["when"], e["url"]))
        for s in fresh:
            print("   + " + s[:700])
    print("\n[%d entries with new text]" % shown, file=sys.stderr)


if __name__ == "__main__":
    main()
