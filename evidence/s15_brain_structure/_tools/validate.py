#!/usr/bin/env python3
"""Validate all shard YAML records against /workspace/spec/effect.schema.json."""
import glob, json, os, sys

try:
    import yaml
except ImportError:
    sys.exit("pyyaml missing: pip install pyyaml")
try:
    import jsonschema
except ImportError:
    jsonschema = None

SCHEMA = json.load(open("/workspace/spec/effect.schema.json"))
files = sorted(f for f in glob.glob("/workspace/evidence/s15_brain_structure/*.yaml"))

n_ok = n_bad = 0
n_effects = 0
tiers, designs = {}, {}
quoteless = []

for f in files:
    d = yaml.safe_load(open(f))
    errs = []
    if jsonschema:
        v = jsonschema.Draft7Validator(SCHEMA)
        errs = [f"{list(e.path)}: {e.message}" for e in v.iter_errors(d)]
    # extra hand checks the schema cannot express
    for i, e in enumerate(d.get("effects", [])):
        n_effects += 1
        if not e.get("quote"):
            quoteless.append(f"{d['study_id']} effect[{i}] ({e.get('outcome_construct')})")
        if e.get("ci") is not None and len(e["ci"]) == 2 and e["ci"][0] > e["ci"][1]:
            errs.append(f"effects[{i}]: ci lower > upper")
    if d.get("study_id") != os.path.basename(f)[:-5]:
        errs.append(f"study_id '{d.get('study_id')}' != filename '{os.path.basename(f)[:-5]}'")
    if d.get("shard") != "s15_brain_structure":
        errs.append("shard field wrong/missing")
    tiers[d.get("tier")] = tiers.get(d.get("tier"), 0) + 1
    designs[d.get("design")] = designs.get(d.get("design"), 0) + 1

    if errs:
        n_bad += 1
        print(f"FAIL {os.path.basename(f)}")
        for e in errs:
            print("      -", e)
    else:
        n_ok += 1
        print(f"  ok {os.path.basename(f):26s} tier={d.get('tier'):3s} n={str(d.get('n')):6s} effects={len(d.get('effects',[]))}")

print(f"\njsonschema available: {bool(jsonschema)}")
print(f"records: {len(files)}   pass: {n_ok}   fail: {n_bad}")
print(f"total effect estimates: {n_effects}")
print(f"tiers:   {dict(sorted(tiers.items(), key=lambda kv: str(kv[0])))}")
print(f"designs: {json.dumps(designs, indent=0)}")
if quoteless:
    print("\nEFFECTS MISSING A VERBATIM QUOTE (violates hard rule 2):")
    for q in quoteless:
        print("   -", q)
else:
    print("\nAll effects carry a verbatim quote.")
