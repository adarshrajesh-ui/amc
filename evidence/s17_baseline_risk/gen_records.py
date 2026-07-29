"""Generate the s17_baseline_risk YAML evidence records from a structured spec."""
import math
from pathlib import Path

import yaml

OUT = Path("/workspace/evidence/s17_baseline_risk")
SHARD = "s17_baseline_risk"


def se_from_ci(lo, hi):
    return (hi - lo) / 3.92


def logratio(v, lo, hi):
    return math.log(v), (math.log(hi) - math.log(lo)) / 3.92


def eff(construct, scale, value, se, ci, quote, *, unit=None, direction,
        exposure=None, conv=None, covariates=None, followup=None, cohort=None,
        from_figure=False, inferred=False, domain="baseline_risk"):
    return {
        "outcome_domain": domain,
        "outcome_construct": construct,
        "exposure": exposure or {"type": "descriptive", "dose_h": None, "referent_h": None,
                                 "duration_days": None,
                                 "contrast_label": "no sleep exposure; absolute baseline risk"},
        "scale": scale, "unit": unit, "value": value, "se": se, "ci": ci,
        "conversion_formula": conv, "from_figure": from_figure, "inferred_from_ci": inferred,
        "direction_note": direction, "covariates": covariates or [],
        "followup_years": followup, "cohort_family": cohort, "quote": quote,
    }


DESC = {"type": "descriptive", "dose_h": None, "referent_h": None, "duration_days": None,
        "contrast_label": "no sleep exposure; absolute baseline risk"}
SHORT = lambda label, dose=None, ref=None: {  # noqa: E731
    "type": "habitual_short_sleep", "dose_h": dose, "referent_h": ref,
    "duration_days": None, "contrast_label": label}

RECORDS = []


def add(**kw):
    kw.setdefault("shard", SHARD)
    kw.setdefault("secondhand_via", None)
    kw.setdefault("n_studies_pooled", None)
    kw.setdefault("tier", "TX")
    kw.setdefault("funding", None)
    RECORDS.append(kw)


# ------------------------------------------------------------------ 1. life tables
add(
    study_id="arias2025_uslifetable",
    citation=("Arias E, Xu JQ, Kochanek K. United States life tables, 2023. National Vital "
              "Statistics Reports. 2025 Jul 15;74(6):1-63. Hyattsville, MD: National Center "
              "for Health Statistics."),
    doi="10.15620/cdc/174591", pmid=None,
    url="https://www.cdc.gov/nchs/data/nvsr/nvsr74/nvsr74-06.pdf",
    verification={"crossref_ok": True, "pubmed_ok": None, "title_similarity": None,
                  "status": "VERIFIED",
                  "resolved_title": "United States Life Tables, 2023"},
    access_tier="full_text", design="life_table", n=None,
    population={"age_mean": None, "age_range": [0, 100], "pct_female": 0.0, "country": "US",
                "adolescent_match": "mixed"},
    effects=[
        eff("life_expectancy_at_age_19_male_years", "years", 57.6565, None, None,
            ("Table 2. Life table for males: United States, 2023 ... "
             "19-20 . . . 0.001061 98,810 105 98,757 5,697,034 57.7 "
             "(columns qx lx dx Lx Tx ex). Full-precision ex at age 19 from the official "
             "spreadsheet Table02.xlsx = 57.656521."),
            unit="years of remaining life expectancy at exact age 19",
            direction=("higher = longer remaining life. This is the DENOMINATOR the whole "
                       "project's life-expectancy losses are subtracted from: 57.6565 y = "
                       "691.88 months."),
            cohort="NVSS_2023"),
        eff("life_expectancy_at_birth_male_years", "years", 75.8178, None, None,
            ("Between 2022 and 2023, life expectancy at birth increased by 1.0 year for "
             "males (from 74.8 to 75.8) and by 0.9 year for females (80.2 to 81.1)."),
            unit="years of life expectancy at birth",
            direction="higher = longer life. Calibration target for gate G10.",
            cohort="NVSS_2023"),
        eff("probability_of_death_between_19_and_20_male", "probability", 0.001061, None, None,
            ("19-20 . . . 0.001061 98,810 105 98,757 5,697,034 57.7"),
            unit="one-year probability of death (qx) at exact age 19",
            direction=("higher = more death. Baseline all-cause hazard against which every "
                       "mortality hazard ratio in this project must be applied."),
            cohort="NVSS_2023"),
        eff("probability_male_survives_from_19_to_65", "probability", 0.7996, None, None,
            ("Computed from the published lx column of Table 2: lx(65)=79,011 divided by "
             "lx(19)=98,810 (full precision 79,011.383 / 98,809.875 = 0.79963)."),
            unit="probability", conv="l(65)/l(19) from NCHS Table 2 published lx column",
            direction=("higher = more likely to survive. A 19-year-old US male has only a "
                       "79.96% chance of reaching 65 and a 51.68% chance of reaching 80; "
                       "this is why unadjusted lifetime risks are inflated."),
            cohort="NVSS_2023"),
    ],
    rob={"tool": "none", "judgement": "na",
         "notes": ("Complete national vital registration; not a study with bias risk. Known "
                   "limitations: PERIOD table, so it assumes a 19-year-old will face 2023's "
                   "age-80 mortality in 2087; Medicare data used for ages 66-99; race/"
                   "ethnicity misclassification adjustment applies to subgroup tables only.")},
    funding="US federal (CDC/NCHS)",
    notes=("PRIMARY SOURCE for /workspace/data/lifetable_us_male.csv. Downloaded the official "
           "machine-readable Table02.xlsx from "
           "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Publications/NVSR/74-06/Table02.xlsx "
           "so no hand transcription was involved. Most recent United States Life Tables "
           "published as of retrieval (data year 2023, published 2025-07-15); the CDC life "
           "tables index lists no 2024 volume. NCHS closes the table at an open-ended "
           "'100 and older' interval, so single-year qx above 99 came from SSA "
           "(record ssa2023_periodlifetable). Recomputing ex from the published qx with "
           "a(x)=0.5 reproduces e0 to 0.0025 y, e19 to 0.0003 y and e65 to 0.0004 y."),
)

add(
    study_id="ssa2023_periodlifetable",
    citation=("U.S. Social Security Administration, Office of the Chief Actuary. Actuarial "
              "Life Table: Period Life Table, 2023, as used in the 2026 Trustees Report. "
              "Baltimore, MD: Social Security Administration; 2026."),
    doi=None, pmid=None, url="https://www.ssa.gov/oact/STATS/table4c6.html",
    verification={"crossref_ok": None, "pubmed_ok": None, "title_similarity": None,
                  "status": "UNVERIFIED",
                  "resolved_title": None},
    access_tier="full_text", design="life_table", n=None,
    population={"age_mean": None, "age_range": [0, 119], "pct_female": 0.0,
                "country": "US", "adolescent_match": "mixed"},
    effects=[
        eff("life_expectancy_at_age_19_male_years", "years", 57.62, None, None,
            "| 19 | 0.001138 | 98,822 | 57.62 | 0.000410 | 99,151 | 62.72 |",
            unit="years of remaining life expectancy at exact age 19",
            direction=("higher = longer remaining life. INDEPENDENT cross-check on the NCHS "
                       "value of 57.6565: agreement to 0.04 y, far inside the 0.3 y gate."),
            cohort="SSA_area_population_2023"),
        eff("life_expectancy_at_birth_male_years", "years", 75.79, None, None,
            "| 0 | 0.006015 | 100,000 | 75.79 | 0.005125 | 100,000 | 81.06 |",
            unit="years of life expectancy at birth",
            direction="higher = longer life. Independent cross-check on NCHS 75.8178.",
            cohort="SSA_area_population_2023"),
        eff("probability_of_death_between_110_and_111_male", "probability", 0.597297,
            None, None,
            "| 110 | 0.597297 | 2 | 1.13 | 0.597297 | 7 | 1.13 |",
            unit="one-year probability of death (qx) at exact age 110",
            direction=("higher = more death. Supplies the single-year tail qx for ages "
                       "100-119 that NCHS does not publish."),
            cohort="SSA_area_population_2023"),
    ],
    rob={"tool": "none", "judgement": "na",
         "notes": ("Official actuarial table. Population is the 'Social Security area' "
                   "population, which includes Puerto Rico, other territories, federal "
                   "employees abroad and insured non-citizens abroad, so it is NOT the US "
                   "resident population NCHS uses. qx for young adults differs from NCHS by "
                   "up to about 7% in relative terms (q19: SSA 0.001138 vs NCHS 0.001061), "
                   "though the absolute difference is 7.7e-5.")},
    funding="US federal (SSA)",
    notes=("VERIFICATION STATUS IS UNVERIFIED BY CONSTRUCTION, NOT BY FAILURE. SSA actuarial "
           "tables carry no DOI and are not indexed in PubMed, so neither Crossref nor "
           "PubMed can resolve them and both identifier fields are correctly null rather "
           "than guessed. Retrieval evidence: www.ssa.gov returns HTTP 403 to automated "
           "clients (Akamai), so the page was fetched through a text-extraction proxy "
           "(r.jina.ai) and parsed programmatically, with the parsed values cross-checked "
           "against a second independent fetch of the same URL. THIS IS NOT A PRIMARY-MODEL "
           "RECORD for gate G2 purposes: it supplies only qx above age 99, which contributes "
           "T(100)/l(0) = 0.0215 years (0.26 months) to e0 and 0.0218 years to e19. Setting "
           "the whole tail to qx=1 at age 100 would change e19 by 0.02 y. The two values "
           "reported here that ARE model-relevant (e0, e19) are corroborated to within 0.04 y "
           "by the fully verified NCHS record."),
)

# ------------------------------------------------------------------ 2. diabetes
add(
    study_id="gregg2014_diabetes_lifetime",
    citation=("Gregg EW, Zhuo X, Cheng YJ, Albright AL, Narayan KMV, Thompson TJ. Trends in "
              "lifetime risk and years of life lost due to diabetes in the USA, 1985-2011: a "
              "modelling study. Lancet Diabetes Endocrinol. 2014;2(11):867-874."),
    doi="10.1016/S2213-8587(14)70161-5", pmid="25128274",
    url=None,
    verification={"crossref_ok": True, "pubmed_ok": True, "title_similarity": None,
                  "status": "VERIFIED",
                  "resolved_title": ("Trends in lifetime risk and years of life lost due to "
                                     "diabetes in the USA, 1985-2011: a modelling study.")},
    access_tier="abstract_only", design="normative_descriptive", n=598216,
    population={"age_mean": None, "age_range": [20, 100], "pct_female": None, "country": "US",
                "adolescent_match": "fair_adult"},
    effects=[
        eff("lifetime_risk_diagnosed_diabetes_from_age_20_male", "probability", 0.402,
            se_from_ci(0.392, 0.413), [0.392, 0.413],
            ("On the basis of 2000-11 data, lifetime risk of diagnosed diabetes from age 20 "
             "years was 40.2% (95% CI 39.2-41.3) for men and 39.6% (38.6-40.5) for women, "
             "representing increases of 20 percentage points and 13 percentage points, "
             "respectively, since 1985-89."),
            unit="probability of ever being diagnosed with diabetes, from exact age 20",
            conv="se = (0.413 - 0.392)/3.92 = 0.00536 on the probability scale",
            direction=("higher = more disease. This is a BASELINE ABSOLUTE RISK, not an "
                       "effect of sleep. Competing mortality handled via a Markov model."),
            covariates=["sex", "race/ethnicity", "calendar period"],
            cohort="NHIS_linked_mortality"),
        eff("life_years_lost_if_diabetes_diagnosed_at_40_male", "years", -5.8,
            se_from_ci(-7.1, -4.6), [-7.1, -4.6],
            ("The number of life-years lost to diabetes when diagnosed at age 40 years "
             "decreased from 7.7 years (95% CI 6.5-9.0) in 1990-99 to 5.8 years (4.6-7.1) in "
             "2000-11 in men, and from 8.7 years (8.4-8.9) to 6.8 years (6.7-7.0) in women "
             "over the same period."),
            unit="years of life expectancy lost, men diagnosed at age 40, 2000-11 cohort",
            conv="se = (7.1 - 4.6)/3.92 = 0.638; sign flipped to negative = years lost",
            direction=("negative = life lost. DOWNSTREAM MULTIPLIER: once the model has an "
                       "absolute increase in diabetes incidence, this converts it to months "
                       "of life expectancy. 5.8 y = 69.6 months per incident case at 40."),
            cohort="NHIS_linked_mortality"),
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "moderate",
         "notes": ("Self-reported diagnosed diabetes only, so undiagnosed disease "
                   "(5.1 percentage points of US men per NHANES) is missed and type 1 is "
                   "included. Markov model with parametric incidence and mortality "
                   "regressions; model uncertainty is not in the CI. Period 2000-2011, now "
                   "superseded by Koyama 2022 for currency.")},
    funding="None declared",
    notes=("The seed paper named in the shard task; it is real and the numbers match. See "
           "koyama2022_diabetes_lifetime for the newer, LOWER estimate from the same data "
           "source. Age-specific cumulative incidence at 50/65/80 is NOT in this paper."),
)

