#!/bin/bash
# usage: pmabs.sh PMID
curl -s -m 60 "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=xml&rettype=abstract&id=$1" | python3 -c "
import sys,xml.etree.ElementTree as ET
t=ET.fromstring(sys.stdin.read())
for a in t.iter('PubmedArticle'):
    art=a.find('.//Article')
    print('PMID:', a.findtext('.//PMID'))
    print('TITLE:', ''.join(art.find('ArticleTitle').itertext()) if art.find('ArticleTitle') is not None else None)
    j=art.findtext('.//Journal/Title'); print('JOURNAL:', j)
    print('YEAR:', art.findtext('.//JournalIssue/PubDate/Year'), 'VOL:', art.findtext('.//JournalIssue/Volume'), 'ISSUE:', art.findtext('.//JournalIssue/Issue'), 'PAGES:', art.findtext('.//Pagination/MedlinePgn') or art.findtext('.//ELocationID'))
    for i in a.iter('ArticleId'):
        print('ID[%s]:'%i.get('IdType'), i.text)
    auth=[]
    for au in a.iter('Author'):
        ln=au.findtext('LastName'); ini=au.findtext('Initials')
        if ln: auth.append(ln+' '+(ini or ''))
    print('AUTHORS:', '; '.join(auth))
    print('ABSTRACT:')
    for ab in a.iter('AbstractText'):
        lab=ab.get('Label')
        print(('['+lab+'] ' if lab else '')+''.join(ab.itertext()))
    print('GRANTS:', '; '.join(set(g.findtext('Agency') or '' for g in a.iter('Grant'))))
    print('='*100)
"
