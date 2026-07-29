# Screening instruments, cut-offs and referral thresholds

Shard `s19_sleep_disorders`. For the measurement protocol of a report on an 18-19 year old male with
~5-6 h weekday sleep and ~7-8 h weekend sleep since age 16.

Every cut-off below is traceable to a YAML record in this directory. Where a cut-off is **not** validated
in this age group, that is stated explicitly rather than glossed.

---

## 1. Summary table

| Instrument | Score range | Cut-off | Validated in 16-19 y? | LR+ / LR− | Source |
|---|---|---|---|---|---|
| **ISI** Insomnia Severity Index | 0-28 | **≥10** (community); **≥8** in young adults; **<7** rules out | No — adults only, but one young-adult validation | **7.00 / 0.159** at ≥10; **3.70 / 0.195** at ≥8; **—/0.057** at <7 [derived] | `morin2011.yaml`, `michaud2021.yaml`, `vanstraten2025.yaml` |
| **ESS / ESS-CHAD** Epworth | 0-24 | **>10** = excessive sleepiness; 12-24 = hypersomnolence-patient range | **No adolescent cut-off exists** | not derivable | `johnshocking1997.yaml`, `janssen2017.yaml`, `johns1991.yaml` |
| **CSRQ** Chronic Sleep Reduction Q. | ~11-55 | **≥40** to act; **<28** to rule out | **Yes** (Dutch, mean 15.4 y) | 4.06 / 0.373 at 40; 1.27 / **0.045** at 28 | `dewaldkaufmann2018.yaml` |
| **MCTQ** → MSFsc | clock time | no cut-off; compare to age/sex norm | Norms yes (US, single years) | 1.1-1.8 only | `roenneberg2019.yaml`, `fischer2017.yaml` |
| **Sleep diary + actigraphy** | — | **14 consecutive days** incl. 2 weekends | AASM conditional, paediatric included | — | `smith2018.yaml`, `auger2015.yaml`, `mader2022.yaml` |
| **Consumer wearable** | — | duration/timing only, ≥14-night averages; **never for sleep onset latency** | Adults only | current-gen TST bias **<12 min**; per-night LoA ≈ ±45 min | `haghayegh2019.yaml`, `chinoy2021.yaml`, `lee2025.yaml` |
| Validated **DSWPD-specific** screener | — | **none exists** | — | — | see §5 |

---

## 2. Insomnia Severity Index (ISI) — the strongest instrument in this set

**Citation.** Morin CM, Belleville G, Bélanger L, Ivers H. The Insomnia Severity Index: psychometric
indicators to detect insomnia cases and evaluate treatment response. *Sleep.* 2011;34(5):601-608.
DOI 10.1093/sleep/34.5.601, PMID 21532953. (`morin2011.yaml`)

**Cut-off.** ≥10, ROC-derived in a population-based community sample (n=959):

> "A cutoff score of 10 was optimal (86.1% sensitivity and 87.7% specificity) for detecting insomnia
> cases in the community sample."

**Derived likelihood ratios [derived, my arithmetic]:**
- LR+ = 0.861 / (1 − 0.877) = **7.00**
- LR− = (1 − 0.861) / 0.877 = **0.159**

**A second validation, in young adults and against a structured DSM-5 interview, gives a *lower*
cut-off.** Michaud AL, Zhou ES, Chang G, Recklitis CJ. Validation of the Insomnia Severity Index (ISI) for
identifying insomnia in young adult cancer survivors: comparison with a structured clinical diagnostic
interview of the DSM-5 (SCID-5). *Sleep Med.* 2021;81:80-85. DOI 10.1016/j.sleep.2021.01.045,
PMID 33640841. (`michaud2021.yaml`) n=250, AUC **0.91**.

| Source | Population | Reference standard | Cut-off | Sens | Spec | LR+ | LR− |
|---|---|---|---|---|---|---|---|
| `morin2011` | community adults, Canada | insomnia case criteria | ≥10 | 0.861 | 0.877 | **7.00** | 0.159 |
| `michaud2021` | **young adults**, US | **SCID-5 interview** | ≥8 | 0.85 | 0.77 | 3.70 | 0.195 |
| `michaud2021` | as above | as above | ≥7 | 0.96 | 0.70 | 3.20 | **0.057** |

All LRs [derived, my arithmetic]. The younger sample yielded a lower optimal threshold, but with two
studies in different populations I cannot attribute that to age — cancer survivorship is at least as
plausible a cause. The authors' own caution is the point to carry:

> "Results of this study and prior studies of the ISI offer important reminders that cut-off scores derived
> from different populations are not generalizable."

**Referral / action thresholds — use the ISI as a graded instrument, not one dichotomy** [judgement: my
synthesis of the two validations, which agree about the extremes and disagree about the middle]:
- **ISI < 7** → insomnia disorder effectively excluded. LR− **0.057**, taking an 18% prior to **~1%**.
  This is the strongest single rule-out in the entire protocol.
- **ISI 7-9** → **indeterminate zone.** Positive by Michaud, negative by Morin. Do not dichotomise here;
  go to the 14-day diary.
- **ISI ≥ 10** → positive on both validations; posterior ~45-61% from an 18% prior. Proceed to a sleep
  diary to determine *which* phenotype, and specifically whether the initiation difficulty is confined to
  conventional bedtimes (which points to DSWPD, and ICSD-3 gives DSWPD diagnostic precedence) or occurs at
  all bedtimes (insomnia disorder). **The ISI score itself cannot make that call** — see §2.2.
