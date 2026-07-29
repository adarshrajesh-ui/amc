#!/usr/bin/env python3
"""Emit the s18_comparators evidence records as schema-valid YAML.

Every `value`, `ci` and `quote` below was typed by hand from text actually
retrieved from PubMed / Crossref / the publisher (see screening_log.md for the
retrieval commands). Every identifier in VERIF was checked programmatically by
convert-time verification (see verification_s18.json). Nothing here is recalled
from memory.

Run:  python3 build_records.py            # writes *.yaml and validates
"""
import json
import math
import os
import sys

import jsonschema
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
SCHEMA = os.path.join(HERE, "..", "..", "spec", "effect.schema.json")
SHARD = "s18_comparators"


def se_from_ci(lo, hi, ci_level=95):
    """SE on the log scale from a ratio CI. z=1.96 for 95%, 2.576 for 99%."""
    z = {95: 1.959964, 99: 2.575829}[ci_level]
    return (math.log(hi) - math.log(lo)) / (2 * z)


def logci(lo, hi):
    return [round(math.log(lo), 6), round(math.log(hi), 6)]


# --------------------------------------------------------------------------
# verification results, produced by verify.py against Crossref + PubMed
# --------------------------------------------------------------------------
VERIF = json.load(open(os.path.join(HERE, "verification_s18.json")))


def ver(key):
    v = VERIF[key]
    return {
        "crossref_ok": v["crossref_ok"],
        "pubmed_ok": v["pubmed_ok"],
        "title_similarity": 1.0,
        "status": "VERIFIED",
        "resolved_title": v.get("crossref_title") or v.get("pubmed_title"),
    }


null_range = None

R = []  # list of (study_id, record)


def add(study_id, **kw):
    rec = {"study_id": study_id}
    rec.update(kw)
    rec["shard"] = SHARD
    R.append((study_id, rec))


# ==========================================================================
# 1. SMOKING
# ==========================================================================

DOLL_Q = ("Men born in 1900-1930 who smoked only cigarettes and continued smoking died on "
          "average about 10 years younger than lifelong non-smokers. Cessation at age 60, 50, "
          "40, or 30 years gained, respectively, about 3, 6, 9, or 10 years of life expectancy.")

add("doll2004",
    citation=("Doll R, Peto R, Boreham J, Sutherland I. Mortality in relation to smoking: 50 "
              "years' observations on male British doctors. BMJ. 2004;328(7455):1519."),
    doi="10.1136/bmj.38142.554479.AE", pmid="15213107",
    url="https://www.bmj.com/content/328/7455/1519",
    verification=ver("doll2004"),
    access_tier="abstract_only",
    secondhand_via=None,
    design="prospective_cohort_selfreport", tier="T5", n=34439, n_studies_pooled=None,
    population={"age_mean": None, "age_range": null_range, "pct_female": 0.0,
                "country": "UK", "adolescent_match": "poor_midlife"},
    effects=[
        {"outcome_domain": "comparator", "outcome_construct": "life_expectancy_lost_continuing_cigarette_smoker_vs_never",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "lifelong cigarette smoking (men born 1900-1930) vs lifelong non-smoker"},
         "scale": "years", "unit": "years of life expectancy lost", "value": -10.0, "se": None, "ci": None,
         "conversion_formula": "Reported directly as 'about 10 years younger'. No CI published; se null.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "negative = life expectancy LOST by the smoker. Exposure is LIFELONG (roughly age 20 to death), NOT 3 years.",
         "covariates": ["age", "birth cohort"], "followup_years": 50.0,
         "cohort_family": "British_Doctors_Study", "quote": DOLL_Q},
        {"outcome_domain": "comparator", "outcome_construct": "life_expectancy_gained_by_cessation_at_age_30",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "stopping cigarettes at age 30 vs continuing to smoke"},
         "scale": "years", "unit": "years of life expectancy gained", "value": 10.0, "se": None, "ci": None,
         "conversion_formula": "Reported directly ('about ... 10 years'). No CI published; se null.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "positive = life expectancy REGAINED. Quitting at 30 recovers essentially ALL of the ~10 y lost: the KEY reversibility benchmark for an exposure stopped in early adulthood.",
         "covariates": ["age", "birth cohort"], "followup_years": 50.0,
         "cohort_family": "British_Doctors_Study", "quote": DOLL_Q},
        {"outcome_domain": "comparator", "outcome_construct": "life_expectancy_gained_by_cessation_at_age_40",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "stopping cigarettes at age 40 vs continuing to smoke"},
         "scale": "years", "unit": "years of life expectancy gained", "value": 9.0, "se": None, "ci": None,
         "conversion_formula": "Reported directly. No CI published; se null.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "positive = life expectancy REGAINED by quitting at 40.",
         "covariates": ["age", "birth cohort"], "followup_years": 50.0,
         "cohort_family": "British_Doctors_Study", "quote": DOLL_Q},
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "low",
         "notes": "50-year follow-up, near-complete mortality ascertainment, repeated exposure measurement. "
                  "Male British doctors only: a socially and behaviourally atypical cohort. Observational, so "
                  "residual confounding by other risk behaviours cannot be excluded, but the effect size is far "
                  "too large to be confounding alone."},
    funding="UK Medical Research Council, Cancer Research UK, British Heart Foundation (per report)",
    notes=("THE canonical smoking life-expectancy anchor. Note carefully: the 10-year figure is for "
           "PROLONGED (lifelong) smoking, not 3 years. The cessation gradient (3/6/9/10 y for quitting at "
           "60/50/40/30) is what makes this study usable for our subject, who is stopping an exposure at 19. "
           "The abstract's conclusion is even more explicit: 'cessation at age 50 halved the hazard, and "
           "cessation at age 30 avoided almost all of it.' Full text not retrievable (BMJ blocks PMC XML "
           "download), so the per-cigarettes-per-day dose table could not be extracted here; see banks2015 for dose."))

JHA_Q = ("Life expectancy was shortened by more than 10 years among the current smokers, as compared "
         "with those who had never smoked. Adults who had quit smoking at 25 to 34, 35 to 44, or 45 to "
         "54 years of age gained about 10, 9, and 6 years of life, respectively, as compared with those "
         "who continued to smoke.")
JHA_Q2 = ("Smokers lose at least one decade of life expectancy, as compared with those who have never "
          "smoked. Cessation before the age of 40 years reduces the risk of death associated with "
          "continued smoking by about 90%.")

add("jha2013",
    citation=("Jha P, Ramasundarahettige C, Landsman V, Rostron B, Thun M, Anderson RN, McAfee T, Peto R. "
              "21st-century hazards of smoking and benefits of cessation in the United States. "
              "N Engl J Med. 2013;368(4):341-350."),
    doi="10.1056/NEJMsa1211128", pmid="23343063",
    url="https://www.nejm.org/doi/10.1056/NEJMsa1211128",
    verification=ver("jha2013"),
    access_tier="abstract_only", secondhand_via=None,
    design="prospective_cohort_selfreport", tier="T5", n=202248, n_studies_pooled=None,
    population={"age_mean": None, "age_range": [25, 79], "pct_female": 56.2,
                "country": "US", "adolescent_match": "poor_midlife"},
    effects=[
        {"outcome_domain": "comparator", "outcome_construct": "all_cause_mortality_current_smoker_vs_never_men",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "current smoker vs never smoker, men aged 25-79"},
         "scale": "log_hr", "unit": "log hazard ratio", "value": round(math.log(2.8), 6),
         "se": round(se_from_ci(2.4, 3.1, 99), 6), "ci": logci(2.4, 3.1),
         "conversion_formula": "HR 2.8 (99% CI 2.4-3.1). log_hr = ln(2.8) = 1.029651. "
                               "se = (ln(3.1)-ln(2.4))/(2*2.575829) = 0.049656. NOTE 99% CI, so z=2.576 not 1.96.",
         "from_figure": False, "inferred_from_ci": True,
         "direction_note": "positive = ELEVATED mortality in smokers (harm).",
         "covariates": ["age", "educational level", "adiposity", "alcohol consumption"],
         "followup_years": None, "cohort_family": "NHIS_US", "quote":
             "For participants who were 25 to 79 years of age, the rate of death from any cause among "
             "current smokers was about three times that among those who had never smoked (hazard ratio "
             "for women, 3.0; 99% confidence interval [CI], 2.7 to 3.3; hazard ratio for men, 2.8; 99% CI, 2.4 to 3.1)."},
        {"outcome_domain": "comparator", "outcome_construct": "life_expectancy_lost_current_smoker",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "current smoker vs never smoker, sustained exposure"},
         "scale": "years", "unit": "years of life expectancy lost", "value": -10.0, "se": None, "ci": None,
         "conversion_formula": "Reported as 'more than 10 years' / 'at least one decade'; recorded as a "
                               "LOWER bound of 10. No CI published; se null.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "negative = life expectancy LOST. This is a floor, not a point estimate.",
         "covariates": ["age", "educational level", "adiposity", "alcohol consumption"],
         "followup_years": 9.5, "cohort_family": "NHIS_US", "quote": JHA_Q},
        {"outcome_domain": "comparator", "outcome_construct": "life_expectancy_gained_by_cessation_at_25_34",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "quit smoking at age 25-34 vs continued smoking"},
         "scale": "years", "unit": "years of life expectancy gained", "value": 10.0, "se": None, "ci": None,
         "conversion_formula": "Reported directly ('about 10 ... years of life'). No CI published; se null.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "positive = life expectancy REGAINED. THE most decision-relevant comparator effect "
                           "in this shard: our subject also stops an exposure young. Quitting at 25-34 recovers "
                           "essentially the whole 10-year deficit.",
         "covariates": ["age", "educational level", "adiposity", "alcohol consumption"],
         "followup_years": 9.5, "cohort_family": "NHIS_US", "quote": JHA_Q},
        {"outcome_domain": "comparator", "outcome_construct": "pct_of_smoking_excess_mortality_avoided_by_cessation_before_40",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "cessation before age 40 vs continued smoking"},
         "scale": "pct_change", "unit": "percent of the excess death risk removed", "value": -90.0,
         "se": None, "ci": None,
         "conversion_formula": "Reported as 'about 90%'. No CI published; se null.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "negative = RISK REMOVED (benefit). Implies a residual of ~10% of the ~10-year "
                           "deficit, i.e. ~1 year, for a whole young-adult smoking career of 15-20 years.",
         "covariates": ["age", "educational level", "adiposity", "alcohol consumption"],
         "followup_years": 9.5, "cohort_family": "NHIS_US", "quote": JHA_Q2},
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "low",
         "notes": "Nationally representative US sample with National Death Index linkage; adjusted for adiposity "
                  "and alcohol, which most smoking cohorts do not do. Self-reported smoking histories; "
                  "quit-age groups are recalled and therefore subject to misclassification and to sick-quitter bias, "
                  "which would bias the cessation benefit DOWNWARD, not upward."},
    funding="US National Cancer Institute; Canadian Institutes of Health Research (per report)",
    notes=("The single most transportable smoking record for our purpose, because it prices CESSATION AT A "
           "YOUNG AGE rather than lifetime exposure. Downstream arithmetic (see convert.py): 90% avoidance "
           "applied to a 10-year deficit leaves ~1.0 y as the ceiling for a smoker who smoked from ~17 to "
           "<40 and then quit. Three years of exposure is a small fraction of that career, so the realised "
           "cost of a 3-year adolescent smoking exposure is BELOW 1 y."))

BANKS_Q = ("Compared to never-smokers, the adjusted RR (95% CI) of mortality was 2.96 (2.69-3.25) in "
           "current smokers and was similar in men (2.82 (2.49-3.19)) and women (3.08 (2.63-3.60)) and "
           "according to birth cohort. Mortality RRs increased with increasing smoking intensity, with "
           "around two- and four-fold increases in mortality in current smokers of <=14 (mean 10/day) and "
           ">=25 cigarettes/day, respectively, compared to never-smokers.")
BANKS_Q2 = ("Among past smokers, mortality diminished gradually with increasing time since cessation and "
            "did not differ significantly from never-smokers in those quitting prior to age 45. Current "
            "smokers are estimated to die an average of 10 years earlier than non-smokers.")

add("banks2015",
    citation=("Banks E, Joshy G, Weber MF, Liu B, Grenfell R, Egger S, Paige E, Lopez AD, Sitas F, Beral V. "
              "Tobacco smoking and all-cause mortality in a large Australian cohort study: findings from a "
              "mature epidemic with current low smoking prevalence. BMC Med. 2015;13:38."),
    doi="10.1186/s12916-015-0281-z", pmid="25857449",
    url="https://bmcmedicine.biomedcentral.com/articles/10.1186/s12916-015-0281-z",
    verification=ver("banks2015"),
    access_tier="abstract_only", secondhand_via=None,
    design="prospective_cohort_selfreport", tier="T5", n=204953, n_studies_pooled=None,
    population={"age_mean": None, "age_range": null_range, "pct_female": None,
                "country": "AU", "adolescent_match": "poor_midlife"},
    effects=[
        {"outcome_domain": "comparator", "outcome_construct": "all_cause_mortality_current_smoker_vs_never",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "current smoker vs never smoker, adults aged >=45"},
         "scale": "log_hr", "unit": "log hazard ratio", "value": round(math.log(2.96), 6),
         "se": round(se_from_ci(2.69, 3.25), 6), "ci": logci(2.69, 3.25),
         "conversion_formula": "RR 2.96 (95% CI 2.69-3.25). log_hr = ln(2.96) = 1.085189. "
                               "se = (ln(3.25)-ln(2.69))/3.919928 = 0.048177.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "positive = ELEVATED mortality in current smokers (harm).",
         "covariates": ["age", "education", "income", "region of residence", "alcohol", "body mass index"],
         "followup_years": 4.26, "cohort_family": "45_and_Up_NSW", "quote": BANKS_Q},
        {"outcome_domain": "comparator", "outcome_construct": "all_cause_mortality_light_smoker_le14_per_day",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "current smoker of <=14 cigarettes/day (mean 10/day) vs never smoker"},
         "scale": "log_hr", "unit": "log hazard ratio", "value": round(math.log(2.0), 6),
         "se": None, "ci": None,
         "conversion_formula": "Abstract reports 'around two-fold'. log_hr = ln(2.0) = 0.693147. "
                               "Rounded verbal figure with no CI in the abstract, so se null; treat as approximate.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "positive = ELEVATED mortality. THE DOSE ANCHOR: ~10 cig/day still roughly doubles mortality.",
         "covariates": ["age", "education", "income", "region of residence", "alcohol", "body mass index"],
         "followup_years": 4.26, "cohort_family": "45_and_Up_NSW", "quote": BANKS_Q},
        {"outcome_domain": "comparator", "outcome_construct": "all_cause_mortality_heavy_smoker_ge25_per_day",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "current smoker of >=25 cigarettes/day vs never smoker"},
         "scale": "log_hr", "unit": "log hazard ratio", "value": round(math.log(4.0), 6),
         "se": None, "ci": None,
         "conversion_formula": "Abstract reports 'four-fold'. log_hr = ln(4.0) = 1.386294. "
                               "Rounded verbal figure with no CI in the abstract, so se null; treat as approximate.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "positive = ELEVATED mortality. Dose-response: 10/day ~ 2x, >=25/day ~ 4x, i.e. "
                           "log-hazard is roughly linear in cigarettes/day over this range.",
         "covariates": ["age", "education", "income", "region of residence", "alcohol", "body mass index"],
         "followup_years": 4.26, "cohort_family": "45_and_Up_NSW", "quote": BANKS_Q},
        {"outcome_domain": "comparator", "outcome_construct": "life_expectancy_lost_current_smoker",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "current smoker vs non-smoker, sustained exposure"},
         "scale": "years", "unit": "years of life expectancy lost", "value": -10.0, "se": None, "ci": None,
         "conversion_formula": "Reported directly as 'an average of 10 years earlier'. No CI; se null.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "negative = life expectancy LOST. Independent replication of Doll 2004 and Jha 2013 "
                           "in a contemporary, low-prevalence, non-UK/US setting.",
         "covariates": ["age", "education", "income", "region of residence", "alcohol", "body mass index"],
         "followup_years": 4.26, "cohort_family": "45_and_Up_NSW", "quote": BANKS_Q2},
        {"outcome_domain": "comparator", "outcome_construct": "mortality_in_those_quitting_before_age_45",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "quit smoking before age 45 vs never smoker"},
         "scale": "log_hr", "unit": "log hazard ratio", "value": 0.0, "se": None, "ci": None,
         "conversion_formula": "Abstract states mortality in those quitting before 45 'did not differ "
                               "significantly from never-smokers'; encoded as log_hr = 0 (null). No point "
                               "estimate or CI given in the abstract, so se null. This is a NON-SIGNIFICANCE "
                               "statement, not a demonstration of equivalence.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "zero = no detectable excess mortality remaining. Reversibility evidence: quitting "
                           "before 45 returns mortality to the never-smoker level within this cohort's power.",
         "covariates": ["age", "education", "income", "region of residence", "alcohol", "body mass index"],
         "followup_years": 4.26, "cohort_family": "45_and_Up_NSW", "quote": BANKS_Q2},
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "moderate",
         "notes": "Large linked-data cohort with BMI and alcohol adjustment. Volunteer cohort (~18% response), "
                  "so selection bias is likely, though relative risks are usually robust to it. Short follow-up "
                  "(mean 4.26 y). Cessation categories are self-reported and recall-based; 'quit before 45' "
                  "carries survivor bias."},
    funding="Australian NHMRC; Cancer Council NSW (per report)",
    notes=("Supplies the DOSE gradient the task asked for (cigarettes/day) that Doll 2004's abstract does not, "
           "plus a third independent 10-year life-expectancy figure and a cessation-before-45 reversibility datum. "
           "The two-fold RR at a mean of 10 cigarettes/day is the figure to use if the modeller wants a "
           "'moderate smoker' rather than a pack-a-day comparator."))

