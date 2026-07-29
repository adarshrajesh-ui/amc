#!/usr/bin/env python3
"""Conversion arithmetic for shard s18_comparators.

Turns published life-expectancy / hazard-ratio estimates for SUSTAINED lifelong
exposures into "3 years of exposure beginning at age 16" figures, under the two
bounding assumptions the modeller has to choose between.

Life table: /workspace/data/lifetable_us_male_full.csv (built by s17_baseline_risk
from NCHS United States life tables 2023, males; gate G10 calibrated).

Run:  python3 convert.py
"""
import csv
import os

LT = os.path.join(os.path.dirname(__file__), "..", "..", "data", "lifetable_us_male_full.csv")


def load_qx(path=LT):
    qx = {}
    with open(path) as fh:
        for row in csv.DictReader(l for l in fh if not l.startswith("#")):
            qx[int(row["age"])] = float(row["qx"])
    return qx


def ex_at(qx, start):
    """Expectation of life at exact age `start` from a dict of single-year qx.

    Standard recursion, half-year assumption for deaths within the year, closed
    with qx = 1 at the top age. Reproduces the published NCHS ex to <1e-3 y when
    given the unmodified table.
    """
    ages = sorted(a for a in qx if a >= start)
    lx, T = 1.0, 0.0
    for a in ages:
        q = min(max(qx[a], 0.0), 1.0)
        d = lx * q
        T += lx - 0.5 * d
        lx -= d
        if lx <= 1e-15:
            break
    return T


def loss_window(hr, start=16, n_years=3, base_age=16):
    """Bound L: hazard multiplied by `hr` for `n_years` only, then back to baseline."""
    qx = load_qx()
    mod = dict(qx)
    for a in range(start, start + n_years):
        mod[a] = min(qx[a] * hr, 1.0)
    return ex_at(qx, base_age) - ex_at(mod, base_age)


def loss_permanent(hr, start=16, base_age=16):
    """Bound U: hazard multiplied by `hr` from `start` for the whole of the rest of life."""
    qx = load_qx()
    mod = {a: (min(q * hr, 1.0) if a >= start else q) for a, q in qx.items()}
    return ex_at(qx, base_age) - ex_at(mod, base_age)


def hr_for_target_loss(target_years, start=40, base_age=40, lo=1.0, hi=20.0):
    """Invert loss_permanent: what lifelong HR from `start` costs `target_years`?"""
    for _ in range(200):
        mid = (lo + hi) / 2
        if loss_permanent(mid, start=start, base_age=base_age) < target_years:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def prorata(published_loss_years, exposure_years_in_published, n_years=3):
    """Cumulative-dose attribution: published lifetime loss shared equally per exposure-year."""
    return published_loss_years * n_years / exposure_years_in_published


