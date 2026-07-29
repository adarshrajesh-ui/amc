# Screening log — shard `s16_social_jetlag`

Domain: circadian misalignment as an exposure **separate from** sleep duration; weekend catch-up
sleep as an effect modifier; adolescent circadian phase delay.

**Records screened: 81. Included: 41. Excluded: 40** (20 excluded with a specific
domain/redundancy reason in the table below; 20 further records logged at the end as clearly
off-domain for this shard).

Every identifier in the INCLUDED set was verified programmatically against **both** Crossref
(`api.crossref.org/works/<DOI>`) and PubMed (`esummary.fcgi`), and the DOI returned by PubMed was
checked for equality with the DOI I recorded. Script: reproduced in `station_report.md`.
Result: **42/42 identifier checks passed, 0 Crossref failures, 0 PubMed failures, 0 DOI mismatches.**
(42 checks for 41 records: `roenneberg2012` contributes both its own DOI and its 2013 Erratum DOI.)

Search strategy: 14 PubMed `esearch` queries plus 6 Europe PMC queries across the seven required
sub-topics, then citation-chasing from `roenneberg2019` (which supplied the age-normative reference
`randler2019`) and from the reference lists of the four meta-analyses.

---

## Included (41)

| # | Identifier | Study | Tier | Why included |
|---|---|---|---|---|
| 1 | PMID 16687322 / 10.1080/07420520500545979 | Wittmann 2006, Chronobiol Int | TX | Originating definition of social jetlag. **Construct only — no numeric age norms extractable, paywalled.** |
| 2 | PMID 31336976 / 10.3390/biology8030054 | Roenneberg 2019, Biology | TX | Formal SJL equation; authors' own critique; states SJL peaks in adolescence; phase moves ~45 min in 2 days. |
| 3 | PMID 30921684 / 10.1016/j.sleep.2019.01.023 | Randler 2019, Sleep Med | TX | **Primary age-specific norm: SJL peaks at 3:18 h at age 16, n=18,323.** |
| 4 | PMID 39760865 / 10.1080/07420528.2024.2444675 | Illingworth 2025, Chronobiol Int | TX | **Second age norm with a usable SD: mean 1:53 h (SD 1:07), peak 2:07 h at 15, n=19,760.** |
| 5 | PMID 39532610 / 10.1016/j.sleh.2024.10.001 | Martins 2025, Sleep Health | TX | Base rate: >80% of adolescents have SJL ≥1 h; highest at 16–17 y. n=64,029. |
| 6 | PMID 22578422 / 10.1016/j.cub.2012.03.038 | Roenneberg 2012, Curr Biol | TX | The requested SJL–BMI paper. OR 3.300 (2.512–4.334). **Effect confined to BMI≥25 subgroup.** |
| 7 | PMID 38072635 / 10.1111/obr.13664 | Arab 2024, Obes Rev | TX | Largest SJL–adiposity meta-analysis (43 studies, n=231,648). |
| 8 | PMID 36351658 / 10.1111/jsr.13770 | Bouman 2023, J Sleep Res | TX | 68-study meta-analysis of MetS/T2D parameters; **null for clinical endpoints.** |
| 9 | PMID 41241628 / 10.1016/j.numecd.2025.104420 | Zhou 2026, Nutr Metab Cardiovasc Dis | TX | **Age-matched** adiposity meta-analysis (children/adolescents, n=197,873). |
| 10 | PMID 28631524 / 10.1177/0748730417713572 | Koopman 2017, J Biol Rhythms | TX | New Hoorn. Duration- and BMI-adjusted; dose-response; age modification. |
| 11 | PMID 26580236 / 10.1210/jc.2015-2923 | Wong 2015, JCEM | TX | **Actigraphic** SJL, adjusted for sleep duration AND sleep debt. |
| 12 | PMID 25601363 / 10.1038/ijo.2014.201 | Parsons 2015, Int J Obes | TX | Dunedin; clinically assessed outcomes; **SJL orthogonal to duration (r=−0.04).** |
| 13 | PMID 38991425 / 10.1016/j.sleep.2024.07.001 | Jiang 2024, Sleep Med | T5 | Only prospective adolescent SJL–adiposity study. **Null in boys.** |
| 14 | PMID 41550113 / 10.1155/da/5542425 | Lu 2026, Depress Anxiety | TX | Age-matched depression/anxiety meta-analysis (14 studies, n=164,529). |
| 15 | PMID 40597088 / 10.1186/s12888-025-07066-x | Sun 2025, BMC Psychiatry | TX | **Supplies the ~2 h depression threshold**; 1–2 h SJL null. |
| 16 | PMID 42480409 / 10.1016/j.smrv.2026.102345 | Ravenhall 2026, Sleep Med Rev | TX | Largest SJL–anxiety meta-analysis in adolescents (n=235,526). |
| 17 | PMID 31387413 / 10.1080/07420528.2019.1636813 | Henderson 2019, Chronobiol Int | TX | Provenance only; superseded by #14–16. **No numbers extracted.** |
| 18 | PMID 42470595 / 10.1007/s00431-026-07250-5 | Sánchez-Charcopa 2026, Eur J Pediatr | TX | **Best per-hour, duration-adjusted academic effect: GPA OR 0.76 (0.68–0.85).** |
| 19 | PMID 24491157 / 10.3109/07420528.2013.879164 | Haraszti 2014, Chronobiol Int | TX | Timing-over-duration dissociation; term vs exam period. **Direction only.** |
| 20 | PMID 26061587 / 10.3109/07420528.2015.1041599 | Díaz-Morales 2015, Chronobiol Int | TX | Replicates the duration/timing dissociation. **Direction only, access restricted.** |
| 21 | PMID 24458353 / 10.2337/db13-1546 | Leproult 2014, Diabetes | **T1** | **THE key causal study: duration equated to 3 min, timing varied. g=−1.23 (men).** |
| 22 | PMID 19255424 / 10.1073/pnas.0808180106 | Scheer 2009, PNAS | T1 | Forced desynchrony; misalignment alone worsens glucose, leptin, MAP. |
| 23 | PMID 22496545 / 10.1126/scitranslmed.3003200 | Buxton 2012, Sci Transl Med | T1 | 5-week protocol; **cannot separate restriction from disruption**; recovery normalised at 9 d. |
| 24 | PMID 25870289 / 10.1073/pnas.1418955112 | Morris 2015, PNAS | T1 | **Calibration: misalignment +6% glucose vs endogenous evening +17%.** |
| 25 | PMID 33729109 / 10.1017/S0033291721000787 | Hasler 2022, Psychol Med | **T1** | **Only experimental misalignment study in adolescents**; school-year vs summer schedule. |
| 26 | PMID 30827911 / 10.1016/j.cub.2019.01.069 | Depner 2019, Curr Biol | **T1** | The "catch-up is harmful" anchor. −13% (SR) vs −27% (WR); DLMO delayed 1.7 h. |
| 27 | PMID 29790200 / 10.1111/jsr.12712 | Åkerstedt 2019, J Sleep Res | T5 | The "catch-up is protective" anchor. SS HR 1.65; **short-weekday/long-weekend null.** |
| 28 | PMID 41192734 / 10.1016/j.jad.2025.120613 | Carbone 2026, J Affect Disord | TX | **Exactly age-matched (16–24)**; WCS → 41% lower odds of daily depressive symptoms. |
| 29 | PMID 42023681 / 10.1093/sleep/zsag113 | Kim & Casement 2026, Sleep | TX | **U-shape with Fitbit sleep**; moderate WCS ≤2 h → anxiety OR 0.49. |
| 30 | PMID 35715557 / 10.1038/s41598-022-14352-1 | Lee 2022, Sci Rep | TX | n=270,619 adolescents; **CUS ratio ≥1.50 harmful, <1.00 worst.** |
| 31 | PMID 40366483 / 10.1007/s11325-025-03349-5 | Lee 2025, Sleep Breath | TX | Age-matched; CUS ≥3 h → overweight/obesity OR 0.67 (0.57–0.80). |
| 32 | PMID 37565249 / 10.3389/fped.2023.1213558 | Choi 2023, Front Pediatr | TX | KNHANES adolescents, **measured** anthropometry; <6 h weekday + <3 h CUS → RR 1.93. |
| 33 | PMID 36521277 / 10.1016/j.puhe.2022.11.008 | Park & Kim 2023, Public Health | **T5** | **Decisive: individual fixed effects REVERSE the sign of the catch-up coefficient.** |
| 34 | PMID 21893646 / 10.1001/archpediatrics.2011.128 | Kim 2011, Arch Pediatr Adolesc Med | TX | **Closest population match to our subject** (weekday 5.70 h, weekend 8.40 h, age 17.3). |
| 35 | PMID 24267542 / 10.1016/j.comppsych.2013.08.023 | Kang 2014, Compr Psychiatry | TX | Harmful column: WCUS → suicide attempts/self-injury. **Direction only.** |
| 36 | PMID 33069999 / 10.1016/j.sleep.2020.09.025 | Kim DJ 2020, Sleep Med | TX | Protective metabolic counterweight to Depner, in chronic short sleepers. |
| 37 | PMID 32431530 / 10.2147/DMSO.S247898 | Son 2020, DMSO | TX | **Placeholder; identifiers verified, abstract not retrieved, no numbers extracted.** |
| 38 | PMID 25380248 / 10.1371/journal.pone.0112199 | Crowley 2014, PLoS One | **T4** | **Authoritative phase delay: ~1 h DLMO delay between ages 17 and 19.** |
| 39 | PMID 8506460 / 10.1093/sleep/16.3.258 | Carskadon 1993, Sleep | TX | Origin of the puberty claim. **Girls only; no numbers; provenance.** |
| 40 | PMID 17383934 / 10.1016/j.sleep.2006.12.002 | Crowley 2007, Sleep Med | TX | Two-process framework; normal delay vs DSPS continuum. Context. |
| 41 | PMID 39901722 / 10.1093/sleep/zsaf031 | Hasler 2025, Sleep | T4 | **Self-report proxies poorly approximate measured phase** — exposure-misclassification caution. |

