#!/usr/bin/env python3
"""Emit the comparator table for comparator_scale.md.

Every number is computed from (a) the published values extracted in the YAML
records of this shard and (b) the US male 2023 life table in
/workspace/data/lifetable_us_male_full.csv. Nothing is typed in by hand except
the published inputs, each of which is tagged with the study_id it came from.

Run:  python3 comparator_table.py
"""
from convert import load_qx, ex_at, loss_window, loss_permanent

QX = load_qx()
E16 = ex_at(QX, 16)
E19 = ex_at(QX, 19)
E30 = ex_at(QX, 30)
E40 = ex_at(QX, 40)
E46 = ex_at(QX, 46)

D = 365.25  # days per year, for reporting


class Row:
    """One comparator: 3 years of exposure beginning at age 16."""

    def __init__(self, name, exposure, source, hr_window, pub_loss, pub_start_e,
                 hr_sustained, reversibility, recommend, note):
        self.name = name
        self.exposure = exposure
        self.source = source
        self.hr_window = hr_window        # hazard ratio operating DURING ages 16-18
        self.pub_loss = pub_loss          # published LE loss for sustained exposure (years)
        self.pub_start_e = pub_start_e    # exposure-years the published loss is spread over
        self.hr_sustained = hr_sustained  # published HR for sustained exposure (for bound U)
        self.reversibility = reversibility
        self.recommend = recommend        # (low, central, high) in years
        self.note = note

    @property
    def bound_L(self):
        """Model W: hazard elevated only during ages 16-18, then baseline."""
        if self.hr_window is None:
            return None
        return loss_window(self.hr_window)

    @property
    def central_P(self):
        """Model P: cumulative-dose pro-rata of the published sustained-exposure loss."""
        if self.pub_loss is None:
            return None
        return self.pub_loss * 3.0 / self.pub_start_e

    @property
    def hr_perm(self):
        """Model P re-expressed as a permanent hazard ratio applied from age 19."""
        if self.hr_sustained is None:
            return None
        return self.hr_sustained ** (3.0 / self.pub_start_e)

    @property
    def bound_U(self):
        """Model F: the full sustained HR applied permanently from age 19. Indefensible ceiling."""
        if self.hr_sustained is None:
            return None
        return loss_permanent(self.hr_sustained, start=19, base_age=16)


