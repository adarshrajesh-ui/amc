# Citadel · unknown unknown · nowcoder

- **Source family:** nowcoder
- **Items:** 3
- **Date range:** unknown – unknown (0/3 dated)
- **Tier mix:** C=2, D=1

---
### Q1 · Tier C · 2026(源帖标题「Citadel vo2026面经」) · superday (终面 60 分钟,含 why-Citadel、行为题、系统设计三部分)

系统设计是全球交易系统,四地多活+Anycast就近接入,跨区域走专线,多主复制+版本向量保一致性,交易路径用Saga,接受短暂不一致但最终收敛,每层冗余+熔断重试保证五个九可用性。

*EN:* System design: a global trading system — four-site active-active with Anycast for nearest-point ingress, dedicated lines across regions, multi-master replication plus version vectors for consistency, Saga for the trading path (accepting brief inconsistency that eventually converges), redundancy at every layer plus circuit-breaking and retries to reach five-nines availability.

*Reported answer:* 发帖人自述回答即题干内容(四地多活+Anycast、专线、多主复制+版本向量、Saga、五个九)

> # Citadel vo2026面经 Citadel面试跟大厂不一样,不考原题不背八股,全程场景驱动,面试官深挖交易系统,追问到你不会为止。刚过三轮Onsite 还是蛮简单的offer稳了 有需要的可以问问 北美oa/vo都可以辅助。 Citadel终面刚结束,Tech Lead面的,60分钟。先问了为什么选Citadel,我说这里工程师直接对盈亏负责,离业务近,比大厂写边缘模块有成就感。行为题讲了实习优化回测框架的事,用profiling找到性能瓶颈,拿数据说服研究员后用SIMD重写,提速40%。系统设计是全球交易系统,四地多活+Anycast就近接入,跨区域走专线,多主复制+版本向量保一致性,交易路径用Saga,接受短暂不一致但最终收敛,每层冗余+熔断重试保证五个九可用性。 反问面试官给了实在建议:基础比框架重要,OS、网络、编译原理吃透,真本事在实战里磨。 北美各大小厂都比较有经验,oa vo都可以来问问
— nowcoder · posted unknown(帖子只显示「07-20 23:52」,无年份;标题自称 vo2026) · full_text · [link](https://www.nowcoder.com/feed/main/detail/116a865d3e564be4a175d6ba580d1fc7)
  1 attestation(s) across 1 domain(s) · doubt: 发帖人是卖「北美 OA/VO 辅助」(即代面/实时助攻)的中介,不是普通复盘的候选人,整帖的功能是广告;按任务的硬性排除规则这类卖服务的帖子原则上应剔除,此处保留仅因为 URL 与正文是我实际读到的原文。可信度问题很具体:(1) 帐号所属学校(法国克莱蒙费朗)与自称的「北美 Citadel 终面」不匹配;(2) 「刚过三轮Onsite 还是蛮简单的offer稳了」这种表述不像真实候选人的语气;(3) 系统设计答案写得像模板化的架构清单(

### Q2 · Tier C · 2026(源帖标题「Citadel vo2026面经」) · superday (终面 60 分钟,含 why-Citadel、行为题、系统设计三部分)

行为题讲了实习优化回测框架的事,用profiling找到性能瓶颈,拿数据说服研究员后用SIMD重写,提速40%。

*EN:* Behavioural question: I talked about optimising a backtesting framework during an internship — using profiling to find the bottleneck, persuading the researchers with data, then rewriting with SIMD for a 40% speed-up.

*Reported answer:* 发帖人自述回答即题干内容(profiling 定位瓶颈 → 用数据说服研究员 → SIMD 重写 → 提速 40%)

> # Citadel vo2026面经 Citadel面试跟大厂不一样,不考原题不背八股,全程场景驱动,面试官深挖交易系统,追问到你不会为止。刚过三轮Onsite 还是蛮简单的offer稳了 有需要的可以问问 北美oa/vo都可以辅助。 Citadel终面刚结束,Tech Lead面的,60分钟。先问了为什么选Citadel,我说这里工程师直接对盈亏负责,离业务近,比大厂写边缘模块有成就感。行为题讲了实习优化回测框架的事,用profiling找到性能瓶颈,拿数据说服研究员后用SIMD重写,提速40%。系统设计是全球交易系统,四地多活+Anycast就近接入,跨区域走专线,多主复制+版本向量保一致性,交易路径用Saga,接受短暂不一致但最终收敛,每层冗余+熔断重试保证五个九可用性。 反问面试官给了实在建议:基础比框架重要,OS、网络、编译原理吃透,真本事在实战里磨。 北美各大小厂都比较有经验,oa vo都可以来问问
— nowcoder · posted unknown(帖子只显示「07-20 23:52」,无年份;标题自称 vo2026) · full_text · [link](https://www.nowcoder.com/feed/main/detail/116a865d3e564be4a175d6ba580d1fc7)
  1 attestation(s) across 1 domain(s) · doubt: 发帖人是卖「北美 OA/VO 辅助」(即代面/实时助攻)的中介,不是普通复盘的候选人,整帖的功能是广告;按任务的硬性排除规则这类卖服务的帖子原则上应剔除,此处保留仅因为 URL 与正文是我实际读到的原文。可信度问题很具体:(1) 帐号所属学校(法国克莱蒙费朗)与自称的「北美 Citadel 终面」不匹配;(2) 「刚过三轮Onsite 还是蛮简单的offer稳了」这种表述不像真实候选人的语气;(3) 系统设计答案写得像模板化的架构清单(

### Q3 · Tier D · 2026(源帖标题「Citadel vo2026面经」) · superday (终面 60 分钟,含 why-Citadel、行为题、系统设计三部分)

先问了为什么选Citadel

*EN:* First they asked why I chose Citadel.

*Reported answer:* 发帖人自述回答:「这里工程师直接对盈亏负责,离业务近,比大厂写边缘模块有成就感」

> # Citadel vo2026面经 Citadel面试跟大厂不一样,不考原题不背八股,全程场景驱动,面试官深挖交易系统,追问到你不会为止。刚过三轮Onsite 还是蛮简单的offer稳了 有需要的可以问问 北美oa/vo都可以辅助。 Citadel终面刚结束,Tech Lead面的,60分钟。先问了为什么选Citadel,我说这里工程师直接对盈亏负责,离业务近,比大厂写边缘模块有成就感。行为题讲了实习优化回测框架的事,用profiling找到性能瓶颈,拿数据说服研究员后用SIMD重写,提速40%。系统设计是全球交易系统,四地多活+Anycast就近接入,跨区域走专线,多主复制+版本向量保一致性,交易路径用Saga,接受短暂不一致但最终收敛,每层冗余+熔断重试保证五个九可用性。 反问面试官给了实在建议:基础比框架重要,OS、网络、编译原理吃透,真本事在实战里磨。 北美各大小厂都比较有经验,oa vo都可以来问问
— nowcoder · posted unknown(帖子只显示「07-20 23:52」,无年份;标题自称 vo2026) · full_text · [link](https://www.nowcoder.com/feed/main/detail/116a865d3e564be4a175d6ba580d1fc7)
  1 attestation(s) across 1 domain(s) · doubt: 发帖人是卖「北美 OA/VO 辅助」(即代面/实时助攻)的中介,不是普通复盘的候选人,整帖的功能是广告;按任务的硬性排除规则这类卖服务的帖子原则上应剔除,此处保留仅因为 URL 与正文是我实际读到的原文。可信度问题很具体:(1) 帐号所属学校(法国克莱蒙费朗)与自称的「北美 Citadel 终面」不匹配;(2) 「刚过三轮Onsite 还是蛮简单的offer稳了」这种表述不像真实候选人的语气;(3) 系统设计答案写得像模板化的架构清单(
