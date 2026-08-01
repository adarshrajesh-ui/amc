#!/usr/bin/env python3
"""p22: D. E. Shaw internship assessments from GeeksforGeeks interview-experiences.

D. E. Shaw was the second-thinnest firm in the shard and three GFG pages had already
been mined. The site's de-shaw tag index turns out to run to four pages / 50 write-ups,
so this pass fetched them all (.gfg_cache) and reads the six most detailed internship
accounts.

Caveat carried in every doubt field: these are D. E. Shaw India's on-campus tech drives
(SDE / QTE / Systems / Q&TE intern), not the New York quant-research pipeline, so the
content is DSA and CS-fundamentals rather than probability. They are still genuine
D. E. Shaw internship assessments and the firm is in the shard, so they are in — but
nobody should read them as evidence about the quant_researcher track.

Quotes are copied from the rendered article body (gfg_read.py), which is the same text
a tag-stripping verifier sees; sentences that sit in adjacent <p> tags are joined with
a single space, matching the verifier's whitespace collapse.
"""
import json
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "p22_gfg_deshaw.jsonl")
rows = []

BASE = "https://www.geeksforgeeks.org/interview-experiences/"


def add(url, quote, qtext, qtype, level, round_, round_name, post_date, poster, doubt,
        platform="unknown", section=None, cycle="unknown", answer=None, office="India",
        role="quant_developer"):
    rows.append({
        "firm": "D. E. Shaw", "role_track": role, "level": level, "cycle": cycle,
        "office": office, "round": round_, "round_name": round_name, "platform": platform,
        "section_context": section, "question_type": qtype, "question_text": qtext,
        "question_text_en": None, "reported_answer": answer, "source_url": url,
        "source_type": "blog", "source_quote": quote, "source_language": "en",
        "post_date": post_date, "access": "full_text", "retrieval_method": "webfetch",
        "poster_context": poster, "doubt": doubt,
    })


# ---------------------------------------------------------------- 2023 on-campus intern
U = BASE + "d-e-shaw-internship-interview-experience-on-campus-2023/"
P = ("Anonymous GeeksforGeeks contributor, on-campus internship drive; eligibility was "
     "CGPA > 7.0 with no backlogs from CSE/ECE/EEE; 20 students shortlisted for interviews "
     "out of the OA, 5 went to round 2, 2 got the internship (the writer did not)")
D = ("GeeksforGeeks interview-experience posts are user-submitted and unverified, and the "
     "site does not date the sitting itself (only 'Last Updated'); this is D. E. Shaw India's "
     "on-campus SDE-style drive rather than the quant-research pipeline, so it says nothing "
     "about the trading/research tracks.")
add(U, "It was conducted on a hacker-rank platform. Students with CGPA > 7.0 (with no backlogs) "
       "from CSE, ECE, EEE were eligible to attend the OA. It had 3 questions and each question "
       "was allotted a specific amount of time.",
    "OA on HackerRank: 3 questions, each with its own timer, total 95 minutes",
    "coding_algorithms", "internship", "online_assessment", "Online Assessment", "2023",
    P, D, platform="HackerRank", section="3 questions, Total Duration: 95 minutes")
add(U, "You are given an unweighted undirected graph. Your task is to color the leaf nodes of "
       "the graph. A node x is diverse if all the leaf nodes in its subtree have different colors.",
    "You are given an unweighted undirected graph. Your task is to color the leaf nodes of the "
    "graph. A node x is diverse if all the leaf nodes in its subtree have different colors. Return "
    "an array of size n where the i th element of the array represents the minimum number of "
    "different colors required to make the number of diverse nodes in the graph greater than or "
    "equal to i . (where n is the number of nodes)",
    "coding_algorithms", "internship", "online_assessment", "Question-1 (25 minutes)", "2023",
    P, D, platform="HackerRank", section="Question-1, 25 minutes of a 95-minute OA",
    answer="Writer solved it with BFS and passed all test cases")
