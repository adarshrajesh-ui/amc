# Station report — shard `s16_social_jetlag`

Domain: **circadian misalignment as an exposure separate from sleep duration, and weekend catch-up
sleep as an effect modifier.**

| | |
|---|---|
| Records screened | **81** (brief required ≥30) |
| Records included | **41** |
| Effect estimates emitted | **111** (42 with an SE and directly poolable; see "how much is poolable") |
| Schema validation | **41/41 pass** against `effect.schema.json` (Draft-07) |
| Effects with a verbatim quote | **111/111** |
| DOIs verified via Crossref | **42/42** |
| PMIDs verified via PubMed eSummary | **41/41** |
| Crossref-vs-PubMed DOI mismatches | **0** |
| Identifiers that FAILED verification | **none** |
| Full text retrieved | 9 studies; 32 abstract-only; 0 secondhand |
| Tier mix | T1 6, T4 2, T5 3, TX 30 |
| Age transportability | `exact_16_19` 21, `good_young_adult` 5, `fair_adult` 4, `mixed` 5, `poor_midlife` 6 |

The 42nd verified identifier is the Roenneberg 2012 **Erratum** (DOI `10.1016/j.cub.2013.04.011`),
which has a DOI but no PMID. It is recorded in `verification.json` and flagged in
`roenneberg2012.yaml` notes; it is not a separate study record, hence 41 YAML files against 42
identifier checks.

---

## What I did

**Method.** All searching went through PubMed eSearch/eSummary/eFetch and Europe PMC via a small
helper (`/tmp/s16/pm.py`); full text via Europe PMC `fullTextXML`, NCBI PMC, Unpaywall and publisher
HTML (`/tmp/s16/ft.py`), re-wrapped one sentence per line so that keyword search over the body text
actually worked (`/tmp/s16/wrap.py`). Every DOI was checked against Crossref and every PMID against
PubMed, and I additionally cross-checked the Crossref DOI against the DOI PubMed holds for the same
record (`/tmp/s16/verify.py`, results in `/tmp/s16/verification.json`). All effect-size conversions
are in `/tmp/s16/convert.py` and are restated inside each record's `conversion_formula`. Records were
emitted programmatically (`/tmp/s16/emit.py`) and validated with `jsonschema`
(`/tmp/s16/validate.py`).

**All seven required extractions were completed.** Item-by-item:

1. **The construct.** `wittmann2006.yaml` — the defining paper, verified (PMID 16687322, DOI
   `10.1080/07420520500545979`), plus `roenneberg2019.yaml` for the formal equation
   **SJL = |MSF − MSW|** from the originators. **Age-specific norms, which the brief flagged as
   critical, came from two much larger later datasets rather than from Wittmann 2006**: Randler 2019
   (n=18,323, peak **3:18 h at age 16**) and Illingworth 2025 (n=19,760, mean **1:53 h, SD 1:07**,
   peak **2:07 h at age 15**), supported by Martins 2025 (n=64,029, >80% exceed 1 h). Illingworth is
   the only anchor that publishes an SD, so it is the only one that supports a percentile.
2. **Roenneberg 2012 BMI.** `roenneberg2012.yaml`, full text read. **The requested per-hour BMI
   coefficient with CI is not in the paper's main text** — see "what I could not find". What the
   paper does support, and what I extracted, is the restriction that matters more: the association is
   **confined to BMI ≥25** and absent in the normal-BMI group (n=43,302).
3. **Cardiometabolic, duration-adjusted.** All three named papers found and extracted:
   `koopman2017.yaml` (n=1,585; MetS prevalence ratio **2.13**, 1.3–3.4 for SJL >2 h vs <1 h in
   under-61s), `wong2015.yaml` (n=447, **actigraphic** SJL; HOMA-IR β=0.11, p=.031 after adjusting
   for sleep duration *and* sleep debt), `parsons2015.yaml` (n=815; effects hold "controlling for
   sex, chronotype and sleep duration", and critically **SJL and sleep duration were uncorrelated,
   r=−0.04, p=0.28**). Added `bouman2023.yaml` and `arab2024.yaml` as the meta-analytic layer and
   `zhou2026.yaml` for the paediatric-specific picture.
