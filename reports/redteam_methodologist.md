# Red-team review: METHODOLOGIST

Adversarial review of the statistical methodology. Every quantified claim below was produced by
running the project's own code with one choice changed at a time. The perturbation harness
(`tmp_s19/rt_harness.py`) reproduces the published Q2/Q3 headline numbers to three decimal places
before any perturbation is applied, so the movements reported are attributable to the changed
choice and not to Monte Carlo noise or a different code path.

Severity key: **CRITICAL** = invalidates a headline number as stated; **MAJOR** = materially changes
a headline number; **MINOR** = should be documented.

Reproduction of the baseline (harness vs `results.json`):

| quantity | harness | published |
|---|---|---|
| vigilance g at subject dose | −0.873 [−2.854, +0.580] | −0.874 [−2.847, +0.580] |
| overall neurocognitive g | −0.252 [−0.785, +0.159] | −0.252 [−0.783, +0.159] |
| measured FSIQ change (points) | −0.699 [−6.673, +6.921] | −0.700 [−6.699, +6.951] |

---

## CRITICAL

### 1. The mortality channel uses a categorical contrast that the project's own evidence station explicitly instructs it not to use. The life-expectancy headline is 4–7× too large.

**Location:** `src/model.py:246–252` (`mort = derived["mortality_rr_short_sleep"]`, `log_rr_mort`,
`hr_while_exposed`); `src/analysis_set.py:147–153`; the instruction it violates is
`evidence/s13_mortality/mortality_summary.md` §8.5.

`model.py` builds the mortality hazard from `mort["value"] = 1.12`, the categorical
"short sleep vs 7–8 h" pooled RR from `cappuccio2010`. The same dictionary it reads from also
carries `dose_response_at_5h: 1.04` and `dose_response_at_6h: 1.01`. Neither is referenced anywhere
in the codebase (verified by grep across `src/`). The subject's modelled mean TST is 5.59 h, which
sits between those two anchors.

This is not an oversight the modeller could have missed. The mortality shard's own summary
contains a section headed "Explicit instructions to the downstream model" whose first item is:

> **1. Use the dose-specific spline values (RR 1.01-1.06 at 5-6 h), not the categorical 1.12-1.14.**
> **2. Set the referent at 7 h, not 8 h.**
> **3. Apply a residual-causal fraction of 0.25 (0.0-0.50)** ...

`model.py` implements instruction 3 and ignores instructions 1 and 2. The same shard tabulates a
multiplicative correction chain in which the dose correction alone retains **0.09–0.50** of the
published log hazard, and a male-sex correction retains **0.2–1.0**. `model.py` applies neither.

Quantified, re-running the life-table chain with the shard's own correction factors:

| specification | window (mo) | permanent (mo) | **total LE change (mo)** | cigarette-equiv/day |
|---|---|---|---|---|
| as published (correction (c) only) | −0.046 | −0.176 | **−0.223 [−0.937, −0.009]** | 2.48 |
| + shard's dose correction U(0.09, 0.50) | −0.012 | −0.045 | **−0.058 [−0.329, −0.002]** | 0.65 |
| + dose and male-sex correction | −0.006 | −0.024 | **−0.031 [−0.223, −0.001]** | 0.35 |

Equivalently: the model retains a median **25%** of the published log hazard in the exposure window,
where its own station's chain gives **3.3%**. Using the dose-appropriate RR directly (1.022 by
interpolation at 5.59 h) gives a total of **−0.043 months**, 5.1× smaller than published.

The headline `life_expectancy_change_months_total` = −0.224 months and
`cigarette_equivalent_per_day_for_3_years` = 2.48 are both overstated by roughly 4–7×.

### 2. `domain_profile_chronic_restriction` pools a meta-analytic composite together with its own three constituent sub-domains, as four independent studies. This violates gate G6 and biases the headline toward zero while making its interval 2.5× too narrow.

**Location:** `src/analysis_set.py:72–81` (the four `lowe2017` selectors);
`src/synthesis.py:346–375` (`dedupe_by_cohort`); `src/model.py:126` (`pooled(...)`).

The four selectors are `overall_neurocognitive_performance_pooled_across_domains`,
`sustained_attention_pooled`, `executive_functioning_pooled` and `long_term_memory_pooled` — all
from Lowe, Safati & Hall 2017, a single meta-analysis of 61 studies / 71 populations. The first is
the pooled estimate *across* the other three. The same primary studies are counted twice, once in
the composite and once in their domain. `dedupe_by_cohort` does not catch it because all four rows
carry `cohort_family: None`, and the function treats a missing family as "independent". Gate G6
("no family contributes > 1 effect per outcome without RVE — enforced") is therefore enforced only
by the presence of an optional free-text field; a null value silently bypasses it. Running my own
G6 audit over the resolved analysis set finds two violations (`lowe2017` × 4 in this parameter,
`duraccio2024` × 2 in a parameter that is not used for a headline number).

Two consequences, both bad for the published number:

- **The point estimate is biased toward zero.** Inverse-variance weighting gives the largest weight
  to `long_term_memory_pooled`, which has the smallest SE (0.0621) *because it is the only one of
  the four whose p-value was reported exactly* (p = 0.002, so SE is identified); the other three
  SEs are upper bounds backed out of "p < 0.001". It is also the smallest effect (−0.192). So the
  pooled mean is dragged toward the least-affected domain by an artefact of reporting precision,
  not of evidential weight. Pooled mu = −0.320 versus the correct single overall estimate −0.383.
- **The interval is far too narrow.** Four correlated rows masquerading as four independent studies
  drive the estimated between-study SD down to tau = 0.109 (REML says exactly 0.000, I² = 0%).

Quantified movement in the headline `overall_neurocognitive_g_at_subject_dose`:

| specification | headline |
|---|---|
| as published (4 nested rows) | **−0.252 [−0.785, +0.159]** |
| `lowe2017` overall row only, same tau prior | −0.292 [−1.629, +0.900] |
| `lowe2017` overall row only, sampling error only | −0.302 [−0.823, +0.036] |

The point estimate is 16–20% too small and the honest interval is between 1.05× and 2.5× wider.

The nesting also manufactures a spurious bias signal that the report presents as a diagnostic:
Egger's intercept on this parameter has p = 0.0062 and PET-PEESE "recommends" **+0.534** — the
opposite sign to the effect. Nested composite-plus-subdomain estimates are guaranteed to correlate
effect size with precision, so that funnel asymmetry is a symptom of the double count, not of
publication bias. Neither value is used, but neither is flagged as structurally uninterpretable.

### 3. Where k ≤ 2, the posterior predictive interval is 100% prior-determined. Two headline numbers are intervals constructed by a prior with no data content.

**Location:** `src/synthesis.py:101–156` (`pool_bayes_grid`), specifically the marginal likelihood at
line 128 and `pred_draws = mu_draws + rng.normal(0,1,n) * tau_draws` at line 142; consumed at
`src/model.py:159–161`.

For k = 1 the profile marginal likelihood of tau is *exactly constant*. I verified this analytically
and numerically: with y = −0.89, se = 0.3282, `log p(y|tau)` evaluates to 0.000000000000 at
tau ∈ {1e−6, 0.05, 0.2, 0.8, 3.0}, because `log(v) + log(1/v) = 0` and the weighted residual sum is
identically zero. The tau posterior is therefore the half-normal prior verbatim: sampled tau median
0.4383 against a prior median of 0.6745 × scale = 0.4427; sampled mean 0.5220 against a prior mean
of 0.5237. The predictive interval width is exactly **12.8 × se** by construction, independent of
anything in the data (verified: scaling se by 0.5×, 1×, 2× gives width/se = 12.732 in all three cases).

`encoding_capacity_persisting` has k = 1 (`cousins2018` alone):