add(U, "Given an array arr of n integers, in a single operation, one can reduce any element of "
       "the array by 1. Find the minimum number of operations required to make the array a "
       "bitonic array.",
    "Given an array arr of n integers, in a single operation, one can reduce any element of the "
    "array by 1. Find the minimum number of operations required to make the array a bitonic array. "
    "Example of bitonic array: [0,1,2,3,2,1,0,0]",
    "coding_algorithms", "internship", "online_assessment", "Question-3(35 minutes)", "2023",
    P, D, platform="HackerRank", section="Question-3, 35 minutes",
    answer="Writer tried two pointers, passed 8/15 test cases")
add(U, "You are given a string which contains only a's and b's. A \"good string\" can be split "
       "into 3 parts. First part should contain only a's(can contain 0 also), second should "
       "contain b's and third should contain a's.",
    "You are given a string which contains only a's and b's. A \"good string\" can be split into 3 "
    "parts. First part should contain only a's(can contain 0 also), second should contain b's and "
    "third should contain a's. Now we need to find the length of the largest good string by "
    "deleting some characters from the string.",
    "coding_algorithms", "internship", "phone_technical", "Interview(Round-1)", "2023",
    P, D, platform="HackerRank", section="HackerRank CodePair, 2 interviewers, ~1 hr 10 min",
    answer="Example given: s = \"aaabbaabbbaa\" answer = 10; solved recursively with an index and "
           "a 0/1/2 state variable, then memoised")
add(U, "He asked some questions on internal implementation of map and unordered map. Like "
       "difference between map and unordered map, what is used to implement it(red black trees), "
       "what is hashing, what are collisions, etc.",
    "Internal implementation of map vs unordered_map in C++ STL: what implements it (red-black "
    "trees), what is hashing, what are collisions",
    "coding_algorithms", "internship", "phone_technical", "Interview(Round-1)", "2023",
    P, D, platform="HackerRank", section="second interviewer, C++/STL block")

# ------------------------------------------- 2025 Technology Developer Intern (on-campus)
U = BASE + "de-shaw-interview-experience-for-technology-developer-intern-2025/"
P = ("Anonymous GeeksforGeeks contributor, on-campus Technology Developer Intern drive; "
     "eligibility CGPA 7+ for IT and 8+ for ECE, 300+ students eligible for the OA, 16 "
     "shortlisted after the OA, 10 after round 2, 3 offers at the end")
D = ("User-submitted and unverified; GFG shows only a 'Last Updated' date so the sitting date "
     "is the writer's own '2025' in the title. This is the India technology-developer track, "
     "not a quant research or trading role.")
add(U, "This round consisted of three coding questions based on topics such as binary search, "
       "dynamic programming, and prefix sums.",
    "OA: three coding questions on binary search, dynamic programming and prefix sums, "
    "medium-to-hard",
    "coding_algorithms", "internship", "online_assessment", "ROUND 1: Online Assessment", "2025",
    P, D, section="3 coding questions; 300+ eligible, 16 shortlisted", cycle="2025")
add(U, "You are given a canvas of size n x m, initially filled with 0. You can perform the "
       "following operations: draw(r, c) : Draw a shape (represented by an alphabet from 'A' to "
       "'Z') on cell (r, c). If multiple shapes are drawn on a cell, the most recent shape is "
       "displayed.",
    "Design a custom class over an n x m canvas of zeros supporting draw(r, c), delete(r, c) and "
    "move(r1, c1, r2, c2), where the most recently drawn shape on a cell is the one displayed",
    "coding_algorithms", "internship", "onsite", "ROUND 3: Technical Interview - 2", "2025",
    P, D, section="offline round, two interviewers on the panel", cycle="2025",
    answer="First solution O(N) per operation; optimised to O(logN) per operation with a hashmap "
           "and a queue")
add(U, "Given two numbers represented as linked lists of the same length, I was tasked with "
       "adding the numbers under the following constraints: Reversing the linked list is not "
       "allowed.",
    "Given two numbers represented as linked lists of the same length, add the numbers with "
    "reversing, modifying, extra space and recursion all disallowed",
    "coding_algorithms", "internship", "onsite", "ROUND 3: Technical Interview - 2", "2025",
    P, D, section="offline round, two interviewers", cycle="2025",
    answer="Writer first proposed O(N^2), then an optimised approach after 10-15 minutes")
