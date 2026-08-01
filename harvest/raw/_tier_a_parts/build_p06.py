import json, io

OUT = "/workspace/harvest/raw/_tier_a_parts/p06_deshaw.jsonl"

U_OFF = "https://www.geeksforgeeks.org/interview-experiences/de-shaw-off-campus-fresher-interview-experience/"
U_21 = "https://www.geeksforgeeks.org/interview-experiences/de-shaw-interview-experience-for-2021-internship-on-campus/"
U_19 = "https://www.geeksforgeeks.org/interview-experiences/de-shaw-on-campus-internship-interview-experience-2019/"

GFG_DOUBT_BASE = ("GeeksforGeeks 'interview experiences' posts are user-submitted and unverified by the site; "
                  "this is also D. E. Shaw India's technology/software track, NOT the US quant researcher or "
                  "trader pipeline, so it should not be read as evidence about D. E. Shaw quant hiring.")

POSTER_OFF = ("Anonymous candidate who applied off-campus via deshawindia.com/careers ('I applied through their careers page "
              "https://www.deshawindia.com/careers/work-with-us'); received an offer at the end. Page last updated 15 Jul 2025; "
              "the interview itself is undated.")
POSTER_21 = ("Anonymous student at an Indian engineering college; 'DE Shaw organized an on-campus recruitment drive for "
             "2-months software development internship.' 2 of 250 students cleared the OA; poster was rejected after the final round.")
POSTER_19 = ("Anonymous student; DE Shaw on-campus summer internship program (SIP) 2019, 250+ sat the aptitude round, "
             "CGPA cutoff 7 for COMP/IT and 7.5 for other electrical branches; poster received the internship offer.")

rows = []


def add(**kw):
    base = dict(firm="D. E. Shaw", role_track="unknown", level="unknown", cycle="unknown", office="unknown",
                round="unknown", round_name="", platform="unknown", section_context=None,
                question_type="other", question_text="", question_text_en=None, reported_answer=None,
                source_url="", source_type="blog", source_quote="", source_language="en",
                post_date="unknown", access="full_text", retrieval_method="webfetch",
                poster_context="", doubt="")
    base.update(kw)
    rows.append(base)


# ---------------- Off-campus fresher (new grad), D. E. Shaw India ----------------
OFF = dict(source_url=U_OFF, level="new_grad", role_track="quant_developer", office="India",
           poster_context=POSTER_OFF, post_date="unknown", source_type="blog")

add(**OFF, round="online_assessment", round_name="Hackerrank Test",
    platform="HackerRank",
    section_context="The test was for 100 marks with 90 minutes time limit; Programming Section had 2 coding questions of 20 and 40 marks each, with a time limit of 50 minutes",
    question_type="coding_algorithms",
    question_text="Another one was about finding kth permutation of a string (k<=1e9).",
    source_quote="The first Coding question was easy, something related to array manipulation and implementation. Another one was about finding kth permutation of a string (k<=1e9).",
    doubt=GFG_DOUBT_BASE + " The poster paraphrases the problem in one clause rather than reproducing the statement, so the exact constraints are his recollection.")

add(**OFF, round="phone_technical", round_name="Round 1: CodePair Round 1.5 hr",
    platform="HackerRank",
    section_context="CodePair Round, 1.5 hr, two programming questions",
    question_type="coding_algorithms",
    question_text="find the number of ways a given number can be expressed as a sum of more than 1 consecutive natural numbers",
    source_quote="The first one was quite easy and straight forward it said to find the number of ways a given number can be expressed as a sum of more than 1 consecutive natural numbers.",
    doubt=GFG_DOUBT_BASE + " The poster links the problem to an existing GfG practice problem, which raises the possibility he is describing a remembered practice problem rather than the exact interview wording.")

