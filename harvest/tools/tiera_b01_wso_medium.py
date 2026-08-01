#!/usr/bin/env python3
"""Batch 1: WSO forum threads and one Medium post, all retrieved as full page text.

WSO /forum/ pages render for WebFetch even though /company/ pages sit behind Cloudflare,
so these quotes are copied out of the page body itself rather than a search snippet.
"""
import sys
sys.path.insert(0, "/workspace/harvest/tools")
from tiera_lib import write

R = []

# ---------------------------------------------------------------------------
# WSO: "Optiver Trading Numerical Test" (2013). Contains a WSO editorial test-format
# block plus two quoted first-person user recalls (@jargon223, @lebron).
# ---------------------------------------------------------------------------
OPT_WSO = "https://www.wallstreetoasis.com/forum/trading/optiver-trading-numerical-test"
OPT_BASE = dict(
    firm="Optiver", source_url=OPT_WSO, source_type="wso", source_language="en",
    post_date="2013-09-28", access="full_text", retrieval_method="webfetch",
    office="unknown", platform="unknown", cycle="unknown",
)

R.append(dict(OPT_BASE,
    role_track="quant_trader", level="unknown",
    round="online_assessment", round_name="numerical test",
    section_context="80 questions in 8 minutes; Multiple Choice; Passing Score: 65 out of 80; Correct answer +1, Incorrect Answer -2, Skip -2",
    question_type="mental_math_speed",
    question_text="15/25 / ? = 14/35\n\nA) 3/5 B) 63/30 C) 14/15 D) 9/6",
    question_text_en=None,
    reported_answer=None,
    source_quote="An example of a question would be as follows\n\n15/25 / ? = 14/35\n\nA) 3/5 B) 63/30 C) 14/15 D) 9/6",
    poster_context="Thread started by a candidate invited to Optiver's numerical test; this specific item sits in a WSO staff-written 'Optiver Trading Math test' block summarising the test format, not in a candidate's own recall.",
    doubt="The arithmetic item is WSO editorial content illustrating the format, so it may have been invented by WSO as an example rather than transcribed from a real Optiver paper; the surrounding thread is genuine but this line has no first-person attestation.",
))

R.append(dict(OPT_BASE,
    role_track="quant_trader", level="unknown",
    round="online_assessment", round_name="numerical test",
    section_context="reported as timed; user says it was not purely mental arithmetic",
    question_type="logic_brainteaser",
    question_text="I got logic and IQ-test-similar questions, algebraic word problems, and problems where I had to draw a given shape on a piece of paper and perform instructions as given (like turn it to the right 90 degrees, flip it over from the right side, etc). This was all timed questions, too.",
    question_text_en=None,
    reported_answer=None,
    source_quote="It wasn't simple mental math at all. I got logic and IQ-test-similar questions, algebraic word problems, and problems where I had to draw a given shape on a piece of paper and perform instructions as given",
    poster_context="Attributed by WSO to 'certified hedge fund user @jargon223', quoted as a first-person account of sitting the Optiver test.",
    doubt="This describes a class of questions rather than reproducing one, and it is a 2013 account relayed by WSO staff quoting another user, so the exact wording could have been edited.",
))

R.append(dict(OPT_BASE,
    role_track="quant_trader", level="unknown",
    round="unknown", round_name="third round",
    section_context="user reports every question was followed by a confidence measure and that most questions were open-ended",
    question_type="expected_value",
    question_text=("You have a dartboard, circumscribed within a square. The square's dimensions are 10\"x10\". "
                   "The circle is split into 20 equal sections, and each is marked with a number alternating "
                   "from the low end to the high end of interval [1,20], so 1, 20, 2, 19, 3, etc. Also, inside "
                   "the center of the dartboard, is another circle 1\" in diameter. This is marked 50. So you "
                   "have 21 sections with numbers in them, these are your point values (payoff in dollars), and "
                   "the area outside the circle but in the square is worth 0.\n"
                   "-What's the EV of the game? -What's the optimal strategy? -If I let you rethrow your first "
                   "throw at the cost of $1, will you take it? What if you have 2 rethrows?"),
    question_text_en=None,
    reported_answer=None,
    source_quote="The circle is split into 20 equal sections, and each is marked with a number alternating from the low end to the high end of interval [1,20], so 1, 20, 2, 19, 3, etc.",
    poster_context="Attributed by WSO to user @lebron, who writes 'I passed the Optiver tests and got to the third round, so I can give you a few insights.'",
    doubt="2013 account; the poster does not say which office or role level, and WSO has reformatted the quote into its own article body so the original post is no longer separable.",
))

