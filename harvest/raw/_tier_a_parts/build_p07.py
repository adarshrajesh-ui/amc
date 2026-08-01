import io
import json
import re

SRC = "/workspace/harvest/raw/_tiera_discover/taro_extracted.json"
OUT = "/workspace/harvest/raw/_tier_a_parts/p07_taro.jsonl"

DATA = json.load(open(SRC, encoding="utf-8"))
GOOD = [o for o in DATA if o["questions"] and len(o["questions"]) > 25]

FIRM_BY_SLUG = {
    "hudson-river-trading": "Hudson River Trading",
    "jump-trading": "Jump Trading",
    "drw": "DRW",
    "akuna-capital": "Akuna Capital",
    "two-sigma": "Two Sigma",
    "de-shaw": "D. E. Shaw",
}

MONTHS = {m: i + 1 for i, m in enumerate(
    "January February March April May June July August September October November December".split())}

TARO_DOUBT = ("jointaro.com aggregates self-reported interview experiences; the poster is anonymous "
              "and Taro does not verify that the person actually interviewed, and the site rewrites "
              "submissions into a house style, so wording may be lightly edited rather than the "
              "candidate's literal words.")


def firm_of(url):
    m = re.search(r"/companies/([^/]+)/", url)
    return FIRM_BY_SLUG[m.group(1)]


def date_of(o):
    m = re.match(r"(\w+) (\d{1,2}), (\d{4})", o["date"] or "")
    if not m:
        return "unknown"
    return "%s-%02d-%02d" % (m.group(3), MONTHS[m.group(1)], int(m.group(2)))


def office_of(o):
    m = re.search(r"Interview Experience - (.+)$", o["title"])
    return m.group(1).strip() if m else "unknown"


def role_title(o):
    m = re.match(r"(.+?) Interview Experience", o["title"])
    if not m:
        return o["title"]
    t = m.group(1)
    for slug, name in FIRM_BY_SLUG.items():
        if t.startswith(name):
            return t[len(name):].strip()
    if t.startswith("D. E. Shaw"):
        return t[len("D. E. Shaw"):].strip()
    return t


def level_of(o):
    return "internship" if re.search(r"intern", o["title"], re.I) else "unknown"


def pick(o, needle):
    """Return the exact contiguous line from the page text that contains `needle`."""
    blob = o["process"] + "\n" + o["questions"]
    for line in blob.split("\n"):
        line = line.strip()
        if needle in line:
            return line
    raise SystemExit("NOT FOUND in #%s: %r" % (o["url"], needle))


rows = []


def add(idx, needle, qtype, rnd, role="quant_developer", round_name=None, platform="unknown",
        section=None, answer=None, extra_doubt="", qtext=None):
    o = GOOD[idx]
    line = pick(o, needle)
    rows.append(dict(
        firm=firm_of(o["url"]),
        role_track=role,
        level=level_of(o),
        cycle="unknown",
        office=office_of(o),
        round=rnd,
        round_name=round_name or "",
        platform=platform,
        section_context=section,
        question_type=qtype,
        question_text=qtext or line,
        question_text_en=None,
        reported_answer=answer,
        source_url=o["url"],
        source_type="blog",
        source_quote=line,
        source_language="en",
        post_date=date_of(o),
        access="full_text",
        retrieval_method="webfetch",
        poster_context=("Anonymous jointaro (Taro) submission, job title as listed: '%s'; "
                        "location %s; experience dated %s. Process as reported: %s"
                        % (role_title(o), office_of(o), o["date"],
                           o["process"][:340].replace("\n", " "))),
        doubt=(TARO_DOUBT + (" " + extra_doubt if extra_doubt else "")),
    ))


# ------------------------------- Hudson River Trading -------------------------------
add(26, "Develop a data structure capable of efficiently handling", "coding_algorithms",
    "phone_technical", round_name="recruiter asked me to introduce myself, then directly asked an interview question",
    extra_doubt="The poster gives no round name beyond 'the recruiter', so the round label is my reading of their process description.")
add(27, "Find the maximum width of two arrays without a tree", "coding_algorithms", "online_assessment",
    round_name="coding challenge", section="three questions in the initial coding challenge",
    extra_doubt="'Maximum width of two arrays without a tree' is garbled enough that the underlying problem is not reconstructable.")