add(
    study_id="koyama2022_diabetes_lifetime",
    citation=("Koyama AK, Cheng YJ, Brinks R, Xie H, Gregg EW, Hoyer A, Pavkov ME, "
              "Imperatore G. Trends in lifetime risk and years of potential life lost from "
              "diabetes in the United States, 1997-2018. PLoS One. 2022;17(5):e0268805."),
    doi="10.1371/journal.pone.0268805", pmid="35609056",
    url="https://pmc.ncbi.nlm.nih.gov/articles/PMC9129010/",
    verification={"crossref_ok": True, "pubmed_ok": True, "title_similarity": None,
                  "status": "VERIFIED",
                  "resolved_title": ("Trends in lifetime risk and years of potential life "
                                     "lost from diabetes in the United States, 1997-2018.")},
    access_tier="full_text", design="normative_descriptive", n=653811,
    population={"age_mean": 46.5, "age_range": [18, 84], "pct_female": 51.5, "country": "US",
                "adolescent_match": "fair_adult"},
    effects=[
        eff("lifetime_risk_diagnosed_diabetes_from_age_20_both_sexes_2015_2018",
            "probability", 0.328, se_from_ci(0.324, 0.332), [0.324, 0.332],
            ("LR for adults at age 20 increased from 31.7% (95% CI: 31.2-32.1%) in 1997-1999 "
             "to 40.7% (40.2-41.1%) in 2005-2009, then decreased to 32.8% (32.4-33.2%) in "
             "2015-2018."),
            unit=("probability of ever being diagnosed with diabetes between exact ages 20 "
                  "and 84"),
            conv="se = (0.332 - 0.324)/3.92 = 0.00204 on the probability scale",
            direction=("higher = more disease. MOST CURRENT lifetime-risk estimate; "
                       "multistate difference equation accounting for competing risks."),
            covariates=["age", "sex", "race/ethnicity", "survey period"],
            cohort="NHIS_linked_mortality"),
        eff("years_of_potential_life_lost_to_diabetes_age_20_2015_2018", "years", -6.2,
            se_from_ci(-6.4, -6.1), [-6.4, -6.1],
            ("YPLL significantly decreased over the study period, with the estimated YPLL "
             "due to diabetes for an adult aged 20 decreasing from 8.9 (8.7-9.1) in 1997-1999 "
             "to 6.2 (6.1-6.4) in 2015-2018 (p = 0.02)."),
            unit="years of potential life lost due to diabetes, adult aged 20",
            conv="se = (6.4 - 6.1)/3.92 = 0.0765; sign flipped to negative = years lost",
            direction="negative = life lost.",
            cohort="NHIS_linked_mortality"),
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "moderate",
         "notes": ("Same self-report limitation as Gregg 2014. NOT SEX-SPECIFIC: reports LR "
                   "for adults overall. Horizon truncated at age 84, which biases the "
                   "lifetime risk slightly downward. An erratum exists (PLoS One 2025 Jun "
                   "23;20(6):e0326955); the erratum was not retrieved, so the possibility "
                   "that it revises these figures is an open flag.")},
    funding="US federal (CDC)",
    notes=("SUPERSEDES Gregg 2014 for currency but not for sex-specificity. Because Gregg "
           "found men 40.2% versus women 39.6%, the male-specific 2015-2018 figure is likely "
           "close to 32.8%. Recommended range for a 19-year-old US male: 33-40%. Figure 1 "
           "shows LR by BASELINE age 18-60, which is the complement of the requested "
           "cumulative incidence by attained age; the figure's underlying values could not "
           "be extracted, which is why baseline_risks.yaml marks the 50/65/80 cutpoints "
           "DERIVED_BOUNDS."),
)

add(
    study_id="narayan2003_diabetes_lifetime",
    citation=("Narayan KMV, Boyle JP, Thompson TJ, Sorensen SW, Williamson DF. Lifetime risk "
              "for diabetes mellitus in the United States. JAMA. 2003;290(14):1884-1890."),
    doi="10.1001/jama.290.14.1884", pmid="14532317", url=None,
    verification={"crossref_ok": True, "pubmed_ok": True, "title_similarity": None,
                  "status": "VERIFIED",
                  "resolved_title": "Lifetime risk for diabetes mellitus in the United States."},
    access_tier="abstract_only", design="normative_descriptive", n=None,
    population={"age_mean": None, "age_range": [0, 80], "pct_female": None, "country": "US",
                "adolescent_match": "mixed"},
    effects=[
        eff("lifetime_risk_diagnosed_diabetes_from_birth_male", "probability", 0.328,
            None, None,
            ("The estimated lifetime risk of developing diabetes for individuals born in 2000 "
             "is 32.8% for males and 38.5% for females."),
            unit="probability of diagnosis between birth and age 80, males born in 2000",
            direction="higher = more disease. No CI reported, so se is null.",
            cohort="NHIS_linked_mortality"),
        eff("qaly_lost_if_diabetes_diagnosed_at_40_male", "years", -18.6, None, None,
            ("For example, we estimate that if an individual is diagnosed at age 40 years, "
             "men will lose 11.6 life-years and 18.6 quality-adjusted life-years and women "
             "will lose 14.3 life-years and 22.0 quality-adjusted life-years."),
            unit="quality-adjusted life-years lost, men diagnosed at 40",
            direction=("negative = QALYs lost. THE ONLY QALY QUANTITY THIS SHARD FOUND "
                       "anywhere in its domain. Use only as a downstream multiplier on an "
                       "absolute diabetes-incidence effect; it is not a sleep effect."),
            cohort="NHIS_linked_mortality"),
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "moderate",
         "notes": ("2003 vintage; the 11.6 life-years lost at diagnosis age 40 is roughly "
                   "double Gregg 2014's 5.8 for the same contrast, because diabetes mortality "
                   "fell sharply between the two analyses. Prefer Gregg/Koyama for the "
                   "mortality consequence and use this record only for the QALY ratio "
                   "18.6/11.6 = 1.60 QALYs lost per life-year lost.")},
    funding="US federal (CDC)",
    notes="Historical anchor; superseded by Gregg 2014 and Koyama 2022.",
)

add(
    study_id="narayan2007_bmi_diabetes",
    citation=("Narayan KMV, Boyle JP, Thompson TJ, Gregg EW, Williamson DF. Effect of BMI on "
              "lifetime risk for diabetes in the U.S. Diabetes Care. 2007;30(6):1562-1566."),
    doi="10.2337/dc06-2544", pmid="17372155", url=None,
    verification={"crossref_ok": True, "pubmed_ok": True, "title_similarity": None,
                  "status": "VERIFIED",
                  "resolved_title": "Effect of BMI on lifetime risk for diabetes in the U.S."},
    access_tier="abstract_only", design="normative_descriptive", n=780694,
    population={"age_mean": None, "age_range": [18, 80], "pct_female": None, "country": "US",
                "adolescent_match": "exact_16_19"},
    effects=[
        eff("lifetime_risk_diabetes_at_age_18_male_underweight", "probability", 0.076,
            None, None,
            ("Lifetime diabetes risk at 18 years of age increased from 7.6 to 70.3% between "
             "underweight and very obese men and from 12.2 to 74.4% for women."),
            unit="probability of ever being diagnosed with diabetes, from exact age 18",
            direction=("higher = more disease. Lower anchor of the BMI gradient at exactly "
                       "the subject's index age."),
            cohort="NHIS_linked_mortality"),
        eff("lifetime_risk_diabetes_at_age_18_male_very_obese", "probability", 0.703,
            None, None,
            ("Lifetime diabetes risk at 18 years of age increased from 7.6 to 70.3% between "
             "underweight and very obese men and from 12.2 to 74.4% for women."),
            unit="probability of ever being diagnosed with diabetes, from exact age 18",
            direction=("higher = more disease. Upper anchor of the BMI gradient. The 9.2-fold "
                       "spread across BMI at age 18 is the lever a sleep->BMI model should "
                       "move the subject along, INSTEAD of applying a diabetes hazard ratio "
                       "to a population-average lifetime risk."),
            cohort="NHIS_linked_mortality"),
        eff("lifetime_risk_difference_diabetes_at_age_65_male_very_obese_vs_normal",
            "probability", 0.239, None, None,
            ("At 65 years of age, compared with normal-weight male subjects, lifetime risk "
             "differences (percent) increased from 3.7 to 23.9 percentage points between "
             "overweight and very obese men and from 8.7 to 26.7 percentage points for women."),
            unit=("risk DIFFERENCE in probability points versus normal weight, assessed at "
                  "exact age 65 (not an absolute risk)"),
            direction=("positive = excess lifetime risk attributable to very obese BMI. "
                       "CRITICAL CONTRAST WITH THE AGE-18 ROWS: the BMI spread is 62.7 points "
                       "at age 18 but only 23.9 points at age 65, i.e. the same BMI shift buys "
                       "about 2.6x less diabetes risk when it happens in later life. This is "
                       "the quantitative argument that an exposure acting at ages 16-19 is "
                       "worth more than the same exposure acting at 65, and it is why this "
                       "shard's risks are indexed by age of assessment at all."),
            cohort="NHIS_linked_mortality"),
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "moderate",
         "notes": ("Only the extreme BMI categories are recoverable from the abstract; full "
                   "text is paywalled (diabetesjournals.org returns HTTP 403 and no PMC copy "
                   "exists), so normal-weight, overweight and obese values are NOT recorded "
                   "rather than interpolated. Self-reported diagnosed diabetes; BMI "
                   "self-reported in NHIS.")},
    funding="US federal (CDC)",
    notes=("MOST TRANSPORTABLE DIABETES RECORD IN THIS SHARD: index age 18 exactly matches "
           "the subject, and the stratifier is the mediator that short sleep is most reliably "
           "shown to move. Downstream use: combine with the sleep->BMI effect from shard s09 "
           "and Ward 2017's persistence coefficient rather than with a diabetes HR."),
)

add(
    study_id="gwira2024_diabetes_prevalence",
    citation=("Gwira JA, Fryar CD, Gu Q. Prevalence of Total, Diagnosed, and Undiagnosed "
              "Diabetes in Adults: United States, August 2021-August 2023. NCHS Data Brief "
              "No. 516. Hyattsville, MD: National Center for Health Statistics; 2024."),
    doi="10.15620/cdc/165794", pmid="40085919",
    url="https://www.cdc.gov/nchs/data/databriefs/db516.pdf",
    verification={"crossref_ok": True, "pubmed_ok": True, "title_similarity": None,
                  "status": "VERIFIED",
                  "resolved_title": ("Prevalence of Total, Diagnosed, and Undiagnosed "
                                     "Diabetes in Adults: United States, August "
                                     "2021-August 2023.")},
    access_tier="full_text", design="cross_sectional", n=2938,
    population={"age_mean": None, "age_range": [20, 999], "pct_female": None, "country": "US",
                "adolescent_match": "poor_midlife"},
    effects=[
        eff("total_diabetes_prevalence_us_male_age20plus", "probability", 0.180,
            se_from_ci(0.157, 0.204), [0.157, 0.204],
            "Men  . . . 1,306 18.0 (15.7-20.4) 1.1",
            unit="prevalence of total (diagnosed + undiagnosed) diabetes, men 20+",
            conv=("se = (0.204 - 0.157)/3.92 = 0.0120; NCHS also publishes SE = 1.1 "
                  "percentage points = 0.011, so the two agree"),
            direction="higher = more disease. Cross-sectional prevalence, NOT lifetime risk.",
            cohort="NHANES"),
        eff("undiagnosed_diabetes_prevalence_us_male_age20plus", "probability", 0.051,
            se_from_ci(0.036, 0.069), [0.036, 0.069],
            "Undiagnosed . . . 2,938 4.5 (3.3-5.9) 0.6 / Men  . . . 1,306 5.1 (3.6-6.9) 0.8",
            unit="prevalence of undiagnosed diabetes, men 20+",
            conv="se = (0.069 - 0.036)/3.92 = 0.00842",
            direction=("higher = more missed disease. CRITICAL CORRECTION FACTOR: the "
                       "diagnosed:total ratio in men is 12.9/18.0 = 0.717, so lifetime risks "
                       "built on DIAGNOSED diabetes (Gregg, Koyama, Narayan) understate the "
                       "lifetime risk of the biological disease by about 1/0.717 = 1.40x."),
            cohort="NHANES"),
        eff("total_diabetes_prevalence_age_40_59_both_sexes", "probability", 0.177,
            se_from_ci(0.147, 0.210), [0.147, 0.210],
            ("Total 20-39. . . 688 3.6 (2.0-5.9) 0.9 / 40-59. . . 861 17.7 (14.7-21.0) 1.4 / "
             "60 and older. . . 1,389 27.3 (23.0-31.9) 2.0"),
            unit="prevalence of total diabetes, adults 40-59, both sexes",
            conv="se = (0.210 - 0.147)/3.92 = 0.0161",
            direction=("higher = more disease. Supplies the age SHAPE for distributing a "
                       "lifetime risk over attained age. Prevalence at 20-39 is 3.6% and at "
                       "60+ is 27.3%."),
            cohort="NHANES"),
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "low",
         "notes": ("Nationally representative, measured (not self-reported) fasting glucose "
                   "and HbA1c. Cross-sectional, so it is not a cumulative incidence: it is "
                   "subject to survivor bias (people who developed diabetes and died are "
                   "absent) and to cohort effects. NHANES 2021-2023 had reduced response "
                   "after the pandemic pause.")},
    funding="US federal (CDC/NCHS)",
)

# ------------------------------------------------------------------ 3. hypertension
add(
    study_id="vasan2002_hypertension_lifetime",
    citation=("Vasan RS, Beiser A, Seshadri S, Larson MG, Kannel WB, D'Agostino RB, Levy D. "
              "Residual lifetime risk for developing hypertension in middle-aged women and "
              "men: The Framingham Heart Study. JAMA. 2002;287(8):1003-1010."),
    doi="10.1001/jama.287.8.1003", pmid="11866648", url=None,
    verification={"crossref_ok": True, "pubmed_ok": True, "title_similarity": None,
                  "status": "VERIFIED",
                  "resolved_title": ("Residual lifetime risk for developing hypertension in "
                                     "middle-aged women and men: The Framingham Heart Study.")},
    access_tier="abstract_only", design="prospective_cohort_objective", n=1298,
    population={"age_mean": None, "age_range": [55, 65], "pct_female": None,
                "country": "US", "adolescent_match": "poor_midlife"},
    effects=[
        eff("residual_lifetime_risk_hypertension_age_55_and_65", "probability", 0.90,
            None, None,
            ("The residual lifetime risks for developing hypertension and stage 1 high blood "
             "pressure or higher (greater-than-or-equal to 140/90 mm Hg regardless of "
             "treatment) were 90% in both 55- and 65-year-old participants."),
            unit="residual lifetime risk of hypertension from age 55 or 65",
            direction=("higher = more disease. WARNING: this is NOT competing-risk adjusted. "
                       "The paper's MAIN OUTCOME MEASURES reads 'Residual lifetime risk "
                       "(lifetime cumulative incidence not adjusted for competing causes of "
                       "mortality) for hypertension'. A 0.90 baseline is nearly saturated, so "
                       "applying any hazard ratio to it is arithmetically almost inert: "
                       "HR 1.20 moves it to 0.937, while naive multiplication gives an "
                       "impossible 1.08."),
            covariates=["sex", "calendar period"], followup=22.0,
            cohort="Framingham"),
        eff("lifetime_probability_of_antihypertensive_medication", "probability", 0.60,
            None, None,
            "The lifetime probability of receiving antihypertensive medication was 60%.",
            unit="lifetime probability of receiving antihypertensive medication",
            direction="higher = more treatment. No CI reported, so se is null.",
            cohort="Framingham"),
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "moderate",
         "notes": ("NOT adjusted for competing mortality, by the authors' own statement. "
                   "Index ages 55-65 are selected survivors who were still normotensive at "
                   "that age, so the estimand is not 'lifetime risk for a 19-year-old'. "
                   "Framingham is overwhelmingly white, New England, 1976-1998. JNC-VI "
                   "threshold >=140/90, which is NOT the current 2017 ACC/AHA >=130/80.")},
    funding="NIH/NHLBI (Framingham Heart Study contract)",
    notes=("The seed paper named in the task; real, and the 90% figure is correct. But it is "
           "the WRONG estimand for this project on three counts (unadjusted, wrong index age, "
           "obsolete threshold) and it is nearly saturated. For a sleep model the informative "
           "hypertension outcome is blood pressure LEVEL or AGE AT ONSET, not lifetime "
           "incidence. Use fryar2024_hypertension_prevalence for the contemporary, "
           "age-matched, current-definition denominator."),
)

