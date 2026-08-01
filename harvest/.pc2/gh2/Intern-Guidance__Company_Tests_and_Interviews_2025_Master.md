REPO: SarthakVerma18/Intern-Guidance
PATH: Company_Tests_and_Interviews_2025_Master.md
URL: https://github.com/SarthakVerma18/Intern-Guidance/blob/main/Company_Tests_and_Interviews_2025_Master.md

**Company Test Details:**

1. **Millennium \- 12th July**  
     
   2 coding questions, 5 MCQs \- 2hrs

MCQs \- Sample Normal distribution, graph of poisson distribution, proportion of marks in tests,  
	Probab that last black ball to pick fro urn is the 9th ball you pick

Coding \-   
1\. BFS \+ Binary Search \- move in a grid to maximize minimum Manhattan distance from blocked nodes  
 2\. Trees \+ DP  
Tree with n nodes rooted at 0\. Nodes are from 0 to n-1. n-1 edges. Edges are from g\_from\[i\] to   
G\_to\[i\]. Each node has arr\[i\]. Collect values at nodes using one of 2 methods:  
\-\> Collect arr\[i\]-k  
\-\> Collect floor(arr\[i\]/2) \-\> If this is chosen, then all values of node j on the nodes subtree are changed to floor(arr\[i\]/2). Can only collect the value at a node if it’s parent’s value has been collected before (except the root). Maximize the total.

2. **Flipkart (Early Careers) \- 13th July**

3 coding questions \- 1\. Knapsack type dp (int dp\[i\]\[rem\]\[rem\_bags\])  
			2\. Remove bridge nodes  \+ MCST  
			3\. Ternery Search \- convert 2 arrays a and b (odd size n) to …x+3,x+2,x+1,x,x+1,x+2,x+3,.... in minimum cost.

3. **JPMC Quant \- 13th July**  
     
   Paper 1 \- 30 MCQs, 35 mins  
   Probab and Statistics \- 12 questions, \+1, \-0.25 \- Very general probab, variance, co-variance (good problems)  
     
   General math \- 8 questions, \+1, \-0.25 \- Very general math, min. Value of tanA+tanB+tanC, series convergence (Leibnitz), telescoping, train moving towards each other  
     
   CS \- 10 questions, \+1, \-0.25 \- n-ery tree, recursive function time complexity, output of OOPS problem, sorting algos, most efficient way to do p\*q/r\*s

	Paper 2 \- 2 coding questions (60 min) \- \+3,0 and \+5,0

1. Heaps related scheduling question \- A→B-\>C process, p,q,r machines of each of A,B,C, each machine takes t1,t2,t3 respectively. Find minimum time to finish n tasks.  
2. DP \- split array into subarrays continuously till all single elements with minimum possible cost (take min. of left, right, and cost). Cost is the difference between the maximum of the 2 subarrays.

**4\. Ebullient Quant Research \- 17th July**

**1:30 hr**  
5 Objective (Only answers required), 5 Subjective of varying marks, 2 sets A and B

Objective:

1. Sum of largest odd factors of all numbers from 549 to 1098

Just pull out evens  \- their largest odd sum is same as sum of their /2s. Repeat to get the answer as 1 \+ 3 \+ … \+ 1097 \+ 549

2. Given 6 elephants of distinct weights, place them in a Pascal’s triangle such that there is always a heavier elephant in the immediate 2 below a lighter one

Just count cases

3. Given heads falls with probability p \> 0.5, what is the expected number of tosses to get equal number of heads and tails, given the first toss is a head  
   Infinity  
     
4. Ebull and Ebear play in a first-to-win 5 matches, Ebull wins with probab ⅔, what is the probab that someone wins in exactly 7 matches

Simple Bernoulli

5. Number of values in 8 to 80085 that cannot be expressed as a difference of squares