Also verified as an identifier (not a standalone record): **10.1016/j.cub.2013.04.011** — the formal
Erratum to Roenneberg 2012 (Crossref `update-to` confirms it). Content **not retrievable**; flagged in
`roenneberg2012.yaml`.

---

## Excluded with a specific reason (20)

| # | Identifier | Study | Exclusion reason |
|---|---|---|---|
| E1 | PMID 20025436 / 10.3109/10826080903498952 | Wittmann 2010, Subst Use Misuse | Outcome is smoking/alcohol via chronotype, not a metabolic/psychiatric/academic endpoint in scope; superseded by wittmann2006 for the construct. |
| E2 | PMID 36479212 / 10.3389/fendo.2022.1008820 | Zhang 2022, Front Endocrinol | Redundant with Bouman 2023, which is larger (68 vs fewer studies), newer, and quality-stratified on the same question. Excluded to avoid double-counting overlapping primary studies. |
| E3 | PMID 34059916 / 10.1093/sleep/zsab136 | Depner 2021, Sleep | Same laboratory protocol and same participants as depner2019; outcome is energy balance. Would double-count the T1 evidence. |
| E4 | PMID 28636610 / 10.1371/journal.pone.0178782 | Fischer 2017, PLoS One | Retrieved in full text and searched: reports US chronotype by age but **no numeric SJL distribution** (only 3 passing mentions of "social jetlag"). No extractable norm. |
| E5 | PMID 34781787 / 10.1080/07420528.2021.2002889 | Fischer 2022, Chronobiol Int | Exposure is longitude within a time zone, not social jetlag; belongs to a time-zone IV shard, not here. |
| E6 | PMID 17936039 / 10.1016/j.smrv.2007.07.005 | Roenneberg 2007, Sleep Med Rev | Superseded by roenneberg2019 (same group, same material, plus self-critique). |
| E7 | PMID 37087961 / 10.1016/j.sleep.2023.04.005 | Hrozanova 2023, Sleep Med | Descriptive sex differences in teen SJL; not open access and adds no norm beyond randler2019/illingworth2025, which are 2 orders of magnitude larger. |
| E8 | PMID 37697814 / 10.1111/jsr.14042 | Tamura 2024, J Sleep Res | Longitudinal course of SJL itself (exposure trajectory), not an SJL→outcome effect. |
| E9 | PMID 37814409 / 10.1080/07420528.2023.2265480 | Conway 2023, Chronobiol Int | Title states the effect holds **for adolescent females but not males**; our subject is male, so it contributes no usable estimate. |
| E10 | PMID 36610292 / 10.1016/j.dcn.2022.101193 | Guldner 2023, Dev Cogn Neurosci | White-matter/internalizing outcome via catch-up sleep; brain-structure domain is another shard's, and n is small. |
| E11 | PMID 33901928 / 10.1016/j.sleep.2021.03.009 | Wang 2021, Sleep Med | Exposure is general "sleep situations", not separable SJL or catch-up. |
| E12 | PMID 32391631 / 10.1111/jsr.13063 | Koo 2021, J Sleep Res | Redundant with lee2022 (same country, same question, n=270,619 vs far smaller). |
| E13 | PMID 27822941 / 10.3346/jkms.2016.31.12.1996 | Lee BH 2016, J Korean Med Sci | Exposure is sleep duration only; no catch-up or SJL contrast. Belongs to the duration shards. |
| E14 | PMID 38137786 / 10.3390/jcm12247716 | Kang 2023, J Clin Med | Population restricted to adolescents with atopic dermatitis; not transportable. |
| E15 | PMID 37046112 / 10.1007/s11325-023-02826-z | Lee K 2023, Sleep Breath | Korean **adults**; redundant with kimdj2020/son2020 on the same KNHANES-family question and would inflate apparent independent evidence. |
| E16 | PMID 42226891 / 10.2147/nss.s603131 | Gong 2026, Nat Sci Sleep | Outcome is gut microbiome; no domain in the schema and not decision-relevant. |
| E17 | PMID 40927700 / 10.2147/nss.s551300 | Luo 2025, Nat Sci Sleep | Outcome is dry eye disease; out of scope. |
| E18 | PMID 39854155 / 10.1002/ajhb.70000 | Miño 2025, Am J Hum Biol | Outcome is physical fitness; out of scope, and same EHDLA cohort as the included sanchezcharcopa2026 (would double-count). |
| E19 | PMID 42205405 / 10.4103/jehp.jehp_1662_25 | Phong 2026, J Educ Health Promot | Self-described "brief report" of prevalence in medical students; no usable effect estimate. |
| E20 | PMID 10025716 / 10.1016/s0304-3940(98)00971-9 | Carskadon 1999, Neurosci Lett | Reports intrinsic circadian **period** (tau) in adolescents, not phase delay magnitude; n=5-ish and does not answer the phase-delay question crowley2014 answers directly. |

