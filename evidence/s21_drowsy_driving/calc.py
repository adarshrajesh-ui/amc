#!/usr/bin/env python3
"""Every number in injury_channel.md is produced by this script. Run it to reproduce them."""

# ---------------------------------------------------------------- STEP 1
# IIHS Fatality Facts 2024 (FARS), male passenger-vehicle DRIVER deaths per 100k population
d = {16: (123, 2_322_582), 17: (175, 2_326_541), 18: (242, 2_296_205), 19: (313, 2_282_142)}
print("STEP 1  male passenger-vehicle driver deaths, per 100,000 population per year")
for a, (n, pop) in d.items():
    print("   age %d: %d / %s = %.3f" % (a, n, f"{pop:,}", n / pop * 1e5))
deaths_16_18 = sum(d[a][0] for a in (16, 17, 18))
pop_16_18    = sum(d[a][1] for a in (16, 17, 18))
p_percap_3y  = deaths_16_18 / pop_16_18 * 3
print("   ages 16-18 pooled: %d deaths / %s pop = %.4f per 100k/yr" %
      (deaths_16_18, f"{pop_16_18:,}", deaths_16_18 / pop_16_18 * 1e5))
print("   3-year cumulative PER CAPITA probability = %.4f per 100k * 3 = %.6e" %
      (deaths_16_18 / pop_16_18 * 1e5, p_percap_3y))

# ---------------------------------------------------------------- STEP 2
# FHWA Highway Statistics 2023, table DL-22: licensed MALE drivers "19 and under" = 4,552,629
lic_male_le19 = 4_552_629
pop_male_15_19 = 2_234_299 + 2_322_582 + 2_326_541 + 2_296_205 + 2_282_142
pop_male_16_19 = pop_male_15_19 - 2_234_299
L_16_19 = lic_male_le19 / pop_male_16_19
L_15_19 = lic_male_le19 / pop_male_15_19
print("\nSTEP 2  licensure fraction")
print("   FHWA 2023 licensed male drivers 19-and-under = %s" % f"{lic_male_le19:,}")
print("   IIHS 2024 male population 16-19 = %s ; 15-19 = %s" % (f"{pop_male_16_19:,}", f"{pop_male_15_19:,}"))
print("   L(16-19) = %.4f     L(15-19) = %.4f" % (L_16_19, L_15_19))
for L, lab in [(0.49, "L=0.49 (16-19 average)"), (0.45, "L=0.45 (younger 16-18 skew)"), (0.40, "L=0.40 (low)")]:
    print("   per-DRIVER 3-y probability at %-28s = %.4e  (1 in %d)" % (lab, p_percap_3y / L, round(1 / (p_percap_3y / L))))

# NHTSA cross-check: all vehicle types, per licensed male driver 15-20
nhtsa_male_driver_deaths_2023 = 1695
lic_male_15_20 = lic_male_le19 + 9_122_651 / 5.0     # add ~1/5 of the male 20-24 licensed bin
r_nhtsa = nhtsa_male_driver_deaths_2023 / lic_male_15_20
print("\n   NHTSA cross-check (ALL vehicle types, ages 15-20):")
print("      1,695 male young-driver deaths / %s licensed = %.2f per 100,000/yr" % (f"{lic_male_15_20:,.0f}", r_nhtsa * 1e5))
print("      3-year cumulative = %.4e" % (r_nhtsa * 3))

P_BASE, P_LO, P_HI = 5.5e-4, 4.5e-4, 8.0e-4
print("\n   ADOPTED  P_base = %.2e   (range %.2e - %.2e)" % (P_BASE, P_LO, P_HI))

# ---------------------------------------------------------------- STEP 3
# risk-weighted fraction of driving-death risk incurred while sleep-restricted
dow = {"Mon": 377, "Tue": 353, "Wed": 324, "Thu": 375, "Fri": 419, "Sat": 549, "Sun": 502}
tot = sum(dow.values())
mf = sum(dow[k] for k in ("Mon", "Tue", "Wed", "Thu", "Fri"))
w_dow = (mf / tot) / (5 / 7)
mon = {"Jan":197,"Feb":192,"Mar":232,"Apr":215,"May":260,"Jun":300,
       "Jul":286,"Aug":273,"Sep":273,"Oct":236,"Nov":236,"Dec":199}
tot_m = sum(mon.values())
summer = mon["Jun"] + mon["Jul"] + mon["Aug"]
days_summer = (30 + 31 + 31) / 365
w_school_months = ((tot_m - summer) / tot_m) / (1 - days_summer)
print("\nSTEP 3  risk-weighted exposed fraction f")
print("   Mon-Fri share of teen crash deaths = %d/%d = %.4f   (vs 5/7 = %.4f of days)  -> per-day weight %.4f"
      % (mf, tot, mf / tot, 5 / 7, w_dow))
print("   Jun-Aug share = %d/%d = %.4f  (vs %.4f of days) -> school-month per-day weight %.4f"
      % (summer, tot_m, summer / tot_m, days_summer, w_school_months))
school_days_frac = 180 / 365
w = w_dow * w_school_months
num = school_days_frac * w
f_central = num / (num + (1 - num))          # = num, since weights renormalise to 1 overall
print("   exposed days = 180 school days / 365 = %.4f of the year" % school_days_frac)
print("   combined per-day risk weight on exposed days = %.4f * %.4f = %.4f" % (w_dow, w_school_months, w))
print("   f = %.4f * %.4f = %.4f     (unexposed days carry the remaining %.4f)" % (school_days_frac, w, f_central, 1 - f_central))
F_CENTRAL, F_LO, F_HI = 0.41, 0.30, 0.55

