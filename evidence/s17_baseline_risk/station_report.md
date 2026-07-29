# Station report — shard `s17_baseline_risk`

**Domain.** Absolute baseline risks for a US male and the life-table machinery that turns another
shard's hazard ratio into months of life expectancy. This shard produces no hazard ratios of its
own; it produces the denominators everything else divides into.

**Screened** 141 PubMed records across 36 queries plus 11 official statistical products.
**Included** 29 records carrying 72 effect estimates, all `outcome_domain: baseline_risk`,
all `tier: TX`. **Schema:** 29/29 validate against `effect.schema.json` with zero failures.
**Citations:** 27/29 resolve through Crossref or PubMed at title similarity 1.00; the 2 that do
not are the SSA period life table and the NSDUH detailed tables, neither of which has a DOI or
PMID, both flagged `UNVERIFIED` in-record rather than given a guessed identifier.

---

## 1. Deliverable 1 — the life table (gate G10)

`/workspace/data/lifetable_us_male.csv` — 92 data rows, ages 19–110, columns `age,qx,lx,ex`,
with a 25-line header comment giving both sources, both URLs, the splice rationale and the
calibration results. A companion `/workspace/data/lifetable_us_male_full.csv` carries ages 0–120
with `dx`, `Lx`, `Tx` and a per-row `qx_source` so a consumer can recompute `e0` and validate
against the published figure independently.

**Values the pipeline should calibrate against, both from NCHS Table 2 (males, 2023):**

| quantity | published | full precision |
|---|---|---|
| `e0` male | 75.8 y | **75.8178** |
| `e19` male | 57.7 y | **57.6565** (= 691.88 months) |
| `e65` male | 18.2 y | 18.1943 |
| `e50` male | 30.0 y | 29.9611 |

Independent cross-check from a different agency (SSA period life table 2023): `e0` = 75.79,
`e19` = 57.62. The two agencies agree to 0.03 y at both index ages.

**Gate result.** Recomputing `ex` from the `qx` column alone — using no published `lx` or `Lx`,
just `dx = lx·qx`, `Lx = lx − 0.5·dx`, `ex = Tx/lx` — reproduces:

- `e0` 75.8203 vs published 75.8178 → **0.0025 y error**
- `e19` 57.6568 vs published 57.6565 → **0.0003 y error**
- `e65` 18.1947 vs published 18.1943 → **0.0004 y error**

All are two orders of magnitude inside the 0.3-year tolerance. The residual is entirely the
`a(x) = 0.5` mid-year assumption versus NCHS's estimated `a(x)` in the first year of life.

**Provenance: fully programmatic, no hand transcription.** `build_lifetable.py` downloads the
official NCHS spreadsheet (`Table02.xlsx`) and the SSA table, parses both, splices and recomputes.
Two sources are required because **NCHS closes its published table at an open-ended "100 and
older" interval**, so single-year `qx` above 99 does not exist in the NCHS product; SSA publishes
male `qx` to 119. SSA *rates* are applied to the NCHS *radix*, so `lx` stays on the NCHS
per-100,000-live-male-births scale throughout. Over the overlapping ages 19–99 the two agencies'
`qx` differ by at most 1.05×10⁻² in absolute terms (age 97) and 6.78% in relative terms (age 19,
where `qx` ≈ 0.001 so the absolute gap is trivial).

**The survival column matters as much as `e19`.** From `lifetable_us_male_full.csv`, a 19-year-old
US male has probability 0.9583 of reaching 40, 0.7996 of reaching 65, **0.5168 of reaching 80**
and 0.1948 of reaching 90. Any lifetime risk quoted without competing mortality is inflated by
roughly the reciprocal of these numbers, which is the entire subject of deliverable 3.

## 2. Deliverable 2 — absolute baseline risks

`/workspace/data/baseline_risks.yaml`, 26 risk entries plus 6 sleep cross-checks. Every entry has
`value`, `ci`, `age_at_assessment`, `sex`, `source`, `doi_or_url`, `year`, plus `definition`,
`competing_risk_adjusted`, a verbatim `quote` and a `verification` block. Headline male figures:

| outcome | value | at age | source |
|---|---|---|---|
| Type 2 diabetes, lifetime risk | **40.2%** (39.2–41.3) | 20 | Gregg 2014 |
| — same, newer cohort | 32.8% (32.4–33.2) | 20 | Koyama 2022 |
| — by BMI at age 18 | **7.6% → 70.3%** | 18 | Narayan 2007 |
| Hypertension, residual lifetime risk | **~90%** | 55 and 65 | Vasan 2002 |
| CHD, lifetime risk | **48.6%** (45.8–51.3) | 40 | Lloyd-Jones 1999 |
| Total CVD, lifetime risk | **60.3%** (59.3–61.2) | 45 | Wilkins 2012 |
| — by risk-factor burden | 51.7% overall, **5.2% if all optimal** | 50 | Lloyd-Jones 2006 |
| Dementia, lifetime risk | **13.8%** (12.2–15.3) | 45 | Chêne 2015 |
| — newest US estimate | 35% (33–36) | 55 | Fang 2025 |
| — reconciled band (see §4) | **20–30%**, range 9–31% | 19 | this shard |
| Obesity, prevalence at midlife | **45.4%** | 40–59 | Emmerich 2024 |
| — projected from childhood | **57.3%** (55.2–60.0) | 35 | Ward 2017 |
| MDD, lifetime prevalence, male | **14.7%** (13.9–15.5) | 18+ | Hasin 2018 |
| — morbid risk to 75, male | **20.1%** (19.2–20.9) | birth | McGrath 2023 |
| MDE, past-year, male 18–25 | **12.4%** (11.3–13.5) | 18–25 | NSDUH 2024 |
| Suicide, annual rate, male | **21.1 / 100,000** | 15–24 | Garnett 2024 |

Three points where I did more than transcribe:

**The diabetes cumulative incidence at 50/65/80 that the brief asked for is not published.** No
source gives age-specific cumulative incidence of diabetes for US males at those horizons. Rather
than invent a schedule I recorded `DERIVED_BOUNDS` with deliberately wide ranges (8–16% by 50,
18–28% by 65, 28–40% by 80) and documented the derivation basis for each. These are bounds, not
point estimates, and the YAML says so.

**Suicide's 15–24 band straddles the subject.** The male rate of 21.1 per 100,000 is a 15–24
average, and the subject sits exactly on the seam. NCHS Data Brief 471 splits the band: 11.8
(15–19) versus 19.4 (20–24) per 100,000, both sexes — a **1.64× gradient across precisely the
ages 18–22 being modelled**. Recorded as a ratio to shape the male rate, not as a male rate.

**MDD needed three sources, not one.** Kessler's NCS-R 16.2% is sex-pooled; Hasin's NESARC-III
gives a clean male 14.7%; and neither is the right *estimand* for an 18-year-old, because a
lifetime prevalence measured in a mostly-middle-aged sample counts risk already realised. McGrath
2023's **morbid risk** to age 75 (male 20.1%) is the projected-forward quantity this subject
needs, and it is 37% higher than the male lifetime prevalence for exactly that reason.

## 3. Deliverable 3 — the conversion machinery

`competing_risk_method.md` (25 KB, 5 sections, 11 cited references) plus a working, runnable
`hr_to_life_expectancy.py` that reads the life table and prints seven panels of worked examples.

**The prohibited operation and why.** Multiplying a hazard ratio by a lifetime risk fails for
three independent reasons, each documented with numbers from this shard's own data:

1. **A hazard ratio is not a risk ratio once risk is large.** Under proportional hazards the
   correct transformation is `F₁ = 1 − (1 − F₀)^θ`. At the diabetes baseline of 40.2% with
   HR 1.20, correct gives 46.0% but naive gives 48.2% — the naive *increment* is overstated by
   1.38×. At the hypertension baseline of 90% the naive answer is **108%**, an impossible
   probability, and the increment is overstated by 4.88×.
2. **Competing mortality absorbs part of the effect.** Raising a disease hazard also removes
   person-time in which the disease could occur.
3. **The two quantities usually refer to different things** — different index ages, different
   ascertainment, different follow-up windows.

The required procedure instead: convert to a hazard, apply it to the age-specific schedule, and
recompute the cumulative incidence function through the competing-risk recursion. Section 3.4
gives it step by step.

**The published demonstration.** Chêne 2015 reports male dementia risk from age 45 as **13.8%
competing-risk adjusted against 61.0% unadjusted — a 4.42× inflation in one paper, one cohort,
one set of men.** Seshadri 1997 shows the same at 3.01×. These are not hypotheticals.