# ---------------------------------------------------------------------------
# WSO: "Jane Street Capital | First Round Phone Interview" (2009), an aggregation of
# several named users' first-person accounts.
# ---------------------------------------------------------------------------
JS1 = "https://www.wallstreetoasis.com/forum/trading/jane-street-capital-first-round-phone-interview"
JS1_BASE = dict(
    firm="Jane Street", source_url=JS1, source_type="wso", source_language="en",
    post_date="2009-10-03", access="full_text", retrieval_method="webfetch",
    office="unknown", platform="unknown", cycle="unknown",
)

R.append(dict(JS1_BASE,
    role_track="quant_trader", level="unknown",
    round="phone_technical", round_name="first round phone interview",
    section_context="no pencil, no paper - all mental",
    question_type="probability",
    question_text="I was asked to do some mental computations, and a basic probability question regarding dice.",
    question_text_en=None,
    reported_answer=None,
    source_quote="I was asked to do some mental computations, and a basic probability question regarding dice. Second round questions were a bit harder, but still reasonable.",
    poster_context="WSO user @brotherbear, describing his own Jane Street first and second round phone interviews.",
    doubt="The recall names the topic (dice probability) but does not reproduce the actual question, and the thread dates from 2009 so the process has almost certainly changed.",
))

R.append(dict(JS1_BASE,
    role_track="quant_trader", level="internship",
    round="superday", round_name="4th round interview for a SA gig",
    section_context="fourth round for a summer analyst position",
    question_type="poker_game_theory",
    question_text="Their 4th round interview for a SA gig (yes 4th round for a summer internship) was almost like a Math Olympiad. Game theory, FORMAL proofs and some conditional probability.",
    question_text_en=None,
    reported_answer=None,
    source_quote="Their 4th round interview for a SA gig (yes 4th round for a summer internship) was almost like a Math Olympiad. Game theory, FORMAL proofs and some conditional probability.",
    poster_context="WSO attributes this to user @eecs describing 'their summer analyst interview experience'; WSO has rewritten it into the third person.",
    doubt="WSO paraphrased this into the third person, so it is not the candidate's own words, and it names topics rather than a specific question.",
))

# ---------------------------------------------------------------------------
# WSO: "Jane Street Final Round - What to Expect" (2012). Long first-person write-up.
# ---------------------------------------------------------------------------
JS2 = "https://www.wallstreetoasis.com/forum/trading/jane-street-final-round-what-to-expect"
JS2_BASE = dict(
    firm="Jane Street", source_url=JS2, source_type="wso", source_language="en",
    post_date="2012-09-03", access="full_text", retrieval_method="webfetch",
    office="unknown", platform="unknown", cycle="unknown",
    poster_context="Original poster describing his own Jane Street final round after five phone interviews; says he finished with 87 chips and still did not get an offer.",
)

R.append(dict(JS2_BASE,
    role_track="quant_trader", level="unknown",
    round="trading_game", round_name="final round",
    section_context="100 poker chips issued at the start of the day, used across 4-6 hour-long interviews",
    question_type="trading_game",
    question_text=("At the final round itself you are given 100 poker chips at the start of the day. Over the course "
                   "of the next 4-6 hour long interviews you have to use the chips to make bets on scenarios given "
                   "to you. ... There is probability involved (for example a deck of cards or non-six sided die), "
                   "so ... a better candidate may end up with fewer chips than one who bet and got lucky."),
    question_text_en=None,
    reported_answer=None,
    source_quote="At the final round itself you are given 100 poker chips at the start of the day.",
    doubt="Describes the format of the round rather than a single question; 2012 vintage, and the poster explicitly declines to reproduce the specific problems he was given.",
))

R.append(dict(JS2_BASE,
    role_track="quant_trader", level="internship",
    round="trading_game", round_name="final round",
    section_context="chip-betting scenarios; poster believes this variant is reserved for internship interviews",
    question_type="market_making",
    question_text="make a market on the temperature in the room",
    question_text_en=None,
    reported_answer=None,
    source_quote="Some sources claim these scenarios can be as simple as 'make a market on the temperature in the room', I didn't get these questions and I'm guessing that they are reserved for internship interviews.",
    doubt="Explicit hearsay: the poster says he did NOT get this question and is repeating what 'some sources claim', and the internship attribution is his guess, so both the question and its level label are unattested.",
))

