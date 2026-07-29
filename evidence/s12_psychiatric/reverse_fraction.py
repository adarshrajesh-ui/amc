"""Estimate what fraction of the observational short-sleep/depression association is NOT
a causal effect of sleep duration. Six independent routes, all on the log scale.

Every input number is quoted verbatim in the corresponding YAML record.
"""
from math import log

print("=" * 78)
print("ROUTE 1: bidirectional coefficients in the SAME adolescent sample")
print("=" * 78)
print("  1a. roberts2014, odds ratios:")
for label, fwd, rev in (("major depression", 3.76, 4.28),
                        ("depressive symptoms", 1.38, 1.24)):
    f, r = log(fwd), log(rev)
    print(f"      {label:<22} forward log_or={f:+.4f}  reverse log_or={r:+.4f}  "
          f"reverse share={r/(f+r):.3f}")
print("  1b. marino2022_qlscd, cross-lagged betas in one model, ages 10-12:")
fwd, rev = 0.10, 0.09
print(f"      {'disturbed sleep <-> dep':<22} forward beta={fwd:+.4f}  reverse beta={rev:+.4f}  "
      f"reverse share={rev/(fwd+rev):.3f}")
print("      ages 12-13: ONLY the reverse arrow survives (beta 0.05), forward null")
print("             -> reverse share at that wave = 1.00")
print("      ages 13-15 and 15-17: BOTH arrows null (subject's own age band)")
print("  -> reverse share 40-52% (roberts2014) and 47% (marino2022_qlscd) on three")
print("     outcomes across two independent cohorts. Converges near one half.")

print()
print("=" * 78)
print("ROUTE 2: MR in both directions on the INSOMNIA axis")
print("=" * 78)
for study, fwd, rev in (("sun2022_mr (log OR)", log(1.31), log(1.37)),
                        ("cai2021_mr (bxy)", 0.57, 0.16)):
    print(f"  {study:<24} forward={fwd:+.4f}  reverse={rev:+.4f}  "
          f"reverse share={rev/(fwd+rev):.3f}")
print("  -> the two MR studies DISAGREE: 22% vs 54%. Range, not a point estimate.")

print()
print("=" * 78)
print("ROUTE 3: what adjusting for BASELINE DEPRESSION does to the youth association")
print("=" * 78)
unadj = log(2.83)   # hertenstein2019 insomnia -> depression, mostly no baseline adjustment
adj = log(1.50)     # marino2021 disturbed sleep -> depression, ALL estimates baseline-adjusted
print(f"  hertenstein2019 (not baseline-adjusted) log_or={unadj:+.4f}")
print(f"  marino2021      (baseline-adjusted)     log_or={adj:+.4f}")
print(f"  -> fraction removed by baseline-depression adjustment = {1 - adj/unadj:.3f}")
print("     CAVEAT: different studies, different exposures. Cross-study, so weak.")

print()
print("=" * 78)
print("ROUTE 4: within-study attenuation from covariate adjustment (short2020, adolescents)")
print("=" * 78)
none_adj, max_adj = log(1.67), log(1.28)
print(f"  covariates = none            log_or={none_adj:+.4f}")
print(f"  covariates = others (max)    log_or={max_adj:+.4f}")
print(f"  -> fraction removed by covariate adjustment alone = {1 - max_adj/none_adj:.3f}")

print()
print("=" * 78)
print("ROUTE 5: observational vs genetically identified, SLEEP DURATION axis")
print("=" * 78)
obs = log(1.31)            # zhai2015 observational prospective, adults
mr_dichot = log(1.179)     # zhang2024_mr genetically proxied SHORT sleep
mr_cont = log(0.998)       # zhang2024_mr genetically proxied CONTINUOUS duration
print(f"  observational short sleep (zhai2015)        log={obs:+.5f}")
print(f"  MR dichotomous short sleep (zhang2024_mr)   log={mr_dichot:+.5f}  "
      f"-> non-causal share={1 - mr_dichot/obs:.3f}")
print(f"  MR continuous duration (zhang2024_mr)       log={mr_cont:+.5f}  "
      f"-> non-causal share={1 - abs(mr_cont)/obs:.3f}")
print("  sun2022_mr continuous duration -> MDD: NULL (no point estimate published)")
print("  -> non-causal share on the duration axis: 39% to ~100%")

print()
print("=" * 78)
print("ROUTE 6: quasi-experimental (externally IMPOSED sleep opportunity) vs observational")
print("=" * 78)
print("  This is the route that matches the subject's exposure: sleep restricted by an")
print("  outside constraint, not by insomnia and not by his own mood.")
sd_kd = (4.8 ** 2 + 5.2 ** 2) / 2.0
sd_kd = sd_kd ** 0.5
d_sad = -0.78 / sd_kd
print(f"  sadikova2024  IV, +30 min/night sustained 2 y  -> d = {d_sad:+.4f}")
print(f"                    naive linear per-hour        -> d = {2*d_sad:+.4f} (linearity UNTESTED)")
print("  wang2026_dsst pooled DSST, +69 min/night        -> g = -0.2000")
print(f"                    implied per-hour             -> g = {-0.20*60/69:+.4f}")
print("  gangwisch2010 parental bedtime >=midnight vs <=10pm, a 2 h swing in imposed")
print(f"                sleep opportunity: OR 1.24 -> log_or {log(1.24):+.4f}, d ~= "
      f"{log(1.24)*0.5513:+.4f}")