Soln: Just figure out that you can make a-b \= 1, a+b \= 4k+1, 4k+3 and a-b \= 2, a+b \= 4k \- but 4k+2 is not possible as parity of a-b and a+b is same.  
Subjective:  
1\. Given a regular tetrahedron placed randomly in space, light is shown from above. Expected area of the shadow (Some hints were given, to find proportionality with surface area, for any convex solid)  
Soln:   
2\. You roll a dice continuously and get the sum as reward. But if you get a number you already got, you lose everything. What is the best strategy to maximize expected winnings, and what is this maximum winnings.

3\. There are 21 players of distinct levels and they take part in a tournament as follows:

A player is randomly chosen (the defender). Then another player is randomly chosen (the challenger) to compete with the defender. Who ever loses is out and the winner continues. The next challenger is randomly chosen to compete with the winner.  
Elliot has level 11\. What is the expected number of matches he plays?

Not sure about the solution yet\!\!

4\. Given a whole number n, prove that there exists some multiple of n whose sum of digits is odd

5\. x customers, y vendors. Every customer is connected to every vendor to form a full bipartite graph. Price is between 1 and x/2 ( x is even). There should be no cycle. (Doubt)

4\.

**5\. Morgan Stanley \- 17th July**

2hrs

Very easy test on basic probab and math. Different 15-20 min sections on probab, aptitude, english, spoken english etc. 2 coding questions \- 1 was dp on trees, other was using a custom sorting function

**6\. APT Research \- 17th July**

1:30 hr  
16 easy proab and puzzles (3 on painting a cube and slicing into smaller cubes) in 20 mins  
3 coding questions (easy-medium CP type)  
Given vector of strings, can swap letters between any to strings and even within string, find the maximum number of palindromes you can form

Given a vector of strings holding starting and ending times of people busy in HH:MM type of format, find if they all can meet for k minutes in the day

**7\. Qube RT \- 18th July** 

75 mins

12 Objective questions on probab statistics \- \*\* Null hypothesis and correlation of data in linear regression, what does df.dropna(), What happens when the features in linear regression are highly correlated, what are the fundamental assumptions of linear regression

2 coding questions \- Given array, take an element, half it and add it’s ceil back to the array k times \- find the minimum sum (priority queue)

Given string return the number of subarrays which have only vowels and all 5 vowels (Nice sliding window problem)

**8\. Adobe \- 18th July**

**1.5 hrs**

20 MCQs, 2 coding problems (Given indices i1, i2, i3 maximize sum(1,i1)-sum(i1,i2) \+ sum(i2,i3) \- sum(i3, n+1)) where sum(i,j) means arr\[i\] \+ …. Arr\[j-1\], n \<= 3000\.

MCQs were on Aptitude, probab, statistics for data, LLMs

**9\. Da Vinci \- 18th July**

19 questions, 20 mins  
Questions on expected value, probab, P\&C, how many people are lying, etc.

**10\. DTL \- 18th July**

Linear regression, P\&C probab and olympiad math

**11\. Microsoft**  
2 easy coding questions, doing it quickly is key.  
Given a vector of strings, return the sorted vector of strings by removing all words which have an anagram (same letters, different order) before it  
Given 2 strings x and y, find the maximum size of a substring of y which is a subsequence of x  
(use binary search)

**12\. WorldQuant**

2 hrs   
JEE Advanced kind of paper. 2 sections 12 questions each \- MCQs, then integer answer  
More than 1 correct answers.  
Questions were on \- probab, P\&C (pretty tough) and which data structure to use, big O time complexity. They tried to frame every question as a finance related thing.  
C++ syntax related question.  
WorldQuant \- GreenBook pg. 34

**13\. IMC**

75 mins technical \+ 40 mins Neurolympics (can practice online)

Technical test had 26 questions \- 15 math, 10 sequences, 1 coding (1st APT problem on scheduling \+ string handling)

Sequences were almost all easy to medium. Math was medium to hard, there were a few heard on the street type of problems.   
Boys to girls ratio with p \= 0.6, and birthing till 2nd boy. \- Just find the expected number of girls \- very simple infinite summation  
A chef cuts a pie into 7 pieces in 3 cuts, how many pieces if he can do at max. 8 cuts (answer range was 30-50).  
Famous recursion \- P(0) \= 1, P(k) \= P(k-1) \+ k

