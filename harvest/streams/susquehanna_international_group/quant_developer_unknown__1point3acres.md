# Susquehanna International Group · quant developer unknown · 1point3acres

- **Source family:** 1point3acres
- **Items:** 4
- **Date range:** 2021-02 – 2021-02 (exact day not shown in retrieved text) (5/4 dated)
- **Tier mix:** C=4

---
### Q1 · Tier C · unknown · online_assessment (总时长20分钟,一共是16道题 (16 questions in 20 minutes). A reply describing the s)

[题面被积分墙挡住。以下为楼主自己更正后的解法,题目结构由此可还原:掷某种随机装置,每次出现 8 的概率 0.07、出现 9 的概率 0.08、出现 10 的概率 0.09(其余 0.76 为无事发生),问「8 和 10 都出现」的概率。] 我刚刚发现我第二题理解错了,我之前理解的是只要出现8或者10就算赢,所以之前那个帖子里算的概率都将近1了。现在我理解就是要8和10都出现才可以。我重新算了一下,还是markov方法: 假设从初始状态到最终状态(8和10出现)的概率是p(s), 从出现一次8的状态到最终状态的概率是p(8),相应的p(9)和p(10)是同样的意思,然后p(8,9)是从出现了一次8和9的状态到最终状态,同理p(9, 10)。然后就可以列方程: p(s) = 0.76p(s) + 0.07p(8) + 0.08p(9) + 0.09p(10) p(8) = 0.83p(8) + 0.09 + 0.08p(8,9). p(9) = 0.76p(9) + 0.07p(8,9) + 0.09p(9, 10). p(10) = 0.85p(10) + 0.07 + 0.08p(9,10). p(8,9) = 0.83p(8,9) + 0.09 p(9,10) = 0.85p(9,10) = 0.07

