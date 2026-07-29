# Station report — s10_immune

**Domain:** immune competence, infection susceptibility, vaccine response, systemic inflammation
under short sleep.
**Target case:** 18-year-old male, weekday sleep ~5-6 h since age 16, weekends 7-8 h, occasional
3-4 h pre-exam nights, occasional 10-11 h weekend nights.

| | |
|---|---|
| Candidate records screened | 44 |
| Included with a YAML record | 25 |
| Excluded (logged with reasons) | 19 |
| Effect estimates extracted | 110 |
| Identifiers failing verification | **0** |
| Schema validation | 25/25 pass `spec/effect.schema.json` + internal consistency checks |

---

## 1. What I did

**Search.** PubMed E-utilities across nine query families (viral-challenge studies; vaccination and
antibody response; CRP/IL-6/TNF meta-analyses; restriction-plus-recovery protocols; pneumonia and
respiratory-infection cohorts; adolescents and college students; NK/T-cell function; Mendelian
randomization; COVID vaccine breakthrough). Full text via Europe PMC `fullTextXML` with a PMC HTML
fallback when the XML route returned a browser challenge.

**Verification.** Every DOI checked against Crossref and every PMID against PubMed `esummary`, with
the two titles compared by sequence similarity and the PubMed-recorded DOI cross-matched against the
asserted one (`_tools/verify.py` → `_tools/verification.json`). All 25 passed on all four checks.

**Arithmetic.** All effect-size conversion is in `_tools/convert.py`; absolute-rate back-calculation
is in `_tools/backcalc.py`. Every derived number is labelled `derived` in its record and never
presented as quoted. `_tools/validate.py` enforces the schema plus four checks the schema cannot
express: every effect carries a non-empty verbatim `quote`, CI bounds bracket the point estimate, `se`
agrees with CI width to within 12%, and the `verification:` block matches `verification.json`.

**Every one of the 7 required extractions was located and extracted.** Nothing on the required list
turned out not to exist, and no seed name was wrong — though two seed *descriptions* were (see §3).

---

## 2. The 6 most decision-relevant estimates

| # | Effect | Estimate | Tier | Record |
|---|---|---|---|---|
| 1 | Objectively measured short sleep (<6 h) around vaccination → lower antibody, **men** | **ES 0.93 (0.54–1.33)**; all-sex 0.79 (0.40–1.18), n=304, 7 studies | T1 | `spiegel2023_vaccine_meta` |
| 2 | Actigraphic <5 h vs >7 h → clinical cold after rhinovirus challenge | **OR 4.50 (1.08–18.69)**; absolute **39.7% vs 12.8%** (derived); n=164 | T2 | `prather2015_rhinovirus` |
| 3 | Categorical short sleep duration → CRP and IL-6 | **CRP 0.08 (−0.01–0.16) NULL** (11 samples, N=19,573); **IL-6 0.08 (−0.02–0.18) NULL** (8 samples, N=12,925) | TX | `irwin2016_inflammation_meta` |
| 4 | Multi-night partial restriction → IL-6 / CRP, experimental | IL-6 d=0.42 (0.11–0.73), CRP d=0.76 (0.09–1.43) **only with outliers excluded**; **both null with all studies in** (0.10 and 0.50) | T1 | `ballesio2026_experimental_meta` |
| 5 | 24-h plasma IL-6 after 6 h × 6 nights, then 2 nights of 10 h | Rose +0.90±0.41, fell −0.93±0.45, **residual 0.02±0.34, P=0.94 — fully normalised** | T1 | `pejovic2013_recovery` |
| 6 | Shortest adolescent sleep trajectory (grades 7-12) → adult CRP ~14 y later | **3.21 vs 3.35 mg/L; derived −0.14 (−0.84 to +0.56) — NULL** | T5 | `stager2023_adolescent_crp` |

Two more that constrain interpretation: objectively measured sleep did **not** predict real-world
COVID breakthrough infection in 5,265 + 2,583 people (`jaiswal2024_breakthrough`), and Mendelian
randomization puts the causal arrow the other way — genetically predicted CRP → *longer* sleep
(`zhang2023_mr_inflammation`).

---

## 3. Where reality differed from the task description

Reported per hard rule #4. Both corrections matter for the pooler.

1. **The rhinovirus study's exposure→outcome path is not the one implied.** The task called it a study
   where sleep duration "predicted susceptibility to experimental rhinovirus challenge." Sleep duration
   predicted developing a *clinical cold*, but was **unrelated to becoming infected**: *"actigraphy
   assessed sleep duration was unrelated to rates of infection (b = -0.11, SE = 0.17, P = 0.543)."*
   75.6% of the sample got infected; only 29.3% got a cold. The effect is on **symptom expression among
   the already-infected**, not on host resistance to viral entry. This single distinction changes what
   the whole shard licenses.

