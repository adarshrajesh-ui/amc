"""S3 agreement statistics (Gates G3, G4).

Compares the first extraction team's values against the blinded re-extraction team's values.

Two agreement figures are reported for continuous values, and both matter:

  raw            - the extractors' numbers exactly as recorded.
  sign-reconciled - the same numbers after allowing a whole-record sign flip.

The re-extractors independently reported that many task specifications were directionally
ambiguous (a construct naming "per additional hour" while the exposure field said "per hour
less"). A sign flip driven by an ambiguous codebook is a specification defect, not an
extraction defect, and conflating the two would either hide a real problem or invent one.
Both numbers are published and the gate is applied to the raw figure.
"""

from __future__ import annotations

import json
import math
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
REEXT = ROOT / "reextraction"
TRUTH_PATH = ROOT / "data" / "reextraction_truth.json"


def icc_2_1(a: np.ndarray, b: np.ndarray) -> float:
    """ICC(2,1): two-way random effects, single measurement, absolute agreement."""
    x = np.column_stack([a, b]).astype(float)
    n, k = x.shape
    if n < 3:
        return float("nan")
    grand = x.mean()
    row_means, col_means = x.mean(axis=1), x.mean(axis=0)
    ss_rows = k * ((row_means - grand) ** 2).sum()
    ss_cols = n * ((col_means - grand) ** 2).sum()
    ss_total = ((x - grand) ** 2).sum()
    ss_err = ss_total - ss_rows - ss_cols
    ms_rows = ss_rows / (n - 1)
    ms_cols = ss_cols / (k - 1)
    ms_err = ss_err / ((n - 1) * (k - 1))
    denom = ms_rows + (k - 1) * ms_err + k * (ms_cols - ms_err) / n
    return float((ms_rows - ms_err) / denom) if denom != 0 else float("nan")


def cohens_kappa(a: list, b: list) -> tuple[float, int]:
    pairs = [(x, y) for x, y in zip(a, b) if x is not None and y is not None]
    if len(pairs) < 3:
        return float("nan"), len(pairs)
    cats = sorted({c for p in pairs for c in p})
    idx = {c: i for i, c in enumerate(cats)}
    m = np.zeros((len(cats), len(cats)))
    for x, y in pairs:
        m[idx[x], idx[y]] += 1
    total = m.sum()
    po = np.trace(m) / total
    pe = float((m.sum(axis=0) / total) @ (m.sum(axis=1) / total))
    if pe == 1.0:
        return 1.0 if po == 1.0 else 0.0, len(pairs)
    return float((po - pe) / (1 - pe)), len(pairs)


def robust_scale(values: np.ndarray) -> float:
    """MAD-based scale used to make mixed-scale effect sizes comparable."""
    if len(values) == 0:
        return 1.0
    med = np.median(values)
    mad = np.median(np.abs(values - med))
    if mad > 0:
        return float(1.4826 * mad)
    sd = float(np.std(values))
    return sd if sd > 0 else 1.0


def _match_key(doi, pmid, construct, scale):
    ident = (str(doi).strip().lower() if doi else "") or (str(pmid).strip() if pmid else "")
    return (ident, str(construct), str(scale))


