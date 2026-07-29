"""Build screening_log.md from screened_pmids.txt, the YAML records, and my exclusion reasons.

Generated rather than hand-typed so that every title, journal and year in the log is what
PubMed actually returns, and so the include/exclude split cannot drift from the YAML files.
"""
from __future__ import annotations

import glob
import json
import os
import re
import time
import urllib.request

UA = "sleep-debt-factory/1.0 (research; s12_psychiatric)"
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
HERE = "/workspace/evidence/s12_psychiatric"

# pmid -> (reason category, reason text) for everything I screened and did NOT extract
EXCLUSIONS = {
    "23261135": ("superseded",
                 "Prospective insomnia/depression study in adolescents. Excluded as superseded: "
                 "roberts2014 uses the same design in a larger sample (n=3,134) and reports BOTH "
                 "cross-lagged directions, which is what I needed."),
    "25697832": ("wrong outcome",
                 "Systematic review of social interactions, emotion and sleep. Excluded: outcome is "
                 "social/interpersonal functioning, not depression, anxiety or suicidality, and no "
                 "pooled effect size is reported."),
    "34951014": ("no extractable estimate",
                 "Later school start times and adolescent mental health. Excluded: commentary-style "
                 "analysis with no pooled or adjusted effect estimate I could quote; the same "
                 "exposure is covered quantitatively by sadikova2024, berger2026_start and "
                 "wang2026_dsst."),
    "39608635": ("wrong outcome",
                 "Umbrella review of non-pharmacological interventions for sleep disturbances in "
                 "children/adolescents. Excluded: outcomes are SLEEP parameters, not mood; the mood "
                 "arm of this literature is captured by blake2017, gee2019 and scott2021."),
    "40668370": ("population/exposure mismatch",
                 "CBT-I in school settings meta-analysis. Excluded: intervention targets INSOMNIA, "
                 "which the subject does not have, and it is redundant with freeman2017 and "
                 "scott2021 which report the mood effect sizes directly."),
    "39078226": ("no extractable estimate",
                 "Delayed school start time in a Hong Kong residential high school (n=227, mean age "
                 "17.0 - an excellent age match). Excluded reluctantly: the abstract reports "
                 "direction only ('was associated with improved sleep duration, mental health, and "
                 "life satisfaction') with no coefficient, CI or test statistic, only 83 students "
                 "were reassessed, and it is probably inside the wang2026_dsst pool."),
    "38074253": ("quality",
                 "School start time and adolescent mood/sleep quality. Excluded: small "
                 "single-site cross-sectional survey in a primary-care journal, no adjusted "
                 "estimates."),
    "35970642": ("not primary evidence",
                 "French-language narrative review of adolescent sleepiness. Excluded: narrative "
                 "review, no pooled estimates."),
    "35699363": ("wrong outcome",
                 "US national survey of adolescent sleep duration, timing and social jetlag during "
                 "COVID-19. Excluded: purely descriptive exposure prevalence with no psychiatric "
                 "outcome. Social jetlag as an exposure is covered by lu2026_sjl."),
    "40354717": ("wrong population",
                 "Sleep bruxism and internalizing symptoms in PRESCHOOLERS. Excluded: age 3-5, "
                 "exposure is bruxism."),
    "41138251": ("wrong outcome",
                 "Weight-loss behaviours and sleep, Growing Up in Ireland. Excluded: outcome is "
                 "disordered eating, not depression/anxiety/suicidality."),
    "30395300": ("wrong exposure",
                 "Long-time mobile phone use, sleep disturbance and mental distress in technical "
                 "college students. Excluded: exposure is phone use; sleep is a mediator, not the "
                 "exposure, so no sleep-dose contrast is recoverable."),
    "26683236": ("wrong outcome",
                 "Sleep problems and pain in emerging adults. Excluded: outcome is pain."),
    "20301574": ("off-topic search noise",
                 "Cystinosis (GeneReviews). Returned by PubMed relevance ranking on a school-start-"
                 "time query; excluded on title."),
    "39181105": ("off-topic search noise",
                 "Diazepam nasal spray for prolonged seizure. Search noise; excluded on title."),
    "37294231": ("off-topic search noise",
                 "Deep brain stimulation for Tourette syndrome. Search noise; excluded on title."),
}