add(
    study_id="fryar2024_hypertension_prevalence",
    citation=("Fryar CD, Kit B, Carroll MD, Afful J. Hypertension Prevalence, Awareness, "
              "Treatment, and Control Among Adults Age 18 and Older: United States, August "
              "2021-August 2023. NCHS Data Brief No. 511. Hyattsville, MD: National Center "
              "for Health Statistics; 2024."),
    doi=None, pmid="40085792",
    url="https://www.cdc.gov/nchs/data/databriefs/db511.pdf",
    verification={"crossref_ok": None, "pubmed_ok": True, "title_similarity": None,
                  "status": "VERIFIED",
                  "resolved_title": ("Hypertension Prevalence, Awareness, Treatment, and "
                                     "Control Among Adults Age 18 and Older: United States, "
                                     "August 2021-August 2023.")},
    access_tier="full_text", design="cross_sectional", n=2776,
    population={"age_mean": None, "age_range": [18, 999], "pct_female": 0.0, "country": "US",
                "adolescent_match": "mixed"},
    effects=[
        eff("hypertension_prevalence_us_male_18_39", "probability", 0.300,
            se_from_ci(0.262, 0.341), [0.262, 0.341],
            ("Men 18 and older (age adjusted). . . 2,776 48.8 (46.2-51.4) 1.2 / 18 and older "
             "(crude) . . . 2,776 50.8 (48.4-53.2) 1.1 / 18-39 . . . 787 30.0 (26.2-34.1) "
             "1.8 / 40-59 . . . 752 55.9 (50.6-61.1) 2.4 / 60 and older . . . 1,237 72.7 "
             "(68.8-76.4) 1.7"),
            unit="prevalence of hypertension in US men aged 18-39",
            conv=("se = (0.341 - 0.262)/3.92 = 0.0202; NCHS publishes SE = 1.8 percentage "
                  "points = 0.018, consistent"),
            direction=("higher = more disease. AGE-OVERLAPPING with the subject: 30.0% of US "
                       "men aged 18-39 already meet the 2017 ACC/AHA definition."),
            cohort="NHANES"),
        eff("hypertension_prevalence_us_male_40_59", "probability", 0.559,
            se_from_ci(0.506, 0.611), [0.506, 0.611],
            "40-59 . . . 752 55.9 (50.6-61.1) 2.4",
            unit="prevalence of hypertension in US men aged 40-59",
            conv="se = (0.611 - 0.506)/3.92 = 0.0268",
            direction="higher = more disease. Midlife denominator.",
            cohort="NHANES"),
        eff("hypertension_prevalence_us_male_60plus", "probability", 0.727,
            se_from_ci(0.688, 0.764), [0.688, 0.764],
            "60 and older . . . 1,237 72.7 (68.8-76.4) 1.7",
            unit="prevalence of hypertension in US men aged 60 and older",
            conv="se = (0.764 - 0.688)/3.92 = 0.0194",
            direction=("higher = more disease. Note the approach to saturation, which is why "
                       "hypertension incidence, not prevalence, is the identifiable outcome."),
            cohort="NHANES"),
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "low",
         "notes": ("Nationally representative with measured blood pressure. Definition is "
                   "SBP >=130 or DBP >=80 or on antihypertensive medication (2017 ACC/AHA), "
                   "which roughly doubles young-adult prevalence relative to the older "
                   ">=140/90 threshold; do NOT compare with Vasan 2002. Cross-sectional.")},
    funding="US federal (CDC/NCHS)",
    notes=("This NCHS Data Brief has no registered DOI, so the doi field is null rather than "
           "guessed; the record verifies through PubMed instead. PDF retrieved directly from "
           "cdc.gov and the figure data tables parsed programmatically."),
)

# ------------------------------------------------------------------ 4. CVD
add(
    study_id="lloydjones1999_chd_lifetime",
    citation=("Lloyd-Jones DM, Larson MG, Beiser A, Levy D. Lifetime risk of developing "
              "coronary heart disease. Lancet. 1999;353(9147):89-92."),
    doi="10.1016/S0140-6736(98)10279-9", pmid="10023892", url=None,
    verification={"crossref_ok": True, "pubmed_ok": True, "title_similarity": None,
                  "status": "VERIFIED",
                  "resolved_title": "Lifetime risk of developing coronary heart disease."},
    access_tier="abstract_only", design="prospective_cohort_objective", n=7733,
    population={"age_mean": None, "age_range": [40, 94], "pct_female": None, "country": "US",
                "adolescent_match": "poor_midlife"},
    effects=[
        eff("lifetime_risk_chd_from_age_40_male", "probability", 0.486,
            se_from_ci(0.458, 0.513), [0.458, 0.513],
            ("Lifetime risk of coronary heart disease at age 40 years was 48.6% (95% CI "
             "45.8-51.3) for men and 31.7% (29.2-34.2) for women. At age 70 years, lifetime "
             "risk was 34.9% (31.2-38.7) for men and 24.2% (21.4-27.0) for women."),
            unit="probability of first CHD event from exact age 40 to death",
            conv="se = (0.513 - 0.458)/3.92 = 0.0140 on the probability scale",
            direction=("higher = more disease. Competing-risk adjusted by multiple-decrement "
                       "life-table methods. CLOSEST published index age to the subject for a "
                       "hard coronary endpoint."),
            followup=None, cohort="Framingham"),
        eff("lifetime_risk_hard_cad_excluding_angina_from_age_40_male", "probability", 0.424,
            None, None,
            ("After we excluded isolated angina pectoris as an initial event, the lifetime "
             "risk of coronary artery disease events at age 40 years was 42.4% for men and "
             "24.9% for women."),
            unit="probability of first hard CAD event from exact age 40",
            direction=("higher = more disease. Narrower, MACE-like endpoint. No CI reported "
                       "for this variant, so se is null."),
            cohort="Framingham"),
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "moderate",
         "notes": ("Framingham: white, largely middle-class New England, examined 1971-1975 "
                   "with mid-20th-century background mortality. Index age 40 requires "
                   "multiplying by P(survive 19->40) = 0.9583 and adding the 19-40 incidence "
                   "the published figure excludes.")},
    funding="NIH/NHLBI",
)

add(
    study_id="lloydjones2006_cvd_lifetime",
    citation=("Lloyd-Jones DM, Leip EP, Larson MG, D'Agostino RB, Beiser A, Wilson PW, Wolf "
              "PA, Levy D. Prediction of lifetime risk for cardiovascular disease by risk "
              "factor burden at 50 years of age. Circulation. 2006;113(6):791-798."),
    doi="10.1161/CIRCULATIONAHA.105.548206", pmid="16461820", url=None,
    verification={"crossref_ok": True, "pubmed_ok": True, "title_similarity": None,
                  "status": "VERIFIED",
                  "resolved_title": ("Prediction of lifetime risk for cardiovascular disease "
                                     "by risk factor burden at 50 years of age.")},
    access_tier="abstract_only", design="prospective_cohort_objective", n=3564,
    population={"age_mean": 50.0, "age_range": [50, 95], "pct_female": 0.0, "country": "US",
                "adolescent_match": "poor_midlife"},
    effects=[
        eff("lifetime_risk_cvd_from_age_50_male", "probability", 0.517,
            se_from_ci(0.493, 0.542), [0.493, 0.542],
            ("At 50 years of age, lifetime risks were 51.7% (95% CI, 49.3 to 54.2) for men "
             "and 39.2% (95% CI, 37.0 to 41.4) for women, with median survivals of 30 and 36 "
             "years, respectively."),
            unit="probability of first atherosclerotic CVD event from exact age 50 to age 95",
            conv="se = (0.542 - 0.493)/3.92 = 0.0125 on the probability scale",
            direction=("higher = more disease. Death free of CVD treated as a competing "
                       "event."),
            covariates=["blood pressure", "total cholesterol", "diabetes", "smoking"],
            cohort="Framingham"),
        eff("lifetime_risk_cvd_from_age_50_male_all_risk_factors_optimal", "probability",
            0.052, None, None,
            ("Compared with participants with > or =2 major risk factors, those with optimal "
             "levels had substantially lower lifetime risks (5.2% versus 68.9% in men, 8.2% "
             "versus 50.2% in women) and markedly longer median survivals (>39 versus 28 "
             "years in men, >39 versus 31 years in women)."),
            unit="probability of first CVD event from age 50, men with all-optimal risk factors",
            direction=("higher = more disease. LOWER end of a 13-fold gradient. No CI "
                       "reported for the strata, so se is null."),
            cohort="Framingham"),
        eff("lifetime_risk_cvd_from_age_50_male_two_or_more_major_risk_factors",
            "probability", 0.689, None, None,
            ("Compared with participants with > or =2 major risk factors, those with optimal "
             "levels had substantially lower lifetime risks (5.2% versus 68.9% in men, 8.2% "
             "versus 50.2% in women) and markedly longer median survivals (>39 versus 28 "
             "years in men, >39 versus 31 years in women)."),
            unit=("probability of first CVD event from age 50, men with >=2 major risk "
                  "factors"),
            direction=("higher = more disease. UPPER end of the gradient. THE KEY RECORD FOR "
                       "MODELLING SLEEP THROUGH MEDIATORS: chronic sleep restriction is "
                       "hypothesised to move blood pressure, glucose and adiposity, so a "
                       "partial shift along the 5.2%-to-68.9% gradient is a better-identified "
                       "construction than applying a CVD hazard ratio to the 51.7% "
                       "population average, and it automatically respects risk-ratio "
                       "compression near a saturated baseline."),
            cohort="Framingham"),
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "moderate",
         "notes": ("Framingham; index age 50 conditional on being CVD-free at 50, i.e. "
                   "selected survivors. Risk-factor strata are observational, so the "
                   "5.2%-vs-68.9% contrast is confounded and must not be read as the causal "
                   "effect of changing risk factors.")},
    funding="NIH/NHLBI",
)

add(
    study_id="wilkins2012_cvd_lifetime",
    citation=("Wilkins JT, Ning H, Berry J, Zhao L, Dyer AR, Lloyd-Jones DM. Lifetime risk "
              "and years lived free of total cardiovascular disease. JAMA. "
              "2012;308(17):1795-1801."),
    doi="10.1001/jama.2012.14312", pmid="23117780",
    url="https://pmc.ncbi.nlm.nih.gov/articles/PMC3748966/",
    verification={"crossref_ok": True, "pubmed_ok": True, "title_similarity": None,
                  "status": "VERIFIED",
                  "resolved_title": ("Lifetime risk and years lived free of total "
                                     "cardiovascular disease.")},
    access_tier="abstract_only", design="meta_analysis_observational", n=None,
    n_studies_pooled=5,
    population={"age_mean": None, "age_range": [45, 95], "pct_female": None, "country": "US",
                "adolescent_match": "poor_midlife"},
    effects=[
        eff("lifetime_risk_total_cvd_from_age_45_male", "probability", 0.603,
            se_from_ci(0.593, 0.612), [0.593, 0.612],
            ("At an index age of 45 years, overall lifetime risk for total CVD was 60.3% "
             "(95% CI, 59.3%-61.2%) for men and 55.6% (95% CI, 54.5%-56.7%) for women. Men "
             "had higher lifetime risk estimates than women across all index ages."),
            unit=("probability of any total CVD event (CHD, stroke, heart failure, other CVD "
                  "death) from exact age 45 to age 95"),
            conv="se = (0.612 - 0.593)/3.92 = 0.00485 on the probability scale",
            direction=("higher = more disease. PREFERRED CENTRAL ESTIMATE for MACE-like "
                       "lifetime risk in a US male: broadest endpoint, 5 pooled cohorts, up "
                       "to 905,115 person-years."),
            covariates=["blood pressure", "total cholesterol", "diabetes", "smoking"],
            cohort="pooled_NHLBI_5cohorts"),
        eff("years_lived_free_of_cvd_gained_with_optimal_risk_factors", "years", 14.0,
            None, None,
            ("Compared with participants with at least 2 major risk factors, those with an "
             "optimal risk factor profile lived up to 14 years longer free of total CVD."),
            unit="years of additional CVD-free life with an optimal risk factor profile",
            direction=("positive = more healthy life. Upper bound ('up to'), no CI, so se is "
                       "null. Comparable in kind to Huang 2023's CVD-free life expectancy."),
            cohort="pooled_NHLBI_5cohorts"),
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "moderate",
         "notes": ("Pools Framingham, Framingham Offspring, ARIC, Chicago Heart Association "
                   "Detection Project in Industry and Cardiovascular Health Study, data from "
                   "1964-2008. COHORT-FAMILY OVERLAP: shares the Framingham sample with "
                   "lloydjones1999_chd_lifetime and lloydjones2006_cvd_lifetime, and the "
                   "ARIC sample with fang2025_dementia_lifetime. The pooler must not treat "
                   "these as independent (gate G6).")},
    funding="NIH/NHLBI",
)

