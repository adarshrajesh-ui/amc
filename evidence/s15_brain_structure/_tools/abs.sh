#!/usr/bin/env bash
# fetch full pubmed abstract(s) as text. usage: ./abs.sh 28181512 32015467
# NOTE: DOI/PMC taken ONLY from PubmedData/ArticleIdList (the article's own ids),
# never from reference lists (which also contain <ArticleId> nodes).
ids=$(echo "$@" | tr ' ' ',')
curl -s --max-time 60 "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=xml&id=${ids}" \
 | python3 -c "
import sys,xml.etree.ElementTree as ET
t=ET.parse(sys.stdin); r=t.getroot()
for art in r.iter('PubmedArticle'):
    pmid=art.findtext('./MedlineCitation/PMID')
    tn=art.find('.//ArticleTitle')
    ti=''.join(tn.itertext()) if tn is not None else ''
    jr=art.findtext('.//Journal/ISOAbbreviation') or ''
    pd=art.find('.//JournalIssue/PubDate')
    yr=(pd.findtext('Year') or pd.findtext('MedlineDate') or '') if pd is not None else ''
    vol=art.findtext('.//JournalIssue/Volume') or ''
    iss=art.findtext('.//JournalIssue/Issue') or ''
    pg=art.findtext('.//Pagination/MedlinePgn') or art.findtext('.//Pagination/StartPage') or ''
    doi=pmc=''
    ail=art.find('./PubmedData/ArticleIdList')
    if ail is not None:
        for aid in ail.findall('ArticleId'):
            if aid.get('IdType')=='doi' and not doi: doi=(aid.text or '')
            if aid.get('IdType')=='pmc' and not pmc: pmc=(aid.text or '')
    auths=[]
    al=art.find('.//AuthorList')
    if al is not None:
        for a in al.findall('Author'):
            ln=a.findtext('LastName'); ini=a.findtext('Initials')
            if ln: auths.append((ln+' '+(ini or '')).strip())
    print('='*100)
    print(f'PMID: {pmid}   DOI: {doi}   PMC: {pmc}')
    print(f'TITLE: {ti}')
    print(f'JOURNAL: {jr}. {yr};{vol}({iss}):{pg}')
    print(f'AUTHORS ({len(auths)}): ' + '; '.join(auths[:16]) + (' ...' if len(auths)>16 else ''))
    pt=[p.text for p in art.iter('PublicationType')]
    print('PUBTYPES: ' + ', '.join([x for x in pt if x]))
    gl=[g.findtext('Agency') or '' for g in art.iter('Grant')]
    if gl: print('GRANTS: ' + '; '.join(sorted(set([g for g in gl if g]))[:8]))
    print('-'*100)
    ab=art.find('.//Abstract')
    if ab is not None:
        for a in ab.findall('AbstractText'):
            lab=a.get('Label')
            print((f'[{lab}] ' if lab else '') + ''.join(a.itertext()))
    else:
        print('(no abstract)')
    print()
"