2. **Irwin 2016's short-sleep result is null, and the paper says so.** Confirmed exactly as the task
   suspected. Categorical short sleep duration was not significantly associated with CRP or IL-6; what
   *was* significant is insomnia/sleep disturbance and **long** sleep duration (CRP 0.17, roughly twice
   the short-sleep point estimate). The commonly cited claim is not in the paper.

3. **A third correction the task did not anticipate.** `stager2023_adolescent_crp`'s abstract says poor
   longitudinal sleep predicted elevated CRP, but its own numbers put the elevation in the group whose
   sleep *increased above* recommended (5.23 mg/L), not the shortest-sleeping group (3.21 vs 3.35 for
   stable-recommended). I extracted the numbers, not the abstract's gloss.

---

## 4. Transient vs. durable — my central finding

The task asked me to keep these apart, and the split is cleaner than I expected.

**(a) Transient.** Every inflammatory and cell-count change measured during restriction reversed, given
enough recovery sleep: IL-6 fully normalised after 2 nights of 10 h (`pejovic2013_recovery`); NK and B
cell counts "recovered almost completely" (`vanleeuwen2009_recovery`); the influenza and H1N1 antibody
gaps closed by 3-4 weeks and by day 10 respectively (`spiegel2002`, `benedict2012_h1n1`).

**(b) Incompletely reversible after an *ordinary* weekend.** Monocyte IL-6 remained elevated *after*
recovery sleep across 3 weeks of 5×4 h + 2×8 h — the closest experimental analogue of the subject's
actual weekly pattern (`simpson2016_repeated_recovery`). Serum CRP was *higher* after the recovery
weekend than after the restriction itself, 231% vs 145% of baseline (`vanleeuwen2009_recovery`).

**The reconciling result, which I consider the most useful single finding in the shard:**
`faraut2011_nap_recovery` is the only study that varied the **recovery dose** while holding restriction
constant, and the same abnormality that **persisted after 8 h** of recovery **resolved after 10 h, or
after a nap + 8 h**. That explains the apparent contradiction between Pejovic (10 h → full
normalisation) and Simpson/van Leeuwen/Faraut (8 h → incomplete) without discarding either. For this
subject it predicts incomplete normalisation on ordinary 7-8 h weekends and fuller normalisation on the
occasional 10-11 h ones — which reframes his long weekend sleeps as partially protective rather than as
the "irregularity" a naive reading would penalise.

**(c) One genuinely durable signal.** In `lange2011_memory` the antigen-specific Th-cell and IgG1
advantage of sleeping after vaccination was still present **one year later**, and three
sleep-deprived participants never reached seroprotection and required re-vaccination (zero in the sleep
condition). Immunological memory laid down badly is not remade by catching up. Scope limit: it required
deprivation timed to three separate immunisations and concerns T-cell memory, not circulating cytokines.

---

## 5. My confidence, by claim

| Claim | Confidence | Basis |
|---|---|---|
| Sleep around vaccination measurably lowers antibody response in young men | **High** | Meta-analysis with participant-level reanalysis + 4 concordant experimental primaries + dose-response in actigraphy cohort |
| That antibody shift translates into more real-world infection | **Low** | The one large objective test of the clinical endpoint is null (`jaiswal2024_breakthrough`) |
| Chronic short sleep at 5-6 h raises systemic CRP/IL-6 durably | **Low** | Largest observational meta-analysis null for categorical short sleep; experimental positives outlier-dependent; adolescent longitudinal CRP null |
| Short sleep increases clinical cold/URTI frequency | **Moderate** | Two challenge experiments agree, but the effect is on illness expression and the 6 h null recurs in 3 large datasets |
| Occasional 3-4 h pre-exam nights cause measurable immune harm | **Low that they do** | Single-night deprivation is null for IL-6, CRP and TNF-α in the experimental meta-analysis |
| Marker changes during restriction reverse with adequate recovery | **Moderate-high** | Direct recovery data in 4 protocols, with a dose-dependence that explains the discordance |
| Years of adolescent short sleep produce durable immune impairment | **Very low confidence either way** | See §6 — this is not a demonstrated null, it is an untested question |

