"""Back-calculate absolute event rates by exposure category from reported ORs,
category ns, and the reported total number of events. Uses a single-parameter
fit on the referent odds so that expected events sum to the observed total.

This is an approximation: published ORs are covariate-adjusted whereas the
implied rates here are marginal. Recorded for transparency; every derived number
is labelled as derived, never as quoted.
"""
from scipy.optimize import brentq


def solve(ns, ors, total_events, label):
    def f(x):
        return sum(n * (o * x) / (1 + o * x) for n, o in zip(ns, ors)) - total_events

    x = brentq(f, 1e-9, 1e6)
    ps = [(o * x) / (1 + o * x) for o in ors]
    print(f"--- {label}")
    print(f"    referent odds = {x:.4f}  referent risk = {ps[-1]*100:.1f}%")
    for n, o, p in zip(ns, ors, ps):
        print(f"    n={n:3d} OR={o:5.2f} -> implied risk {p*100:5.1f}%  (events {n*p:.1f})")
    print(f"    sum events = {sum(n*p for n, p in zip(ns, ps)):.1f} (target {total_events})")
    print(f"    absolute risk difference, most-exposed vs referent = "
          f"{(ps[0]-ps[-1])*100:.1f} pct points")
    print()
    return ps


# Prather 2015 Sleep: actigraphy duration categories, clinical cold outcome
solve([36, 54, 52, 22], [4.50, 4.24, 1.66, 1.0], 48,
      "Prather 2015: clinical cold by actigraphy sleep duration (<5, 5-6, 6.01-7, >7 h)")

# Cohen 2009 Arch Intern Med: self-report duration tertiles, objective cold
solve([58, 52, 43], [2.94, 1.63, 1.0], 54,
      "Cohen 2009: objective cold by self-report duration tertile (<7, 7-<8, >=8 h)")

# Cohen 2009: sleep efficiency tertiles, objective cold
solve([48, 53, 52], [5.50, 3.94, 1.0], 54,
      "Cohen 2009: objective cold by sleep efficiency tertile (<92, 92-98, >98%)")


def logratio(v, lo, hi, name):
    import math
    lv = math.log(v)
    se = (math.log(hi) - math.log(lo)) / 3.92
    print(f"{name}: log = {lv:.4f}, se = {se:.4f}, ci_log = [{math.log(lo):.4f}, {math.log(hi):.4f}]")


print("--- log-OR conversions (se = (ln upper - ln lower)/3.92)")
logratio(4.50, 1.08, 18.69, "Prather2015 <5h vs >7h  OR")
logratio(4.24, 1.08, 16.71, "Prather2015 5-6h vs >7h OR")
logratio(1.66, 0.40, 6.95, "Prather2015 6.01-7h vs >7h OR")
logratio(2.94, 1.18, 7.30, "Cohen2009 <7h vs >=8h OR")
logratio(1.63, 0.63, 4.19, "Cohen2009 7-<8h vs >=8h OR")
logratio(5.50, 2.08, 14.48, "Cohen2009 eff<92 vs >98 OR")
logratio(3.94, 1.50, 10.37, "Cohen2009 eff92-98 vs >98 OR")
logratio(5.37, 1.51, 19.1, "Cohen2009 eff<=85 vs rest OR")
