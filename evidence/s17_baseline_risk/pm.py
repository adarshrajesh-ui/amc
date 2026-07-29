"""PubMed / Crossref helper with on-disk cache."""
import json, os, re, sys, time, urllib.parse, urllib.request

CACHE = "/tmp/s17/cache"
os.makedirs(CACHE, exist_ok=True)
UA = "sleep-debt-factory-s17/1.0 (research)"


def _fetch(url, binary=False):
    key = os.path.join(CACHE, re.sub(r"[^A-Za-z0-9]", "_", url)[-180:])
    if os.path.exists(key):
        return open(key, "rb").read() if binary else open(key, encoding="utf-8", errors="replace").read()
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for a in range(4):
        try:
            with urllib.request.urlopen(req, timeout=45) as fh:
                data = fh.read()
            break
        except Exception as e:
            if a == 3:
                return f"__ERROR__ {e}"
            time.sleep(1.5 * (a + 1))
    open(key, "wb").write(data)
    time.sleep(0.34)
    return data if binary else data.decode("utf-8", "replace")


def search(term, retmax=12):
    u = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json"
         f"&retmax={retmax}&term=" + urllib.parse.quote(term))
    r = _fetch(u)
    if r.startswith("__ERROR__"):
        print(r); return []
    return json.loads(r)["esearchresult"].get("idlist", [])


def summary(pmids):
    if not pmids:
        return {}
    u = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id="
         + ",".join(pmids))
    r = _fetch(u)
    if r.startswith("__ERROR__"):
        print(r); return {}
    d = json.loads(r).get("result", {})
    out = {}
    for p in pmids:
        rec = d.get(p)
        if not rec or "error" in rec:
            continue
        doi = next((x["value"] for x in rec.get("articleids", []) if x["idtype"] == "doi"), None)
        out[p] = {"title": rec.get("title", ""), "journal": rec.get("source"),
                  "date": rec.get("pubdate"), "doi": doi,
                  "vol": rec.get("volume"), "issue": rec.get("issue"), "pages": rec.get("pages"),
                  "authors": [a["name"] for a in rec.get("authors", [])][:8]}
    return out


def abstract(pmid):
    u = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=text"
         f"&rettype=abstract&id={pmid}")
    return _fetch(u)


def show(term, retmax=12):
    ids = search(term, retmax)
    s = summary(ids)
    print(f"### {term}  -> {len(ids)} hits")
    for p in ids:
        r = s.get(p)
        if not r:
            print(f"  {p}: <no summary>"); continue
        print(f"  {p} | {r['journal']} {r['date']} | doi={r['doi']}")
        print(f"      {r['title'][:150]}")
    return ids


if __name__ == "__main__":
    for t in sys.argv[1:]:
        show(t)
        print()
