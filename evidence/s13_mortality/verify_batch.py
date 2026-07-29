#!/usr/bin/env python3
"""Verify every DOI/PMID this shard intends to cite. Writes verification_raw.json."""
import json
import time
import urllib.parse
import urllib.request

UA = "sleep-debt-factory/1.0 (research; s13_mortality)"
EU = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

TARGETS = [
    ("cappuccio2010", "10.1093/sleep/33.5.585", "20469800"),
    ("liu2017", "10.1016/j.smrv.2016.02.005", "27067616"),
    ("yin2017", "10.1161/JAHA.117.005947", "28889101"),
    ("itani2017", "10.1016/j.sleep.2016.08.006", "27743803"),
    ("jike2018", "10.1016/j.smrv.2017.06.011", "28890167"),
    ("ungvari2025", "10.1007/s11357-025-01592-y", "40072785"),
    ("akerstedt2019", "10.1111/jsr.12712", "29790200"),
    ("akerstedt2017", "10.1007/s10654-017-0297-0", "28856478"),
    ("chaput2026", "10.1093/sleep/zsag193", "42454954"),
    ("saintmaurice2024", "10.1093/sleep/zsad312", "38066693"),
    ("liang2023", "10.1093/gerona/glad108", "37186145"),
    ("windred2024", "10.1093/sleep/zsad253", "37738616"),
    ("li2026", "10.1038/s41467-026-72461-1", "42045198"),
    ("wu2024", "10.1038/s41398-024-02826-x", "38388528"),
    ("zhang2025", "10.1089/rej.2024.0058", "39883542"),
    ("duggan2014", "10.1037/hea0000078", "24588628"),
    ("wang2020", "10.1001/jamanetworkopen.2020.5246", "32442289"),
    ("kurina2013", "10.1016/j.annepidem.2013.03.015", "23622956"),
    ("pienaar2021", "10.1177/0890117121992288", "33567861"),
    ("fernandezmendoza2019", "10.1161/JAHA.119.013043", "31575322"),
    ("svensson2021", "10.1001/jamanetworkopen.2021.22837", "34477853"),
    ("kripke2002", "10.1001/archpsyc.59.2.131", "11825133"),
]


def get(url, parse_json=True):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as fh:
                raw = fh.read().decode("utf-8", "replace")
            time.sleep(0.34)
            return json.loads(raw) if parse_json else raw
        except Exception as exc:
            if attempt == 3:
                return {"__error__": str(exc)}
            time.sleep(2 ** attempt)


def main():
    out = {}
    for sid, doi, pmid in TARGETS:
        rec = {"doi": doi, "pmid": pmid}
        cr = get("https://api.crossref.org/works/" + urllib.parse.quote(doi))
        if "message" in cr:
            m = cr["message"]
            rec["crossref_ok"] = True
            rec["crossref_title"] = (m.get("title") or [""])[0]
            rec["crossref_container"] = (m.get("container-title") or [""])[0]
            rec["crossref_year"] = ((m.get("published") or {}).get("date-parts")
                                    or [[None]])[0][0]
            rec["crossref_first_author"] = (m.get("author") or [{}])[0].get("family")
        else:
            rec["crossref_ok"] = False
            rec["crossref_error"] = str(cr)[:200]

        pm = get(EU + "esummary.fcgi?db=pubmed&retmode=json&id=" + pmid)
        res = (pm.get("result") or {}).get(pmid, {})
        if res and not res.get("error"):
            rec["pubmed_ok"] = True
            rec["pubmed_title"] = res.get("title")
            rec["pubmed_source"] = res.get("source")
            rec["pubmed_date"] = res.get("pubdate")
            rec["pubmed_doi"] = next((a["value"] for a in res.get("articleids", [])
                                      if a.get("idtype") == "doi"), None)
            rec["doi_match"] = (str(rec["pubmed_doi"]).lower() == doi.lower())
        else:
            rec["pubmed_ok"] = False
            rec["pubmed_error"] = str(res)[:200]

        rec["status"] = ("VERIFIED" if rec.get("crossref_ok") and rec.get("pubmed_ok")
                         and rec.get("doi_match") else "CHECK")
        out[sid] = rec
        print("%-22s cr=%-5s pm=%-5s doimatch=%-5s %s | %s" % (
            sid, rec.get("crossref_ok"), rec.get("pubmed_ok"), rec.get("doi_match"),
            rec["status"], str(rec.get("pubmed_title"))[:78]))
    with open("verification_raw.json", "w") as fh:
        json.dump(out, fh, indent=1)
    bad = [k for k, v in out.items() if v["status"] != "VERIFIED"]
    print("\nNOT FULLY VERIFIED: %s" % (bad or "none"))


if __name__ == "__main__":
    main()
