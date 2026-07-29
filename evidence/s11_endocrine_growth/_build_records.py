#!/usr/bin/env python3
"""Emit + schema-validate the s11_endocrine_growth evidence records.

Every value in R below was copied from an abstract/full text actually retrieved in this
session; the `quote` field on each effect carries the verbatim supporting sentence.
Derived SEs are documented in `conversion_formula`.
"""
import json
import os
import sys

import yaml

SHARD = "s11_endocrine_growth"
OUT = os.path.dirname(os.path.abspath(__file__))
SCHEMA = "/workspace/spec/effect.schema.json"


def v(title, crossref=True, pubmed=True, status="VERIFIED"):
    return {"crossref_ok": crossref, "pubmed_ok": pubmed,
            "resolved_title": title, "status": status}


R = []

# ---------------------------------------------------------------- GROWTH HORMONE
R.append(dict(
    study_id="vancauter1998",
    citation="Van Cauter E, Plat L, Copinschi G. Interrelations between sleep and the somatotropic axis. Sleep. 1998;21(6):553-566.",
    doi="10.1093/sleep/21.6.553", pmid="9779515",
    verification=v("Interrelations between sleep and the somatotropic axis."),
    access_tier="abstract_only", secondhand_via=None,
    design="normative_descriptive", tier="TX", n=None, n_studies_pooled=None,
    population={"age_mean": None, "age_range": None, "pct_female": 0.0,
                "country": "US/BE", "adolescent_match": "mixed"},
    effects=[
        dict(outcome_domain="endocrine", outcome_construct="fraction_of_24h_gh_output_secreted_during_early_sleep",
             exposure={"type": "descriptive", "dose_h": None, "referent_h": None,
                       "duration_days": None, "contrast_label": "narrative synthesis, adult men, normal sleep"},
             scale="pct_change", unit="% of 24-h GH output", value=70.0, se=None, ci=None,
             conversion_formula=None, from_figure=False, inferred_from_ci=False,
             direction_note="Positive = share of daily GH output that is sleep-associated. This is the SIZE OF THE EXPOSED FRACTION, not a harm estimate. Review states 'approximately' with no dispersion, hence se=null.",
             covariates=[], followup_years=None, cohort_family=None,
             quote="In men, approximately 70% of the daily GH output occurs during early sleep throughout adulthood."),
        dict(outcome_domain="endocrine", outcome_construct="sws_gh_dose_response_qualitative",
             exposure={"type": "descriptive", "dose_h": None, "referent_h": None,
                       "duration_days": None, "contrast_label": "amount of SW sleep vs concomitant GH secretion"},
             scale="pct_change", unit="qualitative (linear relation asserted, no slope reported)", value=0.0, se=None, ci=None,
             conversion_formula=None, from_figure=False, inferred_from_ci=False,
             direction_note="value=0 is a PLACEHOLDER: the review asserts a linear SWS-GH relation but reports no slope. Do NOT pool this as an effect; it is mechanism context only.",
             covariates=[], followup_years=None, cohort_family=None,
             quote="There is a linear relationship between amounts of SW sleep--whether measured by visual scoring or by delta activity--and amounts of concomitant GH secretion, although dissociations may occur, most likely because of variable levels of somatostatin inhibition."),
    ],
    rob={"tool": "none", "judgement": "na",
         "notes": "narrative review; the 70% figure is the canonical source of the 'GH is a sleep hormone' claim but is given without a CI"},
    funding="NIH / non-US government",
    notes="Establishes the size of the sleep-dependent GH fraction in men (~70%). Compare with brandenberger2004 which measured 52.8 +/- 3.5% directly. The two bracket the plausible range 50-70%.",
    shard=SHARD,
))

R.append(dict(
    study_id="brandenberger2004",
    citation="Brandenberger G, Weibel L. The 24-h growth hormone rhythm in men: sleep and circadian influences questioned. J Sleep Res. 2004;13(3):251-255.",
    doi="10.1111/j.1365-2869.2004.00415.x", pmid="15339260",
    verification=v("The 24-h growth hormone rhythm in men: sleep and circadian influences questioned"),
    access_tier="abstract_only", secondhand_via=None,
    design="cross_sectional", tier="TX", n=21, n_studies_pooled=None,
    population={"age_mean": None, "age_range": None, "pct_female": 0.0,
                "country": "FR", "adolescent_match": "fair_adult"},
    effects=[
        dict(outcome_domain="endocrine", outcome_construct="sleep_related_gh_pulse_as_pct_of_24h_gh_production",
             exposure={"type": "descriptive", "dose_h": 8, "referent_h": None, "duration_days": None,
                       "contrast_label": "day-active men, habitual 23:00-07:00 sleep, 10-min sampling over 24 h (n=10)"},
             scale="pct_change", unit="% of 24-h GH production", value=52.8, se=3.5,
             ci=[45.9, 59.7],
             conversion_formula="se = reported SEM (3.5); ci = 52.8 +/- 1.96*3.5. Implied SD = 3.5*sqrt(10) = 11.07.",
             from_figure=False, inferred_from_ci=False,
             direction_note="Positive = share of 24-h GH production attributable to the sleep-onset pulse. This is the EXPOSED FRACTION, not a harm.",
             covariates=[], followup_years=None, cohort_family=None,
             quote="In day-active subjects, melatonin and GH showed the well-known 24-h profiles, with a major sleep-related GH pulse accounting for 52.8 +/- 3.5% of the 24-h GH production and the onset of the melatonin surge occurring at 21:53 hours +/- 18 min."),
        dict(outcome_domain="endocrine", outcome_construct="total_24h_gh_secretion_under_displaced_sleep",
             exposure={"type": "other", "dose_h": 8, "referent_h": 8, "duration_days": None,
                       "contrast_label": "night workers sleeping 07:00-15:00 (n=11) vs day-active men (n=10)"},
             scale="pct_change", unit="% change in 24-h GH production", value=0.0, se=None, ci=None,
             conversion_formula=None, from_figure=False, inferred_from_ci=False,
             direction_note="value=0 encodes the authors' finding of NO net change in 24-h GH output ('constant') despite a blunted sleep-onset pulse. Negative would mean genuine loss. No dispersion reported, so se=null; treat as a qualitative null.",
             covariates=[], followup_years=None, cohort_family=None,
             quote="The sleep-related GH pulse was lowered, but the reduction was compensated for by the emergence of large individual pulses occurring unpredictably during waking periods, so that the total amount of GH secreted during the 24 h was constant."),
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "moderate",
         "notes": "small n; night workers vs day workers is a between-group comparison with self-selection; 10-min sampling over 24 h is a strong exposure measure"},
    funding=None,
    notes="THE decisive study for the redistribution-vs-loss question. Sleep displacement blunts the sleep-onset GH pulse but 24-h total GH is preserved by compensatory waking pulses. Authors generalise this explicitly to sleep deprivation: 'the blunting of the sleep-related GH pulse is counteracted, as in sleep-deprived persons, by a compensatory mechanism promoting GH pulses during wakefulness.'",
    shard=SHARD,
))

R.append(dict(
    study_id="spiegel2000gh",
    citation="Spiegel K, Leproult R, Colecchia EF, L'Hermite-Baleriaux M, Nie Z, Copinschi G, Van Cauter E. Adaptation of the 24-h growth hormone profile to a state of sleep debt. Am J Physiol Regul Integr Comp Physiol. 2000;279(3):R874-R883.",
    doi="10.1152/ajpregu.2000.279.3.R874", pmid="10956244",
    verification=v("Adaptation of the 24-h growth hormone profile to a state of sleep debt"),
    access_tier="abstract_only", secondhand_via="magee2010 (Journal of Obesity 2010;2010:821710) for the direction of the 24-h GH change",
    design="lab_restriction_within_subject", tier="T1", n=11, n_studies_pooled=None,
    population={"age_mean": None, "age_range": None, "pct_female": 0.0,
                "country": "US", "adolescent_match": "good_young_adult"},
    effects=[
        dict(outcome_domain="endocrine", outcome_construct="gh_profile_shape_biphasic_redistribution",
             exposure={"type": "chronic_restriction", "dose_h": 4, "referent_h": 12, "duration_days": 6,
                       "contrast_label": "6 nights 4 h TIB (01:00-05:00) vs 7 nights 12 h TIB (21:00-09:00)"},
             scale="pct_change", unit="qualitative pattern change (biphasic vs monophasic)", value=0.0, se=None, ci=None,
             conversion_formula=None, from_figure=False, inferred_from_ci=False,
             direction_note="value=0 encodes REDISTRIBUTION not loss: a presleep 'circadian' pulse appears and is NEGATIVELY correlated with the postsleep pulse, i.e. the two trade off. No 24-h total is quoted in the abstract, so no signed magnitude is extractable.",
             covariates=[], followup_years=None, cohort_family="UChicago_VanCauter_sleepdebt",
             quote="During the state of sleep debt, the GH secretory pattern was biphasic, with both a presleep onset \"circadian\" pulse and a postsleep onset pulse. Postsleep onset GH secretion was negatively related to presleep onset secretion and tended to be positively correlated with the amount of concomitant SWA."),
        dict(outcome_domain="sleep_need", outcome_construct="sws_and_swa_under_4h_restriction",
             exposure={"type": "chronic_restriction", "dose_h": 4, "referent_h": 12, "duration_days": 6,
                       "contrast_label": "6 nights 4 h TIB vs 7 nights 12 h TIB"},
             scale="pct_change", unit="qualitative direction (increase)", value=1.0, se=None, ci=None,
             conversion_formula=None, from_figure=False, inferred_from_ci=False,
             direction_note="Positive = SWS/SWA INCREASED under restriction. Slow-wave sleep, the GH-permissive stage, is preserved and intensified rather than sacrificed. No magnitude in abstract.",
             covariates=[], followup_years=None, cohort_family="UChicago_VanCauter_sleepdebt",
             quote="When sleep was restricted, both SWS and SWA were increased during early sleep."),
    ],
    rob={"tool": "RoB2", "judgement": "some_concerns",
         "notes": "n=11, no blinding possible, comparator is 12 h TIB (supraphysiological) not 8 h, which exaggerates any contrast versus real-world sleep"},
    funding="NIH / non-US government / US government",
    notes=("Full text is paywalled (OpenAlex oa_status=closed; publisher blocks scraping), so only the abstract was read directly. "
           "A review by the same literature (Magee CA et al., J Obesity 2010) characterises the direction of the 24-h change: "
           "'The elevation in GH levels observed by Spiegel et al. [41] was the result of an extended period of nocturnal GH secretion.' "
           "i.e. GH went UP, via a lengthened secretory window, not down. Authors' own summary: 'neither the GH profile nor the "
           "distribution of SWA conformed with predictions from acute sleep deprivation studies, indicating that adaptation "
           "mechanisms are operative during chronic partial sleep loss.'"),
    shard=SHARD,
))

R.append(dict(
    study_id="magee2010",
    citation="Magee CA, Huang XF, Iverson DC, Caputi P. Examining the pathways linking chronic sleep restriction to obesity. J Obes. 2010;2010:821710.",
    doi="10.1155/2010/821710", pmid="20798899",
    verification=v("Examining the Pathways Linking Chronic Sleep Restriction to Obesity"),
    access_tier="full_text", secondhand_via="reports the direction of the Spiegel 2000 (PMID 10956244) 24-h GH result",
    design="normative_descriptive", tier="TX", n=None, n_studies_pooled=None,
    population={"age_mean": None, "age_range": None, "pct_female": None,
                "country": "AU", "adolescent_match": "mixed"},
    effects=[
        dict(outcome_domain="endocrine", outcome_construct="direction_of_24h_gh_change_under_chronic_restriction",
             exposure={"type": "chronic_restriction", "dose_h": 4, "referent_h": 12, "duration_days": 6,
                       "contrast_label": "secondhand report of Spiegel 2000: 6 nights of 4 h sleep"},
             scale="pct_change", unit="qualitative direction (increase in GH exposure)", value=1.0, se=None, ci=None,
             conversion_formula=None, from_figure=False, inferred_from_ci=False,
             direction_note="Positive = GH levels INCREASED (not decreased) under 6 nights of 4 h sleep, via a lengthened nocturnal secretory window. This is the secondhand confirmation that the GH change is redistribution/extension, not loss.",
             covariates=[], followup_years=None, cohort_family=None,
             quote="In particular, six consecutive nights of sleep restriction (four hours sleep per night) were associated with increases in sympathetic nervous system (SNS) activity, evening cortisol levels and growth hormone levels (GH), and reductions in thyroid stimulating hormone (TSH), and leptin [16, 17, 41]. ... The elevation in GH levels observed by Spiegel et al. [41] was the result of an extended period of nocturnal GH secretion."),
    ],
    rob={"tool": "AMSTAR-2", "judgement": "high",
         "notes": "narrative review, no systematic search; used ONLY to establish the sign of a result whose primary full text is paywalled"},
    funding=None,
    notes="Reference [41] in this review was confirmed by parsing the article's own reference list to be Spiegel K, Leproult R, Colecchia EF, et al. Am J Physiol 2000;279(3):R874-R883, doi 10.1152/ajpregu.2000.279.3.R874.",
    shard=SHARD,
))

