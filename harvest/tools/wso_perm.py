#!/usr/bin/env python3
"""Read the cached WallStreetOasis per-interview permalink pages.

The company listing truncates each write-up; the permalink serves it whole, so these
pages carry text that never appeared on the pages already mined. Layout differs from
the listing: fields are "What did the interview consist of?", "Please describe the
interview / hiring process." and "What were the interview questions?" under an
"Interview Details" heading.

Usage: wso_perm.py [firm-slug-substring] [--new]
"""
import glob
import json
import os
import re
import sys

CACHE = "/workspace/harvest/.verify_cache"
DATASET = "/workspace/harvest/raw/tier_a_hrt_jump_drw_others.jsonl"

FIRM_OF = {
    "hudson-river-trading-llc": "Hudson River Trading", "jump-trading": "Jump Trading",
    "drw": "DRW", "five-rings-capital-llc": "Five Rings", "akuna-capital-llc": "Akuna Capital",
    "old-mission-capital": "Old Mission Capital", "two-sigma-investments": "Two Sigma",
    "de-shaw": "D. E. Shaw",
}
STOP = re.compile(r"\[Add your data to unlock interview\]|Overall Company Rankings|"
                  r"\[Add Your Data\]|Want Access to these")


def parse(path):
    raw = open(path, encoding="utf-8", errors="replace").read()
    m = re.search(r"URL Source:\s*(\S+)", raw)
    url = m.group(1) if m else None
    if not url:
        return None
    slug = re.search(r"/company/([^/]+)/interview/", url)
    firm = FIRM_OF.get(slug.group(1)) if slug else None
    if not firm:
        return None
    head = raw.split("Interview Details", 1)
    if len(head) < 2:
        return None
    body = STOP.split(head[1])[0]
    # The page repeats the title as an H1 above the details block.
    title = re.search(r"\n#\s+([^\n]+)", head[0])
    when = re.search(r"\n\s*([A-Z][a-z]+ 20\d\d)\s*\n", head[0])
    consist = re.search(r"What did the interview consist of\?(.*?)(?=Please describe|What were|\Z)",
                        body, re.S)
    desc = re.search(r"Please describe the interview / hiring process\.(.*?)(?=What were|\Z)",
                     body, re.S)
    ques = re.search(r"What were the interview questions\?(.*?)\Z", body, re.S)

    def clean(m):
        if not m:
            return ""
        t = re.sub(r"!?\[[^\]]*\]\([^)]*\)", " ", m.group(1))
        t = re.sub(r"\n{2,}", "\n", t).strip()
        return re.sub(r"[ \t]{2,}", " ", t)

    return {"firm": firm, "url": url, "title": (title.group(1).strip() if title else "?"),
            "when": when.group(1) if when else "unknown",
            "consist": clean(consist), "narrative": clean(desc), "questions": clean(ques),
            "path": path}


def main():
    want = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else ""
    only_new = "--new" in sys.argv
    done = set()
    if only_new and os.path.exists(DATASET):
        done = {json.loads(l)["source_url"] for l in open(DATASET, encoding="utf-8")}
    n = 0
    for p in sorted(glob.glob(os.path.join(CACHE, "*_company_*_interview_*.txt"))):
        if "_interview_page_" in p:
            continue
        e = parse(p)
        if not e or (want and want not in e["url"]) or (only_new and e["url"] in done):
            continue
        if not (e["narrative"] or e["questions"]):
            continue
        n += 1
        print("\n=== %s | %s | %s\n%s" % (e["firm"], e["title"], e["when"], e["url"]))
        if e["consist"]:
            print("  CONSIST: " + " ".join(e["consist"].split())[:200])
        if e["narrative"]:
            print("  NARRATIVE: " + e["narrative"][:2000])
        if e["questions"]:
            print("  QUESTIONS: " + e["questions"][:1500])
    print("\n[%d shown]" % n, file=sys.stderr)


if __name__ == "__main__":
    main()