add(
    study_id="khan2018_bmi_cvd_lifetime",
    citation=("Khan SS, Ning H, Wilkins JT, Allen N, Carnethon M, Berry JD, Sweis RN, "
              "Lloyd-Jones DM. Association of Body Mass Index With Lifetime Risk of "
              "Cardiovascular Disease and Compression of Morbidity. JAMA Cardiol. "
              "2018;3(4):280-287."),
    doi="10.1001/jamacardio.2018.0022", pmid="29490333",
    url="https://pmc.ncbi.nlm.nih.gov/articles/PMC5875319/",
    verification={"crossref_ok": True, "pubmed_ok": True, "title_similarity": None,
                  "status": "VERIFIED",
                  "resolved_title": ("Association of Body Mass Index With Lifetime Risk of "
                                     "Cardiovascular Disease and Compression of Morbidity.")},
    access_tier="abstract_only", design="meta_analysis_observational", n=190672,
    n_studies_pooled=10,
    population={"age_mean": 46.0, "age_range": [20, 79], "pct_female": 73.9, "country": "US",
                "adolescent_match": "poor_midlife"},
    effects=[
        eff("log_competing_hr_total_cvd_overweight_vs_normal_bmi_middle_aged_men",
            "log_hr", logratio(1.21, 1.14, 1.28)[0], logratio(1.21, 1.14, 1.28)[1],
            [math.log(1.14), math.log(1.28)],
            ("Compared with normal weight, among middle-aged men and women, competing hazard "
             "ratios for incident CVD were 1.21 (95% CI, 1.14-1.28) and 1.32 (95% CI, "
             "1.24-1.40), respectively, for overweight (BMI, 25.0-29.9), 1.67 (95% CI, "
             "1.55-1.79) and 1.85 (95% CI, 1.72-1.99) for obesity (BMI, 30.0-39.9), and 3.14 "
             "(95% CI, 2.48-3.97) and 2.53 (95% CI, 2.20-2.91) for morbid obesity (BMI, "
             ">=40.0)."),
            unit="log competing hazard ratio, BMI 25.0-29.9 vs 18.5-24.9, middle-aged men",
            conv=("log_hr = ln(1.21) = 0.1906; se = (ln(1.28) - ln(1.14))/3.92 = 0.02962"),
            direction=("positive = elevated CVD risk with higher BMI. Supplied so the "
                       "sleep->BMI->CVD path can be evaluated on the same competing-risk "
                       "scale as the absolute lifetime risks."),
            covariates=["age", "sex", "cohort"], cohort="pooled_10_US_cohorts"),
        eff("log_competing_hr_total_cvd_obese_vs_normal_bmi_middle_aged_men",
            "log_hr", logratio(1.67, 1.55, 1.79)[0], logratio(1.67, 1.55, 1.79)[1],
            [math.log(1.55), math.log(1.79)],
            ("... 1.67 (95% CI, 1.55-1.79) and 1.85 (95% CI, 1.72-1.99) for obesity (BMI, "
             "30.0-39.9) ..."),
            unit="log competing hazard ratio, BMI 30.0-39.9 vs 18.5-24.9, middle-aged men",
            conv="log_hr = ln(1.67) = 0.5128; se = (ln(1.79) - ln(1.55))/3.92 = 0.03664",
            direction="positive = elevated CVD risk with obesity.",
            covariates=["age", "sex", "cohort"], cohort="pooled_10_US_cohorts"),
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "moderate",
         "notes": ("73.9% female overall and mean age 46 for men, so this is a midlife "
                   "estimate. These are COMPETING (cause-specific Cox) hazard ratios, not "
                   "Fine-Gray subdistribution hazard ratios, so they cannot be read directly "
                   "as multipliers on absolute risk. Cohort overlap with wilkins2012.")},
    funding="NIH",
    notes=("Included in a baseline-risk shard because it is the conversion coefficient "
           "between a BMI shift and a CVD hazard shift, which is what lets the model use the "
           "well-identified sleep->BMI literature instead of the poorly identified "
           "sleep->CVD literature."),
)

# ------------------------------------------------------------------ 5. dementia
add(
    study_id="chene2015_dementia_lifetime",
    citation=("Chene G, Beiser A, Au R, Preis SR, Wolf PA, Dufouil C, Seshadri S. Gender and "
              "incidence of dementia in the Framingham Heart Study from mid-adult life. "
              "Alzheimers Dement. 2015;11(3):310-320."),
    doi="10.1016/j.jalz.2013.10.005", pmid="24418058",
    url="https://pmc.ncbi.nlm.nih.gov/articles/PMC4092061/",
    verification={"crossref_ok": True, "pubmed_ok": True, "title_similarity": None,
                  "status": "VERIFIED",
                  "resolved_title": ("Gender and incidence of dementia in the Framingham "
                                     "Heart Study from mid-adult life.")},
    access_tier="full_text", design="prospective_cohort_objective", n=7901,
    population={"age_mean": None, "age_range": [45, 105], "pct_female": 54.8, "country": "US",
                "adolescent_match": "poor_midlife"},
    effects=[
        eff("lifetime_risk_dementia_from_age_45_male_competing_adjusted", "probability",
            0.138, se_from_ci(0.122, 0.153), [0.122, 0.153],
            ("Table 2 (index age 45), Lifetime risk row: 507 | 270 | 76.5 [60.9-92.2] | 61.0 "
             "[50.4-71.5] | 0.11 | 22.7 [20.9-24.5] | 13.8 [12.2-15.3] | <0.001 "
             "(women then men, competing-mortality-unadjusted then competing-mortality-"
             "adjusted cumulative incidence). Text: 'LTR of dementia/AD at age 45 was 1 in 5 "
             "in women and 1 in 10 in men.'"),
            unit=("competing-mortality-adjusted lifetime risk of all-cause dementia from "
                  "exact age 45"),
            conv="se = (0.153 - 0.122)/3.92 = 0.00791 on the probability scale",
            direction=("higher = more disease. USE THIS, not the unadjusted 0.610 below."),
            covariates=["sex"], followup=None, cohort="Framingham"),
        eff("lifetime_risk_dementia_from_age_45_male_NOT_competing_adjusted", "probability",
            0.610, se_from_ci(0.504, 0.715), [0.504, 0.715],
            ("Table 2 (index age 45), Lifetime risk row, competing-mortality-UNADJUSTED "
             "cumulative incidence: men 61.0 [50.4-71.5]."),
            unit=("Kaplan-Meier lifetime risk of dementia from age 45, competing mortality "
                  "IGNORED"),
            conv="se = (0.715 - 0.504)/3.92 = 0.0538 on the probability scale",
            direction=("higher = more disease. RECORDED ONLY AS A NEGATIVE CONTROL. Same men, "
                       "same cohort, same endpoint as the record above: 61.0% unadjusted "
                       "versus 13.8% adjusted, a factor of 4.42. Any downstream dementia "
                       "denominator must state which of the two it is."),
            cohort="Framingham"),
        eff("lifetime_risk_alzheimer_from_age_45_male_competing_adjusted", "probability",
            0.103, se_from_ci(0.089, 0.118), [0.089, 0.118],
            ("Table 2 (index age 45), AD Lifetime risk row: 412 | 187 | 72.3 [54.0-90.7] | "
             "53.3 [41.1-65.5] | 0.09 | 19.5 [17.8-21.2] | 10.3 [8.9-11.8] | <0.001"),
            unit="competing-adjusted lifetime risk of Alzheimer's disease from exact age 45",
            conv="se = (0.118 - 0.089)/3.92 = 0.0074",
            direction="higher = more disease. Unadjusted counterpart is 53.3% (5.17x larger).",
            cohort="Framingham"),
        eff("lifetime_risk_dementia_from_age_65_male_competing_adjusted", "probability",
            0.155, se_from_ci(0.137, 0.172), [0.137, 0.172],
            ("Table 3 (index age 65), Lifetime risk row: 503 | 259 | 76.5 (60.8-92.1) | 60.7 "
             "(50.0-71.4) | 0.10 | 24.6 (22.7-24.5) | 15.5 (13.7-17.2) | <0.001"),
            unit="competing-adjusted lifetime risk of dementia from exact age 65",
            conv="se = (0.172 - 0.137)/3.92 = 0.00893",
            direction="higher = more disease.",
            cohort="Framingham"),
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "moderate",
         "notes": ("Framingham clinical dementia ascertainment, which is less complete than "
                   "active surveillance plus claims linkage; see fang2025_dementia_lifetime, "
                   "which gets 35% for men from ARIC. Predominantly white New England "
                   "sample. Index age 45, not 19.")},
    funding="NIH/NIA/NHLBI; Inserm",
    notes=("THE CANONICAL COMPETING-RISK DEMONSTRATION for this project. Tables extracted "
           "programmatically from the PMC full text (PMC4092061)."),
)

add(
    study_id="seshadri1997_dementia_lifetime",
    citation=("Seshadri S, Wolf PA, Beiser A, Au R, McNulty K, White R, D'Agostino RB. "
              "Lifetime risk of dementia and Alzheimer's disease. The impact of mortality on "
              "risk estimates in the Framingham Study. Neurology. 1997;49(6):1498-1504."),
    doi="10.1212/wnl.49.6.1498", pmid="9409336", url=None,
    verification={"crossref_ok": True, "pubmed_ok": True, "title_similarity": None,
                  "status": "VERIFIED",
                  "resolved_title": ("Lifetime risk of dementia and Alzheimer's disease. The "
                                     "impact of mortality on risk estimates in the Framingham "
                                     "Study.")},
    access_tier="abstract_only", design="prospective_cohort_objective", n=2611,
    population={"age_mean": 66.0, "age_range": [65, 100], "pct_female": 59.4, "country": "US",
                "adolescent_match": "poor_elderly"},
    effects=[
        eff("remaining_lifetime_risk_dementia_age_65_male", "probability", 0.109,
            se_from_ci(0.080, 0.138), [0.080, 0.138],
            ("In a 65-year-old man, the remaining lifetime risk of AD was 6.3% (95% CI, 3.9 "
             "to 8.7) and the remaining lifetime risk of developing any dementing illness was "
             "10.9% (95% CI, 8.0 to 13.8); corresponding risks for a 65-year-old woman were "
             "12% (95% CI, 9.2 to 14.8) and 19% (95% CI, 17.2 to 22.5)."),
            unit="remaining lifetime risk of any dementing illness for a 65-year-old man",
            conv="se = (0.138 - 0.080)/3.92 = 0.0148 on the probability scale",
            direction="higher = more disease. Competing mortality accounted for.",
            followup=20.0, cohort="Framingham"),
        eff("remaining_lifetime_risk_alzheimer_age_65_male", "probability", 0.063,
            se_from_ci(0.039, 0.087), [0.039, 0.087],
            ("In a 65-year-old man, the remaining lifetime risk of AD was 6.3% (95% CI, 3.9 "
             "to 8.7) ..."),
            unit="remaining lifetime risk of Alzheimer's disease for a 65-year-old man",
            conv="se = (0.087 - 0.039)/3.92 = 0.0122",
            direction="higher = more disease.",
            cohort="Framingham"),
        eff("cumulative_incidence_dementia_65_to_100_male_NOT_competing_adjusted",
            "probability", 0.328, None, None,
            ("The cumulative incidence between age 65 and 100 years was much higher: for AD, "
             "25.5% in men and 28.1% in women; for dementia, 32.8% in men and 45% in women. "
             "The actual remaining lifetime risk of AD or dementia varies with age, sex, and "
             "life expectancy and is lower than the hypothetical risk estimated by a "
             "cumulative incidence in the same population."),
            unit="cumulative incidence of dementia, men, age 65 to 100, mortality ignored",
            direction=("higher = more disease. NEGATIVE CONTROL: 32.8% ignoring competing "
                       "mortality versus 10.9% accounting for it, a factor of 3.01, in the "
                       "same men. The authors' framing: 'Conventional estimates of cumulative "
                       "incidence overestimate the risk when there is a substantial "
                       "probability of mortality due to competing causes.' No CI reported, "
                       "so se is null."),
            cohort="Framingham"),
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "moderate",
         "notes": ("1997 vintage, mean baseline age 66, only 198 incident dementia cases. "
                   "Elderly index age, so transportability to a 19-year-old is poor except "
                   "as a demonstration of the competing-risk principle.")},
    funding="NIH/NIA/NINDS",
)

