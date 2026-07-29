"""All effect-size arithmetic for shard s12_psychiatric, in one auditable place."""
from math import log, sqrt


def logratio(point, lo, hi, label):
    v, se = log(point), (log(hi) - log(lo)) / 3.92
    print(f"{label:<58} log={v:+.5f} se={se:.5f} ci=[{log(lo):+.5f},{log(hi):+.5f}]")
    return v, se


def dz_from_t(t, n, label):
    """Within-subject standardized mean difference from paired t (or Wilcoxon Z) and n pairs."""
    d = abs(t) / sqrt(n)
    se = sqrt(1.0 / n + d * d / (2.0 * n))
    print(f"{label:<58} d_z={d:.4f} se={se:.4f} ci=[{d-1.96*se:+.4f},{d+1.96*se:+.4f}]")
    return d, se


def smd_ci(g, lo, hi, label):
    se = (hi - lo) / 3.92
    print(f"{label:<58} g={g:+.4f} se={se:.4f}")
    return g, se


print("=== OBSERVATIONAL: log-OR / log-RR ===")
logratio(1.31, 1.04, 1.64, "zhai2015 short sleep -> depression (adults, RR)")
logratio(1.42, 1.04, 1.92, "zhai2015 long sleep -> depression (adults, RR)")
logratio(1.55, 1.44, 1.67, "short2020 overall mood deficit (adolescents)")
logratio(1.62, 1.38, 1.85, "short2020 depressed mood")
logratio(1.41, 1.29, 1.54, "short2020 anxiety")
logratio(1.83, 1.51, 2.15, "short2020 anger")
logratio(2.02, 1.62, 2.42, "short2020 positive affect")
logratio(1.72, 1.48, 1.97, "short2020 experimental subgroup")
logratio(1.42, 1.31, 1.53, "short2020 cross-sectional subgroup")
logratio(1.67, 1.48, 1.85, "short2020 covariates=none")
logratio(1.28, 1.18, 1.38, "short2020 covariates=others (max adjusted)")
logratio(1.50, 1.13, 2.00, "marino2021 disturbed sleep -> depression (youth OR)")
logratio(2.83, 1.55, 5.17, "hertenstein2019 insomnia -> depression onset")
logratio(3.23, 1.52, 6.85, "hertenstein2019 insomnia -> anxiety onset")
logratio(0.89, 0.88, 0.90, "chiu2018 suicide plan per +1 h sleep")
logratio(1.24, 1.04, 1.49, "gangwisch2010 late parental bedtime -> depression")
logratio(1.07, 0.88, 1.30, "gangwisch2010 same, + sleep duration mediators")
logratio(1.20, 1.01, 1.41, "gangwisch2010 late bedtime -> suicidal ideation")
logratio(1.09, 0.92, 1.29, "gangwisch2010 same, + sleep duration mediators")
logratio(1.38, 1.28, 1.48, "wang2024 insufficient sleep -> suicidal ideation aOR")
logratio(1.34, 1.23, 1.46, "wang2024 insufficient sleep -> suicide plan aOR")
logratio(1.24, 1.17, 1.38, "wang2024 insufficient sleep -> suicide attempt aOR")

print("\n=== ROBERTS 2014 BIDIRECTIONAL (same sample, both arrows) ===")
f_mdd = logratio(3.76, 1.65, 8.58, "FWD short sleep WN -> major depression W2 (adj)")
r_mdd = logratio(4.28, 2.21, 8.32, "REV major depression -> short sleep WN W2 (adj)")
f_sym = logratio(1.38, 1.02, 1.85, "FWD short sleep WN -> depressive symptoms W2 (adj)")
r_sym = logratio(1.24, 0.94, 1.63, "REV depressive symptoms -> short sleep WN W2 (adj)")
logratio(3.12, 1.55, 6.27, "FWD short sleep WN/WE -> major depression W2 (adj)")
logratio(1.95, 0.94, 4.04, "REV major depression -> short sleep WN/WE W2 (adj)")
logratio(1.25, 1.01, 1.54, "FWD short sleep WN/WE -> dep symptoms W2 (adj)")
logratio(1.14, 0.93, 1.40, "REV dep symptoms -> short sleep WN/WE W2 (adj)")
for nm, f, r in (("major depression", f_mdd, r_mdd), ("depressive symptoms", f_sym, r_sym)):
    frac = r[0] / (f[0] + r[0])
    print(f"  reverse share of total log-OR ({nm}): {frac:.3f}")

print("\n=== WINSLER 2015 per hour LESS sleep ===")
for lbl, orv in (("hopelessness", 1.38), ("suicidal ideation", 1.42), ("suicide attempt", 1.58)):
    v = log(orv)
    se_ub = v / 3.29  # p < .001 => |z| > 3.29 => se < v/3.29
    print(f"winsler {lbl:<20} log_or={v:+.5f} se_upper_bound={se_ub:.5f} (CI not reported)")
print("  risk difference 9h -> 4h: hopeless 19.2%->51.6%; ideation 8.1%->31.5%; attempt 1.8%->13.3%")

print("\n=== MENDELIAN RANDOMIZATION ===")
logratio(1.31, 1.25, 1.37, "sun2022 insomnia -> MDD")
logratio(1.37, 1.14, 1.64, "sun2022 MDD -> insomnia")
logratio(1.179, 1.108, 1.255, "zhang2024 short sleep duration -> MDD")
logratio(1.233, 1.214, 1.253, "zhang2024 insomnia -> MDD")
logratio(0.998, 0.996, 0.999, "zhang2024 continuous sleep duration -> MDD")
logratio(0.77, 0.63, 0.94, "daghlas2021 1h earlier sleep midpoint -> MDD")
print("cai2021 insomnia -> MDD  bxy=+0.57 se=0.07 (as reported, +/- form)")
print("cai2021 MDD -> insomnia  bxy=+0.16 se=0.02 (as reported)")
print(f"  cai2021 reverse share of total bxy: {0.16/(0.16+0.57):.3f}")