- **ISI ≥ 15** is the conventional moderate-severity band and a reasonable trigger for referral to CBT-I.
  *The 15 threshold is not in Morin 2011 — do not cite that paper for it.* It is however now supported
  independently at population level: defining insomnia as ISI ≥ 15 selects **7.5% (95% CI 4.8-11.4%)** of
  the general population (`vanstraten2025.yaml`), a defensible referral yield, whereas ISI ≥ 8 would flag
  25.1% and over-refer.
- **Treatment response:** a fall of **8.4 points** (95% CI 7.1-9.4) corresponds to moderate
  clinician-rated improvement. Use as the responder threshold if monitoring.

**Psychometrics.** Cronbach α 0.90 (community) and 0.91 (clinical). Item response theory found adequate
discrimination for only 5 of the 7 items.

### 2.1 Independent population-level validation of the ≥10 cut-off

van Straten A, Weinreich KJ, Fábián B, et al. The Prevalence of Insomnia Disorder in the General
Population: A Meta-Analysis. *J Sleep Res.* 2025;34(5):e70089. DOI 10.1111/jsr.70089, PMID 40369835.
(`vanstraten2025.yaml`) 47 studies, PROSPERO CRD42023402745.

Defining insomnia as **ISI ≥ 10 yields a population prevalence of 12.5% (95% CI 5.3-26.8%)**, against
**12.4% (95% CI 9.0-16.8%)** from DSM diagnostic interviews in the same synthesis. The cut-off recovers
the right population prevalence, reached by a completely different route from Morin's ROC analysis. The
authors recommend it explicitly:

> "the two instruments we currently recommend are the Sleep Condition Indictor, which is based on DSM-5
> criteria, or the Insomnia Severity Index with a cut-off of 10, which although based on the DSM-IV
> resulted in a prevalence estimate close to that of the clinical interviews."

Same source, useful for reading the rest of this shard's insomnia numbers: interview-based prevalence
12.4% vs self-report 16.3%, and high-quality studies 10.7% vs lower-quality 17.1% (P = 0.02). Expect
questionnaire-based estimates to run roughly 1.3× interview-based ones.

### 2.2 Important limitation: the ISI does **not** discriminate DSWPD from insomnia disorder

I originally described the ISI as the highest-information measurement in the protocol. That claim holds
**only for the insomnia-vs-no-insomnia question**, and one record forces the qualification.

In the only DLMO-confirmed DSWPD sample I have (`sletten2018.yaml`, n=116 Australian outpatients with
salivary melatonin onset confirmed delayed relative to desired bedtime), the **mean baseline ISI was
12.93 (SD 4.86)** — above the ≥10 case-detection threshold but inside the ISI's own *subthreshold*
insomnia band (8-14). Only 40.0% were in the moderate/severe band, and **16.4% scored in the "insomnia
absent" band (0-7)**.

Two consequences:
- An **ISI ≥ 10 in this subject is equally consistent with DSWPD as with insomnia disorder.** It cannot
  adjudicate between them; sleep *timing* does that.
- An **ISI < 10 does not exclude DSWPD**, even though it largely excludes insomnia disorder.

**Age limitation.** The cut-off was derived in adults and Morin 2011 gives no age-stratified analysis. A
separate adolescent ISI psychometrics paper exists (PMID 34381573, Iranian adolescents) but is a
translation/factor-structure study and would not change the threshold. `vanstraten2025.yaml` cannot help
either: its contributing studies have mean ages of 37.0-84.3 years, so its null age moderator (P = 0.98)
says nothing about 18-19 year olds.

---

## 3. Epworth Sleepiness Scale — use the adolescent wording, borrow the adult threshold, and say so

**Three separate citations are needed, and the usual single-citation practice is wrong.**

### 3.1 The original validation does not contain a cut-off
Johns MW. A new method for measuring daytime sleepiness: the Epworth sleepiness scale. *Sleep.*
1991;14(6):540-545. PMID 1798888. (`johns1991.yaml`) — establishes construct validity only. **Citing
Johns 1991 for the ">10" threshold, which is common, is incorrect.**

### 3.2 The cut-off and the normal range come from a 1997 occupational survey
Johns M, Hocking B. Daytime sleepiness and sleep habits of Australian workers. *Sleep.*
1997;20(10):844-849. PMID 9415943. (`johnshocking1997.yaml`)

> "Normal sleepers, without any evidence of a sleep disorder, had ESS scores between 0 and 10, with a
> mean of 4.6 +/- 2.8 (standard deviation)."
> "They were clearly separated from the 'sleepy' patients suffering from narcolepsy or idiopathic
> hypersomnia whose ESS scores were in the range 12-24, as described previously."
> "ESS scores > 10 were taken to represent excessive daytime sleepiness, the prevalence of which was 10.9%."

| Quantity | Value |
|---|---|
| Normal-sleeper range | **0-10** (mean 4.6, SD 2.8) |
| Cut-off for excessive daytime sleepiness | **>10** (i.e. ≥11) |
| Range in central-hypersomnolence patients | **12-24** |
| Prevalence of ESS >10 in healthy adult workers | **10.9%** (95% CI 7.6-14.3% [derived]) |

**Two things the report must not do with this.** First, >10 is a *normal-range boundary from an
occupational sample aged 22-59*, not an ROC-optimised cut-off against a diagnostic standard; no
sensitivity or specificity exists for it, which is why I give no likelihood ratio. Second, roughly **1 in
9 healthy adult workers screens positive**, so a positive ESS alone is weak evidence of pathology. If the
goal is to detect a hypersomnolence disorder rather than to flag any sleepiness, **≥12-13** is the more
defensible threshold, because that is where the patient distribution began with no overlap.