R.append(dict(JS2_BASE,
    role_track="quant_trader", level="unknown",
    round="trading_game", round_name="final round",
    section_context="deliberately unsolvable prompt; candidate bets chips on a confidence interval for their own solve time",
    question_type="betting_odds_arbitrage",
    question_text=("they do ask an unsolvable question (or rather, one that you need a PhD in probability to answer) "
                   "... The point of the questions is not to get it right, but to bet chips on how long you think it "
                   "will take you to answer it (the prompt is deceptively easy)."),
    question_text_en=None,
    reported_answer=None,
    source_quote="The point of the questions is not to get it right, but to bet chips on how long you think it will take you to answer it (the prompt is deceptively easy).",
    doubt="The poster deliberately withholds the actual prompt, so only the mechanism is attested; it is also a 2012 report of a single candidate's day.",
))

R.append(dict(JS2_BASE,
    role_track="quant_trader", level="unknown",
    round="trading_game", round_name="final round",
    section_context="pre-round preparation material sent by the firm",
    question_type="market_making",
    question_text=("Before the final round they send you a sheet outlining the basics of trading terminology. What bid "
                   "and ask mean, as well as how to properly phrase that you would like to make a trade and at what price."),
    question_text_en=None,
    reported_answer=None,
    source_quote="Before the final round they send you a sheet outlining the basics of trading terminology. What bid and ask mean, as well as how to properly phrase that you would like to make a trade and at what price.",
    doubt="This is process detail about what the firm sends candidates, not a question they were asked; included because it pins down what the market-making round actually requires.",
))

# ---------------------------------------------------------------------------
# Medium: first-person Citadel Securities HackerRank recall, dated Feb 22 2026.
# ---------------------------------------------------------------------------
CIT_MED = "https://hiya31.medium.com/what-they-asked-me-in-the-citadel-securities-hackerrank-coding-round-ed3ceded3c04"
CIT_BASE = dict(
    firm="Citadel Securities", source_url=CIT_MED, source_type="blog",
    source_language="en", post_date="2026-02-22", access="full_text",
    retrieval_method="webfetch", office="unknown", platform="HackerRank",
    cycle="unknown", role_track="quant_developer", level="unknown",
    round="online_assessment", round_name="Citadel Securities HackerRank round",
    section_context="two coding questions, ninety minutes, large constraints",
    poster_context="Named Medium author HIYA CHATTERJEE, writing in the first person ('I went into the Citadel Securities HackerRank round expecting standard interview problems') and showing a screenshot captioned 'The email I received after the round'.",
)

R.append(dict(CIT_BASE,
    question_type="coding_algorithms",
    question_text=("You're given arrays of start times and end times for employees. Each pair represents when someone "
                   "is active. The task: compute the maximum number of employees overlapping at any single moment. "
                   "... the constraint quietly says n can be as large as 2 x 10^5."),
    question_text_en=None,
    reported_answer="Sort the start times. Sort the end times. Sweep through them in order, tracking how many intervals are currently active. Increase when a new interval begins. Decrease when one ends. Track the maximum. O(n log n).",
    source_quote="You're given arrays of start times and end times for employees. Each pair represents when someone is active. The task: compute the maximum number of employees overlapping at any single moment.",
    doubt="The author's blog is general-interest tech content and the post is written in a heavily stylised, SEO-friendly voice, so it is possible the problems were reconstructed from a public source rather than from the sitting itself; the role and level are never stated.",
))

R.append(dict(CIT_BASE,
    question_type="coding_algorithms",
    question_text=("Again, start and end times. Again, overlapping intervals. But this time the task changed subtly. "
                   "Instead of asking for the global maximum number of simultaneous employees, they asked for the "
                   "maximum number of direct overlaps centered around a single employee. ... If one employee ends at "
                   "time 5 and another starts at time 5, do they overlap? In this problem, yes."),
    question_text_en=None,
    reported_answer="Sort the start times. Sort the end times. For each interval, determine how many intervals finish strictly before it starts. Then determine how many intervals begin strictly after it ends. Everything else overlaps. Binary search; O(n log n).",
    source_quote="Instead of asking for the global maximum number of simultaneous employees, they asked for the maximum number of direct overlaps centered around a single employee.",
    doubt="Same source caveat as the first problem: stylised write-up, no role or level stated, and the second problem is described mainly by contrast with the first rather than reproduced as a prompt.",
))

write(R)
