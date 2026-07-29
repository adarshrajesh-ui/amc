# Screening priors, likelihood ratios and posteriors — sleep disorders in an 18-19 year old male

Shard `s19_sleep_disorders`. Subject: male, 18-19, entering second year of college. Reports weekday
sleep ~5-6 h from age 16 to 19, weekend/holiday sleep ~7-8 h with occasional 10-11 h nights, occasional
3-4 h nights before exams. Attributes the pattern to workload.

Every number below is traceable to a YAML record in this directory. Numbers I computed myself are marked
**[derived]**; numbers resting on an assumption not present in any source are marked **[judgement]**.

---

## 0. Headline answer

The task asks for the posterior probability that the subject has an undiagnosed, treatable *intrinsic*
sleep disorder rather than purely behaviourally-imposed sleep restriction. That posterior is **almost
entirely determined by one question that has not yet been asked**: how long does he take to fall asleep
once he is in bed and trying?

| Information state | DSWPD | Insomnia disorder | OSA | **P(any intrinsic treatable disorder)** |
|---|---|---|---|---|
| **S0** Pattern only — no discriminating question asked (current state) | 1.9% | 18.4% | 0.8% | **21%** (interval 12-32%) |
| **S1** Falls asleep ≤20 min on weekday *and* free nights; no irrepressible sleepiness; function preserved | 0.1% | 1.6% | 1.0% | **3%** (interval 1-7%) |
| **S2** Takes >60 min to fall asleep *every* night including free nights; oversleeps most days | 35.6% | 47.4% | 0.3% | **83%** (interval 70-92%) |
| **S3** Takes >60 min on weekday nights but sleeps normally at his late free-day time; oversleeps most days | 44.9% | 15.5% | 0.6% | **61%** (interval 45-75%) |

**Recommended single posterior to carry into the report: 21%, interval 12-32%** (state S0, which is the
honest description of what we currently know). This is *not* a small number and it does justify the
measurement protocol in `instruments.md`. But note carefully where it comes from: most of that 21% is
**insomnia disorder (18%), not DSWPD (2%)**, because the adolescent insomnia prior is roughly five times
the DSWPD prior. The task brief's hypothesis — that this is DSWPD — is a real possibility but is *not*
the leading intrinsic candidate on the evidence available, and the pattern he describes barely moves it.

**The most probable single explanation of his reported pattern remains behaviourally imposed sleep
restriction** (BIISS 29% + behavioural restriction not meeting BIISS criteria 50% ≈ 79% in state S0).

---

## 1. Prior prevalence for each candidate disorder

### 1.1 Delayed sleep-wake phase disorder (DSWPD)

| Estimate | Population | Criteria | Source |
|---|---|---|---|
| **4.7%** (95% CI 3.7-5.7% [derived]) | male university students, Norway | self-reported ICSD-3 | `sivertsen2021.yaml` |
| 2.7% (95% CI 2.2-3.2% [derived]) | boys 16-19, Norway, n≈9,338 | ICSD-R | `sivertsen2013.yaml` |
| 4.0% | ages 16-26, Sweden | DSM-5 | `danielsson2016.yaml` |
| 5.7% (delayed sleep phase **with impairment**) | high-school students 16-19, Norway | delayed phase + impairment | `saxvig2012.yaml` |
| 8.4% (delayed sleep phase **trait**, no impairment requirement) | high-school students 16-19, Norway | phase only | `saxvig2012.yaml` |

**Prior adopted: 4.0%, range 2.7-5.7%.** I take the male-specific ICSD-3 figure (4.7%) and the
male-specific ICSD-R figure (2.7%) as the bracketing pair and sit near their midpoint, because the
higher figures (5.7%, 8.4%) come from operationalisations that relax the disorder threshold.

Two caveats the report must state. First, every one of these is **self-report questionnaire-based**;
none used actigraphy plus DLMO, so all are likely to over-call. Second, three of the five are
Norwegian, so they share a cohort family and must not be treated as independent replications.

**Why age matters more than anything else here.** The most recent systematic review of DSWPD in young
people states the contrast directly (`dama2025.yaml`): "survey data suggests that DSWPD may affect 3.3 to
17.9% of young individuals, which is far greater than the prevalence rate of **0.13 to 0.17%** seen in the
general population." That is a 20-100× age gradient, and it is the reason an adult or all-age base rate
must not be used for this subject. I did **not** adopt the 3.3-17.9% range as my prior: it is an
introductory narrative range across four surveys, the review did not meta-analyse prevalence at all, and
its upper bound comes from the loosest self-report operationalisations. My 4.0% remains anchored on the
strict-criteria primaries. The review's reference list contains Sivertsen 2013, Danielsson 2016 and
Sivertsen 2021 — all of which I extracted directly — which is a useful confirmation that my search found
the right primaries rather than new evidence.

