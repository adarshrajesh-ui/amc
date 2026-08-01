# Quant developer / software engineering questions

128 questions across 16 firms, out of the 346-question corpus.

The developer and SWE tracks, a genuinely different assessment from the trading and research pipelines. This set is the largest because developer-track recall is shared far more freely, not because these firms mostly ask coding questions.

**By level:** internship 75 · unknown 23 · experienced 20 · new_grad 10

Tier is sort order, not confirmation: A means multiple independent dated attestations, B a single dated full-text one, C weak or snippet-only, D provenance real but a negative signal fired. See `REPORT.md` §6.

---

## D. E. Shaw  (53)

**1.** `B` · internship · online_assessment · unknown

Given a list of string. Each string of the form s1-s2, where s1 is a computer connected to s2 and vice versa. If a hacker attacks one of your computer, then its connected computers will also be hacked and in turn its connected computers will also get hacked just like chain reaction. We have to find maximum count of computers that will get hacked.

*Reported answer:* build an adjacency list from it (Remember it should be an undirected graph). After building the graph apply BFS utility function starting from each vertex and find the maximum count we can get and keep track of visited vertices to avoid cycles. That maximum count is the answer.

<sub>blog · 2019 · [source](https://www.geeksforgeeks.org/interview-experiences/de-shaw-on-campus-internship-interview-experience-2019/)</sub>

**2.** `B` · internship · online_assessment · unknown

You are given an unweighted undirected graph. Your task is to color the leaf nodes of the graph. A node x is diverse if all the leaf nodes in its subtree have different colors. Return an array of size n where the i th element of the array represents the minimum number of different colors required to make the number of diverse nodes in the graph greater than or equal to i . (where n is the number of nodes)

*Reported answer:* Writer solved it with BFS and passed all test cases

<sub>blog · 2023 · [source](https://www.geeksforgeeks.org/interview-experiences/d-e-shaw-internship-interview-experience-on-campus-2023/)</sub>

**3.** `B` · internship · online_assessment · unknown

Given an array arr of n integers, in a single operation, one can reduce any element of the array by 1. Find the minimum number of operations required to make the array a bitonic array. Example of bitonic array: [0,1,2,3,2,1,0,0]

*Reported answer:* Writer tried two pointers, passed 8/15 test cases

<sub>blog · 2023 · [source](https://www.geeksforgeeks.org/interview-experiences/d-e-shaw-internship-interview-experience-on-campus-2023/)</sub>

**4.** `B` · internship · online_assessment · unknown

Given an array of n integers, you can divide the array into sections containing k elements each (n is divisible by k). The score of each section is the product of the elements in that section. Find the maximum sum of scores of all sections that you can achieve.

<sub>blog · 2021-07 · [source](https://www.geeksforgeeks.org/interview-experiences/d-e-shaw-internship-interview-experience-on-campus-2022-2/)</sub>

**5.** `B` · internship · online_assessment · unknown

Given three item types A, B and C, order them so that no three consecutive items are the same; for each of n queries (a, b, c) find the maximum number of items you can place

<sub>blog · 2021-07 · [source](https://www.geeksforgeeks.org/interview-experiences/d-e-shaw-internship-interview-experience-on-campus-2022-2/)</sub>

**6.** `B` · internship · online_assessment · unknown

You are given an NxM matrix of '*' (land) and '.' (water); find the largest of all the minimum-area rectangles that completely enclose an island

<sub>blog · 2021-08 · [source](https://www.geeksforgeeks.org/interview-experiences/d-e-shaw-interview-experience-for-summer-intern-2022-on-campus/)</sub>

**7.** `B` · internship · online_assessment · unknown

You have been given N strings, you need to create a minimum length string such that those N strings are substrings of that output string, with the extra condition that if A precedes B in the list then B must start after A starts

<sub>blog · 2021-08 · [source](https://www.geeksforgeeks.org/interview-experiences/d-e-shaw-interview-experience-for-summer-intern-2022-on-campus/)</sub>

**8.** `B` · internship · online_assessment · unknown

Given an array of n numbers, find the number of triplets such that Ai<Aj<Ak or Ai>Aj>Ak where i, j, k are indices and i<j<k

*Reported answer:* The O(n^3) approach would not pass all the test cases and the solution needed to be optimized to O(n^2) or O(n log(n))

<sub>blog · 2020-08 · [source](https://www.geeksforgeeks.org/interview-experiences/de-shaw-internship-interview-experience-on-campus-2021-2/)</sub>

**9.** `B` · internship · online_assessment · unknown

You are given x lions, y tigers, z leopards, and w panthers and m cages in a line; fill all m cages so no two same animals are adjacent, and count the total number of ways

*Reported answer:* Constraints 0<=x,y,z,w<=51; the writer says it was to be solved using DP

<sub>blog · 2020-08 · [source](https://www.geeksforgeeks.org/interview-experiences/de-shaw-internship-interview-experience-on-campus-2021-2/)</sub>

**10.** `B` · internship · online_assessment · unknown

Given an array of positive integers, find out the number of sub-arrays that consist of prime numbers only.

*Reported answer:* Example given: [2,3,1,7,2] -> subarrays [2],[3],[2,3],[7],[2],[7,2], answer 6

<sub>blog · 2020-08 · [source](https://www.geeksforgeeks.org/interview-experiences/de-shaw-summer-internship-interview-experience-2021-on-campus-vit-vellore/)</sub>

**11.** `B` · internship · online_assessment · unknown

Two arrays are given, a binary array A and a cost array B of the same length; convert A to all 1s at minimum cost, where flipping A[i] costs B[i] but is free if A[i-1] and A[i+1] are both 1

*Reported answer:* Writer passed no test cases on this question

<sub>blog · 2020-08 · [source](https://www.geeksforgeeks.org/interview-experiences/de-shaw-summer-internship-interview-experience-2021-on-campus-vit-vellore/)</sub>

**12.** `B` · internship · online_assessment · unknown

A matrix is given or r rows and c columns. Each cell is a factory that has a loot amount of a(i,j). We can start looting from any cell. The Directions allowed to move are Down & Right with a constraint that i can loot a factory only is previous loot is lesser than this loot. We need to find the maximum number of factories that can be looted.

*Reported answer:* Dynamic programming, worth 30 marks

<sub>blog · 2021 · [source](https://www.geeksforgeeks.org/interview-experiences/de-shaw-interview-experienceon-campus-internship-2021/)</sub>

**13.** `B` · internship · online_assessment · unknown

Given that you have three items A, B, and C that you need to put them in a particular order such that there are no three consecutive same items. Given n queries of the form (a, b, c) where a, b and c are the number of items A, B, and C that you have, find the maximum number of A, B, and C items that you can order by following the above constraint.

*Reported answer:* Math, with low constraints, per the poster's own tag

<sub>blog · 2022 · [source](https://www.geeksforgeeks.org/interview-experiences/d-e-shaw-internship-interview-experience-on-campus-2022/)</sub>

**14.** `B` · internship · online_assessment · unknown

Two coding questions drawn from competitive-programming dynamic programming

<sub>university_bbs · 2021-04-18 · [source](https://ecedplacement.wordpress.com/2021/04/18/de-shaw-2/)</sub>

**15.** `B` · internship · onsite · unknown

A couple of open-ended problems that required some knowledge of basic ML techniques, statistics, and probability (no need to write code for these).

<sub>blog · 2020-10-17 · [source](https://www.jointaro.com/interviews/companies/de-shaw/experiences/software-engineerinternship-new-york-ny-october-17-2020-no-offer-positive-5f41aca8)</sub>

**16.** `B` · internship · onsite · unknown

The most unexpected question was: how would you color a 3-colorable graph?

*Reported answer:* I was initially thinking that you had to do something efficient, which isn't possible. But he just wanted some way of doing it.

<sub>blog · 2013-11-01 · [source](https://www.jointaro.com/interviews/companies/de-shaw/experiences/quantitative-analystsoftware-developer-intern-new-york-ny-november-1-2013-accepted-offer-positive-763017cd)</sub>

**17.** `B` · internship · onsite · 2025

Design a custom class over an n x m canvas of zeros supporting draw(r, c), delete(r, c) and move(r1, c1, r2, c2), where the most recently drawn shape on a cell is the one displayed

*Reported answer:* First solution O(N) per operation; optimised to O(logN) per operation with a hashmap and a queue

<sub>blog · 2025 · [source](https://www.geeksforgeeks.org/interview-experiences/de-shaw-interview-experience-for-technology-developer-intern-2025/)</sub>

**18.** `B` · internship · onsite · 2025

Given two numbers represented as linked lists of the same length, add the numbers with reversing, modifying, extra space and recursion all disallowed

*Reported answer:* Writer first proposed O(N^2), then an optimised approach after 10-15 minutes

<sub>blog · 2025 · [source](https://www.geeksforgeeks.org/interview-experiences/de-shaw-interview-experience-for-technology-developer-intern-2025/)</sub>

**19.** `B` · internship · onsite · unknown

Given an array of strings A, find the longest string all of whose prefixes also appear in the array

*Reported answer:* Example: for ['a','ab','abc','abcd','aaaaa','aabsd'] the answer is 'abcd'; writer used a hashmap of all strings and checked prefixes

<sub>blog · 2020-08 · [source](https://www.geeksforgeeks.org/interview-experiences/de-shaw-summer-internship-interview-experience-2021-on-campus-vit-vellore/)</sub>

**20.** `B` · internship · onsite · unknown

Given pickup, drop and tip arrays where trip i earns drop[i]-pickup[i]+tip[i] and the next pickup must be at or after the last drop, maximise earnings

*Reported answer:* Writer concluded dynamic programming was the way to go but their code segfaulted before time ran out

<sub>blog · 2020-08 · [source](https://www.geeksforgeeks.org/interview-experiences/de-shaw-summer-internship-interview-experience-2021-on-campus-vit-vellore/)</sub>

**21.** `B` · internship · phone_technical · unknown

Q8) Puzzle. Given 10 stacks each stack contains 10 coins of 1 gram each. But one stack all coins with weight 9 gram. You have a weighing machine. You have to find the faulty stack in minimum number of weighings ?

*Reported answer:* For best case, you just need one weighing. Take 1 coin from first stack, 2 from second, 3 from third and so on and weigh them together. If there was no faulty stack, then this weight would be 550. Now if weight is 549 then 1st stack is faulty, if 548 then 2nd and so on.

<sub>blog · 2019 · [source](https://www.geeksforgeeks.org/interview-experiences/de-shaw-on-campus-internship-interview-experience-2019/)</sub>

**22.** `B` · internship · phone_technical · unknown

Q6) One of your friend is getting UI of particular website, but you are not, so what is the problem, how will use you diagnose it?

<sub>blog · 2019 · [source](https://www.geeksforgeeks.org/interview-experiences/de-shaw-on-campus-internship-interview-experience-2019/)</sub>

**23.** `B` · internship · phone_technical · unknown

How to find the intersection of two linked lists?

<sub>blog · 2023-08-01 · [source](https://www.jointaro.com/interviews/companies/de-shaw/experiences/software-engineerinternship-mumbai-august-1-2023-no-offer-positive-41d29adc)</sub>

**24.** `B` · internship · phone_technical · unknown

Given an array of n integers and an integer x, provide an algorithm that determines if a pair of integers in the array sum to x.

<sub>blog · 2017-09-01 · [source](https://www.jointaro.com/interviews/companies/de-shaw/experiences/software-engineerinternship-new-york-ny-september-1-2017-no-offer-positive-82ecc6f8)</sub>

**25.** `B` · internship · phone_technical · unknown

You are given a string which contains only a's and b's. A "good string" can be split into 3 parts. First part should contain only a's(can contain 0 also), second should contain b's and third should contain a's. Now we need to find the length of the largest good string by deleting some characters from the string.

*Reported answer:* Example given: s = "aaabbaabbbaa" answer = 10; solved recursively with an index and a 0/1/2 state variable, then memoised

<sub>blog · 2023 · [source](https://www.geeksforgeeks.org/interview-experiences/d-e-shaw-internship-interview-experience-on-campus-2023/)</sub>

**26.** `B` · internship · phone_technical · unknown

Why did you use MongoDB over MySQL, and which database performs better under different circumstances?

<sub>blog · 2025-12 · [source](https://www.geeksforgeeks.org/interview-experiences/de-shaw-interview-experience-for-system-intern-role/)</sub>

**27.** `B` · internship · phone_technical · unknown

There is an N-floor building and you have one egg. You need to find the lowest floor from which the egg breaks on dropping. Follow-up: what is the most optimal method with 2 eggs?

*Reported answer:* One egg: linear scan upward, O(N). Two eggs: use one egg to shorten the search range, then linear search inside it

<sub>blog · 2021-07 · [source](https://www.geeksforgeeks.org/interview-experiences/d-e-shaw-internship-interview-experience-on-campus-2022-2/)</sub>

**28.** `B` · internship · phone_technical · unknown

Which of the two is bigger, 50^99 or 99! ? Why?

*Reported answer:* Writer answered 50^99 and justified it by rewriting both numbers in terms of 100; the interviewers were not fully satisfied

<sub>blog · 2021-07 · [source](https://www.geeksforgeeks.org/interview-experiences/d-e-shaw-internship-interview-experience-on-campus-2022-2/)</sub>

**29.** `B` · internship · phone_technical · unknown

How would you implement your own vector (dynamic array) in C++, with add, delete, search and access and their time complexities?

<sub>blog · 2020-08 · [source](https://www.geeksforgeeks.org/interview-experiences/de-shaw-internship-interview-experience-on-campus-2021-2/)</sub>

**30.** `B` · internship · phone_technical · unknown

Calculate the time to process 1 billion instructions, given the time for each cycle

<sub>blog · 2020-08 · [source](https://www.geeksforgeeks.org/interview-experiences/de-shaw-internship-interview-experience-on-campus-2021-2/)</sub>

**31.** `B` · internship · phone_technical · unknown

Implement a Python-style list (which can hold different types of data in one list) in C++

<sub>blog · 2020-08 · [source](https://www.geeksforgeeks.org/interview-experiences/de-shaw-internship-interview-experience-on-campus-2021-2/)</sub>

**32.** `B` · internship · phone_technical · unknown

Given a regex built from \d, \w, $, ^, + and *, generate as many kinds of matching strings as possible

*Reported answer:* Writer tokenised the regex into [symbol, modifier] pairs and grew a vector of candidate strings built from 'a' and '1'

<sub>blog · 2020-08 · [source](https://www.geeksforgeeks.org/interview-experiences/de-shaw-summer-internship-interview-experience-2021-on-campus-vit-vellore/)</sub>

**33.** `B` · internship · phone_technical · unknown

There are n goods, the i-th of weight wi, and m trucks; load the trucks so each carries almost equal weight

*Reported answer:* Writer gave a DP solution for m == 2 and was not asked to generalise

<sub>blog · 2019-08 · [source](https://www.geeksforgeeks.org/interview-experiences/d-e-shaw-internship-interview-experience-on-campus/)</sub>

**34.** `B` · internship · phone_technical · unknown

Design a data structure with insert, delete and search in O(1) worst case, then add getRandom in O(1)

*Reported answer:* Once told the data was in range 1-9999 the writer used a direct-address array of 0/1 flags

<sub>blog · 2019-08 · [source](https://www.geeksforgeeks.org/interview-experiences/d-e-shaw-internship-interview-experience-on-campus/)</sub>

**35.** `B` · internship · phone_technical · unknown

You are given data for 5 years for 50 cities. Data Includes city name, date, minimum temperature, maximum temperature. You need to predict the data structure required to answer the following queries: a) Hottest city on a given date b) Coldest city on a given date c) Hottest city in entire period d) Coldest city in entire period e)Hottest day of entire period f) Coldest day of entire period

<sub>blog · 2021 · [source](https://www.geeksforgeeks.org/interview-experiences/de-shaw-interview-experienceon-campus-internship-2021/)</sub>

**36.** `B` · internship · phone_technical · unknown

You have N machines which produce bolts (each bolt weighing exactly 10 gm) with one machine which is defective and produces bolts of 9 grams. You are given an electronic weighing machine. You need to use the machine minimum number of times and tell which machine is faulty. What is the minimum number of times you will use the machine

<sub>blog · 2021 · [source](https://www.geeksforgeeks.org/interview-experiences/de-shaw-interview-experienceon-campus-internship-2021/)</sub>

**37.** `B` · internship · phone_technical · unknown

There are two traffic lights between your house and office. While going from your house to the office, you stop two times but while returning home from the office you stop only once. Given that the traffic lights are always red whenever you encounter them, how is this situation possible.

*Reported answer:* Hint given by the poster: you don't need to stop at a traffic light when you need to turn left

<sub>blog · 2022 · [source](https://www.geeksforgeeks.org/interview-experiences/d-e-shaw-internship-interview-experience-on-campus-2022/)</sub>

**38.** `B` · internship · phone_technical · unknown

Given an integer n you can perform the following two operations any number of times : (i) decrement n by 1 or (ii) divide n by any of its factors except self. Find the minimum number of operations to convert n to 0.

<sub>blog · 2022 · [source](https://www.geeksforgeeks.org/interview-experiences/d-e-shaw-internship-interview-experience-on-campus-2022/)</sub>

**39.** `B` · internship · phone_technical · unknown

Given a linked list and a node, how will you delete that node from the linked list? He asked me to explain my approach when I had a pointer to the start of the linked list as well as when I only had the pointer to the node to be deleted.

<sub>blog · 2022 · [source](https://www.geeksforgeeks.org/interview-experiences/d-e-shaw-internship-interview-experience-on-campus-2022/)</sub>

**40.** `B` · internship · phone_technical · unknown

Given a binary tree, first, print its left side view then its right side view. Print the root node only once.

*Reported answer:* The interviewer wanted the approach, the time complexities and a dry run on two test cases

<sub>blog · 2022 · [source](https://www.geeksforgeeks.org/interview-experiences/d-e-shaw-internship-interview-experience-on-campus-2022/)</sub>

**41.** `B` · internship · phone_technical · unknown

You are given a function getManager(int id) which returns the manager of the employee whose id is passed. You need to implement a function getCManager(int id1, int id2) which should return the lowest common manager of the two employees whose id is passed. You are not provided with the actual tree structure, only the getManager function.

*Reported answer:* The poster's accepted answer was to store all managers of one employee in an unordered_set and then walk the other employee's managers checking membership

<sub>blog · 2022 · [source](https://www.geeksforgeeks.org/interview-experiences/d-e-shaw-internship-interview-experience-on-campus-2022/)</sub>

**42.** `B` · internship · phone_technical · unknown

Given a sum and you have to find the no. of ways to form that sum using only consecutive numbers. For ex: sum = 21 ... Ans: 3 (total counts)

*Reported answer:* The poster solved it with the two pointer method

<sub>blog · 2020 · [source](https://www.geeksforgeeks.org/interview-experiences/de-shaw-internship-interview-experience-on-campus-2020/)</sub>

**43.** `B` · internship · phone_technical · unknown

you have given bombs and you have to find the min intensity of all the bombs such that you can skip max 2 bombs.

*Reported answer:* The poster gave a DP approach which the interviewers accepted, but could not write working code

<sub>blog · 2020 · [source](https://www.geeksforgeeks.org/interview-experiences/de-shaw-internship-interview-experience-on-campus-2020/)</sub>

**44.** `C` · new_grad · phone_technical · unknown

find the number of ways a given number can be expressed as a sum of more than 1 consecutive natural numbers

<sub>blog · unknown · [source](https://www.geeksforgeeks.org/interview-experiences/de-shaw-off-campus-fresher-interview-experience/)</sub>

**45.** `C` · new_grad · phone_technical · unknown

Given a matrix(n * m) and a queen positioned at (n-1,m/2). Find the number of ways in which the queen can reach cell no. (x,y) in minimum number of moves. There were Q queries of (x,y). The queen can move in any of the eight valid directions in one move. Preprocessing of O(n2) was allowed and queries were supposed to be answered in O(1).

<sub>blog · unknown · [source](https://www.geeksforgeeks.org/interview-experiences/de-shaw-off-campus-fresher-interview-experience/)</sub>

**46.** `C` · new_grad · phone_technical · unknown

Given stock prizes for N days. Each day you could either buy a stock or sell some/all of the stocks you have purchased previously. It is also allowed to not perform any operation for a day. Buying a stock will count as a negative addition to profit and selling will count as a positive addition to the profit. Find the maximum profit that could be achieved given the Stock prizes for N days. Example : [1,5,2,100,3,2]

*Reported answer:* Find the next maximum Stock price for each day and buy that stock only if there is any available higher prize. So the profit will be: For each ith day buying a stock ( - stockPrize[i] ) and selling the stock at a later day with highest stock prize ( i.e. +max(stockPrize[i+1,n-1] ) ). This range maximum could be easily computed using suffix maximum, given a solution in linear time.

<sub>blog · unknown · [source](https://www.geeksforgeeks.org/interview-experiences/de-shaw-off-campus-fresher-interview-experience/)</sub>

**47.** `C` · new_grad · phone_technical · unknown

What is the significance of on condition in an outer join?

<sub>blog · unknown · [source](https://www.geeksforgeeks.org/interview-experiences/de-shaw-off-campus-fresher-interview-experience/)</sub>

**48.** `C` · new_grad · phone_technical · unknown

Design and implement a class that can be used to allocate and de-allocate a certain amount of memory blocks. The class will initially have a fixed block of memory which will only be used to allocate memory. Say 1024 blocks.

<sub>blog · unknown · [source](https://www.geeksforgeeks.org/interview-experiences/de-shaw-off-campus-fresher-interview-experience/)</sub>

**49.** `C` · new_grad · phone_technical · unknown

Given a file consisting of millions of records. The data is in a structured format i.e in a tabular format with each record consisting of many attributes. How will you perform search operation on the file given the file is stored in secondary memory? Optimize it.

<sub>blog · unknown · [source](https://www.geeksforgeeks.org/interview-experiences/de-shaw-off-campus-fresher-interview-experience/)</sub>

**50.** `C` · new_grad · phone_technical · unknown

What is a Trie Data Structure? Explain it's node structure and working? What is it's applications?How will you optimize the memory usage in Trie?

<sub>blog · unknown · [source](https://www.geeksforgeeks.org/interview-experiences/de-shaw-off-campus-fresher-interview-experience/)</sub>

**51.** `C` · new_grad · phone_technical · unknown

A simple Game Theory question: Given Two Players A and B separated by N number of tiles. In a move, each one can move one or two-step ahead. Who will win if player A starts and each one plays alternately and optimally. The player who is not able to make any move losses the game.

*Reported answer:* if you write down all the values of f() you will find that it decomposes to f(n) = 0 if n is a multiple of 3 otherwise f(n)=1

<sub>blog · unknown · [source](https://www.geeksforgeeks.org/interview-experiences/de-shaw-off-campus-fresher-interview-experience/)</sub>

**52.** `C` · internship · phone_technical · unknown

You are a given a text written in JSON ... Now he asked me to design a structure which can store this information from this code and answer the queries efficiently. For example if the query is A.B.C then answer will be {D:45}, similarly if the query is A.C.B then answer will be 98, formally I have to return all the information inside the given path or determine that the given path is invalid. An invalid path means a path which does not exists for example B.A

*Reported answer:* Lastly I thought an approach using TRIE data structure (better than the previous one) and I was able to code it at the time of interview

<sub>blog · unknown · [source](https://www.geeksforgeeks.org/interview-experiences/de-shaw-interview-experience-for-2021-internship-on-campus/)</sub>

**53.** `D` · experienced · take_home · 2025

Calculate Volume weighted average price (VWAP)

<sub>chat_telegram · 2025-05-17 · [source](https://t.me/usinterview/23220)</sub>


## Jump Trading  (16)

**1.** `B` · internship · online_assessment · unknown

Given a sequence A of length n (n<=100000), get the pair (i,j) such that |i-j|>1 and minimize A[i]+A[j].

<sub>blog · 2023-03-06 · [source](https://www.jointaro.com/interviews/companies/jump-trading/experiences/c-developer-intern-china-march-6-2023-no-offer-neutral-efe36ae5/)</sub>

**2.** `B` · unknown · onsite · unknown

a straightforward whiteboard question with two separate tasks: 1. Convert decimal-based number to a 16-bit binary representation 2. Represent as 4x4 matrix of 0s and 1s 3. Detect if path of 0s exists in matrix from top left to bottom right cell and if so, print out the path in the format of a string; otherwise, return a "No path" string

<sub>wso · 2018-02-05 · [source](https://www.wallstreetoasis.com/company/jump-trading/interview)</sub>

**3.** `B` · unknown · onsite · unknown

Given a char buffer[4096], write a malloc implementation.

<sub>blog · 2016-11-09 · [source](https://www.jointaro.com/interviews/companies/jump-trading/experiences/quantitative-software-engineer-new-york-new-york-november-9-2016-no-offer-negative-d0b7db19)</sub>

**4.** `B` · unknown · onsite · unknown

Given a dependency graph, write a function to return a vector of all nodes such that all children are listed before the parent. Then make the function print each node only once.

<sub>blog · 2016-11-09 · [source](https://www.jointaro.com/interviews/companies/jump-trading/experiences/quantitative-software-engineer-new-york-new-york-november-9-2016-no-offer-negative-d0b7db19)</sub>

**5.** `B` · unknown · onsite · unknown

Two players are playing a game where you can pick either 1 or 2. The player that gets to 15 wins. Is there a strategy such that one player will always win, and if so, which player can use it?

<sub>blog · 2016-11-09 · [source](https://www.jointaro.com/interviews/companies/jump-trading/experiences/quantitative-software-engineer-new-york-new-york-november-9-2016-no-offer-negative-d0b7db19)</sub>

**6.** `B` · unknown · onsite · unknown

Write a dot product of 1,000,000 numbers that runs as fast as possible using SSE/AVX.

<sub>blog · 2016-11-09 · [source](https://www.jointaro.com/interviews/companies/jump-trading/experiences/quantitative-software-engineer-new-york-new-york-november-9-2016-no-offer-negative-d0b7db19)</sub>

**7.** `B` · internship · onsite · unknown

For a 2-level nested loop iterating a 2D array, will exchanging the loop iteration index make a difference in performance?

<sub>blog · 2012-02-01 · [source](https://www.jointaro.com/interviews/companies/jump-trading/experiences/software-engineer-internship-chicago-illinois-february-1-2012-no-offer-neutral-2e39e052)</sub>

**8.** `B` · experienced · onsite · unknown

Implement std:: classes like shared_ptr and vector.

<sub>blind · 2025-06-02 · [source](https://www.teamblind.com/post/swe-to-hedge-fundquant-firm-k6vktyvq)</sub>

**9.** `B` · internship · onsite · unknown

How I would store key value pairs, then a discussion about how I would implement a hash map data structure, tradeoffs between various implementations, and implement methods to add a key to the hashmap and retrieve a key from the hashmap.

<sub>wso · 2019-10-08 · [source](https://www.wallstreetoasis.com/company/jump-trading/interview)</sub>

**10.** `B` · experienced · onsite · unknown

Two of the questions were leetcode medium-ish. But not exactly leetcode questions. The rest were not on leetcode but I would categorize them as high medium. They do go very deep into optimization all the way to optimizing for the underlying architecture

<sub>blind · 2022-05-08 · [source](https://www.teamblind.com/post/jump-trading-interview-process-swe-k5k5jexb)</sub>

**11.** `B` · unknown · onsite · unknown

implement deque which invalidates iterators, implement lazy leaky singletone, implement allocator, tell me about virtual memory, codeforces div2 D questions, sfinae simple stuff

<sub>blind · 2022-09-30 · [source](https://www.teamblind.com/post/old-mission-capital-jump-trading-xnpmnp28)</sub>

**12.** `B` · internship · phone_technical · unknown

Two people were playing a game to find words from a dictionary.

<sub>blog · 2023-11-14 · [source](https://www.jointaro.com/interviews/companies/jump-trading/experiences/software-engineer-internship-chicago-illinois-november-14-2023-no-offer-positive-fe777791)</sub>

**13.** `B` · internship · phone_technical · unknown

Finding the first instance of a specific value in a sorted list.

<sub>blog · 2020-06-29 · [source](https://www.jointaro.com/interviews/companies/jump-trading/experiences/software-engineer-intern-united-states-june-29-2020-no-offer-positive-3c7cf4f1)</sub>

**14.** `B` · internship · phone_technical · unknown

Given two lists of tuples representing time series data, merge them to form one large time series represented as a list of tuples.

<sub>blog · 2025-09-29 · [source](https://www.jointaro.com/interviews/companies/jump-trading/experiences/software-engineer-internship-united-kingdom-september-29-2025-no-offer-neutral-8a8eb483)</sub>

**15.** `C` · internship · online_assessment · unknown

Implement a users endpoint against a written spec: return status code 400 if age is missing; 400 if age is not a number or the name is not a string; 400 if name is longer than 32 characters.

<sub>1point3acres · unknown · [source](https://www.1point3acres.com/bbs/thread-1023934-1-1.html)</sub>

**16.** `C` · internship · onsite · Summer 2023

第一题的operations有可能是三个吗?或者多个每个只能用一次么,还是所有list的数字都可以用任意这四个里面的operation combine?

*English:* Could the first question's operations be three? Or several, each usable only once? Or can all the numbers in the list be combined using any of these four operations?

<sub>1point3acres · 2022-11 · [source](https://www.1point3acres.com/bbs/thread-942280-1-1.html)</sub>


## Hudson River Trading  (15)

**1.** `B` · internship · online_assessment · unknown

Find the maximum width of two arrays without a tree.

<sub>blog · 2020-12-03 · [source](https://www.jointaro.com/interviews/companies/hudson-river-trading/experiences/software-engineering-intern-united-states-december-3-2020-no-offer-positive-4795704d)</sub>

**2.** `B` · internship · online_assessment · unknown

Write a program that can add two binary strings (without leading zeroes).

<sub>blog · 2022-11-01 · [source](https://www.jointaro.com/interviews/companies/hudson-river-trading/experiences/software-engineerinternship-united-states-november-1-2022-no-offer-positive-4c20631b)</sub>

**3.** `B` · internship · online_assessment · unknown

Implement a front-end interface for virtual credit card generation.

<sub>blog · 2022-12-28 · [source](https://www.jointaro.com/interviews/companies/hudson-river-trading/experiences/software-engineer-intern-united-states-december-28-2022-no-offer-neutral-a3a68e56)</sub>

**4.** `B` · unknown · online_assessment · unknown

given a string with only A, B, C or D, remove adjacents A and Bs and remove adjacent C and Ds so 'ABACD' becomes 'ACD' becomes 'A'

<sub>reddit_thread · 2022-01-08 · [source](https://www.reddit.com/r/csMajors/comments/rz3dvc/oa_with_hudson_river_trading_and_preparation/)</sub>

**5.** `B` · internship · onsite · unknown

Design a system that can process transactions and perform specific operations on them.

<sub>blog · 2023-10-01 · [source](https://www.jointaro.com/interviews/companies/hudson-river-trading/experiences/software-engineer-internship-new-york-ny-october-1-2023-no-offer-positive-14c6dc5d)</sub>

**6.** `B` · internship · onsite · unknown

For example, the balanced tree started as basically, "Do you know how to use a BBST and how to traverse it?" to, "How can I rebuild it?" to then, reasoning about real internals (such as walking a subsection of the binary tree; walking a subtree is O(K + nlogn), even if random access to all nodes is Klog(n)).

<sub>blog · 2025-10-13 · [source](https://www.jointaro.com/interviews/companies/hudson-river-trading/experiences/software-engineerinternship-united-states-october-13-2025-accepted-offer-positive-ab3e79e2)</sub>

**7.** `B` · unknown · onsite · unknown

a large coding task where you take a spec and implement it, questions on OS/"how computers work", and system design questions are the main things usually covered.

<sub>blind · 2023-05-04 · [source](https://www.teamblind.com/post/hudson-river-trading-interview-process-87mxp0h4)</sub>

**8.** `B` · internship · phone_technical · unknown

Find the k largest values in an array in average time O(n).

<sub>blog · 2020-10-01 · [source](https://www.jointaro.com/interviews/companies/hudson-river-trading/experiences/software-engineer-intern-united-states-october-1-2020-no-offer-neutral-bf7b5f5d)</sub>

**9.** `B` · internship · phone_technical · unknown

Design an abstract class for task scheduling.

<sub>blog · 2024-09-26 · [source](https://www.jointaro.com/interviews/companies/hudson-river-trading/experiences/software-engineering-intern-new-york-ny-september-26-2024-no-offer-neutral-8cd5c8d8)</sub>

**10.** `B` · internship · phone_technical · unknown

What happens in the synthesis stage of building an FPGA design?

<sub>blog · 2024-01-04 · [source](https://www.jointaro.com/interviews/companies/hudson-river-trading/experiences/hardware-engineer-internship-new-york-ny-january-4-2024-declined-offer-positive-177d38ab)</sub>

**11.** `B` · internship · phone_technical · unknown

Design concurrent framework and contact tracing graph problem.

<sub>blog · 2024-11-29 · [source](https://www.jointaro.com/interviews/companies/hudson-river-trading/experiences/software-engineerinternship-singapore-november-29-2024-no-offer-negative-f71a48c9)</sub>

**12.** `B` · internship · phone_technical · unknown

An expected value question involving order statistics

<sub>wso · 2024-10 · [source](https://www.wallstreetoasis.com/company/hudson-river-trading-llc/interview/campus-algo-dev)</sub>

**13.** `B` · new_grad · phone_technical · unknown

A hard dynamic-programming problem, solution only - no code required

<sub>blind · 2023-10-25 · [source](https://www.teamblind.com/post/hudson-river-trading-c-software-engineer-interview-dbyj50eq)</sub>

**14.** `B` · internship · take_home · unknown

Design a two-stage pipelined ALU that handles a collection of instructions in hex.

<sub>blog · 2021-11-21 · [source](https://www.jointaro.com/interviews/companies/hudson-river-trading/experiences/hardware-engineer-intern-united-states-november-21-2021-no-offer-neutral-4624d8cb)</sub>

**15.** `C` · internship · online_assessment · 2024

第二题 union find,最后count两个group的成员个数 第三题 第一部分topological sort?

*English:* Question 2 is union-find, finally counting the members of the two groups. Question 3: is the first part topological sort?

<sub>1point3acres · unknown · [source](https://www.1point3acres.com/bbs/thread-1022110-1-1.html)</sub>


## Akuna Capital  (8)

**1.** `B` · unknown · online_assessment · unknown

How can we get the output of the combination of two strings with some requirements?

<sub>blog · 2020-10-01 · [source](https://www.jointaro.com/interviews/companies/akuna-capital/experiences/quant-development-boston-ma-october-1-2020-no-offer-neutral-05436f5d)</sub>

**2.** `B` · unknown · online_assessment · unknown

Find the maximum number of points in a polygon with a maximum perimeter, given the coordinates of all points.

<sub>blog · 2018-07-01 · [source](https://www.jointaro.com/interviews/companies/akuna-capital/experiences/quantitative-software-developer-united-states-july-1-2018-no-offer-negative-04c8914b)</sub>

**3.** `B` · internship · online_assessment · unknown

Given two lists of exchange records, each record has a timestamp associated with the transaction. Timestamps might have an error within 0.05s. Compare the two lists and return whether all records in them can be matched.

<sub>blog · 2021-08-25 · [source](https://www.jointaro.com/interviews/companies/akuna-capital/experiences/software-engineer-intern-united-states-august-25-2021-no-offer-positive-4f76616e)</sub>

**4.** `B` · unknown · onsite · unknown

申的C++ Junior Dev,似乎要on-site了,有人面过么?求点经验,感觉略虚,还是E文的。

*English:* I applied for C++ Junior Dev and it looks like I'm going to on-site. Has anyone interviewed? Looking for some experience — I feel a bit shaky, and it's in English too.

<sub>nowcoder · 2016-10-25 · [source](https://www.nowcoder.com/discuss/353153964797534208)</sub>

**5.** `B` · unknown · phone_technical · unknown

How to determine the max value in a sliding window (didn't know what a monotonic queue was)

<sub>wso · 2025-10-19 · [source](https://www.wallstreetoasis.com/company/akuna-capital-llc/interview)</sub>

**6.** `B` · internship · phone_technical · unknown

What's the difference between is and == , and how do you override both?

<sub>blog · 2019-08-01 · [source](https://www.jointaro.com/interviews/companies/akuna-capital/experiences/software-engineerinternship-united-states-august-1-2019-no-offer-neutral-1ee81320)</sub>

**7.** `B` · internship · phone_technical · unknown

Implement a String object without using std::string or any of its methods.

<sub>blog · 2021-08-01 · [source](https://www.jointaro.com/interviews/companies/akuna-capital/experiences/c-developer-intern-united-states-august-1-2021-no-offer-positive-e98411cb)</sub>

**8.** `D` · experienced · online_assessment · 2025

Write an exchange order Matching Engine. The supported operations are: BUY SELL CANCEL MODIFY PRINT

<sub>chat_telegram · 2025-10-13 · [source](https://t.me/usinterview/25781)</sub>


## Jane Street  (7)

**1.** `C` · experienced · onsite · 2025

- How would you design the abstractions for exchanges and instruments? - How do you ensure performance when there are 10^6 quote updates across instruments and exchanges every second?

<sub>other · 2025-05-12 · [source](https://web.archive.org/web/20250614052758/https://www.1point3acres.com/bbs/thread-1128313-1-1.html)</sub>

**2.** `C` · experienced · phone_technical · 2025

Design a supermarket queue. ... [karma wall] ... r customers? How to implement? (Use a red-black tree)

<sub>other · 2025-06-01 · [source](https://web.archive.org/web/20250630171445/https://www.1point3acres.com/bbs/thread-1131152-1-1.html)</sub>

**3.** `C` · experienced · phone_technical · 2025

“customers can go between other customers”是不是说新进来的顾客可以插到队伍中间?为啥一定要用红黑树,其他数据结构不行吗?

*English:* Does "customers can go between other customers" mean a newly arriving customer can cut into the middle of the queue? And why must a red-black tree be used — would no other data structure do?

<sub>other · 2025-06-01 · [source](https://web.archive.org/web/20250630171445/https://www.1point3acres.com/bbs/thread-1131152-1-1.html)</sub>

**4.** `D` · experienced · phone_technical · 2024

Implement APIs for a tree class backend — Tree node的定义已知,所有API已知(不用实现)class Node { vector getAncestors

*English:* Implement APIs for a tree class backend. The tree node definition is given and all APIs are given (you do not implement them): class Node { vector getAncestors... (preview truncated)

<sub>chat_telegram · 2024-12-03 · [source](https://t.me/usinterview/20583)</sub>

**5.** `D` · experienced · phone_technical · 2025

Design a supermarket queue. Operations: add customer, change cu

<sub>chat_telegram · 2025-05-31 · [source](https://t.me/usinterview/23478)</sub>

**6.** `D` · experienced · phone_technical · 2025

Implement 一个connect four的游戏,区别在于新放进去球会掉在最底下,然后把上面球顶上去。

*English:* Implement a Connect Four game, except that a newly inserted ball drops to the very bottom and pushes the balls above it up.

<sub>chat_telegram · 2025-07-20 · [source](https://t.me/usinterview/24268)</sub>

**7.** `D` · experienced · phone_technical · unknown

算数part 1: input是一个算数组,求结果只考虑+-x /eg. (4 + 5) x 6 = ? parser的部分不用写直接求结果

*English:* Arithmetic, part 1: the input is an array representing an arithmetic expression; compute the result considering only + - x /, e.g. (4 + 5) x 6 = ? You do not need to write the parser, just produce the result.

<sub>chat_telegram · 2022-09-19 · [source](https://t.me/usinterview/14711)</sub>


## Citadel  (6)

**1.** `B` · unknown · datathon · 2024

In Python, which of the following gives the correct order, from first to last, of scope resolution? A. local function, enclosing function, global statements, built-in names B. local function, global statements, built-in names, enclosing function C. built-in names, global statements, local function, enclosing function D. built-in names, global statements, enclosing function, local function E. local function, global statements, enclosing function, built-in names

*Reported answer:* 【参考答案】A

<sub>blog · 2024-06-25 · [source](https://blog.csdn.net/dcdsc/article/details/139953481)</sub>

**2.** `B` · unknown · datathon · 2024

In Python, if you had to iteratively read over two files line-by-line, which of the following would be the BEST way to accomplish this task? A. Use with open () to open the two files as f1 and f2 then use readline() and a for loop to iteratively read lines from each file B. Use open () to open the two files as f1 and f2, then use readline() and a for loop to iteratively read lines from each file C. Use with open () to open the two files as f1 and f2, then use zip() to iterate over the two files together D. Use open () to open the two files as f1 and f2, then use zip() to iterate over the two files together E. Implement a file seek () function and call the function for the two files simultaneously

*Reported answer:* 【参考答案】C

<sub>blog · 2024-06-25 · [source](https://blog.csdn.net/dcdsc/article/details/139953481)</sub>

**3.** `B` · unknown · datathon · 2024

In Python, which of the following statements are true?: • I. The pipe module can be used to run shell commands in a program • Il. A pickle can store any Python object except tuples in string format • Ill. If you have a Python program called player.py, then you can import the module by running import player. py A. l and Il only B. I and Ill only C. Il and Ill only D. I, Il, and Ill E. None of A through D

*Reported answer:* 【参考答案】E

<sub>blog · 2024-06-25 · [source](https://blog.csdn.net/dcdsc/article/details/139953481)</sub>

**4.** `B` · internship · online_assessment · unknown

Given an nxn chess board, return the minimum number of knight moves it would take to get from point (a,b) to point(c,d)

<sub>glassdoor · 2023-09-24 · [source](https://www.glassdoor.com/Interview/Citadel-Software-Engineering-Intern-Interview-Questions-EI_IE14937.0,7_KO8,35.htm)</sub>

**5.** `D` · experienced · onsite · 2023

2) C++ 函数 void func(int8_t i);void main() { int32_t x = 1; func(x); }会发生什么 ?

*English:* 2) A C++ function void func(int8_t i); void main() { int32_t x = 1; func(x); } — what happens?

<sub>chat_telegram · 2022-08-18 · [source](https://t.me/usinterview/14353)</sub>

**6.** `D` · experienced · phone_technical · 2026

Find all elements equal to K in a sorted array.

<sub>chat_telegram · 2026-06-30 · [source](https://t.me/usinterview/28985)</sub>


## DRW  (6)

**1.** `B` · new_grad · online_assessment · unknown

You get more points on OA if you write at least 1/3 questions in C++ iirc

<sub>blind · 2020-09-01 · [source](https://www.teamblind.com/post/DRW-phone-interview-qPFU5TMW)</sub>

**2.** `B` · internship · phone_technical · unknown

How would you find all the words that are anagrams of each other in a text document?

<sub>blog · 2018-10-07 · [source](https://www.jointaro.com/interviews/companies/drw/experiences/software-engineer-internship-united-states-october-7-2018-no-offer-neutral-1ae58c58)</sub>

**3.** `B` · internship · phone_technical · unknown

Given some multithreaded code in C++, explain the flow and result of the program.

<sub>blog · 2023-09-01 · [source](https://www.jointaro.com/interviews/companies/drw/experiences/software-engineer-intern-london-england-september-1-2023-no-offer-neutral-7a2332eb)</sub>

**4.** `B` · experienced · phone_technical · unknown

You will have to download Amazon DCV Viewer and remote into an EC2 instance. You will have to complete a coding task in an ide of your choice with the interviewer also logged in. Pretty standard stuff, not hardcore leetcode.

<sub>blind · 2025-02-05 · [source](https://www.teamblind.com/post/drw-senior-software-engineer-interview-2fu5tboo)</sub>

**5.** `B` · unknown · superday · unknown

A graph problem at the on-site superday, described as quite difficult

<sub>wso · 2020-09 · [source](https://www.wallstreetoasis.com/company/drw/interview/full-time)</sub>

**6.** `B` · unknown · take_home · unknown

Implement a game according to some specs. No test cases given

<sub>glassdoor · 2025-05-22 · [source](https://www.glassdoor.com/Interview/DRW-Interview-Questions-E235115.htm)</sub>


## Optiver  (5)

**1.** `D` · experienced · online_assessment · 2025

Given a two-dimensional character matrix, create a function that identifies how many times the sequence "OPTIVER" appears. Matches can be found in straight lin

<sub>chat_telegram · 2025-06-10 · [source](https://t.me/usinterview/23610)</sub>

**2.** `D` · experienced · online_assessment · 2026

design a news subscription process engine两个小时

*English:* Design a news subscription process engine. Two hours.

<sub>chat_telegram · 2026-07-27 · [source](https://t.me/usinterview/29070)</sub>

**3.** `D` · experienced · phone_technical · 2025

Design a queue,discuss the performance tradeoff.

<sub>chat_telegram · 2025-08-08 · [source](https://t.me/usinterview/24673)</sub>

**4.** `D` · experienced · phone_technical · 2024

design 一个class提供四个api,带on的都是callback 用来update internal data structure。最后一

*English:* Design a class exposing four APIs; the ones prefixed with "on" are callbacks used to update the internal data structure. The last...

<sub>chat_telegram · 2024-10-25 · [source](https://t.me/usinterview/20082)</sub>

**5.** `D` · experienced · phone_technical · 2025

An array of 1000 integers of 0-1000000,how many bytes does it require to store?

<sub>chat_telegram · 2024-12-12 · [source](https://t.me/usinterview/20685)</sub>


## Two Sigma  (5)

**1.** `B` · internship · online_assessment · unknown

Design a random number generator that does not output a number that has already been generated.

<sub>blog · 2020-03-10 · [source](https://www.jointaro.com/interviews/companies/two-sigma/experiences/software-engineerinternship-united-kingdom-march-10-2020-no-offer-positive-fb1924e4)</sub>

**2.** `B` · experienced · online_assessment · unknown

Two medium leetcode questions which I've seen before thus I was able to solve it in 30 minutes (you get 3 hours).

<sub>blind · 2021-04-20 · [source](https://www.teamblind.com/post/two-sigma-interview-advice-mazcdp6r)</sub>

**3.** `B` · internship · onsite · unknown

You were given a table with four currencies and their respective trading values (not symmetric). You were asked that, given a start currency and an end currency, you maximize the end value. You cannot trade for the same currency twice.

<sub>blog · 2019-01-01 · [source](https://www.jointaro.com/interviews/companies/two-sigma/experiences/software-engineerinternship-new-york-ny-january-1-2019-no-offer-positive-bfe6e554)</sub>

**4.** `B` · internship · phone_technical · unknown

How do you pick random objects given weights?

<sub>blog · 2019-06-05 · [source](https://www.jointaro.com/interviews/companies/two-sigma/experiences/software-engineerinternship-united-states-june-5-2019-no-offer-negative-9d46e9ec)</sub>

**5.** `B` · internship · phone_technical · unknown

A LeetCode-hard equivalent coding problem in the one-on-one round

<sub>wso · 2025-02 · [source](https://www.wallstreetoasis.com/company/two-sigma-investments/interview/software-engineering-intern-1)</sub>


## Bridgewater Associates  (1)

**1.** `B` · unknown · onsite · 2025

Given a list of items and their utilitites, give an algorithm to maximise utility

<sub>interview_review_db · 2025-09-30 · [source](https://www.wallstreetoasis.com/company/bridgewater/interview)</sub>


## Citadel Securities  (1)

**1.** `B` · unknown · online_assessment · unknown

Again, start and end times. Again, overlapping intervals. But this time the task changed subtly. Instead of asking for the global maximum number of simultaneous employees, they asked for the maximum number of direct overlaps centered around a single employee. ... If one employee ends at time 5 and another starts at time 5, do they overlap? In this problem, yes.

*Reported answer:* Sort the start times. Sort the end times. For each interval, determine how many intervals finish strictly before it starts. Then determine how many intervals begin strictly after it ends. Everything else overlaps. Binary search; O(n log n).

<sub>blog · 2026-02-22 · [source](https://hiya31.medium.com/what-they-asked-me-in-the-citadel-securities-hackerrank-coding-round-ed3ceded3c04)</sub>


## Old Mission Capital  (1)

**1.** `B` · unknown · onsite · unknown

implement deque which invalidates iterators, implement lazy leaky singletone, implement allocator, tell me about virtual memory, codeforces div2 D questions, sfinae simple stuff

<sub>blind · 2022-09-30 · [source](https://www.teamblind.com/post/old-mission-capital-jump-trading-xnpmnp28)</sub>


## Squarepoint Capital  (1)

**1.** `B` · unknown · phone_technical · 2024

What is the difference between multi-thread and multi-processing

<sub>interview_review_db · 2025-01-13 · [source](https://www.wallstreetoasis.com/company/squarepoint-capital/interview)</sub>


## Susquehanna International Group  (1)

**1.** `C` · unknown · online_assessment · unknown

If day is a “Good” Day, [there] is a 60% chance that the next day will be “Good” and a 40% chance it will be “Bad”. If day is a “Bad” Day, there is a 70% chance that the next day will be “Bad” and 30% chance it will be “Good”. If today is Good Day, on average, how many days do we have to wait until the next “Bad” Day?

*Reported answer:* No final number stated. A commenter gives the full method: 如果今天是好天气,1天后是坏天气的概率是0.4,2天后坏天气的概率是0.6*0.4,3天后坏天气的概率是0.6*0.6*0.4 ... n天后的坏天气概率是0.6^(n-1)*0.4, then sums n * P(n) by the 错位相减 (shift-and-subtract) trick, noting it matches the Markov-chain answer.

<sub>1point3acres · 2021-02 · [source](https://www.1point3acres.com/bbs/thread-719224-1-1.html)</sub>


## Tibra Capital  (1)

**1.** `B` · unknown · phone_technical · interviewed 2015

Given a random variable x, and a series of random varies y_1, y_2, ..., y_x, what is the expected sum of the random variables y_1 ... y_x given that x is drawn from a normal distribution with mean 10, and variance 500, and y from uniform on the interval 0, 1. I think there was some speciication that if x is negative, we re draw x, but I'm not a 100% sure.

<sub>interview_review_site · 2016-11-07 · [source](https://www.wallstreetoasis.com/company/tibra-capital/interview)</sub>


## Tower Research Capital  (1)

**1.** `B` · internship · onsite · interviewed 2012

How do you find two numbers in an array that sum to x?

<sub>interview_review_site · 2012-11-22 · [source](https://www.wallstreetoasis.com/company/tower-research-capital/interview)</sub>