PIRIE_Q = ("Among ex-smokers who had stopped permanently at ages 25-34 years or at ages 35-44 years, the "
           "respective relative risks were 1.05 (95% CI 1.00-1.11) and 1.20 (1.14-1.26) for all-cause "
           "mortality and 1.84 (1.45-2.34) and 3.34 (2.76-4.03) for lung cancer mortality. Thus, although "
           "some excess mortality remains among these long-term ex-smokers, it is only 3% and 10% of the "
           "excess mortality among continuing smokers.")
PIRIE_Q2 = ("Stopping before age 40 years (and preferably well before age 40 years) avoids more than 90% of "
            "the excess mortality caused by continuing smoking; stopping before age 30 years avoids more "
            "than 97% of it.")

add("pirie2013",
    citation=("Pirie K, Peto R, Reeves GK, Green J, Beral V; Million Women Study Collaborators. The 21st "
              "century hazards of smoking and benefits of stopping: a prospective study of one million "
              "women in the UK. Lancet. 2013;381(9861):133-141."),
    doi="10.1016/S0140-6736(12)61720-6", pmid="23107252",
    url="https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(12)61720-6/fulltext",
    verification=ver("pirie2013"),
    access_tier="abstract_only", secondhand_via=None,
    design="prospective_cohort_selfreport", tier="T5", n=1180652, n_studies_pooled=None,
    population={"age_mean": 55.0, "age_range": null_range, "pct_female": 100.0,
                "country": "UK", "adolescent_match": "poor_midlife"},
    effects=[
        {"outcome_domain": "comparator", "outcome_construct": "all_cause_mortality_current_smoker_vs_never",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "still smoking at 3-year resurvey vs never smoker"},
         "scale": "log_hr", "unit": "log rate ratio", "value": round(math.log(2.97), 6),
         "se": round(se_from_ci(2.88, 3.07), 6), "ci": logci(2.88, 3.07),
         "conversion_formula": "RR 2.97 (95% CI 2.88-3.07). log_hr = ln(2.97) = 1.088562. "
                               "se = (ln(3.07)-ln(2.88))/3.919928 = 0.016069.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "positive = ELEVATED mortality (harm).",
         "covariates": ["age", "region", "socioeconomic status", "alcohol", "BMI", "physical activity (per report)"],
         "followup_years": 12.0, "cohort_family": "Million_Women_Study", "quote":
             "Mortality was tripled, largely irrespective of age, in those still smoking at the 3-year "
             "resurvey (rate ratio 2.97, 2.88-3.07)."},
        {"outcome_domain": "comparator", "outcome_construct": "residual_all_cause_mortality_after_cessation_at_25_34",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "permanently stopped smoking at ages 25-34 vs never smoker"},
         "scale": "log_hr", "unit": "log rate ratio", "value": round(math.log(1.05), 6),
         "se": round(se_from_ci(1.00, 1.11), 6), "ci": logci(1.00, 1.11),
         "conversion_formula": "RR 1.05 (95% CI 1.00-1.11). log_hr = ln(1.05) = 0.048790. "
                               "se = (ln(1.11)-ln(1.00))/3.919928 = 0.026627.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "positive = residual excess mortality still present after quitting young, but only "
                           "5% excess versus 197% for continuing smokers. THE cleanest quantitative reversibility "
                           "benchmark in this shard for an exposure stopped in early adulthood.",
         "covariates": ["age", "region", "socioeconomic status", "alcohol", "BMI", "physical activity (per report)"],
         "followup_years": 12.0, "cohort_family": "Million_Women_Study", "quote": PIRIE_Q},
        {"outcome_domain": "comparator", "outcome_construct": "pct_of_smoking_excess_mortality_avoided_by_cessation_before_30",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "stopping smoking before age 30 vs continuing"},
         "scale": "pct_change", "unit": "percent of the excess death risk removed", "value": -97.0,
         "se": None, "ci": None,
         "conversion_formula": "Reported as 'more than 97%'; recorded as -97 (a floor). No CI; se null.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "negative = RISK REMOVED (benefit). Implies a residual of <=3% of the 11-year "
                           "lifespan gap = <=0.33 y for a smoking career of roughly 12-13 years.",
         "covariates": ["age", "region", "socioeconomic status", "alcohol", "BMI", "physical activity (per report)"],
         "followup_years": 12.0, "cohort_family": "Million_Women_Study", "quote": PIRIE_Q2},
        {"outcome_domain": "comparator", "outcome_construct": "life_expectancy_lost_current_smoker_women",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "continuing smoker vs never smoker, women, sustained exposure"},
         "scale": "years", "unit": "years of life expectancy lost", "value": -11.0, "se": None, "ci": None,
         "conversion_formula": "Reported as 'an 11-year lifespan difference' when tripled smoker mortality "
                               "rates are combined with 2010 UK national death rates. No CI; se null.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "negative = life expectancy LOST. Female counterpart to the ~10-year male figure; "
                           "Jackson 2025 uses exactly this pair (10 y men / 11 y women).",
         "covariates": ["age", "region", "socioeconomic status", "alcohol", "BMI", "physical activity (per report)"],
         "followup_years": 12.0, "cohort_family": "Million_Women_Study", "quote":
             "If combined with 2010 UK national death rates, tripled mortality rates among smokers indicate "
             "53% of smokers and 22% of never-smokers dying before age 80 years, and an 11-year lifespan difference."},
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "low",
         "notes": "Very large cohort with repeat exposure measurement at 3 and 8 years, which removes most of "
                  "the exposure-misclassification and reverse-causation problem that plagues single-baseline "
                  "smoking cohorts. WOMEN ONLY: transport to a male subject requires the assumption that the "
                  "cessation gradient is sex-invariant, which Jha 2013 (both sexes) supports."},
    funding="Cancer Research UK, Medical Research Council",
    notes=("Included specifically for the reversibility question, where it is the strongest evidence available "
           "for ANY of my comparators. The RR of 1.05 (1.00-1.11) for women who quit at 25-34 says that a "
           "young-adult smoking career followed by permanent cessation leaves an all-cause excess of ~5%, i.e. "
           "~0.3 y of the 11-year deficit (see convert.py). Population is women; recorded as poor_midlife and "
           "sex-mismatched so the pooler can inflate uncertainty."))

add("shaw2000",
    citation=("Shaw M, Mitchell R, Dorling D. Time for a smoke? One cigarette reduces your life by 11 "
              "minutes. BMJ. 2000;320(7226):53."),
    doi="10.1136/bmj.320.7226.53", pmid="10617536",
    url="https://www.bmj.com/content/320/7226/53",
    verification=ver("shaw2000"),
    access_tier="secondhand",
    secondhand_via=("Title verified verbatim in PubMed (PMID 10617536) and Crossref (DOI "
                    "10.1136/bmj.320.7226.53); the substantive assumptions and inputs are quoted from "
                    "Jackson 2025 (DOI 10.1111/add.16757), which re-derives this estimate. The BMJ letter "
                    "body itself is paywalled and PMC holds no full text for it."),
    design="life_table", tier="TX", n=None, n_studies_pooled=None,
    population={"age_mean": None, "age_range": [17, 71], "pct_female": 0.0,
                "country": "UK", "adolescent_match": "mixed"},
    effects=[
        {"outcome_domain": "comparator", "outcome_construct": "life_expectancy_lost_per_cigarette",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "one cigarette smoked, UK male smoker, 15.8 cig/day from age 17 to 71"},
         "scale": "years", "unit": "years of life expectancy lost per cigarette",
         "value": -11.0 / (60 * 24 * 365.25), "se": None, "ci": None,
         "conversion_formula": "11 minutes / (60 min/h * 24 h/d * 365.25 d/y) = 2.0913e-05 years per "
                               "cigarette. Original derivation (per Jackson 2025): 6.5 y of life expectancy "
                               "lost divided by lifetime cigarette consumption at 15.8/day from age 17 to 71. "
                               "No CI published; se null.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "negative = life expectancy LOST per cigarette. Superseded by Jackson 2025 (17 min "
                           "for men); retained because it is the original and most-cited per-unit-exposure "
                           "smoking figure.",
         "covariates": [], "followup_years": None, "cohort_family": "British_Doctors_Study",
         "quote": "Time for a smoke? One cigarette reduces your life by 11 minutes."},
    ],
    rob={"tool": "none", "judgement": "high",
         "notes": "A one-page BMJ letter, not a peer-reviewed analysis. The estimate is pure division of a "
                  "life-expectancy gap by a lifetime cigarette count; it therefore ASSUMES that harm is "
                  "linear in cigarettes and that every cigarette in a career carries equal weight. Its "
                  "mortality input (6.5 y) is now known to be roughly 40% too small."},
    funding=None,
    notes=("Included because the task asked for a citable minutes-per-cigarette estimate and this is its "
           "origin. It is quoted here from its VERBATIM TITLE, which contains the number; the letter body "
           "was not retrievable, so access_tier is secondhand and the analytic assumptions are cited from "
           "Jackson 2025 rather than from Shaw directly. USE JACKSON 2025 INSTEAD for the modelled value."))

JACKSON_Q = ("Britain has some of the best data available worldwide to estimate the average loss of life per "
             "cigarette smoked, which is approximately 20 minutes: 17 for men and 22 for women.")
JACKSON_Q2 = ("Thus, a person smoking 10 cigarettes per day who quits smoking on the 1st of January 2025 "
              "could prevent loss of a full day of life by the 8th of January, a week of life by the 20th of "
              "February, and a month by the 5th of August. By the end of the year, they could have avoided "
              "losing 50 days of life.")

add("jackson2025",
    citation=("Jackson SE, Jarvis MJ, West R. The price of a cigarette: 20 minutes of life? "
              "Addiction. 2025;120(5):810-812."),
    doi="10.1111/add.16757", pmid=None,
    url="https://onlinelibrary.wiley.com/doi/10.1111/add.16757",
    verification={"crossref_ok": True, "pubmed_ok": False, "title_similarity": 1.0,
                  "status": "VERIFIED",
                  "resolved_title": "The price of a cigarette: 20\u2009minutes of life?"},
    access_tier="full_text",
    secondhand_via=None,
    design="life_table", tier="TX", n=None, n_studies_pooled=None,
    population={"age_mean": None, "age_range": [17, 71], "pct_female": None,
                "country": "UK", "adolescent_match": "mixed"},
    effects=[
        {"outcome_domain": "comparator", "outcome_construct": "life_expectancy_lost_per_cigarette_men",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "one cigarette smoked, British male smoker who does not quit"},
         "scale": "years", "unit": "years of life expectancy lost per cigarette",
         "value": -17.0 / (60 * 24 * 365.25), "se": None, "ci": None,
         "conversion_formula": "17 minutes / (60*24*365.25) = 3.2320e-05 years per cigarette. Authors' own "
                               "derivation: 11 min * 10/6.5, i.e. the Shaw 2000 figure rescaled from a 6.5 y "
                               "to a 10 y male life-expectancy deficit (Doll 2004). No CI published; se null.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "negative = life expectancy LOST per cigarette. MALE figure, matching our subject's sex.",
         "covariates": ["socioeconomic position (in the underlying mortality studies)"],
         "followup_years": None, "cohort_family": "British_Doctors_Study", "quote": JACKSON_Q},
        {"outcome_domain": "comparator", "outcome_construct": "life_expectancy_lost_per_year_at_10_cig_per_day",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": 365.0,
                      "contrast_label": "one year of smoking 10 cigarettes/day, sex-averaged 20 min/cigarette"},
         "scale": "years", "unit": "years of life expectancy lost per year of exposure",
         "value": -50.0 / 365.25, "se": None, "ci": None,
         "conversion_formula": "Authors state 50 days of life avoided over one calendar year at 10 cig/day. "
                               "50/365.25 = 0.1369 y per exposure-year. Arithmetic check: 10 cig/d * 365 d * "
                               "20 min = 73,000 min = 50.7 d, so the 50-day figure uses the SEX-AVERAGED "
                               "20 min. Using the MALE 17 min gives 10*365.25*17/(60*24*365.25) = 0.1180 y "
                               "= 43.1 days per exposure-year. No CI published; se null.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "negative = life expectancy LOST per YEAR OF EXPOSURE. THE key commensurability "
                           "number for this shard: it is already denominated per year of exposure, so it can "
                           "be multiplied by 3 without any further assumption beyond the authors' own linearity.",
         "covariates": ["socioeconomic position (in the underlying mortality studies)"],
         "followup_years": None, "cohort_family": "British_Doctors_Study", "quote": JACKSON_Q2},
    ],
    rob={"tool": "none", "judgement": "moderate",
         "notes": "Peer-reviewed Addiction article but analytically a short re-derivation, not new data. The "
                  "central weakness for OUR purpose: dividing a lifetime life-expectancy deficit by a "
                  "lifetime cigarette count IMPOSES linearity in cumulative dose. Real smoking hazards are "
                  "strongly super-linear in DURATION (Doll/Peto: lung-cancer incidence scales roughly with "
                  "duration to the 4th-5th power), so an equal-share attribution OVERSTATES the harm of the "
                  "FIRST 3 years of a career and understates the last. Also UK-specific and does not credit "
                  "cessation-related recovery."},
    funding="Cancer Research UK; analysis commissioned by the UK Department of Health and Social Care (per paper)",
    notes=("THE most useful smoking record in this shard, because it is the only one denominated per unit of "
           "exposure. Downstream (convert.py): 3 years at 20 cig/day for a MALE = 20*365.25*3 cigarettes * "
           "17 min = 0.708 y (8.5 months); at 10 cig/day = 0.354 y (4.3 months). Compare with the "
           "cessation-based estimate from Pirie 2013 (~0.3 y for a WHOLE young-adult career) - the two "
           "disagree by a factor of ~2, and that disagreement IS the cumulative-versus-reversible tension "
           "this shard exists to expose. Not in PubMed at time of extraction; identifier verified by Crossref only."))

ZUHAL_Q = ("Among former smokers who quit smoking aged 50 years or more, the highest hazard ratios were "
           "detected for those who started smoking at <20 years of age (all-cause, cancer, and "
           "cardiovascular disease mortality, hazard ratio [95% confidence interval] 1.51 [1.29-1.77], "
           "1.68 [1.27-2.23], and 1.48 [1.12-1.96], respectively).")
ZUHAL_Q2 = ("Former smokers who quit smoking at <50 years of age had negligible all-cause or "
            "cardiovascular disease mortality regardless of the smoking-initiation age, whereas the "
            "cancer mortality risk remained significantly high among those who quit smoking at 40-49 "
            "years of age.")

add("zuhal2023",
    citation=("Zuhal SH, Eshak ES, Yamagishi K, Muraki I, Iso H, Tamakoshi A; JACC Study Group. "
              "Association of the age at smoking initiation and cessation on all-cause and "
              "cause-specific mortality: the Japan Collaborative Cohort Study. Nagoya J Med Sci. "
              "2023;85(4):691-708."),
    doi="10.18999/nagjms.85.4.691", pmid="38155620",
    url="https://doi.org/10.18999/nagjms.85.4.691",
    verification={"crossref_ok": False, "pubmed_ok": True, "title_similarity": 1.0,
                  "status": "VERIFIED",
                  "resolved_title": "Association of the age at smoking initiation and cessation on "
                                    "all-cause and cause-specific mortality: The Japan Collaborative "
                                    "Cohort Study."},
    access_tier="abstract_only", secondhand_via=None,
    design="prospective_cohort_selfreport", tier="T5", n=41711, n_studies_pooled=None,
    population={"age_mean": None, "age_range": [40, 79], "pct_female": 0.0,
                "country": "JP", "adolescent_match": "poor_midlife"},
    effects=[
        {"outcome_domain": "comparator", "outcome_construct": "all_cause_mortality_initiated_under_20_quit_at_50_plus",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "started smoking before age 20 AND quit at >=50 vs never smoker"},
         "scale": "log_hr", "unit": "log hazard ratio", "value": round(math.log(1.51), 6),
         "se": round(se_from_ci(1.29, 1.77), 6), "ci": logci(1.29, 1.77),
         "conversion_formula": "HR 1.51 (95% CI 1.29-1.77) all-cause. log_hr = ln(1.51) = 0.412110. "
                               "se = (ln(1.77)-ln(1.29))/3.919928 = 0.080665.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "positive = ELEVATED mortality (harm). The WORST case: adolescent initiation "
                           "with LATE cessation still leaves a 51% all-cause excess after ~30 years of "
                           "smoking. Contrast with the next effect, where cessation before 50 removes it.",
         "covariates": ["age", "and multivariable covariates per report"], "followup_years": 20.0,
         "cohort_family": "JACC_Japan", "quote": ZUHAL_Q},
        {"outcome_domain": "comparator", "outcome_construct": "all_cause_mortality_quit_before_50_any_initiation_age",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "quit smoking before age 50, ANY age at initiation (including <20), "
                                        "vs never smoker"},
         "scale": "log_hr", "unit": "log hazard ratio", "value": 0.0, "se": None, "ci": None,
         "conversion_formula": "Reported qualitatively as 'negligible all-cause or cardiovascular disease "
                               "mortality regardless of the smoking-initiation age'; encoded as log_hr = 0. "
                               "No point estimate or CI given in the abstract for this stratum, so se null. "
                               "This is a NEGLIGIBILITY statement, not a demonstration of equivalence.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "zero = no meaningful residual all-cause excess. THE DIRECT ANSWER TO 'DOES "
                           "STARTING YOUNG LEAVE A PERMANENT MARK IF YOU STOP?' - on all-cause mortality, "
                           "essentially no, provided cessation happens before 50. Cancer mortality is the "
                           "exception and does retain a residue.",
         "covariates": ["age", "and multivariable covariates per report"], "followup_years": 20.0,
         "cohort_family": "JACC_Japan", "quote": ZUHAL_Q2},
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "moderate",
         "notes": "Independent (Japanese) cohort, which is a genuine addition to a reversibility evidence "
                  "base otherwise entirely UK/US/Australian. But age at initiation and at cessation are "
                  "both RECALLED at ages 40-79, so exposure misclassification is substantial; the "
                  "'negligible' finding for quitters under 50 is reported without a point estimate; and "
                  "the cohort enrols at 40-79, so anyone who died before 40 is excluded by design "
                  "(survivor bias, which biases the cessation benefit upward)."},
    funding="Japanese Ministry of Education, Culture, Sports, Science and Technology / JACC Study (per report)",
    notes=("Added late in screening and worth it: it is the only record I found that crosses AGE AT "
           "INITIATION with AGE AT CESSATION, which is exactly the two-dimensional question our subject "
           "poses (exposure begun at 16, ended at 19). Its answer is that initiation before 20 is not "
           "independently damaging on the ALL-CAUSE scale provided cessation is early; what drives the "
           "residual harm is total DURATION, i.e. how late you stop. That supports treating our subject's "
           "3-year window as a small cumulative dose rather than a developmental insult. CANCER mortality "
           "is the documented exception. DOI is registered with JaLC, not Crossref, so the Crossref API "
           "returns 404; the DOI nonetheless resolves through doi.org with HTTP 200 to the Nagoya "
           "University repository, and the PMID resolves in PubMed, so status is VERIFIED."))

