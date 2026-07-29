# Station report — shard `s03_memory_consolidation`

**Mandate:** supply channel (c) — knowledge and skill never encoded because sleep-dependent
consolidation/encoding was impaired across three years of schooling — kept separate from
(a) reversible state deficits and (b) permanent change in ability.

**Output:** 58 records screened, 24 included, 86 effect estimates, 0 identifier verification failures.
All 24 records validate against `effect.schema.json`. Plus `architecture_under_restriction.md`
(the flagged deliverable) and `screening_log.md`.

---

## 1. The headline finding, which is not the one the task anticipated

The task framed requirement 4 as a choice: at 5–6 h, do we lose "the consolidation-relevant sleep or
preferentially lose REM?" The evidence dissolves the dichotomy, and the answer reframes the whole
channel.

**Slow-wave sleep is not lost at all.** Across five independent laboratories, five doses (4, 5, 7, 7.5,
8.5 h TIB) and both adolescents and adults, SWS/N3 minutes are actively defended. Campbell 2021's
adolescent PSG table is the cleanest: cutting TIB from 10 h to 7 h costs 124 min of total sleep, of
which N2 absorbs −88 min and REM −39 min, while **N3 *gains* 3 min**. At 4 h TIB, Kopasz 2010 measures
NREM −50%, REM −70%, and **SWS −5%**. At the subject's own 5 h dose in his own age band, Lo 2016 cut
TST, N1, N2 and REM at P < 0.001 while N3 was statistically indistinguishable on all three PSG nights
(P = 0.23, 0.36, 0.10).

**REM is preferentially lost — but REM duration does not predict memory.** Berres & Erdfelder find REM
duration does not moderate the sleep benefit across 427 effect sizes (β = −0.016, 95% CI [−0.28, 0.25]),
with the sign negative. Within Lo 2016's restricted arm, *more* REM predicted *worse* 6-week recall
(r > −0.50, P < 0.013) — the opposite of what a REM-mediated model requires, and the authors flag it as
unexpected. So the stage that is preferentially lost is not the consolidation-relevant one, and the
stage that is consolidation-relevant is not preferentially lost.

**The one architecture variable that does move is spindle activity — and its slope is small.** Sigma
(11–15 Hz) energy falls 28–40% from 10 h to 7 h TIB even though N3 minutes do not (Campbell 2021;
foreshadowed in Brunner 1990, where slow-wave *energy* fell while SWS minutes did not). But the only
meta-analysis of the spindle→memory slope puts it at r = 0.21 for declarative memory (k = 812), falling
to r = 0.13 in the subset of effect sizes least exposed to selective reporting, with a significant Egger
test and a reported PET-PEESE reanalysis that nulls it entirely (Kumral 2023). Multiplied through, a
28–40% spindle loss buys roughly **0.07–0.21 SD** of declarative memory.

**Consequence for the modeller: the entire sleep-architecture route predicts only a small consolidation
loss at 5–6 h.** A naive "hours below 8" ledger is not merely imprecise, it is mis-specified — it keys
the harm to a quantity (total sleep, or SWS) that is either preserved or non-predictive.

## 2. The reconciliation that matters most: it is encoding, not consolidation

The matched-dose behavioural literature looks contradictory until it is sorted by *when* the restriction
fell relative to learning. Sorted that way it is almost perfectly consistent, and the pattern is the
single most useful structural result this shard produces.

**Restriction BEFORE encoding → large, persistent deficit:**

- `cousins2018` — 5 h TIB × 5 nights, *then* encode. Recognition tested after 3 recovery nights of 9 h
  in **both** arms, so test-time fatigue is excluded by design. g = −0.89 (95% CI −1.43 to −0.36), and
  the authors report the impairment "was not correlated with decline in vigilance."
- `yoo2007` — 35 h total deprivation, then encode. 19% lower d′ (2.58 → 2.17, P < 0.031), reduced
  hippocampal encoding activation, **and the behavioural deficit was measured after two recovery
  nights.**

**Encoding BEFORE restriction (i.e. testing consolidation of already-learned material) → null:**

- `lo2016` — prose encoded first, then 5 h TIB × 7 nights. No group difference in recall at any time
  point (F(1,43) = 1.13, P = 0.29). Only the *growth* of the advantage for prioritised material was
  attenuated, and even that difference was not supported by the formal three-way interaction (P = 0.41).
