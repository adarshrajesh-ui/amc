#!/bin/bash
# Fetch jointaro interview-experience pages listed on stdin into a cache dir.
CACHE=/workspace/harvest/.taro_cache
mkdir -p "$CACHE"
n=0
while read -r url; do
  [ -z "$url" ] && continue
  key=$(printf '%s' "$url" | md5sum | cut -c1-16)
  out="$CACHE/$key.html"
  if [ -s "$out" ]; then continue; fi
  timeout 45 curl -sL --max-time 40 -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36" \
    "$url" -o "$out"
  printf '%s\t%s\n' "$key" "$url" >> "$CACHE/index.tsv"
  n=$((n+1))
  [ $((n % 25)) -eq 0 ] && echo "  fetched $n" >&2
  sleep 0.25
done
echo "done: $n new" >&2
