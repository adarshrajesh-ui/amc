# Station report — `s01_cognition_dose_response`

**Domain:** experimental dose-response between chronic partial sleep restriction (3–7 h TIB, ≥5 consecutive
nights) and objective neurobehavioural performance in healthy people.

**Headline:** 185 records screened, 30 included, 142 effect records extracted, 30/30 identifiers verified
against both Crossref and PubMed (title similarity 1.000 on all 30), 0 schema errors. The dose-response
backbone is solid and quantified. The three-year extrapolation the project actually needs is **not** —
the longest experiment in the entire literature is 42 days, and the published functional forms for
extending beyond it disagree with each other by large factors.

---

## 1. What was produced

| Artefact | Content |
|---|---|
| 30 × `<study_id>.yaml` | 142 effect records, all schema-valid |
| `notes_for_modeller.md` | 1,178 lines; **6 published functional forms** quoted verbatim with fitted parameters, plus a recommended parameterisation and the reasons the forms conflict |
| `screening_log.md` | all 185 PMIDs with decision and reason; 14 exclusion codes |

**Composition.** Tier T1 = 26, TX = 4 (the four modelling/normative papers). Age match: **9 records
`exact_16_19`**, 5 `good_young_adult`, 4 `mixed`, 10 `fair_adult`, 2 `poor_midlife`. Dispersion: 42/142
effects carry both an SE and a CI (43 carry at least one); 25/142 were digitised from figures and are
flagged `from_figure: true`. Six `cohort_family` labels cover the 78 effects drawn from overlapping
samples.

**Verification.** Every identifier resolved; no record needed `secondhand` tier for identifier reasons.
Access splits 14 full text / 16 abstract-only. The abstract-only tier is a data-completeness limit, not a
citation problem — but it does bound what those 16 records contribute, because per-arm means and
dispersions generally live in the body text and tables rather than the abstract. The two that hurt most
are `short2018` (the closest age match in the shard) and `campbell2024`; both are genuinely paywalled with
no OA copy.

---

## 2. The six required extractions

**1. Van Dongen 2003 — done, full text, 14 effects.** This is the deepest record in the shard. Figure 1 was
digitised panel by panel to recover per-arm day-14 values, because the paper publishes trajectories
graphically and coefficients only in text. At day 14 vs the 8 h arm, change from baseline: PVT lapses
**+12.34** (4 h) and **+7.39** (6 h) per 10-min bout; DSST **−14.75** correct responses per 1.5 min (4 h);
serial addition/subtraction **−2.75** correct per min (4 h); Stanford Sleepiness Scale **+0.77** points
(4 h). Standardised: PVT lapses g = **+1.44** (SE 0.49) at 4 h and **+0.86** (SE 0.45) at 6 h; DSST
g = **−1.16** (SE 0.47). Critical daily sleep duration **8.16 h** (SE 0.73, between-subject SD 3.58 h).

**2. Belenky 2003 — done, full text, 11 effects.** Four doses (3/5/7/9 h × 7 nights) is the widest
restriction ladder in the literature. Night-7 lapse increases over baseline: **+15.47** (3 h), **+4.68**
(5 h), **+2.02** (7 h). PVT mean speed vs the 9 h arm: g = **−2.00** (SE 0.46) at 3 h, **−0.95** (SE 0.40)
at 5 h, **−0.56** (SE 0.37) at 7 h. Recovery is the important part: after **three** nights at 8 h TIB the
3 h arm was still at g = **−1.05** (SE 0.40) and retained **93%** of its night-7 lapse deficit.

**3. Banks & Dinges 2007 — done, full text.** Used as intended: for pooled statements and as a route to
primaries. It is not load-bearing for any quantity.

**4. Lo / Chee "Need for Sleep" series — 5 records, 24 effects, `cohort_family: NFS_Singapore`.**
`lo2016` (n=56), `lo2017` (n=83), `lo2019` (n=58), `lo2022` (n=194, pooled), `koa2024` (n=52). The task
described this as 5 h vs 9 h; **`lo2022` is better than that** — it is a four-dose ladder (5 / 6.5 / 8 / 9 h
nocturnal TIB) across two simulated school weeks in 15–19 year-olds, and it is the best age-matched
dose-response design that exists. `lo2016` gives PVT lapses g = **+2.40** (SE 0.35) at 5 h vs 9 h on
night 7, with lapses accumulating at **2.41 per session per night**.