| specification | headline |
|---|---|
| as published | **−0.886 [−2.968, +1.247]** |
| sampling error only (the only information present) | −0.890 [−1.532, −0.248] |

The published interval is 3.3× wider and crosses zero; the data alone excludes zero. The report
calls this "the learning-loss channel", so an interval that admits a large *benefit* from sleep
restriction is not a cosmetic issue.

`residual_deficit_after_recovery_sleep` (k = 2) has the same defect: published −0.451
[−1.546, +0.682], with REML tau = 0.000 and I² = 0%.

The decisive internal check: `tests/test_calibration.py::test_bayes_grid_tau_agrees_with_reml`
asserts `|reml_tau − grid_tau| < 0.05`, on a synthetic 5-study dataset. Applied to the project's
actual analysis-set parameters:

| parameter | k | REML tau | grid tau | \|diff\| | passes tol 0.05 |
|---|---|---|---|---|---|
| `pvt_g_large_dose` | 5 | 0.6942 | 0.6929 | 0.0013 | yes |
| `domain_profile_chronic_restriction` | 4 | 0.0000 | 0.1093 | 0.1093 | **no** |
| `habitual_short_sleep_g_observational` | 2 | 0.0000 | 0.1724 | 0.1724 | **no** |
| `residual_deficit_after_recovery_sleep` | 2 | 0.0000 | 0.2347 | 0.2347 | **no** |
| `encoding_capacity_persisting` | 1 | 0.0000 | 0.4383 | 0.4383 | **no** |

**Four of the five primary parameters fail the project's own agreement tolerance.** The docstring of
`synthesis.py` says "a sampler that disagrees with the exact posterior is broken", and the two-method
cross-check is run only grid-vs-NUTS — the same model with the same prior, which cannot detect this.
The one comparison that would have caught it (grid tau vs REML tau on the real inputs) is run only
on a synthetic example that happens to have tau > 0.

### 4. Route C generates the entire upper limb of the headline IQ interval, is transported with the wrong denominator, and the four routes are not independent as documented.

**Location:** `src/model.py:168–196`; the comment "Four independent routes, deliberately kept
separate before averaging" at line 169.

Three separate defects compound here.

**(a) Route C is the only positive route and it owns the upper half of the interval.** `route_c` =
`N(+3.6, 2.768) × transport`, from `binks1999`'s WAIS-R short form after 34–36 h total deprivation,
under a convention where positive = better. Its published summary is +2.80 [−1.50, +8.95]. The
mixture's 97.5th percentile (+6.93) is essentially route C's own 91.7th percentile (+6.87) — which is
exactly what a 30%-weight component contributes to a 2.5% tail. Dropping route C:

| specification | measured FSIQ change (points) |
|---|---|
| as published (w = .35/.25/.30/.10) | **−0.699 [−6.673, +6.921]** |
| route C removed, A and B reweighted | −1.249 [−7.465, **+0.584**] |

The median moves 79% and the upper limit moves from +6.92 to +0.58. The claim that the subject
might currently be testing **7 IQ points above** his rested self is a single-study artefact.

**(b) Route C is transported with the chronic-restriction denominator and gets no
total-deprivation-to-chronic conversion.** Route B, from the same kind of source (`lim2010`, total
deprivation), correctly applies `chronic_scale ~ U(0.5, 0.9)` before `transport`. Route C applies
`transport` alone. `transport = (deficit/3.7)^gamma`, and 3.7 h is the *chronic-restriction* studied
contrast; for a 34–36 h total-deprivation protocol the studied deficit is ~8.7 h, giving
transport ≈ 0.32 rather than 0.85. Giving route C route B's structure moves route C from +2.80 to
+1.91 and the mixture upper limit from +6.92 to **+5.01**.

**(c) Routes A and B are the same study.** Route A's `discount` is
`lim2010/ratio_reasoning_to_simple_attention_g` = 0.164; route B's numerator is
`lim2010/reasoning_and_crystallized_intelligence_accuracy` = −0.125. The ratio's numerator *is* the
route B estimate (0.125/0.762 = 0.164 — the project's own
`test_lim2010_reasoning_to_lapses_ratio` states this). So routes A and B, carrying a combined
weight of 0.60, are both driven by a single reasoning-domain estimate from a single meta-analysis.
The header comment asserting independence is false, and the mixture is not the model-averaging over
independent identification strategies it is described as.

**(d) The weights are unjustified and dominate the interval.** Between-route variance is
5.163 and within-route variance is 5.335, so **49.2% of the reported IQ variance is pure route
choice** — a modelling decision, not a measurable quantity. Route-only medians span +2.80 (C) to
−1.80 (A), a 4.6-point range, and equal weights give −0.674 while dropping C gives −1.249.
On whether averaging is legitimate at all: routes A, B and D are all standardized-effect chains
scaled into IQ points and are at least commensurable. Route C is a *directly measured* FSIQ change
in raw points from an acute total-deprivation protocol. Pooling a measured quantity with three
constructed proxies under hand-set weights is not Bayesian model averaging (no marginal likelihoods
are computed, and the weights carry no data), it is a weighted opinion. The mixture's bimodality is
real, not an artefact of my analysis — but reporting its median as the answer is misleading, because
the median of a bimodal mixture is a value that no component considers likely.

### 5. The permanence model conflates a probability of an event with a fraction of a magnitude. The two permanence probability headlines move by 33–275×, and a third of the "permanent change" posterior is a permanent *gain*.

**Location:** `src/model.py:200–201` (`perm_frac = rng.beta(1.2, 18.0, N_DRAWS)`); the cited
justification is `structural_permanence_probability` in `src/analysis_set.py:176–180`.

`Beta(1.2, 18)` appears nowhere except as a literal in `model.py`. Grep across `src/`, `spec/`,
`reports/*.md` and `evidence/*/*.md` returns only lines 200–201 and 337/579. It has no source
attribution, no `DERIVED_PARAMS` entry, and no evidence record — unlike essentially every other
prior in the project. The inline comment justifies it by "P(detectable permanent structural change)
~ 0.03", which is `structural_permanence_probability` = 0.03 [0.01, 0.10]. Two problems:

- The distribution does not match the cited quantity. `Beta(1.2, 18)` has mean 0.0625 (2.1× the
  cited 0.03) and a 97.5th percentile of 0.202 (2× the cited upper bound of 0.10).
- More fundamentally, 0.03 is the **probability that permanent change exists**. `perm_frac` is used
  as a **multiplicative fraction of the deficit that persists**. These are different objects.
  Multiplying by a small fraction produces a smooth, tiny, symmetric number; the coherent
  specification is a mixture — with probability p the deficit persists, otherwise it does not.

Quantified, re-specifying permanence as the coherent Bernoulli mixture at the project's own cited
probabilities:

| specification | permanent change (points) | P(loss > 1 pt) | P(loss > 3 pts) |
|---|---|---|---|
| as published, `Beta(1.2,18)` shrinkage | −0.020 [−0.532, +0.570] | **0.00594** | **0.000115** |
| Bernoulli p = 0.03 (the cited value) | 0.000 [0.000, 0.000] | 0.01287 | **0.00385** |
| Bernoulli p = 0.10 (cited upper bound) | 0.000 [−1.805, +1.144] | 0.04188 | 0.01277 |
| Bernoulli p = 0.25 (`durable_neurobiological_change_any_kind`, unused) | 0.000 [−3.490, +4.044] | 0.10404 | 0.03157 |

`prob_permanent_loss_exceeds_3_points` moves from 0.00012 to 0.0038 (33×) at the cited probability
and to 0.032 (275×) at the record's own `durable_neurobiological_change_any_kind` = 0.25, a field
that is defined in `DERIVED_PARAMS` and never read.

