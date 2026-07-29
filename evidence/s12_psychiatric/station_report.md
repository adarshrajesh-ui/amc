# Station report - shard `s12_psychiatric`

Domain: depression, anxiety, emotional regulation and suicidality in relation to short sleep in
adolescents and young adults, with the explicit task of separating causal direction.

## What I produced

| | |
|---|---|
| candidate records screened | **57** (requirement: >=25; task asked for >=30) |
| YAML records written | **42** |
| effect estimates extracted | **161** |
| schema validation | **42/42 pass** (`validate.py`, jsonschema Draft7) |
| citation audit vs PubMed `esummary` | **41/41 checked, 0 discrepancies** (`audit_citations.py`) |
| identifiers that failed verification | **0** — every DOI resolved on Crossref and every PMID on PubMed |
| tier distribution | T1 x15, T2 x4, T3 x5, T4 x1, T5 x11, TX x6 |

## What I did

Worked outward from the seed names in my task, then followed citation trails and ran ~35 PubMed
queries (logged in `screening_log.md`). Retrieved full text where possible (Europe PMC, PMC efetch,
Unpaywall, publisher PDFs); 16 records are `abstract_only` and 2 are `secondhand`. Every effect-size
conversion is recorded in `convert.py` / `convert_batch2.py` with its arithmetic printed to
`conversions*.txt`, and every extracted number carries a verbatim `quote`.

Three integrity habits caught real defects, so they were worth the time:

- **`audit_citations.py`** checks every citation string field by field against PubMed. It exists
  because I caught myself writing an author list from memory for `wang2024_yrbs` early on. It later
  caught a wrong first author (`gao2018_basus` was actually **Conklin** — file renamed to
  `conklin2018_basus` and all cross-references updated), a missing volume in `kok2026`, and an
  author-rendering quirk in `zhang2024_mr`.
- **`validate.py`** checks the schema plus my own invariants (point estimate inside its own CI, CI
  bounds ordered, no negative SEs, every effect has a quote). It caught two wrong SEs in
  `blake2017`.
- **Recomputing reported statistics before trusting them.** For `talbot2010` I recomputed
  partial eta-squared from each F and df pair; all four matched the printed values, which also
  exposed a **df typo in the paper** (printed `F(1,67)` with eta_p^2 = 0.10, which is only
  consistent at df_err ~= 55). For `sadikova2024` my standardisation reproduced the authors' own
  "15.6% of a standard deviation" to three decimals, confirming the SD I had derived.

## Confidence, by claim

| claim | confidence | why |
|---|---|---|
| Sleep loss causally degrades irritability, anxiety, positive affect and emotional regulation | **High** | 154-experiment meta-analysis (`palmer2024`) plus 5 within-subject experiments, consistent direction, plausible mechanism (`motomura2013` amygdala d_z 1.50), and reversible on extension (`vandyk2017`) |
| Improving *sleep quality* improves mood | **High** | 65 RCTs, g -0.35 after publication-bias adjustment (`scott2021`) |
| Insomnia causally raises depression risk | **Moderate-high** | 3 of 4 MR studies agree; `hertenstein2019` OR 2.83 |
| The observational association is heavily inflated | **High** | 7 independent routes, all pointing the same way |
| Reverse-causation share ~40-50% | **Moderate** | 3 cohort estimates converge (40/47/52%) but MR spans 22-54%, one reverse coefficient is non-significant, and `zink2024_abcd` dissents outright |
| **Short sleep *duration* causally raises depression risk** | **Low** | Continuous-duration MR is null twice over; the causal signal appears to live on the insomnia axis and leak into dichotomous short-sleep instruments |
| The causal effect on depression *scales* is mostly fatigue-item movement | **Moderate** | Compelling and replicated by two estimators — but in **one cohort** (START). This is the load-bearing claim with the thinnest independent support |
| Male attenuation for depression outcomes | **Moderate** | 4 designs agree, 1 dissents; none of the quasi-experiments published a sex split |
| Absolute risk figures | **Low-moderate** | Base rates are solid; the male-specific MDE base rate (9-12%) is **my inference**, not a quoted number, and the suicide arithmetic applies ideation ORs to death rates, which overstates |

## What I could not find or could not get

