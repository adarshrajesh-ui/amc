#!/usr/bin/env python3
"""Shard s08 helper: PubMed search / abstract fetch / Crossref verify.

Usage:
  python3 pm.py search "query terms" [retmax]
  python3 pm.py abs PMID [PMID ...]
  python3 pm.py cr DOI
"""
import json
import sys
import time
import urllib.parse
import urllib.request

UA = "sleep-debt-factory/1.0 (research; s08_cardiovascular)"
EU = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"


def get(url, parse_json=True):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=45) as fh:
                raw = fh.read().decode("utf-8", "replace")
            time.sleep(0.35)
            return json.loads(raw) if parse_json else raw
        except Exception as exc:
            if attempt == 3:
                return {"__error__": str(exc)} if parse_json else f"__error__ {exc}"
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
            print("PMID %s | %s | %s | %s" % (
                i, r.get("pubdate", "?"), r.get("source", "?"), r.get("title", "?")))
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
                   for a in (m.get("author") or [])][:12],
        "type": m.get("type"),
    }, indent=1))


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "search":
        search(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else 20)
    elif cmd == "abs":
        abstracts(sys.argv[2:])
    elif cmd == "cr":
        crossref(sys.argv[2])
