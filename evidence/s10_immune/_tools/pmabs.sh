#!/usr/bin/env bash
# Helper: fetch PubMed abstracts as text. Usage: pmabs.sh PMID[,PMID,...]
set -euo pipefail
IDS="$1"
curl -s --max-time 60 "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=text&rettype=abstract&id=${IDS}"
