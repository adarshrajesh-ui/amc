#!/usr/bin/env bash
# getfull.sh <PMID> <slug>  -> tries PMC full text, writes <slug>.txt (falls back to abstract)
set -u
PMID="$1"; SLUG="$2"
D="$(cd "$(dirname "$0")" && pwd)"
sleep 0.7
PMCID=$(curl -s --max-time 60 \
  "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id=${PMID}" \
  | python3 -c '
import json,sys
try:
    d=json.load(sys.stdin)["result"]
except Exception:
    print(""); raise SystemExit
u=d["uids"][0]
out=""
for a in d[u].get("articleids",[]):
    if a.get("idtype")=="pmc": out=a["value"]
print(out.strip())')
echo "PMID $PMID -> PMC='$PMCID'"
if [ -n "$PMCID" ]; then
  sleep 1
  curl -sL --max-time 120 -A "Mozilla/5.0 (research)" \
    "https://pmc.ncbi.nlm.nih.gov/articles/${PMCID}/" -o "$D/${SLUG}.html"
  python3 "$D/h2t.py" "$D/${SLUG}.html" "$D/${SLUG}.txt"
  if [ "$(wc -c < "$D/${SLUG}.txt")" -lt 6000 ]; then
    echo "PMC text short -> appending abstract"
    python3 "$D/pm.py" abs "$PMID" >> "$D/${SLUG}.txt"
  fi
  rm -f "$D/${SLUG}.html"
else
  echo "no PMC id; falling back to abstract"
  python3 "$D/pm.py" abs "$PMID" > "$D/${SLUG}.txt"
fi
wc -c "$D/${SLUG}.txt"
