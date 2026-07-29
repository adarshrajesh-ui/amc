"""S3 sampler: build blinded re-extraction tasks (Gates G3, G4).

Selects a seeded random 30% sample of evidence records stratified by shard, plus 100% of a
hand-designated influential set, and emits task files that contain the *target* of extraction
(identifier, outcome construct, exposure contrast, scale) but NOT the extracted values. A second
set of agents fills these in without seeing the originals; agreement is then computed by
src/agreement.py.
"""

from __future__ import annotations

import json
import random
from collections import defaultdict
from pathlib import Path

from validate_evidence import load_all, poolable_effects

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "reextraction"
SEED = 20260728
SAMPLE_FRACTION = 0.30
N_BATCHES = 6

# Studies whose values move the headline numbers most; re-extracted at 100%.
INFLUENTIAL = [
    "vandongen2003", "lo2016", "lo2022", "belenky2003", "banks2010", "kitamura2016",
    "lim2010", "lowe2017", "wild2018", "fjell2023", "binks1999", "campbell2024",
    "lauderdale2008", "short2018sleepneed", "hirshkowitz2015", "klerman2008",
    "shan2015", "kuroda2025", "cappuccio2010", "yin2017", "akerstedt2019", "sabia2021",
    "daghlas2019", "creswell2023", "heissel_norris2018", "groen_pabilonia2019",
    "scott2021", "sadikova2024", "leproult2011", "prather2015_rhinovirus",
    "cousins2018", "berres2021", "depner2019", "zhao2023",
]


def main() -> dict:
    rng = random.Random(SEED)
    records, problems = load_all()
    assert not problems, f"fix schema problems first: {problems[:3]}"

    rows = poolable_effects(records)
    by_key = defaultdict(list)
    for r in rows:
        by_key[(r["file"], r["study_id"])].append(r)

    keys = sorted(by_key)
    by_shard = defaultdict(list)
    for k in keys:
        by_shard[by_key[k][0]["shard"]].append(k)

    selected, reasons = [], {}
    for shard, shard_keys in sorted(by_shard.items()):
        shard_keys = sorted(shard_keys)
        rng.shuffle(shard_keys)
        take = max(1, round(SAMPLE_FRACTION * len(shard_keys)))
        for k in shard_keys[:take]:
            selected.append(k)
            reasons[k] = "random_30pct"

    for k in keys:
        if by_key[k][0]["study_id"] in INFLUENTIAL and k not in reasons:
            selected.append(k)
            reasons[k] = "influential"

    selected = sorted(set(selected))
    tasks = []
    for k in selected:
        cands = sorted(by_key[k], key=lambda r: r["effect_index"])
        eff = cands[rng.randrange(len(cands))] if reasons[k] == "random_30pct" else cands[0]
        rec = next(r for r in records if r["_file"] == k[0] and r.get("study_id") == k[1])
        tasks.append({
            "task_id": f"{eff['study_id']}::{eff['effect_index']}",
            "reason_selected": reasons[k],
            "study_id": eff["study_id"],
            "citation": rec.get("citation"),
            "doi": rec.get("doi"),
            "pmid": rec.get("pmid"),
            "target_outcome_domain": eff["domain"],
            "target_outcome_construct": eff["construct"],
            "target_exposure_type": eff["exposure_type"],
            "target_exposure_dose_h": eff["dose_h"],
            "target_exposure_referent_h": eff["referent_h"],
            "target_exposure_duration_days": eff["duration_days"],
            "target_scale": eff["scale"],
            "target_unit": eff["unit"],
            # ---- fields the re-extractor must fill, blinded ----
            "your_value": None,
            "your_se": None,
            "your_n": None,
            "your_design": None,
            "your_tier": None,
            "your_rob_judgement": None,
            "your_quote": None,
            "your_confidence": None,
            "your_note": None,
        })

    OUT.mkdir(parents=True, exist_ok=True)
    rng.shuffle(tasks)
    batches = [tasks[i::N_BATCHES] for i in range(N_BATCHES)]
    for i, batch in enumerate(batches, start=1):
        (OUT / f"batch{i:02d}_tasks.json").write_text(json.dumps(batch, indent=1))

    # Truth file kept out of the batch files so re-extractors cannot see it.
    # Key on file as well as study_id: 47 study_ids appear in more than one shard, and a
    # study_id::index key silently overwrites one shard's record with another's.
    truth = {}
    for k in selected:
        for eff in by_key[k]:
            rec = next(r for r in records if r["_file"] == k[0] and r.get("study_id") == k[1])
            truth[f"{eff['file']}::{eff['study_id']}::{eff['effect_index']}"] = {
                "value": eff["value"], "se": eff["se"], "scale": eff["scale"],
                "n": eff["n"], "design": eff["design"], "tier": eff["tier"],
                "rob_judgement": eff["rob"], "shard": eff["shard"], "file": eff["file"],
                "domain": eff["domain"], "construct": eff["construct"],
                "doi": rec.get("doi"), "pmid": rec.get("pmid"),
            }
    (ROOT / "data" / "reextraction_truth.json").write_text(json.dumps(truth, indent=1))

    summary = {
        "seed": SEED, "n_records_with_poolable_effects": len(keys),
        "n_selected": len(selected), "n_tasks": len(tasks),
        "fraction_selected": round(len(selected) / len(keys), 3),
        "n_influential_found": sum(1 for v in reasons.values() if v == "influential"),
        "batches": {f"batch{i:02d}": len(b) for i, b in enumerate(batches, start=1)},
    }
    (OUT / "sample_summary.json").write_text(json.dumps(summary, indent=1))
    return summary


if __name__ == "__main__":
    print(json.dumps(main(), indent=1))
