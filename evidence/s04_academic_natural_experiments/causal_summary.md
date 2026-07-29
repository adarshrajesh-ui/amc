# Causal summary — shard `s04_academic_natural_experiments`

**What this shard was asked to do:** find Tier-2 quasi-experimental and instrumental-variable
evidence on how sleep affects academic and cognitive outcomes in adolescents and college students,
rank it by identification strength, and state what it collectively implies about the effect of ~1–2
hours less habitual sleep on academic achievement in SD and GPA units.

**Headline answer up front.** Pooling only the estimates that are both credibly identified and
age-appropriate, one hour less habitual sleep costs roughly **0.13 SD of academic achievement
(defensible range 0.02–0.30 SD)**, equivalently about **0.07–0.08 GPA points on a 4.0 scale**. For
1–2 hours less habitual sleep that is **−0.13 to −0.26 SD**, or **−0.07 to −0.16 GPA points**. If
the subject's weekday sleep sits at or below 6 h — where the best college-student study locates a
threshold — the 2-hour figure should be treated as a lower bound and could plausibly reach
**−0.20 to −0.25 GPA**.

The single most important methodological finding is stated in section 5: **the school-start-time
literature's famous reduced-form estimates are small (~0.06–0.10 SD per hour of bell time) only
because the first stage is small.** A one-hour bell delay buys just 19–37 minutes of extra sleep.
Dividing through is what produces the per-hour-of-sleep numbers above, and any model that reads the
reduced forms as sleep effects will understate the damage by a factor of roughly 2–3.

---

## 1. Ranking by identification strength

Ranked on internal validity of the design *as a device for learning about sleep*, not on how large
or convenient the answer is. Tier labels follow the spec: T1 = randomized, T2 = quasi-experiment/IV,
T4 = prospective cohort with objective exposure, TX = context only.

### Tier A — identification is close to experimental

| Rank | Study | Tier | Why it ranks here | What kills it or limits it |
|---|---|---|---|---|
| 1 | **Herber, Quis & Heineck 2017** (DST × TIMSS/PIRLS test date) | T2 | Test dates are set by international agencies for logistical reasons and schools are unidentifiable in the data, so assignment to "week after the clock change" is as good as random. Covariate balance verified with Imbens–Wooldridge normalized differences. | Exposure is *one hour on one night*, and the result is a **null** (≈0.06 SD math, n.s.; reading ≈+0.01 SD). Age 9–11. Bounds the acute effect; says nothing about chronic. |
| 2 | **Lo et al. 2016** + **Huang et al. 2016** (Need for Sleep Study) | T1 | Actual randomization of sleep itself: 56 adolescents aged 15–19 randomized to 5 h vs 9 h TIB for 7 nights in a controlled boarding school. Exposure matches the subject's weekday dose almost exactly. | 7 nights, not 3 years. Participants were *not* habitual short sleepers, so no adaptation. Effect sizes are Cohen f² of an interaction, not per-hour SMDs. Both papers are the **same 56 subjects** — must not be double-counted. |
| 3 | **Carrell, Maghakian & West 2011** (USAFA) | T2 | Random assignment of freshmen to sections and instructors, plus two exogenous administrative bell changes. Largest effect in the literature (−0.140 SD, SE 0.045, for a 7:00 am class). | **No sleep measurement whatsoever.** Herber et al. point out that USAFA prohibited napping and mandated early breakfast, so "it seems equally likely that students in late courses achieved higher grades because the empty time-slot allowed them to repeat and thereby better remember the course content." Mechanism disputed. |
| 4 | **Bessone et al. 2021** (QJE, Chennai) | T1 | Well-powered field RCT, actigraphy-verified exposure, pre-specified indices with multiplicity control, and a within-study active comparator (naps). | Adults, not students; the achieved extension is only +27 min; and sleep *efficiency*, not duration, was the binding constraint in that population. |
| 5 | **Jin & Ziebarth 2020** (DST "fall back") | T2 | Statutory transition date, daily event study, 3.4 M BRFSS respondents plus 160 M German admissions, placebo outcomes tested, spring/fall asymmetry exploited. | Health outcomes, not academic. Effect explicitly transient ("persists for four days"). |