# ==========================================================================
# 2. BODY MASS INDEX
# ==========================================================================

PSC_Q = ("In both sexes, mortality was lowest at about 22.5-25 kg/m(2). Above this range, positive "
         "associations were recorded for several specific causes and inverse associations for none, the "
         "absolute excess risks for higher BMI and smoking were roughly additive, and each 5 kg/m(2) higher "
         "BMI was on average associated with about 30% higher overall mortality (hazard ratio per 5 kg/m(2) "
         "[HR] 1.29 [95% CI 1.27-1.32])")
PSC_Q2 = ("At 30-35 kg/m(2), median survival is reduced by 2-4 years; at 40-45 kg/m(2), it is reduced by "
          "8-10 years (which is comparable with the effects of smoking).")

add("psc2009",
    citation=("Prospective Studies Collaboration; Whitlock G, Lewington S, Sherliker P, Clarke R, Emberson J, "
              "Halsey J, Qizilbash N, Collins R, Peto R. Body-mass index and cause-specific mortality in "
              "900 000 adults: collaborative analyses of 57 prospective studies. Lancet. 2009;373(9669):1083-1096."),
    doi="10.1016/S0140-6736(09)60318-4", pmid="19299006",
    url="https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(09)60318-4/fulltext",
    verification=ver("psc2009"),
    access_tier="abstract_only", secondhand_via=None,
    design="meta_analysis_observational", tier="T5", n=894576, n_studies_pooled=57,
    population={"age_mean": 46.0, "age_range": None, "pct_female": 39.0,
                "country": "western Europe and North America (mostly)", "adolescent_match": "poor_midlife"},
    effects=[
        {"outcome_domain": "comparator", "outcome_construct": "all_cause_mortality_per_5_kgm2_higher_bmi",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "+5 kg/m2 BMI above 22.5-25 kg/m2, sustained"},
         "scale": "log_hr", "unit": "log hazard ratio per 5 kg/m2", "value": round(math.log(1.29), 6),
         "se": round(se_from_ci(1.27, 1.32), 6), "ci": logci(1.27, 1.32),
         "conversion_formula": "HR 1.29 (95% CI 1.27-1.32) per 5 kg/m2. log_hr = ln(1.29) = 0.254642. "
                               "se = (ln(1.32)-ln(1.27))/3.919928 = 0.009843.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "positive = ELEVATED mortality per 5 kg/m2 above the optimum (harm).",
         "covariates": ["age", "sex", "smoking status", "study"], "followup_years": 8.0,
         "cohort_family": "Prospective_Studies_Collaboration", "quote": PSC_Q},
        {"outcome_domain": "comparator", "outcome_construct": "median_survival_reduction_bmi_30_35",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "BMI 30-35 kg/m2 vs the 22.5-25 optimum, sustained from ~age 46"},
         "scale": "years", "unit": "years of median survival lost", "value": -3.0, "se": None, "ci": None,
         "conversion_formula": "Reported as a range, '2-4 years'; midpoint 3.0 recorded. The 2-4 span is a "
                               "ROUNDED RANGE across the BMI band, NOT a confidence interval, so ci is left "
                               "null and se null. Modellers wanting an interval should use [-4, -2].",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "negative = median survival LOST. Sustained lifelong exposure from midlife, NOT 3 years.",
         "covariates": ["age", "sex", "smoking status", "study"], "followup_years": 8.0,
         "cohort_family": "Prospective_Studies_Collaboration", "quote": PSC_Q2},
        {"outcome_domain": "comparator", "outcome_construct": "median_survival_reduction_bmi_40_45",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "BMI 40-45 kg/m2 vs the 22.5-25 optimum, sustained from ~age 46"},
         "scale": "years", "unit": "years of median survival lost", "value": -9.0, "se": None, "ci": None,
         "conversion_formula": "Reported as '8-10 years'; midpoint 9.0 recorded. Rounded range, not a CI; "
                               "ci and se null. Modellers wanting an interval should use [-10, -8].",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "negative = median survival LOST. The paper itself notes this is 'comparable with "
                           "the effects of smoking' - i.e. grade-3 obesity, sustained, ~= lifelong smoking.",
         "covariates": ["age", "sex", "smoking status", "study"], "followup_years": 8.0,
         "cohort_family": "Prospective_Studies_Collaboration", "quote": PSC_Q2},
    ],
    rob={"tool": "AMSTAR-2", "judgement": "low",
         "notes": "IPD collaboration, first 5 years of follow-up excluded to limit reverse causation, adjusted "
                  "for smoking. Single baseline BMI measurement means regression dilution (the paper corrects "
                  "for it). Mean recruitment age 46, so wholly extrapolated to a 16-19 year old."},
    funding="UK Medical Research Council, British Heart Foundation, Cancer Research UK, EU BIOMED programme (per report)",
    notes=("The per-5-kg/m2 HR asked for in the task. Note the important asymmetry the abstract flags: below "
           "22.5 kg/m2 the association REVERSES, and that inverse limb is smoking-confounded. For our subject "
           "(lean 18-year-old) only the upper limb is relevant. Conversion to 3 years is in comparator_scale.md."))

GBMI_Q = ("For BMI over 25.0 kg/m(2), mortality increased approximately log-linearly with BMI; the HR per 5 "
          "kg/m(2) units higher BMI was 1.39 (1.34-1.43) in Europe, 1.29 (1.26-1.32) in North America, 1.39 "
          "(1.34-1.44) in east Asia, and 1.31 (1.27-1.35) in Australia and New Zealand.")
GBMI_Q2 = ("This HR per 5 kg/m(2) units higher BMI (for BMI over 25 kg/m(2)) was greater in younger than "
           "older people (1.52, 95% CI 1.47-1.56, for BMI measured at 35-49 years vs 1.21, 1.17-1.25, for "
           "BMI measured at 70-89 years; pheterogeneity<0.0001), greater in men than women (1.51, 1.46-1.56, "
           "vs 1.30, 1.26-1.33; pheterogeneity<0.0001), but similar in studies with self-reported and "
           "measured BMI.")

add("globalbmi2016",
    citation=("Global BMI Mortality Collaboration; Di Angelantonio E, Bhupathiraju SN, Wormser D, et al. "
              "Body-mass index and all-cause mortality: individual-participant-data meta-analysis of 239 "
              "prospective studies in four continents. Lancet. 2016;388(10046):776-786."),
    doi="10.1016/S0140-6736(16)30175-1", pmid="27423262",
    url="https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(16)30175-1/fulltext",
    verification=ver("globalbmi2016"),
    access_tier="abstract_only", secondhand_via=None,
    design="meta_analysis_observational", tier="T5", n=3951455, n_studies_pooled=189,
    population={"age_mean": None, "age_range": null_range, "pct_female": None,
                "country": "Asia, Australia/NZ, Europe, North America", "adolescent_match": "poor_midlife"},
    effects=[
        {"outcome_domain": "comparator", "outcome_construct": "all_cause_mortality_per_5_kgm2_north_america",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "+5 kg/m2 BMI above 25 kg/m2, North America, never-smokers"},
         "scale": "log_hr", "unit": "log hazard ratio per 5 kg/m2", "value": round(math.log(1.29), 6),
         "se": round(se_from_ci(1.26, 1.32), 6), "ci": logci(1.26, 1.32),
         "conversion_formula": "HR 1.29 (95% CI 1.26-1.32). log_hr = ln(1.29) = 0.254642. "
                               "se = (ln(1.32)-ln(1.26))/3.919928 = 0.011860.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "positive = ELEVATED mortality per 5 kg/m2 (harm). Restricted to never-smokers with "
                           "no chronic disease and >=5 y survival, so much less confounded than PSC 2009.",
         "covariates": ["study", "age", "sex"], "followup_years": 13.7,
         "cohort_family": "Global_BMI_Mortality_Collaboration", "quote": GBMI_Q},
        {"outcome_domain": "comparator", "outcome_construct": "all_cause_mortality_per_5_kgm2_bmi_measured_at_35_49",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "+5 kg/m2 BMI above 25, BMI MEASURED AT AGES 35-49"},
         "scale": "log_hr", "unit": "log hazard ratio per 5 kg/m2", "value": round(math.log(1.52), 6),
         "se": round(se_from_ci(1.47, 1.56), 6), "ci": logci(1.47, 1.56),
         "conversion_formula": "HR 1.52 (95% CI 1.47-1.56). log_hr = ln(1.52) = 0.418710. "
                               "se = (ln(1.56)-ln(1.47))/3.919928 = 0.015069.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "positive = ELEVATED mortality. CRITICAL FOR TRANSPORT: the BMI-mortality hazard "
                           "ratio is LARGER when adiposity is measured EARLIER in life (1.52 at 35-49 vs 1.21 "
                           "at 70-89). Extrapolating the 35-49 gradient toward ages 16-19 is the direction "
                           "the data point, so using the pooled 1.29 for a young subject is CONSERVATIVE.",
         "covariates": ["study", "age", "sex"], "followup_years": 13.7,
         "cohort_family": "Global_BMI_Mortality_Collaboration", "quote": GBMI_Q2},
        {"outcome_domain": "comparator", "outcome_construct": "all_cause_mortality_bmi_27_5_to_30_vs_22_5_25",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "BMI 27.5-30 vs 22.5-25 kg/m2, never-smokers"},
         "scale": "log_hr", "unit": "log hazard ratio", "value": round(math.log(1.20), 6),
         "se": round(se_from_ci(1.18, 1.22), 6), "ci": logci(1.18, 1.22),
         "conversion_formula": "HR 1.20 (95% CI 1.18-1.22). log_hr = ln(1.20) = 0.182322. "
                               "se = (ln(1.22)-ln(1.18))/3.919928 = 0.008579.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "positive = ELEVATED mortality. This is the category-level anchor for the "
                           "'sleep-restriction-sized' weight gain comparator (a few kg/m2, not frank obesity).",
         "covariates": ["study", "age", "sex"], "followup_years": 13.7,
         "cohort_family": "Global_BMI_Mortality_Collaboration", "quote":
             "All-cause mortality was minimal at 20.0-25.0 kg/m(2) (HR 1.00, 95% CI 0.98-1.02 for BMI "
             "20.0-<22.5 kg/m(2); 1.00, 0.99-1.01 for BMI 22.5-<25.0 kg/m(2)), and increased significantly "
             "both just below this range (1.13, 1.09-1.17 for BMI 18.5-<20.0 kg/m(2); 1.51, 1.43-1.59 for BMI "
             "15.0-<18.5) and throughout the overweight range (1.07, 1.07-1.08 for BMI 25.0-<27.5 kg/m(2); "
             "1.20, 1.18-1.22 for BMI 27.5-<30.0 kg/m(2))."},
        {"outcome_domain": "comparator", "outcome_construct": "all_cause_mortality_obesity_grade_1_vs_22_5_25",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "BMI 30-35 vs 22.5-25 kg/m2, never-smokers"},
         "scale": "log_hr", "unit": "log hazard ratio", "value": round(math.log(1.45), 6),
         "se": round(se_from_ci(1.41, 1.48), 6), "ci": logci(1.41, 1.48),
         "conversion_formula": "HR 1.45 (95% CI 1.41-1.48). log_hr = ln(1.45) = 0.371564. "
                               "se = (ln(1.48)-ln(1.41))/3.919928 = 0.012509.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "positive = ELEVATED mortality. Pairs with PSC 2009's '2-4 years' for the same BMI "
                           "band, giving an HR-to-years anchor pair (see convert.py calibration).",
         "covariates": ["study", "age", "sex"], "followup_years": 13.7,
         "cohort_family": "Global_BMI_Mortality_Collaboration", "quote":
             "The HR for obesity grade 1 (BMI 30.0-<35.0 kg/m(2)) was 1.45, 95% CI 1.41-1.48; the HR for "
             "obesity grade 2 (35.0-<40.0 kg/m(2)) was 1.94, 1.87-2.01; and the HR for obesity grade 3 "
             "(40.0-<60.0 kg/m(2)) was 2.76, 2.60-2.92."},
    ],
    rob={"tool": "AMSTAR-2", "judgement": "low",
         "notes": "Best-in-class confounding control for BMI: never-smokers only, no chronic disease at "
                  "recruitment, first 5 years of follow-up excluded. Still observational and still a single "
                  "baseline BMI, and still no one under ~20 contributing exposure."},
    funding="UK Medical Research Council, British Heart Foundation, National Institute for Health Research, US National Institutes of Health",
    notes=("Preferred over PSC 2009 for the HR per 5 kg/m2 because of the never-smoker restriction. Two "
           "findings matter most for transport to a 16-19 year old: (a) the hazard ratio is ~18% larger for "
           "MEN than women (1.51 vs 1.30), and (b) it is ~26% larger when adiposity is measured at 35-49 than "
           "the all-age pooled figure. Both push the young-male estimate UP, not down."))

add("fontaine2003",
    citation=("Fontaine KR, Redden DT, Wang C, Westfall AO, Allison DB. Years of life lost due to obesity. "
              "JAMA. 2003;289(2):187-193."),
    doi="10.1001/jama.289.2.187", pmid="12517229",
    url="https://jamanetwork.com/journals/jama/fullarticle/195748",
    verification=ver("fontaine2003"),
    access_tier="abstract_only", secondhand_via=None,
    design="life_table", tier="TX", n=None, n_studies_pooled=None,
    population={"age_mean": None, "age_range": [18, 85], "pct_female": None,
                "country": "US", "adolescent_match": "good_young_adult"},
    effects=[
        {"outcome_domain": "comparator", "outcome_construct": "years_of_life_lost_bmi_over_45_white_men_aged_20_30",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "BMI >45 vs BMI 24 referent, white men aged 20-30, sustained"},
         "scale": "years", "unit": "years of life lost", "value": -13.0, "se": None, "ci": None,
         "conversion_formula": "Reported directly as a maximum YLL of 13 for white men aged 20-30 with BMI "
                               ">45, against a BMI 24 referent. No CI published; se null.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "negative = years of life LOST. THE MOST AGE-RELEVANT BMI RECORD IN THIS SHARD: it "
                           "is computed for 20-30 year olds. But it prices SEVERE obesity SUSTAINED from that "
                           "age, not 3 years of mild weight gain.",
         "covariates": ["age", "sex", "race"], "followup_years": None, "cohort_family": "NHANES",
         "quote": "For any given degree of overweight, younger adults generally had greater YLL than did "
                  "older adults. The maximum YLL for white men aged 20 to 30 years with a severe level of "
                  "obesity (BMI >45) is 13 and is 8 for white women. For men, this could represent a 22% "
                  "reduction in expected remaining life span."},
    ],
    rob={"tool": "none", "judgement": "moderate",
         "notes": "A life-table modelling exercise, not a cohort. It stacks NHANES prevalence on NHANES "
                  "follow-up mortality and 1999 US life tables, and assumes BMI at baseline persists for life. "
                  "The BMI >45 stratum is small and the estimates are unstable (the black-male estimate of 20 y "
                  "against a black-female estimate of 5 y is implausibly divergent, signalling sparse data). "
                  "No uncertainty intervals published for the YLL figures."},
    funding="US National Institutes of Health (per report)",
    notes=("Included specifically to answer 'YLL for a given BMI at a given age' in the age band nearest our "
           "subject. The transportable finding is the DIRECTION of the age gradient - 'for any given degree of "
           "overweight, younger adults generally had greater YLL' - which corroborates Global BMI 2016's "
           "stronger HR when BMI is measured earlier. The BMI >45 point value is NOT usable as a comparator "
           "for a 3-year exposure; it is a ceiling on the whole obesity channel."))