4. **Mood and academic.** `sun2025.yaml` (depression, **≥2 h → OR 1.44**, 1.18–1.77; **1–2 h → OR
   1.05**, null), `ravenhall2026.yaml` (anxiety, n=235,526), `lu2026.yaml`, `haraszti2014.yaml`
   (university students), `sanchezcharcopa2026.yaml` (**per-hour, duration-adjusted GPA OR 0.76**,
   0.68–0.85, official school records), `diazmorales2015.yaml`, `henderson2019.yaml`.
5. **Experimental misalignment with duration held constant.** `leproult2014.yaml` (full text; the
   single most important record in the shard), `scheer2009.yaml`, `buxton2012.yaml`,
   `morris2015.yaml`, and `hasler2022.yaml` — the only experimental misalignment study in
   adolescents, which imposed literally the school-versus-summer schedule contrast.
6. **Weekend catch-up.** Åkerstedt 2019 (`akerstedt2019.yaml`, full text) and Depner 2019
   (`depner2019.yaml`, full text) both found and read in full. The named "Oh et al." and "Im et al."
   I could not confirm as such (see below), but the intended Korean national-data evidence is covered
   by `lee2022.yaml` (n=270,619), `lee2025.yaml`, `choi2023.yaml`, `kimdj2020.yaml`, `son2020.yaml`,
   `kim2011.yaml`, `kang2014.yaml`, and — decisively — `park2023.yaml`, a six-wave
   individual-fixed-effects panel analysis. Catch-up and depression: `carbone2026.yaml` (NHANES,
   **ages 16–24**) and `kimcasement2026.yaml` (Fitbit-measured, explicit U-shape).
7. **Adolescent phase delay.** `crowley2014.yaml` (full text; laboratory melatonin plus actigraphy,
   ages 9–19), `crowley2007.yaml`, `carskadon1993.yaml`, `hasler2025.yaml`.

**The critical tension was resolved**, not merely reported. `jetlag_summary.md` §5 shows the
protective and harmful literatures are not contradictory for two identifiable reasons — they code
**different exposures** (duration difference vs timing difference, which move together for the same
behaviour), and the true dose–response is **U-shaped** with each camp having sampled one arm — and
then gives an outcome-by-outcome table and a per-domain modifier grid.

---

## What I could not find

Listed in descending order of how much it cost the extraction.

1. **The per-hour SJL→BMI coefficient with CI from Roenneberg 2012.** This was explicitly requested.
   The main text reports the association qualitatively and directs the reader to supplementary Table
   S1B, which I could not retrieve, and a formal **Erratum (DOI `10.1016/j.cub.2013.04.011`,
   Crossref-confirmed) whose content I also could not retrieve.** I refused to reconstruct the
   coefficient from the figure. Substitutes actually extracted: Bouman 2023's **0.49 kg/m²**
   (0.21–0.77) for any SJL vs none, and Parsons 2015's per-unit β=0.10, p=0.012. The unresolved
   erratum is a live risk flag: I cannot rule out that it revises the very number the brief asked
   for.
2. **Åkerstedt 2019's numeric estimate for the short-weekday/long-weekend cell.** This is the single
   most decision-relevant point estimate in the whole protective column, because it is the exact
   pattern our subject exhibits. The paper states the null in words — *"The mortality rate of
   individuals with short sleep during weekdays, but medium or long sleep over weekends (SML), did
   not differ from the reference group rate"* — but the point estimate and CI appear only in Figure
   4. I recorded the stated null and **did not digitise the figure**. The comparator HR I did extract
   with a CI is consistently-short: **HR 1.65 (1.22–2.23)**.