You roll 10-sided die till the numbers are strictly increasing, and the total rolls value is your payoff. What is the expected number of rolls and expected payoff. 

Expected number of rolls is just summation of 10Ck/10^k from k \= 1 to 10, which is (1 \+ 1/10)^10 \- 1 \= e-1 which is around 1.7  
Given a bus comes on an average every 10 minutes, and it’s speed is 30 kmph, you walk at 5kmph, what is the better mode of transport to travel to your destination which is 1 km away.

How many to reject among 100 candidates till we get the best candidate (37 \- famous problem):  
k is the position of the best candidate. r is the index of the person we hire. (Didn’t understand this, try to understand this better)

10 prisoners numbered from 1 to 10 need to pick their respective numbers from 10 boxes (random). Each prisoner gets to open 5 boxes. If any one prisoner gets a wrong number they are all executed. The prisoners get to decide a strategy before going in. What is the probability that they all survive.

Sleep well for NeurOlympics

**14\. Google**

1 hr test, 2 questions (similar to Microsoft) on HackerEarth 

1. What is the smallest special number greater than N. A number is special if each digit d in it occurs d times.  
2. Given Z zeros, O ones, and a number K, what is the number of sequences who have the length of the longest non-decreasing subsequence atleast K.

**14\. Optiver**  
No games etc. this year, only NumberLogic (Sequences) and BeatTheOdds (Probab). Sequences was easy to medium, 26 questions in 25 mins. Probability was extremely tough with a lot of time pressure (30 questions, 1.5 min per question).

You are at a vertex of a decagon, toss a coin to go CW or ACW. Expected number of tosses to reach the opposite end, expected number of tosses to reach back to where you are.  
Pick 2 3 digit numbers, probab that there diff is \< 100

Expected sum you get if you roll a dice til you get the same number consecutively:

Expected number of rolls to get the same number consecutively: You do the first roll. Then E\[N\] \= ⅙(1) \+ ⅚(1 \+ E\[N\]) \=\> Gives E\[N\] \= 6, so total 6 \+ 1 \= 7 rolls. This makes the answer 3.5 \* 7 \= 24.5

Need a lot of speed and very fast estimation of numbers

**14\. NK Securities**

20 MCQs, 2 coding questions, \- 1 on map\<string, int\> message timing type, 2nd on tree shortening in some maximum number of iterations.  
MCQs were on random topics \- like finance (bonds), loans, CS concepts like OOPS and scheduling in OS, etc.

**15\. Flow Traders**

Just 80 in 8 and sequences test (26 in 25 mins) \- straight from trading interview types.

**16\. D.E Shaw & Co.**

Time limit for 3 individual coding problems. Very tough, like atleast 1600+ rating.

**17\. Graviton**

There are 4 questions, 1hr:  
1\. Given 200 barrels, and 5 slaves to use, 1 of the barrels is poisonous. Once a slave takes poison, he takes 24 hrs to die. How can you find the poisonous barrel in 48 hrs?

2\. a. Given a grid (n\*n), how many ways to go from (0,0) to (n,n) without crossing the diagonal (without touching any point with x \< y). \- Catalan Numbers \- check proof\!\!\!

b. Given an n\*m grid now (n \< m), find the number of ways to reach (n,n) from (0,0) without crossing the line from (0,0) to (x,x)

3\. a. You have a random number generator from \[0,1\]. You continuously take their sum. What is the probability that you n numbers sum \<= 1

b. What is the expected number of numbers needed to get sum \> \= 1

4\. Gambler’s ruin, A has $1, B has $2, A winning probab is ⅔, whoever wins gets a dollar, player loses if they go bankrupt, probability of A winning?

**18\. AlphaGrep**

2 hrs 15 mins \- 4 questions