**Calibration notes against myself.** Three places where I distrust my own extraction:
`spiegel2002_influenza_vaccine` is `access_tier: secondhand` (paywalled JAMA letter, no abstract, no
PMC deposit, WebFetch timed out), so its numbers come from three verified secondary sources and I set
`se: null` rather than reconstruct one. My back-calculated absolute rates are *marginal* whereas the
published ORs are *covariate-adjusted*, so they are approximations — though for `prather2015` my
back-calculated ~27-point gap independently reproduces the paper's own Figure 1 (~45% vs ~17%), which
is reassuring. And `stager2023`'s CRP model had df of (2,127), i.e. ~130 people: my null CI excludes a
large durable elevation but not a small one.

---

## 6. The single biggest gap in the evidence for this domain

**No study has ever measured immune outcomes in people with a multi-year history of adolescent sleep
restriction using an adequate design.** The literature has exactly two shapes, and the subject's
exposure falls between them:

- **Short and sharp** — lab protocols of 1-14 nights, which is where all the causal identification and
  all the mechanistic detail lives (T1, good young-adult samples), but which cannot speak to 3 years.
- **Long and confounded** — observational cohorts with self-reported sleep, cross-sectional or with
  midlife exposure, where the recurring symmetric U-shape (long sleep as harmful as short) and the
  Mendelian randomization result both indicate that reverse causation and shared confounding dominate.

The bridge is missing entirely. `stager2023_adolescent_crp` is the only record with adolescent-exact
exposure and an objectively measured later outcome; it is null and underpowered at ~130 people. The
consequence for the downstream model: **the absence of demonstrated durable immune harm here is mostly
an absence of evidence, not evidence of absence**, and uncertainty should be inflated rather than the
gap being read as a null. The one exception is adult CRP, where a real if underpowered null exists.

A second, narrower gap: the highest-value actionable finding — that the sensitive window for vaccine
response is the **two nights before** inoculation (`prather2021_influenza`) — rests on one study, and
nobody has run the obvious trial of extending sleep before immunisation.

**A known limit in my own reading, flagged rather than buried:** a published Comment on the Zhang
Mendelian randomization paper (doi 10.1093/sleep/zsad223) may qualify its conclusions. I did not
retrieve it, so the MR record's weight should be treated as provisional.

---

## 7. Cross-shard notes

- **Double-counting.** `cohort_family` is set on every observational record (`NHANES`, `NHS`,
  `Add_Health`, `ALSPAC`, `Nurses_Health_Study_II`, etc.). `prather2015_rhinovirus` and
  `cohen2009_cold` are separate Pittsburgh challenge cohorts, not overlapping samples. I deliberately
  did **not** extract Vgontzas 2004 or Meier-Ewert 2004 separately because both are pooled inside my
  two included inflammation meta-analyses.
- **Overlap with other shards.** `pejovic2013_recovery` reports a PVT result (performance did not
  recover while IL-6 did) and `moralesmunoz2024_alspac` reports a psychosis outcome; both belong to
  cognition/psychiatric shards and I extracted them only as immune records, flagging the other
  outcomes in `notes`.
- **A measurement warning that generalises beyond this shard.** In `prather2015_rhinovirus`,
  actigraphic mean sleep was 5.8 h while *diary* mean in the same people was 7.5 h. A subject who
  *reports* 5-6 h likely sits in that study's *<5 h actigraphic* band. Self-reported and objective
  hours are not interchangeable, and in `prather2012_hepb` the actigraphy effect was significant while
  diary sleep was null **in the same participants**.
- **Duration is the weaker axis.** In every dataset that measured both, continuity/quality beat
  duration: efficiency OR 5.50 vs duration 2.94 (`cohen2009_cold`); perceived inadequacy RR 1.50 vs
  ≤5 h 1.39 (`patel2012_pneumonia`); disturbance OR 1.27 vs ≤5 h 1.17 (`pratherleung2016_nhanes`);
  insomnia SMD 0.12/0.20 vs short-duration null (`irwin2016_inflammation_meta`). Social jet lag
  predicted colds independently of duration, OR 4.28 (`martinezalbert2025_infection`) — plausibly the
  more relevant exposure axis for a student with a split weekday/weekend schedule.

## 8. Files

25 YAML records; `immune_summary.md` (absolute infection numbers, vaccine effect, inflammation
meta-analytics including nulls, reversibility); `screening_log.md` (44 screened, all exclusions
reasoned, tier/access/population distributions read from the YAML). Tooling in `_tools/`:
`verify.py` + `verification.json`, `convert.py`, `backcalc.py`, `validate.py`, `pmquery.sh`,
`pmabs.sh`, `getft.sh`, `html2txt.py`. Retrieved full texts in `_raw/`.
