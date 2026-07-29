# s10_immune — immune competence, infection, vaccine response and inflammation under short sleep

Target case: **18-year-old male**, weekday sleep ~5-6 h since age 16, weekends 7-8 h, occasional
3-4 h pre-exam nights and occasional 10-11 h weekend nights.

**One-paragraph bottom line.** The immune evidence for chronic short sleep is much weaker and much
more marker-specific than its reputation. The strongest finding in the domain is not "short sleep
weakens immunity" but "sleep in the few days around an immunisation measurably shapes the antibody
response" (pooled effect size 0.79 for objectively measured short sleep, 0.93 in men). For infection,
the best-identified study — an actigraphy-plus-viral-challenge experiment — found that short sleep
predicted developing a *cold* but **not** becoming *infected*, meaning the effect is on symptom
expression rather than host resistance. For inflammation, the largest observational meta-analysis
found that categorical short sleep duration was **not** significantly associated with either CRP or
IL-6; the significant associations were for *insomnia/sleep disturbance* and for *long* sleep. Every
inflammatory change measured during restriction is either reversible within 2 nights of extended
sleep, or reverses partially, and no study anywhere has demonstrated durable immune impairment from
years of adolescent short sleep — the one longitudinal adolescent dataset with an objective outcome
found the shortest-sleeping trajectory had **no** elevation in adult CRP.

---

## 1. Infection risk in ABSOLUTE terms

Every number below is quoted or derived from a record in this shard. "Derived" means I computed it
from published ORs plus category sample sizes plus the reported total event count; the arithmetic is
in `_tools/backcalc.py` and each derivation is labelled in the source YAML.

### The rare quasi-experiment: rhinovirus challenge with objective exposure

`prather2015_rhinovirus` (T2, n=164, ages 18-55, 7 nights of actigraphy before a standardised
RV39 nasal challenge). This is the highest-quality infection evidence that exists.

| Actigraphic sleep | n | OR for clinical cold (vs >7 h) | Absolute cold rate (derived) |
|---|---|---|---|
| <5 h | 36 | **4.50** (1.08–18.69) | 39.7% |
| 5–6 h | 54 | **4.24** (1.08–16.71) | 38.3% |
| 6.01–7 h | 52 | 1.66 (0.40–6.95) — **null** | 19.6% |
| >7 h | 22 | 1 (reference) | 12.8% |

Whole sample: **124/164 (75.6%) became infected, but only 48/164 (29.3%) developed a verified cold.**
The paper's own Figure 1 (adjusted predicted values) gives roughly 45% vs 17% for <5 h vs >7 h, an
absolute gap of ~28 points, which agrees with my back-calculated ~27 points by a different route.

**The single most important caveat in this entire shard:** sleep duration did *not* predict whether
infection took hold. Verbatim — *"in adjusted analyses, actigraphy assessed sleep duration was
unrelated to rates of infection (b = -0.11, SE = 0.17, P = 0.543)."* The authors attribute the cold
effect "primarily" to **illness expression** among the already-infected. So this is evidence about
symptom generation, not about host resistance to viral entry.

**Dose-calibration warning:** actigraphic mean sleep was 5.8 h while diary mean *in the same people*
was 7.5 h. A student who *reports* 5-6 h is probably in this study's *"<5 h"* actigraphic band.
Self-reported and objective hours are not interchangeable anywhere in this literature.

### The earlier challenge study

`cohen2009_cold` (T2, n=153, ages 21-55, 14 days of self-reported sleep before rhinovirus challenge).

| Exposure | OR for verified cold | Absolute rate (derived) |
|---|---|---|
| Duration <7 h vs ≥8 h | **2.94** (1.18–7.30) | 46.7% vs 23.0% |
| Duration 7–<8 h vs ≥8 h | 1.63 (0.63–4.19) — **null** | 32.7% |
| Efficiency <92% vs >98% | **5.50** (2.08–14.48) | 49.9% vs 15.3% |
| Efficiency 92–98% vs >98% | **3.94** (1.50–10.37) | 41.6% |

Note that **sleep efficiency (OR 5.50) beat sleep duration (OR 2.94)**, and that here too the
association was with clinical illness, not with infection.

### Population-scale absolute rates

