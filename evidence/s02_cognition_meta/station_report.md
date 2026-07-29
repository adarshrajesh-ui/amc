# Station report — shard `s02_cognition_meta`

**Domain:** meta-analytic and large-sample estimates relating sleep loss and habitual short sleep to
cognitive ability, plus the evidence needed to convert standardized effect sizes into IQ-scale
points.

**Output:** 15 YAML records / 91 effect estimates / 43 records screened / 15 included, 28 excluded.
All 15 identifiers VERIFIED on both Crossref and PubMed at title similarity 1.0. All 15 validate
against `effect.schema.json`. Zero identifiers failed verification.

---

## 1. What I was asked for and what I found

| Task item | Status | Record(s) |
|---|---|---|
| 1. Lim & Dinges 2010, per-domain pooled g | **complete, all 6 domains + speed/accuracy** | `lim2010` (12 effects) |
| 2. Lowe, Safati & Hall 2017, per-domain + restriction vs deprivation separation | **complete but abstract-only** (paywalled) | `lowe2017` (7 effects) |
| 3. Wild et al. 2018, shape / optimum / ageing-equivalent | **complete** | `wild2018` (10 effects) |
| 4. UK Biobank / large-cohort duration vs fluid intelligence and RT | **complete, two independent analyses** | `kyle2017`, `west2024`, plus `fjell2023` (which includes UKB) |
| 5. Experimental restriction/extension in children and adolescents | **complete, and stronger than expected** | `campbell2024`, `lo2016`, `huang2016`, `sadeh2003`, `lundahl2015`, `astill2012`, `dewald2010` |
| 6. Is measured IQ depressed by acute sleep loss on test day | **complete — and the answer is essentially no** | `binks1999`, plus the reasoning cells of `lim2010`/`lowe2017` |
| **CRITICAL: IQ conversion basis** | **complete, with a two-route validation** | `iq_conversion_basis.md` |

**The task brief asked me to report reality where it differs from the brief's expectations, and
there are three places where it does.**

**(a) The brief's framing implies acute sleep loss depresses measured IQ. It does not, or not
measurably.** `lim2010` finds reasoning accuracy to be the *smallest and only non-significant*
effect across its six domains (g = −0.125, 95% CI [−0.268, **+0.016**]) against g = −0.762 for
lapses of attention — a sixfold gradient. `lowe2017` reports intelligence as null under partial
restriction. `binks1999` measured an actual WAIS-R short form after 34–36 h awake and found the
deprived group *3.6 points higher*. `astill2012` found the child intelligence subdomain
non-significant (r = .10, k = 6, p = .08). Four independent designs agree. The honest answer to task
item 6 is: **acute sleep loss does not measurably depress psychometric IQ, and the direct evidence
bounds any decrement at under ~2 points.**

**(b) I found a better age-matched study than the brief anticipated.** The brief pointed to Sadeh
and Gruber. `campbell2024` (*Sleep*, PMID 39283917) is a within-subject **dose-response** design
(7 / 8.5 / 10 h TIB × 4 nights) spanning **ages 9.9–22.8**, which brackets the target subject
exactly. It supplies a graded and *convex* per-hour vigilance slope, a quantified
maturation-equivalent, a clean vigilance-vs-working-memory dissociation, and a null TIB × age
interaction. It should dominate the youth-experimental part of the pool.

**(c) "Years of ageing" and "years of development" claims are real and appear three times
independently, but they are not IQ statements.** `wild2018`'s headline ("4 hours per night was
equivalent to aging 8 years") is produced by dividing a cognitive decrement by that study's own
*cross-sectional* age slope. `sadeh2003` asserted the same kind of thing qualitatively in 2003
("similar to those gained by 2 years of development"). `campbell2024` supplies the properly
quantified version in the right age band: **3.85 years of adolescent maturation (95% CI 2.4–5.3)**
for a 3-hour TIB reduction on PVT signal-to-noise. Three independent convergent estimates — but all
three are ratios against an age slope on a *specific task*, not against the IQ scale, and the
downstream model must not silently convert one into the other.

---

## 2. The per-domain pooled effects (the shard's core numbers)

### Acute total sleep deprivation — `lim2010`, 70 articles, 147 tests, n = 1,533

