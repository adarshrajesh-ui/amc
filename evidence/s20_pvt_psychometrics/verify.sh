#!/usr/bin/env bash
# Identifier verification helper for shard s20_pvt_psychometrics.
# Usage: ./verify.sh doi <DOI>   |   ./verify.sh pmid <PMID>   |   ./verify.sh search "<query>"
set -uo pipefail
case "${1:-}" in
  doi)
    curl -s --max-time 30 "https://api.crossref.org/works/$2" \
      | python3 -c 'import json,sys;d=json.load(sys.stdin)["message"];print("TITLE:",d.get("title"));print("CONTAINER:",d.get("container-title"));print("YEAR:",d.get("issued",{}).get("date-parts"));print("TYPE:",d.get("type"));print("AUTH:",[a.get("family") for a in d.get("author",[])][:8])' 2>/dev/null \
      || echo "CROSSREF_FAIL"
    ;;
  pmid)
    curl -s --max-time 30 "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id=$2" \
      | python3 -c 'import json,sys;r=json.load(sys.stdin)["result"];k=r["uids"][0];d=r[k];print("TITLE:",d.get("title"));print("SOURCE:",d.get("source"),d.get("pubdate"));print("AUTH:",[a["name"] for a in d.get("authors",[])][:8]);print("IDS:",[(x["idtype"],x["value"]) for x in d.get("articleids",[])])' 2>/dev/null \
      || echo "PUBMED_FAIL"
    ;;
  search)
    curl -s --max-time 30 --data-urlencode "term=$2" \
      "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json&retmax=15" -G \
      | python3 -c 'import json,sys;d=json.load(sys.stdin)["esearchresult"];print("COUNT:",d.get("count"));print(" ".join(d.get("idlist",[])))'
    ;;
  summ)
    shift
    curl -s --max-time 30 "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id=$(echo "$@" | tr ' ' ',')" \
      | python3 -c '
import json,sys
r=json.load(sys.stdin)["result"]
for k in r["uids"]:
    d=r[k]
    print(k,"|",d.get("source"),d.get("pubdate"),"|",d.get("title"))
'
    ;;
  abst)
    shift
    curl -s --max-time 40 "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=text&rettype=abstract&id=$(echo "$@" | tr ' ' ',')"
    ;;
  *) echo "usage: verify.sh {doi|pmid|search|summ|abst} ARG"; exit 1;;
esac
