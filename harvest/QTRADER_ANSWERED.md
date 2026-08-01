# Quant trader questions — with answers

185 questions across 29 firms. Every question has an answer underneath it.

## How the answers were checked

- **144 answers are backed by a program** that independently recomputes the result — exact enumeration where the state space allows it, otherwise Monte Carlo with at least two million trials. Every one of those programs was re-executed from scratch and reproduced its recorded result, so the check is not merely claimed.
- **45 are marked *guidance*** rather than solved. These are behavioural, market-making, estimation or open-modelling questions with no single correct value; the answer describes what the interviewer is testing and the shape of a strong reply.
- **6 answers contradict the answer the original candidate gave.** Those are called out inline — candidate recollections are sometimes wrong, and silently agreeing with one would propagate the error.

Where a question was a terse recollection missing a parameter, the assumption used is stated with the answer rather than hidden inside it.

---

## Susquehanna International Group  (53)

### 1. `SIG-055` · `A` · new_grad · online_assessment · 2026

A frog is traveling from point A(0,0) to point B(5,6) but each step can only be 1 unit up or 1 unit to the right. Additionally, the frog refuses to move three steps in the same direction consecutively. Compute the number of ways the frog can move from A to B.

**Answer:** 113

*Working:* Same method as the (7,4) version: words with 5 R's and 6 U's, all runs of length 1 or 2. Splits of 5 into j parts of size 1-2: C(j,5-j) gives j=3 -> 3, j=4 -> 4, j=5 -> 1. Splits of 6 into k parts: C(k,6-k) gives k=3 -> 1, k=4 -> 6, k=5 -> 5, k=6 -> 1. Combine over |j-k| <= 1, with a factor 2 when j = k: (3,3): 3*1*2=6; (3,4): 3*6=18; (4,3): 4*1=4; (4,4): 4*6*2=48; (4,5): 4*5=20; (5,4): 1*6=6; (5,5): 1*5*2=10; (5,6): 1*1=1. Total 113.

*Assumption:* 'Refuses to move three steps in the same direction consecutively' means no run of length >= 3.

<sub>numerically verified — `CHECK 113 vs 113`</sub>

<sub>Source: other · 2025-09-04 · [link](https://web.archive.org/web/20250912084409/https://www.1point3acres.com/bbs/thread-1144112-1-1.html)</sub>

---

### 2. `SIG-013` · `A` · new_grad · phone_technical · 2022 Programme (applied 13 Sep 2021)

The last question ("3 biased coins") was a standard Bayes' problem; was something like given a fair coin, a coin with only heads and coin with only tails (or something like that with different probabilities), if you pick a random coin and it's head, what is the probability it was from coin 2?

**Answer:** 6/13 (about 0.4615) for the coin with P(heads) = 1/2. Full posterior over the three coins: 6/13, 4/13, 3/13.

*Working:* With a uniform prior over the three coins, the posterior after one head is proportional to each coin's head probability: P(coin i | H) = p_i / (p_1 + p_2 + p_3). Reconstructing the coins as p = 1/2, 1/3, 1/4 (the sum is 13/12), the posteriors are (1/2)/(13/12) = 6/13, (1/3)/(13/12) = 4/13, (1/4)/(13/12) = 3/13. The interviewer's intuition note - the coin with the highest head rate is the most likely source of an observed head - is exactly the statement that the posterior is proportional to p_i.

*Assumption:* The recalled text (fair coin, all-heads coin, all-tails coin) is not consistent with the 6/13 the scorecard records; that setup gives 2/3 for the all-heads coin and 1/3 for the fair one. I reconstructed the coins as 1/2, 1/3, 1/4, which is the natural triple that produces 6/13, and it matches the interviewer's remark about needing 'more tosses to get a head' (mean waiting times 2, 3 and 4 tosses).

<sub>numerically verified — `CHECK posterior(p=1/2 coin)=6/13 (0.46154) mc=0.46056 vs 6/13=0.46154 | literal 2-headed-coin posterior=2/3 vs 2/3` · confidence: **medium**</sub>

<sub>Source: github_repo · 2022-04-08 · [link](https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2021-22/SIG/Quantitative%20Trader%20-%202022%20Programme.md)</sub>

---

### 3. `SIG-036` · `B` · unknown · online_assessment · 2026

Question 2: I need to seat 5 toddlers (Anna, Brian, Charlie, Dixie, Eva) at a round table with these rules: i) Anna won’t sit next to Brian or Eva. ii) Brian won’t sit next to Charlie. iii) Dixie won’t sit next to Eva or Charlie. If Dixie is sitting to the left of Anna, who is sitting to the left of Brian?

**Answer:** Eva

*Working:* At a round table of 5 everyone has exactly 2 neighbours, which pins the arrangement down. Anna cannot sit by Brian or Eva, so Anna's neighbours are Charlie and Dixie. Dixie cannot sit by Eva or Charlie, so Dixie's neighbours are Anna and Brian. Brian cannot sit by Charlie (rule ii) or Anna (rule i), so Brian's neighbours are Dixie and Eva. The remaining edge closes the cycle Charlie-Eva. So the unique seating is the cycle Anna-Charlie-Eva-Brian-Dixie-Anna. 'Dixie is to the left of Anna' fixes which way round we read it: going leftwards from Anna gives Anna, Dixie, Brian, Eva, Charlie. Hence the person to Brian's left is Eva.

*Assumption:* 'To the left of' is a single consistent rotational direction for everyone (all toddlers facing the table), so the clue about Dixie fixes the direction; the answer does not depend on which physical direction 'left' is, because the seating cycle is unique up to reflection.

<sub>numerically verified — `CHECK ['E'] cycles= [('A', 'D', 'B', 'E', 'C')] vs ['E']`</sub>

