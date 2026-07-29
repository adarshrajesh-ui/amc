# Station report — shard `s04_academic_natural_experiments`

## What I did

Screened **58 candidate records**, included **21**, and wrote 21 schema-valid YAML files carrying
**60 individual effect estimates**. Every DOI and PMID was verified programmatically against Crossref
`/works` or PubMed E-utilities before it was written into a record, and re-verified in a final sweep
(21/21 DOIs HTTP 200 with matching titles; 7/7 PMIDs resolve). Every one of the 60 effect entries
carries a verbatim `quote` from the source I actually retrieved — I checked this programmatically, not
by eye.

Source acquisition: I obtained **full text for 17 of the 21 included studies** (working-paper versions
for the paywalled economics articles, PMC versions for the medical ones), which is why I was able to
extract table-level coefficients and standard errors rather than abstract-level summaries. Three
records are `abstract_only` (Huang 2016, Dewald-Kaufmann 2013) or `secondhand` (Gaski & Sagarin 2011)
and are flagged as such; in those the effect entries carry explicit placeholder markers and
`DO NOT POOL` instructions rather than invented magnitudes.

Coverage against the six required searches:

| Required search | Status |
|---|---|
| 1. School start time quasi-experiments (Carrell, Edwards, Heissel & Norris, Groen & Pabilonia, Hafner/RAND) | **Complete.** All named authors found and extracted except Hafner/RAND, which I deliberately excluded — see "What I could not find" below. Added Hinrichs 2011 (the literature's precise null), Dunster 2018 (actigraphy first stage) and Morgenthaler 2016 (pooled first stage), which the task did not name. |
| 2. Time-zone boundary / sunset IV (Giuntella & Mazzonna; Giuntella, Han & Mazzonna) | **Complete**, with first stages and reduced forms for both. Added Gibson & Shrader 2018 (ReStat) and Jagnani 2024 (ReStat), the latter being the only sunset-IV study with an academic outcome. |
| 3. DST discontinuities on test scores / cognition (Jin & Ziebarth) | **Complete.** Jin & Ziebarth 2020 extracted, plus the two DST/test-score studies that actually exist: Herber, Quis & Heineck 2017 (credible RD, null) and Gaski & Sagarin 2011 (confounded cross-section). |
| 4. Okano et al. — MIT actigraphy study | **Complete**, including all correlations, the R² decomposition, and a definitive answer on night-before vs semester-long sleep. **Retiered from T2 to T4** — it has no exogenous variation and is not a natural experiment. |
| 5. Randomized sleep-extension trial in adolescents/college students with academic or cognitive outcomes | **Partially complete, and the answer is largely negative.** Found Dewald-Kaufmann 2013 (n=55, cognitive not academic) and Bessone 2021 (adults). Also extracted the far stronger randomized *restriction* evidence at exactly the right age (Lo 2016 / Huang 2016, n=56, 5 h vs 9 h × 7 nights). |
| 6. GPA per hour of habitual sleep with identification strategy | **Complete.** Creswell et al. 2023: +0.07 GPA per hour, N=557, identification = lagged-outcome value-added regression on actigraphy. Strategy stated explicitly in the record and in `causal_summary.md`. |

## Headline numbers

- **0.13 SD** of academic achievement per hour of habitual sleep (80% interval 0.02–0.30 SD).
- **0.07 GPA points** (4.0 scale) per hour, from Creswell et al. directly; the SD route independently
  gives 0.08. That convergence between a T4 college-GPA study and a set of T2 school-start-time
  quasi-experiments is the most reassuring result in the shard.
- For the subject's actual exposure (~2.4 h average nightly deficit): **−0.31 SD** or **−0.17 GPA**,
  treated as a lower bound.
- **Central first stage: 0.45 h of sleep per hour of schedule shift** (range 0.31–0.62). This is the
  number that converts the literature's reduced forms into sleep effects, and the reason the
  per-hour-of-sleep effect is 2–3× the per-hour-of-bell-time effect.

## Where I corrected the task's premises

The task's seed names were mostly accurate, but four things differed from what the brief implied and
the pipeline needs to know:

1. **Okano et al. is not Tier 2.** The task grouped it with the natural experiments. It is an
   unadjusted observational correlation study with objective exposure measurement, i.e. T4 by the
   spec's own definitions. Its implied per-hour effect (~12.6 grade points) is roughly 7× the
   lagged-outcome-adjusted estimate from Creswell et al. in the same population, which is a direct
   measurement of how much confounding it carries.
2. **Heissel & Norris is JHR volume 53, not 54,** and its DOI is `10.3368/jhr.53.4.0815-7346r1`. The
   DOI form implied by the task's approximate citation does not resolve.
3. **Four of the five school-start-time papers measure no sleep at all.** Carrell, Edwards, Heissel &
   Norris and Hinrichs report effects per hour of *bell time*. The task asked for effect sizes "per
   hour of additional sleep, and the implied first stage" — the honest answer is that the first stage
   has to be imported from three other studies (Groen & Pabilonia, Dunster, Morgenthaler), and I have
   done that arithmetic explicitly rather than silently.
4. **Carrell's mechanism is contested in the published literature.** Herber, Quis & Heineck point out
   that USAFA prohibited napping and mandated early breakfast, so the additional-sleep interpretation
   is not the only one available; they suggest the empty morning time-slot allowed revision. Anyone
   using Carrell's 0.14 SD as a sleep effect should know this.

## Genuinely credible vs dressed-up-as-causal

The task asked me to separate these explicitly. My verdict:

**Genuinely credible identification:** Herber/Quis/Heineck (near-random test dates), Lo & Huang
(actual randomization of sleep at the right age), Carrell (randomized sections, though the mechanism
is contested), Bessone (large field RCT), Jin & Ziebarth (statutory transition date, event study),
Heissel & Norris (within-student, with a puberty-timing falsification test that a confounder could
not mimic), Edwards (bus-schedule variation with placebo tests), Gibson & Shrader (dual instruments
with the labor-supply channel tested and rejected), Hinrichs (clean DiD, and its null is precise).

**Weaker than it looks:** Groen & Pabilonia is selection-on-observables plus a lagged outcome, not a
natural experiment — the authors say so themselves — yet it is simultaneously the most *useful*
record in the shard because it is the only one with a first stage and an academic outcome in the same
high-school sample. Giuntella/Han/Mazzonna has no discontinuity, only longitude. Jagnani's design is
serious but its implied magnitude (−1.15 SD per hour) is not credible.

**Dressed up as causal, exclude:** Gaski & Sagarin 2011 (Indiana counties by DST regime — a
cross-section confounded by Chicago/Louisville commuting ties, reporting an effect 3–16× the
credible DST estimate). Shapiro 2015 is a narrative advocacy synthesis by a co-author of the largest
positive primary study, and it does not engage with the null result in its own literature.

**Use only for the first stage, not the outcome:** Dunster 2018 — superb actigraphy, but the grade
result is an uncontrolled two-cohort pre/post with teacher-assigned grades that the authors themselves
warn may be biased by teachers' opinions about the policy.

## My own confidence

**Moderate-to-good on sign and order of magnitude; moderate on magnitude; low on the shape of the
dose–response below 6 hours.**

What I trust: the sign is stable across every credible specification I found except one precise null.
Two independent routes (T4 college GPA; T2 start-time reduced forms divided by measured first stages)
converge on 0.07–0.08 GPA per hour and 0.10–0.26 SD per hour. The first stage is well measured by
three independent methods (actigraphy, time diaries, pooled review) that agree on 19–37 minutes per
hour of bell time.

What I do not trust: (a) the three large outliers (Jagnani, Giuntella–Han–Mazzonna, Carrell) are all
either IV ratios with small denominators, where exclusion-restriction violations get amplified, or
reduced forms with no first stage — I have put them in the right tail rather than the centre, but a
different analyst could defensibly weight them higher and get an answer 2–3× larger; (b) the sex
heterogeneity in Groen & Pabilonia (0.156 SD female reading vs 0.003 male) runs directly against our
male subject and I cannot tell whether it is real or small-sample noise; (c) several standard errors
in my records are *inferred* from reported p-values or CI widths rather than reported directly, and
those entries are flagged `inferred_from_ci: true` — Heissel & Norris and Creswell in particular.

What I am confident is wrong in the wider literature: reading the school-start-time reduced forms as
sleep effects. That single error understates the per-hour-of-sleep effect by a factor of ~2–3, and it
is pervasive.

## The single biggest gap in the evidence for my domain

**There is no randomized controlled trial of sleep extension in adolescents or college students with
an academic achievement outcome (grades, GPA, or a standardized test), and therefore no experimental
estimate of how much of a chronic sleep deficit's academic cost is recoverable.**

Everything in this domain is one of three second-best things:

- **Randomized, right age, right dose — but wrong outcome and wrong duration.** Lo/Huang randomized
  56 adolescents aged 15–19 to 5 h vs 9 h TIB for *7 nights* and measured laboratory cognition plus
  vocabulary recall. Excellent internal validity; tells us nothing about a 3-year exposure or a GPA.
- **Right outcome and right age — but not randomized.** Creswell (+0.07 GPA/h) and Okano (r = 0.38)
  are observational. The best of them controls for previous-term GPA; neither has exogenous variation.
- **Quasi-random and right outcome — but the treatment is a bell time, not sleep.** The
  school-start-time literature delivers only ~19–37 minutes of extra sleep per hour of delay, so its
  reduced forms are small, its first stages are mostly unmeasured, and the per-hour-of-sleep effect has
  to be recovered by division, which multiplies every bias in either component.

Why this gap matters specifically for the pipeline's question: the two randomized *extension* studies
that exist both underperformed expectations. Bessone et al. added 27 minutes for three weeks to a
severely sleep-deprived adult population and found **−0.01 SD (SE 0.04)** on their overall index — a
precise null — while naps in the same sample produced +0.12 SD. Dewald-Kaufmann's adolescent extension
trial produced only a selective visuospatial improvement in an n = 55, 85.5%-female sample. So the
restriction→harm direction is much better evidenced than the extension→benefit direction, and **the
model must not assume the two are symmetric.** Our subject's counterfactual is the extension one.

A secondary gap worth flagging: **nothing in this literature measures a multi-year exposure.** The
longest exposures are Edwards's grade-10 persistence result (a bell time experienced two years earlier
still shows up, at 2.0 percentile points) and Jagnani's chronic-sunset attainment result (−0.14 years
of education per 10 minutes). Both suggest the damage does not wash out, and Gibson & Shrader's
long-run:short-run ratio of ~4.5× suggests chronic exposure is worse than acute — but no study
observes three years of adolescent sleep restriction and then measures achievement. Any statement
about our subject's cumulative 3-year loss is an extrapolation, and the pipeline should grade it
accordingly.
