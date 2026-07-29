#!/bin/bash
# usage: pmc.sh PMCID outfile
curl -s -m 90 "https://www.ebi.ac.uk/europepmc/webservices/rest/$1/fullTextXML" -o "$2.xml"
python3 - "$2.xml" "$2.txt" <<'PY'
import sys,re,xml.etree.ElementTree as ET
src,dst=sys.argv[1],sys.argv[2]
raw=open(src,encoding='utf-8',errors='replace').read()
if len(raw)<500:
    print("NO FULLTEXT (len=%d)"%len(raw)); sys.exit(0)
try:
    t=ET.fromstring(raw)
except Exception as e:
    print("parse fail",e); sys.exit(1)
def txt(e):
    return ''.join(e.itertext())
out=[]
for sec in t.iter():
    pass
body=t.find('.//body')
front=t.find('.//front')
if front is not None: out.append("### FRONT\n"+re.sub(r'\n{3,}','\n\n',txt(front)))
if body is not None: out.append("### BODY\n"+re.sub(r'\n{3,}','\n\n',txt(body)))
open(dst,'w',encoding='utf-8').write('\n\n'.join(out))
print("WROTE",dst,len(open(dst,encoding='utf-8').read()),"chars")
PY