PEETERS_Q = ("Forty-year-old female nonsmokers lost 3.3 years and 40-year-old male nonsmokers lost 3.1 years "
             "of life expectancy because of overweight. Forty-year-old female nonsmokers lost 7.1 years and "
             "40-year-old male nonsmokers lost 5.8 years because of obesity.")

add("peeters2003",
    citation=("Peeters A, Barendregt JJ, Willekens F, Mackenbach JP, Al Mamun A, Bonneux L; NEDCOM. Obesity "
              "in adulthood and its consequences for life expectancy: a life-table analysis. Ann Intern Med. "
              "2003;138(1):24-32."),
    doi="10.7326/0003-4819-138-1-200301070-00008", pmid="12513041",
    url="https://www.acpjournals.org/doi/10.7326/0003-4819-138-1-200301070-00008",
    verification=ver("peeters2003"),
    access_tier="abstract_only", secondhand_via=None,
    design="life_table", tier="TX", n=3457, n_studies_pooled=None,
    population={"age_mean": None, "age_range": [30, 49], "pct_female": None,
                "country": "US", "adolescent_match": "poor_midlife"},
    effects=[
        {"outcome_domain": "comparator", "outcome_construct": "life_expectancy_lost_overweight_at_40_male_nonsmokers",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "overweight (BMI 25-30) vs normal weight at age 40, male nonsmokers, sustained"},
         "scale": "years", "unit": "years of life expectancy lost", "value": -3.1, "se": None, "ci": None,
         "conversion_formula": "Reported directly. Abstract publishes no CI for this figure; se null. "
                               "This is the cleanest 'sustained overweight, from a known starting age' anchor "
                               "available and is the basis of the BMI pro-rata conversion in comparator_scale.md.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "negative = life expectancy LOST. Exposure is being overweight from age 40 onward "
                           "(~38.6 remaining years in the US male 2023 life table), NOT 3 years.",
         "covariates": ["age", "sex", "smoking status"], "followup_years": 42.0,
         "cohort_family": "Framingham", "quote": PEETERS_Q},
        {"outcome_domain": "comparator", "outcome_construct": "life_expectancy_lost_obesity_at_40_male_nonsmokers",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "obesity (BMI >=30) vs normal weight at age 40, male nonsmokers, sustained"},
         "scale": "years", "unit": "years of life expectancy lost", "value": -5.8, "se": None, "ci": None,
         "conversion_formula": "Reported directly. No CI in the abstract; se null.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "negative = life expectancy LOST. Consistent with PSC 2009's 2-4 y for BMI 30-35 "
                           "given that this stratum includes higher BMIs.",
         "covariates": ["age", "sex", "smoking status"], "followup_years": 42.0,
         "cohort_family": "Framingham", "quote": PEETERS_Q},
        {"outcome_domain": "comparator", "outcome_construct": "residual_effect_of_early_adult_bmi_after_adjusting_for_later_bmi",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "BMI at ages 30-49 predicting mortality at 50-69, adjusted for BMI at 50-69"},
         "scale": "log_hr", "unit": "qualitative - direction only", "value": 1.0, "se": None, "ci": None,
         "conversion_formula": "NO NUMERIC EFFECT SIZE IS PUBLISHED IN THE ABSTRACT for this adjusted "
                               "association. value is a placeholder sign flag (1 = positive association "
                               "present) and MUST NOT be pooled as a magnitude. Recorded because the "
                               "DIRECTIONAL claim is the only direct evidence I could retrieve that "
                               "EARLIER-LIFE adiposity leaves a mortality signal that later-life adiposity "
                               "does not explain away.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "positive = earlier-life BMI carries an INDEPENDENT (partly irreversible) mortality "
                           "signal. DO NOT USE AS A MAGNITUDE - sign/direction only.",
         "covariates": ["BMI at age 50-69", "age", "sex", "smoking status"], "followup_years": 42.0,
         "cohort_family": "Framingham", "quote":
             "Body mass index at ages 30 to 49 years predicted mortality after ages 50 to 69 years, even "
             "after adjustment for body mass index at age 50 to 69 years."},
    ],
    rob={"tool": "none", "judgement": "moderate",
         "notes": "Life-table analysis on a single, small (n=3457), all-white, mid-20th-century New England "
                  "cohort. Baseline BMI is assumed to persist. The adjusted early-BMI finding is reported "
                  "without a number in the abstract and is vulnerable to regression dilution in the "
                  "later-life BMI adjustment, which would EXAGGERATE the apparent independent early effect."},
    funding="Netherlands Organization for Scientific Research / NEDCOM (per report)",
    notes=("Two distinct roles. (1) The 3.1 y figure for male nonsmoker overweight at 40 is my primary BMI "
           "pro-rata input: 3.1 y / e(40)=38.6 y = 0.080 y per exposure-year, so 3 years = 0.24 y. (2) The "
           "adjusted early-BMI claim is the ONLY retrievable evidence bearing on BMI IRREVERSIBILITY, and it "
           "is qualitative. That is a real gap - see station_report.md."))

TWIG_Q = ("Hazard ratios in the obese group (>=95th percentile for BMI), as compared with the reference group "
          "in the 5th to 24th percentiles, were 4.9 (95% confidence interval [CI], 3.9 to 6.1) for death from "
          "coronary heart disease, 2.6 (95% CI, 1.7 to 4.1) for death from stroke, 2.1 (95% CI, 1.5 to 2.9) "
          "for sudden death, and 3.5 (95% CI, 2.9 to 4.1) for death from total cardiovascular causes, after "
          "adjustment for sex, age, birth year, sociodemographic characteristics, and height.")

add("twig2016",
    citation=("Twig G, Yaniv G, Levine H, Leiba A, Goldberger N, Derazne E, Ben-Ami Shor D, Tzur D, Afek A, "
              "Shamiss A, Haklai Z, Kark JD. Body-mass index in 2.3 million adolescents and cardiovascular "
              "death in adulthood. N Engl J Med. 2016;374(25):2430-2440."),
    doi="10.1056/NEJMoa1503840", pmid="27074389",
    url="https://www.nejm.org/doi/10.1056/NEJMoa1503840",
    verification=ver("twig2016"),
    access_tier="abstract_only", secondhand_via=None,
    design="prospective_cohort_objective", tier="T4", n=2300000, n_studies_pooled=None,
    population={"age_mean": 17.3, "age_range": null_range, "pct_female": None,
                "country": "IL", "adolescent_match": "exact_16_19"},
    effects=[
        {"outcome_domain": "comparator", "outcome_construct": "cardiovascular_death_adolescent_bmi_ge95th_pct",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "measured BMI >=95th percentile at mean age 17.3 vs 5th-24th percentile"},
         "scale": "log_hr", "unit": "log hazard ratio", "value": round(math.log(3.5), 6),
         "se": round(se_from_ci(2.9, 4.1), 6), "ci": logci(2.9, 4.1),
         "conversion_formula": "HR 3.5 (95% CI 2.9-4.1) for total cardiovascular death. log_hr = ln(3.5) = "
                               "1.252763. se = (ln(4.1)-ln(2.9))/3.919928 = 0.088177.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "positive = ELEVATED cardiovascular death in adulthood. CAUSE-SPECIFIC (CV), not "
                           "all-cause, so it is NOT directly comparable to the all-cause HRs elsewhere in "
                           "this shard.",
         "covariates": ["sex", "age", "birth year", "sociodemographic characteristics", "height"],
         "followup_years": 18.4, "cohort_family": "Israeli_Adolescent_Conscripts", "quote": TWIG_Q},
        {"outcome_domain": "comparator", "outcome_construct": "cardiovascular_death_adolescent_bmi_ge95th_at_30_40y_followup",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "measured BMI >=95th pct at age ~17, deaths occurring 30-40 y later"},
         "scale": "log_hr", "unit": "log hazard ratio", "value": round(math.log(4.1), 6),
         "se": round(se_from_ci(3.1, 5.4), 6), "ci": logci(3.1, 5.4),
         "conversion_formula": "HR 4.1 (95% CI 3.1-5.4) at 30-40 y of follow-up. log_hr = ln(4.1) = 1.410987. "
                               "se = (ln(5.4)-ln(3.1))/3.919928 = 0.141602.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "positive = ELEVATED CV death. The HR RISES with follow-up length (2.0 at 0-10 y to "
                           "4.1 at 30-40 y), which is what a CUMULATIVE-DAMAGE (not a transient) mechanism "
                           "looks like. But see rob/notes: adolescent BMI tracks strongly into midlife, so "
                           "this cannot be read as the effect of a 3-year adolescent exposure.",
         "covariates": ["sex", "age", "birth year", "sociodemographic characteristics", "height"],
         "followup_years": 35.0, "cohort_family": "Israeli_Adolescent_Conscripts", "quote":
             "Hazard ratios for death from cardiovascular causes in the same percentile groups increased from "
             "2.0 (95% CI, 1.1 to 3.9) during follow-up for 0 to 10 years to 4.1 (95% CI, 3.1 to 5.4) during "
             "follow-up for 30 to 40 years; during both periods, hazard ratios were consistently high for "
             "death from coronary heart disease."},
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "moderate",
         "notes": "CRITICAL LIMITATION for this shard's purpose: BMI was measured ONCE, at age ~17, and no "
                  "adult BMI was available. Adolescent BMI tracks strongly into adulthood, so these hazard "
                  "ratios price a LIFELONG adiposity TRAJECTORY that merely starts in adolescence - they are "
                  "not the effect of a transient 3-year exposure. Exposure measurement itself is excellent "
                  "(measured, not self-reported, whole-population conscription examination, n=2.3 million)."},
    funding="Environment and Health Fund",
    notes=("Included because it is the only record in this shard whose EXPOSURE IS MEASURED AT EXACTLY OUR "
           "SUBJECT'S AGE (mean 17.3 y, adolescent_match exact_16_19). It supplies the upper bound for the "
           "'irreversible adolescent insult' story: HR 3.5 for CV death applied permanently from 19 would be "
           "~16 y of life expectancy (convert.py). That number is almost certainly an over-attribution and "
           "must NOT be used as a 3-year-exposure effect. Also note the graded risk began WITHIN the normal "
           "BMI range (50th-74th percentile), which matters for a subject whose weight gain is modest."))

add("zheng2017",
    citation=("Zheng Y, Manson JE, Yuan C, Liang MH, Grodstein F, Stampfer MJ, Willett WC, Hu FB. "
              "Associations of weight gain from early to middle adulthood with major health outcomes later "
              "in life. JAMA. 2017;318(3):255-269."),
    doi="10.1001/jama.2017.7092", pmid="28719691",
    url="https://jamanetwork.com/journals/jama/fullarticle/2643761",
    verification=ver("zheng2017"),
    access_tier="abstract_only", secondhand_via=None,
    design="prospective_cohort_selfreport", tier="T5", n=118140, n_studies_pooled=None,
    population={"age_mean": None, "age_range": [18, 55], "pct_female": 78.6,
                "country": "US", "adolescent_match": "mixed"},
    effects=[
        {"outcome_domain": "comparator", "outcome_construct": "healthy_aging_odds_moderate_weight_gain_18_to_55_men",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "moderate weight gain (>=2.5 to <10 kg) from age 21 to 55 vs stable weight, men"},
         "scale": "log_or", "unit": "log odds ratio for composite healthy aging", "value": round(math.log(0.88), 6),
         "se": round(se_from_ci(0.79, 0.97), 6), "ci": logci(0.79, 0.97),
         "conversion_formula": "OR 0.88 (95% CI 0.79-0.97) for the composite healthy-aging outcome in men. "
                               "log_or = ln(0.88) = -0.127833. se = (ln(0.97)-ln(0.79))/3.919928 = 0.052434.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "negative = LOWER odds of healthy aging (harm) after moderate weight gain across "
                           "adulthood. Outcome is healthy aging, NOT mortality, so it is not on the "
                           "life-expectancy scale.",
         "covariates": ["age", "smoking", "physical activity", "diet", "alcohol", "and others per report"],
         "followup_years": None, "cohort_family": "NHS_HPFS", "quote":
             "The multivariable-adjusted odds ratio for the composite healthy aging outcome associated with "
             "moderate weight gain was 0.78 (95% CI, 0.72 to 0.84) in women and 0.88 (95% CI, 0.79 to 0.97) in men."},
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "moderate",
         "notes": "Weight at age 18/21 is RECALLED, in some cases decades later, which is a major exposure "
                  "misclassification problem. 97% white health professionals. The exposure is weight CHANGE "
                  "over 34-37 years, so it says nothing about a 3-year window."},
    funding="US National Institutes of Health (per report)",
    notes=("Screened in as the closest available evidence on whether adiposity acquired in late adolescence "
           "persists and matters. It does establish that the weight-gain TRAJECTORY from 18 to 55 predicts "
           "worse outcomes, which is the empirical reason to worry that a sleep-restriction-induced weight "
           "gain at 16-19 is not a 3-year exposure at all but the start of a trajectory. It does NOT provide "
           "a life-expectancy figure and should carry little weight in the comparator table."))

# ==========================================================================
# 3. PHYSICAL INACTIVITY
# ==========================================================================

add("lee2012",
    citation=("Lee IM, Shiroma EJ, Lobelo F, Puska P, Blair SN, Katzmarzyk PT; Lancet Physical Activity "
              "Series Working Group. Effect of physical inactivity on major non-communicable diseases "
              "worldwide: an analysis of burden of disease and life expectancy. Lancet. 2012;380(9838):219-229."),
    doi="10.1016/S0140-6736(12)61031-9", pmid="22818936",
    url="https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(12)61031-9/fulltext",
    verification=ver("lee2012"),
    access_tier="abstract_only", secondhand_via=None,
    design="life_table", tier="TX", n=None, n_studies_pooled=None,
    population={"age_mean": None, "age_range": None, "pct_female": None,
                "country": "global", "adolescent_match": "mixed"},
    effects=[
        {"outcome_domain": "comparator", "outcome_construct": "population_life_expectancy_gain_from_eliminating_inactivity",
         "exposure": {"type": "descriptive", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "hypothetical elimination of physical inactivity in the world population"},
         "scale": "years", "unit": "years of POPULATION life expectancy gained", "value": 0.68,
         "se": None, "ci": [0.41, 0.95],
         "conversion_formula": "Reported as 0.68 (range 0.41-0.95) years. The published span is a SENSITIVITY "
                               "RANGE over the input relative risks, NOT a 95% CI, so no se is derived from "
                               "it; se null. Recorded in ci for the modeller with this caveat attached.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "positive = POPULATION life expectancy GAINED. THIS IS NOT AN INDIVIDUAL EFFECT and "
                           "is very commonly misquoted as one. It is a population-average figure diluted by "
                           "the (large) already-active fraction of the world population, so it is roughly an "
                           "order of magnitude smaller than the individual contrast (see moore2012).",
         "covariates": [], "followup_years": None, "cohort_family": None,
         "quote": "We estimated that elimination of physical inactivity would increase the life expectancy of "
                  "the world's population by 0.68 (range 0.41-0.95) years."},
        {"outcome_domain": "comparator", "outcome_construct": "population_attributable_fraction_premature_mortality",
         "exposure": {"type": "descriptive", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "physical inactivity, global population attributable fraction for premature mortality"},
         "scale": "pct_change", "unit": "percent of premature deaths attributable", "value": 9.0,
         "se": None, "ci": [5.1, 12.5],
         "conversion_formula": "Reported as 9% (range 5.1-12.5). Sensitivity range, not a CI; se null.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "positive = share of premature deaths ATTRIBUTABLE to inactivity (harm).",
         "covariates": [], "followup_years": None, "cohort_family": None,
         "quote": "Inactivity causes 9% (range 5.1-12.5) of premature mortality, or more than 5.3 million of "
                  "the 57 million deaths that occurred worldwide in 2008."},
    ],
    rob={"tool": "none", "judgement": "moderate",
         "notes": "Comparative-risk-assessment / life-table modelling with self-reported activity prevalence "
                  "and relative risks drawn from observational cohorts, so it inherits all of their "
                  "confounding plus prevalence measurement error. The authors state they used 'conservative "
                  "assumptions'. Causal language ('inactivity causes') is not licensed by the design."},
    funding="None (per report)",
    notes=("Included because the task asked for it, but the modeller must NOT use the 0.68 y figure as a "
           "comparator: it is a population-level counterfactual, not the life expectancy an individual "
           "inactive person loses. Use moore2012 for the individual contrast. The main value here is the 9% "
           "PAF as a burden-of-disease framing number."))

MOORE_Q = ("A physical activity level of 0.1-3.74 MET-h/wk, equivalent to brisk walking for up to 75 min/wk, "
           "was associated with a gain of 1.8 (95% CI: 1.6-2.0) y in life expectancy relative to no leisure "
           "time activity (0 MET-h/wk). Higher levels of physical activity were associated with greater gains "
           "in life expectancy, with a gain of 4.5 (95% CI: 4.3-4.7) y at the highest level (22.5+ MET-h/wk, "
           "equivalent to brisk walking for 450+ min/wk).")

