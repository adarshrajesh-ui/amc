# Station report — shard `s19_sleep_disorders`

**35 records included, 62 screened, 158 effect estimates, all validating against
`/workspace/spec/effect.schema.json`. 0 identifiers failed verification.**

---

## 1. The headline finding, and it is not what the brief expected

The brief proposed that the subject's pattern — 5-6 h weekday sleep, 7-8 h weekend, occasional 10-11 h, in a
16-19 year old male — is "also the classic presentation of delayed sleep-wake phase disorder", and asked me
to treat that as a priority. I did, and the evidence points the other way. **That pattern is the classic
presentation of being a teenager, and as a diagnostic test for DSWPD it is worth almost nothing.**

Three independent lines converge on a likelihood ratio near 1:

1. Adolescents with **clinically diagnosed** DSPD had a weekend-minus-weekday sleep gap of only **1.33 h**
   (`gradisar2011rct.yaml`). The subject's ~2 h gap is *larger than the diagnosed cases'*. A feature more
   extreme in the subject than in the disease group cannot be a strong positive test for that disease.
2. In n≈9,338 age-exact adolescents the DSPS-vs-non-DSPS difference in that gap was **0.60 h (SE 0.086)**
   (`sivertsen2013.yaml`) — a 36-minute mean separation against a ~1.5 h population SD.
3. A 2+ hour weekend delay with more weekend sleep is the **worldwide adolescent norm** across 41 surveys,
   and the meta-analysts themselves note it is "consistent with symptoms of Delayed Sleep Phase Disorder"
   (`gradisar2011meta.yaml`).

