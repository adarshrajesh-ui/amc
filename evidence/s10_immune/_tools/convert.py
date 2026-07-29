"""All ratio -> log-scale conversions and derived SDs used in the YAML records.
se = (ln(upper) - ln(lower)) / 3.92  per EXTRACTION_INSTRUCTIONS.md
"""
import math


def lr(label, v, lo, hi):
    print(f"{label:52s} log={math.log(v):+.4f} se={(math.log(hi)-math.log(lo))/3.92:.4f} "
          f"ci_log=[{math.log(lo):+.4f}, {math.log(hi):+.4f}]")


print("== Prather 2015 clinical cold, actigraphy duration (ref >7h)")
lr("<5h vs >7h  OR 4.50 (1.08-18.69)", 4.50, 1.08, 18.69)
lr("5-6h vs >7h OR 4.24 (1.08-16.71)", 4.24, 1.08, 16.71)
lr("6.01-7h vs >7h OR 1.66 (0.40-6.95) NS", 1.66, 0.40, 6.95)

print("\n== Cohen 2009 objective cold (ref top tertile)")
lr("dur <7h vs >=8h OR 2.94 (1.18-7.30)", 2.94, 1.18, 7.30)
lr("dur 7-<8h vs >=8h OR 1.63 (0.63-4.19) NS", 1.63, 0.63, 4.19)
lr("eff <92% vs >98% OR 5.50 (2.08-14.48)", 5.50, 2.08, 14.48)
lr("eff 92-98% vs >98% OR 3.94 (1.50-10.37)", 3.94, 1.50, 10.37)
lr("eff <=85% vs rest OR 5.37 (1.51-19.1)", 5.37, 1.51, 19.1)

print("\n== Prather & Leung 2016 NHANES (ref 7-8h), Model 2 fully adjusted")
lr("cold <=5h OR 1.17 (1.01-1.35)", 1.17, 1.01, 1.35)
lr("cold 6h OR 1.02 (0.91-1.14) NULL", 1.02, 0.91, 1.14)
lr("cold >=9h OR 0.97 (0.83-1.14) NULL", 0.97, 0.83, 1.14)
lr("infection <=5h OR 1.51 (1.18-1.93)", 1.51, 1.18, 1.93)
lr("infection 6h OR 0.97 (0.76-1.25) NULL", 0.97, 0.76, 1.25)
print("  Model 1 (age+sex only):")
lr("cold <=5h OR 1.28 (1.10-1.48)", 1.28, 1.10, 1.48)
lr("infection <=5h OR 1.82 (1.42-2.34)", 1.82, 1.42, 2.34)

print("\n== Patel 2012 pneumonia (ref 8h), Multivariate Model 2")
lr("<=5h RR 1.39 (1.06-1.82)", 1.39, 1.06, 1.82)
lr("6h RR 1.17 (0.96-1.41) NULL", 1.17, 0.96, 1.41)
lr("7h RR 1.14 (0.96-1.35) NULL", 1.14, 0.96, 1.35)
lr(">=9h RR 1.38 (1.04-1.84)", 1.38, 1.04, 1.84)
print("  age-adjusted:")
lr("<=5h RR 1.70 (1.30-2.23)", 1.70, 1.30, 2.23)
lr("6h RR 1.29 (1.07-1.56)", 1.29, 1.07, 1.56)

print("\n== Martinez-Albert 2025 cold past 30d (ref 7-8h)")
lr("<=6h OR 1.83 (1.21-2.76)", 1.83, 1.21, 2.76)
lr(">=9h OR 3.60 (1.52-8.57)", 3.60, 1.52, 8.57)
lr("other infections <=6h OR 1.31 (0.62-2.75) NULL", 1.31, 0.62, 2.75)
lr("SJL >60min, cold past 12m OR 4.28 (1.50-12.21)", 4.28, 1.50, 12.21)

print("\n== Forthun 2023 (ref 7-8h), adjusted RR")
lr("any infection <6h RR 1.27 (1.11-1.46)", 1.27, 1.11, 1.46)
lr("RTI <6h RR 1.16 (0.96-1.42) NULL", 1.16, 0.96, 1.42)
lr("GI <6h RR 1.92 (1.29-2.87)", 1.92, 1.29, 2.87)
lr("antibiotics <6h RR 1.57 (1.13-2.18)", 1.57, 1.13, 2.18)

print("\n== Prather 2012 HepB clinical protection")
lr("per +1h actigraphy sleep, OR protected 3.53 (1.22-10.27)", 3.53, 1.22, 10.27)
lr("<6h vs >7h, OR protected 0.09 (0.01-0.94)", 0.09, 0.01, 0.94)
lr("6-7h vs >7h, OR protected 0.36 (0.04-3.67) NS", 0.36, 0.04, 3.67)
lr("per +1h diary sleep, OR protected 2.73 (1.20-6.23)", 2.73, 1.20, 6.23)