add(U, "I was challenged to create an object of a class with only a private constructor.",
    "Create an object of a class that has only a private constructor",
    "coding_algorithms", "internship", "onsite", "ROUND 3: Technical Interview - 2", "2025",
    P, D, section="OOP block, second interviewer", cycle="2025",
    answer="Writer suggested static keyword and getter/setter approaches; interviewer was not "
           "satisfied")

# --------------------------------------------------- Dec 2025 System Engineer Intern
U = BASE + "de-shaw-interview-experience-for-system-intern-role/"
P = ("Vedant Singh, CSE at Visvesvaraya National Institute of Technology Nagpur; names himself "
     "in the write-up; applied for System Engineer Intern (2 months), process run online on "
     "4th July; 14 shortlisted after the OA, 4 after the technical round, 1 final offer")
D = ("Self-published account on a user-submission site with no corroboration; the writer names "
     "the sitting as '4th July' without a year, so the 2025 date is the article's publication "
     "date rather than an attested sitting date. Systems-engineering intern track, not quant.")
add(U, "The first round was an online assessment conducted on HackerRank. It consisted of: 1 DSA "
       "coding question 10\u201315 MCQs",
    "OA on HackerRank: 1 DSA coding question plus 10-15 MCQs",
    "coding_algorithms", "internship", "online_assessment", "Initial Screening (Online Assessment)",
    "2025-12", P, D, platform="HackerRank", section="1 DSA question + 10-15 MCQs")
add(U, "The DSA question involved graph traversal (BFS) along with prime number checking. "
       "Initially, the question appeared to be a tree-based problem, which made it a bit "
       "confusing.",
    "OA DSA question combining graph traversal (BFS) with prime number checking; it looked "
    "tree-based at first",
    "coding_algorithms", "internship", "online_assessment", "Initial Screening (Online Assessment)",
    "2025-12", P, D, platform="HackerRank",
    answer="Writer concluded BFS over a graph was the correct approach")
add(U, "I was asked why I used MongoDB over MySQL and which database performs better under "
       "different circumstances.",
    "Why did you use MongoDB over MySQL, and which database performs better under different "
    "circumstances?",
    "sql_data", "internship", "phone_technical", "Technical Round", "2025-12", P, D,
    section="project discussion on a Gatepass Management System")
add(U, "Next, I was asked the difference between authentication and authorization, which I "
       "answered satisfactorily. Then I was asked about the difference between HTTP and HTTPS.",
    "Difference between authentication and authorization; difference between HTTP and HTTPS",
    "other", "internship", "phone_technical", "Technical Round", "2025-12", P, D)

# ------------------------------------------------------- QTE intern, on-campus July 2021
U = BASE + "d-e-shaw-internship-interview-experience-on-campus-2022-2/"
P = ("Anonymous GeeksforGeeks contributor; on-campus drive at their college in July 2021 for a "
     "2-month QTE intern position; describes a 95-minute HackerRank test and two 60-minute "
     "CodePair interviews")
D = ("User-submitted and unverified. QTE at D. E. Shaw India is a quality/test engineering "
     "track, so despite the quant-adjacent employer this is not a trading or research "
     "assessment; the write-up itself is unusually specific, which argues for authenticity.")
add(U, "D.E. Shaw held an on-campus recruitment drive in my college for the position of QTE "
       "intern (2 months) in July 2021.",
    "Round 1 structure: 14 aptitude MCQs in 28 minutes, 12 technical MCQs in 17 minutes, then 2 "
    "coding questions with 20 and 30 minute timers",
    "other", "internship", "online_assessment",
    "Round 1(Technical Test-95 minutes on Hacker Rank)", "2021-07", P, D, platform="HackerRank",
    section="three sections; 14 aptitude MCQ/28 min, 12 technical MCQ/17 min, 2 coding/20+30 min")
add(U, "Given an array of n integers, you can divide the array into sections containing k "
       "elements each (n is divisible by k). The score of each section is the product of the "
       "elements in that section. Find the maximum sum of scores of all sections that you can "
       "achieve.",
    "Given an array of n integers, you can divide the array into sections containing k elements "
    "each (n is divisible by k). The score of each section is the product of the elements in that "
    "section. Find the maximum sum of scores of all sections that you can achieve.",
    "coding_algorithms", "internship", "online_assessment", "coding section", "2021-07", P, D,
    platform="HackerRank", section="first coding question, 20 minutes")
