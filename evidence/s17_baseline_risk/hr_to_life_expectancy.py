"""Conversion machinery: hazard ratio -> change in life expectancy; lifetime risk with
competing mortality.

Reads /workspace/data/lifetable_us_male_full.csv (built by build_lifetable.py from
NCHS United States Life Tables 2023, Table 2, males, spliced with the SSA 2023 tail).

Three public functions, all documented in competing_risk_method.md:

  delta_ex(hr, age_from, age_to, index_age, cause_fraction)
      Hazard-modified life table. Returns the change in expectation of life at
      index_age when the all-cause (or cause-specific) mortality hazard is
      multiplied by `hr` over [age_from, age_to).

  lifetime_risk(incidence, index_age, cause_deleted_mortality)
      Discrete Aalen-Johansen / cumulative-incidence-function lifetime risk with
      death as a competing event.

  naive_vs_correct(...)  demonstrates the three errors the model must not make.

Run with no arguments to print the worked examples quoted in competing_risk_method.md.
"""

from __future__ import annotations

import csv
import math
from pathlib import Path

FULL = Path("/workspace/data/lifetable_us_male_full.csv")
OMEGA = 120  # last age in the table; qx == 1 there


def load_qx(path: Path = FULL) -> dict[int, float]:
    with path.open() as fh:
        rows = csv.DictReader([l for l in fh if not l.startswith("#")])
        return {int(r["age"]): float(r["qx"]) for r in rows}


def qx_to_hazard(q: float) -> float:
    """Piecewise-constant (exponential) hazard implied by a one-year probability."""
    return -math.log(1.0 - q) if q < 1.0 else float("inf")


def hazard_to_qx(mu: float) -> float:
    return 1.0 - math.exp(-mu) if math.isfinite(mu) else 1.0


def ex_from_qx(qx: dict[int, float], index_age: int) -> float:
    """Expectation of life at index_age, a(x)=0.5 within each year of age."""
    lx, T = 1.0, 0.0
    for age in range(index_age, OMEGA + 1):
        q = min(qx.get(age, 1.0), 1.0)
        d = lx * q
        T += lx - 0.5 * d
        lx -= d
        if lx <= 0:
            break
    return T


def apply_hr(qx: dict[int, float], hr: float, age_from: int, age_to: int,
             cause_fraction: float = 1.0) -> dict[int, float]:
    """Multiply the mortality HAZARD (not qx, not the death count) by hr on [age_from, age_to).

    cause_fraction < 1 makes the HR cause-specific: only that share of the age-specific
    hazard is scaled, which is the cause-modified life table of Beltran-Sanchez (2008).
    """
    out = dict(qx)
    for age in range(age_from, min(age_to, OMEGA + 1)):
        if age not in out or out[age] >= 1.0:
            continue
        mu = qx_to_hazard(out[age])
        mu_new = mu * (1.0 + cause_fraction * (hr - 1.0))
        out[age] = hazard_to_qx(mu_new)
    return out


def delta_ex(hr: float, age_from: int, age_to: int, index_age: int = 19,
             cause_fraction: float = 1.0, qx: dict[int, float] | None = None) -> float:
    """Change in expectation of life at index_age, in YEARS (negative = life lost)."""
    qx = qx or load_qx()
    return ex_from_qx(apply_hr(qx, hr, age_from, age_to, cause_fraction), index_age) \
        - ex_from_qx(qx, index_age)