print("\n=== EXPERIMENTAL: within-subject d_z from Wilcoxon Z / paired t ===")
print("baum2014, n=50 pairs, 6.5h vs 10h TIB x 5 nights:")
dz_from_t(3.25, 50, "  POMS Tension/Anxiety (Z=-3.25)")
dz_from_t(3.10, 50, "  POMS Anger/Hostility (Z=-3.10)")
dz_from_t(4.78, 50, "  POMS Fatigue/Inertia (Z=-4.78)")
dz_from_t(3.37, 50, "  POMS Confusion (Z=-3.37)")
dz_from_t(3.02, 50, "  POMS Vigor loss (Z=-3.02)")
dz_from_t(2.71, 50, "  self-report Emotion Regulation problems (Z=-2.71)")
dz_from_t(2.47, 50, "  self-report Oppositionality/Irritability (Z=-2.47)")
dz_from_t(2.40, 50, "  parent-report Emotion Regulation (Z=-2.40)")
dz_from_t(2.22, 50, "  parent-report Oppositionality/Irritability (Z=-2.22)")
print("  POMS Depression/Dejection: NOT significant, p>.05 -> d_z < 2.01/sqrt(50) = %.3f" % (2.01 / sqrt(50)))

print("motomura2013, n=14 pairs, 4h vs 8h TIB x 5 nights:")
dz_from_t(2.74, 14, "  STAI-state anxiety (t=-2.74)")
dz_from_t(0.40, 14, "  POMS Depression (t=-0.40, NS)")
dz_from_t(0.46, 14, "  POMS Tension-Anxiety (t=-0.46, NS)")
dz_from_t(1.30, 14, "  POMS Fatigue (t=-1.30, NS)")
dz_from_t(3.51, 14, "  Stanford Sleepiness Scale (t=-3.51)")

print("\n=== INTERVENTION SMDs ===")
smd_ci(-0.53, -0.68, -0.38, "scott2021 composite mental health")
smd_ci(-0.63, -0.83, -0.43, "scott2021 depression (k=61)")
smd_ci(-0.47, -0.57, -0.37, "scott2021 depression, outliers removed")
smd_ci(-0.50, -0.76, -0.24, "scott2021 anxiety (k=35)")
smd_ci(0.10, -3.74, 3.94, "scott2021 suicidal ideation (k=2, NS, adverse sign)")
smd_ci(-0.35, -0.55, -0.16, "scott2021 composite, trim-and-fill adjusted")
smd_ci(-0.45, -0.55, -0.36, "gee2019 depression (k=49)")
smd_ci(-0.81, -1.13, -0.49, "gee2019 depression, mental-health subgroup")
smd_ci(-1.29, -2.11, -0.47, "gebara2018 HAM-D")
smd_ci(-0.68, -1.29, -0.06, "gebara2018 BDI")
print("freeman2017 PHQ-9 wk10: adj diff -2.83 (-3.30,-2.35), d=0.48; "
      "se(d) from raw: %.4f" % (0.48 * (0.475 / 2.83)))
print("  arithmetic: raw diff -2.83, half-CI-width = (3.30-2.35)/2 = 0.475; "
      "se_d = d * (halfwidth/1.96) / |diff| = 0.48*0.2423/2.83")
print("  se_d = %.4f" % (0.48 * (0.475 / 1.96) / 2.83))
print("freeman2017 GAD-7 wk10: adj diff -1.86 (-2.29,-1.43), d=0.33; se_d = %.4f"
      % (0.33 * ((2.29 - 1.43) / 2 / 1.96) / 1.86))

print("\n=== GAO 2018 BASUS: male-specific chronic sleep deprivation -> CESD ===")
m_chr, m_chr_lo, m_chr_hi = 15.32, 12.86, 17.78
m_non, m_non_lo, m_non_hi = 14.38, 13.05, 15.72
se_chr, se_non = (m_chr_hi - m_chr_lo) / 3.92, (m_non_hi - m_non_lo) / 3.92
diff = m_chr - m_non
se_diff = sqrt(se_chr ** 2 + se_non ** 2)
sd_cesd = 11.0
print(f"  males: chronic {m_chr} (se {se_chr:.3f}) vs none {m_non} (se {se_non:.3f})")
print(f"  raw diff = {diff:.2f} CESD points, se_diff = {se_diff:.3f} "
      f"(independence assumption -> conservative/wide)")
print(f"  d = diff/SD({sd_cesd}) = {diff/sd_cesd:.4f}, se_d = {se_diff/sd_cesd:.4f}, "
      f"ci=[{(diff-1.96*se_diff)/sd_cesd:+.4f},{(diff+1.96*se_diff)/sd_cesd:+.4f}]")
f_chr, f_non = 19.48, 16.33
se_f_chr, se_f_non = (21.38 - 17.59) / 3.92, (17.24 - 15.42) / 3.92
dfem = f_chr - f_non
se_dfem = sqrt(se_f_chr ** 2 + se_f_non ** 2)
print(f"  females: chronic {f_chr} vs none {f_non}; diff {dfem:.2f}, se {se_dfem:.3f}, "
      f"d = {dfem/sd_cesd:.4f} (paper states Cohen's D = 0.13 adjusted, 0.20 unadjusted)")