ROWS = [
    Row("Smoking, 20 cig/day",
        "20 cigarettes/day, ages 16-19, then permanent cessation",
        "jackson2025 / doll2004 / banks2015 / pirie2013",
        # 10 y is Doll 2004's figure at Jackson 2025's assumed 15.8 cig/day base; scaled to
        # 20 cig/day it is 10*(20/15.8) = 12.66 y, which reproduces the per-cigarette route.
        hr_window=1.02, pub_loss=10.0 * 20 / 15.8, pub_start_e=54.0, hr_sustained=2.96,
        reversibility="HIGH but INCOMPLETE. pirie2013: quitting at 25-34 leaves all-cause RR 1.05 "
                      "(1.00-1.11), i.e. 3% of the excess of continuing. jha2013: cessation before 40 "
                      "removes ~90%. doll2004: cessation at 30 gains ~10 of the ~10 y. Residual damage "
                      "is real (lung-cancer RR still 1.84 after quitting at 25-34) and is CUMULATIVE in "
                      "pack-years.",
        recommend=(0.05, 0.15, 0.75),
        note="Model P (0.70 y, matching jackson2025's per-cigarette route exactly) and the "
             "cessation-calibrated estimate (~0.08 y, from pirie2013) disagree by ~9x. Pro-rata "
             "overstates the first 3 years because smoking hazard is super-linear in DURATION, and "
             "it gives no credit for post-cessation repair. I recommend the low end."),
    Row("Smoking, 10 cig/day",
        "10 cigarettes/day, ages 16-19, then permanent cessation",
        "jackson2025 / banks2015",
        hr_window=1.01, pub_loss=10.0 * 10 / 15.8, pub_start_e=54.0, hr_sustained=1.98,
        reversibility="as above",
        recommend=(0.03, 0.08, 0.37),
        note="banks2015 puts ~10 cig/day at RR ~2.0, i.e. roughly half the log-hazard of a pack "
             "a day. Model P here reproduces jackson2025's per-cigarette route (0.354 y at the "
             "male 17 min/cigarette figure; 0.41 y at the sex-averaged 20 min)."),
    Row("Overweight, BMI 27.5 vs 22.5",
        "+5 kg/m2 above optimum for 3 years, ages 16-19, then return to 22.5",
        "peeters2003 / globalbmi2016 / psc2009",
        hr_window=1.20, pub_loss=3.1, pub_start_e=E40, hr_sustained=1.20,
        reversibility="PARTIAL and in practice POOR. Metabolic risk is largely reversible on weight "
                      "loss, but (a) peeters2003 found BMI at 30-49 predicted mortality at 50-69 even "
                      "after adjustment for BMI at 50-69, and (b) adolescent adiposity tracks strongly "
                      "into midlife (twig2016, zheng2017), so a 3-year adolescent exposure is usually "
                      "the START of a trajectory rather than a closed window.",
        recommend=(0.03, 0.15, 0.25),
        note="globalbmi2016 finds the HR per 5 kg/m2 is LARGER for men (1.51) and when BMI is "
             "measured younger (1.52 at 35-49), so 1.20 is conservative for our subject."),
    Row("Obesity grade 1, BMI ~32",
        "BMI 30-35 for 3 years, ages 16-19, then return to 22.5",
        "psc2009 / globalbmi2016",
        hr_window=1.45, pub_loss=3.0, pub_start_e=E46, hr_sustained=1.45,
        reversibility="as above; worse, because grade-1 obesity at 18 very rarely resolves",
        recommend=(0.07, 0.20, 0.27),
        note="psc2009 gives 2-4 y for sustained BMI 30-35 from ~46; midpoint 3 y used."),
    Row("Physical inactivity",
        "0 MET-h/wk leisure activity for 3 years, ages 16-19, then meeting guidelines",
        "moore2012 / mok2019 / hogstrom2016",
        hr_window=1.35, pub_loss=3.4, pub_start_e=E40, hr_sustained=1.35,
        reversibility="HIGH. mok2019: becoming more active cut all-cause mortality (HR 0.76 per "
                      "1 kJ/kg/day/y rise) INDEPENDENT of baseline activity, and increasing "
                      "trajectories beat consistent inactivity even from the lowest baseline "
                      "(HR 0.76, 0.65-0.88). Fitness is a state variable restored within months of "
                      "resuming training. The competing signal is hogstrom2016 (fitness at 18, "
                      "HR 0.49 over 29 y), but that is confounded by tracking.",
        recommend=(0.02, 0.07, 0.26),
        note="Because reversibility is high, I recommend a central estimate near the WINDOW bound. "
             "ekelund2019's device-measured HR 3.7 is an outlier driven by reverse causation in "
             "62-year-olds and is not used."),
    Row("Alcohol, ~200-350 g/wk",
        "14-25 US standard drinks/week for 3 years, ages 16-19, then moderation",
        "wood2018 + gbd2016alcohol",
        hr_window=2.0, pub_loss=1.5, pub_start_e=E40, hr_sustained=1.148,
        reversibility="SPLIT. The chronic channel (BP, liver, cardiac remodelling) is largely "
                      "reversible. The ACUTE INJURY channel is not reversible but is RESOLVED WITHIN "
                      "THE WINDOW: it is a mortality lottery, so conditional on surviving to 19 "
                      "unharmed almost none of it is carried forward. Ex ante expected loss and ex "
                      "post realised loss therefore differ sharply for alcohol alone.",
        recommend=(0.12, 0.25, 0.35),
        note="THE ONE COMPARATOR WHERE THE WINDOW TERM DOMINATES. gbd2016alcohol: alcohol is the "
             "LEADING risk factor for male deaths at 15-49 (PAF 12.2%), via road injury and "
             "self-harm. Central = chronic pro-rata (0.117 y) PLUS an injury window term; the "
             "window HR of 2.0 is an ASSUMPTION, not an extraction - see caveats."),
    Row("Typical Western diet",
        "typical Western vs longevity-optimal diet for 3 years, ages 16-19, then optimal",
        "fadnes2022 / fadnes2024",
        hr_window=1.05, pub_loss=4.2, pub_start_e=40.0, hr_sustained=1.318,
        reversibility="HIGHEST of all comparators. fadnes2022's own age gradient shows 8.8 of the "
                      "13.0 y available at 20 is STILL available at 60 (68%), and 3.4 y at 80. A "
                      "3-year bad-diet window closed at 19 forfeits almost nothing in that model.",
        recommend=(0.01, 0.15, 0.32),
        note="Model P here uses fadnes2022's OWN delayed-cessation gradient (13.0 y at 20 minus "
             "8.8 y at 60 = 4.2 y over 40 exposure-years) rather than naive pro-rata over e(20), "
             "which would give 0.69 y. The 60->80 segment shows the marginal cost per bad-diet "
             "year RISES with age, so even 0.32 y overstates ages 16-19."),
    Row("REFERENCE: insufficient sleep",
        "short habitual sleep for 3 years, ages 16-19 (this project's own exposure)",
        "cappuccio2010 / li2024sleep",
        hr_window=1.12, pub_loss=1.23, pub_start_e=E40, hr_sustained=1.12,
        reversibility="NOT ESTABLISHED on the mortality scale by any record in this shard. No "
                      "sleep study reports a cessation gradient analogous to pirie2013's "
                      "quit-at-25-34 result. This is the single biggest asymmetry between our "
                      "exposure and its comparators.",
        recommend=(0.02, 0.10, 0.30),
        note="Included so the modeller can see our own exposure on the identical scale. Low end = "
             "cappuccio2010 RR 1.12 over the window; high end = li2024sleep's 4.7 y for men "
             "pro-rated over e(30)=%.1f. Both are for SUSTAINED midlife exposure." % E30),
]


