#!/usr/bin/env python3
"""Verify every DOI/PMID pair for shard s07_metabolic against Crossref + PubMed."""
import json
import re
import sys
import time
import urllib.parse
import urllib.request

RECORDS = [
    ('beals2026', '10.2337/dc25-2083', '41564347'),
    ('bos2019', '10.3390/jcm8050682', '31096629'),
    ('broussard2012', '10.7326/0003-4819-157-8-201210160-00005', '23070488'),
    ('buxton2010', '10.2337/db09-0699', '20585000'),
    ('buxton2012_fd', '10.1126/scitranslmed.3003200', '22496545'),
    ('cappuccio2010', '10.2337/dc09-1124', '19910503'),
    ('chen2021', '10.1016/j.jadohealth.2020.10.012', '33221190'),
    ('cheung2026', '10.1093/sleep/zsaf339', '41165770'),
    ('dashti2019', '10.1038/s41467-019-08917-4', '30846698'),
    ('depner2019', '10.1016/j.cub.2019.01.069', '30827911'),
    ('dutil2024', '10.1093/sleep/zsad313', '38070132'),
    ('gao2020', '10.3389/fgene.2020.607865', '33384720'),
    ('hartescu2022', '10.1111/jsr.13469', '34459060'),
    ('javaheri2011', '10.1016/j.jpeds.2010.09.080', '21146189'),
    ('killick2015', '10.1111/cen.12747', '25683266'),
    ('klingenberg2013', '10.5665/sleep.2816', '23814346'),
    ('kuroda2025', '10.1111/jdi.70039', '40181521'),
    ('leproult2014', '10.2337/db13-1546', '24458353'),
    ('liu2025', '10.1080/07853890.2024.2447422', '39748566'),
    ('matthews2012', '10.5665/sleep.2112', '23024433'),
    ('nedeltcheva2009', '10.1210/jc.2009-0483', '19567526'),
    ('nedeltcheva2012', '10.1038/oby.2012.97', '22513492'),
    ('ness2019', '10.1152/ajpregu.00336.2018', '30892916'),
    ('shan2015', '10.2337/dc14-2073', '25715415'),
    ('sondrup2022', '10.1016/j.smrv.2022.101594', '35189549'),
    ('spiegel1999', '10.1016/S0140-6736(99)01376-8', '10543671'),
    ('wang2019', '10.1016/j.ypmed.2018.11.019', '30508554'),
    ('wang2025_wsr', '10.1530/EC-25-0191', '40590721'),
    ('yuan2021', '10.3389/fphys.2021.764737', '34744800'),
    ('zuraikat2024', '10.2337/dc23-1156', '37955852'),
]

UA = {"User-Agent": "evidence-extraction/1.0 (mailto:research@example.org)"}


def get(url):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=45) as r:
            return json.load(r)
    except Exception as e:
        return {"__err": str(e)}


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()


def sim(a, b):
    """Token Jaccard on titles."""
    A, B = set(norm(a).split()), set(norm(b).split())
    return round(len(A & B) / max(1, len(A | B)), 3)


out = {}
for sid, doi, pmid in RECORDS:
    row = {"doi": doi, "pmid": pmid}
    cr = get("https://api.crossref.org/works/" + urllib.parse.quote(doi))
    m = cr.get("message") if "__err" not in cr else None
    row["crossref_ok"] = bool(m and m.get("title"))
    row["cr_title"] = (m.get("title") or [None])[0] if m else None
    row["cr_journal"] = (m.get("container-title") or [None])[0] if m else None
    row["cr_year"] = (m.get("issued", {}).get("date-parts") or [[None]])[0][0] if m else None

    pm = get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
             "?db=pubmed&retmode=json&id=" + pmid)
    r = (pm.get("result") or {}).get(pmid, {})
    row["pubmed_ok"] = bool(r.get("title"))
    row["pm_title"] = r.get("title")
    row["pm_journal"] = r.get("source")
    row["pm_doi"] = next((i["value"] for i in r.get("articleids", [])
                          if i["idtype"] == "doi"), None)
    row["doi_matches_pmid"] = (row["pm_doi"] or "").lower() == doi.lower()
    row["title_similarity"] = sim(row["cr_title"], row["pm_title"])
    row["status"] = ("VERIFIED" if row["crossref_ok"] and row["pubmed_ok"]
                     and row["title_similarity"] >= 0.7 else "CHECK")
    out[sid] = row
    print(f"{sid:18s} CR={row['crossref_ok']!s:5s} PM={row['pubmed_ok']!s:5s} "
          f"doi_match={row['doi_matches_pmid']!s:5s} sim={row['title_similarity']:.2f} "
          f"{row['status']:8s} | {row['pm_journal']} {row['cr_year']}")
    if row["status"] != "VERIFIED":
        print(f"    CR: {row['cr_title']}\n    PM: {row['pm_title']}\n    pm_doi={row['pm_doi']}")
    time.sleep(0.34)

json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else "_verify.json", "w"), indent=1)
print("\nVERIFIED:", sum(1 for v in out.values() if v["status"] == "VERIFIED"), "/", len(out))