### Tier B — credible quasi-experiments, but sleep is inferred rather than measured

| Rank | Study | Tier | Why it ranks here | What kills it or limits it |
|---|---|---|---|---|
| 6 | **Heissel & Norris 2018** (time-zone boundary IV) | T2 | Within-student panel: tracks the *same* student across a residential move that crosses the Florida time-zone boundary. Cragg–Donald F = 404–1230. The decisive falsification test: the math effect "spikes precisely at the gender-specific age of median entrance into an important pubertal stage" — a confounder would have to mimic a puberty-timing discontinuity that differs by two years between girls and boys. | Sleep never measured. A household move is a bundled treatment; cross-boundary movers start 0.08–0.09 SD below non-movers. Authors concede they cannot separate learning from test-day effects. |
| 7 | **Edwards 2012** (Wake County bus schedules) | T2 | Bell times move because the district's bus-routing problem changes as enrollment grows. School FE *and* student-school FE. Placebo tests show no relationship between start-time changes and per-grade enrollment or share of returning students. n ≈ 100k. | Sleep not measured. Grades 6–8 (ages ~11–14); only the grade-10 persistence result reaches the subject's age band. |
| 8 | **Gibson & Shrader 2018** (dual sunset instruments) | T2 | Two complementary instruments — within-location seasonal sunset variation with location FE (short run) and cross-location average sunset (long run). Explicitly tests and rejects the labor-supply channel; rules out compensating naps. | Outcome is earnings, not achievement. The long-run half collapses to 529 locations and is essentially cross-sectional. |
| 9 | **Hinrichs 2011** (Minneapolis vs St. Paul DiD) | T2 | Clean policy DiD around a real bell-time change in one metro with an adjacent untreated twin. Yields a **precise null**: 95% CI (−0.0512, +0.0406) SD per hour. | Effectively one treated cluster. ACT is self-selected and not taken on the normal school schedule, so it may be insensitive to a same-day alertness channel. |
| 10 | **Giuntella & Mazzonna 2019** (US time-zone border RD) | T2 | Spatial RD at time-zone borders with a genuine measured first stage (−19 min). Effects concentrated among those with early schedules, exactly as the mechanism predicts. | Adults 18–55. Cognitive outcome is a self-reported impairment dummy. Cross-border commuting and border-following economic discontinuities remain. |
| 11 | **Jagnani 2024** (India sunset IV) | T2 | Measured first stage (−0.47 h sleep per hour of sunset delay), district×season FE, child FE, weather controls, time-use evidence on where the displaced time goes. Only sunset-IV study with an *academic* outcome, and the only one with a long-run attainment result (−0.14 years of education per 10 min). | Implied **−1.15 SD per hour of sleep** — implausible, roughly the magnitude of total sleep deprivation. Sunset colinear with evening heat and light in a partly electrified rural setting. Indian children 6–16. |
| 12 | **Giuntella, Han & Mazzonna 2017** (China sunset IV) | T2 | Single national time zone across ~60° of longitude gives huge sunset variation. Hukou registration nearly eliminates residential sorting (<1% live outside their Hukou city). Effects present for urban employees, **absent for farmers and the self-employed** — a generic east–west confounder would not switch off for farmers. | No discontinuity to lean on; longitude in China correlates with nearly every development variable. 0.4–0.6 SD per hour is very large. Population aged 45+. |
| 13 | **Dewald-Kaufmann, Oort & Meijer 2013** | T1 | Randomized, actigraphy-verified, and uniquely tests *extension* in adolescents already selected for chronic sleep reduction — the correct direction of the counterfactual. | n = 55, 85.5% female, no-instruction control, and "some aspects of cognitive performance, especially visuospatial processing" is a strong selective-reporting signal. No academic outcome. Abstract only. |

