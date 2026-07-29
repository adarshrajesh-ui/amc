#!/usr/bin/env python3
"""HTML -> plain text, for reading retrieved full texts. Usage: python3 h2t.py in.html out.txt"""
import html
import pathlib
import re
import sys

raw = pathlib.Path(sys.argv[1]).read_text(errors="ignore")
raw = re.sub(r"(?is)<(script|style|noscript|svg)[^>]*>.*?</\1>", " ", raw)
raw = re.sub(r"(?i)</(p|div|li|tr|h[1-6]|section|br)>", "\n", raw)
raw = re.sub(r"(?i)<br\s*/?>", "\n", raw)
txt = re.sub(r"(?s)<[^>]+>", " ", raw)
txt = html.unescape(txt)
txt = txt.replace("\u2009", " ").replace("\u202f", " ").replace("\xa0", " ")
txt = re.sub(r"[ \t]+", " ", txt)
txt = re.sub(r"\n[ \t]*", "\n", txt)
txt = re.sub(r"\n{3,}", "\n\n", txt)
out = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else sys.argv[1] + ".txt")
out.write_text(txt)
print("wrote %s  (%d chars)" % (out, len(txt)))
