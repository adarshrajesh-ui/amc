# Psychiatric outcomes of chronic short sleep in adolescents and young adults

Shard `s12_psychiatric`. 57 candidate records screened, 42 extracted, 161 effect estimates.
Every number below is quoted verbatim in the corresponding YAML record; nothing here is recalled
from memory. Study identifiers are `study_id` values in this directory.

---

## Headline

The observational association between short sleep and depression in young people is large
(OR 1.5-2.8). The causally identified effect is small (d 0.12-0.31), and when the depression scale
is decomposed item by item, the causally identified effect **lands almost entirely on fatigue and
sleep items rather than on depressed mood**. My best estimate is that **55-70% of the observational
association is not a causal effect of sleep duration on mood** — roughly half of that from reverse
causation, the rest from confounding and from depression instruments re-measuring the exposure.

For the subject specifically — an 18-year-old **male** whose restriction is **workload-imposed, not
insomnia** — three independent features of the evidence all push the estimate down. The honest
bottom line is a **modest** excess risk of depression (on the order of **+1 to +3 percentage points**
of past-year MDE risk, and plausibly near zero), a **real and larger** effect on irritability,
anxiety, low positive affect and emotional dysregulation, and a suicide-mortality excess that is
**too small to estimate reliably at the individual level** (order of 1 extra death per 20,000-25,000
similarly exposed males per year, from a base rate of 17-28 per 100,000).

---

## 1. The observational association

### Sleep duration and depression

| source | exposure | estimate | n | tier |
|---|---|---|---|---|
| `zhai2015` | short vs normal sleep duration | **RR 1.31** (1.04-1.64), 7 studies, I²=0% | 25,271 | T5 |
| `zhai2015` | LONG vs normal sleep duration | **RR 1.42** (1.04-1.92) | 23,663 | T5 |
| `short2020` | short sleep -> any mood deficit, adolescents | **OR 1.55** (1.44-1.67), 23 studies | 361,505 | T5 |
| `short2020` | short sleep -> depressed mood | **OR 1.62** (1.38-1.85) | | T5 |
| `hertenstein2019` | **insomnia** -> incident depression | **OR 2.83** (1.55-5.17) | | T5 |
| `marino2021` | disturbed sleep -> depression, **baseline-depression-adjusted** | **OR 1.50** (1.13-2.00) | 28,895 | T5 |

Two things in this table matter more than the point estimates.

**`zhai2015` is an adult meta-analysis, not an adolescent one.** My task described it as adolescent;
it is not — seven prospective studies of adults. I report reality. It also finds *long* sleep
(RR 1.42) more strongly associated with depression than *short* sleep (RR 1.31). Long sleep has no
plausible mechanism for causing depression and is a classic marker of prodromal illness, so the
long-sleep arm is effectively a **built-in positive control for confounding and reverse causation**,
and it is larger than the exposure of interest. `zhang2024_mr` confirms the long-sleep association is
genetically null.

**The effect size tracks the exposure definition, not the sleep deficit.** Insomnia gives OR 2.83;
short duration gives OR 1.55-1.62; baseline-adjusted disturbed sleep gives OR 1.50. The subject has
the *weakest* of these exposures.

`lovato2014`, named in my task, is real and correctly described but reports **no pooled effect
size** — a qualitative model only. It cannot contribute a number.

### Suicidality, with absolute prevalences

Absolute numbers were mandatory, so these are stated as prevalences, not only ratios.

`winsler2015` (n=27,939, Fairfax County), raw cross-sectional prevalence by reported weekday sleep:

| weekday sleep | felt sad/hopeless | suicidal ideation | suicide attempt |
|---|---|---|---|
| 9 h | 19.2% | **8.1%** | 1.8% |
| 4 h | — | **31.5%** | — |

`wang2024_yrbs` (n=73,356, national YRBS), insufficient sleep vs sufficient:

| outcome | adjusted OR | 2019 absolute prevalence |
|---|---|---|
| suicidal ideation | 1.38 (1.28-1.48) | 11.0% |
| suicide plan | 1.34 (1.23-1.46) | 9.5% |
| suicide attempt | 1.24 (1.17-1.38) | 4.5% |
| injurious attempt | — | 0.9% |

`chiu2018` (dose-response, n=598,281) finds a **curvilinear** relationship for ideation and attempts
with a **nadir at 8-9 h**, and OR 0.89 per extra hour for suicide plans. Notably, depression did
**not** moderate the association.

