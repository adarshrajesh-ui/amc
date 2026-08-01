REPO: SarthakVerma18/Intern-Guidance
PATH: QuantSDE_GODtips.md
URL: https://github.com/SarthakVerma18/Intern-Guidance/blob/main/QuantSDE_GODtips.md

# Overview

There is always a non zero chance of getting fucked over, just take lite and have fun :)

- [Overview](#overview)
  - [My goals](#my-goals)
  - [Preparation](#preparation)
  - [General Tips](#general-tips)
- [Interview Experience](#interview-experience)
  - [Optiver (SDE)](#optiver-sde)
  - [IMC (SDE)](#imc-sde)
  - [Graviton (Quant)](#graviton-quant)
  - [NK Securities (SDE)](#nk-securities-sde)
  - [Quadeye (??)](#quadeye-)


## My goals
Just after sem 4 ended, I made up my mind... I wanted a job (preferably one that gives me more pocket money).

I decided I wanted either sde (due to my advantage in dsa) or quant (for exposure in a mathsy field).

## Preparation

I started doing codeforces in my first year in college. In my second year my team qualified for the ICPC West Asia Continent Regionals. At the time of intern season I had a rating of 2090 on codeforces.

To practice CP I mainly did the cses problem set (sorting, dp and strings) and the codeforces edu course (for dsu, segtree and binary search).

**DISCLAIMER:** The level of questions they ask is much easier than any of this (I think someone able to maintain a 1600 rating is good enough to solve most of the questions they give).

**NOTE**: I did not take any probability course prior to intern season but I wish I did, it would have made a lot of things easier.

During my third semester I solved a lot of questions from https://www.puzzledquant.com/ (I did approximately 200 of them).

Just after sem 4 I was averaging about 20-30 in zetamac, I did about 2 runs everyday and by the time intern season came I averaged about 40-50 (still low compared to the others, but it was only really relevant in the Flow Traders test).

After semester 4 I started doing some books to study probability and logical reasoning.
- **50 challenging problems**: Has a lot of standard questions, I recommend spending atleast 30 minutes before viewing the solution to problems you don't get. I went through the entire book once in May and once just before my DaVinci interview at the end of July.
- **Heard on the Street**: I solved the first and fourth chapters (The ones that didn't have any financial terms). The difficulty in this book varies a lot, I only did one pass of this sometime in the beginning of July. Since I was low on time I directly viewed the solutions for questions where I didn't get an idea at first glance.
- **Dice Problems**: I only did the first chapter and I hated it. There aren't any beautiful solutions, he just uses brute force for everything, would not recommend.
- **Algorithmic Puzzles (Levitin)**: I did only a few problems in this, it is definitely overkill (but very fun).

**Things I Missed:** I should have read about databases, networking, system design and c++ behaviour.

## General Tips

Having a CG above 9 will get you through most of the CG cutoffs, below 8 and your options start to get very limited.

Having a decent codeforces rating is not required but it definitely helps, especially for indian quants. I felt like some of the indian quants just selected people based off of cf rating.

I'd recommend using C++ as your main programming language (Python users only had an advantage in the stripe OA).

Indian quants tend to ask textbook questions about c++ and software in general (I was not prepared for this). Optiver and IMC asked more practical questions.

- **Aptitide Sections (OA)** usually asked standard problems. You didn't have to solve all the questions to get through (atleast on the harder tests). The more practice you have (do the books I recommended and more), the better. 

- All companies (except IMC, Optiver and DaVinci) had an **SDE Section (OA)**. I was severely underprepared for these, I just ended up guessing everything. The questions were based on CS topics like paging, resource allocation graphs, sql etc.

- **Coding Sections (OA)** tend to be about 1500ish rated problems. Be comfortable with dp, graph traversal (bfs and dfs), sorting, arrays etc. (Know how to use stuff in the standard library)

- During your **GD** just focus on communicating well. They are mainly looking at how well you speak and how well you listen to others. Just be chill and you'll be fiiine.

- In your **technical interviews** speak out your thoughts (I kept on yapping in all my interviews). These guys are all chill people, they want to know how you approach problems. They are on your side, they will try and keep you on the right track :)

- **HR Interviews** are liite. These guys are usually easier to talk to (more extroverted) than the technical rounds guys. Feel free to be funny (I was cracking jokes whenever I got the chance to). I think this is mostly a formaility, they just want to know why you do what you do.


# Interview Experience

I got shortlists for about 20 roles but I only gave 7 before being allowed to leave and pack the rest (I had gotten confirmation from optiver).

I got packed by DaVinci (quant role) and QuantBox (quant role). DaVinci required to be able to calculate fast while QuantBox had multiple rounds of proving type of questions (They gave sufficient time to think).

Below is the list of companies I got offers from and their individual recruiting process.

## Optiver (SDE)
- ### 1. Online Assesment
    There were 2 parts to this.
    
    Part 1 was a 75 minute coding assignment where they described the requirements of a graph based network, we were simply asked to implement it (no optimizations required). They just wanted to test if you could get a working solution (need not be the best).

    Part 2 was a 20 minutes long MCQ test based on DSA, Networks, SQL ans system design. Correct answers give 1 point and wrong answers removed 1 point. I could solve most of these just by logical deduction. We were not required to solve all correctly to pass on to the next round. (I think I wouldv'e got about 15ish? in the test)

- ### 2. Group Discussion
    They divided us into groups. They gave a simple logic puzzle at first and gave similar questions (same setup) but with a higher difficulty. It was not related to software in any way. They were just testing our communication skills (and ofcourse that you were able to solve these brain teaser type of questions). My group members stayed relatively silent whereas I kept yapping, I think this is what got me through to the next round. 

    The optiver guys only spoke to us when they wanted to hear our solutions or when they introduced the next question. Most of the interaction was with my group members.
    This round lasted about 30 minutes? (We were given more than enough time to solve the questions).

- ### 3. Technical Interview
    This round lasted 45 minutes, my interviewer already knew my name from the GD on the previous day (that might have given me an advantage? I made a good impression in the gd).

    I was presented with a software design type of question. He gave me the required functionality of their trading engine and I was expected to sketch out the classes and the functions I would implement in each of these classes on a canvas (flowchart types).

    The question was roughly the following
    ```
    Create a system that handles trading with multiple exchanges. Each exchange may use different network protocols and require different file formats (File formats may be common between some exchanges).
    ```

    I wasn't required to write any code, he did ask me how I would implement certain functionality and I just had to speak it out to him. The interviewer was very nice, he clarified all doubts I had regarding the question.

    He mainly asked for my reasoning behind certain decisions I made and also questioned me on how I would test out my code. My initial solution had some minor flaws (I had made some wrong assumptions), but as he asked his questions I made changes to my design to better suit the problem at hand.
- ### 4. Behavioural Interview
    This was liiiite. The HR person literally just had a chat with me for 30 minutes. She basically just wanted to know my motivation behind applying to optiver and other general aspects of who I am (what motivates me, what interests I have etc..). It was a very lighthearted interview, I just said the first thing that popped up in my mind. Just don't be a sociopath and you'll be fiiine.

## IMC (SDE)
- ### 1. Online Assesment
    This was a 105 minute coding test with 2 questions.

    The first question was a simple dp question.
    ```
    You start at x = 0, at any instant you can move either `a` steps or `b` steps to the right (a, b > 0). Additionally you could at some point (exactly once) jump back to half of your current coordinate. What is the closest you can get to x = `t` given that you are never allowed to cross `t`.
    ```

    The second question was a simple graph question (I don't remember the exact wording but the question boiled down to the following)
    ```
    Given a directed graph with n vertices where each vertex has exactly one edge going out of it, find the number of vertices not present in a cycle.
    ```

- ### 2. Group Discussion
    They provided each of us with the implementation of some ResourceManager. We were asked to read it individually and write down our answers to some questions on the paper. Then they divided us into groups and we were asked to make optimizations and discuss implementations of specific parts of the program.
    
    For each optimization and implementation a different IMC employee sat with us. The interaction with them was much more than the interaction between fellow group members.

    Finally we were asked to present our solutions to the other groups. There was no real discussion in this round (I guess they ran out of time).
    
    This round lasted about 45 minutes?

- ### 3. Technical Interview
    This round had a time limit of 90 minutes. There were 2 interviewers present in my room. The first 30 minutes I had to spend just figuring out and discussing with them the most optimal method to solve the question they had given.

    ```
    You have to maintain an orderbook. You must implement an `order` function that handles an order correctly (match order with the order book as described by them). Additionally you must allow an order to be cancelled by the `cancel` function.
    ```

    After a few iterations I landed on a O(T + logN) complexity for the order function and an O(log N) solution for the cancel function (Here T is the number of trades made by an order and N is number of orders in orderbook). My initial solution was close (I had (T * logN) for my order), they helped me figure out the solution.

    No coding was requird for the above section, I just had to discuss it with them. They were very nice.

    Then I had 60 minute to complete their orderbook handling code (it was not the implementation I had suggested). They told that they didn't want any optimized code, they just wanted to see if I could get it to work. After about 20 minutes I was able to pass all test cases but you were not required to pass all cases to get an offer.

- ### 4. HR Interview
    This was also liiiite. There were 2 HR people talking to me. This was also another 30 minute chat. In this interview they asked me about some stuff on my resume and why I wanted to join IMC. Again they just wanted to know what type of a person I am. The interviewers were a blast to talk with. I was answering a lot of questions unseriously (making an obnoxious amount of jokes) because I found it funny, ig they found it funny too :)

## Graviton (Quant)
- ### 1. Offline Assesment
    The quant and software roles had a 1 hour written paper each. They software part was just 3 medium level CP questions that we were required to write down our approach for (I only solved 2). The quant section were 7 proving type of maths questions (I only solved 4). You were not required to solve all questions to move onto the next round.

- ### 2. Interview
    I had gotten shortlist to both quant and sde, they let me choose what I wanted to try for first, I went with quant.

    The first round was with a junior quant. This lasted about 30 minutes. He asked a few simple maths problems.
    ```
    1. What is the sum of all rational numbers with terminating decimal expansions.

    2. A number N has all the digits from 1-9 exactly once, prove that it cannot be a perfect square.

    3a. What is the expected draws from a uniform distribution [0, 1] such that their sum crosses 1.

    3b. What is the expected draws from a uniform distribution [0, 2] such that their sum crosses 1.

    3c. What is the expected draws from a uniform distribution [0, 1] such that their sum crosses 2.
    ```

    The second round was with a senior quant. This lasted about 20 minutes. he asked a single question.
    ```
    Alice and Bob are playing a game with 2 piles of coins where Alice goes first. At each turn a player removes a full stack of coins and then divides the other pile into two piles of non zero coins. The first player who cannot make a move (eg: if the piles are 1 1) loses. Find out who wins based on the initial configuration.
    ```

- ### 3. HR Interview?
    They had pretty much decided to give me an offer. So for about 10 minutes the HR was telling me about how nice graviton is (He was a pretty nice dude).


## NK Securities (SDE)
- ### 1. Online Assesment
    There was a 90 minute coding test. I do not remember the questions asked, but I remember thinking it wasn't hard.

- ### 2. Interview
    It was at 5am, the interviewer realllly wanted to sleep (I could tell). He gave me a few cp type of questions where I just had to discuss my approach (It wasn't really a discussion as he was muted most of the time). But he seemed satisfied ig, at the end of the interview he said I could look forward to an offer. The interview lasted about 45 minutes.

## Quadeye (??)
They directly had interviews (resume based shortlist). I bombed this interview on purpose (optiver had already confirmed). I don't know what role I even applied for, I made sure not to answer anything correctly. I think they figured out something was fishy and just sent an offer because of my codeforces rating. 
