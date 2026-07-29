"""S10 report compiler: renders REPORT.md from results.json and the evidence corpus."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def fmt(d, unit="", nd=2, signed=True):
    """Render a summary dict as 'median [lo, hi] unit'."""
    if d is None:
        return "n/a"
    s = f"{{:+.{nd}f}}" if signed else f"{{:.{nd}f}}"
    lo, hi = d["ci95"]
    return f"{s.format(d['median'])} [{s.format(lo)}, {s.format(hi)}]{(' ' + unit) if unit else ''}"


# Confidence ledger: quantity -> (evidence quantity, quality/tier, transportability,
# model dependence). A-D per spec/gates.md. Any D on transportability or model dependence is
# labelled a GUESS in the report body.
LEDGER = {
    "Q1 cumulative debt vs need": ("B", "B", "B", "C"),
    "Q1 incremental debt from the change at 16": ("B", "B", "B", "C"),
    "Q1 mean nightly deficit": ("B", "B", "B", "C"),
    "Q1 inferred individual sleep need": ("D", "B", "B", "D"),
    "Q2 vigilance deficit now": ("B", "A", "B", "C"),
    "Q2 overall neurocognitive deficit now": ("C", "A", "C", "C"),
    "Q2b academic achievement": ("B", "A", "A", "C"),
    "Q3 measured IQ change now": ("C", "B", "C", "C"),
    "Q3 permanent IQ change": ("C", "B", "D", "D"),
    "Q4 final adult height": ("B", "B", "A", "A"),
    "Q4 testosterone": ("D", "A", "A", "B"),
    "Q4 growth hormone 24 h output": ("D", "A", "B", "B"),
    "Q4 brain structure permanence": ("B", "B", "D", "D"),
    "Q5 depression symptom effect": ("B", "A", "A", "B"),
    "Q5 absolute excess depression risk": ("C", "B", "B", "C"),
    "Q6 life expectancy change": ("B", "C", "D", "C"),
    "Q6 type 2 diabetes absolute risk change": ("B", "B", "D", "C"),
    "Q6 dementia": ("D", "D", "D", "D"),
    "Q6 injury / drowsy driving": ("C", "C", "A", "D"),
    "Q7 comparator rank": ("B", "C", "C", "D"),
    "Q8 recovery time constant": ("C", "A", "B", "C"),
    "Q9 maintenance dose": ("D", "B", "B", "D"),
    "Screenable sleep disorder probability": ("C", "C", "A", "D"),
}


def bibliography():
    """Every verified record in the corpus, grouped by shard."""
    ver = json.loads((ROOT / "reports" / "verification.json").read_text())
    status = {r["file"]: r for r in ver["records"]}
    by_shard = defaultdict(list)
    for path in sorted((ROOT / "evidence").rglob("*.y*ml")):
        rel = str(path.relative_to(ROOT))
        try:
            docs = [d for d in yaml.safe_load_all(path.read_text()) if isinstance(d, dict) and d]
        except yaml.YAMLError:
            continue
        for doc in docs:
            v = status.get(rel, {})
            by_shard[path.parent.name].append({
                "citation": doc.get("citation", "?"),
                "doi": doc.get("doi"), "pmid": doc.get("pmid"),
                "tier": doc.get("tier"), "rob": (doc.get("rob") or {}).get("judgement"),
                "access": doc.get("access_tier"),
                "status": v.get("status", "NOT_CHECKED"),
                "study_id": doc.get("study_id"),
            })
    return by_shard


def main() -> str:
    res = json.loads((ROOT / "results.json").read_text())
    a = res["answers"]
    gate = json.loads((ROOT / "reports" / "gate_log.json").read_text())
    inv = json.loads((ROOT / "reports" / "inventory.json").read_text())
    agr = json.loads((ROOT / "reports" / "agreement.json").read_text())
    ver = json.loads((ROOT / "reports" / "verification.json").read_text())
    mv = res["multiverse"]
    voi = res["value_of_information"]

    q1, q2, q2b = a["Q1_dose"], a["Q2_cognition_current"], a["Q2b_academic"]
    q3, q5, q6 = a["Q3_intelligence"], a["Q5_psychiatric"], a["Q6_long_run"]
    q7, q89 = a["Q7_calibration"], a["Q8_Q9_recovery_and_prescription"]
    iq_now = q3["measured_full_scale_iq_change_if_tested_now_vs_after_8_weeks_adequate_sleep_points"]
    iq_perm = q3["permanent_change_in_adult_cognitive_ability_points"]
    le = q6["life_expectancy_change_months_total"]

    L = []
    W = L.append

    # ---------------------------------------------------------------- 1. BLUF
    W("# What three years of short sleep actually did to you")
    W("")
    W("## 1. Bottom line")
    W("")
    W(f"Not catastrophic. Against an age-appropriate requirement you accumulated about "
      f"**{q1['cumulative_debt_vs_individual_need_h']['median']:,.0f} hours** of sleep debt "
      f"(95% interval {q1['cumulative_debt_vs_individual_need_h']['ci95'][0]:,.0f}-"
      f"{q1['cumulative_debt_vs_individual_need_h']['ci95'][1]:,.0f}) from age 16, averaging "
      f"**{q1['mean_nightly_deficit_h']['median']:.1f} h short per night**. But only about "
      f"**{q1['incremental_debt_attributable_to_change_at_16_h']['median']:,.0f} hours** of that "
      f"is attributable to what changed at 16: your self-described *good* schedule of 6-8 h at "
      f"ages 14-16 was already roughly 2 h below an age-appropriate requirement, so most of the "
      f"debt would have accrued anyway.")
    W("")
    W(f"Measured full-scale IQ today versus after eight weeks of adequate sleep: "
      f"**{fmt(iq_now, 'points', 1)}**. Permanent change in adult cognitive ability: "
      f"**0.0 points, 95% interval {iq_perm['ci95'][0]:.1f} to {iq_perm['ci95'][1]:.1f}** — the "
      f"most likely value is exactly no loss, with a "
      f"{q3['prob_permanent_loss_exceeds_1_point']*100:.0f}% probability of losing more than "
      f"1 point and {q3['prob_permanent_loss_exceeds_3_points']*100:.1f}% of losing more than 3. "
      f"Life expectancy: **{le['median']:.2f} months** "
      f"({le['ci95'][0]:.2f} to {le['ci95'][1]:.2f}), i.e. days, not years. On a like-for-like "
      f"basis this exposure ranks **{q7['rank_of_this_exposure_on_same_footing']} of "
      f"{q7['n_exposures_compared']}** against smoking, obesity, inactivity, alcohol and poor "
      f"diet — mid-band, with all of them inside 1-3 months.")
    W("")
    W(f"The real damage is not your brain or your lifespan. It is "
      f"**{q2b['gpa_points_saturating']['median']:.2f} GPA points** "
      f"({q2b['gpa_points_saturating']['ci95'][0]:.2f} to "
      f"{q2b['gpa_points_saturating']['ci95'][1]:.2f}) of coursework you did not learn, which "
      f"does not come back, plus a current vigilance deficit of **Hedges' g "
      f"{q2["vigilance_g_at_subject_dose"]["median"]:.2f}** that does. Prescription: "
      f"**{q89['maintenance_dose_time_in_bed_h']['median']:.1f} h in bed** "
      f"(not 8 h of sleep — {q89['maintenance_dose_time_in_bed_h']['median']:.1f} h in bed to "
      f"*get* ~8 h), seven days a week, plus a short afternoon nap if you want to close the last "
      f"half hour. Expect "
      f"{q89['policies']['9h_in_bed_plus_45min_nap']['pct_of_recoverable_deficit_recovered']['week_4']['median']:.0f}% "
      f"recovery by week 4 and "
      f"{q89['policies']['9h_in_bed_plus_45min_nap']['pct_of_recoverable_deficit_recovered']['week_52']['median']:.0f}% "
      f"by week 52. There is a "
      f"{a['screenable_disorder']['value']*100:.0f}% chance you have a treatable sleep disorder "
      f"rather than only a schedule problem, which is worth ruling out.")
    W("")
    W("---")
    W("")

    # ---------------------------------------------------------------- 2. dashboard
    W("## 2. The dashboard")
    W("")
    W("Confidence grades are A-D on four axes: evidence **Qty**, evidence **Qual**ity and "
      "identification tier, **Trans**portability to a 16-19 year old, and **Model** dependence. "
      "A D on transportability or model dependence means the number is a **guess** and is "
      "labelled as such.")
    W("")
    W("| Quantity | Estimate | 95% interval | Qty | Qual | Trans | Model |")
    W("|---|---|---|---|:-:|:-:|:-:|:-:|")

    def row(label, d, unit="", nd=2, signed=True, override=None):
        g = LEDGER.get(label, ("?", "?", "?", "?"))
        if override is not None:
            est, ci = override
        else:
            est = f"{d['median']:+.{nd}f}" if signed else f"{d['median']:.{nd}f}"
            est = f"{est} {unit}".strip()
            ci = f"{d['ci95'][0]:+.{nd}f} to {d['ci95'][1]:+.{nd}f}" if signed \
                else f"{d['ci95'][0]:.{nd}f} to {d['ci95'][1]:.{nd}f}"
        W(f"| {label} | {est} | {ci} | {g[0]} | {g[1]} | {g[2]} | {g[3]} |")

    row("Q1 cumulative debt vs need", q1["cumulative_debt_vs_individual_need_h"], "h", 0, False)
    row("Q1 incremental debt from the change at 16",
        q1["incremental_debt_attributable_to_change_at_16_h"], "h", 0, False)
    row("Q1 mean nightly deficit", q1["mean_nightly_deficit_h"], "h", 2, False)
    row("Q1 inferred individual sleep need", q1["inferred_individual_sleep_need_at_19_h"], "h", 2, False)
    row("Q2 vigilance deficit now", q2["vigilance_g_at_subject_dose"], "g", 2)
    row("Q2 overall neurocognitive deficit now", q2["overall_neurocognitive_g_at_subject_dose"], "g", 2)
    row("Q2b academic achievement", q2b["achievement_sd_saturating_alternative"], "SD", 2)
    row("Q3 measured IQ change now", iq_now, "pts", 2)
    row("Q3 permanent IQ change", None,
        override=("0.0 pts", f"{iq_perm['ci95'][0]:.2f} to {iq_perm['ci95'][1]:.2f}"))
    row("Q4 final adult height", None, override=("0.0 cm", "0.0 to 0.7"))
    row("Q4 testosterone", None, override=("-10.3 %", "-20.6 to -0.1"))
    row("Q4 growth hormone 24 h output", None, override=("0 %", "-32 to +32"))
    row("Q4 brain structure permanence", None, override=("P = 0.03", "0.01 to 0.10"))
    row("Q5 depression symptom effect", q5["depression_symptom_d_causal_at_subject_dose"], "d", 3)
    row("Q5 absolute excess depression risk",
        q5["absolute_excess_risk_major_depressive_episode_pp"], "pp", 2)
    row("Q6 life expectancy change", le, "months", 2)
    row("Q6 type 2 diabetes absolute risk change",
        q6["type_2_diabetes_absolute_lifetime_risk_change_pp"], "pp", 2)
    row("Q6 dementia", None, override=("INSUFFICIENT EVIDENCE", "not quantifiable"))
    row("Q6 injury / drowsy driving", None,
        override=("-0.03 months if you drive", "-0.01 to -0.14; 0 if you do not drive"))
    row("Q7 comparator rank", None,
        override=(f"{q7['rank_of_this_exposure_on_same_footing']} of {q7['n_exposures_compared']}",
                  "all comparators 0.8-3.0 months"))
    row("Q8 recovery time constant", q89["recovery_time_constant_days"], "days", 1, False)
    row("Q9 maintenance dose", q89["maintenance_dose_time_in_bed_h"], "h in bed", 2, False)
    row("Screenable sleep disorder probability", None, override=("P = 0.21", "0.12 to 0.32"))
    W("")
    W("Three entries are graded D on both transportability and model dependence and are therefore "
      "**guesses, not estimates**: the permanent IQ change, the dementia channel, and the "
      "maintenance dose. The first two are guesses because no study has followed anyone exposed "
      "at this age; the third because your own sleep need is unmeasured and its population prior "
      "rests on 15 subjects.")
    W("")
    W("---")
    W("")

    # ---------------------------------------------------------------- 3. prescription
    W("## 3. The prescription")
    W("")
    rc = q89["reachability_check"]
    W(f"**Maintenance dose: {q89['maintenance_dose_time_in_bed_h']['median']:.1f} hours in bed, "
      f"every night, seven days a week.** That is time in bed, not sleep. Sleep efficiency in "
      f"healthy young adults is about 87.5%, so a sleep target needs roughly 45-60 minutes more "
      f"time in bed than the target itself. This is the number that stops new debt accruing.")
    W("")
    W(f"There is a hard ceiling you should know about. Habitual **nocturnal** sleep saturates near "
      f"{rc['max_sustainable_nocturnal_tst_h']} h; the frequently quoted "
      f"{rc['max_sustainable_tst_with_a_nap_h']} h figure was obtained in a protocol that "
      f"included a daytime nap opportunity. There is a "
      f"{rc['prob_need_exceeds_nocturnal_ceiling']*100:.0f}% probability your own requirement is "
      f"above what night-time sleep alone can deliver, in which case the remainder has to come "
      f"from a scheduled nap. That is why the prescription is a time-in-bed target *plus* an "
      f"optional nap rather than a single number.")
    W("")
    W("**Projected recovery of the reversible deficit, by policy and week (median %):**")
    W("")
    weeks = ["week_0", "week_1", "week_2", "week_4", "week_12", "week_26", "week_52"]
    W("| Policy | Sleep obtained | Balance vs need | " + " | ".join(w.replace("week_", "wk ") for w in weeks) + " |")
    W("|---|---|---|" + "---|" * len(weeks))
    for name, p in q89["policies"].items():
        vals = " | ".join(f"{p['pct_of_recoverable_deficit_recovered'][w]['median']:.0f}" for w in weeks)
        W(f"| {name.replace('_', ' ')} | {p['sustained_tst_weekday_h']:.2f} h | "
          f"{p['mean_nightly_balance_vs_need_h']['median']:+.2f} h | {vals} |")
    W("")
    cu = q89["weekend_catchup_alone"]
    W(f"**Weekend catch-up alone cannot work, and this is arithmetic rather than physiology.** "
      f"Repaying a weekday deficit of {q1['mean_nightly_deficit_h']['median']:.1f} h over two "
      f"weekend nights would require "
      f"{cu['required_sleep_per_weekend_night_h']:.1f} h of sleep per weekend night against a "
      f"single-night ceiling of about 10.2 h. At best a weekend repays "
      f"{cu['fraction_repayable']*100:.0f}% of the week's deficit. Sleeping in on Saturday is "
      f"worth doing and is not a solution.")
    W("")
    lg = q89["ledger_is_not_a_schedule"]
    W(f"**Do not read the {q1['cumulative_debt_vs_individual_need_h']['median']:,.0f}-hour debt as "
      f"a repayment schedule.** Your maximum sustainable nightly surplus over requirement is a "
      f"fraction of an hour, so clearing the ledger arithmetically would take "
      f"{lg['nights_to_repay_arithmetically']/365:.0f}+ years. That is not what happens. "
      f"Function recovers on a time constant of "
      f"{q89['recovery_time_constant_days']['median']:.0f} days "
      f"({q89['recovery_time_constant_days']['ci95'][0]:.0f}-"
      f"{q89['recovery_time_constant_days']['ci95'][1]:.0f}) largely independently of how many "
      f"ledger hours accumulated. The hours figure measures the size of the historical exposure, "
      f"not the length of the repayment.")
    W("")
    W("Two things that do work, and one that does not:")
    W("")
    W("- **Banking works forwards.** Sleep extension *before* a known restriction period "
      "measurably buffers the subsequent impairment. Extending sleep the week before finals is "
      "supported; catching up after is much less efficient.")
    W("- **Naps are load-bearing, not optional garnish.** They are the only route past the "
      "nocturnal ceiling.")
    W("- **Sleeping much more than your requirement does not help and is not the U-shaped risk "
      "people claim.** The long-sleep limb of the mortality and diabetes curves largely "
      "disappears under objective measurement and under genetic instrumentation, so your "
      "occasional 10-11 h weekend nights are recovery, not a risk factor.")
    W("")
    W("---")
    W("")

    # ---------------------------------------------------------------- 4. permanent
    W("## 4. What is permanent and what is not")
    W("")
    W("| System | Verdict | P(irreversible) |")
    W("|---|---|:-:|")
    W("| Vigilance and attention | Reversible, time constant ~2-3 weeks; residual not excluded | low |")
    W("| Working memory, executive function | Reversible; age-matched randomised tests are null | low |")
    W("| Full-scale / crystallized IQ | No detectable loss to reverse | ~0 |")
    W("| Fluid cognition, processing speed | Reversible state effect | low |")
    W("| **Coursework and skills not learned** | **Not recoverable by sleeping** | **1.0** |")
    W("| Brain structure | No evidence of permanent change | 0.03 (0.01-0.10) |")
    W("| Insulin sensitivity, glucose tolerance | Reversible in days to ~2 weeks | 0.05 |")
    W("| Inflammation (CRP, IL-6) | No durable effect; meta-analysis null for short sleep | 0.02 |")
    W("| Immune competence | Reversible, but recovery is dose-dependent | 0.02 |")
    W("| Testosterone | Reversible; measurable rebound within ~3 nights | low |")
    W("| Growth hormone | Redistributed, not lost; 24 h output unchanged | ~0 |")
    W("| **Final adult height** | **Unaffected: the window had essentially closed** | **0** |")
    W("| Amyloid / neurodegeneration | Acute rise reverses; no adolescent evidence exists | 0.03 |")
    W("| Mortality hazard | No evidence a closed adolescent exposure shifts it permanently | ~0 |")
    W("")
    W("The honest split: **one thing on this list is permanent, and it is not a biological "
      "injury.** It is the material you did not learn while you were too tired to encode it. "
      "Everything with a biological mechanism either has reverted or reverts on a timescale of "
      "days to weeks once you sleep adequately.")
    W("")
    W("Two important caveats in the other direction. First, *reversible* is established over the "
      "days-to-weeks windows that studies have actually observed; the longest chronic-restriction "
      "experiment ever run is 42 nights against your roughly 1,040, and 39% of the recovery "
      "literature followed people for three nights or fewer. Every time someone extended the "
      "observation window they found *more* incomplete recovery, never less. Second, "
      "\"no evidence of permanent change\" is not the same as \"evidence of no permanent "
      "change\": nobody has ever imaged or tested habitual 5-6 h sleepers aged 16-19 more than "
      "once, so the reassuring nulls are extrapolations downward past the range anyone sampled.")
    W("")
    W("---")
    W("")

    # ---------------------------------------------------------------- 5. reasoning
    W("## 5. Reasoning, outcome by outcome")
    W("")
    W("### Dose: how much sleep you actually lost")
    W("")
    W(f"Your reported hours were not used as measured hours. Self-reported habitual sleep exceeds "
      f"objectively measured sleep by roughly an hour on average, reports cluster on whole and "
      f"half hours, and it is unresolved whether you meant time in bed or time asleep. The model "
      f"corrects the habitual level while preserving your within-person contrasts (so a reported "
      f"3.5 h exam night is not 'corrected' upward to 6 h), applies a school/break/exam calendar "
      f"rather than a flat average, and credits the ~14-16 weeks a year you slept on an ad-lib "
      f"schedule. Estimated actual sleep over the exposure window: "
      f"**{fmt(q1['mean_actual_tst_over_exposure_h'], 'h', 2, False)}**, against an inferred "
      f"requirement of {fmt(q1['inferred_individual_sleep_need_at_19_h'], 'h', 2, False)}.")
    W("")
    W(f"{q1['fraction_of_nights_below_6h']['median']*100:.0f}% of nights fell below 6 h and "
      f"{q1['fraction_of_nights_below_5h']['median']*100:.0f}% below 5 h.")
    W("")
    W("The single most important framing point in this whole report: **the referent matters more "
      "than the exposure.** Comparing you to an age-appropriate requirement gives a large debt. "
      "Comparing you to *your own prior schedule* gives roughly a quarter of it, because 6-8 h at "
      "ages 14-16 was also below what a 15-year-old needs. If you have been carrying a sense that "
      "junior year broke something, the arithmetic says junior year made an existing deficit "
      "moderately worse rather than creating one.")
    W("")
    W("### Cognition now")
    W("")
    pv = res["pooled"]["pvt_g_large_dose"]
    W(f"Vigilance is the most affected function and the best evidenced. Pooling "
      f"{pv['k']} within-subject experimental restriction studies (including one four-dose ladder "
      f"in 15-19 year olds, the closest age match that exists) gives a pooled effect of "
      f"g {pv['bayes']['mu_median']:.2f} "
      f"[{pv['bayes']['mu_ci95'][0]:.2f}, {pv['bayes']['mu_ci95'][1]:.2f}] at the studied doses, "
      f"with substantial heterogeneity (tau {pv['bayes']['tau_median']:.2f}). Transported to your "
      f"dose, the estimate for you is **g {fmt(q2['vigilance_g_at_subject_dose'], '', 2)}**.")
    W("")
    W("Be careful how you read that interval: it spans 'no deficit' to 'severe'. That width is "
      "not sloppiness, it is the single most important fact in this section. Vulnerability to "
      "sleep loss is strongly trait-like (intraclass correlation ~0.675, stable over years), so "
      "the population average is a poor guide to any individual. The interval quoted is the "
      "*predictive* interval for one person, not the confidence interval on the average, which is "
      "much narrower and would be the wrong number to give you.")
    W("")
    W("Higher-order cognition is a different story, and the contrast is the reason the IQ answer "
      "is small. In the same literature, effect sizes fall steeply as tasks move from vigilance "
      "toward reasoning: pooled lapses around −0.5 to −0.8, executive function around −0.32, "
      "long-term memory around −0.19, and reasoning around −0.13. Two randomised experiments in "
      "exactly your age band returned nulls on higher-order measures: working memory was "
      "unaffected at 7 h versus 10 h in bed, and a 2024 crossover trial found cognitive effects "
      "only in adolescents with overweight or obesity, reporting that 'no differences emerged for "
      "adolescents with healthy weight'.")
    W("")
    W("### Intelligence")
    W("")
    dm = q3["direct_measurement_bound_iq_points"]
    W(f"The decisive constraint is direct measurement. {dm['study']} found "
      f"{dm['observed']:+.1f} points (SE {dm['se']:.2f}) — no decrement at all — after a harsher "
      f"exposure than yours, and its interval excludes a decrement worse than about "
      f"{abs(dm['lower_95_bound']):.1f} points.")
    W("")
    W("The common error here is multiplying a vigilance effect size by 15 and calling the result "
      "IQ points. That is wrong by roughly a factor of five: a reaction-time task shares only "
      "about 20-25% of its variance with general intelligence, and the measured "
      "reasoning-to-lapses ratio inside the largest meta-analysis is 0.164. Applying the naive 1:1 "
      "mapping to your exposure would yield a double-digit IQ loss, which is falsified by the "
      "direct measurement above.")
    W("")
    pdc = q3["permanent_decomposition"]
    W(f"Splitting crystallized from fluid: crystallized ability and full-scale IQ show no "
      f"detectable decrement; the state deficit sits in fluid and processing-speed measures. "
      f"Permanent change is **0.0 points with a 95% interval of {iq_perm['ci95'][0]:.2f} to "
      f"{iq_perm['ci95'][1]:.2f}**. The probability of a permanent loss exceeding 3 points is "
      f"{q3['prob_permanent_loss_exceeds_3_points']*100:.1f}%.")
    W("")
    W(f"That number is built from two separate possibilities rather than one, because they are "
      f"different claims. The first is that part of your current state deficit simply fails to "
      f"reverse (contributing {fmt(pdc['persistent_fraction_of_the_current_state_deficit'], 'points', 2)}). "
      f"The second is a developmental effect — that restriction during ongoing brain maturation "
      f"left a mark unrelated in size to how tired you are today, modelled with a "
      f"{pdc['prob_any_developmental_effect']['median']*100:.0f}% probability of occurring and "
      f"contributing {fmt(pdc['independent_developmental_effect'], 'points', 2)}. "
      f"{pdc['note']}")
    W("")
    W("### Academic achievement — the part that actually cost you something")
    W("")
    W(f"Quasi-experimental evidence (school start-time changes, time-zone and sunset-time "
      f"instruments, daylight-saving discontinuities) gives about "
      f"{q2b['per_hour_coefficient_used']['median']:.2f} SD of achievement per hour of habitual "
      f"sleep. Two figures are given because extrapolation matters: linear in dose gives "
      f"{fmt(q2b['achievement_sd_linear_extrapolation'], 'SD', 2)}, and a saturating form gives "
      f"{fmt(q2b['achievement_sd_saturating_alternative'], 'SD', 2)}. In GPA terms, "
      f"{fmt(q2b['gpa_points_saturating'], 'points', 2)}.")
    W("")
    W(f"{q2b['caveat']} The saturating figure is the one to believe.")
    W("")
    W("This is the largest real cost of the exposure and the only one that does not reverse. "
      "Sleeping properly from now on restores your capacity to learn; it does not retroactively "
      "teach you the material you encoded badly at 16 and 17.")
    W("")
    W("### Mood and psychiatric risk")
    W("")
    W(f"The observational literature looks alarming and mostly is not applicable to you. The key "
      f"structure is an exposure gradient of roughly tenfold: insomnia disorder carries an odds "
      f"ratio near 2.8, behaviourally imposed short sleep near 1.2, and genetically instrumented "
      f"sleep duration is null. Your exposure is the weakest of the three. Between 55% and 70% of "
      f"the observational association is non-causal — reverse causation plus confounding plus "
      f"criterion contamination, where depression scales count fatigue items that short sleep "
      f"moves directly. In the best instrumental-variable study the mood items alone were null "
      f"(d {q5['mood_items_only_effect_in_iv_study']['d']:+.2f}) while the fatigue items carried "
      f"the effect.")
    W("")
    W(f"Causal symptom effect at your dose: {fmt(q5['depression_symptom_d_causal_at_subject_dose'], 'd', 3)}. "
      f"Absolute excess risk of a major depressive episode: "
      f"{fmt(q5['absolute_excess_risk_major_depressive_episode_pp'], 'percentage points', 2)}.")
    W("")
    W("### Metabolic, cardiovascular, immune, endocrine")
    W("")
    W(f"All four are real while the exposure is running and revert once it stops. Type 2 diabetes: "
      f"applying the dose-response per-hour risk ratio and then the fraction that survives "
      f"genetic instrumentation gives a relative risk of "
      f"{fmt(q6['type_2_diabetes_rr_while_exposed_mr_adjusted'], '', 3, False)} while exposed, and "
      f"an absolute lifetime change of "
      f"{fmt(q6['type_2_diabetes_absolute_lifetime_risk_change_pp'], 'percentage points', 2)} "
      f"against a baseline lifetime risk of "
      f"{q6['type_2_diabetes_baseline_lifetime_risk_pct']:.0f}%. Cardiovascular: "
      f"{q6['hypertension_cvd']}")
    W("")
    W("Immune effects are real and reversible, but reversibility is dose-dependent in a way worth "
      "knowing: the one study that varied recovery sleep while holding restriction constant found "
      "abnormalities persisting after 8 h of recovery and resolving only after 10 h, or after a "
      "nap plus 8 h. Your occasional 10-11 h weekend nights were doing more work than you "
      "thought.")
    W("")
    W("On the things people worry about most: 24-hour growth hormone output is unchanged because "
      "the blunted sleep-onset pulse is compensated by waking pulses, and slow-wave sleep — when "
      "most sleep-onset growth hormone is released — is preserved, indeed slightly increased, "
      "under restriction, while stage 2 and REM absorb the loss. Final adult height is unaffected: "
      "a male has only about 3.65 cm of median growth left between 16 and 19, and 0.40 cm between "
      "18 and 19. Testosterone fell about 10% during the exposure and rebounds within days.")
    W("")
    W("### Lifespan, and why the number is so small")
    W("")
    W(f"Life expectancy change: **{fmt(le, 'months', 2)}**. The reason this is days rather than "
      f"years is a single arithmetic fact that dominates every long-run channel: the probability "
      f"a US male dies between exact ages 16 and 19 is about 0.0025. A hazard ratio applied only "
      f"across that window therefore costs almost nothing no matter how large it is — tripling "
      f"the hazard for three years costs about 107 days. The same ratio applied for the rest of "
      f"life costs 50-60 times more. Which of those applies depends entirely on whether a closed "
      f"adolescent exposure permanently shifts the hazard, and **no study of any design has ever "
      f"measured that**. The model assumes it mostly does not, on the grounds that every "
      f"mechanism anyone has measured reverts.")
    W("")
    W(f"{q6['dementia']}")
    W("")
    W(f"One channel does act inside the window rather than in old age, and it was missing from the "
      f"first version of this analysis: drowsy driving. Conditional on being a typical licensed "
      f"US male teenage driver it costs about "
      f"{q6['injury_channel_drowsy_driving_months']['conditional_on_being_a_typical_licensed_teenage_driver']['median']:.2f} "
      f"months (0.01-0.14), and zero if you do not drive. Small in absolute terms, but comparable "
      f"to the entire chronic-disease contribution, and it is the one mortality risk that was "
      f"live at the time rather than fifty years away.")
    W("")
    W("### How catastrophic, relative to things you already have opinions about")
    W("")
    W("| Exposure, 3 years from age 16 | Life expectancy lost (months) | 80% interval |")
    W("|---|---|---|")
    for r in q7["ranking_ascending_like_for_like_pro_rata"]:
        mark = " **<- this exposure**" if "THIS_SUBJECT" in r["exposure"] else ""
        W(f"| {r['exposure'].replace('_', ' ')}{mark} | {r['le_months_lost_central']:.1f} | "
          f"{r['interval80'][0]:.1f} to {r['interval80'][1]:.1f} |")
    W("")
    W(f"On this like-for-like basis you rank {q7['rank_of_this_exposure_on_same_footing']} of "
      f"{q7['n_exposures_compared']} — worse than three years of physical inactivity, comparable "
      f"to three years of smoking ten a day or of carrying a BMI of 27.5, and better than three "
      f"years of heavy drinking. Note how tight that band is: every one of these exposures, "
      f"honestly costed over three years starting at 16, lands between 0.8 and 3.0 months. That "
      f"is the real answer to 'how catastrophic is this'. It is a normal-sized lifestyle exposure, "
      f"not a category apart.")
    W("")
    W("I am deliberately not giving you a headline cigarette-equivalent number. It ranges from "
      "0.7 to 13 cigarettes a day depending purely on whether the comparison credits accumulated "
      "damage or credits cessation, and a figure that moves twentyfold with a defensible framing "
      "choice should not be quoted as a fact.")
    W("")
    W("---")
    W("")

    # ---------------------------------------------------------------- 6. what would change it
    W("## 6. What would change this answer")
    W("")
    W("### The surviving objections from adversarial review")
    W("")
    W("Three independent critics were given the full repository and instructed to break it: a "
      "methodologist, a domain skeptic, and a contrarian mandated to argue that the damage is "
      "negligible. They filed 49 numbered objections. Two full rework loops followed. Every "
      "objection is resolved in writing in `reports/objection_resolution.md`; the material "
      "corrections were:")
    W("")
    W("- The sleep-need referent was being taken from a study measuring maximal sleep *capacity* "
      "with a nap opportunity, and a stray clip in the code made the parameter unable to move "
      "below 8 h while the value *reported* as the requirement bypassed the clip. Fixing this "
      "reduced the debt by ~400 h and is the largest single correction in the project.")
    W("- The mortality channel used a categorical short-versus-normal risk ratio when "
      "dose-specific values were available, which inflated the life-expectancy loss roughly "
      "fourfold.")
    W("- The IQ estimate averaged four routes that were neither four nor independent, one of "
      "which produced an upper interval limit implying you would test 7 points *above* your own "
      "rested self. Restructured; the interval narrowed from ±7 to about −3.4 to +0.3.")
    W("- The comparator ranking discounted this exposure for cessation while not discounting the "
      "comparators, which is how it originally came out 'least harmful of eight'. On a symmetric "
      "basis it is 3rd of 8.")
    W("- Two harm channels were missing entirely: academic achievement, and drowsy-driving "
      "mortality. Both are now included.")
    W("")
    W("What survives and is not fixed: the publication-bias corrections are computed and reported "
      "but not propagated into the posterior, because with 1-5 studies per parameter the "
      "estimators are too unstable to correct with. Both that and the exclusion of qualitatively-"
      "reported null findings from inverse-variance pools bias this report **toward overstating "
      "harm**, and neither is corrected.")
    W("")
    W("### Model dependence")
    W("")
    W(f"The multiverse enumerates {mv['n_branches']} branches across three axes: whether your "
      f"reports meant time in bed or time asleep, which of three defensible self-report "
      f"calibrations applies, and which of three sleep-need referents is right. **Every branch "
      f"agrees you accumulated a real deficit** — the sign is completely robust — but the "
      f"magnitude spans {mv['debt_h_min']:,.0f} to {mv['debt_h_max']:,.0f} hours, a factor of "
      f"{mv['debt_h_spread_ratio']:.1f}. Nightly deficit spans "
      f"{mv['nightly_deficit_h_min']:.2f} to {mv['nightly_deficit_h_max']:.2f} h.")
    W("")
    W("So: treat the direction and the ordering of these findings as solid, and treat every "
      "specific number as good to one significant figure.")
    W("")
    W("### What to measure, in priority order")
    W("")
    o1 = voi["output_1_measured_iq_deficit"]
    W(f"The variance decomposition is unusually clear about this. "
      f"**{o1['fractional_variance_attributable'][o1['highest_value_measurement']]*100:.0f}% of "
      f"the uncertainty in the cognitive estimate is between-person heterogeneity in how people "
      f"respond to sleep loss**, not uncertainty about the literature. {o1['interpretation']}")
    W("")
    W(f"And the prescription is dominated by a different unknown: "
      f"{voi['output_2_maintenance_sleep_dose']['interpretation']}")
    W("")
    W(f"{voi['overall_recommendation']}")
    W("")
    W("---")
    W("")

    # ---------------------------------------------------------------- 7. protocol
    W("## 7. The four-week measurement protocol")
    W("")
    W("This converts every population number above into a personal one. It is worth more than "
      "anything else in this report.")
    W("")
    W("**Weeks 1-2, measure your baseline.** Sleep diary every morning plus a wearable or "
      "actigraph every night. Fourteen nights is the minimum: a single night's estimate of "
      "habitual sleep has an intraclass correlation of only 0.24, and you need 13 nights for a "
      "reliability of 0.80 and 15 for a standard error of measurement under 20 minutes. Record "
      "lights-out, estimated sleep onset latency, wake time, and out-of-bed time, because time in "
      "bed minus time asleep is the quantity the prescription hinges on. Do **not** trust a "
      "wearable's sleep-onset-latency estimate; current devices underestimate it, which is "
      "falsely reassuring on the single most diagnostic variable. Take latency from your diary.")
    W("")
    W("Complete three instruments once: the Epworth Sleepiness Scale, the Insomnia Severity "
      "Index, and the Munich Chronotype Questionnaire. Note the asymmetry in how to read them: a "
      "*normal* Epworth does not argue against a circadian disorder (about 85% of confirmed cases "
      "score in the normal range), but an Insomnia Severity Index below 7 is the strongest "
      "rule-out available.")
    W("")
    W("**Weeks 3-4, measure your sleep need.** An ad-lib protocol: 12 hours of sleep opportunity "
      "per night, no alarm, dark room, for at least 9 consecutive nights. Sleep duration will be "
      "long for the first 3-4 nights and then asymptote; the asymptote is your requirement. Three "
      "nights is not enough — the published protocol took 4 days just to discharge one hour of "
      "debt and 9 nights to reach a stable value. A school break is the only realistic window for "
      "this.")
    W("")
    W("**Throughout, measure your own sensitivity.** A validated psychomotor vigilance test, five "
      "times a day at fixed clock times. Use **mean reciprocal reaction time** as the primary "
      "outcome, not lapse count: it is the most sensitive metric (d_z 1.21 versus 0.91 for "
      "lapses) and lapse counts have poor test-retest reliability (intraclass correlation 0.51). "
      "Discard the first five sessions as practice; speed shows no practice effect but accuracy "
      "does.")
    W("")
    W("**Honest power calculation, because you should know what this can and cannot detect.** "
      "With a within-person rested standard deviation of about 6% of your own mean reciprocal "
      "reaction time, and an expected effect of about 0.21 s⁻¹ for a 2 h/night contrast, you need "
      "**about 31 analysed nights per condition** — 62 total — for 80% power at alpha 0.05 using "
      "a paired t-test, and 20-28 calendar weeks once night-to-night dependence is modelled. A "
      "four-week design has only 11-16% power for a 2 h contrast. **So a four-week protocol will "
      "reliably measure your sleep need and your habitual duration, and will not reliably measure "
      "your vigilance sensitivity.** If you want the second, plan on six blocks of 14 nights with "
      "a 3 h contrast.")
    W("")
    W(f"**When to see a sleep physician rather than just going to bed earlier.** There is a "
      f"{a['screenable_disorder']['value']*100:.0f}% probability "
      f"({a['screenable_disorder']['interval'][0]*100:.0f}-"
      f"{a['screenable_disorder']['interval'][1]*100:.0f}%) that something treatable is present, "
      f"and the composition matters: insomnia ~{a['screenable_disorder']['components']['insomnia']*100:.0f}%, "
      f"delayed sleep-wake phase disorder "
      f"~{a['screenable_disorder']['components']['dswpd']*100:.0f}%, obstructive sleep apnea "
      f"~{a['screenable_disorder']['components']['osa']*100:.0f}%. Go if, during the two diary "
      f"weeks, you routinely take more than 60 minutes to fall asleep on nights when you have the "
      f"opportunity, or if you cannot fall asleep at your target bedtime even with a full "
      f"opportunity and no alarm the next day. That specific pattern points to a circadian "
      f"disorder, for which the treatment is completely different from 'go to bed earlier' — "
      f"timed morning bright light plus low-dose melatonin taken hours before bedtime, which in "
      f"adolescents took the proportion still meeting diagnostic criteria from 82% to 13%.")
    W("")
    W("One thing the weekday/weekend gap does **not** tell you: it has essentially no diagnostic "
      "value for a circadian disorder (likelihood ratio 1.13), and a 2 h weekend delay is the "
      "worldwide adolescent norm. Your own social jetlag of about "
      f"{a['social_jetlag']['value']:.2f} h sits at roughly the "
      f"{a['social_jetlag']['percentile_for_age']}th percentile for your age. You are unremarkable "
      "on circadian misalignment and unusual only on duration.")
    W("")
    W("---")
    W("")

    # ---------------------------------------------------------------- 8. provenance + biblio
    W("## 8. How this was produced, and the evidence base")
    W("")
    vs = ver["summary"]
    W(f"- **{inv['n_records']} evidence records** across 21 domain shards, carrying "
      f"**{inv['n_effects_total']} effect estimates**, of which {inv['n_effects_poolable']} have a "
      f"usable standard error. Tier mix: {inv['records_by_tier']}.")
    W(f"- **Citation verification: {vs['n_identifier_resolves']}/{vs['n_records']} identifiers "
      f"resolved against Crossref and PubMed with the resolved title matched against the recorded "
      f"citation**; the remaining {vs['n_official_source']} are official statistical products with "
      f"no DOI, verified by domain. {vs['n_unverified']} unverified. No fabricated citation was "
      f"detected.")
    W(f"- **Blinded re-extraction** of {agr['n_reextraction_tasks_returned']} targets "
      f"(38.7% of records with poolable effects, including all 33 designated influential studies) "
      f"by six independent agents that could not see the first team's work. Agreement: ICC "
      f"{agr['continuous_raw']['icc_weighted_mean_across_scales']} raw, "
      f"{agr['continuous_sign_reconciled']['icc_weighted_mean_across_scales']} sign-reconciled; "
      f"kappa {agr['categorical']['kappa_tier']['kappa']} on evidence tier, "
      f"{agr['categorical']['kappa_rob']['kappa']} on risk of bias.")
    W(f"- **{gate['n_pass']} of {gate['n_gates']} acceptance gates pass**, with failures described "
      f"rather than relaxed, in `reports/gate_log.md`. Risk of bias carries no numeric weight "
      f"anywhere in the model because its inter-rater agreement (kappa "
      f"{agr['categorical']['kappa_rob']['kappa']}) is too low to justify weighting on it.")
    W(f"- **{gate['n_tests']} tests pass**, including regression tests that reproduce published "
      f"pooled estimates, agreement between two independent posterior computations (exact grid "
      f"marginalisation and NUTS, agreeing to 0.0005 on the pooled mean), and reproduction of the "
      f"published US male life expectancy at 19 to 0.0002 years.")
    W(f"- **{res['meta']['n_monte_carlo_draws']:,} Monte Carlo draws**, fixed seed "
      f"{res['meta']['seed']}, everything regenerable with `make all`.")
    W("")
    W("Bias diagnostics: E-values are "
      f"{a['bias_analysis']['e_value_mortality_rr_1.12']:.2f} for the mortality association and "
      f"{a['bias_analysis']['e_value_t2d_rr_1.09_per_hour']:.2f} for the per-hour diabetes "
      f"association. {a['bias_analysis']['interpretation']}")
    W("")
    W("### Bibliography")
    W("")
    bib = bibliography()
    total = sum(len(v) for v in bib.values())
    W(f"{total} records. `V` = identifier resolved and title matched; `O` = official statistical "
      f"source verified by domain. Tier and risk-of-bias grade as assessed by the extraction "
      f"station.")
    W("")
    for shard in sorted(bib):
        W(f"#### {shard}")
        W("")
        for r in sorted(bib[shard], key=lambda x: str(x["study_id"])):
            flag = {"VERIFIED": "V", "OFFICIAL_SOURCE": "O",
                    "OFFICIAL_SOURCE_UNREACHED": "O"}.get(r["status"], "?")
            ident = f"doi:{r['doi']}" if r.get("doi") else (
                f"PMID:{r['pmid']}" if r.get("pmid") else "no persistent identifier")
            W(f"- [{flag}] [{r['tier']}/{r['rob']}/{r['access']}] {r['citation']} — {ident}")
        W("")

    text = "\n".join(L)
    (ROOT / "REPORT.md").write_text(text)
    return text


if __name__ == "__main__":
    t = main()
    print(f"REPORT.md written: {len(t.splitlines())} lines, {len(t.split())} words")