add(
    study_id="fang2025_dementia_lifetime",
    citation=("Fang M, Hu J, Weiss J, Knopman DS, Albert M, Windham BG, Walker KA, Sharrett "
              "AR, Gottesman RF, Lutsey PL, Mosley T, Selvin E, Coresh J. Lifetime risk and "
              "projected burden of dementia. Nat Med. 2025;31(3):772-776."),
    doi="10.1038/s41591-024-03340-9", pmid="39806070",
    url="https://pmc.ncbi.nlm.nih.gov/articles/PMC12305800/",
    verification={"crossref_ok": True, "pubmed_ok": True, "title_similarity": None,
                  "status": "VERIFIED",
                  "resolved_title": "Lifetime risk and projected burden of dementia."},
    access_tier="full_text", design="prospective_cohort_objective", n=15043,
    population={"age_mean": None, "age_range": [55, 95], "pct_female": 55.1, "country": "US",
                "adolescent_match": "poor_elderly"},
    effects=[
        eff("lifetime_risk_dementia_after_age_55_male", "probability", 0.35,
            se_from_ci(0.33, 0.36), [0.33, 0.36],
            ("There was a higher lifetime risk of dementia in women versus men (48% (95% CI: "
             "46-50) versus 35% (95% CI: 33-36)) and Black versus White adults (44% (95% CI: "
             "41-46) versus 41% (95% CI: 40-43))."),
            unit="lifetime risk of dementia in men from age 55 to age 95",
            conv="se = (0.36 - 0.33)/3.92 = 0.00765 on the probability scale",
            direction=("higher = more disease. Competing risk of death accounted for. "
                       "CONTRADICTS Framingham by about 2.5x (35% vs 13.8% for men); the "
                       "authors attribute the gap to ascertainment completeness, not method."),
            covariates=["sex", "race", "APOE e4"], cohort="ARIC"),
        eff("lifetime_risk_dementia_after_age_55_both_sexes", "probability", 0.42,
            se_from_ci(0.41, 0.43), [0.41, 0.43],
            ("The lifetime risk of dementia after age 55 years was 42% (95% confidence "
             "interval: 41-43)."),
            unit="lifetime risk of dementia, both sexes, from age 55",
            conv="se = (0.43 - 0.41)/3.92 = 0.0051",
            direction="higher = more disease.",
            cohort="ARIC"),
        eff("lifetime_risk_dementia_white_men_apoe_e4_homozygous", "probability", 0.60,
            se_from_ci(0.49, 0.70), [0.49, 0.70],
            ("sex and race APOE e4 status Difference (2 alleles - 0 alleles) 0 alleles 1 "
             "allele 2 alleles White Women 45 (42, 48) 56 (51, 60) 64 (52, 73) 19 White Men "
             "31 (29, 34) 40 (37, 44) 60 (49, 70) 29 Black Women 44 (39, 48) 53 (48, 58) 67 "
             "(56, 76) 23 Black Men 34 (29, 38) 38 (33, 43) 39 (26, 51) 5 ... Estimates are "
             "reported as percentages and indicate the cumulative incidence at the age of "
             "last observation (up to age 95 years) after accounting for the competing risk "
             "of death."),
            unit="lifetime risk of dementia, White men with two APOE e4 alleles, from 55",
            conv="se = (0.70 - 0.49)/3.92 = 0.0536",
            direction=("higher = more disease. Genotype spread in White men is 31% (0 "
                       "alleles) to 60% (2 alleles), which is LARGER than any plausible "
                       "sleep effect and must be carried as effect-modification uncertainty."),
            cohort="ARIC"),
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "low",
         "notes": ("Best available US ascertainment: in-person cognitive assessment, "
                   "informant interview, hospitalisation and death records, plus Medicare "
                   "claims. Four US communities, so not nationally representative. Index age "
                   "55. COHORT-FAMILY OVERLAP with wilkins2012 (both include ARIC).")},
    funding="NIH (NHLBI, NIA, NINDS)",
    notes=("THE LARGEST SINGLE DENOMINATOR UNCERTAINTY IN THIS SHARD. Fang et al. note the "
           "discrepancy themselves: 'Previous studies suggest that 11-14% of men and 19-23% "
           "of women in the United States will develop dementia during their lives' and 'In "
           "the Framingham Heart Study, 14% of men and 23% of women developed dementia from "
           "age 45-105 years'. Male dementia lifetime risk is therefore 14%-35%. Carry both; "
           "do not collapse."),
)
add(
    study_id="hudomiet2025_dementia_lifetime",
    citation=("Hudomiet P, Hurd MD, Rohwedder S. Inequalities in the Duration and Lifetime "
              "Risk of Dementia in the United States. Demography. 2025;62(4):1389-1412."),
    doi="10.1215/00703370-12175489", pmid="40739976",
    url="https://pmc.ncbi.nlm.nih.gov/articles/PMC12370282/",
    verification={"crossref_ok": True, "pubmed_ok": True, "title_similarity": None,
                  "status": "VERIFIED",
                  "resolved_title": ("Inequalities in the Duration and Lifetime Risk of "
                                     "Dementia in the United States")},
    access_tier="full_text", design="prospective_cohort_objective", n=8814,
    population={"age_mean": None, "age_range": [70, 999], "pct_female": 55.0, "country": "US",
                "adolescent_match": "poor_elderly"},
    effects=[
        eff("dementia_probability_6mo_before_death_given_death_after_70_both_sexes",
            "probability", 0.413, se_from_ci(0.393, 0.432), [0.393, 0.432],
            ("We found a higher lifetime risk of dementia than found in earlier U.S. studies: "
             "41.3% (CI: 39.3% to 43.2%) of those who died after age 70 had dementia assessed "
             "at six months before death."),
            unit=("probability of having dementia six months before death, CONDITIONAL on "
                  "dying after age 70; both sexes"),
            conv="se = (0.432 - 0.393)/3.92 = 0.00995",
            direction=("higher = more disease. THE HIGHEST US DEMENTIA ESTIMATE THIS SHARD "
                       "FOUND, and the estimand is NOT a lifetime risk from a young index "
                       "age: it conditions on surviving to 70. Converting to the "
                       "unconditional risk this project needs requires multiplying by "
                       "S(19->70) = 0.7274 from this shard's life table, giving 30.0% both "
                       "sexes. That multiplication is exactly the competing-mortality "
                       "correction documented in competing_risk_method.md section 2."),
            covariates=["sex", "education", "race/ethnicity", "nativity", "lifetime earnings",
                        "marital status", "age at death", "stroke", "hypertension",
                        "diabetes", "heart problems", "survey wave"],
            cohort="HRS"),
        eff("dementia_probability_5y_before_death_given_death_after_70_both_sexes",
            "probability", 0.201, se_from_ci(0.186, 0.215), [0.186, 0.215],
            ("38.7% (CI: 36.8% to 40.5%), 33.6% (CI: 31.8% to 35.4%), and 20.1% (18.6% to "
             "21.5%) had dementia one, two, and five years before death, respectively."),
            unit=("probability of having dementia at least FIVE years before death, "
                  "conditional on dying after age 70; both sexes"),
            conv="se = (0.215 - 0.186)/3.92 = 0.0074",
            direction=("higher = more disease. THE DURATION-WEIGHTED FIGURE, AND THE ONE A "
                       "QALY MODEL SHOULD USE. 41.3% ever have dementia before death but only "
                       "20.1% live with it for 5+ years, so roughly half of all dementia in "
                       "this cohort is a terminal-phase phenomenon of under 5 years. A model "
                       "that multiplies a 41% lifetime risk by a multi-year disability weight "
                       "would roughly double the true QALY loss."),
            covariates=["sex", "education", "race/ethnicity", "age at death", "stroke"],
            cohort="HRS"),
        eff("dementia_risk_difference_women_minus_men_6mo_before_death", "probability", 0.064,
            se_from_ci(0.033, 0.095), [0.033, 0.095],
            ("Table 2. OLS regressions of the probability of having dementia six months and "
             "five years before death. 5 years / 6 months: Women 0.057 ** [0.033; 0.081] / "
             "0.064 ** [0.033; 0.095]"),
            unit=("adjusted risk difference, women minus men, in probability of dementia six "
                  "months before death"),
            conv=("se = (0.095 - 0.033)/3.92 = 0.0158. THIS SHARD'S DERIVATION of the male "
                  "level: applying the 6.4-point female excess to the published 41.3% "
                  "marginal at the published sample weights (45.0% male, 55.0% female) gives "
                  "men approx 41.3 - 0.55*6.4 = 37.8% and women approx 44.2%. Approximate, "
                  "because the 6.4 points is a covariate-adjusted coefficient rather than a "
                  "marginal difference; the paper does not publish the male level directly."),
            inferred=True,
            direction=("positive = higher risk in women, so MALE RISK IS LOWER, which matters "
                       "because the subject is male and this is the only sex information the "
                       "paper reports. Men approx 37.8% conditional on dying after 70, i.e. "
                       "approx 27.5% unconditional from age 19 after multiplying by "
                       "S(19->70) = 0.7274."),
            covariates=["education", "race/ethnicity", "nativity", "lifetime earnings",
                        "marital status", "age at death", "stroke", "hypertension",
                        "diabetes", "heart problems", "survey wave"],
            cohort="HRS"),
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "moderate",
         "notes": ("Dementia status is imputed by a joint longitudinal latent-variable model "
                   "of cognition, dementia and survival rather than clinically diagnosed, so "
                   "the estimates inherit that model's assumptions. The authors validate it "
                   "against ADAMS, the HRS clinical-assessment substudy, and match it closely "
                   "at ages 85+ (0.359 vs ADAMS 0.358) where the widely used calibrated "
                   "cutoff method underpredicts by 4.8 points (0.310) - this is a genuine "
                   "strength over the comparison methods. Sample is decedents aged 70+ from "
                   "HRS waves 2000-2016, so the estimand is inherently conditional on "
                   "surviving to 70 and cannot be read as a lifetime risk from a young age. "
                   "No adolescent content whatsoever.")},
    funding="NIA / RAND (per paper)",
    notes=("THIS RECORD IS THE ARBITRATOR FOR THIS SHARD'S LARGEST DISAGREEMENT. The paper's "
           "discussion diagnoses, in the authors' own words, why published US dementia "
           "lifetime risks range from 11% to 41%, and the mechanisms are all ascertainment "
           "rather than statistical method: (a) claims-based ascertainment misses undiagnosed "
           "dementia (Alzheimer's Association 2014, about one-third); (b) the calibrated "
           "cutoff method underpredicts dementia prevalence at 85+ by 4.8 points, which they "
           "show explains Hale 2020 (24% men, 37% women) and Cha 2024; (c) estimates from "
           "measured status some months before death miss progression in the final months "
           "(Fishman 2017, 24% for 70-year-old men); and (d) older Framingham cohorts had "
           "LOWER life expectancy, so more members died young where dementia risk is low, "
           "which they name explicitly as a reason Seshadri 1997 and Seshadri & Wolf 2007 "
           "are low. Every one of those four mechanisms biases DOWNWARD, which means the "
           "13.8% from Chene 2015 that this shard also carries is very likely a floor rather "
           "than a central estimate. See the dementia_denominator_reconciliation block in "
           "baseline_risks.yaml for all five estimates converted to a common index age of 19."),
)


# ------------------------------------------------------------------ 6. obesity
add(
    study_id="emmerich2024_obesity_prevalence",
    citation=("Emmerich SD, Fryar CD, Stierman B, Ogden CL. Obesity and Severe Obesity "
              "Prevalence in Adults: United States, August 2021-August 2023. NCHS Data Brief "
              "No. 508. Hyattsville, MD: National Center for Health Statistics; 2024."),
    doi="10.15620/cdc/159281", pmid="39808758",
    url="https://www.cdc.gov/nchs/data/databriefs/db508.pdf",
    verification={"crossref_ok": True, "pubmed_ok": True, "title_similarity": None,
                  "status": "VERIFIED",
                  "resolved_title": ("Obesity and Severe Obesity Prevalence in Adults: "
                                     "United States, August 2021-August 2023.")},
    access_tier="full_text", design="cross_sectional", n=2680,
    population={"age_mean": None, "age_range": [20, 999], "pct_female": 0.0, "country": "US",
                "adolescent_match": "mixed"},
    effects=[
        eff("obesity_prevalence_us_male_40_59", "probability", 0.454, 0.019,
            [0.454 - 1.96 * 0.019, 0.454 + 1.96 * 0.019],
            ("Men 20 and older. . . 2,680 39.2 1.9 39.3 1.9 / 20-39. . . 672 34.3 2.8 / "
             "40-59. . . 762 45.4 1.9 / 60 and older. . . 1,246 38.0 2.3"),
            unit="prevalence of BMI >= 30 in US men aged 40-59 (midlife)",
            conv=("NCHS publishes SE = 1.9 percentage points; ci computed as "
                  "value +/- 1.96*SE because the data brief prints SEs, not CIs"),
            inferred=True,
            direction=("higher = more obesity. DIRECT ANSWER to 'probability of being obese "
                       "by midlife for a US male' read as a period prevalence: 45.4%."),
            cohort="NHANES"),
        eff("obesity_prevalence_us_male_20_39", "probability", 0.343, 0.028,
            [0.343 - 1.96 * 0.028, 0.343 + 1.96 * 0.028],
            "20-39. . . 672 34.3 2.8",
            unit="prevalence of BMI >= 30 in US men aged 20-39",
            conv="ci = value +/- 1.96 * published SE of 2.8 percentage points",
            inferred=True,
            direction=("higher = more obesity. AGE-OVERLAPPING with the subject: 34.3% of US "
                       "men aged 20-39 are already obese, so the baseline the sleep exposure "
                       "perturbs is already high."),
            cohort="NHANES"),
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "low",
         "notes": ("Nationally representative with measured height and weight. "
                   "Cross-sectional prevalence is not cumulative incidence: it understates "
                   "the fraction EVER obese by midlife (some regress below BMI 30) and it "
                   "embeds cohort effects, which for obesity are strongly upward.")},
    funding="US federal (CDC/NCHS)",
)

add(
    study_id="ward2017_obesity_age35",
    citation=("Ward ZJ, Long MW, Resch SC, Giles CM, Cradock AL, Gortmaker SL. Simulation of "
              "Growth Trajectories of Childhood Obesity into Adulthood. N Engl J Med. "
              "2017;377(22):2145-2153."),
    doi="10.1056/NEJMoa1703860", pmid="29171811",
    url="https://pmc.ncbi.nlm.nih.gov/articles/PMC9036858/",
    verification={"crossref_ok": True, "pubmed_ok": True, "title_similarity": None,
                  "status": "VERIFIED",
                  "resolved_title": ("Simulation of Growth Trajectories of Childhood Obesity "
                                     "into Adulthood.")},
    access_tier="abstract_only", design="normative_descriptive", n=41567,
    n_studies_pooled=5,
    population={"age_mean": None, "age_range": [2, 35], "pct_female": None, "country": "US",
                "adolescent_match": "exact_16_19"},
    effects=[
        eff("probability_obese_at_age_35_current_us_children", "probability", 0.573,
            se_from_ci(0.552, 0.600), [0.552, 0.600],
            ("Given the current level of childhood obesity, the models predicted that a "
             "majority of today's children (57.3%; 95% uncertainly interval [UI], 55.2 to "
             "60.0) will be obese at the age of 35 years, and roughly half of the projected "
             "prevalence will occur during childhood."),
            unit="probability of BMI >= 30 at exact age 35, 2016 US population aged 0-19",
            conv="se = (0.600 - 0.552)/3.92 = 0.0122 on the probability scale",
            direction=("higher = more obesity. FORWARD-LOOKING denominator for the subject's "
                       "own birth cohort, and HIGHER than the current 40-59 prevalence of "
                       "45.4% because of cohort effects. Both sexes combined."),
            cohort="pooled_5_US_longitudinal_studies"),
        eff("log_rr_adult_obesity_for_19yo_with_severe_obesity", "log_rr",
            logratio(3.10, 2.43, 3.65)[0], logratio(3.10, 2.43, 3.65)[1],
            [math.log(2.43), math.log(3.65)],
            ("Our simulations indicated that the relative risk of adult obesity increased "
             "with age and BMI, from 1.17 (95% UI, 1.09 to 1.29) for overweight 2-year-olds "
             "to 3.10 (95% UI, 2.43 to 3.65) for 19-year-olds with severe obesity."),
            unit="log relative risk of obesity at 35 for a severely obese 19-year-old",
            conv="log_rr = ln(3.10) = 1.1314; se = (ln(3.65) - ln(2.43))/3.92 = 0.10389",
            direction="positive = higher risk of adult obesity.",
            cohort="pooled_5_US_longitudinal_studies"),
        eff("probability_not_obese_at_35_if_severely_obese_at_19", "probability", 0.061,
            se_from_ci(0.021, 0.099), [0.021, 0.099],
            ("For children with severe obesity, the chance they will no longer be obese at "
             "the age of 35 years fell from 21.0% (95% UI, 7.3 to 47.3) at the age of 2 years "
             "to 6.1% (95% UI, 2.1 to 9.9) at the age of 19 years."),
            unit="probability of escaping obesity by 35 given severe obesity at exactly 19",
            conv="se = (0.099 - 0.021)/3.92 = 0.0199",
            direction=("higher = more escape. THE PERSISTENCE COEFFICIENT THE MODEL NEEDS: "
                       "BMI status at exactly age 19 is nearly absorbing (only a 6.1% chance "
                       "of escape), so a sleep-driven BMI shift at ages 16-19 should be "
                       "modelled as largely PERMANENT rather than transient. This is the "
                       "empirical warrant for the 'mediator-locked' persistence scenario in "
                       "competing_risk_method.md section 1.3, which is worth about -18 months "
                       "of e19 versus -0.3 months for the transient scenario."),
            cohort="pooled_5_US_longitudinal_studies"),
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "moderate",
         "notes": ("Microsimulation, so the uncertainty intervals reflect parameter and "
                   "sampling uncertainty but not structural model uncertainty. Secular trend "
                   "extrapolation to 2016 and beyond. Both sexes combined for the headline "
                   "57.3%. Severe obesity in children defined as >=120% of the 95th "
                   "percentile.")},
    funding="JPB Foundation and others",
)