**5. Other ≥3-dose experiments — 7 found.** Belenky 2003 (4 doses), Van Dongen 2003 (3 + TSD), `lo2022`
(4 doses, adolescent), `short2018` (5/7.5/10 h, ages 15–17), the Campbell series `campbell2017` /
`campbell2019` / `campbell2024` (7 / 8.5 / 10 h, adolescent), `rupp2009` (3 doses incl. extension), and
`banks2010` (a six-level *recovery* ladder, 0–10 h).

**6. Cumulative vs plateau — resolved as far as the evidence allows, and the answer is "neither, and it
matters which".** See §3.

---

## 3. What the downstream model asked for

**Per-hour effect below 8 h.** Derivable, but the dose-response is **convex** over 4–8 h, so a single slope
loses real structure. Reported anyway, with raw per-arm data in the records so a spline can be fitted:

| Source | Slope | Age match |
|---|---|---|
| Van Dongen 2003, day 14 | **3.08** extra PVT lapses per 10-min bout per hour less TIB below 8 h | adult |
| Belenky 2003, night 7 | **2.46** extra lapses per session per hour less TIB | adult (to 62 y) |
| Campbell 2019 | **0.243 ± 0.051** dB PVT log-SNR per hour of TIB | **exact_16_19** |
| Campbell 2017 | **0.56 ± 0.07** KSS points per hour of TIB | adolescent |
| Campbell 2019 | **41.5 ± 0.8** min PSG sleep per hour of TIB (69% efficiency) | **exact_16_19** |

That last row is a unit-conversion trap worth stating plainly: nearly every study doses in *time in bed*,
while Short's 9.35 h requirement and the UMP's debt scale are in *sleep*. Mixing the axes is a silent
~45% error.

**Accumulate or saturate across 14 days?** Van Dongen's own fitted exponent settles the 14-day question:
θ = **0.78 ± 0.04** for PVT lapses in `y_t = β·t^θ`. Below 1, so the build-up **decelerates but does not
asymptote** — still climbing at day 14, no plateau reached. Beyond 14 days there is one properly validated
estimate of the accumulation rate: the UMP's **τ_LA = 7.00 ± 1.67 days** (`ramakrishnan2016`), implying
~63% saturation by day 7, ~86% by day 14, ~95% by day 21. McCauley 2009 supplies the competing structure —
a **bifurcation at 3.8 h daily sleep** (W_c = 20.2 h), above which trajectories converge to a
dose-dependent impaired plateau and below which they diverge. Our subject's weekday 5–6 h sits *above* the
threshold; his pre-exam 3–4 h nights sit *at or below* it.

**Subjective/objective dissociation — quantified twice, independently.** Van Dongen 2003 fits the same
power law to both channels in the same subjects: θ_PVT = **0.78 ± 0.04** but θ_SSS = **0.24 ± 0.04**.
Subjective sleepiness flattens almost immediately while objective vigilance keeps climbing — a
three-fold difference in curvature exponent. `rabat2016` shows the same thing as a clean within-study
time contrast at 4 h TIB × 7 nights: KSS ends at g = **+1.12** after 7 nights but had already **arrived by
day 4** — the day-4→day-7 increment was just **+0.07** KSS points, ~5% of the size of the baseline→day-4
increment, and the evening rating actually moved *backwards*. Over the same three days the Maintenance of
Wakefulness Test kept falling, ending at g = **−1.14**, having lost a further **−5.5 min** of sleep
latency after day 4 — **122% more** than its own baseline→day-4 decrement. So in the second half of the
week the subjective channel contributed ~5% of its earlier change while the objective channel more than
doubled its earlier change. Two more supports:
`rupp2009` found zero subjective group difference where PVT and MWT both found significant ones, and
`vandongen2004` found subjective and objective vulnerability load on **separate** trait dimensions.
The practical conclusion is unambiguous: this subject's self-report cannot be used as a proxy for his
performance, in either direction.

**Practice / test-retest effects — and they run in opposite directions by task.** Van Dongen's own 8 h
control arm gained **+9.61** DSST correct responses per 1.5 min over 14 days with 9 bouts/day, i.e. the
rested-control practice gain is **65% of the size of the 4 h arm's deficit** (−14.75). Any DSST or
serial-addition trajectory is uninterpretable without practice correction. PVT is the opposite and, in
adolescents, worse than neutral: `campbell2019` found PVT performance **declined** across repeated
laboratory visits, with the decline largest after the most restricted prior visit — carryover, not
learning. `campbell2017` found MSLT sleep-onset likelihood *increased* with repeated visits (adaptation to
the laboratory). So the confound is task-specific and signed, and pooling across tasks would cancel out
real effects.