add(**OFF, round="phone_technical", round_name="Round 1: CodePair Round 1.5 hr",
    platform="HackerRank",
    section_context="second of two programming questions in the 1.5 hr CodePair round",
    question_type="coding_algorithms",
    question_text="Given a matrix(n * m) and a queen positioned at (n-1,m/2). Find the number of ways in which the queen can reach cell no. (x,y) in minimum number of moves. There were Q queries of (x,y). The queen can move in any of the eight valid directions in one move. Preprocessing of O(n2) was allowed and queries were supposed to be answered in O(1).",
    source_quote="The second one was: Given a matrix(n * m) and a queen positioned at (n-1,m/2). Find the number of ways in which the queen can reach cell no. (x,y) in minimum number of moves.",
    doubt=GFG_DOUBT_BASE + " This is an unusually specific and self-consistent problem statement, which argues for authenticity, but nothing corroborates it independently.")

add(**OFF, round="phone_technical", round_name="Round 2: Technical Round 1 hr",
    platform="HackerRank",
    section_context="Round 2, 1 hr, on HackerRank CodePair; one programming question plus DBMS/OS/project questions",
    question_type="coding_algorithms",
    question_text="Given stock prizes for N days. Each day you could either buy a stock or sell some/all of the stocks you have purchased previously. It is also allowed to not perform any operation for a day. Buying a stock will count as a negative addition to profit and selling will count as a positive addition to the profit. Find the maximum profit that could be achieved given the Stock prizes for N days. Example : [1,5,2,100,3,2]",
    reported_answer="Find the next maximum Stock price for each day and buy that stock only if there is any available higher prize. So the profit will be: For each ith day buying a stock ( - stockPrize[i] ) and selling the stock at a later day with highest stock prize ( i.e. +max(stockPrize[i+1,n-1] ) ). This range maximum could be easily computed using suffix maximum, given a solution in linear time.",
    source_quote="The question was: Given stock prizes for N days. Each day you could either buy a stock or sell some/all of the stocks you have purchased previously.",
    doubt=GFG_DOUBT_BASE + " This is a well-known competitive-programming pattern, so it may be a practice problem the poster conflated with the interview.")

add(**OFF, round="phone_technical", round_name="Round 2: Technical Round 1 hr",
    section_context="DBMS/OS/project questions after the coding question",
    question_type="sql_data",
    question_text="What is a Composite Index? How does it work?",
    source_quote="What is a Composite Index? How does it work?",
    doubt=GFG_DOUBT_BASE + " Very short and generic; a question this standard could plausibly have been reconstructed from a list rather than recalled.")

add(**OFF, round="phone_technical", round_name="Round 2: Technical Round 1 hr",
    section_context="DBMS/OS/project questions after the coding question",
    question_type="sql_data",
    question_text="What is the significance of on condition in an outer join?",
    source_quote="What is the significance of on condition in an outer join?",
    doubt=GFG_DOUBT_BASE + " Very short and generic DBMS trivia; hard to distinguish a genuine recall from a topic list.")

add(**OFF, round="phone_technical", round_name="Round 3: Technical Round 1.5 hr",
    platform="HackerRank",
    section_context="Round 3, 1.5 hr, on HackerRank CodePair",
    question_type="coding_algorithms",
    question_text="Design and implement a class that can be used to allocate and de-allocate a certain amount of memory blocks. The class will initially have a fixed block of memory which will only be used to allocate memory. Say 1024 blocks.",
    source_quote="Design and implement a class that can be used to allocate and de-allocate a certain amount of memory blocks. The class will initially have a fixed block of memory which will only be used to allocate memory. Say 1024 blocks.",
    doubt=GFG_DOUBT_BASE + " The poster reports the follow-up probing in detail, which reads as genuine, but the page is undated so the cycle cannot be established.")

add(**OFF, round="phone_technical", round_name="Round 3: Technical Round 1.5 hr",
    section_context="open-ended design discussion in Round 3",
    question_type="coding_algorithms",
    question_text="Given a file consisting of millions of records. The data is in a structured format i.e in a tabular format with each record consisting of many attributes. How will you perform search operation on the file given the file is stored in secondary memory? Optimize it.",
    source_quote="Given a file consisting of millions of records. The data is in a structured format i.e in a tabular format with each record consisting of many attributes.",
    doubt=GFG_DOUBT_BASE + " I split one multi-part discussion into a single question; the poster presents it as bullets rather than a single stated prompt.")

