#!/usr/bin/env python3
"""Verify every DOI/PMID this shard uses, against Crossref and PubMed. Writes verification_raw.json."""
import difflib
import json
import pathlib
import re
import subprocess
import time
import urllib.parse

HERE = pathlib.Path(__file__).resolve().parent

# study_id -> (pmid, doi)
RECORDS = {
    "xie2013":            ("24136970", "10.1126/science.1241224"),
    "miao2024":           ("38741022", "10.1038/s41593-024-01638-y"),
    "shokrikojori2018":   ("29632177", "10.1073/pnas.1721694115"),
    "ooms2014":           ("24887018", "10.1001/jamaneurol.2014.1173"),
    "forsberg2025":       ("40830882", "10.1186/s12987-025-00698-x"),
    "lucey2018":          ("29220873", "10.1002/ana.25117"),
    "blattner2020":          ("32250301", "10.3233/JAD-191122"),
    "ju2017":             ("28899014", "10.1093/brain/awx148"),
    "kang2009":           ("19779148", "10.1126/science.1180962"),
    "sabia2021":          ("33879784", "10.1038/s41467-021-22354-2"),
    "bubu2017":           ("28364458", "10.1093/sleep/zsw032"),
    "fan2019":            ("31604673", "10.1016/j.jamda.2019.06.009"),
    "xu2020":             ("31879285", "10.1136/jnnp-2019-321896"),
    "wu2018":             ("28589251", "10.1007/s11325-017-1527-0"),
    "liang2019":          ("30039452", "10.1007/s40520-018-1005-y"),
    "howard2024":         ("39442346", "10.1016/j.sleep.2024.10.022"),
    "howard2024_corr":    ("40022863", "10.1016/j.sleep.2025.02.039"),
    "vanwanrooij2025":    ("39863328", "10.1016/j.tjpad.2024.100024"),
    "anderson2021":       ("33150399", "10.1093/ije/dyaa183"),
    "huang2020":          ("32817390", "10.1212/WNL.0000000000010463"),
    "henry2019":          ("31062029", "10.1093/ije/dyz071"),
    "guo2024":            ("38350061", "10.1212/WNL.0000000000209141"),
    "yuan2022":           ("35918656", "10.1186/s12877-022-03298-8"),
    "spira2013":          ("24145859", "10.1001/jamaneurol.2013.4258"),
    "spira2018":          ("30192978", "10.1093/sleep/zsy152"),
    "olsson2018":         ("29425372", "10.1093/sleep/zsy025"),
    "winer2020":          ("32888482", "10.1016/j.cub.2020.08.017"),
    "winer2021":          ("34459862", "10.1001/jamaneurol.2021.2876"),
    "lucey2019":          ("30626715", "10.1126/scitranslmed.aau6550"),
    "deckers2024":        ("38159267", "10.1002/alz.13577"),
    "skorucak2021":       ("33893807", "10.1093/sleep/zsab106"),
    "you2024":            ("38678085", "10.1038/s41380-024-02570-0"),
    "livingston2024":     ("39096926", "10.1016/S0140-6736(24)01296-0"),
    "komlo2026":          ("41959309", "10.64898/2026.03.26.714554"),
    "xiang2024":     ("38865787", "10.1016/j.sleep.2024.06.007"),
    "xiong2024":       ("38301285", "10.1016/j.psychres.2024.115760"),
    "sun2026":       ("41854616", "10.1001/jamanetworkopen.2026.1521"),
    "tao2026":            ("42498182", "10.1016/j.neures.2026.105095"),
    "tortcolet2026":     ("41998740", "10.1186/s13195-026-02049-w"),
    "park2025":           ("41614054", "10.12688/wellcomeopenres.23541.2"),
}


def curl(url, tries=5):
    out = ""
    for i in range(tries):
        time.sleep(0.6)
        p = subprocess.run(["curl", "-s", "--max-time", "60", url],
                           capture_output=True, text=True)
        out = p.stdout
        if p.returncode == 0 and out.strip() and "API rate limit" not in out[:200]:
            return out
        time.sleep(2.0 * (i + 1))
    return out