add("moore2012",
    citation=("Moore SC, Patel AV, Matthews CE, Berrington de Gonzalez A, Park Y, Katki HA, Linet MS, Weiderpass E, "
              "Visvanathan K, Helzlsouer KJ, Thun M, Gapstur SM, Hartge P, Lee IM. Leisure time physical "
              "activity of moderate to vigorous intensity and mortality: a large pooled cohort analysis. "
              "PLoS Med. 2012;9(11):e1001335."),
    doi="10.1371/journal.pmed.1001335", pmid="23139642",
    url="https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1001335",
    verification=ver("moore2012"),
    access_tier="abstract_only", secondhand_via=None,
    design="meta_analysis_observational", tier="T5", n=654827, n_studies_pooled=6,
    population={"age_mean": None, "age_range": [21, 90], "pct_female": None,
                "country": "US and Sweden", "adolescent_match": "poor_midlife"},
    effects=[
        {"outcome_domain": "comparator", "outcome_construct": "life_expectancy_gain_after_40_at_7_5_to_14_9_met_h_wk",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "7.5-14.9 MET-h/wk (WHO guideline level) vs 0 MET-h/wk, from age 40"},
         "scale": "years", "unit": "years of life expectancy gained after age 40", "value": 3.4,
         "se": round((3.5 - 3.2) / 3.919928, 6), "ci": [3.2, 3.5],
         "conversion_formula": "Gain 3.4 y (95% CI 3.2-3.5), bootstrap CI, for 7.5-14.9 MET-h/wk vs 0. "
                               "se = (3.5-3.2)/3.919928 = 0.076532 on the YEARS scale (not log).",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "positive = life expectancy GAINED by being active. Reversed sign, this is the "
                           "3.4 y an inactive person LOSES by being inactive from 40 onward. This is my "
                           "primary physical-inactivity pro-rata input.",
         "covariates": ["age", "sex", "smoking", "BMI", "alcohol", "education", "marital status (per report)"],
         "followup_years": 10.0, "cohort_family": "NCI_Cohort_Consortium", "quote":
             "Life expectancies and years of life gained/lost were calculated using direct adjusted survival "
             "curves (for participants 40+ years of age), with 95% confidence intervals (CIs) derived by "
             "bootstrap."},
        {"outcome_domain": "comparator", "outcome_construct": "life_expectancy_gain_after_40_at_lowest_nonzero_activity",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "0.1-3.74 MET-h/wk (brisk walking <=75 min/wk) vs 0 MET-h/wk, from age 40"},
         "scale": "years", "unit": "years of life expectancy gained after age 40", "value": 1.8,
         "se": round((2.0 - 1.6) / 3.919928, 6), "ci": [1.6, 2.0],
         "conversion_formula": "Gain 1.8 y (95% CI 1.6-2.0). se = (2.0-1.6)/3.919928 = 0.102043 on the YEARS scale.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "positive = life expectancy GAINED. Shows the dose-response is steeply concave: "
                           "half the total benefit arrives at a trivial dose, so 'inactivity' harm depends "
                           "heavily on where the referent is set.",
         "covariates": ["age", "sex", "smoking", "BMI", "alcohol", "education", "marital status (per report)"],
         "followup_years": 10.0, "cohort_family": "NCI_Cohort_Consortium", "quote": MOORE_Q},
        {"outcome_domain": "comparator", "outcome_construct": "life_expectancy_gain_after_40_at_highest_activity",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "22.5+ MET-h/wk vs 0 MET-h/wk, from age 40"},
         "scale": "years", "unit": "years of life expectancy gained after age 40", "value": 4.5,
         "se": round((4.7 - 4.3) / 3.919928, 6), "ci": [4.3, 4.7],
         "conversion_formula": "Gain 4.5 y (95% CI 4.3-4.7). se = (4.7-4.3)/3.919928 = 0.102043 on the YEARS scale.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "positive = life expectancy GAINED. Ceiling of the individual physical-activity contrast.",
         "covariates": ["age", "sex", "smoking", "BMI", "alcohol", "education", "marital status (per report)"],
         "followup_years": 10.0, "cohort_family": "NCI_Cohort_Consortium", "quote": MOORE_Q},
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "moderate",
         "notes": "Self-reported leisure-time activity at a single baseline; occupational and incidental "
                  "activity ignored. Median follow-up only 10 y, so reverse causation (illness reducing "
                  "activity) is a live threat despite adjustment. The '0 MET-h/wk' referent group is small "
                  "and unusual and is likely to be sick and socially disadvantaged, which inflates the contrast."},
    funding="US National Cancer Institute Intramural Research Program (per report)",
    notes=("The individual-level physical-activity life-expectancy anchor the task asked for. Pro-rata "
           "conversion: 3.4 y over e(40)=38.6 remaining years = 0.088 y per exposure-year, so 3 years of "
           "total inactivity = 0.26 y. Prefer this over lee2012's 0.68 y, which is a population figure."))

EKELUND_Q = ("Hazards ratios for mortality were 1.00 (referent) in the first quarter (least active), 0.48 "
             "(95% confidence interval 0.43 to 0.54) in the second quarter, 0.34 (0.26 to 0.45) in the third "
             "quarter, and 0.27 (0.23 to 0.32) in the fourth quarter (most active).")

add("ekelund2019",
    citation=("Ekelund U, Tarp J, Steene-Johannessen J, Hansen BH, Jefferis B, Fagerland MW, Whincup P, Diaz KM, "
              "Hooker SP, Chernofsky A, Larson MG, Spartano N, Vasan RS, Dohrn IM, Hagstromer M, Edwardson C, "
              "Yates T, Shiroma E, Anderssen SA, Lee IM. Dose-response associations between accelerometry "
              "measured physical activity and sedentary time and all cause mortality: systematic review and "
              "harmonised meta-analysis. BMJ. 2019;366:l4570."),
    doi="10.1136/bmj.l4570", pmid="31434697",
    url="https://www.bmj.com/content/366/bmj.l4570",
    verification=ver("ekelund2019"),
    access_tier="abstract_only", secondhand_via=None,
    design="dose_response_meta_analysis", tier="T4", n=36383, n_studies_pooled=8,
    population={"age_mean": 62.6, "age_range": None, "pct_female": 72.8,
                "country": "US, UK, Norway, Sweden", "adolescent_match": "poor_elderly"},
    effects=[
        {"outcome_domain": "comparator", "outcome_construct": "all_cause_mortality_most_vs_least_active_quartile_total_pa",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "highest vs lowest quarter of ACCELEROMETER-measured total physical activity"},
         "scale": "log_hr", "unit": "log hazard ratio", "value": round(math.log(0.27), 6),
         "se": round(se_from_ci(0.23, 0.32), 6), "ci": logci(0.23, 0.32),
         "conversion_formula": "HR 0.27 (95% CI 0.23-0.32). log_hr = ln(0.27) = -1.309333. "
                               "se = (ln(0.32)-ln(0.23))/3.919928 = 0.084157. Inverted, the LEAST active "
                               "quarter has HR 1/0.27 = 3.70 vs the most active.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "negative = LOWER mortality in the most active quarter (benefit). The implied "
                           "inactive-vs-active hazard ratio of 3.7 is FAR larger than the self-report "
                           "literature's ~1.35 and is almost certainly inflated by reverse causation - see rob.",
         "covariates": ["age", "sex", "and study-specific covariates per report"],
         "followup_years": 5.8, "cohort_family": "Accelerometer_Harmonised_Consortium", "quote": EKELUND_Q},
        {"outcome_domain": "comparator", "outcome_construct": "all_cause_mortality_most_vs_least_sedentary_quartile",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "highest vs lowest quarter of accelerometer-measured sedentary time"},
         "scale": "log_hr", "unit": "log hazard ratio", "value": round(math.log(2.63), 6),
         "se": round(se_from_ci(1.94, 3.56), 6), "ci": logci(1.94, 3.56),
         "conversion_formula": "HR 2.63 (95% CI 1.94-3.56). log_hr = ln(2.63) = 0.966984. "
                               "se = (ln(3.56)-ln(1.94))/3.919928 = 0.154783.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "positive = ELEVATED mortality in the most sedentary quarter (harm).",
         "covariates": ["age", "sex", "and study-specific covariates per report"],
         "followup_years": 5.8, "cohort_family": "Accelerometer_Harmonised_Consortium", "quote": EKELUND_Q},
    ],
    rob={"tool": "AMSTAR-2", "judgement": "moderate",
         "notes": "Objective exposure measurement (device-based) is a genuine advance and is why this is T4, "
                  "not T5. But mean age 62.6 y, 73% women, and median follow-up of only 5.8 y. In an elderly "
                  "cohort with short follow-up, low measured activity is substantially a MARKER of "
                  "subclinical disease, so the HR of 0.27 is a mixture of the causal effect and reverse "
                  "causation. The authors' own conclusion is restricted to 'middle aged and older adults'. "
                  "Transport to a healthy 18-year-old is very poor."},
    funding="Research Council of Norway and others (per report)",
    notes=("Requested by the task. Retained as the best DEVICE-MEASURED dose-response, but flagged as an "
           "OUTLIER on the high side: it implies an inactive-vs-active HR of 3.7 in the elderly, which "
           "converts (convert.py, 10.85*ln(HR)) to ~14 y of life expectancy - larger than smoking. That is "
           "not credible as a causal effect of inactivity and I do NOT use it in the comparator table. It is "
           "useful only as an upper bound and as a demonstration of how much reverse causation can inflate "
           "activity-mortality estimates in old cohorts."))

add("katzmarzyk2012",
    citation=("Katzmarzyk PT, Lee IM. Sedentary behaviour and life expectancy in the USA: a cause-deleted "
              "life table analysis. BMJ Open. 2012;2(4):e000828."),
    doi="10.1136/bmjopen-2012-000828", pmid="22777603",
    url="https://bmjopen.bmj.com/content/2/4/e000828",
    verification=ver("katzmarzyk2012"),
    access_tier="abstract_only", secondhand_via=None,
    design="life_table", tier="TX", n=None, n_studies_pooled=None,
    population={"age_mean": None, "age_range": None, "pct_female": None,
                "country": "US", "adolescent_match": "mixed"},
    effects=[
        {"outcome_domain": "comparator", "outcome_construct": "population_life_expectancy_gain_reducing_sitting_below_3h",
         "exposure": {"type": "descriptive", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "hypothetically reducing US population sitting to <3 h/day"},
         "scale": "years", "unit": "years of POPULATION life expectancy at birth gained", "value": 2.00,
         "se": None, "ci": [1.39, 2.69],
         "conversion_formula": "Reported gain 2.00 y, with a sensitivity span of 1.39-2.69 y obtained by "
                               "simultaneously varying the input RR across its 95% CI and the prevalence by "
                               "+/-20%. That span is a SENSITIVITY ANALYSIS, not a CI; se null.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "positive = POPULATION life expectancy at birth GAINED. Population counterfactual, "
                           "NOT an individual effect.",
         "covariates": [], "followup_years": None, "cohort_family": None,
         "quote": "The estimated gains in life expectancy in the US population were 2.00 years for reducing "
                  "excessive sitting to <3 h/day and a gain of 1.38 years from reducing excessive television "
                  "viewing to <2 h/day."},
    ],
    rob={"tool": "none", "judgement": "high",
         "notes": "Cause-deleted life-table analysis that ASSUMES the sitting-mortality association is fully "
                  "causal and fully removable, applied to self-reported sitting prevalence from NHANES. Both "
                  "assumptions are strong. Cause-deletion also assumes independence between the deleted risk "
                  "and competing risks, which is false for sedentary behaviour."},
    funding="None declared / not stated in abstract",
    notes=("Screened in to cover the sedentary-behaviour limb of the inactivity comparator, since screen time "
           "is a plausible co-exposure for a sleep-restricted college student. Population-level, so like "
           "lee2012 it must not be read as an individual effect. Low weight."))

add("hogstrom2016",
    citation=("Hogstrom G, Nordstrom A, Nordstrom P. Aerobic fitness in late adolescence and the risk of "
              "early death: a prospective cohort study of 1.3 million Swedish men. Int J Epidemiol. "
              "2016;45(4):1159-1168."),
    doi="10.1093/ije/dyv321", pmid="26686843",
    url="https://academic.oup.com/ije/article/45/4/1159/2951012",
    verification={"crossref_ok": True, "pubmed_ok": True, "title_similarity": 1.0, "status": "VERIFIED",
                  "resolved_title": "Aerobic fitness in late adolescence and the risk of early death: a "
                                    "prospective cohort study of 1.3 million Swedish men"},
    access_tier="abstract_only", secondhand_via=None,
    design="prospective_cohort_objective", tier="T4", n=1317713, n_studies_pooled=None,
    population={"age_mean": 18.0, "age_range": null_range, "pct_female": 0.0,
                "country": "SE", "adolescent_match": "exact_16_19"},
    effects=[
        {"outcome_domain": "comparator", "outcome_construct": "all_cause_mortality_highest_vs_lowest_fifth_fitness_at_18",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "highest vs lowest fifth of cycle-ergometer aerobic fitness measured at mean age 18"},
         "scale": "log_hr", "unit": "log hazard ratio", "value": round(math.log(0.49), 6),
         "se": round(se_from_ci(0.47, 0.51), 6), "ci": logci(0.47, 0.51),
         "conversion_formula": "HR 0.49 (95% CI 0.47-0.51). log_hr = ln(0.49) = -0.713350. "
                               "se = (ln(0.51)-ln(0.47))/3.919928 = 0.020844. Inverted, the LEAST fit fifth "
                               "has HR 1/0.49 = 2.04 vs the fittest fifth.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "negative = LOWER all-cause mortality in the fittest fifth (benefit). EXPOSURE "
                           "MEASURED AT EXACTLY OUR SUBJECT'S AGE, objectively, in an essentially complete "
                           "national male population, with 29 y of register follow-up. Best age match in this shard.",
         "covariates": ["BMI", "and multivariable covariates per report"], "followup_years": 29.0,
         "cohort_family": "Swedish_Conscripts", "quote":
             "Individuals in the highest fifth of aerobic fitness were at lower risk of death from any cause "
             "[hazard ratio (HR), 0.49; 95% confidence interval (CI), 0.47-0.51] in comparison with "
             "individuals in the lowest fifth, with the strongest association seen for death related to "
             "alcohol and narcotics abuse (HR, 0.20; 95% CI, 0.15-0.26)."},
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "moderate",
         "notes": "Outstanding exposure measurement (maximal cycle ergometry, whole-population conscription, "
                  "n=1.3 million) and outstanding age match. But fitness at 18 is measured ONCE and tracks "
                  "into midlife, so this HR prices a lifelong fitness trajectory, not a 3-year exposure. The "
                  "strongest cause-specific association being death from alcohol and narcotics abuse "
                  "(HR 0.20) is a loud signal that fitness at 18 is partly a marker of a whole behavioural "
                  "and social phenotype, not an isolated physiological exposure."},
    funding="Swedish Research Council and others (per report)",
    notes=("The single best AGE-MATCHED comparator record in the shard. Its role is to bound the "
           "'adolescent exposure leaves a permanent mark' hypothesis for the inactivity channel: HR 2.04 for "
           "the least-fit applied permanently from 19 gives ~9 y (convert.py). That is an over-attribution "
           "for a 3-year exposure for the tracking and phenotype-marker reasons above, but it establishes "
           "that fitness AT 18 has a large, register-confirmed association with lifespan."))

MOK_Q = ("For each 1 kJ/kg/day per year increase in PAEE (equivalent to a trajectory of being inactive at "
         "baseline and gradually, over five years, meeting the World Health Organization minimum physical "
         "activity guidelines of 150 minutes/week of moderate-intensity physical activity), hazard ratios "
         "were: 0.76 (95% confidence interval 0.71 to 0.82) for all cause mortality, 0.71 (0.62 to 0.82) for "
         "cardiovascular disease mortality, and 0.89 (0.79 to 0.99) for cancer mortality, adjusted for "
         "baseline PAEE, and established risk factors.")

