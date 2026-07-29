"""Validate every YAML record in this shard against /workspace/spec/effect.schema.json."""
from __future__ import annotations

import glob
import json
import os
import sys

try:
    import yaml
except ImportError:
    sys.exit("pyyaml missing: pip install pyyaml")

try:
    from jsonschema import Draft7Validator
except ImportError:
    Draft7Validator = None

SCHEMA = json.load(open("/workspace/spec/effect.schema.json"))
REQ_TOP = SCHEMA["required"]
REQ_EFFECT = SCHEMA["properties"]["effects"]["items"]["required"]

n_ok = n_bad = 0
total_effects = 0
tiers: dict[str, int] = {}

validator = Draft7Validator(SCHEMA) if Draft7Validator else None

for path in sorted(glob.glob("/workspace/evidence/s12_psychiatric/*.yaml")):
    name = os.path.basename(path)
    try:
        rec = yaml.safe_load(open(path, encoding="utf-8"))
    except Exception as exc:
        print("YAML PARSE FAIL %-24s %s" % (name, exc))
        n_bad += 1
        continue

    errors: list[str] = []
    if validator:
        for e in sorted(validator.iter_errors(rec), key=lambda e: list(e.path)):
            errors.append("/".join(str(p) for p in e.path) + ": " + e.message)
    else:
        for k in REQ_TOP:
            if k not in rec:
                errors.append("missing required top-level key: " + k)
        for i, eff in enumerate(rec.get("effects") or []):
            for k in REQ_EFFECT:
                if k not in eff:
                    errors.append("effects/%d missing required key: %s" % (i, k))

    # my own additional checks beyond the schema
    if rec.get("study_id") != os.path.splitext(name)[0]:
        errors.append("study_id '%s' != filename" % rec.get("study_id"))
    for i, eff in enumerate(rec.get("effects") or []):
        ci = eff.get("ci")
        if ci and eff.get("value") is not None:
            if not (ci[0] - 1e-6 <= eff["value"] <= ci[1] + 1e-6):
                errors.append("effects/%d: value %s outside its own CI %s" % (i, eff["value"], ci))
        if ci and ci[0] > ci[1]:
            errors.append("effects/%d: CI bounds reversed %s" % (i, ci))
        if eff.get("se") is not None and eff["se"] < 0:
            errors.append("effects/%d: negative se" % i)
        if not eff.get("quote"):
            errors.append("effects/%d: no quote" % i)
    total_effects += len(rec.get("effects") or [])
    t = rec.get("tier")
    tiers[t] = tiers.get(t, 0) + 1

    if errors:
        n_bad += 1
        print("FAIL %-24s" % name)
        for e in errors:
            print("      - " + e)
    else:
        n_ok += 1
        print("ok   %-24s tier=%-3s effects=%-2d n=%s" % (name, t, len(rec.get("effects") or []),
                                                          rec.get("n")))

print("\n==== %d valid, %d invalid, %d total effect estimates ====" % (n_ok, n_bad, total_effects))
print("tier distribution:", dict(sorted(tiers.items(), key=lambda kv: str(kv[0]))))
print("jsonschema available:", bool(validator))
