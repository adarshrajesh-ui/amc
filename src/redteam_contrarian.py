"""Contrarian (red-team) recomputation of the headline numbers.

Runs the project's own engines under the most favourable parameter choices that remain
defensible from the corpus, and prints a side-by-side against the published results.

Every parameter change is annotated with the evidence record that licenses it. Nothing here
invents an effect estimate; the changes are all choices among values already in evidence/.

Usage:  python3 redteam_contrarian.py
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

import analysis_set as ASET
import exposure as EXP
import lifetable as LT
import synthesis as SYN

ROOT = Path(__file__).resolve().parent.parent
SEED = 20260728
N = 400_000
IQ_SD = 15.0


def q(x, name=""):
    x = np.asarray(x, float)
    return {"name": name, "median": float(np.median(x)), "mean": float(np.mean(x)),
            "ci95": [float(np.percentile(x, 2.5)), float(np.percentile(x, 97.5))],
            "p10_p90": [float(np.percentile(x, 10)), float(np.percentile(x, 90))]}


def line(label, s, unit="", w=46):
    return (f"  {label:<{w}s} {s['median']:9.3f}  [{s['ci95'][0]:8.3f}, "
            f"{s['ci95'][1]:8.3f}] {unit}")


# ======================================================================================
# 1. EXPOSURE
# ======================================================================================
def run_exposure(branch: dict, n_draws: int = 150_000) -> dict:
    """Run EXP.simulate with patched priors. Restores globals afterwards."""
    saved = {k: EXP.PRIORS[k] for k in ("need_at_16_h", "need_at_19_h", "reverse_beta_options",
                                        "need_sd_individual_h", "sleep_efficiency")}
    saved_curve = EXP.need_curve
    try:
        EXP.PRIORS["need_at_16_h"] = branch["need16"]
        EXP.PRIORS["need_at_19_h"] = branch["need19"]
        EXP.PRIORS["reverse_beta_options"] = branch["beta_options"]
        EXP.PRIORS["need_sd_individual_h"] = branch.get("need_sd", 0.70)
        EXP.PRIORS["sleep_efficiency"] = branch.get("efficiency", (0.875, 0.06))

        n16, n19 = branch["need16"], branch["need19"]
        lo, hi = min(n16, n19) - 0.001, max(n16, n19) + 0.001

        def curve(ages, _n16=n16, _n19=n19, _lo=lo, _hi=hi):
            return np.clip(_n16 + (np.asarray(ages) - 16.0) * (_n19 - _n16) / 3.0, _lo, _hi)

        EXP.need_curve = curve
        res = EXP.simulate(n_draws=n_draws, seed=SEED,
                           tib_scenario=branch["tib"], calibration=branch["cal"])
    finally:
        EXP.PRIORS.update(saved)
        EXP.need_curve = saved_curve
    d = res["draws"]
    return {
        "debt": np.asarray(d["cumulative_debt_vs_individual_need_h"], float),
        "deficit": np.asarray(d["mean_nightly_deficit_exposure_h"], float),
        "tst": np.asarray(d["mean_tst_exposure_h"], float),
        "need19": np.asarray(d["individual_need_at_19_h"], float),
        "frac6": np.asarray(d["frac_nights_below_6h"], float),
        "n_nights": res["n_nights_exposure_from_16"],
    }


BRANCHES = {
    # Project central, reproduced for calibration of this script against results.json.
    "P_project_central": dict(
        tib="mixed", cal="mixed", beta_options=(0.19, 0.50, 1.00), need16=9.00, need19=8.70,
        why="published analysis: 50/50 TIB-vs-TST branch, calibration averaged over "
            "naive/reverse/none, need from the T1 satiation asymptotes"),

    # C1: change ONLY the calibration, to the one the shard itself recommends, at the one
    # slope measured in age-matched adolescents (white2026ffcws beta = 0.19, 95% CI 0.13-0.26).
    "C1_agematched_calibration_only": dict(
        tib="tst", cal="reverse", beta_options=(0.19, 0.19, 0.19), need16=9.00, need19=8.70,
        why="reports read as TST and calibrated by reverse regression at the only slope measured "
            "in 14-17 year olds (white2026ffcws beta=0.19); need unchanged"),

    # C2: C1 + individual need shrunk by the OSD-on-HSD regression inside kitamura2016
    # (r = 0.514 between optimal and habitual sleep duration).
    "C2_plus_individual_need_regression": dict(
        tib="tst", cal="reverse", beta_options=(0.19, 0.19, 0.19), need16=8.14, need19=8.14,
        why="C1 + kitamura2016's own OSD-on-HSD slope (r=0.514) applied to a habitually short "
            "sleeper: 8.41 - 0.31*(6.5-7.37)/1 ~ 8.14 h", need_sd=0.60),

    # C3: unit-matched on the SELF-REPORT scale. Exposure = the reports as given; referent =
    # wild2018's cognitive optimum, which is also a self-reported duration (7.38 h, n=10,886).
    "C3_unitmatched_selfreport_scale": dict(
        tib="tst", cal="none", beta_options=(0.19, 0.19, 0.19), need16=7.38, need19=7.38,
        why="both sides of the subtraction on the self-report scale: reported hours vs wild2018's "
            "self-reported cognitive optimum 7.38 h"),

    # C4: unit-matched on the TST scale. Exposure calibrated to TST at beta=0.19, referent =
    # wild2018's optimum put through the SAME calibration (7.0 + 0.19*(7.38-8.0) = 6.88 h).
    "C4_unitmatched_tst_scale": dict(
        tib="tst", cal="reverse", beta_options=(0.19, 0.19, 0.19), need16=6.88, need19=6.88,
        why="both sides on the objective-TST scale: reverse-regressed exposure vs the same "
            "reverse regression applied to wild2018's optimum. Reductio: at beta=0.19 the "
            "report is so uninformative that the exposure gradient nearly vanishes"),

    # C6: the TIB branch, with sleep efficiency measured AT A RESTRICTED TIB rather than at a
    # habitual one. campbell2024 (n=159, 9.9-22.8 y): night-4 TST was 401.7 min at 7 h TIB
    # = 95.6% efficiency, versus 525.8 min at 10 h TIB = 87.6%. Efficiency rises as TIB falls
    # because sleep-onset latency collapses (campbell2021: SOL 3.7 min at 7 h vs 21.4 min at
    # 10 h TIB). The published model applies the habitual 0.875 to a restricted TIB.
    "C6_tib_branch_restricted_efficiency": dict(
        tib="tib", cal="none", beta_options=(0.19, 0.19, 0.19), need16=9.00, need19=8.70,
        efficiency=(0.956, 0.03),
        why="if the reports are TIB, efficiency at a SHORT TIB is ~0.956 (campbell2024), not the "
            "habitual 0.875; need left at the published value to isolate this one lever"),

    # C5: my headline contrarian central. Adult reverse-regression slope (cespedes2016hchs
    # beta = 0.333, a larger and tighter study than white2026), referent at the functional
    # optimum band (wild2018 7.38 / yin2017 mortality nadir 7.0 / fjell2023 volumetric 6.5).
    "C5_contrarian_central": dict(
        tib="tst", cal="reverse", beta_options=(0.333, 0.333, 0.333), need16=7.40, need19=7.20,
        why="cespedes2016hchs beta=0.333 (n=2086, CI 0.317-0.367) + referent at the functional "
            "optimum rather than the satiation asymptote (wild2018 7.38 h cognitive optimum; "
            "yin2017 mortality nadir 7.0 h; fjell2023 volumetric optimum 6.5 h)"),
}


# ======================================================================================
# 2. VIGILANCE POOL
# ======================================================================================
def vigilance_pools(extraction_sd: float) -> dict:
    aset = ASET.resolve()
    eff = aset["pvt_g_large_dose"]["effects"]
    by_id = {e["study_id"]: e for e in eff}

    def pool(rows, tag):
        y = np.array([r["value"] for r in rows], float)
        se = np.sqrt(np.array([r["se"] for r in rows], float) ** 2 + extraction_sd ** 2)
        b = SYN.pool_bayes_grid(y, se, seed=SEED)
        f = SYN.pool_frequentist(y, se)
        pp = SYN.pet_peese(y, se) if len(rows) >= 3 else {"recommended": None}
        tf = SYN.trim_and_fill(y, se) if len(rows) >= 3 else {"adjusted_mu": None}
        return {"tag": tag, "k": len(rows), "ids": [r["study_id"] for r in rows],
                "bayes_mu": b["mu_median"], "pred_draws": b["pred_draws"],
                "freq_mu": f["mu"], "freq_ci": f["ci95"], "i2": f["i2"],
                "pet": pp.get("recommended"), "trimfill": tf.get("adjusted_mu")}

    all_rows = list(eff)
    # lo2016 is excluded on the adjudicator's own finding: its magnitude comes either from
    # figure digitisation with quote:null (violating extraction hard-rule 2) or from
    # d = 2*sqrt(f2) applied to a PROC MIXED group-by-day interaction, which the adjudicator
    # ruled "does not hold". Blinded re-extraction confidence on this row is "low".
    no_lo = [e for e in eff if e["study_id"] != "lo2016"]
    # Dose-matched subset: contrasts of about 2 h of TIB below the referent, i.e. the closest
    # available match to the subject's own weekday shortfall.
    dose_matched = [e for e in eff if e["study_id"] in
                    ("vandongen2003", "belenky2003", "pejovic2013_recovery_dissociation")]
    return {"all": pool(all_rows, "all 5 (published)"),
            "drop_lo2016": pool(no_lo, "lo2016 excluded"),
            "dose_matched": pool(dose_matched, "dose-matched (~2 h below referent)"),
            "by_id": by_id}


# ======================================================================================
def main() -> None:
    rng = np.random.default_rng(SEED)
    aset = ASET.resolve()
    extraction_sd = ASET.extraction_error_sd()
    report: dict = {}

    print("=" * 96)
    print("CONTRARIAN RECOMPUTATION".center(96))
    print("=" * 96)

    # ---------------------------------------------------------------- exposure
    print("\n[1] EXPOSURE  (n_nights in window = 1040)\n")
    print(f"  {'branch':<38s} {'debt (h)':>10s} {'95% CI':>20s}  {'TST':>6s} {'deficit':>8s}")
    exp_out = {}
    for name, br in BRANCHES.items():
        r = run_exposure(br)
        exp_out[name] = r
        sd = q(r["debt"])
        print(f"  {name:<38s} {sd['median']:10.0f} "
              f"[{sd['ci95'][0]:8.0f},{sd['ci95'][1]:8.0f}] "
              f"{np.median(r['tst']):6.2f} {np.median(r['deficit']):8.2f}")
        report[f"exposure::{name}"] = {
            "why": br["why"],
            "debt_h": q(r["debt"]), "mean_tst_h": q(r["tst"]),
            "mean_nightly_deficit_h": q(r["deficit"]),
            "frac_nights_below_6h": q(r["frac6"]),
        }

    central = exp_out["C5_contrarian_central"]
    deficit_c = np.clip(central["deficit"], 0.0, None)
    need19_c = central["need19"]

    # ---------------------------------------------------------------- vigilance
    print("\n[2] VIGILANCE POOL  (Hedges' g, negative = worse)\n")
    vp = vigilance_pools(extraction_sd)
    print("  per-study inputs:")
    for sid, e in vp["by_id"].items():
        print(f"    {sid:<36s} g={e['value']:+7.3f} se={e['se']:.3f} "
              f"dose={str(e['dose_h']):>4s}h ref={str(e['referent_h']):>4s}h "
              f"match={e['adolescent_match']}")
    print()
    for k in ("all", "drop_lo2016", "dose_matched"):
        p = vp[k]
        pet = f"{p['pet']:+.3f}" if p["pet"] is not None else "  n/a"
        tf = f"{p['trimfill']:+.3f}" if p["trimfill"] is not None else "  n/a"
        print(f"  {p['tag']:<38s} k={p['k']}  bayes mu={p['bayes_mu']:+.3f}  "
              f"freq mu={p['freq_mu']:+.3f}  I2={p['i2']:5.1f}%  PET={pet}  trim&fill={tf}")
        report[f"vigilance_pool::{k}"] = {
            "k": p["k"], "study_ids": p["ids"], "bayes_mu_median": p["bayes_mu"],
            "frequentist_mu": p["freq_mu"], "frequentist_ci95": p["freq_ci"],
            "i2": p["i2"], "pet_recommended": p["pet"], "trim_and_fill_mu": p["trimfill"],
        }

    def resample(dr, n):
        dr = np.asarray(dr, float)
        return dr[rng.integers(0, len(dr), n)]

    # transport to the subject's dose, using the project's own functional form
    studied_deficit_h = 3.7
    gamma = rng.uniform(0.8, 1.5, N)
    transport_c = np.clip(resample(deficit_c, N) / studied_deficit_h, 0.0, 2.0) ** gamma

    g_pool_all = resample(vp["all"]["pred_draws"], N)
    g_pool_nolo = resample(vp["drop_lo2016"]["pred_draws"], N)

    g_vig_published_style = g_pool_all * np.clip(
        resample(np.clip(exp_out["P_project_central"]["deficit"], 0, None), N) / 3.7, 0, 2) ** gamma
    g_vig_contrarian = g_pool_nolo * transport_c

    print()
    print(line("vigilance g, published inputs (check)", q(g_vig_published_style)))
    print(line("vigilance g, CONTRARIAN", q(g_vig_contrarian)))
    print(line("  transport factor, contrarian", q(transport_c)))
    report["vigilance_g_published_reproduction"] = q(g_vig_published_style)
    report["vigilance_g_contrarian"] = q(g_vig_contrarian)
    report["transport_factor_contrarian"] = q(transport_c)

    # --- which lever does the work? exposure branch x pool choice, no double counting ---
    # The dose-matched pool is anchored at its OWN studied shortfall (~2 h TIB below the
    # referent, which is ~1.75 h of TST at 0.875 efficiency), not at the 3.7 h the published
    # model assumes, otherwise the dose correction would be applied twice.
    print("\n  sensitivity grid: median vigilance g by exposure branch x pooling choice")
    print(f"    {'branch':<38s} {'all 5 @3.7h':>12s} {'no lo2016 @3.7h':>16s} "
          f"{'dose-matched @1.75h':>21s}")
    grid = {}
    for name in BRANCHES:
        dfc = np.clip(exp_out[name]["deficit"], 0, None)
        dfc_n = resample(dfc, N)
        row = {}
        for tag, pool_key, anchor in (("all5", "all", 3.7),
                                      ("no_lo2016", "drop_lo2016", 3.7),
                                      ("dose_matched", "dose_matched", 1.75)):
            tr = np.clip(dfc_n / anchor, 0.0, 2.0) ** gamma
            gv = resample(vp[pool_key]["pred_draws"], N) * tr
            row[tag] = q(gv)
        grid[name] = row
        print(f"    {name:<38s} {row['all5']['median']:12.3f} "
              f"{row['no_lo2016']['median']:16.3f} {row['dose_matched']['median']:21.3f}")
    report["vigilance_g_sensitivity_grid"] = grid
    report["vigilance_g_contrarian_dose_matched_pool"] = \
        grid["C5_contrarian_central"]["dose_matched"]
    print("    (published cell = P_project_central x all5 = the -0.87 headline)")

    # fraction of the contrarian posterior in which no debt accrued at all
    for name in ("C1_agematched_calibration_only", "C5_contrarian_central",
                 "C4_unitmatched_tst_scale"):
        f0 = float(np.mean(exp_out[name]["debt"] <= 0.0))
        report[f"exposure::{name}"]["prob_no_net_debt"] = f0
        print(f"    P(no net debt at all) under {name}: {f0:.3f}")

    # ---------------------------------------------------------------- IQ
    print("\n[3] MEASURED IQ CHANGE IF TESTED NOW  (points)\n")
    disc_eff = aset["iq_discount_vigilance_to_g"]["effects"][0]
    discount = np.clip(rng.normal(disc_eff["value"], disc_eff["se"], N), 0.05, 0.60)
    route_a = g_vig_contrarian * discount * IQ_SD

    reason_eff = aset["reasoning_g_total_deprivation"]["effects"][0]
    g_reason = rng.normal(reason_eff["value"], reason_eff["se"], N)
    chronic_scale = rng.uniform(0.5, 0.9, N)
    route_b = g_reason * chronic_scale * transport_c * IQ_SD

    # binks1999 raw +3.6 points, but the same record carries a baseline screening-IQ imbalance
    # of +2.7 points favouring the deprived group. The imbalance-corrected point estimate is
    # +0.9. Carried here as the honest version of the direct-measurement route.
    fsiq = aset["fsiq_direct_measurement"]["effects"][0]
    route_c_raw = rng.normal(fsiq["value"], fsiq["se"], N) * transport_c
    route_c_adj = rng.normal(fsiq["value"] - 2.7, fsiq["se"], N) * transport_c

    # observational route, at the subject's own dose only (wild2018 5.5 h vs 7.38 h optimum,
    # overall composite -0.083 SD), rather than pooled with the 4.0 h contrast
    obs_dose_matched = rng.normal(-0.083, 0.072, N)
    conf_surv = rng.uniform(0.20, 0.50, N)
    route_d = obs_dose_matched * conf_surv * IQ_SD

    w = np.array([0.35, 0.25, 0.30, 0.10])
    which = rng.choice(4, size=N, p=w / w.sum())
    iq_contrarian = np.where(which == 0, route_a,
                     np.where(which == 1, route_b,
                       np.where(which == 2, route_c_adj, route_d)))

    for nm, arr in [("route A  vigilance x g-loading", route_a),
                    ("route B  reasoning, chronic-scaled", route_b),
                    ("route C  binks1999 raw (+3.6)", route_c_raw),
                    ("route C' binks1999 imbalance-corrected", route_c_adj),
                    ("route D  observational, dose-matched", route_d),
                    ("BMA measured IQ change, CONTRARIAN", iq_contrarian)]:
        print(line(nm, q(arr), "pts"))
        report[f"iq_route::{nm.strip()}"] = q(arr)
    report["iq_measured_contrarian"] = q(iq_contrarian)

    # ---------------------------------------------------------------- permanent IQ
    print("\n[4] PERMANENT IQ CHANGE  (points)\n")
    perm_project = rng.beta(1.2, 18.0, N)                 # mean 0.0625
    perm_contra = rng.beta(1.0, 32.0, N)                  # mean 0.0303, matches the shard's own
    for nm, pf in [("perm. IQ, project's Beta(1.2,18)", perm_project),
                   ("perm. IQ, structural prior 0.03", perm_contra)]:
        arr = iq_contrarian * pf
        print(line(nm, q(arr), "pts"))
        print(f"      P(loss > 1 pt) = {float(np.mean(arr < -1.0)):.5f}   "
              f"P(loss > 3 pt) = {float(np.mean(arr < -3.0)):.5f}   "
              f"mean permanence fraction = {float(np.mean(pf)):.4f}")
        report[f"permanent_iq::{nm.strip()}"] = {
            **q(arr), "p_loss_gt_1pt": float(np.mean(arr < -1.0)),
            "p_loss_gt_3pt": float(np.mean(arr < -3.0))}

    # ---------------------------------------------------------------- life expectancy
    print("\n[5] LIFE EXPECTANCY  (months, negative = lost)\n")
    p_die_16_19 = 0.00248
    yll_per_death = 58.0
    hr_grid = np.linspace(1.0, 1.15, 61)
    dle_grid = np.array([LT.delta_le_months(float(h), from_age=19, exposure_end_age=None)
                         for h in hr_grid])

    def le_block(rr, ci, causal_iv, resid_iv, tag, note):
        log_rr = rng.normal(math.log(rr), (math.log(ci[1]) - math.log(ci[0])) / 3.92, N)
        cf = rng.uniform(*causal_iv, N)
        pr = rng.uniform(*resid_iv, N)
        hr_win = np.exp(log_rr * cf)
        hr_perm = np.exp(log_rr * cf * pr)
        win = -np.abs(p_die_16_19 * (hr_win - 1.0) * yll_per_death * 12.0)
        perm = np.interp(np.clip(hr_perm, 1.0, 1.15), hr_grid, dle_grid)
        tot = win + perm
        print(f"  {tag}")
        print(f"      {note}")
        print(line("    HR while exposed", q(hr_win), "", 44))
        print(line("    LE lost, window only", q(win), "mo", 44))
        print(line("    LE lost, permanent residue", q(perm), "mo", 44))
        print(line("    LE lost, TOTAL", q(tot), "mo", 44))
        report[f"life_expectancy::{tag}"] = {
            "note": note, "rr": rr, "ci95": list(ci),
            "residual_causal_fraction": list(causal_iv),
            "permanent_residue_fraction": list(resid_iv),
            "hr_while_exposed": q(hr_win), "le_months_window": q(win),
            "le_months_permanent": q(perm), "le_months_total": q(tot)}
        return tot

    le_pub = le_block(1.12, (1.06, 1.18), (0.0, 0.50), (0.0, 0.12),
                      "PUBLISHED: categorical short-sleep RR 1.12",
                      "cappuccio2010 categorical bin, pooled cutpoints <5 h to <7 h")
    le_dose = le_block(1.01, (1.00, 1.015), (0.0, 0.50), (0.0, 0.12),
                       "CONTRARIAN a: dose-specific spline at 6 h, RR 1.01",
                       "yin2017 spline at 6 h (40 cohorts, 3,582,016 people)")
    le_male = le_block(1.02, (0.98, 1.06), (0.0, 0.28), (0.0, 0.12),
                       "CONTRARIAN b: male-specific at 6 h, RR 1.02 + MR-bounded causal share",
                       "liu2017 males-only 6 h RR 1.02 (0.98-1.06); causal share capped by "
                       "sambou2024 (28% survives MR) and zhang2025 (0% survives)")

    print("\n  comparator anchors, same 3-year footing (s18): "
          "smoking 20/day 1.8 mo, alcohol 200-350 g/wk 3.0 mo, inactivity 0.8 mo")
    print(f"  contrarian central total: {np.median(le_male):.4f} mo "
          f"= {np.median(le_male)*30.44:.2f} days")
    report["le_contrarian_central_days"] = float(np.median(le_male) * 30.44)

    # ---------------------------------------------------------------- learning channel
    print("\n[5b] THE 'LEARNING-LOSS CHANNEL' WITH THE AGE-MATCHED NULLS PUT BACK\n")
    print("  The published analysis set gives this channel k = 1 (cousins2018, g = -0.89).")
    print("  The corpus contains three further randomised restriction experiments in 14-19")
    print("  year olds with declarative-memory outcomes. Two are exact nulls whose effect rows")
    print("  carry se: null, so they are unpoolable as recorded and drop out silently.")
    learn = [
        ("cousins2018   5h x5n, picture recognition after 3 recovery nights", -0.890, 0.270, 59),
        ("huang2016     5h x?n, GRE vocabulary cued recall (retention)", -0.408, 0.271, 56),
        ("huang2016     5h x?n, GRE vocabulary after review session", -0.329, 0.270, 56),
        ("voderholzer2011  9/8/7/6/5h x4n, declarative word pairs: NULL", 0.000, 0.213, 88),
        ("kopasz2010    4h x1n, declarative recall: NULL", 0.000, 0.426, 22),
    ]
    for nm, v, s, n in learn:
        print(f"    {nm:<62s} g={v:+.3f}  se={s:.3f}  n={n}")
    for tag, subset in (("published (cousins2018 only)", learn[:1]),
                        ("cousins + the 2 age-matched nulls", [learn[0], learn[3], learn[4]]),
                        ("all 5 adolescent memory rows", learn)):
        y = np.array([r[1] for r in subset], float)
        se = np.sqrt(np.array([r[2] for r in subset], float) ** 2 + extraction_sd ** 2)
        if len(y) == 1:
            mu, ci = float(y[0]), [float(y[0] - 1.96 * se[0]), float(y[0] + 1.96 * se[0])]
        else:
            f = SYN.pool_frequentist(y, se)
            mu, ci = f["mu"], f["ci95"]
        print(f"    -> {tag:<40s} g = {mu:+.3f}  95% CI [{ci[0]:+.3f}, {ci[1]:+.3f}]")
        report[f"learning_channel::{tag}"] = {"g": mu, "ci95": [float(c) for c in ci],
                                             "k": len(subset)}
    print("    SEs for the two null rows are independent-groups approximations at g = 0")
    print("    (sqrt(4/n)); the corpus records no SE for them. Labelled illustrative.")

    # ---------------------------------------------------------------- prescription
    print("\n[6] PRESCRIPTION: time in bed required to obtain the requirement\n")
    import recovery as REC
    for tag, nd in (("published need 8.70 h", 8.70), ("contrarian need 7.40 h", 7.40),
                    ("contrarian need 7.20 h", 7.20)):
        tib = (nd - REC.TST_FROM_TIB_INTERCEPT) / REC.TST_FROM_TIB_SLOPE
        print(f"  {tag:<34s} required TIB = {tib:5.2f} h")
        report[f"prescription::{tag}"] = {"need_h": nd, "required_tib_h": float(tib)}
    tib_c = (need19_c - REC.TST_FROM_TIB_INTERCEPT) / REC.TST_FROM_TIB_SLOPE
    print(line("  contrarian maintenance TIB (full posterior)", q(tib_c), "h", 44))
    report["prescription::contrarian_posterior"] = q(tib_c)

    (ROOT / "reports" / "redteam_contrarian_numbers.json").write_text(
        json.dumps(report, indent=1, default=str))
    print("\nwrote reports/redteam_contrarian_numbers.json")


if __name__ == "__main__":
    main()
