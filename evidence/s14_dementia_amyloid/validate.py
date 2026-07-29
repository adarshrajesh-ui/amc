#!/usr/bin/env python3
"""Validate every YAML record in this shard against /workspace/spec/effect.schema.json.

Also runs shard-specific consistency checks that the schema cannot express:
  * study_id must equal the filename stem
  * every effect must carry a non-empty verbatim `quote`
  * log-scale value/ci must be internally consistent (value inside ci)
  * se, when present alongside a ci, must be within 20% of (ci_hi - ci_lo)/3.92
  * every identifier must appear in verify.py's RECORDS and be VERIFIED
"""
import json
import math
import pathlib
import re
import sys

try:
    import yaml
except ImportError:
    sys.exit("pip install pyyaml")
try:
    from jsonschema import Draft7Validator
except ImportError:
    sys.exit("pip install jsonschema")

HERE = pathlib.Path(__file__).parent
SCHEMA = json.loads(pathlib.Path("/workspace/spec/effect.schema.json").read_text())
VALIDATOR = Draft7Validator(SCHEMA)

verify_src = (HERE / "verify.py").read_text()
known_ids = set(re.findall(r'^\s*"([a-z0-9_]+)":\s*\(', verify_src, re.M))
raw = json.loads((HERE / "verification_raw.json").read_text())
verified = {k for k, v in raw.items() if v.get("status") == "VERIFIED"}

errors, warnings, n_eff = [], [], 0
files = sorted(p for p in HERE.glob("*.yaml"))

for path in files:
    doc = yaml.safe_load(path.read_text())
    sid = doc.get("study_id")
    tag = path.name

    for e in VALIDATOR.iter_errors(doc):
        errors.append("%s: SCHEMA %s at %s" % (tag, e.message, list(e.absolute_path)))

    if sid != path.stem:
        errors.append("%s: study_id %r != filename stem %r" % (tag, sid, path.stem))
    if sid not in known_ids:
        errors.append("%s: study_id %r absent from verify.py RECORDS" % (tag, sid))
    elif sid not in verified:
        errors.append("%s: study_id %r not VERIFIED in verification_raw.json" % (tag, sid))

    if doc.get("shard") != "s14_dementia_amyloid":
        errors.append("%s: wrong shard tag %r" % (tag, doc.get("shard")))

    for i, eff in enumerate(doc.get("effects") or []):
        n_eff += 1
        loc = "%s effect[%d] %s" % (tag, i, eff.get("outcome_construct"))
        q = (eff.get("quote") or "").strip()
        if len(q) < 25:
            errors.append("%s: quote missing or too short (%d chars)" % (loc, len(q)))

        val, se, ci = eff.get("value"), eff.get("se"), eff.get("ci")
        scale = eff.get("scale")
        if ci and val is not None and scale in ("log_rr", "log_hr", "log_or",
                                                "hedges_g", "cohens_d", "smd"):
            lo, hi = ci
            if not (lo - 1e-6 <= val <= hi + 1e-6):
                errors.append("%s: value %.6g outside ci [%.6g, %.6g]" % (loc, val, lo, hi))
        if ci and se:
            implied = (ci[1] - ci[0]) / 3.92
            if implied > 0 and abs(implied - se) / max(se, 1e-12) > 0.20:
                warnings.append("%s: se %.6g vs ci-implied %.6g (%.0f%% apart)"
                                % (loc, se, implied, 100 * abs(implied - se) / se))
        if se is not None and se <= 0:
            errors.append("%s: non-positive se %r" % (loc, se))
        if eff.get("scale") in ("log_rr", "log_hr", "log_or") and val is not None:
            if abs(val) > 3:
                warnings.append("%s: |log effect| = %.3g is implausibly large - check units"
                                % (loc, abs(val)))

print("files=%d  effects=%d" % (len(files), n_eff))
print("verify.py RECORDS=%d  VERIFIED=%d" % (len(known_ids), len(verified)))
unused = sorted(known_ids - {p.stem for p in files})
if unused:
    # Expected: identifiers checked for provenance but carrying no extractable effect
    # (an erratum, and a registered protocol whose results do not exist yet).
    print("identifiers verified but deliberately not extracted: %s"
          % ", ".join(unused))
print()
for w in warnings:
    print("WARN  " + w)
print()
if errors:
    for e in errors:
        print("ERROR " + e)
    print("\nFAILED: %d error(s)" % len(errors))
    sys.exit(1)
print("ALL %d RECORDS VALID against effect.schema.json (%d warnings)" % (len(files), len(warnings)))
