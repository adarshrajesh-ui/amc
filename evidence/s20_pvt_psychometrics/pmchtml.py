#!/usr/bin/env python3
"""Fetch a PMC article's rendered HTML (works for non-OA PMC deposits where the
BioC and Europe PMC XML APIs refuse) and flatten it to plain text."""
import html
import re
import sys
import urllib.request

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")


def fetch(pmcid: str) -> str:
    url = f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/"
    req = urllib.request.Request(url, headers={"User-Agent": UA,
                                              "Accept": "text/html,application/xhtml+xml"})
    with urllib.request.urlopen(req, timeout=120) as fh:
        return fh.read().decode("utf-8", "replace")


def flatten(doc: str) -> str:
    doc = re.sub(r"<script.*?</script>", " ", doc, flags=re.S | re.I)
    doc = re.sub(r"<style.*?</style>", " ", doc, flags=re.S | re.I)
    # keep table/paragraph structure as line breaks so numbers stay adjacent to labels
    doc = re.sub(r"</(p|div|tr|h1|h2|h3|h4|li|caption|title)>", "\n", doc, flags=re.I)
    doc = re.sub(r"</t[dh]>", " | ", doc, flags=re.I)
    doc = re.sub(r"<[^>]+>", " ", doc)
    doc = html.unescape(doc)
    doc = re.sub(r"[ \t]+", " ", doc)
    doc = re.sub(r"\n[ \t]*", "\n", doc)
    doc = re.sub(r"\n{3,}", "\n\n", doc)
    return doc.strip()


if __name__ == "__main__":
    pmcid = sys.argv[1]
    dest = sys.argv[2] if len(sys.argv) > 2 else f"/tmp/{pmcid}_pmc.txt"
    body = flatten(fetch(pmcid))
    with open(dest, "w") as fh:
        fh.write(body)
    print(f"{dest}  chars={len(body)}")