| Domain | Accuracy g [95% CI] | Speed/RT g [95% CI] |
|---|---|---|
| Simple attention — **lapses** | **−0.762** [−0.948, −0.576] | −0.732 [−0.874, −0.590] |
| Working memory | −0.555 [−0.741, −0.368] | −0.515 [−0.704, −0.326] |
| Complex attention | −0.479 [−0.640, −0.318] | −0.312 [−0.429, −0.197] |
| Short-term memory | −0.383 recall [−0.647, −0.118] | −0.378 recognition [−0.624, −0.132] |
| Processing speed | −0.245 [−0.500, **+0.010**] | −0.302 [−0.464, −0.140] |
| **Reasoning** | **−0.125** [−0.268, **+0.016**] | — |

Derived: reasoning/lapses ratio = **0.164** [−0.025, 0.354].

### Chronic partial restriction — `lowe2017`

| Domain | g |
|---|---|
| Attentional lapses | −0.516 |
| Sustained attention | −0.409 |
| Overall neurocognitive composite | −0.383 |
| Behavioural inhibition | −0.464 |
| Executive functioning | −0.324 |
| Long-term memory | −0.192 [−0.314, −0.070] |
| **Intelligence** | **null (reported as 0)** |

**The two meta-analyses agree on the ordering and disagree on the magnitude by about 30%
(lapses −0.762 acute vs −0.516 restriction), which is what you would expect from a milder
exposure.** The domain ordering is the robust finding; it reproduces in `campbell2024` and (with
sustained attention as the exception) inverts in `astill2012`'s child data.

### Youth experimental and observational

| Record | Exposure | Outcome | Effect |
|---|---|---|---|
| `lundahl2015` | extension vs restriction, trim-and-fill adjusted | attention | **g = −0.26** [−0.46, −0.05] |
| `lundahl2015` | restriction vs baseline, trim-and-fill adjusted | attention | g = −0.14 [−0.32, 0.04] (n.s.) |
| `campbell2024` | 7 vs 10 h TIB, 4 nights, ages 9.9–22.8 | PVT LSNR | −0.77 dB = **3.85 y maturation** [2.4, 5.3] |
| `campbell2024` | 7 vs 10 h TIB | Sternberg working memory | **null**, F(2,729) = 0.68, p = .51 |
| `sadeh2003` | ±1 h × 3 nights, ages 9–12 | digit span forward | g = −0.76 [−1.37, −0.15] |
| `huang2016` | 5 vs 9 h TIB, adolescents | GRE vocabulary cued recall | g = −0.41 (retention), −0.33 (post-review) |
| `astill2012` | habitual duration, ages 5–12 | intelligence | r = 0.10, k = 6, p = .08 |
| `astill2012` | habitual duration | **sustained attention** | **r = 0.02**, k = 15 |
| `dewald2010` | habitual duration, ages 8–18 | school performance | r = 0.069 [0.043, 0.095] |

### Habitual short sleep in large cohorts

| Record | n | Effect |
|---|---|---|
| `kyle2017` | 477,529 (UK Biobank) | <7 h vs 7–9 h: reasoning g = −0.069; RT g = −0.019; numeric memory g = −0.033 |
| `west2024` | 26,820 (UK Biobank) | short vs normal sleep: global cognitive z −0.057 (cohort 1), −0.005 (cohort 2) |
| `fjell2023` | 47,029 (Lifebrain + HCP + UKB) | <6 h vs 7–8 h on an extracted g factor: **−0.16 and −0.19 SD = −2.4 and −2.9 IQ points** |
| `wild2018` | 10,886 | 4 h vs 7.38 h optimum: overall −0.26 SD, reasoning −0.20 SD; optimum **7.38 h** |

`cohort_family` is set on every observational effect (`UK_Biobank`, `Lifebrain_HCP_UKB`,
`UCDavis_Campbell_adolescent_TIB`, `Sadeh_TelAviv_2003`, `Binks_LSU`, and the shared
`lo2016`/`huang2016` Need-for-Sleep cohort) so the pooler can de-duplicate. **`kyle2017`,
`west2024` and `fjell2023` all contain UK Biobank participants and must not be pooled as
independent.**