add(**OFF, round="phone_technical", round_name="Round 3: Technical Round 1.5 hr",
    section_context="Round 3 CS-fundamentals probing",
    question_type="coding_algorithms",
    question_text="What is a Trie Data Structure? Explain it's node structure and working? What is it's applications?How will you optimize the memory usage in Trie?",
    source_quote="What is a Trie Data Structure? Explain it's node structure and working?",
    doubt=GFG_DOUBT_BASE + " Standard data-structures trivia that appears in countless prep lists.")

add(**OFF, round="phone_technical", round_name="Round 3: Technical Round 1.5 hr",
    section_context="Round 3, described by the poster as 'A simple Game Theory question'",
    question_type="logic_brainteaser",
    question_text="A simple Game Theory question: Given Two Players A and B separated by N number of tiles. In a move, each one can move one or two-step ahead. Who will win if player A starts and each one plays alternately and optimally. The player who is not able to make any move losses the game.",
    reported_answer="if you write down all the values of f() you will find that it decomposes to f(n) = 0 if n is a multiple of 3 otherwise f(n)=1",
    source_quote="A simple Game Theory question: Given Two Players A and B separated by N number of tiles. In a move, each one can move one or two-step ahead.",
    doubt=GFG_DOUBT_BASE + " Classic Nim-style subtraction game found in every competitive-programming textbook, so content alone is not evidence of provenance.")

# ---------------- On-campus internship, 2021 drive ----------------
I21 = dict(source_url=U_21, level="internship", role_track="quant_developer", office="India",
           poster_context=POSTER_21, post_date="unknown", source_type="blog")

add(**I21, round="online_assessment", round_name="Round 0: Online Coding and Aptitude Test",
    section_context="This test had 26 MCQs (14 aptitude + 12 technical) and 2 coding Questions",
    question_type="coding_algorithms",
    question_text="Coding Question One: This question was similar to Maximum Sum choosing Non-adjacent elements. Coding Question Two: This question was similar to Minimum points required to reach the end of the grid.",
    source_quote="Coding Question One: This question was similar to Maximum Sum choosing Non-adjacent elements.",
    doubt=GFG_DOUBT_BASE + " The poster only says the OA questions were 'similar to' two named standard problems, so this is a topic pointer rather than the actual question text.")

add(**I21, round="phone_technical", round_name="Round 1: Codepair Round (60 mins) | Hackerrank",
    platform="HackerRank",
    section_context="Codepair Round, 60 mins; 'The number of questions asked in this test were not fixed for every candidate, basically it depends on the interviewer.'",
    question_type="coding_algorithms",
    question_text="First Question(Cakewalk) : Given two numbers 'a' and 'b' having equal number of digits. The task is to find the minimum number of moves required to convert 'a' to 'b'. In on move you can increment or decrement any digit of 'a' by 1. For example: a = 45, b = 34, Answer = 2 (Increment 4 by 1 and decrement 5 by 1).",
    source_quote="Given two numbers 'a' and 'b' having equal number of digits. The task is to find the minimum number of moves required to convert 'a' to 'b'",
    doubt=GFG_DOUBT_BASE + " The worked example the poster gives (a=45, b=34 -> 2) is internally consistent, which supports a genuine recall, but the page carries no interview date.")

add(**I21, round="phone_technical", round_name="Round 1: Codepair Round (60 mins) | Hackerrank",
    platform="HackerRank",
    section_context="second question of the 60-minute Codepair round, labelled 'Open ended' by the poster",
    question_type="coding_algorithms",
    question_text="Second Question(Open ended) : There are many telecom towers in a region, each tower have a certain signal range and bandwidth range. However for every pair of towers having an overlapping signal range, there should not be any point which is lying in the bandwidth range of both the towers (i.e. their bandwidth ranges should not overlap each other). The task is to find the minimum number of unique bandwidth ranges which we can use to assign all the towers.",
    reported_answer="I gave an approach using graph but it was failing at some cases. (graph colouring)",
    source_quote="There are many telecom towers in a region, each tower have a certain signal range and bandwidth range.",
    doubt=GFG_DOUBT_BASE + " This is an unusually elaborate disguised graph-colouring statement, which reads as genuinely recalled, but no date or corroborating account exists.")