Separately: because `perm_frac` multiplies the full mixture including the positive route C,
**P(iq_permanent > 0) = 0.342**. A third of the posterior for "permanent change in adult cognitive
ability" is a permanent *improvement* produced by shrinking a positive draw toward zero. The
headline `permanent_ci_includes_zero: true` is partly manufactured by this. `perm_frac` is
documented as "the share that does not recover"; a share of a benefit is not a coherent reading.

### 6. Not one of the six simulated recovery policies delivers adequate sleep, and the policy the report itself prescribes is absent from the menu. Every recovery percentage in Q8/Q9 is capped by an uncited constant.

**Location:** `src/recovery.py:85–102` (`policies`, `policy_weekly_balance`), `:78–82`
(`floor_from_policy`); `src/model.py:337–353`, `:356`.

`sustained_tst(tib)` = `min(0.237 + 0.8915 × tib, 8.9)`, so 9 h in bed yields 8.26 h of sleep
against a modelled need of 8.70 h. Mean nightly balance versus need, at the median need:

| policy | balance (h/night) |
|---|---|
| status quo 5.5 h weekday | −3.050 |
| 7 h every night | −2.222 |
| 8 h every night | −1.331 |
| 8 h + scheduled nap | −0.831 |
| 9 h every night | −0.439 |
| weekday 5.5 h / weekend 10 h | −2.486 |
| *9.5 h every night (not in the menu)* | *+0.006* |
| *9 h + 1 h nap (not in the menu)* | *+0.200* |

Every simulated policy still under-sleeps, so `floor_from_policy` is strictly positive for all of
them and no trajectory can approach full recovery. Meanwhile `maintenance_dose_time_in_bed_h` — the
report's own prescription — is **9.50 h**, which is precisely the value that zeroes the balance and
is *not one of the simulated policies*. The reported ceiling, "68.5% of the recoverable deficit
recovered at 52 weeks under the best policy", is therefore an artefact of an incomplete menu. At
9.5 h TIB the ceiling is `1 − residual_frac` ≈ **92%**.

The ceiling is set by `floor_from_policy = impairment × shortfall/(shortfall + 1.0)`, an arbitrary
saturating function with a hard-coded 1.0 h scale, no citation, and no multiverse branch. Varying
that single constant:

| saturation scale S | status quo | 8 h/night | 9 h/night |
|---|---|---|---|
| 0.5 h | 14% | 27% | 53% |
| **1.0 h (as published)** | **25%** | **43%** | **69%** |
| 2.0 h | 40% | 60% | 82% |
| 4.0 h | 57% | 75% | 90% |

Every percentage in `pct_of_recoverable_deficit_recovered` — six policies × seven timepoints, 42
reported numbers with intervals — is a direct function of an uncited scalar that moves them by a
factor of 2 to 4. `residual_frac = rng.beta(1.3, 12.0)` (`model.py:337`) has the same provenance
problem: no citation anywhere, and it alone sets the asymptote at `100 × (1 − residual_frac)`.

A labelling error compounds this: the metric is called "% of *recoverable* deficit recovered" but is
computed as `(start − traj)/start`, i.e. against the *total* deficit. A policy that recovers
everything recoverable therefore reports ~92%, not 100%.

---

## MAJOR

### 7. The project computes evidence of a small-study effect in its primary cognition parameter, reports it, and then propagates none of it. Combined with the G4 response, no bias correction of any kind reaches a headline number.

**Location:** `src/model.py:78–79` (`pet_peese`, `trim_and_fill` written into the record),
`:145–146` (headline uses the uncorrected `pred_draws`).

For `pvt_g_large_dose`: trim-and-fill fills 2 studies and moves the inverse-variance mean from
−0.967 to −0.691, a **29% attenuation**; PEESE gives −0.754 and PET gives −0.243 against a pooled
mu of −1.116. Propagating each as a level shift on the predictive:

| bias treatment | vigilance g at subject dose |
|---|---|
| as published (none) | **−0.874 [−2.866, +0.579]** |
| trim-and-fill (Duval–Tweedie L0) | −0.649 [−2.562, +0.826] |
| PEESE | −0.580 [−2.469, +0.906] |
| PET | −0.177 [−1.927, +1.396] |

A 26% attenuation under the mildest defensible correction, 80% under the harshest. Route A, the
highest-weighted IQ route, scales linearly with this. I will not argue PET's −0.24 is right — with
k = 5, PET-PEESE is unstable and its p = 0.81 means the conditional estimator has simply failed to
detect an effect. But trim-and-fill's −0.69 is a standard sensitivity analysis, it is computed and
stored in `results.json`, and it appears in no headline number and in no multiverse branch.

**On gate G4 and risk of bias:** kappa on RoB judgement is 0.36 against a 0.80 threshold, and the
project's response is to not use RoB as a weight. Taken alone that is defensible — weighting by a
field with kappa 0.36 would inject noise. But `poolable_effects` extracts `rob` and *nothing* reads
it: not as a weight, not as an exclusion criterion, not as a sensitivity branch. Combined with the
ignored funnel diagnostics above, the result is that **no risk-of-bias or small-study adjustment of
any kind reaches any reported number**, in a synthesis whose primary cognition parameter rests on
five small laboratory studies with I² = 79%. "We did not use the unreliable field" answers the
narrow question and leaves the substantive one — that the evidence base is unadjusted for bias —
unaddressed. Not using a broken instrument is not the same as concluding the thing it measures is
absent.

### 8. `studied_deficit_h = 3.7` is a bare scalar with no uncertainty, sitting multiplicatively in the middle of every cognition and psychiatric number. The 26× duration extrapolation is handled by nothing at all.

**Location:** `src/model.py:137–140`.

```python
studied_deficit_h = 3.7
gamma = rng.uniform(0.8, 1.5, N_DRAWS)
dose_ratio = np.clip(deficit_nightly / studied_deficit_h, 0.0, 2.0)
transport = dose_ratio ** gamma
```

`gamma` carries uncertainty about the *shape* of the dose-response; the *location* of the anchor
carries none. Reconstructing the anchor from the pooled studies' own `dose_h`/`referent_h` fields
(TIB 5, 6, 7, 4, 6 → mean 5.6 h → TST 5.23 h via the project's own `banks2010` regression → deficit
3.47 h against an 8.7 h need) gives ~3.5 h, not 3.7 h. Sensitivity of the headline:

| studied_deficit_h | transport factor | vigilance g |
|---|---|---|
| 3.0 | 1.074 | −1.109 [−3.647, +0.737] |
| **3.7 (as published)** | **0.851** | **−0.873 [−2.854, +0.580]** |
| 4.5 | 0.683 | −0.698 [−2.283, +0.464] |

A ±20% change in an asserted constant moves the headline by ±25%, and that movement appears in no
interval. By contrast, widening `gamma` to U(0.5, 2.5) moves the median only from −0.873 to −0.823:
the modelled uncertainty is on the axis that matters least. Setting gamma = 1 (pure linearity) gives
−0.899. **The functional-form uncertainty is a rounding error next to the anchor uncertainty that is
not modelled at all.**

**Duration.** The protocols run 5–14 nights; the exposure is 1040 nights, a 26× extrapolation, and
there is no term for it. The model implicitly asserts a stationary steady state. That assertion is
not neutral: it could be wrong in either direction (continued accrual beyond the observed
plateau, versus habituation and partial weekly repayment), and the exposure engine's own
`tau_accrue_days = (7.0, 1.67)` establishes that the modeller believes accrual dynamics exist. I
tested the one duration-related quantity the engine does compute (see clean bill 21) and it changes
nothing, so the objection is specifically that no *parameter* represents duration extrapolation,
not that a specific alternative is available.

### 9. The predictive-versus-mean choice is defensible in principle, applied to the wrong variance component, applied to 5 of 12 uncertain inputs, and it determines whether the two headline cognition numbers exclude zero.