def esummary(pmids: list[str]) -> dict:
    out: dict[str, dict] = {}
    for i in range(0, len(pmids), 40):
        chunk = pmids[i:i + 40]
        url = EUTILS + "esummary.fcgi?db=pubmed&retmode=json&id=" + ",".join(chunk)
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        for attempt in range(4):
            try:
                with urllib.request.urlopen(req, timeout=60) as fh:
                    res = json.loads(fh.read().decode("utf-8", "replace"))["result"]
                for p in chunk:
                    if p in res:
                        out[p] = res[p]
                break
            except Exception:
                if attempt == 3:
                    raise
                time.sleep(2 * (attempt + 1))
        time.sleep(0.4)
    return out


# pmid -> study_id from the YAML records themselves
included: dict[str, str] = {}
no_pmid: list[str] = []
tiers: dict[str, str] = {}
for path in sorted(glob.glob(os.path.join(HERE, "*.yaml"))):
    text = open(path, encoding="utf-8").read()
    sid = os.path.splitext(os.path.basename(path))[0]
    m = re.search(r'^pmid:\s*"?([0-9]+)"?\s*$', text, re.M)
    t = re.search(r"^tier:\s*(\w+)\s*$", text, re.M)
    tiers[sid] = t.group(1) if t else "?"
    if m:
        included[m.group(1)] = sid
    else:
        no_pmid.append(sid)

screened = [ln.strip() for ln in open(os.path.join(HERE, "screened_pmids.txt")) if ln.strip()]
meta = esummary(screened)

rows_inc, rows_exc = [], []
for p in screened:
    r = meta.get(p, {})
    title = (r.get("title") or "??").rstrip(".")
    journal = r.get("source", "?")
    year = str(r.get("pubdate", ""))[:4]
    if p in included:
        sid = included[p]
        rows_inc.append((p, sid, tiers.get(sid, "?"), year, journal, title))
    else:
        cat, reason = EXCLUSIONS.get(p, ("UNLOGGED", "NO REASON RECORDED - THIS IS A DEFECT"))
        rows_exc.append((p, cat, year, journal, title, reason))

unlogged = [r for r in rows_exc if r[1] == "UNLOGGED"]

