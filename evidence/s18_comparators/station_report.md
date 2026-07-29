# Station report — shard `s18_comparators`

Domain: **calibration anchors.** Supply the comparison exposures against which "3 years of
adolescent sleep restriction" can be ranked, on a commensurable life-expectancy scale, at
matched exposure duration.

- **74 records screened, 29 included, 45 excluded.** Gate G1 (≥ 25) met.
- **68 effect estimates extracted**, each with a verbatim supporting quote. Gate: 68/68.
- **29/29 records validate against `spec/effect.schema.json`.** Gate G0 met.
- **29/29 records `VERIFIED`.** 27 against both Crossref and PubMed; 2 against a single
  registry with the failure documented (§5). Gate G2 met.

Deliverables in this directory:

| File | What it is |
|---|---|
| `comparator_scale.md` | **The deliverable.** Table of LE lost per 3 years of exposure from age 16, with interval, reversibility and conversion assumption per comparator. |
| `convert.py` | All conversion arithmetic. Both bounds, the HR→years calibration, the alcohol injury channel. Reproducible: `python3 convert.py`. |
| `comparator_table.py` | Generates the comparator table numerically from the extracted published values. |
| `build_records.py` | Emits and schema-validates the 29 YAML records. |
| `verification_s18.json` | Raw Crossref/PubMed verification output. |
| `screening_log.md` | Every record screened, every search run, every identifier failure. |
| `<study_id>.yaml` | 29 evidence records. |

---

## 1. What I did

I built the shard around a single question: *what does 3 years of exposure beginning at age
16 cost, for each comparator, on the same scale?* Everything followed from taking that
question literally.

**Step 1 — find estimates that are already denominated per unit of exposure, not per
lifetime.** Almost none exist. The one clean success is Jackson 2025 (*Addiction*),
which prices smoking at 17 minutes of life per cigarette for men and states that a 10-a-day
smoker who quits recovers 50 days of life over the following year. That is directly
multipliable by 3 years. I found no equivalent for BMI, inactivity, alcohol or diet: every
one of those literatures reports life expectancy for *sustained* exposure only.

**Step 2 — build the conversion machinery and be explicit that it, not the epidemiology, is
the dominant source of uncertainty.** Using the G10-calibrated US male 2023 life table that
shard `s17_baseline_risk` built, I implemented three models (window-only, pro-rata
cumulative dose, full permanent hazard shift) and computed all three for every comparator.
The bounds span a factor of 100 to 4000 per comparator. The epidemiological confidence
intervals span factors of 1.1 to 1.5. **The conversion assumption is between two and three
orders of magnitude more consequential than the measurement uncertainty in the source
studies.**

**Step 3 — validate the conversion engine against the sources' own published years.**
Applying each source's own hazard ratio from age 40 for life reproduces its own published
years-of-life-lost to within about 18-20% (consistently on the high side, five anchors).
That gave me both a sanity check and a correction factor (0.80), and it revealed a clean
regularity: in this life table **years of life lost ≈ 10.85 × ln(HR)** for a hazard
sustained from a fixed age, essentially constant across HR 1.12 to 2.96. That linearity is
what lets Model P be re-expressed as a single permanent hazard ratio
\(\text{HR}_{\text{pub}}^{3/E}\) applicable from age 19, which is the modeller-ready form
in the table.

**Step 4 — hunt specifically for evidence on reversibility after cessation in early
adulthood,** because that is what distinguishes a fair comparison from an unfair one. Four
independent smoking-cessation gradients (UK doctors, US NHIS, UK Million Women, Japan JACC)
converge on the same answer. For physical inactivity there is one good record (Mok 2019).
For diet the source model quantifies its own reversibility via an age gradient. For BMI
there is almost nothing. For sleep there is nothing at all (§4).

---

## 2. THE CRITICAL METHODOLOGICAL WARNING

**Every comparator estimate in the published literature is for a hazard sustained for the
rest of life, usually measured in midlife adults. None of them is for 3 years of exposure
at age 16-19. Converting between the two is an assumption, and the assumption dominates the
answer.**

The reason is arithmetic, not epidemiological. **A US male's probability of dying between
exact age 16 and exact age 19 is 0.00248 — 248 per 100,000.** Adolescence is the safest
window in the human lifespan. So:

- If an exposure only raises the hazard *while it is happening* (Model W), then even
  tripling the hazard for those 3 years costs **107 days**, and a plausible 20% elevation
  costs **11 days**.
- If the same exposure permanently shifts the hazard (Model F), a 20% elevation costs
  **2.3 years** and a tripling costs **14 years**.

That is a factor of 78 for HR 1.2 and 48 for HR 3.0, from the *same* hazard ratio, purely
by choosing when the hazard applies. No amount of care in the underlying epidemiology
touches this.

### 2.1 What I recommend

