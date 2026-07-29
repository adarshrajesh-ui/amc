#!/usr/bin/env python3
"""Attach a per-effect verbatim `quote` to every effect in every YAML record.

Anti-fabrication guard: each quote must appear, after whitespace normalisation, inside material this
shard actually retrieved -- the record's own notes/rob.notes/direction_note text, or one of the source
files under src/. If any quote fails that check nothing is written.
"""
import glob
import os
import re
import sys
import textwrap

import yaml

D = os.path.dirname(os.path.abspath(__file__))


def norm(s):
    return re.sub(r"\s+", " ", s or "").strip()


# ---------------------------------------------------------------- quote assignments
T16_ACUTE_TAIL = ("Drivers who reported having slept for 4:00 - 4:59, 5:00 - 5:59, and 6:00 - 6:59 had 4.3 "
                  "(CI 2.2 - 8.3), 1.9 (CI 1.3 - 2.6), and 1.3 (CI 1.1 - 1.7) times the odds, respectively, "
                  "of having contributed to the crash in which they were involved compared with drivers who "
                  "had slept for 7 hours or longer.")
T16_USUAL_TABLE = ('[Table 3, unmatched, critical-reason: "Usual daily hours of sleep ... < 4:00 0.8 (0.1-5.6) '
                   '... 4:00 - 4:59 5.4 (1.6-17.6) ... 5:00 - 5:59 1.4 (0.5-3.6) ... 6:00 - 6:59 1.4 (0.9-2.0) '
                   '... >= 7:00 1.0 Ref"]')
T16_DEV_TAIL = ("drivers who slept for 2-3 hours, 3-4 hours, and more than 4 hours less than usual had 3.0 "
                "(CI 2.0 - 4.3), 2.1 (CI 1.0 - 4.4), and 10.2 (CI 4.6 - 22.9) times the odds of having "
                "contributed to the crash in which they were involved, respectively, compared with drivers who "
                "had slept for at least their usual amount in the 24 hours preceding the crash.")
T18_MAIN = ("Drivers who reported having slept for 6, 5, 4, and less than 4 hr in the 24 hr before crashing had "
            "1.3 (95% confidence interval [CI] = 1.04 to 1.7), 1.9 (1.1 to 3.2), 2.9 (1.4 to 6.2), and 15.1 "
            "(4.2 to 54.4) times the odds, respectively, of having been culpable for their crashes, compared "
            "with drivers who reported 7-9 hr of sleep.")
T12_IMPUTED = ("In the imputed data, an estimated 7.0% of all crashes (95% confidence interval: 4.6%, 9.3%), "
               "13.1% of non-fatal crashes that resulted in hospital admission (95% confidence interval: 8.8%, "
               "17.3%), and 16.5% of fatal crashes (95% confidence interval: 12.5%, 20.6%) involved a drowsy "
               "driver.")
NHTSA_1115 = ("driver drowsiness was involved in an estimated 1.4% of all police reported crashes nationwide, "
              "2.0% of crashes that resulted in injuries and 2.4% of crashes that resulted in a death in years "
              "2011-2015 (National Center for Statistics & Analysis, 2017)")
NHTSA_2023 = ("In 2023 (the most recent year for which data are available), FARS indicated that 1.5% of fatal "
              "crashes involved a drowsy driver and 1.8% of drivers in fatal crashes were either 'drowsy, "
              "asleep, fatigued, ill or black[ed] out.' Using these data, NHTSA reported that 633 people were "
              "killed in drowsy driving crashes in 2023.")
OWENS_HEAD = ("drowsiness was identified in 8.8%-9.5% of all crashes examined and 10.6%-10.8% of crashes that "
              "resulted in significant property damage, airbag deployment, or injury.")
OWENS_AGE_NS = ("Variation by age, sex, and crash severity was not statistically significant (all P > 0.20).")
GOTT_PERHOUR = ("For every hour decrease in usual sleep duration, the aOR for any motor vehicle crash increased "
                "by 13% in the overall population and by 22% in participants who did not report excessive "
                "sleepiness (Table 2).")
GOTT_CAT = ("Compared to those sleeping 7 or 8 hours per night (n = 2105), those who reported sleeping only 6 "
            "hours per night (n = 626) had a 33% higher aOR for any motor vehicle crash, while those sleeping 5 "
            "or fewer hours per night (n = 235) had a 47% higher aOR.")