add(**I21, round="phone_technical", round_name="Round 1: Codepair Round (60 mins) | Hackerrank",
    platform="HackerRank",
    section_context="third question of the 60-minute Codepair round, labelled by the poster 'Maths and Bitwise Operators'",
    question_type="probability",
    question_text="Third Question(Maths and Bitwise Operators) : You are given a method which can generate 0 and 1 with 50% probability. You need to design a new method which can generate 0 with 75% and 1 with 25% probability using the given method.",
    reported_answer="I used bitwise AND operator to perform the given task.",
    source_quote="You are given a method which can generate 0 and 1 with 50% probability. You need to design a new method which can generate 0 with 75% and 1 with 25% probability using the given method.",
    doubt=GFG_DOUBT_BASE + " This biased-coin-from-fair-coin construction is a stock quant/CS interview problem that also appears in textbooks, so its presence proves little on its own; the first-person round context is what carries the weight here.")

add(**I21, round="phone_technical", round_name="Round 2: Codepair Round(60 mins) | Hackerrank (Final Round)",
    platform="HackerRank",
    section_context="Final round, 60 mins, Codepair; first of two questions",
    question_type="coding_algorithms",
    question_text="You are a given a text written in JSON ... Now he asked me to design a structure which can store this information from this code and answer the queries efficiently. For example if the query is A.B.C then answer will be {D:45}, similarly if the query is A.C.B then answer will be 98, formally I have to return all the information inside the given path or determine that the given path is invalid. An invalid path means a path which does not exists for example B.A",
    reported_answer="Lastly I thought an approach using TRIE data structure (better than the previous one) and I was able to code it at the time of interview",
    source_quote="Now he asked me to design a structure which can store this information from this code and answer the queries efficiently.",
    doubt=GFG_DOUBT_BASE + " The poster admits he does not know JSON and is reconstructing the interviewer's snippet from memory ('There might be some syntax errors'), so the literal prompt is approximate.")

add(**I21, round="phone_technical", round_name="Round 2: Codepair Round(60 mins) | Hackerrank (Final Round)",
    platform="HackerRank",
    section_context="last question of the final round",
    question_type="sql_data",
    question_text="Second Question : This was the last question of the final round and it was based on DBMS. Given an employee table, find all data of the employee having maximum salary.",
    source_quote="Given an employee table, find all data of the employee having maximum salary.",
    doubt=GFG_DOUBT_BASE + " A textbook SQL exercise; only the round context distinguishes it from a generic practice question.")

# ---------------- On-campus internship, 2019 SIP ----------------
I19 = dict(source_url=U_19, level="internship", role_track="quant_developer", office="India",
           poster_context=POSTER_19, post_date="2019", source_type="blog")

add(**I19, round="online_assessment", round_name="Round 1: [Aptitude] ... Section 1 Coding question (20 min)",
    platform="HackerRank",
    section_context="4 sections: Section 1 Coding question (20 min, 20 marks); Section 2 Technical MCQS (20 min, 10 MCQs); Section 3 Quant MCQS (20 min, 10 MCQs); Section 4 System MCQS 6 questions",
    question_type="coding_algorithms",
    question_text="Given a list of string. Each string of the form s1-s2, where s1 is a computer connected to s2 and vice versa. If a hacker attacks one of your computer, then its connected computers will also be hacked and in turn its connected computers will also get hacked just like chain reaction. We have to find maximum count of computers that will get hacked.",
    reported_answer="build an adjacency list from it (Remember it should be an undirected graph). After building the graph apply BFS utility function starting from each vertex and find the maximum count we can get and keep track of visited vertices to avoid cycles. That maximum count is the answer.",
    source_quote="Given a list of string. Each string of the form s1-s2, where s1 is a computer connected to s2 and vice versa.",
    doubt=GFG_DOUBT_BASE + " Largest-connected-component in disguise; standard fare, though the surrounding section/timing detail is specific enough to look genuine.")