add(U, "Given that you have three items A, B, and C that you need to put them in a particular "
       "order such that there are no three consecutive same items.",
    "Given three item types A, B and C, order them so that no three consecutive items are the "
    "same; for each of n queries (a, b, c) find the maximum number of items you can place",
    "combinatorics", "internship", "online_assessment", "coding section", "2021-07", P, D,
    platform="HackerRank", section="second coding question, 30 minutes")
add(U, "We have N blocks that are required to be painted by using K colors with the following "
       "condition that at most only 1 pair of adjacent blocks could have the same color.",
    "We have N blocks that are required to be painted by using K colors with the condition that at "
    "most only 1 pair of adjacent blocks could have the same color",
    "combinatorics", "internship", "phone_technical",
    "Technical Interview Round 1(60 minutes on Hacker Rank Code Pair)", "2021-07", P, D,
    platform="HackerRank",
    answer="Writer identified it as DP and gave the recursive then memoised approach")
add(U, "We go from our house to the office and back, it is given that the traffic lights are "
       "always red whenever you encounter them. Now while going from your house to the office, "
       "you stop two times but while returning home from the office you stop only once. How is "
       "this situation possible.",
    "We go from our house to the office and back, it is given that the traffic lights are always "
    "red whenever you encounter them. Now while going from your house to the office, you stop two "
    "times but while returning home from the office you stop only once. How is this situation "
    "possible.",
    "logic_brainteaser", "internship", "phone_technical",
    "Technical Interview Round 1(60 minutes on Hacker Rank Code Pair)", "2021-07", P, D,
    answer="Hint given in the write-up: You don't need to stop in a traffic light when you need "
           "to turn left")
add(U, "There is an N-floor building and you have one egg. You need to find the lowest floor "
       "from which the egg breaks on dropping.",
    "There is an N-floor building and you have one egg. You need to find the lowest floor from "
    "which the egg breaks on dropping. Follow-up: what is the most optimal method with 2 eggs?",
    "logic_brainteaser", "internship", "phone_technical",
    "Technical Interview Round 1(60 minutes on Hacker Rank Code Pair)", "2021-07", P, D,
    answer="One egg: linear scan upward, O(N). Two eggs: use one egg to shorten the search range, "
           "then linear search inside it")
add(U, "They started with a mathematical puzzle where he asked to find which of the two is "
       "bigger, 50^(99) or 99!, once I said that 50^99 was bigger they then asked me why?",
    "Which of the two is bigger, 50^99 or 99! ? Why?",
    "logic_brainteaser", "internship", "phone_technical",
    "Technical Interview Round 2(60 minutes on HackerRank Code Pair)", "2021-07", P, D,
    answer="Writer answered 50^99 and justified it by rewriting both numbers in terms of 100; the "
           "interviewers were not fully satisfied")
add(U, "We are making an exam-timetable in which every student should give only one exam a day "
       "and the number of days the exam spans over should be minimized and we are required to "
       "find the minimum number of days it would take to conduct the examination.",
    "Students each take several courses; build an exam timetable where every student sits at most "
    "one exam a day, minimising the number of days",
    "coding_algorithms", "internship", "phone_technical",
    "Technical Interview Round 2(60 minutes on HackerRank Code Pair)", "2021-07", P, D,
    answer="Model courses as graph nodes with an edge where a student takes both, then topological "
           "sort and count levels")

# ---------------------------------------------- Summer Intern 2022, VJTI Mumbai, Aug 2021
U = BASE + "d-e-shaw-interview-experience-for-summer-intern-2022-on-campus/"
P = ("Anonymous GeeksforGeeks contributor at VJTI Mumbai; DE Shaw visited in the first week of "
     "August 2021 for a 2-month software development internship; the writer received one of the "
     "3 offers made")
D = ("User-submitted and unverified, and the three OA questions are paraphrased by the writer "
     "('the gist was') rather than transcribed. India SDE internship track, not quant research.")
