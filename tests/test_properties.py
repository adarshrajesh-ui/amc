"""S8 property, unit and invariant tests (Gate G11).

These assert things that must be true regardless of the numbers: dimensional consistency,
monotonicity, sign conventions, and that the safeguards actually bind.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np
import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

import analysis_set as ASET  # noqa: E402
import exposure as EXP  # noqa: E402
import lifetable as LT  # noqa: E402
import recovery as REC  # noqa: E402

N = 6_000


# ------------------------------------------------------------------ exposure engine
def test_more_reported_sleep_means_less_debt():
    """Monotonicity: raising every reported value must lower the debt."""
    base = EXP.simulate(n_draws=N, seed=1)
    orig = [(e.weekday_report_h, e.weekend_report_h) for e in EXP.EPOCHS]
    try:
        for e in EXP.EPOCHS:
            e.weekday_report_h += 1.0
            e.weekend_report_h += 1.0
        more = EXP.simulate(n_draws=N, seed=1)
    finally:
        for e, (wd, we) in zip(EXP.EPOCHS, orig):
            e.weekday_report_h, e.weekend_report_h = wd, we
    a = np.median(base["draws"]["cumulative_debt_vs_individual_need_h"])
    b = np.median(more["draws"]["cumulative_debt_vs_individual_need_h"])
    assert b < a, "sleeping more must reduce debt"


def test_debt_units_are_hours_and_reconcile_with_nightly_deficit():
    """Dimensional check: total hours must equal mean nightly deficit times nights."""
    res = EXP.simulate(n_draws=N, seed=2)
    d = res["draws"]
    n_nights = res["n_nights_exposure_from_16"]
    implied = d["mean_nightly_deficit_exposure_h"] * n_nights
    actual = d["cumulative_debt_vs_individual_need_h"]
    assert np.allclose(implied, actual, rtol=1e-6), "debt is not deficit x nights"


def test_exposure_window_night_count_matches_calendar():
    res = EXP.simulate(n_draws=200, seed=3)
    expected = int(round((EXP.AGE_NOW - 16.0) * EXP.DAYS_PER_YEAR))
    assert abs(res["n_nights_exposure_from_16"] - expected) <= 2


def test_individual_need_is_a_person_level_trait_not_per_night():
    """Need must be drawn once per person. If it were redrawn nightly its variance would
    average away and the debt interval would collapse."""
    res = EXP.simulate(n_draws=20_000, seed=4)
    need_sd = float(np.std(res["draws"]["individual_need_at_19_h"]))
    assert need_sd == pytest.approx(EXP.PRIORS["need_sd_individual_h"], rel=0.15)
    debt_sd = float(np.std(res["draws"]["cumulative_debt_vs_individual_need_h"]))
    n_nights = res["n_nights_exposure_from_16"]
    # A person-level need SD of 0.70 h propagates to ~0.70 * n_nights of debt SD, which is
    # enormous. If need were redrawn per night the debt SD would be ~sqrt(n) times smaller.
    assert debt_sd > 0.4 * EXP.PRIORS["need_sd_individual_h"] * n_nights


def test_calibration_branches_are_mutually_exclusive_no_double_discount():
    """The TIB and TST corrections must never compound."""
    tst = EXP.simulate(n_draws=N, seed=5, tib_scenario="tst", calibration="naive")
    tib = EXP.simulate(n_draws=N, seed=5, tib_scenario="tib", calibration="naive")
    m_tst = float(np.median(tst["draws"]["mean_tst_exposure_h"]))
    m_tib = float(np.median(tib["draws"]["mean_tst_exposure_h"]))
    # Under a compounding bug the TIB branch would be about an hour below the TST branch on
    # top of the efficiency multiplication, driving sleep implausibly low.
    assert m_tib > 3.5, f"TIB branch collapsed to {m_tib} h, suggesting a double discount"
    assert abs(m_tst - m_tib) < 1.5


def test_face_value_calibration_gives_least_debt():
    """Taking reports at face value must be the most optimistic branch."""
    none_ = EXP.simulate(n_draws=N, seed=6, tib_scenario="tst", calibration="none")
    naive = EXP.simulate(n_draws=N, seed=6, tib_scenario="tst", calibration="naive")
    assert (np.median(none_["draws"]["cumulative_debt_vs_individual_need_h"])
            < np.median(naive["draws"]["cumulative_debt_vs_individual_need_h"]))


def test_envelope_and_simulation_agree_within_gate():
    env = EXP.envelope()
    sim = EXP.simulate(n_draws=40_000, seed=7)
    med = float(np.median(sim["draws"]["cumulative_debt_vs_individual_need_h"]))
    assert abs(med - env["total_debt_h"]) / env["total_debt_h"] <= 0.20


def test_incremental_debt_is_smaller_than_total_debt():
    """The change at 16 cannot explain more debt than exists in total."""
    inc = EXP.incremental_debt(n_draws=40_000, seed=8)
    assert (inc["incremental_debt_attributable_to_change_at_16_h"]["median"]
            < inc["debt_vs_guideline_need_h"]["median"])
    assert inc["incremental_debt_attributable_to_change_at_16_h"]["median"] > 0


# ------------------------------------------------------------------ recovery
def test_sleep_never_exceeds_opportunity():
    for tib in np.linspace(1, 16, 40):
        assert REC.tst_from_opportunity(tib) <= tib + 1e-9


def test_more_opportunity_never_yields_less_sleep():
    tib = np.linspace(2, 14, 60)
    tst = np.array([REC.sustained_tst(float(t)) for t in tib])
    assert np.all(np.diff(tst) >= -1e-9)


def test_sustained_sleep_respects_ad_lib_asymptote():
    """No policy may predict sustained sleep above the observed ad-lib asymptote."""
    for tib in (9, 10, 12, 16):
        assert REC.sustained_tst(float(tib)) <= REC.CEILING_SUSTAINED_H + 1e-9


def test_recovery_is_monotone_and_bounded_by_residual():
    start = np.full(500, 1.0)
    tau = np.full(500, 14.0)
    resid = np.full(500, 0.10)
    weeks = np.array([0, 1, 2, 4, 8, 26, 52])
    traj = REC.recovery_trajectory(start, tau, resid, weeks, np.full(500, +0.5))
    med = np.median(traj, axis=1)
    assert np.all(np.diff(med) <= 1e-9), "impairment must not increase under a surplus policy"
    assert med[-1] >= 0.10 - 1e-6, "cannot recover past the residual floor"
    assert med[0] == pytest.approx(1.0, rel=1e-6)


def test_policy_still_short_of_need_does_not_fully_recover():
    """A policy that keeps under-sleeping must not be projected to reach full recovery."""
    start = np.full(500, 1.0)
    traj = REC.recovery_trajectory(start, np.full(500, 14.0), np.full(500, 0.0),
                                   np.array([52.0]), np.full(500, -2.0))
    assert float(np.median(traj)) > 0.3, "an under-sleeping policy cannot recover the deficit"


def test_weekend_catchup_is_arithmetically_insufficient():
    r = REC.weekend_catchup_arithmetic(3.0, REC.CEILING_SINGLE_NIGHT_H, 8.7)
    assert r["physiologically_possible"] is False
    assert r["fraction_repayable"] < 0.5


def test_maintenance_tib_exceeds_the_sleep_target():
    """Because efficiency is below 1, required time in bed must exceed the sleep need."""
    for need in (7.5, 8.0, 8.7, 9.0):
        tib = (need - REC.TST_FROM_TIB_INTERCEPT) / REC.TST_FROM_TIB_SLOPE
        assert tib > need


# ------------------------------------------------------------------ life table
def test_life_expectancy_decreases_with_age():
    ages, qx = LT.load_qx()
    es = [LT.life_expectancy(ages, qx, a) for a in (19, 30, 45, 65, 80)]
    assert all(es[i] > es[i + 1] for i in range(len(es) - 1))


def test_qx_is_a_valid_probability_series():
    ages, qx = LT.load_qx()
    assert (qx >= 0).all() and (qx <= 1).all()
    assert len(ages) == len(set(ages.tolist())), "duplicate ages in the life table"
    assert np.all(np.diff(ages) == 1), "life table must be contiguous by single year of age"


def test_hazard_ratio_of_one_is_a_no_op():
    ages, qx = LT.load_qx()
    assert np.allclose(LT.apply_hr(ages, qx, 1.0, 19, None), qx, atol=1e-12)


def test_window_limited_hazard_costs_far_less_than_permanent():
    """The distinction that dominates the long-run answers must actually be large."""
    perm = abs(LT.delta_le_months(1.12, from_age=19, exposure_end_age=None))
    short = abs(LT.delta_le_months(1.12, from_age=19, exposure_end_age=22.0))
    assert perm > 10 * short


# ------------------------------------------------------------------ analysis set
def test_analysis_set_resolves_and_signs_are_canonical():
    """Every harm effect in the curated set must be negative after canonicalisation."""
    aset = ASET.resolve()
    harm_params = ["pvt_g_large_dose", "domain_profile_chronic_restriction",
                   "habitual_short_sleep_g_observational",
                   "residual_deficit_after_recovery_sleep", "encoding_capacity_persisting"]
    for name in harm_params:
        for e in aset[name]["effects"]:
            assert e["value"] < 0, f"{name}/{e['study_id']} has non-canonical sign {e['value']}"


def test_analysis_set_fails_loudly_on_missing_evidence():
    """A typo in a selector must raise, never silently fall back to a default."""
    original = dict(ASET.ANALYSIS_SET["encoding_capacity_persisting"])
    try:
        ASET.ANALYSIS_SET["encoding_capacity_persisting"] = {
            **original, "selectors": [("no_such_study", "no_such_construct", False)]}
        with pytest.raises(RuntimeError, match="absent from the corpus"):
            ASET.resolve()
    finally:
        ASET.ANALYSIS_SET["encoding_capacity_persisting"] = original


def test_duplicate_records_inflate_rather_than_hide_disagreement():
    """Where two shards disagree under one construct label, the SE must reflect the spread."""
    aset = ASET.resolve()
    found = False
    for spec in aset.values():
        for e in spec["effects"]:
            if e.get("duplicate_values"):
                vals = e["duplicate_values"]
                spread = max(vals) - min(vals)
                if spread > 0:
                    assert e["se"] >= spread / 2 - 1e-9
                    found = True
    assert found, "expected at least one duplicated construct in the corpus"


def test_fsiq_anchor_bounds_the_iq_claim():
    """The direct FSIQ measurement must be present and must not itself indicate a large loss."""
    aset = ASET.resolve()
    e = aset["fsiq_direct_measurement"]["effects"][0]
    lower = e["value"] - 1.96 * e["se"]
    assert lower > -3.0, ("the direct WAIS-R measurement must bound the decrement; "
                          f"lower bound was {lower}")


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-v", "--tb=short"]))
