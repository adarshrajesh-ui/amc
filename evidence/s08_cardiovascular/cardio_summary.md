# Cardiovascular summary — shard `s08_cardiovascular`

Subject: male, 18 turning 19, entering second year of college. Weekday sleep ~5-6 h since age 16;
weekend/holiday 7-8 h; occasional 3-4 h pre-exam nights; occasional 10-11 h weekend nights.

18 records, 71 effect estimates, all identifiers verified against both Crossref and PubMed.

---

## 1. Bottom line first

At the subject's actual exposure the cardiovascular signal is **small, endpoint-specific, and
substantially confounded**. Three findings dominate:

1. **The dose-response curve is nearly flat between 6 h and 7 h.** In the best-tabulated
   dose-response meta-analysis (Yin 2017, 3.58 M participants), 6 h vs 7 h gives total-CVD
   RR **1.02** (1.00-1.03) and stroke RR **0.99** (0.96-1.03). Only coronary heart disease shows a
   non-trivial gradient (5 h: RR 1.11).
2. **Roughly one-third of the crude association survives full covariate adjustment.** In UK Biobank,
   the 6 h vs 7-8 h myocardial-infarction hazard ratio falls from **1.16 → 1.05** (CI 0.98-1.13, i.e.
   null) on adjustment — **67% of the crude log-HR is attenuated away**.
3. **Mendelian randomization nonetheless supports causality for coronary disease, and not for
   stroke.** Two independent MR studies give OR **1.12-1.25 per hour of sleep lost** for MI; two
   independent MR studies find **no** causal effect of sleep *duration* on stroke, while both confirm
   one for *insomnia*.

For blood pressure specifically — the outcome most often invoked — the evidence in **young males** is
close to null. A meta-analysis of randomised sleep-restriction trials finds no effect on SBP, DBP or
heart rate; the one well-instrumented crossover trial in young adults found its entire blood-pressure
signal came from women, with **no 24-h BP effect in men at all**.

---

## 2. The dose-response curve

### 2.1 Primary curve (Yin 2017, restricted cubic spline, 4 knots, referent 7 h)

RR (95% CI) by nightly sleep duration. Bold marks the subject's weekday range.

| Sleep | All-cause mortality | Total CVD | CHD | Stroke |
|---|---|---|---|---|
| 3 h | 1.12 (1.10-1.14) | 1.14 (1.09-1.19) | — | — |
| 4 h | 1.08 (1.06-1.09) | 1.09 (1.06-1.13) | 1.16 (1.09-1.23) | 1.05 (0.96-1.15) |
| **5 h** | **1.04 (1.03-1.05)** | **1.05 (1.03-1.08)** | **1.11 (1.06-1.16)** | **1.02 (0.96-1.08)** |
| **6 h** | **1.01 (1.00-1.01)** | **1.02 (1.00-1.03)** | **1.05 (1.03-1.08)** | **0.99 (0.96-1.03)** |
| 7 h | 1.00 (ref) | 1.00 (ref) | 1.00 (ref) | 1.00 (ref) |
| 8 h | 1.04 (1.04-1.05) | 1.03 (1.02-1.05) | 1.01 (0.99-1.03) | 1.08 (1.06-1.11) |
| 9 h | 1.15 (1.14-1.16) | 1.16 (1.13-1.19) | 1.14 (1.08-1.20) | 1.30 (1.24-1.37) |
| 10 h | 1.32 (1.29-1.35) | 1.37 (1.29-1.45) | 1.34 (1.20-1.50) | 1.64 (1.47-1.82) |
| 11 h | 1.53 (1.47-1.59) | — | — | — |

Number of contributing risk estimates: 40 / 26 / 20 / 17 respectively.

**Per-hour slopes below the 7 h inflection** (Yin 2017): total CVD **1.06** (1.03-1.08),
CHD **1.07** (1.03-1.12), stroke **1.05** (1.01-1.09), all-cause mortality **1.06** (1.04-1.07).

### 2.2 Three features of this curve that matter more than its height

