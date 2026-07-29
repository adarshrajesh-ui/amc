#!/usr/bin/env python3
"""Compute log-scale point estimates and SEs for every ratio effect in shard s21.

se = (ln(upper) - ln(lower)) / 3.92  per EXTRACTION_INSTRUCTIONS.md
For p-value-only effects, se = ln(OR) / z(p) and inferred_from_ci must be true.
"""
import math


def lg(label, est, lo=None, hi=None):
    v = math.log(est)
    if lo is None:
        print("%-58s log=%+.6f  se=None  (no CI reported)" % (label, v))
        return
    se = (math.log(hi) - math.log(lo)) / 3.92
    print("%-58s log=%+.6f  se=%.6f  ci=[%+.6f, %+.6f]" % (
        label, v, se, math.log(lo), math.log(hi)))


def from_p(label, est, p):
    # two-sided normal z for given p
    import statistics
    z = abs(statistics.NormalDist().inv_cdf(p / 2.0))
    v = math.log(est)
    print("%-58s log=%+.6f  se=%.6f  (z=%.4f from p=%.3f)" % (label, v, abs(v) / z, z, p))


print("== tefft2016_aaa: sleep in past 24 h (referent >=7 h), unmatched primary ==")
lg("<4:00", 11.5, 2.9, 45.7)
lg("4:00-4:59", 4.3, 2.2, 8.3)
lg("5:00-5:59", 1.9, 1.3, 2.6)
lg("6:00-6:59", 1.3, 1.1, 1.7)
print("== tefft2016_aaa: USUAL daily sleep (referent >=7 h), unmatched primary ==")
lg("usual <4:00", 0.8, 0.1, 5.6)
lg("usual 4:00-4:59", 5.4, 1.6, 17.6)
lg("usual 5:00-5:59", 1.4, 0.5, 3.6)
lg("usual 6:00-6:59", 1.4, 0.9, 2.0)
print("== tefft2016_aaa: deviation from usual ==")
lg("0:01-0:59 less", 1.2, 0.9, 1.6)
lg("1:00-1:59 less", 1.3, 1.0, 1.7)
lg("2:00-2:59 less", 3.0, 2.0, 4.3)
lg("3:00-3:59 less", 2.1, 1.0, 4.4)
lg(">=4:00 less", 10.2, 4.6, 22.9)

print("\n== tefft2018 (Sleep, peer-reviewed, same NMVCCS data) ==")
lg("6 h", 1.3, 1.04, 1.7)
lg("5 h", 1.9, 1.1, 3.2)
lg("4 h", 2.9, 1.4, 6.2)
lg("<4 h", 15.1, 4.2, 54.4)
lg("<4 h single- vs multi-vehicle ratio-of-ORs", 3.4, 2.1, 5.6)

print("\n== connor2002 ==")
lg("Stanford Sleepiness 4-7 vs 1-3", 8.2, 3.4, 19.7)
lg("<=5 h in past 24 h vs >5 h", 2.7, 1.4, 5.4)
lg("driving 02:00-05:00 vs other", 5.6, 1.4, 22.7)

print("\n== bioulac2017 meta-analysis ==")
lg("sleepiness at the wheel, pooled", 2.51, 1.87, 3.39)

print("\n== gottlieb2018 (SHHS) ==")
lg("per 1 h LESS usual sleep, all", 1.13, 1.01, 1.28)
lg("per 1 h LESS usual sleep, non-sleepy", 1.22, 1.05, 1.43)
lg("Epworth >=11", 1.54, 1.15, 2.07)
lg("6 h vs 7-8 h", 1.33)
lg("<=5 h vs 7-8 h", 1.47)
lg(">=9 h vs 7-8 h", 0.76)

print("\n== cummings2001 ==")
lg("felt falling asleep", 14.2, 1.4, 147.0)
lg("per additional 100 miles", 2.2, 1.4, 3.3)

print("\n== martiniuk2013 (DRIVE) ==")
lg("<=6 h vs >6 h per night, any crash", 1.21, 1.04, 1.41)
lg("less weekend sleep, run-off-road crash", 1.55, 1.21, 2.00)
lg("less sleep, crash 00:00-05:59", 1.86, 1.11, 3.13)
lg("less sleep, crash 20:00-23:59", 1.66, 1.15, 2.39)

print("\n== pizza2010 (p-values only) ==")
from_p("sleepiness while driving", 2.1, 0.010)
from_p("bad sleep", 1.9, 0.047)
from_p("male sex", 3.3, 0.0001)
from_p("tobacco use", 3.2, 0.0001)

print("\n== binhasan2020 ==")
lg("FC pre vs post SST delay, all crashes", 1.07, 1.00, 1.14)
lg("FC pre vs post, distraction-related", 1.14, 0.99, 1.31)

print("\n== vorona2011 derived rate ratios ==")
for yr, (vb_r, ch_r) in {"2008": (65.8, 46.6), "2007": (71.2, 55.6)}.items():
    n_vb, n_ch = 12916, 8459
    c_vb, c_ch = vb_r / 1000 * n_vb, ch_r / 1000 * n_ch
    rr = vb_r / ch_r
    se = math.sqrt(1 / c_vb + 1 / c_ch)
    print("  %s VB/Ches RR=%.4f log=%+.6f se=%.6f (crashes %.0f vs %.0f, "
          "se=sqrt(1/a+1/b))" % (yr, rr, math.log(rr), se, c_vb, c_ch))

print("\n== vorona2014 derived rate ratio (2009-10, 16-18 y) ==")
print("  Henrico 48.8/1000 vs Chesterfield 37.9/1000; RR=%.4f log=%+.6f "
      "(denominators not reported in abstract -> se from p=0.04)"
      % (48.8 / 37.9, math.log(48.8 / 37.9)))
from_p("  vorona2014 2009-10 RR", 48.8 / 37.9, 0.04)
print("  2010-11, 16-17 y: 53.2 vs 42.0 -> RR=%.4f log=%+.6f"
      % (53.2 / 42.0, math.log(53.2 / 42.0)))

print("\n== danner2008 derived difference-in-differences ==")
post_pre = 1 - 0.165
state = 1 + 0.078
did = post_pre / state
print("  county post/pre = %.4f; rest-of-state post/pre = %.4f; "
      "DiD ratio = %.4f -> log=%+.6f (no CI reported)"
      % (post_pre, state, did, math.log(did)))

print("\n== foss2019 ==")
for lab, pct, p in [("overall level shift", -0.14, 0.076),
                    ("07:00-07:59", -0.25, 0.008),
                    ("08:00-08:59", 0.21, 0.004),
                    ("14:00-14:59", -0.48, 0.0005),
                    ("15:00-15:59", 0.32, 0.024),
                    ("16:00-16:59", 0.19, 0.102)]:
    rr = 1 + pct
    from_p("  %s (%.0f%%)" % (lab, pct * 100), rr, p)