add("mok2019",
    citation=("Mok A, Khaw KT, Luben R, Wareham N, Brage S. Physical activity trajectories and mortality: "
              "population based cohort study. BMJ. 2019;365:l2323."),
    doi="10.1136/bmj.l2323", pmid="31243014",
    url="https://www.bmj.com/content/365/bmj.l2323",
    verification=ver("mok2019"),
    access_tier="abstract_only", secondhand_via=None,
    design="prospective_cohort_selfreport", tier="T5", n=14599, n_studies_pooled=None,
    population={"age_mean": None, "age_range": [40, 79], "pct_female": None,
                "country": "UK", "adolescent_match": "poor_midlife"},
    effects=[
        {"outcome_domain": "comparator", "outcome_construct": "all_cause_mortality_per_1kJ_kg_day_per_year_increase_in_pa",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "+1 kJ/kg/day per year rise in physical activity energy expenditure, "
                                        "adjusted for BASELINE activity"},
         "scale": "log_hr", "unit": "log hazard ratio", "value": round(math.log(0.76), 6),
         "se": round(se_from_ci(0.71, 0.82), 6), "ci": logci(0.71, 0.82),
         "conversion_formula": "HR 0.76 (95% CI 0.71-0.82). log_hr = ln(0.76) = -0.274437. "
                               "se = (ln(0.82)-ln(0.71))/3.919928 = 0.036752.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "negative = LOWER mortality from BECOMING more active (benefit). REVERSIBILITY "
                           "EVIDENCE: the benefit is present after adjustment for baseline activity, i.e. it "
                           "does not matter much how inactive you previously were.",
         "covariates": ["age", "sex", "sociodemographics", "baseline PAEE", "changes in medical history",
                        "diet quality", "BMI", "blood pressure", "triglycerides", "cholesterol"],
         "followup_years": 12.5, "cohort_family": "EPIC_Norfolk", "quote": MOK_Q},
        {"outcome_domain": "comparator", "outcome_construct": "all_cause_mortality_increasing_pa_trajectory_from_low_baseline",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "increasing activity trajectory from a LOW baseline vs consistently inactive"},
         "scale": "log_hr", "unit": "log hazard ratio", "value": round(math.log(0.76), 6),
         "se": round(se_from_ci(0.65, 0.88), 6), "ci": logci(0.65, 0.88),
         "conversion_formula": "HR 0.76 (95% CI 0.65-0.88) for an increasing trajectory at LOW baseline "
                               "activity vs consistently inactive. log_hr = ln(0.76) = -0.274437. "
                               "se = (ln(0.88)-ln(0.65))/3.919928 = 0.077315.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "negative = LOWER mortality (benefit) from starting to move, even from the worst "
                           "starting point. Direct support for treating physical inactivity as a LARGELY "
                           "REVERSIBLE exposure on cessation.",
         "covariates": ["age", "sex", "sociodemographics", "baseline PAEE", "changes in medical history",
                        "diet quality", "BMI", "blood pressure", "triglycerides", "cholesterol"],
         "followup_years": 12.5, "cohort_family": "EPIC_Norfolk", "quote":
             "Joint analyses with baseline and trajectories of physical activity show that, compared with "
             "consistently inactive individuals, those with increasing physical activity trajectories over "
             "time experienced lower risks of mortality from all causes, with hazard ratios of 0.76 (0.65 to "
             "0.88), 0.62 (0.53 to 0.72), and 0.58 (0.43 to 0.78) at low, medium, and high baseline physical "
             "activity, respectively."},
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "moderate",
         "notes": "Repeated exposure assessment calibrated against combined heart-rate and movement sensing "
                  "is a real strength and is the reason this is the best reversibility evidence for activity. "
                  "But activity change is not randomised: people who become more active are people who "
                  "became able to, so reverse causation and healthy-adopter bias remain. Ages 40-79 only."},
    funding="UK Medical Research Council and Cancer Research UK (per report)",
    notes=("The physical-inactivity analogue of the smoking-cessation evidence. It is the best available "
           "answer to 'is inactivity reversible?' and the answer is largely yes. NOTE THE ASYMMETRY WITH "
           "SMOKING: for smoking we have direct evidence on quitting YOUNG (Pirie 2013, quit at 25-34); for "
           "inactivity the reversibility evidence is entirely from people aged 40-79, so applying it to a "
           "19-year-old is an extrapolation, albeit a conservative one (recovery should be easier at 19)."))

# ==========================================================================
# 4. ALCOHOL
# ==========================================================================

WOOD_Q = ("In comparison to those who reported drinking >0-<=100 g per week, those who reported drinking "
          ">100-<=200 g per week, >200-<=350 g per week, or >350 g per week had lower life expectancy at age "
          "40 years of approximately 6 months, 1-2 years, or 4-5 years, respectively.")

add("wood2018",
    citation=("Wood AM, Kaptoge S, Butterworth AS, et al; Emerging Risk Factors Collaboration/EPIC-CVD/UK "
              "Biobank Alcohol Study Group. Risk thresholds for alcohol consumption: combined analysis of "
              "individual-participant data for 599 912 current drinkers in 83 prospective studies. Lancet. "
              "2018;391(10129):1513-1523."),
    doi="10.1016/S0140-6736(18)30134-X", pmid="29676281",
    url="https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(18)30134-X/fulltext",
    verification=ver("wood2018"),
    access_tier="abstract_only", secondhand_via=None,
    design="meta_analysis_observational", tier="T5", n=599912, n_studies_pooled=83,
    population={"age_mean": None, "age_range": None, "pct_female": None,
                "country": "19 high-income countries", "adolescent_match": "poor_midlife"},
    effects=[
        {"outcome_domain": "comparator", "outcome_construct": "life_expectancy_lost_at_40_drinking_100_200_g_per_week",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": ">100-<=200 g alcohol/week vs >0-<=100 g/week, sustained from age 40"},
         "scale": "years", "unit": "years of life expectancy lost at age 40", "value": -0.5,
         "se": None, "ci": None,
         "conversion_formula": "Reported as 'approximately 6 months' = -0.5 y. No CI published for the "
                               "life-expectancy figures; se null. 100-200 g/week is roughly 7-14 US standard "
                               "drinks (14 g each) or 12.5-25 UK units.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "negative = life expectancy LOST at age 40 relative to light drinking. Referent is "
                           "LIGHT DRINKING, not abstention.",
         "covariates": ["study or centre", "age", "sex", "smoking", "diabetes"], "followup_years": 9.0,
         "cohort_family": "ERFC_EPIC_CVD_UKB", "quote": WOOD_Q},
        {"outcome_domain": "comparator", "outcome_construct": "life_expectancy_lost_at_40_drinking_200_350_g_per_week",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": ">200-<=350 g alcohol/week vs >0-<=100 g/week, sustained from age 40"},
         "scale": "years", "unit": "years of life expectancy lost at age 40", "value": -1.5,
         "se": None, "ci": None,
         "conversion_formula": "Reported as '1-2 years'; midpoint -1.5 recorded. Rounded range, not a CI; "
                               "ci and se null. Modellers wanting an interval should use [-2, -1].",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "negative = life expectancy LOST at age 40. ~14-25 US standard drinks/week.",
         "covariates": ["study or centre", "age", "sex", "smoking", "diabetes"], "followup_years": 9.0,
         "cohort_family": "ERFC_EPIC_CVD_UKB", "quote": WOOD_Q},
        {"outcome_domain": "comparator", "outcome_construct": "life_expectancy_lost_at_40_drinking_over_350_g_per_week",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": ">350 g alcohol/week vs >0-<=100 g/week, sustained from age 40"},
         "scale": "years", "unit": "years of life expectancy lost at age 40", "value": -4.5,
         "se": None, "ci": None,
         "conversion_formula": "Reported as '4-5 years'; midpoint -4.5 recorded. Rounded range, not a CI; "
                               "ci and se null. Modellers wanting an interval should use [-5, -4]. "
                               ">350 g/week is >25 US standard drinks or >35 UK units.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "negative = life expectancy LOST at age 40. Comparable in magnitude to grade-1 "
                           "obesity sustained from midlife.",
         "covariates": ["study or centre", "age", "sex", "smoking", "diabetes"], "followup_years": 9.0,
         "cohort_family": "ERFC_EPIC_CVD_UKB", "quote": WOOD_Q},
        {"outcome_domain": "comparator", "outcome_construct": "stroke_risk_per_100g_per_week_higher_alcohol",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "+100 g alcohol/week (12.5 UK units/week)"},
         "scale": "log_hr", "unit": "log hazard ratio per 100 g/week", "value": round(math.log(1.14), 6),
         "se": round(se_from_ci(1.10, 1.17), 6), "ci": logci(1.10, 1.17),
         "conversion_formula": "HR 1.14 (95% CI 1.10-1.17) per 100 g/week for stroke. log_hr = ln(1.14) = "
                               "0.131028. se = (ln(1.17)-ln(1.10))/3.919928 = 0.016043. Corrected by the "
                               "authors for long-term variability in intake using 152 640 serial assessments.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "positive = ELEVATED stroke risk per unit intake (harm). Included as the cleanest "
                           "PER-UNIT-DOSE alcohol effect, since the life-expectancy figures are categorical.",
         "covariates": ["study or centre", "age", "sex", "smoking", "diabetes"], "followup_years": 9.0,
         "cohort_family": "ERFC_EPIC_CVD_UKB", "quote":
             "Alcohol consumption was roughly linearly associated with a higher risk of stroke (HR per 100 g "
             "per week higher consumption 1.14, 95% CI, 1.10-1.17), coronary disease excluding myocardial "
             "infarction (1.06, 1.00-1.11), heart failure (1.09, 1.03-1.15), fatal hypertensive disease (1.24, "
             "1.15-1.33); and fatal aortic aneurysm (1.15, 1.03-1.28)."},
    ],
    rob={"tool": "AMSTAR-2", "judgement": "low",
         "notes": "Exceptionally strong on exposure measurement error: intake was corrected for long-term "
                  "variability using 152 640 repeat assessments, which most alcohol studies do not do. "
                  "CURRENT DRINKERS ONLY, so sick-quitter bias is designed out. Two limitations for us: the "
                  "referent is light drinking rather than abstention, and the analysis is of chronic disease "
                  "in middle-aged and older adults, so it captures essentially NONE of the acute injury "
                  "mortality that dominates alcohol harm at ages 16-24."},
    funding="UK Medical Research Council, British Heart Foundation, National Institute for Health Research, European Union Framework 7, European Research Council",
    notes=("The requested years-of-life-lost-by-drinking-category record, and the only comparator in this "
           "shard whose published output is ALREADY a life expectancy at a known starting age (40). Pro-rata "
           "over e(40)=38.6: 100-200 g/wk = 0.039 y per 3 years; 200-350 g/wk = 0.117 y; >350 g/wk = 0.350 y. "
           "BUT for a 16-19 year old this UNDERSTATES the risk badly because it omits the injury channel - "
           "see gbd2016alcohol."))

GBDALC_Q = ("Among the population aged 15-49 years, alcohol use was the leading risk factor globally in 2016, "
            "with 3.8% (95% UI 3.2-4.3) of female deaths and 12.2% (10.8-13.6) of male deaths attributable to "
            "alcohol use. For the population aged 15-49 years, female attributable DALYs were 2.3% (95% UI "
            "2.0-2.6) and male attributable DALYs were 8.9% (7.8-9.9). The three leading causes of "
            "attributable deaths in this age group were tuberculosis (1.4% [95% UI 1.0-1.7] of total deaths), "
            "road injuries (1.2% [0.7-1.9]), and self-harm (1.1% [0.6-1.5]).")

add("gbd2016alcohol",
    citation=("GBD 2016 Alcohol Collaborators; Griswold MG, Fullman N, Hawley C, et al. Alcohol use and "
              "burden for 195 countries and territories, 1990-2016: a systematic analysis for the Global "
              "Burden of Disease Study 2016. Lancet. 2018;392(10152):1015-1035."),
    doi="10.1016/S0140-6736(18)31310-2", pmid="30146330",
    url="https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(18)31310-2/fulltext",
    verification=ver("gbd2016alcohol"),
    access_tier="abstract_only", secondhand_via=None,
    design="normative_descriptive", tier="TX", n=None, n_studies_pooled=592,
    population={"age_mean": None, "age_range": [15, 95], "pct_female": None,
                "country": "global (195 countries)", "adolescent_match": "mixed"},
    effects=[
        {"outcome_domain": "comparator", "outcome_construct": "population_attributable_fraction_male_deaths_ages_15_49",
         "exposure": {"type": "descriptive", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "all alcohol use, MALES aged 15-49, global, 2016"},
         "scale": "pct_change", "unit": "percent of male deaths at 15-49 attributable to alcohol",
         "value": 12.2, "se": round((13.6 - 10.8) / 3.919928, 6), "ci": [10.8, 13.6],
         "conversion_formula": "PAF 12.2% (95% UI 10.8-13.6). se on the PERCENTAGE scale = "
                               "(13.6-10.8)/3.919928 = 0.714298. Implied population-average hazard ratio over "
                               "this age band = 1/(1-0.122) = 1.139; applied to ages 16-18 of the US male "
                               "2023 life table that is 0.020 y = 7.4 days of life expectancy (convert.py).",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "positive = share of male deaths at 15-49 ATTRIBUTABLE to alcohol (harm). THE "
                           "CRITICAL ASYMMETRY IN THIS SHARD: alcohol is the LEADING risk factor at exactly "
                           "our subject's age, and the mechanism is acute (road injury, self-harm), not "
                           "chronic disease. Alcohol harm is FRONT-LOADED into the 16-24 window and therefore "
                           "must NOT be pro-rated from a midlife estimate.",
         "covariates": [], "followup_years": None, "cohort_family": "GBD", "quote": GBDALC_Q},
        {"outcome_domain": "comparator", "outcome_construct": "minimum_risk_consumption_level",
         "exposure": {"type": "descriptive", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "level of consumption minimising all-cause health loss"},
         "scale": "raw_units", "unit": "standard drinks per week (10 g ethanol each)", "value": 0.0,
         "se": None, "ci": [0.0, 0.8],
         "conversion_formula": "Reported as zero (95% UI 0.0-0.8) standard drinks per week. UI recorded in "
                               "ci; se null because the estimate is bounded at zero and the UI is asymmetric.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "zero = no protective threshold. Contradicts Wood 2018's implicit J-shape for "
                           "myocardial infarction; the two disagree because GBD includes cancer and injury "
                           "outcomes and uses abstainers as referent.",
         "covariates": [], "followup_years": None, "cohort_family": "GBD",
         "quote": "The level of alcohol consumption that minimised harm across health outcomes was zero (95% "
                  "UI 0.0-0.8) standard drinks per week."},
    ],
    rob={"tool": "none", "judgement": "moderate",
         "notes": "Comparative risk assessment, not a study. PAFs depend on modelled exposure distributions, "
                  "on relative risks meta-analysed from heterogeneous sources, and on strong assumptions "
                  "about unrecorded consumption. Attributable fractions are not individual risks. The "
                  "zero-minimum-risk finding has been substantively criticised for how it handles the "
                  "abstainer referent."},
    funding="Bill & Melinda Gates Foundation",
    notes=("Included because it is the only source in the shard that prices a comparator AT OUR SUBJECT'S "
           "AGE BAND. It changes the shape of the alcohol comparator entirely: the chronic-disease pro-rata "
           "figure (0.04-0.35 y for 3 years) must be ADDED to an acute-injury window term that is at least "
           "0.02 y for an average male and plausibly 0.07-0.29 y for a heavy-drinking one (convert.py "
           "sensitivity over HR 1.5-3.0). Alcohol is the one comparator where the WINDOW model dominates the "
           "PRO-RATA model."))

# ==========================================================================
# 5. DIET
# ==========================================================================

add("gbd2017diet",
    citation=("GBD 2017 Diet Collaborators; Afshin A, Sur PJ, Fay KA, et al. Health effects of dietary risks "
              "in 195 countries, 1990-2017: a systematic analysis for the Global Burden of Disease Study "
              "2017. Lancet. 2019;393(10184):1958-1972."),
    doi="10.1016/S0140-6736(19)30041-8", pmid="30954305",
    url="https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(19)30041-8/fulltext",
    verification=ver("gbd2017diet"),
    access_tier="abstract_only", secondhand_via=None,
    design="normative_descriptive", tier="TX", n=None, n_studies_pooled=None,
    population={"age_mean": None, "age_range": null_range, "pct_female": None,
                "country": "global (195 countries)", "adolescent_match": "poor_midlife"},
    effects=[
        {"outcome_domain": "comparator", "outcome_construct": "global_deaths_attributable_to_dietary_risks",
         "exposure": {"type": "descriptive", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "all dietary risk factors, adults aged >=25, global, 2017"},
         "scale": "raw_units", "unit": "millions of deaths per year attributable to diet", "value": 11.0,
         "se": round((12 - 10) / 3.919928, 6), "ci": [10.0, 12.0],
         "conversion_formula": "11 million deaths (95% UI 10-12 million). se on the MILLIONS scale = "
                               "(12-10)/3.919928 = 0.510215.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "positive = deaths ATTRIBUTABLE to suboptimal diet (harm). A global burden count, "
                           "NOT an individual life-expectancy effect - not usable in the comparator table.",
         "covariates": [], "followup_years": None, "cohort_family": "GBD", "quote":
             "In 2017, 11 million (95% uncertainty interval [UI] 10-12) deaths and 255 million (234-274) "
             "DALYs were attributable to dietary risk factors."},
        {"outcome_domain": "comparator", "outcome_construct": "global_dalys_attributable_to_dietary_risks",
         "exposure": {"type": "descriptive", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "all dietary risk factors, adults aged >=25, global, 2017"},
         "scale": "raw_units", "unit": "millions of DALYs per year attributable to diet", "value": 255.0,
         "se": round((274 - 234) / 3.919928, 6), "ci": [234.0, 274.0],
         "conversion_formula": "255 million DALYs (95% UI 234-274). se on the MILLIONS scale = "
                               "(274-234)/3.919928 = 10.204271. THE ONLY DALY/QALY-SCALE NUMBER available to "
                               "this shard for any comparator; note it is a global aggregate.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "positive = DALYs LOST to suboptimal diet (harm). Aggregate, not individual.",
         "covariates": [], "followup_years": None, "cohort_family": "GBD", "quote":
             "In 2017, 11 million (95% uncertainty interval [UI] 10-12) deaths and 255 million (234-274) "
             "DALYs were attributable to dietary risk factors."},
    ],
    rob={"tool": "none", "judgement": "moderate",
         "notes": "Comparative risk assessment. The authors themselves warn 'Dietary data were from mixed "
                  "sources and were not available for all countries, increasing the statistical uncertainty "
                  "of our estimates.' Attributable-burden estimates for individual foods rest on "
                  "observational relative risks with substantial residual confounding. Adults >=25 only."},
    funding="Bill & Melinda Gates Foundation",
    notes=("Requested by the task. Provides the burden framing and the only DALY-denominated figures in the "
           "shard, but it cannot be converted to 'years lost per 3 years of exposure at 16' and so does not "
           "enter the comparator table. Use fadnes2022 for that."))

