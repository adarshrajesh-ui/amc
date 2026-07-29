#!/usr/bin/env bash
# helper: pubmed search -> pmid list + titles
# usage: ./search.sh "adolescent sleep duration brain structure" [retmax]
q="$1"; rm_ax="${2:-12}"
enc=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote_plus(sys.argv[1]))" "$q")
ids=$(curl -s --max-time 40 "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json&retmax=${rm_ax}&term=${enc}" \
  | python3 -c "
import json,sys
try:
    d=json.load(sys.stdin)
    print(','.join(d['esearchresult'].get('idlist',[])))
except Exception:
    print('')
")
echo "== QUERY: $q"
if [ -z "$ids" ]; then echo "   (no hits)"; exit 0; fi
curl -s --max-time 40 "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id=${ids}" \
 | python3 -c "
import json,sys
try:
    d=json.load(sys.stdin)['result']
except Exception as e:
    print('   (esummary parse fail)'); raise SystemExit(0)
for u in d.get('uids',[]):
    r=d[u]
    doi=''
    for aid in r.get('articleids',[]):
        if aid['idtype']=='doi': doi=aid['value']
    print(f\"{u}\t{r.get('pubdate','')[:4]}\t{r.get('source','')}\tDOI:{doi}\t{r.get('title','')[:150]}\")
"