FOSS_HOURS = ("Crashes from 7 to 7:59 am decreased sharply (-25%, p = .008), but increased similarly from 8 to "
              "8:59 am (21%, p = .004).")
W16_SHORT = ("The likelihood of each of the five risk behaviors was significantly higher for students who "
             "reported sleeping <=7 hours on an average school night")
PIZZA_MODEL = ("The logistic procedure established a significant predictive role of male sex (p < 0.0001; odds "
               "ratio = 3.3), tobacco use (p < 0.0001; odds ratio = 3.2), sleepiness while driving (p = 0.010; "
               "odds ratio = 2.1), and bad sleep (p = 0.047; odds ratio = 1.9) for the crash risk.")
HUTCH = ("Aside from length of licensure, only driving alone while drowsy and being a current smoker were "
         "associated with having been in a crash.")
VOR11 = ("For VB and Chesapeake, teen drivers' crash rates in 2008 were 65.8/1000 and 46.6/1000 (p < 0.001), "
         "respectively, and in 2007 were 71.2/1000 and 55.6/1000.")

QUOTES = {
    "tefft2016_aaa": [
        ("drivers who reported having slept for less than 4 hours in the past 24 hours had an estimated 11.5 "
         "times the odds of having contributed to the crash in which they were involved, compared with drivers "
         "who reported having slept for 7 or more hours in the past 24 hours (Odds Ratio [OR] 11.5; 95% "
         "Confidence Interval [CI] 2.9 - 45.7)"),
        T16_ACUTE_TAIL, T16_ACUTE_TAIL, T16_ACUTE_TAIL,
        T16_USUAL_TABLE, T16_USUAL_TABLE,
        ("Drivers who reported usually sleeping for between 4 and 5 hours daily had an estimated 5.4 (CI 1.6 - "
         "17.6) times the odds of having contributed to the crash in which they were involved compared with "
         "drivers who reported usually sleeping for 7 hours or longer"),
        T16_USUAL_TABLE,
        ("Drivers who slept for between 1 and 2 hours less than usual in the past 24 hours had a statistically "
         "significant 30% increase in the odds of having contributed to the crash (OR 1.3; CI 1.0 - 1.7)"),
        T16_DEV_TAIL, T16_DEV_TAIL, T16_DEV_TAIL,
    ],
    "tefft2018": [
        T18_MAIN, T18_MAIN, T18_MAIN, T18_MAIN,
        ("Drivers who had slept less than 4 hr had 3.4 (95% CI = 2.1 to 5.6) times the increase in odds of "
         "culpable involvement in single-vehicle crashes compared with multiple-vehicle crashes."),
    ],
    "connor2002": [
        ("with drivers who reported five hours or less of sleep in the previous 24 hours compared with more than "
         "five hours (2.7, 1.4 to 5.4)"),
        ("drivers who identified themselves as sleepy (Stanford sleepiness score 4-7 v 1-3; odds ratio 8.2, 95% "
         "confidence interval 3.4 to 19.7)"),
        "with driving between 2 am and 5 am compared with other times of day (5.6, 1.4 to 22.7)",
        ("The population attributable risk for driving with one or more of the acute sleepiness risk factors was "
         "19% (15% to 25%)."),
    ],
    "martiniuk2013": [
        ("those who reported sleeping 6 or fewer hours per night had an increased risk for crash compared with "
         "those who reported sleeping more than 6 hours (relative risk [RR], 1.21; 95% CI, 1.04-1.41)"),
        ("Less weekend sleep was significantly associated with an increased risk for run-off-road crashes (RR, "
         "1.55; 95% CI, 1.21-2.00)."),
        ("Crashes for individuals who had less sleep per night (on average and on weekends) were significantly "
         "more likely to occur between 8 pm and 6 am (RR, 1.86; 95% CI, 1.11-3.13, for midnight to 5:59 am"),
        "RR, 1.66; 95% CI, 1.15-2.39, for 8:00 pm to 11:59 pm",
    ],
    "gottlieb2018": [GOTT_PERHOUR, GOTT_PERHOUR, GOTT_CAT, GOTT_CAT,
                     ("Considering usual sleep duration of 7 to 8 hours per night as normative, the "
                      "population-attributable fraction of motor vehicle crashes related to sleep duration of 6 "
                      "or fewer hours per night was 9%.")],
    "bioulac2017": [("Sleepiness at the wheel was associated with an increased risk of motor vehicle accidents "
                     "(pooled OR 2.51 [95% CI 1.87; 3.39]).")],
    "cummings2001": [
        ("Crash risk was greater among drivers who felt they were falling asleep (adjusted relative risk (aRR) "
         "14.2, 95% confidence interval (CI) 1.4 to 147)"),
        "those who drove longer distances (aRR 2.2 for each additional 100 miles, 95% CI 1.4 to 3.3)",
        "drank coffee within the last two hours (aRR 0.5, 95% CI 0.3 to 0.9)",
    ],
    "foss2019": [
        ("In the intervention county, there was a 14% downward shift in the time-series following the 75 min "
         "delay in school start times (p = .076). There was no change approaching statistical significance in "
         "any of the other three counties."),
        FOSS_HOURS, FOSS_HOURS,
        ("Crashes from 2 to 2:59 pm declined dramatically (-48%, p = .000), then increased to a lesser degree "
         "from 3 to 3:59 pm (32%, p = .024) and non-significantly from 4 to 4:59 (19%, p = .102)."),
        ("There was no meaningful change in early morning or nighttime crashes, when drowsiness-induced crashes "
         "might have been expected to be most common."),
    ],
    "binhasan2020": [
        ("The crash rate per 1000 in 16- to 18-year-old licensed drivers in FC during T1 was significantly "
         "higher compared to T2, 31.63 versus 29.59 accidents per 1,000 (95% confidence interval, 1.0-1.14, "
         "odds ratio 1.07, P = .03)."),
        ("there was a trend toward significance in distraction-related crashes per 1,000 in FC at T1 compared to "
         "T2 at 7.01 versus 6.13 (95% confidence interval, 0.99-1.31, odds ratio 1.14, P = .05), but were not "
         "significantly different in the remainder of the state."),
    ],
    "danner2008": [
        ("Average crash rates for teen drivers in the study county in the 2 years after the change in school "
         "start time dropped 16.5%, compared with the 2 years prior to the change, whereas teen crash rates for "
         "the rest of the state increased 7.8% over the same time period."),
        "Average hours of nightly sleep increased and catch-up sleep on weekends decreased.",
    ],
    "vorona2011": [VOR11, VOR11],
    "vorona2014": [
        ("Henrico teens manifested a statistically higher crash rate of 48.8/1000 licensed drivers versus "
         "Chesterfield's 37.9/1000 (p = 0.04) for 2009-2010."),
        ("For 2010-2011, HC 16-17 year old teens demonstrated a statistically significant higher crash rate "
         "(53.2/1000 versus 42.0/1000), while for 16-18 teens a similar trend was found, albeit nonsignificant "
         "(p = 0.09)."),
        ("Post hoc analyses found significantly more run-off road crashes to the right (potentially "
         "sleep-related) in Chesterfield teens."),
    ],
    "iihs2024_fars": [
        '"| 16 | 2,322,582 | 123 | 5.3 | 71 | 3.1 | ..."',
        '"| 17 | 2,326,541 | 175 | 7.5 | 101 | 4.3 | ..."',
        '"| 18 | 2,296,205 | 242 | 10.5 | 109 | 4.7 | ..."',
        ('"| 19 | 2,282,142 | 313 | 13.7 | 100 | 4.4 | ..." "| 20-24 | 11,451,815 | 1,360 | 11.9 | 377 | 3.3 | '
         '..." and the text: "The rate of deaths per 100,000 people in 2024 peaked at age 19 for male drivers '
         '(13.7)'),
        '"| 20-24 | 11,451,815 | 1,360 | 11.9 | 377 | 3.3 | ..."',
        '"| 16-19 | 9,006,150 | 1,317 | 14.6 | 8,596,938 | 632 | 7.4 | 17,603,088 | 1,950 | 11.1 |"',
        '"| 20-24 | 11,126,811 | 1,937 | 17.4 | 10,684,361 | 826 | 7.7 | 21,811,172 | 2,765 | 12.7 |"',
        '"| 16-19 | 2,268 | 24,773,280,873 | 9.2 | 931 | 17,958,953,050 | 5.2 | 3,202 | 42,732,233,923 | 7.5 |"',
        ('"| Sunday | 502 | 17 | | Monday | 377 | 13 | | Tuesday | 353 | 12 | | Wednesday | 324 | 11 | | '
         'Thursday | 375 | 13 | | Friday | 419 | 15 | | Saturday | 549 | 19 | | Total | 2,899 | 100 |"'),
        ('"In 2024, teenage crash deaths peaked in June." with "| June | 300 | 10 | | July | 286 | 10 | | August '
         '| 273 | 9 |"'),
        ('"Among passenger vehicle drivers ages 16-19 involved in fatal crashes in 2024, 41% were involved in '
         'single-vehicle crashes. This was the highest of any age group."'),
    ],
    "nhtsa_drowsy_counted": [NHTSA_1115, NHTSA_1115, NHTSA_1115, NHTSA_2023, NHTSA_2023],
    "ghsa2026": [
        ("researchers have also estimated that about 1.57% of baseline driving is drowsy. This means that at any "
         "given moment on the road, three out of every 200 people behind the wheel are driving drowsy."),
        ("Assuming the same proportion of fatalities in 2023 involved drowsy driving, there would have been "
         "6,326 roadway deaths in 2023 caused by drowsy driving. This is ten times more than the raw FARS data "
         "reported by NHTSA."),
        ("A survey of 718 college students at a sizable university in the Southwestern U.S. found that nearly "
         "half reported drowsy driving in the past month. Two other recent studies found 20% of 1,039 college "
         "students reported having fallen asleep while driving and 31% of 450 university students reported "
         "driving while drowsy at least once in the past month."),
        ("Males drive drowsy somewhat more frequently than females. Younger drivers 16 to 24 years old drive "
         "drowsy more frequently than older drivers."),
    ],
    "owens2018_aaa": [
        OWENS_HEAD,
        "Total Police-Reportable c 186 20 (10.8)",
        "Driver Age 16 to 19 158 14 (8.9) 20 to 24 160 18 (11.3)",
        "Driver Age 16 to 19 158 14 (8.9) 20 to 24 160 18 (11.3)",
        ("Lighting Conditions Daylight 408 25 (6.1) Dawn/Dusk 28 2 (7.1) Dark 153 29 (19.0)"),
    ],
    "owens2019": [
        ("The covariate-adjusted prevalence of drowsy driving was 13.9% (95% CI 3.0%-24.9%) higher in students "
         "who slept <7 hours on school-nights than in those who slept 8 or more hours."),
        ("Compared with those with a morning chronotype, the adjusted prevalence of drowsy driving was 15.2% "
         "(95% CI 4.5%-25.9%) higher among those with an evening chronotype."),
        ("Among survey respondents, 63.1% drove at least several times a week and 47.6% reported drowsy "
         "driving."),
    ],
    "tefft2012": [
        T12_IMPUTED, T12_IMPUTED, T12_IMPUTED,
        ("In the original (non-imputed) data, 3.9% of all crashes, 7.7% of non-fatal crashes that resulted in "
         "hospital admission, and 3.6% of fatal crashes involved a driver coded as drowsy; however, the "
         "drowsiness status of 45% of drivers was unknown."),
    ],
    "tefft2024_aaa": [
        ("Results show that an estimated 17.6% of all fatal crashes in years 2017-2021 involved a drowsy "
         "driver."),
        ("Over the 5-year study period, an estimated 29,834 people were killed in crashes that involved drowsy "
         "drivers."),
        ("In percentage terms, the proportion of fatal-crash-involved drivers who were drowsy was greatest among "
         "drivers aged 16-20; however, the largest number of drowsy drivers in crashes were aged 21-34."),
        ("An estimated 17% of drivers with BAC of 0.01-0.07 and 20% of drivers with BAC >=0.08 were drowsy, "
         "compared with 11% of those who had not been drinking."),
    ],
    "wheaton2016": [
        W16_SHORT, W16_SHORT, W16_SHORT, W16_SHORT,
        ("infrequent seatbelt use, riding with a drinking driver, and drinking and driving were also more likely "
         "for students who reported sleeping >=10 hours compared with 9 hours on an average school night"),
    ],
    "wheaton2014": [
        "The results showed that 4.0% reported falling asleep while driving during the previous 30 days.",
        "drowsy driving was more prevalent among binge drinkers than non-binge drinkers or abstainers",
        ("also more prevalent among drivers who sometimes, seldom, or never wear seatbelts while driving or "
         "riding in a car, compared with those who always or almost always wear seatbelts"),
        "Drowsy driving did not vary significantly by self-reported smoking status.",
    ],
    "pizza2010": [PIZZA_MODEL, PIZZA_MODEL, PIZZA_MODEL],
    "hutchens2008": [HUTCH, HUTCH],
    "czeisler2016": [
        ("'Drivers who have slept for two hours or less in the preceding 24 hours are not fit to operate a motor "
         "vehicle.'"),
        ("Panelists further agreed that most healthy drivers would likely be impaired with only 3 to 5 hours of "
         "sleep during the prior 24 hours."),
    ],
}

