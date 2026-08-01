#!/usr/bin/env python3
"""Check whether a candidate URL / question wording already exists in questions.jsonl.

Usage:
    python3 check_corpus.py url <url> [<url> ...]
    python3 check_corpus.py text "<question wording>"
    python3 check_corpus.py domain <netloc-substring>
"""
import json
import re
import sys
from difflib import SequenceMatcher
from urllib.parse import urlparse

CORPUS = "/workspace/harvest/questions.jsonl"


def load():
    recs = []
    with open(CORPUS) as fh:
        for line in fh:
            line = line.strip()
            if line:
                recs.append(json.loads(line))
    return recs


def norm(s):
    s = (s or "").lower()
    s = re.sub(r"[^a-z0-9\u4e00-\u9fff ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def main():
    recs = load()
    mode = sys.argv[1]

    if mode == "url":
        for target in sys.argv[2:]:
            t = target.rstrip("/").lower()
            tp = urlparse(t)
            hits = []
            for r in recs:
                for a in r.get("attestations", []):
                    u = (a.get("source_url") or "").rstrip("/").lower()
                    if not u:
                        continue
                    up = urlparse(u)
                    if u == t or (
                        up.netloc == tp.netloc
                        and up.path == tp.path
                        and up.query == tp.query
                    ):
                        hits.append((r["id"], r["firm"], r["question_text"][:70], u))
            print(f"\n== {target}")
            print(f"   exact/path hits: {len(hits)}")
            for h in hits[:5]:
                print("   ", h)
            # also report same-host presence for context
            host = tp.netloc.replace("www.", "")
            same_host = sum(
                1
                for r in recs
                for a in r.get("attestations", [])
                if host and host in (a.get("source_url") or "")
            )
            print(f"   same-host attestations in corpus: {same_host}")

    elif mode == "text":
        q = norm(sys.argv[2])
        qtok = set(q.split())
        scored = []
        for r in recs:
            for field in ("question_text", "question_text_en"):
                c = norm(r.get(field, ""))
                if not c:
                    continue
                ctok = set(c.split())
                jac = len(qtok & ctok) / max(1, len(qtok | ctok))
                ratio = SequenceMatcher(None, q, c).ratio() if jac > 0.15 else 0.0
                scored.append((max(jac, ratio), jac, ratio, r["id"], r["firm"], r.get(field)[:150]))
        scored.sort(reverse=True)
        print(f"query: {q[:110]}")
        for s in scored[:6]:
            print(f"  score={s[0]:.3f} jac={s[1]:.3f} seq={s[2]:.3f} [{s[3]}] {s[4]}: {s[5]}")

    elif mode == "domain":
        needle = sys.argv[2].lower()
        out = []
        for r in recs:
            for a in r.get("attestations", []):
                u = (a.get("source_url") or "").lower()
                if needle in u:
                    out.append(u)
        print(f"{len(out)} attestations on '{needle}'")
        for u in sorted(set(out)):
            print("  ", u)


if __name__ == "__main__":
    main()