### 1.1b Natural history: a delayed phase at this age mostly does *not* resolve on its own

Every other prevalence source in this shard is cross-sectional and therefore silent on whether a delayed
pattern in a 16-19 year old goes away. One prospective study answers it (`jaakallio2026.yaml`, n=1,374
Finnish adolescents, mean age 16.8 y, followed 19 months with 8 nights of actigraphy and 3 nights of
skin-temperature recording at each follow-up): **"The stability of DSP was 70%."**

This matters for the recommendation, not the diagnosis. "He will grow out of it" is not a safe default —
if the subject genuinely is phase-delayed, it is more likely than not that he stays delayed through the
college years, which is exactly the window where the academic cost lands. Three qualifications: the
follow-up sample was deliberately DSP-enriched so 70% is not a population transition probability; the
abstract gives two candidate denominators and no CI, so I did not manufacture one; and the cohort was 66%
girls whereas our subject is male.

**The same study cuts against the circadian framing, and that belongs on the record.** The authors found
that behavioural factors (poor self-control, ADHD symptoms, alcohol use) explained DSP trajectories while
the physiological measures they took — circadian thermoregulation, physical-activity volume and intensity
— **did not associate with DSP continuity at all**. Their conclusion: "The outcomes emphasize behavioral
over the potential physiological components of DSP measured in this study." This is evidence *against* a
purely physiological-circadian reading of adolescent delayed sleep and partially supports the behavioural
explanation the subject himself offers, so it should temper rather than inflate the DSWPD posterior. Two
things stop it from settling the question: the behavioural block explained only 18% of continuity (82%
unexplained), and skin temperature is a noisy surrogate for melatonin phase, so a null result on it is
weak evidence about the underlying pacemaker.

### 1.2 Delayed chronotype as distinct from the disorder

This is where the discrimination problem lives, and it is the single most important finding in my shard.

- **Peak circadian lateness in males occurs at age 19.2 y**, with weekend mid-sleep (MSFWe) of 04:40 on
  the smoothed curve and 05:02 as the raw age-19 mean, SD **2.60 h**, n=229 (`fischer2017.yaml`).
- Population norms for US males: age 16 → 04:20 (SD 1.79); 17 → 04:35 (SD 2.23); 18 → 04:37 (SD 2.14);
  19 → **05:02 (SD 2.60)** (`fischer2017.yaml`, Table 1).
- Chronotype **variance also peaks** in this age band and is higher in males (SD 2.65 h at 20-24 y).
- A 2+ hour weekend bedtime delay with more weekend sleep is the **worldwide adolescent norm** across
  41 surveys, and the meta-analysts state the normative pattern is "consistent with symptoms of Delayed
  Sleep Phase Disorder" (`gradisar2011meta.yaml`).

So the subject sits at the exact age of maximum population-level circadian delay, drawn from the
widest-variance distribution in the human lifespan. **Delayed chronotype at 19 is normal; DSWPD requires
inability to sleep at the desired time plus impairment.**

### 1.3 Insomnia disorder

| Estimate | Population | Criteria | Source |
|---|---|---|---|
| **22.2%** | male university students, Norway | DSM-5 | `sivertsen2019.yaml` |
| 18.5% | adolescents 16-19, Norway | DSM-5 | `hysing2013.yaml` |
| 22.1% | US college students | screen-based | `williams2020.yaml` |
| 10.7% (lifetime) | US adolescents 13-16 | DSM-IV, **diagnostic interview** | `johnson2006.yaml` |

**Prior adopted: 18%, range 10.7-22.2%.** The interview-based figure (10.7%) is the methodologically
strongest and the lowest, which is the usual pattern; the questionnaire figures cluster near 20%.
`ohayon2002.yaml` documents why the spread is so wide — prevalence falls by roughly a factor of three as
one moves up the definitional ladder from "insomnia symptoms" to "diagnosis".

**The 2025 meta-analysis now quantifies the correction, and it suggests my 18% is too high.** From
`vanstraten2025.yaml` (47 studies, PROSPERO CRD42023402745, restricted to true random general-population
samples with DSM-anchored ascertainment):

| Ascertainment | Pooled prevalence | 95% CI |
|---|---|---|
| DSM **diagnostic interview** | **12.4%** | 9.0-16.8% |
| DSM **self-report** questions | 16.3% | 11.3-23.0% |
| High-quality studies | 10.7% | — |
| Lower-quality studies | 17.1% | — (P = 0.02 for the difference) |

So expect questionnaire-based prevalence to run about **1.3×** interview-based prevalence. Every adolescent
figure in my table above except Johnson 2006 is questionnaire-based, which means **18% is more likely too
high than too low**; a value nearer 13-15% would be defensible. I have kept 18% for the computations below
so that the posteriors are conservative in the direction of *over*-calling intrinsic disorder, and §3.2
shows the conclusions do not turn on it.

