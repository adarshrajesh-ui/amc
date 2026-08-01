#!/usr/bin/env python3
"""Render the cached GeeksforGeeks interview-experience pages down to the write-up.

GFG wraps ~2kB of first-person account in ~160kB of nav, course ads and "Similar
Reads" rails, so a plain tag strip buries the text. The article always starts at the
"Last Updated : <date>" line the template emits under the H1 and ends at the "Comment"
/ "Explore" footer, so slice between those and drop the boilerplate lines that repeat
on every page.

Usage:
  gfg_read.py list                 # one line per page: date, length, title
  gfg_read.py show <substring>     # full body of the matching page(s)
"""
import glob
import os
import re
import sys

sys.path.insert(0, "/workspace/harvest/tools")
from pagetext import clean  # noqa: E402

CACHE = "/workspace/harvest/.gfg_cache"
# The template's own furniture, identical on every page.
CHROME = re.compile(r"^(Courses|Tutorials|Interview Prep|DSA|Practice Problems|C|C\+\+|"
                    r"Java|Python|JavaScript|Data Science|Machine Learning|Linux|DevOps|"
                    r"Explore|Comment|More info|Advertise with us|Next Article|"
                    r"Similar Reads|Article Tags :)\s*$")


def body(path):
    txt = clean(open(path, encoding="utf-8", errors="replace").read())
    m = re.search(r"Last Updated :\s*([^\n]+)", txt)
    date = m.group(1).strip() if m else "?"
    start = m.end() if m else 0
    tail = re.search(r"\n\s*(Comment\s*\n\s*Explore|Explore\s*\nDSA Tutorial)", txt[start:])
    chunk = txt[start:start + tail.start()] if tail else txt[start:start + 12000]
    lines = [l.strip() for l in chunk.split("\n")]
    lines = [l for l in lines if l and not CHROME.match(l)]
    title = txt.split("\n", 1)[0].replace(" - GeeksforGeeks", "").strip()
    return {"path": path, "title": title, "date": date, "text": "\n".join(lines)}


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "list"
    pages = [body(p) for p in sorted(glob.glob(os.path.join(CACHE, "*.html")))]
    if cmd == "list":
        for p in pages:
            print("%-14s %5d  %-56s %s" % (p["date"], len(p["text"]), p["title"][:56],
                                           os.path.basename(p["path"])))
        print("\n[%d pages]" % len(pages), file=sys.stderr)
        return
    pat = sys.argv[2]
    for p in pages:
        if pat not in p["path"] and pat.lower() not in p["title"].lower():
            continue
        print("\n=== %s | %s\n%s\n%s" % (p["title"], p["date"], p["path"], p["text"]))


if __name__ == "__main__":
    main()
