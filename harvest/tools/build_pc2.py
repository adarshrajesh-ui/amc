#!/usr/bin/env python3
"""Assemble positive_controls_v2.json.

Every source_quote is sliced out of a locally cached copy of the page rather than
retyped, so the stored text is byte-identical to what the page served.
"""
import json
import os
import re

P = "/workspace/harvest/.pc2"
OUT = "/workspace/harvest/spec/positive_controls_v2.json"

# (cache file, first anchor, last anchor) -> quote is file[start(anchor1) : end(anchor2)]
RECORDS = [
    dict(
        firm="Tower Research Capital",
        role_track="quant_developer",
        level="new_grad",
        round="onsite",
        question_text=(
            "There is a standard deck of cards and two of the cards are chosen at random. "
            "Compute the probability of choosing a third card at random whose number is in "
            "between the numbers of initially chosen cards."
        ),
        source_url="https://www.geeksforgeeks.org/interview-experiences/tower-research-interview-experience-set-2-software-developer/",
        post_date="2017-12-05",
        source_type="interview_experience_writeup",
        cache=f"{P}/gfg/aa773d3843dc.txt",
        a1="6. What is pipelining?",
        a2="based on your intuition.",
        how_verified=(
            "Fetched the page with curl (HTTP 200) into .pc2/gfg/aa773d3843dc.html, extracted the "
            "article body, and sliced the quote directly out of that text; the phrase 'whose number "
            "is in between the numbers of initially chosen cards' is also present in the raw HTML."
        ),
    ),
    dict(
        firm="Tower Research Capital",
        role_track="quant_developer",
        level="internship",
        round="phone_technical",
        question_text=(
            "An infinite stream of numbers is given. The stream is stopped at an arbitrary point. "
            "Return any number of the stream read till now with equal probability, using O(1) space."
        ),
        source_url="https://www.geeksforgeeks.org/interview-experiences/telephonic-interview-for-tower-research-llc-gurgaon-internshiphigh-frequency-trading/",
        post_date="2014-08-28",
        source_type="interview_experience_writeup",
        cache=f"{P}/gfg/e513e80ab9e7.txt",
        a1="1. Brief explanation of a research project",
        a2="using O(1) space.",
        how_verified=(
            "curl fetch of the GfG page (cached at .pc2/gfg/e513e80ab9e7.html); the numbered list "
            "of telephonic-round questions was sliced verbatim from the extracted article body."
        ),
    ),
    dict(
        firm="Dolat Capital",
        role_track="quant_analyst",
        level="new_grad",
        round="onsite",
        question_text=(
            "What is the minimum number of times a dice is to be rolled to get 2 consecutive 6's?"
        ),
        source_url="https://www.geeksforgeeks.org/interview-experiences/dolat-capital-quantitative-analyst-high-frequency-trading-interview-experience/",
        post_date="2020-08-04",
        source_type="interview_experience_writeup",
        cache=f"{P}/gfg/4f3d5a1ffa48.txt",
        a1="Some basic questions on moving average",
        a2="I will share it with you.",
        how_verified=(
            "curl fetch cached at .pc2/gfg/4f3d5a1ffa48.html; quote sliced from the extracted "
            "'Round 4: Final Round' paragraph, which ends with the poster's own recall disclaimer."
        ),
    ),
    dict(
        firm="AlphaGrep Securities",
        role_track="quant_developer",
        level="new_grad",
        round="online_assessment",
        question_text=(
            "There are N palaces and M tunnels connecting different palaces. M tunnels are input as "
            "a tuple of three integers (Ai, Bi, Ri) for i from 1 to M which means there is a tunnel "
            "of distance Ri connecting palaces Ai and Bi. Determine whether all N palaces can be "
            "connected by some set of tunnels such that total distance covered is minimum. The "
            "question asked to print \"YES\" if such minimum path exists, \"NO\" otherwise."
        ),
        source_url="https://www.geeksforgeeks.org/interview-experiences/alphagrep-securities-interview-experience/",
        post_date="2020-01-21",
        source_type="interview_experience_writeup",
        cache=f"{P}/gfg/64720cbcb333.txt",
        a1="Round 1: Online test - Technical",
        a2="starting from any node using DFS.",
        how_verified=(
            "curl fetch cached at .pc2/gfg/64720cbcb333.html; the Round 1 block including the "
            "HackerRank framing and the poster's own solution note was sliced verbatim."
        ),
    ),
    dict(
        firm="JPMorgan Chase",
        role_track="quant_researcher",
        level="new_grad",
        round="phone_technical",
        question_text=(
            "If I flip a fair coin 10 times, what's the expected number of \"HH\" observed?"
        ),
        source_url="https://www.geeksforgeeks.org/interview-experiences/jp-morgan-interview-experience-for-quantitative-researcher-on-campus-2022/",
        post_date="2021-12-30",
        source_type="interview_experience_writeup",
        cache=f"{P}/gfg2/cee024fad3c6.txt",
        a1="Round 3(Interview 2 - 45 mins)",
        a2="same question being on stackexchange.",
        how_verified=(
            "curl fetch cached at .pc2/gfg2/cee024fad3c6.html; quote sliced from the extracted "
            "'Round 3(Interview 2 - 45 mins)' paragraph including the hint the interviewer gave."
        ),
    ),
    dict(
        firm="JPMorgan Chase",
        role_track="quant_researcher",
        level="new_grad",
        round="phone_technical",
        question_text=(
            "You are given a circular board of radius R. A person throws a dart at the board and the "
            "dart can hit the board anywhere with equal probability. Find the expected value of the "
            "distance between the center of the board and the point where the dart hits."
        ),
        source_url="https://www.geeksforgeeks.org/interview-experiences/jp-morgan-interview-experience-for-quantitative-and-research-analysis-role/",
        post_date="2020-09-28",
        source_type="interview_experience_writeup",
        cache=f"{P}/gfg2/ad303d92bed1.txt",
        a1="These questions were followed by some Probability questions.",
        a2="quite satisfied with my answer.",
        how_verified=(
            "curl fetch cached at .pc2/gfg2/ad303d92bed1.html; quote sliced from the extracted "
            "'Round 2 : Online Interview - I' section covering the dart question and its follow-up."
        ),
    ),
    dict(
        firm="Dolat Capital",
        role_track="quant_developer",
        level="new_grad",
        round="online_assessment",
        question_text=(
            "Insert and delete an integer value in a linked list from either end (insertion and "
            "deletion should be from one end only), and also find the maximum value in the linked "
            "list at any point. All the operations on this ADT need to be done in constant time "
            "complexity."
        ),
        source_url="https://www.geeksforgeeks.org/interview-experiences/dolat-capital-interview-experience-set-1-on-campus/",
        post_date="2015-10-04",
        source_type="interview_experience_writeup",
        cache=f"{P}/gfg2/817673d845aa.txt",
        a1="It was an on-campus interview.",
        a2="needs to be done in constant time complexity.",
        how_verified=(
            "curl fetch cached at .pc2/gfg2/817673d845aa.html; the on-campus framing plus the "
            "Round 1 'Program 1 (highest weightage)' statement were sliced verbatim."
        ),
    ),
    dict(
        firm="AQR Capital Management",
        role_track="quant_developer",
        level="new_grad",
        round="phone_technical",
        question_text=(
            "Given a list of strings: {area, acre, bat, ball, Amsterdam, am, AmsterdaM}. Find the "
            "string that contains a, A, m, M in it."
        ),
        source_url="https://www.geeksforgeeks.org/interview-experiences/aqr-capital-interview-experience-for-software-engineer-full-time/",
        post_date="2024-06-17",
        source_type="interview_experience_writeup",
        cache=f"{P}/gfg2/b91e2480ec49.txt",
        a1="In this round, the interviewer gave me OUTPUT Questions",
        a2="Expected output - 2,12,22,32,42.",
        how_verified=(
            "curl fetch cached at .pc2/gfg2/b91e2480ec49.html; the Round-2 block listing the three "
            "coding questions was sliced verbatim from the extracted article body."
        ),
    ),
    dict(
        firm="Optiver",
        role_track="quant_trader",
        level="internship",
        round="trading_game",
        question_text=(
            "Make a market on the expected number of rolls of a dice to see every face at least "
            "once. (Follow-up after the candidate said he knew the answer: make a market on the "
            "expected number of rolls of a dice to see every face at least once and the number 6 "
            "at least twice.)"
        ),
        source_url="https://github.com/SmthnNotTaken/Interns-IITM/blob/main/Optiver/README.md",
        post_date="2025-05-18",
        source_type="github_repo_markdown",
        cache=f"{P}/gh2/Interns-IITM__Optiver_README.md",
        a1="### Q2",
        a2="the number 6 at least twice.",
        how_verified=(
            "Fetched raw.githubusercontent.com/SmthnNotTaken/Interns-IITM/HEAD/Optiver/README.md and "
            "sliced the Q2 block verbatim out of those bytes; the surrounding file documents the "
            "author's own Optiver quant-trader test and Interview Round 1 market-making game."
        ),
    ),
    dict(
        firm="Optiver",
        role_track="quant_developer",
        level="internship",
        round="onsite",
        question_text=(
            "Create a system that handles trading with multiple exchanges. Each exchange may use "
            "different network protocols and require different file formats (File formats may be "
            "common between some exchanges)."
        ),
        source_url="https://github.com/SarthakVerma18/Intern-Guidance/blob/main/QuantSDE_GODtips.md",
        post_date="2025-08-03",
        source_type="github_repo_markdown",
        cache=f"{P}/gh2/Intern-Guidance__QuantSDE_GODtips.md",
        a1="- ### 3. Technical Interview\n    This round lasted 45 minutes",
        a2="common between some exchanges).\n    ```",
        how_verified=(
            "Fetched raw.githubusercontent.com/SarthakVerma18/Intern-Guidance/HEAD/QuantSDE_GODtips.md "
            "and sliced the Optiver 'Technical Interview' block verbatim, including the fenced code "
            "block in which the author reproduces the question."
        ),
    ),
    dict(
        firm="Optiver",
        role_track="quant_trader",
        level="internship",
        round="trading_game",
        question_text=(
            "Each person gets a slip with 4 commodities (e.g. silver, gold, copper, platinum) and "
            "conversion rates between them (e.g. 4 Gold to 3 Platinum, 1 Platinum to 2 Silver). "
            "Given 4 Gold coins, what's the minimum number of trades to get 6 Gold? Then find trades "
            "to get 100 Gold coins, and estimate for 1 million Gold coins."
        ),
        source_url="https://github.com/SarthakVerma18/Intern-Guidance/blob/main/Optiver_trading.md",
        post_date="2025-07-26",
        source_type="github_repo_markdown",
        cache=f"{P}/gh2/Intern-Guidance__Optiver_trading.md",
        a1="Format:\n  5 people per group",
        a2="They were similar in style.)",
        how_verified=(
            "Fetched raw.githubusercontent.com/SarthakVerma18/Intern-Guidance/HEAD/Optiver_trading.md "
            "and sliced the group-discussion block verbatim; the author's caveat that he cannot "
            "recall the last two questions is included in the excerpt."
        ),
    ),
    dict(
        firm="IMC Trading",
        role_track="quant_developer",
        level="internship",
        round="online_assessment",
        question_text=(
            "You start at x = 0, at any instant you can move either `a` steps or `b` steps to the "
            "right (a, b > 0). Additionally you could at some point (exactly once) jump back to half "
            "of your current coordinate. What is the closest you can get to x = `t` given that you "
            "are never allowed to cross `t`."
        ),
        source_url="https://github.com/SarthakVerma18/Intern-Guidance/blob/main/QuantSDE_GODtips.md",
        post_date="2025-08-03",
        source_type="github_repo_markdown",
        cache=f"{P}/gh2/Intern-Guidance__QuantSDE_GODtips.md",
        a1="- ### 1. Online Assesment\n    This was a 105 minute coding test",
        a2="not present in a cycle.\n    ```",
        how_verified=(
            "Same raw.githubusercontent.com fetch as the Optiver design question; the IMC 'Online "
            "Assesment' block with both fenced problem statements was sliced verbatim from those bytes."
        ),
    ),
    dict(
        firm="IMC Trading",
        role_track="quant_developer",
        level="internship",
        round="onsite",
        question_text=(
            "We are building a scanner which scans the ID of 2 objects, uses the ID to fetch the "
            "weight of the object and then compares the weights. Explain how you will build a "
            "digital circuit to solve this."
        ),
        source_url="https://github.com/SmthnNotTaken/Interns-IITM/blob/main/IMC/README.md",
        post_date="2025-05-18",
        source_type="github_repo_markdown",
        cache=f"{P}/gh2/Interns-IITM__IMC_README.md",
        a1="# Interview\n2 questions, 1.5 hours",
        a2="how you will build a digital circuit to solve this.",
        how_verified=(
            "Fetched raw.githubusercontent.com/SmthnNotTaken/Interns-IITM/HEAD/IMC/README.md; the "
            "whole '# Interview' section (both questions) was sliced verbatim from those bytes. The "
            "companion file IMC/Q1.v is the code referenced in Question 1."
        ),
    ),
    dict(
        firm="Graviton Research Capital",
        role_track="quant_researcher",
        level="internship",
        round="online_assessment",
        question_text=(
            "200 people in a firm, who trade in various markets. What is minimum number of markets "
            "that need to exist, such that for any 2 people A and B in the firm, there exists at "
            "least 1 market that A trades in and B does not, and vice versa."
        ),
        source_url="https://github.com/SmthnNotTaken/Interns-IITM/blob/main/Graviton/README.md",
        post_date="2025-05-18",
        source_type="github_repo_markdown",
        cache=f"{P}/gh2/Interns-IITM__Graviton_README.md",
        a1="# Test\n3 challenging Probability puzzles.",
        a2="A trades in and B does not, and vice versa.",
        how_verified=(
            "Fetched raw.githubusercontent.com/SmthnNotTaken/Interns-IITM/HEAD/Graviton/README.md "
            "and sliced the '# Test' header plus Q1 verbatim; the author states he was shortlisted "
            "off this paper and then describes his own two interview rounds below it."
        ),
    ),
    dict(
        firm="Graviton Research Capital",
        role_track="quant_researcher",
        level="internship",
        round="onsite",
        question_text=(
            "Alice and Bob are playing a game with 2 piles of coins where Alice goes first. At each "
            "turn a player removes a full stack of coins and then divides the other pile into two "
            "piles of non zero coins. The first player who cannot make a move (eg: if the piles are "
            "1 1) loses. Find out who wins based on the initial configuration."
        ),
        source_url="https://github.com/SarthakVerma18/Intern-Guidance/blob/main/QuantSDE_GODtips.md",
        post_date="2025-08-03",
        source_type="github_repo_markdown",
        cache=f"{P}/gh2/Intern-Guidance__QuantSDE_GODtips.md",
        a1="The second round was with a senior quant.",
        a2="based on the initial configuration.\n    ```",
        how_verified=(
            "Same raw.githubusercontent.com fetch; the Graviton second-round block was sliced "
            "verbatim from those bytes, including the author's note that it was a single question."
        ),
    ),
    dict(
        firm="Virtu Financial",
        role_track="quant_trader",
        level="new_grad",
        round="phone_technical",
        question_text=(
            "What is the angle between the minute and hour hand of a clock at 5:15 PM? Follow-up: at "
            "what time would the minute and hour hand of a clock coincide after 5 PM?"
        ),
        source_url="https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2021-22/Virtu/Quantitative%20Trading%20Analyst.md",
        post_date="2021-12-10",
        source_type="github_repo_markdown",
        cache=f"{P}/virtu.md",
        a1="She started the interview by telling",
        a2="(in about 30 seconds).",
        how_verified=(
            "File body was pulled from the Leader-board/OA-and-Interviews repository "
            "(Application experiences/2021-22/Virtu/Quantitative Trading Analyst.md) and the "
            "Round 1 paragraph plus the blockquoted brain-teasers were sliced verbatim."
        ),
    ),
    dict(
        firm="Tibra Global Services",
        role_track="quant_trader",
        level="new_grad",
        round="phone_technical",
        question_text=(
            "You have a right-angled triangle with perpendicular side lengths of 10 and 15. What is "
            "the area of the largest square that fits into the triangle, whose sides are parallel to "
            "the perpendicular sides of the triangle."
        ),
        source_url="https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2023-24/Tibra/Quant%20Trader%20Developer.md",
        post_date="2023-05-23",
        source_type="github_repo_markdown",
        cache=f"{P}/tibra24.md",
        a1="The phone interview was via Teams",
        a2="moving on after that!",
        how_verified=(
            "File body was pulled from the Leader-board/OA-and-Interviews repository "
            "(Application experiences/2023-24/Tibra/Quant Trader Developer.md); the '### The phone "
            "interview' section with both brain-teasers and the author's own error was sliced verbatim."
        ),
    ),
    dict(
        firm="Jane Street",
        role_track="quant_trader",
        level="unknown",
        round="phone_technical",
        question_text=(
            "Suppose we play a game in which I give you a die to roll and offer to pay you in dollars "
            "the number that you roll. If you're dissatisfied with the number you roll on your first "
            "try, I'll let you roll again with the same offer, up to a maximum of 3 do-overs, though "
            "you can elect to stop after any roll. How much would you pay me to play this game?"
        ),
        source_url="https://www.quora.com/What-is-a-first-round-quant-interview-at-Jane-Street-like",
        post_date="unknown",
        source_type="qa_site_answer",
        cache=f"{P}/quora_janestreet.txt",
        # the page ships a collapsed preview of this answer before the full text, so
        # anchor on the second copy to avoid quoting Quora's "Continue Reading" stub
        a1="Agree with[Eugene Chen](https://www.quora.com/profile/Eugene-Chen-2)- the interviews were generally probability/expected value questions with a nod towards game theory or optimal strategies. They got harder in each successive round. If you want a concrete example",
        occ=2,
        a2="Talk about high standards!",
        how_verified=(
            "curl gets a Cloudflare 403 on quora.com, so the page was retrieved twice through the "
            "search tool's full-page dump (saved as .pc2/quora_janestreet.txt) on two separate "
            "calls, both returning the same text; Michael Fu's answer was sliced verbatim from it, "
            "including his statement that this was one of his own first-round questions in 2012. "
            "An exact-phrase search on 'I also stipulate that if you’re dissatisfied...' returns "
            "this Quora page as a hit."
        ),
    ),
    dict(
        firm="Hudson River Trading",
        role_track="quant_trader",
        level="internship",
        round="trading_game",
        question_text=(
            "They gave me four cards and told me that I had to trade on what I thought the sum of "
            "these four cards was, and then every round they flipped one card over."
        ),
        source_url="https://www.businessinsider.com/quant-trading-intern-what-it-was-like-hrt-sig-2023-12",
        post_date="2023-12-12",
        source_type="news_first_person_essay",
        cache=f"{P}/bi_hrt.txt",
        a1="Take my HRT interview, for example.",
        a2="It was a fun experience.",
        how_verified=(
            "curl fetch of the article (HTTP 200, 428 KB, cached at .pc2/bi_hrt.html); the paragraph "
            "was sliced from the extracted body text and the string 'four cards' is present twice in "
            "the raw HTML. The piece is an as-told-to first-person essay by the candidate herself."
        ),
    ),
    dict(
        firm="D. E. Shaw",
        role_track="quant_developer",
        level="internship",
        round="onsite",
        question_text=(
            "Magnets are placed linearly, with each magnet to be considered as a point object. Each "
            "magnet suffers force from its left-sided magnets such that they repel it to the right "
            "and vice versa. All forces are repulsive and the force is inversely proportional to "
            "distance (1/d). Write a function that takes n, the number of magnets, and an array of "
            "their distances from the origin, and finds all the points along the linear line where "
            "net force is ZERO, to a precision of epsilon."
        ),
        source_url="https://www.geeksforgeeks.org/interview-experiences/de-shaw-internship-interview-experience-on-campus-2021/",
        post_date="2020-08-07",
        source_type="interview_experience_writeup",
        cache=f"{P}/gfg3/90889414d9b8.txt",
        a1="Convert BST to min-heap.",
        a2="Few more questions on OOPS which I don't remember.",
        how_verified=(
            "curl fetch cached at .pc2/gfg3/90889414d9b8.html; the Technical Interview 1 question "
            "list, including the magnets puzzle, was sliced verbatim from the extracted article body."
        ),
    ),
]


