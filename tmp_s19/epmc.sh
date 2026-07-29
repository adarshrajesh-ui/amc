#!/bin/bash
# usage: epmc.sh "query"  -> search Europe PMC for OA fulltext availability
Q=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$1")
curl -s -m 40 "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=$Q&resultType=core&format=json&pageSize=5" | jq -r '.resultList.result[]? | "ID:\(.id) SRC:\(.source) PMID:\(.pmid // "-") PMCID:\(.pmcid // "-") OA:\(.isOpenAccess) FULLTEXT:\(.hasTextMinedTerms // "-") TITLE:\(.title)"'