**Model P (pro-rata cumulative dose) as the structural default, expressed as a permanent
hazard ratio of \(\text{HR}_{\text{pub}}^{3/E}\) applied from age 19, then moved toward the
window bound in proportion to the strength of the comparator's post-cessation recovery
evidence, plus a separate additive within-window term for any comparator whose hazard is
concentrated at ages 16-24 (in practice, alcohol alone).**

Why Model P and not Model W as the default:

1. Model W makes 3 years of a 40-year habit almost free, which contradicts the pack-year
   literature outright.
2. Model P is the only one of the three that a published source independently endorses:
   Jackson 2025's per-cigarette figure *is* a pro-rata attribution, and Model P at 20
   cig/day reproduces it to within 1% (8.4 vs 8.5 months for 3 years).
3. It degrades correctly at both limits.

Why Model P must not be used uncorrected:

1. **It assumes harm is linear in exposure-years.** For smoking this is known false —
   hazard is strongly super-linear in *duration* — so pro-rata over-charges the first 3
   years of a career.
2. **It gives no credit for repair.** For smoking, Model P (8.4 months) and the
   cessation-calibrated estimate (~1 month) differ by a factor of ~9, and the second is the
   one backed by observed mortality in people who actually stopped young.
3. **It discards front-loaded acute hazards.** Pro-rating a midlife chronic-disease
   estimate throws away the injury mortality that dominates alcohol harm at exactly our
   subject's age.

### 2.2 Both bounds, for every comparator

Given in full in `comparator_scale.md` §1. Summary, in months of life expectancy lost from
3 years of exposure beginning at age 16:

| Comparator | Bound L (window) | Recommended | Bound U (full permanent) |
|---|---|---|---|
| Smoking 20/day | 0.04 mo | **1.8 mo** (0.6-9.0) | 168 mo |
| Smoking 10/day | 0.02 mo | **1.0 mo** (0.4-4.4) | 104 mo |
| Overweight (BMI 27.5) | 0.35 mo | **1.8 mo** (0.4-3.0) | 27 mo |
| Obesity grade 1 (BMI ~32) | 0.79 mo | **2.4 mo** (0.8-3.2) | 56 mo |
| Physical inactivity | 0.61 mo | **0.8 mo** (0.2-3.1) | 45 mo |
| Alcohol 200-350 g/wk | 1.76 mo | **3.0 mo** (1.4-4.2) | 21 mo |
| Typical Western diet | 0.09 mo | **1.8 mo** (0.1-3.8) | 41 mo |
| *Insufficient sleep (ours)* | *0.21 mo* | ***1.2 mo*** *(0.2-3.6)* | *17 mo* |

**Bound U is not a defensible estimate for a 3-year exposure and I am not offering it as
one.** It is the published headline figure — it is what a careless reading of Doll, PSC or
Wood produces — and it is tabulated so the modeller can see the size of the error that
reading would introduce.

### 2.3 Cumulative-irreversible versus reversible-on-cessation

The single most useful thing this shard establishes. Ranked by how much of the damage the
subject is stuck with after stopping at 19:

1. **Smoking — most cumulative.** Pack-years is a real irreversible dose and lung-cancer
   risk persists (`pirie2013`: RR 1.84 after quitting at 25-34). *But* the all-cause
   residue after young cessation is only 3-5% of the excess. Four independent gradients
   agree: `doll2004` (cessation at 30 gains ~10 of the 10 years), `jha2013` (before 40
   removes ~90%), `pirie2013` (before 30 avoids >97%; quit at 25-34 leaves RR 1.05,
   1.00-1.11), `zuhal2023` (initiation before 20 is not independently damaging on
   all-cause mortality provided cessation is before 50 — what matters is total duration).
2. **BMI — partly cumulative, and worse, usually not reversed at all.** `peeters2003`: BMI
   at 30-49 predicted mortality at 50-69 *after* adjustment for BMI at 50-69. The bigger
   issue is tracking: adolescent adiposity persists (`zheng2017`, `twig2016`), so "3 years
   then cessation" may be a counterfactual that rarely occurs.
3. **Alcohol — structurally unlike the rest.** Chronic channel largely reversible; acute
   injury channel irreversible but *resolved inside the window*. It is a mortality lottery,
   so conditional on surviving to 19 unharmed, almost none of it carries forward. Ex ante
   expected loss and ex post realised loss diverge sharply for alcohol and nothing else.
4. **Physical inactivity — largely reversible.** `mok2019`: HR 0.76 (0.71-0.82) per
   +1 kJ/kg/day/y rise, *adjusted for baseline activity*; increasing trajectories beat
   consistent inactivity from any starting point. Fitness is a state variable.
5. **Diet — most reversible, and the source quantifies it.** `fadnes2022`: 8.8 of the 13.0
   years available at age 20 are still available at 60 — 68% of the benefit survives a
   40-year delay.