Also directly relevant to our differential: in that sample a raised ESS tracked reduced time in bed
(insufficient sleep) and insomnia and snoring, and did **not** track obesity. **An elevated ESS in this
subject is not specific to OSA and is fully compatible with pure behavioural sleep restriction.**

### 3.2b A normal ESS does **not** argue against DSWPD — it would miss ~5 of 6 confirmed cases

This is the most important qualification in this section, and it comes from the only DLMO-confirmed DSWPD
sample in my evidence base (`sletten2018.yaml`, n=116).

At baseline, **84.5% (95% CI 75.2-93.8% [derived]) of confirmed DSWPD patients scored in the
normal/borderline ESS range (0-9)**; only 15.5% exceeded the conventional >9 threshold. An ESS used to
screen for DSWPD would therefore **miss roughly five in six confirmed cases**.

> "Normal/borderline (0-9) 49 (84.5) 49 (84.5) >0.999 ... Excessive daytime sleepiness (>9) 9 (15.5) 9 (15.5)"

Two consequences for the protocol:
- **Do not use the ESS as a DSWPD screen, and do not treat a normal ESS in this subject as reassuring
  about DSWPD.** It has essentially no power to lower that posterior. The underlying reason is that DSWPD
  sleepiness is schedule-dependent — it appears when the person is forced awake at a socially required
  time, not as a constitutional trait the ESS is built to capture.
- Conversely this **sharpens the ESS's role in separating BIISS from DSWPD**: irrepressible daytime
  sleepiness is a *required* criterion for BIISS (ICSD-3 criterion A) but is absent in most DSWPD. So a
  clearly elevated ESS points towards insufficient sleep rather than towards a circadian disorder.

### 3.3 Adolescent norms do not exist — a documented gap
Janssen KC, Phillipson S, O'Connor J, Johns MW. Validation of the Epworth Sleepiness Scale for Children
and Adolescents using Rasch analysis. *Sleep Med.* 2017;33:30-35. DOI 10.1016/j.sleep.2017.01.014,
PMID 28449902. (`janssen2017.yaml`)

The developers of the adolescent version state in their own validation paper:

> "Further studies are needed to establish the internal validity of the ESS-CHAD for children under 12
> years, and to establish external validity and **accurate cut-off points for children and adolescents**."

**Practical instruction.** Administer the **ESS-CHAD** wording (the adult ESS references alcohol and
driving, which either do not apply or invite non-response), score 0-24 as usual, and interpret against
the adult thresholds **while stating that they are unvalidated in this age group**. Treat the ESS as a
triage and severity measure, not as a diagnostic test. I searched for a large representative adolescent
ESS normative sample with a derived cut-off and did not find one; what exists is a set of
non-English-language translations and a paediatric narcolepsy validation.

**Referral thresholds (adult thresholds, applied with the caveat above):**
- ESS ≤10 → within the adult normal range. Sleepiness is not the presenting problem. **This does not lower
  the DSWPD posterior** (§3.2b).
- ESS 11-15 → above normal. Consistent with insufficient sleep; **first action is a 14-day diary and a
  trial of sleep extension, not a sleep-clinic referral.**
- ESS ≥16, **or** ESS ≥12 that persists after 2-4 weeks of adequate sleep opportunity → refer to sleep
  medicine. Persistent sleepiness despite corrected sleep opportunity is the finding that makes an
  intrinsic disorder (OSA, narcolepsy, idiopathic hypersomnia) worth objective testing, and it is the
  operational form of ICSD-3 BIISS criterion E.

---

## 4. Munich ChronoType Questionnaire and MSFsc

**Citations.** Roenneberg T, Pilz LK, Zerbini G, Winnebeck EC. Chronotype and Social Jetlag: A (Self-)
Critical Review. *Biology (Basel).* 2019;8(3):54. DOI 10.3390/biology8030054, PMID 31336976
(`roenneberg2019.yaml`) — the formula. Fischer D, Lombardi DA, Marucci-Wellman H, Roenneberg T.
Chronotypes in the US — Influence of age and sex. *PLoS One.* 2017;12(6):e0178782.
DOI 10.1371/journal.pone.0178782, PMID 28636610 (`fischer2017.yaml`) — the age/sex norms.

### 4.1 How MSFsc is computed (verbatim)

> "To clean chronotype of the confounder sleep debt, we correct MSF (MSF sc = sleep corrected MSF). For
> this correction, we first calculate the average sleep duration across the entire week (SD week) and
> then correct MSF by subtracting half of the oversleep. This correction is only applied for people who
> sleep longer on work-free days than on workdays (SD f > SD w):"

```
If SD_f <= SD_w :   MSFsc = MSF   = SO_f + SD_f/2
If SD_f  > SD_w :   MSFsc = MSF - (SD_f - SD_week)/2  =  SO_f + SD_week/2
```

where `SO_f` = sleep onset on free days, `SD_w` / `SD_f` = sleep duration on work/free days,
`SD_week` = weekly average sleep duration (= (5·SD_w + 2·SD_f)/7 for a five-day week), `MSF` = mid-sleep
on free days.

Related: social jetlag `SJL = |MSF − MSW|` (uncorrected MSF, **not** MSFsc — using MSFsc here is a
documented common error). The sleep-corrected variant simplifies algebraically to `|SO_f − SO_w|`.

### 4.2 Worked example on this subject's own numbers **[derived, illustrative]**

Taking SD_w = 5.5 h and SD_f = 7.5 h: SD_week = (5×5.5 + 2×7.5)/7 = **6.07 h**, and since SD_f > SD_w,
**MSFsc = SO_f + 3.04 h**. So a 01:30 free-night sleep onset gives MSFsc 04:32; a 02:30 onset gives 05:32.
Under his occasional 10-11 h weekend variant (SD_f = 10.5): SD_week = 6.93 h, MSFsc = SO_f + 3.46 h.