The 8.1% -> 31.5% gradient in `winsler2015` is the largest number in my shard and it is also the
least trustworthy: raw, unadjusted, cross-sectional, self-reported on both sides, in a sample where
the 4-hour sleepers are a small and highly selected group. It should not be read as a risk
difference. The adjusted YRBS ORs of 1.24-1.38 are the defensible version of the same signal, and
note how the effect **shrinks as the outcome gets harder**: ideation 1.38 -> plan 1.34 ->
attempt 1.24. Effects that attenuate as outcome severity increases are a signature of reporting
correlation rather than causation.

---

## 2. Experimental mood effect size

This is where the evidence is strongest for a genuine causal effect, and where the pattern of
*which* emotions move is unmistakable.

`palmer2024` (Psychological Bulletin; 154 experiments, 1,338 effect sizes, n=5,717, healthy
participants only) is the definitive synthesis:

| outcome | pooled SMD |
|---|---|
| **positive affect** | **-0.27 to -1.14** (reduced) |
| **anxiety symptoms** | **+0.57 to +0.63** (increased) |
| emotional arousal blunting | -0.20 to -0.53 |
| **negative affect and depressive symptoms** | **mixed; no consistent pooled effect** |

`baum2014` (adolescents 14-17, 5 nights 6.5 h vs 10 h TIB, the best-matched chronic-restriction
experiment):

| POMS subscale | d |
|---|---|
| tension-anxiety | **-0.46** (-0.75, -0.17) |
| anger-hostility | **-0.44** (-0.73, -0.15) |
| emotion regulation problems | **-0.38** (-0.67, -0.10) |
| oppositionality/irritability | **-0.35** (-0.63, -0.06) |
| **depression-dejection** | **0.00** (-0.28, 0.28) |

`talbot2010` (the Talbot/Dahl seed; 2 nights, max 2 h on night 2):

| outcome | d_z |
|---|---|
| **positive affect** | **+0.77** (0.47, 1.06) — worse |
| **negative affect** | **null, \|d_z\| < 0.13** |
| anxiety during catastrophising | +0.33 (0.06, 0.59) |
| threat appraisal of own worst worry | +0.28 (0.01, 0.56) |

`motomura2013` (5 nights 4 h TIB, **young males**, actigraphy-verified 4.60 h vs 8.09 h):
left amygdala reactivity to fearful faces **d_z = 1.50** (0.73, 2.26), FWE-corrected; reduced
amygdala–ventral-anterior-cingulate connectivity; **POMS Depression d_z = 0.11**.

`vandyk2017` (sleep *extension* in habitually short-sleeping adolescents, ~+1.2 h): improvements in
sleepiness, **anger, vigor, fatigue and confusion**; depression and anxiety not reported as improved.

**Mood versus cognition, as requested.** The affective effect is roughly **1.5-2x** the
neurocognitive effect for the same exposure class: `palmer2024` gives |SMD| 0.57-0.63 for anxiety
and 0.27-1.14 for positive affect, against `lowe2017` g = -0.383 overall neurocognition
(-0.409 sustained attention, -0.324 executive function, -0.192 long-term memory). `pilcher1996`
reached the same conclusion 28 years earlier: *"mood is more affected by sleep deprivation than
either cognitive or motor performance."* So yes — the mood effect is larger than the performance
effect, and my task's expectation is confirmed.

**But the requested framing needs one correction, and it is the most important finding in this
shard.** "Mood" in this literature is not depression. Across five experiments and one 154-study
meta-analysis, sleep loss reliably degrades **positive affect, anxiety, anger, irritability and
emotional regulation**, and reliably *fails* to move **depressed mood** — `baum2014` d = 0.00,
`motomura2013` d_z = 0.11, `talbot2010` |d_z| < 0.13, `palmer2024` "mixed." Depression requires
depressed mood or anhedonia. Sleep restriction hits the anhedonia/low-energy axis hard and leaves
the dysphoria axis untouched, at least over days to weeks.

---

## 3. Intervention effect size (the strongest causal test)

