# Station report — shard `s06_sleep_need_measurement`

## What I did

Screened **49** candidate records, included **29**, extracted **96** effect estimates. Every effect carries a
verbatim `quote` field, so each number is independently auditable without re-reading the source. All 29
records validate against `effect.schema.json`.

**Identifier verification: 29/29 passed, 0 failures.** For each record I resolved the DOI through Crossref,
resolved the PMID through PubMed `esummary`, and checked that the DOI *PubMed reports for that PMID* matches
the DOI in the YAML. That third check is the one that catches transposition errors, and it did catch one: my
first draft of `screening_log.md` listed the wrong identifier for `weedon2022` (I had written PMID 35468939 /
`10.1186/s12920-022-01212-0`; the verified record is PMID 36137075 / `10.1371/journal.pgen.1010356`). Fixed,
and the log is now programmatically cross-checked against the YAML files.

Access: **16 full text, 13 abstract-only, 0 secondhand** (cross-checked programmatically against the
screening log, which agrees for all 29). Two full texts were recovered only by falling back
to PMC article *HTML* after the PMC *XML* deposit turned out to contain the abstract alone — including
`evans2021actigraphy`, which supplied the single most useful number in the shard.

## The six numbers that matter

| Quantity | Value | Tier | Source |
|---|---|---|---|
| Self-report minus objective sleep, mean bias | **+1.00 h** (SD on mean 0.30) | TX | 8 studies, adolescent mean 1.12 h / adult 0.99 h |
| Between-person SD of that bias | **1.40 h** (LoA −1.74 to +3.74) | TX | `white2026ffcws` 1.55, `lauderdale2008` 1.19 |
| Reverse calibration slope d(true)/d(report) | **0.19** (0.13-0.26) adolescents; 0.33 adults | TX | `white2026ffcws`, `cespedes2016hchs` |
| Sleep efficiency (TST/TIB), ages 16-19 | **0.875** (SD 0.06) | TX | `evans2021actigraphy` 0.872, `mitterling2015` 0.870, `meredithjones2024` 0.891 |
| Sleep need, ages 16-18 / 18-19 | **9.00 h / 8.70 h** | **T1** | `short2018sleepneed` 9.0-9.35, `klerman2008` 8.9, `kitamura2016` 8.41 |
| SD of individual sleep need | **0.70 h** (0.4-1.0) | **T1** | `kitamura2016` only (n = 15) |

## The single biggest gap in the evidence for my domain

**Nobody has measured how to convert an adolescent's sleep self-report into an estimate of his actual sleep,
and the two available methods disagree by more than the effect being estimated.**

Subtracting the mean bias gives 4.50 h for a 5.5 h report. The reverse regression gives 5.75 h at my
recommended β, or 6.53 h at the literature's measured β. That is a spread of **2.0 h in the exposure**, which
propagates to a weekday deficit anywhere from 2.2 to 4.5 h per night — a factor of two in the quantity the
entire factory exists to estimate. No downstream dose-response precision can survive it.

The gap is not that the studies are missing. It is that the studies answer the *wrong conditional*.
`lauderdale2008` regresses report on truth; the model needs truth on report. Only two retrieved studies ran
the reverse regression, and only one of those was in adolescents (`white2026ffcws`, β = 0.19). Nobody has
validated a *structured* self-report — weekday and weekend reported separately, which is what this subject
actually gave — against actigraphy or PSG in 16-19 year olds. `arora2013` shows the format matters enormously
(diaries correlated with actigraphy; single-item self-report did not, in the same 225 adolescents), so β for
a structured account is probably well above 0.19, but **no study measures it**. My β = 0.50 is an
interpolation, and I have flagged it as a judgement rather than a measurement.

**What would close it:** an adolescent cohort with (a) a structured weekday/weekend self-report, (b) at least
a week of actigraphy, and ideally (c) concurrent PSG on a subset to calibrate the actigraphy, analysed as the
reverse regression with the report as predictor. If the orchestrator can commission one targeted retrieval,
this is the highest-value one in my domain.

## Second gap: the SD of individual sleep need rests on 15 men

The between-person SD of sleep need is a load-bearing latent parameter — it decides whether "9 h needed" is
a population fact or a personal one — and my entire estimate of it comes from **one study of 15 healthy
Japanese men aged 20-26** (`kitamura2016`, SD = 0.18 × √15 = 0.697 h). Sampling uncertainty alone puts the
95% interval at 0.44-0.96 h before any concern about transportability to an American 18-year-old.

Neither guideline panel helps. Both assert that individual variability exists and neither quantifies it.
`paruthi2016`: *"Individual variability in sleep need is influenced by genetic, behavioral, medical, and
environmental factors. A clearer understanding of the precise biological mechanisms underlying sleep need
requires further scientific investigation."* `watson2015method` lists "Identify biomarker(s) of sleep need or
sleep deprivation" as a *future* research priority — i.e. no such biomarker exists.

