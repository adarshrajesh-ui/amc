"""Citation verification (Gate G2).

Every evidence record must resolve against Crossref (by DOI) and/or PubMed (by PMID),
and the resolved title must actually appear inside the recorded citation string. This is
the anti-fabrication mechanism: a hallucinated DOI fails to resolve, and a real DOI
attached to the wrong claim fails the title match.

Responses are cached to data/refcache.json so `make all` is reproducible without network.
"""

from __future__ import annotations

import html
import json
import re
import sys
import time
import unicodedata
import urllib.parse
import urllib.request
from difflib import SequenceMatcher
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
EVIDENCE = ROOT / "evidence"
CACHE_PATH = ROOT / "data" / "refcache.json"
OUT_PATH = ROOT / "reports" / "verification.json"

TITLE_SIM_THRESHOLD = 0.72
UA = "sleep-debt-factory/1.0 (research; contact via repo)"


def load_cache() -> dict:
    if CACHE_PATH.exists():
        return json.loads(CACHE_PATH.read_text())
    return {}


def save_cache(cache: dict) -> None:
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    CACHE_PATH.write_text(json.dumps(cache, indent=1, sort_keys=True))


def _get(url: str, cache: dict, offline: bool = False) -> dict | None:
    if url in cache:
        return cache[url]
    if offline:
        return None
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=30) as fh:
                payload = json.loads(fh.read().decode("utf-8", "replace"))
            cache[url] = payload
            time.sleep(0.15)
            return payload
        except Exception as exc:  # noqa: BLE001
            if attempt == 3:
                cache[url] = {"__error__": str(exc)}
                return cache[url]
            time.sleep(2 ** attempt)
    return None


GREEK = {
    "\u03b1": "alpha", "\u03b2": "beta", "\u03b3": "gamma", "\u03b4": "delta",
    "\u03b5": "epsilon", "\u03ba": "kappa", "\u03bb": "lambda", "\u03bc": "mu",
    "\u03c3": "sigma", "\u03c4": "tau", "\u03c9": "omega", "\u0391": "alpha",
    "\u0392": "beta", "\u0394": "delta", "\u03a9": "omega",
}
STOPWORDS = {
    "a", "an", "the", "of", "in", "on", "and", "or", "for", "with", "to", "from", "by",
    "is", "are", "as", "at", "be", "not", "its", "their", "into", "during", "between",
    "among", "across", "study", "trial", "analysis", "results",
}


def normalize(text: str) -> str:
    """Fold HTML entities, tags, Greek letters and accents so titles compare across sources."""
    text = html.unescape(html.unescape(text or ""))
    text = re.sub(r"<[^>]+>", " ", text)
    for ch, name in GREEK.items():
        text = text.replace(ch, f" {name} ")
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = text.lower()
    # collapse "beta-amyloid" / "amyloid-beta" / "abeta" style variants
    text = re.sub(r"\bamyloid\s*beta\b", "beta amyloid", text)
    text = re.sub(r"\ba\s*beta\b", "beta amyloid", text)
    text = re.sub(r"[^a-z0-9 ]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def _tokens(text: str) -> list[str]:
    return [t for t in normalize(text).split() if t not in STOPWORDS and len(t) > 2]


def title_in_citation(title: str, citation: str) -> float:
    """Agreement between a resolved title and the recorded citation string.

    Three views are combined because bibliographic strings differ from publisher titles in
    predictable ways (subtitles, translated titles, entity encoding): contiguous-block match,
    content-token containment, and overall sequence ratio.
    """
    # Bilingual titles append a translation after a colon; score each segment and take the best.
    raw_segments = [title] + [s for s in re.split(r":\s+", title) if len(s.strip()) > 15]
    return max(_score_one(seg, citation) for seg in raw_segments)


def _score_one(title: str, citation: str) -> float:
    t, c = normalize(title), normalize(citation)
    if not t:
        return 0.0
    if t in c:
        return 1.0
    match = SequenceMatcher(None, t, c).find_longest_match(0, len(t), 0, len(c))
    contiguous = match.size / len(t)
    t_tok, c_tok = _tokens(title), set(_tokens(citation))
    containment = (sum(tok in c_tok for tok in t_tok) / len(t_tok)) if t_tok else 0.0
    ratio = SequenceMatcher(None, t, c).ratio()
    return max(contiguous, containment, ratio * 0.9)


OFFICIAL_DOMAINS = (
    "cdc.gov", "who.int", "ssa.gov", "samhsa.gov", "nih.gov", "census.gov",
    "nhlbi.nih.gov", "bls.gov", "data.gov", "europa.eu", "oecd.org", "aasm.org",
)


def official_url_ok(url: str, cache: dict, offline: bool) -> bool | None:
    """Records without a DOI/PMID (official statistics) are verified by resolving their URL."""
    if not url:
        return None
    if not any(d in url for d in OFFICIAL_DOMAINS):
        return False
    key = "HEAD:" + url
    if key in cache:
        return bool(cache[key].get("ok"))
    if offline:
        return None
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30) as fh:
            ok = 200 <= fh.status < 400
    except Exception:  # noqa: BLE001
        ok = False
    cache[key] = {"ok": ok}
    return ok


