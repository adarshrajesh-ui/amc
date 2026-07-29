#!/usr/bin/env bash
# fetch PMC OA full text as plain text. usage: ./pmc.sh PMC5299428
id="${1#PMC}"
curl -s --max-time 90 "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&retmode=xml&id=${id}" \
 | python3 -c "
import sys,xml.etree.ElementTree as ET
raw=sys.stdin.read()
try:
    r=ET.fromstring(raw)
except Exception as e:
    print('PARSE FAIL:', e); print(raw[:800]); raise SystemExit(0)
def txt(e):
    return ''.join(e.itertext())
body=r.find('.//body')
if body is None:
    print('(no OA body available for this PMC id)')
    ab=r.find('.//abstract')
    if ab is not None: print(txt(ab))
    raise SystemExit(0)
for el in body.iter():
    if el.tag in ('title',):
        s=txt(el).strip()
        if s: print('\n### '+s)
    elif el.tag=='p':
        s=' '.join(txt(el).split())
        if s: print(s)
# tables & captions
print('\n\n@@@@@@@@@@ TABLES / CAPTIONS @@@@@@@@@@')
for tw in r.iter('table-wrap'):
    lab=tw.findtext('label') or ''
    cap=' '.join(txt(tw.find('caption')).split()) if tw.find('caption') is not None else ''
    print(f'\n--- {lab}: {cap}')
    for tb in tw.iter('table'):
        for tr in tb.iter('tr'):
            cells=[' '.join(txt(c).split()) for c in tr]
            print(' | '.join(cells))
for fg in r.iter('fig'):
    lab=fg.findtext('label') or ''
    cap=' '.join(txt(fg.find('caption')).split()) if fg.find('caption') is not None else ''
    print(f'\n--- {lab}: {cap}')
"
