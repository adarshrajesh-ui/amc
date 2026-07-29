# Station report — shard `s13_mortality`

Domain: **all-cause mortality in relation to habitual sleep duration**, for conversion into a change
in life expectancy in months for a 19-year-old male.

| Metric | Value |
|---|---|
| Records screened and individually adjudicated | **72** (gate G1 threshold 25), from 249 archived title-level hits |
| Records included with YAML | **28** |
| Records excluded with a logged reason | **44** |
| Effect estimates extracted | **122** |
| Schema validation failures | **0** (gate G0) |
| Identifiers failing verification | **0** (gate G2); 28/28 `VERIFIED` on both Crossref and PubMed with DOI string match |
| Records at `access_tier: secondhand` | **0** |
| Access tier | `full_text` **7** · `abstract_only` **21** · `secondhand` **0** |
| Tier distribution | T3 (MR) 3 · T4 (objective cohort) 9 · T5 (self-report cohort) 15 · TX 1 |
| `adolescent_match` distribution | `poor_midlife` **19** · `poor_elderly` **4** · `fair_adult` **2** · `mixed` **2** · `exact_16_19` **1** · `good_young_adult` **0** |
| Named cohort families | **UK_Biobank 8 records** · SHHS 2 · Swedish_National_March_Cohort 2 · CPS_II · Whitehall_II · Asia_Cohort_Consortium · Kailuan · Southern_Community_Cohort_Study · Terman_Life_Cycle_Study · Penn_State_Adult_Cohort · UK_Biobank+FinnGen · Timmers_parental_lifespan_GWAS · plus 7 `pooled_multi_cohort_*` families for the meta-analyses |

---

## 1. What I did

Executed 16 queries (12 PubMed, 4 Europe PMC), archived verbatim in `search_hits.txt` and
reproducible through `screen_runs.sh`. Retrieved abstracts for every candidate that passed title
screening and full text from Europe PMC / PMC wherever open access permitted. Wrote four small tools,
all in the shard directory and all re-runnable:

- `pm.py` — PubMed search / abstract fetch / Crossref verify / Europe PMC search + full-text XML.
- `verify_batch.py`, `verify_batch2.py` — programmatic verification of every DOI and PMID against
  **both** Crossref and PubMed, with the PubMed-reported DOI string-matched against the DOI I
  recorded. Raw responses preserved in `verification_raw.json` (28 entries).
- `conv.py` — log-ratio conversion, `value = ln(point)`, `se = (ln hi − ln lo)/3.92`.
- `validate.py` — validates all YAML against `effect.schema.json` **and** re-audits every log-scale
  effect for internal consistency between `value`, `ci` and `se`. It caught one inconsistency
  (`windred2024`), which I fixed.

Every extracted number carries a verbatim `quote`. Where a paper reported only a range or a threshold
(`kripke2002`, `xiao2019`, `windred2024`), I recorded `se: null` and said so in
`conversion_formula`, rather than manufacture an interval.

## 2. Required extractions — status

| # | Requirement | Status |
|---|---|---|
| 1 | Cappuccio et al. short and long pooled RR, with CIs, studies, participants, deaths | **DONE.** Short **RR 1.12 (1.06-1.18)**, long **RR 1.30 (1.22-1.38)**; 16 studies / 27 cohort samples, 1 382 999 participants, 112 566 deaths. |
| 2 | Dose-response MAs: per-hour RR below nadir, nadir location, RR at 5 h and 6 h, shape | **DONE.** `yin2017`, `liu2017`, `itani2017`, `jike2018` + newest `ungvari2025` and `chaput2026`. Nadir **7 h** (5 independent confirmations). Per-hour below nadir **RR 1.06 (1.04-1.07)**; above **1.13 (1.11-1.15)**. **5 h: 1.04-1.06. 6 h: 1.01-1.04.** Shape **J, not U** — long arm 2.2-2.9x steeper on the log scale. |
| 3 | Causal or confounded? Objective measurement, MR, reverse-causation handling, quantified attenuation | **DONE, and the task's premise was wrong.** See §3 below. Attenuation ladder quantified in 7 analyses: **37-93% survives covariate adjustment, 73% survives adjustment + early-death exclusion, 0-28% survives genetic instrumentation.** |
| 4 | Åkerstedt weekend catch-up — every cell (HIGH PRIORITY) | **DONE, plus three studies the task did not name.** All cells in `mortality_summary.md` §4. **SS 1.65 (1.22-2.23); SML (catch-up) 1.09 (0.77-1.54); MM 1.00 ref; ML 1.02; LL 1.25**, age <65. |
| 5 | Exposure measured in adolescence/young adulthood | **INSUFFICIENT EVIDENCE**, stated explicitly. Only `duggan2014` exists and it cannot answer the question. |
| 6 | Does the association differ by age at exposure; does it attenuate in younger cohorts? | **DONE, and the answer is the opposite of reassuring.** It is **larger** in younger strata (`akerstedt2017`: **2.45 under 45 y** vs **1.05 over 65 y**) and age is a significant modifier in men (`svensson2021`, P<.001). It does **not** attenuate in younger cohorts. |