def lifetime_risk(incidence: dict[int, float], index_age: int,
                  qx: dict[int, float] | None = None,
                  horizon: int = OMEGA) -> dict[str, float]:
    """Lifetime risk of a non-fatal event from index_age, death as a competing event.

    incidence[age] = probability that a person alive and event-free at exact age x
                     has a first event during [x, x+1).
    Returns the competing-risk-adjusted lifetime risk (the cumulative incidence
    function, CIF) and, for contrast, the naive 1 - Kaplan-Meier estimate that
    ignores competing mortality.
    """
    qx = qx or load_qx()
    alive_free = 1.0   # P(alive and event-free at exact age x)
    cif = 0.0          # competing-risk-adjusted lifetime risk
    km_surv = 1.0      # censoring-at-death KM survival, i.e. mortality ignored
    for age in range(index_age, horizon + 1):
        i = incidence.get(age, 0.0)
        m = min(qx.get(age, 1.0), 1.0)
        # events and other-cause deaths compete inside the interval; split the
        # interval evenly (actuarial correction) so neither is double-counted
        cif += alive_free * i * (1.0 - 0.5 * m)
        alive_free *= (1.0 - i) * (1.0 - m)
        km_surv *= (1.0 - i)
        if alive_free <= 1e-12:
            break
    return {"lifetime_risk_competing_adjusted": cif,
            "one_minus_km_ignoring_mortality": 1.0 - km_surv,
            "inflation_factor_if_mortality_ignored": (1.0 - km_surv) / cif if cif else float("nan")}


def cif_under_hr(baseline_cif: float, hr: float) -> dict[str, float]:
    """Correct vs naive way to move an absolute risk with a hazard ratio.

    Under proportional hazards with constant ratio hr, S1 = S0 ** hr, so
        CIF1 = 1 - (1 - CIF0) ** hr
    Naive multiplication (CIF0 * hr) is an upper bound that diverges badly once
    CIF0 is large; it can even exceed 1.
    """
    correct = 1.0 - (1.0 - baseline_cif) ** hr
    naive = baseline_cif * hr
    return {"baseline": baseline_cif, "correct_ph": correct, "naive_multiply": naive,
            "naive_minus_correct_pp": 100.0 * (naive - correct),
            "naive_overstatement_ratio": (naive - baseline_cif) / (correct - baseline_cif)
            if correct > baseline_cif else float("nan")}


