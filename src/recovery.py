"""S6 recovery dynamics.

An "hours owed" ledger is not a repayment schedule, and the difference matters enormously here.
The arithmetic debt runs to thousands of hours, but nightly sleep is bounded: an ad-lib sleeper
asymptotes around 8.5-8.9 h (klerman2008 gave subjects 16 h in bed and they settled at 8.9 h,
spending 7.1 h awake in bed), so the maximum nightly surplus over an ~8.7 h requirement is a
fraction of an hour. Taken literally the ledger would imply years of repayment.

What the experimental literature actually shows is that *function* recovers on a time constant of
days to weeks largely independent of how many ledger hours accumulated, while a residual
component has never been shown to close because no study has followed recovery long enough. So
two quantities are modelled separately:

  ledger   - hours, reported because it was asked for, and explicitly labelled as not a schedule
  function - a state variable with an accrual and a recovery time constant, which is what a
             recovery prescription can actually act on

Repayment yield is concave: banks2010 gives TST = 0.237 + 0.8915 x TIB, with the marginal yield
falling from 0.94 to 0.725 h of sleep per hour in bed across the 2-10 h ladder.
"""

from __future__ import annotations

import json

import numpy as np

# TST obtained from a given sleep opportunity (banks2010 regression, R^2 = 0.997).
TST_FROM_TIB_INTERCEPT = 0.237
TST_FROM_TIB_SLOPE = 0.8915
CEILING_SINGLE_NIGHT_H = 10.2
CEILING_SUSTAINED_H = 8.9      # klerman2008 asymptote, 95% CI 8.1-9.7
CEILING_NOCTURNAL_ONLY_H = 7.9  # the last hour must come from a daytime nap

# Recovery time constants, days.
TAU_DURATION_DAYS = (2.5, 5.0)      # kitamura2016 tau=2.52; klerman2008 ~5
TAU_FUNCTION_LOGNORM = (np.log(16.0), 0.55)   # >7 d and never observed to complete


def tst_from_opportunity(tib_h: np.ndarray | float, nap_h: float = 0.0) -> np.ndarray:
    """Actual sleep obtained from a nightly opportunity, with the empirical ceilings applied."""
    tib = np.asarray(tib_h, dtype=float)
    nocturnal = np.minimum(TST_FROM_TIB_INTERCEPT + TST_FROM_TIB_SLOPE * tib,
                           CEILING_NOCTURNAL_ONLY_H if nap_h > 0 else CEILING_SINGLE_NIGHT_H)
    return np.minimum(nocturnal + nap_h, CEILING_SINGLE_NIGHT_H + nap_h)


def sustained_tst(tib_h: float, nap_h: float = 0.0) -> float:
    """Sleep obtained per 24 h under a policy sustained for weeks, not one recovery night."""
    return float(min(tst_from_opportunity(tib_h, nap_h), CEILING_SUSTAINED_H + nap_h))


def recovery_trajectory(impairment_now: np.ndarray, tau_days: np.ndarray,
                        residual_fraction: np.ndarray, weeks: np.ndarray,
                        nightly_balance_h: np.ndarray) -> np.ndarray:
    """Impairment over time under a policy.

    impairment_now      current deficit on whatever scale the caller is using
    tau_days            recovery time constant
    residual_fraction   the share that does not recover (posterior, wide)
    nightly_balance_h   sleep obtained minus individual need under the policy. If negative the
                        policy is still accruing deficit and function does not return to zero;
                        it relaxes toward a new, worse steady state instead.

    Returns an array of shape (n_weeks, n_draws).
    """
    t_days = np.asarray(weeks, float)[:, None] * 7.0
    # Steady state under the policy. A policy that still under-sleeps has a non-zero floor,
    # scaled by how far short it falls relative to the original deficit.
    shortfall = np.maximum(-nightly_balance_h, 0.0)
    orig_deficit = np.maximum(impairment_now, 1e-9)
    floor_from_policy = impairment_now * np.clip(shortfall / np.maximum(shortfall + 1.0, 1e-9), 0, 1)
    floor = np.maximum(residual_fraction * impairment_now, floor_from_policy)
    return floor + (impairment_now - floor) * np.exp(-t_days / tau_days)


