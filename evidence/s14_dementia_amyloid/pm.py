#!/usr/bin/env python3
"""PubMed / Crossref retrieval helper for shard s14_dementia_amyloid.

Usage:
  python3 pm.py search "query terms" [retmax]      # esearch -> pmid list + titles
  python3 pm.py abs PMID [PMID ...]                # efetch abstract text (saved to <pmid>.txt)
  python3 pm.py sum PMID [PMID ...]                # esummary one-liners
  python3 pm.py doi DOI                            # crossref title/journal/year
"""
import json
import pathlib
import subprocess
import sys
import time
import urllib.parse

HERE = pathlib.Path(__file__).resolve().parent
EUT = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"


def curl(url):
    """NCBI allows 3 req/s without a key; throttle hard and retry on rate-limit."""
    for attempt in range(6):
        time.sleep(0.6)
        p = subprocess.run(["curl", "-sL", "--max-time", "60", url],
                           capture_output=True, text=True)
        out = p.stdout
        if p.returncode == 0 and out.strip() and "API rate limit exceeded" not in out[:200]:
            return out
        time.sleep(2.0 * (attempt + 1))
    return out


def search(term, retmax="20"):
    url = "%s/esearch.fcgi?db=pubmed&retmode=json&retmax=%s&term=%s" % (
        EUT, retmax, urllib.parse.quote(term))
    raw = curl(url)
    try:
        ids = json.loads(raw)["esearchresult"]["idlist"]
    except Exception:
        print("SEARCH FAILED:", raw[:300])
        return []
    print("query: %s  -> %d hits" % (term, len(ids)))
    if ids:
        summarize(ids)
    return ids


def summarize(pmids):
    url = "%s/esummary.fcgi?db=pubmed&retmode=json&id=%s" % (EUT, ",".join(pmids))
    raw = curl(url)
    try:
        res = json.loads(raw)["result"]
    except Exception:
        print("SUMMARY FAILED:", raw[:300])
        return
    for pid in res.get("uids", []):
        r = res[pid]
        doi = ""
        for aid in r.get("articleids", []):
            if aid.get("idtype") == "doi":
                doi = aid["value"]
        print("  %-9s %-30s %-6s %s | DOI %s" % (
            pid, (r.get("fulljournalname") or r.get("source", ""))[:30],
            (r.get("pubdate") or "")[:6], (r.get("title") or "")[:110], doi))


def abstracts(pmids):
    url = "%s/efetch.fcgi?db=pubmed&rettype=abstract&retmode=text&id=%s" % (
        EUT, ",".join(pmids))
    raw = curl(url)
    for pid in pmids:
        pass
    # single-id fetches keep files clean
    if len(pmids) == 1:
        (HERE / ("%s.txt" % pmids[0])).write_text(raw)
    print(raw)


def crossref(doi):
    raw = curl("https://api.crossref.org/works/%s" % urllib.parse.quote(doi, safe=""))
    try:
        m = json.loads(raw)["message"]
    except Exception:
        print("CROSSREF FAIL for %s: %s" % (doi, raw[:200]))
        return None
    print("  DOI %s\n    title: %s\n    journal: %s %s  type=%s" % (
        doi, (m.get("title") or [""])[0],
        (m.get("container-title") or [""])[0],
        m.get("issued", {}).get("date-parts", [[None]])[0][0], m.get("type")))
    return m


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "search":
        search(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else "20")
    elif cmd == "abs":
        abstracts(sys.argv[2:])
    elif cmd == "sum":
        summarize(sys.argv[2:])
    elif cmd == "doi":
        crossref(sys.argv[2])
