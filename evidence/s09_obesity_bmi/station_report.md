# Station report — shard `s09_obesity_bmi`

Domain: short sleep, energy balance, appetite regulation and body weight, emphasis on adolescents
and young adults.

| | |
|---|---|
| Records screened | 85 |
| Included (YAML written) | 39 |
| Excluded | 46 |
| Effect estimates extracted | 87 |
| Identifier verification | **39/39 VERIFIED**, 0 failures |
| Schema validation | 39/39 pass against `effect.schema.json` |

Tier mix: **T1 = 15** (randomized/within-subject lab restriction, sleep-extension RCTs, pooled
RCTs), **T2 = 1** (school-start-time quasi-experiment), **T3 = 3** (Mendelian randomization),
**T4 = 1** (prospective cohort with actigraphy + measured fat mass), **T5 = 12** (prospective
cohort, self-reported exposure), **TX = 7** (cross-sectional / umbrella, context only).

Age match: `exact_16_19` = 5, `good_young_adult` = 7, `mixed` = 13, `fair_adult` = 8,
`poor_midlife` = 6. Access: `full_text` = 9, `abstract_only` = 30, `secondhand` = 0.

---

## What I did

Searched NCBI E-utilities (relevance- and date-sorted), Europe PMC REST, Crossref, Semantic Scholar
and Unpaywall. Every DOI was checked against Crossref *and* PubMed, and the DOI PubMed reports was
compared to the DOI written into the YAML. No record rests on recall.

All seven requested extractions were completed, and all four named meta-analyses exist and were
retrieved:

1. **Meta-analyses** — Cappuccio 2008 (`10.1093/sleep/31.5.619`), Fatima 2015
   (`10.1111/obr.12245`), Chen 2008 (`10.1038/oby.2007.63`), Miller 2018
   (`10.1093/sleep/zsy018`). Pooled ORs/RRs and per-hour BMI/BMI-z coefficients extracted.
2. **Dose-response** — found three: Zhou 2019 (adults, RR 1.09 per h below 7 h), Ruan 2015
   (paediatric, 0.05 kg/m² per h per **year**), Deng 2021 (paediatric, prospective only). Itani 2017
   is a fourth synthesis that looked for and **did not find** an obesity dose-response.
3. **Energy intake** — Spaeth 2013, Markwald 2013, St-Onge 2011, Nedeltcheva 2009 all retrieved, plus
   the pooled estimate (Al Khatib 2017, +385 kcal/d) and the heterogeneity record (McNeil 2017).
4. **Hormones** — Spiegel 2004 (leptin −18%, ghrelin +28%) and Taheri 2004 (−15.5%, +14.9%) both
   retrieved, alongside Nedeltcheva's 14-day **non-replication**.
5. **Expenditure offset** — Markwald 2013 (+~5%, ~111 kcal/d) against Al Khatib's pooled EE null and
   St-Onge's DLW null; Shechter 2014 rules out thermogenesis as the route.
6. **Mendelian randomization** — Hayes 2023, Wang 2019, Yu 2022.
7. **Adolescent cohorts** — Suglia 2014 and Sokol 2020 (Add Health, ages 16→21 and 12→32), Krueger
   2015, Asarnow 2015, plus Widome 2023 as the quasi-experimental counterweight.

Three departures from the task framing, reported as reality per hard rule 4:

- **Cappuccio's per-hour figure is 0.35 kg/m², cross-sectional**, and its authors explicitly decline
  causal inference. It is ~12× the best prospective estimate. I recorded it as an upper bound.
- **Fatima 2015's OR 2.15 is short-vs-LONG sleep**, not short-vs-normal. Used as-is it inflates the
  contrast. Flagged in the record and the log.
- **MR does not support the effect the task's framing anticipates.** Hayes 2023 finds +0.039 SD/h
  (p=0.42) for adult BMI — null and wrong-signed. Yang 2024's umbrella review claims MR demonstrates
  causality for obesity; that claim conflicts with the primary MR records and names neither study nor
  trait. Unresolved, logged.

## What I could not find

- **The reversibility question. Nothing measures it.** See the gap section below.
- **No sleep-restriction experiment in 16–19 year olds with an adiposity or energy-intake endpoint.**
  Two adolescent manipulations exist but have other primary outcomes: Dutil 2024 (insulin
  sensitivity) and Stager 2024 (cognition, adiposity as moderator). Both excluded here and **flagged
  to the metabolic and cognition shards**. Every T1 energy-balance number in this shard therefore
  comes from adults, mostly 18–50 y; the closest is Spiegel 2004 (12 men, 22 ± 2 y).
- **No MR restricted to adolescents.** Wang 2019 and Hayes 2023 use childhood-BMI GWAS consortia
  (EGG) for the child estimates and middle-aged UK Biobank for adults; neither instruments a 16–19 y
  exposure window.
- **No abstract exists for Chen 2008** in PubMed or Europe PMC; numbers came from retrieved publisher
  full text. Europe PMC `fullTextXML` returned zero bytes for Markwald 2013, Depner 2019, Widome 2023
  and Sokol 2020 (reCAPTCHA wall on `pmc.ncbi.nlm.nih.gov`); the first three were recovered from
  publishers, Sokol only at abstract level (`se: null`, `access_tier: abstract_only`).
