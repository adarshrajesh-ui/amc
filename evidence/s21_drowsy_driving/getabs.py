import sys, time, urllib.request, xml.etree.ElementTree as ET

UA = {"User-Agent": "s21_drowsy_driving-extraction/1.0 (evidence extraction; contact: shard s21)"}

def fetch(pmids):
    url = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=xml"
           "&rettype=abstract&id=" + ",".join(pmids))
    req = urllib.request.Request(url, headers=UA)
    return urllib.request.urlopen(req, timeout=60).read()

def main():
    pmids = sys.argv[1:]
    raw = fetch(pmids)
    r = ET.fromstring(raw)
    for a in r.iter("PubmedArticle"):
        pmid = a.findtext(".//PMID")
        ti = a.find(".//ArticleTitle")
        print("=" * 100)
        print("PMID %s" % pmid)
        print("TITLE: %s" % ("".join(ti.itertext()) if ti is not None else None))
        j = a.findtext(".//Journal/Title")
        yr = a.findtext(".//JournalIssue/PubDate/Year") or a.findtext(".//JournalIssue/PubDate/MedlineDate")
        print("JOURNAL: %s (%s)  vol %s issue %s pages %s" % (
            j, yr, a.findtext(".//JournalIssue/Volume"), a.findtext(".//JournalIssue/Issue"),
            a.findtext(".//Pagination/MedlinePgn")))
        auth = []
        for au in a.iter("Author"):
            ln, ini = au.findtext("LastName"), au.findtext("Initials")
            if ln:
                auth.append("%s %s" % (ln, ini or ""))
        print("AUTHORS: %s" % "; ".join(auth))
        for ab in a.iter("AbstractText"):
            lab = ab.get("Label") or ""
            print(("[%s] " % lab if lab else "") + "".join(ab.itertext()))
        gr = [g.text for g in a.iter("Agency")]
        if gr:
            print("GRANTS/AGENCY: %s" % "; ".join(sorted(set(x for x in gr if x))))
        for c in a.iter("CoiStatement"):
            print("COI: %s" % "".join(c.itertext())[:400])

main()
