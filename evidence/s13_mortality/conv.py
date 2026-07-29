#!/usr/bin/env python3
"""log-ratio conversion helper: value=ln(point), se=(ln(hi)-ln(lo))/3.92."""
import math
import sys

ROWS = [
    # label, point, lo, hi
    ("ak19_tot_SS", 1.10, 0.94, 1.29),
    ("ak19_tot_SML", 1.04, 0.79, 1.37),
    ("ak19_tot_ML", 0.94, 0.83, 1.08),
    ("ak19_tot_LL", 1.06, 0.95, 1.17),
    ("ak19_tot_LS", 1.10, 0.85, 1.43),
    ("ak19_u65_SS", 1.65, 1.22, 2.23),
    ("ak19_u65_SML", 1.09, 0.77, 1.54),
    ("ak19_u65_ML", 1.02, 0.86, 1.21),
    ("ak19_u65_LL", 1.25, 1.05, 1.50),
    ("ak19_u65_LS", 1.26, 0.80, 1.98),
    ("ak19_o65_SS", 0.97, 0.81, 1.18),
    ("ak19_o65_SML", 1.21, 0.67, 1.69),
    ("ak19_wknd_u65_le5", 1.52, 1.15, 2.02),
    ("ak19_wknd_u65_le5_wdadj", 1.40, 0.97, 2.02),
    ("ak19_wknd_u65_6h", 0.82, 0.62, 1.07),
    ("ak19_wknd_tot_le5", 1.10, 0.95, 1.28),
    ("ak17_all_le5_crude", 1.13, 1.01, 1.25),
    ("ak17_all_le5_adj", 1.12, 0.99, 1.27),
    ("ak17_all_6h_adj", 0.98, 0.88, 1.09),
    ("ak17_all_ge8_adj", 1.10, 1.00, 1.20),
    ("ak17_u65_le5_crude", 1.45, 1.19, 1.77),
    ("ak17_u65_le5_adj", 1.37, 1.09, 1.71),
    ("ak17_u65_6h_adj", 0.92, 0.77, 1.08),
    ("ak17_u65_ge8_adj", 1.27, 1.08, 1.48),
    ("ak17_o65_le5_adj", 1.05, 0.90, 1.22),
    ("ak17_u65_le5_excl2y", 1.31, 1.03, 1.65),
    ("ak17_u65_le5_ref78", 1.25, 1.01, 1.55),
    ("ak17_u65_6h_ref78", 0.84, 0.72, 0.98),
    ("ak17_u45_le5_adj", 2.45, 1.19, 5.04),
    ("ak17_u45_ge8_adj", 2.10, 1.32, 3.34),
    ("ak17_u70_le5_adj", 1.38, 1.16, 1.65),
    ("cap10_short", 1.12, 1.06, 1.18),
    ("cap10_long", 1.30, 1.22, 1.38),
    ("liu17_4h", 1.05, 1.02, 1.07),
    ("liu17_5h", 1.06, 1.03, 1.09),
    ("liu17_6h", 1.04, 1.03, 1.06),
    ("liu17_9h", 1.13, 1.10, 1.16),
    ("liu17_10h", 1.25, 1.22, 1.28),
    ("liu17_male_4h", 1.01, 0.96, 1.06),
    ("liu17_male_5h", 1.02, 0.97, 1.08),
    ("liu17_male_6h", 1.02, 0.98, 1.06),
    ("liu17_fem_5h", 1.08, 1.03, 1.14),
    ("yin17_3h", 1.12, 1.10, 1.14),
    ("yin17_4h", 1.08, 1.06, 1.09),
    ("yin17_5h", 1.04, 1.03, 1.05),
    ("yin17_6h", 1.01, 1.00, 1.01),
    ("yin17_8h", 1.04, 1.04, 1.05),
    ("yin17_9h", 1.15, 1.14, 1.16),
    ("yin17_10h", 1.32, 1.29, 1.35),
    ("yin17_perh_short", 1.06, 1.04, 1.07),
    ("yin17_perh_long", 1.13, 1.11, 1.15),
    ("yin17_shortest_vs_ref", 1.13, 1.10, 1.17),
    ("yin17_longest_vs_ref", 1.35, 1.29, 1.41),
    ("itani17_short_mort", 1.12, 1.08, 1.16),
    ("jike18_long_mort", 1.39, 1.31, 1.47),
    ("ungvari25_short", 1.14, 1.10, 1.18),
    ("ungvari25_long", 1.34, 1.26, 1.42),
    ("chaput26_spt_7v5", 0.70, 0.61, 0.79),
    ("chaput26_tst_7v5", 0.83, 0.78, 0.89),
    ("chaput26_sr_7v5", 0.86, 0.74, 1.00),
    ("stmaurice24_5v7", 1.29, 1.09, 1.52),
    ("liang23_short", 1.27, 1.11, 1.45),
    ("liang23_long", 1.16, 1.06, 1.28),
    ("li26_SR_norebound", 1.15, 1.01, 1.31),
    ("li26_SR_rebound", 1.12, 0.98, 1.28),
    ("li26_sevSR_norebound", 1.42, 1.24, 1.63),
    ("li26_sevSR_rebound", 1.13, 0.95, 1.36),
    ("li26_short_SR_noreb", 1.19, 1.01, 1.40),
    ("li26_short_sevSR_noreb", 1.38, 1.17, 1.63),
    ("li26_u65_SR_noreb", 1.43, 1.13, 1.79),
    ("li26_u65_sevSR_noreb", 1.35, 1.03, 1.77),
    ("zhang25_obs_short", 1.246, 1.195, 1.298),
    ("zhang25_obs_long", 1.735, 1.643, 1.831),
    ("zhang25_mr_nap", 1.219, 1.071, 1.387),
    ("duggan14_male_quad", 1.15, 1.05, 1.27),
    ("duggan14_female_quad", 1.02, 0.91, 1.14),
    ("wang20_lowstable_death", 1.50, 1.07, 2.10),
    ("wang20_normdecr_death", 1.34, 1.15, 1.57),
    ("kripke02_ref", 1.00, 1.00, 1.00),
]


def show(label, p, lo, hi):
    v = math.log(p)
    se = (math.log(hi) - math.log(lo)) / 3.92 if hi > lo else None
    ci = [math.log(lo), math.log(hi)]
    print("%-26s HR=%-6s log=%+.6f  se=%s  logci=[%+.6f, %+.6f]" % (
        label, p, v, ("%.6f" % se) if se else "None", ci[0], ci[1]))
    return v, se


if __name__ == "__main__":
    if len(sys.argv) > 3:
        show("adhoc", float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))
    else:
        for r in ROWS:
            show(*r)