- `voderholzer2011` — 88 adolescents randomised across 9/8/7/6/5 h TIB for 4 nights after learning.
  No effect on declarative or procedural memory at 2 recovery nights or 4 weeks.
- `kopasz2010` — 4 h TIB, no persisting effect on declarative recall after a recovery night.

`cousins2018` and `lo2016` come from the **same research programme, the same boarding school, the same
5 h dose and the same age band.** The discrepancy therefore cannot be population or dose. It is the
design: one impaired encoding, the other did not impair consolidation.

**So channel (c) most plausibly operates through degraded encoding capacity during the waking day, not
through failed overnight consolidation of material that was successfully learned.** This has a concrete
implication the downstream model should not miss: the harm accrues to material *studied while
sleep-deprived*, and it is not repaired by later sleep. It is also why the architecture route (§1) and
the behavioural route disagree by an order of magnitude — they are measuring different mechanisms, and
the architecture route is measuring the one that turns out to matter less.

## 3. Recoverability (requirement 5): the encoding window does not reopen

Four independent designs agree that sleeping well *afterwards* does not restore what was not encoded:

- `yoo2007` — the 19% d′ deficit was measured **after two recovery nights**.
- `cousins2018` — the g = −0.89 deficit was measured **after three 9 h recovery nights in both arms**.
- `stickgold2000nn` — 30 h deprivation after training abolished overnight improvement, and **two full
  recovery nights did not restore it** (g = −1.14, 95% CI −2.07 to −0.21 between groups).
- `brunner1990` — sigma-band power was still *reduced during the recovery nights themselves*, after
  total sleep time had been restored.

One important dissent, and it is meta-analytic. Berres & Erdfelder's deprivation subgroup finds the
sleep benefit falls to a non-significant g = 0.14 when a recovery night intervenes, versus g = 0.30
without recovery — i.e. in aggregate, recovery sleep *does* substantially attenuate the measured
impairment. I report both faithfully. The tension may be a difference between total deprivation
protocols (where much of the measured deficit is state-dependent and does recover) and encoding-capacity
protocols (where it does not), but I cannot resolve it from the retrieved evidence.

Architecture recovery is also incomplete on the timescale of a weekend: `ong2016` reports REM, N2 and
TST still above baseline by the third recovery night, i.e. a debt still being repaid.

## 4. Requirement-by-requirement status

| # | Requirement | Status | Notes |
| --- | --- | --- | --- |
| 1 | Declarative + procedural meta-analyses with pooled effects, CIs, heterogeneity | **Complete** | The named study exists but is about ***episodic*** memory, not declarative: Berres & Erdfelder 2021, *Psychol Bull*, "The sleep benefit in episodic memory." g = 0.44 uncorrected, **0.28 after Egger correction**; 823 effect sizes, 271 samples. Procedural covered three ways with a genuine literature conflict: `panrickard2015` (no sleep enhancement after moderators), `schmid2020` (g = 0.43, but **no positive effect in deprivation designs**), `rickard2022` (bias-corrected post-sleep gain negative). Plus `schimke2021` (novel word learning, g = 0.50) and `kumral2023` (spindle slope). |
| 2 | Yoo 2007 behavioural + hippocampal | **Complete, with a data defect** | 19% d′ decrement (2.58 → 2.17); reduced hippocampal encoding activation. **Table 1's dispersion values are internally inconsistent with the reported P = 0.031** — read as SDs they imply t ≈ 5.9 (P < 0.0001), read as SEMs they imply t ≈ 1.56 (P ≈ 0.13). I back-computed g = −0.84 (95% CI −1.61 to −0.06) from the P value per the instructions and documented the inconsistency rather than picking a reading. |
| 3 | Multi-night partial restriction with next-day learning/retention | **Complete, and genuinely contested** | Five records at 4–5 h in adolescents: `cousins2018`, `huang2016`, `lo2016`, `voderholzer2011`, `kopasz2010`. Split resolved by encoding timing — see §2. `huang2016` adds a moderator worth carrying: impairment for **massed** learning (g ≤ −0.93) but **none for spaced** learning (P = 0.80), i.e. cramming under restriction is where the loss concentrates. |
| 4 | SWS/REM minutes at 4/6/8 h TIB — flagged deliverable | **Complete** | `architecture_under_restriction.md`, 5 doses, 5 laboratories, adolescents + adults, with a consolidated dose–response table. Headline: SWS incompressible, REM/N2 absorb the loss, spindles −28–40%, spindle slope small. |
| 5 | Is consolidation loss recoverable? | **Complete** | See §3. Four designs say no; one meta-analytic subgroup says partly yes. |
| 6 | Longitudinal adolescent sleep → knowledge accumulation over a school year | **Adequate, weakest area** | `james2023` (n = 2153, difference-in-differences, GPA +0.08 to +0.17 in **year 2 only**), `widome2020` (+43 min/night objectively measured, same cohort), `dunster2018` (independent cohort, +34 min → +4.5 percentage points), `okano2019` (semester actigraphy, r = 0.38 for duration; **sleep the night before a test predicted nothing**), `dewald2010` (self-report meta-analysis, r = 0.069 — a deliberate downward anchor). |