3. **"Oh et al." and "Im et al." on Korean catch-up sleep.** I searched for both by name against
   PubMed and could not confirm either as the intended paper. Per hard rule 4 I am reporting reality
   rather than attaching a plausible-looking identifier to a seed name. The substance the brief
   wanted is covered by the eight Korean records listed above. **Cohort-family warning for the
   pooler:** several of these draw on the KNHANES/Korea-Youth-Risk-Behaviour family and are recorded
   with `cohort_family` set accordingly — they must **not** be treated as independent.
4. **A Depner 2019 between-arm contrast (weekend-recovery vs continuous-restriction).** It does not
   exist. Reading the full text, the analysis is explicitly *"within group"*: the widely cited
   −27%-versus−13% insulin-sensitivity comparison **was never statistically tested**, there is no CI
   or p-value for the difference anywhere in the paper, and the −27% itself **lost significance when
   body weight was controlled (P=0.054)**. I recorded the two within-arm changes separately with
   `se: null` and declined to emit a between-arm effect size. This materially weakens the
   "catch-up is metabolically harmful" position, which rests almost entirely on this study.
5. **Phase-delay estimates indexed by pubertal stage.** Requested, but not supportable. In the best
   longitudinal data Tanner stage adds *"no statistically significant information above chronological
   age"* except a ~12-minute effect on weekday sleep onset in the younger cohort; the pubertal
   framing traces to Carskadon 1993, which used a **questionnaire** rather than measured phase and
   found the association **in girls only**, with a non-significant trend in boys. For an 18-year-old
   male I recommend the age-indexed figure instead: **~1 h of delay across ages 17→19**.
6. **Any measured dose–response for misalignment below ~8 h.** See "biggest gap".
7. **Full text for 32 of 41 included studies.** Extraction there rests on abstracts and, where
   available, published tables. Flagged per record via `access_tier`.

**One published defect found and preserved rather than silently cleaned:** Arab 2024 reports an OR of
1.20 with a 95% CI of (1.02, 1.140) — the point estimate lies outside its own interval, so the
interval is internally impossible and no SE is derivable from it. I extracted the internally
consistent pooled correlations instead (**r = 0.12**, 0.07–0.17) and flagged the OR with `se: null`.

---

## My own confidence

**High confidence (would defend without qualification):**

- **Misalignment harms metabolism independently of sleep duration.** Leproult 2014 equated sleep to
  **three minutes** across arms (4 h 48 min vs 4 h 45 min) and still found insulin sensitivity in men
  falling **−58% vs −32%** (p=0.011; my computed **g = −1.23, SE 0.505**) and hsCRP rising **+146% vs
  +64%** (p=0.049). Duration is not doing that work. Parsons 2015 supplies the observational analogue
  in a cohort where SJL and duration were **uncorrelated**.
- **The subject is not a social-jetlag outlier.** His central **1.75 h** sits at roughly the
  **45th percentile** for his age against Illingworth and well below Randler's 3.30 h peak. Kim 2011
  found a whole national cohort at mean age 17.3 averaging weekday 5.70 h / weekend 8.40 h / catch-up
  2.70 h — our subject's pattern *is* the population mean at his age. His deviance is in **duration**,
  not alignment.
- **Weekend catch-up genuinely delays circadian phase** (~1.7 h in Depner vs ~25 min without it).
  The mechanism behind the harmful position is real even where the metabolic endpoint is shaky.

**Moderate confidence:**

- The **~2 h threshold**, because two independent literatures on different outcomes (depression,
  academics) put the inflection in the same place, which is more than either would carry alone. It
  matters a lot here: the subject's central estimate falls in the **null band**, his long-weekend
  excursions cross out of it.
- The **net verdict that catch-up is mildly protective for this subject**, on the grounds that his
  actual counterfactual is *consistently short* rather than *consistently adequate*.

**Low confidence, and the modeller should inflate uncertainty accordingly:**

- **Any quantitative transport of the experimental effects to this subject.** Every causal estimate
  uses an 8.5–12 h misalignment dose; his is ~1.75 h, a factor of 5–7 smaller. Morris 2015 is the
  sobering calibration: a **full 12 h behavioural inversion moved postprandial glucose only 6%**,
  less than ordinary meal-timing variation (17%).