**Location:** `src/model.py:142–149` and the justifying comment; `src/synthesis.py:141–142`.

The user's framing asked whether the choice is right. My answer: the *intent* is right and the
*implementation* is not.

**(a) It is the wrong variance.** In the normal-normal hierarchical model, `theta_j ~ N(mu, tau²)`
are **study-level** true effects, so `pred_draws = mu + tau·z` is a draw of a **new study's true
mean** — the spread attributable to protocol, task, population and analysis differences across
studies. The comment justifies using it by citing trait-like individual vulnerability
("ICC 0.675, vandongen2004"), which is a **between-person** quantity. These are different variances
that happen to be numerically similar here (tau = 0.69). Each `theta_j` is already a standardized
mean difference, i.e. already expressed in units of the between-person SD; the between-person spread
in response is a property *within* each study and should be recovered from the reported
within-study distribution of individual responses (van Dongen 2004 gives it), not from tau. Using
tau as a stand-in is a category substitution that happens to land in the right order of magnitude.

**(b) It is applied to 5 of 12 uncertain inputs.** The predictive is used for the five g-scale
pooled parameters. Every other uncertain input is drawn as `rng.normal(value, se)` — the
CI-on-the-mean analogue, with no heterogeneity component: the `lim2010` reasoning effect
(`model.py:176`), the g-loading discount (`:171`), the `binks1999` FSIQ measurement (`:183`), the
depression d (`:228`), the T2D per-hour RR (`:271`) and — most consequentially — the mortality RR
(`:247`). `cappuccio2010` pools 27 independent cohort samples and the evidence record's own quote
states "significant heterogeneity between studies (P = 0.02)". Its predictive interval is far wider
than the CI 1.06–1.18 the model uses (se 0.0274).

Applying the project's own logic consistently to the mortality channel (tau consistent with
I² ≈ 50%, giving predictive sd ≈ 0.145):

| mortality uncertainty | total LE change (months) | P(LE change > 0) |
|---|---|---|
| CI on pooled mean (as published) | −0.224 [−0.938, −0.010] | 0.000 |
| predictive incl. tau, computed correctly | −0.152 [−1.739, **+0.510**] | **0.217** |

**The headline claim that the life-expectancy loss excludes zero survives only because the
mortality channel is the one place the predictive is not used.** Under the project's own stated
rationale the interval crosses zero and P(no loss) ≈ 22%.

**(c) It determines the Q2 sign conclusion.** Switching the g-scale parameters from the predictive
to the CI on mu:

| specification | vigilance g | overall neurocognitive g |
|---|---|---|
| predictive (as published) | −0.873 [−2.854, **+0.580**] | −0.252 [−0.785, **+0.159**] |
| CI on mu | −0.909 [−2.002, **−0.202**] | −0.256 [−0.617, **−0.024**] |

Both headline cognition intervals flip from including zero to excluding it. The project's choice is
the *conservative* one here, which is to its credit; but the choice, not the evidence, is what
decides the qualitative statement, and there is no multiverse branch for it.

### 10. The Q7 ranking places this exposure first only because the permanence discount applied to it is 4–16× harsher than the one applied to any comparator. The "same footing" claim in the report text is false.