| Source | Population | Outcome | Short sleep | Referent | Absolute gap |
|---|---|---|---|---|---|
| `pratherleung2016_nhanes` | 22,726 US adults, mean 46 y | head/chest cold, 30 d | 19.0% (≤5 h) | 15.5% (7–8 h) | **+3.5 points** |
| `pratherleung2016_nhanes` | same | flu/pneumonia/ear, 30 d | 5.9% (≤5 h) | 3.3% (7–8 h) | **+2.6 points** |
| `martinezalbert2025_infection` | 642 adults, **57% aged 18–25** | cold, 30 d | 37.2% (≤6 h) | 26.5% (7–8 h) | **+10.7 points** |
| `patel2012_pneumonia` | 56,953 nurses, 37–57 y | incident pneumonia | 6.5 /1000 py (≤5 h) | 3.8 /1000 py (8 h) | **+2.7 /1000 py** |
| `forthun2023_gp_infection` | 1,848 GP attenders, Norway | any infection, 3 mo | 62.1% (<6 h) | 48.6% (7–8 h) | **+13.5 points** |

Put plainly: even taking these associations at face value, the serious-infection effect is about
**one extra pneumonia per 370 short-sleeping person-years**, and the cold effect in a
nationally representative sample is about **one extra cold-month per 29 short sleepers per month**.

### Four reasons to discount these observational numbers

1. **A 6-hour null.** In 22,726 Americans, 6 h/night showed *no* excess colds (OR 1.02) and *no*
   excess infections (OR 0.97). Everything is carried by ≤5 h. `patel2012_pneumonia` likewise: 6 h
   was significant age-adjusted (RR 1.29) but **null** after full adjustment (RR 1.17, 0.96–1.41).
   `prather2015_rhinovirus` places its threshold at ~6 h actigraphic. Three independent datasets
   locate the inflection at 5-6 h, i.e. right at the boundary of the subject's exposure.
2. **A symmetric U-shape.** Long sleep is as bad or worse in five separate datasets:
   pneumonia RR 1.38 (≥9 h) vs 1.39 (≤5 h); cold OR **3.60** (≥9 h) vs 1.83 (≤6 h); GI infection
   RR 2.33 (>9 h) vs 1.92 (<6 h). Long sleep is not plausibly immunosuppressive, so a symmetric U
   is a signature of reverse causation and shared confounding.
3. **Site-specificity that goes the wrong way.** `forthun2023_gp_infection` disaggregated by site:
   the *respiratory* component — the mechanism everyone invokes — was **null** (RR 1.16, 0.96–1.42).
   `martinezalbert2025_infection`: no sleep variable predicted any infection *other than* colds.
4. **A Mendelian randomization result pointing the other way.** `zhang2023_mr_inflammation` found
   genetically predicted CRP causally associated with *longer* sleep (0.017, CI 0.003–0.031) and
   *less* short sleep, concluding *"elevated CRP and IL-6 have causal effects on longer sleep
   duration."*

---

## 2. Vaccine response — the strongest signal in the domain

`spiegel2023_vaccine_meta` (T1, 7 studies; the authors obtained participant-level data from the
original investigators). Positive effect size = short sleep associated with **lower** antibody.

| Analysis | n | Effect size (95% CI) |
|---|---|---|
| **Objectively measured** short sleep (<6 h), ages 18–60 | 304 | **0.79 (0.40–1.18)** |
| — experimental studies only | 133 | **0.86 (0.28–1.44)** |
| — prospective studies only | 171 | **0.67 (0.18–1.16)** |
| — **men** (the sex-matched estimate) | — | **0.93 (0.54–1.33)** |
| — women | — | 0.42 (−0.49–1.32) — **null** |
| **Self-reported** short sleep, ages 18–85 | 504 | 0.29 (−0.04–0.63) — **null** |
| Self-reported, exploratory, ages 18–60 only | 299 | **0.59 (0.12–1.05)** |

**Magnitude anchor, from the paper itself:** *"The ES for waning over two months was 0.79,
essentially identical to the ES estimated for objectively assessed short sleep duration."* Sleeping
<6 h around a vaccination costs roughly the same antibody as letting the vaccine age two months.

**Individual primaries:**

- `spiegel2002_influenza_vaccine` (T1, n=25 young men, 4 h × 4 nights before + 2 after): day-10
  antibody **less than half** of controls. *Access caveat: paywalled JAMA letter with no abstract;
  all numbers are secondhand from three sources I verified.*
