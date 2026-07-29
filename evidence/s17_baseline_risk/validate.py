"""Validate every YAML record this shard wrote against /workspace/spec/effect.schema.json."""
import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft7Validator

SCHEMA = json.loads(Path("/workspace/spec/effect.schema.json").read_text())
DIR = Path("/workspace/evidence/s17_baseline_risk")

v = Draft7Validator(SCHEMA)
fail = 0
n_eff = 0
records = sorted(DIR.glob("*.yaml"))
for p in records:
    doc = yaml.safe_load(p.read_text())
    errs = sorted(v.iter_errors(doc), key=lambda e: list(e.path))
    n_eff += len(doc.get("effects", []))
    if errs:
        fail += 1
        print(f"FAIL {p.name}")
        for e in errs:
            print(f"   /{'/'.join(map(str, e.path))}: {e.message}")
    else:
        print(f"ok   {p.name}  ({len(doc['effects'])} effects, tier {doc['tier']})")

print(f"\n{len(records)} records, {n_eff} effects, {fail} schema failures")

# the two data deliverables must also parse
lt = Path("/workspace/data/lifetable_us_male.csv")
rows = [r for r in lt.read_text().splitlines() if not r.startswith("#")]
print(f"lifetable_us_male.csv: {len(rows)} non-comment lines (1 header + 92 ages expected)")
br = yaml.safe_load(Path("/workspace/data/baseline_risks.yaml").read_text())
print(f"baseline_risks.yaml: parses, top-level keys = {list(br)}")
sys.exit(1 if fail else 0)
