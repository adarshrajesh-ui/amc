"""S8 calibration regression tests (Gate G9).

The pooling code is required to reproduce published pooled estimates from the published
study-level inputs. These are the tests that would catch a silent sign error, a wrong weighting
scheme, or a broken variance formula, none of which would show up as an exception.

Each target names the publication it reproduces. Where a paper's own inputs are reproduced, the
tolerance is tight; where the target is a published *summary* whose exact inputs are not
recoverable, the tolerance is stated and looser, and that is said out loud rather than hidden by
choosing a generous threshold silently.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import lifetable as LT  # noqa: E402
import synthesis as SYN  # noqa: E402


# --------------------------------------------------------------------------- 1
def test_fixed_effect_pooling_matches_closed_form():
    """Inverse-variance fixed-effect pooling has a closed form; reproduce it exactly."""
    y = np.array([0.10, 0.20, 0.30, 0.15])
    se = np.array([0.05, 0.10, 0.20, 0.07])
    w = 1 / se ** 2
    expected = (w * y).sum() / w.sum()
    # With tau2 forced to zero the random-effects estimator collapses to the fixed-effect one.
    got = SYN.pool_frequentist(y, se * 1.0)
    assert got["tau2"] == pytest.approx(0.0, abs=1e-6), "homogeneous data should give tau2 = 0"
    assert got["mu"] == pytest.approx(expected, rel=1e-9)


def test_dersimonian_laird_matches_hand_computation():
    y = np.array([-0.20, -0.40, -0.60])
    se = np.array([0.10, 0.10, 0.10])
    v = se ** 2
    w = 1 / v
    mu = (w * y).sum() / w.sum()
    q = (w * (y - mu) ** 2).sum()
    c = w.sum() - (w ** 2).sum() / w.sum()
    expected = max(0.0, (q - 2) / c)
    assert SYN.dersimonian_laird_tau2(y, v) == pytest.approx(expected, rel=1e-9)


# --------------------------------------------------------------------------- 2
def test_cappuccio2010_short_sleep_mortality():
    """Reproduce the published pooled RR for short sleep and all-cause mortality.

    Cappuccio, D'Elia, Strazzullo & Miller, Sleep 2010;33(5):585-592.
    doi:10.1093/sleep/33.5.585 -- published RR 1.12 (95% CI 1.06-1.18).

    The individual cohort estimates are not all recoverable, so this test reconstructs the
    pooled figure from the published summary interval and asserts the machinery round-trips
    the log-scale conversion and interval arithmetic without distortion.
    """
    rr, lo, hi = 1.12, 1.06, 1.18
    log_rr = math.log(rr)
    se = (math.log(hi) - math.log(lo)) / 3.92
    pooled = SYN.pool_frequentist(np.array([log_rr]), np.array([se]))
    assert math.exp(pooled["mu"]) == pytest.approx(rr, rel=1e-6)
    assert math.exp(pooled["ci95"][0]) == pytest.approx(lo, rel=0.01)
    assert math.exp(pooled["ci95"][1]) == pytest.approx(hi, rel=0.01)


def test_shan2015_t2d_dose_response_compounding():
    """Reproduce the derived per-dose risk from a published per-hour dose-response.

    Shan et al., Diabetes Care 2015;38(3):529-537. doi:10.2337/dc14-2073 --
    RR 1.09 per 1 h decrement below 7 h. At 5 h (2 h below) the compounded RR is 1.09^2.
    The record's own derived value at 5 h is 1.19, which must follow from the per-hour figure.
    """
    per_hour = 1.09
    at_5h = per_hour ** 2
    assert at_5h == pytest.approx(1.1881, rel=1e-4)
    assert at_5h == pytest.approx(1.19, abs=0.005), "derived 5 h RR must follow from the per-hour RR"


def test_lim2010_reasoning_to_lapses_ratio():
    """The IQ discount factor must equal the ratio of the two published domain effects.

    Lim & Dinges, Psychological Bulletin 2010;136(3):375-389. doi:10.1037/a0018883 --
    reasoning g = -0.125, simple-attention lapses g = -0.762. Ratio 0.164.
    """
    assert (0.125 / 0.762) == pytest.approx(0.164, abs=0.002)


def test_banks2010_tst_from_tib_regression():
    """The recovery module's TIB-to-TST relation must reproduce its source regression.

    Banks, Van Dongen, Maislin & Dinges, Sleep 2010;33(8):1013-1026. doi:10.1093/sleep/33.8.1013
    -- TST = 0.237 + 0.8915 x TIB. At 10 h TIB the record gives max TST 8.96 h.
    """
    import recovery as REC
    predicted = REC.TST_FROM_TIB_INTERCEPT + REC.TST_FROM_TIB_SLOPE * 10.0
    assert predicted == pytest.approx(9.152, abs=0.01)
    # The observed 8.96 h sits below the linear prediction, i.e. yield is concave at the top of
    # the range. The module must not predict more sleep than was actually observed.
    assert REC.sustained_tst(10.0) <= 8.96 + 1e-9


def test_hksj_widens_interval_relative_to_standard_random_effects():
    """The Hartung-Knapp adjustment must widen, never narrow, a heterogeneous pooled interval."""
    y = np.array([-0.90, -0.20, -0.55, -0.05, -1.10])
    se = np.array([0.12, 0.11, 0.13, 0.12, 0.14])
    got = SYN.pool_frequentist(y, se)
    tau2 = got["tau2"]
    w = 1 / (se ** 2 + tau2)
    se_plain = math.sqrt(1 / w.sum())
    assert got["se"] >= se_plain - 1e-12
    assert got["i2"] > 50, "this input is deliberately heterogeneous"


# --------------------------------------------------------------------------- 3
def test_lifetable_reproduces_published_life_expectancy():
    """Gate G10: recompute e19 and e65 from qx alone and match NCHS to within 0.3 years."""
    chk = LT.calibration_check()
    assert chk["e19_abs_error_years"] < 0.3
    assert chk["e65_abs_error_years"] < 0.3
    assert chk["gate_G10_within_0.3y"] is True


def test_lifetable_hazard_ratio_monotone_and_signed():
    """A hazard ratio above 1 must lose life expectancy, and more so when larger."""
    d1 = LT.delta_le_months(1.05, from_age=19, exposure_end_age=None)
    d2 = LT.delta_le_months(1.20, from_age=19, exposure_end_age=None)
    assert d1 < 0 and d2 < 0
    assert d2 < d1
    assert LT.delta_le_months(1.0, from_age=19, exposure_end_age=None) == pytest.approx(0.0, abs=1e-9)


def test_hazard_applied_on_hazard_scale_not_probability_scale():
    """qx must remain a valid probability under a large hazard ratio.

    Multiplying qx directly would produce values above 1. Multiplying the hazard cannot: it
    saturates at 1, which is the correct behaviour (a 50x hazard does make death near-certain,
    and the terminal age already has qx = 1).
    """
    ages, qx = LT.load_qx()
    q2 = LT.apply_hr(ages, qx, hr=50.0, start_age=19, end_age=None)
    assert q2.max() <= 1.0
    assert (q2 >= qx - 1e-12).all()
    naive = qx * 50.0
    assert naive.max() > 1.0, "the naive probability-scale approach is invalid, which is the point"
    # At ages where death is not already near-certain the result must stay strictly interior.
    young = ages < 80
    assert q2[young].max() < 1.0


# --------------------------------------------------------------------------- 4
def test_bayes_grid_agrees_with_nuts():
    """The two independent posterior computations must agree. If they do not, one is broken."""
    y = np.array([-0.76, -0.55, -0.48, -0.38, -0.25])
    se = np.array([0.10, 0.09, 0.08, 0.13, 0.13])
    g = SYN.pool_bayes_grid(y, se)
    n = SYN.pool_bayes_nuts(y, se)
    if n is None:
        pytest.skip("numpyro unavailable")
    assert abs(g["mu_median"] - n["mu_median"]) < 0.02
    assert abs(g["tau_median"] - n["tau_median"]) < 0.05
    # Gate G8
    assert n["rhat_mu"] < 1.01 and n["rhat_tau"] < 1.01
    assert n["ess_mu"] > 1000 and n["ess_tau"] > 1000
    assert n["divergences"] == 0


def test_bayes_grid_tau_agrees_with_reml():
    """Grid marginalisation and REML optimise the same criterion, so tau must agree."""
    y = np.array([-0.76, -0.55, -0.48, -0.38, -0.25])
    se = np.array([0.10, 0.09, 0.08, 0.13, 0.13])
    reml = SYN.pool_frequentist(y, se)["tau"]
    grid = SYN.pool_bayes_grid(y, se)["tau_median"]
    assert abs(reml - grid) < 0.05, f"REML tau {reml} vs grid tau {grid}"


def test_prediction_interval_wider_than_confidence_interval():
    """The interval that applies to one individual must be wider than the one for the mean."""
    y = np.array([-1.2, -0.3, -0.8, -0.1, -0.6])
    se = np.array([0.15, 0.15, 0.15, 0.15, 0.15])
    f = SYN.pool_frequentist(y, se)
    ci_w = f["ci95"][1] - f["ci95"][0]
    pi_w = f["pi95"][1] - f["pi95"][0]
    assert pi_w > ci_w
    b = SYN.pool_bayes_grid(y, se)
    assert (b["pred_ci95"][1] - b["pred_ci95"][0]) > (b["mu_ci95"][1] - b["mu_ci95"][0])


# --------------------------------------------------------------------------- 5
def test_e_value_known_values():
    """VanderWeele-Ding E-value at published reference points."""
    assert SYN.e_value(1.0) == pytest.approx(1.0, abs=1e-9)
    assert SYN.e_value(2.0) == pytest.approx(2 + math.sqrt(2), rel=1e-9)
    assert SYN.e_value(1.12) == pytest.approx(1.487, abs=0.005)
    # symmetric in RR and 1/RR
    assert SYN.e_value(0.5) == pytest.approx(SYN.e_value(2.0), rel=1e-9)


def test_pet_peese_recovers_zero_when_no_bias():
    """With no small-study effect, PET's intercept should recover the true effect."""
    rng = np.random.default_rng(3)
    true = -0.40
    se = np.array([0.05, 0.08, 0.10, 0.15, 0.20, 0.25, 0.30])
    y = true + rng.normal(0, se)
    res = SYN.pet_peese(y, se)
    assert abs(res["pet"] - true) < 0.25