# ------------------------------------------------------------------ 7. MDD
add(
    study_id="nsduh2024_mde_male_18_25",
    citation=("Substance Abuse and Mental Health Services Administration, Center for "
              "Behavioral Health Statistics and Quality. 2024 National Survey on Drug Use and "
              "Health: Detailed Tables. Rockville, MD: SAMHSA; 2025. Tables 6.39B "
              "(percentages) and 6.39D (standard errors)."),
    doi=None, pmid=None,
    url="https://www.samhsa.gov/data/report/2024-nsduh-detailed-tables",
    verification={"crossref_ok": None, "pubmed_ok": None, "title_similarity": None,
                  "status": "UNVERIFIED", "resolved_title": None},
    access_tier="full_text", design="cross_sectional", n=None,
    population={"age_mean": None, "age_range": [18, 25], "pct_female": 0.0, "country": "US",
                "adolescent_match": "good_young_adult"},
    effects=[
        eff("past_year_major_depressive_episode_us_male_18_25", "probability", 0.124, 0.0058,
            [0.124 - 1.96 * 0.0058, 0.124 + 1.96 * 0.0058],
            ("Table 6.39B - Major Depressive Episode in Past Year: Among People Aged 18 or "
             "Older; by Sex and Detailed Age Category, Percentages, 2023 and 2024. Row "
             "'18-25': 17.5a | 15.9 | 12.8 | 12.4 | 22.2b | 19.3 (columns Total 2023, Total "
             "2024, Male 2023, Male 2024, Female 2023, Female 2024). Table 6.39D standard "
             "errors, row '18-25': 0.51 | 0.48 | 0.65 | 0.58 | 0.72 | 0.71."),
            unit="past-12-month prevalence of DSM-5-aligned MDE, US males aged 18-25, 2024",
            conv=("ci = value +/- 1.96 * published SE of 0.58 percentage points; SAMHSA "
                  "prints SEs, not CIs"),
            inferred=True,
            direction=("higher = more depression. AGE-MATCHED CONTEMPORARY DENOMINATOR: "
                       "12.4% of US males aged 18-25 had a past-year major depressive "
                       "episode in 2024, roughly double the 6.4% for males 18+."),
            cohort="NSDUH"),
        eff("past_year_major_depressive_episode_us_male_18_20", "probability", 0.112, 0.0092,
            [0.112 - 1.96 * 0.0092, 0.112 + 1.96 * 0.0092],
            ("Table 6.39B row '18-20': 15.8 | 16.0 | 11.2 | 11.2 | 20.9 | 21.2. "
             "Table 6.39D row '18-20': 0.80 | 0.77 | 1.03 | 0.92 | 1.18 | 1.19."),
            unit="past-12-month prevalence of MDE, US males aged 18-20, 2024",
            conv="ci = value +/- 1.96 * published SE of 0.92 percentage points",
            inferred=True,
            direction=("higher = more depression. THE EXACT AGE BAND OF THE SUBJECT: 11.2% "
                       "(SE 0.92) of US males aged 18-20 had a past-year MDE. This is the "
                       "denominator against which any sleep-restriction depression odds ratio "
                       "must be applied."),
            cohort="NSDUH"),
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "moderate",
         "notes": ("Nationally representative but the 2024 NSDUH had 47.9% adult "
                   "non-response and used multimode (in-person plus web) collection; SAMHSA "
                   "itself warns that 'comparison of estimates from the 2024 NSDUH with those "
                   "from prior years must be made with caution'. Measures MDE (an episode) "
                   "not MDD (the disorder): MDE omits the bipolar exclusion. Self-report "
                   "instrument, not a clinician interview.")},
    funding="US federal (SAMHSA)",
    notes=("VERIFICATION UNVERIFIED BY CONSTRUCTION, NOT BY FAILURE: NSDUH detailed tables "
           "carry no DOI and are not indexed in PubMed, so both identifier fields are "
           "correctly null rather than guessed. Retrieval evidence: the official SAMHSA ZIP "
           "2024-nsduh-detailed-tables-072325.zip was downloaded from samhsa.gov, extracted, "
           "and tables 6.39B and 6.39D parsed programmatically from the HTML rather than "
           "transcribed. CORROBORATION: NIMH's Major Depression statistics page reports 18.6% "
           "past-year MDE for all adults aged 18-25 in 2021 (both sexes) and 6.2% for adult "
           "males overall, consistent in level and in the male-female ratio."),
)

add(
    study_id="hasin2018_mdd_nesarc3",
    citation=("Hasin DS, Sarvet AL, Meyers JL, Saha TD, Ruan WJ, Stohl M, Grant BF. "
              "Epidemiology of Adult DSM-5 Major Depressive Disorder and Its Specifiers in "
              "the United States. JAMA Psychiatry. 2018;75(4):336-346."),
    doi="10.1001/jamapsychiatry.2017.4602", pmid="29450462",
    url="https://pmc.ncbi.nlm.nih.gov/articles/PMC5875313/",
    verification={"crossref_ok": True, "pubmed_ok": True, "title_similarity": None,
                  "status": "VERIFIED",
                  "resolved_title": ("Epidemiology of Adult DSM-5 Major Depressive Disorder "
                                     "and Its Specifiers in the United States.")},
    access_tier="full_text", design="cross_sectional", n=36309,
    population={"age_mean": None, "age_range": [18, 999], "pct_female": None, "country": "US",
                "adolescent_match": "fair_adult"},
    effects=[
        eff("lifetime_prevalence_mdd_us_male", "probability", 0.147, 0.0040,
            [0.147 - 1.96 * 0.0040, 0.147 + 1.96 * 0.0040],
            ("Table 1: Male | 7.2 (0.26) | 0.5 (0.46-0.55) | 14.7 (0.40) | 0.5 (0.46-0.53) "
             "(columns: 12-month prevalence % (SE), 12-month OR, lifetime prevalence % (SE), "
             "lifetime OR). Text: 'Of the 36 309 adult participants in NESARC-III, 12-month "
             "and lifetime prevalences of MDD were 10.4% and 20.6%, respectively.'"),
            unit="lifetime prevalence of DSM-5 MDD, US males aged 18+",
            conv="ci = value +/- 1.96 * published SE of 0.40 percentage points",
            inferred=True,
            direction=("higher = more disorder. An all-ages male cross-section, so it "
                       "UNDERSTATES a 19-year-old's forward-looking lifetime risk; use "
                       "mcgrath2023_morbid_risk for that."),
            cohort="NESARC_III"),
        eff("twelve_month_prevalence_mdd_us_male", "probability", 0.072, 0.0026,
            [0.072 - 1.96 * 0.0026, 0.072 + 1.96 * 0.0026],
            "Table 1: Male | 7.2 (0.26) | 0.5 (0.46-0.55) | 14.7 (0.40) | 0.5 (0.46-0.53)",
            unit="12-month prevalence of DSM-5 MDD, US males aged 18+",
            conv="ci = value +/- 1.96 * published SE of 0.26 percentage points",
            inferred=True,
            direction="higher = more disorder.",
            cohort="NESARC_III"),
        eff("lifetime_prevalence_mdd_age_18_29_both_sexes", "probability", 0.202, 0.0055,
            [0.202 - 1.96 * 0.0055, 0.202 + 1.96 * 0.0055],
            "Table 1, Age, y: 18-29 | 12.9 (0.47) | 3.0 (2.48-3.55) | 20.2 (0.55) | 1.9 (1.65-2.10)",
            unit="lifetime prevalence of DSM-5 MDD, US adults aged 18-29, both sexes",
            conv="ci = value +/- 1.96 * published SE of 0.55 percentage points",
            inferred=True,
            direction=("higher = more disorder. Age band overlapping the subject, but both "
                       "sexes; men are roughly half the female rate (lifetime OR 0.5)."),
            cohort="NESARC_III"),
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "moderate",
         "notes": ("Large nationally representative in-person survey with the AUDADIS-5 lay "
                   "interview, whose agreement with clinician diagnosis for MDD is moderate. "
                   "Cross-sectional lifetime recall is subject to forgetting, which biases "
                   "lifetime prevalence downward, especially in older respondents. "
                   "2012-2013 data.")},
    funding="NIAAA intramural",
)

add(
    study_id="kessler2003_mdd_ncsr",
    citation=("Kessler RC, Berglund P, Demler O, Jin R, Koretz D, Merikangas KR, Rush AJ, "
              "Walters EE, Wang PS. The epidemiology of major depressive disorder: results "
              "from the National Comorbidity Survey Replication (NCS-R). JAMA. "
              "2003;289(23):3095-3105."),
    doi="10.1001/jama.289.23.3095", pmid="12813115", url=None,
    verification={"crossref_ok": True, "pubmed_ok": True, "title_similarity": None,
                  "status": "VERIFIED",
                  "resolved_title": ("The epidemiology of major depressive disorder: results "
                                     "from the National Comorbidity Survey Replication "
                                     "(NCS-R).")},
    access_tier="abstract_only", design="cross_sectional", n=9090,
    population={"age_mean": None, "age_range": [18, 999], "pct_female": None, "country": "US",
                "adolescent_match": "fair_adult"},
    effects=[
        eff("lifetime_prevalence_mdd_us_adults_both_sexes", "probability", 0.162,
            se_from_ci(0.151, 0.173), [0.151, 0.173],
            ("The prevalence of CIDI MDD for lifetime was 16.2% (95% confidence interval "
             "[CI], 15.1-17.3) (32.6-35.1 million US adults) and for 12-month was 6.6% (95% "
             "CI, 5.9-7.3) (13.1-14.2 million US adults)."),
            unit="lifetime prevalence of DSM-IV MDD, US adults 18+, both sexes",
            conv="se = (0.173 - 0.151)/3.92 = 0.00561 on the probability scale",
            direction="higher = more disorder.",
            cohort="NCS_R"),
        eff("twelve_month_prevalence_mdd_us_adults_both_sexes", "probability", 0.066,
            se_from_ci(0.059, 0.073), [0.059, 0.073],
            ("The prevalence of CIDI MDD for lifetime was 16.2% ... and for 12-month was "
             "6.6% (95% CI, 5.9-7.3) (13.1-14.2 million US adults)."),
            unit="12-month prevalence of DSM-IV MDD, US adults 18+, both sexes",
            conv="se = (0.073 - 0.059)/3.92 = 0.00357",
            direction="higher = more disorder.",
            cohort="NCS_R"),
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "moderate",
         "notes": ("2001-2002 data, DSM-IV, lay CIDI interview. The abstract does NOT report "
                   "a sex-by-age-band breakdown, so the male 18-25 figure had to come from "
                   "NSDUH and the male lifetime figure from NESARC-III. Full text not "
                   "retrievable, so the sex-specific table could not be read.")},
    funding="NIMH, and others",
    notes=("The NCS-R paper named in the shard task; real, and the headline numbers match. "
           "Kessler 2005 (Arch Gen Psychiatry 62:593, DOI 10.1001/archpsyc.62.6.593, PMID "
           "15939837) is the companion age-of-onset paper: lifetime prevalence of any mood "
           "disorder 20.8%, median age of onset for mood disorders 30 years, projected "
           "lifetime risk of ANY disorder at age 75 of 50.8% versus observed lifetime "
           "prevalence 46.4%, and 'Half of all lifetime cases start by age 14 years and "
           "three fourths by age 24 years'. That last sentence matters here: the subject's "
           "exposure window sits inside the peak-onset window, so a sleep effect on "
           "depression can plausibly act on incidence rather than only on recurrence."),
)

add(
    study_id="mcgrath2023_morbid_risk",
    citation=("McGrath JJ, Al-Hamzawi A, Alonso J, et al.; WHO World Mental Health Survey "
              "Collaborators. Age of onset and cumulative risk of mental disorders: a "
              "cross-national analysis of population surveys from 29 countries. Lancet "
              "Psychiatry. 2023;10(9):668-681."),
    doi="10.1016/S2215-0366(23)00193-1", pmid="37531964",
    url="https://pmc.ncbi.nlm.nih.gov/articles/PMC10529120/",
    verification={"crossref_ok": True, "pubmed_ok": True, "title_similarity": None,
                  "status": "VERIFIED",
                  "resolved_title": ("Age of onset and cumulative risk of mental disorders: a "
                                     "cross-national analysis of population surveys from 29 "
                                     "countries.")},
    access_tier="full_text", design="cross_sectional", n=156331,
    n_studies_pooled=32,
    population={"age_mean": None, "age_range": [18, 999], "pct_female": 54.5,
                "country": "29 countries incl. US", "adolescent_match": "fair_adult"},
    effects=[
        eff("morbid_risk_mdd_by_age_75_male", "probability", 0.201,
            se_from_ci(0.192, 0.209), [0.192, 0.209],
            ("Major depressive disorder | 20.1 | (19.2-20.9) | 34.0 | (33.2-34.9) | 2.7 | "
             "(2.6-2.8) | 2.5 | (2.4-2.5)  (Morbid risk per 100 participants at age 75: male "
             "then female, then the ratio of morbid risk to lifetime prevalence for each "
             "sex.)"),
            unit="projected cumulative lifetime risk of DSM-IV MDD by age 75, males",
            conv="se = (0.209 - 0.192)/3.92 = 0.00434 on the probability scale",
            direction=("higher = more disorder. RECOMMENDED FORWARD-LOOKING MDD DENOMINATOR "
                       "for a 19-year-old male: about 20% will develop MDD by 75. Note the "
                       "morbid-risk-to-lifetime-prevalence ratio of 2.7 in males, which "
                       "quantifies how badly a cross-sectional lifetime prevalence "
                       "understates a young person's risk."),
            cohort="WHO_WMH"),
        eff("morbid_risk_any_mental_disorder_by_age_75_male", "probability", 0.464,
            se_from_ci(0.449, 0.478), [0.449, 0.478],
            ("Morbid risk of any mental disorder by age 75 years was 46.4% (44.9-47.8) for "
             "male respondents and 53.1% (51.9-54.3) for female respondents. Conditional "
             "probabilities of first onset peaked at approximately age 15 years, with a "
             "median age of onset of 19 years (IQR 14-32) for male respondents and 20 years "
             "(12-36) for female respondents."),
            unit="projected cumulative lifetime risk of any of 13 DSM-IV disorders by 75, males",
            conv="se = (0.478 - 0.449)/3.92 = 0.0074",
            direction=("higher = more disorder. Also records the fact most relevant to this "
                       "project: the MEDIAN AGE OF FIRST ONSET of any mental disorder in "
                       "males is exactly 19, so the sleep-restriction exposure window and "
                       "the peak-incidence window coincide completely."),
            cohort="WHO_WMH"),
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "moderate",
         "notes": ("Cross-national, NOT US-specific; the US contributes one of 32 surveys, so "
                   "transportability to a US male is only fair. Morbid risk is projected from "
                   "retrospectively reported ages of onset, which are subject to recall "
                   "telescoping, and it is NOT adjusted for competing mortality (the paper "
                   "projects to age 75 in a survey population). Surveys span 2001-2022 with "
                   "heterogeneous fielding.")},
    funding="None declared",
)