**Do not substitute 12.4% as the prior, and do not read this meta-analysis's null age moderator as
permitting it.** The contributing studies have mean ages of **37.0 to 84.3 years** — the adolescent and
young-adult band is entirely absent. The finding that mean age was unassociated with prevalence (P = 0.98)
is a statement about the 37-84 y range only, and 21 of 47 studies never reported a mean age at all.
Age-matched primaries remain the right source for this subject.

### 1.4 Behaviourally induced insufficient sleep syndrome (BIISS)

| Estimate | Population | Source |
|---|---|---|
| **10.4%** | high-school students 16-19, Norway | `pallesen2011.yaml` |
| 9.9% | US college students | `williams2020.yaml` |

**Prior adopted: 10%, range 9.9-10.4%.** Two independent populations agree closely, which is unusual and
reassuring. Note this is the prevalence of the *full syndrome* including the irrepressible-sleepiness
criterion; short habitual sleep without that criterion is far more common and is not BIISS.

### 1.5 Obstructive sleep apnoea

**No study I retrieved reports symptomatic OSA prevalence in lean males aged 18-25.** The closest data:

| Estimate | Population | Threshold | Source |
|---|---|---|---|
| 7.0% | **lean** men 30-49 | AHI ≥5 | `peppard2013.yaml` |
| 0.93% | lean men 30-49 | AHI ≥15 | `peppard2013.yaml` |
| **2.7%** | lean men 30-49 | AHI ≥5 **plus ESS >10** (nearest to "symptomatic OSA") | `peppard2013.yaml` |
| 10.6% (8-y incidence) | representative adolescents, mean age 16.5, lab PSG | paediatric AHI ≥5 | `bixler2016.yaml` |
| 22% | cohort followed from childhood to mean age 20.2, enriched for childhood SDB | OAHI ≥5 | `chan2019.yaml` |
| — | **restricted to ages 30-69, supplies nothing for this age band** | — | `benjafield2019.yaml` |

**Prior adopted for a clinically significant, treatable OSA syndrome in a lean 19-year-old male: 1%,
range 0.5-3% [judgement].** Reasoning, laid out so it can be audited: start from Peppard's 2.7% for
symptomatic OSA in *lean* men aged 30-49; OSA prevalence rises steeply across midlife so 19 must sit
below the 30-49 figure; but adolescent males are not at zero risk (Bixler shows AHI ≥5 is not rare on
PSG). I therefore take roughly a third to a half of the lean 30-49 symptomatic figure. **This is an
extrapolation, not an extracted literature value, and must be presented as such.** Bixler's 10.6% is a
*polysomnographic finding*, not a disorder — an unselected adolescent crossing AHI 5 on one lab night is
usually asymptomatic — and it is scored by paediatric conventions that are not interchangeable with the
adult thresholds. The report should also note (`bixler2016.yaml`) that childhood OSA remitted in **100%**
of cases by adolescence and that mild SDB/snoring does not predict progression, so a childhood history is
uninformative either way.

---

## 2. Likelihood ratios for the features of this subject's presentation

### 2.1 The disease-present distributions I built these from

Diagnosed adolescent DSPD, sleep-diary values, pooled across both randomised arms pre-treatment
(`gradisar2011rct.yaml`, n=40, ICSD-2 diagnosis by clinician consensus + 7-day diary) **[derived pooling]**:

| Parameter | Diagnosed DSPD | Comparator | Source of comparator |
|---|---|---|---|
| School-night sleep onset latency | **78.4 min** (SD 37.2) | 44.4 min (SD 37.4) | `sivertsen2013.yaml` difference + `hysing2013.yaml` base rate |
| Free-night sleep onset latency | **66.0 min** (SD 40.2) | ~44 min | as above |
| School-night total sleep time | **7.02 h** (SD 1.34) | 6.42 h | `hysing2013.yaml` |
| Weekend total sleep time | **8.34 h** (SD 1.54) | 7.42 h | `sivertsen2019.yaml` |
| Weekend − weekday sleep gap | **1.33 h** | 1.02 h | `sivertsen2019.yaml` |
| Weekend mid-sleep | **05:12** | 05:02 (age-19 male norm) | `fischer2017.yaml` |

**Internal consistency check that gives me confidence in the comparator distribution:** the non-DSPD
sleep-onset-latency distribution is over-determined. Sivertsen 2013 reports that DSPS adolescents' latency
exceeds non-DSPS by 34 min, which puts the non-DSPD mean at 78.4 − 34 = 44.4 min. Independently, Hysing
2013 reports that 65% of adolescents have latency >30 min, which given a mean of 44.4 min implies an SD of
37.4 min. That derived SD (37.4) is almost identical to the *observed* SD in the DSPD cohort (37.2) from a
different country, decade and study design. Two unrelated papers therefore pin down the same distribution.