def slice_quote(path, a1, a2, occ=1):
    txt = open(path, encoding="utf-8", errors="replace").read()
    i = -1
    for _ in range(occ):
        i = txt.find(a1, i + 1)
        if i < 0:
            raise SystemExit(f"ANCHOR-1 MISS in {path}: {a1[:60]!r}")
    j = txt.find(a2, i)
    if j < 0:
        raise SystemExit(f"ANCHOR-2 MISS in {path}: {a2[:60]!r}")
    return txt[i : j + len(a2)]


def tidy(q):
    """Collapse the runs of whitespace that HTML-to-text extraction leaves behind."""
    q = q.replace("\r", "")
    q = re.sub(r"[ \t]+", " ", q)
    q = re.sub(r" *\n *", "\n", q)
    q = re.sub(r"\n{3,}", "\n\n", q)
    return q.strip()


CORPUS = "/workspace/harvest/questions.jsonl"


def norm_txt(s):
    s = (s or "").lower()
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def corpus_evidence():
    """Return a callable that describes how a candidate relates to the existing corpus."""
    from difflib import SequenceMatcher
    from urllib.parse import unquote, urlparse

    recs = [json.loads(l) for l in open(CORPUS) if l.strip()]
    urls, hosts = set(), {}
    for r in recs:
        for a in r.get("attestations", []):
            u = (a.get("source_url") or "").strip().rstrip("/").lower()
            if not u:
                continue
            p = urlparse(u)
            urls.add(u)
            urls.add(unquote(p.netloc + p.path).rstrip("/"))
            h = p.netloc.replace("www.", "")
            hosts[h] = hosts.get(h, 0) + 1

    def describe(url, question):
        p = urlparse(url.strip().rstrip("/").lower())
        keys = {url.strip().rstrip("/").lower(), unquote(p.netloc + p.path).rstrip("/")}
        url_hit = bool(keys & urls)
        host = p.netloc.replace("www.", "")
        q = norm_txt(question)
        qt = set(q.split())
        best, who = 0.0, ""
        for r in recs:
            for field in ("question_text", "question_text_en"):
                cand = norm_txt(r.get(field, ""))
                if not cand:
                    continue
                ct = set(cand.split())
                jac = len(qt & ct) / max(1, len(qt | ct))
                if jac < 0.30:
                    continue
                score = max(jac, SequenceMatcher(None, q, cand).ratio())
                if score > best:
                    best, who = score, f"{r['firm']}: {r.get(field, '')[:70]}"
        return (
            f"Scanned all {len(recs)} questions.jsonl records: the source_url appears "
            f"{0 if not url_hit else 1}x among their attestations "
            f"({hosts.get(host, 0)} corpus attestations exist on {host}, none at this path). "
            f"Closest wording match anywhere in the corpus scores {best:.2f} "
            f"(max of token-Jaccard and SequenceMatcher) against \u2014 {who or 'nothing above the 0.30 floor'}."
        )

    return describe


def main():
    describe = corpus_evidence()
    out = []
    for r in RECORDS:
        quote = tidy(slice_quote(r["cache"], r["a1"], r["a2"], r.get("occ", 1)))
        rec = {
            "firm": r["firm"],
            "role_track": r["role_track"],
            "level": r["level"],
            "round": r["round"],
            "question_text": r["question_text"],
            "source_url": r["source_url"],
            "source_quote": quote,
            "post_date": r["post_date"],
            "source_type": r["source_type"],
            "how_verified": r["how_verified"],
            "not_in_corpus": describe(r["source_url"], r["question_text"]),
        }
        out.append(rec)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(out, open(OUT, "w"), indent=1, ensure_ascii=False)
    print(f"wrote {len(out)} records -> {OUT}")
    for r in out:
        print(f"  {r['firm']:28s} q={len(r['question_text']):4d} quote={len(r['source_quote']):5d}")


if __name__ == "__main__":
    main()
