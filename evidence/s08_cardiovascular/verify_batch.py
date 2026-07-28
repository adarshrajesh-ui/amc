#!/usr/bin/env python3
"""Batch-verify the DOI/PMID pairs this shard intends to cite."""
import json
import sys
import time
import urllib.parse
import urllib.request

UA = "sleep-debt-factory/1.0 (research; s08_cardiovascular)"

PAIRS = [
    ("cappuccio2011", "10.1093/eurheartj/ehr007", "21300732"),
    ("yin2017", "10.1161/JAHA.117.005947", "28889101"),
    ("huang2022", "10.3389/fcvm.2022.907990", "36237900"),
    ("kwok2018", "10.1161/JAHA.118.008552", "30371228"),
    ("itani2017", "10.1016/j.sleep.2016.08.006", "27743803"),
    ("wang2022_stroke", "10.1016/j.sleep.2021.11.001", "35245890"),
    ("guo2013_bp", "10.1016/j.sleep.2012.12.001", "23394772"),
    ("wang2012_htn", "10.1038/hr.2012.91", "22763475"),
    ("li2019_htn_dr", "10.1038/s41371-018-0135-1", "30451942"),
    ("gangwisch2006", "10.1161/01.HYP.0000217362.34748.e0", "16585410"),
    ("covassin2021", "10.1161/HYPERTENSIONAHA.121.17622", "34247512"),
    ("vanleeuwen2018", "10.1007/s41105-017-0122-x", "29367834"),
    ("hu2020_bp_rct_ma", "10.1177/0193945919868143", "31455197"),
    ("daghlas2019", "10.1016/j.jacc.2019.07.022", "31488267"),
    ("zhao2025_mr", "10.1136/openhrt-2024-002866", "40086821"),
    ("guo2024_stroke_mr", "10.1212/WNL.0000000000209141", "38350061"),
    ("sands2012_cimt", "10.1161/STROKEAHA.112.660332", "22935396"),
    ("meininger2014", "10.1093/ajh/hpt297", "24487981"),
]


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=45) as fh:
                out = json.loads(fh.read().decode("utf-8", "replace"))
            time.sleep(0.3)
            return out
        except Exception as exc:
            if attempt == 3:
                return {"__error__": str(exc)}
            time.sleep(2 ** attempt)


out = {}
for sid, doi, pmid in PAIRS:
    cr = get("https://api.crossref.org/works/" + urllib.parse.quote(doi))
    cr_ok = "message" in cr and cr.get("status") == "ok"
    cr_title = (cr.get("message", {}).get("title") or [None])[0] if cr_ok else None
    cr_journal = (cr.get("message", {}).get("container-title") or [None])[0] if cr_ok else None

    pm = get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
             "?db=pubmed&retmode=json&id=" + pmid)
    rec = pm.get("result", {}).get(pmid, {}) if "result" in pm else {}
    pm_ok = bool(rec) and "error" not in rec
    pm_title = rec.get("title")
    out[sid] = {"doi": doi, "pmid": pmid, "crossref_ok": cr_ok, "pubmed_ok": pm_ok,
                "crossref_title": cr_title, "crossref_journal": cr_journal,
                "pubmed_title": pm_title, "pubmed_source": rec.get("source"),
                "pubmed_date": rec.get("pubdate"), "volume": rec.get("volume"),
                "issue": rec.get("issue"), "pages": rec.get("pages"),
                "authors": [a.get("name") for a in rec.get("authors", [])][:10]}
    flag = "OK " if (cr_ok and pm_ok) else "!! "
    print("%s%-20s cr=%-5s pm=%-5s | %s | %s" % (
        flag, sid, cr_ok, pm_ok, rec.get("source", "?"), (pm_title or cr_title or "?")[:78]))

json.dump(out, open("verification_raw.json", "w"), indent=1)
print("\nwrote verification_raw.json;  n_ok=%d / %d" % (
    sum(1 for v in out.values() if v["crossref_ok"] and v["pubmed_ok"]), len(PAIRS)))