### 2.2 The four features the task asked about

#### (a) "Large weekday-weekend sleep discrepancy" — LR ≈ **1.1-1.4**, essentially uninformative

| Observed gap | LR for DSWPD |
|---|---|
| 2.0 h (his usual: 5.5 → 7.5 h) | **1.13** (cross-check with Sivertsen 2013 means: 1.22) |
| 2.5 h | 1.22 (cross-check 1.41) |
| 5.0 h (his occasional 10-11 h weekend) | 1.76 (cross-check 2.87) |
| 1.0 h (a normative gap) | 0.97 |

**[derived]** Normal-approximation likelihood ratio, disease-present mean 1.33 h (Gradisar) vs
disease-absent mean 1.02 h (Sivertsen 2019), common SD 1.45 h obtained from the two arms' TST SDs assuming
a within-person school/weekend correlation of r=0.5. Sensitivity: r=0.3 → SD 1.71; r=0.7 → SD 1.13; the LR
stays in the 1.05-1.25 band for a 2-hour gap across that whole range.

**Why this feature is nearly worthless, stated plainly for the report.** Three independent lines converge:

1. Adolescents with **clinically diagnosed** DSPD had a weekend-minus-weekday gap of only **1.33 h**. The
   subject's ~2 h gap is *larger than the diagnosed cases'*. A feature that is more extreme in the
   subject than in the disease group cannot be a strong positive test for that disease.
2. Sivertsen 2013 (n≈9,338) measured the DSPS-vs-non-DSPS difference in this gap directly: **0.60 h**
   (SE 0.086). A 36-minute mean separation against a ~1.5 h within-population SD cannot generate a
   large likelihood ratio.
3. A 2+ hour weekend delay with more weekend sleep is the **worldwide adolescent norm**
   (`gradisar2011meta.yaml`, 41 surveys). Features present in most of the healthy population have LR ≈ 1
   by construction.

This is the central corrective my shard supplies. The brief's premise — "that exact pattern is also the
classic presentation of DSWPD" — is true as a statement about phenotype and false as a statement about
diagnostic information. It is the classic presentation of *being a teenager*.

#### (b) "Long sleep onset latency on weekday nights" — LR+ up to **3.4**, and LR− as low as **0.21**

| Threshold | P(+ \| DSWPD) | P(+ \| no DSWPD) | LR+ | LR− |
|---|---|---|---|---|
| >20 min | 0.942 | 0.743 | 1.27 | 0.227 |
| >30 min | 0.903 | 0.650 | 1.39 | 0.277 |
| >45 min | 0.815 | 0.494 | 1.65 | 0.365 |
| >60 min | 0.689 | 0.338 | **2.04** | 0.469 |
| >90 min | 0.378 | 0.111 | **3.40** | 0.700 |
| **≤15 min** | 0.044 | 0.216 | — | **0.205** |
| **≤20 min** | 0.058 | 0.257 | — | **0.227** |

**[derived]** from the distributions in §2.1.

**This is the load-bearing feature, and it works far better as a rule-out than as a rule-in.** Note that
the conventional 30-minute threshold is close to useless in this population (LR+ 1.39) because
`hysing2013.yaml` shows **65% of all adolescents already exceed it**. If a threshold is used at all it
should be 60 or 90 minutes. Conversely, "falls asleep within 15-20 minutes on a weekday night" carries
LR ≈ 0.21-0.23, dividing the DSWPD odds by more than four — the strongest single piece of evidence
obtainable from one question.

#### (c) "Ability to sleep normally when the schedule permits" — LR ≈ **0.49-0.53** for falling asleep quickly on free nights, and the textbook claim is overstated

ICSD-3 and the review literature assert a clean split. Verbatim (`mader2022.yaml`):

> "When given the opportunity to sleep (e.g., during the weekend), a person with delayed sleep-wake phase
> disorder or insomnia disorder will have difficulty initiating sleep at the desired time; however, a
> person with ISS will easily fall asleep."

The diary data do not support this as cleanly as the sentence implies. Diagnosed DSPD adolescents still
took **66.0 min (SD 40.2)** to fall asleep on *free* nights — only ~12 min less than on school nights
(`gradisar2011rct.yaml`). So:

| Observation | LR for DSWPD |
|---|---|
| Free-night latency ≤20 min | **0.49** |
| Free-night latency ≤30 min | **0.53** |

