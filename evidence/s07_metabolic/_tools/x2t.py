#!/usr/bin/env python3
"""JATS/HTML -> plain text, for quoting verbatim sentences from retrieved full texts."""
import re
import sys


def strip(path):
    raw = open(path, encoding="utf-8", errors="replace").read()
    raw = re.sub(r"<\?xml.*?\?>", " ", raw, flags=re.S)
    raw = re.sub(r"<(script|style)\b.*?</\1>", " ", raw, flags=re.S | re.I)
    # keep structural breaks so sentences don't fuse across cells
    raw = re.sub(r"</(p|title|td|th|tr|sec|abstract|caption|li|h[1-6]|div)>", "\n", raw, flags=re.I)
    raw = re.sub(r"<br\s*/?>", "\n", raw, flags=re.I)
    raw = re.sub(r"<[^>]+>", " ", raw)
    for a, b in [("&#x000a0;", " "), ("&#x2009;", " "), ("&#x2013;", "-"), ("&#x2014;", "-"),
                 ("&#x2212;", "-"), ("&#x00b1;", "+/-"), ("&#x2018;", "'"), ("&#x2019;", "'"),
                 ("&#x201c;", '"'), ("&#x201d;", '"'), ("&#x0025;", "%"), ("&#x000b7;", "."),
                 ("&nbsp;", " "), ("&amp;", "&"), ("&lt;", "<"), ("&gt;", ">"), ("&quot;", '"'),
                 ("&#x003c;", "<"), ("&#x003e;", ">"), ("&#x00d7;", "x"), ("&#x0394;", "delta")]:
        raw = raw.replace(a, b)
    raw = re.sub(r"&#x([0-9a-fA-F]+);", lambda m: chr(int(m.group(1), 16)), raw)
    raw = re.sub(r"&#(\d+);", lambda m: chr(int(m.group(1))), raw)
    raw = re.sub(r"[ \t]+", " ", raw)
    raw = re.sub(r"\n\s*\n+", "\n", raw)
    return raw.strip()


if __name__ == "__main__":
    txt = strip(sys.argv[1])
    if len(sys.argv) > 2:  # grep mode: print lines matching any regex, with context
        pats = [re.compile(p, re.I) for p in sys.argv[2:]]
        for line in txt.split("\n"):
            if any(p.search(line) for p in pats):
                print(line.strip()[:2000])
                print("---")
    else:
        print(txt)
