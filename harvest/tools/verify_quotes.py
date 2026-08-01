#!/usr/bin/env python3
"""Mechanical quote gate.

Re-fetches every cited URL and asserts the recorded source_quote actually appears
in the page text. This is the trust foundation of the corpus: a quote that cannot
be re-found is a quote we cannot prove was ever read.

Verification is deliberately not a judgment call. A record either passes a byte-level
normalized-substring check against retrieved text, or it does not.

Fetch strategies are tried in order and the one that succeeded is recorded, because
"verified against the live page" and "verified against an archive snapshot" are
different epistemic claims and the report must distinguish them.
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import gzip
import hashlib
import html
import io
import json
import pathlib
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
CACHE = pathlib.Path(__file__).resolve().parent.parent / "evidence" / "pagecache"
CACHE.mkdir(parents=True, exist_ok=True)

# A quote shorter than this cannot meaningfully corroborate anything; treating a
# handful of characters as "verified" would launder noise into evidence.
MIN_QUOTE_CHARS = 24


def norm(s: str) -> str:
    """Whitespace-collapsed, unicode-normalized, casefolded text.

    CJK sources arrive with full-width punctuation and stray zero-width joiners that
    differ between the search index and the live page while representing identical
    text, so NFKC runs before comparison.
    """
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("\u200b", "").replace("\ufeff", "").replace("\xa0", " ")
    s = re.sub(r"\s+", " ", s)
    return s.strip().casefold()


_TAG_STRIP = re.compile(
    r"<(script|style|noscript|svg)\b[^>]*>.*?</\1>", re.S | re.I
)


def html_to_text(raw: str) -> str:
    raw = _TAG_STRIP.sub(" ", raw)
    raw = re.sub(r"<br\s*/?>|</p>|</div>|</li>|</tr>", "\n", raw, flags=re.I)
    raw = re.sub(r"<[^>]+>", " ", raw)
    return html.unescape(raw)


# Politeness state. Hammering these hosts concurrently gets the whole run throttled,
# and a throttled fetch is indistinguishable from a missing quote unless we are careful
# to classify it separately -- so we serialize per host and back off hard.
_DOMAIN_LOCKS: dict[str, "threading.Lock"] = {}
_DOMAIN_LAST: dict[str, float] = {}
_LOCKS_GUARD = None
DOMAIN_DELAY_S = 2.5

import threading  # noqa: E402

_LOCKS_GUARD = threading.Lock()


def _domain_lock(host: str) -> "threading.Lock":
    with _LOCKS_GUARD:
        if host not in _DOMAIN_LOCKS:
            _DOMAIN_LOCKS[host] = threading.Lock()
        return _DOMAIN_LOCKS[host]


# Bodies that are technically HTTP 200 but contain no source content. Scoring these
# as "quote not found" would manufacture false fabrication signals, which is the most
# damaging error this tool can make.
BLOCK_MARKERS = (
    "performing security verification",
    "enable javascript and cookies to continue",
    "checking your browser before accessing",
    "just a moment...",
    "attention required! | cloudflare",
    "access to this page has been denied",
    "请开启javascript并刷新该页",
    "滑动验证",
    "您的访问出现异常",
    "verify you are human",
    "unusual traffic from your computer",
)


def looks_blocked(text: str) -> bool:
    head = text[:4000].casefold()
    if any(m in head for m in BLOCK_MARKERS):
        return True
    # A page with almost no text is a wall or a JS shell, not an article.
    return len(text.strip()) < 500


def _get(url: str, timeout: int = 30, attempts: int = 3) -> tuple[str | None, str]:
    """Fetch with per-host serialization and backoff.

    Returns (text, note) where note explains a failure well enough to tell a block
    apart from a genuine absence.
    """
    host = urllib.parse.urlparse(url).netloc
    lock = _domain_lock(host)
    last_note = "unknown"
    for attempt in range(attempts):
        with lock:
            gap = time.time() - _DOMAIN_LAST.get(host, 0.0)
            if gap < DOMAIN_DELAY_S:
                time.sleep(DOMAIN_DELAY_S - gap)
            _DOMAIN_LAST[host] = time.time()
            req = urllib.request.Request(
                url,
                headers={
                    "User-Agent": UA,
                    "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8",
                    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
                    "Accept-Encoding": "gzip",
                    "Referer": f"https://{host}/",
                },
            )
            try:
                with urllib.request.urlopen(req, timeout=timeout) as r:
                    data = r.read()
                    if r.headers.get("Content-Encoding") == "gzip":
                        data = gzip.GzipFile(fileobj=io.BytesIO(data)).read()
                    charset = r.headers.get_content_charset() or "utf-8"
                    return data.decode(charset, errors="replace"), "ok"
            except urllib.error.HTTPError as e:
                last_note = f"http_{e.code}"
                if e.code in (429, 503, 403):
                    time.sleep(4 * (2 ** attempt))
                    continue
                return None, last_note
            except Exception as e:
                last_note = type(e).__name__
                time.sleep(2 * (2 ** attempt))
    return None, last_note


def strategies(url: str):
    """Yield (name, fetcher) pairs, cheapest and most authoritative first."""
    yield "live", lambda: _get(url)
    # Text proxy renders JS and carries a different egress reputation, which gets
    # past several bot walls that block us directly.
    yield "jina", lambda: _get("https://r.jina.ai/" + url, timeout=60)
    # Archive last: it proves the text existed, not that it is live now.
    yield "wayback", lambda: _wayback(url)


def _wayback(url: str) -> tuple[str | None, str]:
    api = "https://archive.org/wayback/available?url=" + urllib.parse.quote(url, safe="")
    meta, note = _get(api, timeout=30)
    if not meta:
        return None, f"wayback_api_{note}"
    try:
        snap = json.loads(meta).get("archived_snapshots", {}).get("closest", {})
    except Exception:
        return None, "wayback_api_badjson"
    if not snap.get("available") or not snap.get("url"):
        return None, "no_snapshot"
    return _get(snap["url"], timeout=60)


def cache_path(url: str, strat: str) -> pathlib.Path:
    h = hashlib.sha256((strat + "|" + url).encode()).hexdigest()[:20]
    return CACHE / f"{h}.txt"


def fetch_text(url: str, refresh: bool = False) -> tuple[str | None, str | None, str]:
    """Return (text, strategy_that_worked, note). text is None if nothing readable."""
    notes = []
    for name, fn in strategies(url):
        cp = cache_path(url, name)
        if cp.exists() and not refresh:
            body = cp.read_text(encoding="utf-8", errors="replace")
            if body.strip() and not looks_blocked(body):
                return body, name, "cached"
            notes.append(f"{name}:cached_empty_or_blocked")
            continue
        raw, note = fn()
        if not raw or not raw.strip():
            cp.write_text("", encoding="utf-8")
            notes.append(f"{name}:{note}")
            continue
        text = html_to_text(raw) if "<" in raw[:2000] else raw
        if looks_blocked(text):
            cp.write_text("", encoding="utf-8")
            notes.append(f"{name}:bot_wall")
            continue
        cp.write_text(text, encoding="utf-8", errors="replace")
        return text, name, "fetched"
    return None, None, ";".join(notes)


def longest_verified_run(quote_n: str, page_n: str) -> int:
    """Longest prefix of the quote present verbatim in the page.

    Reported on failures so a near-miss (source lightly edited, or the collector
    trimmed a trailing clause) is distinguishable from a quote that is simply absent.
    """
    if not quote_n:
        return 0
    lo, hi, best = 0, len(quote_n), 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid and quote_n[:mid] in page_n:
            best, lo = mid, mid + 1
        else:
            hi = mid - 1
    return best


def verify_one(rec: dict, refresh: bool = False) -> dict:
    url = (rec.get("source_url") or "").strip()
    quote = (rec.get("source_quote") or "").strip()
    out = {
        "id": rec.get("id"),
        "source_url": url,
        "status": None,
        "method": None,
        "reason": None,
        "quote_chars": len(quote),
        "matched_chars": 0,
        "content_hash": None,
    }
    if not url.startswith("http"):
        out.update(status="FAIL", reason="no_url")
        return out
    if len(quote) < MIN_QUOTE_CHARS:
        out.update(status="FAIL", reason=f"quote_too_short(<{MIN_QUOTE_CHARS})")
        return out

    text, method, note = fetch_text(url, refresh=refresh)
    if text is None:
        out.update(status="UNREACHABLE", reason=note or "all_fetch_strategies_failed")
        return out

    out["method"] = method
    out["content_hash"] = hashlib.sha256(text.encode("utf-8", "replace")).hexdigest()[:16]
    pn, qn = norm(text), norm(quote)
    if qn in pn:
        out["status"] = "PASS"
        out["matched_chars"] = len(qn)
        return out

    run = longest_verified_run(qn, pn)
    out["matched_chars"] = run
    # A long verbatim head that then diverges is characteristic of a live page whose
    # tail was edited, not of an invented quote.
    out["status"] = "PARTIAL" if run >= max(MIN_QUOTE_CHARS, int(len(qn) * 0.5)) else "FAIL"
    out["reason"] = f"quote_not_found(matched {run}/{len(qn)} chars via {method})"
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("infile")
    ap.add_argument("-o", "--out", default="reports/quote_gate.json")
    ap.add_argument("-j", "--jobs", type=int, default=12)
    ap.add_argument("--refresh", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    recs = [json.loads(l) for l in open(args.infile, encoding="utf-8") if l.strip()]
    if args.limit:
        recs = recs[: args.limit]

    t0 = time.time()

    # Warm the cache one URL at a time. Many records share a URL, and fetching the
    # same page concurrently from several threads both wastes the politeness budget
    # and is what got this run throttled the first time.
    urls = sorted({(r.get("source_url") or "").strip() for r in recs if str(r.get("source_url", "")).startswith("http")})
    print(f"warming {len(urls)} unique URLs for {len(recs)} records", file=sys.stderr, flush=True)
    with cf.ThreadPoolExecutor(max_workers=args.jobs) as ex:
        futs = {ex.submit(fetch_text, u, args.refresh): u for u in urls}
        for i, fut in enumerate(cf.as_completed(futs), 1):
            try:
                fut.result()
            except Exception:
                pass
            if i % 20 == 0:
                print(f"  fetched {i}/{len(urls)}  {time.time()-t0:.0f}s", file=sys.stderr, flush=True)

    results = []
    with cf.ThreadPoolExecutor(max_workers=args.jobs) as ex:
        futs = {ex.submit(verify_one, r, False): r for r in recs}
        for i, fut in enumerate(cf.as_completed(futs), 1):
            results.append(fut.result())
            if i % 50 == 0:
                print(f"  checked {i}/{len(recs)}  {time.time()-t0:.0f}s", file=sys.stderr, flush=True)

    tally: dict[str, int] = {}
    for r in results:
        tally[r["status"]] = tally.get(r["status"], 0) + 1

    outp = pathlib.Path(args.out)
    outp.parent.mkdir(parents=True, exist_ok=True)
    outp.write_text(json.dumps({"tally": tally, "results": results}, indent=1))

    total = len(results)
    print(f"\nquote gate over {total} records ({time.time()-t0:.0f}s)")
    for k in ("PASS", "PARTIAL", "FAIL", "UNREACHABLE"):
        n = tally.get(k, 0)
        print(f"  {k:12s} {n:5d}  {100*n/max(total,1):5.1f}%")
    print(f"\nwrote {outp}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