add(U, "Each question had a separate timer, and it wasn\u2019t allowed to attempt the previous "
       "questions once the timer ran out. Switching between questions wasn\u2019t allowed either.",
    "Round 1 coding test: 3 coding questions, each with a separate timer, no switching back",
    "coding_algorithms", "internship", "online_assessment", "Round 1: Coding Test", "2021-08",
    P, D, section="Number of questions: 3 Coding questions")
add(U, "You are given an NxM matrix. The cells contain *(asterisk) or .(dot) Here, \u2018*\u2019 "
       "means land, and \u2018.\u2019 means water. You need to find the maximum one of all the "
       "minimum area rectangles that can completely enclose an island.",
    "You are given an NxM matrix of '*' (land) and '.' (water); find the largest of all the "
    "minimum-area rectangles that completely enclose an island",
    "coding_algorithms", "internship", "online_assessment", "Round 1: Coding Test", "2021-08",
    P, D, section="one of 3 timed coding questions")
add(U, "You have been given N strings, you need to create a minimum length string such that "
       "those N strings are substrings of that output string.",
    "You have been given N strings, you need to create a minimum length string such that those N "
    "strings are substrings of that output string, with the extra condition that if A precedes B "
    "in the list then B must start after A starts",
    "coding_algorithms", "internship", "online_assessment", "Round 1: Coding Test", "2021-08",
    P, D, section="one of 3 timed coding questions")
add(U, "Explain 1NF, 2NF, 3NF using a university database example. Write the query to find the "
       "maximum salary for every department from a table (Basically use of group by clause)",
    "Explain 1NF, 2NF, 3NF using a university database example; write the query to find the "
    "maximum salary for every department",
    "sql_data", "internship", "phone_technical", "Round 2: Technical Interview 1", "2021-08",
    P, D, section="DBMS block")
add(U, "Kadane\u2019s algorithm - I was asked to code the algorithm and also dry-run it on an "
       "example.",
    "Code Kadane's algorithm and dry-run it on an example, then the k-th largest sum contiguous "
    "subarray follow-up",
    "coding_algorithms", "internship", "phone_technical", "Round 3: Technical Interview 2",
    "2021-08", P, D)

# ------------------------------------------------ SDE intern, on-campus Aug 2020 (2021 post)
U = BASE + "de-shaw-internship-interview-experience-on-campus-2021-2/"
P = ("Anonymous GeeksforGeeks contributor; DE Shaw ran an on-campus drive for a 2-month SDE "
     "intern position in the first week of August 2020; 12 of 101 shortlisted for interview, "
     "3 of 12 to the second interview, 2 offers, writer was one of them")
D = ("User-submitted and unverified; the OA question statements are the writer's recollection "
     "weeks later. India SDE internship, so nothing here speaks to the quant tracks.")
add(U, "Given an array of n numbers, find the number of triplets such that Ai<Aj<Ak or Ai>Aj>Ak "
       "where I, j, k are indices of the array and i<j<k.",
    "Given an array of n numbers, find the number of triplets such that Ai<Aj<Ak or Ai>Aj>Ak "
    "where i, j, k are indices and i<j<k",
    "coding_algorithms", "internship", "online_assessment",
    "Round 1: Technical Test (90 minutes) | Hacker Rank", "2020-08", P, D, platform="HackerRank",
    section="three coding questions, each with its own time limit, in 90 minutes",
    answer="The O(n^3) approach would not pass all the test cases and the solution needed to be "
           "optimized to O(n^2) or O(n log(n))")
add(U, "You are given x lions, y tigers, z leopards, and w panthers. There are m cages in a line "
       "and you have to fill all the m cages such that no two same animals are adjacent to each "
       "other. Find the total number of ways to do so.",
    "You are given x lions, y tigers, z leopards, and w panthers and m cages in a line; fill all m "
    "cages so no two same animals are adjacent, and count the total number of ways",
    "combinatorics", "internship", "online_assessment",
    "Round 1: Technical Test (90 minutes) | Hacker Rank", "2020-08", P, D, platform="HackerRank",
    section="second of three coding questions, 30 minutes",
    answer="Constraints 0<=x,y,z,w<=51; the writer says it was to be solved using DP")