with open(os.path.join(HERE, "screening_log.md"), "w", encoding="utf-8") as fh:
    w = fh.write
    w("# Screening log - shard `s12_psychiatric`\n\n")
    w("Domain: depression, anxiety, emotional regulation and suicidality in relation to short "
      "sleep in adolescents and young adults.\n\n")
    w("Every record below was retrieved from PubMed and screened on title and abstract. "
      "Titles, journals and years in this table are printed from PubMed `esummary` at build time, "
      "not typed by hand. The instructions require at least 25 candidates screened and every "
      "exclusion logged with a reason.\n\n")
    w("| | count |\n|---|---|\n")
    w("| candidate records screened (unique PMIDs) | %d |\n" % len(screened))
    w("| INCLUDED, extracted to a YAML record | %d |\n" % len(rows_inc))
    w("| additional records with no PMID (data sources) | %d |\n" % len(no_pmid))
    w("| **total YAML records written** | **%d** |\n" % (len(rows_inc) + len(no_pmid)))
    w("| EXCLUDED | %d |\n\n" % len(rows_exc))

    w("## Included (%d)\n\n" % len(rows_inc))
    w("| PMID | study_id | tier | year | journal | title |\n")
    w("|---|---|---|---|---|---|\n")
    for p, sid, t, year, journal, title in sorted(rows_inc, key=lambda r: r[1]):
        w("| %s | `%s` | %s | %s | %s | %s |\n" % (p, sid, t, year, journal, title))
    w("\n")

    if no_pmid:
        w("## Included with no PubMed identifier (%d)\n\n" % len(no_pmid))
        w("| study_id | tier | what it is |\n|---|---|---|\n")
        w("| `cdc_suicide_rates` | TX | CDC WONDER / WISQARS US suicide mortality rates by age "
          "and sex. A government data query, not a journal article, so `pmid: null` and "
          "`access_tier` reflects the query rather than a publication. Needed for the absolute "
          "risk denominators. |\n\n")

    w("## Excluded (%d)\n\n" % len(rows_exc))
    w("| PMID | year | journal | title | reason for exclusion |\n")
    w("|---|---|---|---|---|\n")
    for p, cat, year, journal, title, reason in sorted(rows_exc, key=lambda r: (r[1], r[0])):
        w("| %s | %s | %s | %s | **%s.** %s |\n" % (p, year, journal, title, cat, reason))
    w("\n")

    if unlogged:
        w("## DEFECT: %d excluded records have no logged reason\n\n" % len(unlogged))
        for r in unlogged:
            w("- %s %s\n" % (r[0], r[4]))
        w("\n")

    w("## Searches run\n\n")
    w("PubMed `esearch` via `pm.py`, iteratively, following citation trails from the "
      "meta-analyses outward. The productive queries were:\n\n")
    for q in [
        "sleep duration depression adolescents meta-analysis",
        "sleep duration depression meta-analysis prospective studies (Zhai seed)",
        "adolescent sleep depression meta-analysis model (Lovato seed)",
        "sleep duration suicidality adolescents dose-response meta-analysis",
        "insomnia predictor mental disorders meta-analysis",
        "disturbed sleep depression children youths cohort meta-analysis",
        "sleep restriction adolescents mood emotion regulation experimental",
        "sleep deprivation adolescents affect (Talbot/Dahl seeds)",
        "sleep loss emotion meta-analysis experimental research",
        "improving sleep mental health randomised controlled trials meta-analysis (Scott seed)",
        "effects of improving sleep on mental health OASIS randomised (Freeman seed)",
        "adolescent cognitive-behavioral sleep interventions meta-analysis (Blake seed)",
        "non-pharmacological sleep interventions depression symptoms meta-analysis (Gee seed)",
        "insomnia treatments depression systematic review meta-analysis",
        "Mendelian randomization insomnia sleep duration depression bidirectional",
        "Mendelian randomization individual sleep traits major depressive disorder",
        "genetically proxied diurnal preference sleep timing major depressive disorder",
        "prospective association sleep deprivation depression adolescents (Roberts seed)",
        "bidirectional longitudinal disturbed sleep depressive symptoms cross-lagged",
        "bidirectional sleep duration screen time internalizing ABCD",
        "chronic sleep deprivation gender-specific depression adolescents prospective",
        "parental set bedtimes depression suicidal ideation (Gangwisch seed)",
        "one more hour of sleep teen hopelessness suicidal ideation (Winsler seed)",
        "insufficient sleep adolescent suicidal behaviors trends YRBS",
        "school start time delay adolescent depression depressive symptoms",
        "extending sleep short-sleeping adolescents emotional impact",
        "sleep debt amygdala anterior cingulate connectivity negative emotion",
        "human emotional brain without sleep prefrontal amygdala disconnect (Yoo seed)",
        "social jetlag depression anxiety adolescents young people meta-analysis",
        "bedtime procrastination college students next-day mood sleepiness",
        "trends US depression prevalence treatment gap",
        "age period cohort trends mood disorder suicide-related outcomes",
        "Mendelian randomization insomnia sleep duration suicide attempt (NO HITS)",
        "college students sleep deprivation depression anxiety longitudinal workload (NO HITS)",
    ]:
        w("- `%s`\n" % q)
    w("\n## Seed names in my task, and what I actually found\n\n")
    w("| seed given to me | resolution |\n|---|---|\n")
    for seed, res in [
        ("Zhai, Zhang & Zhang, Depression and Anxiety ~2015",
         "FOUND as `zhai2015`, PMID 26047492. **But it is an ADULT meta-analysis, not adolescent** "
         "- 7 prospective studies, n=25,271, mean ages well above 25. My task described it as being "
         "about adolescents; it is not. Reported as reality."),
        ("Lovato & Gradisar, Sleep Medicine Reviews ~2014",
         "FOUND as `lovato2014`, PMID 24857255. Real, adolescent, and correctly described - but it "
         "reports **no pooled effect size**, only a qualitative model, so it cannot contribute a "
         "number."),
        ("newer dose-response synthesis",
         "FOUND TWO: `chiu2018` (PMID 30093362, dose-response meta-analysis of sleep duration and "
         "suicidality, n=598,281) and `short2020` (PMID 32240932, sleep duration and mood in "
         "adolescents)."),
        ("Winsler et al., J Youth Adolesc ~2015",
         "FOUND as `winsler2015`, PMID 25178930, n=27,939 Fairfax County. Correctly described."),
        ("Gangwisch et al., Sleep ~2010, parental set bedtimes",
         "FOUND as `gangwisch2010`, PMID 20120626, n=15,659 Add Health. Correctly described, and it "
         "is the closest conceptual match to the subject's exposure that the pre-2020 literature "
         "contains."),
        ("CDC YRBS analyses",
         "FOUND as `wang2024_yrbs`, PMID 38506779, n=73,356, with absolute prevalences by sleep "
         "category as required."),
        ("Baum",
         "FOUND as `baum2014`, PMID 24889207, experimental adolescent sleep restriction."),
        ("Talbot",
         "FOUND as `talbot2010`, PMID 21058849 (Dahl is a co-author, so this seed and the Dahl seed "
         "resolve to one paper)."),
        ("Short",
         "FOUND TWO: `short2015` (PMID 26141007, experimental) and `short2020` (PMID 32240932, "
         "meta-analysis)."),
        ("Dahl", "resolved via `talbot2010`, on which Dahl RE is the fourth author."),
        ("meta-analysis of experimental sleep loss and mood",
         "FOUND as `palmer2024`, PMID 38127505, Psychological Bulletin, 'over 50 years of "
         "experimental research'. This is the single best source for the experimental mood effect "
         "size."),
        ("Freeman et al. OASIS, Lancet Psychiatry ~2017",
         "FOUND as `freeman2017`, PMID 28888927, n=3,755. Correctly described."),
        ("Blake et al. meta-analysis of adolescent sleep interventions",
         "FOUND as `blake2017`, PMID 28331991, plus the `blake2016_sense` RCT, PMID 27775416."),
        ("Gee et al.", "FOUND as `gee2019`, PMID 30579141."),
        ("Scott et al. ~2021, Sleep Medicine Reviews",
         "FOUND as `scott2021`, PMID 34607184, 'Improving sleep quality leads to better mental "
         "health'. Correctly described."),
        ("Yoo, Walker and successors, amygdala",
         "`yoo2007` VERIFIED (PMID 17956744) but **NO NUMBER IS RETRIEVABLE** - Current Biology "
         "magazine format with no abstract in PubMed, no PMC copy, and Cell Press returned HTTP 403 "
         "to every PDF attempt. Recorded with `se: null` and no magnitude. The mechanism requirement "
         "is discharged instead by `motomura2013` (PMID 23418586), which is better matched anyway: "
         "5 nights of 4 h TIB, young males, actigraphy-verified."),
    ]:
        w("| %s | %s |\n" % (seed, res))
print("wrote screening_log.md: %d screened, %d included (+%d no-pmid), %d excluded, %d unlogged"
      % (len(screened), len(rows_inc), len(no_pmid), len(rows_exc), len(unlogged)))
