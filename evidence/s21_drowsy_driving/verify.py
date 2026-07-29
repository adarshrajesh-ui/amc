#!/usr/bin/env python3
"""Verify every DOI against Crossref and every PMID against PubMed for shard s21.

Writes verification_raw.json and prints a one-line-per-identifier report.
"""
import json
import os
import sys
import time
import urllib.parse
import urllib.request

UA = "sleep-debt-factory/1.0 (research; s21_drowsy_driving)"
EU = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
HERE = os.path.dirname(os.path.abspath(__file__))

# study_id -> (doi, pmid)
TARGETS = {
    "tefft2018":        ("10.1093/sleep/zsy144",            "30239905"),
    "tefft2012":        ("10.1016/j.aap.2011.05.028",       "22269499"),
    "connor2002":       ("10.1136/bmj.324.7346.1125",       "12003884"),
    "connor2001":       ("10.1016/s0001-4575(00)00013-0",   "11189120"),
    "bioulac2017":      ("10.1093/sleep/zsx134",            "28958002"),
    "gottlieb2018":     ("10.1186/s12916-018-1025-7",       "29554902"),
    "cummings2001":     ("10.1136/ip.7.3.194",              "11565983"),
    "horne1995":        ("10.1136/bmj.310.6979.565",        "7888930"),
    "martiniuk2013":    ("10.1001/jamapediatrics.2013.1429", "23689363"),
    "owens2019":        ("10.1016/j.jpeds.2018.09.072",     "30392873"),
    "pizza2010":        ("10.5664/jcsm.27708",              "20191936"),
    "wheaton2016":      ("10.15585/mmwr.mm6513a1",          "27054407"),
    "danner2008":       ("10.5664/jcsm.27345",              "19110880"),
    "vorona2011":       ("10.5664/jcsm.28101",              "21509328"),
    "vorona2014":       ("10.5664/jcsm.4192",               "25325600"),
    "foss2019":         ("10.1016/j.aap.2018.03.031",       "29706226"),
    "binhasan2020":     ("10.5664/jcsm.8208",               "31992393"),
    "czeisler2016":     ("10.1016/j.sleh.2016.04.003",      "28923267"),
    "higgins2017":      ("10.1093/sleep/zsx001",            "28364516"),
    "dingus2016":       ("10.1073/pnas.1513271113",         "26903657"),
    # non-indexed grey literature / agency reports: no DOI or PMID exists
    "tefft2016_aaa":    (None, None),
    "owens2018_aaa":    (None, None),
    "tefft2017_aaa":    (None, None),
    "tefft2024_aaa":    (None, None),
    "nhtsa2023_youngdrivers": (None, None),
    "nhtsa_fars_drowsy": (None, None),
    "iihs2023_rates":   (None, None),
    "iihs2024_teens":   (None, None),
    "curtin2020_nchs":  (None, None),
    "ghsa2026":         (None, None),
}


def get(url, as_json=True):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as fh:
                raw = fh.read().decode("utf-8", "replace")
            time.sleep(0.35)
            return json.loads(raw) if as_json else raw
        except Exception as exc:
            if attempt == 3:
                return {"__error__": str(exc)}
            time.sleep(2 ** attempt)


def crossref(doi):
    d = get("https://api.crossref.org/works/" + urllib.parse.quote(doi))
    if not isinstance(d, dict) or "message" not in d:
        return False, None, d
    m = d["message"]
    return True, (m.get("title") or [None])[0], {
        "container": (m.get("container-title") or [None])[0],
        "volume": m.get("volume"), "page": m.get("page"),
        "published": (m.get("published") or {}).get("date-parts"),
        "first_author": ((m.get("author") or [{}])[0] or {}).get("family"),
        "type": m.get("type"),
    }


def pubmed(pmid):
    d = get(EU + "esummary.fcgi?db=pubmed&retmode=json&id=" + pmid)
    try:
        r = d["result"][pmid]
    except Exception:
        return False, None, d
    if "error" in r:
        return False, None, r
    return True, r.get("title"), {
        "source": r.get("source"), "pubdate": r.get("pubdate"),
        "volume": r.get("volume"), "pages": r.get("pages"),
        "ids": [a.get("value") for a in r.get("articleids", [])
                if a.get("idtype") in ("doi", "pmc")],
    }


out = {}
bad = []
for sid in sorted(TARGETS):
    doi, pmid = TARGETS[sid]
    rec = {"doi": doi, "pmid": pmid, "crossref_ok": None, "pubmed_ok": None,
           "crossref_title": None, "pubmed_title": None,
           "crossref_meta": None, "pubmed_meta": None}
    if doi:
        ok, title, meta = crossref(doi)
        rec.update(crossref_ok=ok, crossref_title=title, crossref_meta=meta)
        if not ok:
            bad.append((sid, "crossref", doi))
    if pmid:
        ok, title, meta = pubmed(pmid)
        rec.update(pubmed_ok=ok, pubmed_title=title, pubmed_meta=meta)
        if not ok:
            bad.append((sid, "pubmed", pmid))
    out[sid] = rec
    flag = "GREY_LIT_no_identifier" if not doi and not pmid else ""
    print("%-24s cr=%-5s pm=%-5s %s %s" % (
        sid, rec["crossref_ok"], rec["pubmed_ok"], flag,
        (rec["pubmed_title"] or rec["crossref_title"] or "")[:78]))

with open(os.path.join(HERE, "verification_raw.json"), "w") as fh:
    json.dump(out, fh, indent=1, sort_keys=True)

print("\nfailed identifier lookups: %d" % len(bad))
for b in bad:
    print("  FAIL", b)
sys.exit(1 if bad else 0)
