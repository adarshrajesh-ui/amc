# Sleep-Debt Damage Estimation — Software Factory Prompt

A single copy-pasteable prompt for an agentic coding tool (Cursor Cloud Agent, Claude Code,
Codex, etc.) with web access and the ability to spawn parallel subagents and run Python.

It instructs the agent to stand up a **software factory** — a staged pipeline of specialized
worker agents with schema-enforced handoffs, acceptance gates, and rework loops — that builds a
reproducible Bayesian/Monte-Carlo model of one person's cumulative sleep restriction and emits
hard numbers with credible intervals.

Copy everything below the horizontal rule.

---

# MISSION

You are the **Chief Engineer** of a software factory. Your product is not an essay. Your product
is a **reproducible quantitative estimate**, shipped as a git repository plus a blunt report, that
answers: *how much measurable damage did ~3 years of sleep restriction do to this specific person,
and what does recovery actually require?*

You will not answer from memory. You will build a machine that answers, then run it, then attack
it, then report what survived.

**Budget is not a constraint.** Spend agents, tokens, wall-clock, and search queries freely.
Under-spending is a defect. Do not ask me questions — resolve ambiguity by modeling every
plausible branch as an explicit scenario and reporting the spread.

---

# 1. THE SUBJECT

Verbatim self-report (treat as raw, noisy, uncalibrated input — not ground truth):

> Up until around sophomore year I had a good sleep schedule, around 6–8 hours, and especially on
> weekends and holidays at least 7–8. Starting junior year — I'm currently 18, going into my second
> year of college. Freshman year of college I started at 18. Senior year I started at 17. Junior
> year I started at 16. So from 16 through now (turning 19 soon) I've been getting around only
> 5 to 6 hours on average on weekdays, and roughly 7–8 hours on average on weekends and holidays.
> On weekends in my first semester it sometimes stretched to 10 or 11 hours. First semester of
> freshman year of college I averaged maybe 5 hours on weekdays, varying from 3 to 7, and pretty
> consistently slept over 7 hours on weekends.

Structured exposure ledger to reconstruct (fill in, do not assume the row boundaries are exact):

| Epoch | Approx age | Weekday sleep | Weekend sleep | Notes |
|---|---|---|---|---|
| HS freshman–sophomore | ~14.0–16.0 | 6–8 h | 7–8 h | baseline / referent period |
| HS junior | ~16.0–17.0 | 5–6 h | 7–8 h | restriction onset |
| HS senior | ~17.0–18.0 | 5–6 h | 7–8 h | restriction |
| College yr 1, semester 1 | ~18.0–18.4 | ~5 h (range 3–7) | 7–11 h | most severe; highest variance |
| College yr 1, semester 2 | ~18.4–18.8 | 5–6 h | 7–8 h | restriction |
| Now | ~18.8 → 19 | — | — | decision point |

Subject is male-presenting by default only if stated; otherwise run sex as an uncertain parameter
where the literature is sex-stratified. Restriction is **behaviorally imposed** (school, workload,
social/screen schedule), not primarily pathological — but you must still assign a non-zero prior to
undiagnosed insomnia, delayed sleep–wake phase disorder (DSWPD), or obstructive sleep apnea, and
report the posterior probability that a screenable disorder is present given the reported pattern.

## 1.1 Mandatory input corrections

Do not use the self-reported numbers naked. Correct them, and carry the correction as uncertainty:

1. **Self-report vs. actigraphy bias.** Habitual self-reported sleep duration typically exceeds
   actigraphy by roughly half an hour to an hour, with large individual variance (Lauderdale 2008
   and successors). Establish the bias distribution from the literature; do not hardcode a guess.
2. **Time in bed vs. total sleep time.** It is unresolved whether the subject reported TIB or TST.
   Model both as scenarios A (reported = TST) and B (reported = TIB, apply a sleep-efficiency
   distribution for healthy young adults). Report both; do not average them silently.