| source | population | outcome | effect |
|---|---|---|---|
| `scott2021` | 65 RCTs, n=8,608 | depression | **g = -0.63** (-0.83, -0.43) |
| `scott2021` | outliers removed | depression | **g = -0.47** (-0.57, -0.37) |
| `scott2021` | | anxiety | **g = -0.50** (-0.76, -0.24) |
| `scott2021` | | composite mental health | g = -0.53 (-0.68, -0.38) |
| `scott2021` | **publication-bias adjusted** | composite | **g = -0.35** (-0.55, -0.16) |
| `freeman2017` (OASIS) | 3,755 students, digital CBT-I | depression | **d = -0.48** |
| `freeman2017` | | anxiety | **d = -0.33** |
| `gee2019` | 18 RCTs, n=5,908 | depression | **SMD = -0.45** |
| `gee2019` | mental-health populations | depression | SMD = -0.81 |
| `gebara2018` | comorbid insomnia+depression | HAM-D / BDI | -1.29 / -0.68 |
| `blake2017` | adolescent CBT sleep interventions | **sleep gain** | ~**+30 min** TST |
| `blake2016_sense` | at-risk adolescents | anxiety improved; **depression not** | |

Randomised evidence therefore does establish a causal sleep -> mood arrow, at d ≈ 0.35-0.5 after
bias adjustment. **Three caveats decide how much of this transfers to the subject.**

1. **Every one of these trials treats insomnia or poor sleep quality, not short sleep duration.**
   The mechanism being manipulated is sleep continuity and sleep-related cognition in people
   distressed about their sleep. The subject is not distressed about his sleep; he is short of
   sleep opportunity. `freeman2017`'s intervention is CBT-I; `gebara2018`'s population is comorbid
   insomnia-plus-depression; `gee2019`'s largest effect (-0.81) is in mental-health populations.
2. **The achievable dose is small.** `blake2017` shows the best adolescent sleep interventions buy
   about **30 minutes**. The subject's deficit is roughly 2 hours on weekdays. No trial has
   demonstrated that a 2-hour extension is achievable, let alone measured its mood effect.
3. **`blake2016_sense`, the trial that deliberately excluded depressed adolescents, improved
   anxiety and not depression** — the same dissociation as the experimental literature.

---

## 4. Mendelian randomization, both directions, insomnia and duration separated

The two axes behave completely differently, exactly as my task anticipated.

### Insomnia axis — bidirectional, roughly symmetric

| study | insomnia -> MDD | MDD -> insomnia |
|---|---|---|
| `sun2022_mr` | **OR 1.31** | **OR 1.37** |
| `cai2021_mr` | bxy **0.57** | bxy **0.16** |
| `gao2019_mr` | **no significant effect** | — |
| `zhang2024_mr` | **OR 1.233** | — |

### Sleep duration axis — forward effect null or near-null, reverse effect present

| study | direction | estimate |
|---|---|---|
| `sun2022_mr` | continuous sleep duration -> MDD | **NULL** (no point estimate published) |
| `sun2022_mr` | MDD -> sleep duration | **OR 0.92**, significant |
| `zhang2024_mr` | **continuous** duration -> MDD | **OR 0.998** — effectively null |
| `zhang2024_mr` | **dichotomous short** sleep -> MDD | **OR 1.179** |
| `zhang2024_mr` | long sleep -> MDD | null |
| `daghlas2021_mr` | 1 h **earlier** sleep midpoint -> MDD | **OR 0.77** |

Three points the modeller should not miss.

**Genetically proxied continuous sleep duration does not cause depression.** Two independent MR
studies agree (`sun2022_mr` null, `zhang2024_mr` OR 0.998). Meanwhile **depression does causally
shorten sleep** (`sun2022_mr` OR 0.92). On the duration axis, MR supports the reverse arrow and not
the forward one.

**`zhang2024_mr` contains an internal contradiction that is itself informative.** Continuous
duration is null (0.998) but *dichotomous short sleep* is not (1.179). A dichotomous "short sleeper"
instrument in UK Biobank inevitably picks up people who sleep briefly *because they cannot sleep* —
i.e. it is partly an insomnia instrument. The most parsimonious reading of the whole MR literature
is that **the causal signal lives on the insomnia axis, and short-sleep instruments inherit it by
contamination**. That reading is bad news for people with insomnia and good news for the subject.

**`daghlas2021_mr` is the MR result most transportable to him.** A 1-hour earlier sleep *midpoint*
lowers MDD risk with OR 0.77 — a larger and cleaner effect than anything on the duration axis. The
subject's workload almost certainly delays his sleep midpoint on weekdays. Combined with `lu2026_sjl`
(social jetlag > 2 h: OR 1.87 for depression, though the authors rate certainty "very low") and
`kok2026` (going to bed later than intended: ~0.9 h less sleep and worse next-day mood), **sleep
timing and its weekday/weekend instability is a better-supported risk pathway for this subject than
sleep duration per se.**

---

## 5. What fraction of the observational association is reverse causation?