**The exposure window dominates everything.** This is the single most consequential number I can
hand the pipeline. An all-cause mortality HR of 1.13, applied lifelong from 19, costs **−1.49 y
(−17.9 months)** of `e19`. The same HR confined to ages 19–21 — the subject's actual documented
exposure — costs **−0.026 y (−0.31 months)**. That is a **58-fold difference driven purely by the
window**, and it is larger than any disagreement among the published sleep estimates. A model
that applies a lifelong HR to a 3-year exposure will overstate the harm by nearly two orders of
magnitude. Cause-specific HRs need a second down-weighting by the cause fraction: HR 1.5 on all
causes costs 60.1 months, but on the 20% of the hazard that is CVD it costs 13.9.

**End-to-end validation.** Feeding an all-cause HR of 1.10–1.13 lifelong from age 20 through this
life table returns −1.15 to −1.48 y; Chaput 2022's independently published figure is −1.2 y.
Different country, different life table, different implementation, same answer. This is a
regression test: if a future change breaks it, the change is wrong.

## 4. Deliverable 4 — published sleep life-expectancy estimates

**Report reality against the brief's hint: RAND publishes no life-expectancy or QALY estimate for
short sleep.** The brief suggested RAND's economic analyses as a likely source. Hafner 2017 is a
macroeconomic model whose outputs are GDP, working days and employment. Its only health-relevant
quantities are relative risks *imported* from prior observational meta-analyses (1.13 for <6 h,
1.07 for 6–7 h, no confidence intervals given) and its cost figures ($280–411 bn/yr for the US,
1.56–2.28% of GDP). **Anyone citing RAND for "years of life lost to short sleep" is misciting
it.** I extracted the RRs, which are usable, and flagged the report `ROBINS-I: critical` because
it treats imported associations as causal with no sensitivity analysis for reverse causation.

**No published QALY estimate for short sleep exists.** Five targeted queries found none. The only
paper linking sleep duration to a QALY-like outcome is in Korean CKD patients (PMID 33957617),
excluded as untransportable. If this pipeline emits a QALY figure it is the first one and has
nothing to validate against; the YAML says so explicitly.

**Four life-year estimates do exist, and they span 1.2 to 5.0 years — but the spread is
explained, not random.** They order themselves precisely by how much *non-sleep* lifestyle each
contrast absorbs:

| study | estimate | index age | what the contrast really is |
|---|---|---|---|
| Chaput 2022 | +1.2 y | 20 | sleep **duration alone**, life table + meta-analytic RR |
| Huang 2023 | −2.31 y | 40 | 5-item sleep composite, **CVD-free** years, men |
| Li 2024 | −4.7 y | 30 | 5-factor sleep composite, men |
| Ma 2023 | +5.0 y | 50 | **1 of 8** CVH components, *not mutually adjusted* |

Ma 2023's 5.0 years is the figure most likely to be quoted and least entitled to be, and the
paper refutes it with its own arithmetic: **the tobacco component alone is 7.4 y and sleep alone
is 5.0 y, summing to 12.4 y — more than the entire high-versus-low total contrast of 8.9 y**
before the other six components are counted. Component contrasts that sum to more than the whole
cannot be independent. Allocating Ma's male total of 8.1 y equally across 8 components gives
≈1.0 y for sleep, which converges with Chaput's 1.2 y and with the HR 1.10–1.13 range above.

**Recommended prior for the mortality channel: 1.0–1.5 years of `e19` for a lifelong short-sleep
habit** — and far less for a 3-year window, per §3.

## 5. What I could not supply

1. **The AHA Statistical Update — the one task-named source I could not open.** I verified the
   current edition (2026, PMID 41562125, `Circulation` 153(9):e275–e906) and the prior one, but
   `ahajournals.org` returns HTTP 403 to automated clients for both HTML and reader views, there
   is no PMC copy, and the PubMed abstract contains no statistics. Hard rule 2 forbids extracting
   what cannot be quoted, so I took nothing rather than recalling a figure. Mitigating: the Update
   does not compute lifetime risk itself — it cites Lloyd-Jones 1999/2006 and Wilkins 2012, all
   included here at first hand, so extracting it would have double-counted Framingham. Logged in
   the YAML with an action note for an operator with institutional access.
