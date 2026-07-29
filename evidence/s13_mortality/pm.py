#!/usr/bin/env python3
"""Shard s13_mortality helper: PubMed search / abstract fetch / Crossref verify / EuropePMC full text.

Usage:
  python3 pm.py search "query terms" [retmax]
  python3 pm.py abs PMID [PMID ...]
  python3 pm.py cr DOI
  python3 pm.py epmc "query" [pageSize]
  python3 pm.py ft PMCID           # Europe PMC full text XML -> stdout
"""
import json
import sys
import time
import urllib.parse
import urllib.request

UA = "sleep-debt-factory/1.0 (research; s13_mortality)"
EU = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/"


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
                return {"__error__": str(exc)} if parse_json else "__error__ %s" % exc
            time.sleep(2 ** attempt)


def search(term, retmax=20):
    url = (EU + "esearch.fcgi?db=pubmed&retmode=json&retmax=%d&term=" % int(retmax)
           + urllib.parse.quote(term))
    data = get(url)
    ids = data.get("esearchresult", {}).get("idlist", [])
    print("QUERY: %s\nCOUNT: %s\nIDS: %s\n" % (
        term, data.get("esearchresult", {}).get("count"), ",".join(ids)))
    if ids:
        summ = get(EU + "esummary.fcgi?db=pubmed&retmode=json&id=" + ",".join(ids))
        res = summ.get("result", {})
        for i in ids:
            r = res.get(i, {})
            doi = ""
            for aid in r.get("articleids", []):
                if aid.get("idtype") == "doi":
                    doi = aid.get("value", "")
            print("PMID %s | %s | %s | doi:%s | %s" % (
                i, r.get("pubdate", "?"), r.get("source", "?"), doi, r.get("title", "?")))
    return ids


def abstracts(pmids):
    url = (EU + "efetch.fcgi?db=pubmed&retmode=text&rettype=abstract&id="
           + ",".join(pmids))
    print(get(url, parse_json=False))


def crossref(doi):
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi)
    d = get(url)
    if "message" not in d:
        print("CROSSREF FAIL for %s: %s" % (doi, json.dumps(d)[:300]))
        return
    m = d["message"]
    print(json.dumps({
        "DOI": m.get("DOI"),
        "title": m.get("title"),
        "container": m.get("container-title"),
        "volume": m.get("volume"),
        "issue": m.get("issue"),
        "page": m.get("page"),
        "published": (m.get("published") or {}).get("date-parts"),
        "author": [" ".join(filter(None, [a.get("family"), a.get("given")]))
                   for a in (m.get("author") or [])][:14],
        "type": m.get("type"),
    }, indent=1))


def epmc(query, page=25):
    url = (EPMC + "search?format=json&pageSize=%d&resultType=core&query=" % int(page)
           + urllib.parse.quote(query))
    d = get(url)
    res = (d.get("resultList") or {}).get("result", [])
    print("EPMC QUERY: %s | hits=%s | shown=%d" % (query, d.get("hitCount"), len(res)))
    for r in res:
        print("- pmid:%s pmcid:%s doi:%s | %s %s | OA:%s inEPMC:%s | %s" % (
            r.get("pmid"), r.get("pmcid"), r.get("doi"), r.get("journalTitle", "?"),
            r.get("pubYear", "?"), r.get("isOpenAccess"), r.get("inEPMC"),
            r.get("title", "?")))


def fulltext(pmcid):
    url = EPMC + "%s/fullTextXML" % pmcid
    print(get(url, parse_json=False))


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "search":
        search(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else 20)
    elif cmd == "abs":
        abstracts(sys.argv[2:])
    elif cmd == "cr":
        crossref(sys.argv[2])
    elif cmd == "epmc":
        epmc(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else 25)
    elif cmd == "ft":
        fulltext(sys.argv[2])