Seven routes, all arithmetic in `reverse_fraction.py`, all inputs quoted in the YAML records.

| route | method | reverse / non-causal share |
|---|---|---|
| 1a | `roberts2014` both arrows, one sample | **40%** (symptoms), **52%** (major depression) |
| 1b | `marino2022_qlscd` cross-lagged, one model, ages 10-12 | **47%** |
| 1b | same, ages 12-13 | **100%** (only reverse arrow survives) |
| 1b | same, ages **13-17** | both arrows **null** |
| 2 | MR both directions, insomnia axis | **22%** (`cai2021_mr`) to **54%** (`sun2022_mr`) |
| 3 | baseline-depression adjustment, cross-study | ~61% *(weak: different studies)* |
| 4 | covariate adjustment within `short2020` (OR 1.67 -> 1.28) | **52%** |
| 5 | observational vs MR, duration axis | **39%** to ~**100%** |
| 6 | quasi-experimental vs observational magnitudes | see below |
| 7 | **criterion contamination** (`sadikova2024`) | **~100% of the scale effect** |

**Routes 1 and 2 converge on roughly one half.** Two independent prospective cohorts modelling both
arrows in one sample give 40%, 47% and 52%. MR on the insomnia axis gives 22-54%. Reverse causation
alone accounts for **about 40-50%** of the observational association.

One precision caveat on route 1a. In `roberts2014` the *major depression* pair has both arrows
individually significant (forward OR 3.76, 1.65-8.58; reverse OR 4.28, 2.21-8.32), so the 52% figure
is solid. The *depressive symptoms* pair does not: the reverse coefficient is OR 1.24 (**0.94-1.63**),
which crosses 1. The 40% share on that outcome therefore rests on a non-significant reverse arrow and
should be treated as indicative only. `marino2022_qlscd`'s 47% has both arrows significant.

**Route 4 adds confounding.** Inside a single meta-analysis, moving from unadjusted to maximally
adjusted estimates shrinks the mood-deficit OR from 1.67 to 1.28 — **52% of the log-OR removed by
covariates alone**, and adjustment is always incomplete.

**Route 7 is a third mechanism I did not anticipate, and it is the largest.** `sadikova2024` is an
instrumental-variable analysis of the START school-start-time natural experiment (n=2,134) — the
best-identified causal estimate in my domain, and the one whose exposure actually matches the
subject's. It decomposed the 6-item Kandel-Davies depression scale:

| component | ITT effect at 2 years |
|---|---|
| **total score** | **-0.26** (-0.50, -0.02) — significant |
| **fatigue items** ("too tired to do things", "trouble sleeping") | **-0.91** (-1.45, -0.38) — significant, 3.5x larger |
| **mood items** (unhappy/sad/depressed, hopeless, nervous, worrying) | **-0.03** (-0.09, 0.02) — **null** |