2. **Narayan 2007's intermediate BMI categories.** `diabetesjournals.org` returns 403 and a
   Cloudflare challenge through a text proxy. Only the published endpoints (7.6% underweight,
   70.3% very obese at age 18) are quotable; normal-weight, overweight and obese are `null`, not
   interpolated.
3. **Age-specific diabetes cumulative incidence** at 50/65/80 — not published anywhere; wide
   `DERIVED_BOUNDS` supplied instead.
4. **Sex-specific dementia risk from Fang 2025** — the ARIC paper reports 35% overall without a
   male stratum.

## 6. My confidence

**High** on the life table. It is machine-downloaded from the authoritative national source,
independently recomputes to within 0.0003 y of the published `e19`, and agrees with a second
agency to 0.03 y. Gate G10 is not at risk.

**High** on the conversion machinery. The formulas are standard and cited, the implementation is
executable, and it reproduces an independently published sleep life-expectancy estimate.

**Moderate** on most absolute risks. Diabetes, CHD, CVD, hypertension and suicide come from
authoritative sources with tight intervals. Two caveats apply to all of them: they are *period*
estimates for cohorts that are not the subject's, and most are indexed at ages 40–65, so
`population.adolescent_match` is `poor_midlife` or worse on the majority of records.

**Low** on dementia — see below.

## 7. The single biggest gap

**Every absolute risk in this shard is indexed at an age the subject has not reached, and the
worst case is dementia, where published male lifetime risk spans a factor of 3.6.**

I put all five published estimates on one scale by multiplying each by `S(19→index)` from this
shard's own life table — which is the competing-mortality correction from §2 applied to the
literature instead of to an incidence schedule:

| study | index age | as published | from age 19 |
|---|---|---|---|
| Seshadri 1997 (Framingham, men) | 65 | 10.9% | 8.7% |
| Chêne 2015 (Framingham, men) | 45 | 13.8% | 13.0% |
| Fishman 2017 (men, via Hudomiet) | 70 | 24.0% | 17.5% |
| Hudomiet 2025 (HRS, men, derived) | 70 | 37.8% | 27.5% |
| Fang 2025 (ARIC, overall) | 55 | 35.0% | 31.3% |

**Standardising the index age does not narrow the range at all**, which is itself the finding:
index age is not the driver, ascertainment is. Hudomiet et al. 2025 — found late in screening and
the most useful single paper for this problem — diagnose the mechanisms, and **all four bias
downward**: claims data miss undiagnosed dementia; the widely used calibrated cutoff method
underpredicts prevalence at 85+ by 4.8 points, validated against the ADAMS clinical substudy
where their model gave 0.359 against an observed 0.358 while the cutoff method gave 0.310;
estimates from status measured months before death miss terminal progression; and older cohorts
had lower life expectancy, so more members died young where dementia risk is low.

**Because every identified bias points the same way, the low end of this range is likelier to be
wrong than the high end.** Chêne's 13.8% — the figure the brief pointed me at and the one a
model would naturally reach for — is probably a floor rather than a central estimate. I recommend
**20–30% as the central band with 9–31% carried as uncertainty.** Any neurodegeneration
conclusion that changes materially across that band is not a conclusion.

A related trap in the same data: 41.3% of decedents ever have dementia but only **20.1% live with
it for five or more years**. A QALY model that applies a multi-year disability weight to the
lifetime risk roughly doubles the true loss.

## 8. Files

**Data deliverables** (`/workspace/data/`): `lifetable_us_male.csv` (ages 19–110, `age,qx,lx,ex`),
`lifetable_us_male_full.csv` (ages 0–120, all columns + `qx_source`), `baseline_risks.yaml`
(26 risks + 6 cross-checks).

**This directory:** 29 YAML evidence records; `competing_risk_method.md`; `screening_log.md`;
this report; and four scripts for reproducibility — `build_lifetable.py` (downloads and builds the
life table), `hr_to_life_expectancy.py` (the conversion machinery, runnable, prints worked
examples), `gen_records.py` (generates the YAML records from a structured spec), `validate.py`
(schema validation), `pm.py` (cached PubMed/Crossref access).

**Reproduce everything:**

```bash
python3 build_lifetable.py /tmp/s17     # rebuild both CSVs from source downloads
python3 hr_to_life_expectancy.py        # print all worked examples and calibration checks
python3 gen_records.py && python3 validate.py   # regenerate and validate all 29 records
```