print("  -> three unrelated quasi-experiments converge on |d| ~ 0.12 to 0.31 for imposed")
print("     short sleep, against observational cross-sectional ORs of 1.7-2.8 (|d| 0.3-0.6).")

print()
print("=" * 78)
print("ROUTE 7: CRITERION CONTAMINATION -- a third inflation mechanism, not reverse causation")
print("=" * 78)
print("  sadikova2024 decomposed the 6-item Kandel-Davies scale under a causal sleep gain.")
print("  Two items are fatigue/sleep ('too tired to do things', 'trouble going to sleep or")
print("  staying asleep'); four are mood (unhappy/sad/depressed, hopeless, nervous, worrying).")
tot_2y, fat_2y, mood_2y = -0.26, -0.91, -0.03
print(f"    total score ITT 2 y : {tot_2y:+.2f} (-0.50, -0.02)  SIGNIFICANT")
print(f"    fatigue cluster     : {fat_2y:+.2f} (-1.45, -0.38)  SIGNIFICANT, 3.5x the total")
print(f"    mood cluster        : {mood_2y:+.2f} (-0.09,  0.02)  NULL")
print("  If the total is the 6-item mean, the 2 fatigue items contribute (2/6)*fatigue:")
fat_contrib = (2.0 / 6.0) * fat_2y
print(f"    fatigue contribution to the total = (2/6) * {fat_2y:+.2f} = {fat_contrib:+.4f}")
print(f"    that is {fat_contrib/tot_2y*100:.0f}% of the observed total effect of {tot_2y:+.2f}")
print("    ASSUMPTION: 'Mood' in Table 2 is the remaining 4 items. If it is item c alone the")
print("    exact share shifts, but it cannot fall much below 100% while mood is null.")
print("  -> essentially the ENTIRE causal effect on the depression SCALE is the scale")
print("     re-measuring the exposure. Independently replicated by berger2026_start in the")
print("     same cohort by difference-in-differences, and predicted by talbot2010's authors")
print("     ('The POMS may indicate greater mood disturbance in part because some of its")
print("     scales overlap with sleepiness, such as fatigue and vigor').")

print()
print("=" * 78)
print("SYNTHESIS: absolute risk arithmetic for an 18-19 y MALE")
print("=" * 78)
# base rates
mde_all_1825 = 0.172          # goodwin2022, NSDUH 2020, combined sex
suicide_m_15_19 = 17.3e-5     # cdc, per year
suicide_m_20_24 = 27.9e-5
print(f"  base rate past-year MDE, 18-25, combined sex : {mde_all_1825:.3f}")
print("  male-specific rate NOT quotable from my sources; direction is lower.")
print("  working male range used below: 0.09 to 0.12")
print(f"  base suicide mortality, male 15-19 : {suicide_m_15_19*1e5:.1f} /100k/y")
print(f"  base suicide mortality, male 20-24 : {suicide_m_20_24*1e5:.1f} /100k/y")

print()
print("  DEPRESSION, absolute excess under three candidate causal ORs:")
for label, orv in (("null continuous-duration MR (sun2022)", 1.00),
                   ("genetic short sleep (zhang2024_mr)", 1.179),
                   ("quasi-experiment (gangwisch2010)", 1.24),
                   ("naive observational (short2020 adj)", 1.28)):
    for base in (0.09, 0.12):
        # convert OR to approximate risk ratio at this base rate
        odds = base / (1 - base)
        new_odds = odds * orv
        new_risk = new_odds / (1 + new_odds)
        if base == 0.09:
            lo = new_risk - base
        else:
            hi = new_risk - base
    print(f"    {label:<38} OR={orv:.3f}  excess = {lo*100:+.2f} to {hi*100:+.2f} pp")

print()
print("  SUICIDE MORTALITY, absolute excess (applying an IDEATION OR to a death rate,")
print("  which OVERSTATES it -- wang2024 shows RR shrinks from 2.01 ideation to 1.52")
print("  medically-treated attempt, so the OR for death is likely well below these):")
base = 20e-5
for label, orv in (("quasi-experiment ideation OR (gangwisch2010)", 1.20),
                   ("YRBS adjusted attempt aOR (wang2024)", 1.24)):
    excess = base * (orv - 1)
    print(f"    {label:<44} +{excess*1e5:.1f} /100k/y  "
          f"= 1 extra death per {1/excess:,.0f} exposed per year")
    print(f"        over 3 years of exposure: ~1 per {1/(excess*3):,.0f}")