# ---------------------------------------------------------------- haystack of retrieved material
src_blob = ""
for p in glob.glob(os.path.join(D, "src", "*")):
    try:
        with open(p, "r", errors="ignore") as fh:
            src_blob += " " + fh.read()
    except OSError:
        pass
SRC = norm(src_blob)

fail = []
for sid, quotes in QUOTES.items():
    path = os.path.join(D, sid + ".yaml")
    rec = yaml.safe_load(open(path))
    hay = norm(" ".join(
        [rec.get("notes") or "", (rec.get("rob") or {}).get("notes") or ""]
        + [e.get("direction_note") or "" for e in rec["effects"]]
    ))
    if len(quotes) != len(rec["effects"]):
        fail.append("%s: %d quotes for %d effects" % (sid, len(quotes), len(rec["effects"])))
        continue
    for i, q in enumerate(quotes):
        nq = norm(q)
        if nq not in hay and nq not in SRC:
            fail.append("%s[%d] NOT FOUND: %s" % (sid, i, nq[:110]))

missing = [os.path.basename(p)[:-5] for p in glob.glob(os.path.join(D, "*.yaml"))
           if os.path.basename(p)[:-5] not in QUOTES]
if missing:
    fail.append("records with no quote mapping: %s" % missing)

if fail:
    print("ABORT - nothing written:")
    for f in fail:
        print("  ", f)
    sys.exit(1)

