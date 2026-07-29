"""S4 Exposure engine.

Reconstructs a posterior over nightly total sleep time for every night from age 14.0 to the
present, then derives cumulative sleep debt.

The self-reported hours are not used as measured hours. Four corrections are applied, each
carrying its own uncertainty:

1. Time-in-bed versus total-sleep-time ambiguity (two scenarios, never averaged silently).
2. Self-report calibration. Two defensible and materially different corrections exist:
   subtracting the mean self-report-minus-actigraphy bias, or reverse regression that treats a
   low report as partly regression to the mean. These disagree by more than the effect being
   estimated, so both are carried as an explicit model-uncertainty axis.
3. Recall rounding: reports cluster on integers and half hours. The rounding error is shared
   across all nights an epoch summarises, so it is drawn once per epoch, not per night.
4. Calendar structure: school weeks, breaks and exam periods, rather than a flat average.

Sleep need is a latent individual trait, drawn once per simulated person and held fixed across
the whole exposure history, because a person does not get a new sleep requirement every night.

Sources for every prior are listed in PRIORS below with the study_id they come from; the
corresponding YAML records live in evidence/ and are citation-verified by src/verify_refs.py.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent

# --------------------------------------------------------------------------------------
# Priors. Every entry names the evidence record it derives from.
# --------------------------------------------------------------------------------------
PRIORS = {
    # s06 exposure_priors.md: self-report minus objective TST, pooled over 8 studies
    # (adolescent mean 1.12 h, adult 0.99 h).
    "bias_mean_h": (1.00, 0.30),
    # Reverse-regression slope of true sleep on reported sleep. lauderdale2008 gives 0.51
    # (0.35-0.67); age-matched adolescent estimates are much flatter (0.19, 0.13-0.26).
    "reverse_beta_options": (0.19, 0.50, 1.00),
    "reverse_anchor_report_h": 8.0,
    "reverse_anchor_true_h": 7.0,
    # Sleep efficiency TST/TIB in healthy 16-25 year olds (evans2021, mitterling2015,
    # meredithjones2024 -> 0.872 / 0.870 / 0.891).
    "sleep_efficiency": (0.875, 0.06),
    # Individual sleep need. T1 evidence is flat across the guideline step at 18:
    # short2018sleepneed 9.0-9.35 h at 15-17; klerman2008 asymptote 8.9 h at 18-32;
    # kitamura2016 asymptote 8.41 h. SD of individual need 0.70 h (0.44-0.96), thin evidence.
    "need_at_16_h": 9.00,
    "need_at_19_h": 8.70,
    "need_sd_individual_h": 0.70,
    # Night-to-night within-epoch variability. The subject reports weekday sleep ranging
    # 3-7 h around a ~5 h mean, implying roughly 1.0-1.3 h SD.
    "sigma_night_h": (1.15, 0.20),
    # Accrual time constant of the neurobehavioural deficit, ramakrishnan2016 tau_LA.
    "tau_accrue_days": (7.00, 1.67),
    # Recovery time constant. Sleep duration recovers in 2.5-5 d (kitamura2016 tau=2.52,
    # klerman2008 ~5 d); vigilance recovery exceeds 7 d and has never been observed to
    # complete, so the prior is deliberately wide and right-skewed.
    "tau_recover_days_lognorm": (np.log(16.0), 0.55),
    # Physiological ceilings on recovery sleep (klerman2008 asymptote 8.9 h with 16 h TIB;
    # single-night ceiling 10.0-10.4 h).
    "ceiling_single_night_h": 10.2,
    "ceiling_sustained_h": 8.9,
}

DAYS_PER_YEAR = 365.25


@dataclass
class Epoch:
    """One reported period of the subject's sleep history."""
    label: str
    age_start: float
    age_end: float
    weekday_report_h: float          # midpoint of the reported weekday range
    weekday_report_lo: float
    weekday_report_hi: float
    weekend_report_h: float
    weekend_report_lo: float
    weekend_report_hi: float
    in_school: bool = True
    # fraction of the epoch that is school/term time rather than holiday
    school_fraction: float = 0.69     # ~36 school weeks of 52
    exam_weeks_per_year: float = 4.0
    exam_weekday_report_h: float | None = None
    is_baseline: bool = False


