#!/usr/bin/env python3
"""Audit: every `quote` in every YAML record must appear in text this shard actually retrieved.

Matching is whitespace- and punctuation-tolerant because the HTML->text and PDF->text converters
mangle unicode dashes, non-breaking spaces, ligatures and Greek letters. A quote counts as VERIFIED
only if a normalised form of it is a substring of a normalised retrieved corpus file.
Anything that does not match is printed for manual inspection - it is not silently passed.
"""
import pathlib
import re
import sys
import unicodedata

import yaml

HERE = pathlib.Path(__file__).parent


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = (s.replace("\u2013", "-").replace("\u2014", "-").replace("\u2212", "-")
          .replace("\u2019", "'").replace("\u2018", "'")
          .replace("\u201c", '"').replace("\u201d", '"'))
    # Greek/beta spellings differ between PubMed plain text and PMC HTML
    s = s.replace("\u03b2", "b").replace("beta", "b").replace("\u03b1", "a")
    # Quotes in this shard transliterate Greek to ASCII for pipeline safety, so the
    # auditor must collapse both spellings to the same token before comparing.
    s = s.replace("\u03b5", "e").replace("epsilon", "e")
    s = s.replace("\u2264", "<=").replace("\u2265", ">=")
    s = re.sub(r"[^a-z0-9<>=.%+-]+", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()


corpus = {}
for p in sorted(HERE.glob("*.txt")) + sorted(HERE.glob("*.html")):
    try:
        corpus[p.name] = norm(p.read_text(errors="ignore"))
    except Exception:
        pass

total = matched = 0
misses = []
ellipsis_joined = []
for path in sorted(HERE.glob("*.yaml")):
    doc = yaml.safe_load(path.read_text())
    for i, eff in enumerate(doc.get("effects") or []):
        q = (eff.get("quote") or "").strip()
        if not q:
            continue
        total += 1
        # Quotes may splice non-contiguous passages with " ... ". Each segment must be
        # independently verbatim; a segment is not allowed to be paraphrase.
        segs = [norm(s) for s in re.split(r"\s*\.\.\.\s*", q) if norm(s)]
        nq = norm(q)
        hit = None
        for name, body in corpus.items():
            if all(s in body for s in segs):
                hit = name
                break
        if hit:
            matched += 1
            if len(segs) > 1:
                ellipsis_joined.append("%s effect[%d]: %d segments, all verbatim in %s"
                                       % (path.name, i, len(segs), hit))
        else:
            # try the longest contiguous 12-word window, to localise the mismatch
            words = nq.split()
            best = None
            for w in (25, 18, 12, 8):
                if len(words) < w:
                    continue
                for st in range(0, len(words) - w + 1):
                    frag = " ".join(words[st:st + w])
                    for name, body in corpus.items():
                        if frag in body:
                            best = (w, frag[:90], name)
                            break
                    if best:
                        break
                if best:
                    break
            misses.append((path.name, i, eff.get("outcome_construct"), q[:110], best))

print("corpus files: %d" % len(corpus))
print("quotes checked: %d   matched verbatim in retrieved text: %d   unmatched: %d"
      % (total, matched, len(misses)))
if misses:
    print()
    for name, i, oc, q, best in misses:
        print("UNMATCHED %s effect[%d] %s" % (name, i, oc))
        print("   quote: %s..." % q)
        if best:
            print("   longest matching window (%d words) found in %s: '%s...'" % (best[0], best[2], best[1]))
        else:
            print("   NO window of 8+ words matched any retrieved file")
        print()
    sys.exit(1)
if ellipsis_joined:
    print()
    print("ellipsis-spliced quotes (every segment independently verbatim): %d" % len(ellipsis_joined))
    for s in ellipsis_joined:
        print("   " + s)
print()
print("ALL QUOTES TRACE TO RETRIEVED TEXT")
