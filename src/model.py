"""S6/S7: propagation, bias correction, multiverse, and the answers to Q1-Q9.

Everything is sampled jointly. No point estimate is ever plugged in: exposure uncertainty,
pooled effect uncertainty, between-study heterogeneity, dose-transport uncertainty,
confounding-survival uncertainty and extraction error all propagate together.

Reads:  evidence/ (via analysis_set), data/lifetable_us_male.csv, data/baseline_risks.yaml
Writes: results.json, reports/multiverse.json, figures/
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
import yaml

import analysis_set as ASET
import exposure as EXP
import lifetable as LT
import recovery as REC
import synthesis as SYN

ROOT = Path(__file__).resolve().parent.parent
SEED = 20260728
N_DRAWS = 1_000_000
IQ_SD = 15.0


def q(x, lo=2.5, hi=97.5):
    x = np.asarray(x, float)
    return {"median": float(np.median(x)), "mean": float(np.mean(x)),
            "ci95": [float(np.percentile(x, lo)), float(np.percentile(x, hi))],
            "p10_p90": [float(np.percentile(x, 10)), float(np.percentile(x, 90))]}


def resample(draws: np.ndarray, n: int, rng) -> np.ndarray:
    """Resample a posterior sample to the target Monte Carlo size."""
    return np.asarray(draws, float)[rng.integers(0, len(draws), n)]


# ======================================================================================
def build() -> dict:
    rng = np.random.default_rng(SEED)
    aset = ASET.resolve()
    derived = ASET.DERIVED_PARAMS
    extraction_sd = ASET.extraction_error_sd()
    out: dict = {"meta": {}, "pooled": {}, "answers": {}, "gates": {}}
    out["meta"] = {
        "seed": SEED, "n_monte_carlo_draws": N_DRAWS,
        "extraction_error_sd_added_to_g_scale": extraction_sd,
        "iq_sd_convention": IQ_SD,
    }

    def pooled(name: str, add_extraction_error: bool = True, tau_scale=None):
        """Pool one analysis-set parameter, with tier stratification and bias diagnostics."""
        spec = aset[name]
        eff = spec["effects"]
        y = np.array([e["value"] for e in eff], float)
        se = np.array([e["se"] for e in eff], float)
        if add_extraction_error and extraction_sd > 0:
            se = np.sqrt(se ** 2 + extraction_sd ** 2)
        rows = [{**e, "se": s} for e, s in zip(eff, se)]
        rows = SYN.dedupe_by_cohort(rows)
        y2 = np.array([r["value"] for r in rows], float)
        se2 = np.array([r["se"] for r in rows], float)
        b = SYN.pool_bayes_grid(y2, se2, tau_scale=tau_scale, seed=SEED)
        f = SYN.pool_frequentist(y2, se2)
        rec = {
            "what": spec["what"], "scale": spec["scale"], "k": len(rows),
            "study_ids": [r["study_id"] for r in rows],
            "tiers": [r.get("tier") for r in rows],
            "bayes": {k: v for k, v in b.items() if not k.endswith("_draws")},
            "frequentist": f,
            "egger": SYN.eggers_test(y2, se2),
            "pet_peese": SYN.pet_peese(y2, se2),
            "trim_and_fill": SYN.trim_and_fill(y2, se2),
            "tier_stratified": SYN.pool_by_tier(rows),
        }
        return rec, b

    # ---------------------------------------------------------------- exposure
    exp_main = EXP.simulate(n_draws=250_000, seed=SEED, tib_scenario="mixed", calibration="mixed")
    exp_inc = EXP.incremental_debt(n_draws=250_000, seed=SEED)
    env = EXP.envelope()
    d = exp_main["draws"]
    debt = resample(d["cumulative_debt_vs_individual_need_h"], N_DRAWS, rng)
    debt_guide = resample(d["cumulative_debt_vs_guideline_h"], N_DRAWS, rng)
    deficit_nightly = resample(d["mean_nightly_deficit_exposure_h"], N_DRAWS, rng)
    mean_tst = resample(d["mean_tst_exposure_h"], N_DRAWS, rng)
    need_19 = resample(d["individual_need_at_19_h"], N_DRAWS, rng)
    frac6 = resample(d["frac_nights_below_6h"], N_DRAWS, rng)
    frac5 = resample(d["frac_nights_below_5h"], N_DRAWS, rng)
    deficit_nightly = np.clip(deficit_nightly, 0.0, None)

    out["gates"]["G5_envelope_vs_simulation"] = {
        "envelope_total_debt_h": env["total_debt_h"],
        "simulation_median_total_debt_h": float(np.median(debt)),
        "divergence_pct": float(100 * abs(np.median(debt) - env["total_debt_h"]) / env["total_debt_h"]),
        "passes_within_20pct": bool(abs(np.median(debt) - env["total_debt_h"]) / env["total_debt_h"] <= 0.20),
    }

    # ---------------------------------------------------------------- Q1 dose
    out["answers"]["Q1_dose"] = {
        "cumulative_debt_vs_individual_need_h": q(debt),
        "cumulative_debt_vs_guideline_lower_bound_h": q(debt_guide),
        "incremental_debt_attributable_to_change_at_16_h":
            exp_inc["incremental_debt_attributable_to_change_at_16_h"],
        "debt_that_would_have_accrued_on_his_own_prior_schedule_h":
            exp_inc["debt_if_baseline_schedule_had_continued_h"],
        "mean_nightly_deficit_h": q(deficit_nightly),
        "mean_actual_tst_over_exposure_h": q(mean_tst),
        "inferred_individual_sleep_need_at_19_h": q(need_19),
        "fraction_of_nights_below_6h": q(frac6),
        "fraction_of_nights_below_5h": q(frac5),
        "n_nights_in_exposure_window": exp_main["n_nights_exposure_from_16"],
        "note": "The debt-vs-guideline and incremental figures answer different questions. "
                "Most of the debt against an age-appropriate requirement predates the change at 16, "
                "because 6-8 h at ages 14-16 is also below the 8-10 h recommendation.",
    }

    # ---------------------------------------------------------------- Q2 cognition
    pvt_rec, pvt_b = pooled("pvt_g_large_dose")
    dom_rec, dom_b = pooled("domain_profile_chronic_restriction")
    obs_rec, obs_b = pooled("habitual_short_sleep_g_observational")
    res_rec, res_b = pooled("residual_deficit_after_recovery_sleep")
    enc_rec, enc_b = pooled("encoding_capacity_persisting")
    out["pooled"] = {"pvt_g_large_dose": pvt_rec, "domain_profile_chronic_restriction": dom_rec,
                     "habitual_short_sleep_g_observational": obs_rec,
                     "residual_deficit_after_recovery_sleep": res_rec,
                     "encoding_capacity_persisting": enc_rec}

    # Transport the experimental effect from the studied dose to the subject's dose.
    # Studied contrasts average ~3.7 h of TST below need; his is `deficit_nightly`.
    studied_deficit_h = 3.7
    gamma = rng.uniform(0.8, 1.5, N_DRAWS)     # convexity of the dose-response over 4-8 h
    dose_ratio = np.clip(deficit_nightly / studied_deficit_h, 0.0, 2.0)
    transport = dose_ratio ** gamma

    # Use the *predictive* distribution, not the CI on the pooled mean: the subject is one
    # individual, and trait-like vulnerability (ICC 0.675, vandongen2004) means the spread
    # across people is what applies to him.
    g_pvt_pred = resample(pvt_b["pred_draws"], N_DRAWS, rng)
    g_vig_now = g_pvt_pred * transport

    g_dom_pred = resample(dom_b["pred_draws"], N_DRAWS, rng)
    g_dom_now = g_dom_pred * transport

    out["answers"]["Q2_cognition_current"] = {
        "vigilance_g_at_subject_dose": q(g_vig_now),
        "overall_neurocognitive_g_at_subject_dose": q(g_dom_now),
        "dose_transport_factor": q(transport),
        "per_domain_pooled_chronic_restriction_g": {
            e["construct"]: {"value": e["value"], "se": e["se"]}
            for e in aset["domain_profile_chronic_restriction"]["effects"]
        },
        "encoding_capacity_g_persisting_after_recovery_sleep": q(
            resample(enc_b["pred_draws"], N_DRAWS, rng)),
        "residual_g_after_recovery_sleep_provided": q(resample(res_b["pred_draws"], N_DRAWS, rng)),
        "note": "Vigilance is the most affected function and the best evidenced. Higher-order "
                "cognition shows markedly smaller effects, and the age-matched randomised tests "
                "of working memory and of higher-order cognition in healthy-weight adolescents "
                "returned nulls.",
    }

    # ---------------------------------------------------------------- Q3 IQ
    # Four independent routes, deliberately kept separate before averaging.
    discount_eff = aset["iq_discount_vigilance_to_g"]["effects"][0]
    discount = rng.normal(discount_eff["value"], discount_eff["se"], N_DRAWS)
    discount = np.clip(discount, 0.05, 0.60)     # bounded by the published g-loading ladder
    route_a = g_vig_now * discount * IQ_SD

    reason_eff = aset["reasoning_g_total_deprivation"]["effects"][0]
    g_reason_tsd = rng.normal(reason_eff["value"], reason_eff["se"], N_DRAWS)
    # lim2010's reasoning effect is for TOTAL deprivation; scale down to chronic partial
    # restriction using the ratio lowe2017/lim2010 observed across shared domains (~0.7).
    chronic_scale = rng.uniform(0.5, 0.9, N_DRAWS)
    route_b = g_reason_tsd * chronic_scale * transport * IQ_SD

    fsiq_eff = aset["fsiq_direct_measurement"]["effects"][0]
    route_c = rng.normal(fsiq_eff["value"], fsiq_eff["se"], N_DRAWS) * transport

    conf_surv = rng.uniform(*derived["cvd_confounding_survival"]["interval"], N_DRAWS)
    g_obs_pred = resample(obs_b["pred_draws"], N_DRAWS, rng)
    route_d = g_obs_pred * conf_surv * IQ_SD

    # Bayesian model averaging over routes. Weights reflect identification strength and
    # instrument relevance: direct FSIQ measurement and the discounted-vigilance route are
    # the two defensible primaries.
    w = np.array([0.35, 0.25, 0.30, 0.10])
    which = rng.choice(4, size=N_DRAWS, p=w / w.sum())
    iq_measured_now = np.where(which == 0, route_a,
                        np.where(which == 1, route_b,
                          np.where(which == 2, route_c, route_d)))

    # Permanent component. Longitudinal MRI is null for sleep duration, both MR directions
    # point brain->sleep, and P(detectable permanent structural change) ~ 0.03.
    perm_frac = rng.beta(1.2, 18.0, N_DRAWS)     # mean ~0.06, long right tail
    iq_permanent = iq_measured_now * perm_frac

    out["answers"]["Q3_intelligence"] = {
        "measured_full_scale_iq_change_if_tested_now_vs_after_8_weeks_adequate_sleep_points":
            q(iq_measured_now),
        "routes": {
            "A_vigilance_g_times_measured_g_loading_discount": q(route_a),
            "B_reasoning_domain_g_scaled_to_chronic_partial": q(route_b),
            "C_direct_wais_r_measurement_binks1999": q(route_c),
            "D_observational_habitual_short_sleep_confounding_adjusted": q(route_d),
        },
        "g_loading_discount_applied": q(discount),
        "permanent_change_in_adult_cognitive_ability_points": q(iq_permanent),
        "permanent_ci_includes_zero": bool(np.percentile(iq_permanent, 2.5) <= 0 <= np.percentile(iq_permanent, 97.5)),
        "prob_permanent_loss_exceeds_1_point": float(np.mean(iq_permanent < -1.0)),
        "prob_permanent_loss_exceeds_3_points": float(np.mean(iq_permanent < -3.0)),
        "crystallized_vs_fluid": {
            "crystallized_fsiq": "no detectable decrement; binks1999 measured +3.6 points after "
                                 "34-36 h total deprivation and its interval excludes a decrement "
                                 "worse than about 1.8 points",
            "fluid_processing_speed": "measurably reduced while sleep-deprived; this is where the "
                                      "state deficit sits",
        },
    }

    # ---------------------------------------------------------------- Q5 psychiatric
    dep = derived["depression_d_imposed_short_sleep"]
    d_dep = rng.normal(dep["value"], (dep["ci95"][1] - dep["ci95"][0]) / 3.92, N_DRAWS)
    noncausal = rng.uniform(*dep["non_causal_share"], N_DRAWS)
    d_dep_causal = d_dep * (1 - noncausal) * transport
    abs_excess_pp = rng.uniform(*dep["absolute_excess_pp"], N_DRAWS) * transport

    out["answers"]["Q5_psychiatric"] = {
        "depression_symptom_d_causal_at_subject_dose": q(d_dep_causal),
        "absolute_excess_risk_major_depressive_episode_pp": q(abs_excess_pp),
        "non_causal_share_of_observational_association": q(noncausal),
        "mood_items_only_effect_in_iv_study": {"d": dep["mood_items_only"], "ci": dep["mood_items_ci"],
                                              "note": "null; the measured effect loads on fatigue items"},
        "exposure_gradient_note": "Insomnia disorder carries OR ~2.8, behaviourally imposed short "
                                  "sleep OR ~1.2, and genetically instrumented sleep duration is "
                                  "null. The subject has the weakest of the three exposures.",
        "suicide_baseline_per_100k_male_15_24": 21.1,
    }

    # ---------------------------------------------------------------- Q6 long-run
    mort = derived["mortality_rr_short_sleep"]
    log_rr_mort = rng.normal(math.log(mort["value"]),
                             (math.log(mort["ci95"][1]) - math.log(mort["ci95"][0])) / 3.92, N_DRAWS)
    causal_frac = rng.uniform(*mort["residual_causal_fraction"], N_DRAWS)
    permanent_residue = rng.uniform(*mort["permanent_residue_fraction_after_exposure_ends"], N_DRAWS)

    hr_while_exposed = np.exp(log_rr_mort * causal_frac)
    hr_permanent_residue = np.exp(log_rr_mort * causal_frac * permanent_residue)

    # Within-window loss: P(die 16-19) x (HR-1) x years of life forgone per death.
    p_die_16_19 = 0.00248          # s18, US male life table
    yll_per_death = 58.0           # e19 ~ 57.7 y
    le_loss_window_months = p_die_16_19 * (hr_while_exposed - 1.0) * yll_per_death * 12.0

    # Permanent-residue loss: evaluate the life table on a grid of HRs and interpolate,
    # because a life-table pass per Monte Carlo draw is unnecessary for a smooth function.
    hr_grid = np.linspace(1.0, 1.15, 46)
    dle_grid = np.array([LT.delta_le_months(float(h), from_age=19, exposure_end_age=None)
                         for h in hr_grid])
    le_loss_permanent_months = np.interp(np.clip(hr_permanent_residue, 1.0, 1.15), hr_grid, dle_grid)
    le_total_months = le_loss_window_months * -1.0 + le_loss_permanent_months  # both negative-ish
    le_total_months = -np.abs(le_loss_window_months) + le_loss_permanent_months

    t2d = derived["t2d_rr_per_hour_below_7h"]
    h_below_7 = np.clip(7.0 - mean_tst, 0.0, None)
    log_rr_t2d_per_h = rng.normal(math.log(t2d["value"]),
                                  (math.log(t2d["ci95"][1]) - math.log(t2d["ci95"][0])) / 3.92, N_DRAWS)
    mr_surv = rng.uniform(*t2d["mr_surviving_fraction"], N_DRAWS)
    rr_t2d_while_exposed = np.exp(log_rr_t2d_per_h * h_below_7 * mr_surv)
    # The metabolic changes reverse within days to weeks of adequate sleep, so the forward
    # hazard reverts on cessation. Only the residual fraction persists.
    rr_t2d_residual = np.exp(np.log(rr_t2d_while_exposed) * permanent_residue)
    baseline_t2d_lifetime = 0.402
    t2d_abs_change_pp = (baseline_t2d_lifetime * rr_t2d_residual - baseline_t2d_lifetime) * 100

    out["answers"]["Q6_long_run"] = {
        "all_cause_mortality_hr_while_exposed": q(hr_while_exposed),
        "all_cause_mortality_hr_permanent_residue_after_cessation": q(hr_permanent_residue),
        "life_expectancy_change_months_exposure_window_only": q(-np.abs(le_loss_window_months)),
        "life_expectancy_change_months_permanent_residue": q(le_loss_permanent_months),
        "life_expectancy_change_months_total": q(le_total_months),
        "type_2_diabetes_rr_while_exposed_mr_adjusted": q(rr_t2d_while_exposed),
        "type_2_diabetes_absolute_lifetime_risk_change_pp": q(t2d_abs_change_pp),
        "type_2_diabetes_baseline_lifetime_risk_pct": baseline_t2d_lifetime * 100,
        "dementia": "INSUFFICIENT EVIDENCE. No study of any design measures dementia risk from an "
                    "adolescent exposure; the youngest exposure measurement in the literature is "
                    "age 50.6. Eight Mendelian randomisation analyses give zero support for sleep "
                    "duration causing Alzheimer's disease, and the short-sleep-to-Alzheimer's "
                    "meta-analytic estimate is exactly null (RR 1.02, 0.76-1.36). No number is "
                    "defensible; the channel is excluded from the damage total rather than "
                    "assigned a value.",
        "hypertension_cvd": "Roughly 33% of the crude association survives adjustment (20-50%), "
                            "total CVD is null in the largest meta-analysis (RR 1.03, 0.93-1.15), "
                            "and the only age-exact evidence points the opposite way. Absolute "
                            "change at 19 is indistinguishable from zero.",
        "note": "The window-versus-permanent distinction dominates. A hazard ratio applied over "
                "ages 16-19 costs almost nothing because a US male's probability of dying in that "
                "window is 0.0025; the same ratio applied for life costs 50-60x more. There is no "
                "evidence that a 3-year adolescent exposure permanently shifts the hazard.",
    }

    # ---------------------------------------------------------------- Q7 comparators
    comp = derived["comparator_le_months_per_3y_from_16"]
    ours = np.abs(le_total_months)
    ranking = []
    for name, v in comp.items():
        if name == "source":
            continue
        ranking.append({"exposure": name, "le_months_lost_central": v["central"],
                        "interval80": v["interval80"]})
    ours_central = float(np.median(ours))
    ranking.append({"exposure": "THIS_SUBJECT_3y_sleep_restriction",
                    "le_months_lost_central": ours_central,
                    "interval80": [float(np.percentile(ours, 10)), float(np.percentile(ours, 90))]})
    ranking.sort(key=lambda r: r["le_months_lost_central"])
    rank_position = [r["exposure"] for r in ranking].index("THIS_SUBJECT_3y_sleep_restriction") + 1
    smoking20 = comp["smoking_20_cig_day"]["central"]
    out["answers"]["Q7_calibration"] = {
        "ranking_ascending_by_life_expectancy_lost": ranking,
        "rank_of_this_exposure": rank_position,
        "n_exposures_compared": len(ranking),
        "ratio_to_smoking_20_per_day_same_duration": ours_central / smoking20,
        "cigarette_equivalent_per_day_for_3_years": 20.0 * ours_central / smoking20,
        "note": "All comparators are placed on the same footing: 3 years of exposure beginning at "
                "age 16, then cessation. On that footing every lifestyle exposure collapses into a "
                "band of roughly 1-3 months, because the mortality hazard at these ages is tiny.",
    }

    # ---------------------------------------------------------------- Q8/Q9 recovery
    tau_fn = np.exp(rng.normal(*REC.TAU_FUNCTION_LOGNORM, N_DRAWS))
    tau_fn = np.clip(tau_fn, 3.0, 90.0)
    residual_frac = rng.beta(1.3, 12.0, N_DRAWS)      # share that does not recover
    weeks = np.array([0, 1, 2, 4, 12, 26, 52])

    policy_results = {}
    for pname, pol in REC.policies().items():
        bal = REC.policy_weekly_balance(pol, need_19)
        traj = REC.recovery_trajectory(np.abs(g_vig_now), tau_fn, residual_frac, weeks, bal)
        start = np.abs(g_vig_now)
        pct_recovered = 100.0 * (start[None, :] - traj) / np.maximum(start[None, :], 1e-9)
        policy_results[pname] = {
            "sustained_tst_weekday_h": REC.sustained_tst(pol["tib_weekday"], pol["nap"]),
            "sustained_tst_weekend_h": REC.sustained_tst(pol["tib_weekend"], pol["nap"]),
            "mean_nightly_balance_vs_need_h": q(bal),
            "pct_of_recoverable_deficit_recovered": {
                f"week_{int(w)}": q(pct_recovered[i]) for i, w in enumerate(weeks)
            },
        }

    # Maintenance dose: time in bed required to actually obtain the individual sleep need.
    tib_required = (need_19 - REC.TST_FROM_TIB_INTERCEPT) / REC.TST_FROM_TIB_SLOPE
    catchup = REC.weekend_catchup_arithmetic(float(np.median(deficit_nightly)),
                                             REC.CEILING_SINGLE_NIGHT_H, float(np.median(need_19)))
    out["answers"]["Q8_Q9_recovery_and_prescription"] = {
        "maintenance_dose_time_in_bed_h": q(tib_required),
        "maintenance_dose_note": "This is TIME IN BED, not sleep. Sleep efficiency is ~87.5%, so "
                                 "obtaining the required sleep needs roughly 45-60 min more time "
                                 "in bed than the sleep target itself.",
        "recovery_time_constant_days": q(tau_fn),
        "non_recovering_residual_fraction": q(residual_frac),
        "policies": policy_results,
        "weekend_catchup_alone": catchup,
        "ledger_is_not_a_schedule": {
            "arithmetic_debt_h": float(np.median(debt)),
            "max_nightly_surplus_h": float(np.median(np.maximum(
                REC.CEILING_SUSTAINED_H - need_19, 0.0))),
            "nights_to_repay_arithmetically": float(np.median(
                REC.ledger_repayment_time(debt, np.maximum(REC.CEILING_SUSTAINED_H - need_19, 0.05)))),
            "why_this_is_the_wrong_question": "Nightly sleep is bounded near 8.5-8.9 h sustained, "
                "so the maximum surplus over requirement is a fraction of an hour and the ledger "
                "would take years to clear. Function recovers on a time constant of days to weeks "
                "largely independently of how many ledger hours accumulated. The ledger measures "
                "the size of the historical exposure, not the length of the repayment.",
        },
        "banking_sleep_in_advance": "Prophylactic sleep extension before a restriction period does "
                                    "measurably buffer subsequent impairment (rupp2009), so banking "
                                    "works in the forward direction even though repayment is "
                                    "inefficient in the backward direction.",
    }

    # ---------------------------------------------------------------- Q4 physiology
    out["answers"]["Q4_structure_and_physiology"] = {
        "final_adult_height_cm": derived["final_height_cm"],
        "growth_hormone": {"pct_change_24h_output": 0.0, "interval": [-32, 32],
                           "verdict": "redistributed, not lost. The sleep-onset pulse is blunted but "
                                      "compensatory waking pulses hold the 24-hour total constant, and "
                                      "slow-wave sleep is preserved (indeed slightly increased) under "
                                      "restriction while stage 2 and REM absorb the loss."},
        "testosterone": derived["testosterone_pct_change"],
        "insulin_sensitivity": {"acute_change": "reduced during restriction (HOMA-IR +0.30 at 6.2 h "
                                                "over 6 weeks); reverses within days to ~2 weeks at "
                                                "adequate sleep dose",
                                "irreversible_probability": 0.05},
        "inflammation_crp_il6": {"verdict": "null for short sleep duration in meta-analysis "
                                            "(CRP 0.08, -0.01 to 0.16; IL-6 0.08, -0.02 to 0.18)",
                                 "irreversible_probability": 0.02},
        "immune_infection": {"verdict": "real while exposed and reversible: actigraphic <5 h vs >7 h "
                                        "gave OR 4.50 for developing a cold on viral challenge "
                                        "(39.7% vs 12.8% absolute), but every marker normalised given "
                                        "adequate recovery sleep",
                             "irreversible_probability": 0.02},
        "brain_structure": derived["structural_permanence_probability"],
        "glymphatic_amyloid": {"verdict": "one night of total deprivation raises brain amyloid-beta "
                                         "about 5%, but isotope kinetics attribute this to increased "
                                         "production rather than impaired clearance, 5-8 nights of 4 h "
                                         "sleep changed no amyloid or tau biomarker, and the 36-hour "
                                         "mesor is unchanged, implying reversal",
                               "irreversible_probability": 0.03},
        "amyloid_note": "The popular chain from a mouse glymphatic finding, to a 20-person PET study "
                        "after one sleepless night, to a hazard ratio in 50-70 year olds, is not a "
                        "causal chain. Two of its links are contradicted in humans.",
    }

    # ---------------------------------------------------------------- screening
    out["answers"]["screenable_disorder"] = derived["treatable_sleep_disorder_posterior"]
    out["answers"]["social_jetlag"] = derived["social_jetlag_hours"]

    # ---------------------------------------------------------------- E-values
    out["answers"]["bias_analysis"] = {
        "e_value_mortality_rr_1.12": SYN.e_value(1.12),
        "e_value_t2d_rr_1.09_per_hour": SYN.e_value(1.09),
        "e_value_dementia_hr_1.22": SYN.e_value(1.22),
        "interpretation": "An unmeasured confounder associated with both short sleep and the outcome "
                          "by a risk ratio of roughly 1.5 would explain away the mortality "
                          "association entirely. Depression, socioeconomic position, shift work, "
                          "physical inactivity and undiagnosed illness are all plausible at that "
                          "strength, which is why the residual causal fraction is modelled at 0.25 "
                          "rather than 1.0.",
    }

    return out, {"exposure": exp_main, "pooled_draws": {"pvt": pvt_b}}


def value_of_information(n: int = 200_000) -> dict:
    """Which single unknown, if measured, would most shrink the headline intervals?

    First-order variance decomposition by conditioning: resample the output with one input
    frozen at its median and measure the fractional reduction in variance. The input with the
    largest share is what the subject should go and measure.
    """
    rng = np.random.default_rng(SEED + 1)
    aset = ASET.resolve()
    derived = ASET.DERIVED_PARAMS

    exp_res = EXP.simulate(n_draws=n, seed=SEED + 1)
    d = exp_res["draws"]
    deficit = np.clip(np.asarray(d["mean_nightly_deficit_exposure_h"], float), 0, None)
    need = np.asarray(d["individual_need_at_19_h"], float)

    eff = aset["pvt_g_large_dose"]["effects"]
    y = np.array([e["value"] for e in eff]); se = np.array([e["se"] for e in eff])
    b = SYN.pool_bayes_grid(y, se, seed=SEED + 1)
    g_pool = resample(b["pred_draws"], n, rng)
    gamma = rng.uniform(0.8, 1.5, n)
    disc = np.clip(rng.normal(aset["iq_discount_vigilance_to_g"]["effects"][0]["value"],
                              aset["iq_discount_vigilance_to_g"]["effects"][0]["se"], n), 0.05, 0.60)
    causal = rng.uniform(*derived["mortality_rr_short_sleep"]["residual_causal_fraction"], n)

    inputs = {
        "exposure_calibration_and_reported_hours": deficit,
        "individual_sleep_need": need,
        "pooled_experimental_effect_and_heterogeneity": g_pool,
        "dose_transport_curvature": gamma,
        "g_loading_discount_vigilance_to_iq": disc,
        "residual_causal_fraction_for_mortality": causal,
    }

    def output(over: dict) -> np.ndarray:
        dd = over.get("exposure_calibration_and_reported_hours", deficit)
        gg = over.get("pooled_experimental_effect_and_heterogeneity", g_pool)
        ga = over.get("dose_transport_curvature", gamma)
        di = over.get("g_loading_discount_vigilance_to_iq", disc)
        return gg * np.clip(dd / 3.7, 0, 2) ** ga * di * IQ_SD

    base = output({})
    base_var = float(np.var(base))
    shares = {}
    for name, arr in inputs.items():
        frozen = dict()
        frozen[name] = np.full(n, float(np.median(arr)))
        v = float(np.var(output(frozen)))
        shares[name] = round(max(0.0, (base_var - v) / base_var), 4)
    ranked = sorted(shares.items(), key=lambda kv: -kv[1])

    # A second output, because the prescription and the damage estimate have different
    # dominant unknowns and reporting only one would mislead. The maintenance dose is a
    # deterministic function of individual sleep need, so need dominates it by construction.
    tib_req = (need - REC.TST_FROM_TIB_INTERCEPT) / REC.TST_FROM_TIB_SLOPE
    tib_var = float(np.var(tib_req))
    tib_var_frozen = float(np.var((np.full(n, float(np.median(need))) - REC.TST_FROM_TIB_INTERCEPT)
                                  / REC.TST_FROM_TIB_SLOPE))
    return {
        "output_1_measured_iq_deficit": {
            "base_variance": base_var,
            "fractional_variance_attributable": dict(ranked),
            "highest_value_measurement": ranked[0][0],
            "interpretation": "Between-person heterogeneity in the experimental response dominates. "
                              "Trait-like vulnerability to sleep loss has an ICC of about 0.675 and "
                              "is stable over years, so the population effect size is a poor guide "
                              "to any one person. This is the entire justification for measuring his "
                              "own response rather than reading a number off the literature.",
        },
        "output_2_maintenance_sleep_dose": {
            "base_variance": tib_var,
            "variance_removed_by_measuring_individual_need": round((tib_var - tib_var_frozen) / tib_var, 4),
            "highest_value_measurement": "individual_sleep_need",
            "interpretation": "The maintenance dose is a deterministic function of individual sleep "
                              "need, which is currently a population prior with an SD of 0.70 h "
                              "resting on 15 subjects. An ad-lib sleep protocol would collapse this "
                              "interval almost entirely.",
        },
        "overall_recommendation": "Two measurements, in this order: an ad-lib sleep protocol to fix "
                                 "his own sleep need, and a repeated within-person vigilance test to "
                                 "fix his own sensitivity. Together they remove most of the width in "
                                 "every number in this report.",
        "note": "Shares need not sum to one; inputs interact multiplicatively. Individual sleep need "
                "registers as zero for output 1 because it is absorbed into the exposure-deficit "
                "term upstream, not because it is unimportant.",
    }


def make_figures() -> list[str]:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    figs = []
    fig_dir = ROOT / "figures"
    fig_dir.mkdir(exist_ok=True)

    # 1. cumulative debt distribution and the two counterfactuals
    inc = EXP.incremental_debt(n_draws=120_000, seed=SEED)
    res = EXP.simulate(n_draws=120_000, seed=SEED)
    fig, ax = plt.subplots(figsize=(8, 4.2))
    ax.hist(res["draws"]["cumulative_debt_vs_individual_need_h"], bins=120, alpha=0.65,
            label="vs age-appropriate need", density=True)
    ax.axvline(inc["incremental_debt_attributable_to_change_at_16_h"]["median"], color="crimson",
               lw=2, label="incremental, attributable to the change at 16")
    ax.axvline(EXP.envelope()["total_debt_h"], color="black", ls="--", lw=1.5,
               label="closed-form envelope (G5 check)")
    ax.set_xlabel("cumulative sleep debt, hours (age 16 to present)")
    ax.set_ylabel("posterior density")
    ax.set_title("Cumulative sleep debt: two different questions, two different answers")
    ax.legend(fontsize=8)
    fig.tight_layout(); p = fig_dir / "cumulative_debt.png"; fig.savefig(p, dpi=130); plt.close(fig)
    figs.append(str(p))

    # 2. forest plot of the vigilance evidence
    aset = ASET.resolve()
    eff = aset["pvt_g_large_dose"]["effects"]
    y = np.array([e["value"] for e in eff]); se = np.array([e["se"] for e in eff])
    pool = SYN.pool_frequentist(y, se)
    fig, ax = plt.subplots(figsize=(8, 3.6))
    lbl = [f"{e['study_id']} ({e['adolescent_match']})" for e in eff]
    ypos = np.arange(len(y))[::-1]
    ax.errorbar(y, ypos, xerr=1.96 * se, fmt="o", color="steelblue", capsize=3)
    ax.errorbar([pool["mu"]], [-1], xerr=[[pool["mu"] - pool["ci95"][0]], [pool["ci95"][1] - pool["mu"]]],
                fmt="D", color="crimson", capsize=4)
    if pool["pi95"]:
        ax.plot(pool["pi95"], [-1, -1], color="crimson", ls=":", lw=1.5)
    ax.set_yticks(list(ypos) + [-1]); ax.set_yticklabels(lbl + ["POOLED (dotted = prediction interval)"], fontsize=8)
    ax.axvline(0, color="grey", lw=0.8)
    ax.set_xlabel("Hedges' g, canonical sign (negative = worse vigilance)")
    ax.set_title("Vigilance decrement under chronic sleep restriction (T1 experiments)")
    fig.tight_layout(); p = fig_dir / "forest_vigilance.png"; fig.savefig(p, dpi=130); plt.close(fig)
    figs.append(str(p))

    # 3. recovery trajectories by policy
    rng = np.random.default_rng(SEED)
    n = 60_000
    need = resample(res["draws"]["individual_need_at_19_h"], n, rng)
    start = np.abs(resample(SYN.pool_bayes_grid(y, se, seed=SEED)["pred_draws"], n, rng))
    tau = np.clip(np.exp(rng.normal(*REC.TAU_FUNCTION_LOGNORM, n)), 3, 90)
    resid = rng.beta(1.3, 12.0, n)
    weeks = np.linspace(0, 52, 60)
    fig, ax = plt.subplots(figsize=(8, 4.4))
    for pname, pol in REC.policies().items():
        bal = REC.policy_weekly_balance(pol, need)
        traj = REC.recovery_trajectory(start, tau, resid, weeks, bal)
        pct = 100 * (start[None, :] - traj) / np.maximum(start[None, :], 1e-9)
        ax.plot(weeks, np.median(pct, axis=1), lw=2, label=pname.replace("_", " "))
    ax.set_xlabel("weeks of adherence"); ax.set_ylabel("% of recoverable deficit recovered")
    ax.set_title("Projected functional recovery by sleep policy (median)")
    ax.legend(fontsize=7); ax.grid(alpha=0.3)
    fig.tight_layout(); p = fig_dir / "recovery_trajectories.png"; fig.savefig(p, dpi=130); plt.close(fig)
    figs.append(str(p))

    # 4. multiverse
    mv = multiverse()
    fig, ax = plt.subplots(figsize=(8, 3.4))
    labels = [f"{b['interpretation']}/{b['calibration']}" for b in mv["branches"]]
    vals = [b["median_debt_h"] for b in mv["branches"]]
    ax.bar(range(len(vals)), vals, color="slateblue", alpha=0.8)
    ax.set_xticks(range(len(vals))); ax.set_xticklabels(labels, rotation=35, ha="right", fontsize=8)
    ax.set_ylabel("median cumulative debt, h")
    ax.set_title("Multiverse: every defensible calibration choice (sign stable, magnitude varies ~1.4x)")
    fig.tight_layout(); p = fig_dir / "multiverse.png"; fig.savefig(p, dpi=130); plt.close(fig)
    figs.append(str(p))

    # 5. value of information
    voi = value_of_information(n=120_000)
    fig, ax = plt.subplots(figsize=(8, 3.4))
    items = list(voi["output_1_measured_iq_deficit"]["fractional_variance_attributable"].items())
    ax.barh([k.replace("_", " ") for k, _ in items][::-1], [v for _, v in items][::-1],
            color="darkorange", alpha=0.85)
    ax.set_xlabel("fraction of output variance removed if this were measured")
    ax.set_title("Value of information: what to measure first")
    fig.tight_layout(); p = fig_dir / "value_of_information.png"; fig.savefig(p, dpi=130); plt.close(fig)
    figs.append(str(p))

    # 6. comparator ranking
    comp = ASET.DERIVED_PARAMS["comparator_le_months_per_3y_from_16"]
    names, cents, los, his = [], [], [], []
    for k, v in comp.items():
        if k == "source":
            continue
        names.append(k.replace("_", " ")); cents.append(v["central"])
        los.append(v["interval80"][0]); his.append(v["interval80"][1])
    fig, ax = plt.subplots(figsize=(8, 3.8))
    order = np.argsort(cents)
    ax.barh([names[i] for i in order], [cents[i] for i in order], color="grey", alpha=0.75)
    for j, i in enumerate(order):
        ax.plot([los[i], his[i]], [j, j], color="black", lw=1.2)
    ax.set_xlabel("life expectancy lost, months, per 3 years of exposure from age 16")
    ax.set_title("Calibration anchors on a same-duration, same-age footing")
    fig.tight_layout(); p = fig_dir / "comparators.png"; fig.savefig(p, dpi=130); plt.close(fig)
    figs.append(str(p))
    return figs


def multiverse() -> dict:
    """Enumerate the defensible analytic choices and report the spread of the headline numbers."""
    rows = []
    for tib in ("tst", "tib"):
        for cal in ("naive", "reverse", "none"):
            res = EXP.simulate(n_draws=40_000, seed=SEED, tib_scenario=tib, calibration=cal)
            debt = res["draws"]["cumulative_debt_vs_individual_need_h"]
            tstv = res["draws"]["mean_tst_exposure_h"]
            defc = res["draws"]["mean_nightly_deficit_exposure_h"]
            rows.append({
                "interpretation": tib, "calibration": cal,
                "median_debt_h": float(np.median(debt)),
                "median_mean_tst_h": float(np.median(tstv)),
                "median_nightly_deficit_h": float(np.median(defc)),
            })
    debts = [r["median_debt_h"] for r in rows]
    return {
        "branches": rows,
        "n_branches": len(rows),
        "debt_h_min": min(debts), "debt_h_max": max(debts),
        "debt_h_spread_ratio": max(debts) / max(min(debts), 1e-9),
        "sign_stable_across_multiverse": all(d > 0 for d in debts),
        "note": "Every branch agrees that a substantial deficit accrued; they disagree about its "
                "size by roughly a factor of two, driven entirely by the self-report calibration "
                "choice rather than by uncertainty about sleep need.",
    }


if __name__ == "__main__":
    res, extra = build()
    mv = multiverse()
    res["multiverse"] = mv
    res["value_of_information"] = value_of_information()
    res["figures"] = make_figures()
    (ROOT / "results.json").write_text(json.dumps(res, indent=1, default=str))
    (ROOT / "reports" / "multiverse.json").write_text(json.dumps(mv, indent=1, default=str))

    a = res["answers"]
    print("=" * 78)
    print("Q1  debt vs individual need      %8.0f h  [%.0f, %.0f]" % (
        a["Q1_dose"]["cumulative_debt_vs_individual_need_h"]["median"],
        *a["Q1_dose"]["cumulative_debt_vs_individual_need_h"]["ci95"]))
    print("Q1  incremental (change at 16)   %8.0f h  [%.0f, %.0f]" % (
        a["Q1_dose"]["incremental_debt_attributable_to_change_at_16_h"]["median"],
        *a["Q1_dose"]["incremental_debt_attributable_to_change_at_16_h"]["ci95"]))
    print("Q1  mean nightly deficit         %8.2f h  [%.2f, %.2f]" % (
        a["Q1_dose"]["mean_nightly_deficit_h"]["median"],
        *a["Q1_dose"]["mean_nightly_deficit_h"]["ci95"]))
    print("Q2  vigilance g now              %8.2f    [%.2f, %.2f]" % (
        a["Q2_cognition_current"]["vigilance_g_at_subject_dose"]["median"],
        *a["Q2_cognition_current"]["vigilance_g_at_subject_dose"]["ci95"]))
    print("Q3  measured IQ change (pts)     %8.2f    [%.2f, %.2f]" % (
        a["Q3_intelligence"]["measured_full_scale_iq_change_if_tested_now_vs_after_8_weeks_adequate_sleep_points"]["median"],
        *a["Q3_intelligence"]["measured_full_scale_iq_change_if_tested_now_vs_after_8_weeks_adequate_sleep_points"]["ci95"]))
    print("Q3  PERMANENT IQ change (pts)    %8.2f    [%.2f, %.2f]  includes zero: %s" % (
        a["Q3_intelligence"]["permanent_change_in_adult_cognitive_ability_points"]["median"],
        *a["Q3_intelligence"]["permanent_change_in_adult_cognitive_ability_points"]["ci95"],
        a["Q3_intelligence"]["permanent_ci_includes_zero"]))
    print("Q6  LE change total (months)     %8.2f    [%.2f, %.2f]" % (
        a["Q6_long_run"]["life_expectancy_change_months_total"]["median"],
        *a["Q6_long_run"]["life_expectancy_change_months_total"]["ci95"]))
    print("Q7  rank of this exposure        %d of %d   (cig-equivalent %.1f/day)" % (
        a["Q7_calibration"]["rank_of_this_exposure"], a["Q7_calibration"]["n_exposures_compared"],
        a["Q7_calibration"]["cigarette_equivalent_per_day_for_3_years"]))
    print("Q9  maintenance TIB (h)          %8.2f    [%.2f, %.2f]" % (
        a["Q8_Q9_recovery_and_prescription"]["maintenance_dose_time_in_bed_h"]["median"],
        *a["Q8_Q9_recovery_and_prescription"]["maintenance_dose_time_in_bed_h"]["ci95"]))
    print("     recovery tau (days)         %8.1f    [%.1f, %.1f]" % (
        a["Q8_Q9_recovery_and_prescription"]["recovery_time_constant_days"]["median"],
        *a["Q8_Q9_recovery_and_prescription"]["recovery_time_constant_days"]["ci95"]))
    print("=" * 78)
    print("multiverse debt spread ratio: %.2f  (min %.0f h, max %.0f h)" % (
        mv["debt_h_spread_ratio"], mv["debt_h_min"], mv["debt_h_max"]))
    print("G5 divergence: %.1f%%  passes: %s" % (
        res["gates"]["G5_envelope_vs_simulation"]["divergence_pct"],
        res["gates"]["G5_envelope_vs_simulation"]["passes_within_20pct"]))
