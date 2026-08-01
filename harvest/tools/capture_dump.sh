#!/bin/bash
# Copy a WebSearch full-page-text dump into the verifier cache under its URL key,
# so verify_quotes.py can check quotes against the exact bytes I actually read.
# usage: capture_dump.sh <agent-tools-file> <url>
set -e
SRC="$1"; URL="$2"
CACHE=/workspace/harvest/.verify_cache
mkdir -p "$CACHE"
KEY=$(python3 -c "import re,sys;print(re.sub(r'[^A-Za-z0-9]+','_',sys.argv[1])[:150])" "$URL")
cp "$SRC" "$CACHE/$KEY.txt"
printf '%s\t%s\n' "$URL" "$CACHE/$KEY.txt" >> "$CACHE/_dumped.tsv"
echo "captured $(stat -c%s "$CACHE/$KEY.txt")B -> $KEY.txt"