# ---------------------------------------------------------------- STEP 4 / 5
def route1(P, f, RR, c):
    M = f * RR + (1 - f)
    AF = (M - 1) / M
    excess = P * AF * c
    return M, AF, excess, excess * 58.0 * 12.0

print("\nSTEP 4/5  ROUTE 1 (relative risk x exposed fraction x causal fraction)")
print("   %-46s %8s %8s %11s %9s" % ("scenario", "M", "AF", "excess p", "months"))
rows = [
    ("CENTRAL  P=5.5e-4 f=.41 RR=1.50 c=0.50",      P_BASE, F_CENTRAL, 1.50, 0.50),
    ("like-for-like habitual RR=1.40",              P_BASE, F_CENTRAL, 1.40, 0.50),
    ("Tefft acute 5-6 h RR=1.90",                   P_BASE, F_CENTRAL, 1.90, 0.50),
    ("Gottlieb 6 h vs 7-8 h RR=1.33",               P_BASE, F_CENTRAL, 1.33, 0.50),
    ("Martiniuk young drivers RR=1.21",             P_BASE, F_CENTRAL, 1.21, 0.50),
    ("LOW    P=4.7e-4 f=.33 RR=1.30 c=0.30",        4.7e-4, 0.33,      1.30, 0.30),
    ("HIGH   P=7.0e-4 f=.50 RR=2.20 c=0.75",        7.0e-4, 0.50,      2.20, 0.75),
    ("EXTREME LOW  P=4.5e-4 f=.30 RR=1.21 c=0.20",  4.5e-4, 0.30,      1.21, 0.20),
    ("EXTREME HIGH P=8.0e-4 f=.55 RR=2.51 c=0.85",  8.0e-4, 0.55,      2.51, 0.85),
]
for lab, P, f, RR, c in rows:
    M, AF, ex, mo = route1(P, f, RR, c)
    print("   %-46s %8.4f %8.4f %11.3e %9.4f" % (lab, M, AF, ex, mo))

# ---------------------------------------------------------------- ROUTE 2
print("\n   ROUTE 2 (drowsy share of fatal crashes x share attributable to habitual restriction)")
print("   %-52s %11s %9s" % ("scenario", "excess p", "months"))
for lab, P, share, attrib in [
    ("CENTRAL  share=0.176 (Tefft 2024) attrib=0.50", P_BASE, 0.176, 0.50),
    ("Tefft 2012 fatal share 0.165",                  P_BASE, 0.165, 0.50),
    ("all-crash share 0.070 (Tefft 2012)",            P_BASE, 0.070, 0.50),
    ("PERCLOS share 0.095 (Owens 2018, all ages)",    P_BASE, 0.095, 0.50),
    ("PERCLOS share 0.0886 (Owens 2018, ages 16-19)", P_BASE, 0.0886, 0.50),
    ("NHTSA POLICE-REPORTED share 0.024  <-- FLOOR",  P_BASE, 0.024, 0.50),
    ("high: share=0.25 (CDC) attrib=0.70",            P_HI,   0.250, 0.70),
]:
    ex = P * share * attrib
    print("   %-52s %11.3e %9.4f" % (lab, ex, ex * 58 * 12))

# ---------------------------------------------------------------- ROUTE 3
print("\n   ROUTE 3 (mechanistic: PERCLOS drowsy-driving time x naturalistic crash OR)")
p0, pc = 0.0157, 0.095
OR = (pc / (1 - pc)) / (p0 / (1 - p0))
print("   drowsy share of baseline driving TIME p0 = %.4f  (GHSA/SHRP2)" % p0)
print("   drowsy share of CRASHES            pc = %.4f  (Owens 2018 PERCLOS)" % pc)
print("   implied drowsy-driving crash OR = (%.6f/%.6f)/(%.6f/%.6f) = %.3f"
      % (pc, 1 - pc, p0, 1 - p0, OR))
for lab, mult in [("Owens 2019 implied 1.35x", 1.35), ("conservative 1.20x", 1.20), ("aggressive 2.00x", 2.00)]:
    p1 = p0 * mult
    M = (p1 * OR + (1 - p1)) / (p0 * OR + (1 - p0))
    AF = (M - 1) / M
    ex = P_BASE * AF
    print("   %-28s p1=%.4f  M=%.4f  AF=%.4f  excess=%.3e  months=%.4f" % (lab, p1, M, AF, ex, ex * 58 * 12))

# ---------------------------------------------------------------- DEDUP
print("\nDE-DUPLICATION against s13_mortality")
allcause_3y = 0.002
share_driver = p_percap_3y / allcause_3y
print("   s13 all-cause 3-y cumulative death probability (their figure) = %.4f" % allcause_3y)
print("   my per-capita driver-death 3-y probability                    = %.6f" % p_percap_3y)
print("   driver deaths are %.1f%% of all-cause adolescent male mortality" % (share_driver * 100))
print("   => s13's 0.2-month CEILING already contains ~%.4f months of driver-death term" % (0.2 * share_driver))
print("   => s13's 0.006-0.05-month CENTRAL band contains ~%.4f-%.4f months of driver-death term"
      % (0.006 * share_driver, 0.05 * share_driver))