# The reported ledger. Ranges are the subject's own words; midpoints are used as the
# central report and the range width feeds the report-level uncertainty.
EPOCHS = [
    Epoch("hs_freshman_sophomore", 14.0, 16.0, 7.0, 6.0, 8.0, 7.5, 7.0, 8.0,
          exam_weekday_report_h=6.0, is_baseline=True),
    Epoch("hs_junior", 16.0, 17.0, 5.5, 5.0, 6.0, 7.5, 7.0, 8.0,
          exam_weekday_report_h=3.5),
    Epoch("hs_senior", 17.0, 18.0, 5.5, 5.0, 6.0, 7.5, 7.0, 8.0,
          exam_weekday_report_h=3.5),
    # First college semester: most severe and highest variance; weekends reported >7 h
    # "averaged over 7 but maybe 20% below 7", occasionally stretching to 10-11 h.
    Epoch("college_y1_sem1", 18.0, 18.4, 5.0, 3.0, 7.0, 8.0, 7.0, 11.0,
          school_fraction=0.80, exam_weeks_per_year=5.0, exam_weekday_report_h=3.5),
    Epoch("college_y1_sem2", 18.4, 18.85, 5.5, 5.0, 6.0, 7.5, 7.0, 8.0,
          school_fraction=0.75, exam_weeks_per_year=5.0, exam_weekday_report_h=3.5),
]

AGE_NOW = 18.85


def build_calendar() -> dict:
    """Day-level calendar: for each night, which epoch, is it a weekend, is it term time."""
    nights = []
    for ep in EPOCHS:
        n_days = int(round((ep.age_end - ep.age_start) * DAYS_PER_YEAR))
        for d in range(n_days):
            age = ep.age_start + d / DAYS_PER_YEAR
            dow = d % 7
            is_weekend = dow in (5, 6)
            # Term time is allocated as a contiguous fraction of each year, with exam
            # periods placed at the end of term.
            year_pos = (age - ep.age_start) % 1.0
            in_term = year_pos < ep.school_fraction
            exam_frac = ep.exam_weeks_per_year * 7 / DAYS_PER_YEAR
            in_exam = in_term and (year_pos > max(0.0, ep.school_fraction - exam_frac))
            nights.append({"age": age, "epoch": ep.label, "is_weekend": is_weekend,
                           "in_term": in_term, "in_exam": in_exam,
                           "is_baseline": ep.is_baseline})
    return {"nights": nights, "epochs": {e.label: e for e in EPOCHS}}


def need_curve(ages: np.ndarray) -> np.ndarray:
    """Population-mean sleep need by age, linear between the two anchor ages."""
    a16, a19 = PRIORS["need_at_16_h"], PRIORS["need_at_19_h"]
    return np.clip(a16 + (ages - 16.0) * (a19 - a16) / 3.0, 8.0, 9.5)