- `lange2003_hepa` (T1, n=19, one night of total deprivation after hepatitis A vaccination):
  **nearly two-fold higher** titre at 4 weeks in the sleep group (p=.018).
- `lange2011_memory` (T1, n=27 men, 3 vaccinations): sleep **doubled** antigen-specific Th cell
  frequency and raised IgG1, **followed for 1 year**. Three wake-condition participants needed
  re-vaccination because they never reached seroprotection; **zero** in the sleep condition.
- `prather2012_hepb` (T4, n=125 midlife, actigraphy): each **+1 h** of sleep → **+56%** secondary
  antibody, and OR **3.53** (1.22–10.27) for being clinically protected at 6 months. Sleeping <6 h
  vs >7 h: OR of protection **0.09** (0.01–0.94). Diary-reported sleep was **null in the same people**.

**Two nulls that constrain how far to push this:**

- `benedict2012_h1n1` (T1, n=24): day-5 deficit in men only, **gone by day 10 and null out to day 52**.
  Title: *"Acute sleep deprivation has no lasting effects on the human antibody titer response."*
- `jaiswal2024_breakthrough` (T4, n=5,265 + 2,583, **objective** wearable sleep, real-world outcome):
  *"Sleep duration was not associated with breakthrough infection after COVID vaccination."*
  This is the clinical endpoint the antibody literature is a proxy for, and it is null.
- The only college-student vaccine data I located (cited in `besedovsky2019_review`) was also null:
  influenza response did not differ between 133 students with and without insomnia.

Reconciliation: antibody protection is a saturating function of titre, so a 0.79-SD titre shift in
already-protected young people need not produce measurable breakthrough infection.

---

## 3. Inflammation — what the meta-analyses actually found, including the nulls

### `irwin2016_inflammation_meta` (72 studies, >50,000 participants)

This is the paper most often cited for "short sleep causes inflammation." **It does not say that.**

| Exposure | CRP | IL-6 |
|---|---|---|
| **Short sleep duration, categorical (extreme)** | **0.08 (−0.01–0.16) — NULL** (11 samples, N=19,573) | **0.08 (−0.02–0.18) — NULL** (8 samples, N=12,925) |
| Short duration, continuous, combined | **0.09 (0.01–0.17)** — significant but ~1/10 SD (16 samples) | 0.11 (−0.01–0.23) — **null** (18 samples) |
| Short duration, continuous, **self-report only** | 0.04 (−0.03–0.11) — **null** | 0.03 (−0.09–0.14) — **null** |
| Short duration, continuous, **objective only** | 0.18 (−0.04–0.41) — **null** | **0.29 (0.05–0.52)** — significant (9 samples, N=489) |
| **LONG sleep duration, categorical** | **0.17 (0.01–0.34)** — significant, ~2× the short-sleep estimate | **0.11 (0.02–0.20)** — significant |
| **Sleep disturbance / insomnia** | **0.12 (0.05–0.19)** — significant | **0.20 (0.08–0.31)** — significant |
| Experimental restriction, multiple nights | 0.61 (−1.09–2.30) — **null**, uninformative | 0.13 (−0.21–0.47) — **null** |
| Experimental total deprivation, 1 night | **−0.43** (−1.62–0.77) — null, point estimate **negative** | 0.16 (−0.11–0.43) — **null** |

TNF-α for categorical short sleep: 0.11 (−0.01–0.22) — **null**.

The paper's own conclusion: **sleep disturbance and long sleep duration, but not short sleep
duration, are associated with increases in markers of systemic inflammation.** The widely repeated
claim that short sleep raises CRP and IL-6 does not survive this meta-analysis in categorical form;
what survives is (a) a tiny continuous CRP effect, (b) an objective-measurement IL-6 effect on 489
people, (c) insomnia, and (d) *long* sleep.

### `ballesio2026_experimental_meta` (35 experimental studies, 887 participants, searched to March 2025)

The best experimental answer, and it is dose-dependent and outlier-fragile:

| Exposure | IL-6 | CRP | TNF-α |
|---|---|---|---|
| **Multiple nights** partial deprivation (~4.3-4.6 h, 3+ nights) | **d=0.42 (0.11–0.73)** *outlier-excluded, k=5* | **d=0.76 (0.09–1.43)** *outlier-excluded, k=5* | **d=−0.34 (−0.88–0.20) — null, wrong direction** |
| — same, **all studies retained** | **d=0.10 (−0.48–0.67) — NULL** (k=6) | **d=0.50 (−0.38–1.38) — NULL** (k=6) | — |
| One night **total** deprivation | d=0.21 (−0.15–0.58) — **null** | d=−0.23 (−0.65–0.19) — **null** | — |
| One night **partial** deprivation | d=0.48 (−0.13–1.10) — **null** | — | — |

Two things must be reported together: the headline positive results (IL-6 0.42, CRP 0.76) **depend
entirely on excluding one study each**; with all studies in, both are null. And **single nights do
nothing measurable** — directly relevant to the subject's occasional 3-4 h pre-exam nights.

Supporting single studies: `vanleeuwen2009_recovery` found IL-6 and IL-1β mRNA up but **TNF-α protein
down (80% of baseline)**; `fondell2011_nk_tcell` found short sleep associated with T-cell function
**49% higher** and NK activity **30% lower** *in the same people on the same mornings*.
"Immune competence" does not move as one thing.

### Adolescent-specific inflammation — the most on-point evidence, and it is null

`stager2023_adolescent_crp` (T5, Add Health, exposure at grades 7-12, mean age 15.7, **objectively
measured adult CRP** ~14 years later). Three trajectories emerged. Adult CRP:

- "shortest" trajectory (24.4% of sample): **3.21 mg/L (SE 0.29)**
- "stable recommended" (67.6%): **3.35 mg/L (SE 0.21)**
- "varied", i.e. rising *above* recommended (8%): **5.23 mg/L (SE 0.68)** — the only elevated group

Derived contrast, shortest vs stable-recommended: **−0.14 mg/L (95% CI −0.84 to +0.56)**. The
shortest-sleeping adolescents had, if anything, *slightly lower* adult CRP. *Honest caveat: the CRP
model's df were (2,127), so this analysis ran on ~130 people and is underpowered; my CI excludes a
large durable elevation but not a small one.* Note also that the paper's abstract says "poor
longitudinal sleep predicted elevated CRP" — but its own numbers show the elevation was in the
*increasing-sleep* group, not the short-sleep group.

`moralesmunoz2024_alspac` is the one prospective result pointing the other way: IL-6 at age 9
partially mediated the link between persistent short sleep **in early childhood (6 months–7 years)**
and psychosis at 24 (estimate 0.003, CI 0.002–0.005). But CRP at both 9 and 15 years was **null**,
the mediated path is tiny relative to the total association (OR 2.50–3.64), and the exposure window
is early childhood, not adolescence.

---

## 4. Reversibility — the transient/durable split

### (a) Transient, and demonstrably so

| Marker | Restriction | Recovery given | Result |
|---|---|---|---|
| 24-h plasma IL-6 (`pejovic2013_recovery`, n=30, mean age 24.7) | 6 h × 6 nights | **2 nights of 10 h** | **Fully normalised**: rose +0.90±0.41 pg/ml, fell −0.93±0.45, residual vs baseline **0.02±0.34, P=0.94** |
| Circulating NK and B cell counts (`vanleeuwen2009_recovery`) | 4 h × 5 nights | 2 nights of 8 h | **"recovered almost completely"** (NK had fallen to 65%, B cells risen to 121%) |
| Leukocyte/neutrophil counts (`faraut2011_nap_recovery`) | one 2 h night | **nap + 8 h, or 10 h** | **"returned nearly to baseline"** |
| Influenza antibody gap (`spiegel2002_influenza_vaccine`) | 4 h × 6 nights | 7 nights of 12 h | **Gap gone by 3–4 weeks** |
| H1N1 antibody gap (`benedict2012_h1n1`) | 1 night total | normal sleep | **Gone by day 10, null to day 52** |

### (b) Incompletely reversible after an ordinary weekend

