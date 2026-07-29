#!/usr/bin/env python3
"""Validate this shard's evidence YAML against /workspace/spec/effect.schema.json (Gate G0)."""
import json
import pathlib
import sys

import jsonschema
import yaml

SHARD = pathlib.Path(__file__).resolve().parent
SCHEMA = json.loads((SHARD.parents[1] / "spec" / "effect.schema.json").read_text())
validator = jsonschema.Draft7Validator(SCHEMA)

fails = 0
n_eff = 0
for path in sorted(SHARD.glob("*.yaml")):
    rec = yaml.safe_load(path.read_text())
    errs = sorted(validator.iter_errors(rec), key=lambda e: list(e.path))
    n_eff += len(rec.get("effects", []))
    if errs:
        fails += 1
        print("FAIL %s" % path.name)
        for e in errs:
            print("   path=%s: %s" % ("/".join(str(p) for p in e.path), e.message[:200]))
    else:
        print("ok   %-26s effects=%-2d tier=%-3s design=%s"
              % (path.name, len(rec["effects"]), rec["tier"], rec["design"]))

print("\n%d files, %d effects, %d schema failures" % (len(list(SHARD.glob('*.yaml'))), n_eff, fails))
sys.exit(1 if fails else 0)
