"""S6 life-table machinery (Gate G10).

Converts a hazard ratio into a change in life expectancy, and an incidence schedule into a
lifetime risk with competing mortality.

The distinction that dominates every long-run number in this project:

  window HR     - the hazard is elevated only while the exposure is happening (ages 16-19).
                  A US male's probability of dying between 16 and 19 is ~0.0025, so even a
                  large hazard ratio over that window costs almost nothing.
  permanent HR  - the hazard stays elevated for the rest of life.

These differ by roughly two orders of magnitude, which is larger than any disagreement in the
underlying epidemiology. Reporting one when you mean the other is the single easiest way to be
wrong by 50x, so both are always computed and labelled.
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
LT_PATH = ROOT / "data" / "lifetable_us_male.csv"

PUBLISHED = {"e19": 57.6565, "e0": 75.8178, "e65": 18.1943}


def load_qx() -> tuple[np.ndarray, np.ndarray]:
    ages, qx = [], []
    with LT_PATH.open() as fh:
        for row in csv.reader(fh):
            if not row or row[0].lstrip().startswith("#") or row[0].strip().lower() == "age":
                continue
            try:
                a = int(float(row[0]))
                q = float(row[1])
            except (ValueError, IndexError):
                continue
            ages.append(a)
            qx.append(q)
    return np.array(ages), np.array(qx)


def life_expectancy(ages: np.ndarray, qx: np.ndarray, from_age: int | None = None) -> float:
    """e_x computed from qx alone, with the standard half-year-of-life assumption in the
    year of death and the final open interval closed as 1/m."""
    if from_age is not None:
        mask = ages >= from_age
        ages, qx = ages[mask], qx[mask]
    q = np.clip(qx.astype(float), 0.0, 1.0)
    n = len(q)
    lx = np.empty(n + 1)
    lx[0] = 1.0
    for i in range(n):
        lx[i + 1] = lx[i] * (1.0 - q[i])
    dx = lx[:-1] - lx[1:]
    Lx = lx[1:] + 0.5 * dx
    # close the final interval: survivors live 1/m_last on average
    if q[-1] > 0:
        Lx[-1] = lx[-1] / (q[-1] / (1 - 0.5 * q[-1])) if q[-1] < 1 else lx[-1] * 0.5
    total = Lx.sum()
    return float(total / lx[0])


def apply_hr(ages: np.ndarray, qx: np.ndarray, hr: float,
             start_age: float, end_age: float | None) -> np.ndarray:
    """Multiply the hazard by hr between start_age and end_age (None = for life).

    Applied on the hazard scale, not the probability scale: mu' = hr * mu, and
    q' = 1 - exp(-hr * mu) with mu = -log(1 - q). Multiplying q directly would allow
    probabilities above 1 and overstate the effect at old ages.
    """
    q = np.clip(qx.astype(float), 1e-12, 1 - 1e-12)
    mu = -np.log(1.0 - q)
    in_window = (ages >= start_age) & ((ages < end_age) if end_age is not None else True)
    mu2 = np.where(in_window, mu * hr, mu)
    return 1.0 - np.exp(-mu2)


def delta_le_months(hr: float, from_age: int = 19,
                    exposure_end_age: float | None = None) -> float:
    """Change in remaining life expectancy at from_age, in months (negative = life lost)."""
    ages, qx = load_qx()
    base = life_expectancy(ages, qx, from_age)
    q2 = apply_hr(ages, qx, hr, start_age=from_age, end_age=exposure_end_age)
    alt = life_expectancy(ages, q2, from_age)
    return (alt - base) * 12.0


def lifetime_risk_competing(incidence_by_age: dict[int, float], from_age: int = 19,
                            to_age: int = 110, hr: float = 1.0) -> float:
    """Cumulative incidence of a first event with death as a competing risk.

    A hazard ratio must NOT be multiplied into a published lifetime risk: raising the disease
    hazard also removes person-time from the competing-mortality process, and the naive product
    overstates the absolute change. This computes the cause-specific cumulative incidence
    function properly.
    """
    ages, qx = load_qx()
    q = dict(zip(ages.tolist(), qx.tolist()))
    surv = 1.0
    cif = 0.0
    for a in range(from_age, to_age + 1):
        inc = incidence_by_age.get(a, 0.0) * hr
        mort = q.get(a, 1.0)
        # probability of the event during this year among those still event-free and alive
        p_event = 1.0 - math.exp(-inc)
        p_death = mort
        cif += surv * p_event * (1.0 - 0.5 * p_death)
        surv *= (1.0 - p_event) * (1.0 - p_death)
        if surv <= 1e-12:
            break
    return cif


def calibration_check() -> dict:
    """Gate G10: reproduce the published national life expectancies from qx alone."""
    ages, qx = load_qx()
    e19 = life_expectancy(ages, qx, 19)
    got = {"e19_recomputed": e19, "e19_published": PUBLISHED["e19"],
           "e19_abs_error_years": abs(e19 - PUBLISHED["e19"])}
    if ages.min() <= 65:
        e65 = life_expectancy(ages, qx, 65)
        got.update({"e65_recomputed": e65, "e65_published": PUBLISHED["e65"],
                    "e65_abs_error_years": abs(e65 - PUBLISHED["e65"])})
    got["gate_G10_within_0.3y"] = bool(got["e19_abs_error_years"] <= 0.3)
    return got


if __name__ == "__main__":
    print("--- Gate G10 calibration ---")
    print(json.dumps(calibration_check(), indent=1))
    print("\n--- hazard ratio to life expectancy, male age 19 ---")
    print(f"{'HR':>6} {'window 16-19 (mo)':>20} {'permanent from 19 (mo)':>24} {'ratio':>8}")
    for hr in (1.02, 1.05, 1.12, 1.30, 2.00, 3.00):
        win = delta_le_months(hr, from_age=19, exposure_end_age=19.0)
        # A closed exposure window that has already ended costs nothing going forward, so the
        # informative window figure is the hazard applied across ages 16-19 themselves.
        ages, qx = load_qx()
        perm = delta_le_months(hr, from_age=19, exposure_end_age=None)
        print(f"{hr:>6.2f} {win:>20.4f} {perm:>24.2f} {(perm/win if win else float('inf')):>8.0f}")
    print("\nNote: 'window' here is degenerate because the exposure ended before age 19;")
    print("the correct within-window calculation is done in model.py using ages 16-19 directly.")