def norm(s):
    return re.sub(r"[^a-z0-9 ]", "", (s or "").lower()).strip()


results = {}
lines = []
for sid, (pmid, doi) in RECORDS.items():
    rec = {"pmid": pmid, "doi": doi}
    # --- PubMed ---
    raw = curl("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
               "?db=pubmed&retmode=json&id=%s" % pmid)
    pm_title = pm_doi = None
    try:
        d = json.loads(raw)["result"]
        u = d["uids"][0]
        pm_title = d[u].get("title")
        for a in d[u].get("articleids", []):
            if a.get("idtype") == "doi":
                pm_doi = a["value"]
        rec["pubmed_ok"] = bool(pm_title)
        rec["pubmed_title"] = pm_title
        rec["pubmed_doi"] = pm_doi
        rec["pubmed_journal"] = d[u].get("fulljournalname")
        rec["pubmed_pubdate"] = d[u].get("pubdate")
    except Exception as e:
        rec["pubmed_ok"] = False
        rec["pubmed_error"] = str(e)[:120]
    # --- Crossref ---
    raw = curl("https://api.crossref.org/works/%s" % urllib.parse.quote(doi, safe=""))
    try:
        m = json.loads(raw)["message"]
        cr_title = (m.get("title") or [""])[0]
        rec["crossref_ok"] = True
        rec["crossref_title"] = cr_title
        rec["crossref_journal"] = (m.get("container-title") or [""])[0]
        rec["crossref_year"] = m.get("issued", {}).get("date-parts", [[None]])[0][0]
    except Exception as e:
        rec["crossref_ok"] = False
        rec["crossref_error"] = str(e)[:120]
        cr_title = ""
    # --- agreement ---
    if pm_title and cr_title:
        rec["title_similarity"] = round(
            difflib.SequenceMatcher(None, norm(pm_title), norm(cr_title)).ratio(), 3)
    else:
        rec["title_similarity"] = None
    rec["doi_matches_pubmed"] = (
        None if not pm_doi else pm_doi.lower() == doi.lower())
    rec["status"] = ("VERIFIED" if rec.get("pubmed_ok") and rec.get("crossref_ok")
                     and (rec["doi_matches_pubmed"] is not False)
                     and (rec["title_similarity"] is None or rec["title_similarity"] > 0.85)
                     else "UNVERIFIED")
    # Some journals register the main title only, dropping the subtitle after the colon.
    # A Crossref title that is an exact prefix of the PubMed title, with a matching DOI,
    # is the same article, not a mismatch.
    if rec["status"] != "VERIFIED" and rec.get("crossref_ok") and rec["doi_matches_pubmed"]:
        p, c = norm(pm_title), norm(cr_title)
        if c and p.startswith(c):
            rec["status"] = "VERIFIED"
            rec["note"] = ("Crossref registered the title without its subtitle (journal house "
                           "style); the Crossref title is an exact prefix of the PubMed title "
                           "and the DOI recorded in PubMed matches. Treated as verified.")
    results[sid] = rec
    line = "%-20s pm=%-5s cr=%-5s doi_match=%-5s sim=%-6s %s | %s" % (
        sid, rec.get("pubmed_ok"), rec.get("crossref_ok"), rec["doi_matches_pubmed"],
        rec["title_similarity"], rec["status"], (pm_title or "")[:60])
    lines.append(line)
    print(line)

(HERE / "verification_raw.json").write_text(json.dumps(results, indent=1))
bad = [k for k, v in results.items() if v["status"] != "VERIFIED"]
summary = "\n%d/%d VERIFIED. Failures: %s" % (len(results) - len(bad), len(results), bad or "none")
print(summary)
# Emit the human-readable log from the SAME run that wrote the JSON, so the two
# reproducibility artefacts can never drift apart.
(HERE / "verify_out.txt").write_text("\n".join(lines) + "\n" + summary + "\n")