add(U, "How would you implement your own vector (Dynamic array) in C++? To which I answered "
       "either using linked list or self-expanding arrays using new and delete (the actual way "
       "how vectors are implemented).",
    "How would you implement your own vector (dynamic array) in C++, with add, delete, search and "
    "access and their time complexities?",
    "coding_algorithms", "internship", "phone_technical",
    "Round 2: Technical Interview (Round 1) | Code Pair (Hacker Rank) | (60 Minutes)", "2020-08",
    P, D, platform="HackerRank")
add(U, "Merge two unsorted arrays of size n and m without extra space",
    "Merge two unsorted arrays of size n and m without extra space",
    "coding_algorithms", "internship", "phone_technical",
    "Round 2: Technical Interview (Round 1) | Code Pair (Hacker Rank) | (60 Minutes)", "2020-08",
    P, D, platform="HackerRank")
add(U, "Calculating time to process 1 billion instructions, given time for each cycle",
    "Calculate the time to process 1 billion instructions, given the time for each cycle",
    "other", "internship", "phone_technical",
    "Round 2: Technical Interview (Round 1) | Code Pair (Hacker Rank) | (60 Minutes)", "2020-08",
    P, D, platform="HackerRank")
add(U, "Implement python style list (which can take different types of data in a single list) "
       "in C++",
    "Implement a Python-style list (which can hold different types of data in one list) in C++",
    "coding_algorithms", "internship", "phone_technical",
    "Round 3: Technical Interview (Round 2) | Code Pair (Hacker Rank) | (60 Minutes)", "2020-08",
    P, D, platform="HackerRank")

# --------------------------------------- Quality & Test Engineering intern, VIT Aug 2020
U = BASE + "de-shaw-summer-internship-interview-experience-2021-on-campus-vit-vellore/"
P = ("Anonymous GeeksforGeeks contributor at VIT Vellore; DE Shaw visited on 21st August 2020 "
     "for a Quality & Test Engineering Intern position for summer 2021; 1500+ sat round 1, 17 "
     "shortlisted, 7 reached the final round, 2 selected including the writer")
D = ("User-submitted and unverified; the writer flags their own paraphrasing ('the gist was'). "
     "Quality & Test Engineering intern at D. E. Shaw India, so this is not a quant assessment "
     "even though the employer is in the shard.")
add(U, "This was a programming & MCQ test for 138 marks with 95 minutes time limit. Each wrong "
       "answer will carry a negative marking of 33% of the marks for that question.",
    "Round 1 on HackerRank: 138 marks in 95 minutes with 33% negative marking, split into "
    "aptitude (14Q/28min), technical (12Q/17min) and two coding sections (20 and 30 min)",
    "other", "internship", "online_assessment", "Round 1 (1500+ people appeared)", "2020-08",
    P, D, platform="HackerRank", section="138 marks, 95 minutes, negative marking")
add(U, "Q. Given an array of positive integers, find out the number of sub-arrays that consist "
       "of prime numbers only.",
    "Given an array of positive integers, find out the number of sub-arrays that consist of prime "
    "numbers only.",
    "coding_algorithms", "internship", "online_assessment", "Coding Section 1 : 1 Question for 20 "
    "minutes", "2020-08", P, D, platform="HackerRank",
    answer="Example given: [2,3,1,7,2] -> subarrays [2],[3],[2,3],[7],[2],[7,2], answer 6")
add(U, "Two arrays are given, one binary array A (containing only 0s and 1s) and the other cost "
       "array B of the same length. You have to convert the binary array to all 1s at minimum "
       "cost.",
    "Two arrays are given, a binary array A and a cost array B of the same length; convert A to "
    "all 1s at minimum cost, where flipping A[i] costs B[i] but is free if A[i-1] and A[i+1] are "
    "both 1",
    "coding_algorithms", "internship", "online_assessment", "Coding Section 2 : 1 Question for 30 "
    "minutes", "2020-08", P, D, platform="HackerRank",
    answer="Writer passed no test cases on this question")
add(U, "Given a regex consisting of '\\d','\\w','$',^','+','*' (where the regex symbols have "
       "their usual meaning). I was asked to generate as many kinds of strings as possible for "
       "any given regex input.",
    "Given a regex built from \\d, \\w, $, ^, + and *, generate as many kinds of matching strings "
    "as possible",
    "coding_algorithms", "internship", "phone_technical", "Round 2 (17 people shortlisted)",
    "2020-08", P, D, platform="HackerRank",
    section="HackerRank CodePair, scheduled 1 hour but ran 1hr 30min, two interviewers",
    answer="Writer tokenised the regex into [symbol, modifier] pairs and grew a vector of "
           "candidate strings built from 'a' and '1'")