---

## 3. The IQ conversion — headline result

Full derivation in `iq_conversion_basis.md`. The summary:

```
IQ_points = 15 * r_g * g_task

  extracted g factor / full IQ test   r_g = 1.00   -> 15.0 pts per 1.00 g
  reasoning / gF task                       0.80   -> 12.0
  latent working-memory factor              0.72   -> 10.8
  single working-memory task                0.48   ->  7.2
  choice RT / mental speed                  0.40   ->  6.0
  PVT / vigilance / simple RT               0.20   ->  3.0   <- recommended
  school performance / grades          DECLINE — not sourced
```

**The recommended vigilance discount of 0.20 is supported by two independent routes that agree to
within a factor of 1.5:**

1. the **measured** domain gradient inside `lim2010`: g_reasoning/g_lapses = **0.164** [−0.025, 0.354];
2. the **psychometric** g-loading of a simple-RT task: **r_g = 0.25** [0.20, 0.35] from Deary 2001
   (simple RT r = .31, n = 900) and Sheppard & Vernon 2008 (mean r = .24 across 1,146 correlations;
   gF–RT range .20–.26).

These come from entirely separate literatures and neither was constructed with the other in mind.
That agreement, not the algebra, is what makes the conversion defensible.

**Calibration the conversion reproduces:** acute total deprivation lands at **1.5–4.0 IQ-equivalent
points** by all three legitimate routes (PVT-with-discount 2.9; reasoning-direct 1.5; direct WAIS-R
measurement excluding decrements worse than 1.8). The naive 1:1 conversion gives 11.4 points, which
is **6.2× the upper bound direct IQ measurement permits** — so the 1:1 mapping is *empirically
falsified*, not merely theoretically suspect.

**Vigilance decrements are not IQ decrements, quantified four ways:** the 6× domain gradient in
`lim2010`; the same ordering with intelligence null in `lowe2017`; the vigilance-moves /
working-memory-doesn't dissociation in `campbell2024`; and the reversal in `astill2012` where
sustained attention is the *least* sleep-associated child domain (r = .02).

**Interpretability benchmark.** `ritchie2018` gives 1.197 IQ points per additional year of education
(SE 0.203, 615,812 participants, conditioning on prior intelligence). On that scale the chronic
short-sleep estimates in this shard (2.4–2.9 points) are worth roughly **two years of schooling** —
which is how I would recommend the downstream report express the finding, since it needs no
vigilance discount at all and comes straight from direct general-ability measurements.

---

## 4. My confidence, by claim

| Claim | Confidence | Why |
|---|---|---|
| Domain ordering: vigilance ≫ working memory ≫ reasoning under sleep loss | **high** | Two independent meta-analyses, one adolescent dose-response experiment, consistent direction; 70+ primary studies behind it |
| Vigilance g should be discounted ~5× before conversion to IQ points | **high** | Two independent routes agreeing to within 1.5×, plus a direct IQ measurement that falsifies the undiscounted version |
| Acute sleep loss does not measurably depress psychometric IQ | **moderate-high** | Four converging designs, but the one direct test (`binks1999`) is underpowered (MDE ≈ 11 IQ points) and confounded (2.7-point baseline imbalance) |
| Sleep-loss effects are approximately age-invariant across 9–23 y | **moderate** | `campbell2024` is well-designed and null on the interaction, but `lundahl2015` and `dewald2010` moderators point in *opposite* directions from each other. Genuinely unresolved — see §5 gap 3 |
| Chronic habitual short sleep costs ~2–3 IQ-equivalent points | **low-moderate** | The magnitude is consistent across `fjell2023` and `wild2018`, but both are **cross-sectional**, and no experiment has ever run long enough to test it |
| Optimum sleep for cognition ≈ 7.4 h (adults) / ≥8.5 h TIB (adolescents) | **moderate** | `wild2018` 7.38 h from n = 10,886; `campbell2024` shows PVT still improving out to 10 h TIB, so the "optimum" is measure-dependent |
| Per-hour dose-response is convex (steeper as sleep shortens) | **low-moderate** | Only `campbell2024` tests it directly, over 7–10 h; the target subject's 5–6 h range is *outside* the observed data |

