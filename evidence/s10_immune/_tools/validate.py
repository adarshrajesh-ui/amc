"""Validate every YAML record in the shard against /workspace/spec/effect.schema.json.

Also runs extra internal checks the schema cannot express:
  - every effect carries a non-empty `quote`
  - ci bounds bracket the point value when both are present
  - se is consistent with ci width when both are present (log/SMD scales)
  - verification block agrees with _tools/verification.json
"""
import glob
import json
import math
import os
import sys

import yaml
from jsonschema import Draft7Validator

SPEC = "/workspace/spec/effect.schema.json"
SHARD = "/workspace/evidence/s10_immune"

schema = json.load(open(SPEC))
validator = Draft7Validator(schema)
ver = json.load(open(os.path.join(SHARD, "_tools", "verification.json")))

files = sorted(glob.glob(os.path.join(SHARD, "*.yaml")))
n_effects = 0
problems = []

for path in files:
    name = os.path.basename(path)
    rec = yaml.safe_load(open(path, encoding="utf-8"))
    errs = sorted(validator.iter_errors(rec), key=lambda e: e.path)
    for e in errs:
        problems.append(f"{name}: SCHEMA {list(e.path)}: {e.message}")

    if rec.get("study_id") != name[: -len(".yaml")]:
        problems.append(f"{name}: study_id '{rec.get('study_id')}' != filename")

    # verification cross-check
    sid = rec.get("study_id")
    if sid in ver:
        v = ver[sid]
        rv = rec.get("verification", {})
        for k in ("crossref_ok", "pubmed_ok"):
            if rv.get(k) != v.get(k):
                problems.append(f"{name}: verification.{k}={rv.get(k)} but verify.py got {v.get(k)}")
        if rv.get("status") != v.get("status"):
            problems.append(f"{name}: verification.status mismatch")
        if str(rec.get("pmid")) != str(v.get("pmid")):
            problems.append(f"{name}: pmid {rec.get('pmid')} != verified {v.get('pmid')}")
        if (rec.get("doi") or "").lower() != (v.get("doi") or "").lower():
            problems.append(f"{name}: doi mismatch vs verification.json")
    else:
        problems.append(f"{name}: study_id not present in verification.json")

    for i, eff in enumerate(rec.get("effects", [])):
        n_effects += 1
        tag = f"{name}[effect {i}] {eff.get('outcome_construct')}"
        q = eff.get("quote")
        if not q or not str(q).strip():
            problems.append(f"{tag}: MISSING QUOTE")
        val, se, ci = eff.get("value"), eff.get("se"), eff.get("ci")
        if ci is not None and val is not None:
            lo, hi = ci
            if not (lo - 1e-6 <= val <= hi + 1e-6):
                problems.append(f"{tag}: value {val} outside ci {ci}")
        if ci is not None and se not in (None, 0):
            implied = (ci[1] - ci[0]) / 3.92
            if implied > 0 and abs(implied - se) / max(se, 1e-9) > 0.12:
                problems.append(
                    f"{tag}: se {se} vs (hi-lo)/3.92 = {implied:.4f} (>12% apart)")
        if eff.get("scale") in ("log_or", "log_rr", "log_hr") and val is not None:
            if abs(val) > 5:
                problems.append(f"{tag}: log-scale value {val} implausible (ratio {math.exp(val):.1f})")

print(f"files validated : {len(files)}")
print(f"effects total   : {n_effects}")
if problems:
    print(f"\nPROBLEMS ({len(problems)}):")
    for p in problems:
        print("  !!", p)
    sys.exit(1)
print("\nALL RECORDS VALID against effect.schema.json + internal consistency checks.")