## Excluded as clearly off-domain (20)

Inspected via title/abstract during searching and not carried forward. Reasons in brackets.

PMID 41878934 [chronotype distribution, Yemen — no SJL effect] · 39956356 [chronobiology review,
Río de la Plata] · 38759704 [rodent adolescent circadian disruption] · 37039532 [pandemic alcohol
use outcome] · 35581310 [chronotype development vs school timing, exposure not SJL] ·
34923707 [teachers' school-start-time preferences] · 28880049 [type 1 diabetes glycaemic control] ·
28651468 [bright-light phase response curves — intervention physiology, not exposure] ·
32361995 [DNA methylation] · 21302851 [general adolescent sleep physiology review, no effects] ·
15251897 [Carskadon 2004 review, superseded by crowley2007/crowley2014] ·
16120098 [sleep tendency during extended wakefulness — homeostatic, not misalignment] ·
29045623 [olfactory sensitivity] · 42049585 [corrigendum notice only] ·
41075475 [Singapore education-system comparison, descriptive] · 41165042 [mediation analysis of
self-control/sleep quality, not a direct SJL→outcome estimate] · 38249148 [Indian school SJL
prevalence, adds no norm beyond the two far larger anchors] · 39203711 [EHDLA obesity outcomes —
same cohort as included sanchezcharcopa2026, would double-count] · 38846590 [sex differences in
attention, small, superseded by kim2011] · 42193513 [sleep *quality* and academic performance —
exposure is not misalignment].
