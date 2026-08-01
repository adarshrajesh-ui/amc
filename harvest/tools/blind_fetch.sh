#!/bin/bash
# teamblind.com answers plain curl with the whole thread (post + comments) in the HTML,
# so it needs no proxy. URLs on stdin, one per line.
CACHE=/workspace/harvest/.verify_cache
mkdir -p "$CACHE"
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122 Safari/537.36"
ok=0; n=0
while read -r url; do
  [ -z "$url" ] && continue
  key=$(python3 -c "import re,sys;print(re.sub(r'[^A-Za-z0-9]+','_',sys.argv[1])[:150])" "$url")
  out="$CACHE/$key.txt"
  n=$((n+1))
  if [ -s "$out" ] && [ "$(stat -c%s "$out")" -gt 50000 ]; then echo "SKIP $url"; ok=$((ok+1)); continue; fi
  timeout 45 curl -sL --max-time 40 --compressed -A "$UA" "$url" -o "$out"
  sz=$(stat -c%s "$out" 2>/dev/null || echo 0)
  if [ "$sz" -gt 50000 ]; then ok=$((ok+1)); echo "OK ${sz}B $url"; else echo "SMALL ${sz}B $url"; fi
  sleep 0.8
done
echo "blind done: $n tried, $ok usable"
