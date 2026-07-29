"""Schema validation and corpus inventory (Gates G0, G1, G6).

Loads every YAML evidence record, validates against effect.schema.json, and reports the
corpus inventory the pooler needs: effects per domain, tier mix, cohort-family collisions,
and which effects are poolable (have a numeric standard error).
"""

from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

import jsonschema
import yaml

ROOT = Path(__file__).resolve().parent.parent
EVIDENCE = ROOT / "evidence"
SCHEMA = json.loads((ROOT / "spec" / "effect.schema.json").read_text())


def load_all(strict_schema: bool = False):
    """Return (records, problems). Records carry _file and _shard provenance."""
    records, problems = [], []
    validator = jsonschema.Draft7Validator(SCHEMA)
    for path in sorted(EVIDENCE.rglob("*.y*ml")):
        rel = str(path.relative_to(ROOT))
        try:
            docs = list(yaml.safe_load_all(path.read_text()))
        except yaml.YAMLError as exc:
            problems.append({"file": rel, "kind": "yaml_error", "detail": str(exc)[:300]})
            continue
        for doc in docs:
            if not isinstance(doc, dict) or not doc:
                continue
            errs = sorted(validator.iter_errors(doc), key=lambda e: e.path)
            if errs:
                for e in errs[:4]:
                    problems.append({"file": rel, "kind": "schema",
                                     "path": "/".join(str(p) for p in e.path),
                                     "detail": e.message[:220]})
                if strict_schema:
                    continue
            doc["_file"] = rel
            doc["_shard"] = doc.get("shard") or path.parent.name
            records.append(doc)
    return records, problems


def poolable_effects(records):
    """Flatten to effect rows that can enter a meta-analysis: numeric value and SE > 0."""
    rows = []
    for rec in records:
        for i, eff in enumerate(rec.get("effects") or []):
            se = eff.get("se")
            val = eff.get("value")
            if se is None or val is None:
                continue
            try:
                se = float(se)
                val = float(val)
            except (TypeError, ValueError):
                continue
            if not (se > 0):
                continue
            rows.append({
                "study_id": rec.get("study_id"), "shard": rec["_shard"], "file": rec["_file"],
                "tier": rec.get("tier"), "design": rec.get("design"),
                "adolescent_match": (rec.get("population") or {}).get("adolescent_match"),
                "n": rec.get("n"), "rob": (rec.get("rob") or {}).get("judgement"),
                "doi": rec.get("doi"), "pmid": rec.get("pmid"),
                "domain": eff.get("outcome_domain"), "construct": eff.get("outcome_construct"),
                "scale": eff.get("scale"), "unit": eff.get("unit"),
                "value": val, "se": se,
                "exposure_type": (eff.get("exposure") or {}).get("type"),
                "dose_h": (eff.get("exposure") or {}).get("dose_h"),
                "referent_h": (eff.get("exposure") or {}).get("referent_h"),
                "duration_days": (eff.get("exposure") or {}).get("duration_days"),
                "cohort_family": eff.get("cohort_family"),
                "from_figure": bool(eff.get("from_figure")),
                "effect_index": i,
            })
    return rows


def inventory():
    records, problems = load_all()
    rows = poolable_effects(records)
    n_effects = sum(len(r.get("effects") or []) for r in records)
    by_shard = Counter(r["_shard"] for r in records)
    by_tier = Counter(r.get("tier") for r in records)
    by_domain = Counter(row["domain"] for row in rows)
    by_match = Counter((r.get("population") or {}).get("adolescent_match") for r in records)
    fam = defaultdict(set)
    for row in rows:
        if row["cohort_family"]:
            fam[row["cohort_family"]].add(row["study_id"])
    dup_ids = {k: v for k, v in Counter(r.get("study_id") for r in records).items() if v > 1}
    out = {
        "n_records": len(records),
        "n_effects_total": n_effects,
        "n_effects_poolable": len(rows),
        "n_problems": len(problems),
        "records_by_shard": dict(sorted(by_shard.items())),
        "records_by_tier": dict(sorted(by_tier.items(), key=lambda x: str(x[0]))),
        "poolable_by_domain": dict(sorted(by_domain.items(), key=lambda x: -x[1])),
        "records_by_adolescent_match": dict(by_match),
        "cohort_families_multi_study": {k: sorted(v) for k, v in sorted(fam.items()) if len(v) > 1},
        "duplicate_study_ids": dup_ids,
        "problems": problems[:80],
    }
    (ROOT / "reports" / "inventory.json").write_text(json.dumps(out, indent=1, default=str))
    return out


if __name__ == "__main__":
    inv = inventory()
    slim = {k: v for k, v in inv.items() if k != "problems"}
    print(json.dumps(slim, indent=1, default=str))
    if inv["problems"]:
        print(f"\n--- {inv['n_problems']} problems (first 25) ---")
        for p in inv["problems"][:25]:
            print(f"  {p['kind']:12s} {p['file']:70s} {p.get('path','')}: {p['detail'][:130]}")
    if "--strict" in sys.argv and inv["n_problems"]:
        sys.exit(1)