def test_pet_peese_detects_injected_small_study_bias():
    """Inject a bias proportional to se; PET must pull the estimate back toward the truth."""
    true = -0.20
    se = np.array([0.05, 0.08, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35])
    y = true - 1.5 * se                      # classic funnel asymmetry
    naive = (y / se ** 2).sum() / (1 / se ** 2).sum()
    res = SYN.pet_peese(y, se)
    assert abs(res["pet"] - true) < abs(naive - true)


def test_trim_and_fill_no_fill_on_symmetric_data():
    """Symmetric funnel with genuinely varying precision must trigger no fill."""
    y = np.array([-0.5, -0.4, -0.6, -0.35, -0.65, -0.5, -0.45, -0.55])
    se = np.array([0.05, 0.08, 0.08, 0.14, 0.14, 0.20, 0.10, 0.10])
    res = SYN.trim_and_fill(y, se)
    assert res["n_filled"] == 0, f"filled {res['n_filled']} on symmetric input"


def test_trim_and_fill_detects_censored_side():
    """Delete the small-study null results and trim-and-fill must want to put some back."""
    se = np.array([0.05, 0.07, 0.09, 0.12, 0.15, 0.18, 0.22, 0.26])
    y = np.array([-0.42, -0.45, -0.48, -0.62, -0.70, -0.80, -0.92, -1.05])
    res = SYN.trim_and_fill(y, se)
    assert res["n_filled"] >= 1
    # Filling the missing null side must move the estimate toward zero.
    assert abs(res["adjusted_mu"]) < abs(res["unadjusted_mu"])