---

## 5. What I could not find, in priority order

### THE SINGLE BIGGEST GAP: nobody has measured the quantity the conversion needs

The downstream model must convert task-level effects into IQ points, and **no study has ever
sleep-deprived a sample and administered both a PVT-type measure and a full psychometric IQ battery
with adequate power.** Every g-loading in `iq_conversion_basis.md` is a *between-person*
individual-differences correlation being used as a proxy for how a *within-person* perturbation
propagates to a measured IQ score. Those are different quantities. `binks1999` is the only direct
attempt in ~30 years and it is underpowered (minimum detectable effect d = 0.72 ≈ 11 IQ points) and
confounded (the deprived arm was 2.7 Shipley IQ points higher at screening, which is larger than the
effect being looked for and biased toward masking it).

Practically, this means the 0.20 vigilance discount rests on a *validated convergence* rather than a
*measurement*. I believe it is right to within a factor of about 1.5, and I would not defend it to
within a factor of 1.1. **The single most valuable study anyone could run in this domain is a
well-powered within-subject sleep-restriction trial administering a full psychometric IQ battery
alongside a PVT.**

### Gap 2: acute performance ≠ chronic ability development, and only the acute side has experiments

Every experimental record in this shard manipulates sleep for **3 to 7 nights** and measures
**same-day performance**. The target subject's exposure is **three years**. The mechanism by which
chronic short sleep would lower a *developed ability score* is not same-day slowing — it is degraded
consolidation, less effective absorption of instruction, and possibly altered development, compounding
over years. The only evidence on that mechanism is:

- `huang2016`: vocabulary **learning** impaired at g = −0.41 after one week of 5 h TIB in
  adolescents — 3× the acute reasoning effect, and a learning rather than performance outcome;
- `fjell2023` and `wild2018`: −2.4 to −2.9 IQ-equivalent points in *habitual* short sleepers,
  **cross-sectional and explicitly non-causal**.

So the chronic estimate the downstream model most needs rests on cross-sectional association, while
all the causal evidence addresses a much shorter exposure. **A model that applies the acute 1.5–4
point band to a three-year exposure is answering the wrong question, and the direction of the error
is that it will understate the effect if the chronic mechanism is real.**

### Gap 3: age moderation is genuinely unresolved, three studies give three answers

| Source | Design | Finding |
|---|---|---|
| `lundahl2015` | meta-regression, k = 5 | **older** youth MORE impaired (b = −0.01 g per month of age, p < .01) |
| `dewald2010` | meta-regression, correlational | **younger** samples show LARGER associations; explicitly attributes it to maturation reducing sleep sensitivity |
| `campbell2024` | within-subject, ages 9.9–22.8 | **no interaction** (p > .48 all executive indices; p = .34 PVT) |

I recommend the pooler treat this as unresolved and **widen uncertainty on any age-transported
effect rather than applying a directional correction.** My own reading favours `campbell2024` — a
within-subject dose-response study covering the actual target age beats two between-study
meta-regressions — but I want the disagreement on the record rather than smoothed away. Note that
`lundahl2015`'s slope, taken literally, implies g = −1.26 at age 18, which exceeds the effect of
*full total sleep deprivation* in adults; I record the moderator and **explicitly refuse the
extrapolation**.

### Gap 4: `lowe2017`'s age moderator, paywalled

`lowe2017` states that age group *was* a significant moderator of the overall restriction effect,
across bands including "adolescents (14–17 years)" and "young adults (18–30)". **The direction and
magnitude of that moderation is the single most decision-relevant number in my entire domain for a
16–19-year-old, and it is behind a paywall.** Unpaywall reports `is_oa = false` with no OA location;
Europe PMC has no full text. The abstract does not state the direction. A shard or human with
institutional access should retrieve Table 3 / the moderator section of
doi:10.1016/j.neubiorev.2017.07.010 — it would resolve gap 3 as well.

### Gap 5: no achievement-to-g loading, so the grades route is closed