def main() -> None:
    qx = load_qx()
    e19 = ex_from_qx(qx, 19)
    e0 = ex_from_qx(qx, 0)
    print(f"# baseline (NCHS 2023 males): e0 = {e0:.4f} y, e19 = {e19:.4f} y "
          f"({e19 * 12:.1f} months)\n")

    print("## A. Hazard ratio applied to ALL-CAUSE mortality, from age 19 to death")
    for hr in (1.05, 1.07, 1.10, 1.12, 1.13, 1.20, 1.30):
        d = delta_ex(hr, 19, OMEGA + 1, 19, qx=qx)
        print(f"   HR={hr:<5} lifelong from 19:  d_e19 = {d:+.3f} y = {d * 12:+.1f} months")

    print("\n## B. Same HR applied ONLY during the 3-year exposure window (ages 19-22)")
    for hr in (1.13, 1.50, 2.00, 3.00):
        d = delta_ex(hr, 19, 22, 19, qx=qx)
        print(f"   HR={hr:<5} ages 19-21 only:   d_e19 = {d:+.5f} y = {d * 12:+.4f} months")

    print("\n## C. Effect confined to later windows (a mediator that only bites in midlife)")
    for lo, hi in ((19, 40), (40, 65), (65, OMEGA + 1), (50, OMEGA + 1)):
        d = delta_ex(1.13, lo, hi, 19, qx=qx)
        print(f"   HR=1.13 on ages {lo}-{hi if hi <= OMEGA else 'omega'}: "
              f"d_e19 = {d:+.3f} y = {d * 12:+.1f} months")

    print("\n## D. Cause-specific HR: HR=1.5 but only on the CVD share of the hazard")
    for f in (1.0, 0.30, 0.20, 0.10):
        d = delta_ex(1.5, 19, OMEGA + 1, 19, cause_fraction=f, qx=qx)
        print(f"   HR=1.5, cause_fraction={f:<5} lifelong: d_e19 = {d:+.3f} y = {d * 12:+.1f} months")

    print("\n## E. WHY YOU MAY NOT MULTIPLY AN HR BY A LIFETIME RISK")
    for base, hr in ((0.402, 1.20), (0.402, 1.37), (0.517, 1.20), (0.90, 1.20),
                     (0.138, 1.20), (0.201, 1.20)):
        r = cif_under_hr(base, hr)
        print(f"   baseline {base:.3f}, HR {hr:.2f} -> correct {r['correct_ph']:.3f}"
              f" vs naive {r['naive_multiply']:.3f}"
              f"  (naive overstates the INCREMENT by {r['naive_overstatement_ratio']:.2f}x)")

    print("\n## F. Lifetime risk with vs without competing mortality")
    # dementia-like schedule: zero before 65, then doubling roughly every 6 years
    inc = {age: (0.0 if age < 65 else min(0.003 * 2 ** ((age - 65) / 6.0), 0.15))
           for age in range(19, OMEGA + 1)}
    r = lifetime_risk(inc, 19, qx=qx)
    print(f"   competing-risk adjusted lifetime risk from 19: {r['lifetime_risk_competing_adjusted']:.3f}")
    print(f"   1 - Kaplan-Meier, mortality ignored:           {r['one_minus_km_ignoring_mortality']:.3f}")
    print(f"   inflation factor if mortality ignored:         "
          f"{r['inflation_factor_if_mortality_ignored']:.2f}x")
    print("   Published anchors for the same bias, same cohort, same men:")
    print("     Chene 2015 FHS men, dementia from age 45:  13.8% competing-risk adjusted")
    print("                                       vs      61.0% NOT adjusted  (4.42x)")
    print("     Seshadri 1997 FHS men, dementia from 65:   10.9% remaining lifetime risk")
    print("                                       vs      32.8% cumulative incidence to 100 (3.01x)")

    print("\n## G. Cross-check against published sleep life-expectancy estimates")
    print("   Chaput 2022 (Canada, life-table + meta-analytic RR): meeting sleep")
    print("     recommendations vs SHORT sleep = +1.2 y of life expectancy at age 20.")
    for hr in (1.10, 1.12, 1.13, 1.15):
        d = delta_ex(hr, 20, OMEGA + 1, 20, qx=qx)
        print(f"     our machinery, all-cause HR={hr} lifelong from 20 -> {d:+.2f} y at age 20")
    print("   => a lifelong all-cause mortality HR of about 1.10-1.13 reproduces the")
    print("      published 1.2-year figure, which is a consistency check on both.")
    print("   Four published anchors, ordered by how much non-sleep lifestyle each absorbs:")
    print("     Chaput 2022  +1.20 y  at 20  sleep DURATION alone, meta-analytic RR")
    print("     Huang 2023   -2.31 y  at 40  5-item sleep composite, CVD-FREE years, men")
    print("     Li 2024      -4.70 y  at 30  5-factor sleep composite, men")
    print("     Ma 2023      +5.00 y  at 50  1 of 8 CVH components, NOT mutually adjusted")
    print("   Ma's own arithmetic bounds itself: tobacco alone 7.4 y + sleep alone 5.0 y")
    print("     = 12.4 y > the ENTIRE high-vs-low LE8 contrast of 8.9 y, so the component")
    print("     contrasts overlap heavily and 5.0 y is a ceiling, not a sleep effect.")
    print("     Equal-share allocation of Ma's MALE total (8.1 y / 8 components) = 1.01 y,")
    print("     which lands on Chaput's 1.2 y and on the HR range just printed.")
    print("     (The equal-share number is OUR arithmetic, not published by Ma et al.)")
    print("   => recommended prior for the pure mortality channel of a LIFELONG habit:")
    print("      1.0-1.5 y of e19. For the subject's actual 3-year window see panel B,")
    print("      where the same HR costs about 0.3 months, i.e. ~58x less.")


if __name__ == "__main__":
    main()
