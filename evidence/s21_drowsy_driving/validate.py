#!/usr/bin/env python3
"""Validate every YAML record in this shard against /workspace/spec/effect.schema.json."""
import glob
import json
import math
import os
import sys

import jsonschema
import yaml

SCHEMA = json.load(open("/workspace/spec/effect.schema.json"))
HERE = os.path.dirname(os.path.abspath(__file__))

fails = 0
n_eff = 0
records = []
for path in sorted(glob.glob(os.path.join(HERE, "*.yaml"))):
    with open(path) as fh:
        doc = yaml.safe_load(fh)
    name = os.path.basename(path)
    try:
        jsonschema.validate(doc, SCHEMA)
        status = "OK"
    except jsonschema.ValidationError as exc:
        status = "FAIL: %s @ %s" % (exc.message[:160], list(exc.absolute_path))
        fails += 1
    ne = len(doc.get("effects") or [])
    n_eff += ne
    records.append((name, doc.get("tier"), ne, (doc.get("verification") or {}).get("status"), status))
    print("%-28s tier=%-3s effects=%-3d verif=%-10s %s" % (
        name, doc.get("tier"), ne, (doc.get("verification") or {}).get("status"), status))

    # arithmetic audit: log-scale value vs ci
    for i, e in enumerate(doc.get("effects") or []):
        if e.get("scale") in ("log_hr", "log_rr", "log_or"):
            ci, se, val = e.get("ci"), e.get("se"), e.get("value")
            if ci and len(ci) == 2:
                mid = (ci[0] + ci[1]) / 2.0
                if val is not None and abs(mid - val) > 0.06:
                    print("   ! %s eff[%d] value %.4f not centred in ci %s (mid %.4f)" % (
                        name, i, val, ci, mid))
                if se:
                    implied = (ci[1] - ci[0]) / 3.92
                    if abs(implied - se) > 0.02 * max(se, 0.01) + 1e-4:
                        print("   ! %s eff[%d] se %.6f != (ci_hi-ci_lo)/3.92 = %.6f" % (
                            name, i, se, implied))

print("\nfiles=%d  effects=%d  schema_failures=%d" % (len(records), n_eff, fails))
sys.exit(1 if fails else 0)