# ---------------------------------------------------------------- write
CF = re.compile(r"^(\s{4})cohort_family:")
for sid, quotes in QUOTES.items():
    path = os.path.join(D, sid + ".yaml")
    lines = open(path).read().split("\n")
    # drop any quote block written by an earlier run so this script is idempotent
    stripped, drop = [], False
    for ln in lines:
        if re.match(r"^\s{4}quote:", ln):
            drop = True
            continue
        if drop:
            if re.match(r"^\s{6}\S", ln):
                continue
            drop = False
        stripped.append(ln)
    lines = stripped
    out, k = [], 0
    for ln in lines:
        out.append(ln)
        if CF.match(ln):
            # break_on_hyphens must stay off: a folded YAML scalar rejoins lines with a space, so
            # wrapping "non-fatal" across lines would silently corrupt the verbatim quote.
            body = textwrap.wrap(norm(quotes[k]), width=108,
                                 break_on_hyphens=False, break_long_words=False)
            out.append("    quote: >")
            out.extend("      " + b for b in body)
            k += 1
    if k != len(quotes):
        print("ABORT %s: matched %d cohort_family lines, expected %d" % (sid, k, len(quotes)))
        sys.exit(1)
    open(path, "w").write("\n".join(out))

# ---------------------------------------------------------------- read back and confirm
bad = 0
for sid, quotes in QUOTES.items():
    rec = yaml.safe_load(open(os.path.join(D, sid + ".yaml")))
    for i, e in enumerate(rec["effects"]):
        if norm(e.get("quote")) != norm(quotes[i]):
            print("ROUNDTRIP MISMATCH %s[%d]" % (sid, i))
            bad += 1
print("done. records=%d effects=%d roundtrip_mismatches=%d"
      % (len(QUOTES), sum(len(v) for v in QUOTES.values()), bad))
sys.exit(1 if bad else 0)
