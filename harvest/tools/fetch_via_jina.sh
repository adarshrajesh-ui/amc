#!/bin/bash
# Pull Cloudflare-fronted pages through the r.jina.ai text proxy, with backoff.
# Writes into the verifier cache so verify_quotes.py picks them up.
CACHE=/workspace/harvest/.verify_cache
mkdir -p "$CACHE"
while read -r url; do
  [ -z "$url" ] && continue
  key=$(python3 -c "import re,sys;print(re.sub(r'[^A-Za-z0-9]+','_',sys.argv[1])[:150])" "$url")
  out="$CACHE/$key.txt"
  if [ -s "$out" ] && [ "$(stat -c%s "$out")" -gt 20000 ]; then
    echo "SKIP (cached $(stat -c%s "$out")B) $url"; continue
  fi
  for attempt in 1 2 3 4; do
    code=$(timeout 90 curl -sL --max-time 85 -A "Mozilla/5.0" \
             -w "%{http_code}" -o "$out.tmp" "https://r.jina.ai/$url")
    sz=$(stat -c%s "$out.tmp" 2>/dev/null || echo 0)
    if [ "$code" = "200" ] && [ "$sz" -gt 20000 ]; then
      mv "$out.tmp" "$out"; echo "OK   ${sz}B  $url"; break
    fi
    echo "  retry $attempt (http=$code size=$sz) $url"
    sleep $((attempt * 20))
  done
  rm -f "$out.tmp"
  sleep 8
done
