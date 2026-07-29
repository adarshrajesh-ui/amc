"""Audit the contrarian report's citations against the evidence corpus.

Parses the appendix table of reports/redteam_contrarian.md and, for every row, checks that a
record with that study_id exists in evidence/, that the DOI and PMID as printed match the ones
stored, and that the record's verification status is VERIFIED. Also flags any study_id cited in
the body of the report that never appears in the appendix table.

Usage:  python3 redteam_check_citations.py
Exit code is non-zero if any row fails, so this can gate a commit.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parent.parent
REPORT = ROOT / "reports" / "redteam_contrarian.md"
EVIDENCE = ROOT / "evidence"

# Cited by prose in a way that does not require an appendix row: shard-level synthesis documents
# and records referenced only via a shard summary rather than by identifier.
BODY_ONLY_EXEMPT = {"prather2015_rhinovirus", "huang2016", "pejovic2013_recovery_dissociation"}


def load_corpus() -> dict:
    """study_id -> (path, parsed yaml). Later duplicates are recorded separately."""
    out: dict[str, tuple[Path, dict]] = {}
    dupes: list[tuple[str, Path]] = []
    for p in sorted(EVIDENCE.glob("s*/*.yaml")):
        try:
            doc = yaml.safe_load(p.read_text())
        except yaml.YAMLError as e:
            print(f"  !! unparseable YAML {p}: {e}")
            continue
        if not isinstance(doc, dict):
            continue
        sid = doc.get("study_id")
        if not sid:
            continue
        if sid in out:
            dupes.append((sid, p))
        else:
            out[sid] = (p, doc)
    return {"by_id": out, "dupes": dupes}


def norm_doi(x) -> str:
    if x is None:
        return ""
    return str(x).strip().lower().replace("https://doi.org/", "").rstrip(".")


def norm_pmid(x) -> str:
    if x is None:
        return ""
    s = str(x).strip()
    return "" if s in {"-", "—", "None", "null"} else s


def norm_access(x) -> str:
    s = str(x or "").strip().lower().replace(" ", "_")
    return {"abstract": "abstract_only", "full": "full_text"}.get(s, s)


def parse_appendix(text: str) -> list[dict]:
    rows = []
    # rows look like: | `white2026ffcws` | 10.1016/j.sleh.2025.10.003 | 41198487 | full text |
    # first cell may name more than one id, e.g. "`guo2024` / `guo2024_stroke_mr`"
    pat = re.compile(r"^\|\s*((?:`[^`]+`[^|]*?)+)\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|\s*$")
    in_appendix = False
    for ln in text.splitlines():
        if ln.startswith("## Appendix"):
            in_appendix = True
        if not in_appendix:
            continue
        m = pat.match(ln)
        if not m:
            continue
        sid_raw, doi, pmid, access = m.groups()
        ids = re.findall(r"`([A-Za-z0-9_]+)`", sid_raw)
        for sid in ids:
            rows.append({"study_id": sid, "doi": doi, "pmid": pmid, "access": access,
                         "raw": sid_raw})
    return rows


def cited_in_body(text: str) -> set[str]:
    body = text.split("## Appendix")[0]
    # backticked tokens that look like study ids: lowercase letters then a 4-digit year
    return {t for t in re.findall(r"`([a-z][a-z0-9_]*\d{4}[a-z0-9_]*)`", body)}


def main() -> int:
    text = REPORT.read_text()
    corpus = load_corpus()
    by_id = corpus["by_id"]
    rows = parse_appendix(text)

    print(f"corpus: {len(by_id)} unique study_ids across {len(list(EVIDENCE.glob('s*/*.yaml')))} "
          f"yaml files")
    if corpus["dupes"]:
        print(f"  note: {len(corpus['dupes'])} duplicate study_id records (multi-shard studies)")
    print(f"appendix rows parsed: {len(rows)}\n")

    fails, warns = [], []
    for r in rows:
        sid = r["study_id"]
        if sid not in by_id:
            fails.append(f"{sid}: NOT FOUND in evidence/")
            continue
        path, doc = by_id[sid]
        want_doi = norm_doi(r["doi"])
        want_pmid = norm_pmid(r["pmid"])

        # A study_id can legitimately appear in several shards, and for fjell2023 the two records
        # are two different papers. Accept a match against any record carrying this study_id, and
        # require the record that matches to be VERIFIED.
        records = []
        for p2 in sorted(EVIDENCE.glob(f"s*/{sid}.yaml")):
            d2 = yaml.safe_load(p2.read_text())
            if isinstance(d2, dict):
                records.append((p2, d2))
        if not records:
            records = [(path, doc)]

        dois = [norm_doi(d2.get("doi")) for _, d2 in records]
        pmids = [norm_pmid(d2.get("pmid")) for _, d2 in records]

        if want_doi and want_doi not in dois:
            fails.append(f"{sid}: DOI mismatch. report={want_doi} corpus={dois}")
        if want_pmid and want_pmid not in pmids:
            fails.append(f"{sid}: PMID mismatch. report={want_pmid} corpus={pmids}")
        if want_pmid and not any(pmids):
            warns.append(f"{sid}: report gives PMID {want_pmid}, corpus stores none")

        # the record whose identifiers the report actually used
        matched = [(p2, d2) for (p2, d2) in records
                   if (not want_doi or norm_doi(d2.get("doi")) == want_doi)
                   and (not want_pmid or norm_pmid(d2.get("pmid")) == want_pmid)]
        for p2, d2 in (matched or records):
            ver = (d2.get("verification") or {}).get("status")
            if ver != "VERIFIED":
                fails.append(f"{sid}: verification.status={ver!r}, expected VERIFIED ({p2.name})")

        want_access = norm_access(r["access"])
        stored_access = [norm_access(d2.get("access_tier")) for _, d2 in (matched or records)]
        if want_access and stored_access and want_access not in stored_access:
            fails.append(f"{sid}: access tier printed as {want_access!r}, corpus {stored_access}")

    body_ids = cited_in_body(text)
    appendix_ids = {r["study_id"] for r in rows}
    missing = sorted(body_ids - appendix_ids - BODY_ONLY_EXEMPT)
    unknown_body = sorted(i for i in missing if i not in by_id)
    uncited = sorted(i for i in missing if i in by_id)

    for sid in unknown_body:
        fails.append(f"{sid}: cited in body, NOT in evidence/ and not in appendix")
    for sid in uncited:
        warns.append(f"{sid}: cited in body, exists in corpus, absent from appendix table")

    print(f"PASS: {len(rows) - len([f for f in fails])} of {len(rows)} appendix rows clean")
    if warns:
        print(f"\nWARNINGS ({len(warns)}):")
        for w in warns:
            print(f"  - {w}")
    if fails:
        print(f"\nFAILURES ({len(fails)}):")
        for f in fails:
            print(f"  - {f}")
        return 1
    print("\nAll appendix citations resolve to VERIFIED corpus records with matching identifiers.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
