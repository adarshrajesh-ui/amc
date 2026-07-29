#!/usr/bin/env python3
"""Verify (pmid, doi) pairs against PubMed esummary and Crossref. Prints a TSV report."""
import json, sys, time, urllib.parse, urllib.request, difflib

PAIRS = [
    ("28181512", "10.1038/srep41678"),
    ("32015467", "10.1038/s41380-020-0663-2"),
    ("22197742", "10.1016/j.neuroimage.2011.11.072"),
    ("28364462", "10.1093/sleep/zsw022"),
    ("31240728", "10.1111/jcpp.13085"),
    ("37798367", "10.1038/s41562-023-01707-5"),
    ("40086297", "10.1016/j.sleep.2025.02.028"),
    ("28526620", "10.1016/j.neuroimage.2017.05.027"),
    ("26812659", "10.1016/j.neuroimage.2016.01.020"),
    ("35422097", "10.1038/s41398-022-01909-x"),
    ("26020651", "10.1371/journal.pone.0127351"),
    ("24346259", "10.1097/WNR.0000000000000091"),
    ("32903801", "10.3389/fnins.2020.00754"),
    ("41562565", "10.1093/sleep/zsag011"),
    ("39580729", "10.1016/j.jadohealth.2024.10.007"),
    ("36610292", "10.1016/j.dcn.2022.101193"),
    ("35914537", "10.1016/S2352-4642(22)00188-2"),
    ("21037021", "10.1164/rccm.201005-0693OC"),
    ("39998447", "10.1164/rccm.202406-1170OC"),
    ("40244849", "10.1016/j.celrep.2025.115565"),
    ("41794771", "10.1038/s41467-026-70135-6"),
    ("39441640", "10.1073/pnas.2407533121"),
    ("31229687", "10.1016/j.nbd.2019.104517"),
    ("30896191", "10.1037/bne0000312"),
    ("36575851", "10.1002/brb3.2859"),
    ("42509928", "10.3390/children13070903"),
    ("40099522", "10.1093/sleep/zsaf070"),
    ("35714839", "10.1016/j.jaac.2022.06.003"),
    ("16857890", "10.1152/ajpregu.00293.2006"),
    ("26093368", "10.1016/j.dcn.2015.05.007"),
    ("33566829", "10.1371/journal.pone.0243720"),
    ("26065720", "10.1378/chest.15-0171"),
    ("33358980", "10.1016/j.bbi.2020.12.017"),
]

UA = {"User-Agent": "evidence-extraction/1.0 (mailto:noreply@example.org)"}

def get(url, tries=3):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=45) as r:
                return json.load(r)
        except Exception as e:
            if i == tries - 1:
                return {"__err__": str(e)}
            time.sleep(1.5 * (i + 1))

def norm(s):
    return "".join(ch.lower() for ch in (s or "") if ch.isalnum() or ch == " ").strip()

print("PMID\tDOI\tPUBMED_OK\tCROSSREF_OK\tSIM\tRESOLVED_TITLE")
for pmid, doi in PAIRS:
    pm = get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
             f"?db=pubmed&retmode=json&id={pmid}")
    pm_title = pm_doi = ""
    pm_ok = False
    try:
        rec = pm["result"][pmid]
        pm_title = rec.get("title", "")
        for aid in rec.get("articleids", []):
            if aid["idtype"] == "doi":
                pm_doi = aid["value"]
        pm_ok = bool(pm_title)
    except Exception:
        pm_ok = False

    cr = get("https://api.crossref.org/works/" + urllib.parse.quote(doi))
    cr_title = ""
    cr_ok = False
    try:
        cr_title = cr["message"]["title"][0]
        cr_ok = True
    except Exception:
        cr_ok = False

    sim = difflib.SequenceMatcher(None, norm(pm_title), norm(cr_title)).ratio() if (pm_ok and cr_ok) else 0.0
    doi_match = (pm_doi.lower() == doi.lower()) if pm_doi else None
    flag = "" if (pm_ok and cr_ok and sim > 0.85 and doi_match) else "  <<<CHECK"
    print(f"{pmid}\t{doi}\t{pm_ok}\t{cr_ok}\t{sim:.3f}\t{cr_title[:78]}{flag}")
    if doi_match is False:
        print(f"        !! PubMed DOI for {pmid} = {pm_doi}  (differs from {doi})")
    time.sleep(0.34)