def simulate(n_draws: int = 200_000, seed: int = 20260728,
             tib_scenario: str = "mixed", calibration: str = "mixed",
             counterfactual: str = "none", dtype=np.float32) -> dict:
    """Simulate the exposure history.

    tib_scenario: 'tst' (reports are total sleep time), 'tib' (reports are time in bed),
                  or 'mixed' (draw between them, 50/50).
    calibration:  'naive' (subtract mean bias), 'reverse' (reverse regression),
                  'none' (take reports at face value), or 'mixed' (draw among them).
    """
    rng = np.random.default_rng(seed)
    cal = build_calendar()
    nights = cal["nights"]
    epochs = cal["epochs"]
    n_nights = len(nights)

    # ---- person-level latent draws (once per simulated person) ----
    need_offset = rng.normal(0.0, PRIORS["need_sd_individual_h"], n_draws).astype(dtype)
    sigma_night = np.abs(rng.normal(*PRIORS["sigma_night_h"], n_draws)).astype(dtype)
    efficiency = np.clip(rng.normal(*PRIORS["sleep_efficiency"], n_draws), 0.70, 0.98).astype(dtype)
    bias = rng.normal(*PRIORS["bias_mean_h"], n_draws).astype(dtype)
    beta_choice = rng.integers(0, 3, n_draws)
    beta = np.array(PRIORS["reverse_beta_options"], dtype=dtype)[beta_choice]

    if tib_scenario == "tst":
        is_tib = np.zeros(n_draws, dtype=bool)
    elif tib_scenario == "tib":
        is_tib = np.ones(n_draws, dtype=bool)
    else:
        is_tib = rng.random(n_draws) < 0.5

    if calibration == "mixed":
        cal_choice = rng.integers(0, 3, n_draws)   # 0 naive, 1 reverse, 2 none
    else:
        cal_choice = np.full(n_draws, {"naive": 0, "reverse": 1, "none": 2}[calibration])

    # ---- epoch-level rounding error (shared across all nights in an epoch) ----
    round_err = {}
    for label in epochs:
        round_err[label] = {
            "weekday": rng.uniform(-0.5, 0.5, n_draws).astype(dtype),
            "weekend": rng.uniform(-0.5, 0.5, n_draws).astype(dtype),
        }

    # Fidelity of the subject's *relative* reports. Reverse regression corrects a person's
    # habitual level toward the population mean; it must not be applied to within-person
    # contrasts, or an exam all-nighter reported as 3.5 h would be "corrected" up to 6 h.
    contrast_fidelity = np.clip(rng.normal(0.90, 0.10, n_draws), 0.55, 1.0).astype(dtype)

    # The subject's own habitual reported level over the exposure window (age >= 16),
    # weighted by how many nights each report summarises.
    baseline_ep = next(e for e in EPOCHS if e.is_baseline)

    def report_for(night, force_baseline_schedule: bool = False):
        """The report governing this night. Under the counterfactual, nights from age 16
        onward are assigned the subject's own pre-16 reported schedule instead."""
        ep = epochs[night["epoch"]]
        if force_baseline_schedule and night["age"] >= 16.0:
            ep = baseline_ep
        if night["is_weekend"] or not night["in_term"]:
            return ep, ep.weekend_report_h, "weekend"
        if night["in_exam"] and ep.exam_weekday_report_h is not None:
            return ep, ep.exam_weekday_report_h, "weekday"
        return ep, ep.weekday_report_h, "weekday"

    use_cf = counterfactual == "own_baseline_schedule"

    _w, _tot = 0.0, 0.0
    for night in nights:
        if night["age"] < 16.0:
            continue
        _, r, _k = report_for(night, use_cf)
        _w += r
        _tot += 1
    habitual_report = _w / _tot

    def calibrate(report: np.ndarray) -> np.ndarray:
        """Map a self-reported duration onto a posterior mean true TST.

        Structure: correct the habitual LEVEL, then re-attach the within-person deviation of
        this night's report from the habitual level. The two interpretations of what the
        subject reported are mutually exclusive branches, never compounded:

          report = TST  -> apply the self-report-versus-actigraphy calibration
          report = TIB  -> apply sleep efficiency

        Applying both would subtract the same missing hour twice.
        """
        r = report.astype(dtype)
        deviation = (r - habitual_report) * contrast_fidelity

        # --- level correction, TST interpretation ---
        anchor_r, anchor_t = PRIORS["reverse_anchor_report_h"], PRIORS["reverse_anchor_true_h"]
        # beta = 1.0 reduces exactly to subtracting the mean bias, so the reverse-regression
        # family nests the naive correction as a special case.
        level_reverse = anchor_t + beta * (habitual_report - anchor_r)
        level_naive = habitual_report - bias
        level_none = np.full(n_draws, habitual_report, dtype=dtype)
        level_tst = np.where(cal_choice == 0, level_naive,
                             np.where(cal_choice == 1, level_reverse, level_none))
        # --- level correction, TIB interpretation ---
        level_tib = habitual_report * efficiency

        level = np.where(is_tib, level_tib, level_tst)
        return np.clip(level + deviation, 1.5, 12.0).astype(dtype)

    # ---- accumulators ----
    zeros = lambda: np.zeros(n_draws, dtype=np.float64)  # noqa: E731
    debt_arith = zeros()             # signed arithmetic ledger vs individual need, age >= 16
    debt_arith_guideline = zeros()   # signed arithmetic ledger vs guideline lower bound
    debt_positive_only = zeros()     # deficits only, surpluses not credited
    baseline_debt = zeros()          # age 14-16, reported as the "good schedule" period
    n_below_6 = zeros()
    n_below_5 = zeros()
    sum_tst = zeros()
    sum_tst_exposure = zeros()       # age >= 16 only
    n_exposure_nights = 0
    sum_deficit_exposure = zeros()

    # recency-weighted effective chronic dose, for the impairment dynamics
    tau_acc = np.abs(rng.normal(*PRIORS["tau_accrue_days"], n_draws)).astype(np.float64)
    tau_acc = np.clip(tau_acc, 2.0, 30.0)
    ewma_deficit = zeros()
    ewma_trace_idx, ewma_trace = [], []

    # per-epoch summaries
    epoch_sum = {label: {"tst": zeros(), "n": 0, "deficit": zeros()} for label in epochs}

    guideline_lower = {True: 8.0, False: 7.0}  # NSF lower bound: 8 h under 18, 7 h at 18+

    for i, night in enumerate(nights):
        age = night["age"]
        # Holiday and break weekdays revert toward the ad-lib weekend pattern.
        ep, rep, re_key = report_for(night, use_cf)
        report_vec = np.full(n_draws, rep, dtype=dtype) + round_err[ep.label][re_key]
        ep = epochs[night["epoch"]]  # accounting stays keyed to the real epoch
        mu_true = calibrate(report_vec)
        tst = mu_true + rng.normal(0.0, 1.0, n_draws).astype(dtype) * sigma_night
        tst = np.clip(tst, 1.5, PRIORS["ceiling_single_night_h"]).astype(np.float64)

        need = need_curve(np.array([age]))[0] + need_offset
        deficit = need - tst

        sum_tst += tst
        es = epoch_sum[ep.label]
        es["tst"] += tst
        es["deficit"] += deficit
        es["n"] += 1

        # The headline debt is the exposure window only: age 16.0 to the present. The
        # pre-exposure baseline years are accumulated separately, because using a
        # debt-laden baseline as its own referent would double-count it.
        if age >= 16.0:
            n_below_6 += (tst < 6.0)
            n_below_5 += (tst < 5.0)
            debt_arith += deficit
            debt_arith_guideline += (guideline_lower[age < 18.0] - tst)
            debt_positive_only += np.maximum(deficit, 0.0)
            sum_tst_exposure += tst
            sum_deficit_exposure += deficit
            n_exposure_nights += 1
        else:
            baseline_debt += deficit

        alpha = 1.0 / tau_acc
        ewma_deficit += alpha * (deficit - ewma_deficit)
        if i % 14 == 0:
            ewma_trace_idx.append(age)
            ewma_trace.append(float(np.mean(ewma_deficit)))

    n_baseline_nights = sum(1 for n in nights if n["is_baseline"])
    out = {
        "n_draws": n_draws,
        "n_nights_total": n_nights,
        "n_nights_exposure_from_16": n_exposure_nights,
        "n_nights_baseline_14_16": n_baseline_nights,
        "tib_scenario": tib_scenario,
        "calibration": calibration,
        "seed": seed,
        "draws": {
            "cumulative_debt_vs_individual_need_h": debt_arith,
            "cumulative_debt_vs_guideline_h": debt_arith_guideline,
            "cumulative_deficit_positive_only_h": debt_positive_only,
            "baseline_debt_age_14_16_h": baseline_debt,
            "mean_tst_all_nights_h": sum_tst / n_nights,
            "mean_tst_exposure_h": sum_tst_exposure / max(n_exposure_nights, 1),
            "mean_nightly_deficit_exposure_h": sum_deficit_exposure / max(n_exposure_nights, 1),
            "frac_nights_below_6h": n_below_6 / max(n_exposure_nights, 1),
            "frac_nights_below_5h": n_below_5 / max(n_exposure_nights, 1),
            "steady_state_ewma_deficit_h": ewma_deficit,
            "individual_need_at_19_h": PRIORS["need_at_19_h"] + need_offset,
        },
        "epoch_means": {
            label: {"mean_tst_h": float(np.mean(v["tst"] / v["n"])),
                    "mean_deficit_h": float(np.mean(v["deficit"] / v["n"])),
                    "n_nights": v["n"]}
            for label, v in epoch_sum.items()
        },
        "ewma_trace": {"age": ewma_trace_idx, "mean_ewma_deficit_h": ewma_trace},
    }
    return out