**The dominant term is free-day sleep ONSET time, and we do not have it. No chronotype can be computed
without it. This is the single highest-value question to ask him.**

### 4.3 Normative distribution for 18-19 year olds

From `fischer2017.yaml`, Table 1 — American Time Use Survey, n=53,689, survey-weighted, **males**,
mid-sleep on weekends (MSFWe), decimal hours:

| Age | n | MSFWe | SD |
|---|---|---|---|
| 15 | 325 | 4.02 (04:01) | 1.53 |
| 16 | 494 | 4.34 (04:20) | 1.79 |
| 17 | 458 | 4.58 (04:35) | 2.23 |
| **18** | 303 | **4.62 (04:37)** | **2.14** |
| **19** | 229 | **5.03 (05:02)** | **2.60** |
| 20 | 214 | 4.86 (04:52) | 2.39 |
| all males | 23,463 | 3.45 (03:27) | 2.44 |

Peak lateness in males is at **age 19.2 y**; whole-population quartiles are 25th percentile 02:24, 75th
percentile 04:15 — i.e. **the average 19-year-old male sits above the whole-adult-population 75th
percentile**, so an adult norm must never be used for him.

**Critical measurement caveat.** These are **MSFWe** — mid-sleep on weekends from a *one-day* time-use
diary, with no sleep-debt correction and no exclusion of alarm-clock use. They are **not MSFsc** and are
biased late relative to true MSFsc. Use them as an age/sex-matched *weekend mid-sleep* norm; do not compare
them to an MSFsc value as though the scales were identical.

### 4.4 There is no MSFsc cut-off, and chronotype is a weak diagnostic test

No threshold on MSFsc defines DSWPD, and none should be invented. As quantified in
`screening_priors.md` §2.3(e), the likelihood ratio for free-day mid-sleep across the plausible range is
only **1.1-1.8**, because diagnosed adolescent DSPD cases had a weekend mid-sleep of ~05:12 — essentially
identical to the age-19 male population norm of 05:02 — while the healthy distribution has an SD of
2.1-2.6 h.

**Use the MCTQ to plan the treatment (it tells you when to time light and melatonin relative to his
internal clock), not to make the diagnosis.**

Criterion validity: MSFsc correlates significantly with DLMO, cortisol, activity acrophase and actimetry,
but `roenneberg2019.yaml` does not report the coefficients, so I cannot supply an r. DLMO remains the
gold standard and is "expensive and burdensome — involving multiple, well-timed sampling".

---

## 5. Validated DSWPD screening tool — none exists

I searched specifically for this and the honest answer is that **no instrument with published sensitivity
and specificity for DSWPD exists** in what I could retrieve. What I found instead: a Chinese-language MEQ
validation for screening DSWPD in bipolar disorder, a Japanese Biological Rhythms Interview validation, a
shift-work-disorder screener, and the Auckland Sleep Questionnaire (a general primary-care sleep tool).
None is a DSWPD screener validated in adolescents or young adults. **This is my nominated biggest evidence
gap** (see `station_report.md`).

### The closest available substitute: the Chronic Sleep Reduction Questionnaire (CSRQ)

Dewald-Kaufmann JF, de Bruin EJ, Smits M, Zijlstra BJH, Oort FJ, Meijer AM. Chronic sleep reduction in
adolescents — clinical cut-off scores for the Chronic Sleep Reduction Questionnaire (CSRQ). *J Sleep Res.*
2018;27(3):e12653. DOI 10.1111/jsr.12653, PMID 29341314. (`dewaldkaufmann2018.yaml`)

Matched case-control, 298 adolescents with insomnia **or DSWPD** vs 298 age/sex-matched healthy
adolescents, mean age ~15.4 y. **AUC 0.84 (95% CI 0.81-0.87).** Reference distributions: healthy
32.98 ± 6.51; clinical 42.59 ± 7.06 (d = 1.42 [derived]).

| Cut-off | Sensitivity | Specificity | LR+ [derived] | LR− [derived] | Use |
|---|---|---|---|---|---|
| **≥28** | 0.99 | 0.22 | 1.27 | **0.045** | **rule out** — a score below 28 divides the odds by 22 |
| **≥40** (Youden optimum) | 0.69 | 0.83 | **4.06** | 0.373 | **act** |
| ≥51 | 0.013 | 0.99 | 1.30 | 0.997 | **do not use** — see below |

**Do not use the 51 cut-off.** The paper offers it as a "high specificity" threshold, but at 1.3%
sensitivity against 99% specificity the LR+ is 1.3, which is diagnostically near-worthless. That the
authors recommend it without noting this is a defect in the paper, and it is a good illustration of why
specificity alone never justifies a threshold.

**Hard limit on what the CSRQ can do here.** Adolescents with insomnia and adolescents with DSWPD scored
**identically** (t(294) = −0.60, P = 0.55) and were pooled for that reason. The CSRQ answers "is this
adolescent's sleep reduction clinically significant?" and is **silent on which disorder it is**. Its
reference standard was itself a questionnaire (Holland Sleep Disorder Questionnaire, insomnia cut-off 3.61,
CRSD cut-off 3.41), not an interview or actigraphy, which inflates apparent performance.

### The role of actigraphy plus sleep diaries

**AASM clinical practice guideline** (Smith MT, McCrae CS, Cheung J, et al. *J Clin Sleep Med.*
2018;14(7):1231-1237. DOI 10.5664/jcsm.7230, PMID 29991437; `smith2018.yaml`). All seven recommendations
are **Conditional** ("We suggest"), none is Strong. The two that apply here, verbatim:

> "We suggest that clinicians use actigraphy in the assessment of pediatric patients with circadian rhythm
> sleep-wake disorder. (Conditional)"
> "We suggest that clinicians use actigraphy to estimate total sleep time in adult patients with suspected
> insufficient sleep syndrome. (Conditional)"

**Duration.** The guideline's floor, verbatim: "The recommended duration of actigraphy recording is a
minimum of 72 hours to 14 consecutive days, in accordance with the Current Procedural Terminology (CPT)
coding requirements." The "7-14 days" figure that circulates appears in the guideline only as a Remark
under the pre-MSLT recommendation: "Actigraphy can be used for 7-14 days prior to the PSG/Multiple Sleep
Latency Test (MSLT) to assure adequate sleep time leading up to the testing."

**My recommendation: 14 consecutive days [judgement].** The 72-hour floor is a billing convention, not a
measurement standard, and a 3-day recording can contain zero or one free day — useless when the clinical
question is a weekday-versus-free-day contrast. 14 days captures two weekends. This aligns with two other
sources: Auger 2015 requires that CRSWD actigraphy include "both work/school and free days"
(`auger2015.yaml`), and ICSD-3's BIISS criteria state that where personal history or sleep logs are in
doubt "actigraphy should be performed, **preferably for at least two weeks**" (`mader2022.yaml`).

**Scope limitation.** The guideline covers only FDA-approved devices, verbatim: "only apply to the use of
FDA-approved devices." **Consumer wearables are out of scope** — see §7.

---

## 6. AASM clinical practice guideline for intrinsic circadian rhythm sleep-wake disorders

Auger RR, Burgess HJ, Emens JS, Deriy LV, Thomas SM, Sharkey KM. *J Clin Sleep Med.* 2015;11(10):1199-1236.
DOI 10.5664/jcsm.5100, PMID 26414986. (`auger2015.yaml`) Every DSWPD recommendation is **WEAK FOR**
(conditional); underlying evidence was LOW except the paediatric melatonin dosing study (MODERATE).

### 6.1 Melatonin — what the guideline actually says

**Children and adolescents with DSWPD, no comorbidity:**
> "5.2.6.2.1a The TF suggests that clinicians treat children and adolescents with DSWPD (and no
> comorbidities) with strategically timed melatonin (versus no treatment). [WEAK FOR]"
> "Optimal results were obtained with a dose of 0.15 mg/kg, taken 1.5-2.0 hours prior to habitual bedtime,
> for 6 nights."

**Do not scale 0.15 mg/kg to adult body mass.** The underlying RCT enrolled **6-12 year olds**, and the
actual mean administered dose in the 0.15 mg/kg arm was **4.4 ± 1.0 mg**. Naive mg/kg scaling to a 70 kg
19-year-old gives 10.5 mg, which is far above the doses that phase-shift effectively and is not supported
by the source data. Effects at that dose: actigraphic sleep onset advanced 42.8 min (95% CI 21.8-63.8) and
latency fell 43.8 min (95% CI 24.1-63.5) versus placebo.

**Adults with DSWPD (the relevant band for a 19-year-old):**
> "5.2.6.1a The TF suggests that clinicians treat DSWPD in adults with and without depression with
> strategically timed melatonin (versus no treatment). [WEAK FOR]"
> "Positive results were obtained with a 5 mg dose timed between 19:00-21:00 (no circadian-based timing),
> for a period of 28 days."
Effects in the non-depressed adult subset (n=12): PSG total sleep time +56.0 min (95% CI 48.5-63.5),
latency −37.7 min (95% CI −43.7 to −31.8).

**Adolescents with DSWPD plus psychiatric comorbidity:** fast-release melatonin **3 mg if <40 kg, 5 mg if
>40 kg**, at 18:00-19:00 for 4 weeks. DLMO advanced **54.2 min** (95% CI 31.7-76.8) and actigraphic sleep
onset **36.6 min** (95% CI 17.0-56.2). This is the only DSWPD arm in the guideline with a *physiological*
circadian outcome, and it is the strongest evidence that the mechanism is genuinely circadian.

**Timing dominates dose** — the most actionable point in the guideline:
> "the authors reported an inverse relationship between the timing of melatonin administration
> (irrespective of dose) and the magnitude of DLMO phase advance, such that earlier timing of the former
> (in relation to DLMO) resulted in greater phase advances."
> "a positive relationship between DLMO phase advances and an earlier circadian TOA was described (no
> relationship observed with respect to clock TOA), but no differences were observed between the various
> melatonin dosage groups."

**Practical synthesis [judgement]:** a low dose (0.5-5 mg) given several hours before habitual sleep onset
— ideally timed relative to estimated DLMO rather than to the clock — is what the evidence supports. The
guideline's own trials used clock timing and produced contradictory results; the dose-response signal is
flat and the timing signal is strong.

### 6.1b The randomised trial that post-dates the guideline — and what it changes

Sletten TL, Magee M, Murray JM, et al. Efficacy of melatonin with behavioural sleep-wake scheduling for
delayed sleep-wake phase disorder: A double-blind, randomised clinical trial. *PLoS Med.*
2018;15(6):e1002587. DOI 10.1371/journal.pmed.1002587, PMID 29912983. (`sletten2018.yaml`)
**Tier T1** — the strongest single piece of treatment evidence in this shard.

The authors' opening observation explains why this matters: *"Although there are published therapeutic
guidelines for the administration of melatonin for DSWPD, to our knowledge, randomised controlled trials
are lacking."* The AASM 2015 recommendation above was made without a trial of this design.