add(**I19, round="online_assessment", round_name="Section 3 Quant MCQS (20 min)",
    platform="HackerRank",
    section_context="10 MCQS. Each MCQ 2 marks, negative marking",
    question_type="other",
    question_text="Section 3 Quant MCQS (20 min) 10 MCQS. Each MCQ 2 marks. I didn't perform well in this, I think I was able to do 2 questions correctly and didn't attempted remaining questions as there was negative marking. Questions were tough. More difficult than RS Agarwal questions.",
    source_quote="Questions were tough. More difficult than RS Agarwal questions.",
    doubt="This is a description of the quant MCQ section's difficulty, NOT an actual question — the poster reproduces no quant item at all. Included only as section-level evidence that D. E. Shaw India's OA has a dedicated quant MCQ block; it must not be treated as a question.")

add(**I19, round="phone_technical", round_name="Round 2: [Technical Round 1] (50 min)",
    section_context="Technical Round 1, 50 min, 2 interviewers, 16 of 250+ reached this round",
    question_type="coding_algorithms",
    question_text="Q2) Given a queue q1 with elements and an empty queue q2. You need to reverse q1 by using q2 or by using nothing. No, you can't use recursion. Using recursion is equivalent to using stack.",
    source_quote="Given a queue q1 with elements and an empty queue q2. You need to reverse q1 by using q2 or by using nothing.",
    doubt=GFG_DOUBT_BASE + " Standard data-structures exercise; the explicit 'no recursion' constraint is the kind of detail a real interviewer adds, but that is weak evidence.")

add(**I19, round="phone_technical", round_name="Round 2: [Technical Round 1] (50 min)",
    section_context="Q8 of Technical Round 1, explicitly labelled 'Puzzle' by the poster",
    question_type="logic_brainteaser",
    question_text="Q8) Puzzle. Given 10 stacks each stack contains 10 coins of 1 gram each. But one stack all coins with weight 9 gram. You have a weighing machine. You have to find the faulty stack in minimum number of weighings ?",
    reported_answer="For best case, you just need one weighing. Take 1 coin from first stack, 2 from second, 3 from third and so on and weigh them together. If there was no faulty stack, then this weight would be 550. Now if weight is 549 then 1st stack is faulty, if 548 then 2nd and so on.",
    source_quote="Given 10 stacks each stack contains 10 coins of 1 gram each. But one stack all coins with weight 9 gram. You have a weighing machine.",
    doubt="This is one of the most famous counterfeit-coin puzzles in existence (it predates quant interviewing entirely and appears in Mosteller-style collections), so the content is textbook; only the dated first-person round context supports it being actually asked here.")

add(**I19, round="phone_technical", round_name="Round 2: [Technical Round 1] (50 min)",
    section_context="Q9 of Technical Round 1, a variant of the GfG '3 ants and triangle' puzzle",
    question_type="probability",
    question_text="Q9) Puzzle https://www.geeksforgeeks.org/aptitude/puzzle-21-3-ants-and-triangle/ . I was asked for four ants and a square.",
    source_quote="I was asked for four ants and a square.",
    doubt="The poster gives the question only by linking a GeeksforGeeks puzzle page and noting the variant asked (square instead of triangle) — so the question text itself is not reproduced, and the puzzle is a well-known textbook item.")

add(**I19, round="phone_technical", round_name="Round 2: [Technical Round 1] (50 min)",
    section_context="Q6 of Technical Round 1",
    question_type="other",
    question_text="Q6) One of your friend is getting UI of particular website, but you are not, so what is the problem, how will use you diagnose it?",
    source_quote="One of your friend is getting UI of particular website, but you are not, so what is the problem, how will use you diagnose it?",
    doubt=GFG_DOUBT_BASE + " Generic networking/debugging question with no quant content; included for completeness of the round rather than for quant value.")

with io.open(OUT, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print("wrote", len(rows), "->", OUT)
