#!/bin/bash
# usage: pmchtml.sh PMCID outbase
curl -sL -m 90 -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36" "https://pmc.ncbi.nlm.nih.gov/articles/$1/" -o "$2.html"
python3 - "$2.html" "$2.txt" <<'PY'
import sys,re,html
src,dst=sys.argv[1],sys.argv[2]
raw=open(src,encoding='utf-8',errors='replace').read()
raw=re.sub(r'(?is)<(script|style|nav|header|footer)[^>]*>.*?</\1>','',raw)
txt=re.sub(r'(?s)<[^>]+>',' ',raw); txt=html.unescape(txt)
txt=re.sub(r'[ \t]+',' ',txt); txt=re.sub(r'\n\s*\n+','\n',txt)
open(dst,'w').write(txt); print("WROTE",dst,len(txt))
PY