### Tier C — rich controls or objective measurement, but no exogenous variation

| Rank | Study | Tier | Why it ranks here | What kills it or limits it |
|---|---|---|---|---|
| 14 | **Groen & Pabilonia 2019** | T2 (nominally) | **The most valuable single record in this shard**, despite mid-table identification: the only study that measures the sleep first stage (24-h time diaries: +36 min per hour of bell time) *and* test scores in the *same* nationally representative **high-school** sample. That is what makes a per-hour-of-sleep estimate possible without importing an external first stage. | Identification is selection-on-observables plus a lagged outcome, not a natural experiment. The authors say so: "it is possible that our estimates suffer from an omitted variables bias due to student sorting into schools with different starting times." n ≈ 600 per sex. Reading effects are **entirely female-driven** (0.156 vs 0.003 for males) and the male four-year-college result (−16.7 pp) is not credible, which signals fragility. |
| 15 | **Creswell et al. 2023** (PNAS) | T4 | Actigraphy, prospective, five samples at three universities, explicit discovery/confirmation split, and — crucially — controls for **previous-term GPA**, so the estimate uses only the *change* in GPA. Survives adding daytime sleep, race, gender, first-generation status and course load. | Observational: no exogenous variation. Residual time-varying confounding and reverse causation remain. Replicated in 3 of 4 confirmatory samples; Study 5 (N=131) was correctly signed but p = .34. |
| 16 | **Morgenthaler et al. 2016** (AASM review) | T2 | Supplies the pooled **first stage** that the whole start-time literature needs: +18.65 min (95% CI 8.13–29.16) for delays ≤60 min, +52.56 min (38.74–66.37) for delays >60 min. | The constituent studies are mostly uncontrolled pre/post. The review itself grades the academic-performance evidence as weak, and reports one long-run evaluation where the sleep gain fully decayed by 9 months. |
| 17 | **Dunster et al. 2018** (Seattle) | T2 | Best-measured first stage anywhere: actigraphy, +34 min from a 55-min delay, achieved entirely by later wake time, with no compensating change on non-school nights and no change in napping. Baseline sleep (6 h 50 min) sits right at the subject's weekday level. | The **grade** outcome is an uncontrolled pre/post comparison of two different cohorts, with absolute teacher-assigned grades that the authors warn "could carry an implicit bias from teachers who could have been for or against the school time change." Use for the first stage; discard the +4.5% grade result. |
| 18 | **Okano et al. 2019** (MIT) | T4 | Best population match in the shard (88 MIT freshmen, mean age 18.19 — essentially the subject's exact demographic), full-semester actigraphy, objectively scored assessments, verified absence of TA effects. | **Zero covariate adjustment.** No prior ability, conscientiousness, course load or mental health controls. Its implied per-hour effect (~+12.6 grade points per hour) is transparently confounded. Task listed it as a natural experiment; **it is not one, and I have retiered it T4.** |

### Tier D — do not use as evidence

| Rank | Study | Tier | Verdict |
|---|---|---|---|
| 19 | **Shapiro 2015** (IZA World of Labor) | TX | Narrative policy synthesis, no search strategy, no pooling, does not engage with Hinrichs's null, and the author is the "Maghakian" of Carrell, Maghakian & West. Useful only for the field's consensus value (~0.10 SD per hour of bell time) and the policy benchmark ("the same effect as... replacing an average teacher with one in the 84th percentile of effectiveness"). Contains no first stage. |
| 20 | **Gaski & Sagarin 2011** (DST × SAT) | T2 nominally | **This is the observational study dressed up as a natural experiment that the task warned about.** A cross-section of Indiana counties by DST regime, where DST observance tracked commuting ties to Chicago and Louisville and therefore income, urbanicity and school quality. Reports −0.16 SD on SAT. Herber et al.'s verbatim reaction: "Yet, we doubt". **Exclude from pooling.** |

---

## 2. The confounding-magnitude calibration this shard produces

Three internal comparisons let us *measure* how badly the observational sleep–achievement literature
is biased, which is worth more to the downstream model than any single point estimate.

1. **Within Edwards 2012.** The raw cross-sectional coefficient is **9.5 percentile points per hour**
   of bell time. Adding individual demographics collapses it to **4.5**; the student-school
   fixed-effects estimate is **1.8**. That is a **5-fold** reduction from naive to quasi-experimental
   in a single dataset.
2. **DST, well-identified vs badly-identified.** The credible DST regression discontinuity (Herber et
   al.) finds **0.01–0.06 SD, not significant**. The confounded DST cross-section (Gaski & Sagarin)
   finds **0.16 SD**. Same topic, ~3–16× discrepancy, attributable entirely to design.
3. **College GPA, adjusted vs unadjusted.** Okano et al. (no covariates) imply roughly **12.6 grade
   points per hour** of sleep. Creswell et al. (controlling for previous-term GPA) find **1.75 grade
   points per hour** (0.07 GPA on a 4.0 scale ≈ 1.75 points on a 100-point scale). A **7-fold**
   reduction from conditioning on the lagged outcome alone.

**Directive for the modeller:** any T5/TX cross-sectional sleep–achievement association entering the
pool should be discounted by a factor of roughly **3–7** before being compared with the T2 estimates
below, or excluded.

---

## 3. The first stage — how much sleep does a schedule shift actually buy?

This table is the bridge between "per hour of bell time" and "per hour of sleep". Every entry is a
directly measured first stage from an included record.

| Source | Instrument | Sleep gained per hour of schedule shift | Measurement |
|---|---|---|---|
| Morgenthaler 2016 (pooled, ≤60 min delays) | school start time | **18.65 min** (95% CI 8.1–29.2) | mostly self-report |
| Giuntella & Mazzonna 2019 | sunset time (US borders) | **19 min** | ATUS time diaries |
| Gibson & Shrader 2018 (short run) | daily sunset | **22.8 min** (SE 2.5) | ATUS time diaries |
| Jagnani 2024 | sunset time (India) | **28 min** | ITUS time diaries |
| Dunster 2018 | 55-min bell delay | **37 min** (34 min per 55 min) | **wrist actigraphy** |
| Groen & Pabilonia 2019 | school start time | **36 min** (SE 13.7) | 24-h time diaries |
| Morgenthaler 2016 (pooled, >60 min delays) | school start time | **52.56 min** (95% CI 38.7–66.4) | mostly self-report |
| Gibson & Shrader 2018 (long run) | annual average sunset | **55.8 min** (SE 16.8) | ATUS time diaries |

**Central first stage: ~0.45 h of sleep per hour of schedule shift (range 0.31–0.62 h).** Two
patterns matter:

- The gain comes **almost entirely from later wake time, not earlier bedtime** (Dunster: +44 min
  sleep offset, sleep onset unchanged; Groen & Pabilonia: wake-up +0.750 h, bedtime effect null;
  Jagnani: bedtime +0.36 h with no compensating wake shift). Adolescent bedtime is circadian-driven
  and does not respond to schedules; wake time is the only lever.
- **Larger shifts buy proportionally more sleep** (52.6 min for >60-min delays vs 18.7 min for ≤60-min
  delays; 55.8 min long-run vs 22.8 min short-run in Gibson & Shrader). Chronic exposure produces a
  near one-for-one chronic deficit rather than being compensated away.

---

## 4. Converting everything to SD of academic achievement per hour of sleep

| Study | Reduced form (SD per hour of schedule shift) | First stage used | **Implied SD per hour of sleep** | Weight |
|---|---|---|---|---|
| Hinrichs 2011 (ACT) | −0.005 (CI −0.051 to +0.041) | 0.45 h | **−0.01** | high — precise null, exact age |
| Creswell 2023 (GPA, direct) | — (direct estimate) | — | **0.10–0.14** | high — exact age, lagged-outcome control |
| Edwards 2012 (math, student-school FE) | 0.045 | 0.45 h | **0.10** | medium — younger sample |
| Edwards 2012 (math, school FE) | 0.056 | 0.45 h | **0.12** | medium |
| Heissel & Norris 2018 (reading, adolescents) | 0.057 | 0.45 h | **0.13** | high — puberty-specific, exact age band |
| Heissel & Norris 2018 (math, adolescents) | 0.081 | 0.45 h | **0.18** | high |
| Groen & Pabilonia 2019 (reading, female) | 0.156 | **0.601 h (own)** | **0.26** | high on relevance, medium on identification |
| Shapiro 2015 (field consensus) | 0.10 | 0.45 h | **0.22** | low — narrative, COI |
| Carrell 2011 (course grades) | 0.168 | 0.45 h (assumed) | **0.37** | low for *sleep* — no first stage, mechanism disputed |
| Giuntella, Han & Mazzonna 2017 (cognition) | — (direct IV) | — | **0.40–0.60** | low — age 45+, cognition not achievement |
| Jagnani 2024 (math) | 0.54 | **0.47 h (own)** | **1.15** | very low — implausible magnitude, Indian children |

**Pooled judgement.** Taking the five age-appropriate, credibly identified, academic-outcome
estimates — Hinrichs (−0.01), Creswell (0.12), Edwards (0.11), Heissel & Norris (0.15), Groen &
Pabilonia (0.26) — the median is **0.13 SD per hour of sleep** and the mean is **0.13**. Adding
Carrell raises the median to 0.15; excluding Groen & Pabilonia on identification grounds lowers it
to 0.12. The estimate is robust to those choices.

The three large outliers (Jagnani 1.15, Giuntella–Han–Mazzonna 0.40–0.60, Carrell 0.37) share a
diagnostic feature: they are either **IV ratios with a small denominator**, where any violation of the
exclusion restriction is amplified, or reduced forms with **no first stage at all**. They should shape
the right tail of the posterior, not its centre.

**Recommended parameter: 0.13 SD of academic achievement per hour of habitual sleep, 80% interval
0.02–0.30 SD, with a long right tail to ~0.5 SD.**

---

## 5. What the T2 evidence collectively implies for 1–2 hours less habitual sleep

### In SD units

| Deficit | Central estimate | 80% interval | Note |
|---|---|---|---|
| 1 hour less | **−0.13 SD** | −0.02 to −0.30 SD | Linear region |
| 2 hours less | **−0.26 SD** | −0.04 to −0.60 SD | Linearity assumed; see nonlinearity caveat |

For scale, Heissel & Norris supply the benchmarks: reducing elementary class size from 22 to 15 buys
0.15–0.20 SD, and a 1 SD improvement in teacher quality buys about 0.10 SD. **A 2-hour habitual sleep
deficit is therefore roughly equivalent to losing a 1-SD-better teacher twice over, or to undoing a
one-third class-size reduction.**

### In GPA units (4.0 scale)

| Deficit | Central estimate | Route |
|---|---|---|
| 1 hour less | **−0.07 GPA** | Creswell et al. 2023, direct: "every additional hour of average nightly sleep duration early in the semester was associated with an 0.07 increase in end-of-term GPA" |
| 1 hour less | **−0.08 GPA** | Cross-check: 0.13 SD × a first-year GPA SD of ~0.6 |
| 2 hours less | **−0.14 GPA** | Linear extrapolation of Creswell |
| 2 hours less | **−0.16 GPA** | Cross-check via SD route |
| 2 hours less, subject below the 6 h threshold | **−0.20 to −0.25 GPA** | Applying Creswell's own threshold finding (see below) |

The agreement between the two independent routes (−0.07 direct vs −0.08 via the SD pool) is the most
reassuring quantitative result in this shard: a T4 college-GPA study and a set of T2
school-start-time quasi-experiments converge on the same per-hour magnitude despite entirely
different designs, populations and outcomes.

### Three caveats that push the estimate up

1. **Nonlinearity below 6 hours.** Creswell et al. find that "sleeping less than 6 h each night was a
   period where sleep shifted from helpful to harmful for end-of-term GPA, relative to previous-term
   GPA." A subject at 5–6 h on weekdays is at or below that threshold, so the linear coefficient
   understates his position.
2. **Chronic exposure appears worse than acute.** Gibson & Shrader's long-run per-hour effect is
   ~4.5× their short-run effect (5% vs 1.1% of earnings), and their long-run first stage is nearly
   one-for-one. Every school-start-time estimate is measured over months at most, not three years.
3. **Weekend recovery is incomplete.** Lo et al. randomized adolescents to 5 h × 7 nights then gave
   them 9 h recovery nights: PVT lapses "remained elevated relative to baseline after the first two
   nights of recovery sleep (P < 0.001)" and arithmetic/processing speed "remained significantly
   poorer than the control group (P < 0.003)". The subject's weekend catch-up is only 7–8 h, i.e.
   *less* than that protocol's recovery dose, so weekday deficits should be assumed to accumulate.

### Three caveats that push the estimate down

1. **The best-identified null is precise, not underpowered.** Hinrichs's 95% CI is (−0.051, +0.041)
   SD per hour of bell time. That is a genuine constraint.
2. **Randomized sleep *extension* has largely failed.** Bessone et al. randomized +27 min for three
   weeks and got −0.01 SD (SE 0.04) on their overall index while *naps* in the same sample produced
   +0.12 SD. Dewald-Kaufmann's adolescent extension trial produced only a selective visuospatial
   improvement. The restriction→harm direction is far better evidenced than the extension→benefit
   direction, and the model should not assume symmetry.
3. **Sex heterogeneity runs against the subject.** Groen & Pabilonia's reading effect is 0.156 SD for
   females and **0.003 SD for males**. Our subject is male. This is one small study and I would not
   zero out the male effect on its strength, but it materially widens the lower tail.

---

## 6. Answers to the specific questions the task asked

**Do the school-start-time studies report a sleep first stage?** Only three do. Groen & Pabilonia
(+36 min/h, time diaries), Dunster (+34 min per 55 min, actigraphy) and Morgenthaler's pooled review
(+18.65 / +52.56 min). **Carrell, Edwards, Heissel & Norris and Hinrichs measure no sleep at all** —
their coefficients are per hour of *bell time*, and treating them as sleep effects without dividing by
a first stage is the most common error in reading this literature.

**Time-zone / sunset IV, first stage and reduced form.** First stages: −19 min (Giuntella & Mazzonna,
US), −22.8 min short run and −55.8 min long run (Gibson & Shrader, US), −28 min (Jagnani, India).
Reduced forms: cognitive impairment probability +0.002 to +0.005 (Giuntella & Mazzonna); log earnings
−0.0051 short run and −0.045 long run per hour of later sunset (Gibson & Shrader); math −0.09 SD per
10 min of later sunset and −0.14 years of education per 10 min of later average sunset (Jagnani);
cognition 0.4–0.6 SD per hour of *sleep* (Giuntella, Han & Mazzonna, China, age 45+).

**DST discontinuities on test scores.** The best-identified one finds **nothing** (Herber, Quis &
Heineck: ≈0.06 SD math, not significant; reading wrong-signed and near zero). The one that finds a
large effect (Gaski & Sagarin, −0.16 SD SAT) is a confounded county cross-section. Jin & Ziebarth's
DST work is about health, not test scores, and finds benefits from the *fall* transition only.

**Okano et al. — night-before vs semester-long sleep.** Unambiguous and directly relevant. Sleep on
the night before a test did **not** predict performance on that test (all rs < 0.20, ps > 0.05 for
midterms; rs 0.01–0.26, ps > 0.05 for quizzes). Semester-long sleep **did**: duration r = 0.38
(p < 0.0005), quality r = 0.44 (p < 0.00005), inconsistency r = −0.36 (p < 0.001). The three
measures jointly explained **24.44%** of grade variance (R² = 0.24, F(3,84) = 8.95, p = 0.00003),
decomposed as 7.16% duration / 9.68% quality / 7.60% inconsistency; only inconsistency was
individually significant (p = 0.03). All signs point the same way — more and better sleep, better
grades — with no sign reversals. The authors' own reading: "the role of sleep is crucial during the
time the content itself is learned, and simply getting good sleep the night before may not be as
helpful."

Huang et al.'s randomized experiment supplies the causal mechanism behind that correlation:
sleep restriction destroyed recall of **massed (crammed)** vocabulary at every retention interval
while leaving **spaced** material intact. **Implication for the subject: his occasional 3–4 h
pre-exam nights are less damaging than his habitual 5–6 h weeknights, and cramming cannot recover
what was not consolidated during term.**

**Randomized sleep-extension trials in adolescents or college students with academic outcomes.**
Effectively none exist. The closest are Dewald-Kaufmann 2013 (n = 55, 85.5% female, cognitive not
academic outcomes, selective reporting) and Bessone 2021 (adults, +27 min, null on cognition). The
randomized *restriction* evidence at this age is far stronger (Lo/Huang, n = 56, 5 h vs 9 h × 7
nights, Cohen f² 0.20–1.48).

**GPA per hour of habitual sleep with identification strategy stated.** Creswell et al. 2023:
**+0.07 GPA per hour**, N = 557 pooled across four confirmatory samples at three universities.
Identification strategy: **lagged-outcome (value-added) regression on observational actigraphy data** —
the causal claim rests on conditioning on previous-term GPA so that only the *change* in GPA is used,
plus covariate robustness to daytime sleep, race, gender, first-generation status and course load.
This is materially better than a raw correlation and materially weaker than a natural experiment. The
authors say "predicts" and "associated with", not "causes", and so should we.

---

## 7. What the downstream model should actually take from this shard

1. **Primary parameter:** academic achievement declines **0.13 SD per hour** of habitual sleep
   deficit (80% interval 0.02–0.30 SD), equivalently **0.07 GPA points per hour** on a 4.0 scale.
2. **For the subject's actual exposure** (weekday 5–6 h, weekend 7–8 h → weekly mean ≈ 6.1 h against
   an age-appropriate ~8.5 h, i.e. a ~2.4 h average nightly deficit): **−0.31 SD, or −0.17 GPA**, with
   a plausible range of −0.05 to −0.72 SD and −0.03 to −0.40 GPA. Treat the central figure as a lower
   bound because of the sub-6 h threshold and the chronic-vs-acute gap.
3. **Down-weight by a factor of 3–7** any cross-sectional sleep–achievement association fed in from
   other shards, on the basis of the three within-topic confounding calibrations in section 2.
4. **Do not pool** Gaski & Sagarin (confounded), Shapiro (narrative, double-counts primaries), the
   Dunster grade outcome (uncontrolled pre/post), or the Okano regression coefficients (unadjusted).
   Do not count Lo 2016 and Huang 2016 as independent studies.
5. **Confidence grades for the headline number** (per `gates.md`): Quantity **B** (5–9 independent
   credibly identified studies); Quality/tier **A** (T1/T2 dominant); Transportability **A/B**
   (Carrell, Hinrichs, Groen & Pabilonia, Lo/Huang, Okano and Creswell are all at 15–19 or
   college-freshman age; Edwards, Jagnani, Herber are younger and Gibson–Shrader,
   Giuntella–Han–Mazzonna, Bessone are older); Model dependence **B** (sign stable across every
   credible specification except Hinrichs's precise null; magnitude varies about 3× across the
   defensible set, from 0.10 to 0.26 SD per hour, and ~10× if the non-transportable outliers are
   admitted).
