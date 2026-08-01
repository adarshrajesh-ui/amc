# Incomplete questions — proposed for removal, awaiting your confirmation

I read all 218 questions in `QTRADER.md` in full and judged each one against a single
test: **can this be solved as written?** Nothing below has been removed yet.

The automated pass flagged 91 candidates. Most were false positives — it read a missing
full stop as a truncation and a 280-character display limit as a cut-off sentence. Every
Citadel Datathon item it flagged turned out to be complete. What follows is my own
reading, not the heuristic's.

To remove all of them, run:

```bash
printf '%s\n' A1 A2 A3 A4 B1 B2 B3 > /dev/null   # (illustrative — use the ID list below)
python3 harvest/tools/apply_review.py
```

More practically: copy the ID block at the bottom into `harvest/removals.txt` and run
`apply_review.py`. They will move to `REMOVED.md` with their evidence intact.

---

## Group A — text is cut off mid-sentence (3)

These stop in the middle of a clause. The missing part carries information you need.

**`IMC-001`** · IMC Trading · Tier D
> Two RVs following uniform[0,1]. What's the probability of the smaller RV is less than the

Stops dead on "less than the". The threshold is exactly the thing being asked about.

**`OPT-007`** · Optiver · Tier C
> a coin and whilst you do this you keep track of the number of Heads and the number of Tails. You can think of this as a race between Heads and Tails. For example, if after 9 flips you have landed on Heads 7 times and Tails 2 times, then Heads is winning the race by 5. Now

Cut at *both* ends — it opens mid-sentence ("a coin and whilst you do this") and ends on
a dangling "Now". The setup survives but the actual question was never captured.

**`OMC-005`** · Old Mission Capital · Tier B
> What is the expected value of a dice roll? Make me a market on __

The first half is fine; the second half has a literal blank where the instrument should
be. As a market-making prompt it is unusable.

---

## Group B — stem never recovered, only the discussion around it (3)

For these the collector captured readers *talking about* a question without ever
capturing the question. They are honest records of a known gap, which is why they were
kept, but they are not practice material.

**`SIG-014`** · SIG · Tier B — Question 14 of the 17-question OA. All that survives is a
reader disputing the answer: 「第14题我看AB等于32也可以?排列如下…1,4,3,2 / 2,1,4,3 / 4,3,2,1 / 3,2,1,4」

**`SIG-041`** · SIG · Tier C — Round 2, question 1, behind the points wall. Two readers
ask about it: 「请问第二轮第一题是在那个三角形平面,还是四面体内,做sampling」

**`SIG-064`** · SIG · Tier C — The final-round questions, behind the paywall. A reader
says 「第1,3题…看了之后没什么头绪」

---

## Group C — describes a question or a round, never states a problem (23)

Not truncated — these are complete sentences. They just tell you a question existed
rather than what it was. Nothing here is solvable because nothing is asked.

| ID | Firm | Text |
|---|---|---|
| `2SIG-003` | Two Sigma | Final technical round: one coding, one stats, one data science, then 2-3 hiring managers |
| `5RINGS-003` | Five Rings | A series of fast-paced estimation-style questions in the first interview |
| `5RINGS-005` | Five Rings | A game theory question — easy math, but you must be careful with all the conditions |
| `5RINGS-007` | Five Rings | A game theory question at second round. Cannot remember exactly as a very long question |
| `BAM-001` | Balyasny | a phone round asking probability brainteasers |
| `CTC-003` | CTC | an online assessment consisting of probability/brainteaser questions, ~10 in thirty minutes |
| `CTC-004` | CTC | A python-based coding question which involved analyzing stock data |
| `MAVEN-001` | Maven | a combinatorial problem about extracting different coloured cubes and the towers they make |
| `OMC-008` | Old Mission | A market making portion of the interview (feedback was that it was too weak) |
| `OPT-001` | Optiver | an SHL "General Ability" test … simple percentages, read data from graphs |
| `OPT-015` | Optiver | an identifying sequences test, e.g. shown a sequence, guess the next or missing number |
| `SIG-004` | SIG | A simple probability question simple math and you have to explain your train of thoughts |
| `SIG-008` | SIG | you only need to know basic probability and stats to solve most of them |
| `SIG-015` | SIG | A lot about options. A project give you tomorrow how will you finish it step by step |
| `SIG-035` | SIG | a couple of questions which required having formulas learnt off |
| `SIG-037` | SIG | an online maths test consisting of probability questions |
| `SIG-045` | SIG | it was around 12 questions in 36 (?) minutes including mostly probability and brain teasers |
| `SIG-046` | SIG | you chat with a recruiter who asks you some fairly straightforward probability questions |
| `SIG-051` | SIG | A problem on Bayes theorem with multiple extensions |
| `SIG-058` | SIG | if you've done it before then its the same questions with different numbers |
| `SIG-061` | SIG | A logic puzzle asking to determine lies and who speaks the truth |
| `VIRTU-003` | Virtu | a probability puzzle about chances of making a basket as a function of the previous n-1 shots |
| `VIRTU-005` | Virtu | a coding screen where you replicate a simulation of a game |

---

## Borderline — I am NOT proposing these, but flag them so you can overrule me

**`SIG-057`** (SIG, Tier C) — the opening sentence was cut by the paywall, but all three
seating constraints and the actual question survived, so it *is* solvable. It is also a
duplicate of the same toddler problem that appears complete elsewhere in the corpus, so
you may want it gone as a duplicate rather than as an incomplete.

**`MAKO-003`** (Mako) — starts lowercase with no question mark, which is why the
heuristic caught it, but "what are the various greeks on this spread, what happens if
underlying sharply moves up" is a fully answerable question.

**`JUMP-017`** (Jump) — phrased as "a math problem about…", but it then specifies the
entire bubble-pass procedure, so the problem is recoverable.

**`5RINGS-004`** (Five Rings) — "X and Y in a normal distribution, find the
distribution/expectation of max(X, Y)" omits that they are iid standard normal, but that
is the obvious reading.

**`SIG-042`** (SIG) — "A classic question of whether HHT or HTH will appear first" names a
well-defined problem even though it does not state it. The same question appears fully
stated elsewhere in the SIG set.

---

## Removal list

29 IDs — Groups A, B and C. QTRADER would go from 218 to 189. Paste into `harvest/removals.txt` and run
`python3 harvest/tools/apply_review.py`.

```
IMC-001 cut off mid-sentence, threshold missing
OPT-007 cut off at both ends, question never captured
OMC-005 literal blank where the instrument should be
SIG-014 stem never recovered, only reply-thread discussion
SIG-041 stem behind points wall, only reader questions survive
SIG-064 final-round stems behind paywall
2SIG-003 describes the round, states no problem
5RINGS-003 describes the round, states no problem
5RINGS-005 describes the round, states no problem
5RINGS-007 poster could not remember the question
BAM-001 describes the round, states no problem
CTC-003 describes the round, states no problem
CTC-004 describes the round, states no problem
MAVEN-001 describes the topic, no parameters given
OMC-008 describes the round, states no problem
OPT-001 describes the test, states no problem
OPT-015 describes the test format, states no problem
SIG-004 describes the round, states no problem
SIG-008 commentary on difficulty, not a question
SIG-015 describes the round, states no problem
SIG-035 describes the round, states no problem
SIG-037 describes the round, states no problem
SIG-045 describes the round, states no problem
SIG-046 describes the round, states no problem
SIG-051 describes the topic, states no problem
SIG-058 commentary on the OA, not a question
SIG-061 describes the topic, no specifics given
VIRTU-003 describes the topic, no parameters given
VIRTU-005 describes the round, states no problem
```