# ------------------------------------------------------------------ 8. suicide
add(
    study_id="garnett2024_suicide",
    citation=("Garnett MF, Curtin SC. Suicide Mortality in the United States, 2002-2022. "
              "NCHS Data Brief No. 509. Hyattsville, MD: National Center for Health "
              "Statistics; 2024."),
    doi="10.15620/cdc/160504", pmid="39392858",
    url="https://www.cdc.gov/nchs/data/databriefs/db509.pdf",
    verification={"crossref_ok": True, "pubmed_ok": True, "title_similarity": None,
                  "status": "VERIFIED",
                  "resolved_title": "Suicide Mortality in the United States, 2002-2022."},
    access_tier="full_text", design="normative_descriptive", n=4779,
    population={"age_mean": None, "age_range": [15, 24], "pct_female": 0.0, "country": "US",
                "adolescent_match": "exact_16_19"},
    effects=[
        eff("suicide_rate_us_male_15_24_2022", "raw_units", 21.1, None, None,
            ("Between 2020 and 2022, rates decreased for males ages 10-14 (3.6 deaths per "
             "100,000 population to 2.8) and 15-24 (22.4 to 21.1), while rates increased for "
             "males age 25 and older. Data table for Figure 3, 2022 row: 303 2.8 | 4,779 "
             "21.1 | 13,390 29.6 | 12,075 29.5 | 4,320 27.2 | 4,395 43.9 (age groups 10-14, "
             "15-24, 25-44, 45-64, 65-74, 75+; number of deaths then rate per 100,000)."),
            unit="suicide deaths per 100,000 US males aged 15-24 per year, 2022",
            direction=("higher = more death. Complete national vital registration, so there "
                       "is no sampling SE; se is null by construction, not omission."),
            cohort="NVSS"),
        eff("suicide_share_of_all_cause_male_mortality_at_age_19", "probability", 0.199,
            None, None,
            ("Numerator from this report (21.1 suicide deaths per 100,000 males aged 15-24 in "
             "2022). Denominator from NCHS United States Life Tables 2023 Table 2: "
             "'19-20 . . . 0.001061 98,810 105 98,757 5,697,034 57.7', i.e. all-cause "
             "q(19) = 0.001061."),
            unit="fraction of all-cause male mortality at age 19 attributable to suicide",
            conv="0.000211 / 0.001061 = 0.199",
            direction=("higher = larger share. THE CAUSE FRACTION f(x) required by "
                       "competing_risk_method.md section 1.4 for turning a suicide-specific "
                       "hazard ratio into months of life expectancy. Suicide is roughly a "
                       "fifth of all young-male mortality, so a psychiatric-channel hazard "
                       "ratio is not a small perturbation at these ages, and because a death "
                       "at 19 destroys the entire 57.66-year remaining life expectancy, this "
                       "is the highest-leverage mortality pathway in the model."),
            cohort="NVSS"),
    ],
    rob={"tool": "none", "judgement": "na",
         "notes": ("Complete national death registration; ICD-10 U03, X60-X84, Y87.0. Known "
                   "limitations: suicide is undercounted because some deaths are certified as "
                   "undetermined intent or unintentional poisoning; the 15-24 band is wider "
                   "than the subject's exposure window; rates are crude within the band and "
                   "the 20-24 rate is substantially higher than the 15-19 rate (27.9 vs 17.3 "
                   "per 100,000 in 2018, the last year the Health United States series "
                   "publishes the 5-year split).")},
    funding="US federal (CDC/NCHS)",
    notes=("Time series for males 15-24, deaths per 100,000: 2018 22.7, 2019 22.0, 2020 22.4, "
           "2021 23.8, 2022 21.1 (Figure 3 data table, extracted programmatically from the "
           "PDF). CORROBORATION for 2023: NIMH's suicide statistics page, Figure 2 ('crude "
           "rates of suicide within sex and age categories in 2023', sourced to CDC "
           "WISQARS/NVSS), gives 21.2 per 100,000 for males aged 15-24 and 5.5 for females, "
           "i.e. essentially unchanged from 2022. That page is an aggregator, so the 2022 "
           "figure from this primary NCHS report is the one recorded above."),
)

# ------------------------------------------------------------------ 9. sleep LE cross-checks
add(
    study_id="chaput2022_years_of_life",
    citation=("Chaput JP, Carrier J, Bastien C, Gariepy G, Janssen I. Years of life gained "
              "when meeting sleep duration recommendations in Canada. Sleep Med. "
              "2022;100:85-88."),
    doi="10.1016/j.sleep.2022.08.006", pmid="36029755", url=None,
    verification={"crossref_ok": True, "pubmed_ok": True, "title_similarity": None,
                  "status": "VERIFIED",
                  "resolved_title": ("Years of life gained when meeting sleep duration "
                                     "recommendations in Canada.")},
    access_tier="abstract_only", design="life_table", n=None,
    population={"age_mean": None, "age_range": [20, 100], "pct_female": None,
                "country": "Canada", "adolescent_match": "good_young_adult"},
    effects=[
        eff("life_expectancy_at_20_lost_by_short_sleepers", "years", -1.2, None, None,
            ("Adults who meet the sleep duration recommendations have an estimated life "
             "expectancy at age 20 years that is 1.2 years longer than short sleepers and 2.6 "
             "years longer than long sleepers. Differences between men and women were "
             "minimal."),
            unit="years of life expectancy at age 20 lost by short vs recommended sleepers",
            exposure={"type": "habitual_short_sleep", "dose_h": None, "referent_h": None,
                      "duration_days": None,
                      "contrast_label": ("habitual short sleep vs meeting national sleep "
                                         "duration recommendations, sustained from age 20")},
            direction=("negative = life lost by short sleepers. THE SINGLE MOST USEFUL "
                       "EXTERNAL CROSS-CHECK IN THIS SHARD: it is a published answer, at "
                       "index age 20, to almost exactly the question this project asks, "
                       "computed with exactly the machinery documented in "
                       "competing_risk_method.md. No CI reported, so se is null."),
            cohort="Canadian_national_life_tables"),
    ],
    rob={"tool": "ROBINS-I", "judgement": "high",
         "notes": ("The life-table arithmetic is sound; the causal input is not. The all-cause "
                   "mortality relative risks are imported from observational meta-analyses "
                   "of self-reported habitual sleep duration, which carry reverse causation "
                   "(illness shortens and lengthens sleep), residual confounding by shift "
                   "work, depression, obesity and socioeconomic position, and measurement "
                   "error. Canadian life tables and Canadian sleep prevalence, not US. No "
                   "adolescents. Applies a single lifelong RR from age 20, which is the "
                   "OPPOSITE of this project's 3-year adolescent exposure, so 1.2 years is an "
                   "UPPER BOUND on the mortality-channel cost of 3 years of restriction "
                   "unless the exposure permanently reprograms risk. Life-years only, no "
                   "QALY weighting.")},
    funding=None,
    notes=("REPRODUCED BY THIS SHARD: feeding an all-cause mortality hazard ratio of "
           "1.10-1.13 lifelong from age 20 through the NCHS 2023 US male life table gives "
           "-1.15 to -1.48 years at age 20 (hr_to_life_expectancy.py section G). The "
           "published 1.2-year figure sits inside that band. Two different life tables and "
           "two independent implementations agree, which validates the conversion machinery. "
           "This is the end-to-end calibration target in competing_risk_method.md section 4."),
)

add(
    study_id="li2024_sleep_life_expectancy",
    citation=("Li H, Qian F, Han L, Feng W, Zheng D, Guo X, Zhang H. Association of healthy "
              "sleep patterns with risk of mortality and life expectancy at age of 30 years: "
              "a population-based cohort study. QJM. 2024;117(3):177-186."),
    doi="10.1093/qjmed/hcad237", pmid="37831896", url=None,
    verification={"crossref_ok": True, "pubmed_ok": True, "title_similarity": None,
                  "status": "VERIFIED",
                  "resolved_title": ("Association of healthy sleep patterns with risk of "
                                     "mortality and life expectancy at age of 30 years: a "
                                     "population-based cohort study.")},
    access_tier="abstract_only", design="prospective_cohort_selfreport", n=172321,
    population={"age_mean": 46.98, "age_range": [18, 999], "pct_female": 50.9,
                "country": "US", "adolescent_match": "fair_adult"},
    effects=[
        eff("life_expectancy_at_30_lost_by_poor_sleep_pattern_male", "years", -4.7,
            se_from_ci(-6.7, -2.7), [-6.7, -2.7],
            ("When compared to those with 0-1 low-risk sleep factors, life expectancy at the "
             "age of 30 years for individuals with all five low-risk sleep factors was 4.7 "
             "(95% CI: 2.7-6.7) years greater for men and 2.4 (95% CI: 0.4-4.4) years greater "
             "for women."),
            unit=("years of life expectancy at age 30 lost by men with 0-1 vs 5 low-risk "
                  "sleep factors"),
            exposure={"type": "habitual_short_sleep", "dose_h": None, "referent_h": None,
                      "duration_days": None,
                      "contrast_label": ("0-1 vs 5 low-risk sleep factors (7-8 h duration, "
                                         "no difficulty falling asleep, no difficulty staying "
                                         "asleep, no sleep medication, feeling rested)")},
            conv="se = (6.7 - 2.7)/3.92 = 1.020; sign flipped to negative = years lost",
            direction=("negative = life lost by the poor-sleep group. MUCH LARGER than "
                       "Chaput's 1.2 years because the contrast is a 5-factor composite, not "
                       "sleep duration alone; attributing all 4.7 years to short duration "
                       "would be a category error."),
            covariates=["age", "sex", "race", "socioeconomic factors", "lifestyle",
                        "comorbidity"],
            followup=4.3, cohort="NHIS_NDI"),
        eff("log_hr_all_cause_mortality_5_vs_0_1_low_risk_sleep_factors", "log_hr",
            logratio(0.70, 0.63, 0.77)[0], logratio(0.70, 0.63, 0.77)[1],
            [math.log(0.63), math.log(0.77)],
            ("The adjusted hazard ratios (95% confidence intervals [CI]) of participants with "
             "five vs. 0-1 low-risk sleep factors for all-cause, cardiovascular, and cancer "
             "mortality were 0.70 (0.63-0.77), 0.79 (0.67-0.93) and 0.81 (0.66-0.98), "
             "respectively. Nearly 8% (population attributable fraction 7.9%, 95% CI: "
             "5.5-10.4) of mortality in this cohort could be attributed to suboptimal sleep "
             "patterns."),
            unit="log hazard ratio for all-cause mortality, 5 vs 0-1 low-risk sleep factors",
            exposure={"type": "habitual_short_sleep", "dose_h": None, "referent_h": None,
                      "duration_days": None,
                      "contrast_label": "5 vs 0-1 low-risk sleep factors"},
            conv="log_hr = ln(0.70) = -0.3567; se = (ln(0.77) - ln(0.63))/3.92 = 0.05122",
            direction=("negative = LOWER mortality with healthy sleep, i.e. the harm "
                       "direction is the reciprocal HR of 1.43 for the poor-sleep group. "
                       "Feeding 1.43 lifelong from age 30 through this shard's life table "
                       "gives about -4.5 years, internally consistent with their 4.7."),
            covariates=["age", "sex", "race", "socioeconomic factors", "lifestyle",
                        "comorbidity"],
            followup=4.3, cohort="NHIS_NDI"),
    ],
    rob={"tool": "ROBINS-I", "judgement": "high",
         "notes": ("Median follow-up only 4.3 years with 8,681 deaths, so life expectancy at "
                   "age 30 is extrapolated far beyond the observed data by a flexible "
                   "parametric model and the reported CI understates that extrapolation "
                   "uncertainty. Reverse causation is severe for the insomnia and restedness "
                   "components: people who died within 4.3 years were often already ill. "
                   "Mean age 47, so essentially no adolescent or young-adult exposure. "
                   "Self-reported sleep at a single time point.")},
    funding=None,
    notes=("US nationally representative (NHIS 2013-18 linked to the National Death Index "
           "through 2019), which is a transportability advantage over Chaput 2022 and Huang "
           "2023. Use as an UPPER bound on the plausible life-expectancy effect of a sleep "
           "syndrome, not of short duration alone."),
)