def load_pairs():
    """Match re-extractions to originals.

    `study_id::effect_index` is NOT a unique key: 47 studies appear in more than one shard,
    so that key silently collided and could pair a re-extraction against a different paper.
    Matching is therefore done on (identifier, construct, scale), which is what the blinded
    task file actually specified, with the task_id used only as a fallback label.
    """
    truth = json.loads(TRUTH_PATH.read_text())
    truth_by_key = {}
    for tid, t in truth.items():
        truth_by_key[_match_key(t.get("doi"), t.get("pmid"), t.get("construct"), t.get("scale"))] = (tid, t)

    done = []
    for path in sorted(REEXT.glob("batch*_done.json")):
        done.extend(json.loads(path.read_text()))
    pairs, unmatched = [], []
    for row in done:
        tid = row.get("task_id")
        key = _match_key(row.get("doi"), row.get("pmid"),
                         row.get("target_outcome_construct"), row.get("target_scale"))
        matched = truth_by_key.get(key)
        t = matched[1] if matched else truth.get(tid)
        if t is None:
            unmatched.append(tid)
            continue
        pairs.append({
            "task_id": tid, "study_id": row.get("study_id"), "shard": t["shard"],
            "scale": t["scale"], "domain": t["domain"], "construct": t["construct"],
            "reason": row.get("reason_selected"),
            "v1": t["value"], "v2": row.get("your_value"),
            "se1": t["se"], "se2": row.get("your_se"),
            "d1": t["design"], "d2": row.get("your_design"),
            "t1": t["tier"], "t2": row.get("your_tier"),
            "r1": t["rob_judgement"], "r2": row.get("your_rob_judgement"),
            "conf": row.get("your_confidence"),
            "has_quote": bool(row.get("your_quote")),
        })
    return pairs, unmatched


def continuous_agreement(pairs, reconcile_sign: bool):
    by_scale = defaultdict(list)
    for p in pairs:
        if p["v1"] is None or p["v2"] is None:
            continue
        by_scale[p["scale"]].append(p)

    z1, z2, rel = [], [], []
    per_scale = {}
    for scale, group in sorted(by_scale.items()):
        a = np.array([g["v1"] for g in group], dtype=float)
        b = np.array([g["v2"] for g in group], dtype=float)
        if reconcile_sign:
            flip = np.sign(a) * np.sign(b) < 0
            b = np.where(flip, -b, b)
        s = robust_scale(np.concatenate([a, b]))
        z1.extend(a / s)
        z2.extend(b / s)
        denom = np.maximum(np.abs(a), 1e-9)
        rel.extend(np.abs(a - b) / denom)
        if len(group) >= 4:
            per_scale[scale] = {"n": len(group), "icc": round(icc_2_1(a, b), 4),
                                "pearson": round(float(np.corrcoef(a, b)[0, 1]), 4)
                                if len(group) > 2 and np.std(a) > 0 and np.std(b) > 0 else None}

    z1a, z2a, rela = np.array(z1), np.array(z2), np.array(rel)
    diffs = z1a - z2a

    # The naively pooled standardized ICC is dominated by whichever scale group has the
    # widest spread and is therefore not a usable gate statistic. Gate on the per-scale
    # ICCs instead: a sample-size-weighted mean, and the worst group.
    scale_iccs = {s: v["icc"] for s, v in per_scale.items() if not math.isnan(v["icc"])}
    weights = {s: per_scale[s]["n"] for s in scale_iccs}
    wmean = (sum(scale_iccs[s] * weights[s] for s in scale_iccs) / sum(weights.values())
             if scale_iccs else float("nan"))
    worst = min(scale_iccs, key=scale_iccs.get) if scale_iccs else None

    return {
        "n_pairs": int(len(z1a)),
        "icc_weighted_mean_across_scales": round(wmean, 4),
        "icc_worst_scale": worst,
        "icc_worst_value": round(scale_iccs[worst], 4) if worst else None,
        "icc_2_1_pooled_standardized_ARTIFACT_DO_NOT_GATE_ON": round(icc_2_1(z1a, z2a), 4),
        "pearson_standardized": round(float(np.corrcoef(z1a, z2a)[0, 1]), 4) if len(z1a) > 2 else None,
        "spearman_like_sign_concordance": round(float(np.mean(np.sign(z1a) == np.sign(z2a))), 4),
        "pct_within_1pct": round(float(np.mean(rela <= 0.01) * 100), 1),
        "pct_within_10pct": round(float(np.mean(rela <= 0.10) * 100), 1),
        "pct_within_25pct": round(float(np.mean(rela <= 0.25) * 100), 1),
        "median_relative_abs_diff": round(float(np.median(rela)), 4),
        "bland_altman_bias_standardized": round(float(np.mean(diffs)), 4),
        "bland_altman_loa_standardized": [round(float(np.mean(diffs) - 1.96 * np.std(diffs, ddof=1)), 4),
                                          round(float(np.mean(diffs) + 1.96 * np.std(diffs, ddof=1)), 4)],
        "per_scale": per_scale,
    }