add(U, "Given an array of strings A, find the string with maximum length for which every prefix "
       "string existed in the array.",
    "Given an array of strings A, find the longest string all of whose prefixes also appear in the "
    "array",
    "coding_algorithms", "internship", "onsite", "Round 3 Final Round (7 people shortlisted)",
    "2020-08", P, D, platform="HackerRank",
    answer="Example: for ['a','ab','abc','abcd','aaaaa','aabsd'] the answer is 'abcd'; writer used "
           "a hashmap of all strings and checked prefixes")
add(U, "Given pickup points , drop points and tips array, every i th Element represents a trip "
       "from pickup[i] to drop[i], which would earn the driver drop[i]-pickup[i]+tip[i].",
    "Given pickup, drop and tip arrays where trip i earns drop[i]-pickup[i]+tip[i] and the next "
    "pickup must be at or after the last drop, maximise earnings",
    "coding_algorithms", "internship", "onsite", "Round 3 Final Round (7 people shortlisted)",
    "2020-08", P, D, platform="HackerRank",
    answer="Writer concluded dynamic programming was the way to go but their code segfaulted "
           "before time ran out")

# ------------------------------------------------- MNIT Jaipur, Aug 2019 SDE internship
U = BASE + "d-e-shaw-internship-interview-experience-on-campus/"
P = ("Anonymous GeeksforGeeks contributor at MNIT Jaipur; DE Shaw visited in the first week of "
     "August 2019 for a 2-month software development internship; 11 of 88 shortlisted after the "
     "50-minute technical test, 5 of 11 promoted to the second technical interview")
D = ("User-submitted and unverified, and the interview questions are given as a numbered list "
     "reconstructed from memory. India SDE internship drive rather than a quant assessment.")
add(U, "1. Find the maximum number of connected nodes in the graph. (Dfs) 2. Delete some numbers "
       "from the given array to maximize the difference between the sum of odd position elements "
       "and even position elements. (Greedy or Dp)",
    "Technical test, 50 minutes, two questions: find the maximum number of connected nodes in the "
    "graph; and delete numbers from an array to maximise the difference between the sum of "
    "odd-position and even-position elements",
    "coding_algorithms", "internship", "online_assessment", "Technical Test (50 min)", "2019-08",
    P, D, section="2 questions in 50 minutes; 11 of 88 shortlisted",
    answer="Example given: 6 7 5 1 9 2 10, Ans 23 ( 7, 1, 9, 2, 10)")
add(U, "2. Implement python list in C. My first solution is using struct and linked list and "
       "then move on to union and linked list and finally accurate one with a linked list with "
       "void * pointer.",
    "Implement a Python list in C",
    "coding_algorithms", "internship", "phone_technical", "Technical Interview 1 (50 min)",
    "2019-08", P, D,
    answer="Writer went struct+linked list, then union+linked list, then a linked list of void* "
           "pointers")
add(U, "22. There are n goods with a weight of ith good is wi and m trucks. You have to load "
       "this truck in such a way that each truck should carry almost equal weights.",
    "There are n goods, the i-th of weight wi, and m trucks; load the trucks so each carries "
    "almost equal weight",
    "coding_algorithms", "internship", "phone_technical", "Technical Interview 1 (50 min)",
    "2019-08", P, D, answer="Writer gave a DP solution for m == 2 and was not asked to generalise")
add(U, "4. Design a data structure with Insert, delete and search operations in O(1)(worst "
       "case).",
    "Design a data structure with insert, delete and search in O(1) worst case, then add "
    "getRandom in O(1)",
    "coding_algorithms", "internship", "phone_technical", "Technical Interview 2(50 min)",
    "2019-08", P, D,
    answer="Once told the data was in range 1-9999 the writer used a direct-address array of "
           "0/1 flags")

with open(OUT, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print("%d records -> %s" % (len(rows), OUT))
