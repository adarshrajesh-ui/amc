#!/usr/bin/env python3
"""Parse the cached WallStreetOasis company-interview pages into structured entries.

Each WSO entry is a fixed run of labelled blocks ("Interviewed:", "Interview",
"Interview Questions", then a [Sample Answer](permalink) link). The paginated list URL
is not a stable citation — it reshuffles as new entries are submitted — so every entry
is keyed by its permalink instead, which serves the same text on its own page.

Usage:
  wso_pages.py list                       # one line per entry, all firms
  wso_pages.py show <permalink-substring>  # full text of matching entries
  wso_pages.py firm <slug> [--new]         # entries for one firm, --new hides mined URLs
"""
import glob
import json
import os
import re
import sys

CACHE = "/workspace/harvest/.verify_cache"
DATASET = "/workspace/harvest/raw/tier_a_hrt_jump_drw_others.jsonl"

FIRM_OF = {
    "hudson-river-trading-llc": "Hudson River Trading",
    "jump-trading": "Jump Trading",
    "drw": "DRW",
    "five-rings-capital-llc": "Five Rings",
    "akuna-capital-llc": "Akuna Capital",
    "old-mission-capital": "Old Mission Capital",
    "two-sigma-investments": "Two Sigma",
    "de-shaw": "D. E. Shaw",
}

FIELDS = ("Outcome", "Interview Source", "Length of Process", "Difficulty",
          "Overall Experience", "Compensation", "Interview Questions", "Interview")


def parse_page(path):
    raw = open(path, encoding="utf-8", errors="replace").read()
    slug = re.search(r"_company_(.+?)_interview", os.path.basename(path))
    slug = slug.group(1).replace("_", "-") if slug else "?"
    firm = FIRM_OF.get(slug)
    if not firm:
        return []
    body = raw.split("## Interview Questions & Answers", 1)
    if len(body) < 2:
        return []
    chunks = re.split(r"\n#### ", body[1])[1:]
    out = []
    for ch in chunks:
        title = ch.split("\n", 1)[0].strip()
        if title.startswith(("Unlock", "Pagination")):
            continue
        link = re.search(r"\[Sample Answer\]\((https://[^)]+)\)", ch)
        loc = re.search(r"Anonymous interview candidate in ([^\n]+)", ch)
        when = re.search(r"Interviewed:\s*([^\n]+)", ch)
        subm = re.search(r"Date Submitted:\s*([^\n]+)", ch)
        # The narrative sits between the "Interview" label and "Interview Questions".
        narr = re.search(r"\n\s*Interview\s*\n(.*?)(?=\n\s*Interview Questions\s*\n|\Z)", ch, re.S)
        ques = re.search(r"\n\s*Interview Questions\s*\n(.*?)(?=\n\s*\[Sample Answer\]|\Z)", ch, re.S)

        def clean(m):
            if not m:
                return ""
            t = re.sub(r"\n{2,}", "\n", m.group(1)).strip()
            return re.sub(r"[ \t]+", " ", t)

        out.append({
            "firm": firm, "slug": slug, "title": title,
            "url": link.group(1) if link else None,
            "office": loc.group(1).strip() if loc else "unknown",
            "interviewed": when.group(1).strip() if when else "unknown",
            "submitted": subm.group(1).strip() if subm else "unknown",
            "narrative": clean(narr), "questions": clean(ques),
            "page": path,
        })
    return out


def all_entries():
    seen, out = set(), []
    for p in sorted(glob.glob(os.path.join(CACHE, "https_www_wallstreetoasis_com_company_*interview*.txt"))):
        for e in parse_page(p):
            k = e["url"] or (e["firm"], e["title"], e["interviewed"], e["questions"][:80])
            if k in seen:
                continue
            seen.add(k)
            out.append(e)
    return out


def mined():
    urls = set()
    if os.path.exists(DATASET):
        for line in open(DATASET, encoding="utf-8"):
            urls.add(json.loads(line)["source_url"])
    return urls


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "list"
    ents = all_entries()
    if cmd == "list":
        for e in ents:
            print("%-20s %-42s %-16s q=%-4d n=%-4d %s" % (
                e["firm"], e["title"][:42], e["interviewed"][:16],
                len(e["questions"]), len(e["narrative"]), e["url"]))
        print("\n[%d entries]" % len(ents), file=sys.stderr)
        return
    if cmd == "firm":
        slug = sys.argv[2]
        only_new = "--new" in sys.argv
        done = mined()
        n = 0
        for e in ents:
            if e["slug"] != slug:
                continue
            if only_new and e["url"] in done:
                continue
            if not (e["questions"] or e["narrative"]):
                continue
            n += 1
            print("\n=== %s | %s | interviewed %s | submitted %s | %s\n%s" % (
                e["firm"], e["title"], e["interviewed"], e["submitted"], e["office"], e["url"]))
            if e["narrative"]:
                print("  NARRATIVE: " + e["narrative"][:1600])
            if e["questions"]:
                print("  QUESTIONS: " + e["questions"][:1600])
        print("\n[%d shown]" % n, file=sys.stderr)
        return
    if cmd == "show":
        pat = sys.argv[2]
        for e in ents:
            if pat not in (e["url"] or ""):
                continue
            print(json.dumps(e, ensure_ascii=False, indent=2))
        return


if __name__ == "__main__":
    main()
