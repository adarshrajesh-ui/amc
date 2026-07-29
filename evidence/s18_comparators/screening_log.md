# Screening log — shard `s18_comparators`

Domain: calibration anchors. Comparator lifestyle exposures on a life-expectancy /
QALY scale, expressible per unit of exposure so that 3 years of one thing can be
compared with 3 years of another.

**Records screened: 74. Included: 29. Excluded: 45.** (Gate G1 requires ≥ 25.)

Retrieval was entirely programmatic. Search: PubMed E-utilities `esearch`, then
`esummary` for titles/journals/DOIs, then `efetch` (XML) for abstracts. Verification:
`https://api.crossref.org/works/<DOI>` and
`https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=<PMID>`.
The verification run is reproducible and its raw output is in `verification_s18.json`.
Two non-PubMed sources (RAND RR-1791, Jackson 2025 *Addiction*) were retrieved from the
publisher directly.

Every record below was screened on at least its title, journal and year as returned by a
live API call. "abstract" in the Screened-on column means the full abstract was retrieved
and read; "metadata" means title/journal/year/DOI only, which was sufficient to exclude.

---

## Included (29)

| # | ID | Study | Screened on | Comparator | Why included |
|---|---|---|---|---|---|
| 1 | PMID 15213107 | Doll 2004, *BMJ* | abstract | smoking | The canonical anchor. 10 y LE lost for continuing smokers; cessation at 60/50/40/30 gains 3/6/9/10 y. |
| 2 | PMID 23343063 | Jha 2013, *NEJM* | abstract | smoking | HR 2.8 (men, 99% CI 2.4-3.1); >10 y LE lost; quitting at 25-34 gains ~10 y; cessation before 40 removes ~90% of the excess risk. The task's key comparison. |
| 3 | PMID 25857449 | Banks 2015, *BMC Med* | abstract | smoking | Supplies the DOSE gradient Doll's abstract lacks (~2x at ≤14/day, ~4x at ≥25/day); third independent 10-y figure; quitting before 45 indistinguishable from never-smokers. |
| 4 | PMID 23107252 | Pirie 2013, *Lancet* | abstract | smoking | Strongest reversibility datum in the shard: quitting at 25-34 leaves all-cause RR 1.05 (1.00-1.11); stopping before 30 avoids >97% of the excess. 11-y lifespan gap. |
| 5 | PMID 10617536 | Shaw 2000, *BMJ* | title (body paywalled) | smoking | Origin of the minutes-per-cigarette figure (11 min). `access_tier: secondhand`; the number is in the verbatim title, the assumptions are quoted from Jackson 2025. |
| 6 | DOI 10.1111/add.16757 | Jackson 2025, *Addiction* | full text (UCL PDF) | smoking | **The only per-unit-exposure LE estimate for any comparator.** 17 min/cigarette for men; 50 days of life per year at 10 cig/day. Not in PubMed; Crossref-verified. |
| 7 | PMID 38155620 | Zuhal 2023, *Nagoya J Med Sci* | abstract | smoking | Only record crossing AGE AT INITIATION with AGE AT CESSATION. Initiation <20 with cessation ≥50 → HR 1.51; cessation <50 → negligible all-cause excess regardless of initiation age. DOI is JaLC-registered so Crossref 404s; doi.org resolves HTTP 200. |
| 8 | PMID 19299006 | Prospective Studies Collaboration 2009, *Lancet* | abstract | BMI | HR 1.29 (1.27-1.32) per +5 kg/m²; 2-4 y lost at BMI 30-35, 8-10 y at 40-45. |
| 9 | PMID 27423262 | Global BMI Mortality Collaboration 2016, *Lancet* | abstract | BMI | Best confounding control (never-smokers, no chronic disease, 5-y lag). Category HRs; HR per 5 kg/m² larger in men (1.51) and when measured younger (1.52 at 35-49) — favourable for transport to age 18. |
| 10 | PMID 12517229 | Fontaine 2003, *JAMA* | abstract | BMI | The requested age-specific YLL. Max 13 y for white men aged **20-30** at BMI >45; younger adults have greater YLL at any given degree of overweight. |
| 11 | PMID 12513041 | Peeters 2003, *Ann Intern Med* | abstract | BMI | 3.1 y lost from overweight and 5.8 y from obesity for 40-y-old male nonsmokers — my primary BMI pro-rata input. Also the only retrievable evidence that early-adult BMI predicts later mortality after adjusting for later BMI. |
| 12 | PMID 27074389 | Twig 2016, *NEJM* | abstract | BMI | Exposure MEASURED at mean age 17.3 in 2.3 million adolescents (`adolescent_match: exact_16_19`). HR 3.5 for CV death, rising to 4.1 at 30-40 y follow-up. Bounds the irreversible-adolescent-insult story. |
| 13 | PMID 28719691 | Zheng 2017, *JAMA* | abstract | BMI | Weight gain from age 18/21 to 55 and healthy aging. Evidence that adolescent adiposity is the start of a trajectory, not a closed window. Low weight (no LE figure). |
| 14 | PMID 22818936 | Lee 2012, *Lancet* | abstract | inactivity | Requested. 9% PAF for premature mortality; +0.68 y (0.41-0.95) population LE if inactivity eliminated. Included with an explicit warning that this is NOT an individual effect. |
| 15 | PMID 23139642 | Moore 2012, *PLoS Med* | abstract | inactivity | The individual-level LE anchor: +1.8 / +3.4 / +4.5 y after age 40 across activity levels. Primary inactivity pro-rata input. |
| 16 | PMID 31434697 | Ekelund 2019, *BMJ* | abstract | inactivity | Requested. Best device-measured dose-response (HR 0.27 top vs bottom quartile) but retained as an OUTLIER/upper bound only — mean age 62.6, 5.8 y follow-up, heavy reverse causation. |
| 17 | PMID 22777603 | Katzmarzyk & Lee 2012, *BMJ Open* | abstract | inactivity | Sedentary limb (+2.00 y from cutting sitting below 3 h/day), relevant to a screen-heavy student. Population counterfactual; low weight. |
| 18 | PMID 26686843 | Högström 2016, *Int J Epidemiol* | abstract | inactivity | **Best age match in the shard.** Cycle-ergometer fitness at mean age 18 in 1,317,713 Swedish conscripts, 29 y follow-up, HR 0.49 (0.47-0.51). |
| 19 | PMID 31243014 | Mok 2019, *BMJ* | abstract | inactivity | Reversibility: HR 0.76 (0.71-0.82) per +1 kJ/kg/day/y rise in activity, adjusted for baseline; increasing trajectories beat consistent inactivity from any baseline. |
| 20 | PMID 29676281 | Wood 2018, *Lancet* | abstract | alcohol | Requested. Years of life lost at age 40 by drinking category (~6 mo / 1-2 y / 4-5 y). Intake corrected for long-term variability using 152,640 repeat assessments. |
| 21 | PMID 30146330 | GBD 2016 Alcohol Collaborators, *Lancet* | abstract | alcohol | The age-band-matched datum: alcohol is the LEADING risk factor for male deaths at 15-49 (PAF 12.2%, 10.8-13.6) via road injury and self-harm. Changes the shape of the alcohol comparator entirely. |
| 22 | PMID 30954305 | GBD 2017 Diet Collaborators, *Lancet* | abstract | diet | Requested. 11 M deaths and 255 M DALYs attributable to dietary risks. Only DALY-denominated figures in the shard. Cannot be converted per-exposure. |
| 23 | PMID 35134067 | Fadnes 2022, *PLoS Med* | abstract | diet | Requested. +13.0 y (9.4-14.3) for US men switching at age 20; **and the age gradient (8.8 y at 60, 3.4 y at 80) that supplies my delayed-cessation conversion.** |
| 24 | PMID 38692410 | Fadnes 2024, *Am J Clin Nutr* | abstract | diet | Updated model adjusted for height, weight and physical activity: +9.7 y (8.1-11.3) US men at 40. Partial check that the 2022 headline was not driven by adiposity/activity confounding. Same `cohort_family` — not independent. |
| 25 | PMID 28983434 / DOI 10.7249/RR1791 | Hafner 2016, RAND RR-1791 | abstract + publisher key-findings page | sleep | Requested. Documents that the leading attempt to price insufficient sleep yields **GDP and working days, not life expectancy or QALYs**, and that its only health input is a borrowed mortality RR. |
| 26 | PMID 37831896 | Li H 2024, *QJM* | abstract | sleep | Closest thing to a genuine sleep life-expectancy figure: +4.7 y (2.7-6.7) at age 30 for men, 5 vs 0-1 low-risk sleep factors; all-cause HR 0.70. |
| 27 | PMID 20469800 | Cappuccio 2010, *Sleep* | abstract | sleep | Puts our own exposure on the comparator HR scale (short-sleep RR 1.12) and identifies the source of RAND's borrowed RR. Long-sleep RR 1.30 recorded as the reverse-causation warning. |
| 28 | PMID 42170608 | Welter 2026, *Int J Public Health* | full text | sleep | Documents the NEGATIVE finding: sleep is in the GBD hierarchy neither as a disorder nor as a risk factor, so no GBD sleep DALY figure exists to quote. |
| 29 | PMID 29712712 | Li Y 2018, *Circulation* | abstract | joint | Internal consistency check: all five comparator behaviours combined cap at +12.2 y (10.1-14.2) at age 50 for men, and its own life-table answer is ~20% below what `10.85·ln(HR)` predicts from its own HR — corroborating my 0.80 calibration factor. |