**Location:** `src/model.py:307–332`, especially the note at `:329` ("All comparators are placed on
the same footing"); `src/analysis_set.py:191–200`;
`evidence/s18_comparators/comparator_scale.md`.

The retained fraction after each exposure's cessation/permanence adjustment, computed from the
comparator shard's own stated numerators and denominators:

| exposure | published / undiscounted | retained | basis |
|---|---|---|---|
| smoking 20/day | 1.8 / 8.4 mo | 21.4% | scaled down ~9× onto the `pirie2013` cessation gradient |
| western diet | 1.8 / 8.28 mo | 21.7% | `fadnes2022` delayed-cessation gradient |
| overweight BMI 27.5 | 1.8 / 2.9 mo | 62.1% | Model P, mild reversibility discount |
| alcohol | 3.0 / 3.16 mo | 94.9% | additive window + chronic (scaled *up*) |
| **this subject** | **0.224 / 3.868 mo** | **5.8%** | `permanent_residue U(0,0.12) × causal U(0,0.5)` |

Giving the subject each comparator's own retention fraction:

| retention applied to the subject | LE lost | rank of 8 | cigarette-equiv/day |
|---|---|---|---|
| **5.8% (as published)** | **0.22 mo** | **1** | **2.5** |
| 21.4% (smoking-like) | 0.81 mo | 2 | 9.0 |
| 62.1% (overweight-like) | 2.40 mo | 6 | 26.6 |
| 100% (no discount) | 3.87 mo | 8 | 43.0 |

The permanence discount is not arbitrary — it is grounded in sleep-specific reversibility evidence
(MR nulls, longitudinal MRI nulls), and that grounding is real. The objection is narrower and it
stands: the report *states* that all comparators sit on a common footing, and on the dimension that
matters most they do not, varying from 5.8% to 95% retention. `cigarette_equivalent_per_day_for_3_years`
= 2.48 is reported as a bare scalar with no interval, and it spans 2.5 to 43 across footings.

**In fairness, and importantly:** objections 1 and 10 push in opposite directions and largely
cancel for the *ordinal* conclusion. Applying both the dose correction and a comparator-matched
permanence retention:

| retention, on a dose-corrected base | LE lost | rank of 8 | cigarette-equiv/day |
|---|---|---|---|
| 5.8% | 0.056 mo | 1 | 0.6 |
| 21.4% | 0.207 mo | 1 | 2.3 |
| 62.1% | 0.601 mo | 1 | 6.7 |
| 100% | 0.968 mo | 2 | 10.8 |

**The rank-1 conclusion is robust; the point estimate is not.** The LE loss spans 0.056 to 0.97
months (17×) and the cigarette-equivalent 0.6 to 10.8/day across internally consistent
specifications, against a published point estimate of 0.224 months and 2.48 cigarettes/day.

### 11. The G3 rescue is not a diagnosis, because the reconciliation operation is fitted to the reference extractor's answer and cannot fail. The gate still fails on the scale that feeds the primary model.

**Location:** `src/agreement.py:136–139`, `:217–221`; `reports/agreement.json`;
`reports/adjudication.md`.

```python
if reconcile_sign:
    flip = np.sign(a) * np.sign(b) < 0
    b = np.where(flip, -b, b)
```

`a` is the reference (team 1 / truth) value. The rule flips team 2's value whenever it disagrees in
sign *with team 1*, using team 1's value to decide. It is therefore monotone — it can never reduce
agreement — and `spearman_like_sign_concordance` becomes exactly 1.0000 by construction (which is
what `agreement.json` reports). It is a fit-to-the-answer transformation, not the application of an
independent codebook rule.

A legitimate reconciliation would derive the intended orientation from each record's own
`direction_note`/`unit` field, independently of team 1's number, and would then be *able* to leave
residual disagreement — including cases where team 2 was right and team 1 wrong. The project's own
adjudication establishes that such cases exist: `lo2016::1` resolves to **+0.484**, which is
neither team's submitted number, and `huang2016::2` resolves to **EXCLUDE**, where neither team was
right. So the sign-flip model is known to be wrong for at least 2 of 9 adjudicated disputes, and
the reconciled statistic silently treats those as perfect agreement.

The adjudication itself is substantive and I do not dispute its verdicts: it retrieved nine sources,
quoted them verbatim, and its finding that the `lo2016` id collision came from
`make_blind_sample.py` keying on the non-unique `study_id::effect_index` is a real and well-evidenced
defect. What does not follow is that the *statistic* may be recomputed under a transformation whose
form is chosen by reference to the answer.

Two further points on the gate as written and as reported:

- `gates.md` G3 says "ICC >= 0.90" without naming the statistic. `agreement.py` computes three
  candidates and the passing headline (0.9706) is a sample-size-weighted mean across 11 scale
  groups. The project's own `gate_G3_all_scales_pass` is **false even after reconciliation**, and
  `icc_worst_value` reconciled is **0.8968 on `hedges_g`** — the scale that carries the entire
  primary cognition model. Raw, the same scale is **−0.3158**, i.e. worse than chance. The gate is
  reported as passed on a statistic under which the failing group is diluted by ten others,
  including six with ICC ≥ 0.99 on scales that feed nothing.
- The project labels `icc_2_1_pooled_standardized` as `ARTIFACT_DO_NOT_GATE_ON`, which is correct
  and is good practice. The same scepticism was not applied to the weighted mean.

### 12. `extraction_error_sd()` uses the sign-reconciled ICC while the module states the gate is applied to the raw figure; the fallback path means worse agreement produces *less* modelled uncertainty; and the scale constant is 43% too small.

**Location:** `src/analysis_set.py:261–276`.

Three defects, none of which moves a headline much — the impact finding is a partial clean bill —
but the third is a genuine structural inversion.

- The function reads `rep["continuous_sign_reconciled"]["per_scale"]["hedges_g"]["icc"]` = 0.8968,
  while `agreement.py`'s docstring says "the gate is applied to the raw figure". `DERIVED_PARAMS`
  describes the value as "the observed inter-extractor ICC on that scale", without saying which.
- `typical_g_sd = 0.55` is asserted as "spread of g values across the sampled cognitive effects".
  The actual SD of the 18 `hedges_g` re-extraction values is **0.786** (team 1) / 0.825 (pooled).
  Since `var_err ∝ typical_g_sd²`, the correct value is 0.1866 × 0.786/0.55 = **0.267**. This is
  corroborated independently: the model-free estimate from the sign-reconciled paired differences,
  `SD(a − b)/√2`, is **0.276**. The published 0.1866 is ~48% too small.
- **The fallback inverts the safeguard.** `var_err = var_true (1 − ICC)/ICC` is defined only for
  ICC ∈ (0, 1]. The raw `hedges_g` ICC is −0.3158, which makes the expression negative, and the
  guard `if not icc or icc <= 0: return 0.0` then adds **zero** extraction error. So if the module
  did what its sibling's docstring says — gate and inflate on the raw figure — the response to
  catastrophic inter-extractor disagreement would be to model no extraction error at all. The code
  is structurally incapable of representing "agreement so poor the values carry little information".

Impact on the headlines is small, and the reason is itself diagnostic: raising the extraction SD to
0.276 moves vigilance g only from −0.873 [−2.854, +0.580] to −0.876 [−2.864, +0.600], because
`tau_scale = 2 × median(se)` rises with the inflated SEs and the predictive width is partly pinned
to `median(se)` rather than to the data's dispersion (see 13). The `overall neurocognitive g`
interval does widen materially, from [−0.785, +0.159] to [−0.935, +0.308].

A fourth item, flagged but not claimed: the sign-reconciled paired differences on the g scale have
mean +0.1185 (SE 0.092, n = 18) — team 1's values are slightly *less* harmful than team 2's. The
model treats extraction error as pure added variance with no bias term. At n = 18 this is not
distinguishable from zero, so it is a limitation of the design rather than a demonstrated bias.

### 13. On the tau prior specifically: `2 × median(se)` is a double use of the data, but the direction of the concern is the opposite of the one posed. It does not understate uncertainty; it manufactures a floor and destroys invariance.

**Location:** `src/synthesis.py:110–114`.

Two experiments settle this.

**Does the data identify tau, or does the prior?** Holding se fixed and scaling the dispersion of y
about its mean by s, tau tracks the dispersion properly for k = 5: s = 0 → tau 0.107; s = 0.5 → 0.285;
s = 1 → 0.694; s = 2 → 1.183; s = 4 → 1.832. **The likelihood dominates for k = 5, and the concern
that the prior swamps the data is unfounded there.** (It is entirely founded for k ≤ 2 — see
objection 3.) But note the s = 0 row: perfectly homogeneous evidence still yields tau = 0.107 and a
predictive width of 1.07 g, so the prior manufactures a ±0.54 g floor on the individual interval
regardless of how consistent the studies are.

**Is the answer invariant to the precision of the evidence?** Holding y fixed and scaling all SEs by c:

| c | median(se) | tau | predictive width |
|---|---|---|---|
| 0.25 | 0.083 | 0.458 | 2.063 |
| 0.50 | 0.167 | 0.592 | 2.781 |
| **1.00** | **0.333** | **0.694** | **3.544** |
| 2.00 | 0.666 | 0.569 | 3.908 |
| 4.00 | 1.332 | 0.534 | 5.079 |

A 16-fold change in the evidence's precision changes the individual interval by only 2.5×, and tau
is *non-monotone* in c. That is the empirical-Bayes signature: the prior partially cancels the
information content of the standard errors.

Sensitivity of the headline across defensible priors, for the primary parameter:

| tau prior scale | tau | vigilance g |
|---|---|---|
| 0.5 × median(se) | 0.318 | −0.847 [−1.957, **−0.150**] |
| 1.0 × median(se) | 0.520 | −0.867 [−2.405, +0.157] |
| fixed 0.30 (a defensible empirical prior for SMDs) | 0.453 | −0.862 [−2.250, **+0.031**] |
| fixed 0.50 | 0.588 | −0.871 [−2.581, +0.316] |
| **2 × median(se) = 0.763 (as published)** | **0.693** | **−0.873 [−2.854, +0.580]** |
| 4 × median(se) | 0.815 | −0.874 [−3.259, +0.995] |

**The median is remarkably stable (−0.847 to −0.874) and the interval is not: the upper limit moves
from −0.150 to +0.995, so the tau prior scale alone decides whether the headline vigilance interval
excludes zero.** The correct statement is therefore that this prior does not threaten the point
estimate — it determines the interval width and the sign conclusion. `2 × median(se)` is if anything
a *generous* choice: it produces the widest intervals of any option tested other than 4×. So the
prior is not hiding uncertainty, as the brief's framing supposed; it is adding an amount of
uncertainty set by the evidence's precision rather than by its dispersion. That is a different and
less serious sin than the one alleged, but it is not harmless, because the amount it adds is what
decides the qualitative claim.

### 14. The multiverse has four distinct branches, not six, and the choices that actually move the headline numbers are not among them.

**Location:** `src/model.py:636–661`; `src/exposure.py:239–244`; `reports/multiverse.json`.

In the `tib` interpretation, `level_tib = habitual_report * efficiency` ignores `cal_choice`
entirely, so all three "calibration" branches are bit-identical:

| interpretation | calibration | median debt (h) |
|---|---|---|
| tst | naive | 3734.8 |
| tst | reverse | 2920.7 |
| tst | none | 2698.5 |
| tib | naive | 3510.1 |
| tib | reverse | 3510.1 *(identical)* |
| tib | none | 3510.1 *(identical)* |

`n_branches: 6` overstates the design by 50%. The `note` in `multiverse.json` says the branches
"disagree about its size by roughly a factor of two" while the computed `debt_h_spread_ratio` in the
same file is **1.386**; `model.py:601`'s figure title says 1.4×, so the note is the outlier and is
simply wrong.

The headline uses `mixed`/`mixed`, which imposes an unstated prior over interpretations: P(TIB) = 0.5,
and within the TST half the three calibrations split evenly, so the largest-debt calibration
(`naive`) receives 1/6 weight. That implicit prior is never stated and is not itself a branch.
It is, however, nearly harmless: equal-weighting the four distinct branches gives 3216 h against
the published 3329 h, a 3.4% change. **Clean bill on the magnitude; the objection is that the
design is misdescribed.**

What is missing is more serious than what is there. The choices demonstrated above to move headline
numbers by 25% to 275%, none of which is a branch:

| unvaried choice | headline it moves | movement |
|---|---|---|
| permanence spec (`Beta(1.2,18)` vs Bernoulli) | P(permanent loss > 3 pts) | 33–275× |
| recovery saturation constant (1.0 h) | every recovery % | 2–4× |
| mortality dose (categorical vs spline) | LE loss | 4–7× |
| route weights / include route C | FSIQ change | median 79%, upper CI +6.9 → +0.6 |
| predictive vs CI on mu | Q2 sign conclusion | includes zero ↔ excludes zero |
| `lowe2017` nesting | overall neurocognitive g | 16–20% and 2.5× interval |
| small-study correction | vigilance g | 26–80% |
| `studied_deficit_h` anchor | vigilance g | ±25% |
| tau prior scale | vigilance g upper limit | +0.03 → +1.00 |

A six-branch (four-branch) enumeration over one axis of the exposure engine is a calibration
sensitivity analysis, not a multiverse. The word implies a joint enumeration over the analytic
choices that plausibly change the answer, and on the evidence above the axis that was varied is
close to the least influential one in the model. (On the specific items the brief raised: there is
no spline anywhere in `src/` — the dose-response is a power law — and tier weights are computed by
`pool_by_tier` and stored under `tier_stratified` but never used to weight anything.)

### 15. `route_d` applies a cardiovascular confounding-survival fraction to a cognitive outcome.

**Location:** `src/model.py:185–187`; `src/analysis_set.py:161–166`.

```python
conf_surv = rng.uniform(*derived["cvd_confounding_survival"]["interval"], N_DRAWS)
route_d = g_obs_pred * conf_surv * IQ_SD
```

`cvd_confounding_survival` = 0.33 [0.20, 0.50] with basis "UK Biobank staged adjustment: 6 h
HR 1.16 → 1.05; 5 h 1.52 → 1.19" — a *cardiovascular* attenuation. Route D's input is
`habitual_short_sleep_g_observational` (`fjell2023`, `wild2018`: cognitive test scores). Sleep-cognition
cross-sectional associations are confounded by a different set (education, SES, depression,
occupational complexity) and in general attenuate more on adjustment than cardiovascular ones. The
parameter name in the code states the mismatch plainly. Route D carries only 0.10 weight, so the
headline effect is small, but the substitution is undocumented in the report body.

---

## MINOR

### 16. `le_total_months` is assigned twice. The surviving expression sign-censors protective draws. Currently benign; it is the mechanism that would conceal the sign ambiguity identified in objection 9.

**Location:** `src/model.py:266–267`.

```python
le_total_months = le_loss_window_months * -1.0 + le_loss_permanent_months  # overwritten
le_total_months = -np.abs(le_loss_window_months) + le_loss_permanent_months  # survives
```

The first expression is correct: it negates a positive "months lost" into a signed change and
preserves the sign when `hr < 1`. The second forces the window term to be a loss even in draws
where the sampled hazard ratio is protective. The same one-sided censoring appears at line 265,
where `np.clip(hr_permanent_residue, 1.0, 1.15)` maps every protective draw to exactly zero rather
than to a life-expectancy gain. Together these make the reported total **structurally incapable of
being positive**.

Currently this is immaterial: sd(log RR) = 0.0274, so P(log RR < 0) = 1.8 × 10⁻⁵ and the two
expressions differ in **36 of 2,000,000 draws**. Medians and 95% intervals agree to six decimals.
The upper clip at 1.15 is also inactive (max sampled `hr_permanent_residue` = 1.0126).

It becomes material the moment the mortality prior is widened as objection 9 requires: at
predictive sd 0.145, 21.6% of draws are protective, and the as-coded chain reports
−0.155 [−1.739, −0.0016] where the sign-correct chain gives −0.152 [−1.739, **+0.510**]. The bug
would convert "22% chance of no loss" into "0% chance of no loss" silently. `Q7` inherits this via
`ours = np.abs(le_total_months)` at line 309.

### 17. Two rows on the paired `cohens_d` (d_z) scale are pooled inside a parameter declared `hedges_g`, and nothing in the pipeline checks scale commensurability.

**Location:** `src/analysis_set.py:36–46`, `:211–258` (`resolve` reads `c["scale"]` per row and never
compares it to `spec["scale"]`); `src/validate_evidence.py` (no such check).

`pvt_g_large_dose` declares `"scale": "hedges_g"` and includes `basner2011_pvt_metrics`
(`scale: cohens_d`, `unit: "d_z (paired)"`, value 0.91) and `pejovic2013_recovery_dissociation`
(`scale: cohens_d`, 0.331). A paired `d_z` = `d_av / √(2(1−r))` and is inflated relative to a
between-condition standardized difference whenever the within-subject correlation is above 0.5.
Converting the two rows to a between-subject scale:

| assumed within-subject r | conversion factor | pooled mu |
|---|---|---|
| 0.5 | 1.000 | −1.116 (= published) |
| 0.7 | 0.775 | −1.047 |
| 0.8 | 0.632 | −1.005 |

A 6–10% attenuation. Small, but it is a violation of the project's own units convention in
`spec/gates.md`, and the absence of any scale-consistency assertion means a future selector could
introduce a much worse mismatch silently. The extraction-error inflation is also applied to these
rows using the `hedges_g` ICC.

The related concern is more interesting than the arithmetic: the project's own adjudication
established that `lo2016` "prints Cohen's d on two scales in one sentence", and `lo2016`'s
g = 2.399 (the largest single input to the primary parameter) and `belenky2003`'s three
conflicting duplicates (−1.998, −0.95, −0.558) are exactly the pattern that scale confusion
produces. The duplicate-spread SE floor (see clean bill 24) handles the *symptom* by widening the
interval; nothing resolves the *cause*.

### 18. Gate G6's de-duplication mechanism depends on an optional free-text field, and 10 of 22 analysis-set rows leave it null.

**Location:** `src/synthesis.py:352–358`; `src/analysis_set.py`.

Rows with `cohort_family: None` per parameter: `domain_profile_chronic_restriction` 4 of 4,
`global_cognition_...` 2 of 2, `residual_deficit_after_recovery_sleep` 2 of 2,
`reasoning_g_total_deprivation` 1 of 1, `iq_discount_vigilance_to_g` 1 of 1. For those rows the
safeguard is a no-op. This is the proximate cause of objection 2.

Two further string-matching fragilities, flagged for checking rather than asserted: `lo2016`
declares `NFS_Singapore` and `cousins2018` declares `NeedForSleep_Singapore` — almost certainly the
same Need For Sleep adolescent cohort under two spellings (they feed different parameters, so no
within-pool double count, but the report treats the encoding-capacity finding as independent
corroboration of the vigilance finding); and `vandongen2003` (`UPenn_GCRC_2003`) versus
`basner2011_pvt_metrics` (`UPenn_Dinges_TSD_PSD`) are both UPenn/Dinges chronic-restriction
datasets whose subject overlap I could not establish from the records (protocols differ: 4/6/8 h ×
14 nights, n = 48 versus 4 h × 5 nights, n = 74), so this needs a source check rather than a code fix.

### 19. `iq_discount_vigilance_to_g` is clipped at 0.05, placing 12% of the posterior mass on a single atom at the boundary.

**Location:** `src/model.py:171–172`.

`discount ~ N(0.164, 0.097)` clipped to [0.05, 0.60]. P(X < 0.05) = 0.12, so 12% of draws sit
exactly at 0.05, which is visible in `results.json` as `g_loading_discount_applied.p10_p90[0] = 0.05`
and `ci95[0] = 0.05`. The clip is justified as "bounded by the published g-loading ladder" but the
effect is to forbid the hypothesis that essentially none of a vigilance decrement transfers to g —
which is the hypothesis the project's own age-matched null findings (`campbell2024`,
`duraccio2024` healthy-weight arm) support. Directionally this inflates route A's estimated loss.
The mean is pushed from 0.164 to 0.170.