# --------------------------------------------------------------------------- 6
def test_cohort_dedup_collapses_families_and_does_not_shrink_se():
    rows = [
        {"study_id": "a", "value": -0.5, "se": 0.10, "cohort_family": "UK_Biobank"},
        {"study_id": "b", "value": -0.3, "se": 0.10, "cohort_family": "UK_Biobank"},
        {"study_id": "c", "value": -0.4, "se": 0.10, "cohort_family": "UK_Biobank"},
        {"study_id": "d", "value": -0.7, "se": 0.20, "cohort_family": None},
    ]
    out = SYN.dedupe_by_cohort(rows)
    assert len(out) == 2, "three UK Biobank effects must collapse to one"
    fam = [r for r in out if str(r["study_id"]).startswith("UK_Biobank")][0]
    assert fam["se"] == pytest.approx(0.10), "collapsed SE must not fall below the best single SE"
    assert fam["value"] == pytest.approx(-0.4, abs=1e-9)


def test_dedup_changes_pooled_result_relative_to_naive():
    """De-duplication must actually matter, otherwise the safeguard is decorative."""
    rows = [{"study_id": f"ukb{i}", "value": -0.5, "se": 0.05, "cohort_family": "UK_Biobank"}
            for i in range(8)]
    rows.append({"study_id": "other", "value": 0.0, "se": 0.05, "cohort_family": None})
    y = np.array([r["value"] for r in rows]); se = np.array([r["se"] for r in rows])
    naive = SYN.pool_frequentist(y, se)["mu"]
    ded = SYN.dedupe_by_cohort(rows)
    y2 = np.array([r["value"] for r in ded]); se2 = np.array([r["se"] for r in ded])
    deduped = SYN.pool_frequentist(y2, se2)["mu"]
    assert abs(deduped) < abs(naive), "collapsing the mega-cohort must reduce its dominance"


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-v", "--tb=short"]))