## 3. Where the task brief was wrong, and I report reality

The brief stated: *"Objective measurement usually WEAKENS the short-sleep association, which is a
crucial finding."* **In five independent analyses it STRENGTHENS it**, including the decisive
head-to-head design:

- `zhao2023` (SHHS, same 5027 people, same model, only the instrument varies): PSG 5-6 h **HR 1.37**
  vs self-reported weekday 5-6 h **HR 1.02**.
- `chaput2026`: device SPT 5 h vs 7 h **1.43**; self-report in the same people **1.16**.
- `saintmaurice2024` **1.29**, `liang2023` **1.27**, `yoshiike2023` PSG <330 min **2.01**.

**The brief's conclusion nevertheless survives, and `zhao2023` shows why more sharply than any
attenuation analysis can:** (a) the objective curve is **not graded** — PSG 6-7 h (1.42) is no better
than PSG 5-6 h (1.37); (b) the self-report curve at the subject's dose is flat and **non-monotone** —
5-6 h → 1.02, 6-7 h → 0.93, **4-5 h → 0.68**; (c) the two instruments were only **weakly correlated**
with each other, so they are not two noisy readings of one exposure but **two different exposures
sharing a label**. Devices measure short sleep better, and in a 64-year-old short sleep measured
better is a better marker of *illness*.

Two smaller corrections to the brief:
- The brief's requested referent for `akerstedt2019` was "consistently 7 h sleepers". The paper's
  referent is **"medium-medium" = 6 OR 7 h on both weekdays and weekends**, and its companion
  `akerstedt2017` concludes **6 h, not 7 h, is the nadir in that cohort**. The subject's weekday 5-6 h
  therefore sits partly *inside* the referent category.
- No MR study of sleep duration on **parental lifespan** specifically exists. A title-restricted
  Europe PMC query returned exactly one record, and it was `duggan2014`. The nearest thing is
  `wu2024`, which uses a lifespan GWAS.

## 4. The limitation I was told to state forcefully, stated forcefully

**Every hazard ratio in this shard answers a question we did not ask.** They answer: *among people
who, at one moment in midlife or later, reported or were measured to sleep X hours, what was the death
rate over the following 5-20 years?* That is a **current-state hazard for a person whose exposure is
ongoing and whose short sleep is entangled with their health, work, mood, poverty and medication at
the moment of measurement**.

Concretely, in this shard's evidence base: the mean age of `akerstedt2019`'s consistently-short-sleep
cell is **61.2 years**. `zhao2023`'s cohort averages **63.9 years and one in four of them died within
11 years**. `chaput2026`, `chaput2024`, `saintmaurice2024`, `liang2023`, `li2026` and `windred2024`
are all UK Biobank participants aged **40-79**. `kripke2002` is 30-102. `svensson2021` averages 54.5.
`cappuccio2010` pools all of that.

**A hazard ratio from a 60-year-old cohort tells us about the effect of BEING a short sleeper. It does
not tell us about the residual effect of HAVING BEEN one for three years in adolescence.** These are
different estimands. The evidence for the second is not weak — **it is absent**. Reading 1.12 as
"1.12x for life because he slept badly at 17" is not a conservative use of the number; it is a
different quantity with no support.

Accordingly, **every one of the 28 records carries an explicit `population.adolescent_match` flag**:
`poor_midlife` 19, `poor_elderly` 4, `fair_adult` 2, `mixed` 2, `exact_16_19` 1 (`duggan2014`, whose
match is exact on age and useless on everything else). **Not one record is `good_young_adult`.**

## 5. INSUFFICIENT EVIDENCE — stated explicitly, as instructed

> **There is no study, of any design — cohort, MR, quasi-experiment or trial — that estimates the
> all-cause mortality consequence of a time-limited period of sleep restriction in adolescence
> followed by normalisation. The evidence base for the subject's actual counterfactual is empty.**

I screened 80 records across two dedicated queries plus a title-restricted Europe PMC query to
establish this. The near-misses and why each fails:

- **`duggan2014`** (Terman, n=1145, childhood sleep → death) — the only childhood-exposure-to-death
  study in existence. It models a **quadratic** deviation from age-predicted sleep, **HR 1.15
  (1.05-1.27) in males for deviation in either direction**, so a short sleeper and a long sleeper
  receive the same coefficient and **no short-sleep-specific estimate is obtainable**. Born 1904-1915,
  gifted Californians, proxy-reported exposure, left-truncated at enrolment. It also cannot separate
  "trait" from "state": a child who slept short probably slept short for decades — the opposite of our
  subject.