R.append(dict(
    study_id="vancauter1992",
    citation="Van Cauter E, Kerkhofs M, Caufriez A, Van Onderbergen A, Thorner MO, Copinschi G. A quantitative estimation of growth hormone secretion in normal man: reproducibility and relation to sleep and time of day. J Clin Endocrinol Metab. 1992;74(6):1441-1450.",
    doi="10.1210/jcem.74.6.1592892", pmid="1592892",
    verification=v("A quantitative estimation of growth hormone secretion in normal man: reproducibility and relation to sleep and time of day."),
    access_tier="abstract_only", secondhand_via=None,
    design="lab_restriction_within_subject", tier="T1", n=8, n_studies_pooled=None,
    population={"age_mean": None, "age_range": None, "pct_female": 0.0,
                "country": "BE", "adolescent_match": "good_young_adult"},
    effects=[
        dict(outcome_domain="endocrine", outcome_construct="gh_secretory_rate_multiple_during_sleep_vs_waking",
             exposure={"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                       "contrast_label": "sleep (including sleep delayed to 04:00) vs normal waking hours, deconvolution of 15-min sampling"},
             scale="raw_units", unit="fold-change in GH secretory rate vs normal waking hours", value=3.0, se=None, ci=None,
             conversion_formula=None, from_figure=False, inferred_from_ci=False,
             direction_note="Positive = GH secretory rate is 3x higher during sleep than during normal waking hours; crucially this holds even when sleep is DELAYED to 04:00, so the driver is sleep itself, not clock time. No dispersion reported.",
             covariates=[], followup_years=None, cohort_family=None,
             quote="During normal waking hours, the GH secretory rate was similar in the evening and the morning. This secretory rate was doubled during wakefulness at times of habitual sleep and tripled during sleep, even when sleep was delayed until 0400 h."),
        dict(outcome_domain="endocrine", outcome_construct="pct_of_sleep_gh_pulses_associated_with_slow_wave_stages",
             exposure={"type": "descriptive", "dose_h": None, "referent_h": None, "duration_days": None,
                       "contrast_label": "GH pulses during sleep, 8 men x 6 sessions"},
             scale="pct_change", unit="% of sleep GH pulses that are SW-associated", value=68.7, se=None, ci=[57.8, 78.2],
             conversion_formula="value = 57/83 = 68.67%; ci = exact binomial (Wilson) 95% interval for 57/83 computed as [0.578, 0.782].",
             from_figure=False, inferred_from_ci=True,
             direction_note="Positive = share of sleep GH pulses coupled to slow-wave stages. Exposed-fraction quantity, not a harm.",
             covariates=[], followup_years=None, cohort_family=None,
             quote="Almost 70% (57 of 83) of the pulses occurring during sleep were associated with slow wave (SW) stages."),
        dict(outcome_domain="exposure_measurement", outcome_construct="within_vs_between_subject_variability_of_24h_gh_output",
             exposure={"type": "descriptive", "dose_h": None, "referent_h": None, "duration_days": None,
                       "contrast_label": "coefficient of variation of total GH secreted, within-subject vs across-subject"},
             scale="pct_change", unit="CV %", value=32.0, se=None, ci=None,
             conversion_formula=None, from_figure=False, inferred_from_ci=False,
             direction_note="Positive = within-subject CV of total GH secreted (32%) vs across-subject CV (65%). Total GH output varies 10-fold between men; this is the measurement-noise floor against which any sleep-restriction GH effect must be judged.",
             covariates=[], followup_years=None, cohort_family=None,
             quote="The total amount of GH secreted varied 10-fold across individual studies, but the within-subject variability (32%) was less than half the across-subject variability (65%)."),
    ],
    rob={"tool": "RoB2", "judgement": "some_concerns", "notes": "n=8 healthy men; 6 sessions each; no blinding possible"},
    funding="Non-US government / US PHS",
    notes="Also reports that IGF-I levels 'did not correlate with the amount of GH secreted' - relevant because IGF-I, not GH pulse amplitude, is the growth-relevant downstream signal.",
    shard=SHARD,
))

R.append(dict(
    study_id="sassin1969",
    citation="Sassin JF, Parker DC, Mace JW, Gotlin RW, Johnson LC, Rossman LG. Human growth hormone release: relation to slow-wave sleep and sleep-waking cycles. Science. 1969;165(3892):513-515.",
    doi="10.1126/science.165.3892.513", pmid="4307378",
    verification=v("Human Growth Hormone Release: Relation to Slow-Wave Sleep and Sleep-Waking Cycles"),
    access_tier="abstract_only", secondhand_via=None,
    design="lab_restriction_within_subject", tier="T1", n=None, n_studies_pooled=None,
    population={"age_mean": None, "age_range": None, "pct_female": None,
                "country": "US", "adolescent_match": "mixed"},
    effects=[
        dict(outcome_domain="endocrine", outcome_construct="gh_release_follows_sleep_not_clock_time",
             exposure={"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                       "contrast_label": "12-h reversal of the sleep-waking cycle"},
             scale="pct_change", unit="qualitative (GH pulse moves with sleep)", value=0.0, se=None, ci=None,
             conversion_formula=None, from_figure=False, inferred_from_ci=False,
             direction_note="value=0 encodes 'the GH pulse follows sleep wherever sleep is placed' - i.e. GH is time-shiftable rather than time-locked. Mechanism context only; not poolable. n not stated in the abstract.",
             covariates=[], followup_years=None, cohort_family=None,
             quote="When sleep-waking cycles are reversed by 12 hours, the release of growth hormone with sleep is reversed; thus release does not follow an inherent circadian rhythm independent of sleep."),
    ],
    rob={"tool": "RoB2", "judgement": "high", "notes": "1969 paper, n not stated in abstract, full text not retrieved"},
    funding=None,
    notes="Historical anchor: the sleep-GH coupling is a coupling to sleep, not to a clock hour. Directly implies that shifting or shortening sleep MOVES the GH pulse.",
    shard=SHARD,
))

R.append(dict(
    study_id="vancauter2000",
    citation="Van Cauter E, Leproult R, Plat L. Age-related changes in slow wave sleep and REM sleep and relationship with growth hormone and cortisol levels in healthy men. JAMA. 2000;284(7):861-868.",
    doi="10.1001/jama.284.7.861", pmid="10938176",
    verification=v("Age-Related Changes in Slow Wave Sleep and REM Sleep and Relationship With Growth Hormone and Cortisol Levels in Healthy Men"),
    access_tier="abstract_only", secondhand_via=None,
    design="cross_sectional", tier="TX", n=149, n_studies_pooled=None,
    population={"age_mean": None, "age_range": [16, 83], "pct_female": 0.0,
                "country": "US/BE", "adolescent_match": "mixed"},
    effects=[
        dict(outcome_domain="sleep_need", outcome_construct="pct_slow_wave_sleep_age_16_25",
             exposure={"type": "descriptive", "dose_h": None, "referent_h": None, "duration_days": None,
                       "contrast_label": "healthy men aged 16-25 y, polysomnography"},
             scale="pct_change", unit="% of sleep period spent in deep slow wave sleep", value=18.9, se=1.3,
             ci=[16.4, 21.4],
             conversion_formula="se = reported SEM (1.3); ci = 18.9 +/- 1.96*1.3.",
             from_figure=False, inferred_from_ci=False,
             direction_note="Positive = more SWS. BASELINE ANCHOR for a 16-19 year old: at this age SWS occupies ~19% of the sleep period, the lifetime maximum, and it falls to 3.4% by midlife.",
             covariates=[], followup_years=None, cohort_family="VanCauter_pooled_1985_1999",
             quote="The mean (SEM) percentage of deep slow wave sleep decreased from 18.9% (1.3%) during early adulthood (age 16-25 years) to 3.4% (1.0%) during midlife (age 36-50 years) and was replaced by lighter sleep (stages 1 and 2) without significant increases in sleep fragmentation or decreases in rapid eye movement (REM) sleep."),
        dict(outcome_domain="endocrine", outcome_construct="gh_secretion_decline_per_decade_early_adulthood_to_midlife",
             exposure={"type": "descriptive", "dose_h": None, "referent_h": None, "duration_days": None,
                       "contrast_label": "per decade of age, early adulthood (16-25 y) to midlife (36-50 y)"},
             scale="per_hour_beta", unit="microgram of 24-h GH secretion lost per decade of age",
             value=-372.0, se=None, ci=None,
             conversion_formula=None, from_figure=False, inferred_from_ci=False,
             direction_note="Negative = GH secretion falls with age. NOT a sleep-restriction effect. This is the COMPARATOR MAGNITUDE: normal ageing removes 372 microgram of 24-h GH per decade, which dwarfs anything an 8-night restriction protocol produces. P<.001; no SE reported.",
             covariates=["age"], followup_years=None, cohort_family="VanCauter_pooled_1985_1999",
             quote="The decline in slow wave sleep from early adulthood to midlife was paralleled by a major decline in GH secretion (-372 microg per decade; P<.001). From midlife to late life, GH secretion further declined at a slower rate (-43 microg per decade; P<.02). Independently of age, the amount of GH secretion was significantly associated with slow wave sleep (P<.001)."),
        dict(outcome_domain="endocrine", outcome_construct="evening_cortisol_rise_per_decade_of_age",
             exposure={"type": "descriptive", "dose_h": None, "referent_h": None, "duration_days": None,
                       "contrast_label": "per decade of age, significant only after age 50 y"},
             scale="per_hour_beta", unit="nmol/L evening cortisol per decade of age", value=19.3, se=None, ci=None,
             conversion_formula=None, from_figure=False, inferred_from_ci=False,
             direction_note="Positive = higher evening cortisol with age. Comparator magnitude for the sleep-restriction cortisol effects; note it becomes significant only after age 50, i.e. it is NOT a young-adult phenomenon. P<.001; no SE reported.",
             covariates=["age"], followup_years=None, cohort_family="VanCauter_pooled_1985_1999",
             quote="Increasing age was associated with an elevation of evening cortisol levels (+19. 3 nmol/L per decade; P<.001) that became significant only after age 50 years, when sleep became more fragmented and REM sleep declined."),
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "moderate",
         "notes": "cross-sectional pooling of studies run 1985-1999 across 4 laboratories; healthy volunteers only; age gradients are between-subject, not longitudinal"},
    funding="Non-US government / US PHS",
    notes="Frequently miscited as evidence that sleep loss destroys GH. It is an AGE-gradient study, not a sleep-restriction study. Its real value here is (a) the 16-25 y SWS baseline of 18.9% and (b) the magnitude of the ageing comparator.",
    shard=SHARD,
))

# ------------------------------------------------------------------ TESTOSTERONE
R.append(dict(
    study_id="leproult2011",
    citation="Leproult R, Van Cauter E. Effect of 1 week of sleep restriction on testosterone levels in young healthy men. JAMA. 2011;305(21):2173-2174.",
    doi="10.1001/jama.2011.710", pmid="21632481",
    verification=v("Effect of 1 Week of Sleep Restriction on Testosterone Levels in Young Healthy Men"),
    access_tier="full_text", secondhand_via=None,
    design="lab_restriction_within_subject", tier="T1", n=10, n_studies_pooled=None,
    population={"age_mean": 24.3, "age_range": None, "pct_female": 0.0,
                "country": "US", "adolescent_match": "good_young_adult"},
    effects=[
        dict(outcome_domain="endocrine", outcome_construct="daytime_total_testosterone_0800_2200",
             exposure={"type": "chronic_restriction", "dose_h": 5, "referent_h": 10, "duration_days": 8,
                       "contrast_label": "8 nights 5 h TIB (00:30-05:30) vs 3 nights 10 h TIB (22:00-08:00); TST 4h48m vs 8h55m"},
             scale="pct_change", unit="% change in mean daytime total testosterone", value=-10.33, se=4.54,
             ci=[-20.60, -0.06],
             conversion_formula=("value = 100*(16.5-18.4)/18.4 = -10.33%. Paired SE inferred from the reported two-sided "
                                 "P=.049 with n=10: t(9) at p=.049 = 2.2745, so SE(diff) = 1.90/2.2745 = 0.835 nmol/L = 4.54 "
                                 "percentage points of the 18.4 nmol/L referent; ci = value +/- t(9,.05)=2.2622 * SE."),
             from_figure=False, inferred_from_ci=True,
             direction_note="Negative = LOWER testosterone under restriction (harm). Upper CI bound is -0.06%, i.e. the interval only just excludes zero.",
             covariates=[], followup_years=None, cohort_family="UChicago_VanCauter_sleepdebt",
             quote="During waking hours common to both conditions (8 AM-10 PM), testosterone levels were lower after sleep restriction than in the rested condition (16.5 [2.8] nmol/L vs 18.4 [3.8] nmol/L; P = .049)."),
        dict(outcome_domain="endocrine", outcome_construct="daytime_total_testosterone_0800_2200_smd",
             exposure={"type": "chronic_restriction", "dose_h": 5, "referent_h": 10, "duration_days": 8,
                       "contrast_label": "8 nights 5 h TIB vs 3 nights 10 h TIB"},
             scale="hedges_g", unit=None, value=-0.52, se=0.23, ci=[-0.97, -0.07],
             conversion_formula=("SD_pooled = sqrt((3.8^2 + 2.8^2)/2) = 3.3377 nmol/L; d = -1.90/3.3377 = -0.5693; "
                                 "J = 1 - 3/(4*9-1) = 0.9143; g = -0.5205. SE(g) = (0.835/3.3377)*0.9143 = 0.2288. "
                                 "ci = g +/- 1.96*SE. Between-condition SD used (conservative for a paired design)."),
             from_figure=False, inferred_from_ci=True,
             direction_note="Negative = lower testosterone under restriction (harm).",
             covariates=[], followup_years=None, cohort_family="UChicago_VanCauter_sleepdebt",
             quote="During waking hours common to both conditions (8 AM-10 PM), testosterone levels were lower after sleep restriction than in the rested condition (16.5 [2.8] nmol/L vs 18.4 [3.8] nmol/L; P = .049)."),
        dict(outcome_domain="endocrine", outcome_construct="afternoon_evening_total_testosterone_1400_2200",
             exposure={"type": "chronic_restriction", "dose_h": 5, "referent_h": 10, "duration_days": 8,
                       "contrast_label": "8 nights 5 h TIB vs 3 nights 10 h TIB, 14:00-22:00 window"},
             scale="pct_change", unit="% change in mean 14:00-22:00 total testosterone", value=-13.41, se=4.75,
             ci=[-24.16, -2.66],
             conversion_formula=("value = 100*(15.5-17.9)/17.9 = -13.41%. SE inferred from two-sided P=.02, n=10: "
                                 "t(9) at p=.02 = 2.8214, SE(diff) = 2.40/2.8214 = 0.851 nmol/L = 4.75 pp of 17.9; "
                                 "ci = value +/- 2.2622*SE."),
             from_figure=False, inferred_from_ci=True,
             direction_note="Negative = lower testosterone under restriction (harm). This is the largest, most robustly significant window.",
             covariates=[], followup_years=None, cohort_family="UChicago_VanCauter_sleepdebt",
             quote="The effect of restricted sleep was especially apparent between 2 PM and 10 PM (15.5 [3.1] nmol/L vs 17.9 [4.0] nmol/L; P = .02)."),
        dict(outcome_domain="endocrine", outcome_construct="daytime_cortisol_profile",
             exposure={"type": "chronic_restriction", "dose_h": 5, "referent_h": 10, "duration_days": 8,
                       "contrast_label": "8 nights 5 h TIB vs 3 nights 10 h TIB"},
             scale="pct_change", unit="% change in daytime cortisol", value=0.0, se=None, ci=None,
             conversion_formula=None, from_figure=False, inferred_from_ci=False,
             direction_note="value=0 encodes a reported NULL: at 5 h TIB for 8 nights there was no cortisol signal. Contrast with guyon2014/spiegel1999 at 4 h TIB, where evening cortisol rose 30-45%. Dose matters.",
             covariates=[], followup_years=None, cohort_family="UChicago_VanCauter_sleepdebt",
             quote="Daytime cortisol profiles were similar under both conditions (Figure). ... This testosterone decline was associated with lower vigor scores but not with increased levels of cortisol, a stress-responsive hormone that can inhibit gonadal function."),
        dict(outcome_domain="sleep_need", outcome_construct="stage3_plus_4_slow_wave_sleep_minutes_per_night",
             exposure={"type": "chronic_restriction", "dose_h": 5, "referent_h": 10, "duration_days": 8,
                       "contrast_label": "each 5 h restricted night vs the 10 h rested night"},
             scale="raw_units", unit="minutes of stage 3+4 sleep per night", value=9.0, se=2.53,
             ci=[3.28, 14.72],
             conversion_formula="se = reported SD(8 min)/sqrt(10) = 2.530; ci = 9 +/- t(9,.05)=2.2622 * SE.",
             from_figure=False, inferred_from_ci=False,
             direction_note=("Positive = MORE slow-wave sleep under restriction. Decisive mechanism: cutting TIB from 10 h to 5 h "
                             "cost 165 min of stage 2 and 63 min of REM but GAINED 9 min of stage 3+4. The GH-permissive stage is "
                             "protected, which is why GH output survives restriction."),
             covariates=[], followup_years=None, cohort_family="UChicago_VanCauter_sleepdebt",
             quote="Relative to the rested condition, during each restricted night, participants lost a total (SD) of 2 hours 45 minutes (29 min) of stage-2 sleep (P = .002) and 1 hour 3 minutes (18 min) of REM sleep (P = .002) and gained 9 minutes (8 min) of sleep in stages 3 + 4 (P = .01)."),
        dict(outcome_domain="sleep_need", outcome_construct="rem_sleep_minutes_per_night",
             exposure={"type": "chronic_restriction", "dose_h": 5, "referent_h": 10, "duration_days": 8,
                       "contrast_label": "each 5 h restricted night vs the 10 h rested night"},
             scale="raw_units", unit="minutes of REM sleep per night", value=-63.0, se=5.69,
             ci=[-75.88, -50.12],
             conversion_formula="se = reported SD(18 min)/sqrt(10) = 5.692; ci = -63 +/- 2.2622 * SE.",
             from_figure=False, inferred_from_ci=False,
             direction_note="Negative = REM sleep lost. REM and stage 2 absorb essentially the entire sleep debt.",
             covariates=[], followup_years=None, cohort_family="UChicago_VanCauter_sleepdebt",
             quote="Relative to the rested condition, during each restricted night, participants lost a total (SD) of 2 hours 45 minutes (29 min) of stage-2 sleep (P = .002) and 1 hour 3 minutes (18 min) of REM sleep (P = .002) and gained 9 minutes (8 min) of sleep in stages 3 + 4 (P = .01)."),
    ],
    rob={"tool": "RoB2", "judgement": "some_concerns",
         "notes": ("n=10 self-described convenience sample recruited by campus flyers; no randomisation of condition order (rested "
                   "always first, so an order/adaptation effect is not excluded); comparator is 10 h TIB, which is longer than any "
                   "realistic habitual sleep, so the true 8 h-referenced effect is smaller than reported")},
    funding="NHLBI 5R01HL72694-5; NIDDK P60DK-020595; NIH MO1-RR-00055",
    notes=("Authors' own conversion: divide nmol/L by 0.0347 for ng/dL. Rested mean 18.4 nmol/L = 530.3 ng/dL; restricted mean "
           "16.5 nmol/L = 475.5 ng/dL. Against the harmonized reference distribution for healthy nonobese men 19-39 y "
           "(travison2017: 2.5th 264, 5th 303, 50th 531, 95th 852 ng/dL) the RESTED mean sits at the 50th percentile (531) and "
           "the RESTRICTED mean at roughly the 34th percentile (z = -0.40), still 1.80x the 2.5th-percentile hypogonadal "
           "threshold of 264 ng/dL. Authors' framing: 'Daytime testosterone levels were decreased by 10% to 15% in this small "
           "convenience sample ... By comparison, normal aging is associated with a decrease of testosterone levels by 1% to 2% "
           "per year.' No participant was reported to have entered the hypogonadal range."),
    shard=SHARD,
))

R.append(dict(
    study_id="reynolds2012",
    citation="Reynolds AC, Dorrian J, Liu PY, Van Dongen HP, Wittert GA, Harmer LJ, Banks S. Impact of five nights of sleep restriction on glucose metabolism, leptin and testosterone in young adult men. PLoS One. 2012;7(7):e41218.",
    doi="10.1371/journal.pone.0041218", pmid="22844441",
    verification=v("Impact of Five Nights of Sleep Restriction on Glucose Metabolism, Leptin and Testosterone in Young Adult Men"),
    access_tier="full_text", secondhand_via=None,
    design="lab_restriction_within_subject", tier="T1", n=14, n_studies_pooled=None,
    population={"age_mean": 27.4, "age_range": None, "pct_female": 0.0,
                "country": "AU", "adolescent_match": "fair_adult"},
    effects=[
        dict(outcome_domain="endocrine", outcome_construct="total_testosterone_null_result",
             exposure={"type": "chronic_restriction", "dose_h": 4, "referent_h": 10, "duration_days": 5,
                       "contrast_label": "5 nights 4 h TIB (04:00-08:00) vs 2 baseline nights 10 h TIB (22:00-08:00)"},
             scale="pct_change", unit="% change in total testosterone (null)", value=0.0, se=None, ci=None,
             conversion_formula="No point estimate reported; only F(1,168)=2.8, p=0.089 (non-significant). value=0 encodes the null.",
             from_figure=False, inferred_from_ci=False,
             direction_note=("value=0 encodes a NON-REPLICATION of the Leproult 2011 testosterone effect at a MORE severe dose "
                             "(4 h vs 5 h TIB). Direction of the trend is not stated in the abstract."),
             covariates=[], followup_years=None, cohort_family=None,
             quote="Also, cortisol (F(1,168) = 10.2, p = 0.002) and leptin (F(1,168) = 10.7, p = 0.001) increased, sex hormone binding globulin (F(1,167) = 12.1, p<0.001) fell and there were no significant changes in ACTH (F(1,168) = 0.3, p = 0.59) or total testosterone (F(1,168) = 2.8, p = 0.089)."),
        dict(outcome_domain="endocrine", outcome_construct="mean_daytime_cortisol",
             exposure={"type": "chronic_restriction", "dose_h": 4, "referent_h": 10, "duration_days": 5,
                       "contrast_label": "5th night of 4 h TIB vs baseline 10 h TIB night, 09:00-20:00 sampling"},
             scale="pct_change", unit="% change in mean cortisol", value=15.47, se=None, ci=None,
             conversion_formula="value = 100*(337.4-292.2)/292.2 = 15.47%. SEs given are for each condition mean (16.9 and 18.1 nmol/L), not for the paired difference; the repeated-measures F was on 168 observations from 14 subjects, so a valid paired SE is not derivable. se=null.",
             from_figure=False, inferred_from_ci=False,
             direction_note="Positive = HIGHER cortisol under restriction (harm). p=0.002.",
             covariates=[], followup_years=None, cohort_family=None,
             quote="Cortisol was 15.5% higher after sleep restriction (mean +/- SE: 337.4+/-16.9 nmol/L) than at baseline (292.2+/-18.1), and this increase was statistically significant ( p = 0.002)."),
        dict(outcome_domain="endocrine", outcome_construct="evening_cortisol_1800h",
             exposure={"type": "chronic_restriction", "dose_h": 4, "referent_h": 10, "duration_days": 5,
                       "contrast_label": "5th night of 4 h TIB vs baseline 10 h TIB night, 18:00 timepoint"},
             scale="pct_change", unit="% change in 18:00 cortisol", value=67.32, se=None, ci=None,
             conversion_formula="value = 100*(298.0-178.1)/178.1 = 67.32%. F(1,97)=13.3, p<0.001. Reported SEMs are per-condition (41.4 and 17.9 nmol/L), not paired; se=null.",
             from_figure=False, inferred_from_ci=False,
             direction_note="Positive = higher evening cortisol under restriction (harm). Largest single-timepoint effect; consistent with guyon2014's +30% evening total cortisol.",
             covariates=[], followup_years=None, cohort_family=None,
             quote="Planned contrasts showed that cortisol levels were significantly higher at 16:00 on SR5 (mean +/- SEM; 247.1+/-21.9) than B1 (179.0+/-16.6; F 1,97 = 5.5, p = 0.02) and at 18:00 (SR5: 298.0+/-41.4, B1: 178.1+/-17.9; F 1,97 = 13.3, p <0.001)."),
    ],
    rob={"tool": "RoB2", "judgement": "some_concerns",
         "notes": "n=14, no randomisation of order (baseline always first), 10 h TIB comparator, food intake controlled at ~2000 kcal/d which is a strength"},
    funding="Non-US government",
    notes=("Key non-replication: at 4 h TIB for 5 nights - a HARSHER dose than Leproult 2011's 5 h for 8 nights - total testosterone "
           "did not change significantly (p=0.089). SHBG fell (p<0.001), which would tend to RAISE free testosterone. The cortisol "
           "signal replicated cleanly."),
    shard=SHARD,
))

R.append(dict(
    study_id="schmid2012",
    citation="Schmid SM, Hallschmid M, Jauch-Chara K, Lehnert H, Schultes B. Sleep timing may modulate the effect of sleep loss on testosterone. Clin Endocrinol (Oxf). 2012;77(5):749-754.",
    doi="10.1111/j.1365-2265.2012.04419.x", pmid="22568763",
    verification=v("Sleep timing may modulate the effect of sleep loss on testosterone"),
    access_tier="abstract_only", secondhand_via=None,
    design="lab_restriction_within_subject", tier="T1", n=15, n_studies_pooled=None,
    population={"age_mean": 27.1, "age_range": None, "pct_female": 0.0,
                "country": "DE", "adolescent_match": "fair_adult"},
    effects=[
        dict(outcome_domain="endocrine", outcome_construct="total_testosterone_late_bedtime_restriction_null",
             exposure={"type": "chronic_restriction", "dose_h": 4, "referent_h": 8, "duration_days": 2,
                       "contrast_label": "2 nights 4 h sleep with LATE bedtime (02:45-07:00) vs 8 h (22:45-07:00); 15-h hormone profile"},
             scale="pct_change", unit="% change in testosterone (null)", value=0.0, se=None, ci=None,
             conversion_formula="No point estimate reported; authors report no difference between conditions. value=0 encodes the null.",
             from_figure=False, inferred_from_ci=False,
             direction_note=("value=0 encodes a NULL. HIGHEST-RELEVANCE exposure pattern for a college student: the sleep loss is "
                             "taken off the FRONT of the night (late bedtime, fixed wake time). Under that pattern testosterone was "
                             "unaffected. Comparator is a realistic 8 h, not 10-12 h."),
             covariates=[], followup_years=None, cohort_family=None,
             quote="Serum LH, T and PRL concentrations showed characteristic diurnal variations across the 15-h period without any differences between the 4- and 8-h sleep conditions."),
        dict(outcome_domain="endocrine", outcome_construct="morning_testosterone_early_night_only_sleep",
             exposure={"type": "chronic_restriction", "dose_h": 4.5, "referent_h": 7, "duration_days": 1,
                       "contrast_label": "1 night 4.5 h sleep confined to the FIRST half of the night (22:30-03:30) vs 7 h (22:30-06:00), separate experiment n=8"},
             scale="pct_change", unit="% change in morning testosterone (direction only)", value=-1.0, se=None, ci=None,
             conversion_formula="No point estimate reported; only 'markedly decreased ... P <= 0.05'. value=-1 encodes a signed but unquantified decrease.",
             from_figure=False, inferred_from_ci=False,
             direction_note=("Negative = lower morning testosterone. The effect appears only when the subject is AWAKE during the "
                             "second half of the night. This is the mechanistic explanation for the Leproult-vs-Reynolds/Schmid "
                             "discrepancy and it depends on WHERE the sleep sits, not only on how much there is."),
             covariates=[], followup_years=None, cohort_family=None,
             quote="However, total sleep deprivation and 4.5 h of sleep restricted to the first night-half markedly decreased morning T and PRL concentrations (both P <= 0.05). ... While sleep loss in the early part of the night does not affect T and PRL, early awakening and wakefulness during the second part of the night reduces morning circulating T and PRL concentrations."),
    ],
    rob={"tool": "RoB2", "judgement": "some_concerns",
         "notes": "n=15 (main) and n=8 (second experiment); only 2 nights of restriction, so chronic adaptation is untested; no effect magnitudes reported for the positive finding"},
    funding="Non-US government",
    notes=("The single most decision-relevant modifier in this shard. Our subject's exposure is late-bedtime restriction with a "
           "fixed alarm - which is Schmid's 02:45-07:00 condition, the one that produced NO testosterone effect at all."),
    shard=SHARD,
))

R.append(dict(
    study_id="axelsson2005",
    citation="Axelsson J, Ingre M, Akerstedt T, Holmback U. Effects of acutely displaced sleep on testosterone. J Clin Endocrinol Metab. 2005;90(8):4530-4535.",
    doi="10.1210/jc.2005-0520", pmid="15914523",
    verification=v("Effects of Acutely Displaced Sleep on Testosterone"),
    access_tier="abstract_only", secondhand_via=None,
    design="rct_crossover", tier="T1", n=7, n_studies_pooled=None,
    population={"age_mean": None, "age_range": [22, 32], "pct_female": 0.0,
                "country": "SE", "adolescent_match": "good_young_adult"},
    effects=[
        dict(outcome_domain="endocrine", outcome_construct="testosterone_rise_across_night_sleep",
             exposure={"type": "other", "dose_h": 8, "referent_h": None, "duration_days": 1,
                       "contrast_label": "night sleep 23:00-07:00, hourly sampling; testosterone at sleep onset vs sleep offset"},
             scale="pct_change", unit="% rise in testosterone across the sleep period", value=65.4, se=None, ci=None,
             conversion_formula="value = 100*(25.3-15.3)/15.3 = 65.36%. Reported values are mean +/- SEM per timepoint (15.3+/-2.1 to 25.3+/-2.2 nmol/L); no SE for the within-subject change is derivable. se=null.",
             from_figure=False, inferred_from_ci=False,
             direction_note=("Positive = testosterone RISES during sleep and falls during wake. Quantifies how large the normal "
                             "sleep-driven testosterone swing is (~65% within one night), which is 5-6x larger than the 10-13% "
                             "daytime deficit reported under a week of restriction."),
             covariates=[], followup_years=None, cohort_family=None,
             quote="Mean testosterone levels increased as a log-linear function of time (hours) across both sleep periods (b = 4.88; P < 0.001), from 15.3 +/- 2.1 to 25.3 +/- 2.2 nmol/liter during night sleep and from 17.3 +/- 2.1 to 26.4 +/- 2.9 nmol/liter during day sleep."),
        dict(outcome_domain="endocrine", outcome_construct="testosterone_rise_across_daytime_sleep",
             exposure={"type": "other", "dose_h": 8, "referent_h": None, "duration_days": 1,
                       "contrast_label": "sleep displaced to 07:00-15:00, hourly sampling"},
             scale="pct_change", unit="% rise in testosterone across the sleep period", value=52.6, se=None, ci=None,
             conversion_formula="value = 100*(26.4-17.3)/17.3 = 52.60%. se=null for the same reason as above.",
             from_figure=False, inferred_from_ci=False,
             direction_note=("Positive = testosterone rises during sleep even when sleep is moved to the daytime, i.e. the driver is "
                             "SLEEP, not clock time. Implies testosterone is recoverable by sleeping, whenever that sleep occurs - "
                             "directly relevant to weekend catch-up."),
             covariates=[], followup_years=None, cohort_family=None,
             quote="In conclusion, testosterone increased during sleep and fell during waking, whereas circadian effects seemed marginal. Individual differences were pronounced."),
    ],
    rob={"tool": "RoB2", "judgement": "some_concerns", "notes": "n=7, balanced order, constant bed rest; very small sample and 'individual differences were pronounced'"},
    funding="Non-US government",
    notes="Mechanism: the testosterone deficit under restriction is a shortfall of sleep-driven accumulation, not damage to the gonadal axis. The axis works normally whenever sleep is provided.",
    shard=SHARD,
))

R.append(dict(
    study_id="killick2015",
    citation="Killick R, Hoyos CM, Melehan KL, Dungan GC, Poh J, Liu PY. Metabolic and hormonal effects of 'catch-up' sleep in men with chronic, repetitive, lifestyle-driven sleep restriction. Clin Endocrinol (Oxf). 2015;83(4):498-507.",
    doi="10.1111/cen.12747", pmid="25683266",
    verification=v("Metabolic and hormonal effects of 'catch-up' sleep in men with chronic, repetitive, lifestyle-driven sleep restriction"),
    access_tier="full_text", secondhand_via=None,
    design="rct_crossover", tier="T1", n=19, n_studies_pooled=None,
    population={"age_mean": 28.6, "age_range": [19, 49], "pct_female": 0.0,
                "country": "AU", "adolescent_match": "fair_adult"},
    effects=[
        dict(outcome_domain="recovery", outcome_construct="morning_total_testosterone_after_3_nights_catchup_sleep",
             exposure={"type": "recovery_sleep", "dose_h": 10, "referent_h": 6, "duration_days": 3,
                       "contrast_label": "3 weekend nights of 10 h TIB vs 3 weekend nights of 6 h TIB, in men with 5.1 y of habitual weekday restriction"},
             scale="raw_units", unit="nmol/L morning total testosterone", value=2.2, se=1.02, ci=[0.2, 4.2],
             conversion_formula="se = (4.2 - 0.2)/3.92 = 1.0204 nmol/L, from the reported 95% CI. +2.2 nmol/L = +63.4 ng/dL (using 1 nmol/L = 28.8 ng/dL).",
             from_figure=False, inferred_from_ci=True,
             direction_note=("Positive = testosterone RECOVERS (rises) with catch-up sleep. Three nights of extended sleep restored "
                             "morning testosterone in men with a 5-year history of exactly this weekday-restriction/weekend-catch-up "
                             "pattern. Effect present in the whole analysed subset (n=8) and in the younger subgroup alone (n=5). "
                             "This is the reversibility evidence."),
             covariates=[], followup_years=None, cohort_family=None,
             quote="Fasting morning testosterone levels were significantly higher following 10 h compared to 6 h (2.2 nM (0.2, 4.2); P = 0.03) in both the group as a whole ( n = 8) and in the younger group alone ( n = 5)."),
        dict(outcome_domain="recovery", outcome_construct="morning_cortisol_after_3_nights_catchup_sleep",
             exposure={"type": "recovery_sleep", "dose_h": 10, "referent_h": 6, "duration_days": 3,
                       "contrast_label": "3 weekend nights of 10 h TIB vs 6 h TIB"},
             scale="pct_change", unit="% change in morning cortisol (null)", value=0.0, se=None, ci=None,
             conversion_formula=None, from_figure=False, inferred_from_ci=False,
             direction_note=("value=0 encodes a NULL: morning cortisol did not differ between chronic 6 h and 10 h catch-up. In "
                             "chronically (not acutely) restricted men habituated to 6 h, there was no residual HPA signal to reverse."),
             covariates=[], followup_years=None, cohort_family=None,
             quote="'Catch-up' sleep increased morning testosterone and did not change morning cortisol."),
    ],
    rob={"tool": "RoB2", "judgement": "some_concerns",
         "notes": "randomised crossover but each man completed only 2 of 3 conditions, so the testosterone comparison rests on n=8; morning fasting single samples rather than 24-h profiles"},
    funding="NIH / non-US government",
    notes=("BEST EXPOSURE MATCH IN THE SHARD. Screening characteristics (Table 1): 'Age (years) 28.6 +/- 2.0 [range] 19-49; Midweek "
           "sleep 6 h 12 min +/- 7 min [range] 5 h 18 min-6 h 54 min; Weekend sleep 8 h 30 min +/- 9 min [range] 6 h 59 min-9 h 39 "
           "min; ... Duration of catch-up sleep patterns (years) 5.1 +/- 0.9 [range] 0.5-15.' That is the subject's pattern almost "
           "exactly: weekday 5-6 h, weekend 7-8 h, sustained for years. In these men the testosterone deficit was still fully "
           "reversible within 3 nights, and cortisol was already normal."),
    shard=SHARD,
))

R.append(dict(
    study_id="arnal2016",
    citation="Arnal PJ, Drogou C, Sauvet F, Regnauld J, Dispersyn G, Faraut B, Millet GY, Leger D, Gomez-Merino D, Chennaoui M. Effect of sleep extension on the subsequent testosterone, cortisol and prolactin responses to total sleep deprivation and recovery. J Neuroendocrinol. 2016;28(2):12346.",
    doi="10.1111/jne.12346", pmid="26647769",
    verification=v("Effect of Sleep Extension on the Subsequent Testosterone, Cortisol and Prolactin Responses to Total Sleep Deprivation and Recovery"),
    access_tier="abstract_only", secondhand_via=None,
    design="rct_crossover", tier="T1", n=14, n_studies_pooled=None,
    population={"age_mean": None, "age_range": None, "pct_female": 0.0,
                "country": "FR", "adolescent_match": "good_young_adult"},
    effects=[
        dict(outcome_domain="recovery", outcome_construct="testosterone_and_cortisol_return_to_baseline_after_one_recovery_night",
             exposure={"type": "recovery_sleep", "dose_h": 8, "referent_h": None, "duration_days": 1,
                       "contrast_label": "one night of recovery sleep after 24 h continuous awakening; 07:00 samples, baseline vs recovery"},
             scale="pct_change", unit="% residual deficit after one recovery night", value=0.0, se=None, ci=None,
             conversion_formula="No residual point estimate reported; authors state basal levels were recovered. value=0 encodes complete recovery.",
             from_figure=False, inferred_from_ci=False,
             direction_note=("value=0 = FULL RECOVERY. Testosterone, cortisol and prolactin all fell at 24 h of continuous "
                             "wakefulness and all returned to basal levels after a single recovery night. No carry-over."),
             covariates=[], followup_years=None, cohort_family=None,
             quote="At 24 h of awakening, testosterone, cortisol and prolactin concentrations were significantly lower compared to B-07.00 and recovered basal levels after recovery sleep at R-07.00 (P < 0.001 for all)."),
        dict(outcome_domain="endocrine", outcome_construct="effect_of_6_nights_prophylactic_sleep_extension_on_hormone_response",
             exposure={"type": "sleep_extension", "dose_h": 10, "referent_h": 8.5, "duration_days": 6,
                       "contrast_label": "6 nights 21:00-07:00 TIB (extended) vs 22:30-07:00 (habitual), then total sleep deprivation"},
             scale="pct_change", unit="% change in the hormone response attributable to prior extension (null)", value=0.0, se=None, ci=None,
             conversion_formula=None, from_figure=False, inferred_from_ci=False,
             direction_note="value=0 encodes a NULL: banking sleep in advance did not protect testosterone or cortisol from the subsequent deprivation. Relevant to whether weekend catch-up 'pre-pays' for a restricted week - for these hormones, it does not.",
             covariates=[], followup_years=None, cohort_family=None,
             quote="No effect of sleep extension was observed on testosterone, cortisol and catecholamines concentrations at 24 and 34 h of awakening."),
    ],
    rob={"tool": "RoB2", "judgement": "low",
         "notes": "randomised counterbalanced crossover with a proper habitual-sleep comparator; n=14; total sleep deprivation is a more extreme exposure than the subject's"},
    funding="Non-US government",
    notes="Exposure is total sleep deprivation, not chronic partial restriction, so transportability is limited. Its value is the clean recovery kinetics: one night restores baseline.",
    shard=SHARD,
))

R.append(dict(
    study_id="travison2017",
    citation="Travison TG, Vesper HW, Orwoll E, Wu F, Kaufman JM, Wang Y, Lapauw B, Fiers T, Matsumoto AM, Bhasin S. Harmonized reference ranges for circulating testosterone levels in men of four cohort studies in the United States and Europe. J Clin Endocrinol Metab. 2017;102(4):1161-1173.",
    doi="10.1210/jc.2016-2935", pmid="28324103",
    verification=v("Harmonized Reference Ranges for Circulating Testosterone Levels in Men of Four Cohort Studies in the United States and Europe"),
    access_tier="abstract_only", secondhand_via=None,
    design="normative_descriptive", tier="TX", n=9054, n_studies_pooled=4,
    population={"age_mean": None, "age_range": [19, 39], "pct_female": 0.0,
                "country": "US/EU", "adolescent_match": "good_young_adult"},
    effects=[
        dict(outcome_domain="comparator", outcome_construct="harmonized_total_testosterone_median_healthy_nonobese_men_19_39",
             exposure={"type": "descriptive", "dose_h": None, "referent_h": None, "duration_days": None,
                       "contrast_label": "CDC-calibrated harmonized reference distribution, healthy nonobese men 19-39 y"},
             scale="raw_units", unit="ng/dL total testosterone (50th percentile)", value=531.0, se=None,
             ci=[264.0, 916.0],
             conversion_formula="ci field holds the 2.5th and 97.5th percentiles of the reference distribution (264, 916 ng/dL), NOT a confidence interval on the median. 5th percentile = 303, 95th = 852.",
             from_figure=False, inferred_from_ci=False,
             direction_note=("Reference distribution, not an effect. Used to convert the Leproult 2011 testosterone deltas into "
                             "clinical units: rested 530.3 ng/dL sits at the 50th percentile, restricted 475.5 ng/dL at ~the 34th "
                             "percentile (z = -0.40) and 1.80x the 264 ng/dL lower reference limit."),
             covariates=[], followup_years=None, cohort_family="FHS_EMAS_MrOS_MSSO",
             quote="In healthy nonobese men, 19 to 39 years, harmonized 2.5th, 5th, 50th, 95th, and 97.5th percentile values were 264, 303, 531, 852, and 916 ng/dL, respectively. ... Harmonized normal range in a healthy nonobese population of European and American men, 19 to 39 years, is 264 to 916 ng/dL."),
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "low",
         "notes": "large multi-cohort sample cross-calibrated to a CDC reference method; the definitive modern reference range"},
    funding="NIH / non-US government",
    notes="Provides the denominator for the 'is a 10-15% testosterone drop clinically meaningful?' question. The implied SD of the young-male distribution is (531-303)/1.6449 = 138.6 ng/dL, so a 10.3% drop = 54.8 ng/dL = 0.40 SD.",
    shard=SHARD,
))

R.append(dict(
    study_id="hernandezperez2024",
    citation="Hernandez-Perez JG, Taha S, Torres-Sanchez LE, Villasante-Tezanos A, Milani SA, Baillargeon J, Canfield S, Lopez DS. Association of sleep duration and quality with serum testosterone concentrations among men and women: NHANES 2011-2016. Andrology. 2024;12(3):518-526.",
    doi="10.1111/andr.13496", pmid="37452666",
    verification=v("Association of sleep duration and quality with serum testosterone concentrations among men and women: NHANES 2011-2016"),
    access_tier="abstract_only", secondhand_via=None,
    design="cross_sectional", tier="TX", n=8748, n_studies_pooled=None,
    population={"age_mean": None, "age_range": [20, 40], "pct_female": None,
                "country": "US", "adolescent_match": "good_young_adult"},
    effects=[
        dict(outcome_domain="endocrine", outcome_construct="odds_of_high_total_testosterone_with_short_sleep_men_20_40",
             exposure={"type": "habitual_short_sleep", "dose_h": 6, "referent_h": 7.5, "duration_days": None,
                       "contrast_label": "self-reported sleep <=6 h vs 7-8 h, men aged 20-40 y"},
             scale="log_or", unit="log odds of being in the HIGH testosterone category", value=1.2865, se=0.49485,
             ci=[0.3148, 2.2546],
             conversion_formula="log_or = ln(3.62) = 1.2865; se = (ln(9.53) - ln(1.37))/3.92 = (2.25464 - 0.31481)/3.92 = 0.49485; ci = ln of the reported bounds [1.37, 9.53].",
             from_figure=False, inferred_from_ci=True,
             direction_note=("POSITIVE = short sleepers had HIGHER odds of high testosterone. This is the OPPOSITE direction to the "
                             "lab studies, in the age band closest to the subject. Cross-sectional and almost certainly confounded "
                             "(reverse causation: high testosterone delays bedtime), but it means the observational literature "
                             "provides no support for a clinically meaningful testosterone deficit in short-sleeping young men."),
             covariates=["age", "sex", "race/ethnicity", "BMI", "other NHANES covariates per weighted multivariable model"],
             followup_years=None, cohort_family="NHANES",
             quote="Sleep deprivation (<=6 h) was associated with high testosterone (odds ratio = 3.62; 95% confidence interval: 1.37, 9.53) among young men (20-40 years old); meanwhile, middle-aged men (41-64 years old) who reported more sleep duration had low testosterone (odds ratio = 2.03; 95% confidence interval: 1.10, 3.73)."),
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "high",
         "notes": "cross-sectional; self-reported sleep; single morning-ish testosterone draw; wide CI (1.37-9.53) implies few young short-sleeping men in the high category; multiple age x sex subgroups tested"},
    funding="Non-US government / NIH",
    notes=("SE recorded as 0.49485 in the notes-level arithmetic; the se field carries that value. Direction is a genuine "
           "contradiction of the lab literature and should widen the posterior rather than be discarded."),
    shard=SHARD,
))

R.append(dict(
    study_id="patel2019",
    citation="Patel P, Shiff B, Kohn TP, Ramasamy R. Impaired sleep is associated with low testosterone in US adult males: results from the National Health and Nutrition Examination Survey. World J Urol. 2019;37(7):1449-1453.",
    doi="10.1007/s00345-018-2485-2", pmid="30225799",
    verification=v("Impaired sleep is associated with low testosterone in US adult males: results from the National Health and Nutrition Examination Survey"),
    access_tier="abstract_only", secondhand_via=None,
    design="cross_sectional", tier="TX", n=2295, n_studies_pooled=None,
    population={"age_mean": None, "age_range": [16, 80], "pct_female": 0.0,
                "country": "US", "adolescent_match": "poor_midlife"},
    effects=[
        dict(outcome_domain="endocrine", outcome_construct="serum_total_testosterone_per_hour_less_sleep",
             exposure={"type": "per_hour_less_sleep", "dose_h": None, "referent_h": None, "duration_days": None,
                       "contrast_label": "each 1 h less self-reported habitual sleep, men aged 16-80 (median 46 y)"},
             scale="per_hour_beta", unit="ng/dL total testosterone per hour of sleep lost", value=-5.85, se=None, ci=None,
             conversion_formula="Only 'p < 0.01' is reported, an inequality, so no defensible SE can be back-calculated; se=null per instructions.",
             from_figure=False, inferred_from_ci=False,
             direction_note=("Negative = less sleep associated with lower testosterone. MAGNITUDE IS THE POINT: at the subject's "
                             "~2.5 h/night weekday deficit this predicts 2.5 x 5.85 = 14.6 ng/dL, i.e. 3.9% of the cohort median of "
                             "377 ng/dL - roughly one third of the effect attributed to a single year of normal ageing "
                             "(0.49 ng/dL/y x 30 y = 14.7 ng/dL)."),
             covariates=["age", "BMI", "comorbidities", "demographics"], followup_years=None, cohort_family="NHANES",
             quote="On multivariate linear regression, we found serum testosterone decreased by 0.49 ng/dL per year of age (p = 0.04), 5.85 ng/dL per hour loss of sleep (p < 0.01) and 6.18 ng/dL per unit of body mass index (BMI) increase (p < 0.01)."),
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "high",
         "notes": "cross-sectional, self-reported sleep, median age 46 y so poorly transportable to 18; no CI reported"},
    funding=None,
    notes=("Verbatim context: 'Median serum testosterone level was 377 ng/dL (IQR: 279-492 ng/dL). Median number of hours slept was "
           "7 h (IQR: 6-8 h).' 'On multivariate linear regression, we found serum testosterone decreased by 0.49 ng/dL per year of "
           "age (p = 0.04), 5.85 ng/dL per hour loss of sleep (p < 0.01) and 6.18 ng/dL per unit of body mass index (BMI) increase "
           "(p < 0.01).' Note the BMI coefficient exceeds the sleep coefficient: one BMI unit outweighs one hour of sleep."),
    shard=SHARD,
))

R.append(dict(
    study_id="wittert2014",
    citation="Wittert G. The relationship between sleep disorders and testosterone. Curr Opin Endocrinol Diabetes Obes. 2014;21(3):239-243.",
    doi="10.1097/MED.0000000000000069", pmid="24739309",
    verification=v("The relationship between sleep disorders and testosterone"),
    access_tier="abstract_only", secondhand_via=None,
    design="normative_descriptive", tier="TX", n=None, n_studies_pooled=None,
    population={"age_mean": None, "age_range": None, "pct_female": 0.0,
                "country": "AU", "adolescent_match": "mixed"},
    effects=[
        dict(outcome_domain="endocrine", outcome_construct="synthesis_sleep_restriction_lowers_testosterone_only_when_early_night_sleep",
             exposure={"type": "chronic_restriction", "dose_h": None, "referent_h": None, "duration_days": None,
                       "contrast_label": "narrative synthesis of experimental sleep-testosterone studies"},
             scale="pct_change", unit="qualitative conditional statement", value=0.0, se=None, ci=None,
             conversion_formula=None, from_figure=False, inferred_from_ci=False,
             direction_note=("value=0 is a placeholder for a conditional qualitative claim, not a poolable effect: total sleep "
                             "deprivation lowers testosterone, but partial restriction does so only for a specific sleep placement."),
             covariates=[], followup_years=None, cohort_family=None,
             quote="Total sleep deprivation lowers testosterone, but sleep restriction only does so if it occurs in the first half of the night. ... The diurnal variation in testosterone depends on sleep rather than circadian rhythm or season. ... In men with obstructive sleep apnoea (OSA), low testosterone is related to obesity rather than the OSA itself, and improves with weight loss but inconsistently with continuous positive airway pressure (CPAP)."),
    ],
    rob={"tool": "AMSTAR-2", "judgement": "high", "notes": "narrative 'recent findings' review; no systematic search"},
    funding="Non-US government",
    notes="Independent expert corroboration of the schmid2012 timing modifier, and a caution that in the OSA literature low testosterone tracks obesity rather than the sleep disturbance itself.",
    shard=SHARD,
))

# ------------------------------------------------------------------ CORTISOL/HPA
R.append(dict(
    study_id="spiegel1999",
    citation="Spiegel K, Leproult R, Van Cauter E. Impact of sleep debt on metabolic and endocrine function. Lancet. 1999;354(9188):1435-1439.",
    doi="10.1016/S0140-6736(99)01376-8", pmid="10543671",
    verification=v("Impact of sleep debt on metabolic and endocrine function"),
    access_tier="abstract_only", secondhand_via="balbo2010 (Int J Endocrinol 2010;2010:759234) for the cortisol magnitudes and the 8-h dose-response point",
    design="lab_restriction_within_subject", tier="T1", n=11, n_studies_pooled=None,
    population={"age_mean": None, "age_range": None, "pct_female": 0.0,
                "country": "US", "adolescent_match": "good_young_adult"},
    effects=[
        dict(outcome_domain="endocrine", outcome_construct="evening_cortisol_elevation_under_4h_tib",
             exposure={"type": "chronic_restriction", "dose_h": 4, "referent_h": 12, "duration_days": 6,
                       "contrast_label": "6 nights 4 h TIB vs 6 nights 12 h TIB (fully rested)"},
             scale="pct_change", unit="qualitative direction (elevation), p=0.0001", value=1.0, se=None, ci=None,
             conversion_formula="No magnitude in the abstract; only p=0.0001. value=1 encodes a signed but unquantified elevation.",
             from_figure=False, inferred_from_ci=False,
             direction_note="Positive = HIGHER evening cortisol under sleep debt (harm). Magnitude not extractable from the abstract.",
             covariates=[], followup_years=None, cohort_family="UChicago_VanCauter_sleepdebt",
             quote="Glucose tolerance was lower in the sleep-debt condition than in the fully rested condition (p<0.02), as were thyrotropin concentrations (p<0.01). Evening cortisol concentrations were raised (p=0.0001) and activity of the sympathetic nervous system was increased in the sleep-debt condition (p<0.02)."),
        dict(outcome_domain="endocrine", outcome_construct="rate_of_evening_free_cortisol_decline_1600_2100",
             exposure={"type": "chronic_restriction", "dose_h": 4, "referent_h": 12, "duration_days": 6,
                       "contrast_label": "6 nights 4 h TIB vs 6 nights 12 h TIB; salivary free cortisol decline 16:00-21:00"},
             scale="raw_units", unit="fold slowing of the evening free-cortisol decline", value=6.0, se=None, ci=None,
             conversion_formula="Secondhand: 'about six times slower'. No dispersion available; se=null.",
             from_figure=False, inferred_from_ci=False,
             direction_note=("Positive = the evening shutdown of cortisol is ~6x slower under sleep debt, and its onset delayed by "
                             "~1.5 h (harm: flatter diurnal slope). Read via balbo2010 because the Lancet full text was not retrieved."),
             covariates=[], followup_years=None, cohort_family="UChicago_VanCauter_sleepdebt",
             quote="[SECONDHAND, Balbo/Leproult/Van Cauter 2010, Int J Endocrinol 2010;2010:759234] The state of sleep debt, as compared to the fully rested state, was associated with elevated cortisol concentrations in the afternoon and in the early evening and with a shorter quiescent period, due to a delay in its onset by nearly 1.5 hour. In addition, the rate of decrease of free cortisol concentrations in saliva between 16.00 hours and 21.00 hours was about six times slower in the sleep-debt than in the fully rested condition."),
    ],
    rob={"tool": "RoB2", "judgement": "some_concerns",
         "notes": ("n=11; the comparator is 12 h TIB, which is not a plausible habitual sleep duration - this inflates the contrast. "
                   "Balbo 2010 reports that when 9 of these 11 men were later studied at 8 h TIB, 'cortisol evening levels observed "
                   "under 8-hour bedtime condition were intermediate between those measured under 4-hour and 12-hour bedtime "
                   "conditions', i.e. roughly half the headline effect corresponds to the 12 h arm being supranormal.")},
    funding="Non-US government / US government",
    notes="The single most-cited sleep-endocrine result. Its 4h-vs-12h design means the widely quoted magnitudes overstate the 5.5h-vs-8h contrast that applies to the subject.",
    shard=SHARD,
))

R.append(dict(
    study_id="balbo2010",
    citation="Balbo M, Leproult R, Van Cauter E. Impact of sleep and its disturbances on hypothalamo-pituitary-adrenal axis activity. Int J Endocrinol. 2010;2010:759234.",
    doi="10.1155/2010/759234", pmid="20628523",
    verification=v("Impact of Sleep and Its Disturbances on Hypothalamo-Pituitary-Adrenal Axis Activity"),
    access_tier="full_text", secondhand_via="reports the Spiegel 1999 (PMID 10543671) cortisol magnitudes and the 8-h intermediate dose-response",
    design="normative_descriptive", tier="TX", n=None, n_studies_pooled=None,
    population={"age_mean": None, "age_range": None, "pct_female": None,
                "country": "US", "adolescent_match": "mixed"},
    effects=[
        dict(outcome_domain="endocrine", outcome_construct="evening_cortisol_dose_response_4h_8h_12h",
             exposure={"type": "chronic_restriction", "dose_h": 8, "referent_h": 12, "duration_days": 6,
                       "contrast_label": "8 h TIB condition placed between the 4 h and 12 h TIB conditions in the same 9 of 11 men"},
             scale="pct_change", unit="qualitative position on a monotone dose-response", value=0.5, se=None, ci=None,
             conversion_formula="value=0.5 encodes 'intermediate between 4 h and 12 h' - i.e. roughly half of the 4h-vs-12h evening cortisol difference is attributable to the 12 h arm being supranormal rather than to the 4 h arm being pathological.",
             from_figure=True, inferred_from_ci=False,
             direction_note=("Positive = higher evening cortisol at shorter sleep. Establishes monotone dose-response AND that the "
                             "canonical 4h-vs-12h contrast roughly doubles the effect relative to an 8 h referent."),
             covariates=[], followup_years=None, cohort_family="UChicago_VanCauter_sleepdebt",
             quote="Nine of the eleven subjects of the previous study participated, one year later, in a separate protocol with 8-hour bedtime, using the same experimental procedures. Interestingly, cortisol evening levels observed under 8-hour bedtime condition were intermediate between those measured under 4-hour and 12-hour bedtime conditions [84] (Figure 5)."),
        dict(outcome_domain="endocrine", outcome_construct="secondhand_spiegel1999_cortisol_magnitudes",
             exposure={"type": "chronic_restriction", "dose_h": 4, "referent_h": 12, "duration_days": 6,
                       "contrast_label": "6 nights 4 h TIB vs fully rested (12 h TIB), n=11"},
             scale="hours", unit="hours of delay in the onset of the evening cortisol quiescent period", value=1.5, se=None, ci=None,
             conversion_formula="Reported as 'nearly 1.5 hour'. No dispersion; se=null.",
             from_figure=False, inferred_from_ci=False,
             direction_note="Positive = later shutdown of cortisol secretion (harm: extended glucocorticoid exposure).",
             covariates=[], followup_years=None, cohort_family="UChicago_VanCauter_sleepdebt",
             quote="The state of sleep debt, as compared to the fully rested state, was associated with elevated cortisol concentrations in the afternoon and in the early evening and with a shorter quiescent period, due to a delay in its onset by nearly 1.5 hour. In addition, the rate of decrease of free cortisol concentrations in saliva between 16.00 hours and 21.00 hours was about six times slower in the sleep-debt than in the fully rested condition."),
    ],
    rob={"tool": "AMSTAR-2", "judgement": "high",
         "notes": "narrative review by the authors of the primary studies it summarises; used to recover magnitudes from a paywalled primary and to establish the dose-response caveat"},
    funding=None,
    notes="Also documents a biphasic HPA response to sleep loss: HPA activation early, blunting when wakefulness is prolonged. And notes contradictory findings on whether recovery sleep normalises cortisol.",
    shard=SHARD,
))

GUYON_Q = (
    "Sleep restriction was associated with a 19% increase in overall ACTH levels (P < .03) that was correlated with the "
    "individual amount of sleep loss (rSp = 0.63, P < .02). Overall total cortisol levels were also elevated (+21%; P = .10). "
    "Pulse frequency was unchanged for both ACTH and cortisol. Morning levels of ACTH were higher after sleep restriction "
    "(P < .04) without concomitant elevation of cortisol. In contrast, evening ACTH levels were unchanged while total and free "
    "cortisol increased by, respectively, 30% (P < .03) and 200% (P < .04). Thus, the amplitude of the circadian cortisol "
    "decline was dampened by sleep restriction (-21%; P < .05)."
)

R.append(dict(
    study_id="guyon2014",
    citation="Guyon A, Balbo M, Morselli LL, Tasali E, Leproult R, L'Hermite-Baleriaux M, Van Cauter E, Spiegel K. Adverse effects of two nights of sleep restriction on the hypothalamic-pituitary-adrenal axis in healthy men. J Clin Endocrinol Metab. 2014;99(8):2861-2868.",
    doi="10.1210/jc.2013-4254", pmid="24823456",
    verification=v("Adverse Effects of Two Nights of Sleep Restriction on the Hypothalamic-Pituitary-Adrenal Axis in Healthy Men"),
    access_tier="abstract_only", secondhand_via=None,
    design="rct_crossover", tier="T1", n=13, n_studies_pooled=None,
    population={"age_mean": None, "age_range": None, "pct_female": 0.0,
                "country": "US", "adolescent_match": "good_young_adult"},
    effects=[
        dict(outcome_domain="endocrine", outcome_construct="evening_total_cortisol",
             exposure={"type": "chronic_restriction", "dose_h": 4, "referent_h": 10, "duration_days": 2,
                       "contrast_label": "2 nights 4 h TIB vs 2 nights 10 h TIB, randomised crossover; evening window"},
             scale="pct_change", unit="% change in evening total cortisol", value=30.0, se=12.19, ci=[3.4, 56.6],
             conversion_formula=("Reported as +30% with P<.03. Using the boundary p=.03 and df=12: t=2.4607, so SE <= 30/2.4607 = "
                                 "12.19 pp (a conservative upper bound on SE); ci = 30 +/- t(12,.05)=2.1788 * SE."),
             from_figure=False, inferred_from_ci=True,
             direction_note="Positive = higher evening cortisol under restriction (harm).",
             covariates=[], followup_years=None, cohort_family="UChicago_VanCauter_sleepdebt",
             quote=GUYON_Q),
        dict(outcome_domain="endocrine", outcome_construct="evening_free_salivary_cortisol",
             exposure={"type": "chronic_restriction", "dose_h": 4, "referent_h": 10, "duration_days": 2,
                       "contrast_label": "2 nights 4 h TIB vs 10 h TIB; salivary free cortisol, evening"},
             scale="pct_change", unit="% change in evening free (salivary) cortisol", value=200.0, se=86.85,
             ci=[10.8, 389.2],
             conversion_formula="Reported as +200% with P<.04. Boundary p=.04, df=12: t=2.3027, SE <= 200/2.3027 = 86.85 pp; ci = 200 +/- 2.1788*SE.",
             from_figure=False, inferred_from_ci=True,
             direction_note="Positive = higher evening free cortisol (harm). The huge percentage reflects a very low evening baseline denominator, not a large absolute excursion.",
             covariates=[], followup_years=None, cohort_family="UChicago_VanCauter_sleepdebt",
             quote=GUYON_Q),
        dict(outcome_domain="endocrine", outcome_construct="amplitude_of_circadian_cortisol_decline",
             exposure={"type": "chronic_restriction", "dose_h": 4, "referent_h": 10, "duration_days": 2,
                       "contrast_label": "2 nights 4 h TIB vs 10 h TIB; amplitude of the diurnal cortisol decline"},
             scale="pct_change", unit="% change in the amplitude of the circadian cortisol decline", value=-21.0, se=9.64,
             ci=[-42.0, 0.0],
             conversion_formula="Reported as -21% with P<.05. Boundary p=.05, df=12: t=2.1788, SE <= 21/2.1788 = 9.64 pp; ci = -21 +/- 2.1788*SE.",
             from_figure=False, inferred_from_ci=True,
             direction_note="Negative = FLATTER diurnal cortisol slope (harm). This is the most mechanistically interpretable HPA outcome: loss of rhythm amplitude, not chronic hypercortisolaemia.",
             covariates=[], followup_years=None, cohort_family="UChicago_VanCauter_sleepdebt",
             quote=GUYON_Q),
        dict(outcome_domain="endocrine", outcome_construct="overall_24h_total_cortisol",
             exposure={"type": "chronic_restriction", "dose_h": 4, "referent_h": 10, "duration_days": 2,
                       "contrast_label": "2 nights 4 h TIB vs 10 h TIB; overall total cortisol"},
             scale="pct_change", unit="% change in overall total cortisol", value=21.0, se=11.78, ci=[-4.7, 46.7],
             conversion_formula="Reported as +21% with P=.10 (non-significant). df=12: t at p=.10 = 1.7823, SE = 21/1.7823 = 11.78 pp; ci = 21 +/- 2.1788*SE, which includes zero as expected.",
             from_figure=False, inferred_from_ci=True,
             direction_note="Positive = higher overall cortisol, but NOT statistically significant. Overall daily glucocorticoid exposure is not clearly raised; the effect is confined to the evening.",
             covariates=[], followup_years=None, cohort_family="UChicago_VanCauter_sleepdebt",
             quote="Sleep restriction was associated with a 19% increase in overall ACTH levels (P < .03) that was correlated with the individual amount of sleep loss (rSp = 0.63, P < .02). Overall total cortisol levels were also elevated (+21%; P = .10). Pulse frequency was unchanged for both ACTH and cortisol. Morning levels of ACTH were higher after sleep restriction (P < .04) without concomitant elevation of cortisol. In contrast, evening ACTH levels were unchanged while total and free cortisol increased by, respectively, 30% (P < .03) and 200% (P < .04). Thus, the amplitude of the circadian cortisol decline was dampened by sleep restriction (-21%; P < .05)."),
        dict(outcome_domain="endocrine", outcome_construct="overall_acth",
             exposure={"type": "chronic_restriction", "dose_h": 4, "referent_h": 10, "duration_days": 2,
                       "contrast_label": "2 nights 4 h TIB vs 10 h TIB; overall ACTH"},
             scale="pct_change", unit="% change in overall ACTH", value=19.0, se=7.72, ci=[2.2, 35.8],
             conversion_formula="Reported as +19% with P<.03. Boundary p=.03, df=12: t=2.4607, SE <= 19/2.4607 = 7.72 pp; ci = 19 +/- 2.1788*SE.",
             from_figure=False, inferred_from_ci=True,
             direction_note="Positive = higher ACTH under restriction, dose-dependent on the individual amount of sleep lost (rSp=0.63).",
             covariates=[], followup_years=None, cohort_family="UChicago_VanCauter_sleepdebt",
             quote=GUYON_Q),
    ],
    rob={"tool": "RoB2", "judgement": "low",
         "notes": ("randomised crossover, polysomnography-verified, 20-min sampling; but only 2 nights of restriction (acute, not "
                   "chronic) and a 10 h TIB comparator. SEs are upper bounds derived from reported p-value inequalities.")},
    funding="NIH / non-US government",
    notes=("Important negative: 'Sleep restriction was not associated with higher perceived stress but resulted in an increase in "
           "appetite that was correlated with the increase in total cortisol.' The HPA change is a circadian-amplitude change, not "
           "a stress response. Also note the exposure is ACUTE (2 nights); killick2015 shows no residual morning cortisol signal in "
           "men chronically restricted for years, implying adaptation."),
    shard=SHARD,
))

R.append(dict(
    study_id="leproult1997",
    citation="Leproult R, Copinschi G, Buxton O, Van Cauter E. Sleep loss results in an elevation of cortisol levels the next evening. Sleep. 1997;20(10):865-870.",
    doi="10.1093/sleep/20.10.865", pmid="9415946",
    verification=v("Sleep Loss Results in an Elevation of Cortisol Levels the Next Evening"),
    access_tier="abstract_only", secondhand_via=None,
    design="lab_restriction_within_subject", tier="T1", n=None, n_studies_pooled=None,
    population={"age_mean": None, "age_range": None, "pct_female": 0.0,
                "country": "US/BE", "adolescent_match": "good_young_adult"},
    effects=[
        dict(outcome_domain="endocrine", outcome_construct="evening_cortisol_1800_2300_after_one_night_partial_deprivation",
             exposure={"type": "chronic_restriction", "dose_h": 4, "referent_h": 8, "duration_days": 1,
                       "contrast_label": "1 night partial sleep deprivation (04:00-08:00) vs normal schedule (23:00-07:00); 18:00-23:00 cortisol on day 2 vs day 1"},
             scale="pct_change", unit="% change in 18:00-23:00 plasma cortisol", value=37.0, se=None, ci=None,
             conversion_formula="Reported as a 37% increase with p=0.03, but n is not stated in the retrievable abstract, so no df is available and no SE can be derived. se=null.",
             from_figure=False, inferred_from_ci=False,
             direction_note=("Positive = higher evening cortisol the day AFTER one restricted night (harm). Note the comparator here "
                             "is a normal 8 h schedule, not 12 h TIB - so this 37% is a cleaner estimate of the real-world contrast "
                             "than spiegel1999's 4h-vs-12h design. But it is a single acute night."),
             covariates=[], followup_years=None, cohort_family="UChicago_VanCauter_sleepdebt",
             quote="After normal sleep, plasma cortisol levels over the 1800-2300-hour period were similar on days 1 and 2. After partial and total sleep deprivation, plasma cortisol levels over the 1800-2300-hour period were higher on day 2 than on day 1 (37 and 45% increases, p = 0.03 and 0.003, respectively), and the onset of the quiescent period of cortisol secretion was delayed by at least 1 hour."),
        dict(outcome_domain="endocrine", outcome_construct="evening_cortisol_1800_2300_after_total_sleep_deprivation",
             exposure={"type": "total_deprivation", "dose_h": 0, "referent_h": 8, "duration_days": 1,
                       "contrast_label": "1 night total sleep deprivation vs normal schedule; 18:00-23:00 cortisol day 2 vs day 1"},
             scale="pct_change", unit="% change in 18:00-23:00 plasma cortisol", value=45.0, se=None, ci=None,
             conversion_formula="Reported as a 45% increase with p=0.003; n not stated in the abstract, so se=null.",
             from_figure=False, inferred_from_ci=False,
             direction_note="Positive = higher evening cortisol (harm). Total deprivation gives 45% vs 37% for partial - a shallow dose gradient at the extreme end.",
             covariates=[], followup_years=None, cohort_family="UChicago_VanCauter_sleepdebt",
             quote="Alterations in cortisol levels could only be demonstrated in the evening following the night of sleep deprivation."),
    ],
    rob={"tool": "RoB2", "judgement": "some_concerns",
         "notes": "n not reported in the retrievable abstract and the full text was not obtained; within-subject day-2-vs-day-1 comparison"},
    funding="Non-US government / US government / US PHS",
    notes=("Important framing from the authors: 'Alterations in cortisol levels could only be demonstrated in the evening following "
           "the night of sleep deprivation.' i.e. the effect is a delayed evening shutdown, not a generalised hypercortisolaemia. "
           "n=null because it was not recoverable; downstream models should inflate uncertainty accordingly."),
    shard=SHARD,
))

R.append(dict(
    study_id="dressle2022",
    citation="Dressle RJ, Feige B, Spiegelhalder K, Schmucker C, Benz F, Mey NC, Riemann D. HPA axis activity in patients with chronic insomnia: A systematic review and meta-analysis of case-control studies. Sleep Med Rev. 2022;62:101588.",
    doi="10.1016/j.smrv.2022.101588", pmid="35091194",
    verification=v("HPA axis activity in patients with chronic insomnia: A systematic review and meta-analysis of case-control studies."),
    access_tier="abstract_only", secondhand_via=None,
    design="meta_analysis_observational", tier="TX", n=806, n_studies_pooled=20,
    population={"age_mean": None, "age_range": [18, 70], "pct_female": None,
                "country": "multiple", "adolescent_match": "fair_adult"},
    effects=[
        dict(outcome_domain="endocrine", outcome_construct="cortisol_in_chronic_insomnia_vs_good_sleepers",
             exposure={"type": "habitual_short_sleep", "dose_h": None, "referent_h": None, "duration_days": None,
                       "contrast_label": "chronic insomnia disorder (449 patients) vs good sleeper controls (357), any cortisol measure"},
             scale="smd", unit=None, value=0.50, se=0.1505, ci=[0.21, 0.80],
             conversion_formula="se = (0.80 - 0.21)/3.92 = 0.1505, from the reported 95% CI.",
             from_figure=False, inferred_from_ci=True,
             direction_note=("Positive = higher cortisol in chronic poor sleepers (harm). CEILING ESTIMATE for a chronic HPA effect: "
                             "even years of clinically diagnosed insomnia yields only SMD ~0.5. EXPOSURE MISMATCH: insomnia disorder "
                             "involves hyperarousal and distress, which behaviourally-chosen short sleep in a healthy student does "
                             "not; the association is also bidirectional."),
             covariates=[], followup_years=None, cohort_family=None,
             quote="Twenty studies (449 patients with insomnia, limited to ages 18-70 not taking any medications; 357 GSC) met the inclusion criteria. ... Results suggest that patients with insomnia show moderately increased cortisol levels (SMD = 0.50, 95% CI: [0.21-0.80]). Higher effect sizes were found by including only studies using blood samples in the analysis (SMD = 0.67, 95% CI: [0.15-1.18]). Furthermore, a positive, but insignificant association was found between the extent of objective sleep loss in insomnia patients and group differences in cortisol levels."),
    ],
    rob={"tool": "AMSTAR-2", "judgement": "moderate",
         "notes": "case-control designs only, so direction of causation unresolved; heterogeneous cortisol matrices; authors note the association with objective sleep loss was itself non-significant"},
    funding=None,
    notes=("The only quantitative meta-analysis available for chronic HPA activity and disturbed sleep. Critically, the association "
           "between the EXTENT of objective sleep loss and the cortisol difference was NOT significant, which argues that the "
           "cortisol elevation in insomnia is driven by hyperarousal rather than by short sleep duration per se."),
    shard=SHARD,
))

# --------------------------------------------------------- HEIGHT / GROWTH PLATE
WHO_Q = (
    "[VERBATIM ROWS from the downloaded WHO LMS table hfa-boys-z-who-2007-exp.xlsx; header: Month, L, M, S, StDev, SD5neg, "
    "SD4neg, SD3neg, SD2neg, SD1neg, SD0, SD1, SD2, SD3, SD4] "
    "Month 180 M=168.9580 | Month 186 M=171.1468 | Month 192 M=172.8967 | Month 198 M=174.2251 | Month 204 M=175.1609 | "
    "Month 210 M=175.7672 | Month 216 M=176.1449 | Month 222 M=176.3851 | Month 228 M=176.5432; last row = "
    "(228, L=1, M=176.5432, S=0.04134, StDev=7.2983)."
)

R.append(dict(
    study_id="who2007hfaboys",
    citation="World Health Organization. WHO Growth Reference 5-19 years: height-for-age (boys), z-scores, LMS parameter table (hfa-boys-z-who-2007-exp.xlsx). Geneva: WHO; 2007.",
    doi=None, pmid=None,
    url="https://cdn.who.int/media/docs/default-source/child-growth/growth-reference-5-19-years/height-for-age-(5-19-years)/hfa-boys-z-who-2007-exp.xlsx",
    verification={"crossref_ok": None, "pubmed_ok": None,
                  "resolved_title": "hfa-boys-z-who-2007-exp.xlsx (WHO Growth Reference 5-19 y, height-for-age boys, LMS/z-score table; 168 monthly rows, ages 61-228 months)",
                  "status": "VERIFIED"},
    access_tier="full_text", secondhand_via=None,
    design="normative_descriptive", tier="TX", n=None, n_studies_pooled=None,
    population={"age_mean": None, "age_range": [5, 19], "pct_female": 0.0,
                "country": "international", "adolescent_match": "exact_16_19"},
    effects=[
        dict(outcome_domain="anthropometric", outcome_construct="residual_median_stature_growth_age_16_0_to_19_0_boys",
             exposure={"type": "descriptive", "dose_h": None, "referent_h": None, "duration_days": None,
                       "contrast_label": "WHO median (M) stature at 228 months minus median stature at 192 months, boys"},
             scale="raw_units", unit="cm of median stature remaining between age 16.0 and 19.0 y", value=3.65, se=None,
             ci=[3.65, 3.65],
             conversion_formula=("From the LMS table rows: Month 192 M=172.8967 cm; Month 228 M=176.5432 cm. "
                                 "residual = 176.5432 - 172.8967 = 3.6465 cm. ci is degenerate because this is a fixed "
                                 "reference quantity, not a sampled estimate. As a share of adult stature: 3.6465/176.5432 = 2.07%. "
                                 "In SD units of 19-y stature (table StDev at month 228 = 7.2983 cm): 0.500 SD."),
             from_figure=False, inferred_from_ci=False,
             direction_note=("This is the ARITHMETIC CEILING on any height effect of an exposure beginning at age 16.0: only 3.65 cm "
                             "of median growth remains. Complete arrest of growth (physiologically absurd) would cost 3.65 cm; a 10% "
                             "suppression of residual velocity costs 0.36 cm; a 20% suppression costs 0.73 cm."),
             covariates=[], followup_years=3.0, cohort_family="WHO_2007_reference",
             quote=WHO_Q),
        dict(outcome_domain="anthropometric", outcome_construct="pct_of_age_19_median_stature_attained_by_age_16_0_boys",
             exposure={"type": "descriptive", "dose_h": None, "referent_h": None, "duration_days": None,
                       "contrast_label": "WHO median stature at 192 months as a percentage of median stature at 228 months"},
             scale="pct_change", unit="% of age-19 median stature already attained at age 16.0", value=97.93, se=None, ci=None,
             conversion_formula="100 * 172.8967/176.5432 = 97.93%. At 17.0 y (M=175.1609) it is 99.22%; at 18.0 y (M=176.1449) it is 99.77%.",
             from_figure=False, inferred_from_ci=False,
             direction_note="Positive = fraction of final stature already banked before the exposure began. 97.9% of adult height was already attained at exposure onset.",
             covariates=[], followup_years=None, cohort_family="WHO_2007_reference",
             quote=WHO_Q),
        dict(outcome_domain="anthropometric", outcome_construct="annual_median_height_velocity_boys_16_to_19",
             exposure={"type": "descriptive", "dose_h": None, "referent_h": None, "duration_days": None,
                       "contrast_label": "successive annual differences in WHO median stature, boys, ages 16-19 y"},
             scale="raw_units", unit="cm/y median height velocity at age 18-19 y", value=0.398, se=None, ci=None,
             conversion_formula="16->17 y: 175.1609-172.8967 = 2.264 cm/y; 17->18 y: 176.1449-175.1609 = 0.984 cm/y; 18->19 y: 176.5432-176.1449 = 0.398 cm/y. Value reported is the 18-19 y velocity.",
             from_figure=False, inferred_from_ci=False,
             direction_note=("Positive = residual growth velocity. By age 18-19 median velocity is 0.4 cm/y, i.e. below the "
                             "measurement precision of routine stadiometry. There is effectively nothing left to lose in the final "
                             "two years of the exposure window."),
             covariates=[], followup_years=None, cohort_family="WHO_2007_reference",
             quote=WHO_Q),
    ],
    rob={"tool": "none", "judgement": "na",
         "notes": "authoritative international growth reference; a reference distribution, not a study. Downloaded and parsed directly from the WHO CDN in this session."},
    funding="WHO",
    notes=("Verbatim table rows parsed from the downloaded file (columns Month, L, M, S, StDev, ...): "
           "Month 192 M=172.8967; Month 198 M=174.2251; Month 204 M=175.1609; Month 210 M=175.7672; Month 216 M=176.1449; "
           "Month 222 M=176.3851; Month 228 M=176.5432; StDev at Month 228 = 7.2983. The reference terminates at 19.0 y, so a "
           "small amount of post-19 growth is not captured - which only makes the residual-growth estimate more conservative "
           "(larger) than truth for the 16-19 window."),
    shard=SHARD,
))

R.append(dict(
    study_id="gupta2020",
    citation="Gupta N, Liu C, King E, Sylvester F, Lee D, Boyle B, Trauernicht A, Chen S, Colletti R. Continued statural growth in older adolescents and young adults with Crohn's disease and ulcerative colitis beyond the time of expected growth plate closure. Inflamm Bowel Dis. 2020;26(12):1880-1889.",
    doi="10.1093/ibd/izz334", pmid="31968095",
    verification=v("Continued Statural Growth in Older Adolescents and Young Adults With Crohn's Disease and Ulcerative Colitis Beyond the Time of Expected Growth Plate Closure"),
    access_tier="abstract_only", secondhand_via=None,
    design="prospective_cohort_objective", tier="T4", n=3007, n_studies_pooled=None,
    population={"age_mean": None, "age_range": [17, 25], "pct_female": 48.0,
                "country": "US", "adolescent_match": "exact_16_19"},
    effects=[
        dict(outcome_domain="anthropometric", outcome_construct="radiographic_age_of_growth_plate_closure_males",
             exposure={"type": "descriptive", "dose_h": None, "referent_h": None, "duration_days": None,
                       "contrast_label": "standard radiographic definition of the end of statural growth"},
             scale="years", unit="bone age (years) at radiographic growth-plate closure in males", value=17.0, se=None, ci=None,
             conversion_formula=None, from_figure=False, inferred_from_ci=False,
             direction_note=("Reference timing, not an effect. The subject was 16 at exposure onset, i.e. within ~1 year of the "
                             "conventional radiographic end of statural growth in males."),
             covariates=[], followup_years=None, cohort_family="ImproveCareNow",
             quote="Cessation of statural growth occurs with radiographic closure of the growth plates, radiographically defined as bone age (BA) 15 years in females and 17 in males."),
        dict(outcome_domain="anthropometric", outcome_construct="median_residual_height_gain_beyond_age_17_males_chronic_disease",
             exposure={"type": "descriptive", "dose_h": None, "referent_h": None, "duration_days": None,
                       "contrast_label": "males older than chronological age 17 y with Crohn's disease, height at >=3 visits >=6 months apart"},
             scale="raw_units", unit="cm of median height gained after chronological age 17 y", value=1.6, se=None, ci=None,
             conversion_formula="Median reported directly (1.6 cm in males with CD, 1.3 cm in males with UC, P=0.0004 between them). No dispersion reported; se=null.",
             from_figure=False, inferred_from_ci=False,
             direction_note=("Positive = height still gained after age 17. EMPIRICAL CEILING: even in a growth-impaired population "
                             "(chronic inflammatory bowel disease, in which delayed bone age is common and 80% still grew), the "
                             "median total residual height after age 17 was only 1.3-1.6 cm. A healthy 16-19 year old has no more "
                             "than this to lose, and probably less."),
             covariates=[], followup_years=None, cohort_family="ImproveCareNow",
             quote="Of these patients, 80% manifested continued growth, more commonly in CD (81%) than UC (75%; P = 0.0002) and in females with CD (83%) than males with CD (79%; P = 0.012). Median height gain was greater in males with CD (1.6 cm) than in males with UC (1.3 cm; P = 0.0004), and in females with CD (1.8 cm) than in females with UC (1.5 cm; P = 0.025)."),
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "moderate",
         "notes": "large registry cohort with serial measured heights (strength); population has chronic disease so it is enriched for delayed maturation, which biases residual growth UPWARD relative to healthy adolescents"},
    funding="Non-US government",
    notes=("Selected as the height ceiling because the bias runs in the conservative direction: if chronically ill adolescents with "
           "delayed bone age gain a median of only 1.3-1.6 cm after 17, a healthy well-nourished male gains no more."),
    shard=SHARD,
))

R.append(dict(
    study_id="abbassi1998",
    citation="Abbassi V. Growth and normal puberty. Pediatrics. 1998;102(2 Pt 3):507-511.",
    doi="10.1542/peds.102.S3.507", pmid="9685454",
    verification=v("Growth and Normal Puberty"),
    access_tier="abstract_only", secondhand_via=None,
    design="normative_descriptive", tier="TX", n=None, n_studies_pooled=None,
    population={"age_mean": None, "age_range": [9, 18], "pct_female": None,
                "country": "US", "adolescent_match": "mixed"},
    effects=[
        dict(outcome_domain="anthropometric", outcome_construct="age_at_peak_height_velocity_boys",
             exposure={"type": "descriptive", "dose_h": None, "referent_h": None, "duration_days": None,
                       "contrast_label": "mean age at peak height velocity in average-maturing American boys"},
             scale="years", unit="years of age at peak height velocity", value=13.5, se=None, ci=None,
             conversion_formula=None, from_figure=False, inferred_from_ci=False,
             direction_note=("Reference timing. The GH/IGF-1-driven pubertal growth spurt peaks at 13.5 y in boys - two and a half "
                             "years BEFORE the subject's exposure began. Peak whole-year velocity is 9.5 cm/y, versus 0.4-2.3 cm/y "
                             "in the exposure window."),
             covariates=[], followup_years=None, cohort_family=None,
             quote="The mean takeoff age in children growing at an average rate is approximately 11 years in boys and 9 years in girls, and peak height velocity occurs at a mean age of 13.5 years and 11.5 years, respectively, in these children. Whole-year peak height velocity is 9.5 cm/y in boys and 8.3 cm/y in girls, with slight variations in the different studies."),
        dict(outcome_domain="anthropometric", outcome_construct="pubertal_contribution_to_final_height_boys",
             exposure={"type": "descriptive", "dose_h": None, "referent_h": None, "duration_days": None,
                       "contrast_label": "total centimetres of stature contributed by puberty in boys"},
             scale="raw_units", unit="cm contributed to final height by the whole of puberty", value=30.5, se=None, ci=[30.0, 31.0],
             conversion_formula="Reported as 'approximately 30 to 31 cm'; value = midpoint 30.5; ci holds the reported range, not a confidence interval.",
             from_figure=False, inferred_from_ci=False,
             direction_note=("Denominator for the height question: the entire pubertal growth spurt contributes ~30-31 cm (17-18% of "
                             "final height), essentially all of it before age 16. The 3.65 cm remaining after 16 is ~12% of the "
                             "pubertal contribution and ~2% of final height."),
             covariates=[], followup_years=None, cohort_family=None,
             quote="The contribution of pubertal growth to final height is approximately 30 to 31 cm in boys, accounting for 17% to 18% of the final height, and 27.5 to 29 cm in girls, accounting for 17% of the final height."),
    ],
    rob={"tool": "none", "judgement": "na", "notes": "narrative review of published growth studies; descriptive norms only"},
    funding=None,
    notes="Used only to place the exposure window on the growth curve. No sleep exposure.",
    shard=SHARD,
))

R.append(dict(
    study_id="bonuck2009",
    citation="Bonuck KA, Freeman K, Henderson J. Growth and growth biomarker changes after adenotonsillectomy: systematic review and meta-analysis. Arch Dis Child. 2009;94(2):83-91.",
    doi="10.1136/adc.2008.141192", pmid="18684748",
    verification=v("Growth and growth biomarker changes after adenotonsillectomy: systematic review and meta-analysis"),
    access_tier="abstract_only", secondhand_via=None,
    design="meta_analysis_observational", tier="TX", n=363, n_studies_pooled=10,
    population={"age_mean": None, "age_range": None, "pct_female": None,
                "country": "multiple", "adolescent_match": "poor_midlife"},
    effects=[
        dict(outcome_domain="anthropometric", outcome_construct="standardised_height_change_after_adenotonsillectomy",
             exposure={"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                       "contrast_label": "pre- vs post-adenotonsillectomy standardised height (z score/centile) in children with sleep-disordered breathing"},
             scale="smd", unit=None, value=0.34, se=0.0689, ci=[0.20, 0.47],
             conversion_formula="se = (0.47 - 0.20)/3.92 = 0.0689, from the reported 95% CI. If mapped onto the SD of adult male stature (7.30 cm) this would be 2.48 cm (95% CI 1.46-3.43 cm) - see direction_note for why that mapping does not transport.",
             from_figure=False, inferred_from_ci=True,
             direction_note=("Positive = height z score IMPROVED after surgical relief of sleep-disordered breathing. This is the "
                             "strongest existing evidence that disturbed sleep can restrict growth, and it is the natural "
                             "upper-bound anchor. THREE reasons it does not transport to the subject: (1) exposure is obstructive "
                             "SDB with intermittent hypoxaemia and increased work of breathing, not voluntary curtailment of time in "
                             "bed; (2) the children were far younger and had most of their growth ahead of them, whereas the subject "
                             "had ~2% of his stature left; (3) the pooled studies are uncontrolled pre/post observational designs, "
                             "so regression to the mean and normal growth are not separated from treatment effect."),
             covariates=[], followup_years=None, cohort_family=None,
             quote="Meta-analysis findings for pre/post-surgery changes were: standardised height: 10 studies, 363 total children, pooled standardised mean differences (SMD) = 0.34 (95% CI 0.20 to 0.47); standardised weight: 11 studies, 390 total children, pooled SMD = 0.57 (95% CI 0.44 to 0.70); IGF-1: 7 studies, 177 total children, pooled SMD = 0.53 (95% CI 0.33 to 0.73); IGFBP-3: 7 studies, 177 total children, pooled SMD = 0.59 (95% CI 0.34 to 0.83)."),
        dict(outcome_domain="endocrine", outcome_construct="igf1_change_after_adenotonsillectomy",
             exposure={"type": "other", "dose_h": None, "referent_h": None, "duration_days": None,
                       "contrast_label": "pre- vs post-adenotonsillectomy serum IGF-1 in children with sleep-disordered breathing"},
             scale="smd", unit=None, value=0.53, se=0.1020, ci=[0.33, 0.73],
             conversion_formula="se = (0.73 - 0.33)/3.92 = 0.1020, from the reported 95% CI.",
             from_figure=False, inferred_from_ci=True,
             direction_note=("Positive = IGF-1 rose after surgery. The only mediator evidence linking sleep pathology to the "
                             "growth axis in humans. Note it is IGF-1 (the growth-relevant integrator), not GH pulse amplitude, "
                             "that tracks growth."),
             covariates=[], followup_years=None, cohort_family=None,
             quote="Meta-analysis findings for pre/post-surgery changes were: standardised height: 10 studies, 363 total children, pooled standardised mean differences (SMD) = 0.34 (95% CI 0.20 to 0.47); standardised weight: 11 studies, 390 total children, pooled SMD = 0.57 (95% CI 0.44 to 0.70); IGF-1: 7 studies, 177 total children, pooled SMD = 0.53 (95% CI 0.33 to 0.73); IGFBP-3: 7 studies, 177 total children, pooled SMD = 0.59 (95% CI 0.34 to 0.83)."),
    ],
    rob={"tool": "AMSTAR-2", "judgement": "high",
         "notes": "pooled uncontrolled pre/post observational studies; 'Setting: Observational studies'; publication bias likely; no randomised comparator"},
    funding=None,
    notes=("The exposure that produces measurable growth effects in humans is sleep-disordered BREATHING in prepubertal children, "
           "not short sleep duration in a 16-19 year old. The randomised test of the same intervention (katz2014) found the effect "
           "on weight/adiposity, not stature."),
    shard=SHARD,
))

R.append(dict(
    study_id="katz2014",
    citation="Katz ES, Moore RH, Rosen CL, Mitchell RB, Amin R, Arens R, Muzumdar H, Chervin RD, Marcus CL, Paruthi S, Willging P, Redline S. Growth after adenotonsillectomy for obstructive sleep apnea: an RCT. Pediatrics. 2014;134(2):282-289.",
    doi="10.1542/peds.2014-0591", pmid="25070302",
    verification=v("Growth After Adenotonsillectomy for Obstructive Sleep Apnea: An RCT"),
    access_tier="abstract_only", secondhand_via=None,
    design="rct_parallel", tier="T1", n=464, n_studies_pooled=None,
    population={"age_mean": None, "age_range": [5, 9.9], "pct_female": None,
                "country": "US", "adolescent_match": "poor_midlife"},
    effects=[
        dict(outcome_domain="anthropometric", outcome_construct="bmi_z_score_change_over_7_months_early_adenotonsillectomy_vs_watchful_waiting",
             exposure={"type": "other", "dose_h": None, "referent_h": None, "duration_days": 210,
                       "contrast_label": "early adenotonsillectomy vs watchful waiting with supportive care, 7-month interval, children with OSAS (mean AHI 5.1/h)"},
             scale="raw_units", unit="BMI z-score units", value=0.18, se=0.0463, ci=[0.089, 0.271],
             conversion_formula=("value = 0.31 (eAT) - 0.13 (WWSC) = 0.18 BMI z units. Only 'P < .0001' is reported; using the "
                                 "boundary p=.0001 with large df, z=3.891, giving SE <= 0.18/3.891 = 0.0463 (an upper bound); "
                                 "ci = 0.18 +/- 1.96*SE."),
             from_figure=False, inferred_from_ci=True,
             direction_note=("Positive = MORE weight gain in the treated arm. Note the direction: relieving the sleep disorder "
                             "increased adiposity, and 52% vs 21% of overweight children became obese. The randomised evidence for "
                             "'fixing sleep improves growth' delivers fat mass, not stature."),
             covariates=["baseline weight", "AHI", "race", "gender", "follow-up AHI"],
             followup_years=0.58, cohort_family="CHAT",
             quote="Interval increases in the BMI z score (0.13 vs. 0.31) was observed in both the WWSC and eAT intervention arms, respectively, but were greater with eAT (P < .0001). ... A greater proportion of overweight children randomized to eAT compared with WWSC developed obesity over the 7-month interval (52% vs. 21%; P < .05). ... eAT for OSAS in children results in clinically significant greater than expected weight gain, even in children overweight at baseline."),
    ],
    rob={"tool": "RoB2", "judgement": "low",
         "notes": "properly randomised multicentre trial with objective polysomnography; the abstract reports BMI z score and does not report a separate stature z-score contrast, so a height effect cannot be extracted"},
    funding="NIH",
    notes=("The only RCT of a sleep intervention with anthropometric outcomes. It reports BMI z score, not stature; a randomised "
           "estimate of a height effect is therefore unavailable even in the paediatric SDB literature where the observational "
           "signal is strongest."),
    shard=SHARD,
))

# ------------------------------------------------------------ PUBERTY / BONE
R.append(dict(
    study_id="gunawan2024",
    citation="Gunawan SP, Huang SY, Wang CC, Huynh LBP, Nguyen NN, Hsu SY, Chen YC. Sleep deprivation alters pubertal timing in humans and rats: the role of the gut microbiome. Sleep. 2024;47(2):zsad308.",
    doi="10.1093/sleep/zsad308", pmid="38065690",
    verification=v("Sleep deprivation alters pubertal timing in humans and rats: the role of the gut microbiome"),
    access_tier="abstract_only", secondhand_via=None,
    design="prospective_cohort_selfreport", tier="T5", n=1418, n_studies_pooled=None,
    population={"age_mean": None, "age_range": None, "pct_female": 67.6,
                "country": "TW", "adolescent_match": "mixed"},
    effects=[
        dict(outcome_domain="endocrine", outcome_construct="odds_of_early_sexual_maturation_with_insufficient_sleep_girls",
             exposure={"type": "habitual_short_sleep", "dose_h": None, "referent_h": None, "duration_days": None,
                       "contrast_label": "self-reported insufficient sleep (PSQI) vs sufficient, girls, Taiwan Pubertal Longitudinal Study"},
             scale="log_or", unit="log odds of early sexual maturation", value=0.3646, se=0.1404, ci=[0.0862, 0.6366],
             conversion_formula="log_or = ln(1.44) = 0.3646; se = (ln(1.89) - ln(1.09))/3.92 = (0.6366 - 0.0862)/3.92 = 0.1404; ci = ln of the reported bounds [1.09, 1.89].",
             from_figure=False, inferred_from_ci=True,
             direction_note=("Positive = EARLIER puberty with insufficient sleep, mediated by obesity, and significant in GIRLS ONLY "
                             "(no significant boy estimate was reported despite 459 boys in the cohort). The paired rat experiment "
                             "found the OPPOSITE direction - delayed vaginal opening and preputial separation - so the literature "
                             "does not even agree on sign. Irrelevant to the subject in any case: he was 16 and post-pubertal at "
                             "exposure onset."),
             covariates=["obesity (tested as mediator)"], followup_years=None, cohort_family="Taiwan_Pubertal_Longitudinal_Study",
             quote="In the human cohort, insufficient sleep increased the risk of early sexual maturation, particularly in girls (OR, 1.44; 95% CI: 1.09 to 1.89; p-value < 0.01). Insufficient sleep also indirectly affected early sexual maturation in girls, with obesity serving as the mediator. ... The sleep-deprived juvenile rats in the sleep-deprived-female (SDF) and sleep-deprived-male (SDM) groups experienced delayed VO (mean VO days: 33 days in control; 35 days in SDF; p-value < 0.05) and PS (mean PS days: 42 days in control; 45 days in SDM; p-value < 0.05), respectively."),
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "high",
         "notes": "self-reported sleep by PSQI; effect significant in girls only; human and animal arms give opposite directions; pubertal onset is not an outcome that can be affected by an exposure beginning at age 16"},
    funding=None,
    notes=("The best available human evidence on sleep and pubertal timing. It concerns pubertal ONSET in pre-pubertal children and "
           "is mediated by adiposity. For a 16-year-old male who has already passed peak height velocity by ~2.5 years, pubertal "
           "timing is not a live outcome."),
    shard=SHARD,
))

R.append(dict(
    study_id="swanson2017",
    citation="Swanson CM, Shea SA, Wolfe P, Cain SW, Munch M, Vujovic N, Czeisler CA, Buxton OM, Orwoll ES. Bone turnover markers after sleep restriction and circadian disruption: a mechanism for sleep-related bone loss in humans. J Clin Endocrinol Metab. 2017;102(10):3722-3730.",
    doi="10.1210/jc.2017-01147", pmid="28973223",
    verification=v("Bone Turnover Markers After Sleep Restriction and Circadian Disruption: A Mechanism for Sleep-Related Bone Loss in Humans"),
    access_tier="abstract_only", secondhand_via=None,
    design="lab_restriction_within_subject", tier="T1", n=10, n_studies_pooled=None,
    population={"age_mean": None, "age_range": [20, 65], "pct_female": 0.0,
                "country": "US", "adolescent_match": "good_young_adult"},
    effects=[
        dict(outcome_domain="endocrine", outcome_construct="p1np_bone_formation_marker_younger_men_20_27",
             exposure={"type": "chronic_restriction", "dose_h": 5.6, "referent_h": 8, "duration_days": 21,
                       "contrast_label": "~3 weeks of 5.6 h sleep/24 h WITH concurrent forced desynchrony (recurring 28-h day, dim light) vs baseline; men aged 20-27 y (n=6)"},
             scale="pct_change", unit="% change in serum P1NP", value=-28.0, se=None, ci=None,
             conversion_formula="Reported as a 28.0% decrease in younger men vs 18.2% in older men, P<0.001 for the age difference. No dispersion for the younger-men percentage; se=null.",
             from_figure=False, inferred_from_ci=False,
             direction_note=("Negative = LESS bone formation (harm), and worse in the young. But the exposure is sleep restriction "
                             "PLUS severe circadian disruption; swanson2022 and depner2021 show that sleep restriction ALONE "
                             "produces no bone-turnover change, so the circadian component appears to be doing the work."),
             covariates=["age"], followup_years=None, cohort_family="Harvard_forced_desynchrony",
             quote="P1NP levels were lower after intervention compared with baseline (P < 0.001); the decrease in P1NP was greater for younger compared with older men (28.0% vs 18.2%, P < 0.001). There was no change in CTX (delta = 0.03 +/- 0.02 ng/mL, P = 0.10). Sclerostin levels were higher postintervention in the younger men only (delta = 22.9% or 5.64 +/- 1.10 pmol/L, P < 0.001)."),
        dict(outcome_domain="endocrine", outcome_construct="ctx_bone_resorption_marker",
             exposure={"type": "chronic_restriction", "dose_h": 5.6, "referent_h": 8, "duration_days": 21,
                       "contrast_label": "~3 weeks of 5.6 h sleep/24 h with forced desynchrony vs baseline, all 10 men"},
             scale="raw_units", unit="ng/mL change in serum CTX", value=0.03, se=0.02, ci=[-0.009, 0.069],
             conversion_formula="Reported directly as delta = 0.03 +/- 0.02 ng/mL, P = 0.10; se = reported 0.02; ci = 0.03 +/- 1.96*0.02.",
             from_figure=False, inferred_from_ci=False,
             direction_note="Positive would mean more resorption, but the interval crosses zero (P=0.10). Bone resorption was unchanged; the effect was confined to formation - an uncoupling, not accelerated loss.",
             covariates=[], followup_years=None, cohort_family="Harvard_forced_desynchrony",
             quote="There was no change in CTX (delta = 0.03 +/- 0.02 ng/mL, P = 0.10). Sclerostin levels were higher postintervention in the younger men only (delta = 22.9% or 5.64 +/- 1.10 pmol/L, P < 0.001)."),
    ],
    rob={"tool": "RoB2", "judgement": "high",
         "notes": "n=10 total (only 6 in the young stratum); the intervention deliberately CONFOUNDS sleep restriction with 28-h forced desynchrony, so the sleep-restriction contribution is not identifiable; no recovery arm"},
    funding="NIH / non-US government",
    notes="Authors' own conclusion names both components: 'Circadian disruption and sleep restriction may be most detrimental to bone in early adulthood.' The isolating experiments (swanson2022, depner2021) found nothing.",
    shard=SHARD,
))

R.append(dict(
    study_id="swanson2022",
    citation="Swanson CM, Shanbhag P, Tussey EJ, Rynders CA, Wright KP, Kohrt WM. Bone turnover markers after six nights of insufficient sleep and subsequent recovery sleep in healthy men. Calcif Tissue Int. 2022;110(6):712-722.",
    doi="10.1007/s00223-022-00950-8", pmid="35133471",
    verification=v("Bone Turnover Markers After Six Nights of Insufficient Sleep and Subsequent Recovery Sleep in Healthy Men"),
    access_tier="abstract_only", secondhand_via=None,
    design="lab_restriction_within_subject", tier="T1", n=12, n_studies_pooled=None,
    population={"age_mean": None, "age_range": None, "pct_female": 0.0,
                "country": "US", "adolescent_match": "good_young_adult"},
    effects=[
        dict(outcome_domain="endocrine", outcome_construct="bone_turnover_markers_after_isolated_sleep_restriction",
             exposure={"type": "chronic_restriction", "dose_h": 5, "referent_h": 8, "duration_days": 6,
                       "contrast_label": "6 nights of 5 h/night vs baseline 8 h/night, WITHOUT circadian disruption; diet, activity and posture controlled"},
             scale="pct_change", unit="% change in PINP/osteocalcin/beta-CTX (null)", value=0.0, se=None, ci=None,
             conversion_formula="Authors report no statistically or clinically significant change (PINP p=0.53, osteocalcin p=0.66, beta-CTX p=0.10). value=0 encodes the null; no point estimates given.",
             from_figure=False, inferred_from_ci=False,
             direction_note=("value=0 encodes a NULL. Isolating sleep restriction from circadian disruption abolishes the "
                             "swanson2017 bone signal. Direct evidence that 5 h/night for a week does not perturb bone metabolism "
                             "in young men."),
             covariates=[], followup_years=None, cohort_family="Colorado_sleep_bone",
             quote="There was no statistically or clinically significant change in PINP (p = 0.53), osteocalcin (p = 0.66), or beta-CTX (p = 0.10) in response to six nights of insufficient sleep."),
        dict(outcome_domain="recovery", outcome_construct="bone_turnover_markers_through_3_weeks_of_recovery",
             exposure={"type": "recovery_sleep", "dose_h": None, "referent_h": 8, "duration_days": 21,
                       "contrast_label": "fasted samples daily inpatient plus 5 times over 3 weeks after discharge"},
             scale="pct_change", unit="% change in bone turnover markers during recovery (null)", value=0.0, se=None, ci=None,
             conversion_formula="All p >= 0.63. value=0 encodes the null.",
             from_figure=False, inferred_from_ci=False,
             direction_note="value=0 = no residual bone-turnover abnormality at up to 3 weeks after the restriction ended. Nothing to recover from.",
             covariates=[], followup_years=0.058, cohort_family="Colorado_sleep_bone",
             quote="There were no significant changes in BTMs from the inpatient stay through 3 weeks of recovery sleep (all p [Formula: see text] 0.63). On average, body weight was stable during the inpatient stay (delta weight = - 0.55 +/- 0.91 kg, p = 0.06)."),
    ],
    rob={"tool": "RoB2", "judgement": "some_concerns",
         "notes": "n=12, single-arm before/after with no concurrent control; strength is tight control of diet, activity, posture and weight, which isolates the sleep exposure; registered NCT03733483"},
    funding="NIH",
    notes="The cleanest available test of the subject's actual exposure (5 h/night) on bone. Result: nothing, and nothing lingering at 3 weeks.",
    shard=SHARD,
))

R.append(dict(
    study_id="depner2021",
    citation="Depner CM, Rice JD, Tussey EJ, Eckel RH, Bergman BC, Higgins JA, Melanson EL, Kohrt WM, Wright KP, Swanson CM. Bone turnover marker responses to sleep restriction and weekend recovery sleep. Bone. 2021;152:116096.",
    doi="10.1016/j.bone.2021.116096", pmid="34216838",
    verification=v("Bone turnover marker responses to sleep restriction and weekend recovery sleep"),
    access_tier="abstract_only", secondhand_via=None,
    design="rct_parallel", tier="T1", n=20, n_studies_pooled=None,
    population={"age_mean": None, "age_range": None, "pct_female": 40.0,
                "country": "US", "adolescent_match": "good_young_adult"},
    effects=[
        dict(outcome_domain="recovery", outcome_construct="bone_turnover_markers_sleep_restriction_with_or_without_weekend_recovery",
             exposure={"type": "weekend_catchup", "dose_h": 5, "referent_h": 9, "duration_days": 9,
                       "contrast_label": "9 nights 5 h/night, vs 4 nights 5 h + ad libitum weekend recovery, vs 9 h/night control; randomised"},
             scale="pct_change", unit="% change in P1NP/osteocalcin/CTX (null)", value=0.0, se=None, ci=None,
             conversion_formula="No significant change baseline to day 11 (all p >= 0.3) and no group x time interaction (p >= 0.4). value=0 encodes the null.",
             from_figure=False, inferred_from_ci=False,
             direction_note=("value=0 encodes a NULL for BOTH the sustained-restriction and the weekend-recovery patterns. The "
                             "weekend-catch-up arm is the closest laboratory analogue of the subject's weekday-restriction/"
                             "weekend-recovery schedule, and it produced no bone-turnover change either."),
             covariates=["age", "sex"], followup_years=None, cohort_family="Colorado_sleep_bone",
             quote="There was no significant difference between the three study groups in change over time (p >= 0.4 for interaction between assigned group and time for all BTMs), adjusted for age and sex. There was no significant change in N-terminal propeptide of procollagen type I (P1NP), osteocalcin, or C-telopeptide of type I collagen (CTX) from baseline to day 11 (all p >= 0.3)."),
    ],
    rob={"tool": "RoB2", "judgement": "some_concerns",
         "notes": "small secondary analysis of stored serum (control arm n=3); mixed sex; ad libitum food intake after baseline; underpowered for small effects, so this is a weak null rather than strong evidence of no effect"},
    funding="NIH / non-US government",
    notes=("Authors are explicit that this is 'a small secondary analysis' and hypothesise that 'age, sex, weight change and morning "
           "circadian misalignment modify the effects of sleep restriction on bone metabolism' - i.e. the circadian and weight "
           "components, not sleep duration, carry the signal."),
    shard=SHARD,
))


R.append(dict(
    study_id="chen2025beijing",
    citation="Chen Y, Wu L, Liao Z, Huang Y, Liu Q, Li S, Liu J, Zong X, Tai J, Chen F. Status of sleeping habits and its influence on growth and metabolism of children in Beijing: a population-based cross-sectional study. BMC Public Health. 2025;25(1):474.",
    doi="10.1186/s12889-025-21637-3", pmid="39910513",
    verification=v("Status of sleeping habits and its influence on growth and metabolism of children in Beijing: a population-based cross-sectional study"),
    access_tier="abstract_only", secondhand_via=None,
    design="cross_sectional", tier="TX", n=5832, n_studies_pooled=None,
    population={"age_mean": None, "age_range": [6, 18], "pct_female": None,
                "country": "CN", "adolescent_match": "mixed"},
    effects=[
        dict(outcome_domain="anthropometric", outcome_construct="height_for_age_z_score_and_poor_sleep_habits",
             exposure={"type": "habitual_short_sleep", "dose_h": None, "referent_h": None, "duration_days": None,
                       "contrast_label": "poor sleep habits by Children's Sleep Habits Questionnaire (CSHQ) vs not, children and adolescents 6-18 y"},
             scale="raw_units", unit="height-for-age z score (HAZ) units", value=-0.111, se=None, ci=None,
             conversion_formula=("Reported as beta = -0.111 with p < 0.05; no SE or CI given, so se=null. If interpreted as the "
                                 "contrast for the 'poor sleep habits' indicator, -0.111 HAZ maps to 0.111 * 7.30 cm = 0.81 cm of "
                                 "adult stature using the WHO 19-y stature SD of 7.2983 cm."),
             from_figure=False, inferred_from_ci=False,
             direction_note=("Negative = shorter for age with poor sleep habits (harm). THE ONLY sleep-to-stature association found "
                             "in a sample spanning adolescence. Magnitude bound: even taken at face value it is ~0.8 cm. Internally "
                             "inconsistent, though: sleep-disordered breathing was POSITIVELY associated with HAZ in the 6-11 y "
                             "group (beta = +0.240, p < 0.05), the opposite sign to the adenotonsillectomy literature, which is a "
                             "strong hint of residual confounding."),
             covariates=["age", "sex (analysed by age group)"], followup_years=None, cohort_family="Beijing_schools_2022_2023",
             quote="Linear regression analysis showed that poor sleep habits were negatively correlated with height for age (HAZ) and systolic blood pressure (SBP) (beta = -0.111 and - 0.459, respectively; p < 0.05). ... while SDB was positively correlated with HAZ only in children aged 6-11 years (beta = 0.240, p < 0.05)."),
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "high",
         "notes": ("cross-sectional; exposure is a composite sleep-habits questionnaire score rather than measured sleep duration; "
                   "the scaling of beta (per CSHQ unit vs binary indicator) is not resolvable from the abstract; attained height is "
                   "not final adult height; opposite-signed SDB association in the same paper suggests confounding")},
    funding=None,
    notes=("Included because sleep-duration-to-stature evidence is nearly absent and this is the closest available. It measures "
           "ATTAINED height in a 6-18 y cross-section, which cannot identify an effect of exposure at 16-19 on FINAL height."),
    shard=SHARD,
))

R.append(dict(
    study_id="li2025shortstature",
    citation="Explainable predictive models of short stature and exploration of related environmental growth factors: a case-control study. BMC Endocr Disord. 2025;25(1):125.",
    doi="10.1186/s12902-025-01936-x", pmid="40355909",
    verification=v("Explainable predictive models of short stature and exploration of related environmental growth factors: a case-control study"),
    access_tier="abstract_only", secondhand_via=None,
    design="cross_sectional", tier="TX", n=300, n_studies_pooled=None,
    population={"age_mean": None, "age_range": None, "pct_female": None,
                "country": "CN", "adolescent_match": "poor_midlife"},
    effects=[
        dict(outcome_domain="anthropometric", outcome_construct="odds_of_normal_variant_short_stature_with_sufficient_night_sleep",
             exposure={"type": "habitual_short_sleep", "dose_h": None, "referent_h": None, "duration_days": None,
                       "contrast_label": "sufficient nighttime sleep duration (parent-reported) vs not; 100 clinic cases of normal-variant short stature vs 200 age-matched controls"},
             scale="log_or", unit="log odds of normal-variant short stature", value=-0.7340, se=0.31391,
             ci=[-1.3471, -0.1165],
             conversion_formula="log_or = ln(0.48) = -0.7340; se = (ln(0.89) - ln(0.26))/3.92 = (-0.11653 - (-1.34707))/3.92 = 0.31391; ci = ln of the reported bounds [0.26, 0.89].",
             from_figure=False, inferred_from_ci=True,
             direction_note=("Negative = sufficient sleep is PROTECTIVE against being in the short-stature category (i.e. short "
                             "sleep is associated with short stature; harm). BUT: paediatric endocrine clinic cases, parental "
                             "recall of sleep, 33 candidate variables screened, and parental height dominated the model "
                             "(maternal OR 0.79 and paternal OR 0.83 per cm). Children in the active growing phase, not 16-19 y."),
             covariates=["child weight", "maternal height", "paternal height", "outdoor activity time", "caregiver education"],
             followup_years=None, cohort_family="Nanjing_Childrens_Hospital",
             quote="In the multivariate logistic regression analysis, children's weight (OR = 0.92, 95% CI: 0.86, 0.99), maternal height (OR = 0.79, 95% CI: 0.72, 0.87), paternal height (OR = 0.83, 95% CI: 0.75, 0.91), sufficient nighttime sleep duration (OR = 0.48, 95% CI: 0.26, 0.89), and outdoor activity time exceeding three hours (OR = 0.02, 95% CI: 0.00, 0.66) were identified as protective factors for normal-variant short stature."),
    ],
    rob={"tool": "Newcastle-Ottawa", "judgement": "critical",
         "notes": ("clinic-based case-control with parent-reported exposure collected AFTER the outcome was known (recall bias runs "
                   "directly toward this finding); 33 variables screened with 100 cases; the outdoor-activity OR of 0.02 is not "
                   "credible and signals severe model instability")},
    funding=None,
    notes=("Author list not recoverable from the PubMed record retrieved in this session, so the citation is title-first; DOI and "
           "PMID both verified. This is the only study found that links sleep DURATION specifically to a stature outcome, and its "
           "risk of bias is critical. It concerns children still growing, not 16-19 year olds."),
    shard=SHARD,
))


# --------------------------------------------------------------------- emit
def main():
    schema = json.load(open(SCHEMA))
    try:
        import jsonschema
    except ImportError:
        print("jsonschema not installed; writing without validation", file=sys.stderr)
        jsonschema = None

    ids = [r["study_id"] for r in R]
    assert len(ids) == len(set(ids)), "duplicate study_id"
    errs = 0
    for rec in R:
        if jsonschema:
            try:
                jsonschema.validate(rec, schema)
            except jsonschema.ValidationError as e:
                errs += 1
                print(f"SCHEMA FAIL {rec['study_id']}: {e.message} @ {list(e.absolute_path)}", file=sys.stderr)
        path = os.path.join(OUT, rec["study_id"] + ".yaml")
        with open(path, "w") as fh:
            yaml.safe_dump(rec, fh, sort_keys=False, allow_unicode=True, width=118, default_flow_style=False)
    n_eff = sum(len(r["effects"]) for r in R)
    print(f"wrote {len(R)} records, {n_eff} effects, {errs} schema errors")


if __name__ == "__main__":
    main()
