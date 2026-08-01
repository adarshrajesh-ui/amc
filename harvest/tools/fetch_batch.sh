#!/bin/bash
# Fetch a list of URLs through r.jina.ai into the verifier cache, with backoff.
CACHE=/workspace/harvest/.verify_cache
mkdir -p "$CACHE"
while read -r url; do
  [ -z "$url" ] && continue
  key=$(python3 -c "import re,sys;print(re.sub(r'[^A-Za-z0-9]+','_',sys.argv[1])[:150])" "$url")
  out="$CACHE/$key.txt"
  if [ -s "$out" ] && [ "$(stat -c%s "$out")" -gt 15000 ]; then
    echo "SKIP $url"; continue
  fi
  for a in 1 2 3; do
    code=$(timeout 100 curl -sL --max-time 95 -A "Mozilla/5.0" -w "%{http_code}" -o "$out.tmp" "https://r.jina.ai/$url")
    sz=$(stat -c%s "$out.tmp" 2>/dev/null || echo 0)
    if [ "$code" = "200" ] && [ "$sz" -gt 8000 ]; then
      mv "$out.tmp" "$out"; echo "OK ${sz}B $url"; break
    fi
    echo "  retry $a (http=$code sz=$sz) $url"; sleep $((a*15))
  done
  rm -f "$out.tmp"; sleep 6
done
echo ALLDONE
