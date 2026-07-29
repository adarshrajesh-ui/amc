#!/usr/bin/env python3
"""Second verification wave: identifiers added after the first pass.
Appends into verification_raw.json."""
import json
import os
import time
import urllib.parse
import urllib.request

UA = "sleep-debt-factory/1.0 (research; s13_mortality)"
EU = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

TARGETS = [
    ("zhao2023", "10.1161/JAHA.122.027832", "36892074"),
    ("chaput2024", "10.1093/sleep/zsae135", "38895883"),
    ("sambou2024", "10.1016/j.jad.2024.01.122", "38262521"),
    ("xiao2019", "10.1016/j.sleh.2019.04.008", "31204307"),
]


def get(url, parse_json=True):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as fh:
                raw = fh.read().decode("utf-8", "replace")
            time.sleep(0.35)
            return json.loads(raw) if parse_json else raw
        except Exception as exc:
            if attempt == 3:
                return {"__error__": str(exc)}
            time.sleep(2 ** attempt)


out = {}
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "verification_raw.json")
if os.path.exists(path):
    out = json.load(open(path))

for sid, doi, pmid in TARGETS:
    rec = {"doi": doi, "pmid": pmid}
    cr = get("https://api.crossref.org/works/" + urllib.parse.quote(doi))
    m = cr.get("message") if isinstance(cr, dict) else None
    rec["crossref_ok"] = bool(m)
    if m:
        rec["crossref_title"] = (m.get("title") or [None])[0]
        rec["crossref_container"] = (m.get("container-title") or [None])[0]
        rec["crossref_year"] = ((m.get("published") or {}).get("date-parts") or [[None]])[0][0]
        au = m.get("author") or []
        rec["crossref_first_author"] = au[0].get("family") if au else None
    ps = get(EU + "esummary.fcgi?db=pubmed&retmode=json&id=" + pmid)
    r = ((ps.get("result") or {}).get(pmid) or {}) if isinstance(ps, dict) else {}
    rec["pubmed_ok"] = bool(r.get("title"))
    rec["pubmed_title"] = r.get("title")
    rec["pubmed_source"] = r.get("source")
    rec["pubmed_date"] = r.get("pubdate")
    pdoi = ""
    for aid in r.get("articleids", []):
        if aid.get("idtype") == "doi":
            pdoi = aid.get("value", "")
    rec["pubmed_doi"] = pdoi
    rec["doi_match"] = pdoi.lower() == doi.lower()
    rec["status"] = "VERIFIED" if (rec["crossref_ok"] and rec["pubmed_ok"] and rec["doi_match"]) else "UNVERIFIED"
    out[sid] = rec
    print("%-14s cr=%-5s pm=%-5s match=%-5s %s | %s" % (
        sid, rec["crossref_ok"], rec["pubmed_ok"], rec["doi_match"], rec["status"],
        (rec.get("pubmed_title") or "")[:80]))

json.dump(out, open(path, "w"), indent=1)
print("total records in verification_raw.json: %d" % len(out))
