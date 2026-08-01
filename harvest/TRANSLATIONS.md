# Chinese questions with English translations

All 20 questions in the corpus whose text contains Chinese, shown with the source text above the translation so the rendering can be checked rather than trusted.

The Chinese is authoritative and is never overwritten. Where a translation was corrected during audit, the correction and its reason are recorded inline.

**Forum slang decoded in these translations:** 面经 interview recall · 笔试 written test · 地里 "on the forum" (1point3acres) · lz / 楼主 original poster · bq behavioural question · 八股 rote-memorisation questions · 手撕 live coding · 求米 / 加米 requests for forum points.

---

### 1. Akuna Capital · quant_developer · onsite · `B`

**中文原文 (source):**

> 申的C++ Junior Dev,似乎要on-site了,有人面过么?求点经验,感觉略虚,还是E文的。

**English:**

I applied for C++ Junior Dev and it looks like I'm going to on-site. Has anyone interviewed? Looking for some experience — I feel a bit shaky, and it's in English too.

<sub>nowcoder · 2016-10-25 · [source](https://www.nowcoder.com/discuss/353153964797534208)</sub>

---

### 2. Citadel · quant_developer · onsite · `D`

**中文原文 (source):**

> 2) C++ 函数 void func(int8_t i);void main() { int32_t x = 1; func(x); }会发生什么 ?

**English:**

2) A C++ function void func(int8_t i); void main() { int32_t x = 1; func(x); } — what happens?