**The regimen exactly as tested** — this is what to quote if the report recommends melatonin:

| Element | As tested |
|---|---|
| Dose | **0.5 mg fast-release** melatonin |
| Timing | **1 hour before the patient's desired bedtime** |
| Frequency | ≥5 consecutive nights per week |
| Duration | 4 weeks |
| Co-intervention | **Behavioural sleep-wake scheduling** (bedtime scheduled at desired bedtime) in *both* arms |
| Population | n=116 outpatients, mean age 29.0 y (range 16-65), **DLMO-confirmed** phase delay |

**Results.** Actigraphic sleep onset **34 min earlier** (95% CI −60 to −8) vs placebo. Clinician-rated
marked improvement in **52.8% vs 24.0%** (P = 0.011) — RR 2.20 (95% CI 1.26-3.83), **NNT 3.5** [derived].
ISI fell 2.37 points more than placebo (95% CI −4.56 to −0.18). No serious adverse events; adverse-event
rates did not differ between arms.

**Two qualifications the report should carry.**

1. **It worked as a hypnotic, not as a clock-resetter.** Post-treatment DLMO was **not** significantly
   advanced (difference 0.49 h, 95% CI −0.20 to +1.18 h [derived]), and the authors conclude:
   *"Improvements were achieved largely through the sleep-promoting effects of melatonin, combined with
   behavioural sleep-wake scheduling."* **Do not tell the subject that 0.5 mg melatonin at bedtime "resets
   his body clock" on the strength of this trial.** If circadian phase advance is the goal, the guideline's
   earlier-timing logic (§6.1) and light therapy (§6.2) are the mechanisms with physiological support. The
   caveat on the caveat: the DLMO substudy had only n=43 of 116 and was underpowered.
2. **The effect is real but modest, and smaller than the behavioural/light option in adolescents.**
   34 min and NNT 3.5 here, versus a 55.9 min reduction in school-night sleep onset latency and NNT 1.4 for
   CBT + morning bright light in *adolescents* (`gradisar2011rct.yaml`). Different populations, outcomes and
   comparators, so I am not pooling them — but nothing in my evidence supports melatonin *ahead of*
   behavioural plus light therapy as first line for a 19-year-old.

Also note the trial estimates the **incremental** effect of melatonin *on top of* behavioural scheduling,
since both arms received it. The placebo arm still improved by 1.59 ISI points on scheduling alone.

### 6.2 Light therapy parameters

The guideline's adolescent recommendation is **WEAK FOR** for post-awakening light *plus behavioural
instructions*, and explicitly **NO RECOMMENDATION** for light monotherapy in adults. Parameters, verbatim:

> "Light therapy occurred via exposure to natural sunlight (when available), or with use of a white broad
> spectrum lamp (~1000 lux, proximity to source not specified), for >= 0.5 hours (2 hours maximum), with
> the time of administration advanced by 0.5 hours daily from 'natural' wake time, until a target time of
> 06:00 was reached. Light therapy was subsequently discontinued, and behavioral interventions ensued."

The trial behind that recommendation is `gradisar2011rct.yaml`, whose protocol section adds the operational
detail:

> "The light source was natural sunlight (when available); otherwise, a broad-spectrum light lamp was
> provided (~1,000 lux). Adolescents were instructed to begin light exposure at their natural wake-up time
> on day 1, with >= 30 min of light (max 2 h). ... Thereafter, they were instructed to begin light exposure
> 30 min earlier each day until they reached a target time of 06:00 ... After adolescents reached their
> target time, they ceased light therapy and attempted to maintain a regular rise time (06:30-07:30) ...
> Furthermore, they were instructed to go to bed when they felt sleepy and to avoid napping."

**Note the intensity: ~1,000 lux, not the 2,500-10,000 lux often quoted for light boxes.** The active
ingredient appears to be the *progressive 30-min-per-day advance of the wake and exposure time*, not
brightness. Effect: 87% of treated adolescents no longer met DSPD criteria versus 18% of waitlist
(χ² = 19.22, P < 0.0001; RR 0.16, **NNT 1.4**), school-night sleep +1.0 h (d = 0.81), school-night latency
78.1 → 22.2 min (d = 1.13).

### 6.3 What the guideline explicitly could NOT recommend for DSWPD

All verbatim, all "No recommendation":
- strategic **avoidance** of light — "There is insufficient evidence to support the use of strategic
  avoidance of light as a treatment for patients with DSWPD (versus no treatment). No recommendation."
- post-awakening light therapy **as monotherapy** — "There is insufficient evidence to support efficacy of
  post-awakening light therapy (monotherapy) as a treatment for DSWPD (versus no treatment)."
- **sleep-promoting medications** — "There is insufficient evidence to support the use of sleep-promoting
  medications as a treatment for patients with DSWPD (versus no treatment)."
- **wakefulness-promoting medications** — "There is no evidence to support the use of wakefulness-promoting
  medications as a treatment for patients with DSWPD."
- **vitamin B12** — "There is insufficient evidence to support the use of oral vitamin B12 (and no
  evidence to support alternate somatic interventions) among patients with DSWPD."

Blue-blocking glasses are mentioned only as indirect evidence in *insomnia* patients (<550 nm for the 3 h
before habitual bedtime), not as a DSWPD recommendation, though the guideline notes "there are no tangible
risks associated with these interventions."

### 6.4 Diagnostic requirement carried by the same guideline

> "the recommendation that CRSWD diagnoses are ascertained via actigraphy derived data when possible (with
> inclusion of both work/school and free days), to provide objective longitudinal documentation of
> sleep-wake patterns. Consistent with this emphasis on objective measures, circadian phase assessments
> (e.g., dim light melatonin onset, or DLMO) are also recommended, if feasible."

