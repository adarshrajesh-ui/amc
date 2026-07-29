#!/usr/bin/env python3
"""Validate every shard YAML record against /workspace/spec/effect.schema.json."""
import glob
import json
import os
import sys

try:
    import yaml
except ImportError:
    sys.exit("pyyaml missing: pip install pyyaml")
try:
    import jsonschema
except ImportError:
    jsonschema = None

SCHEMA = json.load(open("/workspace/spec/effect.schema.json"))
here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

fail = 0
n_eff = 0
files = sorted(f for f in glob.glob(os.path.join(here, "*.yaml")))
for f in files:
    doc = yaml.safe_load(open(f))
    errs = []
    if jsonschema:
        v = jsonschema.Draft7Validator(SCHEMA)
        errs = [f"{list(e.path)}: {e.message}" for e in v.iter_errors(doc)]
    # extra hand checks the schema cannot express
    for i, e in enumerate(doc.get("effects", [])):
        if not e.get("quote"):
            errs.append(f"effects[{i}]: MISSING QUOTE (hard rule violation)")
        if e.get("value") is None:
            errs.append(f"effects[{i}]: value is None")
    if doc.get("verification", {}).get("status") not in ("VERIFIED", "UNVERIFIED", "NOT_CHECKED"):
        errs.append("verification.status invalid")
    n_eff += len(doc.get("effects", []))
    tag = "FAIL" if errs else "ok  "
    print(f"{tag} {os.path.basename(f):24s} effects={len(doc.get('effects', [])):2d} "
          f"tier={doc.get('tier')} match={doc['population'].get('adolescent_match')}")
    for e in errs:
        print("      -", e)
        fail += 1

print(f"\n{len(files)} records, {n_eff} effect estimates, {fail} problems"
      f"{' (jsonschema NOT installed - structural check skipped)' if not jsonschema else ''}")
sys.exit(1 if fail else 0)