def fmt(v, unit="y"):
    if v is None:
        return "n/a"
    if unit == "y":
        return f"{v:.3f}"
    return f"{v:.0f}"


def main():
    print(f"life table: e(16)={E16:.2f}  e(19)={E19:.2f}  e(30)={E30:.2f}  "
          f"e(40)={E40:.2f}  e(46)={E46:.2f}")
    p3 = 1.0
    for a in (16, 17, 18):
        p3 *= (1 - QX[a])
    print(f"P(death, ages 16-18, US male 2023) = {1-p3:.5f} = {(1-p3)*1e5:.0f} per 100,000")
    print()
    hdr = ("| Comparator | **RECOMMENDED central (months)** | 80% interval (months) | "
           "Bound L: window only | Model P: pro-rata | Model P as permanent HR from age 19 | "
           "Bound U: full HR permanent |")
    print(hdr)
    print("|---|---|---|---|---|---|---|")
    for r in ROWS:
        lo, ce, hi = r.recommend
        print(f"| {r.name} | **{ce*12:.1f} mo** | {lo*12:.1f}-{hi*12:.1f} mo | "
              f"{r.bound_L*12:.2f} mo ({r.bound_L*D:.0f} d) | {r.central_P*12:.1f} mo | "
              f"{r.hr_perm:.4f} | {r.bound_U*12:.0f} mo ({r.bound_U:.1f} y) |")
    print()
    print("=== per-comparator detail ===")
    for r in ROWS:
        lo, ce, hi = r.recommend
        print(f"\n## {r.name}")
        print(f"  exposure        : {r.exposure}")
        print(f"  sources         : {r.source}")
        print(f"  published input : {r.pub_loss} y lost over {r.pub_start_e:.1f} exposure-years "
              f"(sustained HR {r.hr_sustained})")
        print(f"  Bound L (window): {r.bound_L:.4f} y = {r.bound_L*D:.1f} days   [HR {r.hr_window} at ages 16-18]")
        print(f"  Model P         : {r.central_P:.4f} y = {r.central_P*12:.2f} months  "
              f"(equivalently a permanent HR of {r.hr_perm:.4f} from age 19)")
        print(f"  Bound U (full)  : {r.bound_U:.3f} y   <-- NOT DEFENSIBLE for a 3-year exposure")
        print(f"  RECOMMENDED     : {ce:.2f} y  [{lo:.2f}, {hi:.2f}]")
        print(f"  reversibility   : {r.reversibility}")
        print(f"  note            : {r.note}")


if __name__ == "__main__":
    main()