def summarize(draws: np.ndarray) -> dict:
    q = np.percentile(draws, [2.5, 25, 50, 75, 97.5])
    return {"mean": float(np.mean(draws)), "median": float(q[2]),
            "ci95": [float(q[0]), float(q[4])], "iqr": [float(q[1]), float(q[3])],
            "sd": float(np.std(draws))}


def envelope() -> dict:
    """Closed-form back-of-envelope for Gate G5, computed independently of the simulation.

    Deliberately crude: flat weekday/weekend averages, no measurement correction, no calendar.
    Its purpose is to catch an order-of-magnitude bug in the simulation, not to be right.
    """
    years = AGE_NOW - 16.0
    n_nights = years * DAYS_PER_YEAR
    weekday_frac, weekend_frac = 5 / 7, 2 / 7
    naive_weekday, naive_weekend = 5.5, 7.5
    school_frac = 0.72
    mean_tst_term = weekday_frac * naive_weekday + weekend_frac * naive_weekend
    mean_tst_break = naive_weekend
    mean_tst_reported = school_frac * mean_tst_term + (1 - school_frac) * mean_tst_break
    # A single flat calibration: reports overstate objective TST by ~1 h, applied once.
    mean_tst = mean_tst_reported - 1.0
    need = 8.85
    return {
        "years_exposed": years,
        "n_nights": n_nights,
        "mean_tst_h_reported": mean_tst_reported,
        "mean_tst_h_calibrated": mean_tst,
        "assumed_need_h": need,
        "mean_nightly_deficit_h": need - mean_tst,
        "total_debt_h": (need - mean_tst) * n_nights,
        "total_debt_h_uncalibrated": (need - mean_tst_reported) * n_nights,
    }


