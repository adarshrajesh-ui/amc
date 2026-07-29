# Converting Hedges' g into full-scale-IQ-equivalent points

Shard `s02_cognition_meta`. This document supplies the conversion the downstream model needs,
the evidence it rests on, the uncertainty on it, and the specific errors it is designed to prevent.

Every number below is traceable to a retrieved source with a verbatim quote. Where I have had to
make an assumption rather than cite a measurement, the assumption is labelled **ASSUMPTION** and
its direction of bias is stated.

---

## 1. The headline recommendation

**Do not use a single conversion factor. Use the decision rule below, in order of preference.**

| | Situation | What to do |
|---|---|---|
| **A** | The study measured a **general ability composite** (a full IQ test, or an extracted g-factor / first principal component of a cognitive battery) | Multiply the standardized effect by **15**. No discount. |
| **B** | The study measured a **reasoning / fluid-intelligence task** (Raven's, verbal-numerical reasoning, a CBS reasoning composite) | Multiply by **0.80 × 15 = 12.0** points per unit g. |
| **C** | The study measured **working memory**, **processing speed**, or **short-term memory** | Multiply by the task-specific `r_g` in §4 × 15. Typically **7.2** points per unit g for a single WM task, **6.0** for choice-RT-type speed. |
| **D** | The study measured **vigilance / PVT / simple reaction time** | Multiply by **0.20 × 15 = 3.0** points per unit g. Plausible range 2.2 to 5.2. |
| **E** | The study measured **school performance / grades** | Do not route this through IQ at all without an explicit achievement-to-g loading, which I was unable to source directly (see §7, gap 2). |

**The single most important number in this document is in row D.** A Hedges' g of 1.00 on a
psychomotor vigilance task is worth roughly **3 IQ-equivalent points, not 15**. Getting this wrong
inflates the estimated cognitive damage by about a factor of five.

---

## 2. Why the naive 1:1 conversion is wrong, and by how much

IQ is scaled to SD = 15 by construction, so `g = 1.0 → 15 points` is correct **only if the measure
in question is a pure measure of general intelligence.** Almost nothing in the sleep literature is.
The sleep literature's workhorse outcome is the psychomotor vigilance task, which is the *least*
g-loaded cognitive measure in wide use — it is deliberately designed to be cognitively trivial so
that it isolates state instability rather than ability.

The 1:1 conversion is not merely theoretically suspect. It is **empirically falsified** by data
inside this shard:

- Apply 1:1 to the pooled acute-total-deprivation effect on lapses of attention
  (`lim2010`, g = −0.762) and you get **11.4 IQ points**.
- Direct measurement of psychometric IQ after 34–36 h of total sleep deprivation (`binks1999`,
  WAIS-R short form, n = 61) gives a 95% CI on the raw difference of **[−1.8, +9.0] points**, with
  the point estimate in the *wrong direction* for a harm hypothesis. That interval **excludes** any
  decrement worse than 1.8 points.
- 11.4 points is therefore **6.2×** larger than the worst decrement the direct measurement permits.

A conversion that contradicts the direct measurement of the very quantity being converted to is
not a conversion; it is an error. Row D exists to prevent exactly this.

---

## 3. Route A — the preferred method: use the direct measurement and skip the conversion entirely

The strongest thing I can tell the downstream model is that **it usually does not need the
g-loading discount at all**, because several studies in this shard measured reasoning or general
ability *directly*, under the same exposures. Those measurements already answer the question.

| Source | Exposure | Outcome measured | Effect | IQ-equivalent |
|---|---|---|---|---|
| `lim2010` | acute total SD (<48 h) | reasoning accuracy, pooled | g = −0.125, 95% CI [−0.268, 0.016] | −1.9 pts (CI −4.0 to +0.2) |
| `lowe2017` | partial restriction | intelligence | reported as **null** | ~0 |
| `binks1999` | 34–36 h total SD | WAIS-R short-form full-scale IQ | +3.6 raw points, CI [−1.8, +9.0] | decrement worse than −1.8 pts excluded |
| `astill2012` | habitual duration, ages 5–12 | intelligence subdomain | r = 0.10, k = 6, p = .08 | ≈ +1.5 pts per SD of sleep (n.s.) |
| `fjell2023` | habitual < 6 h vs 7–8 h | extracted g factor (GCA) | −0.16 and −0.19 SD | **−2.4 and −2.9 pts (authors' own conversion)** |
| `wild2018` | 4 h vs optimum | CBS reasoning composite | −0.20 SD | −2.4 pts at `r_g` = 0.80 |

Five independent designs — a meta-analysis of 70 acute-deprivation articles, a restriction
meta-analysis, a lab IQ test, a child meta-analysis, a 47,029-person multi-cohort study, and a
~10,000-person online study — all land between **0 and 3 IQ-equivalent points**. That convergence,
not any g-loading algebra, is the real basis for the conversion.

`fjell2023` is also the **published precedent** for the arithmetic. Its authors performed the
SD × 15 conversion themselves on an extracted g factor:

> "Still, although short sleep was not associated with smaller regional brain volumes, the short
> sleepers scored lower on tests of general cognitive abilities. The effect sizes were equal to 2.9
> and 2.4 IQ-points for the short sleepers with and without sleep problems and daytime sleepiness,
> respectively."
> — Fjell et al., *J Neurosci* 2023;43(28):5241–5250. doi:10.1523/JNEUROSCI.2330-22.2023, PMID 37365003

0.19 × 15 = 2.85 ≈ 2.9 and 0.16 × 15 = 2.40, matching exactly. Row A of the recommendation is
this paper's method, and it is legitimate there **because and only because** the outcome was a
g-factor score rather than a single task.

---

## 4. Route B — the g-loading discount, when only a task-level g exists

### The formula, and why it is `r_g` and not `r_g²`

Let `T` be the task, `G` the general factor, and `r_g = corr(T, G)` the task's g-loading. Given a
standardized shift of `g_task` SDs on the task, the projection of that shift onto `G` is

```
Δ_G  =  r_g · g_task           (in SD units of G)
IQ-equivalent points  =  15 · r_g · g_task
```

Two errors to avoid:

- **Do not use `r_g²`.** Shared *variance* answers a different question (how much of the
  between-person spread in T is g) and would understate the point change. For the PVT, `r_g²` = 0.06
  would give 0.9 points where `r_g` gives 3.0.
- **Do not divide by `r_g`.** Dividing corresponds to a causal model in which sleep loss acts *on G
  itself* and the task merely indexes it — which would *amplify* a PVT effect to 45 IQ points. That
  model is refuted by the domain gradient in §5: if sleep loss acted through g, reasoning would move
  as much as vigilance, and it does not.

**ASSUMPTION (the load-bearing one):** multiplying by `r_g` assumes the sleep-induced perturbation is
distributed across the task's variance components in proportion to those components — i.e. that the
perturbation is "generic" with respect to the task's factor structure. It almost certainly is not:
sleep loss preferentially attacks the state-instability component of the PVT, which is precisely its
*non*-g component. **So `15 · r_g · g_task` is an upper bound on the IQ-equivalent, not a point
estimate.** Direction of bias: overstates the IQ effect. The §5 validation shows how much.

**SECOND CAVEAT, stated plainly:** every `r_g` below is a *between-person individual-differences*
correlation. It quantifies how much of the spread across people in a task is general ability. It is
not a measurement of how a *within-person experimental perturbation* propagates to a measured IQ
score, which is what we actually want. No published study measures that quantity directly, so far as
I could find. `r_g` is a proxy. Its adequacy is established by the §5 triangulation, not by
assumption.

### The g-loading table, with sources

| Measure type | `r_g` point | plausible range | IQ pts per 1.00 g | Source |
|---|---|---|---|---|
| PVT / simple RT (vigilance) | **0.25** | 0.20 – 0.35 | 3.8 | Deary 2001; Sheppard & Vernon 2008 |
| Choice RT / general mental speed | 0.40 | 0.24 – 0.49 | 6.0 | Deary 2001; Sheppard & Vernon 2008 |
| Single working-memory task | 0.48 | 0.45 – 0.55 | 7.2 | Ackerman 2005; Kane 2005 |
| Latent working-memory factor | 0.72 | 0.41 – 1.00 | 10.8 | Kane 2005 |
| Reasoning / gF task | 0.80 | 0.63 – 0.90 | 12.0 | Lyall 2016 (lower bound); psychometric convention |
| Extracted g factor / full IQ | 1.00 | 0.90 – 1.00 | 15.0 | Fjell 2023 (precedent) |

**A note on where I chose 0.20 rather than 0.25 for row D of the recommendation.** The table's
point estimate for simple RT is 0.25, from the individual-differences literature. Row D recommends
0.20 because it is the pooled compromise between that 0.25 and the *measured* domain-gradient
discount of 0.164 (§5), and because the "generic perturbation" assumption biases `r_g` upward.

### The citations, with the sentences they rest on

**Deary IJ, Der G, Ford G. Reaction times and intelligence differences: A population-based cohort
study. *Intelligence*. 2001;29(5):389–399. doi:10.1016/S0160-2896(01)00062-9** (Crossref VERIFIED;
not indexed in PubMed). n = 900, broadly representative Scottish population sample, age 56.

> "AH4 Part I total scores correlated .31 with simple reaction time, .49 with four-choice reaction
> time, and .26 with intraindividual variability in both reaction time procedures."

The **.31 for simple reaction time** is the single most directly relevant published number for the
PVT, because the PVT *is* a simple reaction-time task. Note also the ordering: simple RT .31 <
four-choice RT .49, and the paper reports the difference between those two correlations as highly
significant (t = 5.62, df = 897). **g-loading rises with task complexity.** The PVT is at the
*simplest* end — its long, randomly-varying foreperiod makes it, if anything, less cognitively
demanding than a standard simple-RT task — so 0.31 is an upper anchor for the PVT rather than a
central estimate. Two opposing corrections apply: (a) Deary's sample has a wide ability range and a
mean age of 56, both of which *inflate* RT–IQ correlations relative to a young restricted-range
student sample of the kind used in sleep studies; (b) single-session RT is unreliable, and
disattenuating for measurement error would *raise* the latent correlation. I have set the range
0.20–0.35 to span both corrections.

**Sheppard LD, Vernon PA. Intelligence and speed of information-processing: A review of 50 years of
research. *Personality and Individual Differences*. 2008;44(3):535–551.
doi:10.1016/j.paid.2007.09.015** (Crossref VERIFIED; not indexed in PubMed). This is the largest
synthesis available, and it is the anchor for the low end.

> "The overall correlation between mental speed and intelligence is moderate but very consistent:
> across all the different studies and measures that were reviewed – which yielded a total of 1146
> correlations – the mean correlation is .24"

> "mean correlations between general intelligence (g) and reaction time measures range from .22 to
> .40, mean correlations between gf and reaction times range from .20 to .26, and mean correlations
> between gc and reaction times range from .17 to .39. There is a trend for correlations with g and
> gc to be higher when reaction time tasks involve more [complexity]"

**r = .24 across 1,146 correlations** is as stable an estimate of the speed–intelligence relation as
exists. Note the gF row specifically: **.20 to .26**. Fluid intelligence — the ability most people
mean by "IQ" in a developmental context — shares even less with reaction time than g overall does.

**Ackerman PL, Beier ME, Boyle MO. Working memory and intelligence: the same or different
constructs? *Psychological Bulletin*. 2005;131(1):30–60. doi:10.1037/0033-2909.131.1.30, PMID
15631550** (Crossref + PubMed VERIFIED). Meta-analysis of 86 samples.

> "The authors conducted a meta-analysis of 86 samples that relate WM to intelligence. The average
> correlation between true-score estimates of WM and g is substantially less than unity (ρ=.479)."

ρ = **.479** is a *true-score* (disattenuated) correlation, so it is already corrected for
unreliability and is the right number for a single WM task.

**Kane MJ, Hambrick DZ, Conway ARA. Working memory capacity and fluid intelligence are strongly
related constructs: comment on Ackerman, Beier, and Boyle (2005). *Psychological Bulletin*.
2005;131(1):66–71. doi:10.1037/0033-2909.131.1.66, PMID 15631552** (Crossref + PubMed VERIFIED).
The rebuttal to Ackerman, and it brackets the range from above.

> "The authors' reanalysis of 14 such data sets from 10 published studies, representing more than
> 3,100 young-adult subjects, suggests a strong correlation between WMC and Gf/reasoning factors
> (median r = .72), indicating that the WMC and Gf constructs share approximately 50% of their
> variance."

> "Table 1 also presents the WMC-Gf correlations, which ranged from .41 to 1.00 with a median value
> of .72."

Critically, Kane et al. concede the point that matters for *task-level* conversion:

> "individual tests of WMC and Gf (or reasoning) share only about 20% of their variance, on average,
> and so these constructs are not synonymous"

20% shared variance between individual tests means **r ≈ 0.45 at the task level**, which agrees with
Ackerman's ρ = .479 to within rounding. **The Ackerman–Kane dispute is about latent factors, not
about tasks, and both sides agree on the task-level number.** That is why I can state 0.48 for a
single WM task with reasonable confidence, while the *latent*-factor row (0.72) carries a range from
0.41 to 1.00 reflecting the genuine and unresolved disagreement. Sleep studies use single tasks
(n-back, Sternberg, digit span), so the 0.48 row is the one that will actually be applied.

**Lyall DM, et al. Cognitive test scores in UK Biobank: data reduction in 480,416 participants and
longitudinal stability in 20,346 participants. *PLoS One*. 2016;11(4):e0154222.** Used here for the
reasoning-task lower bound.

> "suggested a one-factor solution (eigenvalue = 1.60), which accounted for around 40% of the
> variance"

A first factor explaining ~40% of variance across four tests implies a mean loading of about
√0.40 ≈ **0.63**. Reasoning is the strongest of the four UK Biobank tests (it has the highest
inter-test correlation, r = 0.391 with numeric memory, and the best retest stability, ICC = 0.65),
so 0.63 is the *floor* for a reasoning task, which is why the range in the table starts there.
**HONEST FLAG:** the 0.80 point estimate for reasoning tasks is psychometric convention, not a
number I retrieved from a source. It is the least well-sourced entry in the table. Its effect on
conclusions is small, because Route A applies to most reasoning outcomes anyway.

---

## 5. The validation: two independent routes to the same discount

This is the part that makes the recommendation defensible rather than merely plausible.

**Estimate (i) — the measured domain gradient.** `lim2010` pooled 70 articles and 147 cognitive
tests under the *same* exposure (short-term total sleep deprivation) and reported effects by domain.
The ratio of the reasoning effect to the simple-attention effect is a *directly measured*
vigilance-to-reasoning discount that requires no psychometric theory at all:

```
g_reasoning / g_lapses  =  0.125 / 0.762  =  0.164        95% CI [-0.025, 0.354]
```

**Estimate (ii) — the psychometric g-loading of a simple-RT task**, from §4: `r_g` = 0.25
[0.20, 0.35].

**These two agree to within a factor of 1.5.** They come from completely different places — one from
the sleep-deprivation meta-analytic literature, one from the differential-psychology literature on
reaction time and intelligence — and neither was constructed with the other in mind. That agreement
is the main empirical result of this document.

**Recommended pooled discount for vigilance → IQ: 0.20, plausible range 0.15 to 0.35,
i.e. 3.0 IQ-equivalent points per 1.00 of vigilance g (range 2.2 to 5.2).**

### Cross-check against the direct IQ measurement

| Route | Calculation | Result |
|---|---|---|
| B, from the PVT | 0.762 × 0.25 × 15 | **2.9 IQ points** (range 2.3–4.0 over `r_g` 0.20–0.35) |
| A, from reasoning | 0.125 × 0.80 × 15 | **1.5 IQ points** (1.9 if reasoning treated as pure g) |
| A, from a real IQ test | `binks1999` 95% CI lower bound | **decrement worse than 1.8 points excluded** |
| Naive 1:1 | 0.762 × 1.00 × 15 | 11.4 points — **6.2× the permitted bound** |

Three legitimate routes land in a **1.5 – 4.0 IQ-point band** for acute total sleep deprivation. The
naive route lands outside what direct measurement allows. The conversion in §1 is calibrated to the
former.

---

## 6. Vigilance decrements are not IQ decrements: the gap, quantified

The task brief asked for this to be explicit. Here it is, four ways, all from retrieved sources.

**(1) In the acute-deprivation meta-analysis, the domain gradient is ~6-fold.** `lim2010`, same 70
articles, same exposure:

| Domain (accuracy measures) | Pooled g | 95% CI |
|---|---|---|
| Simple attention — **lapses** | **−0.762** | [−0.948, −0.576] |
| Working memory | −0.555 | [−0.741, −0.368] |
| Complex attention | −0.479 | [−0.640, −0.318] |
| Short-term memory (recall) | −0.383 | [−0.647, −0.118] |
| Processing speed | −0.245 | [−0.500, 0.010] |
| **Reasoning** | **−0.125** | [−0.268, **+0.016**] |

Reasoning is the **smallest effect in the entire meta-analysis and the only cognitive-accuracy
domain whose CI crosses zero.** The most sleep-sensitive and the most g-loaded outcomes are at
*opposite ends* of the same table.

**(2) The same ordering appears in the partial-restriction meta-analysis.** `lowe2017`: attentional
lapses g = −0.516, sustained attention g = −0.409, executive functioning g = −0.324, long-term
memory g = −0.192, and **intelligence reported as null**.

**(3) The same dissociation appears experimentally in the target age group.** `campbell2024`, ages
9.9–22.8, within-subject, 4 nights at 7 vs 8.5 vs 10 h TIB: PVT signal-to-noise fell by 0.77 dB
across the 3-hour TIB range (p < .0001 at every step), while **Sternberg working memory was entirely
unaffected** (F(2,729) = 0.68, p = .51). One measure moved a lot; the other did not move at all, in
the same people, in the same week.

**(4) It appears in the child observational literature too.** `astill2012` found sustained attention
— the most sleep-sensitive adult domain — to be the *least* associated with habitual sleep duration
in 5–12 year olds (r = 0.02, k = 15), and flagged the reversal itself: "Quite unlike typical findings
in adults, sleep duration was not associated with sustained attention and memory."

**The practical consequence.** A headline of the form "sleep restriction produced a large cognitive
deficit (g = −0.8)" is, in the sleep literature, almost always a statement about *vigilance*. It
licenses claims about lapses, microsleeps, driving safety, and moment-to-moment reliability. It does
**not** license a claim about intelligence, and converting it as if it did overstates the IQ effect
by about fivefold.

---

## 7. What this conversion does *not* cover, and the three gaps that matter

**Gap 1 — acute performance decrement is not the same question as chronic ability development, and
this is the biggest limitation of everything above.** Every validation in §5 comes from *acute*
manipulations measuring *same-day* performance. The target subject's exposure is three years of
habitual 5–6 h weekday sleep. The mechanism by which chronic short sleep would lower a *measured
ability score* is not same-day slowing; it is degraded consolidation of learning, less effective
absorption of instruction, and possibly altered development, accumulating over years. The acute
literature bounds the former and says nothing about the latter. **A model that applies §5's 1.5–4
point acute band to a three-year chronic exposure will understate the effect if the chronic
mechanism is real, and there is direct evidence that it is:**

- `huang2016` (same "Need for Sleep" adolescent cohort as `lo2016`): GRE vocabulary cued recall
  under 5 h vs 9 h TIB, g = −0.41 (retention phase) and −0.33 (after a review session). That is a
  *learning* outcome, not a performance outcome, and it is 3× the acute reasoning effect. At a
  vocabulary-learning `r_g` of ~0.6 this is ~3.7 IQ-equivalent points from a single week.
- `fjell2023`: −2.4 to −2.9 IQ points on an extracted g factor in *habitual* short sleepers,
  cross-sectionally, in 47,029 people. This is the best anchor available for a chronic exposure, and
  it should carry more weight for this subject than any acute record — subject to it being
  observational and non-causal, which the authors state explicitly.

The honest summary for the chronic case is therefore **roughly 2–3 IQ-equivalent points, sourced
from a cross-sectional association rather than an experiment**, with the acute experimental
literature providing a consistent but not directly applicable 1.5–4 point band.

**Gap 2 — I could not source an achievement-to-g loading.** `dewald2010` and `astill2012` give
well-powered school-performance associations (r = 0.069 and r = 0.09 for habitual duration), and
grades are the outcome a reader most intuitively cares about. But converting a grades effect to IQ
points requires the g-loading of an achievement composite, and I did not retrieve a citable source
for it. The only figure I encountered is *secondhand inside* `sadeh2003`, which cites Arcia et al.
(1991) for digit span correlating r = .56 with reading and r = .58 with mathematics on the California
Achievement Test — suggestive of an achievement `r_g` around 0.5–0.7, but I did not retrieve Arcia
and will not treat it as sourced. **Row E of §1 therefore declines the conversion.** A shard with
access to the education literature should fill this in.

**Gap 3 — no study measures the quantity the conversion actually needs.** As stated in §4, every
`r_g` is a between-person correlation, and what we want is the propagation of a within-person
perturbation. Nobody has, to my knowledge, sleep-deprived a large sample and administered both a PVT
and a full-scale IQ test with enough power to estimate the mapping empirically. `binks1999` is the
closest attempt and it is underpowered (minimum detectable effect d = 0.72 ≈ 11 IQ points) and
confounded (the deprived arm was 2.7 Shipley IQ points higher at screening). **The single most
valuable study anyone could run in this area is a well-powered within-subject sleep-restriction trial
with a full psychometric IQ battery alongside a PVT.** It does not exist.

---

## 8. Summary card for the downstream model

```
IQ_points = 15 * r_g * g_task

r_g:   extracted g factor / full IQ test  1.00   [0.90, 1.00]
       reasoning / gF task                0.80   [0.63, 0.90]
       latent working-memory factor       0.72   [0.41, 1.00]
       single working-memory task         0.48   [0.45, 0.55]
       choice RT / mental speed           0.40   [0.24, 0.49]
       PVT / vigilance / simple RT        0.20   [0.15, 0.35]   <- recommended, pooled
       school performance / grades        DECLINE - not sourced

Prefer a directly measured general-ability outcome over any conversion.
Treat 15 * r_g * g_task as an UPPER BOUND (the perturbation is not generic w.r.t. g).
Never use r_g^2 (understates), never divide by r_g (wildly overstates).

Calibration checks the conversion must reproduce:
  acute total SD, from PVT   -> 2.3 to 4.0 IQ pts
  acute total SD, direct IQ  -> decrement worse than 1.8 pts EXCLUDED (binks1999)
  habitual short sleep       -> 2.4 to 2.9 IQ pts (fjell2023, authors' own conversion)
  naive 1:1 from PVT         -> 11.4 pts, FALSIFIED (6.2x the permitted bound)
```

---

## 9. Sources cited in this document

| Purpose | Citation | ID | Verified |
|---|---|---|---|
| Simple/choice RT–intelligence correlations, n = 900 | Deary IJ, Der G, Ford G. Reaction times and intelligence differences: A population-based cohort study. *Intelligence*. 2001;29(5):389–399. | doi:10.1016/S0160-2896(01)00062-9 | Crossref ✓ (not in PubMed) |
| Mental speed–intelligence, 1,146 correlations | Sheppard LD, Vernon PA. Intelligence and speed of information-processing: A review of 50 years of research. *Personality and Individual Differences*. 2008;44(3):535–551. | doi:10.1016/j.paid.2007.09.015 | Crossref ✓ (not in PubMed) |
| WM–g true-score correlation, 86 samples | Ackerman PL, Beier ME, Boyle MO. Working memory and intelligence: the same or different constructs? *Psychological Bulletin*. 2005;131(1):30–60. | doi:10.1037/0033-2909.131.1.30, PMID 15631550 | Crossref ✓ PubMed ✓ |
| Latent WMC–Gf correlation, 3,168 subjects | Kane MJ, Hambrick DZ, Conway ARA. Working memory capacity and fluid intelligence are strongly related constructs. *Psychological Bulletin*. 2005;131(1):66–71. | doi:10.1037/0033-2909.131.1.66, PMID 15631552 | Crossref ✓ PubMed ✓ |
| UK Biobank cognitive factor structure | Lyall DM, et al. Cognitive test scores in UK Biobank: data reduction in 480,416 participants and longitudinal stability in 20,346 participants. *PLoS One*. 2016;11(4):e0154222. | doi:10.1371/journal.pone.0154222 | see `kyle2017.yaml` |
| SD → IQ-point conversion precedent | Fjell AM, et al. Is short sleep bad for the brain? Brain structure and cognitive function in short sleepers. *J Neurosci*. 2023;43(28):5241–5250. | doi:10.1523/JNEUROSCI.2330-22.2023, PMID 37365003 | `fjell2023.yaml` |
| Per-domain acute gradient | Lim J, Dinges DF. A meta-analysis of the impact of short-term sleep deprivation on cognitive variables. *Psychological Bulletin*. 2010;136(3):375–389. | doi:10.1037/a0018883, PMID 20438143 | `lim2010.yaml` |
| Per-domain restriction gradient | Lowe CJ, Safati A, Hall PA. The neurocognitive consequences of sleep restriction: A meta-analytic review. *Neuroscience & Biobehavioral Reviews*. 2017;80:586–604. | doi:10.1016/j.neubiorev.2017.07.010, PMID 28757454 | `lowe2017.yaml` |
| Direct test-day IQ measurement | Binks PG, Waters WF, Hurry M. Short-term total sleep deprivations does not selectively impair higher cortical functioning. *Sleep*. 1999;22(3):328–334. | doi:10.1093/sleep/22.3.328, PMID 10341383 | `binks1999.yaml` |
| Age-matched experimental dissociation | Campbell IG, et al. Sleep restriction and age effects on distinct aspects of cognition in adolescents. *Sleep*. 2024;47(12):zsae216. | doi:10.1093/sleep/zsae216, PMID 39283917 | `campbell2024.yaml` |
| Child intelligence subdomain | Astill RG, et al. Sleep, cognition, and behavioral problems in school-age children: A century of research meta-analyzed. *Psychological Bulletin*. 2012;138(6):1109–1138. | doi:10.1037/a0028204, PMID 22545685 | `astill2012.yaml` |
