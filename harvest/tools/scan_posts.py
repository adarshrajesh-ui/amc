#!/usr/bin/env python3
"""Scan crawled forum HTML for posts that read like a first-person interview recall."""
import glob
import re
import sys

sys.path.insert(0, "/workspace/harvest/tools")
from crawl_forum import posts_of  # noqa: E402

FIRST_PERSON = re.compile(
    r"\b(i was asked|they asked me|asked me (?:to|the|this|a|about|how|what|why)|"
    r"i got asked|i had (?:my|an|a) (?:phone |first |second |final |onsite )?interview|"
    r"in my interview|at my interview|during my interview|my interviewer asked|"
    r"the interviewer asked|one of the questions (?:i|they)|"
    r"i interviewed (?:with|at)|questions i (?:was |got )?asked|"
    r"here (?:are|is) the questions|i just had (?:a|an|my))",
    re.I,
)
QUESTIONISH = re.compile(
    r"(what is the (?:probability|expected|value|chance)|"
    r"how many|what would you|expected value|make a market|"
    r"you (?:roll|flip|draw|pick|have) (?:a|an|two|three|\d)|probability that|"
    r"\bbid\b.*\bask\b|fair (?:coin|die|dice)|what's the (?:probability|expected))",
    re.I,
)
FIRM = re.compile(
    r"optiver|susquehanna|\bsig\b|jane street|citadel|imc|akuna|jump trading|"
    r"\bdrw\b|hudson river|five rings|two sigma|de shaw|getco|ghco|wolverine|"
    r"belvedere|flow traders|transmarket|peak6|spot trading|infinium|chicago trading|"
    r"first new york|tower research|virtu|jane st",
    re.I,
)

if __name__ == "__main__":
    for d in sys.argv[1:]:
        for f in sorted(glob.glob(f"{d}/*.html")):
            try:
                url, posts = posts_of(f)
            except Exception:
                continue
            for i, p in enumerate(posts):
                if FIRST_PERSON.search(p) and QUESTIONISH.search(p) and FIRM.search(p):
                    print("=" * 100)
                    print(f"{url}  [post {i}]")
                    print(p[:1600])
