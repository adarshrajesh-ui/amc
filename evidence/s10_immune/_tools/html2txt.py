import html
import re
import sys

for path in sys.argv[1:]:
    raw = open(path, encoding="utf-8", errors="replace").read()
    raw = re.sub(r"(?is)<(script|style|noscript|svg)\b.*?</\1>", " ", raw)
    body = re.search(r'(?is)<(?:article|main)\b.*?</(?:article|main)>', raw)
    if body:
        raw = body.group(0)
    raw = re.sub(r"(?i)</(p|div|tr|li|h[1-6]|section|table|caption)>", "\n", raw)
    raw = re.sub(r"(?i)</t[dh]>", " | ", raw)
    txt = re.sub(r"<[^>]+>", " ", raw)
    txt = html.unescape(txt)
    txt = re.sub(r"[ \t\xa0]+", " ", txt)
    txt = re.sub(r"\n\s*\n+", "\n", txt)
    out = path.rsplit(".", 1)[0] + ".txt"
    open(out, "w", encoding="utf-8").write(txt)
    print(f"{path} -> {out} ({len(txt)} chars)")