### 20. `absolute_excess_risk_major_depressive_episode_pp` multiplies a percentage-point risk difference by a factor calibrated on standardized mean differences.

**Location:** `src/model.py:231`.

`abs_excess_pp = rng.uniform(*dep["absolute_excess_pp"], N) * transport`. `transport` is
`(deficit/3.7)^gamma` where the exponent's plausible range was chosen as the convexity of a
*g-scale* dose-response over 4–8 h. An absolute risk difference on the probability scale is not
proportional to the same power of dose as a standardized mean difference, because the underlying
risk function is a nonlinear (logistic-like) transform of the linear predictor. The published
median of 1.115 pp is 15% below the untransported 1.45 pp; the objection is that the scale
conversion is incoherent, not that the number is far off.

### 21. `steady_state_ewma_deficit_h` is computed for exactly this purpose and then discarded — but it would not have changed the answer.

**Location:** `src/exposure.py:305–306`, `:330`; `src/model.py:91`.

The exposure engine maintains a recency-weighted deficit with `tau_accrue_days = (7.0, 1.67)`,
which is the right state variable for a *current* impairment estimate; `model.py` instead uses
`mean_nightly_deficit_exposure_h`, the flat mean over all 1040 nights including weekends and
holidays. Substituting the EWMA moves vigilance g from −0.873 [−2.854, +0.580] to
−0.900 [−2.990, +0.599], a 3% change. **Clean bill on impact**; the objection is only that a
computed and better-motivated quantity is silently unused.

