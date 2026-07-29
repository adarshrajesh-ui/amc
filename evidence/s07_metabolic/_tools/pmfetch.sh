#!/usr/bin/env bash
# Helpers for verified PubMed / Crossref retrieval. Shard s07_metabolic.
set -uo pipefail

pmsearch() {  # pmsearch "<query>" [retmax]
  local q="$1"; local rm="${2:-15}"
  curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json&retmax=${rm}&term=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$q")" \
   | python3 -c "import json,sys; d=json.load(sys.stdin)['esearchresult']; print('COUNT',d.get('count')); print('\n'.join(d.get('idlist',[])))"
}

pmsum() {  # pmsum <pmid,pmid,...>
  curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id=$1" \
   | python3 -c "
import json,sys
d=json.load(sys.stdin)['result']
for u in d['uids']:
    r=d[u]
    ids={i['idtype']:i['value'] for i in r.get('articleids',[])}
    print('PMID',u,'|',r.get('pubdate'),'|',r.get('source'),'|',ids.get('doi'))
    print('   ',r.get('title'))
    print('   AUTH:', '; '.join(a['name'] for a in r.get('authors',[])[:6]))
    print()
"
}

pmabs() {  # pmabs <pmid>
  curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=text&rettype=abstract&id=$1"
}

crossref() {  # crossref <doi>
  curl -s "https://api.crossref.org/works/$1" | python3 -c "
import json,sys
try:
    m=json.load(sys.stdin)['message']
except Exception as e:
    print('CROSSREF_FAIL', e); sys.exit(0)
print('CR_OK title:', (m.get('title') or ['?'])[0])
print('   journal:', (m.get('container-title') or ['?'])[0], '| year:', m.get('issued',{}).get('date-parts'))
print('   vol/page:', m.get('volume'), m.get('page'))
"
}
export -f pmsearch pmsum pmabs crossref 2>/dev/null || true
