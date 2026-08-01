# Citadel · unknown internship · nowcoder

- **Source family:** nowcoder
- **Items:** 7
- **Date range:** 2021-01-26 – 2021-01-26 (3/7 dated)
- **Tier mix:** B=3, C=2, D=2

---
### Q1 · Tier B · unknown · phone_technical

如果两个变量0.999相关,权重会如何分配,如果是lasso 和 ridge分别会如何,实践中如何选择保留哪个变量。

*EN:* If two variables are 0.999 correlated, how will the weights be distributed? What happens under lasso and under ridge respectively? In practice how do you choose which variable to keep?

> # 城堡hk量化实习两轮电面挂经 牛客逛了一圈没有看到类似的面经,就分享一下。lz港校cs phd,非主流生物方向。找了一圈quant的实习,没有相关实习经历,research也不太行,基本都在简历就挂了,akuna上海挂在第一轮电面,大城堡投了两次终于被捞起来,上个月给了一个电面,上周又面了一轮,然后挂了。 一面小哥是刚毕业的牛津统计phd,ml方向,聊了十几分钟简历项目,然后开始问线性回归,解析解是什么,如果样本数量n很大不能同时放进内存怎么办,分成几部分来算,为什么可以这样做,因为XTX是dxd的矩阵。如果两个变量0.999相关,权重会如何分配,如果是lasso 和 ridge分别会如何,实践中如何选择保留哪个变量。如果在x加上噪声,会怎么样,分别从直观感受和推导上说,最后一直说到给x加噪声可以起到和正则化同样的作用。
— nowcoder · posted 2021-01-26 · full_text · [link](https://www.nowcoder.com/discuss/353157497731096576)
  1 attestation(s) across 1 domain(s) · doubt: Nowcoder renders no visible publication date on the fetched page, so the cycle and recency of this recall cannot be pinned down at all — the questions could be several years old; also the poster writes from memory in sum

### Q2 · Tier B · unknown · phone_technical

如果在x加上噪声,会怎么样,分别从直观感受和推导上说,最后一直说到给x加噪声可以起到和正则化同样的作用。

*EN:* If you add noise to x, what happens? Explain both intuitively and by derivation. (Led to: adding noise to x has the same effect as regularisation.)

*Reported answer:* 给x加噪声可以起到和正则化同样的作用

> # 城堡hk量化实习两轮电面挂经 牛客逛了一圈没有看到类似的面经,就分享一下。lz港校cs phd,非主流生物方向。找了一圈quant的实习,没有相关实习经历,research也不太行,基本都在简历就挂了,akuna上海挂在第一轮电面,大城堡投了两次终于被捞起来,上个月给了一个电面,上周又面了一轮,然后挂了。 一面小哥是刚毕业的牛津统计phd,ml方向,聊了十几分钟简历项目,然后开始问线性回归,解析解是什么,如果样本数量n很大不能同时放进内存怎么办,分成几部分来算,为什么可以这样做,因为XTX是dxd的矩阵。如果两个变量0.999相关,权重会如何分配,如果是lasso 和 ridge分别会如何,实践中如何选择保留哪个变量。如果在x加上噪声,会怎么样,分别从直观感受和推导上说,最后一直说到给x加噪声可以起到和正则化同样的作用。
— nowcoder · posted 2021-01-26 · full_text · [link](https://www.nowcoder.com/discuss/353157497731096576)
  1 attestation(s) across 1 domain(s) · doubt: Nowcoder renders no visible publication date on the fetched page, so the cycle and recency of this recall cannot be pinned down at all — the questions could be several years old; also the poster writes from memory in sum

### Q3 · Tier B · unknown · phone_technical

如果样本数量n很大不能同时放进内存怎么办,分成几部分来算,为什么可以这样做,因为XTX是dxd的矩阵。

*EN:* If the number of samples n is so large that the data cannot all be held in memory at once, what do you do? Split it into several parts and compute; why is that valid? (Because X^T X is a d x d matrix.)

*Reported answer:* 因为XTX是dxd的矩阵

> # 城堡hk量化实习两轮电面挂经 牛客逛了一圈没有看到类似的面经,就分享一下。lz港校cs phd,非主流生物方向。找了一圈quant的实习,没有相关实习经历,research也不太行,基本都在简历就挂了,akuna上海挂在第一轮电面,大城堡投了两次终于被捞起来,上个月给了一个电面,上周又面了一轮,然后挂了。 一面小哥是刚毕业的牛津统计phd,ml方向,聊了十几分钟简历项目,然后开始问线性回归,解析解是什么,如果样本数量n很大不能同时放进内存怎么办,分成几部分来算,为什么可以这样做,因为XTX是dxd的矩阵。如果两个变量0.999相关,权重会如何分配,如果是lasso 和 ridge分别会如何,实践中如何选择保留哪个变量。如果在x加上噪声,会怎么样,分别从直观感受和推导上说,最后一直说到给x加噪声可以起到和正则化同样的作用。
— nowcoder · posted 2021-01-26 · full_text · [link](https://www.nowcoder.com/discuss/353157497731096576)
  1 attestation(s) across 1 domain(s) · doubt: Nowcoder renders no visible publication date on the fetched page, so the cycle and recency of this recall cannot be pinned down at all — the questions could be several years old; also the poster writes from memory in sum

### Q4 · Tier C · unknown · phone_technical

然后是给定一堆x,求y使得 sum|x_i-y| 最小,随口说了mean,面试官说是median,然后问怎么median,先说了排序,又问怎么优化,说了quick select,然后让对比quick select和quick sort。

*EN:* Given a pile of x values, find y minimising sum|x_i - y|. (Answer: the median, not the mean.) Then how do you find the median? Sorting first, then how to optimise -- quickselect; then compare quickselect with quicksort.

*Reported answer:* 面试官说是median;优化用 quick select

> 然后是给定一堆x,求y使得 sum|x_i-y| 最小,随口说了mean,面试官说是median,然后问怎么median,先说了排序,又问怎么优化,说了quick select,然后让对比quick select和quick sort。
— nowcoder · posted unknown · full_text · [link](https://www.nowcoder.com/discuss/353157497731096576)
  1 attestation(s) across 1 domain(s) · doubt: Nowcoder renders no visible publication date on the fetched page, so the cycle and recency of this recall cannot be pinned down at all — the questions could be several years old; also the poster writes from memory in sum

### Q5 · Tier C · unknown · phone_technical

先是求第n个斐波那契数,时空复杂度,然后问了如何优化,说了矩阵快速幂,问了一些具体的做法。

*EN:* Find the n-th Fibonacci number; give the time and space complexity, then how would you optimise it? (Matrix fast exponentiation, and the specifics of how to do it.)

*Reported answer:* 矩阵快速幂

> 先是求第n个斐波那契数,时空复杂度,然后问了如何优化,说了矩阵快速幂,问了一些具体的做法。
— nowcoder · posted unknown · full_text · [link](https://www.nowcoder.com/discuss/353157497731096576)
  1 attestation(s) across 1 domain(s) · doubt: Nowcoder renders no visible publication date on the fetched page, so the cycle and recency of this recall cannot be pinned down at all — the questions could be several years old; also the poster writes from memory in sum

### Q6 · Tier D · unknown · phone_technical

然后问一堆数据复制一遍,mean和variance会不会变。

*EN:* If you duplicate a pile of data (each point repeated once), do the mean and the variance change?

> 先聊了二十分钟简历项目,然后问一堆数据复制一遍,mean和variance会不会变。
— nowcoder · posted unknown · full_text · [link](https://www.nowcoder.com/discuss/353157497731096576)
  1 attestation(s) across 1 domain(s) · doubt: Nowcoder renders no visible publication date on the fetched page, so the cycle and recency of this recall cannot be pinned down at all — the questions could be several years old; also the poster writes from memory in sum

### Q7 · Tier D · unknown · phone_technical

然后开始问线性回归,解析解是什么

*EN:* Linear regression: what is the closed-form (analytic) solution?

> 聊了十几分钟简历项目,然后开始问线性回归,解析解是什么,如果样本数量n很大不能同时放进内存怎么办
— nowcoder · posted unknown · full_text · [link](https://www.nowcoder.com/discuss/353157497731096576)
  1 attestation(s) across 1 domain(s) · doubt: Nowcoder renders no visible publication date on the fetched page, so the cycle and recency of this recall cannot be pinned down at all — the questions could be several years old; also the poster writes from memory in sum
