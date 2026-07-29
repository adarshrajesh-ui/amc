"""PubMed/Crossref helper for shard s12_psychiatric.

Usage:
  python3 pm.py search "<query>" [retmax]     -> PMID<TAB>year<TAB>journal<TAB>title
  python3 pm.py abs <pmid> [<pmid> ...]       -> full abstract text per PMID
  python3 pm.py doi <DOI>                     -> crossref title/year/journal
  python3 pm.py sum <pmid>                    -> esummary title + doi
"""
from __future__ import annotations

import json
import sys
import time
import urllib.parse
import urllib.request

UA = "sleep-debt-factory/1.0 (research; s12_psychiatric)"
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"


def get(url: str, tries: int = 4) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for i in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=45) as fh:
                return fh.read().decode("utf-8", "replace")
        except Exception as exc:  # noqa: BLE001
            if i == tries - 1:
                return f"__ERROR__ {exc}"
            time.sleep(1.5 * (i + 1))
    return "__ERROR__"


def search(term: str, retmax: int = 15) -> None:
    url = (EUTILS + "esearch.fcgi?db=pubmed&retmode=json&retmax=%d&term=%s"
           % (retmax, urllib.parse.quote(term)))
    raw = get(url)
    try:
        ids = json.loads(raw)["esearchresult"]["idlist"]
    except Exception:
        print(raw[:400])
        return
    if not ids:
        print("NO_HITS\t" + term)
        return
    time.sleep(0.34)
    surl = (EUTILS + "esummary.fcgi?db=pubmed&retmode=json&id=" + ",".join(ids))
    sraw = get(surl)
    try:
        res = json.loads(sraw)["result"]
    except Exception:
        print(sraw[:400])
        return
    for pid in ids:
        r = res.get(pid, {})
        doi = ""
        for aid in r.get("articleids", []):
            if aid.get("idtype") == "doi":
                doi = aid.get("value", "")
        print("\t".join([pid, str(r.get("pubdate", ""))[:4], r.get("source", ""),
                         r.get("title", ""), doi]))


def abstracts(pmids: list[str]) -> None:
    url = (EUTILS + "efetch.fcgi?db=pubmed&rettype=abstract&retmode=text&id=" + ",".join(pmids))
    print(get(url))


def doi_lookup(doi: str) -> None:
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi)
    raw = get(url)
    try:
        m = json.loads(raw)["message"]
    except Exception:
        print("__CROSSREF_FAIL__ " + raw[:200])
        return
    print(json.dumps({
        "title": (m.get("title") or [None])[0],
        "container": (m.get("container-title") or [None])[0],
        "year": (m.get("issued", {}).get("date-parts") or [[None]])[0][0],
        "volume": m.get("volume"), "page": m.get("page"),
        "type": m.get("type"),
        "authors": [f"{a.get('family')} {a.get('given','')[:1]}" for a in m.get("author", [])][:6],
    }, indent=1))


def summary(pmid: str) -> None:
    url = EUTILS + "esummary.fcgi?db=pubmed&retmode=json&id=" + pmid
    raw = get(url)
    try:
        r = json.loads(raw)["result"][pmid]
    except Exception:
        print("__PUBMED_FAIL__ " + raw[:300])
        return
    doi = ""
    for aid in r.get("articleids", []):
        if aid.get("idtype") == "doi":
            doi = aid.get("value", "")
    print(json.dumps({"title": r.get("title"), "source": r.get("source"),
                      "pubdate": r.get("pubdate"), "volume": r.get("volume"),
                      "pages": r.get("pages"), "doi": doi,
                      "authors": [a["name"] for a in r.get("authors", [])][:8]}, indent=1))


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "search":
        search(sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 15)
    elif cmd == "abs":
        abstracts(sys.argv[2:])
    elif cmd == "doi":
        doi_lookup(sys.argv[2])
    elif cmd == "sum":
        summary(sys.argv[2])
