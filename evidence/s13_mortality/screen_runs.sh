#!/bin/bash
# Re-run the canonical searches for this shard and archive the hit lists so the
# screening log is grounded in records actually retrieved.
cd "$(dirname "$0")" || exit 1
OUT=search_hits.txt
: > "$OUT"
run() { echo "===== $1" >> "$OUT"; python3 pm.py search "$1" "${2:-25}" >> "$OUT" 2>&1; }

run "sleep duration AND all-cause mortality AND (meta-analysis[pt] OR meta-analysis[tiab])" 30
run "\"sleep duration\"[tiab] AND mortality[tiab] AND \"dose-response\"[tiab]" 25
run "accelerometer[tiab] AND sleep[tiab] AND mortality[tiab] AND \"UK Biobank\"[tiab]" 25
run "actigraphy[tiab] AND sleep[tiab] AND mortality[tiab]" 25
run "\"Mendelian randomization\"[tiab] AND \"sleep duration\"[tiab] AND (mortality[tiab] OR lifespan[tiab] OR longevity[tiab])" 25
run "\"weekend\"[tiab] AND sleep[tiab] AND mortality[tiab]" 20
run "\"catch-up sleep\"[tiab] OR \"sleep rebound\"[tiab] AND mortality[tiab]" 20
run "sleep[tiab] AND mortality[tiab] AND (\"reverse causation\"[tiab] OR \"reverse causality\"[tiab])" 25
run "\"sleep duration\"[tiab] AND mortality[tiab] AND (\"age\"[tiab] AND (\"effect modification\"[tiab] OR \"stratified\"[tiab] OR \"younger\"[tiab]))" 25
run "(childhood[tiab] OR adolescen*[tiab]) AND \"sleep duration\"[tiab] AND (mortality[tiab] OR lifespan[tiab] OR longevity[tiab])" 25
run "\"sleep duration\"[tiab] AND mortality[tiab] AND (trajector*[tiab] OR \"change in sleep\"[tiab] OR \"sleep change\"[tiab])" 25
run "polysomnograph*[tiab] AND \"sleep duration\"[tiab] AND mortality[tiab]" 20
wc -l "$OUT"
