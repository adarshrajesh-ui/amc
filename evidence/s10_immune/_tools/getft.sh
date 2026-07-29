#!/usr/bin/env bash
# Fetch full text for a PMCID. Tries Europe PMC fullTextXML, then PMC efetch.
# Usage: getft.sh PMC11753884 outfile
set -uo pipefail
ID="$1"; OUT="$2"
curl -s --max-time 90 "https://www.ebi.ac.uk/europepmc/webservices/rest/${ID}/fullTextXML" -o "/tmp/${ID}.xml"
SZ=$(wc -c < "/tmp/${ID}.xml")
if [ "$SZ" -gt 5000 ]; then
  python3 - "$ID" "$OUT" <<'PY'
import re, sys, html
pmcid, out = sys.argv[1], sys.argv[2]
raw = open(f"/tmp/{pmcid}.xml", encoding="utf-8", errors="replace").read()
raw = re.sub(r"<(table-wrap|graphic|inline-graphic)\b[^>]*/>", " ", raw)
# keep table content as text
txt = re.sub(r"<[^>]+>", " ", raw)
txt = html.unescape(txt)
txt = re.sub(r"[ \t]+", " ", txt)
txt = re.sub(r"\n\s*\n+", "\n", txt)
open(out, "w", encoding="utf-8").write(txt)
print(f"OK europepmc {pmcid} -> {out} ({len(txt)} chars)")
PY
else
  echo "europepmc miss ($SZ bytes) for $ID"
fi