`dewald2010` (r = 0.069) and `astill2012` (r = 0.09) give well-powered school-performance
associations, and grades are what a reader intuitively cares about. But converting them to IQ points
needs the g-loading of an achievement composite, and I could not retrieve a citable source. The only
figure I encountered is secondhand *inside* `sadeh2003` (Arcia et al. 1991: digit span r = .56 with
reading, .58 with mathematics), which I have declined to treat as sourced. `iq_conversion_basis.md`
row E therefore refuses the conversion. This is a cheap gap for another shard to close.

### Gap 6: nothing measures 5–6 h, the target subject's actual exposure

`campbell2024`'s shortest condition is 7 h TIB. `wild2018`'s spline is fit on self-report with few
observations below 5 h. `lo2016`/`huang2016` use 5 h TIB and are the closest match, but n = 56 and
they share a single cohort. The per-hour slope in `campbell2024` **steepens** as sleep shortens
(−0.220 dB/h from 10→8.5 h, −0.293 dB/h from 8.5→7 h), so extrapolating a linear slope below 7 h
will understate the damage — but the convexity itself is measured over only 3 hours in one study.

---

## 6. Methodological notes the pooler should propagate

**Exposure pass-through is systematically under 100%, in the same direction in every study that
reports it.** `campbell2024`: 3 h less TIB produced only 2.07 h less actual sleep (69%).
`sadeh2003`: a nominal ±1 h manipulation (2 h separation) achieved only 1.27 h (63%). **Any study
labelling its exposure in time-in-bed is delivering a milder total-sleep-time contrast than the
label implies**, which biases effect-per-hour estimates toward zero.

**Habitual sleep is a contaminated comparator in adolescents.** `lundahl2015`'s restriction-vs-baseline
contrast (g = −0.14, n.s.) is much weaker than its extension-vs-restriction contrast (g = −0.26,
significant) because "baseline" in an adolescent sample is itself frequently insufficient. This
matters directly for a subject whose normal is 5–6 h: **relative to a genuinely rested state his
deficit is larger than any baseline-referenced study would show.**

**Publication bias is material and was detected in every cell that was tested for it.**
`lundahl2015`: attention −0.37 → −0.26 (30% shrinkage), hyperactivity −0.35 → −0.20 (loses
significance). `astill2012`: overall cognition r = .08 → .06. **I have recorded bias-adjusted
estimates wherever they were published and recommend the pooler prefer them.** Where subdomain cells
were not separately adjusted (`astill2012`'s intelligence cell, notably), the estimates are
unadjusted and probably optimistic.

**Watch three specific traps in my records.**
- `astill2012` reports **85% confidence intervals**, not 95%. Its "significant" calls are more
  permissive than conventional. I converted every interval to 95% and the `ci` fields hold my
  derived 95% intervals, not the published 85% ones — flagged in each `conversion_formula`.
- Several `value` fields are **not effect sizes**: `campbell2024`'s X-probe row holds an *F
  statistic* with `se: null`; `lo2016`'s rows hold *Cohen's f²* interaction effects (all `se: null`);
  `lundahl2015` and `dewald2010` each carry a *meta-regression coefficient* with `se: null`. Every
  such row says so in `conversion_formula` and carries `se: null` precisely so nothing pools them.
- Sign conventions differ by outcome (more PVT lapses = worse; fewer Category Test errors = better;
  higher reaction time = worse). Every effect has an explicit `direction_note`.

**`sadeh2003`'s SEs rest on an assumed pre-post correlation** because change-score SDs were never
published. I report the conservative r = 0.5 values and give the r = 0.7 alternative in each
`conversion_formula`. The point estimates are sound; the SEs are pessimistic.

---

## 7. Files produced

| File | Contents |
|---|---|
| `iq_conversion_basis.md` | **The critical deliverable.** Conversion rule, g-loading table with sources and verbatim quotes, the two-route validation, the falsification of the 1:1 mapping, the vigilance≠IQ gap quantified four ways, and three named gaps. |
| `screening_log.md` | All 43 records with decision and reason; the two wrong-DOI near-misses; access outcomes. |
| `station_report.md` | This file. |
| 15 × `<study_id>.yaml` | `lim2010` `lowe2017` `wild2018` `kyle2017` `west2024` `fjell2023` `lo2016` `huang2016` `astill2012` `dewald2010` `lundahl2015` `sadeh2003` `campbell2024` `binks1999` `ritchie2018` |
