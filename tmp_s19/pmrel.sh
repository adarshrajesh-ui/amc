#!/bin/bash
# usage: pmrel.sh "query" [retmax]   -- PubMed search sorted by relevance
Q=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$1")
RM=${2:-10}
IDS=$(curl -s -m 40 "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json&sort=relevance&retmax=$RM&term=$Q" | jq -r 'try (.esearchresult.idlist | join(",")) catch ""')
if [ -z "$IDS" ] || [ "$IDS" = "null" ]; then echo "NO HITS"; exit 0; fi
curl -s -m 40 "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id=$IDS" | jq -r '.result as $r | $r.uids[] | "PMID \(.)\t\($r[.].pubdate)\t\($r[.].fulljournalname)\t\($r[.].title)"'