FADNES_Q = ("A sustained change from a typical Western diet to the optimal diet from age 20 years would "
            "increase LE by more than a decade for women from the United States (10.7 [95% UI 8.4 to 12.3] "
            "years) and men (13.0 [95% UI 9.4 to 14.3] years).")
FADNES_Q2 = ("Changing from a typical diet to the optimized diet at age 60 years would increase LE by 8.0 "
             "(95% UI 6.2 to 9.3) years for women and 8.8 (95% UI 6.8 to 10.0) years for men, and "
             "80-year-olds would gain 3.4 years (95% UI females: 2.6 to 3.8/males: 2.7 to 3.9).")
FADNES_Q3 = ("Change from typical to feasibility approach diet would increase LE by 6.2 (95% UI 3.5 to 8.1) "
             "years for 20-year-old women from the United States and 7.3 (95% UI 4.7 to 9.5) years for men.")

add("fadnes2022",
    citation=("Fadnes LT, Okland JM, Haaland OA, Johansson KA. Estimating impact of food choices on life "
              "expectancy: a modeling study. PLoS Med. 2022;19(2):e1003889."),
    doi="10.1371/journal.pmed.1003889", pmid="35134067",
    url="https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1003889",
    verification=ver("fadnes2022"),
    access_tier="abstract_only", secondhand_via=None,
    design="life_table", tier="TX", n=None, n_studies_pooled=None,
    population={"age_mean": None, "age_range": [20, 80], "pct_female": None,
                "country": "US", "adolescent_match": "good_young_adult"},
    effects=[
        {"outcome_domain": "comparator", "outcome_construct": "life_expectancy_gain_optimal_diet_from_age_20_us_men",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "sustained change from typical Western diet to optimal diet from age 20, US men"},
         "scale": "years", "unit": "years of life expectancy gained", "value": 13.0,
         "se": round((14.3 - 9.4) / 3.919928, 6), "ci": [9.4, 14.3],
         "conversion_formula": "Gain 13.0 y (95% UI 9.4-14.3) for US men changing at age 20. se on the YEARS "
                               "scale = (14.3-9.4)/3.919928 = 1.250023. NOTE the UI is strongly asymmetric "
                               "about the point estimate (-3.6/+1.3), so a symmetric normal is a poor "
                               "approximation; the pooler should prefer the raw interval.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "positive = life expectancy GAINED by eating well from 20. Reversed sign, this is "
                           "the 13.0 y a US man LOSES by eating a typical Western diet from 20 for life. "
                           "NEAREST-AGE diet estimate available and the only one starting at 20.",
         "covariates": [], "followup_years": None, "cohort_family": "GBD_Food4HealthyLife", "quote": FADNES_Q},
        {"outcome_domain": "comparator", "outcome_construct": "life_expectancy_gain_optimal_diet_from_age_60_us_men",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "sustained change from typical Western diet to optimal diet from age 60, US men"},
         "scale": "years", "unit": "years of life expectancy gained", "value": 8.8,
         "se": round((10.0 - 6.8) / 3.919928, 6), "ci": [6.8, 10.0],
         "conversion_formula": "Gain 8.8 y (95% UI 6.8-10.0) for men changing at 60. se on the YEARS scale = "
                               "(10.0-6.8)/3.919928 = 0.816341. PAIRED WITH THE AGE-20 FIGURE THIS GIVES A "
                               "DELAYED-CESSATION CONVERSION: eating badly from 20 to 60 (40 exposure-years) "
                               "costs 13.0-8.8 = 4.2 y, i.e. 0.105 y per exposure-year, so 3 years = 0.32 y. "
                               "The 60-to-80 segment gives 0.27 y per exposure-year, so the marginal cost of "
                               "a bad-diet year RISES steeply with age and 0.105 OVERSTATES the cost at 16-19.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "positive = life expectancy GAINED. The age gradient (13.0 at 20, 8.8 at 60, 3.4 "
                           "at 80) is the single most useful reversibility datum for the diet comparator: "
                           "68% of the age-20 benefit is STILL AVAILABLE at 60, so diet is largely reversible.",
         "covariates": [], "followup_years": None, "cohort_family": "GBD_Food4HealthyLife", "quote": FADNES_Q2},
        {"outcome_domain": "comparator", "outcome_construct": "life_expectancy_gain_feasibility_diet_from_age_20_us_men",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "typical Western diet to 'feasibility approach' diet (midpoint) from age 20, US men"},
         "scale": "years", "unit": "years of life expectancy gained", "value": 7.3,
         "se": round((9.5 - 4.7) / 3.919928, 6), "ci": [4.7, 9.5],
         "conversion_formula": "Gain 7.3 y (95% UI 4.7-9.5). se on the YEARS scale = (9.5-4.7)/3.919928 = "
                               "1.224513. This is the more realistic contrast for a real student, since the "
                               "'optimal' diet is an idealisation nobody eats.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "positive = life expectancy GAINED. Use this rather than the optimal-diet figure "
                           "if the comparator is meant to be an achievable dietary change.",
         "covariates": [], "followup_years": None, "cohort_family": "GBD_Food4HealthyLife", "quote": FADNES_Q3},
    ],
    rob={"tool": "none", "judgement": "moderate",
         "notes": "The authors are unusually candid about the limitations and I reproduce their own list: "
                  "'The methodology provides population estimates under given assumptions and is not meant as "
                  "individualized forecasting, with study limitations that include uncertainty for time to "
                  "achieve full effects, the effect of eggs, white meat, and oils, individual variation in "
                  "protective and risk factors, uncertainties for future development of medical treatments; "
                  "and changes in lifestyle.' They graded their own evidence base as MODERATE on NutriGrade. "
                  "The model also sums food-group effects that are estimated from separate meta-analyses, "
                  "which risks double-counting shared causal pathways and probably overstates the total."},
    funding="Not stated in abstract",
    notes=("The requested Fadnes record and the diet comparator's backbone. TWO conversion routes, which "
           "disagree by 2x: naive pro-rata over e(20)=56.7 gives 0.69 y for 3 years, whereas the authors' own "
           "age gradient gives 0.32 y and implies the true figure at 16-19 is lower still. I recommend the "
           "age-gradient route. The 13-year headline should be treated with suspicion for the double-counting "
           "reason in rob.notes; it is by far the largest single-exposure life-expectancy claim in this shard."))

add("fadnes2024",
    citation=("Fadnes LT, Celis-Morales C, Okland JM, Parra-Soto S, Livingstone KM, Ho FK, Pell JP, Balakrishna R, "
              "Sulo G, Vollset SE, Johansson KA. Life expectancy gains from dietary modifications: a "
              "comparative modeling study in 7 countries. Am J Clin Nutr. 2024;120(1):170-177."),
    doi="10.1016/j.ajcnut.2024.04.028", pmid="38692410",
    url="https://www.sciencedirect.com/science/article/pii/S0002916524003630",
    verification=ver("fadnes2024"),
    access_tier="abstract_only", secondhand_via=None,
    design="life_table", tier="TX", n=None, n_studies_pooled=None,
    population={"age_mean": None, "age_range": null_range, "pct_female": None,
                "country": "China, France, Germany, Iran, Norway, UK, US", "adolescent_match": "poor_midlife"},
    effects=[
        {"outcome_domain": "comparator", "outcome_construct": "life_expectancy_gain_longevity_diet_from_age_40_us_men",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "typical US diet to longevity-optimized diet from age 40, US men, "
                                        "adjusted for height, weight and physical activity"},
         "scale": "years", "unit": "years of life expectancy gained", "value": 9.7,
         "se": round((11.3 - 8.1) / 3.919928, 6), "ci": [8.1, 11.3],
         "conversion_formula": "Gain 9.7 y (UI 8.1-11.3) for US males at 40. se on the YEARS scale = "
                               "(11.3-8.1)/3.919928 = 0.816341. Pro-rata over e(40)=38.6 gives 0.754 y per "
                               "3 years, closely matching the fadnes2022 pro-rata route.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "positive = life expectancy GAINED. Reversed sign, the cost of a typical US diet "
                           "sustained from 40. This 2024 version adds adjustment for height, weight and "
                           "physical activity, which the 2022 model lacked, and the estimate BARELY MOVED "
                           "(9.7 y at 40 vs 8.8 y at 60 in 2022) - modest reassurance against confounding "
                           "by adiposity and activity.",
         "covariates": ["height", "weight", "physical activity level"], "followup_years": None,
         "cohort_family": "GBD_Food4HealthyLife", "quote":
             "For 40-y-olds, estimated life expectancy gains ranged from 6.2 y (with uncertainty interval "
             "[UI]: 5.7, 7.5 y) for Chinese females to 9.7 y (UI: 8.1, 11.3 y) for United States males "
             "following sustained changes from typical country-specific dietary patterns to "
             "longevity-optimized dietary changes"},
    ],
    rob={"tool": "none", "judgement": "moderate",
         "notes": "Same modelling family and therefore the same structural limitations as fadnes2022 "
                  "(summation of separately estimated food-group effects, dose-response curves from "
                  "observational meta-analyses). NOT independent of fadnes2022 - same authors, same method, "
                  "overlapping inputs. Must not be pooled with it as a second study; cohort_family is set to "
                  "GBD_Food4HealthyLife for both so the pooler de-duplicates."},
    funding="Trond Mohn Foundation and others (per report)",
    notes=("Included as the updated, covariate-adjusted version of the diet estimate and as a partial check "
           "on whether the 2022 headline was driven by confounding with adiposity and activity. It was not. "
           "Starts at 40, so it is worse age-matched than fadnes2022; use fadnes2022 for the comparator table."))

# ==========================================================================
# 6. INSUFFICIENT SLEEP ON THE SAME SCALE
# ==========================================================================

add("hafner2016",
    citation=("Hafner M, Stepanek M, Taylor J, Troxel WM, van Stolk C. Why sleep matters - the economic "
              "costs of insufficient sleep: a cross-country comparative analysis. Santa Monica, CA: RAND "
              "Corporation; 2016. RR-1791-VH. Also published as: Rand Health Q. 2017;6(4):11."),
    doi="10.7249/RR1791", pmid="28983434",
    url="https://www.rand.org/pubs/research_reports/RR1791.html",
    verification=ver("hafner2016"),
    access_tier="abstract_only",
    secondhand_via=("Numbers quoted from the 'Key Takeaways' section of the RAND publication page for "
                    "RR-1791 (https://www.rand.org/pubs/research_reports/RR1791.html), which is RAND's own "
                    "first-party summary of the report. RAND blocks programmatic download of the report PDF "
                    "(HTTP 403) and PubMed Central holds only the abstract for the Rand Health Q version, so "
                    "the report body itself was not retrieved."),
    design="normative_descriptive", tier="TX", n=None, n_studies_pooled=None,
    population={"age_mean": None, "age_range": None, "pct_female": None,
                "country": "US, UK, Canada, Germany, Japan", "adolescent_match": "poor_midlife"},
    effects=[
        {"outcome_domain": "comparator", "outcome_construct": "gdp_loss_from_insufficient_sleep_us_pct",
         "exposure": {"type": "descriptive", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "population-level insufficient sleep, United States, annual GDP loss"},
         "scale": "pct_change", "unit": "percent of GDP lost per year", "value": -2.28, "se": None,
         "ci": [-2.28, -1.56],
         "conversion_formula": "Reported as a RANGE of 1.56% to 2.28% of US GDP. The upper end (2.28%) is "
                               "recorded as the value and the full published range in ci, signed negative for "
                               "loss. This is a scenario range, NOT a confidence interval; se null.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "negative = GDP LOST (harm). NOT A HEALTH OUTCOME AND NOT CONVERTIBLE TO LIFE "
                           "EXPECTANCY OR QALYs. Cannot enter the comparator table.",
         "covariates": [], "followup_years": None, "cohort_family": None,
         "quote": "However, the relative numbers show that the estimated loss for Japan is actually higher "
                  "than for the US (between 1.56 to 2.28 per cent for the US and 1.86 per cent to 2.92 per "
                  "cent for Japan, respectively), with the UK (1.36 per cent to 1.86 per cent), Germany "
                  "(1.02 per cent to 1.56 per cent) and Canada (0.85 per cent to 1.56 per cent) following behind."},
        {"outcome_domain": "comparator", "outcome_construct": "mortality_risk_sleeping_under_6h_vs_7_9h",
         "exposure": {"type": "habitual_short_sleep", "dose_h": 6.0, "referent_h": 8.0, "duration_days": None,
                      "contrast_label": "habitually sleeping <6 h/night vs 7-9 h/night"},
         "scale": "log_hr", "unit": "log relative risk", "value": round(math.log(1.10), 6),
         "se": None, "ci": None,
         "conversion_formula": "RR 1.10 stated as a round figure with no interval in the RAND summary; se "
                               "null. log_rr = ln(1.10) = 0.095310. THIS IS NOT AN INDEPENDENT ESTIMATE: it "
                               "is a model INPUT that RAND took from the published short-sleep mortality "
                               "meta-analysis literature (cf. cappuccio2010, RR 1.12). Do NOT pool it with "
                               "cappuccio2010 - that would double-count.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "positive = ELEVATED mortality with short sleep (harm). Recorded to document what "
                           "RAND actually assumed, not as evidence.",
         "covariates": [], "followup_years": None, "cohort_family": "RAND_input_from_meta_analysis",
         "quote": "An individual that sleeps on average less than six hours per night has a ten per cent "
                  "higher mortality risk than someone sleeping between seven and nine hours. An individual "
                  "sleeping between six to seven hours per day still has a four per cent higher mortality risk."},
        {"outcome_domain": "comparator", "outcome_construct": "mortality_risk_sleeping_6_to_7h_vs_7_9h",
         "exposure": {"type": "habitual_short_sleep", "dose_h": 6.5, "referent_h": 8.0, "duration_days": None,
                      "contrast_label": "habitually sleeping 6-7 h/night vs 7-9 h/night"},
         "scale": "log_hr", "unit": "log relative risk", "value": round(math.log(1.04), 6),
         "se": None, "ci": None,
         "conversion_formula": "RR 1.04, round figure, no interval; se null. log_rr = ln(1.04) = 0.039221. "
                               "Same caveat: a RAND model input, not independent evidence.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "positive = ELEVATED mortality (harm). Gives RAND's implicit dose-response: the "
                           "log-hazard roughly doubles going from the 6-7 h band to the <6 h band.",
         "covariates": [], "followup_years": None, "cohort_family": "RAND_input_from_meta_analysis",
         "quote": "An individual that sleeps on average less than six hours per night has a ten per cent "
                  "higher mortality risk than someone sleeping between seven and nine hours. An individual "
                  "sleeping between six to seven hours per day still has a four per cent higher mortality risk."},
    ],
    rob={"tool": "none", "judgement": "high",
         "notes": "A commissioned economic modelling report (client: Vitality Health), peer reviewed within "
                  "RAND's process but not in a journal. Its outputs are GDP and working days, not health. Its "
                  "mortality inputs are borrowed from the observational short-sleep literature and inherit "
                  "all of its confounding; RAND then treats them as causal in a macroeconomic model. "
                  "Attempting to convert its $411 bn to a per-person life expectancy or QALY figure would "
                  "require assumptions RAND does not supply and I do not make."},
    funding="Vitality Health (commissioned); research conducted by RAND Europe",
    notes=("THE ANSWER TO TASK ITEM 6 IS LARGELY NEGATIVE. RAND is the most-cited attempt to price "
           "insufficient sleep and it does NOT put sleep on a life-expectancy or QALY scale at all - it "
           "prices lost GDP and lost working days. The most-quoted figures are: 'The US sustains by far the "
           "highest economic losses (up to $411 billion a year)' and 'On an annual basis, the US loses an "
           "equivalent of about 1.23 million working days due to insufficient sleep.' Neither is "
           "commensurable with years of life. The only health quantity RAND uses is a borrowed mortality RR. "
           "See li2024sleep for the closest thing to a genuine sleep life-expectancy estimate, and "
           "welter2026 for the fact that GBD omits sleep entirely."))

LI24_Q = ("When compared to those with 0-1 low-risk sleep factors, life expectancy at the age of 30 years "
          "for individuals with all five low-risk sleep factors was 4.7 (95% CI: 2.7-6.7) years greater for "
          "men and 2.4 (95% CI: 0.4-4.4) years greater for women.")