---

## Excluded (45)

| # | ID | Study | Screened on | Exclusion reason |
|---|---|---|---|---|
| 30 | PMID 15668706 | Doll 2005, *Br J Cancer*, cancer mortality in British doctors | metadata | Cause-specific (cancer only); no life-expectancy figure. Superseded for our purpose by the all-cause Doll 2004. |
| 31 | PMID 23343064 | Thun 2013, *NEJM*, 50-year trends in smoking-related mortality | metadata | Reports secular trends in smoking-attributable mortality, not LE per unit exposure. Redundant with Jha 2013, same issue of *NEJM*, overlapping US data. |
| 32 | PMID 27682045 | Twig 2016, *NEJM* correspondence | metadata | Correspondence on PMID 27074389, which is included. Would double-count. |
| 33 | PMID 29871640 | Furer 2018, *Cardiovasc Diabetol*, sex-specific adolescent BMI categories | metadata | Sex-stratified re-analysis of the same Israeli conscript cohort as Twig 2016; same `cohort_family`, would violate gate G6. |
| 34 | PMID 30518353 | Twig 2018, *Cardiovasc Diabetol*, adolescent cognitive function | metadata | Exposure is cognitive function, not a modifiable lifestyle comparator. Out of shard scope. |
| 35 | PMID 35333861 | Fadnes 2022 correction notice, *PLoS Med* | metadata | Correction to PMID 35134067, which is included. |
| 36 | PMID 30392731 | GBD 2016 Alcohol and Drug Use, *Lancet Psychiatry* | metadata | Overlaps GBD 2016 Alcohol (included); illicit drug use is outside the comparator set. |
| 37 | PMID 33069327 | GBD 2019 Risk Factors Collaborators, *Lancet* | abstract | Aggregate DALY/death counts for 87 risk factors. No per-person, per-exposure-year figure and no life-expectancy decomposition, so not convertible to a 3-year exposure. |
| 38 | PMID 41092926 | GBD 2023 Diseases/Injuries/Risk Factors, *Lancet* | metadata | Same reason as #37, plus far too broad. |
| 39 | PMID 41092927 | GBD 2023 Demographics, *Lancet* | metadata | National life expectancy estimates. The pipeline already uses a G10-calibrated NCHS US male life table (`s17_baseline_risk`); a second source would create an inconsistency. |
| 40 | PMID 41092928 | GBD 2023 Causes of Death, *Lancet* | metadata | Cause-of-death counts, not exposure effects. |
| 41 | PMID 31648977 | GBD 2017 Colorectal Cancer, *Lancet Gastroenterol Hepatol* | metadata | Cause-specific. |
| 42 | PMID 41015051 | GBD 2023 Cancer, *Lancet* | metadata | Cause-specific. |
| 43 | PMID 42476159 | GBD 2023 Road Injuries, *Lancet Public Health* | metadata | Injury burden by cause, not by alcohol exposure level. Would have been useful for the alcohol window term but does not stratify by individual drinking. |
| 44 | PMID 42167272 | GBD 2023 Mental Disorders, *Lancet* | metadata | Search false positive; out of scope. |
| 45 | PMID 41785894 | GBD 2023 Breast Cancer, *Lancet Oncol* | metadata | Cause-specific and female-only. |
| 46 | PMID 41386261 | GBD 2023 Intimate Partner/Sexual Violence, *Lancet* | metadata | Search false positive; out of scope. |
| 47 | PMID 21160056 | Roger 2011, *Circulation*, AHA heart disease and stroke statistics 2011 | metadata | Descriptive statistics compendium; no exposure effect estimates. |
| 48 | PMID 41534147 | Lo 2026, *Public Health*, lifetime productivity loss from smoking in Taiwan | metadata | Outcome is productivity, not life expectancy or QALYs; Taiwan-specific. |
| 49 | PMID 15923452 | Yang 2005, *Tob Control*, smoking-attributable expenditures and YPLL in Taiwan | metadata | Population years of potential life lost, not per-unit-exposure LE. |
| 50 | PMID 34861866 | Souto 2021, *BMC Oral Health*, cessation cost-effectiveness for tooth loss | metadata | Outcome irrelevant. |
| 51 | PMID 39556676 | Sylvia 2022, PCORI report | metadata | Not a comparator study; search false positive with no title in the PubMed record. |
| 52 | PMID 23382654 | Banks 2013, *PLoS Med*, erectile dysfunction severity | metadata | Search false positive (author-name collision with Banks 2015). |
| 53 | DOI 10.1016/j.amepre.2020.11.003 | Zhu 2021, *Am J Prev Med*, smoking and cessation with overall and cause-specific mortality | metadata (Crossref) | Redundant: a fifth smoking-cessation gradient adds nothing beyond Doll 2004, Jha 2013, Pirie 2013 and Zuhal 2023, which already span the UK, US and Japan. |
| 54 | PMID 41740083 | Ahn 2026, *Neurology*, dynamic smoking patterns and Parkinson disease | metadata | Primary outcome is Parkinson disease; competing-risk design not convertible to LE. |
| 55 | PMID 39815190 | Yin 2025, *BMC Cancer*, cessation and lung cancer | metadata | Cause-specific (lung cancer). |
| 56 | PMID 39402526 | Aryannezhad 2024, *BMC Med*, activity and diet changes, EPIC-Norfolk | metadata | Same cohort (`EPIC_Norfolk`) as Mok 2019, which is included; no life-expectancy figure. Gate G6. |
| 57 | PMID 31401610 | Yang 2019, *BMJ Open*, adult BMI trajectories, Melbourne Collaborative Cohort | metadata | Trajectory categories cannot be converted to a per-exposure-year figure; no LE output. |
| 58 | PMID 33957617 | Lee 2021, *Am J Nephrol*, sleep duration, mortality and QoL in chronic kidney disease | metadata | Disease-specific population (CKD); the QoL component is not a QALY estimate. Best candidate returned by the sleep-QALY search, and its inadequacy is the basis for the negative finding in `comparator_scale.md` §3.6. |
| 59 | PMID 39896296 | Javadi Arjmand 2025, *Curr Dev Nutr*, Nordic Nutrition Recommendations LE | metadata | Same Fadnes modelling family and Nordic/Baltic populations; would double-count `GBD_Food4HealthyLife`. |
| 60 | PMID 39956388 | Onni 2025, *Adv Nutr*, umbrella review of food groups and all-cause mortality | metadata | Relative risks only, no life-expectancy conversion, and it largely overlaps the meta-analytic inputs Fadnes already uses. |
| 61 | PMID 40591623 | De Matteu Monteiro 2025, *PLoS One*, health impact assessment of food regulations | metadata | Policy-level regulatory impact assessment; not an individual exposure effect. |
| 62 | PMID 40338834 | Ballin 2025, *PLoS Med*, adolescent cardiorespiratory fitness and cancer | metadata | Cause-specific (cancer) and same Swedish conscript `cohort_family` as Högström 2016. |
| 63 | PMID 39006434 | Ballin 2024, *medRxiv* | metadata | Preprint of PMID 40338834. |
| 64 | PMID 34226237 | Af Geijerstam 2021, *BMJ Open*, fitness/strength and COVID-19 severity | metadata | Outcome irrelevant; same conscript cohort family. |
| 65 | PMID 32856610 | Crump 2020, *Cancer Epidemiol Biomarkers Prev*, early-life fitness and prostate cancer | metadata | Cause-specific; same conscript cohort family. |
| 66 | PMID 29579585 | Lindgren 2018, *Int J Cardiol*, resting heart rate in late adolescence | metadata | Exposure is a physiological trait, not a modifiable lifestyle comparator. |
| 67 | PMID 41808934 | Cai 2026, *J Exerc Sci Fit*, 24-h movement behaviours, compositional mediation | metadata | No LE output; restricted to a CVD subpopulation. |
| 68 | PMID 36279884 | Chan 2023, *Int J Cancer*, postdiagnosis body fatness and breast cancer prognosis | metadata | Cancer survivors, female; wrong population and cause-specific. |
| 69 | PMID 29271279 | Borisenko 2018, *J Med Econ*, bariatric surgery cost-effectiveness in Belgium | metadata | Cost-effectiveness in morbid obesity; the exposure contrast is surgical, not a 3-year adolescent lifestyle window. Best candidate from the BMI-reversibility search and its inadequacy is noted as a gap. |
| 70 | PMID 38721870 | Cormick 2024, Cochrane, calcium supplementation in overweight/obesity | metadata | Intervention and outcome both irrelevant; search false positive. |
| 71 | PMID 38710853 | Ryding 2025, *J Cancer Surviv*, dietetic care for cancer survivors | metadata | Wrong population and outcome. |
| 72 | PMID 38495815 | Anazco 2024, *Obes Pillars*, weight-centric prevention of cancer | metadata | Narrative review; cause-specific. |
| 73 | PMID 36389682 | Frede 2022, *Front Immunol*, respiratory infections in spondyloarthritis | metadata | Search false positive; entirely out of scope. |
| 74 | PMID 42098913 | Pleym 2026, *Addiction*, cost-effectiveness of in-hospital cessation counselling | metadata | Intervention cost-effectiveness, not an exposure effect. |