add(27, "Minimum steps to reach a binary number to zero", "coding_algorithms", "online_assessment",
    round_name="coding challenge", section="second of three questions in the coding challenge")
add(30, "Find the k largest values in an array in average time O(n)", "coding_algorithms",
    "phone_technical", round_name="technical phone interview",
    section="preceded by an automated coding test with three questions in C++, LeetCode Easy to Medium")
add(39, "Implement a pool allocator in C++", "coding_algorithms", "onsite",
    round_name="virtual on-site interview",
    section="OA (3 easy-medium problems), then first round, then virtual on-site; all coding in C++",
    extra_doubt="The poster accepted an offer, which usually means better recall, but they do not say which of the two interview rounds this question came from.")
add(57, "requirements to create a concurrent framework", "coding_algorithms", "phone_technical",
    round_name="interview was held online, but without a camera")
add(81, "Build a game (Lines and Squares)", "coding_algorithms", "phone_technical",
    round_name="C++ implementation question",
    section="the OA was LeetCode Mediums; this was the live C++ implementation round",
    extra_doubt="The poster explicitly forgot the game's name, so the problem cannot be pinned down.")
add(101, "Write a program that can add two binary strings", "coding_algorithms", "online_assessment",
    round_name="Online assessment with 4 parts", section="Online assessment with 4 parts")
add(101, "Complete the calculator class", "coding_algorithms", "online_assessment",
    round_name="Online assessment with 4 parts", section="Online assessment with 4 parts")
add(112, "Design an abstract class for task scheduling", "coding_algorithms", "phone_technical",
    round_name="first-round interview",
    section="first round: an operating systems design question and a LeetCode Medium BFS problem")
add(127, "Design a system that can process transactions", "coding_algorithms", "onsite",
    round_name="multiround, with each round mainly technical")
add(140, "What happens in the synthesis stage of building an FPGA design", "other", "phone_technical",
    round_name="technical interviews covering FPGAs and how they work under the hood",
    section="preceded by a SystemVerilog programming task",
    extra_doubt="This is the hardware/FPGA track, so it is only quant-adjacent.")
add(143, "the balanced tree started as basically", "coding_algorithms", "onsite",
    round_name="First round was algorithms, balanced trees",
    section="1 hour, 15 minutes per interview; four rounds: balanced trees, K-d tree internals, OS, networking",
    extra_doubt="The poster is describing the shape of a question progression rather than quoting a prompt, so there is no single verbatim question.")
add(160, "Minimum distance between houses (DFS)", "coding_algorithms", "online_assessment",
    round_name="Super long coding assessment that is automatically given to you")
add(198, "How to write a buffered reader", "coding_algorithms", "phone_technical",
    round_name="Two phone interviews", section="two phone interviews of about 45 minutes each over Zoom, ranging from programming to math")
add(223, "Implement a front-end interface for virtual credit card generation", "coding_algorithms",
    "online_assessment", round_name="OA",
    extra_doubt="A front-end credit-card UI task is an odd fit for HRT and the poster gives no further detail.")
add(243, "Design concurrent framework and contact tracing graph problem", "coding_algorithms",
    "phone_technical", round_name="1-hour phone screen", platform="CodeSignal",
    section="3-hour Codesignal OA followed by a 1-hour phone screen")
add(254, "Design a task switching algorithm", "coding_algorithms", "phone_technical",
    round_name="Difficult interview",
    extra_doubt="The poster says they could not understand the interviewer's accent or the question, so their rendering of it is unreliable.")
add(267, "Design a two-stage pipelined ALU", "other", "take_home",
    round_name="A one-week take-home assessment for an ALU design with a two-stage pipeline design",
    section="one-week take-home, then two one-hour phone interviews",
    extra_doubt="Hardware engineering track, not a quant role.")

# ------------------------------- Jump Trading -------------------------------
add(76, "Given a char buffer[4096], write a malloc implementation", "coding_algorithms", "onsite",
    role="quant_developer", round_name="multiple sessions",
    extra_doubt="The poster is openly hostile ('they were just farming me for trading strategies') and says they are publishing the questions out of spite, which is a motive both to remember accurately and to embellish.")