The two fatigue items contribute (2/6) x -0.91 = -0.303 of a total effect of -0.26 — i.e.
**~117%, the entire effect**. A causally identified increase in adolescent sleep reduced the
depression *score* by making adolescents less tired, and did not detectably reduce sadness,
hopelessness or worry. This replicates independently in the same cohort by a different estimator
(`berger2026_start`, difference-in-differences: *"These differences were primarily driven by the
items in the scale related to fatigue"*), and `talbot2010`'s authors predicted it in 2010:
*"The POMS may indicate greater mood disturbance in part because some of its scales overlap with
sleepiness, such as fatigue and vigor."*

The START investigators state the implication themselves: their policy could reduce *"either the
prevalence of depression **or the prevalence of children whose chronic tiredness leads to
misdiagnosis of depression**."*

### My estimate

**55-70% of the observational short-sleep/depression association in young people is not a causal
effect of sleep duration on mood.** Decomposed: ~40-50% reverse causation and confounding
(routes 1-5, which overlap and cannot simply be added), plus a further large share of whatever
remains attributable to depression instruments containing sleep and fatigue items (route 7).

Two honest caveats. `zink2024_abcd` (n=10,828) found the association **unidirectional** — reverse
arrow null in both sexes — which argues *against* a large reverse share; I record it rather than
suppress it. And routes 3 and 5 are cross-study comparisons, so they are the weakest links.

---

## 6. Workload-imposed restriction versus insomnia: the quantified difference

This is the question that most changes the subject's estimate, and enough evidence exists to answer
it semi-quantitatively. Ordering exposures from most to least insomnia-like:

| exposure | source | effect on depression |
|---|---|---|
| insomnia disorder -> incident depression | `hertenstein2019` | **OR 2.83** (1.55-5.17) |
| insomnia (genetic) -> MDD | `sun2022_mr`, `zhang2024_mr` | **OR 1.31**, **1.23** |
| self-reported short sleep, unadjusted | `short2020` | **OR 1.67** |
| self-reported short sleep, adjusted | `short2020` | **OR 1.28** |
| genetically proxied *short sleep* (dichotomous) | `zhang2024_mr` | **OR 1.179** |
| **imposed late bedtime (parental rule), 2 h swing** | `gangwisch2010` | **OR 1.24** (1.04-1.49) |
| **imposed sleep gain (school start policy), +30 min** | `sadikova2024` | **d = -0.156**, mood component **null** |
| **imposed sleep gain (pooled DSST), +69 min** | `wang2026_dsst` | **g = -0.20** |
| genetically proxied *continuous* duration -> MDD | `sun2022_mr`, `zhang2024_mr` | **NULL**, **OR 0.998** |

**The gradient is monotone and spans a factor of about ten.** Insomnia disorder, OR 2.83. Imposed
short sleep opportunity, OR ≈ 1.2 / d ≈ 0.12-0.31. Continuous sleep duration in MR, null.

Three quasi-experiments with genuinely exogenous exposures — a parental bedtime rule
(`gangwisch2010`), a school-start-time policy analysed as an instrument (`sadikova2024`), and a
pooled set of start-time delays (`wang2026_dsst`) — **converge independently on |d| ≈ 0.12-0.31**.
That is the right magnitude class for the subject, and it is roughly **a quarter to a half** of what
the insomnia literature reports.

`gangwisch2010` also shows that this route is real rather than merely small: ~69% of the effect of an
imposed late bedtime on depression, and ~53% of its effect on suicidal ideation, is mediated through
actually obtaining less sleep. So imposed short sleep does causally move these outcomes — the effect
is simply modest, and per `sadikova2024` its measurable part is concentrated in fatigue.

### Sex: a second, independent downgrade

The subject is male, and four studies with four different designs found the depression/anxiety
association concentrated in females:

- `conklin2018_basus`: chronic short sleep predicted depression in young **women** (adjusted
  Cohen's D 0.13), **not** in young men.
- `short2015`: after total sleep deprivation, depressed mood and anxiety worsened in **female**
  participants only.
- `zink2024_abcd` (n=10,828): significant associations **"among females only"**; nothing in males.
- `wang2024_yrbs`: associations stronger in girls; male trends non-significant.

Dissent: `marino2022_qlscd` found no sex moderation (χ²₃₃ = 29.5, p = .64) — but that is a global
invariance test, far less sensitive than stratified estimation. I read the balance of evidence as a
genuine and consistently replicated attenuation in males for *depression* outcomes.

**The critical asymmetry: this does not extend to suicide mortality.** Males aged 15-19 die by
suicide at **3.3x** the female rate (`cdc_suicide_rates`: 17.3 vs 5.2 per 100,000). Lower
self-reported ideation in males coexists with far higher lethality. Any downgrade of the subject's
*depression* risk on sex grounds must not be carried across to *suicide* risk.

### Age: a third downgrade

`marino2022_qlscd` modelled both arrows across five adolescent waves to age 17. Both were significant
at ages 10-12; only the reverse arrow at 12-13; and **neither direction was detectable after age 13**.
The subject is 18. In the one cohort that looks, the sleep-depression coupling is a phenomenon of
early adolescence. I hold this loosely — n = 1,113 with attrition, so a null may be low power — but it
points the same way as everything else.

---

## 7. Absolute risk numbers for an 18-19 year old male

### Base rates

| quantity | value | source |
|---|---|---|
| past-year major depressive episode, ages 18-25, **both sexes** | **17.2%** (2020) | `goodwin2022` |
| male-specific MDE rate, 18-25 | **not quotable from my sources**; male rates are lower. Working range **9-12%** | — |
| suicide mortality, **male 15-19** | **17.3 per 100,000/year** | `cdc_suicide_rates` |
| suicide mortality, **male 20-24** | **27.9 per 100,000/year** | `cdc_suicide_rates` |
| suicide mortality, female 15-19 (comparator) | 5.2 per 100,000/year | `cdc_suicide_rates` |
| suicidal ideation prevalence, HS students, 2019 | 11.0% | `wang2024_yrbs` |
| suicide attempt prevalence, 2019 | 4.5% | `wang2024_yrbs` |
| injurious suicide attempt, 2019 | 0.9% | `wang2024_yrbs` |

The 9-12% male working range is **my inference**, not a quoted figure — `goodwin2022` reports the
combined-sex 17.2% and states male rates are lower. Flagged so the modeller can widen it.

### Depression: absolute excess for this subject

| assumed causal OR | source of the OR | absolute excess in past-year MDE risk |
|---|---|---|
| **1.00** | continuous-duration MR (`sun2022_mr`, `zhang2024_mr`) | **0.0 pp** |
| **1.179** | genetic short sleep (`zhang2024_mr`) | **+1.4 to +1.9 pp** |
| **1.24** | imposed bedtime quasi-experiment (`gangwisch2010`) | **+1.9 to +2.5 pp** |
| **1.28** | adjusted observational (`short2020`) | **+2.2 to +2.9 pp** |

So: **on the order of +1 to +3 percentage points on a base of 9-12%, and plausibly zero.** I would
weight the low end, because the two estimates with the cleanest identification and the best-matched
exposure (continuous-duration MR, and `sadikova2024`'s mood-item decomposition) are both null, and
because the male-specific findings are null in three of four studies that looked.

### Suicide mortality: absolute excess

Applying an *ideation* OR to a *death* rate overstates the risk — `wang2024_yrbs` shows the effect
shrinking from ideation (1.38) to attempt (1.24), so the OR for death is likely lower still. With
that caveat, from a base of ~20 per 100,000 per year:

| assumed OR | absolute excess | interpretation |
|---|---|---|
| 1.20 (`gangwisch2010` ideation) | **+4.0 per 100,000/year** | ~1 extra death per **25,000** exposed males per year |
| 1.24 (`wang2024_yrbs` attempt) | **+4.8 per 100,000/year** | ~1 extra death per **20,800** exposed males per year |

Over three years of exposure: roughly **1 extra death per 7,000-8,300** similarly exposed males.
This is an upper bound and it is far too small to be meaningful for one individual; it matters at
population scale, not in a personal risk assessment.

### What he is most likely actually experiencing

The effects best supported for his exposure are **not** major depression. They are, with the
experimental effect sizes attached:

- **irritability and anger** — `baum2014` d = -0.44, `short2020` OR 1.83, `vandyk2017` improved on
  extension
- **anxiety and threat sensitivity** — `palmer2024` SMD 0.57-0.63, `baum2014` d = -0.46,
  `talbot2010` d_z = 0.33
- **loss of positive affect / anhedonia** — `palmer2024` SMD up to -1.14, `talbot2010` d_z = 0.77,
  `short2020` OR 2.02
- **impaired emotional regulation** — `baum2014` d = -0.38, with the neural correlate in
  `motomura2013` (amygdala d_z = 1.50 in young males, reduced prefrontal coupling)
- **fatigue that will score as depression on any standard instrument** — `sadikova2024`,
  `berger2026_start`

These are largely **reversible**: `vandyk2017` extended sleep by ~1.2 h in habitually short-sleeping
adolescents and anger, vigor, fatigue and confusion all improved.

---

## 8. What would change these conclusions

1. **A randomised sleep-extension trial in healthy short-sleeping young adults with depression and
   anxiety as primary outcomes, reported at item level.** It does not exist. `vandyk2017` is the
   closest (n=54, feasibility, ~1.2 h, mood secondary).
2. **Any depression measure that excludes sleep and fatigue items**, used in a causal design. The
   entire route-7 argument rests on one cohort analysed twice.
3. **Sex-stratified estimates from the quasi-experiments.** `gangwisch2010` and `sadikova2024` both
   have the data; neither published the split. Given how consistent the female-specific pattern is,
   this is the highest-value missing number in my domain.
4. **MR restricted to non-insomnia short sleep.** Would directly test whether the `zhang2024_mr`
   dichotomous-vs-continuous contradiction is instrument contamination.

---

## Files

- 42 YAML records, 161 effect estimates, all validating against `effect.schema.json` (`validate.py`)
- all 41 PubMed-indexed citations audited against `esummary`, 0 discrepancies (`audit_citations.py`)
- `screening_log.md` — 57 screened, 42 included, 16 excluded with reasons
- `reverse_fraction.py` / `.txt` — the seven-route reverse-causation and absolute-risk arithmetic
- `convert.py`, `convert_batch2.py` / `conversions*.txt` — every effect-size conversion
- `station_report.md` — confidence, failures, and the single biggest gap