<sub>Source: 1point3acres · unknown · [link](https://www.1point3acres.com/bbs/thread-1144112-1-1.html)</sub>

---

### 4. `SIG-001` · `B` · internship · online_assessment · Nov 2025

A gardener is eagerly waiting for his two favorite flowers to bloom. The purple flower will blossom at some point uniformly at random in the next 20 days and be in bloom for exactly 4 days. Independent of the purple flower, the red flower will blossom at some point uniformly at random in the next 20 days and be in bloom for exactly 8 days. Compute the probability that both flowers will simultaneously be in bloom at some point in time. Express your answer as a fraction in simplest form. Enter the numerator in the first blank and the denominator in the second blank.

**Answer:** 1/2 (numerator 1, denominator 2)

*Working:* Let X, Y ~ U[0,20] be the two blossom times. Purple is in bloom on [X, X+4], red on [Y, Y+8]; the intervals overlap iff X < Y + 8 and Y < X + 4, i.e. -8 < X - Y < 4. Geometrically that is a diagonal strip in the 20x20 square: its complement is two right triangles with legs 20-8 = 12 and 20-4 = 16, of total area (144 + 256)/2 = 200, so the overlap area is 400 - 200 = 200 and the probability is 200/400 = 1/2. The suspiciously clean answer is a good sign the intended reading is right, since 4 + 8 = 12 and (20-4)^2 + (20-8)^2 = 400 = 2 * 20^2 is exactly the knife-edge case.

*Assumption:* Blossom START times are iid uniform on [0,20] days and a bloom may run past day 20 (the natural reading of 'will blossom at some point uniformly at random in the next 20 days'). Under the alternative discrete reading - blossoming on one of days 1..20 - the answer would instead be 186/400 = 93/200; under the reading that each bloom must finish within the 20 days it changes again. The clean 1/2 strongly indicates the continuous reading is intended.

<sub>numerically verified — `CHECK ('1/2', 0.49993) vs ('1/2', 0.5)`</sub>

<sub>Source: glassdoor · 2026-07-06 · [link](https://www.glassdoor.com/Interview/Susquehanna-International-Group-Interview-E24446-RVW104664176.htm)</sub>

---

### 5. `SIG-009` · `B` · internship · online_assessment · Aug 2025

A deck contains ten cards: two 10s, two Js, two Qs, two Ks, two As. You're dealt five cards without replacement from the stack. Compute the expected number of pairs.

**Answer:** 10/9 (about 1.111 pairs)

*Working:* Linearity of expectation over the five ranks. Rank r contributes a pair iff both of its cards are among the five dealt: P = C(8,3)/C(10,5) = 56/252 = 2/9, equivalently (5/10)(4/9) = 2/9. Expected number of pairs = 5 * 2/9 = 10/9.

*Assumption:* 'Pair' means a rank appearing twice in the hand; since each rank has only two cards, no rank can appear more than twice, so there is no three-of-a-kind ambiguity.

<sub>numerically verified — `CHECK enum=10/9 vs 10/9=10/9 (252 hands)`</sub>

<sub>Source: glassdoor · 2025-08-23 · [link](https://www.glassdoor.com/Interview/Susquehanna-International-Group-Interview-E24446-RVW99548933.htm)</sub>

---

### 6. `SIG-002` · `B` · unknown · online_assessment · Mar 2024

Mickey and Minnie plan to meet at a cafe, but will each independently show up at a uniformly random time between 9:00 to 10:00. Mickey will only wait 10 minutes for Minnie before leaving, but Minnie will wait 30 minutes for Mickey before leaving. What is the probability they end up meeting each other?

**Answer:** 19/36 (about 0.5278)

*Working:* Let X and Y be Mickey's and Minnie's arrival times, independent and uniform on [0,60] minutes after 9:00. If Mickey arrives first he waits 10 minutes, so they meet iff Y - X <= 10; if Minnie arrives first she waits 30 minutes, so they meet iff X - Y <= 30. The meeting region is therefore -30 <= Y - X <= 10, and its complement in the 60x60 square is two right triangles with legs 50 and 30. P = 1 - (50^2 + 30^2)/(2*60^2) = 1 - 3400/7200 = 19/36 = 0.5278.

*Assumption:* Arrival times independent and uniform over the hour. The waiting period is allowed to run past 10:00, which is irrelevant here because the meeting condition involves only the two arrival times.

<sub>numerically verified — `CHECK mc=0.52794 exact=19/36 vs 19/36=0.52778`</sub>

<sub>Source: glassdoor · 2024-03-29 · [link](https://www.glassdoor.com/Interview/Susquehanna-International-Group-Interview-E24446-RVW85828435.htm)</sub>

---

### 7. `SIG-043` · `B` · unknown · online_assessment · 2026

Two friends canoe upstream for 3 hours, only to realize that their campsite is downstream. They turn around and paddle downstream for 4 hours. The next morning, they pack up and get back on the river to canoe to their original starting point 28 miles upstream and arrive at 2 pm. Assume the river always flows at a constant rate of 2 miles per hour, and the two friends always paddle at a constant rate. What time did they leave for their return trip?

**Answer:** 11:40 am

*Working:* Let p be their paddling speed in still water; the current is 2 mph. Day 1: 3 hours upstream covers 3(p-2), then 4 hours downstream covers 4(p+2), leaving them 4(p+2) - 3(p-2) = p + 14 miles BELOW the start. The campsite is 28 miles below the start, so p + 14 = 28 and p = 14 mph. The return trip is 28 miles upstream at 14 - 2 = 12 mph, taking 28/12 = 7/3 hours = 2 h 20 min. Arriving at 2:00 pm, they set off at 11:40 am.

*Assumption:* Paddling speed relative to the water is the same constant on both days; current is 2 mph throughout; no stops.

<sub>numerically verified — `CHECK downstream=28mi p=14 travel=7/3h depart=11:40 vs 28mi p=14 travel=7/3h depart=11:40`</sub>

<sub>Source: glassdoor · 2026-03-30 · [link](https://www.glassdoor.com/Interview/Susquehanna-International-Group-Interview-E24446-RVW103369878.htm)</sub>

---

### 8. `SIG-025` · `B` · new_grad · online_assessment · Feb 2024

A can finish a job in 100 min, B can finish the same job in 120 min. A and B work together on this job, but after 40 min C comes to help them and they finish the job in additional 10 min. How long would it take to C to finish the job by himself?

**Answer:** 120 minutes

*Working:* Rates: A = 1/100 and B = 1/120 of the job per minute, summing to 11/600. In the first 40 minutes they complete 40 * 11/600 = 11/15, leaving 4/15. In the final 10 minutes all three work: 10*(11/600 + 1/c) = 4/15, so 10/c = 4/15 - 11/60 = 1/12, giving c = 120 minutes.

*Assumption:* Constant work rates that add, and C works only during the final 10 minutes.

<sub>numerically verified — `CHECK C alone = 120 min, work completed = 1 vs 120, 1 (A+B did 11/15 in 40 min)`</sub>

<sub>Source: glassdoor · 2024-03-17 · [link](https://www.glassdoor.com/Interview/Susquehanna-International-Group-Interview-RVW85406907.htm)</sub>

---

### 9. `SIG-033` · `B` · new_grad · phone_technical · Mar 2015

I have a painting, if it's an original it's worth 500k if it isn't it's worth 10k. The probability it's an original is 0.2. I have an option to pay 100k for the picture after inspection what is the value of the option?

**Answer:** $80,000

*Working:* The option is exercised after inspection, so you only pay when it pays to pay. If the painting is original (p = 0.2) you pay 100k for something worth 500k: +400k. If it is a fake (p = 0.8) it is worth 10k < 100k, so you walk away: 0. Value = 0.2 * 400k + 0.8 * 0 = 80k. Useful contrast for the interviewer: an obligation to buy at 100k would be worth only 0.2(400k) + 0.8(-90k) = 8k, so the 72k difference is exactly the value of being allowed to decline.

*Assumption:* Risk-neutral valuation, no discounting/time value, inspection is perfectly informative and free, and 'worth' means you can realise 500k / 10k on resale.

<sub>numerically verified — `CHECK option=80000 unconditional_buy=8000 vs option=80000 (unconditional=8000)`</sub>

<sub>Source: glassdoor · 2015-03-24 · [link](https://www.glassdoor.com/Interview/Susquehanna-International-Group-Interview-E24446-RVW6185890.htm)</sub>

---

### 10. `SIG-016` · `B` · new_grad · phone_technical · Nov 2014

You start out with 1 dollar and your friend starts out with 2 dollars. You bet 1 dollar until one of you runs out of money. You have a 2/3 chance of winning each bet. What is your chance of winning?

**Answer:** 4/7 (about 0.5714)

*Working:* Gambler's ruin on {0,1,2,3} starting at 1, up with p = 2/3, down with q = 1/3, so r = q/p = 1/2. P(reach 3 before 0 from i) = (1 - r^i)/(1 - r^N) = (1 - 1/2)/(1 - 1/8) = (1/2)/(7/8) = 4/7. Directly: f(1) = p*f(2), f(2) = p + q*f(1), so f(1) = p^2/(1 - pq) = (4/9)/(7/9) = 4/7.

*Assumption:* Fair $1 stakes, independent bets, and play continues until one player is broke, which happens with probability 1 because the state space is finite.

<sub>numerically verified — `CHECK exact=4/7 (0.57143) mc=0.57128 vs 4/7=0.57143`</sub>

<sub>Source: glassdoor · 2014-12-09 · [link](https://www.glassdoor.com/Interview/Susquehanna-International-Group-Interview-E24446-RVW5503556.htm)</sub>

---

### 11. `SIG-006` · `B` · new_grad · phone_technical · Feb 2016

A boat fires torpedoes at another boat, the probability that the torpedo hits is 1/3, if the torpedo hits the boat, the boat is destroyed. 2 torpedoes are fired, what is the probability of the ship being destroyed?

**Answer:** 5/9 (about 0.5556)

*Working:* The ship survives only if both torpedoes miss: (2/3)^2 = 4/9. So P(destroyed) = 1 - 4/9 = 5/9. Equivalently 1/3 + (2/3)(1/3) = 5/9.

*Assumption:* The two torpedoes hit independently with probability 1/3 each and a single hit destroys the ship. If the second torpedo is only fired when the first misses, the answer is unchanged, since the ship is already destroyed on the other branch.

<sub>numerically verified — `CHECK enum=5/9 vs 5/9=5/9`</sub>

<sub>Source: glassdoor · 2016-02-29 · [link](https://www.glassdoor.com/Interview/Susquehanna-International-Group-Interview-E24446-RVW9742732.htm)</sub>

---

### 12. `SIG-056` · `B` · unknown · phone_technical · 2024

Given 5 fair dices. What is the probability to get results containing 3 same values.

**Answer:** 23/108 (approx 21.30%) for 'some value appears at least 3 times', which is how I read 'containing 3 same values'. If 'exactly three' is meant: 125/648 (approx 19.29%) for some value appearing exactly three times, or 25/162 (approx 15.43%) for poker's three-of-a-kind (exactly three alike and the other two distinct, excluding a full house).

*Working:* Out of 6^5 = 7776 equally likely rolls: three of a kind with two distinct kickers = 6 * C(5,3) * 5 * 4 = 1200; full house = 6 * C(5,3) * 5 = 300; four of a kind = 6 * C(5,4) * 5 = 150; five of a kind = 6. At least three alike = 1200 + 300 + 150 + 6 = 1656, and 1656/7776 = 23/108. Exactly three of some value = 1200 + 300 = 1500 -> 125/648. Strict poker trips = 1200 -> 25/162.

*Assumption:* Five independent fair d6. Read 'containing 3 same values' as 'at least three dice show the same value'; the two stricter readings are quoted as well.

<sub>numerically verified — `CHECK 23/108 125/648 25/162 vs 23/108 125/648 25/162` · confidence: **medium**</sub>

<sub>Source: glassdoor · 2024-01-31 · [link](https://www.glassdoor.com/Interview/Susquehanna-International-Group-Interview-E24446-RVW83922916.htm)</sub>

---

### 13. `SIG-049` · `B` · unknown · phone_technical · Jan 2025

what’s the probability of getting HTH before HHT of flipping a fair coin?

**Answer:** 1/3 (so HHT beats HTH with probability 2/3)

*Working:* Track the useful suffix. States: S (nothing), H, HH, HT. From HH you can never reach HTH first: any further H keeps you at HH and the first T completes HHT, so P(HTH | HH) = 0. From HT, an H wins immediately and a T sends you back to S: p(HT) = 1/2 + (1/2)p(S). Also p(H) = (1/2)(0) + (1/2)p(HT) and p(S) = (1/2)p(H) + (1/2)p(S) => p(S) = p(H). Substituting, p(S) = (1/2)p(HT) = 1/4 + (1/4)p(S), so p(S) = 1/3. The intuition: once you see HH - which happens before any HT in the race - HHT is already locked in.

*Assumption:* Fair coin, flips independent, race continues until one of the two patterns appears.

<sub>numerically verified — `CHECK 0.3332 (exact 1/3 ) vs 1/3`</sub>

<sub>Source: glassdoor · 2025-01-13 · [link](https://www.glassdoor.com/Interview/Susquehanna-International-Group-Interview-E24446-RVW94285408.htm)</sub>

---

### 14. `SIG-067` · `B` · internship · phone_technical · 2023

There's a painting that has a 80% chance of being fake. If the painting is real it's worth 500k, if it's fake it's worth 10k. The seller asks for 120k. Will you buy it?

**Answer:** No - do not buy at 120k. Expected value = 0.2*500k + 0.8*10k = 108k, so you are paying 12k over fair value. Your maximum risk-neutral bid is 108k.

*Working:* EV = 0.8*10,000 + 0.2*500,000 = 8,000 + 100,000 = $108,000 < $120,000, an expected loss of $12,000. Worth adding: the payoff is extremely lumpy (80% chance of losing ~110k), so a risk-averse buyer with limited capital should demand a discount to 108k, not just pay up to it. The answer flips only if you can change the odds or the payoff - pay for authentication before committing, negotiate a contingent price, or resell to a buyer whose valuation of a genuine work exceeds 500k.

*Assumption:* Risk-neutral valuation; the stated 80% is your true posterior and the values are what you could actually realise on resale.

<sub>numerically verified — `CHECK ev_value=108000 edge_at_120k=-12000 vs claimed=108000 and -12000`</sub>

<sub>Source: glassdoor · 2023-12-03 · [link](https://www.glassdoor.com/Interview/Susquehanna-International-Group-Interview-E24446-RVW82280962.htm)</sub>

---

### 15. `SIG-066` · `B` · internship · phone_technical · unknown

There is a game where you flip a coin 4 times and if you guess right each time, you win $10. It costs $1 to play. Should you play?

**Answer:** No - do not play. EV = -3/8 = -$0.375 per play. P(all four guesses correct) = (1/2)^4 = 1/16, so EV = 10*(1/16) - 1 = 5/8 - 1 = -3/8. Break-even prize is $16.

*Working:* Guesses are independent of a fair coin, so P(4 for 4) = 1/16 regardless of what you guess. Expected gross return 10/16 = $0.625 against a $1 cost gives -$0.375, a -37.5% edge. If instead '$10' means net profit on top of the stake being returned, EV = 10/16 - 15/16 = -5/16 = -$0.3125; still negative, still don't play.

*Assumption:* Fair coin; your guesses cannot be revised after seeing outcomes. Ambiguity: '$10' read as gross payout (primary, EV = -3/8) vs net profit (EV = -5/16). Both readings say no.

<sub>numerically verified — `CHECK ev=-3/8 (-0.3750) alt_reading_ev=-5/16 vs claimed=-3/8 (-0.375)`</sub>

<sub>Source: reddit_thread · 2018-10-29 · [link](https://www.reddit.com/r/FinancialCareers/comments/9sd7h0/_/e8o5bwh/)</sub>

---

### 16. `SIG-030` · `B` · unknown · phone_technical · unknown

If you had a deck of 52 playing cards, no jokers. What is the probability of pulling 3 of a kind?

**Answer:** 1/425 (approx 0.235%), i.e. 424:1 against, reading the question as: draw 3 cards from a 52-card deck and all three share a rank.

*Working:* Count directly: C(13,1) ranks x C(4,3) ways to pick 3 of that rank / C(52,3) hands = 13*4/22100 = 52/22100 = 1/425. Sequentially it is the same thing: the first card can be anything (52/52), the second must match its rank (3/51), the third must match as well (2/50), and (3/51)*(2/50) = 6/2550 = 1/425. If instead the question meant a 5-card poker hand containing three of a kind (exactly three, other two unpaired), the answer is 54912/2598960 = 88/4165 (approx 2.113%).

*Assumption:* Assumed the natural reading: three cards drawn at random from a full 52-card deck, 'three of a kind' = all three of the same rank.

> ⚠️ **The candidate's reported answer is wrong.** mixed. The poster's final figure 1/425 is correct, but his stated route (1/51 x 1/50) is not - that gives 1/2550. The correct route is (3/51)*(2/50) = 1/425, as the harvest note already flags. riskarb's '416:1 against' is wrong: 1/425 corresponds to 424:1 against, and 416:1 would mean p = 1/417.

<sub>numerically verified — `CHECK 3-card=1/425 5-card-trips=88/4165(54912/2598960) vs 3-card=1/425, 5-card-trips=88/4165`</sub>

<sub>Source: elitetrader · 2006-04-28 · [link](https://www.elitetrader.com/et/threads/phone-interview-with-sig.67976/)</sub>

---

### 17. `SIG-039` · `B` · new_grad · unknown · Sep 2014

There are 2 boys and unknown number of girls in a nursery. A new baby is just born inside the room. We pick randomly a baby from the room, it turns out that the baby is a boy. What is the probability that the new baby just born is a boy?

**Answer:** 3/5

*Working:* Let g be the unknown number of girls and let B = 1 if the newborn is a boy. After the birth the room holds 2 + B boys and g + (1-B) girls, i.e. 3 + g babies in total either way. P(draw a boy | newborn is a boy) = 3/(3+g); P(draw a boy | newborn is a girl) = 2/(3+g). Bayes: P(newborn boy | drew a boy) = (1/2)(3/(3+g)) / [(1/2)(3/(3+g)) + (1/2)(2/(3+g))] = 3/(3+2) = 3/5. The 3+g cancels, which is why the number of girls can be left unknown - that is the whole point of the question.

*Assumption:* Newborn is a boy or girl with probability 1/2 each, independent of the room; the baby drawn is uniform over everyone in the room including the newborn.

<sub>numerically verified — `CHECK 0.5994 (exact 3/5 ) vs 3/5`</sub>

<sub>Source: glassdoor · 2014-10-12 · [link](https://www.glassdoor.com/Interview/Susquehanna-International-Group-Interview-E24446-RVW5151839.htm)</sub>

---

### 18. `SIG-012` · `B` · new_grad · unknown · Dec 2013

a group of people wants to determine their average salary on the condition that no individual would be able to find out anyone else's salary. How can they accomplish this?

**Answer:** Two standard protocols. (1) Masked accumulator: the first person adds a large secret random number R to their salary and passes the total to the next, each person adds their own salary, and the last passes back to the first, who subtracts R and divides by n. (2) Additive secret sharing: each person splits their salary into n random numbers that sum to it, sends one share to each participant, everyone announces the sum of the shares they received, and the announced values are added and divided by n.

*Working:* Both work because every number anyone sees is their own salary plus an unknown offset, and only the total is ever revealed. The details that earn the marks are the failure modes. In protocol 1, person 1 learns the grand total (as does everyone else once the average is announced), so with n = 2 each person recovers the other's salary exactly - the scheme needs n >= 3. Also, the two neighbours of person i, colluding, can difference the running totals and recover person i's salary; randomising the passing order or re-running with a different order mitigates this. Protocol 2 has no privileged first party and survives collusion better: any coalition short of n-1 participants learns nothing beyond the total. Both are honest-but-curious protocols - they assume nobody lies about their salary or their share - and both leak the total, which is unavoidable when the average is the output.

<sub>guidance, no single correct value</sub>

<sub>Source: glassdoor · 2015-06-11 · [link](https://www.glassdoor.com/Interview/Susquehanna-International-Group-Interview-E24446-RVW6877957.htm)</sub>

---

### 19. `SIG-032` · `B` · new_grad · unknown · 2025

Pick three numbers between 1 and 20. What is the probability that one number is the average of the other two?

**Answer:** 3/38 (approx 7.89%)

*Working:* One of three numbers is the average of the other two exactly when the three form a 3-term arithmetic progression. For common difference d there are 20-2d such triples in {1,...,20}, so the total is sum_{d=1}^{9}(20-2d) = 18+16+14+12+10+8+6+4+2 = 90. Probability = 90/C(20,3) = 90/1140 = 3/38. If instead the three numbers are drawn independently with replacement, the answer is 7/100: 90*6 = 540 ordered AP triples plus the 20 all-equal triples (where each number trivially is the average of the other two), over 20^3 = 8000.

*Assumption:* Assumed three distinct integers chosen uniformly at random from {1,...,20} inclusive. The with-replacement variant (7/100) is given as well since 'pick three numbers' is not explicit.

<sub>numerically verified — `CHECK 3/38 7/100 vs 3/38 7/100`</sub>

<sub>Source: glassdoor · 2025-01-30 · [link](https://www.glassdoor.com/Interview/Susquehanna-International-Group-Interview-E24446-RVW94712966.htm)</sub>

---

### 20. `SIG-022` · `B` · internship · unknown · Apr 2023

If you play a game and your opponent doubles the stakes of the game, what likelihood should you have of winning for you to accept this instead of having to resign the game.

**Answer:** p >= 1/4 (25%)

*Working:* Normalise the current stake to 1 unit. Resigning (declining) loses 1 for certain. Accepting makes the stake 2, worth 2p - 2(1-p) = 4p - 2. Accept iff 4p - 2 >= -1, i.e. p >= 1/4. This is the backgammon 'take point'.

*Assumption:* The double is take-it-or-leave-it, the game then plays to a simple win or loss at double stakes, and there is no further doubling. Two refinements worth saying out loud in the interview: after taking you normally own the cube and may redouble later, which is worth something and pushes the practical take point below 25% (roughly 20% in backgammon); conversely, if the loss can be multiplied further (gammons, backgammons) or the position can deteriorate past the point of a profitable recube, the take point rises.

<sub>numerically verified — `CHECK breakeven p in [0.250000, 0.250000], EV(accept at 1/4)=-1 vs 1/4, -1`</sub>

<sub>Source: glassdoor · 2024-11-06 · [link](https://www.glassdoor.com/Interview/Susquehanna-International-Group-Interview-E24446-RVW92591239.htm)</sub>

---

### 21. `SIG-031` · `B` · internship · unknown · 2022

Q: How many ways can you sit in a circle of 5 people that you end up sitting with your best friend?

**Answer:** 12 arrangements out of 24 (counting seatings up to rotation); equivalently 60 out of 120 if the five chairs are labelled. Either way the probability is 1/2.

*Working:* Circular arrangements of 5 people = (5-1)! = 24. Treat you and your best friend as one block: (4-1)! = 6 circular arrangements of the 4 units, times 2 for the order inside the block = 12. Sanity check without counting: in a 5-cycle you have exactly 2 neighbours among the other 4 people, so P = 2/4 = 1/2.

*Assumption:* 'Sitting with' = sitting immediately next to. Counted seatings up to rotation, which is the usual convention for round tables; the labelled-chair count 60/120 is given too since the question does not say.

<sub>numerically verified — `CHECK 12/24 rotationally distinct, 60/120 labelled, p=1/2 vs 12/24, 60/120, p=1/2`</sub>

<sub>Source: glassdoor · 2022-10-14 · [link](https://www.glassdoor.com/Interview/Susquehanna-International-Group-Interview-E24446-RVW70139863.htm)</sub>

---

### 22. `SIG-007` · `B` · internship · unknown · Feb 2023

Compute conditional probabilities, and explain one's thought process.

**Answer:** No single numeric answer - this is the interviewer's note that the round was a conditional-probability question graded on the explanation. Method: write the sample space, state the exact conditioning event, apply P(A|B) = P(A and B)/P(B), or use posterior odds = prior odds x likelihood ratio, then sanity check an extreme case.

*Working:* What is actually being tested is whether you notice that the answer depends on how the information reached you, and whether you can narrate that. The canonical demonstration: for a two-child family, 'at least one is a girl' gives P(both girls) = 1/3, while 'the elder is a girl' gives 1/2 - the same-sounding fact, a different conditioning event (both verified below). The same trap drives Monty Hall and the disease-test question. Out loud, the odds form is faster and less error-prone than the ratio form: state prior odds, multiply by the likelihood ratio for the evidence, convert back. Finish by checking a limit (prevalence to zero, or a perfectly accurate test) to show the answer behaves sensibly.

*Assumption:* The record contains no specific problem, so I have answered the method question and verified the illustrative example I quote.

<sub>numerically verified — `CHECK P(GG|>=1 G)=1/3, P(GG|elder G)=1/2 vs 1/3, 1/2`</sub>

<sub>Source: glassdoor · 2023-08-28 · [link](https://www.glassdoor.com/Interview/Susquehanna-International-Group-Interview-E24446-RVW79550591.htm)</sub>

---

### 23. `SIG-050` · `B` · internship · unknown · Apr 2023

There are two fair dices, you should dice another if you didn’t get 6 for that dice. Calculate the Expected number of times you get dice 1=6.

**Answer:** 6, reading it as 'how many rolls of die 1 until it shows a 6'. (The number of rolls is geometric with p = 1/6, mean 1/p = 6.) If the intended question is instead 'how many rounds until BOTH dice have shown a 6, re-rolling only the dice that are not yet 6', the answer is 96/11 = 8.7272... ; and if it is 'how many times does die 1 show a 6 before the process stops', the answer is trivially 1.

*Working:* Rolls until a 6 is geometric: E = sum_{k>=1} k(5/6)^{k-1}(1/6) = 6. For the two-dice variant, each die independently needs a Geom(1/6) number of rolls N1, N2 and the process ends at max(N1,N2); E[max] = E[N1] + E[N2] - E[min] = 6 + 6 - 1/(1-(5/6)^2) = 12 - 36/11 = 96/11.

*Assumption:* The recollection is garbled ('you should dice another if you didn't get 6 for that dice'). I read it as: each die is re-rolled until it shows a 6, and the question asks for the expected number of rolls of die 1. The two plausible alternative readings are answered above.

<sub>numerically verified — `CHECK E[rolls of die1]=6.0017 E[rounds until both]=8.7283 vs 6 and 8.7273 (=96/11)` · confidence: **low**</sub>

<sub>Source: glassdoor · 2023-05-27 · [link](https://www.glassdoor.com/Interview/Susquehanna-International-Group-Interview-E24446-RVW76835111.htm)</sub>

---

### 24. `SIG-018` · `B` · internship · unknown · 2021

Given x identical marbles how can you figure out which is the dissimilar marble in y uses of the scale

**Answer:** Each weighing has 3 outcomes, so y weighings distinguish at most 3^y cases. If the odd marble is known to be the heavier one, y = ceil(log_3 x) weighings suffice and are necessary (x <= 3^y). If you do not know whether it is heavy or light and must also report which, the maximum is x <= (3^y - 3)/2, i.e. 12 marbles in 3 weighings and 39 in 4. Relaxing either half of that last requirement raises the maximum to (3^y - 1)/2, i.e. 13 in 3: enough if you have one marble known to be genuine to use as a makeweight, or if you only have to name the odd marble without saying whether it is heavy or light.

*Working:* Known-heavier case: split into three groups as equal as possible, weigh two of them against each other, and recurse into the heavier group or into the unweighed group if they balance; each weighing divides the candidate set by 3, so ceil(log_3 x) rounds are enough, and the 3^y outcome count shows you cannot do better. Unknown direction: there are 2x scenarios, and the tight construction for y = 3 labels the 12 marbles with 12 of the 13 antipodal pairs of nonzero vectors in {-1,0,+1}^3, one representative each, with signs chosen so every coordinate has as many +1s as -1s; weighing j puts the +1 marbles on the left pan and the -1 marbles on the right, and the resulting outcome triple names the marble (its vector) and the direction (sign). 13 is impossible with direction required: a first weighing of k against k leaves 2(13 - 2k) scenarios if it balances, needing 2(13-2k) <= 9, and 2k scenarios if it tips, needing 2k <= 9 - no integer k satisfies both.

*Assumption:* x and y are left symbolic in the question, and the direction of the anomaly is not stated, so I give all three standard variants. A balance scale (three outcomes) is assumed, not a weighing scale.

<sub>numerically verified — `CHECK known-heavy y=ceil(log3 x) for x<=40: True | 12-marble/3-weighing schemes found: 304 | 13-with-direction impossible: True vs True, >0, True`</sub>

<sub>Source: glassdoor · 2021-09-07 · [link](https://www.glassdoor.com/Interview/Susquehanna-International-Group-Interview-E24446-RVW52200794.htm)</sub>

---

### 25. `SIG-029` · `B` · internship · unknown · Nov 2018

If you get multiple offers, how would you choose?

**Answer:** No numeric answer. Give a ranked, honest decision framework - learning rate and mentorship, the desk and product, the people, the firm's edge and how it is sustained, with compensation named as a real but secondary factor.

*Working:* The interviewer is testing how you make decisions under uncertainty and whether you are straight with people, not trying to find out who else is bidding. A strong answer states two or three criteria in priority order and why they matter over a career: the speed and quality of feedback you would get in the first two years, who you would learn from, the product and whether you would understand it deeply, and whether the firm's edge is something you could contribute to. Say plainly that compensation matters and that you would not pretend otherwise, but that at the start of a career the difference between offers is dominated by what you learn. Add that you would talk to people at each firm and be transparent about your timelines rather than shopping offers against each other. Red flags: claiming money is irrelevant, using the answer to start a negotiation, or having no criteria at all.

<sub>guidance, no single correct value</sub>

<sub>Source: glassdoor · 2018-11-25 · [link](https://www.glassdoor.com/Interview/Susquehanna-International-Group-Interview-E24446-RVW23551083.htm)</sub>

---

### 26. `SIG-003` · `B` · internship · unknown · Dec 2017

You seem to be doing fairly well up to now, why do you think that is?

**Answer:** No numeric answer. Attribute the run to one or two concrete, repeatable habits, give evidence for each, name what you got lucky on and what is still weak, and note that one interview is a small sample.

*Working:* The interviewer is testing whether you can separate process from outcome and discuss your own performance without arrogance or false modesty - exactly the skill a trader needs to tell edge from variance. A strong answer names mechanisms rather than traits: 'I drill mental arithmetic and estimation, so I don't burn clock on the arithmetic and can spend it on the structure of the problem', or 'I say my assumptions out loud, so a wrong turn gets caught in the first thirty seconds instead of the last'. Then add the honest half: a question you'd answer differently now, and the observation that a handful of questions is a small sample from which you would not conclude much either way. Weak answers are 'I guess I got lucky' (no self-model), 'I'm just good at maths' (no process, and it invites a harder question), or a recital of your CV.

<sub>guidance, no single correct value</sub>

<sub>Source: glassdoor · 2017-12-16 · [link](https://www.glassdoor.com/Interview/Susquehanna-International-Group-Interview-E24446-RVW18371833.htm)</sub>

---

### 27. `SIG-063` · `B` · internship · unknown · Dec 2017

You have 8 marbles. One is heavier than the rest. You have a balance scales and you can use it only twice. Can you determine which marble is heaviest?

**Answer:** Yes. 2 weighings suffice (and 2 is the minimum). Weigh {1,2,3} vs {4,5,6}. If a side goes down, the heavy marble is in that trio: weigh two of them against each other; the heavier is it, or if they balance it is the third. If the first weighing balances, weigh the two set-aside marbles against each other.

*Working:* Each weighing yields one of 3 outcomes, so k weighings separate at most 3^k cases. Since 3^1 = 3 < 8, one weighing cannot do it; 3^2 = 9 >= 8, and the 3/3/2 split achieves it because every branch leaves at most 3 candidates, which one further weighing resolves.

*Assumption:* Exactly one ball is heavier, all others equal, balance scale gives only lighter/heavier/equal.

<sub>numerically verified — `CHECK 8/8 solved in 2 weighings; 3^1=3 < 8 so 1 is impossible vs 8/8, minimum 2`</sub>

<sub>Source: glassdoor · 2017-12-15 · [link](https://www.glassdoor.com/Interview/Susquehanna-International-Group-Interview-E24446-RVW18357302.htm)</sub>

---

### 28. `SIG-023` · `B` · unknown · unknown · Feb 2024

what is the expectation of a coin tossing game.

**Answer:** Underspecified as recorded. For a fair coin: E[tosses to the first head] = 2; E[heads in n tosses] = n/2; E[tosses to see HH] = 6 while E[tosses to see HT] = 4; and the St Petersburg game (2^k for a first head on toss k) has infinite expectation.

*Working:* Say which game you are solving before you solve it - that is the graded part. First head: geometric with p = 1/2, so E = 1/p = 2. Pattern HH: with a = E[from no trailing head] and b = E[from one trailing head], a = 1 + b/2 + a/2 and b = 1 + a/2 give a = 6; for HT the same setup gives a = 1 + b/2 + a/2 and b = 1 + b/2, so a = 4. The asymmetry - 6 against 4 for two patterns of equal probability - is the point of the question: HH can overlap itself, so a failure after one H throws away progress, whereas HT cannot. If instead the game pays $1 a head and costs $0.50 a flip, the expectation is 0 per flip and the follow-up is usually about variance or an optimal stopping rule rather than the mean.

*Assumption:* The record contains only the phrase 'the expectation of a coin tossing game', so I have answered every standard reading and verified the three numeric ones.

<sub>numerically verified — `CHECK E[first H]=2 (mc 1.999), E[HH]=6 (mc 6.011), E[HT]=4 (mc 4.004) vs 2, 6, 4` · confidence: **medium**</sub>

<sub>Source: glassdoor · 2025-01-09 · [link](https://www.glassdoor.com/Interview/Susquehanna-International-Group-Interview-E24446-RVW94209537.htm)</sub>

---

### 29. `SIG-068` · `B` · internship · unknown · Sep 2025

Calculate the probability that the value of the first roll of a six-sided die is strictly less than the value of the second roll. Why SIG? Why Trading?

**Answer:** P(first roll < second roll) = 15/36 = 5/12 (about 0.4167). For the 'Why SIG / why trading' part see reasoning - no numeric answer.

*Working:* By symmetry P(a<b) = P(a>b), and P(a=b) = 6/36 = 1/6. So P(a<b) = (1 - 1/6)/2 = 5/12. Direct count: 5+4+3+2+1 = 15 favourable ordered pairs out of 36. For 'Why SIG / why trading': they want evidence you know what the job is day to day and that your reasons survive contact with reality - decisions under uncertainty with fast, objective feedback; the SIG-specific hook is the poker/decision-process culture and the fact that they train traders from scratch rather than hiring for prior finance experience. Bring one concrete story (a game, a competition, a research project) where you made a decision on incomplete information and can say what you learned from being wrong. Avoid 'I like markets and maths'.

*Assumption:* Two fair independent six-sided dice; 'strictly less' excludes ties.

<sub>numerically verified — `CHECK p=5/12 (0.416667) count=15/36 vs claimed=5/12 (0.416667)`</sub>

<sub>Source: glassdoor · 2025-11-09 · [link](https://www.glassdoor.com/Interview/Susquehanna-International-Group-Interview-E24446-RVW101165338.htm)</sub>

---

### 30. `SIG-027` · `B` · unknown · unknown · Nov 2024

Calculate the probability of having a disease if the test is positive. What is the probability if the test is positive twice?

**Answer:** P(D|+) = pi*s / (pi*s + (1-pi)*f) and P(D|++) = pi*s^2 / (pi*s^2 + (1-pi)*f^2), where pi = prevalence, s = sensitivity, f = false-positive rate. With the standard textbook numbers pi = 1%, s = 99%, f = 1%: P(D|+) = 1/2 and P(D|++) = 99/100.

*Working:* Use odds. Prior odds of disease are pi:(1-pi) = 1:99; a positive test multiplies the odds by the likelihood ratio s/f = 99, giving posterior odds 99:99 = 1:1, so P(D|+) = 1/2 - the answer that surprises people, because a 99%-accurate test on a 1%-prevalent disease is a coin flip. A second independent positive multiplies by 99 again: odds 99:1, so P(D|++) = 99/100.

*Assumption:* No numbers were recorded with the question, so I give the closed form plus the canonical 1%/99%/99% instance. The two tests are treated as conditionally independent given disease status - worth flagging out loud, because repeat tests on the same person are positively correlated in practice (a patient whose blood cross-reacts will keep testing positive), so the true P(D|++) is lower than the independent calculation, and a different test type is more informative than repeating the same one.

<sub>numerically verified — `CHECK P(D|+)=1/2 (0.5000, mc 0.4966), P(D|++)=99/100 (0.9900, mc 0.9894) vs 1/2, 99/100`</sub>

<sub>Source: glassdoor · 2025-05-13 · [link](https://www.glassdoor.com/Interview/Susquehanna-International-Group-Interview-E24446-RVW97303579.htm)</sub>

---

### 31. `SIG-065` · `B` · unknown · unknown · 2025

Basic questions like how would you apply ML and AI to your job?

**Answer:** Model answer: name one or two concrete trading problems, then show you understand why financial data breaks standard ML. Good candidate applications: (1) short-horizon return prediction from order-book features (queue imbalance, trade signs, microprice); (2) fill-probability / queue-position models that feed a quoting engine; (3) execution and market-impact models for scheduling child orders; (4) fitting and de-arbing the implied vol surface; (5) classification of toxic vs benign order flow; (6) non-alpha uses - parsing filings/news with LLMs, research tooling, code review, data-quality monitors. Then the discipline: define label and horizon first; purged/embargoed walk-forward validation, never random k-fold on time series; strict point-in-time data to avoid lookahead and survivorship bias; signal-to-noise is so low (daily R^2 of 0.001-0.01 is a real signal) that regularised linear models and gradient-boosted trees usually beat deep nets; put transaction costs inside the objective, not after; respect the latency budget at inference; monitor for decay and regime change. Close by naming where ML is the wrong tool: no-arbitrage relations and thin-data problems are better served by explicit models.

*Working:* Open-ended screening question. The interviewer is testing judgement, not vocabulary: can you connect a method to a problem that actually makes money, and do you know why backtests lie? Reciting architectures is the failure mode; naming a concrete use case plus one validation pitfall is the pass.

<sub>guidance, no single correct value</sub>

<sub>Source: glassdoor · 2025-04-09 · [link](https://www.glassdoor.com/Interview/Susquehanna-International-Group-Interview-E24446-RVW96560287.htm)</sub>

---

### 32. `SIG-044` · `B` · new_grad · unknown · 2024

Compute the probability of an overlap of arrivals.

**Answer:** Underspecified as recorded. For the standard set-up - two people (or ships, or trains) arrive independently and uniformly at random in a window of length T, and each stays for time w - the probability their visits overlap is 1 - ((T-w)/T)^2. With the usual numbers (one-hour window, each waits 15 minutes) that is 1 - (3/4)^2 = 7/16 = 0.4375.

*Working:* Plot arrival times (X, Y) uniformly on the T x T square. They miss each other iff |X - Y| > w, which is two right triangles of leg T - w, total area (T-w)^2. So P(overlap) = 1 - (T-w)^2/T^2. If the two have different stay lengths a and b, the two triangles differ and P(overlap) = 1 - [(T-a)^2 + (T-b)^2]/(2T^2).

*Assumption:* The question as harvested carries no parameters at all, so I solved the canonical 'two uniform arrivals in a fixed window, each waits w' problem and gave the general formula plus the standard 60-minute/15-minute instance. If the original had different numbers, substitute them into 1 - ((T-w)/T)^2.

<sub>numerically verified — `CHECK 0.4372 (exact 7/16 ) vs 7/16` · confidence: **low**</sub>

<sub>Source: glassdoor · 2024-10-28 · [link](https://www.glassdoor.com/Interview/Susquehanna-International-Group-Interview-E24446-RVW92322145.htm)</sub>

---

### 33. `SIG-048` · `B` · new_grad · unknown · Aug 2024

You have $100 and get an extra $100 to play a casino game where you bet on flips of a fair coin, and this game has 4:5 payout. You must bet a total of at least $500 to cash out. How do you maximize your expected earnings?

**Answer:** Bet big, not small: stake the whole $200 on the first flip; if it wins ($360 in hand) stake exactly $300 on the second flip, which clears the $500 wagering requirement, then cash out. Expected cash-out $165, i.e. expected profit $65 on your own $100. Outcome distribution: 1/2 -> $0 (lose your $100), 1/4 -> $600 (+$500), 1/4 -> $60 (-$40).

*Working:* At 4:5, a $5 stake wins $4 or loses $5, so every dollar wagered has EV -$0.10. By optional stopping, E[final bankroll] = 200 - 0.1*E[W], where W is the total ever wagered, so maximising profit means MINIMISING E[W]. You must reach W = 500 to cash out, and the only way to stop short of that is to go broke - which is a good outcome here, because the $100 bonus means busting costs you only $100 while capping W at $200. Bold play maximises that escape: E[W] = (1/2)(200) + (1/2)(500) = 350, so E[profit] = 100 - 35 = $65. Note that any strategy that never busts wagers the full $500 and earns 100 - 50 = -$50, so grinding out small bets loses money; the bonus plus the bust-escape is what makes the game beatable. A dynamic program over stake sizes confirms 350 is the minimum attainable E[W] (also re-run on a $1 stake grid, same answer).

*Assumption:* 4:5 means the house pays $4 profit per $5 staked (a 10% house edge); the $100 bonus is cashable once the $500 total-wagering requirement is met; stakes are unrestricted up to your bankroll; you cannot withdraw anything before clearing the requirement. If the bonus were 'sticky' (non-withdrawable) the numbers change.

<sub>numerically verified — `CHECK strategyEV=65 dpMinE[W]=350 dpBestProfit=65 vs strategyEV=65 dpMinE[W]=350 dpBestProfit=65` · confidence: **medium**</sub>

<sub>Source: glassdoor · 2024-09-27 · [link](https://www.glassdoor.com/Interview/Susquehanna-International-Group-Interview-E24446-RVW91423031.htm)</sub>

---

### 34. `SIG-060` · `B` · internship · unknown · 2025

How would you price an option contract given its strike price and possible fair values?

**Answer:** Guidance: value = discounted risk-neutral expectation of the payoff. With a discrete set of possible fair values S_i carrying probabilities p_i, a call struck at K is worth C = DF * sum_i p_i * max(S_i - K, 0), and a put is DF * sum_i p_i * max(K - S_i, 0).

*Working:* What the interviewer is testing: do you price the payoff distribution rather than guess, and do you know the probabilities must be risk-neutral, not your personal view. A strong answer walks through: (1) list the possible fair values and their probabilities; (2) check the probabilities are consistent with the underlying's forward price - sum p_i * S_i must equal the forward, otherwise you are quoting an arbitrageable market in the stock before you even trade the option; (3) compute the expected payoff max(S_i - K, 0) under those probabilities; (4) discount at the risk-free rate to today; (5) sanity check against the no-arbitrage bounds (a call is worth between max(F - K, 0) discounted and the value of the underlying, is monotone decreasing in strike, and convex in strike) and against put-call parity C - P = DF*(F - K); (6) then quote a two-sided market around theory, widening for uncertainty in the probabilities, hedging costs and your risk limits, rather than quoting the theoretical value itself. Concrete example to offer: if the stock will be 120 or 80 with probability 1/2 each (forward 100) and K = 100 with zero rates, the call is 0.5*20 + 0.5*0 = 10, the put is 10, and parity holds since F = K. Mentioning that this is exactly the discrete-state analogue of Black-Scholes - and that replication, not the expectation, is what makes the price enforceable - is the extra step that distinguishes a strong answer.

*Assumption:* The question describes a method rather than a specific numeric case, so I set out the framework with a worked micro-example.

<sub>guidance, no single correct value</sub>

<sub>Source: glassdoor · 2025-07-18 · [link](https://www.glassdoor.com/Interview/Susquehanna-International-Group-Interview-E24446-RVW98791545.htm)</sub>

---

### 35. `SIG-026` · `B` · internship · unknown · 2023

You are playing a game where you and your opponent have put $10 in the pot each. Your opponent bets another $10. What is the minimum probability of you winning to call this $10 bet?

**Answer:** 1/4 (25%)

*Working:* There is $20 in the pot; the opponent's $10 bet makes it $30, and calling costs you $10 - pot odds of 3:1. Relative to folding, calling gains $30 with probability p and loses $10 with probability 1-p, so break-even is 30p - 10(1-p) = 0, i.e. 40p = 10 and p = 1/4. Equivalently in absolute terms: folding is -$10, calling is 20p - 20(1-p) = 40p - 20, and these are equal at p = 1/4.

*Assumption:* The call closes the action (no further betting, no fold equity, no possibility of a chopped pot), and 'winning' means taking the whole pot. With more betting to come, implied odds and reverse implied odds move the threshold.

<sub>numerically verified — `CHECK breakeven p = 0.250000 (incremental) / 0.250000 (absolute), edge(1/4)=0 vs 1/4, 1/4, 0`</sub>

<sub>Source: glassdoor · 2023-09-25 · [link](https://www.glassdoor.com/Interview/Susquehanna-International-Group-Interview-E24446-RVW80372101.htm)</sub>

---

### 36. `SIG-020` · `B` · internship · unknown · 2020

You have 9 coins, one of which is heavier than the others, and a scale. How can you determine which coin is heavier by only using the scale twice?

**Answer:** Yes, two weighings always suffice: weigh three against three, then one against one.

*Working:* Split the coins into {1,2,3}, {4,5,6}, {7,8,9}. Weigh the first group against the second: if one pan falls, the heavy coin is among those three; if they balance, it is in {7,8,9}. Now weigh two coins of the identified triple against each other: the pan that falls names the coin, and if they balance it is the third. This is information-theoretically tight - two weighings produce 3^2 = 9 distinguishable outcomes and there are exactly 9 candidates - so 9 is the largest number of coins solvable in two weighings.

*Assumption:* A two-pan balance (three possible outcomes per weighing) and exactly one heavy coin, all others identical.

<sub>numerically verified — `CHECK identified 9/9 coins in 2 weighings, capacity 3^2=9 vs 9/9, 9`</sub>

<sub>Source: glassdoor · 2020-12-11 · [link](https://www.glassdoor.com/Interview/Susquehanna-International-Group-Interview-E24446-RVW39378462.htm)</sub>

---

### 37. `SIG-024` · `B` · unknown · unknown · Jul 2023

Do you have any experience with sports trading?

**Answer:** No numeric answer. Answer honestly; if you have sports-trading experience, describe how you formed a price and managed risk, and if you do not, map the adjacent experience you do have.

*Working:* Sports markets are a favourite SIG proxy for trading because they have a clean, fast-settling truth and an explicit house edge to beat. A strong answer covers: how you formed your own number before looking at the market price, where you thought your edge came from and why it would persist, how you sized (fraction of bankroll, Kelly or a fraction of it), how you dealt with the vig and with limits or being restricted, and how you measured yourself - closing line value is the answer that signals you understand the difference between being right and being lucky. If you have no experience, say so and offer the nearest thing: poker, prediction markets, a model you built and tracked, or any situation where you had to commit to a number and were scored on it. Do not inflate - the follow-up will ask for the details.

<sub>guidance, no single correct value</sub>

<sub>Source: glassdoor · 2024-04-13 · [link](https://www.glassdoor.com/Interview/Susquehanna-International-Group-Interview-E24446-RVW86283368.htm)</sub>

---

### 38. `SIG-010` · `B` · unknown · unknown · 2023

Which financial derivatives do you have experience trading?

**Answer:** No numeric answer. Say exactly what you have traded, in what size, and what you learned - and if the honest answer is 'none', say so and pivot to the adjacent experience you do have.

*Working:* The question is a screen for bluffing: whatever you name, the follow-up is a mechanics question ('what is the delta of an at-the-money call', 'you are long a straddle and vol drops, what happens', 'what is the settlement on that future'), and inflated claims collapse immediately. Structure a strong answer as: instrument and venue, why you put the trade on, how you sized it, and one specific thing that surprised you - ideally a loss and the lesson. If you have not traded derivatives, say that plainly and offer what is genuinely analogous: paper trading with a written thesis, prediction markets, poker or sports betting where you priced something and were held to it, a pricing or backtesting project you built. Interviewers value a well-understood small experience over a vague large claim.

<sub>guidance, no single correct value</sub>

<sub>Source: glassdoor · 2023-09-21 · [link](https://www.glassdoor.com/Interview/Susquehanna-International-Group-Interview-E24446-RVW80270779.htm)</sub>

---

### 39. `SIG-052` · `B` · internship · unknown · 2026

What is the max entry fee you would take to earn the outcome of a dice roll?

**Answer:** $3.50 (= 7/2), the expected face value

*Working:* A fair six-sided die paying its face value in dollars has EV (1+2+3+4+5+6)/6 = 21/6 = 7/2 = 3.5. A risk-neutral player is indifferent at a 3.50 fee and pays anything below it. Two things worth saying out loud in the interview: (i) with real risk aversion, or with the game played only once for meaningful size, you would pay less than 3.50 - the certainty equivalent is below the mean; (ii) if asked to make a market rather than name a number, quote around it, e.g. 3.40 at 3.60.

*Assumption:* Standard fair d6, payoff equals the face value in dollars, single roll, risk-neutral pricing.

<sub>numerically verified — `CHECK 7/2 3.5 vs 7/2 3.5` · confidence: **medium**</sub>

<sub>Source: glassdoor · 2026-07-02 · [link](https://www.glassdoor.com/Interview/Susquehanna-International-Group-Interview-E24446-RVW104625356.htm)</sub>

---

### 40. `SIG-017` · `B` · internship · unknown · 2013

the probability of seeing a shooting star in 1 hour is 91%. What is the probability of seeing a shooting star in 30 minutes?

**Answer:** 7/10 = 70%

*Working:* Model the sightings as a Poisson process, so 'no star' probabilities multiply over disjoint intervals. P(no star in an hour) = 0.09 = P(no star in 30 min)^2, so P(no star in 30 min) = 0.3 and P(at least one) = 0.7. The trap answer is 91%/2 = 45.5%, which is wrong because 'at least one' is not additive over intervals.

*Assumption:* Stars arrive as a homogeneous Poisson process (equivalently: the two half-hours are independent and identically distributed). The nice arithmetic - 0.09 is a perfect square - confirms this is the intended reading.

<sub>numerically verified — `CHECK exact=0.700000 mc=0.700479 vs 0.7`</sub>

<sub>Source: glassdoor · 2013-03-11 · [link](https://www.glassdoor.com/Interview/Susquehanna-International-Group-Interview-E24446-RVW2450001.htm)</sub>

---

### 41. `SIG-053` · `B` · unknown · unknown · unknown

Years ago, I was asked about coin flipping outcome with normal coins and a biased coin. Given five flips are all heads, what is the probability that the coin is the biased one (both sides are heads)?

**Answer:** With n coins in total (n-1 fair plus 1 two-headed), one picked at random: P(two-headed | 5 heads) = 32/(n+31). Instances: n=2 -> 32/33; n=3 -> 16/17; n=10 -> 32/41; n=100 -> 32/131; n=1000 -> 32/1031.

*Working:* Bayes: P(biased | HHHHH) = (1/n)(1) / [(1/n)(1) + ((n-1)/n)(1/32)] = 32/(32 + n - 1) = 32/(n+31). The 1/32 is the chance a fair coin gives five heads; the two-headed coin gives them with certainty, so its likelihood ratio is 32:1 against each individual fair coin.

*Assumption:* The number of coins is missing from the recollection, so I give the general formula. Assumed one coin is drawn uniformly at random from n-1 fair coins plus 1 double-headed coin and then flipped 5 times, all heads. Plug in the n from the original question.

<sub>numerically verified — `CHECK [(2, 0.9699, Fraction(32, 33), 0.9697), (10, 0.7794, Fraction(32, 41), 0.7805)] vs formula 32/(31+n): n=2 -> 32/33=0.9697, n=10 -> 32/41=0.7805` · confidence: **medium**</sub>

<sub>Source: reddit_thread · 2022-04-09 · [link](https://www.reddit.com/r/FinancialCareers/comments/tzyuhp/_/i42romz/)</sub>

---

### 42. `SIG-062` · `C` · new_grad · online_assessment · 2026

You walk into a barn and see a collection of spiders, chickens, and cows. You notice that there are 520 legs in total. The number of chickens is twice the number of cows and the number of spiders is twice the number of chickens. Compute the number of spiders.

**Answer:** 52 spiders

*Working:* Let c = cows, so chickens = 2c and spiders = 4c. Legs: cows 4, chickens 2, spiders 8, giving 4c + 2(2c) + 8(4c) = 4c + 4c + 32c = 40c = 520, so c = 13. Then chickens = 26 and spiders = 52 (check: 52 + 52 + 416 = 520).

*Assumption:* Spiders have 8 legs, chickens 2, cows 4; whole animals only.

<sub>numerically verified — `CHECK [(52, 26, 13)] vs [(52, 26, 13)]`</sub>

<sub>Source: other · 2025-09-04 · [link](https://web.archive.org/web/20250912084409/https://www.1point3acres.com/bbs/thread-1144112-1-1.html)</sub>

---

### 43. `SIG-038` · `C` · new_grad · online_assessment · 2026

I need to seat 5 toddlers (Anna, Brian, Charlie, Dixie, Eva) at a round table with these rules: i) Anna won’t sit next to Brian or Eva. ii) Brian won’t sit next to Charlie. iii) Dixie won’t sit next to Eva or Charlie. If Dixie is sitting to the left of Anna, who is sitting to the left of Brian?

**Answer:** Eva

*Working:* At a round table of 5 everyone has exactly 2 neighbours, which pins the arrangement down. Anna cannot sit by Brian or Eva, so Anna's neighbours are Charlie and Dixie. Dixie cannot sit by Eva or Charlie, so Dixie's neighbours are Anna and Brian. Brian cannot sit by Charlie (rule ii) or Anna (rule i), so Brian's neighbours are Dixie and Eva. The remaining edge closes the cycle Charlie-Eva. So the unique seating is the cycle Anna-Charlie-Eva-Brian-Dixie-Anna. 'Dixie is to the left of Anna' fixes which way round we read it: going leftwards from Anna gives Anna, Dixie, Brian, Eva, Charlie. Hence the person to Brian's left is Eva.

*Assumption:* 'To the left of' is a single consistent rotational direction for everyone (all toddlers facing the table), so the clue about Dixie fixes the direction; the answer does not depend on which physical direction 'left' is, because the seating cycle is unique up to reflection.

<sub>numerically verified — `CHECK ['E'] cycles= [('A', 'D', 'B', 'E', 'C')] vs ['E']`</sub>

<sub>Source: other · 2025-09-04 · [link](https://web.archive.org/web/20250912084409/https://www.1point3acres.com/bbs/thread-1144112-1-1.html)</sub>

---

### 44. `SIG-005` · `C` · new_grad · online_assessment · 2026

Compute the weight of the green triangle in pounds if the following system is balanced and weighs 96 pounds in total.

**Answer:** 6 pounds - but conditional on a diagram that is not in the harvested text.

*Working:* The balance figure was an image and is absent, so the puzzle is not solvable from the words alone. The general rule is torque balance: a beam pivoted with arm lengths a on the left and b on the right satisfies a*W_left = b*W_right, so a hanging beam divides the load it carries in the ratio b:a, and an equal-arm beam halves it. The source's own explanation ('the system is balanced, so triangle = 96/2/2/2/2') describes four nested equal-arm balances above the green triangle: 96 -> 48 -> 24 -> 12 -> 6.

*Assumption:* That the figure is a four-level equal-arm mobile with the green triangle as a leaf, which is what the source's arithmetic implies. This number is figure-specific: solutions circulating for other sittings of the same SIG item give 8 lb and 48 lb, so it is the diagram, not a universal answer.

<sub>confidence: **medium**</sub>

<sub>Source: other · 2025-09-04 · [link](https://web.archive.org/web/20250912084409/https://www.1point3acres.com/bbs/thread-1144112-1-1.html)</sub>

---

### 45. `SIG-021` · `C` · new_grad · online_assessment · 2026

You roll three fair 6-sided dice. If they all show the same number, you earn $20. If exactly two of the numbers are the same, you earn $10. If all of the numbers are different, you lose $2. Compute your expected return per roll in dollars. (Round to the nearest cent.)

**Answer:** 65/18 = $3.61 (3.6111...)

*Working:* Out of 216 equally likely ordered triples: 6 are all-same, 6*5*4 = 120 are all-different, leaving 216 - 6 - 120 = 90 with exactly two matching. E = (6*20 + 90*10 + 120*(-2))/216 = (120 + 900 - 240)/216 = 780/216 = 65/18 = 3.6111, i.e. $3.61 to the nearest cent.

*Assumption:* Fair independent dice; 'earn'/'lose' are the net amounts, with no separate entry fee.

<sub>numerically verified — `CHECK E=65/18 (3.6111, $3.61) counts={'all same': 6, 'exactly two': 90, 'all diff': 120} vs 65/18=3.6111, $3.61, {6,90,120}`</sub>

<sub>Source: other · 2025-09-04 · [link](https://web.archive.org/web/20250912084409/https://www.1point3acres.com/bbs/thread-1144112-1-1.html)</sub>

---

### 46. `SIG-059` · `C` · new_grad · online_assessment · 2026

Suppose you have 3 tokens for a betting game and your goal is to reach 5 tokens before running out. Each turn you bet as many tokens as possible but not more than needed to reach 5. You win each bet with probability 2/3​. Compute the probability you reach 5 tokens before running out. (Give your answer as a reduced fraction.)

**Answer:** 62/77 (approx 0.8052)

*Working:* Bold play: from i tokens you stake min(i, 5-i). Let p_i be the probability of reaching 5. p_1 = (2/3)p_2, p_2 = (2/3)p_4, p_3 = 2/3 + (1/3)p_1, p_4 = 2/3 + (1/3)p_3. Then p_1 = (4/9)p_4, so p_4 = 2/3 + (1/3)[2/3 + (4/27)p_4] = 8/9 + (4/81)p_4, giving p_4 = 72/77 and p_3 = 2/3 + (4/27)(72/77) = 154/231 + 32/231 = 186/231 = 62/77.

*Assumption:* Even-money bets (a winning stake of s returns s in profit), win probability 2/3 each turn, independent turns, ruin at 0 tokens.

<sub>numerically verified — `CHECK exact=62/77 mc=0.8053 vs 62/77 0.8052`</sub>

<sub>Source: other · 2025-09-04 · [link](https://web.archive.org/web/20250912084409/https://www.1point3acres.com/bbs/thread-1144112-1-1.html)</sub>

---

### 47. `SIG-054` · `C` · unknown · online_assessment · unknown

青蛙想从(0,0)跳到(7,4),每次只能向右跳一格或向上跳一格。青蛙不愿意同方向连续跳三次。共多少种不同跳法?

*English:* A frog wants to jump from (0,0) to (7,4); each jump can only be one square to the right or one square up. The frog is unwilling to jump three times in a row in the same direction. How many different jump sequences are there?

**Answer:** 30

*Working:* The path is a word with 7 R's and 4 U's whose runs all have length 1 or 2. If the R's form j runs and the U's form k runs then |j - k| <= 1, and the number of ways to split 7 into j parts of size 1 or 2 is C(j, 7-j): j=4 -> 4, j=5 -> 10, j=6 -> 6, j=7 -> 1. Splitting 4 into k such parts gives C(k, 4-k): k=2 -> 1, k=3 -> 3, k=4 -> 1. Interleavings: 2 when j = k, 1 when |j - k| = 1. Total = (j=4,k=3): 4*3 = 12, plus (j=4,k=4): 4*1*2 = 8, plus (j=5,k=4): 10*1 = 10, giving 30.

*Assumption:* 'Unwilling to jump three times in a row in the same direction' means no run of 3 or more identical steps (runs of 2 are allowed).

<sub>numerically verified — `CHECK 30 vs 30`</sub>

<sub>Source: 1point3acres · unknown · [link](https://www.1point3acres.com/bbs/thread-1114232-1-1.html)</sub>

---

### 48. `SIG-057` · `C` · unknown · online_assessment · unknown

[... 5 toddlers at a round table, opening sentence cut off by the paywall ...] are some problems! i. Anna won't sit next to Brian or Eva. ii. Brian won't sit next to Charlie. iii. Dixie won't sit next to Eva or Charlie. If Dixie is sitting to the left of Anna, who is sitting to the left of Brian?

**Answer:** Eva

*Working:* At a round table of 5 everyone has exactly 2 neighbours, which pins the arrangement down. Anna cannot sit by Brian or Eva, so Anna's neighbours are Charlie and Dixie. Dixie cannot sit by Eva or Charlie, so Dixie's neighbours are Anna and Brian. Brian cannot sit by Charlie (rule ii) or Anna (rule i), so Brian's neighbours are Dixie and Eva. The remaining edge closes the cycle Charlie-Eva. So the unique seating is the cycle Anna-Charlie-Eva-Brian-Dixie-Anna. 'Dixie is to the left of Anna' fixes which way round we read it: going leftwards from Anna gives Anna, Dixie, Brian, Eva, Charlie. Hence the person to Brian's left is Eva.

*Assumption:* 'To the left of' is a single consistent rotational direction for everyone (all toddlers facing the table), so the clue about Dixie fixes the direction; the answer does not depend on which physical direction 'left' is, because the seating cycle is unique up to reflection.

<sub>numerically verified — `CHECK ['E'] cycles= [('A', 'D', 'B', 'E', 'C')] vs ['E']`</sub>

<sub>Source: 1point3acres · unknown · [link](https://www.1point3acres.com/bbs/thread-1086565-1-1.html)</sub>

---

### 49. `SIG-028` · `C` · unknown · onsite · unknown

二面就纯bq,问了一些地里其他一样的bq,类似与why QR? why SIG这种之类的。

*English:* The second round was purely behavioural — the same BQs as others on this forum have had, along the lines of "why QR?", "why SIG?" and so on.

**Answer:** No numeric answer. For 'why quant research', describe the work and the feedback loop, not the field's prestige; for 'why SIG', name things that are specifically true of SIG and back each with something you did or saw.

*Working:* These questions are a filter for whether you have actually looked into the job. 'Why QR': say what the day looks like and why it suits you - building models whose predictions are scored by the market within days, having to be numerate and decisive at once, being wrong in public and updating - and give one piece of evidence from your own history (a research project you pushed to a testable conclusion, a competition, a trading or betting habit with a written process). 'Why SIG': the specifics that distinguish it are the poker and decision-making culture (probabilistic thinking under uncertainty, explicitly taught), the education-first onboarding rather than immediate desk assignment, the private partnership structure and what that means for horizon and incentives, and the market-making focus in options. Anchor at least one of those to a concrete touchpoint - a person you spoke to, a talk, a specific problem set. Avoid compensation as your headline, avoid 'prestigious', and avoid anything you could say verbatim about three other firms. Have one honest question ready in return; that is often what the interviewer remembers.

<sub>guidance, no single correct value</sub>

<sub>Source: other · unknown · [link](https://www.1point3acres.com/bbs/thread-1042392-1-1.html)</sub>

---

### 50. `SIG-019` · `C` · unknown · phone_technical · unknown

1. 圆里随机画n条线,问能把圆分成几分 (期望)? 把分成的份数和交点个数对应起来,然后算交点个数的期望。

*English:* 1. Draw n lines at random inside a circle — into how many pieces do they divide the circle (in expectation)? Match the number of pieces to the number of intersection points, then compute the expected number of intersection points.

**Answer:** 1 + n + n(n-1)/6

*Working:* Two chords whose four endpoints are independent and uniform on the circle cross with probability 1/3: given the four points, the three ways to pair them into two chords are equally likely and exactly one pairing crosses. With no three chords concurrent, Euler's formula gives the region count exactly: V = 2n + I, E = 2n arcs + (n + 2I) chord segments, so F - 1 = E - V + 1 = 1 + n + I interior regions. Taking expectations, E[I] = C(n,2)/3 = n(n-1)/6, so E[regions] = 1 + n + n(n-1)/6.

*Assumption:* 'Random line' means a chord with two independent uniform endpoints on the circle. This matters: under other natural models (Bertrand-style random midpoint or random distance from centre) the crossing probability, and hence the constant, changes.

<sub>numerically verified — `CHECK P(cross)=0.33334, E[regions|n=5]=9.3379, geometry confirms 1+n+I in 25/25 vs 1/3=0.33333, 9.3333, 25/25`</sub>

<sub>Source: other · 2020-11-11 · [link](https://www.1point3acres.com/bbs/thread-686183-1-1.html)</sub>

---

### 51. `SIG-011` · `C` · unknown · phone_technical · unknown

2. 扔硬币 进入 HTH HHT 之一就结束,问进入每一个的概率是多大?(不太记得具体ending state是啥了)

*English:* 2. Flip a coin; the game ends as soon as you hit either HTH or HHT. What is the probability of ending on each of them? (I don't remember exactly what the ending states were.)

**Answer:** HHT first with probability 2/3; HTH first with probability 1/3.

*Working:* Flip until the first H. From state 'H': with probability 1/2 the next flip is H, giving 'HH', and from 'HH' the sequence HHT is certain to come first (further H's keep you in 'HH' and the first T completes HHT, while HTH can no longer appear before it). With probability 1/2 the next flip is T, giving 'HT', from which H completes HTH and T returns you to the start. So p = P(HHT first) satisfies p = 1/2 * 1 + 1/2 * (1/2 * 0 + 1/2 * p), i.e. p = 1/2 + p/4, giving p = 2/3.

*Assumption:* Fair coin, and the two ending patterns are HTH and HHT as recorded. The poster flags that they may be misremembering the patterns; the answer is pattern-specific, e.g. a race between HH and HT is 1/2 to 1/2 (also verified below).

<sub>numerically verified — `CHECK exact P(HHT first)=2/3 (0.66667), mc=0.66669, and P(HH before HT) mc=0.50012 vs 2/3=0.66667, 1/2`</sub>

<sub>Source: other · 2020-11-11 · [link](https://www.1point3acres.com/bbs/thread-686183-1-1.html)</sub>

---

### 52. `SIG-047` · `C` · internship · unknown · unknown

-If you have 8 balls with one is slightly heavier, how do you weight the least time to find that one?

**Answer:** 2 weighings, and 2 is provably the minimum. Weigh {1,2,3} vs {4,5,6}. If a side goes down, the heavy ball is in that trio: weigh two of them against each other; the heavier one is it, or if they balance it is the third. If the first weighing balances, weigh the two set-aside balls against each other.

*Working:* Each weighing yields one of 3 outcomes, so k weighings separate at most 3^k cases. Since 3^1 = 3 < 8, one weighing cannot do it; 3^2 = 9 >= 8, and the 3/3/2 split achieves it because every branch leaves at most 3 candidates, which one further weighing resolves.

*Assumption:* Exactly one ball is heavier, all others equal, balance scale gives only lighter/heavier/equal.

<sub>numerically verified — `CHECK 8/8 solved in 2 weighings; 3^1=3 < 8 so 1 is impossible vs 8/8, minimum 2`</sub>

<sub>Source: student_doc · unknown · [link](https://quizlet.com/928572850/sig-qt-intern-interview-questions-flash-cards/)</sub>

---

### 53. `SIG-034` · `C` · unknown · unknown · unknown

you have 8 marbles, 1 weighs less than the others but you cannot tell which one is lighter by touching them. they give you a balance and you only have 2 chances to measure all 8 to find out which one is the lighter one. How would you do it?

**Answer:** Yes - 2 weighings always suffice. Weigh {1,2,3} vs {4,5,6}. If one side RISES, the light marble is in that trio: weigh two of those three against each other; the one that rises is it, and if they balance it is the third. If the first weighing balances, the light marble is one of {7,8}: weigh them against each other. 2 is also the minimum, since one weighing has only 3 outcomes and 3 < 8.

*Working:* Information bound: each weighing has 3 outcomes, so k weighings distinguish at most 3^k cases; 3^1 = 3 < 8 <= 9 = 3^2, so 2 weighings are necessary and (by the 3/3/2 split above) sufficient. The 3/3/2 split is what makes it work: the balanced branch leaves 2 candidates and each unbalanced branch leaves 3, all resolvable by one more weighing.

*Assumption:* One marble is lighter, all others are identical in weight, the balance is exact.

> ⚠️ **The candidate's reported answer is wrong.** source is wrong (in wording, not in structure): the split 3/3/2 and the two-weighing plan are right, but the problem states the odd marble is LIGHTER while the answer says to keep 'the heavier' group and find 'the heaviest'. Followed literally it identifies the wrong marble. It should read: keep the side that rises, and pick the lighter one.

<sub>numerically verified — `CHECK 8 of 8 identified in 2 weighings vs 8`</sub>

<sub>Source: student_doc · unknown · [link](https://quizlet.com/240587160/sig-interview-flash-cards/)</sub>

---


## Citadel  (14)

### 1. `CIT-006` · `B` · unknown · datathon · 2024

Suppose you are given a highway congestion dataset with one feature - the average vehicle speed. It is found that if the average speed is above 70 kilometers per hour, then there are no accidents on the highway. However, if the average speed is below 70 kilometers per hour, then there is at least one accident on the highway. You would like to build a classifier for this problem using support vector machines (SVM). Your colleague suggests that this approach could be problematic due to imbalances in the distribution of vehicle speeds. Is your colleague correct, and why or why not? A. Your colleague is correct - a SVM's performance will suffer because of the reason he mentioned B. Your colleague is incorrect - SVMs assign greater weights to the data near the boundary so will perform fine C. Your colleague is correct - SVMs are bad at classifying traffic-related data in general D. Your colleague is incorrect - although linear VMs will perform poorly, radial basis VMs will perform fine E. None of the above

**Answer:** B: the colleague is incorrect - the boundary is set by the points nearest it, so the overall imbalance in the speed distribution does not hurt here.

*Working:* The data as described is perfectly separable in one dimension at 70 km/h. The max-margin solution depends only on the support vectors - the fastest 'accident' observation and the slowest 'no accident' observation - so multiplying the number of points far from 70 changes nothing. That is exactly B's reasoning. C is a non-argument, D is wrong (a linear SVM is ideal for a 1-D threshold; an RBF kernel would only add variance).

*Assumption:* Worth flagging: B is right for this problem, not as a general law. With overlapping classes and a soft-margin SVM, class imbalance does drag the boundary toward the minority class - which is why class_weight='balanced' exists. B's phrase 'assigns greater weights to the data near the boundary' is also loose: the hinge loss simply ignores correctly-classified points beyond the margin.

<sub>confidence: **medium**</sub>

<sub>Source: blog · 2024-06-25 · [link](https://blog.csdn.net/dcdsc/article/details/139953481)</sub>

---

### 2. `CIT-009` · `B` · unknown · datathon · 2024

3% of a country's population has a particular disease. The national health institute has developed a test for this disease: the test has a 98% "true positive" rate (the probability that a person will test positive given that they have the disease). However, it also has a 4% "false positive" rate (the probability that a person will test positive given that they do NOT have the disease). If you simultaneously take the test twice, and it comes out with two positive results, which of the following is CLOSEST to the probability that you actually have the disease, assuming the tests are independent? A. 0.96 B. 0.95 C. 0.94 D. 0.93 E. 0.92

**Answer:** B: 0.95 (exactly 7203/7591 = 0.94889).

*Working:* Bayes with two independent tests: P(D | ++) = 0.03 * 0.98^2 / (0.03 * 0.98^2 + 0.97 * 0.04^2) = 0.028812 / 0.030364 = 0.948887. Closest listed option is 0.95. The point of the question is that squaring both likelihoods drives the posterior from 0.43 after one positive to 0.95 after two, because the likelihood ratio squares from 24.5 to 600.

*Assumption:* Tests are conditionally independent given disease status - as the question states - which in reality is the questionable part, since repeated runs of the same assay on the same person share error sources.

<sub>numerically verified — `CHECK posterior=7203/7591=0.948887 closest_option=B vs claimed 7203/7591=0.948887 B`</sub>

<sub>Source: blog · 2024-06-25 · [link](https://blog.csdn.net/dcdsc/article/details/139953481)</sub>

---

### 3. `CIT-003` · `B` · unknown · datathon · 2024

What is the MAIN advantage of using a random forest over a decision tree? A. It can be parallelized B. It captures non-linear decision boundaries C. It allows for batch learning D. It reduces overfitting E. It uses less memory

**Answer:** D: it reduces overfitting.

*Working:* A single deep tree is a low-bias, high-variance estimator. A random forest averages many trees grown on bootstrap samples with a random feature subset at each split; the decorrelation is what makes the averaging actually cut variance, so generalisation error drops. A is true but incidental (you could parallelise for speed without changing accuracy); B is false - a single tree already produces non-linear boundaries; C is false; E is false, a forest costs many times the memory of one tree.

<sub>Source: blog · 2024-06-25 · [link](https://blog.csdn.net/dcdsc/article/details/139953481)</sub>

---

### 4. `CIT-019` · `B` · unknown · datathon · 2024

You have a dataset with two features, employee _age (range of 20 to 60) and annual_salary (range of 50,000 to 500,000). Which of the following situations is MOST likely to occur if you feed the dataset as is to a K - means clustering algorithm? A. The data will be appropriately clustered B. The program will run out of memory due to the large annual_salary values C. There will be numerical overflows due to the large annual_salary values D. The clusters will not be meaningful due to the disparity between the variances of the two features E. None of the above

**Answer:** D - the clusters will not be meaningful, because of the disparity in scale/variance between the two features.

*Working:* K-means minimises squared Euclidean distance, so every feature contributes in proportion to its own spread. annual_salary spans 450,000 while age spans 40, so the salary term is ~10^4 larger in distance and ~10^8 larger in squared distance: the age axis is effectively ignored and the algorithm just does a 1-D split on salary. B and C are wrong because values of order 10^5 are trivial for float64 - no overflow, no memory blow-up; A is wrong because the partition is an artefact of units (switch salary to thousands and you get different clusters). The fix is to standardise (z-score) or min-max scale the features first.

<sub>Source: blog · 2024-06-25 · [link](https://blog.csdn.net/dcdsc/article/details/139953481)</sub>

---

### 5. `CIT-018` · `B` · unknown · datathon · 2024

Which of the following machine learning algorithms is NOT sensitive to the initial variables used in the optimization algorithm? A. Hidden Markov models B. Artificial neural networks C. Random forests D. Support vector machines E. k - nearest neighbors

**Answer:** E: k-nearest neighbours.

*Working:* kNN has no training-time optimisation at all - it memorises the data and decides at query time - so there is nothing to initialise. A (HMMs via Baum-Welch/EM) and B (neural nets via SGD) are both non-convex and famously initialisation-dependent; C, random forests, depends on the random seed for bootstrap samples and per-split feature subsets.

*Assumption:* D is a defensible competing answer: SVM training is a convex QP with a unique global optimum, so its solution is also insensitive to initialisation (only runtime changes). The question's phrase 'the initial variables used in the optimization algorithm' points at E, since kNN has no optimisation algorithm whatsoever - but a strict reading admits D as well.

<sub>confidence: **medium**</sub>

<sub>Source: blog · 2024-06-25 · [link](https://blog.csdn.net/dcdsc/article/details/139953481)</sub>

---

### 6. `CIT-008` · `B` · unknown · datathon · 2024

Which of the following assumptions is NOT necessary when performing multiple linear regression with homoskedastic errors? A. The distribution of errors is normal B. The variables are continuous C. The variables are uncorrelated D. The error variance is constant across sample data E. The sample data are independent

**Answer:** B: the variables need not be continuous.

*Working:* Dummy/categorical regressors are completely standard in multiple regression, so continuity of the variables is not an assumption. D is the homoskedasticity the question itself stipulates, and E (independent observations) is a core requirement.

*Assumption:* The question is sloppy and B is the intended answer rather than the uniquely defensible one: A (normally distributed errors) is also unnecessary for OLS to be unbiased and BLUE under Gauss-Markov - normality is needed only for exact finite-sample t/F inference - and C is ambiguous (regressors merely need to be free of perfect collinearity, though errors must be uncorrelated with regressors). If forced to pick one, B, since it is not an assumption under any reading.

<sub>confidence: **medium**</sub>

<sub>Source: blog · 2024-06-25 · [link](https://blog.csdn.net/dcdsc/article/details/139953481)</sub>

---

### 7. `CIT-007` · `B` · unknown · datathon · 2024

You have two fair coins and one coin with heads on both sides. You pick a coin at random and toss it twice. If it reads heads both times, what is the probability it also reads heads after a third toss? A. 1/6 B. 1/3 C. 1/2 D. 2/3 E. 5/6

**Answer:** E: 5/6.

*Working:* Prior 1/3 double-headed, 2/3 fair. P(HH | DH) = 1, P(HH | fair) = 1/4. Posterior P(DH | HH) = (1/3) / (1/3 + (2/3)(1/4)) = (1/3)/(1/2) = 2/3. Then P(3rd toss is heads | first two heads) = (2/3)(1) + (1/3)(1/2) = 5/6. The common wrong answer is 1/2, from forgetting that two heads is itself evidence for the two-headed coin.

*Assumption:* Two fair coins and one two-headed coin, one picked uniformly at random and used for all three tosses.

<sub>numerically verified — `CHECK exact=5/6 montecarlo=0.83312 vs claimed 5/6 0.83333`</sub>

<sub>Source: blog · 2024-06-25 · [link](https://blog.csdn.net/dcdsc/article/details/139953481)</sub>

---

### 8. `CIT-004` · `B` · unknown · datathon · 2024

A government office has two officers handling people's requests. Suppose that the time between request arrivals at the first officer's desk is random and follows an exponential distribution withλ=μ1\lambda=\mu_1 . Similarly, the time between request arrivals at the second officer's desk is also random and follows an exponential distribution with λ=μ2\lambda=\mu_2 . The first officer has probability P1P_1 of referring any request he receives to the office supervisor, and the second officer has probability P2P_2 of doing so. What is the average time between requests referred to the supervisor? A. P1/μ1+P2/μ2P_1/\mu_1 + P_2/\mu_2 B. (P1+P2)/(μ1+μ2)(P_1+P_2) / (\mu_1+\mu_2) C. 1/(μ1P1+μ2P2)1/(\mu_1P_1+\mu_2P_2) D. 1/μ1P1+1/μ2P21/\mu_1P_1 + 1/\mu_2P_2 E. None of the above

**Answer:** C: 1/(mu1*P1 + mu2*P2).

*Working:* Exponential inter-arrival times means each desk is a Poisson process, rates mu1 and mu2. Independent thinning of a Poisson process - keep each arrival with probability P - is again Poisson with rate mu*P. Superposing two independent Poisson processes gives a Poisson process whose rate is the sum. So referrals arrive as a Poisson process of rate mu1*P1 + mu2*P2, and the mean gap is the reciprocal. A and D add mean times rather than rates, which is the trap; B is dimensionally wrong.

*Assumption:* The two desks' arrival streams and the two referral decisions are mutually independent.

<sub>numerically verified — `CHECK mean_gap=0.79972 n=2500869 vs claimed 1/(mu1*P1+mu2*P2)=0.80000`</sub>

<sub>Source: blog · 2024-06-25 · [link](https://blog.csdn.net/dcdsc/article/details/139953481)</sub>

---

### 9. `CIT-002` · `B` · unknown · datathon · 2024

Consider a function f(x,y)f(x, y) of two variables xx and yy . Which of the following statements is ALWAYS true? Here, maxkmax_k and minkmin_k , refer to the maximum over kk and the minimum over kk respectively. A. maxx,minyf(x,y)=minymaxxf(x,y)max_x,min_y f(x, y) = min_ymax_xf(x, y) B. maxx,minyf(x,y)≤minymaxxf(x,y)max_x,min_y f(x, y) \leq min_ymax_xf(x, y) C. maxx,minyf(x,y)≥minymaxxf(x,y)max_x,min_y f(x, y) \geq min_ymax_xf(x, y) D. maxx,minyf(x,y)<minymaxxf(x,y)< span="">max_x,min_y f(x, y) < min_ymax_xf(x, y) E. None of the above, because the answer depends on the specific functional form of f

**Answer:** B: max_x min_y f(x,y) <= min_y max_x f(x,y).

*Working:* For any x0 and any y0, min_y f(x0,y) <= f(x0,y0) <= max_x f(x,y0). The left end does not depend on y0 and the right end does not depend on x0, so maximise the left over x0 and minimise the right over y0: maximin <= minimax, always. A (equality) needs a saddle point, which requires extra structure (von Neumann/Sion: convex-concave and compact), so it is not always true; C is the reverse inequality; D forbids equality, which does occur (any constant f, or any f with a saddle point). E is wrong because B holds for every f.

*Assumption:* Assumes the max and min are attained (or read as sup/inf, under which the inequality is unchanged).

<sub>numerically verified — `CHECK B_violations=0 A_fails=True C_fails=True D_fails=True vs claimed 0 True True True (answer B)`</sub>

<sub>Source: blog · 2024-06-25 · [link](https://blog.csdn.net/dcdsc/article/details/139953481)</sub>

---

### 10. `CIT-012` · `B` · unknown · datathon · 2024

Suppose you have NN samples drawn from NN independent and identical distributions. You use the method of Maximum Likelihood Estimators to estimate the true parameters Θ\Theta governing these distributions, and it gives you parameters Θ\Theta . Which of the following statements is true? A. As NN grows asymptotically large, Θ\Theta becomes an unbiased estimator for Θ\Theta B. As NN grows asymptotically large, no other unbiased estimator of Θ\Theta can achieve a strictly smaller mean squared error value on the sample than Θ\Theta does C. Θ\Theta tends to be normally distributed for large sample sizes D. If the MLEs for Θ1\Theta_1 , Θ2\Theta_2 are Θ1,Θ2\Theta_1, \Theta_2 , respectively, then the MLE of any function of Θ1,Θ2\Theta_1, \Theta_2 is that same function with Θ1,Θ2\Theta_1, \Theta_2 as arguments instead E. All of the above

**Answer:** E: all of the above.

*Working:* Under the usual regularity conditions the MLE is consistent and asymptotically unbiased (A); asymptotically efficient, attaining the Cramer-Rao bound so no competing unbiased estimator beats it asymptotically (B); asymptotically normal, sqrt(N)(theta_hat - theta) -> N(0, I^-1) (C); and functionally invariant, so the MLE of g(theta) is g(theta_hat) (D). All four are the standard textbook properties.

*Assumption:* Requires the usual regularity conditions (identifiability, interior true parameter, smooth likelihood). Two technical caveats an examiner is not asking about: MLEs are typically biased in finite samples (A is an asymptotic claim only - e.g. the MLE of Gaussian variance divides by N), and superefficient estimators like Hodges' beat the Cramer-Rao bound on a measure-zero set, so B holds only in the usual regular sense.

<sub>confidence: **medium**</sub>

<sub>Source: blog · 2024-06-25 · [link](https://blog.csdn.net/dcdsc/article/details/139953481)</sub>

---

### 11. `CIT-011` · `B` · unknown · datathon · 2024

A space probe is controlled by 7 different instructions from the ground. The probabilities of sending these instructions vary - the three most common instructions have probabilities 1/2. 1/4, and 1/8 of being sent, respectively. The remaining four instructions are equally likely to be sent. In expectation, what is the minimum number of whole number bits required to communicate with the probe? A. 2 B. 3 C. 4 D. 5 E. 6

**Answer:** A: 2 bits.

*Working:* The four rare instructions share the leftover 1 - (1/2 + 1/4 + 1/8) = 1/8, so each has probability 1/32. Entropy = (1/2)(1) + (1/4)(2) + (1/8)(3) + 4 x (1/32)(5) = 0.5 + 0.5 + 0.375 + 0.625 = 2 bits exactly. Every probability is a power of 1/2, so Huffman meets the entropy bound exactly with codeword lengths 1, 2, 3, 5, 5, 5, 5 (Kraft sum = 1) and expected length exactly 2. So 2 bits per instruction on average.

*Assumption:* 'Minimum number of whole-number bits in expectation' = expected length of an optimal prefix code, i.e. each codeword is an integer number of bits but the expectation need not be. (A fixed-length code would need 3 bits per instruction; the answer 2 is the average under an optimal variable-length code.)

<sub>numerically verified — `CHECK huffman_expected_bits=2 entropy=2 codeword_lengths=[1, 2, 3, 5, 5, 5, 5] vs claimed 2 2 (answer A)`</sub>

<sub>Source: blog · 2024-06-25 · [link](https://blog.csdn.net/dcdsc/article/details/139953481)</sub>

---

### 12. `CIT-010` · `B` · unknown · datathon · 2024

15. An alternative to k - means clustering is k - medoids clustering. This algorithm chooses actual data points as centers, as opposed to choosing centroids (the mean of data points in a cluster) as centers. Which of the following BEST describes why the k - mediods algorithm is often used over the k - means algorithm? • I. The k - medoids algorithm runs faster than the k - means algorithm does • I. The k - medoids algorithm is more robust to outliers than the k - means algorithm is • Ill. It is easier to choose the value of k in the k - mediods algorithm than in the k - means algorithm A. I only B. lI only C. Ill only D. I and Il only E. ll and Ill only

**Answer:** B: II only - k-medoids is more robust to outliers.

*Working:* II is the real motivation: a medoid is an actual data point minimising summed (often L1) dissimilarity, so a single extreme point cannot drag a centre the way it drags a mean. I is backwards - PAM costs O(k(n-k)^2) per iteration against k-means' O(nkd), so k-medoids is slower. III is false: choosing k is exactly as unguided in both (elbow/silhouette/gap either way). Also worth noting k-medoids only needs a dissimilarity matrix, so it works where no mean is definable.

<sub>Source: blog · 2024-06-25 · [link](https://blog.csdn.net/dcdsc/article/details/139953481)</sub>

---

### 13. `CIT-020` · `B` · unknown · datathon · 2024

A bag contains one fair coin, two two-headed coins, and three two-tailed coins. Each of the six coins is flipped, but the outcomes of five of the coins are hidden from you. randomly. If the outcome you see is heads, what is the probability that the fair coin (which may or may not be the coin that was shown to you) landed heads up? A. 1/5 B. 2/5 C. 1/2 D. 3/5 E. 4/5

**Answer:** 3/5 (choice D)

*Working:* Label the coins F (fair), H1, H2 (two-headed), T1, T2, T3 (two-tailed); one of the six is revealed uniformly. P(revealed face is heads) = P(F revealed and F=H) + P(a two-headed coin revealed) = (1/6)(1/2) + 2/6 = 5/12. Given heads, the revealed coin is F with probability (1/12)/(5/12) = 1/5, in which case the fair coin is certainly heads; otherwise (probability 4/5) it is a two-headed coin, and the fair coin was flipped independently, so it is heads with probability 1/2. Total: (1/5)(1) + (4/5)(1/2) = 1/5 + 2/5 = 3/5.

*Assumption:* The stem is garbled ('...hidden from you. randomly'); I assume the one revealed coin is chosen uniformly at random among the six and that all six flips are independent.

> ⚠️ **The candidate's reported answer is wrong.** source is wrong: it reports B (2/5); the correct value is 3/5, choice D. 2/5 is exactly what you get if you count only the branch in which the fair coin is NOT the one you were shown (4/5 x 1/2 = 2/5) and drop the 1/5 branch in which the coin you are looking at IS the fair coin showing heads. The parenthetical 'which may or may not be the coin that was shown to you' is there precisely to tell you to include that branch.

<sub>numerically verified — `CHECK exact=3/5 (0.60000) mc=0.59989 vs claimed=3/5=0.6`</sub>

<sub>Source: blog · 2024-06-25 · [link](https://blog.csdn.net/dcdsc/article/details/139953481)</sub>

---

### 14. `CIT-016` · `B` · unknown · datathon · 2024

Marty has a bar of gold. Marty's friend Shea is to be paid this gold over the course of 15 days, such that on day XX , 0<=X<=150 <= X <= 15 , Shea has exactly X/15X/15 of the total gold. Additionally, on day 0, Shea has no available gold to use as change. What is the MINIMUM number of pieces that Marty must break the gold bar into so that he can pay Shea in this way? A. 4 B. 5 C. 7 D. 8 E. 15

**Answer:** A: 4 pieces, of sizes 1/15, 2/15, 4/15 and 8/15.

*Working:* Work in fifteenths and let Shea hand pieces back as change. With pieces 1, 2, 4, 8 every value 1..15 is a subset sum (binary), so on day X give Shea exactly the pieces in X's binary expansion, taking back whatever is no longer needed - e.g. day 3 = 1+2, day 4 = give the 4 and take back the 1 and 2. Lower bound: k pieces have only 2^k - 1 non-empty subsets, and 3 pieces give at most 7 < 15 distinct holdings, so 4 is minimal.

*Assumption:* Marty can take pieces back as change from day 1 onward (day 0 is the only day Shea has nothing to give back, which the binary schedule never needs). If no change were ever allowed, the answer would be 15.

<sub>numerically verified — `CHECK min_pieces=4 example=(1, 2, 4, 8) vs claimed 4 (1,2,4,8) -> option A`</sub>

<sub>Source: blog · 2024-06-25 · [link](https://blog.csdn.net/dcdsc/article/details/139953481)</sub>

---


## G-Research  (11)

### 1. `GRES-006` · `C` · unknown · unknown · unknown

Suppose that X and Y are mean zero, unit variance random variables. If least squares regression (without intercept) of Y against X gives a slope of β (i.e. it minimises E[(Y − βX)^2]), what is the slope of the regression of X against Y?

**Answer:** beta again — the slope of X on Y is the same number beta, and both equal rho = E[XY] = Corr(X, Y).

*Working:* Minimising E[(Y − bX)^2] gives b = E[XY]/E[X^2]; minimising E[(X − bY)^2] gives b = E[XY]/E[Y^2]. Both variances are 1 and both means are 0, so both slopes equal the covariance E[XY] = rho, i.e. beta. This coincidence is specific to equal variances: in general beta_(Y|X) = rho·sigma_Y/sigma_X and beta_(X|Y) = rho·sigma_X/sigma_Y, whose product is rho^2 ≤ 1. The two fitted lines are still different lines in the (x, y) plane (slopes beta and 1/beta when drawn on the same axes) unless |rho| = 1 — the regression-to-the-mean point the interviewer is usually fishing for.

*Assumption:* Population (L^2 projection) regression, no intercept, as the question states; E[X^2] = E[Y^2] = 1 given.

<sub>numerically verified — `CHECK (0.2079581895, 0.2079581912, rho=0.2079581949) vs (beta, beta, beta=0.2079581949)`</sub>

<sub>Source: firm_official_pdf · unknown · [link](https://www.gresearch.com/wp-content/uploads/2019/12/Sample-Quant-Exa.pdf)</sub>

---

### 2. `GRES-010` · `C` · unknown · unknown · unknown

I meet someone with 2 children, and I learn that one of the children is a boy. What's the probability that the other child is also a boy? What if one of the children is a boy born on a Tuesday?

**Answer:** 1/3 for the plain version, and 13/27 (≈ 0.4815) for the Tuesday version.

*Working:* Equally likely families {BB, BG, GB, GG}. Conditioning on 'at least one boy' leaves {BB, BG, GB}, of which one is BB: 1/3. With days of the week there are 14×14 = 196 equally likely (sex, day) pairs. P(at least one Tuesday boy) = 1 − (13/14)^2 = 27/196; P(two boys and at least one born Tuesday) = (1/4)(1 − (6/7)^2) = 13/196. Ratio = 13/27. The extra information moves the answer towards 1/2 because it partially identifies *which* child is the boy. Important caveat: both answers depend on the protocol. If instead you met one randomly chosen child of the two and he happened to be a boy (born on a Tuesday), the answer is 1/2 in both versions. The 1/3 and 13/27 answers require that the statement is 'at least one of my two children is a boy (born on a Tuesday)', volunteered independently of which child it is.

*Assumption:* Boys and girls equally likely and independent across children; birth days uniform over 7 and independent of sex; the 'at least one' reading of the information, as intended by the classic puzzle.

<sub>numerically verified — `CHECK (1/3, 13/27) vs (1/3, 13/27)`</sub>

<sub>Source: firm_official_pdf · unknown · [link](https://www.gresearch.com/wp-content/uploads/2019/12/Sample-Quant-Exa.pdf)</sub>

---

### 3. `GRES-003` · `C` · unknown · unknown · unknown

A stock has beta of 2.0 and stock specific daily volatility of 2%. Suppose that yesterday's closing price was $100 and today the market goes up by 1%. What's the probability of today's closing price being at least $103? What's the probability that the closing price is at least $110?

**Answer:** P(close >= $103) = 1 - Phi(0.5) = 0.308538 ~ 30.9%. P(close >= $110) = 1 - Phi(4) = 3.167 x 10^-5 ~ 0.0032%, about 1 in 31,600.

*Working:* Decompose the return as r = beta * r_market + eps with eps ~ N(0, (2%)^2) independent of the market. Given r_market = +1% and beta = 2, r ~ N(2%, (2%)^2). $103 needs r >= 3%, i.e. eps >= 1% = +0.5 sigma, so 1 - Phi(0.5) = 30.85%. $110 needs r >= 10%, i.e. eps >= 8% = +4 sigma, so 1 - Phi(4) = 3.17e-5. Caveats to say out loud: the 2% is stock-SPECIFIC (residual) vol, which is why the market move shifts the mean rather than inflating the variance; and a normal model badly understates the second number - real single-name daily residuals are fat-tailed (earnings, M&A, guidance), so the true probability of an idiosyncratic 4-sigma day is realistically an order of magnitude or more above 1-in-31,600.

*Assumption:* Returns are simple (not log) and normally distributed, beta and residual vol are the correct conditional parameters for today, and the market move is treated as known/realised.

<sub>numerically verified — `CHECK P(>=103)=0.308538 (int 0.308538, mc 0.308880) P(>=110)=3.167e-05 (int 3.167e-05, mc 2.875e-05) vs claimed 0.308538 and 3.167e-05`</sub>

<sub>Source: firm_official_pdf · unknown · [link](https://www.gresearch.com/wp-content/uploads/2019/12/Sample-Quant-Exa.pdf)</sub>

---

### 4. `GRES-011` · `C` · unknown · unknown · unknown

If I break a stick of unit length into three random pieces, what's the expected length of the largest piece?

**Answer:** 11/18 ≈ 0.6111.

*Working:* Two independent uniform cut points give piece lengths that are Dirichlet(1,1,1), so P(a given piece > t) = (1−t)^2. By inclusion–exclusion P(max > t) = 3(1−t)^2 − 3(1−2t)^2·1{t<1/2} + (1−3t)^2·1{t<1/3}, and E[max] = ∫_0^1 P(max > t) dt = 1 − 1/2 + 1/9 = 11/18. Equivalently, for n pieces from n−1 uniform cuts E[max] = H_n/n, and H_3/3 = (11/6)/3 = 11/18.

*Assumption:* 'Three random pieces' = two independent uniform cut points on the stick (the standard reading). Sequential schemes give different answers, e.g. breaking uniformly, then breaking the larger part uniformly, gives a different expectation.

<sub>numerically verified — `CHECK (MC=0.61111, exact=11/18=0.61111) vs (11/18=0.61111)`</sub>

<sub>Source: firm_official_pdf · unknown · [link](https://www.gresearch.com/wp-content/uploads/2019/12/Sample-Quant-Exa.pdf)</sub>

---

### 5. `GRES-001` · `C` · unknown · unknown · unknown

What is the Delta of an at-the-money binary option with a payoff 0 at < $100, and payoff 1 at ≥ $100, as it approaches expiry?

**Answer:** It diverges: delta -> +infinity. Exactly, delta = e^{-rT} phi(d2)/(S sigma sqrt(T)), which at the money is ~ 1/(S sigma sqrt(2 pi T)) -> infinity as T -> 0.

*Working:* The cash-or-nothing digital call is worth e^{-rT} N(d2) with d2 = [ln(S/K) + (r - sigma^2/2)T]/(sigma sqrt(T)); differentiating in S gives delta = e^{-rT} phi(d2)/(S sigma sqrt(T)). At S = K, d2 = -(sigma/2) sqrt(T) + O(sqrt(T)) -> 0, so phi(d2) -> 1/sqrt(2 pi) and delta ~ 1/(S sigma sqrt(2 pi T)), which blows up like 1/sqrt(T). With S = K = 100 and sigma = 20%: ~0.02 with a year left, ~0.32 with a day, ~6.3 with a minute. Economically the payoff is converging to a step function at 100, whose derivative is a Dirac delta at the strike - the position is unhedgeable when pinned at the strike into expiry, which is why desks represent a digital as a tight call spread (long 1/(2e) calls at K-e, short at K+e) and thereby cap the effective delta at 1/(2e).

*Assumption:* Black-Scholes, cash-or-nothing digital (payoff 1 unit of cash), S = K = 100 exactly, no dividends.

<sub>numerically verified — `CHECK deltas_by_T=[(1.0, 0.01985), (0.08333333, 0.06907), (0.00396825, 0.3166), (1.018e-05, 6.253), (0.0, 630.8)] atm_formula_at_T=1e-9 -> 630.8 vs cl`</sub>

<sub>Source: firm_official_pdf · unknown · [link](https://www.gresearch.com/wp-content/uploads/2019/12/Sample-Quant-Exa.pdf)</sub>

---

### 6. `GRES-004` · `C` · unknown · unknown · unknown

(You probably need to look up numbers for this.) Suppose the moon were to disintegrate, and fall to earth over 5000 years. How does this influx of power compare to that of the Sun? Much more, about the same, or much less?

**Answer:** Much more - about 170x the solar power Earth intercepts (~2.9 x 10^19 W of infalling energy versus ~1.7 x 10^17 W of sunlight).

*Working:* Energy released per kg falling from lunar orbit to Earth's surface = GM_E/R_E - GM_E/(2d) = 6.26e7 - 5.2e5 ~ 6.2e7 J/kg (the second term is the specific orbital energy at the Moon's distance, and it is a 1% correction). Times the Moon's mass 7.35e22 kg gives ~4.6e30 J. Spread over 5000 years = 1.58e11 s, that is ~2.9e19 W. Sunlight intercepted by Earth = 1361 W/m^2 x pi R_E^2 = 1.7e17 W. Ratio ~170, so MUCH MORE. Two footnotes: the Moon's own self-binding energy (~1.2e29 J) is a ~3% addition and does not change the conclusion; and measured against the Sun's total luminosity (3.8e26 W) the infall is a mere 7e-8, but the meaningful comparison for a question about Earth is the power Earth actually receives. Physically, ~170 suns of extra heating would boil the oceans and sterilise the planet, so 5000 years is far too fast for this to be survivable.

*Assumption:* Standard constants: M_moon = 7.35e22 kg, Earth-Moon distance 3.844e8 m, R_E = 6.371e6 m, solar constant 1361 W/m^2. Material is assumed to arrive at rest on the surface, starting from circular lunar orbit, at a uniform rate.

<sub>numerically verified — `CHECK per_kg=6.204e+07J E=4.555e+30J P_fall=2.887e+19W P_solar_intercepted=1.735e+17W ratio=166 (vs L_sun ratio=7.5e-08) vs claimed ~3e19 W, ~170x, MU`</sub>

<sub>Source: firm_official_pdf · unknown · [link](https://www.gresearch.com/wp-content/uploads/2019/12/Sample-Quant-Exa.pdf)</sub>

---

### 7. `GRES-008` · `C` · unknown · unknown · unknown

Consider all 100 digit numbers, i.e. those between 0 to 10^100 − 1, inclusive. For each number, take the product of non-zero digits (treat the product of digits of 0 as 1), and sum across all the numbers. What's the last digit?

**Answer:** 6. (The full sum is exactly 46^100.)

*Working:* Every integer in [0, 10^100 − 1] is a distinct string of 100 digits with leading zeros allowed, and the 100 digit positions vary independently. Each position contributes a multiplicative factor f(d) with f(0) = 1 and f(d) = d otherwise, so the whole sum factorises: sum = (sum_{d=0}^{9} f(d))^100 = (1 + 1+2+...+9)^100 = 46^100. Mod 10, 46^k ≡ 6^k ≡ 6 for every k ≥ 1, so the last digit is 6.

*Assumption:* 'Product of non-zero digits' means skip the zeros (equivalently replace each 0 by 1), consistent with the stated convention that the number 0 contributes 1.

<sub>numerically verified — `CHECK (brute==46^k for k=1..6: True, last digit of 46^100 = 6) vs (True, 6)`</sub>

<sub>Source: firm_official_pdf · unknown · [link](https://www.gresearch.com/wp-content/uploads/2019/12/Sample-Quant-Exa.pdf)</sub>

---

### 8. `GRES-007` · `C` · unknown · unknown · unknown

Let R(n) be a random draw of integers between 0 and n − 1 (inclusive). I repeatedly apply R, starting at 10^100. What's the expected number of repeated applications until I get zero?

**Answer:** H_(10^100) = sum_{k=1}^{10^100} 1/k ≈ 100·ln(10) + gamma ≈ 230.8357 applications (so about 231).

*Working:* Let E(n) be the expected number of applications from n. Then E(0) = 0 and E(n) = 1 + (1/n)·sum_{k=0}^{n-1} E(k), which solves to E(n) = H_n (the n-th harmonic number): E(1) = 1, E(2) = 3/2, E(3) = 11/6, ... A cleaner argument: the trajectory strictly decreases, so the number of steps equals the number of distinct states visited after the start. From any state above j, the next draw conditioned on landing in {0,...,j} is uniform there, so the walk visits j with probability 1/(j+1). Hence E[T] = 1 + sum_{j=1}^{n-1} 1/(j+1) = H_n. For n = 10^100, H_n = ln(n) + gamma + O(1/n) = 100·ln(10) + 0.5772157 = 230.83572496...

*Assumption:* R(n) is uniform on {0, ..., n−1}, draws independent; the count stops the moment 0 is drawn (the drawing of 0 itself counts as an application).

<sub>numerically verified — `CHECK (recursion==H_n: True, MC(1e6)=14.3915 vs H_1e6=14.3927, H_1e100=230.8357249643) vs (True, equal, 230.8357249643)`</sub>

<sub>Source: firm_official_pdf · unknown · [link](https://www.gresearch.com/wp-content/uploads/2019/12/Sample-Quant-Exa.pdf)</sub>

---

### 9. `GRES-002` · `C` · unknown · unknown · unknown

How many ways are there to tile dominos (with size 2 × 1) on a grid of 2 × n? How about on a grid of 3 × 2n?

**Answer:** 2 x n: F_{n+1} tilings, Fibonacci with F_1 = F_2 = 1 (so 1, 2, 3, 5, 8, 13, ... for n = 1, 2, 3, 4, 5, 6). 3 x 2n: a_n = 4 a_{n-1} - a_{n-2} with a_0 = 1, a_1 = 3, giving 3, 11, 41, 153, 571, ...; closed form a_n = [(3 + sqrt3)(2 + sqrt3)^n + (3 - sqrt3)(2 - sqrt3)^n]/6.

*Working:* 2 x n: look at the leftmost column - either one vertical domino covers it (leaving 2 x (n-1)) or two horizontal dominoes do (leaving 2 x (n-2)). So T(n) = T(n-1) + T(n-2) with T(1) = 1, T(2) = 2, i.e. T(n) = F_{n+1}. 3 x m: let f(m) count tilings of the full 3 x m board and g(m) tilings of 3 x m with one corner square removed. Breaking on the left edge gives f(m) = f(m-2) + 2 g(m-1) and g(m) = f(m-1) + g(m-2); eliminating g yields f(m) = 4 f(m-2) - f(m-4). Odd m give 0 by the parity of the cell count, so writing a_n = f(2n) gives a_n = 4 a_{n-1} - a_{n-2}, a_0 = 1, a_1 = 3. The characteristic roots are 2 +/- sqrt3, and fitting the two initial values gives the closed form; growth rate (2 + sqrt3) ~ 3.732 per two columns.

<sub>numerically verified — `CHECK 2xn=[1, 2, 3, 5, 8, 13, 21, 34, 55, 89] (fib [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]) 3x2k=[3, 11, 41, 153, 571] (recurrence [3, 11, 41, 153, 571], `</sub>

<sub>Source: firm_official_pdf · unknown · [link](https://www.gresearch.com/wp-content/uploads/2019/12/Sample-Quant-Exa.pdf)</sub>

---

### 10. `GRES-005` · `C` · unknown · unknown · unknown

I have $50 and I'm gambling on a series of coin flips. For each head I win $2 and for each tail I lose $1. What's the probability that I will run out of money?

**Answer:** ((sqrt5 - 1)/2)^50 = phi^-50 = (28143753123 - 12586269025 sqrt5)/2 ~ 3.5532 x 10^-11 (about 1 in 28 billion).

*Working:* Because the only losing step is -$1, running out of money means hitting exactly $0, so ruin from $50 is the 50-fold product of independent one-dollar down-crossings. Let q = P(the walk ever falls one dollar below its current level). Condition on the first flip: with probability 1/2 you lose $1 immediately; with probability 1/2 you gain $2 and must then come down three levels, which by the strong Markov property has probability q^3. So q = 1/2 + q^3/2, i.e. q^3 - 2q + 1 = 0 = (q - 1)(q^2 + q - 1). The drift is +$0.50 per flip so ruin is not certain and the relevant root is q = (sqrt5 - 1)/2 = 1/phi ~ 0.61803, not q = 1. Hence P(ruin) = q^50 = phi^-50; using phi^-50 = ((1-sqrt5)/2)^50 = (L_50 - F_50 sqrt5)/2 with F_50 = 12586269025 and L_50 = 28143753123 gives ~3.5532e-11.

*Assumption:* Fair coin, unlimited number of flips, ruin = wealth reaching exactly $0, bets are fixed at +$2/-$1 regardless of wealth.

<sub>numerically verified — `CHECK q=0.618034 (mc 0.618106) r1=0.618034 ruin_from_50: decimal=3.553186e-11 lucas=3.553186e-11 valueiter=3.553186e-11 vs claimed 3.5532e-11`</sub>

<sub>Source: firm_official_pdf · unknown · [link](https://www.gresearch.com/wp-content/uploads/2019/12/Sample-Quant-Exa.pdf)</sub>

---

### 11. `GRES-009` · `C` · unknown · unknown · unknown

(Hard) A company has a competition to win a car. Each contestant needs to pick a positive integer. If there's at least one unique choice, the person who made the smallest unique choice wins the car. If there are no unique choices, the company keeps the car and there's no repeat of the competition. It turns out that there are only three contestants, and you're one of them. Everyone knows before picking their numbers that there are only three contestants. How should you make your choice?

**Answer:** There is no good pure strategy — randomise. The unique symmetric Nash equilibrium is geometric: pick k with probability p_k = (1−q)q^(k−1), where q ≈ 0.5436890127 is the real root of q^3 + q^2 + q = 1. That is 1 with prob ≈ 45.6%, 2 with ≈ 24.8%, 3 with ≈ 13.5%, 4 with ≈ 7.3%, 5 with ≈ 4.0%, ... Each player then wins with probability q^2 ≈ 29.56%, and with probability (1−q)^3/(1−q^3) ≈ 11.3% nobody wins.

*Working:* If I pick k and the two opponents draw independently from p, I win in exactly two disjoint ways: both of them tie on some j ≠ k (their choice is then not unique, mine is), or all three are distinct and mine is smallest. So W(k) = sum_{j<k} p_j^2 + (sum_{j>k} p_j)^2. No finite support can work: if m is the largest number played, W(m+1) = W(m) + p_m^2 > W(m), so you would always want to go one higher. Trying p_k = (1−q)q^(k−1) gives W(k) = (1−q)/(1+q) + q^(2k−2)·(q^2 − (1−q)/(1+q)), which is independent of k exactly when q^2 = (1−q)/(1+q), i.e. q^3 + q^2 + q = 1. The common value is then q^2 ≈ 0.2956. Practically, against real people (who over-pick 1 and 'clever' mid-sized numbers), deviate towards 2 or 3; the equilibrium is a safety net, not an exploit.

*Assumption:* Symmetric equilibrium sought (asymmetric equilibria exist, e.g. the three players coordinating on 1, 2, 3); all players rational and value the car identically; no prize for second.

<sub>numerically verified — `CHECK (q=0.543689013, spread of W(1..40)=5.55e-17, W=0.295598, MC win=0.29556, p_1..p_5=['0.456', '0.248', '0.135', '0.073', '0.040'], P(no winner)=0.`</sub>

<sub>Source: firm_official_pdf · unknown · [link](https://www.gresearch.com/wp-content/uploads/2019/12/Sample-Quant-Exa.pdf)</sub>

---


## Old Mission Capital  (11)

### 1. `OMC-006` · `B` · unknown · online_assessment · unknown

Given a list of n numbers, return the median of each sublist up to the kth element.

**Answer:** Running (prefix) medians via two heaps: keep a max-heap `lo` holding the smaller half and a min-heap `hi` holding the larger half, rebalanced so 0 <= len(lo)-len(hi) <= 1. After inserting the k-th element the median is lo[0] when k is odd and (lo[0]+hi[0])/2 when k is even. O(log k) per element, O(n log n) total, O(n) space.

*Working:* Push x onto lo, pop lo's max into hi, then if hi is larger pop hi's min back into lo. This keeps both halves ordered and correctly sized, so the median is always readable in O(1) from the heap tops. Alternatives: a `bisect.insort` sorted list is O(k) per insert (O(n^2) total but very fast constants in CPython); a Fenwick/order-statistic tree over the value domain gives O(log U) per insert and is the right answer if values are bounded integers; re-sorting each prefix is the O(n^2 log n) naive baseline. If instead only ONE k is meant (the median of the first k elements), quickselect answers it in O(k) expected time.

*Assumption:* Read as 'for every k = 1..n output the median of the first k elements' (the classic running/streaming median). Even-length median taken as the mean of the two central values.

<sub>numerically verified — `CHECK 400 vs 400`</sub>

<sub>Source: wso · 2024-11-15 · [link](https://www.wallstreetoasis.com/company/old-mission-capital/interview)</sub>

---

### 2. `OMC-013` · `B` · unknown · phone_technical · unknown

If you think the market is overestimating volatility, what options strategy can you use

**Answer:** Sell volatility: short a delta-hedged straddle (or strangle) at the strike/tenor you think is richest, and keep re-hedging the delta so the P&L is the implied-vs-realised spread rather than a directional bet.

*Working:* What they are testing: do you know that an option's price is a bet on volatility, and can you isolate that bet? If your forecast of realised vol is below implied, options are rich, so you sell them; you then hedge the delta, leaving short gamma / short vega, and you collect theta as long as realised moves stay smaller than the implied breakeven (roughly sigma_impl * S * sqrt(dt) per rebalance). Short straddle for maximum vega/gamma at one strike, short strangle if you want a wider profit zone, iron condor / butterfly (or a short calendar) if you want the same view with capped tails. Selling a variance swap is the cleanest pure expression. Strong answers add: sell where the richness is (front-dated for gamma/theta, longer-dated for vega), and name the risks - unbounded loss, gap/jump risk, vol-of-vol and the fact that realised vol spikes exactly when you are shortest, plus margin and pin risk. If they push on 'what if you only think the SHAPE is wrong', pivot to relative value: sell the rich strike/tenor against buying a cheaper one (vol spread, skew or calendar trade).

*Assumption:* Reading 'overestimating volatility' as implied vol > your forecast of realised vol.

<sub>guidance, no single correct value</sub>

<sub>Source: wso · 2025-06-16 · [link](https://www.wallstreetoasis.com/company/old-mission-capital/interview)</sub>

---

### 3. `OMC-002` · `B` · internship · phone_technical · unknown

Four points are chosen uniformly at random on the surface of a sphere. What is the probability that the center of the sphere lies inside the tetrahedron whose vertices are at the four points?

**Answer:** 1/8 = 0.125.

*Working:* The clean argument (Wendel's symmetry trick): fix the four lines through the centre, i.e. the unordered pairs {+v_i, -v_i}, and note that independently replacing each point by its antipode leaves the distribution unchanged. That gives 16 equally likely sign patterns for a given set of four lines. For four points in general position in R^3, exactly 2 of those 16 patterns put the centre inside the tetrahedron — a pattern and its complement — so P = 2/16 = 1/8. Equivalently, Wendel's theorem: for n points drawn from any centrally symmetric distribution in R^d, P(0 not in the convex hull) = 2^(-n+1) * sum_{k=0}^{d-1} C(n-1, k); with n = 4, d = 3 this is (1+3+3)/8 = 7/8, so P(inside) = 1/8. Useful cross-check with the same formula: three points on a circle contain the centre with probability 1/4, which is the well-known 2-D version. The verification below tests both the 1/8 by direct simulation and the exact '2 out of 16 sign patterns' claim on thousands of random configurations.

*Assumption:* 'Uniformly at random on the surface' means independent points from the rotation-invariant distribution on the sphere; general position holds with probability 1, so boundary cases have measure zero.

<sub>numerically verified — `CHECK mc=0.12534 signflip_counts=[2] vs 1/8=0.12500, {2}/16`</sub>

<sub>Source: wso · 2019-10-10 · [link](https://www.wallstreetoasis.com/company/old-mission-capital/interview)</sub>

---

### 4. `OMC-004` · `B` · internship · phone_technical · unknown

There was also a Markov Chain chess question. It essentially went as follows: You and I play chess. 1/2 games end in draws and in the other half I win with 2/3 probability and you win with 1/3. If the matches with either of us winning 3 consecutive games, what is the probability that I win?

**Answer:** 86/99 = 0.8687 (about 86.9%) that the stronger player ('I') wins the match. The other absorption probabilities on the way: with a streak of 1 my win chance is 29/33, with a streak of 2 it is 10/11; when the opponent has a streak of 1 it is 28/33 and with 2 it is 8/11.

*Working:* Per game: P(I win) = (1/2)(2/3) = 1/3 = p, P(you win) = (1/2)(1/3) = 1/6 = q, P(draw) = 1/2 = d. Five transient states: S0 (no current streak, including just after a draw), A1/A2 (my streak of 1 or 2), B1/B2 (yours). Let f be the probability I eventually win. f(S0) = p f(A1) + q f(B1) + d f(S0) f(A1) = p f(A2) + q f(B1) + d f(S0) f(A2) = p*1 + q f(B1) + d f(S0) f(B1) = p f(A1) + q f(B2) + d f(S0) f(B2) = p f(A1) + q*0 + d f(S0) Solving exactly gives f(S0) = 86/99. Sanity check on the direction: draws help the stronger player here, because a draw resets both streaks and returns the match to the neutral state where I have the edge — with no draws at all the answer would be lower (104/123 = 0.8455), and as the draw rate goes to 1 it rises toward 8/9 = 0.889, the chance that a run of three straight decisive games is all mine.

*Assumption:* A draw breaks a run: the match ends when one player wins three CONSECUTIVE games, and a draw in between resets the count for both. This is the natural reading but it is not stated explicitly. Under the alternative convention that draws are simply ignored or replayed (so each decisive game I win with probability 2/3), the answer would be 104/123 = 0.8455 — both are computed in the verification.

<sub>numerically verified — `CHECK exact=86/99(0.868687) mc=0.868725 draws_ignored=104/123(0.845528) vs claimed exact`</sub>

<sub>Source: wso · 2019-10-10 · [link](https://www.wallstreetoasis.com/company/old-mission-capital/interview)</sub>

---

### 5. `OMC-011` · `B` · internship · phone_technical · unknown

2) What is the expected value of rolling a fair dice? What if you can re-roll? What if the re-roll cost 1 dollar and you make 1 dollar for every dot on the die that is shown?

**Answer:** Plain roll: 7/2 = 3.5. With one free optional re-roll: 17/4 = 4.25. With one optional re-roll costing $1 (payoff = $1 per pip): 23/6 ~= 3.8333.

*Working:* E[die] = 21/6 = 7/2. Free re-roll: keep the first roll iff it beats 3.5, i.e. keep 4,5,6, re-roll 1,2,3 -> (1/2)(3.5) + (1/6)(4+5+6) = 17/4. Costed re-roll: re-rolling is worth 3.5 - 1 = 2.5, so re-roll only on 1 or 2 -> (2/6)(2.5) + (1/6)(3+4+5+6) = 5/6 + 3 = 23/6. (If instead you may re-roll indefinitely at $1 a time, the fixed point V = E[max(x, V-1)] gives V = $4 exactly, with the optimal rule 're-roll on 1 or 2'.)

*Assumption:* Fair 6-sided die. 'You can re-roll' read as one optional re-roll whose result you must keep; the $1 version read as the same single re-roll but with a $1 fee and a payoff of $1 per pip. The unlimited-re-roll variant is given too since the wording does not settle it.

<sub>numerically verified — `CHECK ('7/2', '17/4', '23/6', '4') vs ('7/2', '17/4', '23/6', '4')`</sub>

<sub>Source: wso · 2018-09-23 · [link](https://www.wallstreetoasis.com/company/old-mission-capital/interview)</sub>

---

### 6. `OMC-010` · `B` · internship · phone_technical · unknown

4) In how many ways can you have three numbers that sum to 10? What about 11? 5) In how many ways can you have three numbers that some to n for any n greater than or equal to 3?

**Answer:** 36 for 10, 45 for 11, and C(n-1,2) = (n-1)(n-2)/2 in general.

*Working:* Stars and bars: ordered triples of positive integers (a,b,c) with a+b+c = n correspond to choosing 2 of the n-1 gaps between n stars, giving C(n-1,2). n=10 -> C(9,2) = 36; n=11 -> C(10,2) = 45. The 'for any n >= 3' phrasing fits this reading exactly, since C(n-1,2) is the first n at which a solution exists.

*Assumption:* Read as ORDERED triples of POSITIVE integers (unbounded), which is the reading that makes 'any n >= 3' meaningful. Other readings, all verified: non-negative integers allowed -> C(n+2,2), i.e. 66 and 78; unordered triples (partitions into exactly 3 positive parts) -> 8 and 10, general formula the nearest integer to n^2/12; three standard dice -> 27 and 27 out of 216 each.

<sub>numerically verified — `CHECK (36, 45, True, 66, 78, True, 8, 10, True, 27, 27) vs (36, 45, True, 66, 78, True, 8, 10, True, 27, 27)` · confidence: **medium**</sub>

<sub>Source: wso · 2018-09-23 · [link](https://www.wallstreetoasis.com/company/old-mission-capital/interview)</sub>

---

### 7. `OMC-001` · `B` · internship · phone_technical · unknown

1) What is the expected value of a random variable x in [0,10]? What is the variance?

**Answer:** Under the intended reading X ~ Uniform[0,10]: E[X] = 5, Var(X) = 100/12 = 25/3 = 8.333..., SD = 10/sqrt(12) = 5/sqrt(3) = 2.887. Strictly, the question as worded does not specify a distribution, and 'a random variable in [0,10]' pins down nothing: the mean can be anywhere in [0,10] and the variance anywhere in [0,25]. The maximum possible variance is 25, attained by the two-point distribution putting mass 1/2 on 0 and 1/2 on 10 (Popoviciu's inequality, Var <= (b-a)^2/4).

*Working:* For U[a,b]: E = (a+b)/2 = 5, and Var = (b-a)^2/12 = 100/12 = 25/3. Derivation worth being able to produce on the spot: E[X^2] = (1/10)*integral_0^10 x^2 dx = 100/3, so Var = 100/3 - 25 = 25/3. The 'what if it is not uniform' remark is a good thing to raise yourself — this question is usually a warm-up and interviewers often follow with exactly the bounded-variance extension.

*Assumption:* X is uniform on [0,10]. The question does not say so; without that assumption only bounds are available, which I give.

<sub>numerically verified — `CHECK mc_mean=4.9983 mc_var=8.3303 vs 5, 100/12=25/3=8.3333`</sub>

<sub>Source: wso · 2018-09-23 · [link](https://www.wallstreetoasis.com/company/old-mission-capital/interview)</sub>

---

### 8. `OMC-007` · `B` · internship · phone_technical · unknown

There are 5 pirates and they are trying to split 100 gold coins in a rational way. The most senior pirate will choose to split in a certain way and all the other pirates will vote to agree or disagree. The most senior pirate is always the one to propose the split and must get at least a majority of the votes from the other pirates for the split to work. How should the senior-most pirate split the 100 gold coins such that he will survive and maximize his own earnings?

**Answer:** 98 / 0 / 1 / 0 / 1 - the senior pirate keeps 98 and gives 1 coin each to the 3rd and 5th pirates (the two who would get nothing if he were thrown overboard).

*Working:* Backward induction with pirates A(senior) > B > C > D > E, each preferring survival, then gold, then fewer rivals. 2 left (D,E): D votes for himself, 1 of 2 passes, so (100,0). 3 left: C needs one more vote and buys E, who gets 0 in the 2-pirate game, for 1 -> (99,0,1). 4 left: B needs one more vote and buys D for 1 -> (99,0,1,0). 5 left: A needs two more votes and buys the two cheapest, C and E (each getting 0 if A dies), for 1 apiece -> (98,0,1,0,1).

*Assumption:* Standard convention: the proposer votes and a tie passes, so with 5 pirates he needs 3 of 5 votes = himself plus 2 others. If instead the rule is read literally as a STRICT majority of the four other pirates (3 of 4), the induction changes (in the 2- and 3-pirate subgames the proposer is killed) and the answer becomes 97/0/1/1/1. The 98/0/1/0/1 version is what the question is testing.

<sub>numerically verified — `CHECK ([98, 0, 1, 0, 1], [97, 0, 1, 1, 1]) vs ([98, 0, 1, 0, 1], [97, 0, 1, 1, 1])`</sub>

<sub>Source: wso · 2018-02-27 · [link](https://www.wallstreetoasis.com/company/old-mission-capital/interview)</sub>

---

### 9. `OMC-014` · `B` · internship · phone_technical · unknown

You have two decks of cards, one with 52 cards and one with 104. If your goal is to draw a black card followed by a red card, which deck would you choose?

**Answer:** The 52-card deck: P = 13/51 ~= 0.25490 versus 26/103 ~= 0.25243 for the 104-card deck.

*Working:* Two draws without replacement. 52 cards: (26/52)(26/51) = 13/51. 104 cards: (52/104)(52/103) = 26/103. The first draw is 1/2 either way; the edge comes from the second draw, where removing one black card raises the red fraction more in the smaller deck (26/51 > 52/103). In general, with 2n cards the probability is n/(2(2n-1)), which decreases in n toward 1/4.

*Assumption:* Both decks are half black / half red (the 104 deck being two standard decks), and the two cards are drawn without replacement from the same deck.

<sub>numerically verified — `CHECK ('13/51', '26/103', True, 0.2551, 0.2526) vs ('13/51', '26/103', True, 0.2549, 0.2524)`</sub>

<sub>Source: wso · 2015-02-28 · [link](https://www.wallstreetoasis.com/company/old-mission-capital/interview)</sub>

---

### 10. `OMC-012` · `B` · internship · phone_technical · unknown

What is fifty six times sixty seven (no calculator, quick response)?

**Answer:** 3752

*Working:* Fastest mental route: 56*67 = 56*70 - 56*3 = 3920 - 168 = 3752. Cross-check with the difference-of-squares style split (60-4)(60+7) = 3600 + 420 - 240 - 28 = 3752.

<sub>numerically verified — `CHECK (3752, 3752) vs (3752, 3752)`</sub>

<sub>Source: wso · 2015-02-28 · [link](https://www.wallstreetoasis.com/company/old-mission-capital/interview)</sub>

---

### 11. `OMC-009` · `B` · internship · phone_technical · unknown

What is the probability of drawing a 4 of a kind in a 5 card poker hand?

**Answer:** 624/2598960 = 1/4165 ~= 0.000240 (about 1 in 4165)

*Working:* Choose the quad rank (13 ways), take all four suits (1 way), then any of the remaining 48 cards as the kicker: 13*48 = 624 hands. Divide by C(52,5) = 2,598,960 to get 624/2598960 = 1/4165.

*Assumption:* 'Four of a kind' means the hand contains four cards of one rank (the standard poker category); 5 cards dealt from a well-shuffled 52-card deck.

<sub>numerically verified — `CHECK (624, 2598960, Fraction(1, 4165)) vs (624, 2598960, Fraction(1, 4165))`</sub>

<sub>Source: wso · 2014-03 · [link](https://www.wallstreetoasis.com/company/old-mission-capital/interview)</sub>

---


## Morgan Stanley  (10)

### 1. `MS-002` · `B` · unknown · phone_technical · 2026

Rolling dice three time, what's the probability of getting strictly increase number?

**Answer:** 5/54 = 20/216 = 0.0926 (about 9.26%).

*Working:* There are 6^3 = 216 equally likely outcomes. A strictly increasing triple needs three distinct faces, and each set of three distinct faces can be arranged in 3! = 6 orders, exactly one of which is increasing. So the count is C(6,3) = 20 and the probability is 20/216 = 5/54. Cross-check by the complementary route: P(all three distinct) = 6*5*4/216 = 120/216 = 5/9, and given distinctness the increasing order is 1 of 6, so (5/9)/6 = 5/54.

*Assumption:* A fair six-sided die, three independent rolls, 'strictly' increasing.

<sub>numerically verified — `CHECK 5/54 (20/216) vs 5/54 = 5/54`</sub>

<sub>Source: chat_telegram · 2026-01-25 · [link](https://t.me/aistockanalyst/1072)</sub>

---

### 2. `MS-008` · `B` · unknown · phone_technical · 2026

Given two iid RV X and Y N~(mu,sig), what's the min Expectation value of X+Y?

**Answer:** E[min(X,Y)] = mu - sigma/sqrt(pi) = mu - 0.5642*sigma (and symmetrically E[max(X,Y)] = mu + sigma/sqrt(pi)). If instead the question is read completely literally, E[X+Y] = 2mu and there is nothing to minimise: X+Y ~ N(2mu, 2*sigma^2) is unbounded below, so 'the minimum of X+Y' does not exist.

*Working:* The identity that almost certainly produced the garbled wording is min(X,Y) = [(X+Y) - |X-Y|]/2. Here X - Y ~ N(0, 2*sigma^2), and for Z ~ N(0, tau^2) we have E|Z| = tau*sqrt(2/pi), so E|X-Y| = sigma*sqrt(2)*sqrt(2/pi) = 2*sigma/sqrt(pi). Therefore E[min] = (2mu - 2*sigma/sqrt(pi))/2 = mu - sigma/sqrt(pi). Sanity checks: E[min] + E[max] = 2mu as it must, and the answer scales correctly in sigma and shifts with mu. For standard normals this is the familiar -1/sqrt(pi) = -0.5642.

*Assumption:* Two readings are possible and I answer both. I take 'min Expectation value' to mean E[min(X,Y)] (the question_type tag is 'probability_min_expectation'), and sigma to be the standard deviation rather than the variance. If sigma denoted the variance v = sigma^2, the answer would be mu - sqrt(v/pi).

<sub>numerically verified — `CHECK E[min]=1.87215 E[X+Y]=6.00232 vs mu-sig/sqrt(pi)=1.87162, 2mu=6.0` · confidence: **medium**</sub>

<sub>Source: chat_telegram · 2026-01-25 · [link](https://t.me/aistockanalyst/1072)</sub>

---

### 3. `MS-001` · `B` · unknown · phone_technical · 2026

Given 99 unbiased coin and 1 two headed coin, P(H|2H)?

**Answer:** Taken literally, P(heads | the coin is the two-headed one) = 1. That is trivial, so the question is almost certainly the reverse conditional, the classic: pick one of the 100 coins at random, flip it, it lands heads — P(it is the two-headed coin) = (1/100) / [(1/100) + (99/100)(1/2)] = (1/100)/(101/200) = 2/101 = 0.0198. Related quantities worth having ready: P(heads) = 101/200 = 0.505; after k heads in a row, P(two-headed) = 2^k/(2^k + 99) (k=1: 2/101; k=5: 32/131 = 0.244; k=7: 128/227 = 0.564, so it takes 7 straight heads to make the trick coin more likely than not).

*Working:* Bayes in odds form: prior odds (two-headed : fair) = 1 : 99, likelihood ratio for one head = 1 : 1/2 = 2 : 1, so posterior odds = 2 : 99, i.e. probability 2/101. For k heads the likelihood ratio is 2^k, giving odds 2^k : 99.

*Assumption:* The recollection 'P(H|2H)' is garbled. I read it as the standard version — one coin drawn uniformly from the 100 and flipped once, showing heads, asking for the probability it is the two-headed coin. This is the one genuine ambiguity in the question; both readings are answered above.

<sub>numerically verified — `CHECK exact=2/101 mc=0.01997 k=1,2,3 -> ['2/101', '4/103', '8/107'] vs 2/101=0.01980`</sub>

<sub>Source: chat_telegram · 2026-01-25 · [link](https://t.me/aistockanalyst/1072)</sub>

---

### 4. `MS-006` · `B` · unknown · phone_technical · 2026

Two people meet at bus stop, only wait for 15 min and leave, probability of they meet? (Poisson Distribution)?

**Answer:** 7/16 = 0.4375, under the standard reading (each arrives at a uniformly random time in a one-hour window, each waits 15 minutes). General formula for waiting time w in a window of length T: P(meet) = 1 - (1 - w/T)^2.

*Working:* Let X, Y ~ U[0,60] independently be the arrival times. They meet iff |X - Y| <= 15. On the 60x60 square the failure region is two right triangles with legs 45, total area 2 * 45^2/2 = 2025, so P(miss) = 2025/3600 = (3/4)^2 = 9/16 and P(meet) = 7/16. On the 'Poisson' aside in the recollection: as literally stated the problem needs a common arrival window, and the uniform assumption is exactly what a Poisson process gives you — conditional on exactly one arrival in [0,T], that arrival time is Uniform[0,T]. So 'uniform' and 'Poisson' are consistent here rather than in conflict. A genuinely Poisson-process version of the question (two independent streams, meet if arrivals fall within 15 minutes) would be a different and underspecified problem.

*Assumption:* The recollection does not state the arrival window; I take the classic one hour. This is the one parameter that changes the answer: with a 30-minute window it would be 1 - (1/2)^2 = 3/4, with two hours 1 - (7/8)^2 = 15/64.

<sub>numerically verified — `CHECK mc=0.43724 exact=7/16 vs 7/16=0.43750` · confidence: **medium**</sub>

<sub>Source: chat_telegram · 2026-01-25 · [link](https://t.me/aistockanalyst/1072)</sub>

---

### 5. `MS-005` · `B` · unknown · phone_technical · 2026

how do you explain logistic regression to your boss who know nothing ?

**Answer:** Model answer, jargon-free: 'Say we want to predict something that either happens or does not — will this client trade today, will this loan default. If I used ordinary regression I could get an answer of 130% or -20%, which is meaningless as a chance. Logistic regression fixes that. Think of it as a scorecard: every input gets a weight, you add up the points, and then you push the total through an S-shaped curve that squeezes any number into the 0-to-100% range. A very negative score comes out near 0%, a score of zero comes out at 50%, a very positive score near 100%. The computer picks the weights so that the outcomes we actually saw in history come out as likely as possible. The one thing worth knowing about the weights is that they act on the odds, not the probability: a weight of 0.7 on "the client called us" means calling roughly doubles the odds of a trade, whether the odds started at 1-in-100 or 1-in-2.' Then close with a caveat and a test, which is what separates a good answer: 'It assumes the score is a straight-line combination of the inputs, so it will not discover on its own that a factor only matters in a crisis — I have to add that. And I would judge it by whether the numbers are honest: of all the days it said 70%, did it happen about 70% of the time?'

*Working:* What is tested: communication, not statistics. The interviewer wants to see whether you can talk to a PM, a risk manager or a client. Rules for the answer: lead with the problem it solves, use one concrete example from their world, use an analogy (scorecard, dimmer switch), never say 'sigmoid', 'logit' or 'maximum likelihood' without immediately unpacking them, keep it under about 45 seconds, and finish with a limitation and how you would check it works. Do not write down the formula unless asked. No verify_code, because this is purely a communication question.

<sub>guidance, no single correct value</sub>

<sub>Source: chat_telegram · 2026-01-25 · [link](https://t.me/aistockanalyst/1072)</sub>

---

### 6. `MS-003` · `B` · unknown · phone_technical · 2026

what if F test give you value 50, how would you interpret it?

**Answer:** F = 50 means the mean square attributable to the model (or to the restriction being tested) is 50 times the residual mean square per degree of freedom. Under H0 an F statistic is centred near 1 (its mean is d2/(d2-2)), so 50 is far into the right tail: with F(1,100) the p-value is 2e-10, with F(3,100) it is 8e-20, with F(5,30) 1e-13, and even with the very small F(10,10) it is 3e-7. Conclusion: reject the null emphatically. But three caveats I would state in the same breath: (i) F says nothing about effect size — the overall F is (R^2/k) / ((1-R^2)/(n-k-1)), so with n = 2500 and one regressor an R^2 of just 2% already gives F = 51. A huge F on a large sample is perfectly consistent with an economically trivial relationship. (ii) An F this large is more often a sign of a broken assumption than of a real effect: heteroskedasticity, autocorrelated or overlapping observations (which inflate the effective sample size), a look-ahead leak, a duplicated regressor, or one outlier. I would look at the residuals and re-run with HAC/robust standard errors before celebrating. (iii) You cannot quote a p-value at all without both degrees of freedom.

*Working:* What is tested: do you know what an F statistic is a ratio of, do you know it is centred near 1 under the null rather than near 0, can you say something about magnitude without a table, and — the real point for a quant role — do you distinguish statistical from economic significance. The p-values above are computed from the exact relation P(F_{d1,d2} > f) = I_x(d2/2, d1/2) with x = d2/(d2 + d1 f).

*Assumption:* The question does not give the degrees of freedom or say which F-test it is (overall regression F, a nested-model restriction test, or a two-sample variance ratio), so I give p-values across a range of plausible df and note that the df are required.

> ⚠️ **The candidate's reported answer is wrong.** source is partly wrong: the conclusion 'reject the null' is right, but the stated reason is not. The F distribution is right-skewed, yet under H0 it is centred near 1 (mean d2/(d2-2)), not 'always close to zero' — for example the 95th percentile of F(3,100) is 2.70. And no p-value can be quoted without the two degrees of freedom. The answer also misses the key point that an F of 50 says nothing about effect size.

<sub>numerically verified — `CHECK table_err=3.16e-05 p(F=50) (1, 100):2.12e-10; (3, 100):7.94e-20; (5, 30):1.18e-13; (10, 10):3.42e-07 | R2=2%,n=2500,k=1 -> F=51.0 vs err<1e-3, a`</sub>

<sub>Source: chat_telegram · 2026-01-25 · [link](https://t.me/aistockanalyst/1072)</sub>

---

### 7. `MS-007` · `B` · unknown · phone_technical · 2026

What if your have large variable but small sample?

**Answer:** Model answer. First name the problem: with p > n, X'X is singular, OLS has infinitely many solutions that all fit perfectly in sample, in-sample R^2 = 1, and out-of-sample performance is noise. Anything unpenalised will overfit. Then the menu, roughly in the order I would offer it: 1) Regularise — the answer the question is fishing for. Ridge (defined for any p, keeps all variables, best when there are many small correlated effects, which is the usual situation in finance), lasso (sparsity and selection, but unstable across correlated predictors and cannot select more than n), elastic net as the compromise. Choose lambda by cross-validation — walk-forward CV, not random k-fold, if it is time series. 2) Reduce the dimension: PCA/principal-components regression (unsupervised, so the top components need not be the ones that predict y), PLS (supervised), or a factor model. This is a fine answer and is what the candidate gave. 3) Say the Bayesian version, because it unifies the above: ridge is a Gaussian prior, lasso a Laplace prior; if you genuinely believe in sparsity use spike-and-slab or the horseshoe. With small n, being explicit about your prior is the honest move. 4) Screening: univariate t/F screening (sure independence screening) is a legitimate first pass, but it must be re-run inside every CV fold or it leaks, and it needs multiplicity control (Benjamini-Hochberg for FDR) or you will select pure noise. 5) Increase n instead of shrinking p: pool cross-sectionally with shared coefficients (panel regression), go to higher frequency, or use a hierarchical model that shrinks each asset toward a common mean. 6) If the estimand is a covariance matrix rather than a regression, the analogue is Ledoit-Wolf shrinkage or imposing a factor structure. 7) The meta-point that impresses: with p >> n, cross-validation itself overfits once you have tried enough models. Keep a final untouched holdout, prefer simple or equal-weighted signal combinations, and let economics rather than the data do most of the variable selection.

*Working:* What is tested: do you recognise the singularity of X'X immediately, do you know the bias-variance rationale for shrinkage, and can you name more than one family of solutions when pushed. The push for 'another method' after PCA is a hint that they wanted to hear regularisation. No verify_code, because the question asks for a menu of modelling approaches rather than a computable quantity.

> ⚠️ **The candidate's reported answer is wrong.** source is incomplete rather than wrong. PCA is a legitimate answer; univariate F-test screening is genuinely used (sure independence screening) but needs FDR control and must sit inside the CV loop, neither of which was mentioned. The canonical expected answer — ridge/lasso/elastic net regularisation — was missing, which is almost certainly why the interviewer pushed.

<sub>guidance, no single correct value</sub>

<sub>Source: chat_telegram · 2026-01-25 · [link](https://t.me/aistockanalyst/1072)</sub>

---

### 8. `MS-010` · `B` · unknown · phone_technical · 2026

Assume our input data has one part is normally distribute at zero (can be positive & negative) and the other part is strictly positive to very large number, what would you do before input it to our model ?

**Answer:** Transform the two blocks differently, because their problem is different: the symmetric block only needs scaling, while the strictly positive block needs its shape fixed before scaling. - Symmetric block (can be either sign, centred at zero): winsorise or clip at about +/-4 standard deviations (or use median and MAD if it is dirty), then z-score. Nothing else needed. - Strictly positive, heavy-tailed block (this looks like volume, notional, market cap or realised vol): take logs first — log(x), or log1p(x) if zeros occur — then z-score. The log is what compresses the tail and makes the variable roughly symmetric; the scaling afterwards is cosmetic. Box-Cox / Yeo-Johnson if you want the exponent fitted. - If you want one transform for both blocks, use the inverse hyperbolic sine, asinh(x/lambda) = log(x/lambda + sqrt(1 + (x/lambda)^2)): linear near zero, logarithmic in the tails, and it handles negatives and zeros, so it can be applied uniformly. - The bulletproof alternative for cross-sectional finance features is a rank / Gaussian-rank transform: rank within each cross-section, map to uniform, then apply the inverse normal CDF. It annihilates outliers and puts both blocks on the same footing, at the cost of throwing away cardinal information. - Two things to say unprompted: (1) fit every transform on a rolling or expanding window using past data only, otherwise the normalisation itself leaks the future into a backtest; (2) it depends on the model — trees only see the ordering so monotone transforms are irrelevant to them, but they matter a lot for regularised linear models, neural nets, k-NN and PCA, where the penalty and the distance metric are scale-dependent.

*Working:* What is tested: do you distinguish rescaling (changes units) from reshaping (changes the distribution), and do you know that a heavy right tail is the actual problem here. The verify_code makes the point concretely: for a lognormal feature, dividing by the sample maximum leaves 99.65% of the mass below 0.01 and the 99th percentile at 0.004 — the feature is now a column of near-zeros plus a couple of spikes — whereas log then z-score gives a well-spread variable with 1st and 99th percentiles near -2.3 and +2.3.

> ⚠️ **The candidate's reported answer is wrong.** source is inadequate rather than flatly wrong: 'divide each value by the max' does bound the range, but it is a pure rescaling that leaves the heavy right tail intact, so almost all the mass collapses toward zero and one observation dominates the feature. Worse, the maximum is itself an extreme order statistic — it is unstable, it is unbounded out of sample (new data exceeds it and breaks the [0,1] range), and in a backtest the full-sample max is a look-ahead leak. The interviewer's 'hmm yeah kinda' reads as exactly that: right instinct on scaling, wrong tool for the tail. The expected answer is a log/asinh (or rank-Gaussian) transform.

<sub>numerically verified — `CHECK divide-by-max: 99.6530% of mass below 0.01, p99=0.0040 | log+z: p1=-2.33 p99=2.32 vs divide-by-max leaves the tail (>99% squashed near 0), log+z`</sub>

<sub>Source: chat_telegram · 2026-01-25 · [link](https://t.me/aistockanalyst/1072)</sub>

---

### 9. `MS-004` · `B` · unknown · phone_technical · 2026

Given time series data, what would you do for missing value ?

**Answer:** Model answer, in the order I would say it: 1) Ask why it is missing before deciding how to fill it. MCAR / MAR / MNAR matters, and in financial time series missingness is usually informative: a trading halt, a holiday or half day, an illiquid name with no print, a vendor outage, an IPO or delisting, a fundamental not yet reported. 'No trade' is not the same as 'no data', and the missingness indicator is often itself a useful feature. 2) Fix the index first. Align to an explicit trading calendar so weekends, holidays and different market hours do not masquerade as gaps. 3) The binding constraint is causality. In a backtest you may only use information available at that timestamp. Forward-fill (last observation carried forward) is causal and is the sane default for levels. Linear interpolation, splines, and mean/median imputation computed over the whole sample are look-ahead leaks and will flatter your backtest — this is the answer the interviewer is listening for. 4) Then it depends on the field: prices/levels -> forward-fill with a staleness cap, plus a 'periods since last update' feature, and drop or mask beyond the cap; returns -> 0 if the fill implies no move, or drop; volume -> 0 is often literally correct; fundamentals -> point-in-time carry-forward with the correct reporting lag. 5) For panel data, impute cross-sectionally (sector or size-bucket median, or a factor model's fitted value) rather than from the asset's own stale history. 6) Model-based options when it matters: a state-space/Kalman filter handles missing observations natively (skip the update step), EM for the parameters, and multiple imputation if you need the imputation uncertainty to show up in your standard errors. Or do not impute at all — gradient-boosted trees learn a default direction for NaNs, and you can mask missing targets out of the loss. 7) Finally, report the fraction imputed and show the conclusion is not an artefact by re-running under two or three fill schemes.

*Working:* What is tested: awareness that imputation can leak the future (the number one sin in backtesting), that missingness in market data is usually not random, and that different fields need different treatment. A weak answer is a single sentence naming 'interpolate' or 'fill with the mean'. No verify_code, because this is a data-handling judgement question with no computable answer.

<sub>guidance, no single correct value</sub>

<sub>Source: chat_telegram · 2026-01-25 · [link](https://t.me/aistockanalyst/1072)</sub>

---

### 10. `MS-009` · `B` · unknown · phone_technical · 2026

Which would you choose to estimate your time series model? R squared, MSE, RMSE, MAE?

**Answer:** The sharp observation first: on a fixed sample, three of the four are the same metric. RMSE is a monotone transform of MSE, and R^2 = 1 - MSE/Var(y) is also a monotone (decreasing) transform of MSE, so R^2, MSE and RMSE rank competing models identically. Only MAE can produce a different ranking. So the real question is (a) squared versus absolute loss and (b) how you want the number scaled. - Squared loss (MSE/RMSE) targets the conditional mean and punishes large errors quadratically. That is the right loss if your P&L or risk is quadratic in the error, but financial data is fat-tailed and a handful of crisis days will dominate the metric. - MAE targets the conditional median and is far more robust to those outliers; Huber is the sensible middle. If you care about robustness to fat tails, MAE. - RMSE is in the units of y, so it is the interpretable one to report. R^2 is unit-free and so comparable across series. - The trap with R^2 in time series: it is inflated by trends and nonstationarity (a random walk 'predicted' by its own lag gives R^2 near 1 and tells you nothing), and it is not comparable across different transformations of y, so a model on levels and a model on differences cannot be ranked by R^2. What I would actually do: none of the four in-sample. Evaluate out of sample with walk-forward / expanding-window validation and report (i) out-of-sample R^2 relative to a naive benchmark — equivalently MASE, which scales the error by the random-walk forecast, (ii) RMSE for units, and (iii) for a return forecast, the metrics that actually correspond to being paid: information coefficient (rank correlation of forecast with realised), hit rate, and the Sharpe/P&L of the strategy the forecast implies, which weights each error by the position it caused. In a return-prediction setting an out-of-sample R^2 of 0.5-2% is a good model, so a metric that cannot resolve that difference from zero is useless. For choosing between nested models on the same data, AIC/BIC rather than raw fit.

*Working:* What is tested: whether you realise the four options are not four independent choices, whether you know R^2 misleads on time series, and whether you push the conversation to out-of-sample evaluation and to a loss function tied to the P&L. The monotone-equivalence claim is checked numerically in verify_code: across 200 random linear models on one fixed sample, the MSE, RMSE and R^2 rankings are identical while the MAE ranking differs.

*Assumption:* 'Estimate your time series model' is read as 'evaluate/select', since none of the four is an estimator. Note that minimising MSE is also the estimation criterion (OLS), in which case the answer is that the loss you fit should match the loss you are scored on.

<sub>numerically verified — `CHECK mse==rmse:True mse==r2:True mse==mae:False vs True True False`</sub>

<sub>Source: chat_telegram · 2026-01-25 · [link](https://t.me/aistockanalyst/1072)</sub>

---


## Optiver  (10)

### 1. `OPT-014` · `B` · unknown · online_assessment · unknown

15/25 / ? = 14/35 A) 3/5 B) 63/30 C) 14/15 D) 9/6

**Answer:** D) 9/6 (= 3/2)

*Working:* 15/25 = 3/5 and 14/35 = 2/5, so the missing divisor is (3/5)/(2/5) = 3/2. Among the options, 9/6 = 3/2, so D. (A = 3/5, B = 21/10, C = 14/15 are all wrong.)

<sub>numerically verified — `CHECK ('3/2', ['D']) vs ('3/2', ['D'])`</sub>

<sub>Source: wso · 2013-09-28 · [link](https://www.wallstreetoasis.com/forum/trading/optiver-trading-numerical-test)</sub>

---

### 2. `OPT-017` · `B` · unknown · unknown · unknown

You have a dartboard, circumscribed within a square. The square's dimensions are 10"x10". The circle is split into 20 equal sections, and each is marked with a number alternating from the low end to the high end of interval [1,20], so 1, 20, 2, 19, 3, etc. Also, inside the center of the dartboard, is another circle 1" in diameter. This is marked 50. So you have 21 sections with numbers in them, these are your point values (payoff in dollars), and the area outside the circle but in the square is worth 0. -What's the EV of the game? -What's the optimal strategy? -If I let you rethrow your first throw at the cost of $1, will you take it? What if you have 2 rethrows?

**Answer:** EV of a random throw = 2179*pi/800 ~= $8.5569. Optimal strategy: aim at the bullseye (the centre). Yes, take the $1 re-throw - it raises the EV to ~$11.1466, and you exercise it whenever the first dart scores 7 or less. Take the second one too: EV ~= $12.5409, re-throwing while the score is 10 or less, then while it is 7 or less.

*Working:* Areas (square = 100 sq in): bull = pi(0.5)^2 = 0.25pi; the 20 numbered sectors share the annulus 25pi - 0.25pi = 24.75pi, so each has area 1.2375pi; outside the circle = 100 - 25pi. EV = [210*(1.2375pi) + 50*(0.25pi)]/100 = 272.375pi/100 = 2179pi/800 ~= 8.5569 (the numbering pattern is irrelevant to the EV, only the value set matters). Re-throw options are optimal-stopping: T1 = E[max(X, T0 - 1)]. With T0 - 1 = 7.5569 you keep 8 and above, giving T1 = 9509pi/4000 + (1 - 1307pi/8000)(2179pi/800 - 1) ~= 11.1466, so the first option is worth ~ +$2.59. Then T2 = E[max(X, T1 - 1)] with threshold 10.1466 = keep 11 and above, giving T2 = 16345pi/8000 + (1 - 101pi/800)(T1 - 1) ~= 12.5409, worth a further ~ +$1.39. On strategy: the alternating 1,20,2,19,... layout is designed so that every neighbourhood out in the annulus averages ~10.5 (adjacent sectors sum to 21 or 22), so no aim point in the ring carries an edge; the centre is the only place with one, worth 50, and aiming there also keeps you off the zero-scoring corners.

*Assumption:* The dart lands uniformly at random over the 10x10 square (an unskilled thrower) and always lands inside it - this is what makes 'the EV of the game' well posed. The circle is inscribed in the square (radius 5). Whether the 20 sectors are drawn as full sectors overlaid by the bull or as annulus sectors makes no difference, since the centred bull removes exactly 1/20 of its area from each. The re-throw answers assume the same uniform throw; a thrower who can actually aim at the bull would decline the re-throws at very different thresholds.

<sub>numerically verified — `CHECK ('exact', 8.5569, 11.1466, 12.5409, '2179pi/800', 8.556913, 'mc', 8.55, 11.138, 12.53) vs ('claimed', 8.5569, 11.1466, 12.5409, '2179pi/800', 8.` · confidence: **medium**</sub>

<sub>Source: wso · 2013-09-28 · [link](https://www.wallstreetoasis.com/forum/trading/optiver-trading-numerical-test)</sub>

---

### 3. `OPT-003` · `C` · internship · online_assessment · 2026

You flip a coin 3 times. What is the probability that the outcome is the same for all flips? all Heads or all Tails.

**Answer:** 1/4 = 0.25

*Working:* 8 equally likely sequences; 2 of them (HHH, TTT) are constant, so 2/8 = 1/4. Equivalently: flips 2 and 3 must each match flip 1, giving (1/2)^2.

*Assumption:* Fair coin, independent flips.

<sub>numerically verified — `CHECK (2, 8, '1/4') vs (2, 8, '1/4')`</sub>

<sub>Source: other · 2025-08-04 · [link](https://www.1point3acres.com/bbs/thread-1141422-1-1.html)</sub>

---

### 4. `OPT-005` · `C` · internship · online_assessment · 2026

You throw one dice two times. What is the probability that the 2nd throw has a different face value than the first throw?

**Answer:** 5/6 ~= 0.8333

*Working:* Whatever the first throw shows, exactly 5 of the 6 equally likely faces on the second throw differ from it, so the probability is 5/6 (30 of the 36 ordered pairs).

*Assumption:* Fair 6-sided die, independent throws.

<sub>numerically verified — `CHECK (30, 36, '5/6') vs (30, 36, '5/6')`</sub>

<sub>Source: other · 2025-08-04 · [link](https://www.1point3acres.com/bbs/thread-1141422-1-1.html)</sub>

---

### 5. `OPT-011` · `C` · internship · online_assessment · 2026

ss. Once you have won a toss, your strategy has been implemented, and you stop. If you have a total bankroll of $63 available to implement this strategy, what is your expected profit?

**Answer:** $0 - the expected profit is exactly zero.

*Working:* $63 = 1 + 2 + 4 + 8 + 16 + 32 funds exactly six bets in the doubling (martingale) sequence. You win $1 net if a head arrives within those six tosses, which happens with probability 1 - (1/2)^6 = 63/64; otherwise you have lost all six and are down $63, with probability 1/64. E[profit] = (63/64)(+1) + (1/64)(-63) = 0. That is the point of the question: doubling up converts the payoff into 'small frequent win, rare large loss' but cannot change the expectation of a fair game, and the bankroll cap is what stops the martingale from being a money machine.

*Assumption:* The question text is truncated. Reconstructed as the standard version: a fair coin, an initial $1 bet, doubling the stake after each loss, stopping at the first win. If the coin were biased the answer would change (with win probability p the expected profit is (1-(1-p)^6)*1 - (1-p)^6*63, which is 0 only at p = 1/2).

<sub>numerically verified — `CHECK ('0', {-63: '1/64', 1: '63/64'}) vs ('0', {-63: '1/64', 1: '63/64'})` · confidence: **medium**</sub>

<sub>Source: other · 2025-08-04 · [link](https://www.1point3acres.com/bbs/thread-1141422-1-1.html)</sub>

---

### 6. `OPT-006` · `C` · internship · online_assessment · 2026

You will play a coin game against an opponent. A biased coin will be continually flipped where there is a 2/3 chance of Heads and a 1/3 chance of Tails. If Heads is flipped then you receive $1 from your opponent. If Tails is flipped then you pay $1 to your opponent. You start with $10 and your opponent starts with $20. You keep playing until one of you is bankrupt (= has $0 left); they will be declared the loser, the other will be declared the winner. What is the probability that you win?

**Answer:** 1048576/1049601 = 2^20/(2^20 + 2^10 + 1) ~= 0.9990234

*Working:* Gambler's ruin with p = 2/3, q = 1/3, so r = q/p = 1/2. Starting at i = 10 with an absorbing barrier at N = 30, P(win) = (1 - r^i)/(1 - r^N) = (1 - 2^-10)/(1 - 2^-30) = (1023/1024) * 2^30/(2^30 - 1). Since 2^30 - 1 = (2^10 - 1)(2^20 + 2^10 + 1), the 1023 cancels and this collapses to 2^20/(2^20 + 2^10 + 1) = 1048576/1049601 ~= 0.999023.

*Assumption:* $1 stakes each toss, play continues until someone is at $0, total stake $30 fixed.

<sub>numerically verified — `CHECK ('1048576/1049601', 0.999023438, 0.999023438) vs ('1048576/1049601', 0.999023438, 0.999023438)`</sub>

<sub>Source: other · 2025-08-04 · [link](https://www.1point3acres.com/bbs/thread-1141422-1-1.html)</sub>

---

### 7. `OPT-012` · `C` · internship · trading_game · unknown

You are given a question, such as “How much money was spent in pubs in the UK, on the first day after the COVID lockdown?”

**Answer:** No single number is being marked - they want a structured Fermi estimate turned into a two-way price you are willing to trade on both sides of, then defended and updated as they trade against you. For the pub example my estimate is roughly 1.5 x 10^8 pounds, so I would quote about 130 / 170 (millions of pounds) and adjust from there.

*Working:* Worked estimate, top-down: UK pub trade is roughly 45,000-50,000 pubs turning over ~ GBP 23bn a year, i.e. ~ GBP 63m on an average day; a Saturday runs perhaps 2-2.5x an average day, so a normal Saturday is ~ GBP 130-160m. Reopening Saturday (4 July 2020, England only) pushes two ways: pent-up demand and long queues, against only about half of pubs actually opening, table service and distancing cutting capacity, and Scotland/Wales/NI still shut. Net: about a normal Saturday. Bottom-up cross-check: ~6-8m adults out (of ~53m) spending ~ GBP 25 each = GBP 150-200m. Both routes land on hundreds of millions, so 10^8 is the defensible order of magnitude and ~ GBP 150m the central estimate. How to play the round: (1) say the estimate out loud with its decomposition so they can see the model; (2) quote a width that reflects your uncertainty, not a token 1% - here maybe +/- 20-25%; (3) never trade through your own fair value, and shade the quote toward the side they keep hitting, because their aggression is information; (4) size down as your uncertainty rises and be willing to move the market rather than defend a stale price; (5) when they hand you a new fact ('half the pubs stayed shut'), re-derive publicly and re-quote. They are marking the process - decomposition, arithmetic under pressure, sensible width, and updating on flow - not the accuracy of the number.

*Assumption:* Read as the Optiver estimation/market-making game; the pub figure is my own order-of-magnitude estimate, not a published statistic.

<sub>guidance, no single correct value · confidence: **medium**</sub>

<sub>Source: blog · unknown · [link](https://www.canarywharfian.co.uk/companies/53/optiver/interviews)</sub>

---

### 8. `OPT-004` · `C` · internship · unknown · unknown

How long would it take you to do 2/17 in your head (to 3 decimal places)?

**Answer:** 2/17 = 0.117647058823... -> 0.118 to three decimal places.

*Working:* The trick worth knowing: 1/17 = 0.0588235294117647... so 2/17 is just double it. Faster in the room: 17 * 0.118 = 2.006, so 2/17 is a shade under 0.118, and 17*0.1176 = 1.9992 pins it at 0.11765 -> 0.118. Another quick route: 2/17 = 12/102 ~= 12/100 * (100/102) = 0.12 * 0.98039 = 0.11765. A few seconds is the expected answer time.

<sub>numerically verified — `CHECK ('0.117647058823', 0.118) vs ('0.117647058823', 0.118)`</sub>

<sub>Source: blog · unknown · [link](https://www.canarywharfian.co.uk/companies/53/optiver/interviews)</sub>

---

### 9. `OPT-002` · `C` · internship · unknown · unknown

Today is a Wednesday, what will be the day of the week on this date next year?

**Answer:** Thursday - unless a 29 February falls in the intervening twelve months, in which case Friday.

*Working:* 365 = 52*7 + 1, so the same date one year later normally advances the weekday by exactly one day: Wednesday -> Thursday. If the span contains a leap day it is 366 days = 52*7 + 2 and the answer is Friday. Over 1901-2100 that happens for about 24.5% of dates, so 'Thursday' is right roughly three times in four; the complete answer names the leap-year exception.

*Assumption:* Gregorian calendar; 'this date next year' means the same month and day one calendar year later.

<sub>numerically verified — `CHECK (0, ['Friday', 'Thursday'], 0.755) vs (0, ['Friday', 'Thursday'], '~3/4 Thursday')`</sub>

<sub>Source: blog · unknown · [link](https://www.canarywharfian.co.uk/companies/53/optiver/interviews)</sub>

---

### 10. `OPT-008` · `C` · internship · unknown · unknown

Simpson’s Paradox question: Was given various pieces of information on two football teams, playing two halves of a game, and they individually have a “pass ratio” for each half. It was asked that if Team X has a higher pass ratio than Team Y in the first half, and the same again in the second half, could Team Y have a higher pass ratio overall? I was then asked to give a numerical example.

**Answer:** Yes - this is Simpson's paradox. Example: Team X completes 9/10 (90%) in the first half and 20/100 (20%) in the second; Team Y completes 85/100 (85%) in the first and 1/10 (10%) in the second. X is higher in both halves, yet overall X is 29/110 ~= 26.4% against Y's 86/110 = 43/55 ~= 78.2%.

*Working:* An overall ratio is an attempt-weighted average of the two half ratios, not a plain average. If the team with the lower rate in each half throws most of its passes in the half where both teams' rates are high, and its rival throws most of its passes in the low-rate half, the weights can reverse the ordering. The reversal requires the attempt mixes to differ across halves - with equal attempt counts in both halves for both teams it is impossible.

*Assumption:* 'Pass ratio' = completions / attempts, and the overall ratio is total completions / total attempts (not the average of the two half ratios). If the overall figure were defined as the unweighted mean of the two halves, no reversal is possible.

<sub>numerically verified — `CHECK (True, '29/110', '43/55', 0.2636, 0.7818) vs (True, '29/110', '43/55', 0.2636, 0.7818)`</sub>

<sub>Source: blog · unknown · [link](https://www.canarywharfian.co.uk/companies/53/optiver/interviews)</sub>

---


## Jump Trading  (9)

### 1. `JUMP-002` · `B` · unknown · onsite · unknown

I'm dealing a deck of poker, you can stop me anytime. If the next card is red, you win. Otherwise you lose. What's optimal strategy and the probability of winning ?

**Answer:** 1/2, and every strategy achieves exactly 1/2 — there is nothing to optimise.

*Working:* Let V(r, b) be the best win probability with r red and b black left. Stopping now wins with probability r/(r+b). Claim V(r, b) = r/(r+b) by induction: continuing gives (r/(r+b))·V(r−1, b) + (b/(r+b))·V(r, b−1) = (r/(r+b))·(r−1)/(r+b−1) + (b/(r+b))·r/(r+b−1) = r/(r+b), identical to stopping. So the fraction of red remaining is a martingale and no stopping rule beats the trivial one. Starting from 26/52 the answer is 1/2. The clean way to say it in an interview: 'bet on the last card' is a legal strategy, and it wins with probability exactly 1/2 because the last card is equally likely to be either colour no matter what you have seen; the induction above then shows no adaptive rule can beat it.

*Assumption:* Standard 52-card deck, 26 red and 26 black, dealt in uniformly random order; you must bet at some point (equivalently, if you never stop you are betting on the last card).

<sub>numerically verified — `CHECK (V(26,26)=1/2, V(r,b)==r/(r+b) everywhere: True) vs (1/2, True)`</sub>

<sub>Source: wso · 2018-12-24 · [link](https://www.wallstreetoasis.com/company/jump-trading/interview)</sub>

---

### 2. `JUMP-017` · `B` · internship · onsite · unknown

a math problem about the probability an array is sorted after swapping the first two if they're out of order, swapping the new second and third if they're out of order, and so on until swapping the last two if they're out of order

**Answer:** 2^(n−1)/n! for a uniformly random permutation of n distinct elements — e.g. 1 for n = 2, 2/3 for n = 3, 1/3 for n = 4, 2/15 for n = 5, 2/45 for n = 6 and 4/315 for n = 7.

*Working:* The described procedure is exactly one pass of bubble sort. It carries a running maximum: after the pass, position i holds min(max(a_1..a_i), a_(i+1)), and the last position holds the overall maximum. A permutation is sorted by one pass if and only if no element has two larger elements anywhere before it (i.e. it avoids the patterns 231 and 321) — one larger element before you can be carried past you, two cannot. They are counted by 2^(n−1) via a clean bijection with compositions of n: cut 1..n into consecutive blocks (2^(n−1) ways, one binary choice per gap) and rotate each block by moving its largest element to the block's front — e.g. for n = 4 the composition (1,3) gives 1 4 2 3. Dividing by n! gives the probability. Brute force for n = 1..8 confirms the count, the pattern characterisation and the bijection.

*Assumption:* The array is a uniformly random permutation of n distinct values, and the recollection describes a single left-to-right pass of adjacent compare-and-swap (the question does not state n, so the answer is given for general n).

<sub>numerically verified — `CHECK (counts n=1..8: [1, 2, 4, 8, 16, 32, 64, 128] == 2^(n-1): True, pattern characterisation: True, composition bijection: True, P for n=3..7: ['2/3`</sub>

<sub>Source: wso · 2018-12-22 · [link](https://www.wallstreetoasis.com/company/jump-trading/interview)</sub>

---

### 3. `JUMP-001` · `B` · unknown · phone_technical · unknown

1)Can you create a linked list? Do it. 2) Let's say we want to change places of 2 nodes in linked list. Can you create a function for that.

**Answer:** Working code, verified below against brute force for every list length up to 6 and 2000 random cases: class Node: def __init__(self, val, nxt=None): self.val, self.next = val, nxt class LinkedList: def __init__(self, vals=()): self.head = tail = None for v in vals: n = Node(v) if tail is None: self.head = tail = n else: tail.next = n; tail = n def swap(self, x, y): if x == y: return prev_x = prev_y = cur_x = cur_y = None prev, cur = None, self.head while cur: if cur.val == x and cur_x is None: prev_x, cur_x = prev, cur elif cur.val == y and cur_y is None: prev_y, cur_y = prev, cur prev, cur = cur, cur.next if cur_x is None or cur_y is None: return if prev_x: prev_x.next = cur_y else: self.head = cur_y if prev_y: prev_y.next = cur_x else: self.head = cur_x cur_x.next, cur_y.next = cur_y.next, cur_x.next The swap relinks nodes rather than copying payloads — that is the whole point of the question. One pass finds each target and its predecessor; then each predecessor (or the head, if a target is first) is repointed at the other node and the two next pointers are exchanged. Written in that order, the adjacent-node case — where one node's predecessor IS the other node — falls out correctly with no special-casing. O(n) time, O(1) extra space.

*Working:* What they are checking: pointer discipline and edge cases, not syntax. Say the edge cases out loud before coding — empty list, one element, target absent, the two targets equal, either target at the head, and the two nodes adjacent (the classic bug). Also ask whether you may swap the values instead of the nodes: that is a two-line answer, and the fact that they asked for nodes means they want the relinking. If asked to extend: a doubly linked list needs the prev pointers fixed too, and a dummy head node removes the head special case.

*Assumption:* Singly linked list, swap by node identity/first occurrence of a value; the question does not specify the language, so Python is used.

<sub>numerically verified — `CHECK (all swaps correct incl. adjacent/head/tail/self: True) vs (True)`</sub>

<sub>Source: wso · 2023-10-03 · [link](https://www.wallstreetoasis.com/company/jump-trading/interview)</sub>

---

### 4. `JUMP-022` · `B` · unknown · phone_technical · unknown

Suppose you sit on the road side and observe cars driving by. Assume the distribution of cars driving by is according to an exponential distribution. Now you observe a first car after sitting for x mins, a second car after sitting for y min. Given those observations, can you estimate the parameter in the distribution?

**Answer:** MLE lambda-hat = 2/y, where y is the total elapsed time to the second car (equivalently 2/(t1+t2) with gaps t1 = x and t2 = y − x). If instead y denotes the gap AFTER the first car, it is 2/(x+y). This estimator is biased (E[lambda-hat] = 2·lambda); the unbiased estimator is 1/y, i.e. (n−1)/(sum of gaps) with n = 2 observations.

*Working:* Cars arriving as a Poisson process means the gaps are iid Exponential(lambda), and by memorylessness the wait from your arrival to the first car is also Exponential(lambda). Log-likelihood l(lambda) = 2·ln(lambda) − lambda·(t1+t2); setting l' = 0 gives lambda-hat = 2/(t1+t2) = 2/y, i.e. simply (number of arrivals)/(total time observed), which is the general Poisson-process MLE. Since t1+t2 ~ Gamma(2, lambda) and E[1/Gamma(k,lambda)] = lambda/(k−1), the MLE has expectation 2·lambda — wildly biased with only two observations — so 1/y is the unbiased choice, and it is worth saying that two data points give a very wide interval: since lambda·y ~ Gamma(2,1), an exact 95% CI is [0.242/y, 5.572/y] — a factor of 23 from end to end.

*Assumption:* Arrivals form a Poisson process (exponential gaps) with unknown rate lambda; you start observing at a time unrelated to the process, so the first wait is also Exponential(lambda). The wording 'after sitting for y min' is read as total elapsed time from when you sat down; the alternative reading is given.

<sub>numerically verified — `CHECK (numeric argmax=0.181818, closed form 2/y=0.181818, E[MLE]=1.3966, E[1/y]=0.6983, 95% CI = [0.242/y, 5.572/y]) vs (2/(t1+t2)=0.181818, same, 2*l` · confidence: **medium**</sub>

<sub>Source: wso · 2018-02-15 · [link](https://www.wallstreetoasis.com/company/jump-trading/interview)</sub>

---

### 5. `JUMP-016` · `B` · unknown · phone_technical · unknown

Suppose you backtested a trading strategy, it did very well. But in live trading, you keep losing money, what would you do?

**Answer:** Model answer. First ask whether the live result is even inconsistent with the backtest: take the backtest's distribution of P&L over windows of the same length and see where the live run sits. If it is within noise the answer is 'size down and keep collecting data', and saying so is a point in your favour. If it is genuinely inconsistent, work the list in order of prior probability: (1) look-ahead and survivorship bias — restated data, point-in-time universe, signals timestamped after the decision, trading the close on the close; (2) overfitting — how many variants were tried, does the Sharpe survive a multiple-testing haircut, does it hold across sub-periods and instruments; (3) costs — backtests fill at mid, live you cross the spread, sit in a queue and move the price, so check turnover × realistic cost against gross alpha; (4) execution and plumbing — latency, fill rates, rejects, partial fills, sign errors, timezone bugs; (5) capacity and crowding, including your own impact and alpha decay; (6) regime change; (7) a research/live data mismatch. The single most diagnostic step: replay the actual live signal values through the backtester and reconcile trade by trade. If the paper P&L of the live signals matches the backtest but the real P&L does not, it is execution and costs; if the paper P&L is also bad, it is the signal or the data. Meanwhile cut size rather than switching off blind, and set a pre-agreed kill level in advance.

*Working:* This is a judgement question about research hygiene. The strong answer is structured (is it noise? then a ranked list of causes), names the one experiment that discriminates fastest, and ends with a risk decision rather than a diagnosis alone.

<sub>guidance, no single correct value</sub>

<sub>Source: wso · 2018-02-15 · [link](https://www.wallstreetoasis.com/company/jump-trading/interview)</sub>

---

### 6. `JUMP-008` · `B` · unknown · phone_technical · unknown

What are ensemble methods? Can you describe boosted tree methods?

**Answer:** Model answer. Ensembles combine many imperfect models so that their errors partly cancel; the two families do different jobs. Bagging/random forests attack VARIANCE: fit deep trees in parallel on bootstrap resamples (random forests also sample features at each split to decorrelate the trees) and average — averaging B models with pairwise correlation rho leaves rho·sigma^2 + (1−rho)·sigma^2/B, so decorrelation is the whole game. Boosting attacks BIAS: fit models sequentially, each on what the current ensemble still gets wrong. Gradient boosting concretely: start with a constant F_0, then at each round compute the negative gradient of the loss with respect to the current predictions (for squared loss these are just the residuals), fit a shallow regression tree to it, and update F_m = F_(m−1) + nu·h_m with a small learning rate nu. AdaBoost is the special case with exponential loss and reweighted examples. XGBoost/LightGBM add a second-order Newton step, L1/L2 penalties on leaf weights, row/column subsampling and histogram split finding. Key trade-off: more trees never really hurt a forest but will overfit a booster, so you early-stop on validation and trade learning rate against number of rounds. Mention stacking as the third family. For a trading firm, add the domain point: with signal-to-noise this low you use shallow trees, strong regularisation, tiny learning rates, and purged/embargoed time-series cross-validation — random k-fold leaks the future and will flatter any boosted model badly.

*Working:* They want to see that you know why averaging helps (variance) versus why sequential fitting helps (bias), can state the gradient-boosting update precisely, and know the practical failure mode — overfitting and leaky cross-validation on time series.

<sub>guidance, no single correct value</sub>

<sub>Source: wso · 2018-02-15 · [link](https://www.wallstreetoasis.com/company/jump-trading/interview)</sub>

---

### 7. `JUMP-024` · `C` · unknown · unknown · unknown

A bee starts at a hive. It has a 20% chance to move forward, a 50% chance to stay still, and a 30% to move backward. What percentage of the time does it spend in the hive?

**Answer:** 1/3, i.e. about 33.3% of the time.

*Working:* Model the bee's distance from the hive as a birth–death chain on {0, 1, 2, ...}: from any position it moves out with p = 0.2, stays with 0.5, comes back with q = 0.3, and at the hive itself a backward move is blocked so it just stays. Detailed balance gives pi_(k+1)/pi_k = p/q = 2/3, so pi_k = pi_0·(2/3)^k and summing the geometric series gives pi_0 = 1 − p/q = 1/3. Note the 50% 'stay still' probability is irrelevant — it slows the chain down but does not change where it spends its time, which is a nice thing to point out. The answer is sensitive to the boundary rule, and this is the genuine ambiguity in the question: if a backward move at the hive instead reflects the bee out to position 1, pi_0 = 1/6; and if the bee lives on the whole line with no barrier the walk drifts away for ever and the long-run fraction is 0. The 1/3 reading (a barrier at the hive) is the one that gives a sensible answer and is almost certainly intended.

*Assumption:* One-dimensional walk with the hive as an absorbing-free reflecting/blocking boundary at 0 (the bee cannot go behind the hive); 'percentage of time' means the long-run stationary fraction.

<sub>numerically verified — `CHECK (blocking: exact=1/3=0.33333, truncated=0.33333, MC=0.33262; reflecting variant=0.16667) vs (1/3=0.33333, 1/3, 1/3, 1/6=0.16667)` · confidence: **medium**</sub>

<sub>Source: blog · unknown · [link](https://www.efinancialcareers-canada.com/news/electronic-trading-interviews)</sub>

---

### 8. `JUMP-018` · `C` · unknown · unknown · unknown

There are four balls, two black and two white. You pick two and random and flip their color from one to the other and repeat. How many times would you do this to ensure all four balls are the same color?

**Answer:** Expected number of moves = 3. (No finite number of moves can 'ensure' it: the probability you are still unfinished after n moves is (2/3)^n, so you need 12 moves to be 99% sure and 23 to be 99.99% sure.)

*Working:* Track the number of black balls. From the 2–2 start, of the C(4,2) = 6 pairs you could flip, one is both-black (→ 0 black, all white), one is both-white (→ 4 black, all black), and four are mixed (→ back to 2–2). So each move finishes with probability 2/6 = 1/3 and otherwise returns you to the identical state; the number of moves is Geometric(1/3) and E = 3. Note the state can never be 1 or 3 black — flipping two balls changes the black count by 0 or ±2, so parity is preserved and 2–2 can only reach 0 or 4.

*Assumption:* 'Pick two at random' = a uniformly random unordered pair of the four balls each time, independently, and both chosen balls are flipped. 'How many times to ensure' is read as the expected number of moves, since no finite number guarantees it.

<sub>numerically verified — `CHECK (exact=3=3.0000, MC=2.9976, rounds for 99%=12, for 99.99%=23, P(alive after 12)=0.00771) vs (3, 3.0, 12, 23, 0.00771)`</sub>

<sub>Source: blog · unknown · [link](https://www.efinancialcareers-canada.com/news/electronic-trading-interviews)</sub>

---

### 9. `JUMP-021` · `C` · unknown · unknown · unknown

What is the probability that two people in a room full of 15 share the same birthday?

**Answer:** 1 − 365!/(350!·365^15) = 1 − (365·364·...·351)/365^15 ≈ 0.2529 (25.29%).

*Working:* Complement: the first person is unconstrained, the second must avoid 1 day, the third 2, and so on, so P(all distinct) = prod_{k=0}^{14} (365−k)/365 ≈ 0.7471 and the answer is ≈ 0.2529. Quick mental check: there are C(15,2) = 105 pairs, each matching with probability 1/365, so the expected number of matching pairs is 105/365 ≈ 0.2877 and the Poisson approximation gives 1 − e^(−0.2877) ≈ 0.2499 — close, and a good thing to say if you have no calculator.

*Assumption:* 365 equally likely birthdays, no leap years, no twins, independence; 'two people share' means at least one coincident pair.

<sub>numerically verified — `CHECK (exact=7535484648737681811365031641358337/29796146005797507000413918212890625, decimal=0.252901) vs (1 - 365!/(350! 365^15) = 0.252901)`</sub>

<sub>Source: blog · unknown · [link](https://www.efinancialcareers-canada.com/news/electronic-trading-interviews)</sub>

---


## Five Rings  (7)

### 1. `5RINGS-004` · `B` · internship · phone_technical · unknown

A question on ordered stats. X and Y in a normal distribution. Find the distribution/expectation value of max(X, Y).

**Answer:** For M = max(X,Y): CDF F_M(m) = Phi(m)^2, density f_M(m) = 2 phi(m) Phi(m), E[M] = 1/sqrt(pi) ~ 0.5642, Var(M) = 1 - 1/pi ~ 0.6817. For iid N(mu, sigma^2): E[M] = mu + sigma/sqrt(pi). For a bivariate normal with correlation rho: E[M] = mu + sigma sqrt((1-rho)/pi).

*Working:* Independence gives P(M <= m) = P(X <= m)P(Y <= m) = Phi(m)^2; differentiate for the density. For the mean use the identity max(X,Y) = (X+Y)/2 + |X-Y|/2: X - Y ~ N(0,2), and E|Z| = sigma_Z sqrt(2/pi) = sqrt(2) sqrt(2/pi) = 2/sqrt(pi), so E[M] = 0 + (1/2)(2/sqrt(pi)) = 1/sqrt(pi). For the variance use max^2 + min^2 = X^2 + Y^2, so E[M^2] + E[min^2] = 2, and by the symmetry min(X,Y) = -max(-X,-Y) the two second moments are equal, giving E[M^2] = 1 and Var(M) = 1 - 1/pi. The correlated case follows the same way since X - Y ~ N(0, 2 sigma^2(1-rho)).

*Assumption:* 'X and Y in a normal distribution' is taken to mean iid standard normal, which is the standard reading; the general iid and correlated formulas are given so the assumption is not load-bearing.

<sub>numerically verified — `CHECK integral_mean=0.564190 mc=0.565085 var=0.681690 vs claimed 1/sqrt(pi)=0.564190 and 1-1/pi=0.681690`</sub>

<sub>Source: wso · 2026-07-28 · [link](https://www.wallstreetoasis.com/company/five-rings-capital-llc/interview)</sub>

---

### 2. `5RINGS-001` · `B` · internship · phone_technical · unknown

what is the maximum number of pieces you can cut a pizza using 10 straight cuts?

**Answer:** 56

*Working:* Lazy caterer: the n-th straight cut meets the previous n-1 cuts in at most n-1 distinct points, which divides that cut into n pieces, and each piece slices one existing region in two - so cut n adds at most n regions. L(n) = 1 + sum_{k=1..n} k = 1 + n(n+1)/2. For n = 10: 1 + 55 = 56. Maximality requires general position: no two cuts parallel, no three concurrent, all intersections inside the pizza.

*Assumption:* Standard 2-D reading: straight cuts all the way across a flat pizza, no stacking or rearranging of pieces between cuts (if you may stack, or cut a 3-D pizza with planes, the answer is larger).

<sub>numerically verified — `CHECK incremental=56 euler=56 formula=56 vs claimed 56`</sub>

<sub>Source: wso · 2023-06-15 · [link](https://www.wallstreetoasis.com/company/five-rings-capital-llc/interview)</sub>

---

### 3. `5RINGS-002` · `B` · unknown · phone_technical · unknown

How many tennis balls in a suit case?, 3^ 3.4? Confidence interval?

**Answer:** 3^3.4 = 41.8998... (exactly 3^(17/5) = fifth root of 3^17 = fifth root of 129140163); quote it as ~41.9 with, say, a 90% interval of [41, 43]. Tennis balls in a suitcase: ~300, order of magnitude 10^2, defensible range roughly 150-500.

*Working:* 3^3.4 = 27 x 3^0.4; ln 3 = 1.0986, so 3^0.4 = e^0.4394 = 1.552, and 27 x 1.552 = 41.9. Sanity bracket: 3^3 = 27 and 3^3.5 = 27 sqrt(3) = 46.77, and 3.4 sits 80% of the way in the exponent, so ~41.9 is right in range. Balls: a tennis ball is 6.7 cm across, volume ~157 cm^3; a medium check-in case is ~70 x 45 x 25 = 79,000 cm^3; at ~64% random close packing that is 0.64 x 79000/157 ~ 320. A carry-on gives ~200, a large case ~490. What the interviewer is scoring on the 'confidence interval' part is calibration: give a point estimate plus a range you would actually bet on - narrow enough to be informative, wide enough to be honest.

*Assumption:* Suitcase size is unstated; I take a medium check-in case (70 x 45 x 25 cm) and standard tennis balls, ignoring the wall thickness of the case.

<sub>numerically verified — `CHECK 3^3.4=41.899830 (=27*3^0.4=41.899830) balls=320 vs claimed 41.8998 and ~300` · confidence: **medium**</sub>

<sub>Source: wso · 2022-09-05 · [link](https://www.wallstreetoasis.com/company/five-rings-capital-llc/interview)</sub>

---

### 4. `5RINGS-008` · `B` · internship · phone_technical · unknown

How many digit 7s appear in the numbers from 1 to 6000?

**Answer:** 1800

*Working:* Count occurrences of the digit 7 (not numbers containing one) in 1..6000. Write every number 0000..5999 as four padded digits; 6000 itself contains no 7, and the padding adds no 7s. In each of the units, tens and hundreds positions the digit cycles uniformly, so a 7 appears in exactly 1/10 of the 6000 numbers = 600 times per position. The thousands digit only runs 0-5, so it is never 7. Total 3 x 600 = 1800. (Tagged as estimation in the source, but it is an exact count.)

<sub>numerically verified — `CHECK brute=1800 formula=1800 vs claimed 1800`</sub>

<sub>Source: wso · 2022-11 · [link](https://www.wallstreetoasis.com/company/five-rings-capital-llc/interview/intern-1)</sub>

---

### 5. `5RINGS-010` · `B` · unknown · phone_technical · unknown

How many balls in a suitcase? (given as an example of the numerous guesstimation problems, 10-15 seconds each)

**Answer:** ~300 balls (order of magnitude 10^2); a defensible range is roughly 150-500 depending on the case.

*Working:* Tennis ball diameter 6.7 cm -> volume ~157 cm^3. Medium check-in case ~70 x 45 x 25 cm = 79,000 cm^3. Spheres do not fill space: random close packing is ~64%, so 0.64 x 79000/157 ~ 320. Cross-check with the faster 10-second method they actually want: treat each ball as filling a 7 cm cube (343 cm^3), giving 79,000/343 ~ 230. Carry-on (55 x 40 x 23) gives ~200, a large case (80 x 50 x 30) ~490. Answer 'about 250-300' and state the two numbers you used (case volume, ball size) - under a 10-15 second clock, showing the two inputs and one division is the whole exercise.

*Assumption:* Suitcase size unstated; medium check-in case assumed, standard tennis balls, wall thickness ignored.

<sub>numerically verified — `CHECK counts={'carry-on 55x40x23': 206, 'medium check-in 70x45x25': 320, 'large 80x50x30': 488} naive_cube_packing=262 vs claimed ~300 (order 10^2, ra` · confidence: **medium**</sub>

<sub>Source: wso · 2019-11 · [link](https://www.wallstreetoasis.com/company/five-rings-capital-llc/interview/quant-trader-1)</sub>

---

### 6. `5RINGS-009` · `B` · internship · phone_technical · unknown

Recruiter 1:1: behavioral (why trading? why Five Rings?) then 10 questions each with a 30 second time limit

**Answer:** No numeric answer - a behavioural screen plus a 10-question timed drill. What is being tested and what a strong response looks like: (1) 'Why trading?' checks whether the motivation is specific and tested, not romantic. Give one concrete origin (a personal trading account, poker or games, a modelling project you actually shipped), one feature of the job you have evidence you enjoy (fast quantitative decisions under uncertainty with immediate, unambiguous feedback), and one thing that is true of this firm and not of every firm (small teams, early responsibility, the specific products they make markets in). Avoid money, 'fast-paced environment', and anything transferable to any employer. (2) 'Why Five Rings?' should reference something checkable - team size, the desk structure, a conversation with someone there. (3) The 30-second drill is testing throughput and composure, not perfection: round aggressively, narrate the approximation out loud, commit to a number with a confidence attached, and never go silent. Eight fast good-enough answers beat four exact ones and six timeouts.

*Working:* Behavioural and speed-drill round; nothing to compute.

<sub>guidance, no single correct value</sub>

<sub>Source: wso · 2024-08 · [link](https://www.wallstreetoasis.com/company/five-rings-capital-llc/interview/trading-intern-13)</sub>

---

### 7. `5RINGS-006` · `D` · internship · online_assessment · 2027

I just got OA. It says 19 min on hackerrank, is that the same you got? I thought hackerrank was just coding not math questions

**Answer:** Not a quantitative question - it is a candidate asking peers about the format. Substance of the answer: HackerRank hosts non-coding assessments too, and for trading/QT roles the Five Rings first screen is typically a short, strictly timed quantitative test (mental arithmetic, probability/expected value, light combinatorics, estimation), not a coding exercise. A ~19-minute clock is consistent with that kind of speed test. Format varies by role and hiring cycle, so another candidate's test length is not a guarantee of yours; software/dev roles do get genuine coding rounds.

*Working:* There is nothing to compute. Practical preparation: drill two-digit multiplication, fraction-to-decimal conversion and percentages to the point of reflex; practise expected-value and simple conditional-probability questions under a stopwatch; assume no calculator unless told otherwise; and budget time so you attempt every question, since these tests reward volume of correct fast answers over perfection on a few.

*Assumption:* The exact duration and content of any specific cycle's OA is not something I can confirm.

<sub>guidance, no single correct value · confidence: **medium**</sub>

<sub>Source: reddit_thread · 2026-03-06 · [link](https://www.reddit.com/r/quantfinance/comments/1rb4s05/just_did_interview_for_five_rings_winternship_2027/)</sub>

---


## Tower Research Capital  (7)

### 1. `TOWER-008` · `B` · internship · onsite · interviewed 2012

How many ways can you jump up stairs if you can only jump either 1 or 2 steps?

**Answer:** f(n) = f(n-1) + f(n-2) with f(1) = 1, f(2) = 2 - the Fibonacci numbers, specifically f(n) = F(n+1) with F(1) = F(2) = 1. So 1, 2, 3, 5, 8, 13, 21, ... and f(10) = 89. Closed form: f(n) = (phi^(n+1) - psi^(n+1))/sqrt(5), phi = (1+sqrt(5))/2, psi = (1-sqrt(5))/2. Equivalently f(n) = sum_{k} C(n-k, k) over k = 0..floor(n/2).

*Working:* Condition on the last jump: it was either a 1-step (leaving f(n-1) ways to have reached n-1) or a 2-step (f(n-2) ways), and these are disjoint and exhaustive - hence the Fibonacci recurrence. Base cases f(1) = 1 and f(2) = 2 shift the index by one relative to the standard Fibonacci sequence, which is the only thing people get wrong here. The binomial form comes from choosing which k of the n-k jumps are the 2-steps.

*Assumption:* Order of jumps matters (sequences, not multisets); stairs are climbed one direction only.

<sub>numerically verified — `CHECK brute=[1, 2, 3, 5, 8, 13, 21, 34] f(10)=89 f(15)=987 matches_F(n+1)=True binet_ok=True vs claimed f(n)=F(n+1): [1,2,3,5,8,13,21,34], f(10)=89, f`</sub>

<sub>Source: interview_review_site · 2012-11-22 · [link](https://www.wallstreetoasis.com/company/tower-research-capital/interview)</sub>

---

### 2. `TOWER-003` · `B` · unknown · phone_technical · interviewed September 2019

Fermi estimation questions: Estimate the surface area of a tennis ball. Number of Starbucks in NYC?

**Answer:** Tennis ball surface area: about 140 cm^2 (0.014 m^2). Diameter ~6.7 cm -> r = 3.35 cm -> A = 4*pi*r^2 = 141 cm^2; across the legal 6.54-6.86 cm range the answer is 134-148 cm^2. Starbucks in NYC: a few hundred - my estimate is ~300, and the true figure is most likely in the 200-350 band (order of magnitude 10^2).

*Working:* Ball: a tennis ball is about the width of three fingers, ~7 cm; 4*pi*(3.35)^2 = 141 cm^2. (The felt nap makes the true wetted area somewhat larger; the geometric sphere is what is being asked.) Starbucks: US has roughly 16,000 stores for ~330M people, i.e. 1 per ~20,000 people. NYC has ~8.5M residents plus a large commuter/tourist daytime population, which would give ~425 at the national rate; Manhattan's density and office traffic push that up, but sky-high rents and unusually strong independent-cafe competition push it down, so I shade to ~300. Cross-check: ~200 in Manhattan alone at roughly one every few blocks in Midtown, plus a thinner scattering across the four outer boroughs, lands in the same band.

*Assumption:* 'Surface area' means the geometric sphere. Starbucks count = the five boroughs, company- operated plus licensed (in-store kiosks are what make this figure fuzzy).

<sub>numerically verified — `CHECK area=141.0 cm^2 (range over legal diameters 134.4-147.8) vs claimed ~141 cm^2 (~0.014 m^2)` · confidence: **medium**</sub>

<sub>Source: interview_review_site · 2020-01-03 · [link](https://www.wallstreetoasis.com/company/tower-research-capital/interview)</sub>

---

### 3. `TOWER-002` · `B` · unknown · phone_technical · interviewed September 2019

How would you replicate a fair coin using an unfair coin? Expected number of tosses? Vice versa?

**Answer:** Unfair -> fair (von Neumann): flip in pairs; HT -> output H, TH -> output T, HH/TT -> discard and repeat. Each pair is decisive with probability 2pq, so the expected number of tosses is 2/(2pq) = 1/(p(1-p)) (e.g. 4 at p=1/2, 1/0.21 = 100/21 = 4.7619 at p=0.3). Fair -> unfair (probability p): read off the binary expansion p = 0.b1b2b3...; flip fair coins f1,f2,... and stop at the first i with fi != bi, returning heads if bi=1 and tails if bi=0. Expected number of fair flips = sum_{k>=1} k*2^-k = 2 for any non-dyadic p (it is 2 - 2^(1-k) if p is dyadic with a k-bit expansion), and this is Knuth-Yao optimal.

*Working:* von Neumann: HT and TH both have probability pq, so conditioning on a decisive pair the output is exactly fair for any p in (0,1) - crucially without knowing p. Number of pairs is Geometric(2pq) with mean 1/(2pq), and each pair costs 2 tosses, giving 1/(pq). Reverse direction: the stopping index N (first fair bit disagreeing with the corresponding bit of p) satisfies P(N>k) = 2^-k, so E[N] = 2; the construction outputs heads exactly when the uniform U built from the fair bits falls below p, i.e. with probability p. Worth adding: von Neumann is not rate-optimal - the Elias/Peres extractors recycle the discarded HH/TT information and approach the entropy limit 1/H(p) tosses per fair bit.

*Assumption:* 0 < p < 1 and p need not be known for the von Neumann direction; the reverse direction assumes you can read the binary expansion of the target p.

<sub>numerically verified — `CHECK vN_prob=0.50084 vN_tosses=4.7619 biased_prob=0.33392 fair_flips=1.9999 vs claimed 0.5, 4.7619, 0.33333, 2.0`</sub>

<sub>Source: interview_review_site · 2020-01-03 · [link](https://www.wallstreetoasis.com/company/tower-research-capital/interview)</sub>

---

### 4. `TOWER-006` · `B` · unknown · phone_technical · interviewed September 2019

If you three random variables X, Y, Z and you know the relationship between X and Y (say they're dependent), does that tell you anything about X and Z or Y and Z? What if the correlation between X and Y is 0.2 and the correlation between Y and Z is 0.5. What is the range for the correlation of X and Z?

**Answer:** Part 1: no. Dependence is not transitive - X and Y dependent tells you nothing about (X,Z) or (Y,Z); Z can be independent of both. (And even pairwise independence of all three pairs does not give mutual independence: X, Y iid uniform on {-1,+1} with Z = XY.) Part 2: correlations are constrained, because the correlation matrix must be positive semidefinite. With r_XY = 0.2 and r_YZ = 0.5, r_XZ lies in [0.1 - (3*sqrt(2))/5, 0.1 + (3*sqrt(2))/5] = [-0.748528..., 0.948528...]. Both endpoints are attainable (the matrix is then singular).

*Working:* General bound: r13 must satisfy r13 in [r12*r23 - sqrt((1-r12^2)(1-r23^2)), r12*r23 + sqrt((1-r12^2)(1-r23^2))]. Derivation: det of the 3x3 correlation matrix is 1 - r12^2 - r23^2 - r13^2 + 2*r12*r23*r13 >= 0, a downward parabola in r13 whose roots are exactly those endpoints. Here r12*r23 = 0.1 and sqrt(0.96*0.75) = sqrt(0.72) = 3*sqrt(2)/5 = 0.848528, giving [-0.748528, 0.948528]. Geometric reading: correlations are cosines of angles between unit vectors, so angle(X,Z) is pinned between |angle(X,Y) - angle(Y,Z)| and angle(X,Y) + angle(Y,Z) - the triangle inequality on the sphere, which is why the interval is not all of [-1,1] but also is not a point.

*Assumption:* Correlations are Pearson correlations of finite-variance, non-degenerate variables.

<sub>numerically verified — `CHECK psd_range=[-0.748528,0.948528] attainable_top=0.9484(with 0.200,0.501) attainable_bot=-0.7479(with 0.200,0.501) vs claimed [-0.748528,0.948528]`</sub>

<sub>Source: interview_review_site · 2020-01-03 · [link](https://www.wallstreetoasis.com/company/tower-research-capital/interview)</sub>

---

### 5. `TOWER-007` · `B` · unknown · phone_technical · interviewed September 2018

Given a biased coin with probability p, how would you replicate n independent tosses of a fair coin? How many tosses do you expect to make to achieve it? Can you give a lower bound on how many tosses you need to do it? A lower bound better than n?

**Answer:** Method: von Neumann pairing, repeated n times - flip pairs, HT -> 1, TH -> 0, discard HH/TT. Expected number of biased tosses = n/(p(1-p)) (e.g. 100n/21 = 14.29 for n=3 at p=0.3). Lower bound: yes, and it beats n. Any scheme obeys E[N] >= n/H(p) where H(p) = -p*log2(p) - (1-p)*log2(1-p); since H(p) <= 1 with equality only at p = 1/2, this is strictly greater than n for any biased coin (at p = 0.3, H = 0.8813 so E[N] >= 1.135n). This bound is achievable asymptotically by the Elias/Peres extractors, which recycle the information von Neumann throws away.

*Working:* Correctness: HT and TH are equally likely (both pq) for every p, so conditioning on a decisive pair gives an exactly fair bit, and distinct pairs are independent - so n repetitions give n iid fair bits, and you never need to know p. Cost: pairs until a decision is Geometric(2pq) with mean 1/(2pq), times 2 tosses per pair, times n bits = n/(pq). Lower bound (the interesting part): each toss carries at most H(p) bits of entropy, and for a stopping time N the observed sequence has entropy E[N]*H(p); it must encode n bits of uniform randomness, so E[N]*H(p) >= n. Trivially E[N] >= n as well since H(p) <= 1, but the entropy bound is strictly stronger whenever p != 1/2. Note the gap: von Neumann pays 1/(pq) = 4.76 tosses per bit at p = 0.3 against a floor of 1.13, so it is correct but far from optimal.

*Assumption:* 0 < p < 1; p unknown is fine for von Neumann (a p-dependent scheme cannot beat the entropy bound either).

<sub>numerically verified — `CHECK vonNeumann_tosses=14.2893 max_pattern_dev=0.00031 entropy_bound=3.4041 H=0.8813 vs claimed 14.2857, ~0, 3.4041 (>n=3)`</sub>

<sub>Source: interview_review_site · 2018-09-09 · [link](https://www.wallstreetoasis.com/company/tower-research-capital/interview)</sub>

---

### 6. `TOWER-005` · `B` · unknown · phone_technical · interviewed September 2018

What are the differences between Lasso and Ridge? Why does Lasso have an effect of feature selection? What if instead of minimizing mean squared error we look at mean absolute error? How do you choose the number of trees in a random forest classifier? Is the more the better?

**Answer:** (1) Lasso vs Ridge: both add a penalty to squared loss - ridge lambda*||beta||_2^2, lasso lambda*||beta||_1. Ridge has the closed form (X'X + lambda*I)^-1 X'y, shrinks all coefficients smoothly toward zero but never to exactly zero, and handles collinearity by splitting weight across correlated predictors. Lasso has no closed form (convex; coordinate descent or LARS), sets coefficients exactly to zero, and among a group of correlated predictors tends to keep one arbitrarily; with p > n it selects at most n. Bayesian view: Gaussian prior vs Laplace prior. Elastic net mixes the two to get sparsity plus grouping. (2) Why lasso selects: with orthonormal X the lasso solution is soft-thresholding, sign(b_ols)*(|b_ols| - lambda)_+, which is exactly 0 whenever |b_ols| <= lambda, while ridge gives b_ols/(1+lambda), never 0. Equivalently the L1 penalty has subgradient +/-lambda at 0 so a coefficient is pinned at zero until the loss gradient exceeds lambda; geometrically the L1 ball has corners on the axes, so the elliptical loss contours touch it at a corner with positive probability. (3) MSE -> MAE: you are now estimating the conditional median instead of the conditional mean (MAE is the tau = 0.5 case of quantile/pinball loss). Much more robust to outliers and fat tails - relevant for returns - but non-differentiable at zero, no closed form (LP or subgradient/IRLS), solutions can be non-unique, and it is less efficient than OLS under Gaussian noise (OLS is Gaussian MLE, LAD is Laplace MLE). (4) Number of trees: unlike boosting, a random forest does not overfit as B grows - the ensemble average converges as B -> infinity, so accuracy is monotone-ish up to noise and 'more is better' is true statistically but bounded by diminishing returns. Var of the average behaves like rho*sigma^2 + (1-rho)*sigma^2/B, so once B >> (1-rho)/rho the correlation term dominates and extra trees buy nothing. Choose B by plotting OOB error against B and stopping at the plateau (typically a few hundred), then spend your budget on mtry and depth instead. The real cost of large B is memory, training time and inference latency - which in a trading system is the binding constraint. Also use more trees than the accuracy plateau if you need stable feature importances or smooth predicted probabilities.

*Working:* Standard ML screen. What is being tested: whether you know the mechanism behind sparsity (not just 'L1 gives sparsity'), that changing the loss changes the estimand, and that you can tell apart hyperparameters that trade off bias/variance from ones that only trade off compute. The soft-thresholding formula and the 'boosting overfits in B, bagging does not' contrast are the two things that separate a strong answer from a memorised one.

<sub>guidance, no single correct value</sub>

<sub>Source: interview_review_site · 2018-09-09 · [link](https://www.wallstreetoasis.com/company/tower-research-capital/interview)</sub>

---

### 7. `TOWER-004` · `B` · unknown · phone_technical · interviewed September 2013

How many golf balls fit in the empire state building? Explain thought process and detailed solution. Interviewers wanted to see train of thought was not looking for correct answer.

**Answer:** About 1.6 x 10^10 golf balls for an empty shell, or ~1 x 10^10 once floors, walls and lift shafts are subtracted. Order of magnitude: 10^10, i.e. tens of billions.

*Working:* Volume: the Empire State Building is ~2.8M sq ft of floor space at ~12 ft per floor, i.e. ~37M cubic feet = 1.05 x 10^6 m^3. (Sanity check from the outside: a ~130 m x 60 m base tapering over 380 m is the same order.) Golf ball: diameter 4.27 cm, so volume = (4/3)pi*r^3 = 40.7 cm^3 = 4.07 x 10^-5 m^3. Poured loose, spheres reach ~64% packing density, so each ball really occupies 40.7/0.64 = 64 cm^3. N = 1.05e6 / 6.4e-5 = 1.6 x 10^10. Knock off ~25% for structure and contents and you get ~1.2 x 10^10. State the packing factor explicitly - forgetting it is the single most common error and inflates the count by ~1.6x.

*Assumption:* Interior treated as empty usable volume; equal spheres at random close packing (0.64) rather than the crystalline optimum (0.74).

<sub>numerically verified — `CHECK V=1.048e+06 m^3 v_ball=4.068e-05 m^3 n_packed=1.65e+10 n_with_structure=1.24e+10 n_no_gaps=2.58e+10 vs claimed ~1.6e10 (order 1e10)` · confidence: **medium**</sub>

<sub>Source: interview_review_site · 2013-09-15 · [link](https://www.wallstreetoasis.com/company/tower-research-capital/interview)</sub>

---


## Chicago Trading Company (CTC)  (6)

### 1. `CTC-007` · `B` · internship · onsite · interviewed January 2020

A stick is randomly cut at 2 different points. What is the probability that the three pieces form a triangle?

**Answer:** 1/4.

*Working:* Let the two cut points be U, V ~ iid Uniform(0,1), and set x = min(U,V), y = max(U,V). The three pieces are x, y - x and 1 - y. A triangle exists iff no piece reaches 1/2 (the triangle inequality against the total length 1), i.e. x < 1/2, y > 1/2 and y - x < 1/2. In the (u,v) unit square that region is two congruent triangles of area 1/8 each, so the probability is 1/4.

*Assumption:* The two cut points are independent and uniform on the stick, chosen simultaneously (the standard reading). The other common variant - break once uniformly, then break the longer piece uniformly - gives a different answer (2 ln 2 - 1 = 0.386), so it is worth confirming which the interviewer means.

<sub>numerically verified — `CHECK montecarlo=0.25040 vs claimed 0.25`</sub>

<sub>Source: interview_review_site · 2020-02-26 · [link](https://www.wallstreetoasis.com/company/chicago-trading-company/interview)</sub>

---

### 2. `CTC-001` · `B` · unknown · phone_technical · interviewed November 2018

You have 8 marbles. One of them weighs more than the 7 others. What is the minimum number of steps you need in order to determine the outlier?

**Answer:** 2 weighings.

*Working:* Balance scale, one marble known heavier. Split 3/3/2. Weigh 3 against 3. If one side is heavier the culprit is in that group of 3: weigh 1 against 1, and either one tips or it is the third. If it balances the culprit is one of the 2 set aside: weigh them against each other. Either branch finishes in 2. Lower bound: one weighing has only 3 outcomes, which cannot distinguish 8 candidates, so 1 is impossible; 2 is optimal (and this scheme would in fact handle up to 9 marbles).

*Assumption:* 'Steps' means weighings on a two-pan balance that reports only left/right/equal. Exhaustive search over all balanced pan assignments confirms the minimax depth is 2.

<sub>numerically verified — `CHECK minimum_weighings=2 info_lower_bound=2 vs claimed 2 2`</sub>

<sub>Source: interview_review_site · 2019-06-04 · [link](https://www.wallstreetoasis.com/company/chicago-trading-company/interview)</sub>

---

### 3. `CTC-005` · `B` · internship · phone_technical · interviewed February 2018

What is 5/32 expressed as a decimal. What is 7/12. What is 34*45.

**Answer:** 5/32 = 0.15625; 7/12 = 0.58333... (0.583 with the 3 repeating) = 58.33%; 34 x 45 = 1530.

*Working:* 5/32: halve repeatedly from 5 - 5/2=2.5, /4=1.25, /8=0.625, /16=0.3125, /32=0.15625. Or 1/32 = 3.125%, times 5 = 15.625%. 7/12 = 7/12; since 1/12 = 0.08333, seven of them = 0.58333 (equivalently 0.5 + 1/12). 34 x 45: halve-and-double to 17 x 90 = 1530. These are speed questions - the method matters as much as the number, so say the route you took.

<sub>numerically verified — `CHECK 5/32=0.15625 7/12=0.583333(=7/12, 0.58333... repeating) 34*45=1530 vs claimed 0.15625 0.583333 1530`</sub>

<sub>Source: interview_review_site · 2018-03-13 · [link](https://www.wallstreetoasis.com/company/chicago-trading-company/interview)</sub>

---

### 4. `CTC-006` · `B` · internship · superday · interviewed October 2020

Estimate how many windows Empire State Building has and how confident are you to your estimation.

**Answer:** About 6,500 windows; the figure the building itself publishes is 6,514. On confidence: I would put ~80% on the true count lying between 5,000 and 8,000, and I would be surprised (<5%) to be off by more than a factor of 2.

*Working:* 102 storeys, but the tower tapers hard: call it ~100 window-bearing floors and use a mid-building floor plate of roughly 60 m x 40 m, i.e. ~200 m of perimeter. Punched windows on that facade sit ~3 m apart, so ~65 windows per floor, and 65 x 100 = ~6,500. The published count is 6,514, so the estimate lands within 1%, which is luck as much as method - the honest error bars are the ones quoted above. The second half of the question is the real test: give a point estimate, then a range, then name the input you are least sure of (here, average windows per floor, because of the setbacks) and say how much it moves the answer.

*Assumption:* Windows in the tower itself, not counting the observatory glazing or the spire.

<sub>confidence: **medium**</sub>

<sub>Source: interview_review_site · 2020-11-15 · [link](https://www.wallstreetoasis.com/company/chicago-trading-company/interview)</sub>

---

### 5. `CTC-002` · `B` · unknown · superday · interviewed November 2017

Estimate the number of barrels of oil you could fit on an aircraft carrier, number of gas stations in California.

**Answer:** Barrels of oil on an aircraft carrier: order 10^5, about 150,000 barrels (range 100k-200k). Gas stations in California: order 10^4, about 10,000-12,000.

*Working:* Carrier: a Nimitz-class displaces ~100,000 t fully loaded against a light-ship weight near 78,000 t, so usable cargo deadweight is ~20,000-25,000 t. A barrel is 42 US gal = 0.159 m^3 and crude is ~0.87 t/m^3, so ~0.138 t/barrel, giving 25,000/0.138 = ~180,000 barrels pumped as bulk, or ~150,000 in steel drums once you pay for drum weight and packing voids. Weight binds before volume: the hangar deck alone (~208 x 33 x 8 m = 55,000 m^3) would hold ~200,000+ drums, which would weigh far more than the ship can carry. Cross-check: a 25,000 DWT product tanker carries ~175,000 barrels - same ballpark, which is the right sanity test. California: ~39m people, ~27m light-duty vehicles, ~11,000 mi/yr at ~24 mpg = ~460 gal/vehicle/yr, so ~12-13 billion gal/yr (matches the ~13-14 billion gal state total). A typical station moves ~100-125k gal/month = ~1.3m gal/yr. 13e9/1.3e6 = ~10,000 stations.

*Assumption:* Aircraft carrier = US Nimitz-class supercarrier; 'barrels' = standard 42-gallon oil barrels, and I read 'fit on' as a realistic load (weight-limited), not a geometric packing of the flight deck. If they genuinely want geometric packing of every deck ignoring buoyancy, the answer rises to ~10^6 and you should say so and let them pick.

<sub>confidence: **medium**</sub>

<sub>Source: interview_review_site · 2020-04-25 · [link](https://www.wallstreetoasis.com/company/chicago-trading-company/interview)</sub>

---

### 6. `CTC-008` · `B` · internship · unknown · interviewed January 2020

You have 27 race horses. You can race five of them at a time. You don't know what each one's time even if you race them (you only know the order in which the five horses raced ended up in). How many races do you need to make, in what order, with what horses, in order to know the top three horses overall from the pool of 27 horses? You also need to know not just which three horses these are, but their order relative to each other (who came first, second, third). Optimize your strategy to find the minimum number of races.

**Answer:** 8 races. Not 7 - the familiar 25-horse answer of 7 does not survive the two extra horses.

*Working:* Strategy: races 1-5, run 25 of the horses in five heats of five. Race 6, run the five heat winners; call them A1 > B1 > C1 > D1 > E1 (relabelling heats to match). A1 is the fastest of those 25, and only A2, A3, B1, B2, C1 can still be 2nd or 3rd of the 25 - everyone else has 3 horses provably ahead of them. Race 7, run those five; its top two are the 2nd and 3rd fastest of the 25. Race 8, run A1, those two, and the two horses held back; the top three of that race, in order, are the top three overall, because every other horse is known to be behind all three of A1 and the 25-pool's 2nd and 3rd. Lower bound: a horse leaves contention for 1st only by losing a race, and a race beats at most 4 previously-unbeaten horses, so eliminating 26 needs ceil(26/4) = 7 races just to name the winner. 7 in total is still impossible: after 6 races at least 27 - 24 = 3 horses are unbeaten, all of them must run race 7 (any unbeaten horse left out stays a candidate for 1st), which leaves at most 2 spare seats. So every horse outside race 7 already needs 3 horses known ahead of it, i.e. 6 races must leave at most 5 horses with fewer than 3. That cannot be done: results ordered by 'fewest known-superiors first' are always consistent with some true ranking, and against that ordering eliminating 24 horses in 6 races forces all six races to consist of 5 unbeaten horses, whereupon race 5's runner-up can never acquire a second horse ahead of it - leaving at least 3 unbeaten + race 6's 2nd and 3rd + that runner-up = 6 > 5. Hence 7 is impossible and 8 is optimal.

*Assumption:* Races give order only, no times; no ties; horse speeds are fixed and consistent across races.

<sub>numerically verified — `CHECK strategy_failures=0 races_used=[8] min_debt_after_6=8 vs claimed 0 [8] >5 (so 7 races cannot suffice, answer 8)`</sub>

<sub>Source: interview_review_site · 2020-02-10 · [link](https://www.wallstreetoasis.com/company/chicago-trading-company/interview)</sub>

---


## Marshall Wace  (6)

### 1. `MW-002` · `C` · new_grad · online_assessment · previous iterations of the Quant Associate Programme

[3 marks] A researcher takes a random sample of 25 fourteen-year-old students from a large population and gives them an IQ test. The population mean IQ is known to be 100. The first student is found to have an IQ of 150. What is your expectation for the average IQ for the sample of 25 students?

**Answer:** 102 IQ points exactly. E[sample mean] = (150 + 24*100)/25 = 2550/25 = 102.

*Working:* Knowing student 1 scored 150 tells you nothing about the other 24, who are still a random sample from a population with mean 100. So E[total] = 150 + 24*100 = 2550 and E[mean] = 2550/25 = 102. The two traps: answering 100 (over-applying 'regression to the mean' to the whole sample) and answering something near 150 (treating the first draw as informative about the rest). Regression to the mean does operate here, but only on the remaining 24: their expectation is 100, not 150, which is exactly why the sample mean is 102 rather than higher. Note the answer does not depend on the population standard deviation at all.

*Assumption:* Population is large enough that sampling without replacement is negligible (the question says 'large population'). For a finite population of size N with mean 100, the exact answer is [150 + 24*(100N-150)/(N-1)]/25, which tends to 102 as N grows.

<sub>numerically verified — `CHECK 101.9983 vs 102`</sub>

<sub>Source: firm_official_pdf · unknown · [link](https://cdn.mwam.com/download/MW_Quant_Application_Guide.pdf)</sub>

---

### 2. `MW-005` · `C` · new_grad · online_assessment · previous iterations of the Quant Associate Programme

[3 marks] You have a table of items containing three columns of length n. Columns A and B contain only integers, while Column C contains only strings, all of which are 6 characters long. ... You use 'quicksort' to sort column A. What is the average time complexity when sorting n elements?

**Answer:** Theta(n log n) average case. Precisely, the expected number of comparisons is 2(n+1)H_n - 4n ~ 2n ln n = (2 ln 2) n log2 n ~ 1.386 n log2 n. Worst case is O(n^2) (already-sorted input with a naive first-element pivot); best case O(n log n); expected auxiliary space O(log n) for the recursion stack.

*Working:* With a random pivot the recurrence is C(n) = (n-1) + (1/n) * sum_{k=0}^{n-1} [C(k) + C(n-1-k)], whose solution is 2(n+1)H_n - 4n = Theta(n log n). Equivalently, elements i and j (in sorted order) are compared iff one of them is the first pivot chosen from the range between them, probability 2/(j-i+1), and summing gives ~2n ln n. Column A holds integers so each comparison is O(1) — the answer would be the same for column C, since comparing fixed-length 6-character strings is O(6) = O(1). Quicksort is also not stable, which matters if you need to carry columns B and C along with A.

*Assumption:* 'Average time complexity' is over a uniformly random input permutation (equivalently, a randomised pivot), which is the standard meaning.

<sub>numerically verified — `CHECK measured/theory for n=1k,2k,4k,8k = 0.998, 0.991, 1.013, 1.009 vs 1.000 each (Theta(n log n))`</sub>

<sub>Source: firm_official_pdf · unknown · [link](https://cdn.mwam.com/download/MW_Quant_Application_Guide.pdf)</sub>

---

### 3. `MW-001` · `C` · new_grad · onsite · previous iterations of the Quant Associate Programme

We each take turns to roll a dice. Each time a number comes up which had not previously come up, we cross it out from the list of numbers 1,2,3,4,5,6. The winner is the player to cross out the last number. Would you prefer to play first or second?

**Answer:** Prefer to go SECOND. The first player wins with probability 461/924 ≈ 0.49892, so the second player wins with probability 463/924 ≈ 0.50108 — an edge of 1/462 ≈ 0.22%.

*Working:* Only the parity of the total number of rolls matters: the winner is whoever makes the roll that crosses out the sixth number, and player one makes rolls 1, 3, 5, ..., so player one wins iff the total roll count T is odd. T is a sum of independent geometrics: while k numbers are crossed out, each roll is a 'success' with probability (6−k)/6, so T = G_0 + ... + G_5 with success probabilities 1, 5/6, 4/6, 3/6, 2/6, 1/6. For a geometric with success probability p, E[(−1)^G] = −p/(2−p), so E[(−1)^T] = the product over the six stages = (−1)(−5/7)(−1/2)(−1/3)(−1/5)(−1/11) = 1/462. Hence P(T even) − P(T odd) = 1/462 and P(first player wins) = P(T odd) = (1 − 1/462)/2 = 461/924. The intuition: the long final stage (waiting for the last face, mean 6 rolls) is nearly parity-neutral, so the tiny bias comes from the early stages, and it happens to favour the second player.

*Assumption:* Players alternate strictly one roll each, and a roll that repeats an already-crossed number simply passes the turn (it does not earn another roll). Under the alternative rule 'keep rolling until you cross one out' the game is deterministic and the second player always wins, which is clearly not the intended puzzle.

<sub>numerically verified — `CHECK (P(first player wins)=461/924=0.498918, gf=461/924, dp=0.498918) vs (461/924=0.498918, so prefer to go SECOND)`</sub>

<sub>Source: firm_official_pdf · unknown · [link](https://cdn.mwam.com/download/MW_Quant_Application_Guide.pdf)</sub>

---

### 4. `MW-006` · `C` · new_grad · onsite · previous iterations of the Quant Associate Programme

You are given an integer array cost where cost[i] is the cost of i th step on a staircase. Once you pay the cost, you can either climb one or two steps. You can either start from the step with index 0, or the step with index 1. Return the minimum cost to reach the top of the floor.

**Answer:** O(n) time, O(1) space DP. dp[i] = min cost to stand on step i = cost[i] + min(dp[i-1], dp[i-2]), with dp[0] = cost[0], dp[1] = cost[1]; the answer is min(dp[n-1], dp[n-2]) because the top of the floor is index n, reachable from either of the last two steps. def minCostClimbingStairs(cost): a = b = 0 # cheapest way to reach steps i-2 and i-1 for c in cost: a, b = b, min(a, b) + c return min(a, b) Examples: [10,15,20] -> 15; [1,100,1,1,1,100,1,1,100,1] -> 6.

*Working:* The cost is paid on the step you stand on, and you leave from it by 1 or 2 steps, so the only way to be on step i is from i-1 or i-2: dp[i] = cost[i] + min(dp[i-1], dp[i-2]). Being allowed to start at index 0 or 1 free is exactly the base case dp[0]=cost[0], dp[1]=cost[1]. 'Top of the floor' is the virtual index n which costs nothing, so the answer is min(dp[n-1], dp[n-2]). Only the last two values are ever needed, hence the rolling-pair version above, which is O(1) space. This is LeetCode 746; the two things interviewers probe are the off-by-one at the top and the O(1) space reduction.

*Assumption:* n = len(cost) >= 2, the standard constraint for this problem.

<sub>numerically verified — `CHECK mismatches=0 examples=(15,6) vs mismatches=0 examples=(15,6)`</sub>

<sub>Source: firm_official_pdf · unknown · [link](https://cdn.mwam.com/download/MW_Quant_Application_Guide.pdf)</sub>

---

### 5. `MW-003` · `C` · new_grad · phone_technical · previous iterations of the Quant Associate Programme

[10 marks] An airline company has 105 aeroplanes in service which fly cargo between London and New York. At the end of each month an inventory is taken of which aeroplanes are at which of the two cities. Every month, the movements of the planes between airports can be summarised as follows: 60% of the planes in London remain in London the following month. 40% of the planes in London are in New York the following month. 100% of the planes in New York are in London the following month. None of the planes in New York remain in New York the following month. a) [7 marks] If at the end of this month there are 70 aeroplanes in London and 35 in New York, how many will there be in each city in T months' time? T is an integer >0. Assume fractional aeroplanes exist, so you can have half an aeroplane in each city for example. b) [3 marks] How many aeroplanes will there be in each city in the distant future, i.e. as T tends to infinity?

**Answer:** (a) London L_T = 75 - 5*(-2/5)^T, New York N_T = 30 + 5*(-2/5)^T (so T=1: 77 and 28; T=2: 74.2 and 30.8; T=3: 75.32 and 29.68). (b) In the limit, 75 aeroplanes in London and 30 in New York.

*Working:* Recursion: L_{T+1} = 0.6*L_T + 1.0*N_T, N_{T+1} = 0.4*L_T, with L_T + N_T = 105 always. Matrix M = [[0.6, 1], [0.4, 0]] has characteristic polynomial lam^2 - 0.6*lam - 0.4 = 0, so lam = 1 and lam = -0.4. The lam=1 eigenvector gives the steady state: L = 0.6L + N and N = 0.4L with L+N=105 => (75, 30). The lam=-0.4 eigenvector is (1, -1). Write the start as (70, 35) = (75, 30) - 5*(1, -1), so (L_T, N_T) = (75, 30) - 5*(-0.4)^T*(1, -1). Check T=1: 0.6*70 + 35 = 77 = 75 + 2. (b) |−0.4| < 1, so the transient dies and the split converges to 75/30 — approached in an alternating fashion (over, then under) because the second eigenvalue is negative. Equivalently 5/7 of the fleet in London, 2/7 in New York.

<sub>numerically verified — `CHECK maxerr=0 limit=(75.000000,30.000000) vs (0, 75, 30)`</sub>

<sub>Source: firm_official_pdf · unknown · [link](https://cdn.mwam.com/download/MW_Quant_Application_Guide.pdf)</sub>

---

### 6. `MW-004` · `C` · new_grad · phone_technical · previous iterations of the Quant Associate Programme

[14 marks] In a legal dispute over paternity, Adam is the alleged father. The judge is a Bayesian statistician, and announces at the start that, in the interests of fairness, his prior belief is that there is a 50% chance Adam is the father. On the first day of the trial, testimonials are given. On the second day, it is revealed that the child has blood type B, and according to geneticists, this would happen with probability 50% if Adam is the father. Furthermore, based on incidence rates of B genes in the population, there is a 10% chance that this child would have blood type B if Adam is not the father. At the end of the second day, the judge announces that his assessment of the probability that Adam is the father is 75%. a) [5 marks] What were the judge's beliefs at the end of the first day? b) [4 marks] Deduce the ratio of the Judge's assessment of the likelihood of the testimonials given that Adam is the father vs given Adam is not the father. c) [5 marks] There is some dispute over the geneticist's assessment that "there is a 10% chance the child would have blood type B if Adam is not the father". Experts are divided in opinion, with estimates for this figure ranging uniformly between 10% and 20%. If the Judge summarises this uncertainty by assigning a Uniform(0.1,0.2) distribution for this figure, rather than using the 10% figure, derive the Judge's final assessment in this case.

**Answer:** (a) 3/8 = 37.5%. (b) P(testimonials | father) / P(testimonials | not father) = 3/5 = 0.6. (c) 2/3 = 66.67%.

*Working:* Work in odds. Blood-type Bayes factor = 0.5/0.1 = 5. Final probability 75% is odds 3, so odds after day 1 = 3/5, i.e. probability (3/5)/(1+3/5) = 3/8 = 37.5%. (b) Prior odds were 1, so the testimonial likelihood ratio is (3/5)/1 = 3/5 = 0.6 — the testimonials were in fact mildly exculpatory, evidence against paternity. (c) With q ~ U(0.1, 0.2) independent of paternity, coherent updating marginalises the likelihood, which just replaces 0.1 by E[q] = 0.15: P = (3/8 * 1/2) / (3/8 * 1/2 + 5/8 * 0.15) = (3/16)/(45/160) = 2/3. Worth flagging the standard error here: averaging the posteriors computed at each q, (1/0.1)*integral of 0.1875/(0.1875+0.625q) dq = 3*ln(1.25) = 0.6694, is NOT the posterior — it ignores that values of q consistent with the data get reweighted. The answer is exactly 2/3.

*Assumption:* In (c) the expert uncertainty q is taken to be independent of whether Adam is the father, and the testimonial evidence from day 1 (posterior 3/8) is carried forward.

<sub>numerically verified — `CHECK a=3/8 b=3/5 c_mc=0.66681 (naive_avg_posterior=0.66943) vs a=3/8->3/4, b=3/5, c=2/3=0.66667`</sub>

<sub>Source: firm_official_pdf · unknown · [link](https://cdn.mwam.com/download/MW_Quant_Application_Guide.pdf)</sub>

---


## Maven Securities  (6)

### 1. `MAVEN-002` · `B` · internship · online_assessment · 2026

If today is Monday, what day will it be in 80 days?

**Answer:** Thursday.

*Working:* Only 80 mod 7 matters. 77 = 7*11, so 80 = 77 + 3, i.e. 80 days is 11 weeks plus 3 days. Monday + 3 = Thursday. (Mental shortcut: knock off the nearest multiple of 7 below — 70 gets you back to Monday, then 10 more days = 7 + 3 = Thursday.)

<sub>numerically verified — `CHECK mod7=Thursday calendar=Thursday vs Thursday`</sub>

<sub>Source: interview_review_db · 2025-11-14 · [link](https://www.wallstreetoasis.com/company/maven-securities/interview)</sub>

---

### 2. `MAVEN-007` · `B` · new_grad · online_assessment · 2026

How many combinations are there of the letters in the word "MISSISSIPPI"?

**Answer:** 34,650 = 11! / (1! * 4! * 4! * 2!) = 39,916,800 / 1152. (Pedantic footnote: 'combinations' is loose wording. If they literally meant distinct sub-multisets of letters of any size, the count is 2*5*5*3 = 150 including the empty one, i.e. 149 non-empty. The intended and expected answer is 34,650 distinct arrangements.)

*Working:* MISSISSIPPI has 11 letters: M x1, I x4, S x4, P x2. Distinct arrangements of a multiset = 11! divided by the factorials of the repeat counts = 11!/(4!4!2!1!) = 34,650. Equivalent constructive count: choose positions for the I's C(11,4) = 330, then the S's C(7,4) = 35, then the P's C(3,2) = 3, then the M in the last slot: 330*35*3 = 34,650.

*Assumption:* 'Combinations' is read as the standard interview meaning: distinct orderings (permutations) of all 11 letters.

<sub>numerically verified — `CHECK enumerated=34650 formula=34650 nonempty_submultisets=149 vs 34650, 34650, 149`</sub>

<sub>Source: interview_review_db · 2026-02-20 · [link](https://www.wallstreetoasis.com/company/maven-securities/interview)</sub>

---

### 3. `MAVEN-004` · `B` · internship · phone_technical · 2025

You observe a symmetric random walk starting at zero. You are allowed to stop at any time, and your payoff when you stop is the position of the walk minus a cost that accumulates with each step. What stopping strategy maximizes your expected payoff?

**Answer:** Stop immediately, at time 0. The optimal expected payoff is 0, and every non-trivial stopping rule is strictly worse. For any cost c > 0 there is no threshold worth waiting for.

*Working:* X_n = S_n - c*n is a supermartingale: E[X_{n+1} | F_n] = X_n - c < X_n, because the walk is symmetric (E[step] = 0) and the cost is deterministic. For any stopping time with E[tau] < infinity, Wald's identity gives E[S_tau] = 0, so E[S_tau - c*tau] = -c*E[tau] <= 0, with equality only if tau = 0 a.s. Stopping times with E[tau] = infinity do not help: the classic candidate 'wait until the walk first hits +a' does reach +a with probability 1, but its expected hitting time is infinite, so the expected accumulated cost is infinite and the expected payoff is -infinity. Hence sup over stopping times of E[S_tau - c*tau] = 0, attained by stopping at once. The intuition worth voicing: a symmetric random walk gives you a free option on wandering up, but that option has zero drift and you are paying rent on it. The problem only becomes interesting if (i) the walk has drift mu > 0, in which case waiting pays iff mu > c and the answer changes character, (ii) the cost is a discount factor rather than a linear charge, or (iii) the horizon is finite and the payoff is convex — e.g. max(S_tau, 0) — in which case a threshold rule is optimal.

*Assumption:* Symmetric +/-1 (or any zero-mean, finite-variance) steps, a strictly positive cost c per step, and a payoff linear in the position. If the intended cost were zero the question would be degenerate (no optimal rule exists).

<sub>numerically verified — `CHECK V0(c=0.5,0.1,0.01) = 0.000000, 0.000000, 0.000000 vs 0 (stop immediately)`</sub>

<sub>Source: interview_review_db · 2025-11-12 · [link](https://www.wallstreetoasis.com/company/maven-securities/interview)</sub>

---

### 4. `MAVEN-005` · `B` · internship · phone_technical · 2025

You quote both a bid and an ask on a product whose fair value jumps up or down randomly every second. Given that informed traders are more likely to hit your quotes when the fair value moves against you, how do you design a quoting strategy to avoid being picked off

**Answer:** Model answer. Frame it as: expected P&L = (spread captured on uninformed flow) - (adverse selection paid to informed flow) - (inventory risk). Your quote is a free option you have written to the market; the whole job is pricing that option and shortening its life. 1) Price the adverse selection into the spread. Glosten-Milgrom: the correct bid is not E[V], it is E[V | someone sells to me] — the arrival of a trade is itself information, so a rational spread already embeds the update. If a fraction alpha of flow is informed and the fair value jumps by J when they trade, you need a half-spread of roughly alpha*J/(1-alpha) just to break even; estimate alpha and J from your own fills rather than guessing. 2) Measure, do not intuit: markouts. For every fill, compute signed P&L against the mid at +1s, +10s, +60s. Systematically negative markouts mean you are being picked off; slice them by venue, counterparty, size and time of day, and widen or withdraw exactly where they are bad. This is the single most concrete thing to say. 3) Shorten the option's life: requote and cancel fast off the fastest fair-value input you have (the lead venue or the future, book imbalance, correlated products). Most pick-offs are stale quotes, not clever adverse selection. 4) Skew instead of only widening. Lean the quote away from the direction you fear and toward flattening inventory (Avellaneda-Stoikov: quote around a reservation price mid - q*gamma*sigma^2*(T-t) rather than the mid). A one-sided quote is often better than a symmetric wide one. 5) Manage size: small at the touch, depth layered away from it, because your worst fills are your biggest ones. Cap inventory and hedge the residual in the most liquid correlated instrument. 6) State the trade-off explicitly: quoting too wide is also a losing strategy — you get no fills and earn no spread. You are maximising expected P&L, not minimising the number of bad trades.

*Working:* What is being tested: do you understand that a resting quote is a written option and that getting filled is bad news (winner's curse / asymmetric information), can you name concrete levers rather than one generic answer, and do you think in terms of measurement. A weak answer is just 'widen the spread'. A strong answer names the spread/skew/size/speed levers, proposes markout analysis as the feedback loop, and closes the loop by noting that widening has a cost too. No verify_code, because this is an open strategy-design question with no single computable quantity — the numbers would depend entirely on an assumed flow model.

<sub>guidance, no single correct value</sub>

<sub>Source: interview_review_db · 2025-11-12 · [link](https://www.wallstreetoasis.com/company/maven-securities/interview)</sub>

---

### 5. `MAVEN-006` · `B` · internship · phone_technical · 2025

You observe a sequence of coin flips, but you do not know whether the coin is fair or biased. You have a small prior belief that it may be biased. After seeing several flips that look suspicious, how would you decide whether the coin is likely biased?

**Answer:** Model answer: treat it as model comparison, not eyeballing. Posterior odds = prior odds x Bayes factor. With a point alternative (say the biased coin has p = 0.7) and h heads in n flips, BF = p^h (1-p)^(n-h) / 0.5^n. With a composite alternative p ~ Beta(a,b), the marginal likelihood is B(a+h, b+n-h)/B(a,b), so under a uniform prior BF = [h!(n-h)!/(n+1)!] / 0.5^n. Concrete example: prior P(biased) = 1%, alternative p = 0.7, data = 8 heads in 10. BF = 0.7^8*0.3^2/0.5^10 = 5.31, posterior odds = (1/99)*5.31 = 0.0537, so P(biased | data) = 5.1%. Under the uniform-p alternative the same data gives BF = 2.07 — essentially nothing. So the honest answer is 'not yet': ten flips cannot overcome a 1% prior. At an 80%-heads rate you need about 28 flips to push a 1% prior past 50%; to detect a 55/45 coin at all you need roughly 800 flips (5% level, 80% power). Two traps to name unprompted: (a) you only started looking because the sequence looked odd — that is post-hoc selection, and the honest correction is the number of sequences you could have flagged; (b) 'suspicious' patterns are normal — in 100 fair flips a run of 6 or more identical outcomes appears with probability 0.807. Also pick the statistic to match the alternative you care about (head count for a biased p, a runs test for serial dependence — a coin alternating HTHTHT has p = 0.5 and is obviously rigged), and if you intend to stop as soon as the evidence looks good, use a sequential test (SPRT or e-values), because optional stopping invalidates fixed-sample p-values.

*Working:* What is being tested: can you convert a vague 'looks suspicious' into a likelihood ratio, do you respect the prior, do you know that small samples move small priors very little, and are you alert to the selection effect that generated the question. The numbers above are the shape of a strong answer; the interviewer usually pushes with 'how many flips would you need?', so have the order of magnitude ready.

*Assumption:* The prior (1% biased), the alternative (p = 0.7) and the data (8 heads in 10) are my own illustrative choices — the question gives no numbers, so the answer is a method plus a worked instance.

<sub>numerically verified — `CHECK LR=5.3128 post_mc=0.05063 BF_unif=2.0687 n_needed=27.5 P(run>=6 in 100)=0.807 vs LR=5.3128 post=0.05093 BF=2.0687 n=27.5 0.807`</sub>

<sub>Source: interview_review_db · 2025-11-12 · [link](https://www.wallstreetoasis.com/company/maven-securities/interview)</sub>

---

### 6. `MAVEN-003` · `B` · new_grad · phone_technical · 2022

Tell me about the current SP500 price. What will be the new price if it increases by 10%, and another 10% again. If we decrease the value by 10% and another 10% will we derive the same price as the original one?

**Answer:** Two successive +10% moves multiply the price by 1.1^2 = 1.21, i.e. +21%, not +20%. Then two successive -10% moves multiply by 0.9^2 = 0.81, giving 1.21 * 0.81 = 0.9801 times the original — so NO, you do not get back to the original price; you end 1.99% below it. (Two -10% moves applied to the original alone give 0.81P, i.e. -19%, not -20%.) Worked with a round P = 6,000: 6,600 -> 7,260 -> 6,534 -> 5,880.60. For the S&P level itself: quote the actual index level on the day, to within a percent or two — I have no live market data, so I will not state a level here.

*Working:* Percentage changes compound multiplicatively, not additively. An up-x then down-x pair gives (1+x)(1-x) = 1 - x^2 < 1, so any symmetric round trip loses x^2 of value: here 1 - 0.01 = 0.99 per pair, and 0.99^2 = 0.9801 for two pairs. The gap is the arithmetic-vs-geometric-mean point that matters for return series: a portfolio that does +10%/-10% repeatedly bleeds ~0.5% per round trip, which is why you compound log returns (ln 1.1 + ln 0.9 = -0.01 < 0) and why volatility drags on compounded returns. To get back to P after a -10% you need +11.1%, not +10%.

*Assumption:* The market-level part of this question is date-dependent and cannot be answered from a static answer key; only the arithmetic is checkable, and that is what I answer. In the interview, knowing the current index level (and roughly where it opened, and the past month's range) is the actual test.

<sub>numerically verified — `CHECK up=121/100 round_trip=9801/10000(0.9801) down_only=81/100 vs 1.21P, 0.9801P (-1.99%), 0.81P`</sub>

<sub>Source: interview_review_db · 2022-11-02 · [link](https://www.wallstreetoasis.com/company/maven-securities/interview)</sub>

---


## Da Vinci Derivatives  (5)

### 1. `DAVINCI-005` · `B` · new_grad · phone_technical · interviewed February 2025

What's your intuition about delta of an ATM option if the implied volatility to becomes very, very, very large?

**Answer:** Call delta -> 1 (and put delta -> 0).

*Working:* Delta = N(d1) with d1 = [ln(S/K) + (r + sigma^2/2)T] / (sigma sqrt(T)). At the money the log term vanishes, so d1 = (r sqrt(T))/sigma + sigma sqrt(T)/2 -> +infinity as sigma -> infinity, hence N(d1) -> 1. Simultaneously d2 = d1 - sigma sqrt(T) -> -infinity, so N(d2) -> 0 and the call price S N(d1) - K e^{-rT} N(d2) -> S: the option becomes the stock. Intuition: with unbounded volatility the terminal lognormal is so dispersed that the strike is irrelevant relative to the spread of outcomes, so the call is just a claim on the stock and must hedge one-for-one. (Note the lognormal quirk: as sigma -> infinity the stock ends up near zero with probability -> 1, and all the value sits in the vanishingly rare enormous outcomes.) By parity the put delta = N(d1) - 1 -> 0 and the put -> K e^{-rT}.

*Assumption:* Black-Scholes, no dividends, ATM in the spot sense S = K.

<sub>numerically verified — `CHECK deltas=[0.5398, 0.6915, 0.9938, 1.0, 1.0] call_price_at_sig=100 -> 100.0000 (spot=100) vs claimed delta -> 1 and price -> S`</sub>

<sub>Source: interview_review_site · 2025-03-14 · [link](https://www.wallstreetoasis.com/company/da-vinci-derivatives/interview)</sub>

---

### 2. `DAVINCI-002` · `B` · new_grad · phone_technical · interviewed February 2025

rapid fire questions such as "What's your favorite color?", "What's 6 * 76?", more rapid fire questions and then "What's the prodcut you got minus 263?

**Answer:** 6 x 76 = 456; 456 - 263 = 193.

*Working:* 6 x 76 = 6 x 70 + 6 x 6 = 420 + 36 = 456. Then 456 - 263: 456 - 200 = 256, 256 - 63 = 193. The point of the format is that the joke questions in between are deliberate interference - the thing being tested is whether you can hold 456 in working memory while answering 'what's your favourite colour?' and then subtract cleanly. Answer crisply; if you have genuinely lost the number, say so rather than guessing.

<sub>numerically verified — `CHECK 6*76=456 and 6*76-263=193 vs claimed 456 and 193`</sub>

<sub>Source: interview_review_site · 2025-03-14 · [link](https://www.wallstreetoasis.com/company/da-vinci-derivatives/interview)</sub>

---

### 3. `DAVINCI-004` · `B` · new_grad · phone_technical · interviewed March 2021

Question like: 8/17 till 4th precision. Follow up question tell me now 5th decimal along with previous 4. That means memory + precision. Now asked my confidence on answer if I was willing to gamble my interview result on that?

**Answer:** 8/17 = 0.470588235294117647... (repeating block of 16 digits). To 4 dp: 0.4706. The 5th decimal digit is 8, so to 5 dp: 0.47059.

*Working:* 1/17 = 0.0588235294117647...; multiply by 8 to get 0.470588235294117647.... The digits after the point are 4,7,0,5,8,8,2,3,5,... so truncating at four gives 0.4705 but the next digit is 8, so the correctly rounded 4-dp value is 0.4706, and the 5-dp value is 0.47059. Fast mental route: 8/17 = 1/2 - (1/2)/17 = 0.5 - 0.0294118 = 0.4705882. On the confidence follow-up: the honest play is to separate the digits you derived from the ones you are extrapolating - offer a calibrated probability (e.g. 'certain on 0.4705, ~90% on the 8') rather than accepting an all-or-nothing bet on digits you did not actually compute.

<sub>numerically verified — `CHECK 8/17=0.470588235294117647... round4=0.4706 round5=0.47059 fifth_digit=8 vs claimed 0.470588235294117647..., 0.4706, 0.47059, 8`</sub>

<sub>Source: interview_review_site · 2021-05-03 · [link](https://www.wallstreetoasis.com/company/da-vinci-derivatives/interview)</sub>

---

### 4. `DAVINCI-001` · `B` · internship · unknown · interviewed August 2024

you are tossing a dice and keeping track of the cumulative sum. what is the probability of ever getting total sum x(for x = 3,4). then asked for what value of x is this probability maximum.

**Answer:** P(ever hit 3) = 49/216 ~ 0.2269; P(ever hit 4) = 343/1296 ~ 0.2647. In general p_n = 7^(n-1)/6^n for 1 <= n <= 6. The maximum over x >= 1 is at x = 6, with p_6 = 16807/46656 ~ 0.3601.

*Working:* Let p_n = P(the running total ever equals n), p_0 = 1, and condition on the last roll: p_n = (1/6) sum_{k=1..6} p_{n-k}. For n <= 6 the sum is just p_0 + ... + p_{n-1}, which telescopes to p_n = 7^(n-1)/6^n: p_1 = 1/6, p_2 = 7/36, p_3 = 49/216, p_4 = 343/1296, p_5 = 2401/7776, p_6 = 16807/46656. p_6 ~ 0.3601 is the peak because it is the largest n for which every one of the six predecessors includes the certain state p_0 = 1; from n = 7 on, p_7 = (7 p_6 - 1)/6 ~ 0.2536 and the sequence oscillates down to the renewal limit 1/E[roll] = 1/3.5 = 2/7 ~ 0.2857, never returning above p_6.

*Assumption:* Fair six-sided die, rolled indefinitely; x = 0 is excluded as trivial (the empty sum is 0 with probability 1).

<sub>numerically verified — `CHECK p3=49/216(0.2269 mc 0.2273) p4=343/1296(0.2647 mc 0.2642) argmax=6 p6=16807/46656(0.3602 mc 0.3599) p7=0.2536(mc 0.2541) limit=0.2857 vs claimed`</sub>

<sub>Source: interview_review_site · 2025-11-21 · [link](https://www.wallstreetoasis.com/company/da-vinci-derivatives/interview)</sub>

---

### 5. `DAVINCI-003` · `B` · internship · unknown · interviewed August 2024

4 cards on a table of value 10, 20, 30, 40 face down and shuffled. you can either pick card or get 25. how to max your score ? what is exp value of the game ?

**Answer:** Depends on the exact game, which the recollection leaves open; all three readings computed: (i) blind pick vs a sure 25 -> EV 25 either way, you are indifferent; (ii) turn one card over, then choose between it and the 25 -> keep a 30 or 40, take the 25 over a 10 or 20, EV = (25+25+30+40)/4 = 30; (iii) turn cards one at a time with the right to reject and continue -> reject everything until the 40 shows (if it never shows earlier you are forced onto the last card, which is then the 40), so you get 40 with certainty, EV 40, and the 25 is never worth taking.

*Working:* (i) mean of {10,20,30,40} = 100/4 = 25, exactly the outside option. (ii) average of max(card, 25) = (25+25+30+40)/4 = 30. (iii) because you know the deck contains exactly one 40, holding out for it guarantees 40; backward induction confirms V(S) = max(S) for every subset S, so the sequential game is worth 40 with no variance at all.

*Assumption:* Which of the three games was meant. The literal 'you can either pick a card or get 25' is reading (i), but then 'how to max your score' has no content, which is why (ii) and (iii) are live candidates. Reading (ii) is the one in which the 25 actually matters strategically.

<sub>numerically verified — `CHECK blind_pick=25 see_then_choose=30 sequential=40 (brute 40) vs claimed 25, 30, 40` · confidence: **low**</sub>

<sub>Source: interview_review_site · 2025-11-21 · [link](https://www.wallstreetoasis.com/company/da-vinci-derivatives/interview)</sub>

---


## Squarepoint Capital  (4)

### 1. `SQP-001` · `B` · unknown · onsite · 2024

Assumptions of linear regression, correlation can be negative intra-month but positive across a year, how?

**Answer:** Assumptions: linearity in the parameters, exogeneity E[eps|X] = 0, no perfect multicollinearity, homoskedastic errors, uncorrelated errors (no autocorrelation), and - only for exact small-sample t/F inference - normal errors. The sign flip is an aggregation effect: within each month a common monthly level/factor is held roughly fixed so only the idiosyncratic parts are compared (they move against each other), while pooling or aggregating across the year lets the shared month-to-month drift dominate, and that drift is common to both series, so the correlation turns positive.

*Working:* This is Simpson's paradox for correlations: the pooled correlation is a mixture of the within-group (demeaned by month) covariance and the between-group covariance of the monthly means. Write X = m + e, Y = m - e with m the common monthly level, sd 3, and e idiosyncratic, sd 1. Within any month m is constant so Y = 2m - X and the correlation is exactly -1; pooled over the year the correlation is (var(m) - var(e))/(var(m) + var(e)) = (9-1)/(9+1) = +0.8. Two other mechanisms worth naming: temporal aggregation with lead-lag cross-autocorrelation (the correlation of summed returns is not the correlation of the components, so a positive lagged cross-correlation can flip the sign of the aggregate even with a negative contemporaneous one), and a common trend / non-stationarity in both series. The practical implication: state your horizon, and decide whether you want the within-month (fixed-effects / demeaned) estimate or the pooled one - a regression with month dummies recovers the negative relationship.

*Assumption:* Reading 'correlation between two series' at two different levels of grouping/horizon; the two effects that produce the flip (grouping and time-aggregation) are given separately since the recollection does not say which is meant.

<sub>numerically verified — `CHECK (-1.0, 0.722, True) vs (-1.0, 'positive', True)`</sub>

<sub>Source: interview_review_db · 2026-05-31 · [link](https://www.wallstreetoasis.com/company/squarepoint-capital/interview)</sub>

---

### 2. `SQP-005` · `B` · unknown · phone_technical · 2025

If nx(n-1)/2 is the sum of 1,2,3,...n what is the equation for 1^2,2^2,3^2,....n^2

**Answer:** 1^2 + 2^2 + ... + n^2 = n(n+1)(2n+1)/6

*Working:* Telescope (k+1)^3 - k^3 = 3k^2 + 3k + 1 from k = 1 to n: (n+1)^3 - 1 = 3*sum k^2 + 3*n(n+1)/2 + n, so sum k^2 = [(n+1)^3 - 1 - n - 3n(n+1)/2]/3 = n(n+1)(2n+1)/6. Note the premise as recollected is off by one: the sum 1+2+...+n is n(n+1)/2, not n(n-1)/2 (n(n-1)/2 is the sum of the first n-1 integers, i.e. C(n,2)). Under that stated formula the analogous 'shifted' answer would be (n-1)n(2n-1)/6, which is the sum of squares up to (n-1)^2 - worth flagging rather than silently answering the wrong question.

*Assumption:* Assumed the intended premise is the standard sum 1+...+n = n(n+1)/2 and the question asks for the sum of the first n squares.

<sub>numerically verified — `CHECK (199, True, True) vs (199, True, True)`</sub>

<sub>Source: interview_review_db · 2025-05-21 · [link](https://www.wallstreetoasis.com/company/squarepoint-capital/interview)</sub>

---

### 3. `SQP-004` · `B` · internship · superday · 2025

You are basically handed a dataset, and you are ask to both analyse it and construct a predictive model from it. After that, you present your result to a researcher for one hour.

**Answer:** There is no single right model. They are grading the research process: framing the prediction problem, honest validation, and whether you can defend your choices for an hour. Deliver a simple, correctly validated baseline you fully understand rather than a complicated model you cannot interrogate.

*Working:* Shape of a strong submission: (1) Frame it - state the target, the horizon, the unit of observation and the metric before modelling, and say what a useful edge would look like. (2) EDA that earns its place - missingness, outliers and their cause, stationarity, whether observations are IID or a time series, duplicates and leakage-prone columns. (3) Split correctly - for anything with a time index use a forward-chaining / purged split with an embargo, never random k-fold, and never fit any transform (scaling, imputation, target encoding) outside the training fold. (4) Baseline first - the mean/last-value predictor, then a regularised linear model, and only then gradient boosting; report the improvement over the baseline, not the raw score. (5) Quantify uncertainty - error bars across folds or blocks, and a clear statement of whether the improvement is inside the noise. (6) Interrogate the model - the most important features, whether their signs make sense, where it fails, and how performance decays out-of-sample. In the presentation, lead with the conclusion and the caveat, keep the derivation in the appendix, say plainly what you would do next with more time, and never oversell: 'this is inside the noise' is a strong answer. The single most common failure they are looking for is leakage - a future-looking feature or a scaler fit on the whole dataset - so call out explicitly how you ruled it out.

*Assumption:* Read as the Squarepoint superday take-home: an open dataset, a predictive model, and a one-hour discussion with a researcher.

<sub>guidance, no single correct value · confidence: **medium**</sub>

<sub>Source: interview_review_db · 2026-07-07 · [link](https://www.wallstreetoasis.com/company/squarepoint-capital/interview)</sub>

---

### 4. `SQP-002` · `C` · unknown · phone_technical · unknown

python 八股:1. tuple Vs. list 2. pass by reference Vs. pass by value? 3. difference between is and ==?

*English:* Python fundamentals drill: 1. tuple vs list 2. pass by reference vs pass by value? 3. difference between is and ==?

**Answer:** (1) A tuple is immutable and fixed-length, hashable when its elements are (so it can be a dict key or set member), and semantically a heterogeneous record; a list is mutable, growable with amortised O(1) append thanks to over-allocation, unhashable, and semantically a homogeneous sequence. (2) Neither: Python is call-by-object-reference ('call by sharing') - the callee gets a new local name bound to the caller's object, so in-place mutation of a mutable argument is visible to the caller but rebinding the parameter is not. (3) `is` tests object identity (same id()), `==` tests value via __eq__; use `is` only for singletons like None, True/False and sentinels.

*Working:* What they are probing: whether you understand Python's object model rather than reciting a table. Worth adding on each - tuples let CPython constant-fold and are marginally smaller/faster to construct, and immutability is what makes them safe as keys and as return values; the mutability question is best answered with the two-function demo (a.append(4) escapes, a = [0] does not), and the same reasoning explains why ints and strings 'look' pass-by-value (they are immutable, so you can only rebind); for `is` vs `==`, the classic traps are small-int caching and string interning making `is` accidentally work for -5..256, `nan != nan` while `nan is nan`, and libraries such as numpy/pandas overriding `==` to return elementwise arrays so `if x == y` raises.

*Assumption:* CPython semantics.

<sub>numerically verified — `CHECK (10, 10) vs (10, 10)`</sub>

<sub>Source: forum_recall_zh · unknown · [link](https://www.1point3acres.com/bbs/collection/253315)</sub>

---


## Virtu Financial  (4)

### 1. `VIRTU-004` · `B` · new_grad · phone_technical · interviewed January 2026

How to make a market/how market-making trading works

**Answer:** Model answer. A market maker quotes a two-sided price - a bid and an offer around their estimate of fair value (the theo) - and earns the spread by buying from sellers and selling to buyers, while taking on inventory risk in between. The mechanics: (1) compute a theo from everything you can observe - the order book microprice, correlated instruments, futures/ETF vs constituents, the option's underlying; (2) set the spread wide enough to cover adverse selection, expected hedging cost, fees and the risk of stale quotes; (3) skew the quote to manage inventory - if you are long, drop both bid and offer so you are more likely to sell than buy; (4) size according to conviction and risk limits, quoting smaller where you are less sure; (5) hedge residual risk (delta-hedge options, trade the correlated leg); (6) pull or widen when flow looks toxic or news is imminent, because the trader hitting you may know something. P&L = spread captured * volume - losses to informed traders - inventory P&L - fees. If they say 'make me a market in X': state a bid and an offer, keep the width honest about your uncertainty (wide is fine if you can defend it), never quote a market you would not trade both sides of, and when they trade with you, update - being lifted means your market was too low, so raise it. Being run over repeatedly without moving your price is the single fastest way to fail this exercise.

*Working:* They are testing whether you understand that the edge is the spread, that the cost is adverse selection and inventory, and - most of all - whether you update on the information content of a trade. The interviewer will usually trade against you and see if you move.

<sub>guidance, no single correct value</sub>

<sub>Source: interview_review_site · 2026-05-01 · [link](https://www.wallstreetoasis.com/company/virtu-financial/interview)</sub>

---

### 2. `VIRTU-002` · `B` · unknown · phone_technical · interviewed October 2025

What is the best way to get/estimate median from given number list with some statistics?

**Answer:** There is no single best way - pick by regime. (a) List in memory, exact: Quickselect / introselect (numpy.partition, C++ nth_element) is O(n) expected, O(n^2) worst; median-of-medians gives O(n) worst-case with a worse constant. Sorting is O(n log n) and only worth it if you need other order statistics too. (b) Streaming, exact: two heaps - a max-heap of the lower half and a min-heap of the upper half, rebalanced to differ by at most one - gives O(log n) per insert and O(1) query; an order-statistic tree also works and supports deletion. (c) Very large or distributed, approximate: a random sample of size m has sample median with asymptotic variance 1/(4*f(median)^2*m), independent of n, so m = 10^4 is already accurate and costs nothing in n; or use a streaming sketch - P^2 (constant memory), t-digest (accurate in the tails), or Greenwald-Khanna with an epsilon guarantee in O((1/eps)log(eps*n)) space. A two-pass histogram (bucket, then refine inside the median bucket) is often the simplest thing that works on disk-scale data. (d) The statistics point they are usually fishing for: the median minimises E|X - c|, has a 50% breakdown point, and for Gaussian data its asymptotic relative efficiency versus the mean is 2/pi = 0.64 - so with clean near-normal data the mean is a better location estimate, and you reach for the median when tails are heavy or outliers are real.

*Working:* Algorithms-plus-statistics question. The interviewer wants you to ask 'how big is the data, does it fit in memory, is it streaming, do you need exact?' before answering. Saying 'sort it' is not wrong but stops at O(n log n) when O(n) selection exists; the strong answer names quickselect, the two-heap streaming structure, and a sampling/sketch option with an accuracy statement. Verification below checks the recommended quickselect against a sorted median on 20,000 random arrays (including ties and even lengths) and confirms the sampling variance claim against the exact result Var = 1/(4(n+2)) for the median of n uniforms.

*Assumption:* Numeric data; 'median' of an even-length list = mean of the two central values.

<sub>numerically verified — `CHECK quickselect_mismatches=0/20000 median_var_mc=0.035691 vs claimed 0 mismatches and exact Var=1/(4(n+2))=0.035714`</sub>

<sub>Source: interview_review_site · 2026-01-20 · [link](https://www.wallstreetoasis.com/company/virtu-financial/interview)</sub>

---

### 3. `VIRTU-006` · `B` · new_grad · phone_technical · interviewed February 2025

Some questions about financial markets. Like who are market makers? Also some brain teasers, quite easy.

**Answer:** Market makers are liquidity providers: firms that continuously quote both a bid and an offer in an instrument, earning the bid-ask spread in exchange for taking on inventory risk and the risk of trading against better-informed counterparties. Modern examples are electronic proprietary firms - Virtu, Citadel Securities, Jane Street, SIG, Optiver, IMC, Flow Traders - trading their own capital, as distinct from brokers (agents executing client orders for commission), asset managers and hedge funds (taking directional or relative-value risk for investors). Some exchanges formalise the role - NYSE Designated Market Makers and options-exchange primary market makers accept obligations to quote a minimum size for a minimum share of the day within a maximum spread, in return for fee rebates and informational privileges. In US equities much retail flow never reaches an exchange: wholesalers internalise it and pay for order flow, which is profitable precisely because retail flow is relatively uninformed. Economically they supply immediacy and contribute to price discovery, and the competition among them is why spreads and retail transaction costs have collapsed. Their risks are inventory, adverse selection, latency and technology failure (Knight Capital in 2012 is the standard cautionary tale).

*Working:* Knowledge screen - they want to know you understand the business you are applying to and can distinguish a market maker from a broker or a hedge fund. Naming the two-sided quote, the spread as revenue, and adverse selection as the cost covers the substance; the DMM obligations and PFOF details show you have read beyond the surface. For the 'easy brain teasers' part: work out loud, state assumptions, and give a number - they are watching your process under mild time pressure, not checking arithmetic.

<sub>guidance, no single correct value</sub>

<sub>Source: interview_review_site · 2025-02-27 · [link](https://www.wallstreetoasis.com/company/virtu-financial/interview)</sub>

---

### 4. `VIRTU-001` · `B` · unknown · phone_technical · interviewed March 2025

Length of every edge of a cube is twice as long. How much does the volume grow?

**Answer:** Volume grows by a factor of 8 (an increase of 700%). Surface area grows 4x, edge length 2x.

*Working:* Volume scales as the cube of a linear dimension: (2s)^3 = 8s^3, independent of the original edge length. The trap is answering '8 times bigger' when asked 'how much does it grow' - if growth means the increase, it is +700%, i.e. 7 times the original volume is added. Worth stating both.

<sub>numerically verified — `CHECK ratio=8 increase=700% vs claimed=8 (a 700% increase)`</sub>

<sub>Source: interview_review_site · 2025-04-13 · [link](https://www.wallstreetoasis.com/company/virtu-financial/interview)</sub>

---


## Akuna Capital  (3)

### 1. `AKUNA-005` · `B` · unknown · phone_technical · unknown

Make me a market for the Chicago metro area. How much would you risk to win $100 if the real answer is in your market?

**Answer:** No single number - the deliverable is a market plus a consistent risk size. Clarify the metric first; for population of the Chicago-Naperville-Elgin MSA (~9.3-9.6 million) quote 9.0 at 10.0 million, i.e. a 1.0 million-wide market. Risk sizing: if you believe with probability p that the truth is inside your market, the break-even stake to win $100 is R* = 100p/(1-p). At p = 0.8, R* = $400, so risk clearly less than that - around $200 - to leave room for being overconfident.

*Working:* Two separate skills are being tested. (1) Anchoring: Chicago city proper is ~2.7m, the MSA is roughly 3x that, and as a sanity check the MSA is ~3% of the ~335m US population - so ~9.5m. A 1m-wide market around 9.5m is tight enough to look confident and wide enough to survive. (2) Coherence between the width you quoted and the money you will put behind it: risking R to win $100 is +EV iff 100p > (1-p)R, i.e. R < 100p/(1-p). Quoting a wide market and then refusing to risk anything, or quoting a tight market and risking a lot, is the failure mode they are looking for. Say the number, say your probability, and derive the stake from it out loud.

*Assumption:* 'The Chicago metro area' does not specify a quantity. I assume MSA population. If they mean land area, the MSA is ~10,900 sq mi and the same risk-sizing logic applies unchanged.

<sub>guidance, no single correct value · confidence: **medium**</sub>

<sub>Source: wso · 2025-10-30 · [link](https://www.wallstreetoasis.com/company/akuna-capital-llc/interview)</sub>

---

### 2. `AKUNA-009` · `B` · unknown · phone_technical · unknown

We are playing a game where we roll two dice. You win if you roll a 10, how much would you risk to win $100?

**Answer:** Break-even stake = $100/11 = $9.09 (approx). You would risk somewhat less than that - quote around $8 - to have edge.

*Working:* Two dice sum to 10 in 3 of 36 ways (4-6, 5-5, 6-4), so p = 1/12 and the true odds are 11 to 1 against. Fair stake R solves (1/12)(100) = (11/12)R, giving R = 100/11 = 9.0909... Anything below that is +EV for you, anything above is -EV.

*Assumption:* 'Roll a 10' means the two dice sum to 10, and 'win $100' means $100 of net profit on top of your returned stake. Under the other reading - $100 is the total returned, so profit is 100 - R - the fair stake is 100 x (1/12) = $8.33.

<sub>numerically verified — `CHECK p=1/12 R=100/11 EV=0 vs claimed p=1/12 R=100/11 EV=0`</sub>

<sub>Source: wso · 2025-10-30 · [link](https://www.wallstreetoasis.com/company/akuna-capital-llc/interview)</sub>

---

### 3. `AKUNA-010` · `B` · unknown · phone_technical · unknown

I don’t remember the exact question, but it was along the lines of two separate games that have the same expected value which one would you choose?

**Answer:** Equal EV means EV is not the deciding variable: choose on risk-adjusted terms. Single play with a stake that matters relative to your bankroll - take the lower-variance game (concave utility / Kelly, which maximises expected log wealth and so penalises variance). Prefer whichever EV you trust more, i.e. the one with the smaller estimation error. Take the higher-variance game only when variance is worth something to you: you must clear a threshold, the downside is capped or optional, or the payoff diversifies an existing book.

*Working:* The interviewer wants to hear that you look past the first moment. Points worth raising, roughly in order of value: variance and the Sharpe-style ratio EV/sigma; skew and tail/ruin risk (repeated play makes the mean dominate by LLN, but only if you cannot be wiped out first); capital and margin usage per unit of EV; correlation with what you already hold; model uncertainty - a 'known' EV and a 'guessed' EV are not the same object; and adverse selection: if someone is offering you the choice, ask why. Concrete framing that lands well: I would take the low-variance game repeatedly and size up, rather than the high-variance one once.

*Assumption:* The question is a candidate's paraphrase with no payoff details, so I answer the general principle rather than a specific pair of games.

<sub>guidance, no single correct value</sub>

<sub>Source: wso · 2025-05-08 · [link](https://www.wallstreetoasis.com/company/akuna-capital-llc/interview)</sub>

---


## Mako Global  (3)

### 1. `MAKO-003` · `B` · unknown · onsite · 2021

you buy a near term expiry straddle and short a longer term expiry straddle, what are the various greeks on this spread, what happens to these greeks if underlying sharply moves up throughout the day

**Answer:** This is a reverse (short) calendar spread. At inception with both struck at spot: delta ≈ 0 (very slightly negative), gamma POSITIVE, theta NEGATIVE, vega NEGATIVE, rho small and negative; you are long front vol / short back vol, i.e. long the slope of the term structure. Worked example (S = K = 100, sigma = 20%, r = 0, long 30-day straddle vs short 180-day straddle, 1×1): delta −0.03, gamma +0.082, vega −33.0 per 1.00 of vol (−0.33 per vol point), theta −16.5 per year (≈ −0.045/day). After a sharp rally the same day: delta turns POSITIVE (+0.27 at S = 115) because the front straddle's delta races towards +1 far faster than the back's; gamma COLLAPSES AND FLIPS NEGATIVE (−0.022 at S = 115, crossing zero at about S = 108.8, a ~9% move) because the front option is now far from its strike with little time left while the back still has gamma at that strike; vega becomes MORE negative (−35.3) as the front's vega evaporates and the back's persists; and theta FLIPS POSITIVE (+5.9/yr) since you are now short a still-fat back straddle and long a nearly worthless front one.

*Working:* Vega scales like sqrt(T) so the longer leg dominates it (short vega); gamma scales like 1/sqrt(T) so the shorter leg dominates it (long gamma); theta must have the opposite sign to gamma when r = 0. The one nuance worth volunteering: struck exactly at SPOT each straddle is slightly delta-long, because d1 = sigma·sqrt(T)/2 > 0, and the back leg more so — hence the small negative starting delta; struck at each leg's zero-delta strike S·exp(sigma^2·T/2) the spread starts exactly delta-flat. The punchline for the interviewer: this position wants realised vol to be high but LOCAL — chop around the strike. A big directional move first pays you (you are long gamma near the strike) and then turns on you once you cross into short gamma, and you end up short gamma and short vega precisely after a move that has probably lifted implieds.

*Assumption:* 1×1 ratio, both straddles struck at the same strike (taken at spot), European options, Black–Scholes with r = 0 and no dividends, both legs at the same implied vol; 'sharply up throughout the day' is taken as a same-day spot move with time to expiry essentially unchanged.

<sub>numerically verified — `CHECK (at S=100 delta=-0.0331 gamma=+0.0824 vega=-33.0 theta=-16.5; zero-delta-strike version delta=1.9e-15 | at S=115 delta=+0.273 gamma=-0.0222 vega`</sub>

<sub>Source: interview_review_db · 2022-02-23 · [link](https://www.wallstreetoasis.com/company/mako-global/interview)</sub>

---

### 2. `MAKO-002` · `B` · new_grad · onsite · 2008

what's your bid and offer in the orange/apple 1by 2?

**Answer:** Model answer (the interpretation matters, so state it before you quote). A '1 by 2' is a ratio spread: long 1 orange, short 2 apples, so the thing being priced is V = P(orange) − 2·P(apple). Work it out loud: an apple is about 30p and an orange about 40p, so fair value ≈ 40 − 60 = −20p. Uncertainty: if each leg is worth ±10p then the combination's standard deviation is roughly sqrt(10^2 + 2^2·10^2) ≈ 22p, so your market must be wide: quote something like '−35 bid at −5, ten up', and tighten to '−30 at −10' only if pressed. Then show the mechanics they are actually grading: ask for units and size before quoting; never show a crossed or inverted market; quote both sides you are genuinely happy to trade; and if you get hit or lifted, MOVE — a fill is information, so shade the mid away from the side that traded and re-quote. Add the risk observation: a 1-by-2 is not neutral, you are net short one unit of fruit, so if apple and orange prices are correlated you carry directional 'fruit' exposure as well as the relative-value view.

*Working:* Market-making questions grade the process, not the number: a stated fair value, a spread that honestly reflects your uncertainty, willingness to be traded on both sides, and updating on flow. The specific fruit prices are irrelevant — what is graded is that you widen when unsure, tighten when pressed but not past your edge, and adjust after being traded with.

*Assumption:* Real ambiguity: the terse recollection gives no context for what 'orange' and 'apple' are (prices, weights, or stand-in underlyings in a Mako trading game) or what a unit is. Taken here as a 1×2 ratio spread, long 1 orange versus short 2 apples, priced in pence at UK supermarket prices; if it is instead a 1×2 call ratio spread on a single underlying, the quoting framework is identical but the fair value would come from the two option prices.

<sub>guidance, no single correct value · confidence: **low**</sub>

<sub>Source: interview_review_db · 2013-05-02 · [link](https://www.wallstreetoasis.com/company/mako-global/interview)</sub>

---

### 3. `MAKO-001` · `B` · new_grad · superday · 2024

Who out of the other candidates would you pick for this job?

**Answer:** Model answer. Name one person, give concrete observed evidence, and own the choice. For example: 'X. In the market-making game she was the only one who widened her spread when the information got worse instead of trying to look confident, and after being lifted twice she moved her market immediately — she was managing risk rather than defending a number. Y got more arithmetic right and was quicker, and I considered him, but he never updated after being traded with, which matters more on a desk.' That structure — a specific person, a specific observed behaviour, and an honest acknowledgement of the runner-up and the trade-off — is the whole answer. Things to avoid: refusing to answer or naming everyone (reads as an inability to make an uncomfortable decision, which is the trait being tested); picking whoever you chatted to at lunch; picking the loudest person; running other candidates down personally — criticise decisions, not people. Do not nominate yourself. A good closing line: pick the person you would most want double-checking your risk at the end of a bad day.

*Working:* This is a judgement and self-awareness test with a social-pressure component: were you paying attention to anyone but yourself during the group exercises, can you make a decision that costs you something and defend it with evidence, and does your read on talent match the firm's? The content of the pick matters far less than that it is specific, evidence-based and delivered without squirming.

<sub>guidance, no single correct value</sub>

<sub>Source: interview_review_db · 2024-11-26 · [link](https://www.wallstreetoasis.com/company/mako-global/interview)</sub>

---


## D. E. Shaw  (2)

### 1. `DES-027` · `B` · unknown · phone_technical · unknown

You call to someone's house and ask if they have two children. The answer happens to be yes. Then you ask if one of their children is a boy. The answer happens to be yes again. What's the probability that the second child is a boy?

**Answer:** 1/3

*Working:* Equally likely ordered pairs BB, BG, GB, GG at 1/4 each. 'At least one is a boy' eliminates GG, leaving three equally likely cases, exactly one of which (BB) has the other child a boy. So the probability is 1/3. This is the standard boy-girl paradox: the question 'is one of them a boy?' returns yes for BG, GB and BB alike, so it does not single out a particular child.

*Assumption:* Each child independently a boy with probability 1/2, the parent answers truthfully, and 'the second child is a boy' means 'the other child is a boy', i.e. P(both are boys). Caveat worth flagging: read literally as the second-BORN child, the answer is 2/3, because the information 'at least one boy' is symmetric in birth order (P(younger is a boy | at least one boy) = (1/4+1/4)/(3/4) = 2/3). 1/3 is the intended answer, and it is the reading that makes the William follow-up (DES-049) interesting by contrast.

<sub>numerically verified — `CHECK both_boys=1/3 (mc 0.3333) other_reading_second_born=2/3 (mc 0.6662) vs claimed=1/3 (2/3 literal)` · confidence: **medium**</sub>

<sub>Source: blog · 2013-11-01 · [link](https://www.jointaro.com/interviews/companies/de-shaw/experiences/software-engineering-and-quantitative-research-new-york-ny-november-1-2013-no-offer-positive-af766cdc)</sub>

---

### 2. `DES-049` · `B` · unknown · phone_technical · unknown

You call to someone's house and ask if they have two children. The answer happens to be yes. Then you ask if one of their children's names is William. The answer happens to be yes again. (We assume William is a boy's name, and that it's possible that both children are Williams.) What's the probability that the second child is a boy?

**Answer:** (2 - p)/(4 - p), where p = P(a boy is named William). For a realistically rare name this is essentially 1/2 (p = 1% gives 0.4987); the intended answer is 1/2.

*Working:* Each child is a boy with probability 1/2 and each boy is independently named William with probability p. P(at least one William) = 1 - (1 - p/2)^2 = p - p^2/4. P(both boys AND at least one William) = (1/4)(1 - (1-p)^2) = (2p - p^2)/4. Dividing: (2-p)/(4-p). As p -> 0 this tends to 1/2; at p = 1 (every boy is called William) it collapses to 1/3, recovering DES-027, which is the consistency check on the formula. Intuition: a rare name is almost a unique identifier, so it effectively points at one specific child, and the other child is then an independent coin flip - unlike 'is one a boy?', which is a statement about the pair.

*Assumption:* p (the frequency of the name among boys) is not given; the intended reading is that William is rare, so p -> 0 and the answer is 1/2. Same convention as DES-027: 'the second child is a boy' = 'both children are boys'.

<sub>numerically verified — `CHECK formula_ok=True p=0.05 exact=0.493671 mc=0.494857 limit_p->0=1/2 vs claimed=(2-p)/(4-p) -> 1/2`</sub>

<sub>Source: blog · 2013-11-01 · [link](https://www.jointaro.com/interviews/companies/de-shaw/experiences/software-engineering-and-quantitative-research-new-york-ny-november-1-2013-no-offer-positive-af766cdc)</sub>

---


## DRW  (2)

### 1. `DRW-001` · `B` · unknown · onsite · unknown

How would you derive the Ordinary Least Squares?

**Answer:** beta_hat = (X'X)^{-1} X'y (for simple regression: beta_1 = Sxy/Sxx = Cov(x,y)/Var(x), beta_0 = ybar - beta_1 xbar).

*Working:* Minimise S(beta) = ||y - X beta||^2 = y'y - 2 beta'X'y + beta'X'X beta. Setting the gradient to zero, dS/dbeta = -2X'y + 2X'X beta = 0, gives the normal equations X'X beta_hat = X'y, hence beta_hat = (X'X)^{-1}X'y; the Hessian 2X'X is positive definite under full column rank, so this is the unique global minimum. Geometric version (worth giving in an interview): y_hat = X beta_hat is the orthogonal projection of y onto the column space of X, so residuals are orthogonal to every regressor, X'(y - X beta_hat) = 0, which is the same system. The estimator is also the MLE if eps ~ N(0, sigma^2 I), and Gauss-Markov makes it BLUE under E[eps|X] = 0 and Var(eps) = sigma^2 I - note that unbiasedness needs no normality assumption.

*Assumption:* X has full column rank; otherwise X'X is singular and one uses the Moore-Penrose pseudo-inverse (beta_hat is then not unique, though the fitted values still are).

<sub>numerically verified — `CHECK X'(y-Xb)=['0', '0', '0'] all_perturbations_worse=True vs claimed 0 vector and True (beta=(X'X)^-1X'y minimises SSE)`</sub>

<sub>Source: blog · 2024-10-01 · [link](https://www.jointaro.com/interviews/companies/drw/experiences/junior-ai-researcher-india-october-1-2024-no-offer-negative-efc70c78)</sub>

---

### 2. `DRW-002` · `C` · unknown · phone_technical · unknown

Expected value of coin flip game (easy) How many (5-card) hands are there that give you four of a kind? Same as above but for full house.

**Answer:** Four of a kind: 624 hands. Full house: 3744 hands. (As probabilities out of C(52,5) = 2,598,960: 624/2598960 = 1/4165 = 0.024%; 3744/2598960 = 6/4165 = 0.144%.)

*Working:* Four of a kind: pick the quad rank (13), take all four suits (1 way), then any of the 48 remaining cards as the kicker: 13 x 48 = 624. Full house: pick the trip rank (13) and its three suits C(4,3) = 4, then a different pair rank (12) and its two suits C(4,2) = 6: 13 x 4 x 12 x 6 = 3744. Ordering matters here - trips and pair are not interchangeable, so there is no division by 2.

*Assumption:* The leading fragment 'expected value of coin flip game (easy)' has no payoff rules, number of flips or stopping rule attached, so it cannot be answered as recorded; only the two counting questions are well posed.

<sub>numerically verified — `CHECK four_of_a_kind=624 full_house=3744 vs claimed 624 and 3744`</sub>

<sub>Source: wso · unknown · [link](https://www.wallstreetoasis.com/forum/job-search/drw-trading-interview-questions)</sub>

---


## Group One Trading  (2)

### 1. `G1-001` · `B` · internship · onsite · interviewed September 2016

Tell me what you know of options? Do you know the difference between a call option and a put option? Can you describe the Black-Scholes model to me? What is the model used for? What factors influence the outcome of the formula?

**Answer:** Model answer. A call is the right, not the obligation, to BUY the underlying at strike K on/before expiry; a put is the right to SELL. Black–Scholes prices a European option assuming the underlying is a geometric Brownian motion with constant volatility, a constant risk-free rate, no frictions and continuous trading. Its real content is the replication argument: an option can be manufactured by continuously delta-hedging, so its price must equal the cost of that hedge, which is the same as the discounted risk-neutral expected payoff. C = S·N(d1) − K·e^(−rT)·N(d2), P = K·e^(−rT)·N(−d2) − S·N(−d1), with d1 = [ln(S/K) + (r + sigma^2/2)T] / (sigma·sqrt(T)) and d2 = d1 − sigma·sqrt(T). Inputs: spot, strike, time to expiry, rate (and dividend/carry), and volatility. Five are observable; volatility is not — which is why in practice the model is used backwards, as a translation device between price and implied vol, and as a source of hedge ratios (delta, gamma, vega, theta). Finish with the caveats, because that is what separates a good answer: real markets show a volatility smile/skew, fat tails, jumps and stochastic vol, so no single sigma fits all strikes; hedging is discrete and costly; and the model assumes you can borrow and short freely.

*Working:* They are testing whether you know that Black–Scholes is a no-arbitrage replication/hedging argument and a market quoting convention, not a belief that returns are lognormal. Say what a call and a put are in one line each, state the formula and its five inputs, say what it is used for (pricing, implied vol, greeks/hedging), and volunteer the assumptions that fail.

<sub>guidance, no single correct value</sub>

<sub>Source: interview_review_site · 2019-04-27 · [link](https://www.wallstreetoasis.com/company/group-one-trading-lp-0/interview)</sub>

---

### 2. `G1-002` · `B` · internship · phone_technical · interviewed November 2024

How is trading with a model like being the house in a casino?

**Answer:** Model answer. The analogy: the house has a small, known edge on every bet, so it does not care about any single outcome — it cares about getting enough independent repetitions at a size small enough relative to its bankroll that the law of large numbers converts a tiny edge into a reliable P&L. A model-driven trader is doing the same thing: a small positive expectancy per trade, many trades, sizing so that variance cannot kill you before the edge shows up, and hard risk limits playing the role of table limits and barring card counters. Then say where the analogy breaks, which is the real point: (1) the casino KNOWS its edge exactly from the geometry of the wheel; a trader only estimates it from noisy, finite data and can be wrong about the sign; (2) casino bets are genuinely independent and stationary, whereas trading edges decay, get crowded out, and fail together — your 'independent' bets share risk factors and all lose on the same day; (3) adverse selection: the casino's customers do not know more about the wheel than the casino, but your counterparty may well know more than you, so the flow you get is not a random sample; (4) the casino's worst case is bounded, while a trader can face gap risk and leverage. So the honest version is: you are the house only as long as your model's edge is real, your costs are below it, and you are not being picked off.

*Working:* This is a conceptual/market-intuition question. They want the law-of-large-numbers intuition first, then evidence that you know a trading edge is estimated rather than known and that flow can be adversely selected.

<sub>guidance, no single correct value</sub>

<sub>Source: interview_review_site · 2025-04-01 · [link](https://www.wallstreetoasis.com/company/group-one-trading-lp-0/interview)</sub>

---


## Jane Street  (2)

### 1. `JS-007` · `B` · unknown · online_assessment · unknown(标题中的 20240401 是发帖日期,不是考试季)

一个盒子有 100 元钱,你和对手分别在纸上写下数字,如果数字之和小于等于 100,那么你们可以各自拿到与自己写下数字价值相同的钱,而如果数字之和大于 100 则两个人都拿不到钱。假设对手是理性的,你的最优策略是什么? Follow up:不再假设对手理性,并且将这个博弈进行 1000 遍,第一次对手说他会写 80,你会怎么办?如果游戏进行了十次,他每次都写 80,你会如何权衡? 思路或想法欢迎在留言区交流

*English:* A box holds 100 yuan. You and your opponent each write down a number. If the sum is at most 100 you each receive money equal to your own number; if the sum exceeds 100 neither gets anything. Assuming the opponent is rational, what is your optimal strategy? Follow-up: dropping the rationality assumption and repeating the game 1000 times, if the opponent says at the first round that he will write 80, what do you do? If he has written 80 every time for ten rounds, how do you weigh it up?

**Answer:** Write 50. Any pair summing to exactly 100 is a Nash equilibrium (verified: 101 of them, plus four degenerate zero-payoff ones), so 'rational' alone does not pin down a number — but 50 is the unique symmetric equilibrium, the Nash bargaining/Schelling focal point, and the only choice you can expect a symmetric rational opponent to be able to guess. Follow-up: against the announced 80, refuse it early. Best response to 80 in a one-shot game is 20, but in a 1000-round game your reputation is the asset, so keep writing 50 and say clearly and in advance that you always will. The arithmetic is one-sided: with 990 rounds left, one more round of stonewalling costs you 20 and, if it makes him switch to 50, gains 30 per round for 989 rounds — break-even probability that he caves is about 0.07%. After ten rounds of 80 you have lost only 200 of a possible 50,000, which is still cheap; the real question is whether he is a committed 'always 80' automaton or a strategic player waiting for you to blink. Keep punishing while the horizon is long, and only start conceding 20 near the end, when few rounds remain to amortise the cost — and note the symmetric danger: he is running exactly the same calculation, so prolonged mutual stubbornness burns both of you.

*Working:* Payoffs: you get x if x + y ≤ 100, else 0. If x + y < 100 both players want to raise, so no such profile survives; every (x, 100−x) is an equilibrium, as are profiles where both write ≥ 100 and both get nothing. Enumeration over integers 0..101 confirms 105 pure equilibria, exactly one of which is symmetric with a positive payoff: (50, 50). The follow-up is a reputation / war-of-attrition problem, and the break-even probability calculation is the thing to say out loud.

*Assumption:* Integer bids in [0, 100]; simultaneous choice; payoffs as stated; in the repeated version, no discounting and a known horizon of 1000.

<sub>numerically verified — `CHECK (num NE=105, efficient NE=101, symmetric positive NE=[(50, 50)], zero-payoff NE=4, break-even p=0.00068) vs (105, 101 splits x+y=100, [(50,50)],` · confidence: **medium**</sub>

<sub>Source: nowcoder · 2024-04-01 · [link](https://www.nowcoder.com/discuss/604265548247040000)</sub>

---

### 2. `JS-009` · `C` · unknown · unknown · unknown

A typical question is like given a game, what is the optimal strategy?

**Answer:** Model answer (no specific game is given, so this is the method). Steps: (1) write down the game tree — players, order of moves, information sets, payoffs; (2) delete dominated actions iteratively; (3) if it is finite with perfect information, backward-induct from the end; (4) if there is hidden information, expect a MIXED equilibrium and use the indifference principle — every action in your support must have the same EV, and you choose your frequencies to make your OPPONENT indifferent, not yourself; (5) verify by checking neither side has a profitable deviation, and compute the game's value from both sides as a cross-check. For poker specifically, the two standard results both drop out of indifference and are worth quoting: against a bet of B into a pot of P, the caller must defend with frequency P/(P+B) (minimum defence frequency) or pure bluffs become free; and the bettor's betting range must be B/(P+2B) bluffs to keep a bluff-catcher indifferent. A half-pot bet therefore means calling 2/3 of the time and a 3:1 value-to-bluff ratio; a pot-sized bet means calling 1/2 and 2:1. Finally, volunteer the exploitative layer — equilibrium is the baseline you fall back on against a strong unknown opponent, but against an over-folder you bluff more and against a station you drop bluffs and value-bet thinner. That trade-off is usually the point of the question.

*Working:* The prompt describes a genre of question rather than one game, so the checkable content is the method plus the canonical toy-game results. The verification solves the standard polarised toy game (pot 2, bet 1) and confirms the 1/4 bluff share, the 3:1 value:bluff ratio and the 2/3 minimum defence frequency, with zero gain to either side from deviating.

*Assumption:* No specific game is stated; the worked numbers assume the standard polarised bettor vs bluff-catcher toy game with pot 2 and bet 1.

<sub>numerically verified — `CHECK (bluff share of betting range=1/4, value:bluff=3:1, MDF=2/3, caller best deviation gain=0, bettor best deviation gain=0) vs (1/4, 3:1, 2/3, 0, 0` · confidence: **medium**</sub>

<sub>Source: glassdoor · unknown · [link](https://www.glassdoor.com/Interview/Jane-Street-Quantitative-Researcher-Interview-Questions-EI_IE255549.0,11_KO12,35.htm)</sub>

---


## Balyasny Asset Management  (1)

### 1. `BAM-002` · `B` · internship · phone_technical · 2024

You have a biased coin that lands heads 60% of the time. How can you use it to simulate a fair coin flip?

**Answer:** Von Neumann extraction: flip the coin twice. HT counts as 'heads', TH counts as 'tails', HH or TT is discarded and you repeat. P(HT) = P(TH) = pq = 0.24, so the two outcomes are exactly equally likely. Expected number of flips = 2/(2pq) = 1/0.24 = 25/6 = 4.167 (approx).

*Working:* The trick is to find two disjoint events with provably identical probability. For two independent flips, P(HT) = pq = P(TH) regardless of p, so conditioning on 'the two flips differed' gives an exactly fair bit. Each pair is decisive with probability 2pq = 0.48, so the number of pairs is geometric with mean 1/0.48 = 25/12, i.e. 25/6 flips on average. Two things worth saying out loud: it needs no knowledge of p (it works for any unknown fixed bias, which is the real point), and since here p = 0.6 is known you could do better on flip-efficiency by extracting entropy from discarded pairs (Elias/Peres), approaching the entropy bound of 1/H(0.6) = 1.03 flips per fair bit.

<sub>numerically verified — `CHECK freq=0.50045 meanflips=4.1663 vs claimed 0.5 4.1667`</sub>

<sub>Source: interview_review_db · 2025-07-06 · [link](https://www.wallstreetoasis.com/company/balyasny-asset-management/interview)</sub>

---


## Belvedere Trading  (1)

### 1. `BELV-001` · `B` · internship · online_assessment · unknown

given 7^1650 how many trailing zeroes are there, what are the sums of the digits etc.

**Answer:** Trailing zeros: 0. Supporting facts: 7^1650 has 1395 digits, its last digit is 9, and its decimal digit sum is 6229 (digital root 1).

*Working:* 7^1650 = 7^1650 has only 7s in its factorisation, so it is divisible by neither 2 nor 5 and therefore ends in no zeros - that is the whole first question. Digit count: floor(1650 x log10 7) + 1 = floor(1394.41) + 1 = 1395. Last digit: powers of 7 end in 7, 9, 3, 1 with period 4 and 1650 = 2 mod 4, so it ends in 9. Digit sum: 6229, which must be = 1 mod 9, and indeed 7^3 = 1 mod 9 with 3 | 1650 gives 7^1650 = 1 mod 9; 6229 -> 6+2+2+9 = 19 -> 1. That mod-9 test is the only hand-check available for the digit sum.

*Assumption:* The question trails off with 'etc.', so I answer the two parts it names (trailing zeros, digit sum) plus digit count and last digit. Note the digit sum is not a mental-arithmetic answer - on an online assessment this is a coding task; only the trailing-zero and last-digit parts are hand-solvable.

<sub>numerically verified — `CHECK zeros=0 ndigits=1395 digitsum=6229 last=9 mod9=1 vs claimed zeros=0 ndigits=1395 digitsum=6229 last=9 mod9=1`</sub>

<sub>Source: forum_thread · 2021-08-18 · [link](https://www.wallstreetoasis.com/forum/trading/belvedere-junior-trader-intern-hirevue)</sub>

---


## Bridgewater Associates  (1)

### 1. `BW-001` · `B` · internship · phone_technical · 2024

It's a philosophical question. Is television damaging to society?

**Answer:** There is no correct side. A strong answer: take a clear position, define the terms and the counterfactual, give your strongest evidence, name the strongest objection yourself, and state what evidence would change your mind. E.g.: 'Net negative, mainly through opportunity cost of time - the average American watches ~3 hours a day, and displaced sleep, exercise and face-to-face contact are the mechanisms I would point to, not content effects. What would change my mind is evidence that the counterfactual use of that time is no better, or that shared broadcast culture has civic value I am underweighting.'

*Working:* Bridgewater is testing thinking style, not TV. They want: (1) do you decompose a vague question into something answerable - damaging to whom, on what dimension, compared to what alternative use of the time; (2) will you actually commit to a view and defend it; (3) when pushed back on - and you will be pushed back on, often hard and possibly on a point where they think you are right - do you update on the argument's merits rather than on social pressure, and do you say explicitly what would change your mind. The two failure modes are refusing to commit ('there are arguments on both sides') and defending your opening position no matter what is said. Treat disagreement as information, and separate 'I was wrong' from 'you pushed harder'.

<sub>guidance, no single correct value</sub>

<sub>Source: interview_review_db · 2025-12-30 · [link](https://www.wallstreetoasis.com/company/bridgewater/interview)</sub>

---


## Flow Traders  (1)

### 1. `FLOW-001` · `B` · new_grad · phone_technical · interviewed February 2025

how much is th SP500 quoted in the market right now ?

**Answer:** No fixed answer - it is a live-market check, and the correct response is the actual level on the day quoted as a two-sided market. I cannot supply the live print: my knowledge is stale relative to the interview date, and quoting a stale index level would be worse than useless. What matters is the form of the answer: give a level and a tight two-sided market - the shape is 'I'd make it X bid at X+10 offered', where X is the level you looked up that morning (I am deliberately not putting a number on X here, since any figure I gave would be stale) - say explicitly whether you are quoting the cash index or the ES future (the future trades at a basis to cash, reflecting carry and dividends), and be ready with the neighbouring numbers - VIX, 10-year Treasury yield, EURUSD, crude, gold, and roughly where the index sits year-to-date and versus its high.

*Working:* What they are testing is whether you actually follow markets and whether you will make a price under uncertainty rather than freeze. Being 1-2% off the true level is survivable and normal; refusing to give a number is the failure mode. If you genuinely have no idea, bracket it out loud from something you do know and widen your market accordingly. Check the level immediately before any Flow Traders call - this question, or its equivalent for another instrument, is close to guaranteed.

*Assumption:* No date-current market data is available to me.

<sub>guidance, no single correct value</sub>

<sub>Source: interview_review_site · 2025-02-26 · [link](https://www.wallstreetoasis.com/company/flow-traders-0/interview)</sub>

---


## Ingensoma Arbitrage  (1)

### 1. `INGEN-001` · `C` · unknown · phone_technical · unknown

1) A has 7 coins. B has 6 coins. Who gets higher heads wins. What's the probability of A winning? 2) You get the value shown on a dice. If you are not satisfied, you can roll it twice or thrice. What's the expected value of the game? 3) Put has delta -0.3. Now vol increases and decreases. How does delta change? 4) Put has delta -0.3. Now time to maturity increases and decreases. How does delta change? 5) How does gamma change when time to maturity increases? 6) How does gamma change when volatility increases? 7) ATM Gamma at t=30 days and t=1 day. Which is higher?

**Answer:** (1) 1/2 exactly. (2) 17/4 = 4.25 with one optional re-roll (up to two rolls); 14/3 ≈ 4.6667 with up to three rolls. (3) Vol up makes the −0.30 put MORE negative (towards −0.5); vol down pushes it towards 0. (4) Same direction: more time to maturity makes it more negative, less time pushes it towards 0. (5) ATM gamma FALLS as time to maturity increases (gamma ~ 1/sqrt(T)); for options well away from the money gamma is hump-shaped in T and can rise with T. (6) ATM gamma FALLS as volatility rises; away-from-the-money gamma RISES with vol. (7) The 1-day ATM gamma is much higher than the 30-day (roughly sqrt(30) ≈ 5.5 times, 0.381 vs 0.070 in the check below).

*Working:* (1) With 7 vs 6 fair coins, let A toss 6 first; by symmetry A's first 6 beat B's 6, tie, or lose with P(win) = P(lose) = p and P(tie) = 1−2p. A's 7th coin wins the ties half the time: P(A) = p + (1−2p)/2 = 1/2. (2) Backwards induction: one roll is worth 7/2; with one re-roll keep 4,5,6 and re-roll otherwise, giving (4+5+6)/6 + (3/6)(7/2) = 17/4; with two re-rolls keep only 5,6 (since 4 < 17/4) giving (5+6)/6 + (4/6)(17/4) = 14/3. (3)&(4) With r = 0, put delta = N(d1) − 1 and d1 = ln(S/K)/x + x/2 where x = sigma·sqrt(T); a −0.30 put is out of the money, and at ordinary vols raising x lowers d1 and so makes delta more negative — volatility and time enter only through the same combination x, which is why (3) and (4) have the same answer. Caveat worth saying out loud: this reverses in the extreme. d1 is minimised at x = sqrt(2·ln(S/K)), and as x → infinity put delta → 0 (an infinite-vol put is worth cash and has no delta), so at very high vol or very long dated the effect flips. In the verified example (S = 100, K = 95.37, T = 0.25) delta goes −0.300 → −0.348 at 30% vol and → −0.206 at 12% vol. (5)–(7) gamma = phi(d1)/(S·sigma·sqrt(T)); at the money phi(d1) is essentially flat, so gamma scales like 1/(sigma·sqrt(T)) — it blows up as expiry approaches and shrinks with vol. For strikes far from spot the phi(d1) term dominates and more vol or more time (which bring the option into play) raise gamma.

*Assumption:* Fair coins in (1); fair six-sided die and the reading 'you may re-roll and must accept the last roll', with up to 2 or up to 3 rolls in (2); European options, Black–Scholes, r = 0 and no dividends in (3)–(7); a −0.30 put is taken to be out of the money at an ordinary vol level.

<sub>numerically verified — `CHECK (P(A)=1/2, E2=17/4, E3=14/3, K=95.37 delta=-0.300, vol_up=-0.348 vol_dn=-0.206, T_up=-0.342 T_dn=-0.193, gATM30=0.0695 gATM1=0.3811, gATMvol .15`</sub>

<sub>Source: interview_review_site · unknown · [link](https://www.wallstreetoasis.com/company/ingensoma-arbitrage-pte-ltd/interview)</sub>

---


## Point72 / Cubist  (1)

### 1. `P72-001` · `C` · unknown · phone_technical · 2026

linear regression. How do we estimate beta. When n >> p, how to find beta?

**Answer:** beta_hat = (X'X)^{-1} X'y, the OLS solution of the normal equations X'X beta = X'y. When n >> p and X has full column rank p, that system is p x p and non-singular, so the solution is unique - compute it by QR (or Cholesky on X'X), not by forming an explicit inverse, at O(np^2) cost.

*Working:* OLS minimises S(beta) = ||y - X beta||^2; setting the gradient -2X'(y - X beta) to zero gives the normal equations, whose solution makes the residual orthogonal to the column space of X. n >> p is the ordinary overdetermined case: X'X is p x p, invertible under full rank, so beta_hat is unique and by Gauss-Markov it is BLUE (E[eps|X]=0, homoskedastic uncorrelated errors), with Var(beta_hat) = sigma^2 (X'X)^{-1}. Practical points that earn the credit: use the thin QR X = QR and solve R beta = Q'y, since forming X'X squares the condition number; SVD if X is near-collinear; with n enormous you only ever need the p x p Gram matrix and the p-vector X'y, so it streams in one pass in O(p^2) memory (or use SGD / minibatch). Contrast with p >> n, where X'X is singular, the fit interpolates, and you need ridge (X'X + lambda I)^{-1} X'y, lasso, or the minimum-norm pseudoinverse solution.

*Assumption:* Standard linear model y = X beta + eps with an intercept column in X and rank(X) = p.

<sub>numerically verified — `CHECK (True, True, True, [1.507, -2.018, 0.728, 3.105]) vs (True, True, True, [1.5, -2.0, 0.7, 3.1])`</sub>

<sub>Source: forum_recall_zh · 2026-05-01 · [link](https://www.1point3acres.com/bbs/thread-1175215-1-1.html)</sub>

---


## Two Sigma  (1)

### 1. `2SIG-008` · `B` · unknown · phone_technical · unknown

How would you make money using social media data?

**Answer:** Model answer, structured as a research plan rather than a stock tip. Hypotheses worth testing: (a) retail attention - mention counts and their abnormal spikes on Reddit/X/ StockTwits - predicts short-horizon flow and volatility in small, hard-to-borrow names; (b) sentiment adds to that, but attention usually dominates sentiment empirically; (c) social data as a fundamentals nowcast (app-store review volume, hiring and job posts, product chatter) to forecast the revenue print ahead of the sell-side consensus; (d) event detection faster than the newswire - outages, accidents, recalls. Data engineering is most of the work: entity resolution ($TSLA vs Tesla vs Elon), bot and spam filtering, deduplication of reposts, and strictly point-in-time timestamps (ingest time, not post time, and keep deleted posts in the history). Signal construction: normalise mentions against each name's own baseline, cross-sectional z-scores, then residualise against size, liquidity, momentum and conventional news so you are not just re-buying a known factor. Validation: purged and embargoed walk-forward, hold out a final period, correct for multiple testing (you will test hundreds of variants), and measure the decay horizon - if the alpha lives for 30 minutes it is a different business from a 5-day signal. Implementation reality: capacity is the binding constraint because the effect concentrates in small caps with wide spreads and borrow costs, so net-of-cost Sharpe is what matters; the data is licensed and commoditised, so crowding decays it; and the feed is adversarial - people post specifically to move algorithms. Honest conclusion: best used as a short-horizon overlay on execution and position sizing, and as a risk flag, not as a standalone strategy.

*Working:* This is a research-process question dressed up as a money question. The interviewer is testing whether you go straight to 'sentiment = buy' or instead reason about labels, point-in-time data, overfitting from multiple testing, decay, capacity and costs. Mentioning that the strongest effects sit in names you cannot trade at size, and that the signal decays as the data is commoditised, is what marks out someone who has actually done this.

<sub>guidance, no single correct value</sub>

<sub>Source: wso · 2024-01 · [link](https://www.wallstreetoasis.com/company/two-sigma-investments/interview/researcher)</sub>

---


## Valkyrie Trading  (1)

### 1. `VALK-001` · `C` · unknown · phone_technical · unknown

1. Tell me about yourself and why are you interested in joining Valkyrie? 2. Why did you change your field from Computer Engineering to Quantitative Finance? 3. What are the Greeks related to Options? 4. What is skewness and Kurtosis of a Probability distribution? 5. What is the Volatility Curve and what is it's significance? 6. I also had a Python Coding Question: Suppose there are two variables a and b, a = 2 b = a b = b+1 print(a) What is the Output of the above code snippet?

**Answer:** (6) has a definite answer: it prints 2. Parts 1-5: (1)/(2) are behavioural - give a specific, honest narrative ending in why a small options market maker, and frame the Computer Engineering -> Quant Finance switch as additive (low-latency systems and numerical skill transfer directly to trading infrastructure), never as an escape. (3) Greeks: delta dV/dS, gamma d2V/dS2, vega dV/dsigma (not a Greek letter), theta dV/dt, rho dV/dr; second-order: vanna d2V/dS dsigma, volga d2V/dsigma2, charm d(delta)/dt. Say which ones you actually hedge: delta continuously, gamma and vega by trading other options. (4) Skewness = E[(X-mu)^3]/sigma^3, the asymmetry; kurtosis = E[(X-mu)^4]/sigma^4, tail weight, equal to 3 for a normal, so 'excess kurtosis' = kurtosis - 3. Equity returns are negatively skewed and leptokurtic, which is precisely why Black-Scholes underprices the tails. (5) The volatility curve is implied vol plotted against strike (smile/skew) for a fixed expiry, with the term structure being its variation across expiries. Under Black-Scholes it would be flat; it is not, because the real risk-neutral distribution has fat tails and negative skew and because there is persistent demand for downside protection. Significance: it is the market's risk-neutral density (Breeden-Litzenberger recovers it from the second strike derivative of call prices), it is what a market maker actually quotes and risk-manages, and it must stay arbitrage-free across strikes and expiries. (6) Output: 2 - integers are immutable, b = a binds b to the same object and b = b + 1 rebinds b to a new object, leaving a untouched.

*Working:* Mixed screen: rapport, options vocabulary, and one Python semantics trap. The Python question is testing whether you understand name binding versus mutation - the same person who answers '2' should be able to say that the answer would differ for a mutable object (b = a; b.append(1) would show through in a). For the Greeks and the vol curve they want working familiarity, not derivations: what each Greek means for your book and how you hedge it.

*Assumption:* Part 6 read exactly as written, with a = 2 (an int).

<sub>numerically verified — `CHECK printed=2 vs claimed=2`</sub>

<sub>Source: interview_review_site · unknown · [link](https://www.wallstreetoasis.com/company/valkyrie-trading/interview)</sub>

---