add(76, "Given a dependency graph, write a function to return a vector of all nodes", "coding_algorithms",
    "onsite", round_name="multiple sessions",
    extra_doubt="Same hostile poster as the other four questions from this page.")
add(76, "Two players are playing a game where you can pick either 1 or 2", "logic_brainteaser", "onsite",
    round_name="multiple sessions",
    extra_doubt="A classic Nim-style subtraction game that also appears in textbooks; the poster's grudge is the main reason to doubt the list.")
add(76, "Write a dot product of 1,000,000 numbers", "coding_algorithms", "onsite",
    round_name="multiple sessions",
    extra_doubt="Highly specific to Jump's low-latency work, which argues for authenticity, but the poster is aggrieved.")
add(76, "Take an integer, sum the square of its digits", "coding_algorithms", "onsite",
    round_name="multiple sessions",
    extra_doubt="This is the 'happy number' idea scaled to a counting problem; jointaro separately lists 'Happy Number' as a Jump question, which may be the same recall recycled.")
add(82, "Two people were playing a game to find words from a dictionary", "coding_algorithms",
    "phone_technical", round_name="first round was an interview with two software engineers",
    section="one coding question requiring recursion, around 30 minutes; no online assessment")
add(86, "Geometric distribution expectation", "probability", "phone_technical",
    round_name="45-minute first-round interview",
    section="45-minute first round on campus, two questions")
add(86, "Finding the first instance of a specific value in a sorted list", "coding_algorithms",
    "phone_technical", round_name="45-minute first-round interview")
add(132, "Design a linked list class", "coding_algorithms", "onsite",
    round_name="four interviews throughout the day",
    section="on-campus first round, then a full day of four interviews at the Chicago office")
add(132, "Swap two variables without using a temp", "logic_brainteaser", "onsite",
    round_name="four interviews throughout the day")
add(144, "Implement decorator in Python", "coding_algorithms", "phone_technical",
    round_name="Interview questions seemed quite random, but mostly LeetCode type")
add(151, "Given a sequence A of length n (n<=100000)", "coding_algorithms", "online_assessment",
    round_name="OA: 3 algorithm problems (easy, medium, medium-hard)",
    section="3 algorithm problems; 'you will fail if you do not get all 3 problems accepted'")
add(172, "Efficient implementation of a lazily initialized singleton in C++", "coding_algorithms",
    "phone_technical", round_name="technical phone interview",
    section="online programming challenge, then technical phone interview, then on-site in London")
add(181, "Prime number factorization, C# Caesar cipher", "coding_algorithms", "onsite",
    round_name="in-person short coding interview, then a longer coding interview",
    extra_doubt="Two problems are compressed into one line, so neither statement is complete.")
add(190, "Write code for the Nth Fibonacci number", "coding_algorithms", "phone_technical",
    round_name="Technical phone interview")
add(190, "For a 2-level nested loop iterating a 2D array", "other", "onsite",
    round_name="On-site interview")
add(193, "Given two lists of tuples representing time series data", "coding_algorithms",
    "phone_technical", round_name="first-round interview",
    section="CV screen, OA, first-round interview, then an onsite with three separate interviews")
add(197, "There was a string of postfix expressions", "coding_algorithms", "onsite",
    round_name="tech round", section="1 hour, one technical question, pen and whiteboard")

# ------------------------------- DRW -------------------------------
add(43, "How would you find all the words that are anagrams of each other", "coding_algorithms",
    "phone_technical", round_name="technical phone interview")
add(58, "Given some multithreaded code in C++, explain the flow and result", "coding_algorithms",
    "phone_technical", round_name="45-minute technical interview",
    section="45-minute technical interview covering concurrency and pointers in C++, then CV questions")
add(60, "Find the number of 1s in 11^n", "coding_algorithms", "online_assessment",
    round_name="coding test", platform="unknown",
    section="Codility, two hours, three tasks; first two graded on correctness, third on efficiency",
    extra_doubt="A one-line paraphrase; whether the intended reading is the digit '1' in the decimal expansion of 11^n or set bits is unclear.")