**[derived]**. Useful but modest — it divides the odds by about two, not by ten. The important
qualification is that the *diagnostically decisive* version of this criterion is not "can he sleep at the
weekend" but "**can he fall asleep if he goes to bed at 22:30 on a Tuesday and genuinely tries**". That
question is near-definitional for ICSD-3 criterion A, and a "yes" is close to an exclusion. I assign it
LR− ≈ 0.07 and LR+ ≈ 3.8 **[judgement — this is derived from the structure of the diagnostic criterion,
not from data, and the report must flag it as such]**.

#### (d) "Difficulty waking" / oversleeping — LR+ = **5.52**, the best dichotomous discriminator available

From `sivertsen2013.yaml`, Table 2, n≈9,338 adolescents aged 16-19:

- Self-reported oversleeping "most days" or "always": **27.6% in DSPS vs 5.0% in non-DSPS**
- **LR+ = 0.276/0.050 = 5.52** ; LR− = 0.724/0.950 = **0.762**

This is a directly measured ratio in an age-exact population, not a modelled one. **It is the single item
the report should ask in preference to computing a weekday-weekend sleep-duration difference.** Note the
asymmetry: its presence is strong evidence (×5.5) but its absence is weak evidence (÷1.3), because 72% of
DSPS cases did *not* report frequent oversleeping.

### 2.3 Two further features, one of which is a surprise

#### (e) Free-day mid-sleep timing / chronotype — LR ≈ **1.1-1.8**, a weak test at this age

| Free-day mid-sleep | LR for DSWPD |
|---|---|
| 03:00 | 0.75 |
| 04:30 | 1.66 |
| 05:00 | 1.81 |
| 06:00 | 1.67 |
| 07:00 | 1.09 |
| 08:00 | 0.50 |

**[derived]**, disease-present 05:12 (SD 1.42 h, from the Gradisar cohort's weekend onset and rise times
and their SDs) vs age-19 male norm 05:02 (SD 2.60 h, `fischer2017.yaml`).

**The diagnosed DSPD cohort's weekend mid-sleep (05:12) is essentially identical to the population norm
for a 19-year-old US male (05:02).** Relative to their own age norm (~04:01 at 14.6 y, SD 1.53 h) the
diagnosed cases sat at only **+0.77 SD**. The healthy 18-19 y male distribution is so wide (SD 2.1-2.6 h)
that diagnosed cases sit comfortably inside it. **Do not diagnose DSWPD from chronotype or mid-sleep
timing alone**, and do not treat a late MSFsc as confirmatory. This also means the LR is non-monotonic:
an extremely late mid-sleep (08:00) actually argues *against* DSWPD-as-characterised-in-the-trial-cohort,
because it is beyond what the diagnosed cases showed.

#### (f) Preserved daytime function — LR ≈ **0.5** [judgement]

Diagnosed adolescent DSPD is functionally destructive (`gradisar2011rct.yaml`): **16%** (8/49, 95% CI
6.0-26.7% [derived]) had stopped attending school entirely; of those still attending, 24% arrived 10+
minutes late *every day*, 5% missed whole days, and **24% had received detention, exclusion or expulsion**
because of lateness. The authors state that this impairment is precisely what "differentiated them from
the typical sleep patterns found during adolescence".

Our subject is progressing into his second year of college and attributes the pattern to workload — he is
meeting his morning obligations. I assign LR ≈ 0.5 rather than something stronger for two reasons: the
trial cohort was clinic-referred and therefore enriched for severity, and the ICSD-3 impairment criterion
can be satisfied by daytime sleepiness alone without attendance failure.

### 2.4 Features that do NOT discriminate — recorded so the report does not misuse them

- **Weekend total sleep time.** DSPS minus non-DSPS = **−0.167 h** (95% CI −0.307 to −0.026), i.e. DSPS
  adolescents slept *very slightly less* at weekends (`sivertsen2013.yaml`). Long weekend sleep is not a
  DSWPD marker.
- **BMI.** No difference between DSPS and non-DSPS (`sivertsen2013.yaml`).
- **Short weekday sleep as such.** The subject's 5-6 h is *shorter* than the diagnosed DSPD cohort's
  7.02 h and shorter than the population mean of 6.42 h. Being more sleep-restricted than DSPD patients
  points away from a circadian mechanism and towards restricted opportunity.
- **The Chronic Sleep Reduction Questionnaire.** Adolescents with insomnia and adolescents with DSWPD
  scored identically on it (t(294) = −0.60, P = 0.55) and were pooled for that reason
  (`dewaldkaufmann2018.yaml`). It measures severity, not differential.
- **A normal Epworth score.** In the only DLMO-confirmed DSWPD sample available (`sletten2018.yaml`,
  n=116), **84.5% of confirmed cases scored in the normal/borderline ESS range (0-9)**; just 15.5%
  exceeded >9. An ESS screen would miss five in six confirmed cases, so **a normal ESS in this subject
  does essentially nothing to lower the DSWPD posterior.** DSWPD sleepiness is schedule-dependent, not
  constitutional. The corollary is useful though: because irrepressible sleepiness is a *required* BIISS
  criterion but absent in most DSWPD, a clearly elevated ESS points towards insufficient sleep rather
  than towards a circadian disorder.
