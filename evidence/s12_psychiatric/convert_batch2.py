"""Conversions for the second extraction batch (talbot2010, sadikova2024).

talbot2010 reports mixed-design repeated-measures ANOVAs: a within-subject Sleep
Condition factor and a between-subject Age Group factor (3 levels). For the Sleep
Condition main effect the F test is equivalent to a paired test on the pooled sample
after removing group means, so d_z = sqrt(F)/sqrt(N) with N = df_error + 3.

The paper prints one internally inconsistent df pair: the anxiety analysis is reported
as F(1,67) with eta_p^2 = 0.10 while the between factor in the SAME analysis is
F(2,57). eta_p^2 = F/(F + df_error) reproduces the printed 0.10 only at df_error ~= 55,
not 67, so I treat 67 as a typographical error and use 55. I check every conversion
against the printed eta_p^2 before using it.
"""
from math import sqrt


def dz_from_f(f, df_err, k_groups=3):
    n = df_err + k_groups
    dz = sqrt(f) / sqrt(n)
    se = sqrt(1.0 / n + dz * dz / (2.0 * n))
    return dz, se, (dz - 1.96 * se, dz + 1.96 * se), n


def eta_p2(f, df_err):
    return f / (f + df_err)


print("=" * 74)
print("talbot2010 -- check printed eta_p^2 against F and df_error")
print("=" * 74)
checks = [
    ("PANAS-C positive affect composite", 34.11, 55, 0.38),
    ("catastrophizing pre-post anxiety",   6.17, 55, 0.10),
    ("catastrophe likelihood rating",      3.79, 49, 0.07),
    ("most threatening worry rating",      4.36, 51, 0.08),
]
for label, f, dfe, printed in checks:
    calc = eta_p2(f, dfe)
    ok = "MATCH" if abs(calc - printed) < 0.006 else "MISMATCH"
    print("  %-34s F=%6.2f df_err=%d  eta_p2 calc=%.4f printed=%.2f  %s"
          % (label, f, dfe, calc, printed, ok))

print()
print("=" * 74)
print("talbot2010 -- d_z conversions")
print("=" * 74)
for label, f, dfe, _ in checks:
    dz, se, ci, n = dz_from_f(f, dfe)
    print("  %-34s N=%2d  d_z=%+.4f  se=%.5f  ci=[%+.4f, %+.4f]"
          % (label, n, dz, se, ci[0], ci[1]))

print()
print("  NEGATIVE affect composite: F(1,55) < 1, ns -> bound only")
print("    F < 1 implies t < 1, so |d_z| < 1/sqrt(58) = %.4f" % (1.0 / sqrt(58)))

print()
print("=" * 74)
print("sadikova2024 -- standardise the IV estimate on the Kandel-Davies scale")
print("=" * 74)
# baseline SDs by arm, quoted in Results: 15.9 (SD 4.8) policy-change, 17.0 (SD 5.2) comparison
sd_pooled = sqrt((4.8 ** 2 + 5.2 ** 2) / 2.0)
print("  pooled baseline SD = sqrt((4.8^2 + 5.2^2)/2) = %.4f" % sd_pooled)
for label, est, lo, hi in (("overall depression symptoms", -0.78, -1.32, -0.28),
                           ("fatigue cluster",             -1.36, -2.19, -0.69)):
    d = est / sd_pooled
    dlo, dhi = lo / sd_pooled, hi / sd_pooled
    se_pts = (hi - lo) / 3.92
    print("  %-28s %.2f pts -> d=%+.4f  ci=[%+.4f,%+.4f]  se_points=%.5f"
          % (label, est, d, dlo, dhi, se_pts))
print("  paper states 0.78 points = '15.6%% of a standard deviation'; my d = %+.4f"
      % (-0.78 / sd_pooled))

print()
print("  per-hour rescaling: the IV contrast is a SUSTAINED 30-MIN gain, so a per-hour")
print("  figure is 2x the above ONLY under linearity, which is not tested:")
print("    overall depression, per +1 h = %+.3f points = d %+.4f"
      % (-0.78 * 2, -0.78 * 2 / sd_pooled))

print()
print("  intention-to-treat (policy) effects from Table 2, points on the same scale:")
for label, est, lo, hi in (("overall, 1 y", -0.13, -0.17, -0.08),
                           ("overall, 2 y", -0.26, -0.50, -0.02),
                           ("mood, 1 y",    -0.04, -0.46, 0.38),
                           ("mood, 2 y",    -0.03, -0.09, 0.02),
                           ("fatigue, 1 y", -0.54, -0.73, -0.35),
                           ("fatigue, 2 y", -0.91, -1.45, -0.38)):
    print("    %-14s %+.2f (%.2f, %.2f)  se=%.5f  d=%+.4f"
          % (label, est, lo, hi, (hi - lo) / 3.92, est / sd_pooled))
