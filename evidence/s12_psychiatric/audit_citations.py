"""Audit every citation string in my YAML records against PubMed esummary.

I fabricated an author list once from memory (wang2024_yrbs). This script checks
every record's first author, journal, year, volume and pages against what PubMed
actually returns, so that class of defect cannot survive in the output.
"""
from __future__ import annotations

import glob
import json
import os
import re
import time
import urllib.request

UA = "sleep-debt-factory/1.0 (research; s12_psychiatric)"
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"


def esummary(pmid: str) -> dict:
    url = EUTILS + "esummary.fcgi?db=pubmed&retmode=json&id=" + pmid
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=45) as fh:
                return json.loads(fh.read().decode("utf-8", "replace"))["result"][pmid]
        except Exception:
            if attempt == 3:
                return {}
            time.sleep(1.5 * (attempt + 1))
    return {}


def field(text: str, key: str) -> str | None:
    m = re.search(r'^%s:\s*"?(.*?)"?\s*$' % key, text, re.M)
    return m.group(1) if m else None


problems: list[str] = []
checked = 0

for path in sorted(glob.glob("/workspace/evidence/s12_psychiatric/*.yaml")):
    text = open(path, encoding="utf-8").read()
    pmid = field(text, "pmid")
    citation = field(text, "citation")
    sid = field(text, "study_id")
    if not pmid or pmid == "null" or not citation:
        print("SKIP  %-18s (no pmid)" % os.path.basename(path))
        continue
    rec = esummary(pmid)
    time.sleep(0.34)
    checked += 1
    if not rec:
        problems.append("%s: esummary FAILED for pmid %s" % (sid, pmid))
        continue

    authors = [a["name"] for a in rec.get("authors", []) if a.get("authtype") == "Author"]
    first = authors[0] if authors else ""
    journal = rec.get("source", "")
    year = str(rec.get("pubdate", ""))[:4]
    vol = rec.get("volume", "")
    pages = rec.get("pages", "")

    flags = []
    # first author surname must appear at the very start of the citation
    surname = first.split()[0] if first else ""
    if surname and not citation.startswith(surname):
        flags.append("first author mismatch: pubmed='%s' citation starts '%s'"
                     % (first, citation[:32]))
    if journal and journal.lower() not in citation.lower():
        flags.append("journal '%s' not in citation" % journal)
    if year and year not in citation:
        flags.append("year %s not in citation" % year)
    if vol and vol not in citation:
        flags.append("volume %s not in citation" % vol)
    if pages and pages.split("-")[0] not in citation:
        flags.append("start page %s not in citation" % pages)

    # every listed author surname in the citation must be a real author of the paper
    cite_head = citation.split(". " + (rec.get("title") or "??")[:18])[0]
    real = {a.split()[0].lower() for a in authors}
    listed = re.findall(r"([A-Z][A-Za-z\u00C0-\u024F'\-]+)\s+[A-Z]{1,3}(?=[,.])", cite_head)
    # a listed token counts as real if it appears anywhere in any author string, so that
    # compound surnames ("Martyn-St James M", "Van Dyk TR") are not false-flagged
    real_blob = " ".join(authors).lower()
    ghosts = [w for w in listed if w.lower() not in real and w.lower() not in real_blob]
    if ghosts:
        flags.append("AUTHORS NOT ON PAPER: %s" % ", ".join(sorted(set(ghosts))))

    status = "OK   " if not flags else "FLAG "
    print("%s %-18s pmid=%-9s n_auth=%-3d %s" % (status, sid, pmid, len(authors),
                                                 "; ".join(flags) if flags else ""))
    if flags:
        problems.append("%s (pmid %s): %s" % (sid, pmid, " | ".join(flags)))

print("\n==== %d records checked, %d with problems ====" % (checked, len(problems)))
for p in problems:
    print(" -", p)