**Derived LR for a 2-hour weekday-weekend gap: 1.13** (cross-check against Sivertsen's means: 1.22).
Essentially uninformative. This is the single most useful thing my shard produces, because it stops the
report from making a confident circadian diagnosis on a feature that every healthy teenager shares.

## 2. Recommended posteriors

| Information state | DSWPD | Insomnia | OSA | **P(any intrinsic treatable disorder)** |
|---|---|---|---|---|
| **S0** Pattern only — current state | 1.9% | 18.4% | 0.8% | **21%** (12-32%) |
| **S1** Falls asleep ≤20 min weekday *and* free nights; function preserved | 0.1% | 1.6% | 1.0% | **3%** (1-7%) |
| **S2** >60 min latency every night incl. free nights; oversleeps | 35.6% | 47.4% | 0.3% | **83%** (70-92%) |
| **S3** >60 min weekday but sleeps normally at his late free-day time; oversleeps | **44.9%** | 15.5% | 0.6% | **61%** (45-75%) |

**Carry 21% (interval 12-32%) as the recommended posterior**, because S0 is the honest description of what is
currently known. Two things about that number matter more than its value:

- **Most of it is insomnia (18%), not DSWPD (2%)**, because the adolescent insomnia prior is roughly five
  times the DSWPD prior. DSWPD is a real possibility but is not the leading intrinsic candidate.
- **The most probable single explanation remains behaviourally imposed restriction** (~79% in S0).

The whole 2%→45% spread turns on **one question that has not been asked: how long does he take to fall
asleep on a weekday night?** LR 0.21 if ≤15 min, 3.40 if >90 min.

## 3. What I was asked for, and whether I got it

| Requirement | Status |
|---|---|
| DSWPD prevalence in adolescents/young adults, with CIs and criteria | **Delivered.** 5 estimates, 3 criteria sets (ICSD-R, ICSD-3, DSM-5). Prior adopted 4.0% (2.7-5.7%) |
| Delayed chronotype as distinct from the disorder | **Delivered.** Trait 8.4% vs disorder-with-impairment 5.7% in the same sample; plus single-year male norms |
| Saxvig, Sivertsen, Gradisar, AASM prevalence statements | **All found and extracted** |
| LR for "large weekday-weekend sleep discrepancy" | **Delivered: 1.1-1.4.** The brief's central hypothesis does not survive it |
| LR for long weekday sleep onset latency | **Delivered.** LR+ 1.27→3.40 across thresholds; **LR− 0.21** |
| LR for "can sleep normally when schedule permits" | **Partially.** 0.49-0.53 [derived]. The textbook version of this criterion is overstated — diagnosed DSPD adolescents still took 66 min to fall asleep on *free* nights |
| LR for difficulty waking | **Delivered: LR+ 5.52** from a directly measured ratio in 9,338 age-exact adolescents. Best dichotomous discriminator available |
| Insomnia prevalence (Hysing, Johnson, Ohayon, recent meta-analysis) | **All four delivered**, including the 2025 meta-analysis |
| OSA prevalence in lean males 18-25 | **Does not exist.** See §5 |
| BIISS ICSD-3 criteria verbatim | **Delivered**, all six criteria A-F |
| ESS original validation, normal range, cut-off, adolescent norms | **Delivered** — including the finding that Johns 1991 contains **no** cut-off, and that **no validated adolescent cut-off exists** |
| MCTQ MSFsc computation + 18-19 y norms | **Delivered.** Formula verbatim; male norms by single year of age |
| ISI cut-offs and validation | **Delivered, and improved on request** — two validations, one against a structured DSM-5 interview in young adults |
| Validated DSWPD screening tool | **None exists.** Documented as a finding, with the CSRQ as nearest substitute |
| Actigraphy + diary role per AASM | **Delivered.** 72 h minimum to 14 days; ICSD-3 "preferably at least two weeks" |
| AASM guideline melatonin dose/timing + light parameters | **Delivered verbatim**, plus the randomised trial that post-dates it |
| Consumer wearable bias and limits of agreement | **Delivered** from three sources, including the device-generation stratification that reconciles them |

## 4. Six findings that change what the report should say

1. **The weekday-weekend gap is diagnostically inert** (§1). Do not build a circadian argument on it.
2. **"Difficulty waking / oversleeping most days" is the question to ask instead.** LR+ 5.52, one item,
   measured directly in the right age band. Asymmetric though: presence multiplies odds by 5.5, absence
   divides by only 1.3.
3. **A normal Epworth score does not argue against DSWPD.** In the only DLMO-confirmed DSWPD sample I have
   (`sletten2018.yaml`), **84.5% of confirmed cases scored in the normal ESS range (0-9)**. An ESS screen
   would miss five in six cases. Its useful role is the reverse: because irrepressible sleepiness is a
   *required* BIISS criterion, an elevated ESS points toward insufficient sleep rather than a circadian
   disorder.
4. **The ISI cannot separate DSWPD from insomnia disorder.** Mean baseline ISI in confirmed DSWPD was
   **12.93** — above the ≥10 cut-off, inside the "subthreshold" band, with 16.4% scoring "insomnia absent".
   I had initially called the ISI the highest-information measurement in the protocol; that holds only for
   the insomnia-vs-no-insomnia question. Sleep *timing* adjudicates the differential, not a questionnaire
   score.
5. **Do not take sleep onset latency from a wearable.** Current-generation devices significantly
   *underestimate* it (`haghayegh2019.yaml`, g = 0.32, 95% CI 0.04-0.60, P = .03), and latency is the
   highest-information variable in the whole differential. The bias runs in the falsely-reassuring
   direction. Lee 2025 found the opposite sign, which is itself the argument: this is not a quantity these
   devices measure reliably in either direction. Take it from the diary; use the device for duration and
   timing only.
6. **Melatonin, as trialled, is a hypnotic rather than a clock-resetter.** In the one randomised trial
   (`sletten2018.yaml`, n=116, double-blind, DLMO-confirmed), 0.5 mg 1 h before desired bedtime advanced
   sleep onset 34 min (95% CI −60 to −8), NNT 3.5 — but post-treatment DLMO was **not** significantly
   advanced (0.49 h, 95% CI −0.20 to +1.18 [derived]). The authors attribute the benefit to
   "sleep-promoting effects ... combined with behavioural sleep-wake scheduling". The report should not tell
   the subject melatonin resets his body clock. Also: adolescent CBT + morning bright light has **NNT 1.4**
   versus melatonin's 3.5, so nothing here supports melatonin ahead of behavioural-plus-light first line.

## 5. What I could not find

**The specific number the task asked for — symptomatic OSA prevalence in lean males aged 18-25 — does not
exist in the literature I could reach.** This is a genuine gap, not a search failure. Benjafield 2019, named
in the brief, is **restricted to ages 30-69** and supplies nothing for this band; Peppard 2013 gives
BMI-stratified rates only for ages 30-49. My **1% (range 0.5-3%) is an explicitly flagged extrapolation**:
Peppard's 2.7% for AHI≥5 *plus* ESS>10 in lean men aged 30-49, discounted by a third to a half for age. It
must be presented as reasoning, not as an extracted value. Supporting context: Bixler's 10.6% adolescent
AHI≥5 incidence is a *polysomnographic finding*, not a disorder, scored by paediatric conventions that are
not interchangeable with adult thresholds — and childhood OSA remitted in **100%** of cases by adolescence,
so a childhood history is uninformative either way.

Also not found:
- **No validated DSWPD-specific screening instrument exists.** I searched for one specifically. The CSRQ is
  the nearest substitute and its own validation paper reports that adolescents with insomnia and with DSWPD
  score *identically* on it (t(294) = −0.60, P = 0.55).
- **No validated adolescent ESS cut-off.** The ESS-CHAD developers say so themselves.
- **No age-stratified insomnia prevalence for 16-25 y in the 2025 meta-analysis.** Its 47 contributing
  studies have mean ages of **37.0 to 84.3 years**. Its null age moderator (P = 0.98) therefore says nothing
  about our subject, and must not be used to justify applying its 12.4% figure to him.
- **No published likelihood ratios for any DSWPD diagnostic feature.** ICSD-3 criteria are qualitative. Every
  LR in `screening_priors.md` is my own derivation from published means, SDs and proportions, with the
  arithmetic recorded in each `conversion_formula` field.

## 6. Confidence

| Component | Confidence | Why |
|---|---|---|
| The weekday-weekend gap is a poor discriminator | **High** | Three independent lines converge; the direction is unambiguous |
| DSWPD prior 4.0% (2.7-5.7%) | **Moderate** | Five age-matched estimates, but all self-report and three share a Norwegian cohort family — not independent replications |
| Insomnia prior 18% | **Moderate-low** | The 2025 meta-analysis shows self-report runs ~1.3× interview-based. My 18% is more likely too **high** than too low; 13-15% would be defensible |
| BIISS prior 10% | **Moderate-high** | Two independent populations agree to within 0.5 pp (10.4% vs 9.9%) — unusual in this literature |
| OSA prior 1% | **Low** | Extrapolated across a 15-year age gap. Flagged as judgement |
| LR+ 5.52 for oversleeping | **Moderate-high** | Directly measured proportions, n≈9,338, age-exact |
| Latency LRs (0.21-3.40) | **Moderate** | Normal approximations to distributions from different studies/countries. Reassuringly, the comparator SD is over-determined: Sivertsen's 34-min difference and Hysing's 65%->30 min figure independently imply SD 37.4 min, against an observed 37.2 min in Gradisar's Australian cohort |
| Instrument cut-offs | **High for the numbers, low for their transportability** | The cut-offs are correctly sourced; almost none is validated in 18-19 year olds, and I have said so at every point |
| Posterior interval 12-32% | **Moderate** | Robust to the sensitivity analyses I ran (§3.2 of `screening_priors.md`), but the partition omits depression (§7) |

**One correction I made to my own analysis mid-way**, recorded because it affects how the numbers should be
read: I initially described the ISI as the single highest-information measurement in the protocol. After
extracting `sletten2018.yaml` I qualified that — it is the best instrument for the insomnia question but is
blind to the DSWPD/insomnia distinction. The posteriors in `screening_priors.md` §3.3 are labelled
accordingly.

## 7. The single biggest evidence gap in my domain

**There is no study that measures the diagnostic accuracy of any sleep questionnaire or reported feature
against an objective circadian standard (DLMO) in adolescents or young adults.**

Everything downstream of that absence is a workaround:

- Every DSWPD prevalence estimate I extracted (4 of 5 by questionnaire alone) is a prevalence of
  *self-reported symptoms consistent with DSWPD*, not of DLMO-confirmed circadian delay. All are likely to
  over-call, by an unknown factor.
- Every likelihood ratio in `screening_priors.md` is **my own construction** from published means and SDs,
  because no primary study reports sensitivity/specificity for any DSWPD feature. Their calibration is
  unverified.
- The one DLMO-confirmed DSWPD sample I found (`sletten2018.yaml`) had a mean age of **29.0 y** and reported
  no age-stratified results, so even the disease-present distributions of the ESS and ISI that I lean on come
  from adults.
- `jaakallio2026.yaml` shows how much this matters: it found that behavioural factors, not the physiological
  circadian markers it measured, predicted delayed-sleep-phase trajectories — implying that a meaningful
  share of adolescents labelled "delayed phase" by questionnaire may not have a circadian abnormality at all.

**Concretely, what is missing is a study that recruits 16-19 year olds with short weekday and long weekend
sleep, measures salivary DLMO plus 14 days of actigraphy and diary, and reports the sensitivity and
specificity of each candidate feature — weekday latency, free-night latency, oversleeping, weekend-weekday
gap — against DLMO-confirmed phase delay.** Until that exists, the DSWPD-versus-behavioural question in an
individual adolescent cannot be settled by questionnaire at any level of sophistication, and the honest
protocol is the 14-day diary plus a therapeutic trial of extended sleep opportunity, not a better
questionnaire.

**A second, narrower gap:** my five-branch partition (BIISS / DSWPD / insomnia / OSA / behavioural-only)
**omits depressive disorder**, which can generate the subject's entire phenotype on its own. The association
with DSWPD is large — Cohen's **d = 0.92 (95% CI 0.76-1.08)** across 16 studies (`dama2025.yaml`) — but
every component study is cross-sectional, so causal direction is unknown and reverse causation is fully
compatible with the data. I did not assign depression a prior because that base rate is outside my shard's
scope. The report should treat this as a named hole in the partition rather than an implicit zero, and should
include a mood screen alongside the circadian workup.

## 8. One lead I could not extract

`PMID 39879677` (*Sleep Med* 2025) is a randomised crossover trial of resistance versus aerobic exercise in
**male college students aged 18-28 with DSWPD** — the most population-exact record I encountered in the
entire search. I excluded it because the intervention was only 3 days, no washout is described, and the
abstract reports only P-values with no effect sizes, SDs or group sizes; nothing was extractable without
fabricating. If the report wants a low-cost adjunct to recommend, the full text is worth a look by a shard
with treatment remit.