O(N^2) or O(N^3) is easy, but they need O(N)

1. Given arr, count for each element how many other elements are a divisor or multiple, 1 \<= n,arr\[i\] \<= 10^5  
2. Given vector of strings, find how many pairs ((i,j), (j,i) are same) exist s.t their concatenation can be rearranged to form a palindrome. 1\<=n\<=10^5, 1\<=length(array\[i\]) \<= 3\*10^5, 1 \<= sum of lengths of strings \<= 3\*10^5  
3. Implement a function htat determines the minimum number of operations needed to transform binary string s to binary string t. 1\<=n\<=3\*10^5. In one operation, you can swap s\[i\],s\[j\] if s\[i\] \= 0 and s\[i+1\] \= …. \= s\[j\] \= 1 OR s\[i\] \= ….=s\[j-1\] \= 1 and s\[j\] \= 0  
4. Using the following rules, find the minimum cost needed to reach any integer oint on the number line. Rules: Start at x=0. For each available distance in distance\[i\], the cost to move to any point x\!= distance\[i\] is cost\[i\]. After paying the cost to use distance\[i\], you can moveto distance\[i\] an infinite number of times without any additional cost.

**18\. DaVinci GD**

**7-8 ppl in one zoom meeting room \- Question: You have 4 dice A,B,C,D. A has 4 faces with numbers 1,2,3,4, B has 6, C has 8, D has 10\. They ask a probability question which is like the fair price (in percentage), after which they randomly ask someone to make a market on that fair price and others have to continuously buy/sell. Saying buy or sell immediately, as soon as you hear a quote is paramount. If you don’t then that means you’re slow or didn’t get the answer yet, which is a big red flag. IT seemed to be the only differentiator to get shortlisted. Get the method to get the probability quickly, and in another 10 seconds convert it to decimal as fast as you can.**

**We didn’t have to remember our trades and PnL, but that’s an obvious next step**

**Note: 5% wide market just means ask-bid \= spread \= 5%. Example: 14%, 19%**

**Questions:**

1. **Probab that all 4 get different numbers (4\*5\*6\*7/4\*6\*8\*10)**  
2.  **Probability that all show same number (4/4\*6\*8\*10)**  
3. **Probab that exactly one is 7 (⅛ \* 9/10 \+ ⅞ \* 1/10)**  
4. **We get a 3, probab that we get it from the 4 face die (simple Bayes theorem)**  
5. **Ratio of probab to get 3 unique to 2 unique (very tough to get exact, asked to estimate in 5 seconds \- guessed 2 to 2.2, answer is around 5\)**

**19\. Optiver GD**

**Simple commodity trading setup, with unidirectional trade between gold, silver, platinum, copper, oil. You start with some amount of gold and need to maximize the amount of gold you can get after doing a certain number of trades, etc. 4-5 rounds each 5-6 mins long. 4 people in each group, need to discuss together and tell the optimal solution. Essentially need to find cycles that start and end at gold. Can only trade integer parts of any commodity. Not sure on what basis they judged people and selected.**

**20\. IMC GD**

**Had 2 parts, total around 1:30 hr. First part was about analysing the order book for some market of fruits and the trade volumes and valuations made by some company (FTX). You need to figure out FTXs trading strategy and what you can improve in that. You were allowed to request for data sorted according to a particular column. Strategy was that it trades a fixed volume if credit (theoretical fair price \- actual price) is above 0.2 else trade 0 volume. Mostly just check days when it makes losses to know how to improve the trading strategy. Possible improvements were to trade more volume when the credit is higher upto some limit and again drop it down as credit increases further. Also if FTX’s volume is the majority of the market share then decrease the volume \- more market share of volume was indicating more losses. Also when the total volume is very high, you can trade higher volume as it means there is strong impression in the market, and it would be a safer bet.**

**Second part was market making game on a guesstimate \- the cheapest price of business class ticket from Chennai to Sydney with a maximum of 2 stops in the next 24 hrs.**