def policies() -> dict:
    """The candidate prescriptions the report has to compare."""
    return {
        "status_quo_5.5h_weekday": {"tib_weekday": 5.5, "tib_weekend": 7.5, "nap": 0.0},
        "7h_every_night": {"tib_weekday": 7.0, "tib_weekend": 7.0, "nap": 0.0},
        "8h_every_night": {"tib_weekday": 8.0, "tib_weekend": 8.0, "nap": 0.0},
        "9h_every_night": {"tib_weekday": 9.0, "tib_weekend": 9.0, "nap": 0.0},
        "8h_plus_scheduled_nap": {"tib_weekday": 8.0, "tib_weekend": 8.0, "nap": 0.5},
        "weekday_5.5h_weekend_10h_catchup": {"tib_weekday": 5.5, "tib_weekend": 10.0, "nap": 0.0},
    }


def policy_weekly_balance(policy: dict, need_h: np.ndarray) -> np.ndarray:
    """Mean nightly (sleep - need) under a policy, averaged over a 7-day week."""
    wd = sustained_tst(policy["tib_weekday"], policy["nap"])
    we = sustained_tst(policy["tib_weekend"], policy["nap"])
    mean_tst = (5 * wd + 2 * we) / 7.0
    return mean_tst - np.asarray(need_h, float)


def weekend_catchup_arithmetic(weekday_deficit_h: float, weekend_ceiling_h: float,
                               need_h: float) -> dict:
    """Can weekend sleep alone repay the weekday deficit? Compute the required ceiling."""
    weekly_deficit = 5 * weekday_deficit_h
    max_weekend_surplus = 2 * max(weekend_ceiling_h - need_h, 0.0)
    required_per_weekend_night = need_h + weekly_deficit / 2.0
    return {
        "weekly_weekday_deficit_h": weekly_deficit,
        "max_available_weekend_surplus_h": max_weekend_surplus,
        "fraction_repayable": (max_weekend_surplus / weekly_deficit) if weekly_deficit > 0 else None,
        "required_sleep_per_weekend_night_h": required_per_weekend_night,
        "physiologically_possible": required_per_weekend_night <= weekend_ceiling_h,
    }


def ledger_repayment_time(debt_h: np.ndarray, nightly_surplus_h: np.ndarray) -> np.ndarray:
    """Nights required to repay a debt at a given nightly surplus. Reported to show that the
    ledger interpretation is not usable, not because it is the right model."""
    s = np.maximum(np.asarray(nightly_surplus_h, float), 1e-6)
    return np.asarray(debt_h, float) / s


if __name__ == "__main__":
    need = 8.7
    print("--- sustained sleep obtained per policy (h/24h) ---")
    for name, p in policies().items():
        wd = sustained_tst(p["tib_weekday"], p["nap"])
        we = sustained_tst(p["tib_weekend"], p["nap"])
        bal = float(policy_weekly_balance(p, np.array([need]))[0])
        print(f"  {name:36s} weekday {wd:.2f}  weekend {we:.2f}  weekly mean balance {bal:+.2f} h/night")

    print("\n--- weekend catch-up arithmetic (need %.1f h) ---" % need)
    for wd_def in (2.0, 3.0, 3.2):
        r = weekend_catchup_arithmetic(wd_def, CEILING_SINGLE_NIGHT_H, need)
        print(f"  weekday deficit {wd_def:.1f} h -> needs {r['required_sleep_per_weekend_night_h']:.1f} h "
              f"per weekend night; ceiling {CEILING_SINGLE_NIGHT_H} h; "
              f"repayable {r['fraction_repayable']*100:.0f}%; possible={r['physiologically_possible']}")

    print("\n--- why the ledger is not a schedule ---")
    for debt in (840, 3330):
        for surplus in (0.2, 0.5, 1.0):
            nights = float(ledger_repayment_time(np.array([debt]), np.array([surplus]))[0])
            print(f"  debt {debt:5d} h at {surplus:.1f} h/night surplus -> {nights:7.0f} nights "
                  f"({nights/365:.1f} years)")