---

## 4. Confidence, by claim

**High.** That chronic restriction at 4–6 h TIB produces large, dose-ordered, cumulative deficits in
sustained attention. At least six independent laboratories across six countries, consistent direction,
effect sizes g ≈ 0.9–2.4, the
largest in age-matched adolescents. That subjective sleepiness understates objective impairment: two
independent quantifications plus two supporting studies.

**Moderate.** The per-hour slopes above. They rest on figure digitisation in the two anchor papers
(Van Dongen and Belenky both publish trajectories graphically), which I have flagged per effect rather
than hidden. The adolescent inflation factor — direction is solid (g = +2.40 at 5 h/7 nights in
adolescents vs +1.44 at a *harsher* 4 h dose over *twice* as many nights in adults), the multiplier is
soft, because the two comparisons differ in dose, duration, task version and laboratory simultaneously.

**Low.** Anything about three years. See §5.

**Explicitly discordant, and I have not averaged it away.** `debruin2017`, a systematic review of sleep
manipulation in adolescents, concludes partial restriction had "small or no effects" on adolescent
cognition outside vigilance. `smith2021` ran six weeks at 5 h weekdays / 8 h weekends and found 8 of 10
cognitive domains unaffected, with the pooled cross-domain slope only **18%** of the vigilant-attention
slope. Both are in the shard as disconfirming evidence. The honest reading is that the large effects are
real but **narrow**: vigilance and wake maintenance degrade steeply, most other domains do not, and a
single "global cognition" decrement would be simultaneously too broad and, for vigilance, far too small.

---

## 5. The single biggest gap: the duration gap

**Our subject has ~1,100 nights of exposure. The longest chronic-restriction experiment ever run is 42
days (`smith2021`, n = 15, ages 30–47). The longest with a ≥3-dose ladder is 14 days (Van Dongen 2003).**
The model must therefore extrapolate **26×** beyond the longest experiment of any design and **78×**
beyond the longest dose-ladder experiment — and the literature offers three mutually incompatible
functional forms for doing exactly that:

- **Unweighted accumulation** (Van Dongen's excess-wakefulness Σ): all 1,100 nights count equally, no
  recovery term at all. Predicts a very large three-year deficit.
- **Pure state-dependence** (McCauley 2009): "past amounts of sleep and wake have no further impact
  beyond the present." Predicts his deficit looks like any short sleeper's, regardless of duration.
- **Recency weighting** (Rajdev 2013 / UMP, τ_LA = 7.00 ± 1.67 d): roughly the last few weeks dominate.
  Predicts ~95% saturation within three weeks and no further growth.

These give materially different three-year answers, and **no experiment is long enough to discriminate
between them.** This is irreducible with the current literature and is the dominant term in the
uncertainty of any three-year extrapolation. My recommendation (`notes_for_modeller.md` §9, items 13–14)
is to adopt the UMP's saturation as the central case — it is the only form fitted to one study and then
validated on 14 conditions across five studies in four other laboratories without refitting — and carry
McCauley's bifurcation as the pessimistic alternative, rather than averaging the forms.

**The compounding problem: not one of the six functional forms has ever been fitted to adolescent data.**
Every dynamic parameter in this shard — θ, W_c, τ_LA, every recovery constant — comes from adult samples.
The age-matched evidence (9 records) supplies *levels and per-hour slopes* but no *time course*; the adult
evidence supplies time course but at the wrong age. Combining an adolescent level with an adult time
course is the least-bad option available and should be stated as a limitation, not buried in a pooled
estimate. This matters mechanistically, not just statistically: McCauley ties W_c to slow-wave activity,
and adolescents have substantially higher SWA, so there is a specific reason to expect the threshold to
sit elsewhere in this age group. No paper calibrates it.

**Second gap, narrower but closable.** No experiment combines ≥3 doses **and** ≥7 nights **and**
adolescents. `lo2022` gets closest (4 doses, 15–19 y, 8 restriction nights across two simulated school
weeks) and is the most valuable single design in the shard for that reason. The Campbell series has 3
doses but only 4 nights; `short2018` has 3 doses and 5 nights but is paywalled.

---

## 6. What I could not obtain

- **`short2018` full text** (*Sleep* 41(4), zsy011) — the most directly age-matched dose-response study
  (ages 15–17, 5/7.5/10 h × 5 nights, modelled requirement **9.35 h** of sleep). Cloudflare 403 at OUP;
  Unpaywall, Semantic Scholar, OpenAlex and Europe PMC all report no OA copy. The headline numbers were
  recovered from the abstract and corroborated secondhand via `campbell2019`, but per-arm PVT values and
  dispersions are missing. **This is the single highest-value target if the orchestrator has journal
  access.**
- **`rajdev2013` equations** (Elsevier paywall). Materially mitigated: the same group's successor
  (`ramakrishnan2016`) was retrieved in full and carries the complete equation set with all eight fitted
  parameters and standard errors.
- **McCauley 2013** (the circadian-timing successor to the bifurcation model) — abstract only in PMC. No
  parameters extracted and none attributed to it.
- **Carskadon & Dement 1981**, the original cumulative-restriction paper — predates electronic full text,
  PubMed carries no abstract, no OA copy exists. Its finding survives secondhand via `banks2007`.
- **10 further on-topic records** were excluded as `E-NOEXTRACT` *only* because full text was unobtainable
  and the abstract carried no per-arm numbers. They are individually listed and justified in the
  "Near-miss exclusions" section of `screening_log.md` and are the records worth revisiting with better
  access.

## 7. Cautions for the pooler

1. **De-duplicate on `cohort_family`.** 78 of 142 effects come from six overlapping sample families.
   `UPenn_GCRC_2003` (18) and `WRAIR_2003` (14) each include modelling records that **refit data already
   present** — `mccauley2009` and `ramakrishnan2016` carry the cohort label of their *fitting* data
   deliberately, so a pooler matching on that string will collapse them instead of counting a refit as new
   evidence. `NFS_Singapore` (24) and `Campbell_Feinberg_Davis` (13) contain records with genuinely
   overlapping participants, noted in each.
2. **The 4 `TX` records contribute no independent observations.** Three (`mccauley2009`, `rajdev2013`,
   `ramakrishnan2016`) are functional forms fitted to data already in the shard; the fourth (`banks2007`)
   is a review. Counting any of them as a study would double-count Van Dongen and Belenky.
3. **25 effects are figure-digitised** and flagged. Treat their dispersion as wider than stated.
4. **`n` in `ramakrishnan2016` (57) is training-data size**, not an independent sample.
5. `belenky2003` is `poor_midlife` (ages 24–62) despite being a core anchor — its ladder is the widest
   available, but the age transport is the weakest of the anchor studies.

---

## 8. Terse numeric summary

```
shard              s01_cognition_dose_response
screened           185     (brief required ≥30; instructions ≥25)
included            30
effects            142     (42 with SE+CI, 25 figure-digitised)
verified            30/30  Crossref + PubMed, title similarity 1.000
schema errors        0
tiers              T1=26  TX=4
access             full_text=14  abstract_only=16
age match          exact_16_19=9  good_young_adult=5  mixed=4  fair_adult=10  poor_midlife=2
functional forms     6     verbatim with parameters in notes_for_modeller.md
cohort families      6     covering 78 of 142 effects
failed identifiers   0
```

**Six most decision-relevant estimates**

| # | Estimate | Value | Source | Tier | Age |
|---|---|---|---|---|---|
| 1 | PVT lapses, 5 h vs 9 h TIB, night 7 | g = **+2.40** (SE 0.35) | `lo2016` | T1 | **15–19** |
| 2 | PVT lapses, 4 h vs 8 h TIB, day 14 | g = **+1.44** (SE 0.49) | `vandongen2003` | T1 | 21–38 |
| 3 | Accumulation curvature, PVT vs subjective | θ = **0.78 ± 0.04** vs **0.24 ± 0.04** | `vandongen2003` | T1 | 21–38 |
| 4 | Sleep-debt saturation time constant | τ_LA = **7.00 ± 1.67 d** | `ramakrishnan2016` | TX | adult |
| 5 | Divergence threshold (daily sleep) | **3.8 h** (W_c = 20.2 h) | `mccauley2009` | TX | adult |
| 6 | Adolescent requirement for optimal PVT | **9.35 h** sleep | `short2018` | T1 | **15–17** |

**Biggest gap.** The duration gap. 42 days is the longest experiment in existence; the subject's exposure
is ~1,100 nights; the three published extrapolation forms disagree by large factors and no data can
choose between them. Compounding it, none of the six functional forms has ever been fitted to adolescent
data.
