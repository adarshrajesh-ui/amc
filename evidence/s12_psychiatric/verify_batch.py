"""Verify every (study_id, doi, pmid) triple I intend to use, against Crossref and PubMed."""
from __future__ import annotations

import json
import time
import urllib.parse
import urllib.request

UA = "sleep-debt-factory/1.0 (research; s12_psychiatric)"

TARGETS = [
    ("zhai2015", "10.1002/da.22386", "26047492"),
    ("lovato2014", "10.1016/j.smrv.2014.03.006", "24857255"),
    ("chiu2018", "10.1016/j.smrv.2018.07.003", "30093362"),
    ("hertenstein2019", "10.1016/j.smrv.2018.10.006", "30537570"),
    ("marino2021", "10.1001/jamanetworkopen.2021.2373", "33749768"),
    ("short2020", "10.1016/j.smrv.2020.101311", "32240932"),
    ("winsler2015", "10.1007/s10964-014-0170-3", "25178930"),
    ("gangwisch2010", "10.1093/sleep/33.1.97", "20120626"),
    ("wang2024_yrbs", "10.1016/j.jadohealth.2024.01.030", "38506779"),
    ("baum2014", "10.1111/jcpp.12125", "24889207"),
    ("short2015", "10.1016/j.sleep.2015.03.007", "26141007"),
    ("palmer2024", "10.1037/bul0000410", "38127505"),
    ("vandyk2017", "10.1093/sleep/zsx123", "28934531"),
    ("lowe2017", "10.1016/j.neubiorev.2017.07.010", "28757454"),
    ("pilcher1996", "10.1093/sleep/19.4.318", "8776790"),
    ("freeman2017", "10.1016/S2215-0366(17)30328-0", "28888927"),
    ("scott2021", "10.1016/j.smrv.2021.101556", "34607184"),
    ("gee2019", "10.1016/j.smrv.2018.09.004", "30579141"),
    ("gebara2018", "10.1002/da.22776", "29782076"),
    ("blake2017", "10.1007/s10567-017-0234-5", "28331991"),
    ("blake2016_sense", "10.1037/ccp0000142", "27775416"),
    ("cai2021_mr", "10.1016/j.gene.2020.145271", "33122081"),
    ("sun2022_mr", "10.1017/S2045796021000810", "35465862"),
    ("gao2019_mr", "10.1016/j.eurpsy.2019.05.004", "31234011"),
    ("daghlas2021_mr", "10.1001/jamapsychiatry.2021.0959", "34037671"),
    ("zhang2024_mr", "10.1016/j.jad.2024.08.068", "39153551"),
    ("roberts2014", "10.5665/sleep.3388", "24497652"),
    ("alvaro2013", "10.5665/sleep.2810", "23814343"),
    ("conklin2018_basus", "10.1186/s12889-018-5656-6", "29890964"),
    ("motomura2013", "10.1371/journal.pone.0056578", "23418586"),
    ("yoo2007", "10.1016/j.cub.2007.08.007", "17956744"),
    ("twenge2019", "10.1037/abn0000410", "30869927"),
    ("goodwin2022", "10.1016/j.amepre.2022.05.014", "36272761"),
    ("kok2026", "10.1093/sleep/zsaf414", "41499144"),
]


def get(url: str) -> dict | None:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    for i in range(3):
        try:
            with urllib.request.urlopen(req, timeout=45) as fh:
                return json.loads(fh.read().decode("utf-8", "replace"))
        except Exception:
            time.sleep(1.2 * (i + 1))
    return None


out = []
for sid, doi, pmid in TARGETS:
    cr = get("https://api.crossref.org/works/" + urllib.parse.quote(doi)) if doi else None
    cr_title = None
    cr_ok = False
    if cr and cr.get("status") == "ok":
        cr_ok = True
        cr_title = (cr["message"].get("title") or [None])[0]
    pm = get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id=" + pmid)
    pm_title, pm_ok, pm_doi = None, False, None
    if pm:
        rec = pm.get("result", {}).get(pmid)
        if rec and "error" not in rec:
            pm_ok = True
            pm_title = rec.get("title")
            for aid in rec.get("articleids", []):
                if aid.get("idtype") == "doi":
                    pm_doi = aid.get("value")
    doi_match = (pm_doi or "").lower() == (doi or "").lower()
    out.append({"study_id": sid, "doi": doi, "pmid": pmid, "crossref_ok": cr_ok,
                "pubmed_ok": pm_ok, "pubmed_doi": pm_doi, "doi_matches_pmid": doi_match,
                "crossref_title": cr_title, "pubmed_title": pm_title})
    flag = "OK " if (cr_ok and pm_ok and doi_match) else "!! "
    print(flag, sid, "cr=%s pm=%s doi_match=%s" % (cr_ok, pm_ok, doi_match))
    print("     ", (cr_title or pm_title or "NO TITLE")[:120])
    time.sleep(0.2)

json.dump(out, open("verification_raw.json", "w"), indent=1)
bad = [r for r in out if not (r["crossref_ok"] and r["pubmed_ok"] and r["doi_matches_pmid"])]
print("\n%d/%d fully verified; %d flagged" % (len(out) - len(bad), len(out), len(bad)))
for r in bad:
    print("  FLAG:", r["study_id"], r["doi"], r["pmid"], "pubmed_doi=", r["pubmed_doi"])