add(
    study_id="ma2023_le8_life_expectancy",
    citation=("Ma H, Wang X, Xue Q, Li X, Liang Z, Heianza Y, Franco OH, Qi L. Cardiovascular "
              "Health and Life Expectancy Among Adults in the United States. Circulation. "
              "2023;147(15):1137-1146."),
    doi="10.1161/CIRCULATIONAHA.122.062457", pmid="37036905",
    url="https://pmc.ncbi.nlm.nih.gov/articles/PMC10165723/",
    verification={"crossref_ok": True, "pubmed_ok": True, "title_similarity": None,
                  "status": "VERIFIED",
                  "resolved_title": ("Cardiovascular Health and Life Expectancy Among Adults "
                                     "in the United States")},
    access_tier="full_text", design="prospective_cohort_selfreport", n=23003,
    population={"age_mean": None, "age_range": [20, 79], "pct_female": None, "country": "US",
                "adolescent_match": "fair_adult"},
    effects=[
        eff("life_expectancy_at_50_gained_high_vs_low_sleep_health_score", "years", 5.0,
            se_from_ci(3.2, 6.7), [3.2, 6.7],
            ("The new component for CVH--high sleep health score was significantly associated "
             "with a longer life expectancy at age 50 by 5.0 (95% CI, 3.2-6.7) years for all "
             "participants."),
            unit=("years of life expectancy at exact age 50, high versus low LE8 sleep health "
                  "score, NOT mutually adjusted for the other seven CVH components"),
            exposure={"type": "habitual_short_sleep", "dose_h": None, "referent_h": 8.0,
                      "duration_days": None,
                      "contrast_label": ("high vs low LE8 sleep health score; LE8 scores "
                                         "7 to <9 h as 100 and short sleep progressively "
                                         "lower, so 'low' is dominated by short duration")},
            conv="se = (6.7 - 3.2)/3.92 = 0.893",
            direction=("positive = years GAINED by good sleep, i.e. 5.0 y notionally lost by "
                       "the poor-sleep group. TREAT AS A HARD CEILING, NOT AN ESTIMATE. The "
                       "paper's own numbers prove the component contrasts are not independent: "
                       "tobacco alone gives 7.4 y and sleep alone gives 5.0 y, summing to 12.4 "
                       "y, which exceeds the ENTIRE high-vs-low LE8 contrast of 8.9 y before "
                       "the other six components are even counted. The components therefore "
                       "overlap heavily and 5.0 y cannot be read as sleep's independent "
                       "contribution. It is 4.2x this shard's life-table result for a lifelong "
                       "all-cause HR of 1.13 (-1.49 y) and 4.2x Chaput's 1.2 y."),
            covariates=["age", "sex", "race/ethnicity"],
            followup=7.8, cohort="NHANES_NDI"),
        eff("life_expectancy_at_50_gained_high_vs_low_total_cvh_male", "years", 8.1,
            se_from_ci(4.2, 12.0), [4.2, 12.0],
            ("In men, participants with high CVH had 8.1 (95% CI, 4.2-12.0) more years of "
             "estimated life expectancy at age 50 compared with those with low CVH."),
            unit=("years of life expectancy at exact age 50, high vs low total LE8 score, "
                  "MALES"),
            exposure={"type": "descriptive", "dose_h": None, "referent_h": None,
                      "duration_days": None,
                      "contrast_label": ("high (LE8 >=80) vs low (LE8 <50) total "
                                         "cardiovascular health; sleep is 1 of 8 components")},
            conv="se = (12.0 - 4.2)/3.92 = 1.990",
            direction=("positive = years gained. THE CEILING FOR THE WHOLE EIGHT-COMPONENT "
                       "LIFESTYLE BUNDLE IN MEN. Sleep duration is one of eight equally "
                       "weighted components, so an equal-share allocation caps sleep at about "
                       "1.0 y (8.1/8) - close to Chaput's independently derived 1.2 y and to "
                       "this shard's HR 1.10-1.13 result. That agreement between three "
                       "unrelated methods is the strongest available constraint on the "
                       "mortality channel. The 1.0 y equal-share figure is THIS SHARD'S "
                       "ARITHMETIC, not published by Ma et al."),
            covariates=["age", "sex", "race/ethnicity"],
            followup=7.8, cohort="NHANES_NDI"),
        eff("life_expectancy_at_50_low_cvh_years", "years", 27.3,
            se_from_ci(26.1, 28.4), [26.1, 28.4],
            ("The estimated life expectancy at age 50 years was 27.3 years (95% CI, "
             "26.1-28.4), 32.9 years (95% CI, 32.3-33.4), and 36.2 years (95% CI, 34.2-38.2) "
             "in participants with low (LE8 score <50), moderate (50<= LE8 score <80), and "
             "high (LE8 score >=80) CVH, respectively."),
            unit="absolute remaining life expectancy at age 50, low-CVH stratum, both sexes",
            conv="se = (28.4 - 26.1)/3.92 = 0.587",
            direction=("higher = longer life. INCLUDED AS A CALIBRATION CHECK ON THE PAPER "
                       "ITSELF, not as an exposure effect: NCHS 2023 Table 2 publishes e50 = "
                       "29.96 y for US males, so this cohort's low-CVH stratum (27.3 y, both "
                       "sexes) sits below the national male value and its high-CVH stratum "
                       "(36.2 y) well above it, which is the expected direction and indicates "
                       "the paper's life-table machinery is not grossly miscalibrated. The "
                       "national value falls between their low and moderate strata, as it "
                       "should for a population whose modal LE8 is moderate."),
            covariates=["age", "sex", "race/ethnicity"],
            followup=7.8, cohort="NHANES_NDI"),
    ],
    rob={"tool": "ROBINS-I", "judgement": "critical",
         "notes": ("The single-component estimates in Table S8, including the 5.0-year sleep "
                   "figure, are marginal high-vs-low contrasts that are NOT adjusted for the "
                   "other seven components. Because the components are strongly correlated in "
                   "these data (the low-CVH stratum has a mean sleep health score of 68.2 "
                   "versus 93.2 in the high-CVH stratum), the sleep contrast absorbs smoking, "
                   "diet, BMI, glucose and blood pressure. The internal arithmetic makes this "
                   "unavoidable: the components sum to far more than the total contrast. "
                   "Additionally, only 1359 deaths (328 CVD) over a median 7.8 years support "
                   "an extrapolation of survival from age 50 to 100, and sleep duration is "
                   "self-reported in a single NHANES interview. Confounding by socioeconomic "
                   "position is not addressed in the component analysis at all.")},
    funding="NIH (per paper)",
    notes=("THE LARGEST PUBLISHED SLEEP LIFE-EXPECTANCY NUMBER THIS SHARD FOUND, AND THE ONE "
           "MOST LIKELY TO BE MISUSED. If a downstream consumer wants a headline 'good sleep "
           "is worth 5 years' claim, this is where it comes from, and it is not defensible as "
           "a causal sleep effect for the reasons in rob.notes. Its real value is as the upper "
           "end of a bracket: the four independent published anchors for the mortality channel "
           "are Chaput 2022 (+1.2 y from age 20, life table + meta-analytic RR), Huang 2023 "
           "(-2.31 CVD-free y in men, UK Biobank), Li 2024 (-4.7 y at age 30 in men, 5-factor "
           "composite) and Ma 2023 (5.0 y at age 50, unadjusted single component). They span "
           "1.2 to 5.0 years and the spread is explained almost entirely by how much "
           "non-sleep lifestyle each contrast absorbs, ordered exactly as one would predict. "
           "Index age 50 versus the subject's 19 is a second reason to discount it: it "
           "conditions on surviving to 50."),
)

add(
    study_id="huang2023_cvdfree_life_expectancy",
    citation=("Huang BH, Del Pozo Cruz B, Teixeira-Pinto A, Cistulli PA, Stamatakis E. "
              "Influence of poor sleep on cardiovascular disease-free life expectancy: a "
              "multi-resource-based population cohort study. BMC Med. 2023;21(1):75."),
    doi="10.1186/s12916-023-02732-x", pmid="36859313",
    url="https://pmc.ncbi.nlm.nih.gov/articles/PMC9979412/",
    verification={"crossref_ok": True, "pubmed_ok": True, "title_similarity": None,
                  "status": "VERIFIED",
                  "resolved_title": ("Influence of poor sleep on cardiovascular disease-free "
                                     "life expectancy: a multi-resource-based population "
                                     "cohort study.")},
    access_tier="abstract_only", design="prospective_cohort_selfreport", n=308683,
    population={"age_mean": None, "age_range": [40, 70], "pct_female": None,
                "country": "UK", "adolescent_match": "poor_midlife"},
    effects=[
        eff("cvd_free_life_expectancy_lost_poor_sleepers_male", "years", -2.31,
            se_from_ci(-3.29, -1.46), [-3.29, -1.46],
            ("We observed a gradual loss in CVD-free life expectancy toward poor sleep such "
             "as, compared with healthy sleepers, poor sleepers lost 1.80 [95% CI 0.96-2.75] "
             "and 2.31 [1.46-3.29] CVD-free years in females and males, respectively, while "
             "intermediate sleepers lost 0.48 [0.41-0.55] and 0.55 [0.49-0.61] years."),
            unit="CVD-free years lost at age 40, poor vs healthy sleepers, males",
            exposure={"type": "habitual_short_sleep", "dose_h": None, "referent_h": None,
                      "duration_days": None,
                      "contrast_label": ("poor vs healthy composite sleep profile "
                                         "(chronotype, duration, insomnia complaints, "
                                         "snoring, daytime sleepiness)")},
            conv="se = (3.29 - 1.46)/3.92 = 0.467; sign flipped to negative = years lost",
            direction=("negative = CVD-free life lost. NOT total life expectancy: this is a "
                       "health-expectancy quantity from a three-state Markov model, closer in "
                       "spirit to a QALY than plain life-years but not utility-weighted."),
            covariates=["age", "sex", "socioeconomic", "lifestyle", "comorbidity"],
            cohort="UK_Biobank"),
        eff("cvd_free_life_expectancy_lost_intermediate_sleepers_male", "years", -0.55,
            se_from_ci(-0.61, -0.49), [-0.61, -0.49],
            ("... while intermediate sleepers lost 0.48 [0.41-0.55] and 0.55 [0.49-0.61] "
             "years."),
            unit="CVD-free years lost at age 40, intermediate vs healthy sleepers, males",
            exposure={"type": "habitual_short_sleep", "dose_h": None, "referent_h": None,
                      "duration_days": None,
                      "contrast_label": "intermediate vs healthy composite sleep profile"},
            conv="se = (0.61 - 0.49)/3.92 = 0.0306; sign flipped to negative",
            direction=("negative = CVD-free life lost. THE MORE RELEVANT CONTRAST for "
                       "mild-to-moderate chronic restriction, and it is 4.2x smaller than the "
                       "poor-sleeper estimate: 0.55 y = 6.6 months."),
            cohort="UK_Biobank"),
    ],
    rob={"tool": "ROBINS-I", "judgement": "high",
         "notes": ("UK Biobank is a healthy-volunteer cohort with about 5% response, "
                   "middle-aged at baseline, so it is not representative and contains no "
                   "adolescents. The composite sleep score conflates duration with insomnia, "
                   "snoring and chronotype, so the exposure is not sleep restriction. "
                   "Self-reported at a single time point. Conditions on survival at age 40, "
                   "which is not the subject's index age.")},
    funding=None,
    notes=("Also reports, among men, 3.84 [0.61-8.59] CVD-free years lost with clinical "
           "insomnia and 6.73 [5.31-8.48] with sleep-related breathing disorders; those are "
           "diagnosed disorders, not restriction, and are not extracted."),
)

add(
    study_id="hafner2017_rand_sleep_costs",
    citation=("Hafner M, Stepanek M, Taylor J, Troxel WM, van Stolk C. Why Sleep Matters - "
              "The Economic Costs of Insufficient Sleep: A Cross-Country Comparative "
              "Analysis. Rand Health Quarterly. 2017;6(4):11. (RAND Corporation research "
              "report RR-1791.)"),
    doi=None, pmid="28983434",
    url="https://www.rand.org/pubs/research_reports/RR1791.html",
    verification={"crossref_ok": None, "pubmed_ok": True, "title_similarity": None,
                  "status": "VERIFIED",
                  "resolved_title": ("Why Sleep Matters-The Economic Costs of Insufficient "
                                     "Sleep: A Cross-Country Comparative Analysis.")},
    access_tier="full_text", design="normative_descriptive", n=None,
    population={"age_mean": None, "age_range": [16, 70], "pct_female": None,
                "country": "US, UK, Japan, Germany, Canada", "adolescent_match": "fair_adult"},
    effects=[
        eff("log_rr_all_cause_mortality_under_6h_vs_7_9h", "log_rr", math.log(1.13),
            None, None,
            ("Insufficient Sleep Increases Mortality Risk by up to 13 Per Cent Investigating "
             "the link between sleep duration and mortality we find that at any given point "
             "in time, an individual that sleeps on average less than six hours per night has "
             "a 13 per cent higher mortality risk than an individual sleeping between seven "
             "and nine hours, which is considered as the healthy amount of sleep. Furthermore, "
             "an individual sleeping between six and seven hours per night has a 7 per cent "
             "higher mortality risk."),
            unit="log relative risk of all-cause mortality, <6 h vs 7-9 h habitual sleep",
            exposure={"type": "habitual_short_sleep", "dose_h": 5.5, "referent_h": 8.0,
                      "duration_days": None,
                      "contrast_label": "habitual sleep <6 h vs 7-9 h per night"},
            conv="log_rr = ln(1.13) = 0.12222; no CI reported in the report, so se is null",
            direction=("positive = elevated mortality with short sleep. THE ONLY QUANTITY IN "
                       "THE RAND REPORT USABLE BY THIS PROJECT. Fed through this shard's life "
                       "table, HR 1.13 costs -1.488 y (-17.9 months) of e19 if sustained for "
                       "life from 19, but only -0.026 y (-0.31 months) if confined to a "
                       "3-year window at ages 19-21. That 58-fold gap is the central "
                       "modelling decision in the mortality channel."),
            cohort="RAND_macro_model"),
        eff("log_rr_all_cause_mortality_6_to_7h_vs_7_9h", "log_rr", math.log(1.07),
            None, None,
            ("Furthermore, an individual sleeping between six and seven hours per night has a "
             "7 per cent higher mortality risk."),
            unit="log relative risk of all-cause mortality, 6-7 h vs 7-9 h habitual sleep",
            exposure={"type": "habitual_short_sleep", "dose_h": 6.5, "referent_h": 8.0,
                      "duration_days": None,
                      "contrast_label": "habitual sleep 6-7 h vs 7-9 h per night"},
            conv="log_rr = ln(1.07) = 0.06766; no CI reported, so se is null",
            direction=("positive = elevated mortality. Gives a crude dose-response: roughly "
                       "half the excess at 6-7 h versus <6 h. Worth -0.821 y (-9.9 months) of "
                       "e19 if lifelong."),
            cohort="RAND_macro_model"),
    ],
    rob={"tool": "ROBINS-I", "judgement": "critical",
         "notes": ("The 13% and 7% figures are ASSOCIATIONS imported from prior observational "
                   "meta-analyses of self-reported sleep duration and then treated as causal "
                   "inside a macroeconomic model, with no sensitivity analysis for reverse "
                   "causation and no confidence intervals reported. No adolescent or "
                   "young-adult stratum. The report's primary outputs are GDP, working days "
                   "and employment, not health.")},
    funding="RAND Corporation / Vitality Group (per report)",
    notes=("THE MOST COMMONLY MISCITED SOURCE IN THIS DOMAIN. RAND DOES NOT PUBLISH A LIFE-"
           "EXPECTANCY OR QALY ESTIMATE for short sleep; anyone citing it for 'years of life "
           "lost to short sleep' is misciting it. Its US findings are: economic cost $280-411 "
           "billion per year (1.56-2.28% of GDP, 2015 prices) and about 1.23 million working "
           "days lost annually, quoted verbatim as 'sustains by far the highest annual "
           "economic loss (between $280 billion and $411 billion currently, depending on the "
           "scenario) due to the size of its economy, followed by Japan (between $88 billion "
           "and $138 billion)'. rand.org returns HTTP 403 to automated clients, so the text "
           "was retrieved from the PubMed Central copy of the Rand Health Quarterly reprint "
           "(PMC5627640); the report has no DOI, so that field is null rather than guessed, "
           "and verification is via PubMed."),
)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for rec in RECORDS:
        p = OUT / f"{rec['study_id']}.yaml"
        p.write_text(yaml.safe_dump(rec, sort_keys=False, allow_unicode=True, width=100))
    print(f"wrote {len(RECORDS)} records to {OUT}")
    ids = [r["study_id"] for r in RECORDS]
    assert len(set(ids)) == len(ids), "duplicate study_id"
    print("\n".join(sorted(ids)))


if __name__ == "__main__":
    main()