- 22 of 87 effects carry `se: null` where no SE was derivable. None was invented.

## My confidence

**Moderately high on the direction and magnitude of the answer; low on any single point estimate.**

What makes me confident: the four identification strategies converge. Cross-sectional gives
0.35 kg/m²/h → prospective 0.03 kg/m²/h → quasi-experiment −0.02 kg/m² (−0.6, 0.6) → MR +0.039 SD
(p=0.42). Designs that break confounding and reverse causation all shrink the effect toward zero, and
the three strongest designs in or near the target age band (Widome T2, Hayes T3, LeMay-Russell T4)
are **all null**. Sokol 2020 locates the reverse arrow directly in the right age window: BMI → shorter
sleep (B = −0.02, p < 0.01) with the forward path null.

What limits me: the laboratory intake signal (+385 kcal/d) over-predicts observed real-world weight
divergence by **roughly 10–50×**, and I can document why (hyperpalatable ad libitum feeding at
130–150% of baseline, 4-h-vs-9-h doses far more extreme than this subject's ~6.5 h annualised
average, control arms that gain weight too, 2–14 day protocols, partial expenditure offset) without
being able to quantify how much each contributes. Anyone anchoring on the kcal/d figure and a
7,700 kcal/kg conversion will get ~39 kg over 3 years, which is certainly wrong.

Confidence-ledger grades for my headline number (per-hour BMI effect): **Quantity A** (24 cohorts in
Miller alone), **Quality B** (T5 dominant for the per-hour coefficient, though T1/T2/T3 corroborate
the null), **Transportability B** (paediatric-to-adolescent pooling; the T1 energy-balance evidence
is adult), **Model dependence C** (magnitude varies ~12× across defensible specifications, though the
sign is stable and every strong design points at ~0).

Specific things I would not defend: Fatima's OR 2.15 as a short-vs-normal contrast; the childhood MR
magnitudes (Hayes' −0.93 SD/h collapses to −1.77 SD, CI −7.24 to 3.39, after Steiger filtering);
Spiegel's −18%/+28% as anything but a 2-day acute upper bound, given Nedeltcheva's 14-day null and
Markwald's hormones moving the protective way while weight rose.

## Single biggest gap

**No study anywhere follows people through a defined multi-year period of short sleep, documents
their sleep normalising, and then measures whether the weight gained during the exposure persists,
reverses, or continues to accumulate.** This is exactly the subject's situation, and it is unmeasured.

The nearest approaches and why each falls short:

- **Markwald 2013** is the only direct measurement of the 5 h → 9 h transition. It lasts **5 days**;
  weight change over recovery was **−0.03 ± 0.50 kg**. Intake fell immediately; the ~0.8 kg already
  gained did not come off.
- **Chaput 2012** is closest in structure and measures the wrong thing: the *rate of further gain*,
  not reversal of past gain. Short sleepers who reached 7–8 h gained 1.1 kg/m² and 2.4 kg fat less
  over 6 y than those who stayed short, and became statistically indistinguishable from never-short
  controls — but n = 23 vs 20, unrandomised, self-selected, obesity-enriched cohort.
- **Tasali 2022** is the best causal design and runs **2 weeks** in adults aged 21–40 (−0.87 kg,
  −1.39 to −0.35). Its authors state that whether sleep extension reverses obesity "remains unknown."
  Al Khatib 2018, the second extension RCT, found no energy-balance effect at all.

Consequence for the downstream model: the persistence parameter should be carried as **unresolved**,
not imputed from these analogues. The defensible reading is that the forward hazard largely stops
once sleep normalises, that there is **no evidence accumulated weight spontaneously reverses**, and
that the amount at stake is small — **+0.05 to +0.23 kg/m² (≈0.2–0.7 kg)** by prospective
coefficients, upper bound ~0.5 kg/m² (≈1.7 kg) cross-sectionally. A posterior centred near zero with
an upper tail of 1–2 kg is defensible; one implying several kg is not.

**Secondary gap:** conditional on Yu 2022 (visceral fat −0.11 kg/h, p = 8×10⁻¹⁶, men −0.17 kg) being
right while every BMI MR is null, BMI may simply be the wrong outcome — the predicted phenotype is
fat redistribution without much BMI change. No study in this shard measures adolescent visceral fat
prospectively against sleep duration.

## De-duplication warnings for the pooler

`cohort_family` is populated on all 87 effects. Non-independent groups: **Add Health** — 7 effects
across `suglia2014`, `sokol2020`, `krueger2015`, `asarnow2015`; **Quebec Family Study** — 5 effects
across `chaput2008`, `chaput2012`; **same Colorado participants** — `depner2019`, `depner2021`;
**Wisconsin Sleep Cohort** — 3 effects in `taheri2004`; **UK Biobank** (± GIANT/EGG) — `hayes2023`,
`wang2019`, `yu2022`. Several paediatric meta-analyses (`miller2018`, `deng2021`, `ruan2015`,
`chen2008`, `fatima2015`) overlap substantially in their primary studies; `cohort_family` records the
pooled-source composition so the overlap is visible.

`shard: s09_obesity_bmi` on every record.
