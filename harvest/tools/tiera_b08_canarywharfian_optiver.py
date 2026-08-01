#!/usr/bin/env python3
"""Optiver Quantitative Trading summer-internship recall from Canary Wharfian.

One candidate who sat the online tests and the first two interview rounds, writing up
the whole funnel: 80-in-8, the sequences test, Zap-N, SHL, a recruiter round, and a
trader round with two market-making games and a list of quant/options questions.

Every question is sliced out of the live page text and asserted before writing, because
the review is full of curly quotes and en-dashes that would silently corrupt a retyped
quote and fail the verifier.
"""
import html
import re
import sys
import urllib.request

sys.path.insert(0, "/workspace/harvest/tools")
import tiera_lib

URL = "https://www.canarywharfian.co.uk/companies/53/optiver/interviews"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")


def page_text():
    req = urllib.request.Request(URL, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        raw = r.read().decode("utf-8", "replace")
    raw = re.sub(r"(?is)<(script|style|noscript|svg)\b[^>]*>.*?</\1>", " ", raw)
    raw = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</li>|</tr>|</h\d>", "\n", raw)
    t = html.unescape(re.sub(r"<[^>]+>", " ", raw))
    t = re.sub(r"[ \t\xa0]+", " ", t)
    return re.sub(r"\n\s*\n+", "\n", t)


TXT = page_text()


def bullets(after, before):
    """Bullet lines between two anchors, as they literally appear."""
    seg = TXT[TXT.index(after) + len(after):TXT.index(before, TXT.index(after))]
    out = []
    for line in seg.split("\n"):
        line = line.strip()
        if line.startswith("- "):
            out.append(line[2:].strip())
    return out


ONLINE = ("Online tests: Optiver cares very heavily about how quickly you can make "
          "numerical decisions, and thus their round of online testing (pre-interview) is "
          "pretty long an strenuous. For the Quantitative Trading role, it includes their "
          "\u201c80 in 8\u201d (80 questions in 8 minutes) mental maths test, followed by an "
          "identifying sequences test, e.g. you are shown a sequence of numbers, and must "
          "guess the next number or missing number.")
assert ONLINE in TXT

ZAPN = ("Another is called Zap-N, and is very similar to Pymetrics used by other firms. The "
        "so-called \u201cgamified assessment\u201d presents you with roughly 10 different mini "
        "games, ranging from remembering incrementally longer strings of numbers to reaction "
        "time tests.")
assert ZAPN in TXT

SHL = ("Finally, an SHL \u201cGeneral Ability\u201d test is sent, which is also similar to what "
       "many banks uses, and consists of questions testing your ability to calculate simple "
       "percentages, read data from graphs and interpret information.")
assert SHL in TXT

MMGAME = ("You are given a question, such as \u201cHow much money was spent in pubs in the UK, "
          "on the first day after the COVID lockdown?\u201d")
assert MMGAME in TXT

MMRULES = ("You are first asked to come up with an estimate, and to give ranges with a 50% and "
           "90% confidence interval (e.g. you are 90% sure that your guess falls within the "
           "range you suggest).")
assert MMRULES in TXT

MMPOS = ("Finally, after 4 rounds of the game, I was asked my net position (how many times I "
         "brought - sold) and average price transacted for.")
assert MMPOS in TXT

BEHAV2 = ("This was followed by a couple of behavioural-based questions, asking about what role "
          "I\u2019d take in a team, and what I\u2019d do if I was confident on a solution to a "
          "particular problem, but a much more experienced team member disagrees with me.")
assert BEHAV2 in TXT

R1 = bullets("The questions asked were:", "It was definitely useful to have")
R2 = bullets("And then the following quantitative and finance-related questions:",
             "Overall Impressions:")
assert len(R1) == 10, R1
assert len(R2) >= 6, R2

POSTER = ("Canary Wharfian candidate review filed under Trading/Global Markets, "
          "'Quantitative Trading - Summer Internship', rated 2/5 and marked 'Added 3 years "
          "ago' as of a 2026-08-01 fetch. The reviewer states: '(I completed the 1st and 2nd "
          "round interviews, but received a rejection prior to the final round).'")
DOUBT_BASE = ("Canary Wharfian reviews are user-submitted and moderated only for 'quality', so "
              "nothing independently confirms the reviewer sat this process; the entry also "
              "carries no absolute date, only a relative 'Added 3 years ago', so the cycle "
              "cannot be pinned down.")
DOUBT_RECALL = (DOUBT_BASE + " Written some time after the interview, so the phrasing is the "
                "candidate's reconstruction rather than the interviewer's words.")

recs = []


def add(qtext, qtype, quote, rnd, rname, section=None, doubt=DOUBT_RECALL, ans=None):
    assert quote in TXT, quote[:70]
    recs.append({
        "firm": "Optiver",
        "role_track": "quant_trader",
        "level": "internship",
        "cycle": "unknown",
        "office": "unknown",
        "round": rnd,
        "round_name": rname,
        "platform": "unknown",
        "section_context": section,
        "question_type": qtype,
        "question_text": qtext,
        "question_text_en": None,
        "reported_answer": ans,
        "source_url": URL,
        "source_type": "blog",
        "source_quote": quote,
        "source_language": "en",
        "post_date": "unknown",
        "access": "full_text",
        "retrieval_method": "webfetch",
        "poster_context": POSTER,
        "doubt": doubt,
    })


# ------------------------------------------------------------------ online test round
add("their \u201c80 in 8\u201d (80 questions in 8 minutes) mental maths test",
    "mental_math_speed", ONLINE, "math_sequences_test",
    "round of online testing (pre-interview)", "80 questions in 8 minutes",
    DOUBT_BASE + " The reviewer describes the test format rather than reproducing any "
    "individual arithmetic item, so no actual question text survives here.")
add("an identifying sequences test, e.g. you are shown a sequence of numbers, and must guess "
    "the next number or missing number",
    "sequences", ONLINE, "math_sequences_test", "identifying sequences test", None,
    DOUBT_BASE + " Format description only -- no specific sequence is reproduced.")
add("the so-called \u201cgamified assessment\u201d presents you with roughly 10 different mini "
    "games, ranging from remembering incrementally longer strings of numbers to reaction time "
    "tests",
    "other", ZAPN, "online_assessment", "Zap-N", "roughly 10 different mini games",
    DOUBT_BASE + " Only two of the roughly ten games are characterised, and neither is named.")
add("an SHL \u201cGeneral Ability\u201d test ... consists of questions testing your ability to "
    "calculate simple percentages, read data from graphs and interpret information",
    "other", SHL, "online_assessment", "SHL \u201cGeneral Ability\u201d test", None,
    DOUBT_BASE + " This is an off-the-shelf SHL product rather than an Optiver-authored test, "
    "so the items are not Optiver's own.")

# ------------------------------------------------------------------------- first round
R1_TYPES = {
    "Why did you choose to study the degree that you are studying?": "behavioral",
    "Why do you want a career in trading specifically?": "behavioral",
    "Why Optiver (over other market making firms)?": "behavioral",
}
R1_QUOTE_BLOCK = TXT[TXT.index("The questions asked were:"):
                     TXT.index("It was definitely useful to have")]
for q in R1:
    quote = q if len(q) >= 45 else None
    if quote is None:
        # Short behavioural prompts get anchored to the neighbouring line so the verifier
        # has enough text to match on.
        i = R1.index(q)
        nb = R1[i + 1] if i + 1 < len(R1) else R1[i - 1]
        seg = R1_QUOTE_BLOCK
        a, b = sorted([seg.index(q), seg.index(nb)])
        quote = seg[a:b + len(nb if seg.index(nb) > seg.index(q) else q)]
    add(q, R1_TYPES.get(q, "behavioral"), quote.strip(), "unknown",
        "1st Round Interview", "takes place with someone from the campus recruiting team")

# ------------------------------------------------------------------------ second round
add("You are given a question, such as \u201cHow much money was spent in pubs in the UK, on the "
    "first day after the COVID lockdown?\u201d",
    "market_making", MMGAME, "trading_game",
    "2nd Round Interview -- Two market-making games were played",
    "no pen-and-paper or calculator; give a bid and ask with a fixed 10% spread")
add("after 4 rounds of the game, I was asked my net position (how many times I brought - sold) "
    "and average price transacted for",
    "market_making", MMPOS, "trading_game",
    "2nd Round Interview -- Two market-making games were played", "after 4 rounds of the game")
add("what role I\u2019d take in a team, and what I\u2019d do if I was confident on a solution to "
    "a particular problem, but a much more experienced team member disagrees with me",
    "behavioral", BEHAV2, "unknown", "2nd Round Interview")

R2_TYPES = {
    "How long would it take you to do 2/17 in your head (to 3 decimal places)?": "mental_math_speed",
    "Today is a Wednesday, what will be the day of the week on this date next year?": "logic_brainteaser",
    "What is a call and put option?": "options_theory",
    "Can you name a few of the Greeks?": "options_theory",
}
R2_BLOCK = TXT[TXT.index("And then the following quantitative and finance-related questions:"):
               TXT.index("Overall Impressions:")]
for q in R2:
    if q.startswith("I said 10 seconds"):
        continue
    qt = R2_TYPES.get(q)
    if qt is None:
        qt = "statistics_regression" if q.startswith("Simpson") else "options_theory"
    quote = q
    if len(q) < 45:
        # Extend forward through the following bullet so the verifier has enough to match.
        i = R2_BLOCK.index(q)
        quote = R2_BLOCK[i:i + 200].rsplit("\n", 1)[0].strip()
    add(q, qt, quote, "unknown", "2nd Round Interview",
        "The second round takes place with a trader ... you are not allowed to use a "
        "pen-and-paper, or a calculator, for the entire duration of the interview")

tiera_lib.write(recs)