---

## 7. Consumer wearable validity for total sleep time

Three sources answer different halves of the question, and the two pooled estimates **disagree on the sign
of the bias**. The third explains why, so the disagreement is resolvable rather than something the report
has to hedge around: **device generation is the moderator** (§7.3).

### 7.1 Mean bias — pooled meta-analysis
Lee YJ, Lee JY, Cho JH, Kang YJ, Choi JH. Performance of consumer wrist-worn sleep tracking devices
compared to polysomnography: a meta-analysis. *J Clin Sleep Med.* 2025;21(3):573-582.
DOI 10.5664/jcsm.11460, PMID 39484805. (`lee2025.yaml`) 24 studies, n=798, random effects.

| Parameter | Pooled mean difference vs PSG | 95% CI | I² |
|---|---|---|---|
| **Total sleep time** | **−16.9 min** | −26.3 to −7.4 | 67.5% |
| Sleep efficiency | −4.7% | −7.1 to −2.3 | 84.1% |
| Sleep onset latency | +2.6 min | +0.6 to +4.5 | 57.9% |
| Wake after sleep onset | +13.3 min | +4.5 to +22.0 | — |

Subgroup: **Fitbit** showed no significant TST difference (−6.6 min, 95% CI −18.9 to +5.8) whereas
non-Fitbit devices did (−26.7 min, 95% CI −39.1 to −14.3). This meta-analysis reports **no limits of
agreement** and is **adults only**.

### 7.2 Limits of agreement — the independent head-to-head study
Chinoy ED, Cuellar JA, Huwa KE, et al. Performance of seven consumer sleep-tracking devices compared with
polysomnography. *Sleep.* 2021;44(5):zsaa291. DOI 10.1093/sleep/zsaa291, PMID 33378539. (`chinoy2021.yaml`)
n=34 healthy young adults (mean 28.1 y), 3 nights each including a disrupted-sleep night, PSG gold
standard, research actigraphy as an active comparator, **no device-company funding**.

| Device | n nights | TST bias (min) | Limits of agreement (min) | p | Hedges g |
|---|---|---|---|---|---|
| Actiwatch 2 (research actigraphy) | 98 | **+23.9** | −40.5 to +88.3 | <0.001 | 0.74 |
| Fatigue Science Readiband | 41 | +13.3 | −93.2 to +119.8 | 0.118 | 0.26 |
| **Fitbit Alta HR** | 49 | **+2.6** | **−42.0 to +47.1** | 0.421 | 0.09 |
| Garmin Fenix 5S | 29 | +43.7 | −47.0 to +134.4 | <0.001 | 1.07 |
| Garmin Vivosmart 3 | 43 | +46.8 | −39.5 to +133.1 | <0.001 | 1.28 |
| EarlySense Live | 51 | +13.6 | −45.1 to +72.3 | 0.002 | 0.42 |
| ResMed S+ | 51 | −0.3 | −70.7 to +70.2 | 0.953 | −0.01 |
| SleepScore Max | 42 | +7.5 | −60.7 to +75.7 | 0.162 | 0.17 |

Positive bias = device reports more sleep than PSG. Limits of agreement are two SD from the bias.

**Three findings that matter more than the headline numbers:**
1. **Research-grade actigraphy was MORE biased (+23.9 min) than the Fitbit (+2.6 min).** The objection
   "wearables aren't accurate enough" applies at least as forcefully to the AASM-endorsed clinical tool.
2. **Device choice dominates**: bias ranged −0.3 to +46.8 min across seven devices. A protocol that says
   "wear a wearable" without naming the device is not a protocol. Both sources independently identify
   Fitbit as among the least biased for TST.
3. **Accuracy degrades on short and disrupted nights** — exactly this subject's weekday nights — and the
   error runs towards *overstating* his sleep: "biases ... were generally the lowest magnitude and least
   variable when participants had higher TST and SE, and was generally more variable and biased on nights
   with lower TST and SE." Several devices showed statistically significant proportional bias.

**Epoch-level:** sensitivity to sleep is high (all ≥0.93) but specificity to wake is low (0.18-0.54).
Consequence: **a wearable cannot measure sleep onset latency**, which is the single most diagnostically
important variable in this differential. Latency must come from the diary.

**Post-processing is required:** the favourable figures above were obtained after the investigators
corrected device output to the true time-in-bed window. Raw app output without a concurrent diary will
perform worse.

### 7.3 Why §7.1 and §7.2 disagree: device generation is the moderator

Haghayegh S, Khoshnevis S, Smolensky MH, Diller KR, Castriotta RJ. Accuracy of Wristband Fitbit Models in
Assessing Sleep: Systematic Review and Meta-Analysis. *J Med Internet Res.* 2019;21(11):e16273.
DOI 10.2196/16273, PMID 31778122. (`haghayegh2019.yaml`) 3,085 records screened → 22 studies, 8 pooled.

This review stratifies by whether the device uses heart-rate variability for staging, and the two strata
behave completely differently:

| Parameter | Older, movement-only models | Current-generation, HRV sleep-staging models |
|---|---|---|
| **Total sleep time** | g = **−0.51** (95% CI −0.71 to −0.30), P<.001; overestimates by ~7-67 min | g = **−0.15** (95% CI −0.43 to 0.13), P=.29 — **no significant bias**; absolute bias **<12 min** |
| Wake after sleep onset | g = +0.60 (0.38 to 0.83), P<.001; underestimates by ~6-44 min | g = +0.16 (−0.12 to 0.44), P=.25 |
| **Sleep onset latency** | g = +0.12 (−0.14 to 0.39), P=.37 | g = **+0.32 (0.04 to 0.60), P=.03 — significantly UNDERestimates** |
| Specificity to wake | 0.10-0.52 | 0.58-0.69 |