6. **Insufficient sleep (ours) — unknown.** See §4.

---

## 3. What I could not find

- **No per-unit-exposure life-expectancy estimate for BMI, physical inactivity, alcohol or
  diet.** Only smoking has one (Jackson 2025). Every other comparator had to be converted
  by me, which is why `convert.py` exists and why the conversion is the headline caveat.
- **No published QALY estimate for insufficient sleep** on a per-person,
  per-unit-exposure basis. The sleep-QALY and sleep-cost-effectiveness searches returned
  only disease-specific work (chronic kidney disease, periodontitis).
- **No GBD figure for sleep of any kind.** `welter2026`: sleep is in the GBD hierarchy
  "*neither included as primary disorders nor as risk factors*", and has been absent since
  the 2004 update. GBD supplies quotable DALY figures for diet, alcohol, physical
  inactivity and high BMI and none for sleep. **Any report that cites a GBD sleep DALY
  figure has invented it.** This also means DALY-space comparison is closed to us; the
  comparison must go through life expectancy.
- **RAND (`hafner2016`) does not do what it is usually said to do.** It prices lost GDP
  (up to $411 bn/yr, 1.56-2.28% of US GDP) and lost working days (~1.23 million/yr for the
  US). It contains no life-expectancy or QALY output, and its only health input is a
  mortality relative risk *borrowed* from the short-sleep meta-analysis literature (RR 1.10
  for <6 h). It must not be pooled with `cappuccio2010` — that double-counts the same RR.
- **No individual-level hazard ratio for alcohol-related injury death in 16-19-year-old
  males.** `gbd2016alcohol` gives a population attributable fraction (12.2% of male deaths
  at 15-49), from which an individual HR cannot be recovered without exposure prevalence.
  The 7.4-day population-average window term *is* derivable; the 53-day figure I use for a
  heavy drinker rests on an assumed HR of 2.0. Under `spec/gates.md` that makes the alcohol
  central estimate **grade D on model dependence, i.e. a GUESS.** It is the cell I would
  most like replaced.
- **Almost no evidence on BMI reversibility after a short exposure.** The best I could
  retrieve was `peeters2003`'s qualitative statement (reported without a number in the
  abstract) and, from the weight-loss searches, only bariatric-surgery
  cost-effectiveness studies in morbid obesity — the wrong contrast entirely. Smoking has
  four cessation gradients; BMI has one sentence.
- **Doll 2004's cigarettes-per-day dose table** could not be extracted (BMJ blocks PMC
  full-text download). `banks2015` supplies the dose gradient instead (~2x at ≤14/day,
  ~4x at ≥25/day).

---

## 4. The single biggest gap in the evidence for my domain

**There is no cessation gradient for sleep.**

For smoking I can tell the modeller, from four independent cohorts, precisely what
happens to a person who is exposed young and then stops: they recover 90-97% of the lost
life expectancy, leaving a residue of roughly 1-4% of the excess. That single fact is what
makes smoking a *fair* comparator for our subject, who is also stopping an exposure young,
and it is why my recommended smoking figure (1.8 months) is 5x below the pro-rata figure
(8.4 months).

**No equivalent evidence exists for sleep.** Not one record I screened reports mortality or
life expectancy in people who slept short for a defined period in adolescence and then
slept normally. The sleep-mortality literature is entirely cross-sectional-exposure
prospective cohorts: sleep is measured once, in midlife, by self-report, and related to
subsequent death. `cappuccio2010` and `li2024sleep` both have that design.

The consequence is severe and asymmetric. **Where the comparators get a
recovery discount that I can justify from data, our own exposure cannot get one, so any
head-to-head ranking is biased against sleep by exactly the size of a discount nobody has
measured.** Concretely: if sleep restriction turns out to be as reversible as physical
inactivity, our subject's 3-year exposure is worth well under a month; if it is as
cumulative as pack-years, it is worth a few months. I cannot distinguish these, and neither
can the literature.

Three further problems compound it:

1. **The long-sleep anomaly.** `cappuccio2010` finds *long* sleep (RR 1.30, 1.22-1.38)
   more strongly associated with death than short sleep (RR 1.12, 1.06-1.18). Long sleep
   has no plausible causal mechanism of that size. That pattern is the signature of reverse
   causation and confounding by prevalent illness, and it should discount the short-sleep
   estimate too — which means our exposure's *sustained* effect may itself be overstated
   before any conversion is applied.
2. **Exposure-definition mismatch.** `li2024sleep`'s 4.7-year figure is for a five-item
   sleep *phenotype* (duration, sleep-onset difficulty, sleep-maintenance difficulty,
   hypnotic use, daytime sleepiness) measured at mean age 47, not for 5-6 h of weekday
   sleep in a healthy 18-year-old with weekend catch-up. Its median follow-up is 4.3 years
   while its outcome is life expectancy at age 30, so the number is a long extrapolation
   from a parametric survival model.