Two results in requirement 6 are unusually diagnostic for channel (c) specifically, because they
dissociate accumulation from state:

- `james2023`: sleep rose by 41 min at year 1 and GPA did not move (+0.01, 95% CI −0.03 to 0.06); by
  year 2 GPA had risen (+0.17, 95% CI 0.11–0.23). A reversible state deficit would have improved
  immediately. A cumulative knowledge effect produces exactly this year-1-null/year-2-effect shape.
- `okano2019`: sleep duration and quality across the *month and week* before an exam predicted scores,
  but sleep on the *night before* did not. Again: accumulation, not test-day state.

## 5. A pattern the orchestrator should propagate: this literature is systematically bias-inflated

Four of the six meta-analyses I extracted tested formally for publication bias, and **all four found it
materially inflates the sleep–memory effect**:

| Meta-analysis | Uncorrected | After bias correction |
| --- | --- | --- |
| `berres2021` (episodic memory) | g = 0.44 | **g = 0.28** (Egger-corrected; 64% of original) |
| `panrickard2015` (motor sequence) | relative sleep gain d = 0.44 (0.09–0.79) | **d = 0.29**, and the authors conclude there is no evidence sleep enhances motor learning once moderators are modelled |
| `rickard2022` (same 88 effect sizes, PET/PEESE) | — | **bias-corrected post-sleep gain negative** |
| `kumral2023` (spindle→memory) | r = 0.236 | r = 0.131 in the least-selected subset; a reported PET-PEESE reanalysis nulls it |

`kumral2023` also shows why: mean constituent sample size is 35.7, falling to 18.6 (range 6–44) once one
large study is removed, with a sample-size/effect-size correlation of −0.175 (P < 0.001). **Recommendation:
apply a substantial discount to any pooled sleep–memory effect in this domain that has not been
bias-corrected, and prefer the corrected estimate wherever both exist.**

## 6. Most decision-relevant estimates

| Estimate | Value | Tier | Why it matters |
| --- | --- | --- | --- |
| `cousins2018` encoding capacity, 5 h × 5 nights, tested after 3 recovery nights | g = **−0.89** (95% CI −1.43 to −0.36) | T1 | Exact dose, exact age, and the only design that isolates channel (c) from channel (a) by construction |
| `berres2021` sleep benefit for episodic memory, bias-corrected | g = **0.28** (uncorrected 0.44) | T1 | Ceiling on what *all* of a night's sleep contributes; our subject lost a fraction of a night, not a night |
| `james2023` GPA, year 2 vs year 1 | **+0.17** (0.11–0.23) at year 2 vs **+0.01** (−0.03–0.06) at year 1 | T2 | The only direct evidence that the learning channel is cumulative rather than state-like |
| Architecture at 5–7 h TIB | N3 **0 to +3 min**; REM **−30%**; sigma **−28 to −40%** | T1 | Kills the "hours below 8" ledger; spindle route bounded at 0.07–0.21 SD |
| `lo2016` + `voderholzer2011` consolidation of already-learned material at 5 h | **null** (P = 0.29; and null across 9/8/7/6/5 h) | T1 | The counterweight; forces the encoding-not-consolidation reading |
| `okano2019` night-before-test sleep | **not significant**, vs r = 0.38 for semester mean | T4 | Dissociates accumulation from test-day state |