def main() -> dict:
    pairs, unmatched = load_pairs()
    raw = continuous_agreement(pairs, reconcile_sign=False)
    rec = continuous_agreement(pairs, reconcile_sign=True)

    k_design, n_design = cohens_kappa([p["d1"] for p in pairs], [p["d2"] for p in pairs])
    k_tier, n_tier = cohens_kappa([p["t1"] for p in pairs], [p["t2"] for p in pairs])
    k_rob, n_rob = cohens_kappa([p["r1"] for p in pairs], [p["r2"] for p in pairs])

    # Tier drives model weighting, so also score a coarsened version: is this
    # causal-identification evidence (T1-T3) or associational (T4/T5/TX)?
    def coarse(t):
        if t is None:
            return None
        return "causal" if t in ("T1", "T2", "T3") else "assoc"
    k_tier_coarse, n_tc = cohens_kappa([coarse(p["t1"]) for p in pairs], [coarse(p["t2"]) for p in pairs])

    disagreements = sorted(
        [p for p in pairs if p["v1"] is not None and p["v2"] is not None],
        key=lambda p: -abs(p["v1"] - p["v2"]) / max(abs(p["v1"]), 1e-9),
    )[:25]

    out = {
        "n_reextraction_tasks_returned": len(pairs),
        "n_unmatched_task_ids": len(unmatched),
        "n_nulled_by_reextractor": sum(1 for p in pairs if p["v2"] is None),
        "n_with_quote": sum(1 for p in pairs if p["has_quote"]),
        "reextractor_confidence": dict(Counter(p["conf"] for p in pairs)),
        "continuous_raw": raw,
        "continuous_sign_reconciled": rec,
        "categorical": {
            "kappa_design": {"kappa": round(k_design, 4), "n": n_design},
            "kappa_tier": {"kappa": round(k_tier, 4), "n": n_tier},
            "kappa_tier_coarse_causal_vs_assoc": {"kappa": round(k_tier_coarse, 4), "n": n_tc},
            "kappa_rob": {"kappa": round(k_rob, 4), "n": n_rob},
        },
        "gate_G3_icc_ge_0.90": bool(raw["icc_weighted_mean_across_scales"] >= 0.90),
        "gate_G3_icc_ge_0.90_sign_reconciled": bool(rec["icc_weighted_mean_across_scales"] >= 0.90),
        "gate_G3_all_scales_pass": bool(raw["icc_worst_value"] is not None
                                        and raw["icc_worst_value"] >= 0.90),
        "gate_G3_failing_scales": [s for s, v in raw["per_scale"].items() if v["icc"] < 0.90],
        "gate_G4_kappa_ge_0.80": bool(min(k_design, k_tier) >= 0.80),
        "largest_disagreements": [
            {"task_id": p["task_id"], "scale": p["scale"], "v1": p["v1"], "v2": p["v2"],
             "shard": p["shard"], "construct": p["construct"], "conf": p["conf"]}
            for p in disagreements
        ],
    }
    (ROOT / "reports" / "agreement.json").write_text(json.dumps(out, indent=1))
    return out


if __name__ == "__main__":
    res = main()
    slim = {k: v for k, v in res.items() if k != "largest_disagreements"}
    print(json.dumps(slim, indent=1))
    print("\n--- largest disagreements ---")
    for d in res["largest_disagreements"][:15]:
        print(f"  {d['task_id']:42s} {d['scale']:14s} v1={d['v1']:>10.4g}  v2={d['v2']:>10.4g}  {d['construct'][:40]}")
