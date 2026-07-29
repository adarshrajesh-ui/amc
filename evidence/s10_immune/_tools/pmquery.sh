#!/usr/bin/env bash
# Helper: PubMed esearch -> esummary titles. Usage: pmquery.sh "query string" [retmax]
set -euo pipefail
Q="$1"
RETMAX="${2:-12}"
ENC=$(python3 -c "import urllib.parse,sys; print(urllib.parse.quote_plus(sys.argv[1]))" "$Q")
IDS=$(curl -s --max-time 40 "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json&retmax=${RETMAX}&term=${ENC}" \
  | python3 -c "import json,sys; d=json.load(sys.stdin); print(','.join(d['esearchresult'].get('idlist',[])))")
if [ -z "$IDS" ]; then echo "NO HITS for: $Q"; exit 0; fi
echo "### QUERY: $Q"
curl -s --max-time 40 "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id=${IDS}" \
 | python3 -c "
import json,sys
d=json.load(sys.stdin)['result']
for u in d['uids']:
    r=d[u]
    doi=''
    for aid in r.get('articleids',[]):
        if aid.get('idtype')=='doi': doi=aid.get('value','')
    la=r.get('lastauthor','')
    fa=r.get('sortfirstauthor','')
    print(f\"PMID {u} | {r.get('pubdate','')} | {r.get('source','')} | {fa} ... {la} | DOI {doi}\")
    print(f\"    {r.get('title','')}\")
"