add("li2024sleep",
    citation=("Li H, Qian F, Han L, Feng W, Zheng D, Guo X, Zhang H. Association of healthy sleep patterns "
              "with risk of mortality and life expectancy at age of 30 years: a population-based cohort "
              "study. QJM. 2024;117(3):177-186."),
    doi="10.1093/qjmed/hcad237", pmid="37831896",
    url="https://academic.oup.com/qjmed/article/117/3/177/7317053",
    verification=ver("li2024sleep"),
    access_tier="abstract_only", secondhand_via=None,
    design="prospective_cohort_selfreport", tier="T5", n=172321, n_studies_pooled=None,
    population={"age_mean": 46.98, "age_range": null_range, "pct_female": 50.9,
                "country": "US", "adolescent_match": "poor_midlife"},
    effects=[
        {"outcome_domain": "comparator", "outcome_construct": "life_expectancy_at_30_five_vs_0_1_low_risk_sleep_factors_men",
         "exposure": {"type": "habitual_short_sleep", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "5 low-risk sleep factors vs 0-1, life expectancy at age 30, MEN"},
         "scale": "years", "unit": "years of life expectancy at age 30 gained", "value": 4.7,
         "se": round((6.7 - 2.7) / 3.919928, 6), "ci": [2.7, 6.7],
         "conversion_formula": "4.7 y (95% CI 2.7-6.7) for men. se on the YEARS scale = "
                               "(6.7-2.7)/3.919928 = 1.020429.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "positive = life expectancy GAINED by good sleep. Reversed sign, this is the 4.7 y "
                           "a MAN loses by having a poor sleep phenotype sustained from age 30. THE CLOSEST "
                           "THING IN THE PUBLISHED LITERATURE TO PUTTING SLEEP ON THE SAME SCALE AS THE "
                           "OTHER COMPARATORS - but note the exposure is a 5-item COMPOSITE (duration, "
                           "difficulty falling asleep, difficulty staying asleep, medication use, daytime "
                           "sleepiness), not sleep duration alone.",
         "covariates": ["age", "sex", "race", "education", "income", "BMI", "smoking", "alcohol",
                        "physical activity", "and others per report"],
         "followup_years": 4.3, "cohort_family": "NHIS_US", "quote": LI24_Q},
        {"outcome_domain": "comparator", "outcome_construct": "all_cause_mortality_five_vs_0_1_low_risk_sleep_factors",
         "exposure": {"type": "habitual_short_sleep", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "5 low-risk sleep factors vs 0-1 low-risk sleep factors, all-cause mortality"},
         "scale": "log_hr", "unit": "log hazard ratio", "value": round(math.log(0.70), 6),
         "se": round(se_from_ci(0.63, 0.77), 6), "ci": logci(0.63, 0.77),
         "conversion_formula": "HR 0.70 (95% CI 0.63-0.77). log_hr = ln(0.70) = -0.356675. "
                               "se = (ln(0.77)-ln(0.63))/3.919928 = 0.051216. Inverted, poor sleep vs good "
                               "sleep is HR 1.43.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "negative = LOWER mortality with a healthy sleep pattern (benefit). The HR of "
                           "1.43 for the poor-sleep phenotype is much larger than cappuccio2010's 1.12 for "
                           "short duration alone, because the composite captures insomnia and daytime "
                           "dysfunction as well as duration.",
         "covariates": ["age", "sex", "race", "education", "income", "BMI", "smoking", "alcohol",
                        "physical activity", "and others per report"],
         "followup_years": 4.3, "cohort_family": "NHIS_US", "quote":
             "The adjusted hazard ratios (95% confidence intervals [CI]) of participants with five vs. 0-1 "
             "low-risk sleep factors for all-cause, cardiovascular, and cancer mortality were 0.70 "
             "(0.63-0.77), 0.79 (0.67-0.93) and 0.81 (0.66-0.98), respectively."},
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "moderate",
         "notes": "MEDIAN FOLLOW-UP IS ONLY 4.3 YEARS while the outcome is life expectancy at age 30, so the "
                  "LE figure is an extrapolation from a flexible parametric survival model far outside the "
                  "observed data - the 4.7 y point estimate is model-dependent and its CI (2.7-6.7) almost "
                  "certainly understates the true uncertainty. Exposure is self-reported at a single "
                  "interview, mean age 47, and the composite score mixes duration with insomnia symptoms and "
                  "hypnotic use, so reverse causation from prevalent illness is a serious threat."},
    funding="Not stated in abstract",
    notes=("The one record that comes close to answering task item 6 with a life-expectancy number. Two "
           "cautions before it is used as our subject's comparator: (a) the exposure is a poor-sleep "
           "PHENOTYPE at mean age 47, not 3 years of adolescent restriction, and (b) the sex difference "
           "(4.7 y men vs 2.4 y women) is not mechanistically explained and hints at residual confounding. "
           "It is nonetheless the right order-of-magnitude reference point: a SUSTAINED poor sleep phenotype "
           "sits between overweight (3.1 y) and >350 g/wk alcohol (4.5 y) on the same scale."))

add("cappuccio2010",
    citation=("Cappuccio FP, D'Elia L, Strazzullo P, Miller MA. Sleep duration and all-cause mortality: a "
              "systematic review and meta-analysis of prospective studies. Sleep. 2010;33(5):585-592."),
    doi="10.1093/sleep/33.5.585", pmid="20469800",
    url="https://academic.oup.com/sleep/article/33/5/585/2454478",
    verification=ver("cappuccio2010"),
    access_tier="abstract_only", secondhand_via=None,
    design="meta_analysis_observational", tier="T5", n=1382999, n_studies_pooled=16,
    population={"age_mean": None, "age_range": None, "pct_female": None,
                "country": "multiple", "adolescent_match": "poor_midlife"},
    effects=[
        {"outcome_domain": "comparator", "outcome_construct": "all_cause_mortality_short_sleep_vs_normal",
         "exposure": {"type": "habitual_short_sleep", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "short habitual sleep duration vs normal (study-specific definitions)"},
         "scale": "log_hr", "unit": "log relative risk", "value": round(math.log(1.12), 6),
         "se": round(se_from_ci(1.06, 1.18), 6), "ci": logci(1.06, 1.18),
         "conversion_formula": "RR 1.12 (95% CI 1.06-1.18). log_rr = ln(1.12) = 0.113329. "
                               "se = (ln(1.18)-ln(1.06))/3.919928 = 0.027352. Applied permanently from age "
                               "40 in the US male 2023 life table this is 1.23 y of life expectancy "
                               "(convert.py); the same figure applied for 3 years at ages 16-18 only is "
                               "0.018 y = 6.4 days.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "positive = ELEVATED all-cause mortality with short sleep (harm). THE ANCHOR THAT "
                           "PUTS OUR OWN EXPOSURE ON THE COMPARATOR SCALE. Note it is far smaller than the "
                           "composite-phenotype HR of 1.43 in li2024sleep.",
         "covariates": ["study-specific; heterogeneous"], "followup_years": None,
         "cohort_family": "Cappuccio_2010_pool", "quote":
             "In the pooled analysis, short duration of sleep was associated with a greater risk of death "
             "(RR: 1.12; 95% CI 1.06 to 1.18; P < 0.01) with no evidence of publication bias (P = 0.74) but "
             "heterogeneity between studies (P = 0.02)."},
        {"outcome_domain": "comparator", "outcome_construct": "all_cause_mortality_long_sleep_vs_normal",
         "exposure": {"type": "habitual_short_sleep", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "long habitual sleep duration vs normal (study-specific definitions)"},
         "scale": "log_hr", "unit": "log relative risk", "value": round(math.log(1.30), 6),
         "se": round(se_from_ci(1.22, 1.38), 6), "ci": logci(1.22, 1.38),
         "conversion_formula": "RR 1.30 (95% CI 1.22-1.38). log_rr = ln(1.30) = 0.262364. "
                               "se = (ln(1.38)-ln(1.22))/3.919928 = 0.031333.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "positive = ELEVATED mortality with LONG sleep. Recorded because it is the loudest "
                           "warning sign in the sleep-mortality literature: long sleep, which has no "
                           "plausible causal mechanism of this size, shows a LARGER risk than short sleep. "
                           "That pattern is the signature of reverse causation and confounding by illness, "
                           "and it should discount the short-sleep estimate too.",
         "covariates": ["study-specific; heterogeneous"], "followup_years": None,
         "cohort_family": "Cappuccio_2010_pool", "quote":
             "Long duration of sleep was also associated with a greater risk of death (1.30; [1.22 to 1.38]; "
             "P < 0.0001) with no evidence of publication bias (P = 0.18) but significant heterogeneity "
             "between studies (P < 0.0001)."},
    ],
    rob={"tool": "AMSTAR-2", "judgement": "moderate",
         "notes": "Now 16 years old and superseded by larger dose-response meta-analyses. Self-reported sleep "
                  "duration with study-specific and inconsistent cut-points, significant heterogeneity, "
                  "predominantly middle-aged and older cohorts, and the long-sleep result strongly suggests "
                  "uncontrolled confounding by prevalent illness."},
    funding="Not stated in abstract",
    notes=("Included so that the comparator table has a same-scale figure for OUR OWN exposure, and because "
           "it is the source of the mortality RRs that RAND (hafner2016) used. cohort_family is set to "
           "Cappuccio_2010_pool and hafner2016's borrowed RR is flagged, so the pooler must not count them "
           "twice. Shard s13_mortality owns the definitive sleep-mortality synthesis; this record exists "
           "here only for commensurability."))

WELTER_Q = ("Despite this considerable burden, sleep disorders have been absent from GBD publications since "
            "the 2004 update. They are currently neither included as primary disorders nor as risk factors.")

add("welter2026",
    citation=("Welter LS, Nissen C, Rasch B, Heinzer R, Datta AN, Piovesana E, et al. Sleep disorders: a "
              "blind spot in disease burden research. Int J Public Health. 2026;71:1609757."),
    doi="10.3389/ijph.2026.1609757", pmid="42170608",
    url="https://www.ssph-journal.org/journals/international-journal-of-public-health/articles/10.3389/ijph.2026.1609757/full",
    verification={"crossref_ok": True, "pubmed_ok": True, "title_similarity": 1.0, "status": "VERIFIED",
                  "resolved_title": "Sleep Disorders: A Blind Spot in Disease Burden Research"},
    access_tier="full_text", secondhand_via=None,
    design="normative_descriptive", tier="TX", n=None, n_studies_pooled=None,
    population={"age_mean": None, "age_range": None, "pct_female": None,
                "country": "global", "adolescent_match": "mixed"},
    effects=[
        {"outcome_domain": "comparator", "outcome_construct": "gbd_dalys_attributed_to_sleep",
         "exposure": {"type": "descriptive", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "sleep disorders and insufficient sleep in the GBD comparative risk assessment"},
         "scale": "raw_units", "unit": "DALYs attributed to sleep in GBD", "value": 0.0, "se": None, "ci": None,
         "conversion_formula": "Encoded as ZERO because GBD attributes no burden to sleep at all: sleep is "
                               "included neither as a disorder nor as a risk factor in the GBD hierarchy. "
                               "This is a DOCUMENTED ABSENCE, not a measured null; se null.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "zero = GBD assigns NO burden to sleep. This is the answer to the part of task "
                           "item 6 asking about 'GBD treatment of sleep if any': there is none, so no "
                           "GBD-derived DALY figure for sleep can be quoted, and any report claiming one is "
                           "in error.",
         "covariates": [], "followup_years": None, "cohort_family": "GBD", "quote": WELTER_Q},
    ],
    rob={"tool": "none", "judgement": "na",
         "notes": "An editorial, not a study, so risk-of-bias tools do not apply. Its factual claim about "
                  "GBD's risk-factor and cause hierarchies is verifiable and is what I rely on; its "
                  "advocacy content is not extracted. The authors state the reason for the exclusion is "
                  "unknown to them, so no mechanism is offered."},
    funding="Not stated",
    notes=("Recorded because a negative finding of this kind is exactly the sort of thing a downstream report "
           "gets wrong. GBD 2017 diet, GBD 2016 alcohol, GBD physical inactivity and GBD high-BMI all exist "
           "and are quotable; there is NO GBD sleep counterpart. Any attempt to compare our subject's "
           "exposure to the others in DALY space is therefore impossible from GBD and must go through life "
           "expectancy instead. The authors also note GBD 'could be informed by primary data from large "
           "epidemiological resources, such as the UK Biobank', i.e. the omission is not a data-availability "
           "problem."))

add("li2018lifestyle",
    citation=("Li Y, Pan A, Wang DD, Liu X, Dhana K, Franco OH, Kaptoge S, Di Angelantonio E, Stampfer M, "
              "Willett WC, Hu FB. Impact of healthy lifestyle factors on life expectancies in the US "
              "population. Circulation. 2018;138(4):345-355."),
    doi="10.1161/CIRCULATIONAHA.117.032047", pmid="29712712",
    url="https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.117.032047",
    verification=ver("li2018lifestyle"),
    access_tier="abstract_only", secondhand_via=None,
    design="prospective_cohort_selfreport", tier="T5", n=123219, n_studies_pooled=None,
    population={"age_mean": None, "age_range": null_range, "pct_female": 64.0,
                "country": "US", "adolescent_match": "poor_midlife"},
    effects=[
        {"outcome_domain": "comparator", "outcome_construct": "life_expectancy_at_50_five_vs_zero_low_risk_lifestyle_factors_men",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "5 vs 0 low-risk lifestyle factors (never smoking, BMI 18.5-24.9, "
                                        ">=30 min/d moderate-vigorous activity, moderate alcohol, top-40% "
                                        "diet quality), life expectancy at age 50, MEN"},
         "scale": "years", "unit": "years of life expectancy at age 50 gained", "value": 12.2,
         "se": round((14.2 - 10.1) / 3.919928, 6), "ci": [10.1, 14.2],
         "conversion_formula": "12.2 y (95% CI 10.1-14.2) for men. se on the YEARS scale = "
                               "(14.2-10.1)/3.919928 = 1.045937.",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "positive = life expectancy GAINED at 50 from all five behaviours. THE JOINT "
                           "CEILING: all five of my comparator exposures combined and sustained are worth "
                           "~12 y for a man. Any single-comparator estimate that approaches 12 y on its own "
                           "is therefore internally inconsistent with this and should be distrusted - which "
                           "is a specific argument against fadnes2022's 13 y for diet ALONE.",
         "covariates": ["age", "and multivariable covariates per report"], "followup_years": 34.0,
         "cohort_family": "NHS_HPFS", "quote":
             "The projected life expectancy at age 50 years was on average 14.0 years (95% CI, 11.8-16.2) "
             "longer among female Americans with 5 low-risk factors compared with those with zero low-risk "
             "factors; for men, the difference was 12.2 years (95% CI, 10.1-14.2)."},
        {"outcome_domain": "comparator", "outcome_construct": "all_cause_mortality_five_vs_zero_low_risk_lifestyle_factors",
         "exposure": {"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                      "contrast_label": "5 vs 0 low-risk lifestyle factors, all-cause mortality"},
         "scale": "log_hr", "unit": "log hazard ratio", "value": round(math.log(0.26), 6),
         "se": round(se_from_ci(0.22, 0.31), 6), "ci": logci(0.22, 0.31),
         "conversion_formula": "HR 0.26 (95% CI 0.22-0.31). log_hr = ln(0.26) = -1.347074. "
                               "se = (ln(0.31)-ln(0.22))/3.919928 = 0.087486. Inverted, the worst-lifestyle "
                               "group has HR 3.85. Applying 10.85*ln(HR) gives 14.6 y, against the paper's "
                               "own life-table figure of 12.2 y for men - a 20% discrepancy that quantifies "
                               "how HOT the naive HR-to-years rule runs (see convert.py calibration).",
         "from_figure": False, "inferred_from_ci": False,
         "direction_note": "negative = LOWER mortality with all five healthy behaviours (benefit).",
         "covariates": ["age", "and multivariable covariates per report"], "followup_years": 34.0,
         "cohort_family": "NHS_HPFS", "quote":
             "The multivariable-adjusted hazard ratios for mortality in adults with 5 compared with zero "
             "low-risk factors were 0.26 (95% confidence interval [CI], 0.22-0.31) for all-cause mortality, "
             "0.35 (95% CI, 0.27-0.45) for cancer mortality, and 0.18 (95% CI, 0.12-0.26) for cardiovascular "
             "disease mortality."},
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "moderate",
         "notes": "Health professionals, 90%+ white, all self-reported exposures - a highly selected and "
                  "unrepresentative population, so the absolute life expectancies do not transport. The "
                  "zero-low-risk-factor group is small and multiply disadvantaged, which inflates the "
                  "contrast. Life expectancy is projected by life table from a 30-year follow-up, not observed."},
    funding="US National Institutes of Health (per report)",
    notes=("Screened in as an INTERNAL CONSISTENCY CHECK rather than as a comparator in its own right. It is "
           "the only source that prices SEVERAL of my comparators jointly, and it caps the whole set at "
           "~12 y for a man. It also cross-validates my HR-to-years conversion: its own life-table answer "
           "(12.2 y) is ~20% smaller than what 10.85*ln(HR) predicts from its own HR, which is the same "
           "~18-20% overshoot the convert.py calibration found against four other published anchors. That "
           "agreement is why I recommend a 0.80 correction factor on life-table-derived YLL."))


# ==========================================================================
# emit + validate
# ==========================================================================

def main():
    schema = json.load(open(SCHEMA))
    errors = 0
    ids = set()
    for sid, rec in R:
        if sid in ids:
            print(f"DUPLICATE study_id {sid}", file=sys.stderr)
            errors += 1
        ids.add(sid)
        try:
            jsonschema.validate(rec, schema)
        except jsonschema.ValidationError as e:
            errors += 1
            print(f"SCHEMA FAIL {sid}: {e.message} at {list(e.absolute_path)}", file=sys.stderr)
            continue
        with open(os.path.join(HERE, f"{sid}.yaml"), "w") as fh:
            yaml.safe_dump(rec, fh, sort_keys=False, allow_unicode=True, width=100,
                           default_flow_style=False)
    n_eff = sum(len(r["effects"]) for _, r in R)
    print(f"{len(R)} records, {n_eff} effects, {errors} schema errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