print("\n== SMD-scale meta-analytic estimates: se = (hi-lo)/3.92")
for lab, v, lo, hi in [
    ("Irwin2016 CRP short dur continuous (16 samples)", 0.09, 0.01, 0.17),
    ("Irwin2016 IL-6 short dur continuous combined (18)", 0.11, -0.01, 0.23),
    ("Irwin2016 IL-6 subj continuous (9 samples)", 0.03, -0.09, 0.14),
    ("Irwin2016 CRP EXTREME short <7h (11 samples)", 0.08, -0.01, 0.16),
    ("Irwin2016 IL-6 EXTREME short <7h (8 samples)", 0.08, -0.02, 0.18),
    ("Irwin2016 TNF EXTREME short (3 samples)", 0.11, -0.01, 0.22),
    ("Irwin2016 CRP EXTREME long >8h (11 samples)", 0.17, 0.01, 0.34),
    ("Irwin2016 IL-6 EXTREME long >8h (8 samples)", 0.11, 0.02, 0.20),
    ("Irwin2016 IL-6 objective continuous (9 samples)", 0.29, 0.05, 0.52),
    ("Irwin2016 CRP objective continuous (5 samples)", 0.18, -0.04, 0.41),
    ("Irwin2016 CRP experimental restriction multi-night (4)", 0.61, -1.09, 2.30),
    ("Irwin2016 IL-6 experimental restriction multi-night (5)", 0.13, -0.21, 0.47),
    ("Irwin2016 CRP experimental 1-night deprivation (4)", -0.43, -1.62, 0.77),
    ("Irwin2016 IL-6 experimental 1-night deprivation (12)", 0.16, -0.11, 0.43),
    ("Ballesio2026 IL-6 multi-night PSD, outlier-excl (k=5)", 0.42, 0.11, 0.73),
    ("Ballesio2026 IL-6 multi-night PSD, ALL studies (k=6)", 0.10, -0.48, 0.67),
    ("Ballesio2026 CRP multi-night PSD, outlier-excl (k=5)", 0.76, 0.09, 1.43),
    ("Ballesio2026 CRP multi-night PSD, ALL studies (k=6)", 0.50, -0.38, 1.38),
    ("Ballesio2026 CRP multi-night, within-subj only (k=4)", 0.61, -0.16, 1.37),
    ("Ballesio2026 TNF multi-night PSD (k=5)", -0.34, -0.88, 0.20),
    ("Ballesio2026 IL-6 1 night TSD (k=8, outlier-excl)", 0.21, -0.15, 0.58),
    ("Ballesio2026 CRP 1 night TSD (k=5)", -0.23, -0.65, 0.19),
    ("Spiegel2023 vaccine, SELF-REPORT short (n=504)", 0.29, -0.04, 0.63),
    ("Spiegel2023 vaccine, SELF-REPORT <65y (n=299)", 0.59, 0.12, 1.05),
    ("Spiegel2023 vaccine, OBJECTIVE short (n=304)", 0.79, 0.40, 1.18),
    ("Spiegel2023 vaccine, OBJECTIVE experimental (n=133)", 0.86, 0.28, 1.44),
    ("Spiegel2023 vaccine, OBJECTIVE prospective (n=171)", 0.67, 0.18, 1.16),
    ("Spiegel2023 vaccine, OBJECTIVE men", 0.93, 0.54, 1.33),
    ("Spiegel2023 vaccine, OBJECTIVE women NS", 0.42, -0.49, 1.32),
]:
    print(f"{lab:56s} v={v:+.2f} se={(hi-lo)/3.92:.4f}")

print("\n== Pejovic 2013 within-subject IL-6 (n=30), raw pg/ml")
n = 30
for lab, m, se in [("SR vs baseline (increase)", 0.90, 0.41),
                   ("recovery vs SR (decrease)", 0.93, 0.45),
                   ("recovery vs baseline (residual)", 0.02, 0.34)]:
    sd_diff = se * math.sqrt(n)
    print(f"  {lab:34s} mean={m:.2f} se={se:.2f} sd_diff={sd_diff:.3f} d_z={m/sd_diff:+.3f}")

print("\n== Stager 2023 adolescent shortest vs stable-recommended adult CRP (mg/L)")
m1, s1, m2, s2 = 3.21, 0.29, 3.35, 0.21
d = m1 - m2
se = math.sqrt(s1 ** 2 + s2 ** 2)
print(f"  diff={d:+.3f} mg/L  se={se:.3f}  95% CI=[{d-1.96*se:+.3f}, {d+1.96*se:+.3f}]")

print("\n== Prather 2012 per-hour antibody change")
print("  reported: each additional hour of sleep -> 56% increase in secondary Ab")
print(f"  log(1.56) = {math.log(1.56):+.4f} (per +1 h); per -1 h => {-math.log(1.56):+.4f}")

print("\n== Fondell 2011 (short <7h vs 7-9h)")
lr("PHA T-cell function +49% (7-109%)", 1.49, 1.07, 2.09)
lr("NKCA -30% (-46 to -8%)", 0.70, 0.54, 0.92)