def crossref_title(doi: str, cache: dict, offline: bool) -> tuple[bool, str | None]:
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi.strip())
    data = _get(url, cache, offline)
    if not data or "__error__" in data or "message" not in data:
        return False, None
    titles = data["message"].get("title") or []
    return (True, titles[0]) if titles else (True, None)


def pubmed_title(pmid: str, cache: dict, offline: bool) -> tuple[bool, str | None]:
    url = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id="
           + urllib.parse.quote(str(pmid).strip()))
    data = _get(url, cache, offline)
    if not data or "__error__" in data:
        return False, None
    result = data.get("result", {})
    rec = result.get(str(pmid).strip())
    if not rec or "error" in rec:
        return False, None
    return True, rec.get("title")


def iter_records():
    for path in sorted(EVIDENCE.rglob("*.y*ml")):
        try:
            docs = list(yaml.safe_load_all(path.read_text()))
        except yaml.YAMLError as exc:
            yield path, {"__yaml_error__": str(exc)}
            continue
        for doc in docs:
            if isinstance(doc, dict) and doc:
                yield path, doc


def verify(offline: bool = False) -> dict:
    cache = load_cache()
    out = {"records": [], "summary": {}}
    seen_ids: dict[str, str] = {}
    for path, rec in iter_records():
        if "__yaml_error__" in rec:
            out["records"].append({"file": str(path.relative_to(ROOT)), "status": "YAML_ERROR",
                                   "detail": rec["__yaml_error__"]})
            continue
        sid = rec.get("study_id", "?")
        citation = rec.get("citation", "")
        doi, pmid = rec.get("doi"), rec.get("pmid")
        cr_ok, cr_title = (crossref_title(doi, cache, offline) if doi else (None, None))
        pm_ok, pm_title = (pubmed_title(pmid, cache, offline) if pmid else (None, None))
        # Best of the two resolved titles: publishers and PubMed disagree on subtitles.
        sims = {}
        for label, title in (("crossref", cr_title), ("pubmed", pm_title)):
            if title:
                sims[label] = title_in_citation(title, citation)
        resolved_label = max(sims, key=sims.get) if sims else None
        resolved = {"crossref": cr_title, "pubmed": pm_title}.get(resolved_label)
        sim = sims.get(resolved_label)
        resolves = bool(cr_ok) or bool(pm_ok)
        if resolves and sim is not None and sim >= TITLE_SIM_THRESHOLD:
            status = "VERIFIED"
        elif not doi and not pmid:
            url = rec.get("url") or ""
            url_ok = official_url_ok(url, cache, offline)
            # Official statistical products have no DOI. An official domain plus a fully
            # specified citation is the strongest available check; some agencies block
            # automated requests, so unreachability is recorded but does not fail the gate.
            official_domain = any(d in url for d in OFFICIAL_DOMAINS)
            status = "OFFICIAL_SOURCE" if official_domain else "UNVERIFIED"
            if official_domain and not url_ok:
                status = "OFFICIAL_SOURCE_UNREACHED"
        else:
            status = "UNVERIFIED"
        dup = seen_ids.get(sid)
        seen_ids[sid] = str(path)
        out["records"].append({
            "file": str(path.relative_to(ROOT)), "study_id": sid, "doi": doi, "pmid": pmid,
            "crossref_ok": cr_ok, "pubmed_ok": pm_ok,
            "resolved_title": resolved, "resolved_via": resolved_label,
            "title_similarity": None if sim is None else round(sim, 3),
            "status": status, "duplicate_of": dup, "url": rec.get("url"),
            "shard": rec.get("shard"), "tier": rec.get("tier"), "access_tier": rec.get("access_tier"),
        })
    save_cache(cache)
    recs = out["records"]
    out["summary"] = {
        "n_records": len(recs),
        "n_verified": sum(r.get("status") == "VERIFIED" for r in recs),
        "n_official_source": sum(str(r.get("status")).startswith("OFFICIAL_SOURCE") for r in recs),
        "n_unverified": sum(r.get("status") == "UNVERIFIED" for r in recs),
        "n_yaml_errors": sum(r.get("status") == "YAML_ERROR" for r in recs),
        "n_duplicate_ids": sum(bool(r.get("duplicate_of")) for r in recs),
        "n_identifier_resolves": sum(bool(r.get("crossref_ok")) or bool(r.get("pubmed_ok")) for r in recs),
        "threshold": TITLE_SIM_THRESHOLD,
    }
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(out, indent=1))
    return out


if __name__ == "__main__":
    offline = "--offline" in sys.argv
    res = verify(offline=offline)
    s = res["summary"]
    print(json.dumps(s, indent=1))
    for r in res["records"]:
        if r.get("status") != "VERIFIED":
            print(f"  !! {r.get('study_id')}: {r.get('status')} "
                  f"doi={r.get('doi')} pmid={r.get('pmid')} sim={r.get('title_similarity')}")
    if "--strict" in sys.argv and s["n_verified"] != s["n_records"]:
        sys.exit(1)