<sub>chat_telegram · 2022-08-18 · [source](https://t.me/usinterview/14353)</sub>

---

### 3. Hudson River Trading · quant_developer · online_assessment · `C`

**中文原文 (source):**

> 第二题 union find,最后count两个group的成员个数 第三题 第一部分topological sort?

**English:**

Question 2 is union-find, finally counting the members of the two groups. Question 3: is the first part topological sort?

<sub>1point3acres · unknown · [source](https://www.1point3acres.com/bbs/thread-1022110-1-1.html)</sub>

---

### 4. Jane Street · quant_developer · phone_technical · `C`

**中文原文 (source):**

> “customers can go between other customers”是不是说新进来的顾客可以插到队伍中间?为啥一定要用红黑树,其他数据结构不行吗?

**English:**

Does "customers can go between other customers" mean a newly arriving customer can cut into the middle of the queue? And why must a red-black tree be used — would no other data structure do?

<sub>other · 2025-06-01 · [source](https://web.archive.org/web/20250630171445/https://www.1point3acres.com/bbs/thread-1131152-1-1.html)</sub>

---

### 5. Jane Street · quant_developer · phone_technical · `D`

**中文原文 (source):**

> Implement 一个connect four的游戏,区别在于新放进去球会掉在最底下,然后把上面球顶上去。

**English:**

Implement a Connect Four game, except that a newly inserted ball drops to the very bottom and pushes the balls above it up.

<sub>chat_telegram · 2025-07-20 · [source](https://t.me/usinterview/24268)</sub>

---

### 6. Jane Street · unknown · unknown · `B`

**中文原文 (source):**

> 一个盒子有 100 元钱,你和对手分别在纸上写下数字,如果数字之和小于等于 100,那么你们可以各自拿到与自己写下数字价值相同的钱,而如果数字之和大于 100 则两个人都拿不到钱。假设对手是理性的,你的最优策略是什么? Follow up:不再假设对手理性,并且将这个博弈进行 1000 遍,第一次对手说他会写 80,你会怎么办?如果游戏进行了十次,他每次都写 80,你会如何权衡?

**English:**

A box holds 100 yuan. You and your opponent each write down a number. If the sum is at most 100 you each receive money equal to your own number; if the sum exceeds 100 neither gets anything. Assuming the opponent is rational, what is your optimal strategy? Follow-up: dropping the rationality assumption and repeating the game 1000 times, if the opponent says at the first round that he will write 80, what do you do? If he has written 80 every time for ten rounds, how do you weigh it up?

**Translation corrected during audit.** 「100 元钱」 is yuan, not dollars. The identical question in cluster fdf6f699 renders it correctly, so the corpus contradicted itself.

<sub>nowcoder · 2024-04-01 · [source](https://www.nowcoder.com/discuss/604265548247040000)</sub>

---

### 7. Jane Street · quant_developer · phone_technical · `D`

**中文原文 (source):**

> 算数part 1: input是一个算数组,求结果只考虑+-x /eg. (4 + 5) x 6 = ? parser的部分不用写直接求结果

**English:**

Arithmetic, part 1: the input is an array representing an arithmetic expression; compute the result considering only + - x /, e.g. (4 + 5) x 6 = ? You do not need to write the parser, just produce the result.

**Translation corrected during audit.** 「算数组」 rendered literally as 'arithmetic array', which is opaque. The worked example (4 + 5) x 6 shows the input encodes an expression.

<sub>chat_telegram · 2022-09-19 · [source](https://t.me/usinterview/14711)</sub>

---

### 8. Jane Street · quant_developer · phone_technical · `D`

**中文原文 (source):**

> Implement APIs for a tree class backend — Tree node的定义已知,所有API已知(不用实现)class Node { vector getAncestors

**English:**

Implement APIs for a tree class backend. The tree node definition is given and all APIs are given (you do not implement them): class Node { vector getAncestors... (preview truncated)

<sub>chat_telegram · 2024-12-03 · [source](https://t.me/usinterview/20583)</sub>

---

### 9. Jane Street · unknown · online_assessment · `B`

**中文原文 (source):**

> 一个盒子有 100 元钱,你和对手分别在纸上写下数字,如果数字之和小于等于 100,那么你们可以各自拿到与自己写下数字价值相同的钱,而如果数字之和大于 100 则两个人都拿不到钱。假设对手是理性的,你的最优策略是什么? Follow up:不再假设对手理性,并且将这个博弈进行 1000 遍,第一次对手说他会写 80,你会怎么办?如果游戏进行了十次,他每次都写 80,你会如何权衡? 思路或想法欢迎在留言区交流

**English:**

A box holds 100 yuan. You and your opponent each write down a number. If the sum is at most 100 you each receive money equal to your own number; if the sum exceeds 100 neither gets anything. Assuming the opponent is rational, what is your optimal strategy? Follow-up: dropping the rationality assumption and repeating the game 1000 times, if the opponent says at the first round that he will write 80, what do you do? If he has written 80 every time for ten rounds, how do you weigh it up?

<sub>nowcoder · 2024-04-01 · [source](https://www.nowcoder.com/discuss/604265548247040000)</sub>

---

### 10. Jump Trading · quant_developer · onsite · `C`

**中文原文 (source):**

> 第一题的operations有可能是三个吗?或者多个每个只能用一次么,还是所有list的数字都可以用任意这四个里面的operation combine?

**English:**

Could the first question's operations be three? Or several, each usable only once? Or can all the numbers in the list be combined using any of these four operations?

<sub>1point3acres · 2022-11 · [source](https://www.1point3acres.com/bbs/thread-942280-1-1.html)</sub>

---

### 11. Optiver · unknown · phone_technical · `D`

**中文原文 (source):**

> design 一个class提供四个api,带on的都是callback 用来update internal data structure。最后一

**English:**

Design a class exposing four APIs; the ones prefixed with "on" are callbacks used to update the internal data structure. The last...

<sub>chat_telegram · 2024-10-25 · [source](https://t.me/usinterview/20082)</sub>

---

### 12. Optiver · quant_developer · online_assessment · `D`

**中文原文 (source):**

> design a news subscription process engine两个小时

**English:**

Design a news subscription process engine. Two hours.

<sub>chat_telegram · 2026-07-27 · [source](https://t.me/usinterview/29070)</sub>

---

### 13. Squarepoint Capital · quant_analyst · phone_technical · `C`

**中文原文 (source):**

> python 八股:1. tuple Vs. list 2. pass by reference Vs. pass by value? 3. difference between is and ==?

**English:**

Python fundamentals drill: 1. tuple vs list 2. pass by reference vs pass by value? 3. difference between is and ==?

<sub>forum_recall_zh · unknown · [source](https://www.1point3acres.com/bbs/collection/253315)</sub>

---

### 14. Susquehanna International Group · unknown · superday · `C`

**中文原文 (source):**

> [终面题目本身在积分墙后。可确认的是终面至少有三题,且第 1、3 题连读者读完题解都无从下手:] 请问lz final round 第1,3题有什么可以参考的思路吗? 看了之后没什么头绪。。。然后lz是有finance背景吗?

**English:**

[The final-round questions themselves are behind the paywall. What is established: the final round had at least three questions, and questions 1 and 3 left even a reader who had read the write-up with no idea how to start.] Reader: 'Could I ask whether there's any line of approach for final-round questions 1 and 3? After reading them I have no clue... also, does OP have a finance background?'

<sub>1point3acres · 2024-10-13 · [source](https://www.1point3acres.com/bbs/thread-1091467-1-1.html)</sub>

---

### 15. Susquehanna International Group · quant_researcher · onsite · `C`

**中文原文 (source):**

> 二面就纯bq,问了一些地里其他一样的bq,类似与why QR? why SIG这种之类的。

**English:**

The second round was purely behavioural — the same BQs as others on this forum have had, along the lines of "why QR?", "why SIG?" and so on.

<sub>other · unknown · [source](https://www.1point3acres.com/bbs/thread-1042392-1-1.html)</sub>

---

### 16. Susquehanna International Group · unknown · phone_technical · `C`

**中文原文 (source):**

> [第二轮第一题 — statement point-gated. All that surfaced are two readers asking about it:] 请问第二轮第一题是在那个三角形平面,还是四面体内,做sampling ... 想问三角形要怎样做?

**English:**

[Round 2, question 1 — statement gated.] Reader: 'Can I ask whether round 2 question 1 does the sampling in that triangular plane, or inside the tetrahedron?' Another reader: 'I want to ask how to do the triangle one.'

<sub>1point3acres · 2020-11 · [source](https://www.1point3acres.com/bbs/thread-686183-1-1.html)</sub>

---

### 17. Susquehanna International Group · quant_researcher · online_assessment · `C`

**中文原文 (source):**

> 青蛙想从(0,0)跳到(7,4),每次只能向右跳一格或向上跳一格。青蛙不愿意同方向连续跳三次。共多少种不同跳法?

**English:**

A frog wants to jump from (0,0) to (7,4); each jump can only be one square to the right or one square up. The frog is unwilling to jump three times in a row in the same direction. How many different jump sequences are there?

<sub>1point3acres · unknown · [source](https://www.1point3acres.com/bbs/thread-1114232-1-1.html)</sub>

---

### 18. Susquehanna International Group · quant_researcher · phone_technical · `C`

**中文原文 (source):**

> 2. 扔硬币 进入 HTH HHT 之一就结束,问进入每一个的概率是多大?(不太记得具体ending state是啥了)

**English:**

2. Flip a coin; the game ends as soon as you hit either HTH or HHT. What is the probability of ending on each of them? (I don't remember exactly what the ending states were.)

<sub>other · 2020-11-11 · [source](https://www.1point3acres.com/bbs/thread-686183-1-1.html)</sub>

---

### 19. Susquehanna International Group · quant_researcher · phone_technical · `C`

**中文原文 (source):**

> 1. 圆里随机画n条线,问能把圆分成几分 (期望)? 把分成的份数和交点个数对应起来,然后算交点个数的期望。

**English:**

1. Draw n lines at random inside a circle — into how many pieces do they divide the circle (in expectation)? Match the number of pieces to the number of intersection points, then compute the expected number of intersection points.

<sub>other · 2020-11-11 · [source](https://www.1point3acres.com/bbs/thread-686183-1-1.html)</sub>

---

### 20. Susquehanna International Group · quant_researcher · online_assessment · `B`

**中文原文 (source):**

> [Question 14 — full stem NOT recovered. Attested only through the reply thread, where a reader disputes the answer:] 你好,第14题我看AB等于32也可以?排列如下,查了也满足要求:1,4,3,2 / 2,1,4,3 / 4,3,2,1 / 3,2,1,4

**English:**

[Question 14 — full stem NOT recovered. Attested only via the reply thread:] 'Hi, for Q14 I think AB = 32 also works? Here's the arrangement, I checked and it satisfies the requirements: 1,4,3,2 / 2,1,4,3 / 4,3,2,1 / 3,2,1,4' [Thread context, not part of the quoted text: the original poster replies that he had dropped a condition when drawing the grid, and that with the missing constraint restored the solution is unique.]

**Translation corrected during audit.** The English carried a sentence with no counterpart in the quoted Chinese. It is thread context, not translation, so it moves to a bracketed note.

<sub>university_bbs · 2025-09-04 · [source](https://www.1point3acres.com/bbs/thread-1144112-1-1.html)</sub>

---