add(89, "Get the travel fee for those days", "coding_algorithms", "online_assessment",
    round_name="2.5 hour coding assessment that required access to the video and audio",
    section="2.5 hour proctored coding assessment with video and audio",
    extra_doubt="The question is reduced to a seven-word fragment with no problem statement.")
add(91, "One is about k-NN, and the other one is solving a math question by coding", "ml_modeling",
    "online_assessment", role="quant_researcher", round_name="online assessment",
    section="two questions, 70 minutes",
    extra_doubt="Listed role is 'ML/AI Intern', which I mapped to quant_researcher; DRW may treat that as a distinct track.")
add(123, "Maximum product subarray with a twist", "coding_algorithms", "online_assessment",
    round_name="Codility programming challenge",
    section="two questions, 3 days to complete; first LeetCode easy on trees, second LeetCode medium")
add(134, "Coin game: board divided in quarters", "logic_brainteaser", "onsite",
    round_name="30 minute puzzle interview",
    section="on-site day: 1-hour unit-testing interview, then a 30-minute puzzle interview, then lunch and a conversation round",
    answer=None,
    extra_doubt="This is the classic 'four coins on a rotating table' puzzle that predates quant interviewing and appears in puzzle anthologies; what supports it here is the unusually detailed dated first-person on-site account around it.")
add(134, "Second question: between each of your turns, the board will be rotated", "logic_brainteaser",
    "onsite", round_name="30 minute puzzle interview",
    extra_doubt="Same textbook-overlap caveat as the base coin puzzle; the poster says they never solved it.")
add(158, "OA LeetCode medium-hard: 3 questions within 150 minutes", "coding_algorithms",
    "online_assessment", round_name="OA", section="3 questions within 150 minutes",
    extra_doubt="This records the OA's shape, not any actual question.")
add(213, "Sort through a list of ones and zeros only by swapping two adjacent values",
    "coding_algorithms", "phone_technical",
    round_name="technical interview with a group of engineers via video")
add(218, "How would you derive the Ordinary Least Squares", "statistics_regression", "onsite",
    role="quant_researcher", round_name="virtual onsite interview",
    section="three back-to-back rounds of 45 minutes each",
    extra_doubt="Listed role is 'Junior AI Researcher' in India; this is a research track but not necessarily DRW's core quant research pipeline.")
add(218, "Dimensionality reduction techniques, PCA", "ml_modeling", "onsite",
    role="quant_researcher", round_name="virtual onsite interview")
add(218, "NLP and transformer-related questions", "ml_modeling", "onsite",
    role="quant_researcher", round_name="virtual onsite interview")
add(237, "How to make a class in C++ hashable", "coding_algorithms", "phone_technical",
    round_name="interview call")
add(276, "Graph, shortest path", "coding_algorithms", "online_assessment",
    round_name="Online assessment with three coding questions",
    section="2.5 hours for three coding challenges; candidate writes their own test cases")

# ------------------------------- Akuna Capital -------------------------------
add(44, "Give a function that takes a list of bowling frames", "coding_algorithms", "onsite",
    round_name="in-person code pair interview",
    section="an easy HackerRank round, then an in-person code pair interview")
add(61, "DSU, calculate the parity of ones in an int32", "coding_algorithms", "phone_technical",
    round_name="online pair coding session lasting one and a half hours, featuring three questions",
    section="three questions in 1.5 hours",
    extra_doubt="Corroborates the same 'parity of ones in an int' problem reported independently on Nowcoder for Akuna, which is either strong confirmation or a widely circulated recall.")
add(75, "The HackerRank had 13 or so pretty in-depth C++ questions", "coding_algorithms",
    "online_assessment", platform="HackerRank", round_name="SWEI C++ HackerRank",
    section="~13 in-depth C++ questions plus two C++ OOP coding questions",
    extra_doubt="Describes the paper's composition rather than reproducing a question.")
add(96, "Possible strategies for a battleship player", "coding_algorithms", "onsite",
    round_name="third round was a Zoom interview",
    section="Part one a systems design question on retrieving product data and a low-latency 'buy low, sell high' system; part two a HackerRank-style Battleships question")
add(115, "The first round of OA focused on Binary Search and Sliding Window", "coding_algorithms",
    "online_assessment", round_name="two rounds of online assessments",
    section="two OAs, one technical interview, one behavioral interview",
    extra_doubt="Topic list, not a question.")