if __name__ == "__main__":
    qx = load_qx()
    print("=== life table calibration ===")
    for a in (0, 16, 19, 40, 65):
        print(f"  e({a:>2}) = {ex_at(qx, a):8.4f}")

    print("\n=== cumulative mortality risk over the 3-year window, ages 16-18, US male 2023 ===")
    surv = 1.0
    for a in (16, 17, 18):
        surv *= (1 - qx[a])
    print(f"  P(die between 16 and 19) = {1-surv:.6f}  ({(1-surv)*1e5:.1f} per 100,000)")

    print("\n=== BOUND L: hazard x HR for ages 16,17,18 only, then baseline (fully reversible) ===")
    print("    HR      LE lost at 16 (years)   (days)")
    for hr in (1.1, 1.2, 1.5, 2.0, 2.96, 3.0, 5.0, 10.0):
        L = loss_window(hr)
        print(f"  {hr:5.2f}   {L:18.5f}   {L*365.25:8.2f}")

    print("\n=== BOUND U: hazard x HR from age 16 for life (permanent shift) ===")
    print("    HR      LE lost at 16 (years)")
    for hr in (1.1, 1.2, 1.29, 1.39, 1.45, 2.0, 2.76, 2.96, 3.0):
        print(f"  {hr:5.2f}   {loss_permanent(hr):18.3f}")

    print("\n=== HR -> years-of-life-lost calibration, hazard x HR from age 40 for life ===")
    print("    HR    LE lost at 40 (y)   published anchor")
    anchors = {
        2.96: "Banks 2015 current smoker vs never (RR 2.96) <-> 'die on average 10 years earlier'",
        2.76: "Global BMI 2016 obesity grade 3 (HR 2.76) <-> PSC 2009 'BMI 40-45: 8-10 y'",
        1.45: "Global BMI 2016 obesity grade 1 (HR 1.45) <-> PSC 2009 'BMI 30-35: 2-4 y'",
        1.29: "PSC 2009 per +5 kg/m2 (HR 1.29)",
        1.20: "Global BMI 2016 BMI 27.5-30 (HR 1.20)",
        1.12: "Cappuccio 2010 short sleep all-cause (RR 1.12)",
    }
    for hr in sorted(anchors, reverse=True):
        print(f"  {hr:5.2f}   {loss_permanent(hr, start=40, base_age=40):10.3f}        {anchors[hr]}")

    print("\n  Implied linear rule of thumb, sustained-from-40 hazard ratio:")
    for hr in (1.12, 1.29, 1.45, 2.0, 2.96):
        L = loss_permanent(hr, start=40, base_age=40)
        import math
        print(f"    HR {hr:5.2f}:  YLL {L:6.3f} y   YLL/ln(HR) = {L/math.log(hr):6.2f}")

    print("\n=== inverse check: HR from age 40 needed to lose N years ===")
    for tgt in (0.5, 1.5, 3.0, 4.5, 9.0, 10.0):
        print(f"  {tgt:5.2f} y  <->  HR {hr_for_target_loss(tgt):6.3f}")

    print("\n=== CUMULATIVE-DOSE (pro-rata) conversions, 3 years of exposure ===")
    cases = [
        ("Smoking 15.8 cig/d, Jackson 2025 per-cigarette route (male, 17 min/cig)",
         None, None, 15.8 * 365.25 * 3 * 17 / (60 * 24 * 365.25)),
        ("Smoking 20 cig/d, Jackson 2025 per-cigarette route (male, 17 min/cig)",
         None, None, 20 * 365.25 * 3 * 17 / (60 * 24 * 365.25)),
        ("Smoking 10 cig/d, Jackson 2025 per-cigarette route (male, 17 min/cig)",
         None, None, 10 * 365.25 * 3 * 17 / (60 * 24 * 365.25)),
        ("Smoking, Doll 2004 10 y over 54 exposure-years (age 17-71, Jackson's base)",
         10.0, 54.0, None),
        ("Overweight BMI 25-30, Peeters 2003 3.1 y over e(40)=38.6 exposure-years",
         3.1, 38.6, None),
        ("Obesity BMI 30-35, PSC 2009 midpoint 3 y over e(46)~34 exposure-years",
         3.0, 34.0, None),
        ("Inactive 0 MET-h/wk, Moore 2012 3.4 y over e(40)=38.6 exposure-years",
         3.4, 38.6, None),
        ("Alcohol 100-200 g/wk, Wood 2018 0.5 y over e(40)=38.6",
         0.5, 38.6, None),
        ("Alcohol 200-350 g/wk, Wood 2018 1.5 y over e(40)=38.6",
         1.5, 38.6, None),
        ("Alcohol >350 g/wk, Wood 2018 4.5 y over e(40)=38.6",
         4.5, 38.6, None),
        ("Typical Western diet, Fadnes 2022 optimal-diet gain 13.0 y from age 20 over e(20)=56.7",
         13.0, 56.7, None),
        ("Typical Western diet, Fadnes 2022 feasibility gain 7.3 y from age 20 over e(20)=56.7",
         7.3, 56.7, None),
    ]
    for label, loss, expo, direct in cases:
        v = direct if direct is not None else prorata(loss, expo)
        print(f"  {v:6.3f} y ({v*12:5.2f} mo)  {label}")

    print("\n=== DELAYED-CESSATION conversion from Fadnes 2022 age gradient (US males) ===")
    g20, g60, g80 = 13.0, 8.8, 3.4
    print(f"  gain switching at 20 = {g20} y; at 60 = {g60} y; at 80 = {g80} y")
    print(f"  loss per year of delay, 20->60: {(g20-g60)/40:.4f} y/y  -> 3 y = {(g20-g60)/40*3:.3f} y")
    print(f"  loss per year of delay, 60->80: {(g60-g80)/20:.4f} y/y  -> 3 y = {(g60-g80)/20*3:.3f} y")
    print("  (rises steeply with age: the marginal cost of a year of bad diet at 16-19")
    print("   is the SMALLEST of any age, so 3 y/40 y x 4.2 y OVERSTATES it)")

    print("\n=== MODEL P as an explicit permanent hazard shift from age 19 ===")
    print("  Because YLL is almost exactly linear in ln(HR) (10.85 y per unit, see above),")
    print("  pro-rating a published LE loss by 3/E is equivalent to applying a PERMANENT")
    print("  hazard ratio of HR_pub**(3/E) from the end of exposure. Modeller-ready form:")
    print("    exposure                                    E     HR_pub  HR_perm  LE lost at 16")
    pmodel = [
        ("smoking 20 cig/d", 54.0, 2.96),
        ("smoking 10 cig/d", 54.0, 1.98),
        ("BMI 27.5 vs 22.5 (overweight)", 38.6, 1.20),
        ("BMI 32 vs 22.5 (obesity gr 1)", 34.0, 1.45),
        ("inactive 0 MET-h/wk vs >=7.5", 38.6, 1.35),
        ("alcohol 100-200 g/wk", 38.6, 1.047),
        ("alcohol >350 g/wk", 38.6, 1.514),
        ("typical Western vs optimal diet", 56.7, 1.318),
    ]
    for label, E, hrpub in pmodel:
        hrp = hrpub ** (3.0 / E)
        L = loss_permanent(hrp, start=19, base_age=16)
        print(f"    {label:42s} {E:5.1f}  {hrpub:6.3f}  {hrp:7.4f}  {L:6.3f} y ({L*12:5.2f} mo)")

    print("\n=== CALIBRATION of the life-table engine against published YLL ===")
    print("  computed / published, hazard applied from 40 for life:")
    checks = [
        ("Banks 2015 smoker RR 2.96 vs 'die 10 y earlier'", 2.96, 10.0),
        ("PSC 2009 BMI 40-45 (HR 2.76) vs '8-10 y'", 2.76, 9.0),
        ("PSC 2009 BMI 30-35 (HR 1.45) vs '2-4 y'", 1.45, 3.0),
        ("Wood 2018 >350 g/wk vs '4-5 y' at 40", 1.514, 4.5),
    ]
    ratios = []
    for label, hr, pub in checks:
        c = loss_permanent(hr, start=40, base_age=40)
        ratios.append(c / pub)
        print(f"    {label:52s} computed {c:6.2f} / published {pub:4.1f} = {c/pub:5.2f}")
    print(f"  mean ratio = {sum(ratios)/len(ratios):.2f}  -> the raw life-table engine runs "
          f"~{(sum(ratios)/len(ratios)-1)*100:.0f}% HOT")
    print("  RECOMMENDED: multiply life-table-derived YLL by 0.80 to match the published")
    print("  literature, or (preferred) use the published YLL directly and pro-rate it.")

    print("\n=== ALCOHOL: acute-injury channel over the 16-18 window (does NOT pro-rate) ===")
    paf = 0.122
    hr_pop = 1 / (1 - paf)
    Lpop = loss_window(hr_pop)
    print(f"  GBD 2016: PAF for alcohol, MALE deaths ages 15-49 = {paf:.3f}")
    print(f"  population-average implied HR over the window = 1/(1-PAF) = {hr_pop:.4f}")
    print(f"  -> LE lost at 16, average male:               {Lpop:.4f} y = {Lpop*365.25:.1f} days")
    print("  for an INDIVIDUAL heavy drinker the HR is several-fold higher; sensitivity:")
    for hr in (1.5, 2.0, 2.5, 3.0):
        L = loss_window(hr)
        print(f"    HR {hr:4.2f} over ages 16-18 -> {L:.4f} y = {L*365.25:5.1f} days")
    print("  NOTE these injury deaths are CONCENTRATED at 16-24; unlike every other")
    print("  comparator, alcohol's window term is larger than its pro-rata chronic term.")

    print("\n=== ADOLESCENT-EXPOSURE 'permanent mark' upper bounds (age-matched cohorts) ===")
    for label, hr in [
        ("Hogstrom 2016 fitness at 18, bottom vs top fifth (1/0.49)", 1 / 0.49),
        ("Twig 2016 adolescent BMI >=95th pct, CV death (HR 3.5)", 3.5),
        ("Twig 2016 adolescent BMI, CV death at 30-40 y follow-up (HR 4.1)", 4.1),
    ]:
        L = loss_permanent(hr, start=19, base_age=16)
        print(f"  {label:62s} HR {hr:5.2f} -> {L:6.2f} y")
    print("  THESE ARE NOT 3-YEAR-EXPOSURE EFFECTS. Adolescent fitness and BMI track")
    print("  strongly into midlife, so these HRs price a LIFELONG trajectory, not a")
    print("  3-year window. They bound the 'irreversible developmental insult' story only.")

    print("\n=== SMOKING: realised loss after cessation at 19 (Pirie 2013 / Jha 2013) ===")
    print("  Pirie 2013: continuing smokers RR 2.76 (excess 176%);")
    print("              stopped at 25-34 RR 1.05 (excess 5%)  -> residual = 5/176 = "
          f"{5/176*100:.1f}% of the excess")
    print(f"              applied to an 11 y lifespan gap  -> {11*5/176:.2f} y")
    print("  Pirie 2013: 'stopping before age 30 years avoids more than 97% of it'")
    print(f"              -> residual <= 3% of 10-11 y = {0.03*10:.2f}-{0.03*11:.2f} y")
    print("  Jha 2013:   'Cessation before the age of 40 years reduces the risk of death")
    print("               associated with continued smoking by about 90%' -> residual <= 10%")
    print(f"              of 10 y = {0.10*10:.2f} y for a WHOLE young-adult smoking career")
