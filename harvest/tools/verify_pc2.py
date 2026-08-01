#!/usr/bin/env python3
"""Audit positive_controls_v2.json before it is handed over.

Checks, per record: the quote is really in the cached page bytes, the URL is absent
from questions.jsonl, the question wording does not collide with anything already in
the corpus, and the quote does not look mechanically derived from question_text.
"""
import json
import re
import sys
from difflib import SequenceMatcher
from urllib.parse import urlparse, unquote

CONTROLS = "/workspace/harvest/spec/positive_controls_v2.json"
CORPUS = "/workspace/harvest/questions.jsonl"

sys.path.insert(0, "/workspace/harvest/tools")
from build_pc2 import RECORDS  # noqa: E402


def norm_ws(s):
    return re.sub(r"\s+", " ", s).strip()


def norm_txt(s):
    s = (s or "").lower()
    s = re.sub(r"[^a-z0-9\u4e00-\u9fff ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def main():
    ctrls = json.load(open(CONTROLS))
    corpus = [json.loads(l) for l in open(CORPUS) if l.strip()]

    urls = set()
    for r in corpus:
        for a in r.get("attestations", []):
            u = (a.get("source_url") or "").strip().rstrip("/").lower()
            if u:
                urls.add(u)
                p = urlparse(u)
                urls.add(unquote(p.netloc + p.path).rstrip("/"))

    fails = 0
    for i, (c, spec) in enumerate(zip(ctrls, RECORDS), 1):
        tag = f"[{i:2d}] {c['firm'][:26]:26s}"
        problems = []

        # 1. quote present in the cached page bytes
        page = norm_ws(open(spec["cache"], encoding="utf-8", errors="replace").read())
        if norm_ws(c["source_quote"]) not in page:
            problems.append("QUOTE NOT IN CACHED PAGE")

        # 2. url absent from corpus
        u = c["source_url"].strip().rstrip("/").lower()
        p = urlparse(u)
        if u in urls or unquote(p.netloc + p.path).rstrip("/") in urls:
            problems.append("URL ALREADY IN CORPUS")

        # 3. question wording collision with corpus
        q = norm_txt(c["question_text"])
        qt = set(q.split())
        best = (0.0, "", "")
        for r in corpus:
            for field in ("question_text", "question_text_en"):
                cand = norm_txt(r.get(field, ""))
                if not cand:
                    continue
                ct = set(cand.split())
                jac = len(qt & ct) / max(1, len(qt | ct))
                if jac < 0.30:
                    continue
                seq = SequenceMatcher(None, q, cand).ratio()
                if max(jac, seq) > best[0]:
                    best = (max(jac, seq), r["firm"], cand[:90])
        if best[0] >= 0.75:
            problems.append(f"NEAR-DUP corpus {best[0]:.2f} [{best[1]}] {best[2]}")

        # 4. the tell that leaked the previous test
        if c["source_quote"] == c["question_text"][:120]:
            problems.append("QUOTE == first 120 chars of question")
        if len(c["source_quote"]) <= len(c["question_text"]):
            problems.append("quote not longer than question")
        if re.search(r"\w$", c["source_quote"]) and not re.search(
            r"[.!?\"')\]`]$", c["source_quote"]
        ):
            problems.append("quote may end mid-word")

        # 5. required fields populated
        for k in ("firm", "role_track", "level", "round", "question_text", "source_url",
                  "source_quote", "post_date", "source_type", "how_verified", "not_in_corpus"):
            if k not in c or c[k] in (None, ""):
                problems.append(f"empty field: {k}")

        if problems:
            fails += 1
            print(f"{tag} FAIL")
            for pr in problems:
                print(f"        - {pr}")
        else:
            print(f"{tag} ok   sim_max={best[0]:.2f} quote={len(c['source_quote'])}b")

    print(f"\n{len(ctrls) - fails}/{len(ctrls)} clean")
    lens = sorted(len(c["source_quote"]) for c in ctrls)
    print(f"quote length min/median/max = {lens[0]}/{lens[len(lens)//2]}/{lens[-1]}")


if __name__ == "__main__":
    main()