add(121, "How can we get the output of the combination of two strings", "coding_algorithms",
    "online_assessment", round_name="one online code assessment",
    section="around 60 minutes, Python only, three questions on strings, dictionaries and arrays")
add(126, "Find the maximum number of points in a polygon with a maximum perimeter",
    "coding_algorithms", "online_assessment", platform="HackerRank",
    round_name="HackerRank test", section="designed to take two hours; 'we don't expect you to finish necessarily'")
add(146, "Detect collinearity", "coding_algorithms", "online_assessment", platform="HackerRank",
    round_name="online interview", section="three questions on HackerRank",
    extra_doubt="The poster applied for the Quantitative Development Internship, Summer 2019 but says the application was moved to the equivalent full-time role, so the level label is genuinely ambiguous.")
add(146, "Market equilibrium", "coding_algorithms", "online_assessment", platform="HackerRank",
    round_name="online interview", section="three questions on HackerRank",
    extra_doubt="Two words only; no problem statement. Same internship/full-time ambiguity as the other questions on this page.")
add(159, "What does the pickle module do", "coding_algorithms", "phone_technical",
    round_name="phone interview", section="applied for the Python Developer internship for Summer 2020")
add(159, "What's the difference between is and ==", "coding_algorithms", "phone_technical",
    round_name="phone interview")
add(168, "Implement a String object without using std::string", "coding_algorithms",
    "phone_technical", round_name="phone screen",
    section="first step a 90-minute HackerRank with multiple-choice and 3-4 coding problems; the phone screen was OOP-centred")
add(203, "Write code to shuffle a 52-card deck", "coding_algorithms", "onsite",
    round_name="called me to their office in Champaign")
add(206, "They asked me about my mental math skills", "mental_math_speed", "online_assessment",
    round_name="mental math test",
    section="'First, they asked me to do a mental math test' before the HackerRank OA",
    extra_doubt="Evidence that Akuna front-loads a mental-math test, but the poster reproduces no actual arithmetic item.")
add(216, "Given two lists of exchange records", "coding_algorithms", "online_assessment",
    platform="HackerRank", round_name="OA",
    section="three coding questions in 75 minutes on HackerRank; one easy, one medium, one hard")
add(221, "Implement Binary Tree Right Side View", "coding_algorithms", "phone_technical",
    round_name="two medium LeetCode problems")
add(233, "bowling scorecard", "coding_algorithms", "onsite", round_name="final round",
    section="HackerRank round, then a technical phone screen with LeetCode Medium-Hard graph questions, then a final round",
    extra_doubt="A bowling-scorecard problem is independently reported for Akuna in a 2019 New Zealand write-up on the same site, so either Akuna reuses it for years or Taro's entries echo each other.")
add(258, "The total number of topological sorts in a graph", "combinatorics", "online_assessment",
    round_name="OA", section="5 questions: two coding questions and three theory questions")
add(268, "Task to determine how long it will take a swarm of drones", "coding_algorithms",
    "online_assessment", platform="HackerRank", round_name="coding challenge on HackerRank",
    section="two hours, four questions on algorithms, optimization, machine learning and string operations")
add(268, "Classify new trades based on their similarity to old trades", "ml_modeling",
    "online_assessment", platform="HackerRank", round_name="coding challenge on HackerRank",
    section="two hours, four questions")
add(273, "Order matching question, not like LeetCode at all", "coding_algorithms",
    "phone_technical", round_name="CoderPad link",
    extra_doubt="Describes the flavour of the question ('very specific to trading/order making') without stating it.")
add(279, "Expected to perform 2's complement", "coding_algorithms", "online_assessment",
    round_name="online assessment", section="within 2 hours",
    extra_doubt="Describes the OA's contents rather than a specific question.")

# ------------------------------- Two Sigma -------------------------------
add(52, "They asked me a probability question about weighted dice", "probability", "onsite",
    role="quant_developer", round_name="onsite interview",
    extra_doubt="The poster describes the topic ('weighted dice and the estimated value of each scenario') without giving the numbers, so the question is not reconstructable.")
add(73, "Create your own random number generator given specific requirements", "coding_algorithms",
    "onsite", round_name="onsite", platform="HackerRank",
    section="HackerRank phone screen with coding questions, then onsite")