*EN:* [Statement behind the paywall. This is the poster's own corrected solution, from which the structure is recoverable: something is generated repeatedly, with per-trial probability 0.07 of an 8, 0.08 of a 9 and 0.09 of a 10 (the remaining 0.76 being nothing); asked for the probability that BOTH an 8 and a 10 appear.] 'I've just realised I misread question 2. I had read it as winning if either an 8 or a 10 shows up, which is why the probability I computed in that earlier post came out near 1. Now I read it as needing both the 8 and the 10. I've recomputed, still by the Markov method: let p(s) be the probability of getting from the initial state to the final state (8 and 10 have appeared), p(8) the probability from the state where an 8 has appeared once, similarly p(9) and p(10); p(8,9) is from the state where an 8 and a 9 have each appeared, likewise p(9,10). Then you can set up the equations: [system as quoted].'

*Reported answer:* p(s) = 13118/21675, per the poster's corrected Markov solution. They immediately flag it as impractical under the time limit: 「但是可以看出来这个方法计算量很大,而且超级容易出错。我很担心就20分钟,这道题用这个方法得用去一大半时间,然后还有可以因为计算出错。我目前没有想到其他更简单的方法了」 — this method is very computation-heavy and extremely error-prone; with only 20 minutes i

> SIG Quantitative Evaluation 2021. OA 2021-02最新|sigPM面经|一亩三分地数科面经版 ... | 我刚刚发现我第二题理解错了,我之前理解的是只要出现8或者10就算赢,所以之前那个帖子里算的概率都将近1了。现在我理解就是要8和10都出现才可以。我重新算了一下,还是markov方法: 假设从初始状态到最终状态(8和10出现)的概率是p(s), 从出现一次8的状态到最终状态的概率是p(8),相应的p(9)和p(10)是同样的意思,然后p(8,9)是从出现了一次8和9的状态到最终状态,同理p(9, 10)。然后就可以列方程: p(s) = 0.76p(s) + 0.07p(8) + 0.08p(9) + 0.09p(10) p(8) = 0.83p(8) + 0.09 + 0.08p(8,9). 1point3acres.com p(9) = 0.76p(9) + 0.07p(8,9) + 
— 1point3acres · posted 2021-02 · snippet_only · [link](https://www.1point3acres.com/bbs/thread-719224-2-1.html)
  1 attestation(s) across 1 domain(s) · doubt: The statement itself never appeared; everything here is reverse-engineered from the poster's own corrected working, and I have marked that explicitly inside question_text rather than writing a clean problem. Specifically

### Q2 · Tier C · unknown · online_assessment (总时长20分钟,一共是16道题 (16 questions in 20 minutes). A reply describing the s)

If day is a “Good” Day, [there] is a 60% chance that the next day will be “Good” and a 40% chance it will be “Bad”. If day is a “Bad” Day, there is a 70% chance that the next day will be “Bad” and 30% chance it will be “Good”. If today is Good Day, on average, how many days do we have to wait until the next “Bad” Day?

*Reported answer:* No final number stated. A commenter gives the full method: 如果今天是好天气,1天后是坏天气的概率是0.4,2天后坏天气的概率是0.6*0.4,3天后坏天气的概率是0.6*0.6*0.4 ... n天后的坏天气概率是0.6^(n-1)*0.4, then sums n * P(n) by the 错位相减 (shift-and-subtract) trick, noting it matches the Markov-chain answer.

> ge, how many days do we have to wait until the next “Bad” Day? 这个有很多种解法,一种麻烦的是马尔可夫过程,或者就是找规律然后用等比数列求和(*0.6 错位相减) ... 我就直接打字了。如果今天是好天气,1天后是坏天气的概率是0.4,2天后坏天气的概率是0.6*0.4,3天后坏天气的概率是0.6*0.6*0.4,4天后的坏天气概率是0.6^3*0.4 . .... 以此类推你可以找规律,n天后的坏天气概率是0.6^(n-1)*4 ... If day is a “Good” Day, is a 60% chance that the next day will be “Good” and a 40% chance it will be “Bad”. If day is a “Bad” Day, there is a 70% chance that the next 
— 1point3acres · posted 2021-02 · snippet_only · [link](https://www.1point3acres.com/bbs/thread-719224-1-1.html)
  1 attestation(s) across 1 domain(s) · doubt: The snippet returned this question's text in two disjoint pieces — the tail ('ge, how many days ...') appeared before the head — so I reassembled them into reading order. The head as returned reads 'If day is a “Good” Da

### Q3 · Tier C · unknown · online_assessment (总时长20分钟,一共是16道题 (16 questions in 20 minutes). A reply describing the s)

1. Knights always tell truth, Knaves always tell lies, and Visitors can either tell truth or lie. These people(One Knight, One Knaves, One Visitor) [text cut off by the forum paywall]

> 刚刚结束的sig(一家对冲基金) 的quantitative developer 笔试!总时长20分钟,一共是16道题。。简直不能再难(md得什么脑子才可以进这种公司????)然后我是第一次发这个东西! 折腾好久才写出来这些东西!因为地里乱七八糟规定太多,所以一直没有发成功!!! 手有余香!!真的是新人求大米!一粒就好谢谢您 .1point3acres -baidu 1point3acres 1. Knights always tell truth, Knaves always tell lies, and Visitors can either tell truth or lie. These people(One Knight, One Knaves, One Visitor)
— 1point3acres · posted 2021-02 · snippet_only · [link](https://www.1point3acres.com/bbs/thread-719224-1-1.html)
  1 attestation(s) across 1 domain(s) · doubt: Truncated right where the actual statements of the three characters would begin, so the puzzle is not reconstructible — only the setup and the unusual three-type variant (Knight / Knave / Visitor, rather than the standar

### Q4 · Tier C · unknown · online_assessment (总时长20分钟,一共是16道题 (16 questions in 20 minutes). A reply describing the s)

有个求五次导数的题我花了很久还做错了,我看了地里这个题就是有技巧可以很快的算出答案

*EN:* There was a question asking for a fifth derivative that took me ages and I still got it wrong; when I looked at this question on the forum it turns out there's a trick that gets the answer quickly.

> 不是的,也是数学题,题型和你这个差不多。有四个section,第一个section里有4道题,要求全部做完,第二个里有5道题,希望做出尽量多的题,然后后面两个section都是附加题,他们说如果你前两个里的题都做出来并认为都对的时候,可以尝试这里的题。我只做完了前两个section里的题,就是算各种概率,排列组合还有一点微积分求导求极限这类题。有个求五次导数的题我花了很久还做错了,我看了地里这个题就是有技巧可以很快的算出答案,这样就可以节省时间作出更多的题了。
— 1point3acres · posted 2021-02 · snippet_only · [link](https://www.1point3acres.com/bbs/thread-719224-1-1.html)
  1 attestation(s) across 1 domain(s) · doubt: This is a commenter describing their own SIG sitting, not the thread author's, and it names a question type ('find the fifth derivative') without stating the function — so it is a topic attestation, not a recoverable que
