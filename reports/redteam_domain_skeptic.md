# Red-team review: DOMAIN SKEPTIC

**Scope.** The sleep science, not the code. I attack substantive claims: the exposure estimate, the
sleep-need parameter, the causal-fraction handling, the reassuring nulls, the alarming point
estimates, the omissions, and the subject-specific conclusions.

**Conventions used below.**

- Every citation carries a PMID I retrieved and read from PubMed in the course of this review. Where
  I state a number from a paper, I read it in that paper's abstract or in the project's own verified
  YAML record and say which.
- Where I am reasoning rather than citing, I write **[reasoning]**.
- Numbers labelled **[re-run]** come from my re-execution of the project's own engine
  (`src/exposure.py`, `src/recovery.py`, `src/synthesis.py`, `src/lifetable.py`) with one parameter
  changed at a time, 60k exposure draws resampled to 200k, same seed (20260728). They are the
  project's arithmetic, not mine.
- "The report" means `results.json` plus the shard summaries it draws on.

---

## PART A — The exposure and the sleep-need parameter

### 1. CRITICAL — `klerman2008`'s 8.9 h is a *maximal sleep capacity* measured with a 4-hour afternoon nap opportunity. It is being used as a nocturnal sleep requirement.

**Claim attacked.** `inferred_individual_sleep_need_at_19_h` = 8.70 h (95% CI 7.33–10.07), anchored
on "klerman2008 (16 h in bed, 8.9 h asymptote)" (`exposure_priors.md` §iv; `PRIORS["need_at_19_h"]`).

**Evidence.** Klerman EB, Dijk DJ. *Age-related reduction in the maximal capacity for sleep —
implications for insomnia.* Curr Biol 2008;18(15):1118–23. **PMID 18656358.** Three things in that
abstract destroy this use of the number:

1. The title and the authors' own summary sentence call the quantity **"the maximal capacity for
   sleep,"** not sleep need.
2. The protocol gave **"extended sleep opportunities covering 2/3 of the circadian cycle (12 hr at
   night and 4 hr in the afternoon)."** The 8.9 h is **total daily sleep including a four-hour
   afternoon nap opportunity.** It is not a nocturnal figure.
3. "Total daily sleep duration, which was **initially longer than habitual sleep duration, declined
   during the experiment**" over only 3–7 days. The asymptote had not demonstrably stabilised, and
   the direction of the residual trend is downward — exactly the debt-dissipation artefact the
   objection anticipates.

The project already knows point (2): `src/recovery.py` line 33 sets
`CEILING_NOCTURNAL_ONLY_H = 7.9` with the comment *"the last hour must come from a daytime nap."*
So the model simultaneously holds that the subject **needs 8.70 h** and that the **maximum sustained
nocturnal sleep is 7.9 h**. A requirement that exceeds the achievable nocturnal supply by 0.8 h is
not a requirement; it is a capacity ceiling measured under nap-permitting conditions, misapplied.

**Direction and magnitude.** The nocturnal-basis need is at most ~7.9 h, plausibly 7.5–8.0 h.
Substituting 7.9 h **[re-run]**: nightly deficit 3.20 → **2.40 h**; cumulative debt 3327 → **2495 h**;
vigilance g −0.88 → **−0.61**; required maintenance TIB 9.49 → **8.60 h**.

**Effect on the conclusion: substantially LESS alarming.**

---

### 2. CRITICAL — The exposure engine hard-floors sleep need at 8.0 h, so the ledger cannot represent the hypothesis that he needs less. The reported need interval is not the interval used.

**Claim attacked.** That the reported 95% CI on individual need (7.33–10.07 h) propagates into the
debt figure, and that the multiverse "disagree[s] about its size … driven entirely by the
self-report calibration choice rather than by uncertainty about sleep need" (`results.json`
→ `multiverse.note`).

**Evidence.** `src/exposure.py::need_curve` returns
`np.clip(a16 + (age−16)·(a19−a16)/3, 8.0, 9.5)`. I set `need_at_19_h` to 8.00, 7.50, 7.00 and 6.50
and checked the value the ledger actually uses **[re-run]**:

| `need_at_19_h` set to | value `need_curve` returns at 18.85 |
|---|---|
| 8.70 | 8.715 |
| 8.00 | 8.015 |
| 7.50 | **8.000** |
| 7.00 | **8.000** |
| 6.50 | **8.000** |

The population-mean requirement can never fall below 8.0 h. Meanwhile the *reported* quantity,
`individual_need_at_19_h`, is computed as `PRIORS["need_at_19_h"] + need_offset` and bypasses the
clip entirely. So the number the report prints as "inferred individual sleep need" is not the
number the deficit ledger consumes. Since every damage channel is a function of
(need − TST) × 1040 nights, an undisclosed floor on need is an undisclosed floor on damage.

The multiverse compounds this: all six branches hold need fixed. The claim that need uncertainty
does not matter is an artefact of never having varied it.

**Direction and magnitude.** With the floor removed **[re-run]**:

| need @19 | mean TST | nightly deficit | cumulative debt | vigilance g (95% CI) |
|---|---|---|---|---|
| 8.70 (published) | 5.59 | 3.20 h | 3327 h | −0.88 (−2.87, +0.57) |
| 8.00 (NSF midpoint) | 5.59 | 2.50 h | 2599 h | −0.64 (−2.30, +0.42) |
| 7.90 (model's own nocturnal ceiling) | 5.59 | 2.40 h | 2495 h | −0.61 (−2.22, +0.40) |
| 7.50 (the challenge value) | 5.59 | 2.00 h | 2079 h | −0.48 (−1.92, +0.33) |
| 7.50 + shard-recommended reverse calibration | 6.14 | 1.61 h | 1683 h | **−0.36 (−1.71, +0.25)** |
| 7.00 + reverse calibration | 6.14 | 1.11 h | 1163 h | **−0.21 (−1.37, +0.17)** |

Answering the question directly: **at need 7.5 h, 38% of the reported dose evaporates and 45% of the
headline vigilance deficit with it. At need 7.5 h combined with the calibration the project's own
measurement shard recommends, 49% of the debt and 59% of the vigilance deficit evaporate, and the
"large" effect becomes a small-to-moderate one.** The multiverse's stated spread ratio of 1.39 should
be roughly **2.9** once need is included as an axis.

**Effect on the conclusion: substantially LESS alarming, and the reported uncertainty is too narrow.**

---

### 3. MAJOR — The SD of individual need (0.70 h) is taken from an n=15 study while the mean is taken from a different study whose identical arithmetic implies an SD three times larger.

**Claim attacked.** `need_sd_individual_h = 0.70`, giving P(his need ≤ 7.5 h) ≈ 4.3% **[re-run]**.

**Evidence.** `exposure_priors.md` §iv derives 0.70 h from Kitamura et al, *Estimating individual
optimal sleep duration and potential sleep debt*, Sci Rep 2016;6:35812 (**PMID 27775095**): reported
8.41 ± 0.18 SEM, n=15, so SD = 0.18 × √15 = 0.697. Apply that same arithmetic to the study supplying
the *mean*: Klerman 2008 reports 8.9 ± 0.4 SEM in n=35 younger subjects (**PMID 18656358**), giving
SD = 0.4 × √35 = **2.37 h**. **[reasoning]** I do not believe 2.37 h is the true between-person SD of
sleep need — but the project cannot use one study's SEM-to-SD conversion for the SD while ignoring
what the same conversion says about its own primary anchor. A defensible prior spans roughly
0.7–1.4 h.

Independently: the NSF panel (Hirshkowitz et al, Sleep Health 2015;1(1):40–43, **PMID 29073412**)
gives 7–9 h as recommended for 18–25 and 6–11 h as "may be appropriate." A prior of N(8.70, 0.70)
places **0.6%** of its mass below 7 h. That is inconsistent with a guideline that calls 6 h
potentially appropriate.

**Direction and magnitude.** Widening to SD 1.10 h raises P(need ≤ 7.5) from 4.3% to **13.7%**
**[re-run]** and widens the vigilance interval to (−3.14, +0.57). Combined with objection 2 the
honest posterior on need is roughly **7.5–8.6 h**, not 8.7 ± 0.7.

**Effect: LESS alarming at the centre, and much wider.**

---

### 4. MAJOR — "Sleep need" is defined by the single most sleep-sensitive test in the battery and then used as the denominator for every unrelated outcome.

**Claim attacked.** A single scalar need of 8.70–9.00 h, sourced partly from `short2018`'s **9.35 h
"needed to maintain optimal sustained attention performance"**, then used to compute the deficit that
drives mortality, T2D, depression and IQ.

**Evidence.** Short MA et al, *Estimating adolescent sleep need using dose-response modeling*, Sleep
2018;41(4):zsy011, **PMID 29325109** — the abstract distinguishes "sleep need estimated from 10-hour
TIB sleep opportunities was approximately 9 hours" from "modeling PVT lapse data suggested that
**9.35 hours** of sleep is needed to maintain **optimal** sustained attention performance."

Decisively, the newest and largest dose-response study in the project's own corpus says the
requirement is measure-specific. Campbell IG et al, *Sleep restriction and age effects on distinct
aspects of cognition in adolescents*, Sleep 2024;47(12):zsae216, **PMID 39283917** (n=77 + 82, ages
9.9–22.8, 7 vs 8.5 vs 10 h TIB × 4 nights):

> "Restricting TIB to 7 hours was associated with impaired top-down attentional control and
> cognitive flexibility, but **performance did not differ between 8.5 and 10 hours of TIB
> conditions.** Psychomotor vigilance test performance decreased as TIB was restricted from 10 to
> 8.5 hours … **the minimal duration of sleep needed for optimal performance appears to differ
> depending on the cognitive measure.**"

So 8.5 h TIB (≈7.8 h TST on the project's own `banks2010` conversion) is indistinguishable from 10 h
TIB for attentional control, cognitive flexibility and working memory. Only the PVT keeps improving
past it. The project selected the PVT-optimality criterion — the most demanding one available — and
then applied the resulting hours-below-need to channels with no PVT-based dose-response whatsoever.

**Direction and magnitude.** For every non-vigilance channel the referent should be ~7.8–8.0 h TST,
not 8.7–9.0 h, removing **0.7–1.2 h of a 3.2 h deficit, i.e. 22–38% of the dose** for those channels
**[reasoning, using the project's own conversion]**. The vigilance channel keeps the higher referent.

**Effect: LESS alarming for mortality, metabolic, psychiatric and IQ; unchanged for vigilance.**

---

### 5. MAJOR — Two thirds of the exposure posterior sits on calibrations the project's own measurement shard forbids, and the resulting TST is a value the shard's key study says was never observed.

**Claim attacked.** `mean_actual_tst_over_exposure_h` = 5.59 h (95% CI 4.78–6.68).

**Evidence.** `exposure_priors.md` opens with a section headed "READ THIS FIRST" whose instruction is
unambiguous: **"Use the reverse regression. Do not subtract the mean bias."** The engine instead
draws uniformly among {naive mean-bias subtraction, reverse regression, none} in the TST branch, and
gives 50% of all draws to a TIB branch where `level_tib = report × efficiency` — a proportional
discount that behaves like the forbidden fixed subtraction and in which the calibration choice has no
effect at all (`multiverse` branches tib/naive, tib/reverse and tib/none return the identical
3508.65 h).

The empirical check the shard itself relies on is Girschik J et al, *Validation of self-reported
sleep against actigraphy*, J Epidemiol 2012;22(5):462–8, **PMID 22850546**, quoted in the shard as:

> "all participants who self-reported a usual sleep duration of 6 hours or less recorded an objective
> mean sleep duration of **greater than** 6 hours."

Under the TIB branch a 5.5 h report becomes 5.5 × 0.875 = **4.81 h** of sleep. That is squarely
inside the region Girschik reports as never having been observed in anyone reporting ≤6 h.

**Direction and magnitude.** Running the shard's own recommendation (reverse regression, TST
interpretation) **[re-run]**: mean TST 5.59 → **6.13 h**; debt 3327 → **2932 h**; vigilance g −0.88 →
**−0.74**. Fraction of nights below 6 h falls from 0.59 to **0.47**.

**Effect: LESS alarming.**

---

### 6. MAJOR — A sustained 3.2 h/night deficit for 1040 nights is not consistent with the observable facts about this subject, and the model's own dynamics say the "1040 nights" is rhetorical.

**Claim attacked.** "3.2 h nightly deficit for 1040 nights; cumulative debt 3329 h."

**Evidence and reasoning.**

*(a) The dose is more severe than the protocols it is compared to.* Van Dongen HPA et al, Sleep
2003;26(2):117–26, **PMID 12683469** ran 4 h and 6 h TIB for 14 days; Belenky G et al, J Sleep Res
2003;12(1):1–12, **PMID 12603781** ran 3/5/7 h for 7 days; Lo JC et al, Sleep 2016;39(3):687–98,
**PMID 26612392** ran 5 h TIB for 7 nights. **None ran longer than 14 days.** A person genuinely
running the model's dose for three years would be, in Van Dongen's terms, permanently at or past the
divergence region. **[reasoning]** The observable consequences of that state — falling asleep in
class daily, failing courses, crashing a car, an Epworth score in the pathological range — are not in
the case description, and he completed high school and a year of college.

*(b) The exposure is intermittent and every source protocol is continuous.* The subject sleeps 7–8 h
on weekends and, per the engine's own calendar, ~25–31% of the year at the weekend/holiday pattern.
`s09`'s annualised arithmetic makes the same point: the weekly average is 6.07–6.43 h, "roughly
**half** the deficit implied by looking only at weekdays — a distinction most of the source literature
does not make." The lab estimates transported into Q2 were measured with zero recovery nights.

*(c) His exposure is the statistical norm, not an outlier.* Wheaton AG et al, MMWR
2018;67(3):85–90, **PMID 29370154**: the project's own derivation from that instrument gives 20.1% of
US high-schoolers reporting ≤5 h and 43.0% reporting <7 h. `s15` quotes `ananth2026`: "fewer than 30%
of high school students obtaining the recommended 8–10 h." **[reasoning]** If a 3.2 h chronic deficit
produced the harms the report attaches to it, those harms would be a visible population-level
phenomenon in most of a generation.

*(d) The model's own dynamics say the 3329 h number is inert.* `PRIORS["tau_accrue_days"] = 7.0`,
sourced to Ramakrishnan S et al, *A Unified Model of Performance*, Sleep 2016;39(1):249–62,
**PMID 26518594**. With a 7-day accrual constant the state variable saturates in ~3 weeks. Three
years and three weeks of exposure produce the *same* current impairment in this model. So "3329 hours
of debt" is a description of exposure duration, not of damage, and the report's own
`ledger_is_not_a_schedule` section concedes as much — but the number is still the headline of Q1.

**Direction and magnitude.** The deficit should be reported as an *annualised* 1.5–2.4 h/night
**[re-run and s09]**, not 3.2 h, and the cumulative-hours figure should be demoted from a headline to
a footnote because the model itself gives it no causal role.

**Effect: LESS alarming, and materially changes what the report appears to be saying.**

---

## PART B — Confounding and residual causal fractions

### 7. MAJOR — The mortality channel uses the categorical hazard ratio its own shard explicitly forbids, and omits two of the four corrections that shard specifies.

**Claim attacked.** `life_expectancy_change_months_total` = −0.224 months; HR while exposed 1.027;
`cigarette_equivalent_per_day_for_3_years` = 2.48.

**Evidence.** `analysis_set.py` sets `mortality_rr_short_sleep = 1.12` (Cappuccio FP et al, Sleep
2010;33(5):585–92, **PMID 20469800**) and applies only correction (c), the residual causal fraction
[0, 0.50]. But the same dict already stores `dose_response_at_5h: 1.04` and
`dose_response_at_6h: 1.01`, and `s13/mortality_summary.md` §8.5 instruction 1 reads:

> "**Use the dose-specific spline values (RR 1.01–1.06 at 5–6 h), not the categorical 1.12–1.14.**"

with §1.3 stating "the categorical estimate is **3–11×** the dose-specific estimate at the subject's
actual dose," and §8.2 listing (a) dose retention 0.09–0.50 and (b) male-sex retention 0.2–1.0 as
separate multipliers from (c). The model applied (c) only.

**Direction and magnitude [re-run, project's own life table]:**

| mortality input | HR while exposed | window | permanent residue | **total** |
|---|---|---|---|---|
| categorical 1.12 (as published) | 1.0270 | −0.047 mo | −0.176 mo | **−0.224 mo** |
| dose-specific 1.035 @5–6 h | 1.0077 | −0.013 mo | −0.051 mo | **−0.065 mo** |
| dose-specific + male discount | 1.0040 | −0.007 mo | −0.027 mo | **−0.035 mo** |

The reported figure is **3.4–6.5× too large** on its own shard's instructions. The cigarette
equivalent falls from 2.48/day to about **0.4–0.7/day**.

**Effect: LESS alarming** — but see objection 15, which more than replaces it.

---

### 8. MINOR — The residual causal fraction of 0.25 for mortality is defensible and if anything generous; the CVD confounding survival of 0.20–0.50 is the stingier of the two.

**Claim attacked.** Whether 0.25 (mortality) and 0.20–0.50 (CVD) are generous or stingy.

**Evidence.** The E-value the report computes for RR 1.12 is 1.49. Depression, socioeconomic
position, undiagnosed illness and physical inactivity are all plausibly associated with both short
sleep and mortality at RR ≥ 1.5 **[reasoning]**, so an E-value of 1.49 means the association is fully
explainable by a single ordinary confounder. Against that, `s13` §5 reports 0–28% survival in
Mendelian randomisation. **A residual causal fraction whose central value is 0.25 when the MR ceiling
is 0.28 and the E-value is 1.49 is at the generous end, not the stingy end.** The uniform [0, 0.50]
prior is honest in shape.

The CVD figure (0.33, range 0.20–0.50) rests on UK Biobank staged adjustment (1.16 → 1.05 at 6 h;
1.52 → 1.19 at 5 h). **[reasoning]** Staged adjustment on measured covariates is an *upper* bound on
survival, because unmeasured confounding is by construction not removed. So 0.33 is also generous.

**Direction.** Both are, if anything, too generous — i.e. the report is already leaning slightly
alarmist here, which partially offsets objection 7. **Effect: negligible in magnitude.**

---

### 9. MINOR — The psychiatric channel is well handled and the non-causal share of 0.55–0.70 is if anything too low.

**Claim attacked.** `non_causal_share_of_observational_association` median 0.625; absolute excess MDE
risk 1.12 pp.

**Evidence.** `s12` documents that MR on *continuous* sleep duration is null in two independent
studies (OR 0.998), that the reverse arrow is present (MDD → sleep OR 0.92), that the causally
identified school-start-time effect loads **entirely** on the two fatigue items (−0.91) with mood
items null (−0.03, 95% CI −0.09 to 0.02), and that three of four sex-stratified studies find nothing
in males. **[reasoning]** If the forward MR is null and the identified quasi-experimental effect on
mood items is null, the non-causal share for *depressed mood specifically* is closer to 0.85–1.00
than 0.625, and the excess-MDE figure of ~1 pp should be reported as "plausibly zero" rather than as
a point estimate.

**Effect: LESS alarming.** The report's own text says this; its number does not.

---

## PART C — The reassuring findings

### 10. CRITICAL — The IQ answer is dragged toward zero by a 1999 between-groups total-deprivation study that had 80% power only for effects of about 11 IQ points, and whose noise happens to point the reassuring way. It carries 30% of the weight.

**Claim attacked.** `measured_full_scale_iq_change` median −0.70 points; and the text "binks1999
measured +3.6 points … and its interval excludes a decrement worse than about 1.8 points."

**Evidence.** Binks PG, Waters WF, Hurry M. *Short-term total sleep deprivations does not selectively
impair higher cortical functioning.* Sleep 1999;22(3):328–34, **PMID 10341383**. From the abstract:
"a group of **29 subjects** who underwent **34–36 hours** of continuous sleep deprivation and **32
normal sleeping control subjects** … **No significant group performance differences in the
hypothesized direction were noted on any measure.**"

Four separate problems, each sufficient on its own:

1. **Wrong exposure.** 34–36 h of *total* deprivation is not chronic partial restriction. Lim &
   Dinges, Psychol Bull 2010;136(3):375–89, **PMID 20438143** — the project's own source for the
   route-A discount — shows the domain profile differs between the two.
2. **Wrong design for the estimand.** It is a **parallel-group** comparison, not a repeated-measures
   IQ change. There is no within-person contrast, so a +3.6-point difference is fully consistent with
   baseline group imbalance in a 61-person study.
3. **No power.** With n=29 vs 32 the SE of *d* is 0.256, so the smallest effect detectable at 80%
   power (two-sided α = .05) is **d = 0.72** — about 8 points on the study's own scale, ~11
   population IQ points **[re-run]**. It cannot address a 1–3 point effect. The report's claim that
   its interval "excludes a decrement worse than about 1.8 points" is a 95%-interval statement
   masquerading as an exclusion, and the stored SE of 2.768 implies a scale SD of 10.8, not the
   report's declared IQ_SD of 15; on a population IQ scale the lower bound is nearer **−3.9 points**.
4. **The study is demonstrably insensitive.** Its abstract reports no significant difference on
   *any* measure, including sustained attention — a domain where Lim & Dinges pool a large effect
   after total deprivation. A study that misses the most replicated finding in the field cannot then
   be used as the "decisive anchor" (`analysis_set.py`'s own words) for a null on IQ.

Route C's median is **+2.80** points (i.e. sleep deprivation *improving* IQ) and it holds 30% of the
mixture weight — the second largest. Dropping it and renormalising the remaining three routes moves
the answer from −0.70 to **−1.22 points** **[re-run]**.

**Direction and magnitude.** Route C should carry ≤5% weight or be reported as an uninformative
bound. The measured state deficit becomes roughly **−1.2 points (95% CI −7.4 to +1.4)**.

**Effect: MORE alarming.**

---

### 11. MAJOR — The corpus contains a 2024 randomised crossover in exactly the right age band that measured a 7.5-point fluid-cognition drop, and it is excluded from the IQ answer while the 1999 adult null is included.

**Claim attacked.** The Q2 note that "the age-matched randomised tests of working memory and of
higher-order cognition in healthy-weight adolescents returned nulls," used to justify the small IQ
answer; and `analysis_set.py`'s `applies_to_subject: False` on `duraccio2024`.

**Evidence.** Stager LM, Watson CS, Cook EW 3rd, Fobian AD. *Effect of Sleep Restriction on
Adolescent Cognition by Adiposity: A Randomized Crossover Trial.* JAMA Neurol 2024;81(7):712–21,
**PMID 38767872**. n=61 (31 healthy weight, 30 overweight/obese), ages 14–19, actigraphy-confirmed,
restricted 4 h 12 min vs adequate 8 h 54 min. In the overweight arm, on NIH Toolbox standardised
scores (mean 100, SD 15): global cognition 103.2 → 98.0, **fluid cognition 102.0 → 94.5**, cognitive
flexibility 92.8 → 84.8. "No differences emerged for adolescents with healthy weight."

**[reasoning]** The healthy-weight "null" has **n=31** and **no published effect size or interval** —
the project's own `analysis_set.py` records `healthy_weight_arm: "null, no numeric estimate
published."` A paired design at n=31 has 80% power only for d_z ≈ 0.52. So this is not a null; it is
a failure to replicate in a subgroup of the same size as the one where the effect appeared. The
honest reading is: one night of 4 h sleep cost adolescents roughly 5 global and 7.5 fluid points,
with an adiposity interaction on n=61 that needs replication. Instead the model excluded the positive
result as subgroup-specific and admitted a 1999 adult between-groups null as decisive.

Compounding it, the model's other "age-matched higher-order null" is Campbell 2024 (**PMID
39283917**) — but that study found **impaired top-down attentional control and cognitive flexibility
at 7 h TIB**, a dose *milder* than the subject's. Only the Sternberg working-memory measure was null,
and that is the single measure the analysis set selected.

**Direction and magnitude.** Higher-order cognition should be modelled as impaired at the subject's
dose, not null. **[reasoning]** A defensible state-deficit estimate on standardised cognitive scores
is 3–7 points at his weekday dose, rather than the reported −0.70.

**Effect: MORE alarming.**

---

### 12. CRITICAL — The "permanent IQ change indistinguishable from zero" result is a structural artefact: permanence is modelled only as a fraction of the current state deficit, so the hypothesis of interest cannot be represented.

**Claim attacked.** `permanent_change_in_adult_cognitive_ability_points` = −0.02 (95% CI −0.54 to
+0.57); `prob_permanent_loss_exceeds_1_point` = 0.0061.

**Evidence.** `model.py`: `iq_permanent = iq_measured_now * perm_frac` with
`perm_frac ~ Beta(1.2, 18)`, mean 0.0625, support [0, 1].

Three consequences **[reasoning]**:

1. The permanent loss can never exceed the *current, reversible state deficit*. But the claim under
   examination is that three years of restriction during a developmental window altered a
   trajectory. That hypothesis predicts a durable change **even if the state deficit resolves
   completely** — for example, less material encoded (see objection 17), a lower academic
   trajectory, or altered maturation. The model has no term capable of expressing it.
2. Because permanence is proportional to the state estimate, the near-zero permanent answer inherits
   the near-zero measured answer, which objection 10 shows is itself an artefact of `binks1999`.
   The two "reassuring" findings are not independent; the second is 6% of the first.
3. `perm_frac`'s mean of 0.0625 is justified by reference to `P(detectable permanent structural
   change) ≈ 0.03`. **A probability that a structural change is detectable on MRI is not the
   fraction of a cognitive deficit that persists.** These are different quantities on different
   scales.

**Direction and magnitude.** `prob_permanent_loss_exceeds_1_point = 0.006` should not be reported.
The channel is *unidentified*, not near-zero, and the honest statement is the one `s03`'s station
report already makes about long-run accumulation: "entirely unidentified."

**Effect: MORE alarming**, in the sense that a false precision is being used to close a question the
evidence leaves open.

---

### 13. MAJOR — "Every immune marker normalised given adequate recovery sleep" is contradicted by three records in the project's own immune shard, including the one that best matches the subject's actual weekly pattern.

**Claim attacked.** Q4 `immune_infection`: "every marker normalised given adequate recovery sleep,"
`irreversible_probability: 0.02`; and `inflammation_crp_il6` `irreversible_probability: 0.02`.

**Evidence** (all from `s10/immune_summary.md` §4(b)–(c), records verified):

- Simpson NS et al, *Repeating patterns of sleep restriction and recovery: do we get used to it?*
  Brain Behav Immun 2016, **PMID 27263430**. n=14, **three weeks of 5 × 4 h + 2 × 8 h** — the shard
  itself calls this "the closest experimental model of the subject's actual pattern." Monocyte IL-6
  was **still elevated after recovery sleep** at week 2 (p<0.05) and week 3 (p<0.09).
- van Leeuwen et al (in-corpus): serum CRP 145% of baseline after restriction and **231% after
  recovery** — higher after the weekend than during the exposure. PBMC IL-6/IL-1β/TNF-α "did not
  return to baseline levels completely."
- Faraut B et al, Brain Behav Immun 2011;25(1), **PMID 20699115**: the abnormality that **persisted
  after 8 h** of recovery resolved only after **10 h, or a nap plus 8 h**. The shard's own conclusion:
  "For this subject — 7–8 h weekends with occasional 10–11 h nights — the prediction is
  **incomplete weekly normalisation on ordinary weekends**."
- Lange T et al, *Sleep after vaccination boosts immunological memory*, J Immunol 2011;187(1):283–90,
  **PMID 21632713**: the antigen-specific advantage was **still detectable one year later**, and three
  deprived participants **never reached seroprotection** and required re-vaccination.

**Direction and magnitude.** "Fully reversible" is wrong. The correct statement is: reversible given
10 h recovery nights, **incompletely reversible on his actual 7–8 h weekends**, with one genuinely
durable compartment (vaccination-timed immunological memory). P(irreversible) should be raised from
0.02 to roughly **0.10–0.25**, and the report should carry an actionable recommendation the current
version lacks: **do not be sleep-restricted in the two nights before any vaccination.**

**Effect: MORE alarming, and adds a cheap, concrete action.**

---

### 14. MAJOR — P(permanent brain structural change) = 0.03 is a product of five subjective probabilities, one of which is a measurement-sensitivity term that has no business being there, and its stated arithmetic does not tie out.

**Claim attacked.** `brain_structure: {value: 0.03, interval: [0.01, 0.10]}`.

**Evidence.** `s15/structure_summary.md` §7 gives the chain: P(difference exists) 0.75 ×
P(causal) 0.20 × P(permanent) 0.20 × P(detectable in this individual) 0.15, described as producing
"≈0.03." That product is **0.0045**, not 0.03. The stated 0.03 is the product of the first three
terms. The derived "P(functionally meaningful) ≈ 0.01" does not follow from either reading.

Three substantive problems **[reasoning]**:

1. **Step 4 answers the wrong question.** Whether an MRI could detect the change is epistemology;
   whether the change occurred is ontology. Including a 0.15 detectability factor deflates the
   damage-existence probability by 6.7×. The report is asked whether damage occurred.
2. **Conditional independence is false, and the error has a sign.** If a real causal effect exists,
   it is *more* likely to be permanent and *more* likely to be detectable. Positively correlated
   steps mean the product understates the joint. A correlated chain plausibly yields 0.10–0.15.
3. **P(causal) = 0.20 rests on Mendelian randomisation that instruments lifelong average habitual
   duration in middle-aged adults.** `s09` states this limitation explicitly for its own MR
   evidence: "a null MR does not exclude a real effect of a discrete 3-year episode." The same
   caveat applies here and is not applied.
4. **P(permanent) = 0.20 is anchored on acute-recovery studies.** `bernardi2016`'s 100% reversal
   follows *one night* of deprivation. **[reasoning]** An acute-reversibility finding cannot bound
   the permanence of a three-year developmental exposure.

The shard also handled Yang FN, Xie W, Wang Z, Lancet Child Adolesc Health 2022;6(10):705–12,
**PMID 35914537** (ABCD, n=8,323, propensity-matched on 11 covariates) with a genuinely good argument
— that an effect-size-map correlation of r=0.61 for grey matter volume across two years demonstrates
*stability*, not *progression*, and is equally consistent with a pre-existing trait. I accept that
argument. But the same paper reports that "structural properties of the anterior temporal lobe
mediate the effect of insufficient sleep on **crystallised intelligence**," which is in direct tension
with the report's Q3 claim of "no detectable decrement" in crystallised FSIQ — and that finding is
not addressed anywhere.

**Direction and magnitude.** The reported quantity should be relabelled
P(*MRI-detectable* permanent change) ≈ 0.03, and P(any permanent sleep-attributable structural
change occurred) should be reported as **0.10–0.20, poorly identified**. The `interval: [0.01, 0.10]`
conveys precision the underlying triple-product of judgements cannot support.

**Effect: MORE alarming, chiefly through removing false precision.**

---

### 15. MINOR — Two reassuring findings are sound and I could not break them.

In fairness, and to calibrate the rest of this review:

- **Final adult height (0.0 cm, interval 0–0.7).** `s11`'s argument is that growth plates close at
  16–17 and the exposure began at 16, and that 24-h GH output is redistributed rather than lost. That
  is mechanistically correct and the arithmetic ceiling of 3.65 cm is properly labelled as a ceiling.
  **No correction needed.**
- **Dementia declared INSUFFICIENT EVIDENCE and excluded from the total.** This is the right call,
  correctly reasoned (youngest exposure measurement age 50.6; eight MR analyses null; short-sleep-to-AD
  meta-analytic RR 1.02, 0.76–1.36), and the `amyloid_note` dismantling the mouse-glymphatic-to-PET-to-
  hazard-ratio chain is the best paragraph in the report. **No correction needed.** The only caveat is
  that `s14`'s own station report concedes its key negative — a multi-night biomarker null at n=13 — is
  underpowered, so "not quantifiable" should not drift into "no risk."

---

## PART D — The alarming findings

### 16. MAJOR — The vigilance point estimate of g ≈ −0.87 is being read as a measurement when its own interval spans "no deficit" and "pathological," and it is transported from continuous protocols in non-habitual short sleepers.

**Claim attacked.** `vigilance_g_at_subject_dose` median −0.874 (95% CI **−2.847 to +0.580**).

**Evidence.**

1. **The interval includes zero and positive values.** Reporting a median from a distribution with
   7.5% of its mass above zero as an alarming finding, without foregrounding that the same
   distribution's lower bound (−2.85) corresponds to gross pathological sleepiness, presents a
   prediction interval as an estimate. **[reasoning]**
2. **k=5, I² = 78.8%, and the bias diagnostics point the other way.** The report's own PET estimate
   is **−0.243** and trim-and-fill gives **−0.691** against an unadjusted −0.967. Neither adjusted
   value is used downstream; the unadjusted predictive distribution is.
3. **The source populations were not habitual short sleepers.** Lo JC et al, Sleep
   2016;39(3):687–98, **PMID 26612392** states its participants "studied in top high schools and were
   **not habitual short sleepers**." So the pooled effect measures the response of a rested adolescent
   dropped acutely to 5 h TIB. Whether that transports to someone three years into 5–6 h is the
   central unanswered question, and Horne JA, Wilkinson S, Psychophysiology 1985;22(1):69–78,
   **PMID 3975321** is in the literature precisely because practice and adaptation effects complicate
   it.
4. **Part of the source effect is a control-group practice gain, not a decrement.** Lo 2016's
   abstract: "Incremental improvement in speed of processing, **as a result of repeated testing and
   learning**, was observed in the control group but was attenuated in the sleep-restricted
   participants." **[reasoning]** In a parallel-group design the end-of-protocol difference is
   (control gain) + (restricted decrement). The subject has no control-group practice contrast, so
   that component does not transfer.
5. **Same-study reuse.** `pejovic2013` (**PMID 23941878**, n=30) supplies one of the five vigilance
   effects *and* one of the two `residual_deficit_after_recovery_sleep` effects. The report then
   presents "current deficit" and "recovery is incomplete" as separate findings.

**Direction and magnitude.** After correcting only the need parameter and the calibration
(objections 1, 2, 5) the same machinery returns **g ≈ −0.36 to −0.61** **[re-run]**. Applying the
report's own trim-and-fill or PET adjustment on top would reduce it further. The defensible headline
is a **small-to-moderate** vigilance deficit, not a large one.

**Effect: LESS alarming.**

---

### 17. MAJOR — `cousins2018` is over-read. It shows that material learned while restricted is less well retained; it does not show that his encoding capacity is now impaired.

**Claim attacked.** `encoding_capacity_g_persisting_after_recovery_sleep` = −0.886, labelled in
`analysis_set.py` as "Encoding capacity measured AFTER recovery sleep … This is the learning-loss
channel," and in `results.json` as "persisting."

**Evidence.** Cousins JN, Sasmita K, Chee MWL. *Memory encoding is impaired after multiple nights of
partial sleep restriction.* J Sleep Res 2018;27(1):138–45, **PMID 28677325**. The sequence in the
abstract is: 2 baseline nights at 9 h TIB → **5 consecutive nights of 5 h TIB** → "Participants
**then** performed a picture-encoding task" → recognition tested after 3 nights of 9 h recovery.

So **encoding happened while the participants were still restricted.** What persists is the memory
trace, not the impairment. The study establishes that learning done during a restricted period is
retained ~0.89 SD worse. It says nothing about whether encoding capacity remains depressed once sleep
normalises — the design cannot address that, because no post-recovery encoding session exists. The
word "persisting" in the parameter name and in the results key is doing work the study does not
support.

Four further limitations:

- **k = 1.** The reported 95% CI (−2.98 to +1.25) comes from imposing a half-normal τ prior of 0.656
  on a *single* study, i.e. inventing between-study heterogeneity. The interval includes "better than
  controls."
- **Effect size back-computed from a P-value.** The project's own YAML: "Back-computed from the
  reported P and group sizes … Two-tailed P = 0.001 at df = 57." Access is `abstract_only`; no means
  or SDs.
- **Parallel groups, n = 29 vs 30, single site, single task** (picture recognition), Singaporean
  boarding school.
- **Not dose-adjusted.** Unlike vigilance, this parameter is *not* multiplied by `transport` in
  `model.py`. It is reported at Cousins's 5 h-vs-9 h contrast (≈4.9 h deficit) and applied to a
  subject the model itself assigns a 0.85 transport factor. Applying the same adjustment used for
  vigilance would give **g ≈ −0.75**, and with the corrections in objections 1–5, **≈ −0.35 to −0.45**.

**Direction and magnitude.** The channel is real and important, but it should be reported as
**"material he learned during those three years is retained roughly 0.4–0.9 SD worse than it would
have been"** — a fixed historical loss — and **not** as a current, persisting capacity deficit.

**Effect: the number gets SMALLER and the interpretation changes materially. This is the single most
consequential mislabelling in the report**, because "his ability to learn is impaired" and "some of
what he learned is thinner than it should be" imply completely different prescriptions.

---

### 18. MINOR — The subjective/objective dissociation claim holds at 6 h, but the cited evidence for it is thinner than the report implies.

**Claim attacked.** The general claim that he cannot feel his own impairment.

**Evidence.** The strongest support at a dose close to his is Pejovic S et al, Am J Physiol
Endocrinol Metab 2013;305(7):E890–6, **PMID 23941878**: **6 h × 6 nights**, then two 10 h recovery
nights — IL-6 and *sleepiness* fully normalised while objective PVT performance **did not improve**
(`s10` §4(d)). Simpson 2016 (**PMID 27263430**) adds, at the 5×4 h + 2×8 h pattern, "Sleep restriction
was **not perceived to be subjectively stressful**" while physiology stayed activated. Lo 2016
(**PMID 26612392**) is the counterweight at 5 h: subjective sleepiness *did* rise and, like sustained
attention, had not returned to baseline after 2 recovery nights — i.e. at 5 h the two track each
other rather than dissociate.

**Direction.** The dissociation is best evidenced **during recovery** (subjective recovers first) and
at **6 h** doses, not as a general "he cannot tell how impaired he is at 5–6 h." **[reasoning]** The
report should narrow the claim to: *feeling recovered after a good weekend is not evidence of having
recovered.* That version is well supported and clinically useful. **Effect: neutral; sharpens rather
than moves.**

---

## PART E — What is missing

### 19. CRITICAL — Drowsy-driving and injury mortality is absent, and on plausible assumptions it is larger than the entire mortality estimate the report does produce.

**Claim attacked.** That Q6/Q7 characterise this exposure's mortality burden. `s13`'s station report
flags this itself: drowsy driving is "**completely absent from every study in this shard**" and is
"my domain's biggest blind spot." Nothing downstream picks it up.

**Evidence.**

- **Dose-matched risk.** Tefft BC. *Acute sleep deprivation and culpable motor vehicle crash
  involvement.* Sleep 2018;41(10):zsy144, **PMID 30239905**. n=6,845 drivers in a representative
  DOT-investigated crash sample. Relative to 7–9 h in the prior 24 h, odds of culpable crash
  involvement were **1.3 (1.04–1.7) at 6 h, 1.9 (1.1–3.2) at 5 h, 2.9 (1.4–6.2) at 4 h, and 15.1
  (4.2–54.4) below 4 h.** The paper notes these approximate incidence rate ratios per unit time
  driving. The subject sits at 5–6 h routinely and 3–4 h on exam nights.
- **Age-exact quasi-experimental support**, which no other mortality channel in this report has.
  Danner F, Phillips B. *Adolescent sleep, school start times, and teen motor vehicle crashes.* J Clin
  Sleep Med 2008;4(6):533–5, **PMID 19110880**: a 1-hour start delay was followed by a **16.5% drop**
  in county teen crash rates while the rest of the state **rose 7.8%**. Vorona RD et al. J Clin Sleep
  Med 2011;7(2):145–51, **PMID 21509328**: adjacent demographically similar cities differing by 75–80
  min in start time had teen crash rates of **65.8 vs 46.6 per 1,000** (2008) and 71.2 vs 55.6 (2007).

**Direction and magnitude [re-run, using the project's own `p_die_16_19 = 0.00248` and 58 years
lost per death].** Motor-vehicle crash accounts for roughly 18–32% of deaths in this age-sex band;
assuming 40–70% of his driving occurs on <7 h sleep and applying Tefft's 1.3–2.9:

| assumption | excess P(death) over 3 y | LE months lost |
|---|---|---|
| MVC 25%, OR 1.3, 70% of driving restricted | 0.000130 | **0.09** |
| MVC 25%, OR 1.9, 70% of driving restricted | 0.000391 | **0.27** |
| MVC 25%, OR 2.9, 70% of driving restricted | 0.000825 | **0.57** |
| full grid | — | **0.04 – 0.74** |

Against the report's **total** mortality figure of 0.224 months — and against the dose-corrected
figure of 0.065 months from objection 7 — **the omitted crash channel is between 0.6× and 11× the
size of everything the report counted.** It also inverts the composition of the answer: the dominant
mortality pathway for a 16–19-year-old male is acute crash risk *during* the exposure, not a
speculative lifelong cardiometabolic residue. And unlike the residue term, it is actionable tonight.

**Caveat.** His driving exposure is unknown. If he does not drive, this channel is zero. That is a
question the report should have asked and did not.

**Effect: MORE alarming, and it changes the prescription. The single most important omission.**

---

### 20. MAJOR — "Slow-wave sleep is preserved" is a stage-scoring artefact and the report's own Q4 verdict overstates it. But it does not rescue 5–6 h nights either.

**Claim attacked.** Q4 `growth_hormone` verdict: "slow-wave sleep is **preserved (indeed slightly
increased)** under restriction while stage 2 and REM absorb the loss." And, more broadly, the
proposition put to me that SWS preservation means 5–6 h nights are far less damaging than an
hours-below-need ledger implies.

**Evidence — both sides.**

*For preservation:* Brunner DP, Dijk DJ, Tobler I, Borbély AA. Electroencephalogr Clin Neurophysiol
1990;75(6):492–9, **PMID 1693894**. Sleep restricted to the first 4 h of habitual bedtime for 2
nights from a 7.5 h baseline (a ~3.5 h deficit, close to the subject's modelled dose): "stages 1 and 2
and REM sleep were reduced, while **slow wave sleep (SWS; stages 3 and 4) was not significantly
affected.**"

*Against:* the very next sentence of the same abstract: "**However, the time integral of EEG power
density in the range of 0.75–4.5 Hz (slow wave energy) was reduced.**" Stage minutes were preserved;
the physiologically meaningful quantity was not.

*And against, more strongly:* Åkerstedt T, Kecklund G, Ingre M, Lekander M, Axelsson J. *Sleep
homeostasis during repeated sleep restriction and recovery: support from EEG dynamics.* Sleep
2009;32(2):217–22, **PMID
19238809**. 4 h across 5 days: "**All sleep stages** and the latencies to sleep and slow wave sleep
(SWS) **showed a significant reduction during PSD.**" What was preserved and dose-responsive was SWS
and low-frequency power **within the first 4 h** — intensity per unit time, not total.

**[reasoning]** So the correct statement is: SWS *intensity* is defended and the first sleep cycle is
protected; total SWS and total slow-wave energy are not, and the protection weakens as restriction
deepens and lengthens. Two further reasons the argument cannot do the work asked of it:

1. The project's own `s03` shard already located the damage in **encoding**, not consolidation —
   "encoding capacity (learning new material) is impaired, not just consolidation of learned
   material." Encoding is a waking function. SWS preservation is irrelevant to it.
2. Vigilance, mood, and the metabolic and immune channels have no SWS-dependence at all.

**Direction and magnitude.** Q4's GH verdict should drop "(indeed slightly increased)" and note the
slow-wave-energy reduction. The SWS argument justifies at most a modest discount to the
*consolidation* sub-channel, which `s03` already prices as small. It does **not** justify a general
discount on the hours-below-need ledger.

**Effect: slightly MORE alarming on physiology, NEUTRAL overall — and it closes off what looked like
the report's best available reassurance.**

---

### 21. MAJOR — The academic/learning channel is parameterised and then never used. The single most consequential outcome for an 18-year-old student is not in the answers.

**Claim attacked.** The completeness of the damage accounting.

**Evidence.** `analysis_set.py::DERIVED_PARAMS` defines `academic_sd_per_hour_sleep` = 0.13
(interval80 0.02–0.30), sourced to `s04/causal_summary.md`, with the basis "Creswell 2023 +0.07
GPA/h; Groen & Pabilonia 0.26 SD/h; Heissel & Norris 0.081 SD per hour of bell time." I searched the
entire `src/` tree: the parameter appears **only** in its own definition and is referenced nowhere
else. `results.json` contains no academic outcome.

Supporting literature the project holds but does not answer with: Dewald JF et al, Sleep Med Rev
2010;14(3):179–89, **PMID 20093054**; Shochat T, Cohen-Zion M, Tzischinsky O, Sleep Med Rev
2014;18(1):75–87, **PMID 23806891**. `s04` also flags that effects are nonlinear below 6 h — the
region where the subject spends 47–59% of his nights.

**[reasoning]** For a subject one year into college, the concrete, measurable, life-affecting damage
is grades, course selection and credential trajectory. Objection 17 identifies the mechanism
(material encoded during restriction is retained worse); `s04` supplies the coefficient; the report
joins neither to the other. On a naive linear reading of 0.13 SD per hour at a 1.6–2.4 h annualised
deficit, the loss is **0.2–0.3 SD of academic achievement, or roughly 0.11–0.17 GPA points** —
labelled by `s04` itself as a large extrapolation from effects identified over 20–40 minute sleep
changes.

**Effect: MORE alarming, and it is the omission most likely to matter to the subject.**

---

### 22. MINOR — Other gaps, in descending order of consequence.

**[reasoning]** with sources named where they exist.

- **The dose-transport denominator is not re-derived when need changes.** `model.py` hard-codes
  `studied_deficit_h = 3.7`, but that figure is itself hours-below-need for the source protocols. If
  need is 7.9 h rather than 8.7 h, the source protocols' deficits shrink too. The subject's dose
  ratio is therefore not identified independently of the contested parameter, and my sensitivity runs
  overstate how much the vigilance estimate falls when need falls. The correction in objection 1
  should be read as an upper bound on the reduction.
- **The residual-deficit pooled estimate (g = −0.45) and the recovery model's non-recovering fraction
  (median 0.078) disagree by about 5×** and are both reported without reconciliation. The former is
  a one-to-two-night recovery measurement; the latter is an asymptote. They are different constructs
  presented as if compatible.
- **Caffeine is nowhere in the model.** A student sleeping 5–6 h almost certainly self-medicates.
  Caffeine is simultaneously a confounder of every association, a partial masker of the PVT deficit,
  and a cause of further sleep-onset delay. Its absence is not neutral: it biases the vigilance
  estimate in an unknown direction and it is the most obvious modifiable factor in the case.
- **Social jetlag is computed (1.75 h) and then not connected to anything.** `s12` identifies sleep
  *timing* as better supported than duration for this subject: Daghlas et al's MR gives OR 0.77 per
  hour-earlier sleep midpoint for MDD, a larger and cleaner effect than anything on the duration
  axis. The report prices duration and ignores timing.
- **Weekend catch-up is treated as nearly worthless.** The `weekday_5.5h_weekend_10h_catchup` policy
  reaches 28.7% recovery at week 52 versus 24.7% for status quo — a 4-point gain for 4.5 extra hours
  of sleep per week. `s09` §4 documents cross-sectional adolescent evidence pointing the other way
  (≥3 h catch-up: OR 0.67 for overweight, −0.18 BMI-z) and `s15` notes weekend catch-up was on the
  favourable side in the one age-matched longitudinal imaging study. The near-zero credit given to
  catch-up is an assumption of the recovery functional form, not a finding.

---

## PART F — The subject-specific conclusions

### 23. MAJOR — The 21% is a base rate wearing a posterior's clothes, and its composition is backwards: insomnia is over-weighted for definitional reasons and DSWPD is under-weighted by using the wrong conditional distribution.

**Claim attacked.** `screenable_disorder` = 0.21 (0.12–0.32), components insomnia 0.184, DSWPD 0.019,
OSA 0.008.

**Evidence.**

*(a) The DSWPD likelihood uses the general-population sleep distribution.* `s19/screening_priors.md`
§3 sets P(5–6 h weekday sleep | DSWPD) = 0.158, "derived: P(5<TST<6) given mean 7.02, SD 1.34
(Gradisar)" — i.e. Gradisar M, Gardner G, Dohnt H, Sleep Med 2011;12(2):110–8, **PMID 21257344**, the
*general adolescent* distribution. **[reasoning]** That is the wrong conditional. Short school-night
sleep is the *defining daytime consequence* of DSWPD: the patient cannot fall asleep until 01:00–02:00
and must rise for a 07:00 obligation. Using the population distribution makes his short weekday sleep
count as mild evidence *against* DSWPD (likelihood 0.158 vs 0.253 for behavioural restriction), when
it is a cardinal feature. On a DSWPD-specific school-night distribution centred near 5.5–6 h, the
likelihood would be ~0.35–0.40 and the posterior would rise 2–2.5× to roughly **4–5%**.

*(b) The DSWPD posterior of 1.9% sits below the unselected base rate for his sex and age.* Sivertsen
B et al, BMC Public Health 2013;13:1163, **PMID 24330358**, n=10,220 aged 16–18, ICSD-R criteria:
DSPS prevalence 3.3% overall, **2.7% in boys**. Saxvig IW et al, Sleep Med 2012;13(2):193–9, **PMID
22153780**, n=1,285 aged 16–19: delayed sleep phase 8.4%, and **5.7%** with a documented daytime
consequence. A subject who presents *with* the phenotype should not end up below the prevalence in
people who present with nothing.

*(c) The insomnia component violates the diagnostic criterion it is named after.* **[reasoning, from
diagnostic criteria]** Both DSM-5 insomnia disorder and ICSD-3 chronic insomnia disorder require that
the complaint occur **despite adequate opportunity for sleep** — ICSD-3 states the complaint "cannot
be explained purely by inadequate opportunity … for sleep." The subject's short sleep is, on the case
description, explained by inadequate opportunity. So conditioning on his reported pattern should
*reduce* the insomnia posterior. Instead the shard's likelihood ratio for insomnia relative to
behavioural restriction is 0.30/0.253 = 1.19, so the 18.4% posterior is essentially the 20% prior
carried through unchanged. **Reporting "18% probability of insomnia disorder" when no insomnia symptom
has been elicited is reporting a base rate.** The shard is transparent that its prior was chosen to be
"conservative in the direction of *over*-calling intrinsic disorder"; `results.json` drops that caveat.

*(d) The framing understates the actionable finding.* The shard classifies behaviourally induced
insufficient sleep syndrome (28.7%) as *not* an intrinsic treatable disorder. But ICSD-3 Insufficient
Sleep Syndrome is a coded diagnosis with a specific treatment, and it is the diagnosis that justifies
the entire prescription. **[reasoning]** On the shard's own numbers, P(a codeable ICSD-3 sleep
disorder) ≈ 21% + 29% ≈ **50%**. A reader given "21%" will hear "79% chance nothing is wrong."

**Direction and magnitude.** Recompose to roughly: **DSWPD 4–8%, insomnia disorder 5–10%, OSA ~1%,
insufficient sleep syndrome 30–45%.** And say plainly what the shard's own S1/S3 rows say: the answer
is dominated by **one unasked question** — how long does he take to fall asleep on a free night at his
own preferred bedtime? That single question moves P(intrinsic disorder) between 3% and 61%.

**Effect: MORE alarming on DSWPD, LESS on insomnia, and the headline number should be replaced by
"unresolved pending one question."**

---

### 24. MAJOR — The 9.5 h time-in-bed prescription is unattainable by the model's own parameters and exceeds the largest demonstrated behavioural sleep extension by 3–8×.

**Claim attacked.** `maintenance_dose_time_in_bed_h` = 9.50 h (95% CI 7.95–11.03).

**Evidence [re-run, project's own constants].**

1. **It breaches the model's own ceiling.** At 9.5 h TIB, `banks2010`'s regression (the project's own
   `TST_FROM_TIB_INTERCEPT = 0.237`, `SLOPE = 0.8915`) predicts **8.71 h of sleep** — above
   `CEILING_NOCTURNAL_ONLY_H = 7.9 h`, the value the project itself labels as requiring "the last
   hour … from a daytime nap." The prescription requires, indefinitely, a nocturnal sleep duration
   the model declares unattainable without a nap.
2. **The stated efficiency and the computed one disagree.** The note says "Sleep efficiency is
   ~87.5%," but 8.70/9.50 = 91.6%. At the stated 87.5% the required TIB is **9.94 h**, not 9.50 h.
3. **No behavioural intervention has ever delivered this.** Al Khatib HK et al, Am J Clin Nutr
   2018;107(1):43–53, **PMID 29381788** — "**+0:55 h in bed yielded only +0:21 h of actual sleep**
   (95% CI 0:06–0:36)," i.e. ~38% conversion. Blake MJ et al, Clin Child Fam Psychol Rev
   2017;20(3):227–49, **PMID 28331991** — meta-analysis of adolescent CBT-sleep trials, subjective TST
   improved by **29.47 min** (95% CI 17.18–41.75). The largest achieved gain in the corpus is Van Dyk
   TR et al, Sleep 2017;40(9):zsx123, **PMID 28934531**: adolescents habitually sleeping 5–7 h given
   +1.5 h TIB gained **+72.6 min/night** of actigraphic sleep (81% conversion — notably better than Al
   Khatib's adults, which is a point in the prescription's favour). The gap being prescribed is
   5.5 h → 9.5 h TIB, **+4.0 h**: 3.3× Van Dyk's achieved gain and 8× Blake's meta-analytic estimate.
4. **The population context.** Gradisar 2011 (**PMID 21257344**) puts adolescent school-night TST near
   7.0 h. The upper bound of the prescription (11.03 h TIB) would place a 19-year-old far into the
   distribution's tail.

**Direction and magnitude.** The prescription should be reframed as a **behavioural target of
8.5–9.0 h TIB on weeknights** — which by the project's own conversion yields 7.8–8.3 h of sleep and
is consistent with Campbell 2024's finding (**PMID 39283917**) that 8.5 h TIB is indistinguishable
from 10 h for everything except the PVT — plus an explicit **floor of 7.0 h TIB on the worst nights**,
which is where adherence is actually won. **[reasoning]** A 9.5 h prescription with an upper bound of
11 h will be read as unserious and discarded, taking the achievable part with it.

**Effect: the report's advice is currently unusable; this makes it usable without making the science
less alarming.**

---

### 25. MAJOR — The pessimism of the recovery projections is a direct arithmetic consequence of the contested need parameter, not of recovery physiology.

**Claim attacked.** "9 h every night recovers only 68% of the recoverable deficit at week 52"; "8 h
every night only 43%"; `non_recovering_residual_fraction` median 0.078.

**Evidence.** `recovery.py` sets a policy floor of `shortfall/(shortfall+1)` where
`shortfall = need − mean TST under the policy`. Recomputing that floor across need values
**[re-run]**:

| assumed need | 8 h every night → max recovery | 9 h every night → max recovery |
|---|---|---|
| **8.70 h (published)** | **42.9%** | **69.5%** |
| 8.00 h | 61.3% | **100%** |
| 7.90 h (model's own nocturnal ceiling) | 65.3% | **100%** |
| 7.50 h | 88.4% | **100%** |
| 7.00 h | 100% | 100% |

(The 42.9% and 69.5% reproduce the report's published 42.8% and 68.5% at week 52, confirming this is
the mechanism.)

**[reasoning]** So the report's central prognostic claim — that even nine hours a night for a full
year leaves a third of the deficit standing — is *entirely* an artefact of setting need at 8.70 h. At
8.0 h, the same code returns complete recovery on a 9 h schedule. Nothing about recovery kinetics
changed; only the denominator did. And 8.70 h is the parameter objection 1 shows to be a
nap-inclusive maximal-capacity asymptote.

**Direction and magnitude.** The correct statement is: **at 8.5–9 h TIB nightly, the model predicts
essentially complete functional recovery within 3–6 months**, with a genuinely uncertain small
residual. **Effect: substantially LESS alarming, and much better news for the subject.**

---

### 26. MINOR — The comparator ranking is fragile in both directions and the "2.5 cigarettes a day" headline should not be quoted.

**Claim attacked.** `rank_of_this_exposure: 1` of 8; `cigarette_equivalent_per_day_for_3_years: 2.48`.

**Evidence [re-run].** The rank rests on a total of 0.224 months. Objection 7 cuts that to 0.035–0.065
months; objection 19 adds 0.04–0.74 months. The corrected central total is roughly **0.15–0.65
months** — still rank 1 of 8, but the 80% interval now overlaps physical inactivity (0.8) and smoking
10/day (1.0). More importantly the *composition* flips from an unmeasurable lifelong residue to a
concrete, immediate, actionable crash risk. **[reasoning]** A cigarette-equivalent computed from a
quantity that moves by an order of magnitude under the report's own shard instructions should not be
in a summary. **Effect: NEUTRAL in rank; the headline number is not robust enough to publish.**

---

## The three substantive claims most likely to be wrong

**1. That his individual sleep need is 8.70 h (95% CI 7.33–10.07), and therefore that his nightly
deficit is 3.2 h.** The anchor is a study whose own title calls the quantity "the **maximal capacity
for sleep**" and whose 8.9 h figure includes a four-hour afternoon nap opportunity and was still
declining when the protocol ended (Klerman & Dijk, **PMID 18656358**). The project's own code
simultaneously caps sustained nocturnal sleep at 7.9 h. The engine additionally hard-floors need at
8.0 h, so the ledger cannot even express a lower value, and the multiverse never varies it.
Correcting to a nocturnal-basis 7.5–8.0 h removes **22–38% of the dose**, cuts the headline vigilance
deficit by **27–45%**, and — through the recovery floor — converts "68% recovery at one year on 9 h"
into **complete recovery**. This one parameter drives more of the report's alarm than any other
single input, exactly as the challenge anticipated.

**2. That the encoding-capacity deficit of g = −0.89 "persists after recovery sleep."** In
`cousins2018` (**PMID 28677325**) encoding took place *during* the restricted week; only retrieval was
after recovery. What persists is the weakened memory, not a weakened faculty. The single study is
n=29 vs 30, parallel-group, abstract-only, effect back-computed from one P-value, at a dose more
severe than the subject's, and it is the only parameter in Q2 not dose-adjusted. The true claim —
"some of what he learned across those three years is thinner than it should be" — is both more
defensible and more useful than the claim the report makes, and it points at the academic channel the
report parameterised and then never used.

**3. That permanent IQ change is indistinguishable from zero, with P(loss > 1 point) = 0.006.** This
rests on two failures stacked. First, 30% of the mixture weight goes to `binks1999` (**PMID
10341383**), a 1999 between-groups total-deprivation study with 80% power only for about 11 IQ points,
which failed to detect even the canonical attention effect, and whose noise happens to run
*positive*. Second, permanence is modelled as a small fraction of the current state deficit, so the
hypothesis actually at issue — that a three-year developmental exposure shifted a trajectory even if
the state deficit resolves — has no representation in the model at all. Meanwhile a 2024 randomised
crossover in exactly the right age band that measured a **7.5-point fluid-cognition drop** (Stager et
al, **PMID 38767872**) was excluded as subgroup-specific on the strength of a same-sized subgroup
null with no published interval. The honest answer is *unidentified*, not *zero*.

---

## Verdict

**The report's overall characterisation of the damage is not calibrated — but not because it is
uniformly too alarming or uniformly too reassuring. It is miscalibrated in a specific and correctable
pattern: too alarming about the size of the exposure and the permanence of function loss, and too
reassuring about the things that are concrete, immediate and actionable.**

The alarming half is inflated by one parameter and one mislabelled study: a nap-inclusive maximal
sleep-capacity asymptote used as a nocturnal requirement, hard-floored so it could not be
falsified within the model, and an encoding study read as demonstrating a persisting capacity deficit
it did not measure. Correcting those two moves the deficit from 3.2 to ~2.0–2.4 h/night, the
vigilance effect from large to small-moderate, and the recovery prognosis from "permanently
compromised" to "essentially recovered in three to six months on 8.5–9 h in bed."

The reassuring half hides in three places: an underpowered 1999 null given 30% weight on IQ while a
2024 age-matched positive was excluded; a permanence term structurally incapable of representing
developmental change; and a claim of full immune reversibility contradicted by the project's own
best-matched experiment, in which inflammatory markers were still elevated after three weeks of
5×4 h + 2×8 h. And the two channels with the strongest age-exact evidence — **drowsy driving**
(Tefft, Danner & Phillips, Vorona) and **academic achievement** (parameterised in `analysis_set.py`
and then never used) — are simply absent, the first of them plausibly larger than every mortality
pathway the report did count.

If I had to put one sentence in front of the subject that the current report does not say: *the
best-evidenced harms from your sleep pattern are that you learned less than you could have, and that
you are measurably more likely to crash a car — and both of those are fixable starting tonight,
whereas the permanent-damage question is genuinely open and the honest answer is that nobody knows.*