def incremental_debt(n_draws: int = 200_000, seed: int = 20260728) -> dict:
    """Debt attributable to the change in schedule at 16, versus the guideline referent.

    Two counterfactuals answer two different questions, and conflating them is the most
    common way to overstate this kind of estimate:

      vs guideline   - how far below an age-appropriate requirement was he? (the full debt)
      vs own baseline - what did *junior year onward* actually change? (the marginal debt)
    """
    actual = simulate(n_draws=n_draws, seed=seed, counterfactual="none")
    counter = simulate(n_draws=n_draws, seed=seed, counterfactual="own_baseline_schedule")
    a = actual["draws"]["cumulative_debt_vs_individual_need_h"]
    c = counter["draws"]["cumulative_debt_vs_individual_need_h"]
    return {
        "debt_vs_guideline_need_h": summarize(a),
        "debt_if_baseline_schedule_had_continued_h": summarize(c),
        "incremental_debt_attributable_to_change_at_16_h": summarize(a - c),
        "mean_tst_actual_h": summarize(actual["draws"]["mean_tst_exposure_h"]),
        "mean_tst_counterfactual_h": summarize(counter["draws"]["mean_tst_exposure_h"]),
    }


if __name__ == "__main__":
    env = envelope()
    print("--- G5 closed-form envelope (uncorrected, flat averages) ---")
    print(json.dumps(env, indent=1))
    res = simulate(n_draws=50_000)
    print("\n--- simulation (50k draws, mixed scenarios) ---")
    for k, v in res["draws"].items():
        s = summarize(v)
        print(f"  {k:42s} median={s['median']:8.2f}  95% CI [{s['ci95'][0]:8.2f}, {s['ci95'][1]:8.2f}]")
    print("\n--- epoch means ---")
    for label, v in res["epoch_means"].items():
        print(f"  {label:28s} n={v['n_nights']:4d}  mean TST={v['mean_tst_h']:.2f} h  "
              f"mean deficit={v['mean_deficit_h']:+.2f} h")
