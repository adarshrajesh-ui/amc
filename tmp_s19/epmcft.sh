#!/bin/bash
Q=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$1")
curl -s -m 40 "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=$Q&format=json&pageSize=8" | jq -r '.hitCount as $h | "HITS: \($h)", (.resultList.result[]? | "ID:\(.id) PMID:\(.pmid // "-") PMCID:\(.pmcid // "-") OA:\(.isOpenAccess) \(.title)")'