**(a) It is markedly asymmetric, and the long arm is steeper.** At 10 h, total CVD is 1.37 and stroke
1.64; at 4 h they are 1.09 and 1.05. A short-sleep toxicity mechanism does not predict this. Reverse
causation — where illness shortens life expectancy and lengthens sleep — does. Every synthesis in
this shard reproduces the asymmetry, and two state it as their conclusion: Kwok 2018 ("Longer
duration of sleep may be more associated with adverse outcomes compared with shorter sleep
durations") and Wang 2022 ("Extended sleep duration was more associated with adverse outcomes
compared with short sleep duration").

**(b) Independent syntheses disagree about whether the short arm exists at all.** Same literature,
overlapping cohorts, four different answers for the region below 7 h:

| Source | n | Verdict below 7 h |
|---|---|---|
| Yin 2017 (JAHA) | 3.58 M | CVD 1.02 at 6 h, 1.05 at 5 h |
| Huang 2022 (Front Cardiovasc Med) | 3.8 M, 71 cohorts | **Risk not elevated anywhere in 4.3-10.3 h** |
| Kwok 2018 (JAHA) | 3.34 M, 74 studies | **"No significant difference ... for periods of self-reported sleep <7 hours"** |
| Itani 2017 (Sleep Med) | 5.17 M, 153 studies | CVD 1.16 / CHD 1.26 for an *undefined* short-sleep dichotomy, **but its own meta-regression found "no dose-response ... in the other outcomes"** |

Two of the four largest analyses in the field place the subject's exposure inside the
non-elevated-risk band. Any pooled estimate must carry heterogeneity wide enough to contain both
"1.02" and "nothing".

**(c) Stroke is the least stable endpoint in the shard.** Cappuccio 2011 RR 1.15 (1.00-1.31,
p=0.047); Yin 2017 spline 1.02 at 5 h and 0.99 at 6 h; Wang 2022 RR 1.33 (1.19-1.49); and **two MR
studies find nothing**. The stroke estimate should be treated as the shard's weakest.

### 2.3 Where the subject sits

Weekday 5-6 h with weekend 7-8 h gives a weekly mean near 6-6.5 h. Reading the CVD column at
6-6.5 h yields **RR ≈ 1.01-1.03**; the CHD column yields **≈ 1.03-1.05**. His occasional 10-11 h
weekend nights fall on the steep long-sleep limb, but that limb is populated by *habitual* long
sleepers — a group enriched for undiagnosed illness — and is not transportable to recovery sleep in a
healthy 19-year-old.

---

## 3. Observational versus Mendelian randomization

### 3.1 Side by side, myocardial infarction / coronary disease

| Design | Estimate | Source |
|---|---|---|
| Observational, **crude**, 6 h vs 7-8 h | HR 1.16 (1.08-1.24) | Daghlas 2019, UK Biobank |
| Observational, **fully adjusted**, 6 h vs 7-8 h | HR **1.05 (0.98-1.13)** — null | Daghlas 2019 |
| Observational, **fully adjusted**, <6 h vs 6-9 h | HR 1.20 (1.07-1.33) | Daghlas 2019 |
| Observational meta-analytic, CHD at 5 h | RR 1.11 (1.06-1.16) | Yin 2017 |
| **MR**, 2-sample, per hour lost, MI | OR **1.25 (1.05-1.49)** | Daghlas 2019 (CARDIoGRAMplusC4D) |
| **MR**, 1-sample, per hour lost, MI | OR 1.16 (0.94-1.43) — **ns, p=0.17** | Daghlas 2019 (UK Biobank) |
| **MR**, per hour lost, MI | OR **1.12 (1.01-1.25)** | Zhao 2025, independent |
| **MR**, 2-sample, per hour lost, CAD | OR 1.27 (1.09-1.47) | Daghlas 2019 |
| **MR**, short-sleep instrument, MI | OR 1.19 (1.09-1.29); UKB replication 1.21 (1.08-1.37) | Daghlas 2019 |
| **MR**, short-sleep instrument, CAD | OR 1.55 (1.17-2.06) | Zhao 2025 |

### 3.2 Does the MR support causality? Yes for coronary disease — with three caveats

**It does.** The point estimates are consistent across two independent research groups and two
outcome consortia, the direction is stable, MR-Egger intercept tests were non-significant for
pleiotropy in both papers (p=0.22-0.23 in Daghlas), leave-one-out revealed no driving variant, and
Daghlas's estimate survived instruments rebuilt from GWAS that excluded shift workers and people with
prevalent disease. This is the strongest causal evidence in the shard.

**Caveat 1 — the famous concordance is partly a scale coincidence.** Daghlas's much-quoted agreement
between observational HR 1.20 and MR OR 1.19 compares two different exposures. The paper is explicit:
"Short sleep duration associations reflect the increase in MI risk concomitant with a **doubling in
the odds** of short sleep duration." That is not the <6 h vs 6-9 h contrast. The genuinely comparable
quantity is the continuous per-hour estimate.

**Caveat 2 — the continuous instrument failed to replicate in-sample.** Daghlas's one-sample UK
Biobank MR gave OR 0.86 per additional hour (0.70-1.06, **p=0.17**). The authors attribute this to
power. Zhao 2025's independent per-hour estimate is real but roughly **half the magnitude** on the
log scale (ln 1.12 = 0.117 vs ln 1.25 = 0.223).

**Caveat 3 — MR cannot see a U-shape.** Guo 2024 states the problem plainly: "if the relationships
are U-shaped ... these may not be detected by MR." A linear instrument applied to a U-shaped exposure
mixes the short and long arms. Since the long arm is *steeper* in every observational analysis here,
a linear MR may be partly reading long-sleep harm and attributing it to the short direction.

### 3.3 The uncomfortable comparison nobody usually makes

Converting Daghlas's UK Biobank hazard ratios to a per-hour scale (referent midpoint 7.5 h):

| | per hour of sleep lost |
|---|---|
| Observational, **crude** | 1.10 (at 6 h) to 1.21 (at 4 h) |
| Observational, **fully adjusted** | **1.03 (at 6 h) to 1.09 (at 4 h)** |
| **MR** | **1.12 to 1.25** |

**The MR estimate is larger than the fully adjusted observational estimate and sits close to the
crude one.** Two readings are possible and the shard cannot decide between them:

- *Over-adjustment.* Daghlas's Model 3 adjusts for BMI, waist-hip ratio, hypertension, type 2
  diabetes, high cholesterol and three drug classes. These are plausible **mediators** of a
  sleep→MI effect, not confounders — Gangwisch 2006 treats obesity and diabetes explicitly as
  "partial mediators". Conditioning on mediators biases the *total* causal effect toward null. On
  this reading the adjusted 1.05 at 6 h *understates* the true total effect, and MR (which captures
  the total effect) is right.
- *Inflated MR.* Sleep-duration instruments are weak and the sleep GWAS is itself self-reported;
  Daghlas concedes the instrument is associated with BMI, "consistent with either a confounding or
  mediating role", and one variant had to be pruned before weighted-median and MR-Egger estimates
  behaved. On this reading MR is upward-biased and the adjusted observational estimate is right.

### 3.4 Stroke: MR does not support causality

| Study | Sleep **duration** → stroke | Insomnia → stroke |
|---|---|---|
| Guo 2024, Neurology (UKB + GIGASTROKE) | **no causal effect detected** | OR 1.27 (1.10-1.47) |
| Zhao 2025, Open Heart | **not among significant or suggestive pairs** | OR 1.26 (1.03-1.54) |

Both MR studies detect a sleep-stroke causal pathway; in both it runs through **insomnia**, not
duration. Guo 2024's observational arm points the same way — after adjustment for cardiovascular risk
factors only insomnia (HR 1.05), napping (1.09) and dozing (1.19) survived for stroke; sleep duration
did not. The subject's exposure is volitional restriction, not insomnia, so the insomnia estimates
are **diagnostic, not applicable** to him.

---

## 4. How much of the association plausibly survives confounding adjustment

**Required explicit statement.** The only record in this shard reporting a full staged adjustment
sequence against a hard endpoint is Daghlas 2019 (UK Biobank, 461,347 participants, 5,218 incident
MIs, median follow-up 7.04 y). Decomposing its log-hazard ratios:

| Sleep | Crude | + age, sex | + BMI, WHR | Fully adjusted | **Fraction of crude log-HR surviving** |
|---|---|---|---|---|---|
| 4 h | 1.96 | 2.12 | 1.93 | 1.34 (1.07-1.68) | **43.5%** |
| 5 h | 1.52 | 1.58 | 1.48 | 1.19 (1.06-1.35) | **41.5%** |
| **6 h** | **1.16** | **1.18** | **1.14** | **1.05 (0.98-1.13)** | **32.9%** |

Step-by-step contribution, as a percentage of the crude log-HR at 6 h:

- age + sex: **+11.5%** (adjustment *increases* the association)
- BMI + waist-hip ratio: **−23.2%**
- everything else — smoking, alcohol, education, income, Townsend deprivation, employment, marital
  status, physical activity (MET-h/week), television watching, grip strength, mental-health contact,
  snoring, sleep medication, sleep apnoea, insomnia, diabetes, hypertension, cholesterol, medications,
  aspirin: **−55.4%**

### The explicit answer

**About one-third (33%) of the crude 6 h association, and about 40% of the 5 h association, survives
full adjustment — and at 6 h what survives is no longer statistically distinguishable from zero
(HR 1.05, CI 0.98-1.13).** On the log scale, **67% of the crude association at the subject's median
weekday exposure is attributable to measured confounders.**

Decomposing *which* confounders, from the same table:

- **BMI/adiposity: ~23%** of the crude association at 6 h.
- **Socioeconomic position, health behaviours, mental health and comorbidity together: ~55%.** The
  single largest bloc, and the one that cannot be cleanly split with published data — Daghlas reports
  these covariates only as a single "Model 3". Notably, participants sleeping 7-8 h "were more likely
  to be employed and report excellent self-reported health, and were less likely to report a history
  of smoking, depression, high cholesterol, or hypertension", so the confounding structure is dense
  and all in the same direction.
- **Depression specifically: ~9-13%** *of even the causal effect.* Zhao 2025's MR mediation analysis
  puts the MDD-mediated fraction at 8.92% (0.87-16.97) for CAD, **11.43% (0.28-22.57) for MI**, and
  12.65% (1.35-23.96) for HF. Genetic liability to short sleep raises depression odds by OR 1.83
  (1.44-2.33). For a student whose short sleep is volitional and academic rather than a depressive
  symptom, this fraction arguably should be **subtracted entirely** from his expected effect.
- **Physical activity and socioeconomic status** are inside the −55.4% bloc and cannot be isolated;
  Daghlas adjusts for MET-h/week, television watching, grip strength, education, income, employment
  and Townsend deprivation index simultaneously.

### But the honest qualification

**The 67% figure is an upper bound on confounding, because Model 3 also adjusts for mediators.**
BMI, hypertension, type 2 diabetes and hypercholesterolaemia are all plausibly *downstream* of
chronic short sleep; conditioning on them removes real causal signal along with confounding. This is
why the MR estimate (1.12-1.25 per hour) exceeds the fully adjusted observational estimate (1.03-1.09
per hour) rather than falling below it.

**Synthesis.** Combining the attenuation evidence with the MR evidence, the defensible range is:

> **For coronary/MI endpoints, somewhere between about one-third and all of the crude association is
> plausibly causal — best point estimate around one-half — with the balance attributable to
> socioeconomic position, health behaviours, adiposity and depression. For stroke, the causal fraction
> is plausibly zero, since two MR studies and one large adjusted cohort analysis all fail to find any
> duration effect. For blood pressure in young males, the randomised evidence is null.**

Corroborating attenuation evidence from a second cohort, Guo 2024: "we found multiple observational
associations, but many of these were no longer significant after controlling for cardiovascular risk
factors", and the sleep traits that *did* survive adjustment for stroke retained hazard ratios of
only 1.05-1.19.

---

## 5. Blood pressure, heart rate and sympathetic activity under experimental restriction

The experimental tier is where the subject's age is best matched — and where the blood-pressure story
weakens sharply once sex is taken into account.

| Outcome | Effect | Source | Tier |
|---|---|---|---|
| 24-h mean arterial pressure, whole sample | **+2.1 mmHg** (0.6, 3.6) | Covassin 2021, 9 nights at 4 h, age 23.4 | T1 |
| 24-h systolic BP, whole sample | **+3.1 mmHg** (0.9, 5.3) | Covassin 2021 | T1 |
| 24-h diastolic BP, whole sample | **+2.2 mmHg** (0.7, 3.7) | Covassin 2021 | T1 |
| 24-h heart rate | **no change** | Covassin 2021 | T1 |
| **24-h BP in MEN** | **no effect on any 24-h outcome**; daytime MAP **−3.8 mmHg** (−6.4, −1.2) | Covassin 2021 | T1 |
| 24-h systolic BP in women | **+8.0 mmHg** (5.1, 10.8); sleep-time SBP +11.3 (5.9, 16.7) | Covassin 2021 | T1 |
| Plasma norepinephrine | **+55.5 pg/mL** (20.0, 91.0) at day 7 | Covassin 2021 | T1 |
| Flow-mediated dilation | **−2.2%** (−3.8, −0.6) | Covassin 2021 | T1 |
| Resting heart rate, young **men** | 60 → 63 bpm after 5 nights at 4 h | van Leeuwen 2018 | T1 |
| HRV LF/HF ratio, young **men** | 4.6 → 6.0 (+30%) | van Leeuwen 2018 | T1 |
| **Pooled across RCTs — systolic BP** | **+1.0 mmHg (−2.3, 4.2), p=0.57** | Hu 2020, 6 RCTs | T1 |
| **Pooled across RCTs — diastolic BP** | **−0.4 mmHg (−3.2, 2.4), p=0.80** | Hu 2020 | T1 |
| **Pooled across RCTs — heart rate** | **+2.0 bpm (−2.2, 6.2), p=0.34** | Hu 2020 | T1 |
| Adolescent 24-h ambulatory SBP, actigraphy | **−0.57 mmHg per hour** more sleep, ages 11-16 | Meininger 2014 | TX |

**What replicates and what does not.** Sympathetic activation replicates across both good crossover
studies — norepinephrine up in Covassin, LF/HF up 30% in van Leeuwen — and endothelial function is
impaired (FMD −2.2%). **Blood pressure does not replicate in males.** Covassin's headline +2.1 mmHg
was generated entirely by 9 women; in the 11 men there was no 24-h effect and daytime pressures went
*down*. The pooled RCT evidence, drawn from a literature Covassin notes "included only men", is null
on all three of SBP, DBP and HR.

**Convergence for a 19-year-old male.** Three independent designs — pooled RCTs (+1.0 mmHg, CI
−2.3 to 4.2), Covassin's male stratum (null), and age-matched adolescent actigraphy
(0.57 mmHg/h → ~0.9-1.1 mmHg at his deficit) — all put his expected systolic change at
**approximately 0 to +3 mmHg**, with confidence intervals comfortably including zero. That is within
the measurement noise of a single clinic reading.

**Reversal is partial.** Covassin: 24-h BP returned to baseline within 3 recovery nights, but
**sleep-time SBP remained +3.3 mmHg** (0.3, 6.3) and **FMD remained −1.8%** (−3.5, −0.1). van
Leeuwen: heart rate did **not** recover — it rose *further*, 63 → 65 bpm, after three 8 h nights
(n=15, so possibly noise, but it is the reported direction). Relevant to the subject's weekend
catch-up pattern, Covassin's authors write: "short periods of extended sleep opportunity may be
insufficient to mitigate the negative effects caused by short sleep during weekdays."

---

## 6. Absolute risk — and why the ratios above are nearly meaningless at 19

Only one record supplies stratum-specific absolute rates. Daghlas 2019, UK Biobank, **ages 40-69**:

| Sleep | Cases / person-years | Incidence per 1000 PY | Excess vs 7-8 h |
|---|---|---|---|
| 4 h | 82 / 28,496 | 2.88 | +1.41 → 1 extra MI per 709 PY |
| 5 h | 310 / 138,902 | 2.23 | +0.76 → 1 extra MI per 1,316 PY |
| **6 h** | **1,058 / 621,416** | **1.70** | **+0.23 → 1 extra MI per 4,348 PY** |
| 7-8 h | 3,248 / 2,205,231 | 1.47 | referent |

These are **crude** rates; two-thirds of the 6 h excess disappears on adjustment.

Other absolute anchors retrieved (all in older cohorts, all whole-sample):

| Source | Cohort age | Absolute |
|---|---|---|
| Cappuccio 2011 | midlife/older | CHD 4,169/474,684 = **0.88%**; stroke 3,478/474,684 = **0.73%** over ~12 y |
| Yin 2017 | midlife/older | total CVD 58,919/3,582,016 = **1.6%**; CHD **0.63%**; stroke **0.43%** |
| Guo 2024 | mean **56.5** y | stroke 10,334/502,383 = **2.06%** |
| Gangwisch 2006 | **32-59** y | incident hypertension 647/4,810 = **13.5%** over 8-10 y |

**The transportability problem, stated plainly.** Every ratio in this shard is measured in cohorts
whose median age is 50-70. UK Biobank's referent MI rate of 1.47 per 1000 person-years applies at
median age ~56. Male MI incidence at age 19 is lower by roughly two orders of magnitude, so applying
the adjusted 6 h hazard ratio of 1.05 to his current baseline yields an absolute excess on the order
of **one event per several hundred thousand person-years** over the next few years. A hazard ratio of
1.2 in a 60-year-old cohort genuinely does imply almost nothing in absolute terms for a 19-year-old
*in the near term*.

**What this shard cannot do.** I did not retrieve an age-specific baseline MI, stroke or hypertension
incidence for 19-year-old males, and I have not invented one. Converting these ratios into absolute
risk for the subject **requires the baseline-risk / life-table shard to supply age-specific incidence
rates**, and requires an explicit assumption about whether a hazard ratio measured at age 56 applies
at age 19 or only after decades of accumulated exposure. The honest framing is that short sleep at 19
is a *risk-factor-trajectory* exposure, not a near-term event risk: the relevant question is whether
3 years of restriction shifts the lifetime curve, and no study in this domain follows adolescents to
cardiovascular events.

---

## 7. Age transportability — and the age interaction, honestly

The task asked whether the hypertension association is stronger in younger people. **It is reported
to be, but not in anyone near 19.**

| Source | Claimed age interaction | What "younger" actually means |
|---|---|---|
| Wang 2012 | Incident hypertension RR **1.33** (1.11-1.61) in subjects **< 65 y** | Everyone under 65. Dominated by midlife adults. No interaction p-value reported |
| Gangwisch 2006 | HR **2.10** (1.58-2.79) at <= 5 h, ages **32-59** | Midlife. The stratum is the headline, which invites selective-reporting bias |

Neither contains a single 19-year-old. And for **hard** cardiovascular endpoints the reported age
interaction runs the *opposite* way — Yin 2017: "several studies found a stronger U-shaped association
between sleep duration and CVDs in older adults compared with younger adults (cutoff at age 65
years)." Daghlas found **no** effect modification at all in UK Biobank.

So the age-interaction literature does **not** license inflating the subject's risk. It supports only
the weaker claim that these associations are detectable in working-age adults and fade in the
elderly — itself the pattern expected if competing risks and reverse causation dominate at older ages.

**Age-match ledger for this shard:**

| Match | Records |
|---|---|
| `exact_16_19` | 1 — Meininger 2014 (ages 11-16), cross-sectional, surrogate outcome, tier TX |
| `good_young_adult` | 2 — Covassin 2021 (23.4 y), van Leeuwen 2018 (young men) |
| `fair_adult` | 1 — Hu 2020 |
| `mixed` | 1 — Guo 2013 (studies spanning 18-106 y) |
| `poor_midlife` | 13 |

**Note a common miscitation I corrected:** Sands 2012 is routinely presented as young-adult evidence
because CARDIA means "Coronary Artery Risk Development in **Young Adults**". That refers to enrolment
in 1985-86. At the time of the actigraphy and carotid ultrasound the participants were **37-52 years
old**. It is a midlife study.

---

## 8. Early vascular markers in the young — thin, as anticipated

| Finding | Number | Design |
|---|---|---|
| cIMT per hour more sleep, **men** | **−0.026 mm** (−0.047, −0.005) | Sands 2012, actigraphy, cross-sectional, ages 37-52 |
| cIMT per hour more sleep, women | −0.001 mm (−0.020, 0.022), p=0.91 | same |
| 24-h ambulatory SBP per hour, ages 11-16 | −0.57 mmHg, P<0.0001 | Meininger 2014, actigraphy, cross-sectional |

Sands' effect scales to ~0.04-0.05 mm of extra cIMT at the subject's deficit — about 4-5 years of
typical vascular ageing *if* it were causal, transportable from midlife men, and prognostically
meaningful. All three conditionals are unverified, the effect was absent in women, and the authors
note it was driven by a single carotid segment (the bulb), which is more consistent with measurement
noise than diffuse atherosclerosis.

**A sex-consistency problem worth flagging.** The two best sex-stratified records in this shard
disagree about which sex is vulnerable: Covassin's blood-pressure effect appeared **only in women**;
Sands' cIMT effect appeared **only in men**. Both cannot be describing the same biology. At least one
is noise, which should temper any use of sex-specific estimates.

I searched specifically for arterial stiffness and pulse-wave velocity in adolescents and young
adults and found only scattered small cross-sectional reports (logged in `screening_log.md`), none
prospective, none in 16-19 year olds.

---

## 9. What this shard does *not* support

Stated explicitly so downstream stations do not over-read the records:

1. **No measurable near-term cardiovascular event risk at age 19.** No study follows adolescents or
   young adults from short sleep to incident cardiovascular events. Every event-based estimate is
   extrapolated across 30-50 years of age.
2. **No causal effect on stroke.** Two MR studies and one large adjusted cohort analysis all fail to
   find one for sleep *duration*.
3. **No sustained blood-pressure elevation in young males.** The pooled randomised evidence is null;
   the best single trial's male stratum is null.
4. **No natural-experiment evidence whatsoever.** Tier T2 is empty — the school-start-time literature
   has never measured cardiovascular outcomes (query returned zero records).
5. **No objective-exposure prospective cohort isolating sleep duration.** The one actigraphy/PSG
   cohort with incident CVD (MESA) uses a composite 8-metric score in a cohort of mean age 69, so the
   duration effect cannot be separated. **Tier T4 is effectively empty for this domain.**

## 10. Confidence grades (per `spec/gates.md`)

| Headline number | Quantity | Quality | Transportability | Model dependence |
|---|---|---|---|---|
| Total CVD RR 1.02 at 6 h | A | C | C | **C** (0.99-1.16 across syntheses) |
| CHD RR 1.05-1.11 at 6-5 h | A | C | C | B |
| Stroke at 5-6 h | A | C | C | **D** — sign flips (0.99 to 1.33) |
| MI per hour lost, MR | C | B | C | B |
| Systolic BP change, young male | B | **A** | B | B |
| Fraction surviving adjustment (~1/3) | D | B | C | **C** |

Two numbers grade **D** and must be labelled GUESS in the report body: the stroke estimate
(model dependence) and the confounding-survival fraction (quantity — it rests on one cohort's table).
