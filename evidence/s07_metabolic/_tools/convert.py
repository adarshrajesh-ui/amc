#!/usr/bin/env python3
"""All effect-size arithmetic for shard s07_metabolic. Printed output is pasted into
the YAML `conversion_formula` / `notes` fields so every number is reproducible."""
import math

from scipy import stats


def ratio(label, est, lo, hi):
    """log-ratio + SE from a reported ratio and its 95% CI."""
    lr, se = math.log(est), (math.log(hi) - math.log(lo)) / 3.92
    print(f"{label:52s} log={lr:+.6f} se={se:.6f}  (check CI: "
          f"{math.exp(lr - 1.96 * se):.3f}-{math.exp(lr + 1.96 * se):.3f})")
    return lr, se


def power(label, est, lo, hi, k):
    """Extrapolate a per-1-h log-linear RR to a k-hour contrast."""
    lr, se = math.log(est), (math.log(hi) - math.log(lo)) / 3.92
    lrk, sek = k * lr, k * se
    print(f"{label:52s} log={lrk:+.6f} se={sek:.6f}  RR={math.exp(lrk):.4f} "
          f"CI {math.exp(lrk - 1.96 * sek):.3f}-{math.exp(lrk + 1.96 * sek):.3f}")
    return lrk, sek


def se_from_p(label, pct, p, n, paired=True):
    """Back out SE of a percent change from a two-tailed p-value and n."""
    df = n - 1 if paired else n - 2
    t = stats.t.isf(p / 2, df)
    se = abs(pct) / t
    print(f"{label:52s} df={df} t={t:.4f} -> se={se:.4f} (pct units)")
    return se


def dz_from_p(label, p, n):
    """Paired standardized effect dz and its SE from a two-tailed p-value and n."""
    t = stats.t.isf(p / 2, n - 1)
    dz = t / math.sqrt(n)
    se = math.sqrt(1 / n + dz ** 2 / (2 * n))
    print(f"{label:52s} t={t:.4f} dz={dz:.4f} se={se:.4f}")
    return dz, se


def se_dz(label, dz, n):
    se = math.sqrt(1 / n + dz ** 2 / (2 * n))
    print(f"{label:52s} dz={dz:.4f} n={n} se={se:.4f}")
    return se


print("=" * 100, "\n== SHAN 2015 dose-response (per-hour RR 1.09, 95% CI 1.04-1.15, below 7 h)")
ratio("shan per 1 h shorter <7h", 1.09, 1.04, 1.15)
power("shan 6h vs 7h (k=1)", 1.09, 1.04, 1.15, 1)
power("shan 5h vs 7h (k=2, DERIVED extrapolation)", 1.09, 1.04, 1.15, 2)
ratio("shan per 1 h longer >8h", 1.14, 1.03, 1.26)

print("=" * 100, "\n== CAPPUCCIO 2010")
ratio("cappuccio short sleep <=5-6h", 1.28, 1.03, 1.60)
ratio("cappuccio short sleep, MEN only", 2.07, 1.16, 3.72)
ratio("cappuccio short sleep, WOMEN only", 1.07, 0.90, 1.28)
ratio("cappuccio <=5h subset (n=5)", 1.36, 1.10, 1.68)
ratio("cappuccio long sleep >8-9h", 1.48, 1.13, 1.96)

print("=" * 100, "\n== LIU 2025 (Ann Med, 53 studies)")
ratio("liu2025 short sleep <7h", 1.18, 1.13, 1.23)
ratio("liu2025 short sleep MEN", 1.13, 1.04, 1.24)
ratio("liu2025 long sleep >8h", 1.13, 1.09, 1.18)

print("=" * 100, "\n== MR ESTIMATES")
ratio("gao2020 MR short sleep (<7h vs 7-8h) -> T2D", 1.15, 0.96, 1.38)
ratio("gao2020 MR insomnia -> T2D", 1.14, 1.09, 1.19)
ratio("gao2020 MR long sleep -> T2D", 1.10, 0.79, 1.51)

print("=" * 100, "\n== BUXTON 2010 (n=19 analysed; F(1,18) reported)")
for nm, pct, F in [("SI (IVGTT) -20%", 20, 15.18), ("M (clamp) -11%", 11, 4.64)]:
    t = math.sqrt(F)
    print(f"{nm:52s} t=sqrt(F)={t:.4f} se={pct / t:.4f} %")
print(f"{'SI: SD 24% -> SE = 24/sqrt(19)':52s} = {24 / math.sqrt(19):.4f} %")

print("=" * 100, "\n== BROUSSARD 2012 (n=7 crossover)")
md, sd_d = 0.47, 0.33
print(f"paired mean diff {md} nM, SD_diff {sd_d} -> SE = {sd_d / math.sqrt(7):.5f} nM")
dz = md / sd_d
print(f"dz = {md}/{sd_d} = {dz:.4f}")
se_dz("broussard dz (EC50 pAkt/tAkt)", dz, 7)
print(f"fold-change EC50 = 0.71/0.24 = {0.71 / 0.24:.3f}  (paper: 'nearly 3-fold')")

print("=" * 100, "\n== KLINGENBERG 2013 (n=21 adolescent boys, crossover; SE from p)")
se_from_p("HOMA-IR +65%, p=0.002", 65, 0.002, 21)
se_from_p("Matsuda index -28%, p=0.007", 28, 0.007, 21)
se_from_p("fasting insulin +59%, p=0.001", 59, 0.001, 21)
se_from_p("fasting C-peptide +24%, p<0.001 (use p=0.001)", 24, 0.001, 21)

print("=" * 100, "\n== NESS 2019 (n=15 men; dz from p)")
dz_from_p("insulin sensitivity, restriction p=0.002", 0.002, 15)
dz_from_p("disposition index AFTER 2 recovery nights p=0.01", 0.01, 15)
dz_from_p("disposition index, restriction p<0.0001 (bound)", 0.0001, 15)

print("=" * 100, "\n== CHEUNG 2026 (reported Cohen's dz; ~16/group of 48)")
se_dz("stable 6h group 2-h glucose dz=0.39", 0.39, 16)
se_dz("variable short sleep group dz=0.99 (bound)", 0.99, 16)

print("=" * 100, "\n== JAVAHERI 2011 (quadratic model predicted HOMA)")
print(f"HOMA 5.0h/7.75h = 2.36/1.96 = {2.36 / 1.96:.4f} -> +{100 * (2.36 / 1.96 - 1):.1f}%")
print(f"HOMA 10.5h/7.75h = 2.41/1.96 = {2.41 / 1.96:.4f} -> +{100 * (2.41 / 1.96 - 1):.1f}%")

print("=" * 100, "\n== HARTESCU 2022 sleep-extension RCT (between-group HOMA-IR)")
print("HOMA-IR change: extension -0.51 (-0.98,-0.03); control +0.28 (-0.20,0.76)")
for nm, e, lo, hi in [("ext", -0.51, -0.98, -0.03), ("ctl", 0.28, -0.20, 0.76)]:
    se = (hi - lo) / 3.92
    print(f"  {nm}: se={se:.4f}")
se_e, se_c = (-0.03 + 0.98) / 3.92, (0.76 + 0.20) / 3.92
diff = -0.51 - 0.28
se_diff = math.sqrt(se_e ** 2 + se_c ** 2)
print(f"  between-group diff = {diff:.3f}, se = {se_diff:.4f}, "
      f"CI {diff - 1.96 * se_diff:.3f} to {diff + 1.96 * se_diff:.3f}")