## 7. My confidence

**Moderate-to-good on the architecture question (§1).** Five laboratories, five doses, unanimous
direction, quantitative PSG tables from primary sources I retrieved and verified. I would be surprised
if SWS preservation under 5–6 h restriction were overturned.

**Moderate on the direction and mechanism of channel (c) (§2).** The encoding-versus-consolidation
reconciliation is coherent, is supported by a same-programme same-dose contrast, and is corroborated by
`yoo2007`'s hippocampal data. But it rests on a small number of studies and I constructed the synthesis;
no paper I retrieved states it in these terms.

**Low on the magnitude.** The two routes to a number disagree by roughly an order of magnitude —
0.07–0.21 SD via architecture/spindles, ~0.89 SD via `cousins2018`. I cannot adjudicate. The modeller
should carry a prior wide enough to span both, and should not treat `cousins2018` as a point estimate
for three years of exposure.

**Low on anything cumulative.** See §8.

**Specific caveats to carry:** `cousins2018`'s g is back-computed from a P value, not from means and SDs
(paywalled). `yoo2007`'s Table 1 is internally inconsistent. `lo2016`'s published Cohen's d values are
on two different scales within one sentence, which inflates its headline contrast roughly two-fold — I
recomputed on a consistent d_z scale. `dunster2018` has no control group and its grades were assigned by
teachers who knew about the intervention. Four records carry `se: null` because no SE was derivable, and
`brunner1990`'s four effect values are direction-encoding placeholders, not measured quantities.

## 8. The single biggest gap in the evidence for this domain

**No study measures cumulative exposure on anything like the subject's timescale, so the accumulation
function is entirely unidentified.**

The longest experimental restriction in this literature is **7 consecutive nights** (`lo2016`,
`ong2016`, `huang2016`); most are 4–5, and several are 1–2. Our subject sustained ~5–6 h weeknights for
**three school years**, on the order of 600 restricted nights, interleaved with partial weekend
recovery. Every T1 effect in this shard therefore requires an extrapolation of roughly two orders of
magnitude in duration, and **nothing in the retrieved evidence constrains the shape of that
extrapolation.** The three live possibilities have very different implications and the literature
cannot distinguish them:

1. **Linear accumulation** — each restricted night adds a deficit. Would predict catastrophic loss over
   600 nights, which is prima facie implausible given the subject is functional.
2. **Plateau/adaptation** — the deficit saturates within days as homeostatic defence of SWS (which we
   *know* happens architecturally) stabilises consolidation. `voderholzer2011`'s and `lo2016`'s nulls
   at 4–7 nights are consistent with early saturation at a low level.
3. **Slow cumulative divergence** — small per-night losses compound into a widening knowledge gap. This
   is what `james2023` actually observes (null at year 1, +0.17 GPA at year 2, "effects were larger in
   the second year"), and it is the only *direct* observation of accumulation dynamics I found.

The critical weakness is that (3) — the only evidence favouring accumulation — **cannot separate
consolidation from instructional time.** In `james2023` the attendance outcomes follow an identical
trajectory (absences null at year 1, −0.8 at year 2). Fewer absences means more hours of teaching, which
produces knowledge accumulation with no consolidation pathway whatsoever. So the single study that tells
us the channel is cumulative cannot tell us it is a *sleep-consolidation* channel.

**What would close the gap:** a multi-year cohort with objective sleep (actigraphy/PSG) and curriculum-
referenced knowledge outcomes, adjusted for attendance and baseline ability. `Fitzsimmons/Carter/Scullin
2026` (PMID 41770612) is the closest existing design — 489 university freshmen, GPA at years 1 and 2,
adjusted for fluid intelligence and prior performance — and I could not extract it (paywalled, no
coefficients in the abstract, exposure is sleep quality rather than duration). **Retrieving that full
text is the highest-value single follow-up action for this shard**, followed by the `cousins2018` full
text to replace a P-value-derived effect size with means and SDs.

Until then the downstream model should treat the per-night consolidation deficit as small and poorly
identified, should **not** integrate any per-night effect linearly over 600 nights, and should treat
`james2023`'s year-2 GPA difference as the most defensible anchor for the real-world magnitude of the
learning channel while noting it is partly an attendance effect.