- **Everything resting on self-reported timing**, i.e. nearly the whole observational base. Hasler
  2025 reports that in high-school students self-report proxies *"for circadian timing were poor
  approximations of biological circadian phase."*
- **The adiposity column specifically.** It is contested in a way the others are not: Bouman 2023 is
  **null for every clinical endpoint**; in children the signal **does not survive quality
  adjustment** (Zhou 2026); the only prospective adolescent study is **null in boys** (Jiang 2024),
  and our subject is male; and Park & Kim 2023 finds the catch-up coefficient **flips sign** under
  individual fixed effects, with 62% of the cross-sectional association being confounding. A
  recurring sex pattern (Conway 2023, Díaz-Morales 2015, Jiang 2024 all female-specific) attenuates
  his expected effect further.

**How much of this is actually poolable — read this before meta-analysing.** Of the 111 effects:

| | count | pooler action |
|---|---|---|
| Point estimate **with** an SE | **42** | poolable as-is |
| Real point estimate, **no derivable SE** | **32** | usable with an imputed or elicited SE; `notes` says why none was derivable |
| **`value: 0.0` with `se: null`** | **37** | **must NOT be pooled — these are not null effects** |

That last row is the one that can do damage. Where a paper's finding is a threshold, a
direction-only statement, a qualitative synthesis, or a contrast the authors never tested, the schema
still demands a numeric `value`, so I encoded the pattern as `0.0` with `se: null` and put the actual
content in `direction_note` and `quote`. Examples: Sánchez-Charcopa's >2 h academic threshold,
Depner's untested weekend-recovery-versus-restriction contrast, Åkerstedt's figure-only
short-weekday/long-weekend cell, Wittmann's construct definition, Roenneberg's formula. **Filtering on
`se != null` before pooling is sufficient to exclude all 37**, and is what I would recommend.

---

## The single biggest gap in my domain

**There is no measured dose–response function for circadian misalignment between roughly 1 and 3
hours — precisely the range every real adolescent, including our subject, actually occupies.**

The causal literature is built at **8.5–12 h** of imposed misalignment (Leproult 8.5 h; Scheer,
Buxton and Morris 12 h inversions). The observational literature covers 1–3 h but cannot separate
timing from duration, because **SJL = (weekend bedtime delay) + (weekend oversleep)/2** is partly a
duration measure by construction — the originators concede it: *"SJL is also positively associated
with perceived sleep debt, making it difficult to disentangle pure sleep timing effects and those of
sleep deprivation."* So the clean evidence is at a dose 5–7× too high, and the on-dose evidence is
not clean.

Everything the modeller most wants to know depends on the shape of that unmeasured curve. If harm is
roughly linear in misalignment, 1.75 h of SJL carries maybe a fifth of Leproult's effect. If there is
a threshold near 2 h — which both the depression and academic literatures independently suggest — the
subject's habitual exposure is close to harmless and only his occasional 10–11 h weekends matter.
Those two readings imply materially different conclusions, **and no study I found can distinguish
them.** This is the dominant uncertainty in my shard, larger than any measurement or confounding
concern.

Three smaller gaps, each individually closable and each currently forcing a judgement call:

- **A between-group test of weekend recovery versus continuous restriction.** Depner's arms were
  never compared, so the entire harmful-metabolic position rests on an untested difference.
- **Åkerstedt's Figure 4 numeric cell** for short weekdays plus long weekends — the exact pattern at
  issue, currently available only as a stated null.
- **Roenneberg 2012's Table S1B and its 2013 Erratum**, which together hold the per-hour SJL→BMI
  coefficient the brief asked for.

---

## Files produced

`jetlag_summary.md` (the required synthesis: subject's SJL with arithmetic and range, normative
placement, duration-adjusted independent effect, outcome-by-outcome catch-up verdict with per-domain
modifiers) · `screening_log.md` (81 records, every exclusion reasoned) · `station_report.md` (this
file) · 41 study records `<study_id>.yaml`.
