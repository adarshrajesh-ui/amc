"""Full-text retrieval attempts: Europe PMC (OA), PMC, and Unpaywall-listed OA locations.

Usage:
  python3 ft.py epmc <PMID>          -> Europe PMC fullTextXML if open access
  python3 ft.py oa <DOI>             -> list OA locations from Unpaywall
  python3 ft.py get <URL>            -> raw fetch (text)
"""
from __future__ import annotations

import json
import re
import sys
import urllib.parse
import urllib.request

UA = "sleep-debt-factory/1.0 (research; s12_psychiatric)"


def get(url: str, accept: str = "*/*") -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": accept})
    try:
        with urllib.request.urlopen(req, timeout=60) as fh:
            return fh.read().decode("utf-8", "replace")
    except Exception as exc:  # noqa: BLE001
        return f"__ERROR__ {exc}"


def strip_tags(xml: str) -> str:
    xml = re.sub(r"<(table-wrap|table)\b", r"\n<\1", xml)
    xml = re.sub(r"</(td|th)>", " | ", xml)
    xml = re.sub(r"</(tr|p|title|sec|caption)>", "\n", xml)
    xml = re.sub(r"<[^>]+>", " ", xml)
    xml = xml.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
    xml = re.sub(r"[ \t]+", " ", xml)
    return re.sub(r"\n\s*\n+", "\n", xml).strip()


def epmc(pmid: str) -> None:
    s = get("https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:%s&resultType=core&format=json" % pmid)
    try:
        res = json.loads(s)["resultList"]["result"]
    except Exception:
        print("__SEARCH_FAIL__ " + s[:300])
        return
    if not res:
        print("__NO_RECORD__")
        return
    r = res[0]
    pmcid = r.get("pmcid")
    print("# pmcid=%s isOpenAccess=%s inEPMC=%s" % (pmcid, r.get("isOpenAccess"), r.get("inEPMC")))
    if pmcid and r.get("isOpenAccess") == "Y":
        xml = get("https://www.ebi.ac.uk/europepmc/webservices/rest/%s/fullTextXML" % pmcid)
        if not xml.startswith("__ERROR__"):
            print(strip_tags(xml))
            return
        print(xml[:200])
    if r.get("abstractText"):
        print("## ABSTRACT ONLY")
        print(strip_tags(r["abstractText"]))


def oa(doi: str) -> None:
    s = get("https://api.unpaywall.org/v2/%s?email=research@example.org" % urllib.parse.quote(doi))
    try:
        d = json.loads(s)
    except Exception:
        print("__FAIL__ " + s[:300])
        return
    print(json.dumps({"is_oa": d.get("is_oa"), "title": d.get("title"),
                      "locations": [{"url": l.get("url_for_pdf") or l.get("url"),
                                     "host": l.get("host_type"), "version": l.get("version")}
                                    for l in d.get("oa_locations", [])]}, indent=1))


def pmc(pmcid: str) -> None:
    url = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&retmode=xml&id="
           + pmcid)
    xml = get(url)
    if xml.startswith("__ERROR__"):
        print(xml[:300])
        return
    print(strip_tags(xml))


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "pmc":
        pmc(sys.argv[2])
    elif cmd == "epmc":
        epmc(sys.argv[2])
    elif cmd == "oa":
        oa(sys.argv[2])
    elif cmd == "get":
        out = get(sys.argv[2])
        print(strip_tags(out) if "<" in out[:2000] else out)
