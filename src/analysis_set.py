"""Curated analysis set: which specific effects feed which model parameter.

The corpus holds 1999 effects. Blindly pooling them would mix incommensurable quantities, so
every model parameter names the exact (study_id, construct) rows it is built from. Selectors
resolve against the corpus and raise if a named effect is missing, so evidence cannot silently
disappear and be replaced by a default.

Sign canonicalisation is done here, explicitly, per construct. The blinded re-extraction found
that the corpus mixes orientations (a lapse count and an accuracy score both "negative = harm"
would mean opposite things), and the adjudicator confirmed 8 of 9 extraction disputes were
caused by this. The canonical convention is:

    continuous outcomes : NEGATIVE = the subject is worse off
    log ratios          : POSITIVE = elevated risk

`flip: true` means the stored value is oriented the other way and must be negated.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from validate_evidence import load_all, poolable_effects

ROOT = Path(__file__).resolve().parent.parent


# study_id, construct (exact), flip
Sel = tuple[str, str, bool]

ANALYSIS_SET: dict[str, dict] = {
    # ---------------------------------------------------------------- cognition, T1 experimental
    "pvt_g_large_dose": {
        "what": "Vigilance decrement under chronic restriction, ~3-5 h below need, T1 experiments.",
        "scale": "hedges_g", "canonical": "negative_is_worse",
        "selectors": [
            ("lo2016", "pvt_lapses", True),                 # +2.399 = more lapses = worse
            ("vandongen2003", "pvt_lapses", True),          # +1.435 = more lapses = worse
            ("belenky2003", "pvt_mean_speed", False),       # -1.998 already speed (worse)
            ("basner2011_pvt_metrics", "pvt_lapses_500ms", True),
            ("pejovic2013_recovery_dissociation", "pvt_lapses_6h_vs_8h_tib_6_nights", False),
        ],
    },
    "global_cognition_g_agematched_obesity_subgroup_only": {
        "what": "Global/fluid cognition after ONE night of restriction in 14-19 year olds "
                "(duraccio2024, randomised crossover). NOT applicable to this subject as a "
                "general estimate: the effects exist only in the overweight/obesity subgroup, "
                "and the paper states 'No differences emerged for adolescents with healthy "
                "weight.' Carried so the report can state the age-matched randomised evidence "
                "on higher-order cognition in a healthy-weight adolescent is NULL, and so this "
                "subgroup result is not silently promoted into a general effect.",
        "scale": "cohens_d", "canonical": "negative_is_worse",
        "applies_to_subject": False,
        "healthy_weight_arm": "null, no numeric estimate published",
        "selectors": [
            ("duraccio2024", "global_cognition_restricted_vs_adequate_higher_adiposity_subgroup", False),
            ("duraccio2024", "fluid_cognition_restricted_vs_adequate_higher_adiposity_subgroup", False),
        ],
    },
    "higher_order_cognition_agematched_nulls": {
        "what": "Age-matched experimental tests of higher-order cognition that returned nulls. "
                "These are as informative as the positive vigilance findings and are the reason "
                "the IQ answer is small.",
        "scale": "raw_units", "canonical": "negative_is_worse",
        "selectors": [
            ("campbell2024", "sternberg_working_memory_slope_ms_per_item", True),
        ],
    },
    "domain_profile_chronic_restriction": {
        "what": "Overall neurocognitive performance under chronic partial restriction (not total "
                "deprivation), from the meta-analytic composite.",
        "scale": "hedges_g", "canonical": "negative_is_worse",
        "double_counting_correction": "Earlier versions pooled lowe2017's overall composite "
            "together with three of its own constituent sub-domains as if they were four "
            "independent studies. That violates the de-duplication rule, understates the "
            "interval, and pulls the estimate toward the composite by construction. Only the "
            "composite is pooled; the sub-domains are reported descriptively below.",
        "selectors": [
            ("lowe2017", "overall_neurocognitive_performance_pooled_across_domains", False),
        ],
    },
    "domain_subscales_descriptive_only": {
        "what": "Constituent sub-domains of the same meta-analysis. Reported to show the shape of "
                "the profile. MUST NOT be pooled with the composite above.",
        "scale": "hedges_g", "canonical": "negative_is_worse", "pool": False,
        "selectors": [
            ("lowe2017", "sustained_attention_pooled", False),
            ("lowe2017", "executive_functioning_pooled", False),
            ("lowe2017", "long_term_memory_pooled", False),
        ],
    },
    "reasoning_g_total_deprivation": {
        "what": "Reasoning / crystallized intelligence under TOTAL deprivation - the upper bound "
                "on an IQ-type decrement from acute sleep loss.",
        "scale": "hedges_g", "canonical": "negative_is_worse",
        "selectors": [("lim2010", "reasoning_and_crystallized_intelligence_accuracy", False)],
    },
    "fsiq_direct_measurement": {
        "what": "Directly measured full-scale IQ after total sleep deprivation. The decisive "
                "anchor against inflated IQ-loss claims.",
        "scale": "raw_units", "canonical": "negative_is_worse", "unit": "IQ points",
        "selectors": [("binks1999", "wais_r_short_form_full_scale_iq_raw_points", False)],
    },
    "iq_discount_vigilance_to_g": {
        "what": "How much of a vigilance effect size transfers to psychometric g. Measured "
                "reasoning-to-lapses ratio inside lim2010.",
        "scale": "raw_units", "canonical": "ratio",
        "selectors": [("lim2010", "ratio_reasoning_to_simple_attention_g", False)],
    },
    "habitual_short_sleep_g_observational": {
        "what": "Observational association of habitual short sleep with general cognitive "
                "ability in large samples. Cross-sectional, midlife: an upper bound that "
                "includes confounding and reverse causation.",
        "scale": "hedges_g", "canonical": "negative_is_worse",
        "selectors": [
            ("fjell2023", "general_cognitive_ability_g_factor", False),
            ("wild2018", "cbs_overall_composite", False),
            ("wild2018", "cbs_reasoning_composite", False),
        ],
    },
    # ---------------------------------------------------------------- persistence after recovery
    "residual_deficit_after_recovery_sleep": {
        "what": "Deficit still present after recovery sleep was provided. The core evidence that "
                "recovery is incomplete on the timescales anyone has actually measured.",
        "scale": "hedges_g", "canonical": "negative_is_worse",
        "selectors": [
            ("banks2010", "pvt_lapses_residual_deficit_after_10h_recovery_night", True),
            ("pejovic2013", "pvt_lapses_after_two_10h_recovery_nights_vs_baseline", True),
        ],
    },
    "encoding_capacity_persisting": {
        "what": "Memory for material ENCODED DURING a restricted week, retrieved after recovery "
                "sleep, in age-matched adolescents (cousins2018).",
        "scale": "hedges_g", "canonical": "negative_is_worse",
        "interpretation_correction": "Adversarial review established that encoding happened "
            "during the restricted week and only RETRIEVAL followed recovery sleep. So this does "
            "NOT show a persisting deficit in the faculty of encoding; it shows that material "
            "learned while sleep-restricted stays less well learned after sleep normalises. That "
            "is the learning-loss channel (knowledge not acquired), not a permanent ability "
            "change, and the report must not present it as the latter.",
        "k": 1,
        "reliability_warning": "k=1, abstract-only, one research programme. Two randomised, "
            "age-matched null results sit in the corpus but carry se: null and so cannot enter "
            "any inverse-variance pool, which biases this channel in one direction.",
        "selectors": [("cousins2018", "picture_recognition_memory_encoding_capacity", False)],
    },
}

# Parameters taken from shard-level syntheses rather than a single effect row. Each names the
# markdown file in evidence/ that derives it, so the provenance is traceable even though the
# quantity is a synthesis rather than one extracted number.
DERIVED_PARAMS = {
    "academic_sd_per_hour_sleep": {
        "value": 0.13, "interval80": [0.02, 0.30],
        "source": "evidence/s04_academic_natural_experiments/causal_summary.md",
        "basis": "T2 quasi-experimental pooled effect, corrected for the 0.45 h sleep-per-hour-"
                 "of-bell-shift first stage. Creswell 2023 +0.07 GPA/h; Groen & Pabilonia "
                 "0.26 SD/h; Heissel & Norris 0.081 SD per hour of bell time in adolescents.",
        "caveat": "Identified over sleep changes of 20-40 min; applying it to a 3 h deficit is a "
                  "large linear extrapolation.",
    },
    "t2d_rr_per_hour_below_7h": {
        "value": 1.09, "ci95": [1.04, 1.15],
        "source": "evidence/s07_metabolic/metabolic_summary.md (shan2015 dose-response)",
        "mr_surviving_fraction": [0.27, 0.43],
    },
    "mortality_rr_short_sleep": {
        "value": 1.12, "ci95": [1.06, 1.18],
        "source": "evidence/s13_mortality/mortality_summary.md (cappuccio2010)",
        "dose_response_at_5h": 1.04, "dose_response_at_6h": 1.01,
        "residual_causal_fraction": [0.0, 0.50], "residual_causal_central": 0.25,
        "permanent_residue_fraction_after_exposure_ends": [0.0, 0.12],
    },
    "depression_d_imposed_short_sleep": {
        "value": -0.156, "ci95": [-0.264, -0.056],
        "source": "evidence/s12_psychiatric/psychiatric_summary.md (sadikova2024 IV)",
        "mood_items_only": -0.03, "mood_items_ci": [-0.09, 0.02],
        "non_causal_share": [0.55, 0.70],
        "absolute_excess_pp": [0.0, 2.9],
    },
    "cvd_confounding_survival": {
        "value": 0.33, "interval": [0.20, 0.50],
        "source": "evidence/s08_cardiovascular/cardio_summary.md",
        "basis": "UK Biobank staged adjustment: 6 h HR 1.16 -> 1.05; 5 h 1.52 -> 1.19. "
                 "67% of the crude log hazard ratio attenuates on adjustment.",
    },
    "testosterone_pct_change": {
        "value": -10.3, "ci95": [-20.6, -0.06],
        "source": "evidence/s11_endocrine_growth/endocrine_summary.md (leproult2011)",
        "reversible": True, "reversal_days": 3,
    },
    "final_height_cm": {
        "value": 0.0, "interval": [0.0, 0.7], "arithmetic_ceiling": 3.65,
        "source": "evidence/s11_endocrine_growth/endocrine_summary.md",
    },
    "structural_permanence_probability": {
        "value": 0.03, "interval": [0.01, 0.10],
        "durable_neurobiological_change_any_kind": 0.25,
        "source": "evidence/s15_brain_structure/structure_summary.md",
    },
    "treatable_sleep_disorder_posterior": {
        "value": 0.21, "interval": [0.12, 0.32],
        "components": {"insomnia": 0.184, "dswpd": 0.019, "osa": 0.008},
        "source": "evidence/s19_sleep_disorders/screening_priors.md",
    },
    "social_jetlag_hours": {
        "value": 1.75, "interval": [1.0, 2.75], "percentile_for_age": 45,
        "source": "evidence/s16_social_jetlag/jetlag_summary.md",
        "depression_threshold_h": 2.0,
    },
    "comparator_le_months_per_3y_from_16": {
        "source": "evidence/s18_comparators/comparator_scale.md",
        "smoking_20_cig_day": {"central": 1.8, "interval80": [0.6, 9.0]},
        "smoking_10_cig_day": {"central": 1.0, "interval80": [0.4, 4.4]},
        "overweight_bmi_27.5": {"central": 1.8, "interval80": [0.4, 3.0]},
        "obesity_bmi_32": {"central": 2.4, "interval80": [0.8, 3.2]},
        "physical_inactivity": {"central": 0.8, "interval80": [0.2, 3.1]},
        "alcohol_200_350g_week": {"central": 3.0, "interval80": [1.4, 4.2]},
        "western_diet": {"central": 1.8, "interval80": [0.1, 3.8]},
    },
    "extraction_error_sd_g_scale": {
        "value": None,
        "source": "reports/agreement.json",
        "basis": "Empirically estimated from the blinded re-extraction pairs on g-type scales. "
                 "Added as an extra variance component to every g-scale effect, because the "
                 "observed inter-extractor ICC on that scale was 0.897, below the 0.90 gate.",
    },
}


def resolve() -> dict:
    """Resolve every selector against the corpus, applying canonical signs."""
    records, problems = load_all()
    if problems:
        raise RuntimeError(f"schema problems present: {problems[:3]}")
    rows = poolable_effects(records)
    index = {}
    for r in rows:
        index.setdefault((r["study_id"], r["construct"]), []).append(r)

    out, missing = {}, []
    for name, spec in ANALYSIS_SET.items():
        picked = []
        for study_id, construct, flip in spec["selectors"]:
            cands = index.get((study_id, construct))
            if not cands:
                missing.append((name, study_id, construct))
                continue
            # A (study_id, construct) pair can appear in several shards holding *different*
            # contrasts under the same label. Picking one arbitrarily would silently swap the
            # quantity, so duplicates are pooled by inverse variance and the standard error is
            # floored at half the spread: where two shards disagree, the disagreement is
            # carried as uncertainty rather than resolved by fiat.
            c = sorted(cands, key=lambda r: r["se"])[0]
            vals = np.array([r["value"] for r in cands], float)
            ses = np.array([r["se"] for r in cands], float)
            if len(cands) > 1:
                w = 1.0 / ses ** 2
                val = float((w * vals).sum() / w.sum())
                se_pooled = float(np.sqrt(1.0 / w.sum()))
                se_val = max(se_pooled, float(vals.max() - vals.min()) / 2.0)
            else:
                val, se_val = float(vals[0]), float(ses[0])
            picked.append({
                "study_id": study_id, "construct": construct,
                "value": -val if flip else val,
                "se": se_val, "flipped": flip,
                "duplicate_values": vals.tolist() if len(cands) > 1 else None,
                "tier": c["tier"], "n": c["n"], "scale": c["scale"],
                "adolescent_match": c["adolescent_match"],
                "cohort_family": c["cohort_family"],
                "dose_h": c["dose_h"], "referent_h": c["referent_h"],
                "shard": c["shard"], "n_duplicate_records": len(cands),
            })
        out[name] = {**{k: v for k, v in spec.items() if k != "selectors"}, "effects": picked}
    if missing:
        raise RuntimeError(f"analysis set references effects absent from the corpus: {missing}")
    return out


def extraction_error_sd() -> float:
    """SD of inter-extractor disagreement on g-type scales, from the blinded re-extraction."""
    path = ROOT / "reports" / "agreement.json"
    if not path.exists():
        return 0.0
    rep = json.loads(path.read_text())
    per_scale = rep["continuous_sign_reconciled"]["per_scale"]
    # Recover an SD from the observed ICC and the spread of g values in the sample:
    # ICC = var_true / (var_true + var_err)  =>  var_err = var_true (1 - ICC) / ICC
    icc = per_scale.get("hedges_g", {}).get("icc")
    if not icc or icc <= 0:
        return 0.0
    typical_g_sd = 0.55   # spread of g values across the sampled cognitive effects
    var_true = typical_g_sd ** 2
    var_err = var_true * (1 - icc) / icc
    return float(np.sqrt(var_err))


if __name__ == "__main__":
    resolved = resolve()
    print(f"extraction-error SD on g scale: {extraction_error_sd():.4f}\n")
    for name, spec in resolved.items():
        print(f"### {name}  [{spec['scale']}]")
        print(f"    {spec['what']}")
        for e in spec["effects"]:
            dup = f"  (dup x{e['n_duplicate_records']})" if e["n_duplicate_records"] > 1 else ""
            print(f"    {e['study_id']:34s} {e['tier']:3s} {e['value']:+8.4f} +- {e['se']:.4f} "
                  f"{'FLIPPED' if e['flipped'] else '       '} {e['adolescent_match']}{dup}")
        print()
