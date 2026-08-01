#!/usr/bin/env python3
"""Pull the dated first-person Process/Questions blocks out of cached jointaro pages."""
import html
import json
import os
import re
import sys
import unicodedata

CACHE = "/workspace/harvest/.taro_cache"


def plain(h):
    h = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", h)
    h = re.sub(r"(?i)<br\s*/?>", "\n", h)
    h = re.sub(r"(?i)</(p|div|li|h[1-6]|section)>", "\n", h)
    h = re.sub(r"(?s)<[^>]+>", " ", h)
    h = html.unescape(h)
    h = unicodedata.normalize("NFKC", h)
    h = re.sub(r"[ \t]+", " ", h)
    h = re.sub(r"\n\s*\n+", "\n", h)
    return h.strip()


def section(txt, head, stops):
    m = re.search(r"(?im)^\s*%s\s*$" % re.escape(head), txt)
    if not m:
        return ""
    rest = txt[m.end():]
    end = len(rest)
    for s in stops:
        mm = re.search(r"(?im)^\s*%s\s*$" % re.escape(s), rest)
        if mm:
            end = min(end, mm.start())
    return rest[:end].strip()


def main():
    idx = {}
    p = os.path.join(CACHE, "index.tsv")
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            k, _, u = line.rstrip("\n").partition("\t")
            idx[k] = u
    out = []
    for fn in sorted(os.listdir(CACHE)):
        if not fn.endswith(".html"):
            continue
        key = fn[:-5]
        url = idx.get(key, "")
        txt = plain(open(os.path.join(CACHE, fn), encoding="utf-8", errors="replace").read())
        title = ""
        m = re.search(r"(?m)^#?\s*(.+? Interview Experience.*?)$", txt)
        if m:
            title = m.group(1).strip()
        proc = section(txt, "Process", ["Questions", "Was this helpful?", "Interview Statistics"])
        ques = section(txt, "Questions", ["Was this helpful?", "Interview Statistics",
                                          "Process", "Advice"])
        date = ""
        md = re.search(r"(?m)^\s*((?:January|February|March|April|May|June|July|August|September|"
                       r"October|November|December) \d{1,2}, \d{4})\s*$", txt)
        if md:
            date = md.group(1)
        if not (proc or ques):
            continue
        out.append(dict(url=url, title=title, date=date, process=proc[:3000], questions=ques[:3000]))
    json.dump(out, open("/workspace/harvest/raw/_tiera_discover/taro_extracted.json", "w",
                        encoding="utf-8"), ensure_ascii=False, indent=1)
    print("extracted", len(out))

    # Surface only the entries that actually recount a question.
    sig = re.compile(r"asked|question|problem|OA|probability|expected|market|estimat|dice|coin|"
                     r"card|puzzle|brainteaser|mental math|leetcode|implement|write a|design",
                     re.I)
    keep = [o for o in out if sig.search(o["process"] + " " + o["questions"])]
    print("with question signal:", len(keep))
    if len(sys.argv) > 1 and sys.argv[1] == "--dump":
        for o in keep:
            print("\n" + "=" * 100)
            print(o["title"], "|", o["date"])
            print(o["url"])
            if o["process"]:
                print("-- PROCESS:", o["process"][:1400])
            if o["questions"]:
                print("-- QUESTIONS:", o["questions"][:1400])


if __name__ == "__main__":
    main()