- **The ISI, as between DSWPD and insomnia disorder.** Mean baseline ISI in that same DLMO-confirmed DSWPD
  sample was **12.93 (SD 4.86)** — above the ≥10 case-detection cut-off but inside the ISI's own
  *subthreshold* band, with 16.4% scoring in the "insomnia absent" range. An ISI ≥10 is therefore equally
  consistent with either diagnosis, and an ISI <10 does not exclude DSWPD. The ISI grades insomnia
  severity; it is not a differential-diagnostic test (see §3.3).

### 2.5 A fifth hypothesis my partition omits: depressive disorder

The model in §3 has five branches and none of them is depression. That is a real limitation, because
depression both delays sleep timing and impairs morning rising, so it can generate the subject's entire
reported phenotype without any circadian pathology.

The association is large. From `dama2025.yaml` (16 studies, 693 participants, all ICSD- or DSM-diagnosed
DSWPD): young people meeting DSWPD criteria had depression symptom severity **Cohen's d = 0.92 (95% CI
0.76-1.08)**, rising to **d = 1.02 (95% CI 0.85-1.19, I² = 0%)** in the cleanest sensitivity analysis, and
holding at **d = 0.88 (0.70-1.06)** when restricted to studies that controlled for psychiatric disorders.
Caveat on the intervals: the authors fitted fixed-effect models at I² = 53-62%, so the primary CI is
narrower than it should be.

Every component study is cross-sectional or case-control, so **the direction of causation is not
established** and reverse causation is fully compatible with the data. The practical consequence is that a
subject with both a delayed pattern and low mood cannot be assigned to DSWPD on that basis, and a mood
screen belongs alongside the circadian workup (see `instruments.md`). I have not assigned depression a
prior or a likelihood because doing so is outside my shard's extraction scope and would require the
adolescent depression base rate; the report should treat this as a named gap in my partition rather than
as an implicit zero.

---

## 3. Posterior computation

### Model

Five competing explanations for the reported pattern, with unconditional priors in 16-19 year old males
and the likelihood of habitual 5-6 h weekday sleep under each:

| Hypothesis | Prior | P(5-6 h weekday sleep \| H) | Basis for the likelihood |
|---|---|---|---|
| BIISS (full ICSD-3 syndrome) | 0.104 | 0.90 **[judgement]** | short sleep is definitional |
| DSWPD | 0.040 | 0.158 **[derived]** | P(5<TST<6) given mean 7.02, SD 1.34 (Gradisar) |
| Insomnia disorder | 0.200 | 0.30 **[judgement]** | short sleep common but not required |
| OSA (symptomatic) | 0.010 | 0.253 **[derived]** | population rate; no strong link to short TST |
| Behavioural restriction not meeting BIISS criteria | 0.646 | 0.253 **[derived]** | P(5<TST<6) given mean 6.42, SD 1.10 |

The `Behavioural restriction` category is short habitual sleep that fails ICSD-3 BIISS criterion A
(irrepressible daytime sleepiness) — i.e. exactly the "purely behaviourally-imposed sleep restriction"
alternative the task brief names. The population weekday SD of 1.10 h is an assumption **[judgement]**;
§3.2 shows the result is insensitive to it.

### 3.1 Results

**S0 — pattern only (current information state):**
behavioural-only 50.2% | BIISS 28.7% | insomnia 18.4% | DSWPD 1.9% | OSA 0.8%
→ **P(any intrinsic treatable disorder) = 21.1%**

**S1 — falls asleep ≤20 min on weekday *and* free nights, no frequent oversleeping, function preserved.**
Composite LRs: DSWPD 0.227 × 0.491 × 0.762 × 0.5 = 0.0425; insomnia 0.227 × 0.30 = 0.068.
behavioural-only 62.0% | BIISS 35.4% | insomnia 1.6% | OSA 1.0% | DSWPD **0.1%**
→ **P(any intrinsic treatable disorder) = 2.6%**

**S2 — latency >60 min every night including free nights, oversleeps most days, cannot sleep early.**
insomnia 47.4% | DSWPD 35.6% | behavioural-only 10.6% | BIISS 6.0% | OSA 0.3%
→ **P(any intrinsic treatable disorder) = 83.4%**
Note insomnia *outranks* DSWPD here purely because its prior is five times larger. ICSD-3 gives DSWPD
diagnostic precedence when the insomnia is explained by circadian misalignment
(`gradisar2011rct.yaml`: "the DPSD diagnosis takes precedence over an insomnia disorder diagnosis"), so
in practice the two would be adjudicated on sleep timing, not on latency alone.