### 22. `maintenance_dose_time_in_bed_h` prescribes, for 39% of the posterior, more sustained sleep than the model's own ceiling permits — unflagged.

**Location:** `src/model.py:356`; `src/recovery.py:32`, `:56–58`.

`tib_required = (need_19 − 0.237)/0.8915`, reported as 9.50 [7.95, 11.03] h. `sustained_tst` caps
sleep at `CEILING_SUSTAINED_H = 8.9` h. With need ~ N(8.70, 0.70), P(need > 8.9) = **0.388**, so in
39% of draws the prescription demands sleep the same module declares physiologically unattainable;
at the upper limit (11.03 h TIB → 10.07 h TST) it exceeds the sustained ceiling by 1.17 h. This is
also why no policy in objection 6 can reach a non-negative balance for a large share of draws.

### 23. Smaller items, listed for completeness.

- **`weekend_catchup_arithmetic` is passed the wrong quantity.** `model.py:357` passes
  `median(deficit_nightly)` — the mean deficit over *all* nights — into a parameter named
  `weekday_deficit_h`, which `recovery.py:108` then multiplies by 5. The true weekday deficit is
  larger than the all-nights mean (weekday TST ≈ 5.5 h vs weekend ≈ 7.5 h), so the reported
  `fraction_repayable = 0.187` is if anything optimistic and the conclusion ("catch-up cannot
  work") holds. A units mislabelling with a conservative direction.
- **`yll_per_death = 58.0`** (`model.py:259`) against a dx-weighted remaining life expectancy of
  **59.46 y** over ages 16–18 — 2.5% low.
- **`p_die_16_19 = 0.00248`** is hard-coded although `data/lifetable_us_male_full.csv` is present
  and contains the answer. It is **exactly right** (0.002482) — see clean bill 25 — but
  `LT.load_qx()` reads the truncated table starting at age 19, so the `apply_hr(start_age=16,
  end_age=19)` machinery is a no-op (`lifetable.py`'s own `__main__` acknowledges this), and
  `PUBLISHED["e0"] = 75.8178` is never checked by `calibration_check()`.
- **Extraction error is not applied to `lim2010`'s g.** `model.py:176` draws
  `N(−0.125, 0.072)` directly, bypassing the `+0.1866` inflation that `pooled()` applies to every
  other `hedges_g` effect. Applying it consistently widens route B from [−2.95, +0.13] to
  [−5.36, +2.52] — a 2.4× widening of the dominant uncertainty in the second-highest-weighted route.
- **Gate G7 is met nominally only.** `N_DRAWS = 1e6`, but `resample()` bootstraps from 40,000
  unique pooled-effect draws and 250,000 exposure draws. Bootstrap resampling adds no information.
  **Clean bill on impact:** across 40 independent 40k grid resamples, the SD of the reported 2.5th
  percentile is 0.0149 g against an interval width of 3.6 g.
- **The value-of-information table decomposes a model that produced no headline number.**
  `model.py:473–478`'s `output()` is `g_pool × (deficit/3.7)^gamma × discount × 15` — route A alone.
  The reported IQ number is a four-route mixture in which **49.2% of the variance is between-route**
  (between-route variance 5.163, within-route 5.335). The largest single contributor to the
  reported interval is absent from the "what to measure first" table, and it is not measurable.
  Relatedly, `residual_causal_fraction_for_mortality` is listed as an input with a 0.0000 variance
  share, but it does not appear in `output()` at all; the note explains the zero for
  `individual_sleep_need` (correctly, it is absorbed upstream) and does not explain this one.
- **Gate bookkeeping.** `spec/gates.md` states "Every gate result is logged to
  `reports/gate_log.md`"; that file does not exist. `results.json`'s `gates` block contains one
  entry (G5). G15 requires every headline number to carry a point estimate, a 95% interval and a
  confidence grade: **no confidence grade appears anywhere in `results.json`** (0 occurrences of
  `grade`, `transportability`, `model_dependence`, `GUESS`), and 44 numeric values under `answers/`
  carry no interval, of which these are genuine headline quantities:
  `cigarette_equivalent_per_day_for_3_years` (2.48; spans 0.6–43 across footings),
  `ratio_to_smoking_20_per_day_same_duration`, `prob_permanent_loss_exceeds_1_point`,
  `prob_permanent_loss_exceeds_3_points`, `fraction_repayable`,
  `nights_to_repay_arithmetically`, and the four `irreversible_probability` values.
  `gates.md` also requires that any number graded D on transportability or model dependence be
  labelled a GUESS; the mortality shard's own summary states that its estimate is "grade D on
  transportability and grade D on model dependence, so it must be labelled a GUESS", and
  `results.json` reports it with no such label.
- **No test imports `model.py`.** The 43 passing tests cover `synthesis`, `lifetable`, `recovery`,
  `exposure` and `analysis_set`. `model.py` — which contains the transport function, the route
  mixture, the permanence model, the life-expectancy assembly and every headline number — has zero
  test coverage. Two of the five G9 "calibration targets reproducing published pooled estimates"
  (`test_shan2015_t2d_dose_response_compounding`, `test_lim2010_reasoning_to_lapses_ratio`) call no
  project code at all: they assert `1.09**2 ≈ 1.1881` and `0.125/0.762 ≈ 0.164` on literals, so
  they cannot fail unless Python's arithmetic breaks, and they do not check that those values
  match what the evidence records actually contain.
  `test_cappuccio2010_short_sleep_mortality` pools a single study consisting of the published
  summary itself and asserts `exp(log(1.12)) == 1.12` — a log/exp round-trip, not a reproduction.
  `test_debt_units_are_hours_and_reconcile_with_nightly_deficit` asserts
  `(x/n) × n == x` on two accumulators that sum the identical quantity. On my reading, one of the
  five G9 targets (the life table) is a genuine external calibration.

---

## Clean bills

Points I went looking for and found correct. These were checked with the same effort as the
objections above.

24. **The `dedupe_by_cohort` SE floor is very nearly exactly right.** The brief asked whether
    flooring at `se.min()` is conservative enough for correlated within-cohort estimates. For
    perfectly correlated estimates (r = 1, the worst case) the exact SE of the inverse-variance
    combination is `Σ w̃ᵢ sᵢ`. For the `wild2018` pair (0.0885, 0.0720) that is 0.0786 against a
    floor of 0.0720 — **8% anti-conservative**. Across other configurations: (0.05, 0.50) → 8%,
    (0.10, 0.10) → 0%, (0.02, 0.40) → 5%. An 8% understatement of one SE in a k = 2 pool is
    negligible. The real de-duplication failure is the nullable grouping key (objection 18), not
    the floor.

25. **The life-table arithmetic is correct, including the parts I expected to be wrong.**
    - G10 reproduces NCHS from qx alone to **2.5 × 10⁻⁴ years** for e19 and 3.7 × 10⁻⁴ for e65.
    - The hazard is correctly applied on the hazard scale (`μ' = hr·μ`, `q' = 1 − exp(−μ')`), never
      on the probability scale.
    - `p_die_16_19 = 0.00248` matches the full table exactly (0.002482 from qx = 0.000698, 0.000833,
      0.000953).
    - The closed-form window loss `p × (hr−1) × yll × 12` agrees with an exact life-table
      recomputation over ages 16–18 to **1.7%** across hr ∈ [1.02, 2.0] (ratio 0.983–0.984,
      stable), and essentially all of that gap is the `yll = 58` versus 59.46 discrepancy noted in
      objection 23.

26. **The E-values are exactly correct**, including the reciprocal branch for RR < 1:
    `e_value(1.12) = 1.4866`, `e_value(1.09) = 1.4032`, `e_value(1.22) = 1.7381`, each matching
    `RR + √(RR(RR−1))` to machine precision, and `e_value(0.8) = 1.8090 = e_value(1.25)`. The
    accompanying interpretation (a confounder at RR ≈ 1.5 would explain away the mortality
    association) is the correct reading, and the choice to model
    `residual_causal_fraction` at 0.25 rather than 1.0 follows from it consistently.

27. **G2 citation verification is genuine.** Every study feeding a primary model parameter is
    `VERIFIED` with `title_similarity = 1.0`: `lo2016`, `vandongen2003`, `belenky2003`,
    `basner2011_pvt_metrics`, `pejovic2013*`, `lowe2017`, `lim2010`, `binks1999`, `fjell2023`,
    `wild2018`, `banks2010`, `cousins2018`, `cappuccio2010`, `shan2015`, `sadikova2024`,
    `duraccio2024`, `campbell2024`, `klerman2008`, `kitamura2016`, `short2018`, `lauderdale2008`,
    `leproult2011`, `rupp2009`. Summary: 593 of 597 records resolve, 4 by official source, 0
    unverified. This verifies that the cited paper exists and matches its identifier — not that the
    extracted number appears in it, which was G3's job and which G3 failed. That is a correct
    division of labour, honestly reported.

28. **`individual_need_at_19_h` is correctly modelled as a person-level latent trait**, drawn once
    per simulated person and held fixed across all 1770 nights (`exposure.py:158`, `:281`). This is
    the right structure and it is the reason the debt interval is wide (±1800 h) rather than
    collapsing by √n. The property test that enforces it is a real test.

29. **The TIB/TST branches genuinely do not compound**, as the docstring claims: the level
    correction is `np.where(is_tib, level_tib, level_tst)` (`exposure.py:244`), a mutually exclusive
    selection, and the within-person deviation is re-attached separately via `contrast_fidelity` so
    that reverse regression is not applied to within-person contrasts. This is a subtle point and
    it is handled correctly.

30. **The trim-and-fill implementation is better than most published ones.** It excludes exact-zero
    deviations from the rank statistic (avoiding tie-break-dependent phantom fills) and evaluates
    the L0 statistic in both orientations rather than assuming which side is censored. Both
    refinements are correct and both are documented with the reason.

31. **The window-versus-permanent-hazard distinction is the single best piece of reasoning in the
    project** and it is right. A hazard ratio applied over ages 16–19 costs ~0.05 months; the same
    ratio applied for life costs ~50× more. Both are always computed and separately labelled. Most
    analyses of this kind get this wrong by reporting one and meaning the other.

32. **Excluding dementia rather than assigning it a number is correct**, and so is refusing to
    convert `duraccio2024`'s obesity-subgroup finding into a general adolescent effect. Carrying
    `global_cognition_g_agematched_obesity_subgroup_only` with `applies_to_subject: False`
    specifically so it cannot be silently promoted is good practice.

---

## The three objections most likely to change the reported answer

1. **Objection 1 — the mortality dose-response.** `life_expectancy_change_months_total` = −0.224 and
   `cigarette_equivalent_per_day_for_3_years` = 2.48 are built on the categorical RR 1.12 when the
   project's own evidence station gives written instructions to use the dose-specific value at
   5–6 h and supplies a 0.09–0.50 retention factor for exactly that correction. Following those
   instructions gives **−0.058 months and 0.65 cigarettes/day** — a 4× move, 7× with the male-sex
   correction. This is the largest single defect I found, it requires no new judgement to fix
   (the replacement values are already in `DERIVED_PARAMS`), and it has downstream effects on Q6
   and Q7.

2. **Objection 4 — route C in the IQ mixture.** `measured_full_scale_iq_change` = −0.70
   [−6.70, +6.95] becomes **−1.25 [−7.47, +0.58]** without route C, and **−0.69 [−6.67, +5.01]** if
   route C is merely transported consistently with route B. The entire upper limb of the headline
   interval — the claim that the subject might be testing 7 points *above* his rested self — is
   generated by one study with a positive point estimate, transported with the wrong denominator
   and no total-deprivation-to-chronic conversion, at a hand-set weight of 0.30. Add that routes A
   and B are both driven by the same `lim2010` reasoning estimate at a combined weight of 0.60, and
   the "four independent routes" of the header comment reduce to about two and a half.

3. **Objections 3 and 5 together — intervals and probabilities manufactured by unidentified priors.**
   Where k ≤ 2 the predictive interval has zero data content: `encoding_capacity_persisting` is
   reported as −0.886 [−2.968, +1.247] where the data alone give −0.890 [−1.532, −0.248], a 3.3×
   inflation that flips the interval across zero. And `prob_permanent_loss_exceeds_3_points` =
   0.00012 becomes **0.0038 at the project's own cited permanence probability and 0.032 at its own
   `durable_neurobiological_change_any_kind` = 0.25** once permanence is modelled as an event rather
   than as a shrinkage factor — a 33× to 275× move on a headline probability, driven by two
   `Beta` priors that appear nowhere in the project except as literals in `model.py`.

## Verdict

**The directional and ordinal conclusions are defensible and in several places unusually well
argued; the specific numbers and intervals attached to them are not.** Every qualitative headline I
was able to stress-test survived — the exposure is real and large, the current cognitive decrement
is genuine and concentrated in vigilance, the permanent-IQ and long-run-mortality effects are small
and not distinguishable from zero, and the exposure ranks at or near the bottom of the comparator
set on either internally consistent footing. But of the eleven headline quantities I perturbed,
**seven move by more than a factor of two under a single defensible change** (LE loss 4–7×,
cigarette-equivalent up to 17×, P(permanent loss > 3 points) 33–275×, recovery percentages 2–4×,
the IQ median 79% with its upper limit collapsing from +6.9 to +0.6, the encoding-capacity interval
3.3×, and the overall-neurocognitive interval 2.5×), and in three cases the reported 95% interval
does not contain the value obtained by following the project's own written instructions or its own
cited priors. The numbers should be reported as one-significant-figure order-of-magnitude
statements with the model-choice sensitivities above disclosed, not as calibrated point estimates
with 95% intervals.
