"""Verify every DOI against Crossref and every PMID against PubMed esummary.
Writes verification.json used to populate the `verification:` block of each record.
"""
import difflib
import json
import re
import time
import urllib.parse
import urllib.request

RECORDS = [
    ("prather2015_rhinovirus", "26118561", "10.5665/sleep.4968"),
    ("cohen2009_cold", "19139325", "10.1001/archinternmed.2008.505"),
    ("spiegel2002_influenza_vaccine", "12243633", "10.1001/jama.288.12.1471-a"),
    ("prather2012_hepb", "22851802", "10.5665/sleep.1990"),
    ("lange2003_hepa", "14508028", "10.1097/01.psy.0000091382.61178.f1"),
    ("lange2011_memory", "21632713", "10.4049/jimmunol.1100015"),
    ("spiegel2023_vaccine_meta", "36917932", "10.1016/j.cub.2023.02.017"),
    ("irwin2016_inflammation_meta", "26140821", "10.1016/j.biopsych.2015.05.014"),
    ("besedovsky2019_review", "30920354", "10.1152/physrev.00010.2018"),
    ("ballesio2026_experimental_meta", "40474574", "10.1111/jsr.70099"),
    ("pratherleung2016_nhanes", "27064773", "10.1001/jamainternmed.2016.0787"),
    ("patel2012_pneumonia", "22215923", "10.5665/sleep.1594"),
    ("vanleeuwen2009_recovery", "19240794", "10.1371/journal.pone.0004589"),
    ("pejovic2013_recovery", "23941878", "10.1152/ajpendo.00301.2013"),
    ("simpson2016_repeated_recovery", "27263430", "10.1016/j.bbi.2016.06.001"),
    ("benedict2012_h1n1", "22217111", "10.1186/1471-2172-13-1"),
    ("martinezalbert2025_infection", "39842484", "10.1098/rstb.2023.0472"),
    ("forthun2023_gp_infection", "36937728", "10.3389/fpsyt.2023.1033034"),
    ("prather2021_influenza", "32236831", "10.1007/s12529-020-09879-4"),
    ("jaiswal2024_breakthrough", "38409137", "10.1038/s41598-024-53743-4"),
    ("zhang2023_mr_inflammation", "37535878", "10.1093/sleep/zsad207"),
    ("faraut2011_nap_recovery", "20699115", "10.1016/j.bbi.2010.08.001"),
    ("stager2023_adolescent_crp", "37395694", "10.1016/j.jadohealth.2023.05.018"),
    ("fondell2011_nk_tcell", "21496482", "10.1016/j.bbi.2011.04.004"),
    ("moralesmunoz2024_alspac", "38717746", "10.1001/jamapsychiatry.2024.0796"),
]

UA = {"User-Agent": "evidence-extraction/1.0 (mailto:noreply@example.org)"}


def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=45) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


def norm(s):
    return re.sub(r"[^a-z0-9 ]", "", (s or "").lower()).strip()


out = {}
for sid, pmid, doi in RECORDS:
    rec = {"pmid": pmid, "doi": doi, "crossref_ok": None, "pubmed_ok": None,
           "crossref_title": None, "pubmed_title": None, "title_similarity": None}
    try:
        d = get("https://api.crossref.org/works/" + urllib.parse.quote(doi))
        rec["crossref_ok"] = d.get("status") == "ok"
        t = d["message"].get("title") or []
        rec["crossref_title"] = t[0] if t else None
        rec["crossref_journal"] = (d["message"].get("container-title") or [None])[0]
        rec["crossref_year"] = (d["message"].get("published-print")
                                or d["message"].get("published-online")
                                or d["message"].get("issued", {})).get("date-parts", [[None]])[0][0]
    except Exception as e:
        rec["crossref_ok"] = False
        rec["crossref_error"] = str(e)
    time.sleep(0.4)
    try:
        d = get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
                f"?db=pubmed&retmode=json&id={pmid}")
        r = d["result"][pmid]
        rec["pubmed_ok"] = "error" not in r
        rec["pubmed_title"] = r.get("title")
        rec["pubmed_journal"] = r.get("source")
        rec["pubmed_date"] = r.get("pubdate")
        rec["pubmed_doi"] = next((a["value"] for a in r.get("articleids", [])
                                  if a.get("idtype") == "doi"), None)
    except Exception as e:
        rec["pubmed_ok"] = False
        rec["pubmed_error"] = str(e)
    if rec["crossref_title"] and rec["pubmed_title"]:
        rec["title_similarity"] = round(difflib.SequenceMatcher(
            None, norm(rec["crossref_title"]), norm(rec["pubmed_title"])).ratio(), 3)
    rec["doi_match"] = (rec.get("pubmed_doi") or "").lower() == doi.lower()
    rec["status"] = "VERIFIED" if (rec["crossref_ok"] and rec["pubmed_ok"]) else "UNVERIFIED"
    out[sid] = rec
    flag = "OK " if rec["status"] == "VERIFIED" else "!! "
    print(f"{flag}{sid:32s} cr={rec['crossref_ok']} pm={rec['pubmed_ok']} "
          f"doimatch={rec['doi_match']} sim={rec['title_similarity']}")
    print(f"    PM: {rec.get('pubmed_title')}")
    if not rec["doi_match"]:
        print(f"    !! pubmed doi = {rec.get('pubmed_doi')!r} vs asserted {doi!r}")
    time.sleep(0.4)

json.dump(out, open("verification.json", "w"), indent=1)
bad = [k for k, v in out.items() if v["status"] != "VERIFIED"]
print(f"\n{len(out)} checked; UNVERIFIED: {bad or 'none'}")