3. **Recall rounding.** Self-reports cluster on integers and half-hours. Apply a de-rounding /
   measurement-error deconvolution rather than treating "5 hours" as exact.
4. **Calendar structure.** Do not use a flat weekday/weekend average across 3 years. Build a
   day-level calendar: ~36 school weeks/year, ~14–16 weeks of summer/winter/spring break and
   holidays at the near-baseline schedule, plus exam-period spikes of acute restriction. Ad-lib
   break sleep materially shrinks cumulative debt and must be credited.
5. **Social jetlag.** The 5-hours-weekday / 10–11-hours-weekend pattern is textbook social jetlag
   plus a delayed circadian phase. Compute Munich-Chronotype-style social jetlag in hours and
   treat it as a **separate exposure** with its own effect estimates (metabolic, mood, BMI), not as
   a footnote to sleep duration.
6. **Weekend catch-up sleep as an effect modifier.** There is cohort evidence that weekend
   recovery sleep attenuates the mortality/metabolic penalty of short weekday sleep. Find it,
   grade it, and apply it. Failing to apply it will overstate harm.

---

# 2. QUESTIONS THAT MUST BE ANSWERED WITH NUMBERS

Every one of these gets a point estimate **and** a 95% interval **and** an evidence grade. "It
depends" is a defect. If the honest answer is "indistinguishable from zero," say that, with the
interval that justifies it.

**Q1 — Dose.** Total cumulative sleep debt in hours relative to age-appropriate need, age 16.0 →
present. Report the total, the per-night mean deficit, and the fraction of nights below 6 h and
below 5 h. Report separately against (a) the AASM/NSF recommended range and (b) the subject's own
**inferred individual sleep need**, which is a latent parameter, not 8 hours by decree.

**Q2 — Cognition, current state.** Present-day cognitive deficit vs. the subject's own rested
counterfactual, expressed in: standardized effect size (Hedges' g) per domain (vigilance/PVT
lapses, working memory, episodic memory consolidation, executive function/inhibition, processing
speed, emotional regulation), then converted to **IQ-scale points** (SD = 15) with the conversion
assumptions stated. Decompose into three separately-reported components:
  - **State deficit** — reversible within days to weeks of adequate sleep.
  - **Trait/developmental deficit** — attributable to restriction during ongoing adolescent
    neurodevelopment (ages 16–18), potentially persistent.
  - **Learning-loss deficit** — content and skill never encoded because consolidation was impaired,
    which is a knowledge/GPA effect, not an ability effect. Do not conflate these.

**Q3 — Intelligence projection.** Expected change in measured full-scale IQ if tested today vs.
tested after 8 weeks of adequate sleep. Then the expected **permanent** change in adult cognitive
ability attributable to this exposure. State explicitly whether the permanent component's credible
interval includes zero. Separate crystallized from fluid.

**Q4 — Structure and physiology.** For each of: hippocampal/gray-matter volume, white-matter
integrity, glymphatic clearance and amyloid-β dynamics, HPA-axis/cortisol slope, growth hormone
and testosterone secretion, adult height attainment (was the exposure inside the growth window?),
insulin sensitivity and HbA1c, blood pressure, BMI trajectory, inflammatory markers (CRP, IL-6),
immune competence and infection risk, and vaccine antibody response — give the expected present
deviation with an interval, and the probability that the change is **irreversible**.

**Q5 — Psychiatric.** Odds/hazard ratios and, more importantly, **absolute** risk changes for
depression, anxiety disorder, and suicidal ideation, over the exposure window and the next 5 years.
Separate the causal estimate from the observational one; short sleep and depression are heavily
bidirectional and you must model reverse causation explicitly.

**Q6 — Long-run clock.** Change in absolute lifetime risk of type 2 diabetes, hypertension, MACE,
obesity, and dementia by ages 50 / 65 / 80. Change in life expectancy in months. Change in
QALYs/DALYs. Use a life-table or microsimulation, not a bare hazard ratio.