---

## Searches run (PubMed E-utilities `term=`)

Each line is one `esearch` call. Hit counts are for the query as written.

1. `21st-century hazards of smoking and benefits of cessation in the United States` → 1
2. `Tobacco smoking and all-cause mortality in a large Australian cohort study mature epidemic` → 0
3. `Banks smoking all-cause mortality Australian cohort 45 and Up` → 2
4. `cigarette minutes of life lost expectancy per cigarette` → 2
5. `Time for a smoke one cigarette reduces your life by 11 minutes` → 1
6. `loss of life expectancy per cigarette smoked estimate` → 11
7. `Jackson Shahab Brown cigarette minutes life expectancy loss 2024` → 0
8. `smoking one cigarette 20 minutes life expectancy loss England` → 1
9. `Doll Peto mortality in relation to smoking 50 years observations male British doctors` → 2
10. `The 21st century hazards of smoking and benefits of stopping a prospective study of one million women in the UK` → 1
11. `50-year trends in smoking-related mortality in the United States` → 1
12. `smoking cessation before age 40 mortality benefit cohort` → 22
13. `Association of the age at smoking initiation and cessation on all-cause and cause-specific mortality` → 49
14. `Body-mass index and cause-specific mortality in 900000 adults collaborative analyses of 57 prospective studies` → 0
15. `Whitlock body-mass index cause-specific mortality 57 prospective studies` → 1
16. `Body-mass index and all-cause mortality individual-participant-data meta-analysis of 239 prospective studies` → 1
17. `Years of life lost due to obesity Fontaine` → 2
18. `Obesity in adulthood and its consequences for life expectancy a life-table analysis` → 1
19. `Body-Mass Index in 2.3 Million Adolescents and Cardiovascular Death in Adulthood` → 0
20. `Twig body-mass index adolescents cardiovascular death adulthood` → 4
21. `Associations of Weight Gain From Early to Middle Adulthood With Major Health Outcomes Later in Life` → 3
22. `intentional weight loss and mortality meta-analysis randomized trials` → 13
23. `association of weight loss interventions with changes in all-cause mortality meta-analysis randomised` → 28
24. `life expectancy after bariatric surgery Swedish Obese Subjects` → 10
25. `Effect of physical inactivity on major non-communicable diseases worldwide` → 1
26. `Dose-response associations between accelerometry measured physical activity and sedentary time and all cause mortality` → 1
27. `Leisure time physical activity of moderate to vigorous intensity and mortality a large pooled cohort analysis` → 1
28. `Sedentary behaviour and life expectancy in the USA a cause-deleted life table analysis` → 0
29. `Katzmarzyk Lee sedentary behaviour life expectancy cause-deleted life table` → 1
30. `Physical activity trajectories and mortality population based cohort study EPIC-Norfolk` → 1
31. `physical activity trajectories and mortality population based cohort study BMJ 2019` → 2
32. `Aerobic fitness in late adolescence and the risk of early death prospective cohort study 1.3 million Swedish men` → 0
33. `cardiorespiratory fitness late adolescence conscription mortality Swedish men cohort` → 6
34. `Hogstrom aerobic fitness adolescence early death Swedish` → 1
35. `physical fitness at age 18 and mortality conscripts cohort 1 million` → 3
36. `Risk thresholds for alcohol consumption combined analysis of individual-participant data for 599 912 current drinkers` → 1
37. `Alcohol use and burden for 195 countries and territories 1990-2016 systematic analysis` → 2
38. `drinking trajectories from adolescence young adulthood and later mortality cohort` → 0
39. `Health effects of dietary risks in 195 countries 1990-2017 systematic analysis Global Burden of Disease` → 4
40. `Estimating impact of food choices on life expectancy a modeling study` → 20
41. `Fadnes food choices life expectancy modelling` → 2
42. `Fadnes LT life expectancy food groups` → 3
43. `Why Sleep Matters The Economic Costs of Insufficient Sleep cross-country comparative analysis` → 1
44. `low-risk sleep patterns life expectancy at age 30 mortality` → 2
45. `insufficient sleep quality-adjusted life years cost-effectiveness burden` → 0
46. `short sleep duration quality-adjusted life years lost model` → 1
47. `insomnia quality adjusted life year loss burden estimate adolescent` → 0
48. `Sleep duration and all-cause mortality a systematic review and meta-analysis of prospective studies Cappuccio` → 1
49. `sleep should be included global burden of disease risk factor` → 164
50. `Global burden of 87 risk factors in 204 countries and territories 1990-2019 systematic analysis` → 5
51. `Impact of Healthy Lifestyle Factors on Life Expectancies in the US Population` → 21
52. `healthy lifestyle factors life expectancy US population Li Circulation 2018` → 2
53. `smoking duration versus intensity lung cancer risk pack-years Doll Peto model` → 0