Sign convention is the authors' own: *"A positive effect size infers lower values derived by Fitbit
relative to those derived by PSG."* So negative = device reports more sleep than PSG.

**This is the answer to "how accurate are current-generation wearables for total sleep time": absolute
bias under 12 minutes, which the authors call clinically negligible.** It also explains the apparent
contradiction above — Chinoy's +2.6 min for the Fitbit Alta HR and Lee's −6.6 min Fitbit subgroup are both
consistent with an unbiased current-generation device, while Lee's −26.7 min non-Fitbit subgroup and the
older movement-only literature are not measuring the same class of instrument.

**But note the caveat this record adds, which cuts against the most important measurement in the
protocol.** Current-generation devices *significantly underestimate sleep onset latency* (g = +0.32,
P = .03), and latency is the single highest-information variable in this differential (LR 0.21 to 3.40,
`screening_priors.md` §2.2b). A device that shortens the measured latency biases that test in the
**falsely reassuring** direction: a phase-delayed subject looks like a prompt sleeper. The mechanism is
the same low wake-specificity seen in Chinoy — quiet wakefulness before sleep onset is scored as sleep.

Two honest qualifications. First, Lee 2025 found the *opposite* sign for latency (+2.6 min, 95% CI +0.6
to +4.5 — devices reporting slightly *longer* latency), though the magnitude is clinically trivial. The two
pooled estimates disagree on direction, and **that disagreement is itself the argument for not taking
latency from a device at all** — it is not a quantity these instruments measure reliably in either
direction. Second, "current generation" in a 2019 review means Charge 2 / Alta HR era hardware; whether
2025-2026 devices have closed the wake-specificity gap is not established, and Lee 2025 (newer, broader)
still found a significant pooled TST underestimate across brands.

### 7.4 Recommended protocol statement [judgement]

> Current-generation consumer wrist wearables — those combining heart-rate variability with accelerometry
> — estimate *average* total sleep time to within about 12 minutes of polysomnography, with no
> statistically significant pooled bias; older movement-only devices overestimate sleep by 7-67 minutes and
> should not be used. Per-night 95% limits of agreement remain wide at roughly ±45 minutes even for the
> best-performing devices. They are therefore adequate for characterising average sleep duration and sleep
> timing over two or more weeks — averaging over 14 nights shrinks the random component of the per-night
> error by a factor of about √14 ≈ 3.7, and a sub-20-minute residual bias is small against the 2-3 hour
> weekday/weekend contrast being measured. They are **inadequate** for single-night estimates, sleep
> staging, and — most importantly here — **sleep onset latency**, which the two available meta-analyses
> cannot even agree on the direction of. Name the specific device in the protocol, and pair any wearable
> with a concurrent written diary recording lights-out, estimated sleep onset, and final wake time.

Useful reference standard carried in `lee2025.yaml`: "Sleep quality is generally considered good in all age
groups with 85% efficiency, 15-minute latency, and 20-minute wake after sleep onset, whereas poor sleep
quality is indicated by 74% efficiency."

---

## 8. Recommended measurement protocol, in order

| Step | Instrument | Threshold | Action if positive |
|---|---|---|---|
| 1 | **ISI** | **<7** rules out; **7-9** indeterminate; **≥10** positive | Insomnia phenotyping; ≥15 → consider CBT-I referral. Cannot separate insomnia from DSWPD (§2.2) |
| 2 | **ESS-CHAD** | >10 (adult threshold, unvalidated here) | Note as sleepiness severity; ≥16, or ≥12 persisting after 2-4 weeks of adequate sleep opportunity → sleep medicine referral |
| 3 | **CSRQ** | <28 rules out; ≥40 acts | ≥40 → clinically significant chronic sleep reduction |
| 4 | **Three single questions** | see below | highest information-per-minute in the protocol |
| 5 | **14-day sleep diary + actigraphy** (or a named current-generation wearable + diary), including 2 weekends | AASM Conditional; ICSD-3 "preferably at least two weeks" | supplies free-day sleep onset for MSFsc and objective TST. **Take sleep onset latency from the diary, not the device** (§7.3) |
| 6 | **MCTQ → MSFsc** | no cut-off; compare to age-19 male norm 05:02 ± 2.60 h | informs light/melatonin *timing*, not the diagnosis |
| 7 | **Trial of sleep extension** 2-4 weeks | resolution of sleepiness | confirms ICSD-3 BIISS criterion E; failure to resolve is the trigger for objective testing |
| 8 | PSG / home sleep apnoea test | only if sleepiness persists after step 7, **or** witnessed apnoeas / obesity | prior for symptomatic OSA in a lean 19-y-o male is ~1% |

**The three questions in step 4**, with their evidenced likelihood ratios for DSWPD:
1. "On a school/work night, how long does it take you to fall asleep after lights out?"
   → **LR 0.21 if ≤15 min; 2.04 if >60 min; 3.40 if >90 min**
2. "Do you oversleep — most days, or always?" → **LR+ 5.52**, LR− 0.76
3. "If you got into bed at 22:30 on a Tuesday and genuinely tried, could you fall asleep?"
   → a "yes" is close to an exclusion of DSWPD **[judgement — near-definitional for ICSD-3 criterion A]**

**Do not** compute a weekday-weekend sleep-duration difference and treat it as diagnostic: its likelihood
ratio is 1.1-1.4 and it is already known (`screening_priors.md` §2.2a).