| Marker | Protocol | Result |
|---|---|---|
| Monocyte IL-6 (`simpson2016_repeated_recovery`, n=14) | **3 weeks of 5×4 h + 2×8 h** — the closest experimental model of the subject's actual pattern | **Still elevated AFTER recovery sleep**, week 2 (p<0.05) and week 3 (p<0.09) |
| Serum CRP (`vanleeuwen2009_recovery`) | 4 h × 5 nights, then 2×8 h | **145% of baseline after restriction, 231% after recovery** — higher after the weekend |
| PBMC IL-6/IL-1β/TNF-α (`vanleeuwen2009_recovery`) | same | *"did not return to baseline levels completely"* |
| Leukocyte/neutrophil counts (`faraut2011_nap_recovery`) | 2 h night, then **8 h only** | **Persisted** |

**The reconciliation, and it is the most useful thing in this section:** `faraut2011_nap_recovery` is
the only study that *varied the recovery dose* while holding restriction constant, and it found that
the same abnormality which **persisted after 8 h** of recovery **resolved after 10 h or after a nap +
8 h**. That maps exactly onto the split between Pejovic (10 h recovery → full normalisation) and
Simpson/van Leeuwen/Faraut (8 h recovery → incomplete). For this subject — 7-8 h weekends with
occasional 10-11 h nights — the prediction is incomplete weekly normalisation on ordinary weekends
and fuller normalisation on the long ones.

### (c) The one genuinely durable signal

`lange2011_memory`: the antigen-specific Th-cell and IgG1 advantage of having slept after vaccination
was **still detectable one year later**, and three deprived participants **never reached
seroprotection** and had to be re-vaccinated. An immunological memory compartment laid down badly is
not remade by catching up on sleep. This is the one place where "transient marker change" is the
wrong frame — but note it required deprivation timed to three separate immunisations, and it concerns
T-cell memory, not circulating cytokines.

### (d) Immune markers recover faster than the brain

In `pejovic2013_recovery`, over the *same* two recovery nights in the *same* people: IL-6 and
sleepiness fully normalised, but objective PVT performance **did not improve**. And in
`simpson2016_repeated_recovery`, participants **subjectively habituated** — *"Sleep restriction was
not perceived to be subjectively stressful"* — while their physiology stayed activated. Feeling fine
on 5-6 h is not evidence of being fine.

---

## 5. Net assessment for the target case

1. **Vaccination timing is the only place with a defensible, decision-relevant effect.** Effect size
   0.93 in men for objectively short sleep, equivalent to two months of natural antibody waning. It
   is also the cheapest to act on: the window is a few days wide, and `prather2021_influenza` localises
   it to the **two nights before** inoculation.
2. **Infection risk is real but small in absolute terms, and probably mis-attributed.** The best study
   found no effect on infection, only on illness expression. The 6 h null recurs across three large
   datasets, the U-shape recurs across five, and the site-specific respiratory null undercuts the
   proposed mechanism.
3. **Systemic inflammation from chronic short sleep specifically is not established.** The largest
   observational meta-analysis is null for categorical short sleep on both CRP and IL-6; the
   experimental meta-analysis is positive only after outlier exclusion; TNF-α trends the wrong way;
   and the one longitudinal adolescent dataset with objective CRP is null.
4. **No evidence of durable immune impairment from years of adolescent short sleep exists**, because
   no study has looked with an adequate design. The absence is a genuine gap, not a demonstrated null —
   except for adult CRP, where `stager2023_adolescent_crp` provides a real, if underpowered, null.
5. **Sleep continuity/quality outperforms duration** as a predictor in essentially every dataset that
   measured both: efficiency OR 5.50 vs duration 2.94 (`cohen2009_cold`); perceived inadequacy RR 1.50
   vs ≤5 h RR 1.39 (`patel2012_pneumonia`); disturbance OR 1.27 vs ≤5 h 1.17 (`pratherleung2016_nhanes`);
   insomnia SMD 0.12/0.20 vs short duration null (`irwin2016_inflammation_meta`). And social jet lag
   predicted colds independently of duration, OR 4.28 (`martinezalbert2025_infection`) — which for a
   student with a weekday/weekend split schedule may be the more relevant exposure axis than hours.

## Files

25 YAML records, 110 effect estimates, all validated against `spec/effect.schema.json` by
`_tools/validate.py`. Identifier verification in `_tools/verification.json` (`_tools/verify.py`);
effect-size arithmetic in `_tools/convert.py` and `_tools/backcalc.py`. Screening in
`screening_log.md`; limitations and gaps in `station_report.md`.
