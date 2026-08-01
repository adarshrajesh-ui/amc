#!/bin/bash
# Fetch nowcoder discussion threads (IDs on stdin) into the verifier cache.
# nowcoder serves the full post body inside its SSR payload, so plain curl is enough.
CACHE=/workspace/harvest/.verify_cache
mkdir -p "$CACHE"
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122 Safari/537.36"
n=0; ok=0
while read -r id; do
  [ -z "$id" ] && continue
  url="https://www.nowcoder.com/discuss/$id"
  key=$(python3 -c "import re,sys;print(re.sub(r'[^A-Za-z0-9]+','_',sys.argv[1])[:150])" "$url")
  out="$CACHE/$key.txt"
  if [ -s "$out" ] && [ "$(stat -c%s "$out")" -gt 6000 ]; then continue; fi
  timeout 40 curl -sL --max-time 35 -A "$UA" -H "Accept-Language: zh-CN,zh;q=0.9" "$url" -o "$out"
  sz=$(stat -c%s "$out" 2>/dev/null || echo 0)
  n=$((n+1))
  if [ "$sz" -gt 6000 ]; then ok=$((ok+1)); echo "OK ${sz}B $url"; else echo "SMALL ${sz}B $url"; fi
  sleep 0.6
done
echo "nowcoder done: $n fetched, $ok usable"