Two web searches were used to locate non-PubMed sources: one for the 2024/2025 update to
the minutes-per-cigarette figure (found Jackson 2025, *Addiction*, DOI 10.1111/add.16757,
confirmed against the UCL Discovery PDF) and one to establish whether GBD includes sleep
(found Welter 2026, DOI 10.3389/ijph.2026.1609757, PMID 42170608).

---

## Identifiers that failed verification

| Identifier | What happened | Resolution |
|---|---|---|
| Jackson 2025, *Addiction* — PMID | No PubMed record exists at time of extraction; `esearch` on the exact title returned 0. | `pmid: null`, `pubmed_ok: false`. DOI 10.1111/add.16757 verified against Crossref (title, authors Jackson/Jarvis/West, *Addiction* 120(5):810-812) and full text retrieved from UCL Discovery. Status VERIFIED on the DOI alone. |
| Zuhal 2023 — DOI 10.18999/nagjms.85.4.691 | `api.crossref.org` returns HTTP 404 "Resource not found"; DataCite also 404. | The DOI is registered with JaLC, not Crossref. Verified instead by resolving `https://doi.org/10.18999/nagjms.85.4.691` (HTTP 200 → Nagoya University repository record 2008439) and by PubMed `esummary` on PMID 38155620. `crossref_ok: false`, `pubmed_ok: true`, status VERIFIED. |
| Shaw 2000 — DOI | PubMed holds no DOI for this record (only PMID and PMCID). | DOI 10.1136/bmj.320.7226.53 constructed from the BMJ volume/issue/page pattern and then **verified** against Crossref, which returned the exact title, author Shaw, *BMJ* 320(7226):53-53, 2000-01-01. Not a guess. |
| Doll 2004 — full text | PMC returns metadata only: "The publisher of this article does not allow downloading of the full text in XML form." | `access_tier: abstract_only`. The per-cigarettes-per-day dose table could not be extracted; Banks 2015 supplies the dose gradient instead. |
| Hafner 2016 (RAND RR-1791) — report body | `rand.org` returns HTTP 403 for both the PDF and the read-online page; PMC holds only the abstract for the *Rand Health Q* version. | Figures quoted verbatim from RAND's own publication-page "Key Takeaways". `access_tier: abstract_only`, `secondhand_via` set with the full explanation. DOI 10.7249/RR1791 and PMID 28983434 both verified. |

All other 24 identifiers verified against **both** Crossref and PubMed with matching titles.
Raw output: `verification_s18.json`.