3. **Age transport runs the wrong way for once.** For BMI, transport to age 18 is
   *favourable* — `globalbmi2016` finds a larger hazard ratio when adiposity is measured
   younger (1.52 at 35-49 vs 1.21 at 70-89) and in men (1.51 vs 1.30), so using the pooled
   figure is conservative. No such reassurance exists for sleep: whether adolescent sleep
   restriction carries a larger or smaller lifetime hazard than midlife short sleep is
   simply unknown.

**What would close the gap:** a cohort with repeated sleep measurement spanning
adolescence into adulthood, analysed as a trajectory the way `mok2019` analysed physical
activity, so that "short in adolescence, normal thereafter" can be contrasted with
"consistently short". Failing that, the closest available substitute is the Swedish and
Israeli conscript design (`hogstrom2016`, `twig2016`) — a whole-population measurement at
age 18 with register follow-up. If an adolescent sleep measurement exists in any
conscription or national-service cohort, that is where the missing number is.

---

## 5. My own confidence

Graded per `spec/gates.md`. Grades are for *the comparator estimates this shard supplies*,
not for the underlying epidemiology, which is generally strong.

| Comparator | Quantity | Quality/tier | Transportability | Model dependence | Overall |
|---|---|---|---|---|---|
| Smoking | **A** — 7 records, 4 independent cessation gradients | **B** — T5 cohorts, but enormous n and 50-y follow-up | **B** — `zuhal2023` addresses initiation <20 directly | **C** — pro-rata vs cessation-calibrated differ ~9x | good |
| BMI | **B** — 6 records | **B** — includes T4 measured exposure at age 17 | **B** — `fontaine2003` is age 20-30; age gradient is favourable | **C** | fair |
| Physical inactivity | **B** — 6 records | **B** — includes device-measured and age-18 objective fitness | **B** — `hogstrom2016` is measured at exactly 18 | **C** | fair |
| Alcohol | **C** — 2 records | **B** | **C** — chronic estimate is midlife; the injury channel is age-matched but only as a PAF | **D** — the window HR is an assumption | **GUESS** |
| Diet | **C** — 3 records | **D** — all life-table modelling on observational inputs | **B** — `fadnes2022` starts at age 20 | **C** — two routes differ 2x | weak |
| Sleep (reference) | **C** — 3 records | **C** — T5 self-report, midlife | **D** — no adolescent exposure, no cessation data | **C** | weak |

**Where I think I am right.** The core finding is robust to essentially every choice I
made: *on a fair 3-years-at-16-19 basis, all of these exposures land in a band of roughly
1 to 3 months of life expectancy, and the decade-scale figures that dominate public
discussion of smoking, alcohol and obesity do not survive conversion.* That conclusion
holds under Model W, under Model P, and under every reversibility discount I considered. It
is driven by the 248-per-100,000 adolescent mortality figure and by the fact that 3 years
is a small fraction of any of these exposure careers — both of which are facts, not
modelling choices.

**Where I think I may be wrong.**

1. **The alcohol window term.** The assumed HR of 2.0 is the weakest number I produced. If
   the true figure for a heavy-drinking 18-year-old male is 1.2, alcohol drops to the
   bottom of the table; if it is 3.0, it roughly doubles. Flagged as a GUESS.
2. **Diet may be substantially overstated at source.** `fadnes2022` gives 13.0 years for
   diet *alone*, while `li2018lifestyle` caps *all five* of these behaviours combined at
   12.2 years for men. A single-exposure estimate exceeding the five-exposure joint
   estimate is internally inconsistent, and it is diet's that does. I suspect the
   food-group summation double-counts shared pathways.
3. **My smoking recommendation is deliberately at the low end** of its own interval, on the
   strength of the cessation evidence. A reviewer who prefers cumulative-dose reasoning
   would put it at 8.4 months rather than 1.8. I think the observed mortality of people who
   quit young beats a linearity assumption, but the interval (0.6-9.0 months) is wide on
   purpose and the disagreement is real.
4. **The 0.80 calibration factor is empirical, not derived.** It reconciles my life-table
   engine with five published anchors and it should not be trusted outside the HR range
   1.1-3.0 in which it was fitted.

**One thing the downstream pooler must not do.** `hafner2016`'s RR 1.10 and
`cappuccio2010`'s RR 1.12 are the same quantity; RAND borrowed it. `fadnes2022` and
`fadnes2024` are the same model by the same authors. `hogstrom2016`, `twig2016` and the
excluded Ballin/Crump/Af Geijerstam papers draw on the same conscript cohorts. Cohort
families are set on every effect so gate G6 can catch these, but the RAND/Cappuccio overlap
is not visible from the cohort field alone and is flagged in both records' `notes`.