**Q7 — Calibration anchor.** Express total harm in units a human can feel by benchmarking against
reference exposures with comparable life-expectancy/QALY accounting: smoking N cigarettes/day for
3 years, BMI +5 for 3 years, 3 years of physical inactivity, 3 years of heavy alcohol use, and
3 years of a poor diet. Rank this exposure among them. This is the "how catastrophic is it,
actually" answer and it must be a rank plus a ratio.

**Q8 — Recoverability.** For each affected system, classify as: fully reversible / partially
reversible with a recovery half-life / plateaued-permanent. Give the recovery time constant τ in
days for the reversible components, sourced from recovery-sleep studies, not invented.

**Q9 — The prescription.** Solve for policy, not platitudes:
  - Hours per night, 7 days/week, to **stop** accruing new debt (the maintenance dose) — derived
    from the subject's inferred individual need, not the population mean.
  - Hours per night, and for how many weeks, to **repay** the recoverable portion of accumulated
    debt (the loading dose). Answer explicitly whether extra sleep repays debt hour-for-hour, and
    if not, give the actual repayment function and its asymptote.
  - Projected percent of the recoverable deficit recovered at 1, 2, 4, 12, 26, and 52 weeks under
    (a) 7 h/night, (b) 8 h/night, (c) 9 h/night, (d) 8 h + a scheduled nap, (e) status quo.
  - Whether weekend catch-up alone is sufficient. Whether sleep can be "banked" in advance.
  - The point of diminishing returns and whether long sleep carries its own risk (the U-shape is
    largely confounded by illness — say so and quantify how much of it survives adjustment).

**Q10 — The measurement plan.** Design a 4-week self-experiment that converts these population
estimates into personal ones: an ad-lib sleep protocol to measure true individual sleep need,
a PVT baseline and retest schedule, actigraphy or a validated wearable, chronotype (MCTQ) and
sleepiness (ESS) instruments, and clinically meaningful thresholds that should trigger a real
sleep-medicine referral. Include expected effect sizes so the subject knows what a real signal
looks like versus noise. Specify the statistical test and the n of nights required for adequate
power.

---

# 3. THE SOFTWARE FACTORY

Instantiate the following stations. Stations at the same tier run **in parallel** as independent
subagents with isolated context. Every handoff is a file on disk conforming to a JSON Schema you
define in Station 0. No station may consume another station's prose — only its schema-valid
artifacts. Every station writes a `station_report.md` with what it did, what it could not do, and
its own confidence.

**S0 — Spec & Ontology.** Define the outcome ontology, the exposure ontology, the JSON Schemas
(`study.schema.json`, `effect.schema.json`, `exposure.schema.json`, `result.schema.json`), the
evidence-grading rubric, the units convention, and the acceptance gates. Scaffold the repo, pin
dependencies, set the global RNG seed. Nothing downstream starts until schemas validate.

**S1 — Evidence Acquisition (≥14 parallel agents, sharded by outcome domain).** Each shard owns one
domain from Q2/Q4/Q5/Q6 and searches PubMed, Cochrane, Google Scholar, medRxiv/bioRxiv, and the
reference lists of the best reviews it finds. Each shard must screen ≥25 candidate records and
justify every exclusion. Prefer, in this order: recent systematic reviews and dose–response
meta-analyses → the primary studies inside them → newer primaries the reviews missed.