- **`yoo2007` — verified but unquotable.** The canonical amygdala citation, named in my task.
  Identifiers resolve cleanly, but it is a *Current Biology* magazine piece (pp. R877-R878) with no
  abstract in PubMed, no PMC or Europe PMC copy, and Cell Press returned **HTTP 403** to every PDF
  attempt; Semantic Scholar's abstract is publisher-elided. Recorded with **no magnitude and
  `se: null`** rather than a plausible-looking invented number. The mechanism requirement is
  discharged instead by `motomura2013`, which is better matched anyway: 5 nights of 4 h TIB, all
  young **males**, actigraphy-verified 4.60 h vs 8.09 h.
- **No sex-stratified estimates from any quasi-experiment.** `gangwisch2010` and `sadikova2024` both
  have the data. Neither published the split. Given four studies showing female-specific effects,
  this is the highest-value single missing number for the subject.
- **No mood-vs-cognition contrast within a single study.** `palmer2024` is closed access, so the
  1.5-2x ratio I report is a comparison *across* meta-analyses (`palmer2024` vs `lowe2017`), which is
  weaker than a within-study contrast. `pilcher1996` supports the same ordering.
- **No CIs for `wang2026_dsst`** (PMC deposit embargoed) and **no numbers at all for
  `berger2026_start`** (not open access, no PMC copy).
- **Two searches returned nothing**: MR of sleep traits on suicide attempt, and longitudinal studies
  of academic-workload-driven sleep restriction with psychiatric outcomes in college students.
- **`zhai2015` is not what my task said it was.** Described to me as adolescent; it is an
  **adult** meta-analysis. Reported as reality, per the instructions.
- **`lovato2014` reports no pooled effect size.** Real and correctly described, but qualitative, so
  it contributes no number.

## Single biggest evidence gap

**No study has measured depression, using an instrument free of sleep and fatigue items, in healthy
young people whose short sleep was imposed by external demands rather than by insomnia.**

Every branch of my evidence base fails at least one of those three conditions. The observational
literature has the wrong exposure (self-reported short sleep, confounded with insomnia and with
depression itself). The randomised literature has the wrong intervention (CBT-I for insomnia, and
only ~30 minutes of achievable sleep gain versus the subject's ~2-hour deficit). The experimental
literature has the wrong duration (days, not three years) and mostly the wrong ages. The one
design that gets the exposure right — the school-start-time natural experiment — has the right
exposure, the right ages, a strong first stage and two years of follow-up, and it reports that
**the entire depression-scale benefit sits in the fatigue items while the mood items do not move**.

That finding is the most decision-relevant thing I extracted, and it rests on **a single cohort
analysed twice** (`sadikova2024`, `berger2026_start`), corroborated only indirectly by an
experimental study whose authors predicted the same artefact 14 years earlier (`talbot2010`) and by
the somatic-subscale specificity in `zink2024_abcd`. If a downstream reader wants to know where this
shard is most likely to be wrong, it is here: I may be over-weighting one cohort's item-level
decomposition into a general claim about the literature. Conversely, if that decomposition is right,
then a large part of the published sleep-and-depression association in adolescents is a measurement
artefact, and the subject's psychiatric risk is materially lower than the headline numbers imply.

## Guidance for the pooler

1. **Do not pool the observational ORs with the quasi-experimental estimates as if they measured the
   same quantity.** They differ by a factor of ~2-10 for identifiable reasons.
2. **Keep the insomnia axis and the duration axis separate.** They diverge sharply in MR, and only
   the duration axis is relevant to this subject.
3. **Cohort de-duplication.** `cohort_family` is populated on every observational effect. Watch in
   particular: `sadikova2024` and `berger2026_start` are the **same 2,134 students** (START), and
   both are probably inside the `wang2026_dsst` pool. `gangwisch2010` is Add Health;
   `winsler2015` and `wang2024_yrbs` are both YRBS-family; `marino2021` (meta-analysis) and
   `marino2022_qlscd` (primary QLSCD) share a first author but are different data objects.
4. **Three records carry direction only and must not be assigned a magnitude**: `yoo2007`,
   `berger2026_start`, and the post-13 nulls in `marino2022_qlscd`. Each has `se: null` and an
   explicit warning in `conversion_formula`.
5. **`palmer2024`'s `ci` fields hold ranges of subgroup point estimates, not confidence intervals**,
   and `se` is null. Do not feed them to an inverse-variance pooler.
6. **Outcome construct matters more than usual in this domain.** Records tagged with fatigue,
   somatic, vigor or positive-affect constructs are measuring something partly downstream of the
   exposure itself. Depressed-mood-specific constructs are the ones that answer the actual question,
   and they are consistently the smallest.
