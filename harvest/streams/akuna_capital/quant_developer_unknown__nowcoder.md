# Akuna Capital · quant developer unknown · nowcoder

- **Source family:** nowcoder
- **Items:** 12
- **Date range:** 2016-10-25 – 2022-09-09 (11/12 dated)
- **Tier mix:** B=5, C=1, D=6

---
### Q1 · Tier B · unknown · online_assessment (10选择必须20分钟 + 6选择+2编程26min)

10选择必须20分钟,记了3题 英语题打起来不用频繁切换中英文了 6选择+2编程26min,这块选择没什么好记的 Unit testing. x y z // 1. 检查二叉搜索树中是否包含某个值

*EN:* 10 multiple-choice questions with a mandatory 20 minutes; then 6 multiple-choice + 2 coding in 26 minutes. Coding Q1: check whether a binary search tree contains a given value.

> 10选择必须20分钟,记了3题 英语题打起来不用频繁切换中英文了 6选择+2编程26min,这块选择没什么好记的
— nowcoder · posted 2022-09-04 · full_text · [link](https://www.nowcoder.com/discuss/396088849078685696)
  1 attestation(s) across 1 domain(s) · doubt: Recovered permalink: this record originally cited nowcoder's client-rendered search page and was marked snippet_only for that reason. Driving nowcoder's search API surfaced the underlying thread, which curl fetches in fu

### Q2 · Tier B · unknown · phone_technical (全英面试,但一上来就做题,四题完了后就反问然后结束)

求int里1的个数是否为奇数 改错,求二叉树最大值(看成了二叉搜索树,写完后提示后再改的) 让修改账户balance值函数变成线程安全的(直接加了两个锁,伪代码) 实现一个模板最小堆

*EN:* Determine whether the count of 1s in an int is odd; fix a bug and find the maximum of a binary tree (I mistook it for a BST and corrected after a hint); make an account-balance function thread-safe (I just added two locks, pseudocode); implement a templated min-heap.

> 全英面试,但一上来就做题,四题完了后就反问然后结束
— nowcoder · posted 2022-09-09 · full_text · [link](https://www.nowcoder.com/discuss/397714545857376256)
  1 attestation(s) across 1 domain(s) · doubt: Recovered permalink: this record originally cited nowcoder's client-rendered search page and was marked snippet_only for that reason. Driving nowcoder's search API surfaced the underlying thread, which curl fetches in fu

### Q3 · Tier B · unknown · phone_technical (直接做题 没有自我介绍)

第一题 求一个数的奇偶校验位 第二题 求二叉树节点最大值 第三题 给一个函数,要求修改成线程安全的 第四题 手写priority_queue

*EN:* Q1: compute the parity bit of a number. Q2: find the maximum node value in a binary tree. Q3: given a function, modify it to be thread-safe. Q4: hand-write a priority_queue.

> 第一题 求一个数的奇偶校验位 第二题 求二叉树节点最大值 第三题 给一个函数,要求修改成线程安全的 第四题 手写priority_queue(构造,析构,push,top,pop)
— nowcoder · posted 2022-08-03 · full_text · [link](https://www.nowcoder.com/feed/main/detail/5363d0b8413448fdb1a2e0c48379aee8)
  1 attestation(s) across 1 domain(s) · doubt: Recovered permalink: this record originally cited nowcoder's client-rendered search page and was marked snippet_only for that reason. Driving nowcoder's search API surfaced the underlying thread, which curl fetches in fu

### Q4 · Tier B · unknown · onsite

申的C++ Junior Dev,似乎要on-site了,有人面过么?求点经验,感觉略虚,还是E文的。

*EN:* I applied for C++ Junior Dev and it looks like I'm going to on-site. Has anyone interviewed? Looking for some experience — I feel a bit shaky, and it's in English too.

> 申的C++ Junior Dev,似乎要on-site了,有人面过么?求点经验,感觉略虚,还是E文的。
— nowcoder · posted 2016-10-25 · full_text · [link](https://www.nowcoder.com/discuss/353153964797534208)
  1 attestation(s) across 1 domain(s) · doubt: nowcoder posts are pseudonymous 面经 write-ups with no verification; the poster is recalling questions after the fact, so wording is theirs rather than the interviewer's. This is a request for advice, not a recall — it con

### Q5 · Tier B · unknown · phone_technical (直接做题 没有自我介绍,四题,做完题反问)

第四题 手写priority_queue(构造,析构,push,top,pop)

*EN:* Question 4: hand-write a priority_queue (constructor, destructor, push, top, pop).

> 第三题 给一个函数,要求修改成线程安全的 第四题 手写priority_queue(构造,析构,push,top,pop)
— nowcoder · posted 2022-08-03 · full_text · [link](https://www.nowcoder.com/feed/main/detail/5363d0b8413448fdb1a2e0c48379aee8)
  1 attestation(s) across 1 domain(s) · doubt: Short bulleted recall with no problem statements — each line names a task in a handful of characters. A commenter on the same post replies '都是典型的题啊' (these are all standard questions), which is consistent with, but not p

### Q6 · Tier C · unknown · phone_technical

自我介绍。可以去一亩三分地论坛上搜akuna的面经,基本都是类似的那种问题,反正全都是概念。

*EN:* Introduce yourself. You can search 1point3acres for Akuna interview write-ups — they are basically all the same sort of question, all concepts.

> akuna capital【1面跪,全程英文】 自我介绍。
— nowcoder · posted unknown · full_text · [link](https://www.nowcoder.com/discuss/353153972942872576)
  1 attestation(s) across 1 domain(s) · doubt: Topic-level only: the poster names no question beyond 自我介绍 and explicitly redirects readers to another forum for the content, so this attests the round's character (all-English, all conceptual) rather than any specific q

### Q7 · Tier D · 2023 · online_assessment (10选择必须20分钟;6选择+2编程26min)

// 1. 检查二叉搜索树中是否包含某个值 // 只需要实现in

*EN:* 1. Check whether a binary search tree contains a given value. You only need to implement `in`.

*Reported answer:* int in(node* root, int val){ while(root){ if(root->val==val)return true; else if(root->val<val) root=root->right; else root=root->left; } return false; }

> // 1. 检查二叉搜索树中是否包含某个值 // 只需要实现in
— nowcoder · posted 2022-09-04 · full_text · [link](https://www.nowcoder.com/discuss/396088849078685696)
  1 attestation(s) across 1 domain(s) · doubt: The poster reconstructed the questions as C++ solution code after the fact rather than copying the prompts off the test screen, so the wording of each problem is their own summary; they also say plainly '记了3题' and '这块选择没

### Q8 · Tier D · 2023 · online_assessment (10选择必须20分钟;6选择+2编程26min)

// 2. 求不超过某上限的最大连续子数组和

*EN:* 2. Find the largest sum of a contiguous subarray that does not exceed a given upper bound.

*Reported answer:* unsigned f(unsigned n, unsigned b, unsigned p[]) { unsigned rb=0, maxrb=0; for(int i=0,j=0;i<n;i++){ rb+=p[i]; while(j<=i&&rb>b) rb-=p[j++]; if(maxrb<rb) maxrb=rb; } return maxrb; }

> // 2. 求不超过某上限的最大连续子数组和 unsigned f(unsigned n, unsigned b, unsigned p[]) {
— nowcoder · posted 2022-09-04 · full_text · [link](https://www.nowcoder.com/discuss/396088849078685696)
  1 attestation(s) across 1 domain(s) · doubt: The poster reconstructed the questions as C++ solution code after the fact rather than copying the prompts off the test screen, so the wording of each problem is their own summary; they also say plainly '记了3题' and '这块选择没

### Q9 · Tier D · unknown · phone_technical (直接做题 没有自我介绍,四题,做完题反问)

第三题 给一个函数,要求修改成线程安全的

*EN:* Question 3: given a function, modify it to be thread-safe.

> 第二题 求二叉树节点最大值 第三题 给一个函数,要求修改成线程安全的
— nowcoder · posted 2022-08-03 · full_text · [link](https://www.nowcoder.com/feed/main/detail/5363d0b8413448fdb1a2e0c48379aee8)
  1 attestation(s) across 1 domain(s) · doubt: Short bulleted recall with no problem statements — each line names a task in a handful of characters. A commenter on the same post replies '都是典型的题啊' (these are all standard questions), which is consistent with, but not p

### Q10 · Tier D · unknown · phone_technical (直接做题 没有自我介绍,四题,做完题反问)

第一题 求一个数的奇偶校验位

*EN:* Question 1: compute the parity bit of a number.

> 直接做题 没有自我介绍 第一题 求一个数的奇偶校验位
— nowcoder · posted 2022-08-03 · full_text · [link](https://www.nowcoder.com/feed/main/detail/5363d0b8413448fdb1a2e0c48379aee8)
  1 attestation(s) across 1 domain(s) · doubt: Short bulleted recall with no problem statements — each line names a task in a handful of characters. A commenter on the same post replies '都是典型的题啊' (these are all standard questions), which is consistent with, but not p

### Q11 · Tier D · 2023 · online_assessment (6选择+2编程26min)

Unit testing.

> 6选择+2编程26min,这块选择没什么好记的 Unit testing.
— nowcoder · posted 2022-09-04 · full_text · [link](https://www.nowcoder.com/discuss/396088849078685696)
  1 attestation(s) across 1 domain(s) · doubt: The poster reconstructed the questions as C++ solution code after the fact rather than copying the prompts off the test screen, so the wording of each problem is their own summary; they also say plainly '记了3题' and '这块选择没

### Q12 · Tier D · unknown · phone_technical (直接做题 没有自我介绍,四题,做完题反问)

第二题 求二叉树节点最大值

*EN:* Question 2: find the maximum node value in a binary tree.

> 第一题 求一个数的奇偶校验位 第二题 求二叉树节点最大值
— nowcoder · posted 2022-08-03 · full_text · [link](https://www.nowcoder.com/feed/main/detail/5363d0b8413448fdb1a2e0c48379aee8)
  1 attestation(s) across 1 domain(s) · doubt: Short bulleted recall with no problem statements — each line names a task in a handful of characters. A commenter on the same post replies '都是典型的题啊' (these are all standard questions), which is consistent with, but not p