**S2 — Extraction & Normalization.** Convert each included study to a schema-valid record:
identifier (DOI/PMID), design, n, population age range and its match to a 16–19-year-old, exposure
contrast in hours, outcome, effect size with SE on a stated scale, covariate set, follow-up,
funding, and risk-of-bias score (RoB 2 for trials, ROBINS-I / Newcastle–Ottawa for observational).
Convert everything to a common scale (log-RR/log-HR, or Hedges' g) with the conversion formula
recorded in the record. Flag every value you had to infer from a figure, a CI, or an abstract.

**S3 — Blinded Re-extraction / Red Team.** A second, independent set of agents that never saw S2's
output re-extracts a random ≥30% sample plus 100% of the ten most influential studies. Compute
inter-extractor agreement (Cohen's/Krippendorff's κ for categorical, ICC and Bland–Altman for
continuous). **Gate: κ ≥ 0.80 and ICC ≥ 0.90.** Below that, the whole shard is rejected and
reworked. Log the defect rate per shard.

**S4 — Exposure Engine.** Implements §1.1 in code. Emits a posterior distribution over
nightly sleep for every night from age 16.0 to today, plus cumulative debt against both the
guideline referent and the latent individual-need referent.

**S5 — Synthesis Engine.** Meta-analytic pooling and dose–response curves per outcome (see §4).

**S6 — Simulation Engine.** Monte Carlo / Bayesian propagation from exposure posterior through
effect posteriors to the answers in §2.

**S7 — Bias & Sensitivity Engine.** Publication bias, confounding, measurement error,
model-form uncertainty (see §4.4). Runs on S6's output and can force S5 to re-pool.

**S8 — Verification.** Unit tests, property tests, and **calibration regression tests**: your
pooling code must reproduce the published pooled estimate of at least five known meta-analyses to
within Monte Carlo error, and your life-table must reproduce a published national life expectancy
to within 0.3 years. **Gate: all green, or the pipeline does not ship.**

**S9 — Adversarial Review Board.** Three independent critics with distinct mandates, each given the
full repo and told to destroy it:
  - *Methodologist*: attack identification, pooling choices, double-counting of correlated
    outcomes, and interval coverage.
  - *Domain skeptic*: attack the sleep science — is the effect real, is it confounded by depression,
    SES, screen time, caffeine, physical activity, or reverse causation?
  - *Contrarian*: argue the null — that the true damage is negligible and mostly recoverable — as
    forcefully as the evidence allows.
  Each writes a signed critique. The Chief Engineer must resolve every objection in writing:
  accepted-and-fixed, accepted-as-limitation, or rejected-with-reason. Unresolved objections block
  the release. Run **at least two full rework loops**; a first-pass ship is a defect.

**S10 — Report Compiler.** Emits `REPORT.md` per §6 and `results.json` per the result schema.

Track and report factory metrics: studies screened, included, defect rate per station, number of
rework loops, gate pass/fail history.

---

# 4. MANDATORY STATISTICAL METHODS

Anything less is a defect. Implement in Python (`numpy`, `scipy`, `statsmodels`, `pymc` or
`numpyro`, `arviz`, `matplotlib`). Fixed seed. Every number in the report must be regenerable by
`make all`.

## 4.1 Pooling
- Random-effects meta-analysis, REML, with the **Hartung–Knapp–Sidik–Jonkman** variance adjustment.
  Report τ², I², and a **prediction interval**, not just the CI on the mean — the prediction
  interval is what applies to one individual and it is the number that actually matters here.
- Where ≥5 studies with ≥3 exposure levels exist, fit a **dose–response** model
  (Greenland–Longnecker / Orsini two-stage) with restricted cubic splines, so you can read off the
  effect at 5.0, 5.5, 6.0, 6.5 h rather than using a crude "short vs. normal" contrast. The
  short-vs-normal dichotomy is the single largest source of avoidable error in this problem.
- **Bayesian hierarchical model** as the primary analysis: partial pooling across studies within
  domain and across domains within system, with weakly-informative priors on τ. Report posterior
  medians and 95% credible intervals. Frequentist pooling is the sensitivity analysis, not the
  headline.
- Multivariate meta-analysis or robust variance estimation for correlated effect sizes from the
  same cohort. Do not let Whitehall II or UK Biobank vote fifteen times.

## 4.2 Causal identification — mandatory evidence tiering
Weight studies by identification strength, and report the pooled estimate **separately by tier**
before combining. If Tier 1–3 and Tier 4–5 disagree by more than a factor of two, that disagreement
is a headline finding, not a footnote.
  - **T1** Randomized/crossover lab restriction and recovery protocols (best for mechanism and
    short-run magnitude; worst for external validity and duration).
  - **T2** Quasi-experiments and natural experiments: school-start-time changes, time-zone-boundary
    and sunset-time IVs, DST discontinuities. These are the best available causal estimates for the
    academic/cognitive outcomes at exactly this age.
  - **T3** Mendelian randomization on sleep-duration GWAS instruments. Report the MR estimate
    alongside the observational one and interpret the gap.
  - **T4** Prospective cohorts with objective (actigraphy/PSG) exposure measurement.
  - **T5** Prospective cohorts with self-reported exposure. Cross-sectional evidence is
    hypothesis-generating only and may not carry weight in the primary model.

## 4.3 Propagation
- ≥10⁶ Monte Carlo draws. Sample jointly from the exposure posterior and the effect-size
  posteriors; do **not** plug in point estimates anywhere.
- MCMC diagnostics where used: 4 chains, R̂ < 1.01, ESS > 1,000, no divergences. Report them.
- Model dose–response nonlinearity and any threshold/floor effects rather than assuming the effect
  of hour 5→6 equals hour 7→8.
- Model **habituation**: subjective sleepiness plateaus while objective performance keeps degrading
  (the core Van Dongen-style finding). The subject's self-assessment of "I feel fine" is not
  evidence and the model must be able to say why.
- Model **accumulation and recovery** as a dynamical system (e.g., a two-process / homeostatic
  formulation with a debt state variable, an accrual rate, and a bounded repayment rate), fit to
  published recovery-sleep data. Report the recovery half-life with an interval. A pure
  "hours owed" ledger is forbidden as the primary model because sleep debt does not repay linearly.

## 4.4 Bias correction — all four, quantitatively
- **Publication bias**: Egger's test, trim-and-fill, PET-PEESE, and a selection model. Report the
  bias-corrected pooled estimate as the primary if correction is material.
- **Unmeasured confounding**: compute **E-values** for every headline association, and run a
  probabilistic bias analysis with priors over confounder prevalence and strength. State plainly
  which associations a plausible confounder could erase.
- **Measurement error**: regression-calibration or SIMEX for the self-report exposure. Attenuation
  from exposure misclassification biases most of this literature toward the null; correcting it
  moves the answer in the *harmful* direction, so do it honestly in both directions.
- **Model uncertainty**: Bayesian model averaging or an explicit multiverse — enumerate the defensible
  analytic choices (referent definition, spline knots, inclusion thresholds, tier weights) and report
  the distribution of answers across the multiverse. If the headline number is not robust across the
  multiverse, say so in the first paragraph.

## 4.5 Sanity gates
- Before running the full model, produce a closed-form back-of-envelope estimate for Q1, Q2, and Q6.
  If the simulation diverges from the envelope by >20%, halt and find the bug. Report both.
- Dimensional analysis on every derived quantity; unit tests that assert units.
- Every interval must be checked for coverage against a simulated ground truth where possible.
- Report the **value of information**: which single unknown, if measured, would most shrink the
  final interval? That is what the subject should go measure.

---

# 5. EVIDENCE INTEGRITY RULES

1. **Every numeric input traces to a real, verifiable citation** with DOI or PMID. Fabricating a
   study, an effect size, an n, or a CI is a catastrophic defect. If you cannot verify a source,
   mark it `UNVERIFIED` and **exclude it from the primary model**; you may report it in a clearly
   labeled appendix only.
2. Record access tier per source (full text / abstract only / secondhand via review) and downweight
   secondhand extractions.
3. Prefer effect estimates from populations matching a 16–19-year-old. Where you must extrapolate
   from middle-aged cohorts (most of the dementia, CVD, and mortality literature), say so and inflate
   uncertainty accordingly. Adolescent sleep need, adolescent circadian phase, and adolescent
   neuroplasticity all differ from the cohorts most of this evidence comes from.
4. Maintain a **confidence ledger**: for each headline number, an A–D grade for (i) evidence quantity,
   (ii) evidence quality/tier, (iii) population transportability, (iv) model dependence. Publish the
   ledger. Any number graded D on transportability must be labeled a guess in the report body, not
   buried in an appendix.
5. Where the literature genuinely cannot answer a question, output `INSUFFICIENT EVIDENCE` plus the
   widest defensible bound plus the study design that would settle it. Do not manufacture precision.

---

# 6. OUTPUT CONTRACT

Ship a git repository:

```
/spec/            schemas, ontology, acceptance gates
/evidence/        one YAML/JSON per included study + screening log with exclusion reasons
/src/             exposure.py, synthesis.py, simulate.py, bias.py, lifetable.py, recovery.py
/tests/           unit, property, and calibration-regression tests
/figures/         dose-response curves, forest plots, tornado/sensitivity, recovery trajectories,
                  cumulative-debt timeline, multiverse distribution
/reports/         station reports, three signed red-team critiques, objection-resolution log
results.json      every headline number, machine-readable, with intervals and grades
REPORT.md         the human answer
Makefile          `make all` reproduces every number from scratch with the fixed seed
```

`REPORT.md` structure, in this order:

1. **BLUF — 200 words, numbers only.** The answer to "how catastrophic is this." Include the total
   debt in hours, the current IQ-equivalent hit split into reversible and permanent, the life
   expectancy delta in months, the cigarette-equivalent benchmark, and the one-line prescription.
   No preamble, no throat-clearing, no restating the question.
2. **The dashboard** — one table, every Q1–Q9 number, its 95% interval, and its confidence grade.
3. **The prescription** — exact hours, exact schedule, exact duration, projected recovery curve.
4. **What is permanent and what is not** — the honest split, with the probability of permanence.
5. **Reasoning per outcome** — the evidence, the tier, the pooled estimate, why you believe it.
6. **What would change this answer** — the red team's surviving objections, the multiverse spread,
   and the value-of-information ranking.
7. **The 4-week measurement protocol** (Q10).
8. **Full bibliography** with DOI/PMID and per-study risk-of-bias grade.

---

# 7. TONE CONTRACT

Be blunt. Blunt means **calibrated**, not dramatic.

- Numbers before narrative. Every paragraph in the BLUF must contain a number.
- If the evidence says the damage is small and largely recoverable, **say that in the first line**
  and do not pad it with dread to seem thorough. Manufacturing alarm is as much a failure as
  minimizing.
- If the evidence says something is genuinely serious or genuinely permanent, say it flatly, in
  one sentence, without cushioning.
- State the boring truth where it applies: that most of this literature is observational, that the
  subject's weekend and holiday recovery sleep materially changes the picture, and that the largest
  real-world cost of this pattern at age 18 is more likely to be daily function, mood, and grades
  than an early death.
- One line of "see a sleep physician if X" is permitted, where X is a specific, named,
  threshold-triggered finding. Anything more is padding and is a defect.
- No moralizing, no lecture about phones, no "everyone is different," no "listen to your body,"
  no refusal, no substituting a disclaimer for an estimate.
- Ranges are required. False precision is a defect; so is retreating to vagueness to avoid being
  wrong. Commit to a point estimate and own the interval.

---

# 8. PROHIBITED

- Answering from memory without building and running the pipeline.
- Any number without a source, an interval, and a confidence grade.
- Any fabricated citation, n, effect size, or confidence interval.
- Treating self-reported hours as measured hours.
- Using a "short vs. normal sleep" dichotomy where dose–response data exists.
- Letting one mega-cohort dominate the pool through repeated publications.
- Reporting a hazard ratio without the corresponding absolute risk at this subject's actual age.
- Conflating measured-IQ-while-sleepy with permanent-ability change.
- Shipping without the three red-team critiques and at least two rework loops.
- Ending on a hedge. End on the number and the prescription.

---

# 9. START

Begin with S0. Print the plan, the station roster, the schemas, and the acceptance gates. Then run
the factory to completion without stopping to ask permission. Report progress by station. When the
gates are green and the review board has signed off, deliver `REPORT.md`.