**S3 — latency >60 min on weekday nights but sleeps normally once at his late free-day time, oversleeps
most days.** This is the genuinely diagnostic DSWPD pattern.
DSWPD **44.9%** | behavioural-only 24.8% | insomnia 15.5% | BIISS 14.2% | OSA 0.6%
→ **P(any intrinsic treatable disorder) = 61.0%**

### 3.2 Sensitivity

Varying the assumed population weekday-sleep SD over 0.9-1.3 h and P(5-6 h | BIISS) over 0.80-0.95 moves
the S1 numbers only within: BIISS 31.9-38.3%, DSWPD 0.10-0.11%, insomnia 1.48-1.68%, behavioural-only
59.1-65.4%. The conclusion is robust to both assumptions.

Varying the DSWPD prior across its full evidenced range:

| DSWPD prior | S1 posterior | S2 posterior |
|---|---|---|
| 2.7% (`sivertsen2013`) | 0.07% | 27.2% |
| 4.0% (adopted) | 0.10% | 35.6% |
| 5.7% (`saxvig2012`) | 0.14% | 44.1% |

The prior choice barely matters in S1 and matters substantially in S2 — i.e. it matters exactly when the
clinical features are already pointing at DSWPD, which is the right behaviour for a prior.

### 3.3 Instrument-conditional posteriors for insomnia

Using the ROC-derived ISI likelihood ratios (LR+ 7.00, LR− 0.159 **[derived]** from sensitivity 86.1% /
specificity 87.7%, `morin2011.yaml`):

| Insomnia prior | ISI ≥10 → posterior | ISI <10 → posterior |
|---|---|---|
| 10.7% | 45.6% | 1.9% |
| 18.0% | 60.6% | 3.4% |
| 22.2% | 66.6% | 4.3% |

A second validation, the only one using a structured DSM-5 interview in young adults
(`michaud2021.yaml`, n=250, AUC 0.91), gives a **lower** optimal threshold of ≥8 (LR+ 3.70, LR− 0.195) and
a high-sensitivity option at ≥7 (LR+ 3.20, **LR− 0.057**). The two validations agree about the extremes and
disagree about the middle, so the defensible reading is graded rather than dichotomous **[judgement]**:

| ISI band | Interpretation | Posterior from an 18% prior |
|---|---|---|
| **<7** | insomnia disorder effectively excluded (LR− 0.057) | **~1%** |
| 7-9 | **indeterminate** — positive by Michaud, negative by Morin | not computable; go to diary |
| ≥10 | positive on both validations | ~45-61% |
| ≥15 | moderate-severe; selects ~7.5% of the population (`vanstraten2025.yaml`) | refer for CBT-I |

**A single ISI score moves the insomnia posterior from ~18% to either ~61% or ~3%.** This is the highest
information-per-minute measurement in the entire protocol **for the insomnia question**.

Two qualifications, the second of which I initially understated:

1. The Morin cut-off is externally corroborated at population level: defining insomnia as ISI ≥10 yields a
   general-population prevalence of **12.5% (95% CI 5.3-26.8%)** against **12.4% (9.0-16.8%)** from DSM
   diagnostic interviews in the same synthesis (`vanstraten2025.yaml`). The threshold recovers the right
   prevalence by a route entirely independent of Morin's ROC analysis.
2. **The ISI does not adjudicate between insomnia disorder and DSWPD.** In the DLMO-confirmed DSWPD sample
   (`sletten2018.yaml`) the mean baseline ISI was 12.93 — i.e. a confirmed DSWPD patient screens *positive*
   at ≥10. So an ISI ≥10 in this subject raises P(insomnia symptoms are real) but does **not**
   redistribute probability between the two competing intrinsic diagnoses. Sleep *timing* from the 14-day
   diary does that, not the ISI score. The 61% figure above should be read as "P(clinically significant
   insomnia complaint)", not "P(insomnia disorder rather than DSWPD)".

---

## 4. Does he meet BIISS criteria? Criterion-by-criterion

ICSD-3 criteria verbatim (`mader2022.yaml`, all of A-F required):

| | Criterion (verbatim, abridged) | Status for this subject |
|---|---|---|
| A | "daily periods of irrepressible need to sleep or daytime lapses into sleep" | **UNKNOWN — must ask.** This is the pivotal unasked question and it is what separates BIISS from ordinary short sleep. |
| B | "sleep time … is usually shorter than expected for age" | **MET.** 5-6 h against the 8-10 h recommended for 13-18 y (`fischer2017.yaml`). |
| C | "curtailed sleep pattern is present most days for at least three months" | **MET.** Three years. |
| D | "curtails sleep time by such measures as an alarm clock … and generally sleeps longer when such measures are not used, such as on weekends or vacations" | **MET.** 5-6 h → 7-8 h, occasionally 10-11 h. |
| E | "Extension of total sleep time results in resolution of the symptoms of sleepiness" | **UNTESTED.** Requires a therapeutic trial of extended sleep, which is itself the recommended first intervention. |
| F | "not better explained by another untreated sleep disorder …" | **This is the whole question above.** |

