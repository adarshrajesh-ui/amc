#!/usr/bin/env python3
"""Fetch PMC full text via the NCBI BioC API (works for author manuscripts) and flatten to text."""
import sys
import urllib.request
import xml.etree.ElementTree as ET

BASE = "https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/{}/unicode"


def fetch(pmcid: str) -> str:
    url = BASE.format(pmcid)
    req = urllib.request.Request(url, headers={"User-Agent": "evidence-extraction/1.0"})
    with urllib.request.urlopen(req, timeout=90) as fh:
        return fh.read().decode("utf-8", "replace")


def flatten(xml_text: str) -> str:
    root = ET.fromstring(xml_text)
    out = []
    for passage in root.iter("passage"):
        section = ""
        for infon in passage.findall("infon"):
            if infon.get("key") in ("section_type", "type"):
                section = f"[{infon.text}] "
        text_el = passage.find("text")
        if text_el is not None and text_el.text:
            out.append(section + text_el.text)
    return "\n\n".join(out)


if __name__ == "__main__":
    pmcid = sys.argv[1]
    dest = sys.argv[2] if len(sys.argv) > 2 else f"/tmp/{pmcid}.txt"
    body = flatten(fetch(pmcid))
    with open(dest, "w") as fh:
        fh.write(body)
    print(f"{dest}  chars={len(body)}")