- **`wang2020`** — a short sleeper who normalised (low-increasing, 4.9 → 6.9 h) retained
  **ln(1.22)/ln(1.47) = 52%** of the excess log-hazard of persistent short sleep — **but for
  cardiovascular EVENTS, not death.** The abstract reports all-cause mortality for the low-stable
  (1.50) and normal-decreasing (1.34) groups and **does not report it for the normalising group**, so
  the closest thing to a reversibility estimate in this literature is not even a mortality estimate.
  Normalisation also occurred in **midlife after decades**.
- **`li2026`** — same-week rebound removes ~65% of the excess hazard. Contradicted by `chaput2024` in
  the same cohort.
- **`ferrie2007`** — hazard tracks the **current trajectory**, and symmetrically: sleep decreased →
  CVD mortality HR 2.4; sleep increased → non-CVD mortality HR 2.1.

## 6. My own confidence

Applying the four `gates.md` grades to my headline outputs:

| Output | Quantity | Quality | Transportability | Model dependence |
|---|---|---|---|---|
| Nadir at 7 h | **A** (5 independent, >5M people) | **C** (T5 dominant) | **C** | **A** |
| Dose-response RR at 5-6 h ≈ 1.01-1.06 | **B** | **C** | **C** | **B** |
| Categorical short-sleep RR 1.12-1.14 | **A** | **C** | **D** | **A** |
| Objective > self-report for short sleep | **B** (5 analyses) | **B** (T4) | **D** | **B** |
| MR shows no large causal mortality effect | **C** (3 studies, disagreeing) | **B** (T3) | **C** | **C** |
| Weekend catch-up is protective | **C** (4 studies) | **B** | **D** | **D → GUESS** |
| Association larger at younger exposure ages | **B** | **C** | **C** | **B** |
| Residual fraction applying to a 3-year adolescent exposure (~1%, 0-12%) | **D** (zero direct studies) | **D** | **D** | **D → GUESS** |

**Where I am confident:** the nadir is 7 h; the curve is flat between 6 and 7 h; the shape is J with a
much steeper long arm; the categorical "short sleep" estimate is 3-11x the dose-specific estimate at
the subject's actual dose; long sleep looks worse than short sleep in every large dataset and stops
doing so when sick people are removed (`pienaar2021`).

**Where I am not confident, and the downstream model must widen:** the true causal fraction (the
attenuation ladder spans 0-93% depending on which control you trust); whether weekend catch-up helps
(sign-unstable across four studies, two of them sharing a cohort and disagreeing); and anything about
adolescent exposure, where I am extrapolating with no data.

**Where I actively disagree with a plausible reading of my own evidence:** `windred2024` implies the
subject's *irregular* pattern (5-6 h weekdays, 7-8 h weekends, 3-4 h before exams, occasional 10-11 h
nights) may be the risk-relevant feature rather than his mean duration — and on that framing his
pattern looks **worse**, not better, than a flat 6 h. That directly tensions with the entire
weekend-catch-up literature, which treats the same weekend extension as protective. **I could not
resolve this and I am flagging it rather than picking a side.**

## 7. The single biggest gap in the evidence for my domain

> **Adolescent all-cause mortality is dominated by injury, motor-vehicle crash, suicide and homicide —
> and every single study in this shard follows midlife or elderly adults dying of cardiovascular
> disease and cancer.**

This is not the same gap as "no adolescent cohorts exist" (§5), and it is more dangerous. My entire
evidence base estimates hazards through **cardiometabolic pathways that take decades to kill**. That
is the *wrong causal pathway* for a 16-19-year-old. The pathway by which sleep restriction plausibly
kills people that age — **drowsy driving, and to a lesser extent impulsivity and suicide risk** — is
**completely unmeasured in all 28 records**, and it is a pathway with a short latency, an acute
dose-response, and a mechanism that would operate *during* the exposure window rather than as a
lifelong residue.

**Consequence for the pipeline:** my ≈0.006-0.05-month exposure-window estimate is an estimate of the
**wrong-mechanism** contribution and is likely an **underestimate of the true adolescent-window
effect**. If another shard holds crash-risk or suicide-risk evidence, **that pathway could dominate
the entire answer**, and it should not be netted against my figure — it should be added to it. If no
shard holds it, the final report should say so, because it is the most decision-relevant thing about
this subject's exposure that this factory will not have measured.

Runner-up gaps, in order:
1. **Eight of my 28 records are one cohort (UK Biobank).** The apparent independence of the objective
   literature is largely illusory. `cohort_family` is populated on every effect; gate G6 must enforce it.
2. **No T1 or T2 evidence exists in this domain.** There is no trial and no quasi-experiment of sleep
   duration on mortality, and there never will be. The best available tier is T3/T4, and the T3
   evidence disagrees with itself.
3. **Nobody has measured the decay constant.** The whole question is whether a past exposure leaves a
   residue and for how long, and not one study in this literature reports a time-since-exposure
   coefficient.