So **three of six criteria are met on his own account, one is unknown, one requires a trial, and one is
the differential**. The report can state that he meets the *pattern* criteria for BIISS and that
confirmation turns on criterion A (sleepiness) and criterion E (does extension fix it).

Note the ICSD-3 requirement of objective corroboration, verbatim (`mader2022.yaml`): "If there is doubt
about the accuracy of personal history or sleep logs, then actigraphy should be performed, **preferably
for at least two weeks**."

---

## 5. What would change the answer, ranked by information value

1. **Weekday sleep-onset latency** — LR 0.21 (fast) to 3.4 (>90 min). One question.
2. **ISI total score** — LR+ 7.00 / LR− 0.159. Seven items.
3. **"Do you oversleep most days or always?"** — LR+ 5.52. One question.
4. **"If you go to bed at 22:30 on a Tuesday and genuinely try, can you fall asleep?"** — near-definitional
   for ICSD-3 criterion A; a "yes" is close to an exclusion of DSWPD. **[judgement]**
5. **Irrepressible daytime sleepiness (ESS-CHAD; BIISS criterion A)** — determines whether this is a
   syndrome or just short sleep.
6. **14 consecutive days of sleep diary + actigraphy including two weekends** — gives free-day sleep onset
   time, which is the missing input for MSFsc, plus objective corroboration for BIISS criterion B.
7. **A mood screen.** Not a discriminator I can quantify, but depression is a competing explanation for
   the whole phenotype and is strongly associated with DSWPD (d ≈ 0.9, `dama2025.yaml`). Omitting it
   leaves a hole in the partition (§2.5).
8. Free-day mid-sleep / chronotype — LR only 1.1-1.8. **Worth measuring for the treatment plan, not for
   the diagnosis.**
9. Weekday-weekend sleep-duration gap — LR 1.1-1.4. **Already known; adds nothing.**

---

## 6. If DSWPD is confirmed, the treatment is different and the effect is large

This is why the 2% (S1) to 45% (S3) spread matters clinically.

From `gradisar2011rct.yaml` (RCT, n=49 diagnosed adolescent DSPD, 6 sessions CBT + morning bright light
vs waitlist): **13% of treated adolescents still met DSPD criteria at post-treatment vs 82% of
waitlist**, χ²(1,N=40) = 19.22, P < 0.0001. Risk ratio 0.16 (log RR −1.84, SE 0.586 **[derived]**),
absolute risk reduction 69 percentage points, **NNT 1.4**. School-night sleep rose 7.1 → 8.1 h (d = 0.81)
and school-night latency fell 78.1 → 22.2 min (d = 1.13).

For melatonin the best randomised evidence is `sletten2018.yaml` (T1, n=116, double-blind,
DLMO-confirmed DSWPD): **0.5 mg fast-release melatonin 1 h before desired bedtime plus behavioural
scheduling** advanced actigraphic sleep onset **34 min** (95% CI −60 to −8) and produced clinician-rated
marked improvement in 52.8% vs 24.0% (RR 2.20, 95% CI 1.26-3.83, **NNT 3.5** [derived]). Note that it
worked as a **hypnotic, not a chronobiotic** — post-treatment DLMO was not significantly advanced
(0.49 h, 95% CI −0.20 to +1.18 [derived]) — so melatonin should not be described to the subject as
resetting his clock. On the available evidence the adolescent behavioural-plus-light option (NNT 1.4) looks
stronger than adult melatonin (NNT 3.5), though these are different populations and I am not pooling them.

The AASM 2015 guideline recommendations and the exact light and melatonin parameters are in
`instruments.md` §6 and `auger2015.yaml`.

Conversely, if this is BIISS, the intervention is sleep-opportunity extension and schedule regularisation,
and timed light or melatonin would be inert at best.

**And the cost of leaving it undiagnosed is not confined to sleep.** Two findings bound it. Young people
meeting DSWPD criteria carry a large excess depressive symptom burden, **d ≈ 0.9-1.0** (`dama2025.yaml`),
though the cross-sectional designs cannot tell us whether treating the circadian problem would relieve it.
And the condition is **70% persistent** over 19 months in late adolescence (`jaakallio2026.yaml`), so the
burden does not self-resolve on the timescale of a degree. Together these justify spending real
measurement effort on a hypothesis whose current posterior is only ~2%: the 21% figure in state S0 is an
expected-value argument, not a claim that DSWPD is likely.