add(110, "Give the dependency completion order", "coding_algorithms", "phone_technical",
    round_name="first technical interview",
    section="initial OA, first technical interview, then onsite")
add(131, "You were given a table with four currencies", "coding_algorithms", "onsite",
    round_name="3 rounds of coding questions",
    section="round 1 a buggy linked list and binary tree; round 2 a maximization problem; round 3 'dealt with actual trading'")
add(141, "Encode and decode a Huffman tree", "coding_algorithms", "phone_technical",
    round_name="live technical interview, which was a LeetCode hard", platform="HackerRank",
    section="first an online coding assessment on HackerRank (two LeetCode mediums), then a live technical interview")
add(155, "How to implement Huffman coding trees", "coding_algorithms", "phone_technical",
    round_name="1-on-1 coding interview")
add(170, "The question was to implement your own hashmap", "coding_algorithms", "phone_technical",
    round_name="first round of the technical interview",
    section="purely coding; no self-introductions, system design questions or resume inquiries")
add(180, "Question about creating slotted memory and storing data in C", "coding_algorithms",
    "phone_technical", round_name="first round of the interview")
add(207, "Implement malloc using an array", "coding_algorithms", "phone_technical",
    round_name="phone screen",
    section="75-minute online assessment, then a phone screen with one hour for one problem, then a 3-hour technical and a 3-hour behavioral")
add(219, "How do you pick random objects given weights", "probability", "phone_technical",
    round_name="Interviews went great")
add(242, "Design a random number generator that does not output a number that has already been generated",
    "coding_algorithms", "online_assessment", platform="HackerRank",
    round_name="HackerRank coding challenge",
    section="HackerRank focused on string manipulation with many test cases and memory limits")
add(282, "How to debug a binary tree", "coding_algorithms", "phone_technical",
    round_name="Technical interview for first-year program",
    section="video call with a Two Sigma SWE, walking through a coding problem in their IDE")

# ------------------------------- D. E. Shaw -------------------------------
add(63, "How to find the intersection of two linked lists", "coding_algorithms", "phone_technical",
    round_name="interview", section="OA of 3 medium-difficulty questions, then an interview with 3 easy-to-medium questions")
add(66, "Given an array of n integers and an integer x", "coding_algorithms", "phone_technical",
    round_name="one technical interview over the phone")
add(118, "A couple of open-ended problems that required some knowledge of basic ML techniques",
    "ml_modeling", "onsite", round_name="virtual onsite",
    section="one-hour phone screen (30 min resume, 30 min LeetCode-style), then a virtual onsite",
    extra_doubt="Names the topics of the open-ended problems without stating any of them.")
add(191, "how would you color a 3-colorable graph", "coding_algorithms", "onsite",
    round_name="five rounds of interviews and an off-the-record lunch discussion",
    answer="I was initially thinking that you had to do something efficient, which isn't possible. But he just wanted some way of doing it.",
    extra_doubt="Dated 2013, so it says nothing about D. E. Shaw's current internship loop.")
add(210, "Find the median of an unsorted list", "coding_algorithms", "phone_technical",
    round_name="first-round interview")
add(212, "What's the probability that the second child is a boy?", "probability", "phone_technical",
    role="quant_researcher",
    round_name="phone interview ... to have pencil and paper ready",
    section="two brain teasers, no coding",
    extra_doubt="This is the canonical boy-girl paradox found in every probability textbook; what makes it worth keeping is the dated first-person account of it being asked, plus the harder 'named William' follow-up which is a much rarer variant.")
add(212, "one of their children's names is William", "probability", "phone_technical",
    role="quant_researcher",
    round_name="phone interview ... to have pencil and paper ready",
    section="the second, '(Much harder)', of two brain teasers",
    extra_doubt="The 'William' variant is a known Gary Foshee-style puzzle, so it is textbook-adjacent, but a 2013 first-person recall attests it here. Role title on the page is 'Software Engineering and Quantitative Research', so the track is genuinely mixed.")

with io.open(OUT, "w", encoding="utf-8") as f:
    for r in rows:
        r.pop("level_hint", None)
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print("wrote", len(rows), "->", OUT)