**First asked for a fair and and 20% wide market (width \= 20% of fair price) and also 90,95 and 99% confidence intervals (not mathematically, just your best guess upto that confidence level).**  
**Then market making game started with all the 9 people in the GD group \- need to give bid-ask quotes or only one sided quotes and continuously trade. Daily position limit is \+/- 10, final position limit is \+/- 3\. Maxkimum of 10 trades. At last, need to report the PnL and final positions.**

**21\. Goldman Sachs \- 3 sections 1 hr**

First section 2 coding problems:  
Given a string, find the minimum length of substring that can be removed so that the remaining string has all distinct characters.  
Given an array of numbers denoting the location of supermarkets, you want to place k warehouses such that the sum of distances for all supermarkets to the nearest warehouse is minimum.  
Next section on 4 problems on covariance, geometry. Next section on general math and probab.

1. **Quadeye Interview** \- 3 rounds, 20 mins each

1st round:

You have 12 coins, 3 of p(H) \= ½, 3 of ⅓, 3 of ⅙, 3 of 1/9. You toss all of them and randomly remove one coin. Probability of getting odd heads.

You start from (0,0) in a grid to (n,n). Given you have to make even number of turns \- what is the total number of paths.

(1 turn is H to V, V to H)

Is 1003 prime (17\*59)

87\*93

There are n students in a circle, each with some number of chocolates \- If anyone has odd number of chocolates then the teacher gives them one. Each person gives half of their chocolates to the person to their left. Prove that after certain number of rounds all of them have equal number of chocolates.

2nd Round:

Given a random integer generator between \[0,9\]. You get three numbers from this machine, what is the probability that the sum of three is divisible by 5 (shrink the sample space to mod 0,1,2,3,4)

Given array of 0s and 1s find number of subarrays with equal number of 1s and 0s.  
Can you do without using map (using array of size 2n as bounds of prefix sum is \-n to n)

3rd Round:

Given a matrix m\*n to be filled with 0s and 1s, what is the number of ways you can fill the matrix such that every row and every col has even parity.  
(just fill m-1, n-1 of the array and prove that for the remaining row and col and corner element it all fits)

Given array a1, a2, … an, Player 1 and 2 can only pick elements from the ends, till the array has no more elements. What strategy to maximise the score?

(They just expected recursion \+ dp solution and it’s time complexity, and not a real strategy)\\

2. **Graviton Interview** \- 2hrs

Tom says “double” every time the same number appears twice in a row. Return the expected number of times he says double. He reads out the number one-by-one.

Given snails travelling along 4 lines, prove that if they intersect 5 times, they will for the 6th time.

Given a circle of diameter 5, prove that you can’t take 10 points on the circle which are all atleast 2 units apart. (Pigeon-hole)

Given 2 \+ve integers x, y s.t y \< x \<= 100 and x/y is an integer and x+1/y+1 is an integer.Find the number of ordered pairs (x,y)

3. **Ebullient Interview** \- 2 rounds 40 mins 

Round 1:

You have n coins with you at the beginning of a round \- n% chance of getting one extra coin during that round. What is the expected number of coins you’ll have at the end of 100 rounds? You start with one coin.

You take 3 points randomly on the circle, what is the expected length of the arc that contains the point (1,0)

One solution using CDF to find PDF. Other solution is to break the circle at (1,0). Now it’s just a line from 0 to 1 with 3 points randomly chosen. Now can also answer for 101 points.

There are n people wanting to move from A to B (n units away). Walking speed \= v1, Bus speed \= v2 (\> v1). Bus has a maximum capacity of k. Each passenger can get onto the bus at most once. Bus can go back and forth and pick and drop. Get all from A to B as soon as possible, and find this time (and total distance travelled).

Round 2:

Resume grilling round. Introduce yourself, then why quant, pick a project you like, went deep into that. Asked for the meanings and checked understanding very in-depth about any terminology used.Why do you think probability and expected value is asked for quant interviews? What can be improved in your project? How can you tell if the outputs of it are good? 