I could have manufactured a tighter-looking number from heritability (√0.46 × 1.1 = 0.75 h, suspiciously
close to Kitamura's 0.70) and I deliberately did not, because heritable variance in observed duration
includes chronotype, schedule sorting and reporting style, none of which is sleep need — and
`kocevska2021herit`'s 6-fold reporter effect (8% parent-report vs 38-52% self-report) proves a large slice of
estimated h² is measurement artefact. The apparent agreement would have been coincidence dressed as
corroboration.

## Where the evidence is genuinely strong

Three things I would defend confidently:

1. **Sleep efficiency ≈ 0.875 for a 16-19 year old.** Four sources, two modalities (PSG and actigraphy), two
   continents, converging on 0.870 / 0.872 / 0.878 / 0.891. Two independent meta-analyses agree that no age
   adjustment is needed across this range (`ohayon2004` d = 0.01; `evans2021actigraphy` r = −0.05, and its
   authors note the association is fragile to single-study removal). The derived TIB−TST gap agrees to within
   two minutes between two independent PSG datasets (63.4 vs 61.8 min).
2. **Adolescent sleep need is ~9 h and does not step down at 18.** The guidelines drop a full hour at the
   18th birthday (`hirshkowitz2015nsf`: 8-10 h → 7-9 h) and the two guidelines even *disagree* about an
   exactly-18-year-old, because `paruthi2016`'s teenage band runs to 18 while NSF's stops at 17. The T1
   evidence shows no step: 9.0 h at ages 15-17 and 8.9 h at ages 18-32.
3. **The observed adolescent sleep decline is lost opportunity, not reduced need.** Three unrelated designs
   agree. `ohayon2004`: duration falls with age on school days (d = −0.57) but not on nonschool days
   (d = −0.04). `inderkum2018twin`: duration heritability 15% on school days versus 68% on free days, in the
   same twins over the same six months. `klerman2005`: short habitual sleepers were objectively sleepier at
   baseline *and* still slept more on day 3 of extended opportunity. Any one could be dismissed; together they
   make "he may simply need less sleep" hard to sustain.

## Unresolved conflicts I am handing over rather than papering over

- **Does actigraphy over- or under-count adolescent sleep?** `meredithjones2024` validated it against
  concurrent home PSG in 8-16 year olds and found specificity of only **63.8%** — a third of true wake scored
  as sleep, so actigraphy **over**-counts. `short2012diary` argues the opposite for adolescent boys
  specifically ("increased sleep motor activity in adolescents that actigraphic algorithms score as wake").
  They cannot both be right and the direction changes the bias magnitude. `jackson2018mesa` sides with
  over-counting (PSG bias 73 min > actigraphy bias 66 min in whites). I widened the SD on the mean bias to
  0.30 h rather than choosing.
- **Did the subject report time in bed or time asleep?** Not recoverable from the case description, and it is
  worth ~1 h. `watson2015method` concedes the whole epidemiological literature has this problem: *"self-report
  questions may have captured time in bed rather than time asleep."* This should be a discrete model branch,
  not an average.
- **`white2026ffcws`'s actigraphy metric is sleep-*period* time**, not total sleep time (*"the period between
  the first and last scored sleep epochs, encompassing sleep onset latency (SOL) and wake after sleep onset
  (WASO)"*). Its +0.46 h weekday bias therefore understates the bias against true TST by roughly 0.5-0.8 h.
  The best-age-matched study in the shard is measuring a slightly different thing from the others.

## Two ways the downstream model could go badly wrong

Both are easy to commit by accident and both are large.

1. **Unit mismatch across the subtraction.** `hirshkowitz2015nsf` warns about its own evidence base:
   *"actual sleep time is typically less than time in bed, which biases data toward higher sleep duration
   estimates."* The NSF bands are partly anchored on time-in-bed-contaminated self-report. Subtracting an
   objective PSG/actigraphy TST from those bands overstates the deficit by roughly the 1.0 h efficiency gap.
2. **Double-discounting.** Subtracting the ~1 h mean bias *and* multiplying by the ~0.875 efficiency applies
   the same ~1 h correction twice. They are alternative routes from subjective report to true sleep, not
   sequential steps.

## Confidence

- Sleep efficiency: **high**. Four-way convergence, explicit definitions, age-invariance established twice.
- Sleep need central estimate: **moderate-to-high** for the central value (three T1 asymptotes at 8.16 /
  8.41 / 8.9 h plus an age-matched 9.0 h), **low** for its SD (one study, n = 15).
- Mean self-report bias: **moderate**. Eight studies, tight clustering near 1 h, but every reference standard
  is imperfect and the best-age-matched study measures a slightly different construct.
- Report-to-truth calibration: **low**, and this is the shard's weak point. The functional form is right and
  the direction is right; the slope for a structured adolescent self-report is not measured anywhere I could
  find.

## Note on what the seed task expected versus what exists

Per the instruction to report reality rather than the task's assumptions: **`kocevska2021norms`
(Nature Human Behaviour 2021) could not serve the role the task assigned it.** The task asked for "means and
SDs by age band, from OBJECTIVE measurement" from that meta-analysis. It is paywalled (Unpaywall
`is_oa: false`, Europe PMC `isOpenAccess: N`, no PMC deposit), and its abstract reports no age-band means and
no SDs — the reference charts are figures in the full text. I extracted only what the abstract states
verbatim (the 51.5% teenage prevalence and the self-report/actigraphy sex sign reversal, which is a genuinely
valuable finding) and did **not** reconstruct numbers from figures. The normative role was reassigned to
`galland2018` (actigraphy, 7.4 h at 15-18 y), `evans2021actigraphy` (actigraphy, 7.18 h and efficiency 0.872
at 10-19.99 y) and `mitterling2015` (PSG, <= 30 y). Similarly, `ohayon2004` does not report age-band means and
SDs at all — it reports standardized *age-association* effect sizes — so I extracted those and said so rather
than inventing band means. `boulos2019` would have given the pooled adult sleep-efficiency level but is
paywalled; only its age slopes were obtainable.
