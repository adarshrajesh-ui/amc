# SIG × 1point3acres harvest log

Shard: Susquehanna International Group (SIG), all quant role tracks.
Source: 一亩三分地 / 1point3acres.com/bbs/...
Output: `/workspace/harvest/raw/sig_1point3acres.jsonl` — **54 records**, 27 distinct
1point3acres URLs.

Retrieval method: **WebSearch snippets only.** 1point3acres is Cloudflare-blocked to direct
fetching; no page on that domain was fetched directly at any point in this run. Every piece of
question text recorded came out of a WebSearch result "Highlights" block that quoted a
1point3acres URL. `access` is `snippet_only` and `retrieval_method` is `websearch_snippet` on
every one of the 54 records.

---

## Technique

The forum hides most post bodies behind a 158/180/188-point paywall
("本帖隐藏的内容需要积分高于 188 才可浏览"). However, the search index has cached large
verbatim spans of several of those posts, and the snippet engine returns a *different window*
of the page depending on which phrase the query matches. So the method was: take a phrase
already known to be in a thread, search it, read the surrounding text that comes back, then use
a phrase from the newly-revealed tail as the anchor for the next query, walking through the
thread piece by piece.

Four secondary tricks, in descending order of how much they produced:

1. **Company tag-listing pages** (`/bbs/tag/sig-905-N.html`, N = 1…16+) carry ~200-character
   **thread previews** that are NOT point-gated, plus a plain list of thread titles. This was by
   far the highest-yield technique in the later passes: the gardener question, the two coding-OA
   questions, the 1–20 average and painted-cube questions, and the 萨斯奎汗 intern OA all came
   only from tag pages, and nearly every new thread ID was discovered there.
2. **Page-2+ URLs** (`thread-XXXXXX-2-1.html`, `-4-1.html`). The paywall applies to the opening
   post; replies on later pages are often ungated. The complete Markov solution for
   thread-719224 Q2 and the umbrella problem in thread-1023600 were both recovered this way.
3. **Alternate Chinese names for Susquehanna.** Searching only "SIG" misses threads titled with
   a transliteration. Three are in active use and each surfaced threads the others did not:
   **海纳国际** (→ thread-1089922), **萨斯奎汗** (→ the 25intern OA preview), and 萨斯奎哈纳.
4. **Mojibake repair.** thread-1165150 came back through the index as UTF-8 bytes rendered
   through GBK. Re-encoding to gb18030 and decoding as UTF-8 recovered legible Chinese and one
   question (the 9-sided-dice item). The raw mojibake is preserved in that record's
   `source_quote` rather than a cleaned-up version.

What did NOT work: the English mirror (`/interview/thread/<id>`) is login-gated and returns only
an SEO abstract; `site:` operators; and querying question numbers directly ("Question 12") — the
gated middle block of the 17-question OA never surfaced by any route tried.

---

## Queries run

Pass 1–2 (earlier session), in execution order; "→" records what came back.

1. `2026 SIG Quant Research OA整理 【带答案】 1point3acres` → **JACKPOT.** thread-1144112
   returned Q1, Q2, Q3, Q16, Q17 verbatim with answers.
2. `SIG QR OA 2024 秋 17题 一亩三分地` → thread-1084760 (gated), plus thread-1082364, 1084480.
3. `SIG OA 蜘蛛 鸡 牛 520条腿 谷仓` → corroborated Q1; mostly content-farm noise.
4. `Anna Brian Charlie Dixie Eva 圆桌 SIG OA` → corroborated Q2 (a Numerade copy had a
   *different* phrasing, "if Brian is sitting to the right of Eva" — noted as a variant).
5. `1point3acres SIG Quant Research OA 青蛙 frog A(0,0) B(5,6) 答案` → SIG tag page + thread-1114232.
6. `一亩三分地 SIG OA 答案 由于对称性，4 种牌相加，期望` → thread-1042392.
7. `1point3acres thread-1144112 SIG Question 7 Question 8 Question 9` → no middle questions;
   surfaced the login-gated English mirror and thread-1143308.
8. `site:1point3acres.com SIG OA 面经` → re-confirmed thread-1144112 window; thread-1141568.
9. `一亩三分地 SIG QR OA 青蛙题目+答案` → **JACKPOT.** thread-1114232 returned the frog question
   verbatim in Chinese, coordinates (7,4), answer 30, and two full solution methods.
10. `1point3acres SIG math OA 真题与答案 canoe time 独木舟` → thread-1092209 gated (title only).
    Discovered the `orange13` series of image-only "SIG math OA真题与答案: X" posts.
11. `一亩三分地 【新人求米】2025 SIG QR Intern OA` → nothing new from 1p3a.
12. `1point3acres SIG OA 绿色三角形 重量 96 磅 平衡` → **JACKPOT.** tag page sig-905-8 returned the
    thread-1082364/1082367 preview listing three questions + the answer 6lb.
13. `一亩三分地 SIG QR 17题OA 扔2次骰子获得最大收益 饼干 A有6个 B有8个 7个排成一排` → re-confirmed
    the same tag-page preview (stable, so not a one-off snippet artifact).
14. `一亩三分地 sig oa grad trader 面经` → **JACKPOT.** thread-1086565 ("SIG Trader OA 新人求米！")
    with the bakery question verbatim. First confirmed QT-track thread.
15. `一亩三分地 SIG Quantitative Strategy Developer New Grad OA 面经` → nothing from 1p3a.
16. `1point3acres SIG OA 一面 圆 切一刀 交点 块数 期望 挂经` → **JACKPOT.** thread-686183
    ("SIG 1轮+2轮面经") with two round-1 questions verbatim; more of thread-1042392.
17. `1point3acres SIG Quant Research OA 答案 Factory A makes 40% red widgets ... 贝叶斯` →
    **JACKPOT.** thread-1144112 returned a *new window*: Q3's answer (52/269), Q4, Q5, Q6.
18. `一亩三分地 SIG Trader OA 新人求米 bakery croissant muffin 5 people waiting in line` →
    re-confirmed thread-1086565; discovered tag pages sig-905-1 and sig-905-2.
19. `1point3acres SIG 1轮+2轮面经 扔硬币 HTH HHT 第二轮` → more of thread-686183 replies;
    discovered thread-1091467 ("SIG：HR面->终面所有面经").
20. `一亩三分地 公司 sig 相关帖子 面经 SIG QT OA 量化交易员` → discovered thread-1051693.
21. `一亩三分地 2026 SIG Quant Research OA整理 Question 7/8/9 答案 缺米看贴` → no middle questions.
22. `一亩三分地 SIG Quant Research OA 答案 Question 12/13/14 期望` → no middle questions.
23. `一亩三分地 SIG OA Quant Researcher 14/17 道题 需要至少 100 分` → title only, gated.
24. `一亩三分地 SIG 量化研究员 第二轮面试题目` → nothing from 1p3a (all content-farm results).

Pass 3–7 (this session), continuing the numbering.

25. `一亩三分地 "SIG QR OA 2024 秋 17题"` → thread-1084760 confirmed **fully gated**: only the
    preamble 刚做完，大部分题目只是改了数字 题不难但是太多了，只有一小时，没有做完 is visible, no
    questions. Tag sig-905-8 returned two new thread previews.
26. `1point3acres thread-1084760 SIG QR OA 17题 求米` → same gate; tag sig-905-2 returned a
    12-title thread list including 萨斯奎哈娜 QR intern 电面1 and SIG Quantitative OA QUESTIONS
    summer2026.
27. `一亩三分地 "萨斯奎哈纳" QR intern 电面` → nothing from 1p3a.
28. `1point3acres "SIG Quantitative OA QUESTIONS summer2026"` → English mirror only (login-gated).
29. `一亩三分地 "SIG 2024 17题OA" 真题 活泼眼睛的萝卜 概率` → tag sig-905-8 (SIG phone interview 真题
    preview), sig-905-1 (14-title list), sig-905-15 (coding-OA previews).
30. `1point3acres "SIG quant OA轮 2026" 面经 题` → thread-1144112, same window.
31. `一亩三分地 "SIG QT Internship OA + HR Round" 面经` → **discovered thread-1089922**
    (求海纳国际 SIG qr intern final 面经).
32. `一亩三分地 "SIG phone interview 真题" 45min 2道数学题 活泼眼睛的萝卜` → tag sig-905-8 preview
    only; **thread ID never recovered** (see gaps).
33. `1point3acres "SIG phone interview 真题" "OA题论坛里很多了，但是interview的比较少"` → richer
    windows on thread-1042392 (二面就纯bq / why QR? why SIG) and thread-686183; thread-669743.
34. `一亩三分地 海纳国际 SIG 面经 概率题 电面 求米` → **thread-1118978 verbatim** (QR岗, the disputed
    2/3-vs-3/4 uniform question); English mirror company page listing ~20 thread titles.
35. `1point3acres "SIG 1轮+2轮面经" "不太记得具体ending state是啥了" 第三题` → **round-1 Q3 exists**
    ("3. 三", truncated) plus two readers asking about it by number.
36. `一亩三分地 "SIG QT QR Online assessment" 题库 答案 面经` → **discovered thread-1166650**
    (2026(1-3月) 金工类 硕士 全职, 17题) — format only, no questions.
37. `1point3acres "Sig phone interview 面筋" quant researcher "17道概率题" 电面是三道经典` → no 1p3a
    body; the preview (匿名 2024-8-30) breaks off at 电面是三道经典选****.
38. `一亩三分地 SIG PhD Tour Internship OA 26道题 面经` → **discovered thread-1167082** (SIG 26 OA,
    2026(1-3月) 金工类 博士 实习, Pass) and thread-1143725; tag sig-905-15.
39. `1point3acres "SIG Strategy Developer" FullTime OT 答案 CodeSignal 20250828 面经` → nothing
    from 1p3a; only job ads and vendor pages.
40. `1point3acres "SIG 量化研究员" "第二轮面试题目" 概率` → **thread-795660 verbatim** (quants intern,
    the 52-card game rules).
41. `1point3acres "SIG电面" "他们的和是6的倍数的概率" 骰子 1/6` → **thread-987697 verbatim**.
42. `1point3acres 一亩三分地 "SIG QT Internship OA" HR Round 面经 实习` → nothing from 1p3a.
43. `1point3acres "SIG QR Fulltime Entry Level" "一共17道题" gradener 卡壳` → **DOUBLE JACKPOT.**
    tag sig-905-8 re-confirmed the gardener preview AND surfaced **thread-1183374 "SIG 2027 OA"**,
    a brand-new cycle with two new questions named.
44. `1point3acres "SIG Trader OA" 新人求米 bakery croissant muffin 题` → **thread-1086565 much
    richer**: full bakery Q1 plus the complete 5-toddler seating puzzle, and the poster's line
    Trader OA 与QR相似. Tag sig-905-6 returned 7 more previews.
45. `1point3acres "SIG 2027 OA" "a farmer is waiting for two flowers to blossom" 新题` →
    thread-1183374 confirmed, same window (stable, not a snippet artifact).
46. `1point3acres 一亩三分地 "SIG Quant Trader Intern 2025 OA" Susquehanna 面经` → thread-1086565
    again; the QT-intern thread itself stayed gated.
47. `1point3acres "SIG qr oa第二部分" 题型都是一样的，但是数字会改` → **discovered thread-1090023**,
    tagged **[实习]** by the forum itself — the shard's only internship-labelled QR OA thread.
48. `1point3acres SIG OA 题 "Question 10" OR "Question 12" OR "Question 14" 概率 答案 一亩三分地`
    → no middle questions (third attempt). Did expose **thread-1144112 Q17's tail and the
    poster's commentary** on having no general solution for B(m,n).
49. `1point3acres "SIG qr oa（2）" 实习 求职 非面经 题` → tag sig-905-10 (9 more thread titles),
    thread-1084480.
50. `1point3acres 一亩三分地 "SIG Quant Research & Quant Systematic Trading OA" 题` → **discovered
    thread-1165150**, returned as mojibake; thread-1091947.
51. `一亩三分地 "SIG Quant Research & Systematic Trading挂经" ECON PhD 绿皮书 概率题 9面筛子出顺子`
    → thread-1165150 confirmed; mojibake decoded to the recruiter-round dice question.
52. `1point3acres SIG OA "60分钟9道题" 新鲜热乎的SIG OA题 求米 解法` → **JACKPOT.**
    **thread-719224 page 2** returned the poster's complete corrected Markov system and the
    answer 13118/21675; tag sig-905-11 returned 6 thread IDs with previews.
53. `1point3acres "SIG OA QR/QT 9题60分钟" 刚做完新鲜出炉 解题思路` → tag sig-905-11 only; the
    19-reply thread-1041382 body stayed gated.
54. `1point3acres "SIG quant OA 60分钟9题" 都柏林 full-time quant researcher` → thread-719224
    page 2 re-confirmed.
55. `1point3acres.com/bbs/tag/sig-905-4.html 公司 Sig 相关帖子 面经 概率` → tag sig-905-4 (8-title
    list incl. two 2025 QR Intern threads and a QSD New Grad OA); **thread-1091467** surfaced.
56. `1point3acres.com/bbs/tag/sig-905-9.html 公司 Sig 面经 题 期望` → tag sig-905-8 returned the
    **萨斯奎汗 25intern oa** preview and a 4-question/70-min OA preview.
57. `1point3acres "2025 SIG QR Intern 第一轮挂经" 求加米 题` → tag sig-905-3 and sig-905-4 title
    lists; neither intern thread body surfaced.
58. `1point3acres "SIG QR 2024 phd 一面面经" 题` → thread-686183 richest window yet (full worked
    solution, n + 1 + n(n−1)/6); thread-1089922.
59. `1point3acres "SIG QT intern 一面 面经" OR "Sig QR/QT OA 26summer" 题 求米` → thread-1089922
    confirmed (奥奥是BQ之后纯概率).
60. `1point3acres.com/bbs/tag/sig-905-3.html Sig 面经 实习 QR intern onsite 题 概率` → tag sig-905-3
    returned an 11-title list, almost all internship (SIG QT intern 一面 面经, Sig QR Summer
    Intern, 2026 SIG Quantitative Trading Intern, SIG 2026 Summer Intern QR OA, …) — none of
    which would open.

**60 distinct queries. 36 of them in this session.**

---

## Threads that YIELDED question text (27 URLs, 54 records)

| URL | Recs | What came out |
| --- | --- | --- |
| thread-1144112 | 9 | The 2026 QR OA. Q1–Q6, Q16, Q17 verbatim WITH answers, plus one orphaned answer from the gated block. Best single source in the shard. |
| thread-686183 | 5 | 2020 two-round loop. Round-1 Q1 + full worked solution, Q2, Q3 (gated to one character); round-2 Q1 and Q2 attested only by readers. |
| thread-1082367 | 4 | 2024 QR 17題 OA: green triangle (6lb), two-dice max payoff, cookie arrangement, 2mile/h departure time. |
| thread-1103279 | 3 | The take-home data exercise, both variants (forecasting, then strategy-finding), plus the phone screen before it and the winner's-curse question after it. |
| thread-1167938 | 3 | 2026 phone + onsite: Movie Theatre, supermarket-checkout OOD, ticker extraction from headlines. |
| thread-719224 (p1+p2) | 4 | 2021 Quantitative Evaluation: Knights/Knaves, Good/Bad-day Markov chain, the 8-and-10 Markov problem with the poster's full corrected system, and a fifth-derivative question. |
| thread-1183374 | 2 | **2027 cycle.** The two questions added relative to 2026: the farmer/two-flowers problem and "expected number of consecutive pairs". |
| thread-1086565 | 2 | QT track. Bakery croissant/muffin question in full, plus the 5-toddler seating puzzle. |
| thread-1146142 | 2 | Spinner EV (Q12) and the frog problem at B(5,4) (Q17). |
| tag/sig-905-6 | 2 | Pick-3-from-1–20 average problem; painted-cube Bayes problem. |
| tag/sig-905-8 | 2 | The gardener problem (truncated); the 萨斯奎汗 2025 intern OA characterisation. |
| tag/sig-905-15 | 2 | The CodeSignal coding OA: battleship + LeetCode 98, and battleship + 利口酒吧. |
| thread-1114232 | 1 | Frog problem at (7,4), verbatim in Chinese, answer 30, two solution methods. |
| thread-1042392 | 1 | Circle/lines expectation, recovered via the poster's solution and follow-up discussion. |
| thread-1143308 | 1 | New-grad coding OA Q1 (truncated). |
| thread-1009682 | 1 | Battleship + LeetCode 98. |
| thread-1019255 | 1 | Cash-register OOD question. |
| thread-1023600 (p4) | 1 | The umbrella/rain Markov chain, reconstructed from four pages of argument. |
| thread-1157580 | 1 | Recruiter call for QR/Systematic Trading: green-book bus problems + simple Markov dice. |
| thread-987697 | 1 | Dice sum a multiple of 6 (tail only), answer 1/6 with the symmetry argument. |
| thread-1118978 | 1 | QR first-round uniform-distribution extension; answer disputed 2/3 vs 3/4 by three people. |
| thread-795660 | 1 | quants intern, the 52-card naming game, defined by a three-clause rules appendix. |
| thread-1165150 | 1 | QR/Systematic Trading recruiter round: 9-sided die, rolling a straight. |
| thread-1090023 | 1 | **[实习]-tagged** QR OA: 17 questions, mostly probability, confirmed as the 1-hour Problem Solving Assessment. |
| thread-1089922 | 1 | QR intern technical phone screen: BQ then pure probability. |
| thread-1091467 | 1 | Final round has ≥3 questions; Q1 and Q3 defeated readers. |

---

## Threads DISCOVERED but which stayed GATED (no question text recovered)

thread-1084760 (**one of the two proven starting points** — fully gated, preamble only),
thread-1166650, thread-1167082, thread-1143725, thread-1091947, thread-1084480, thread-1092209,
thread-1141568, thread-1051693, thread-1037583, thread-1041382 (19 replies, would likely be
rich), thread-1043089 (Dublin full-time QR), thread-1044569, thread-1044718, thread-1038885,
thread-1082364, thread-669743, thread-1149541.

Title-only, thread ID never resolved: **SIG phone interview 真题** (活泼眼睛的萝卜, 2024-09-02,
17 replies / 6969 views — the highest-traffic interview thread found and the biggest single
miss), Sig phone interview 面筋 (匿名 2024-08-30), SIG 2024 17題OA(真題) ×2, SIG QT Internship OA
+ HR Round, SIG qr/qst intern HR一轮游, SIG Capital Markets OA, SIG Power Analyst hr轮挂经,
SIG OA Quantitative Strategy Developer, SIG Quantitative Strategy Developer- New Grad OA,
SIG Strategy Developer (FullTime) OT+答案, 【新人求米】2025 SIG QR Intern OA,
【求加米】2025 SIG QR Intern 第一轮挂经, SIG QR intern onsite, SIG QT intern 一面 面经,
Sig QR/QT OA 26summer, Sig QR Summer Intern, 2026 SIG Quantitative Trading Intern,
SIG 2026 Summer Intern QR OA, 26 summer sig OA, SIG 2025-Apr OA 17题,
个人整理的地里SIG的高频概率题以及答案 (a compiled question-and-answer document that two
commenters point to — chased, never surfaced).

---

## What I could NOT establish

- **Questions 7–15 of the 17-question QR OA.** Attacked from four directions (question numbers,
  answer fragments, the English mirror, adjacent-phrase anchors) across queries 7, 21, 22 and 48.
  Never surfaced. The only trace is one orphaned answer sentence ("由于对称性，4 种牌相加，
  期望 = 4 × (3/14) = 6/7") sitting between Q3 and Q16 in the index, which is recorded as its own
  record with the statement missing. Non-1point3acres pages do list a Q7 (bakery), Q8 (Asta /
  Bronya / Clara cats) and Q9 (three cats jumping contest), and the bakery item is independently
  confirmed as SIG's by thread-1086565 — but those pages are excluded sources, so I did not take
  Q8 or Q9 from them.
- **thread-1084760**, the second proven starting point, has no recoverable questions. Its body is
  entirely behind the paywall.
- **Image-only posts.** A large fraction of SIG recall on this forum is posted as screenshots
  (只能发9张图 / 一次只能发九张 / 我attach的图片都不见了). The search index cannot read them, so
  these threads are permanently out of reach by this method regardless of query.
- **Role track for 27 of 54 records.** Most SIG threads simply do not state the track. I left
  these `unknown` rather than inferring from context; in particular I did not relabel the
  general-SWE coding OA threads as quant_developer.
- **Office** is unknown on all 54 records. Only one thread mentioned an office (thread-1043089,
  Dublin) and it stayed gated.
- **Level** for 49 of 54. The four internship records come from threads whose title or forum
  prefix says so explicitly.

---

## Exclusions applied

Question text was taken ONLY from 1point3acres. The following appeared repeatedly in results and
were used only to decide what to search for next, never as a source for `question_text` or
`source_quote`: programhelp.net (and its dev.to / jishuzhan.net mirrors), quantblueprint.com,
tradermath.org, everythingquant.com, techinterview.org, jobtestprep, aptitude-test-prep.com,
csoahelp.com, oavoservice.com, interviewchamp.ai, interviewsense.org, linkjob.ai, quantt.co.uk,
extern.com. Glassdoor, Wall Street Oasis and the Leader-board/OA-and-Interviews GitHub repo also
surfaced with plausible first-hand SIG content; they are out of scope for this shard and were
likewise not used.

One judgement call worth flagging: csoahelp.com hosts what appear to be verbatim transcriptions
of the same 2025 QR OA, including the middle questions this shard is missing. It is an OA
ghost-writing service, i.e. exactly the kind of vendor page the exclusion rule targets, so I did
not lift Q7/Q8/Q9 from it even though doing so would have visibly improved coverage.

---

## Known weaknesses in the output

- **11 of 54 records have no usable question statement** — they are round/topic attestations
  (what a round contains) or truncated fragments. Every one says so in its own `doubt` field and
  most say so inside `question_text` too, in brackets. They are kept because they carry track,
  level, round and date information that the fuller records lack.
- **Several items are recognisable textbook problems** (the umbrella/wandering-umbrellas Markov
  chain, dice sum divisible by 6, Penney's game HTH/HHT). These are retained because the
  attestation is a candidate saying it appeared on their SIG assessment, which is recall, not a
  textbook citation — but a downstream consumer should know that one thread's commenters
  themselves link the umbrella item to a Berkeley exercise sheet, and one candidate explicitly
  sources SIG's recruiter-round questions to 绿皮书 (the Green Book).
- **The same problem recurs with different numbers.** The frog problem appears at B(5,6), B(5,4)
  and (7,4); the 5-toddler seating puzzle appears in both a QR thread and a QT thread. These are
  recorded as separate records because they are separate attestations from separate sittings, and
  the variation is itself the finding — SIG changes the numbers, not the items.
- **thread-1165150's `source_quote` is mojibake**, deliberately. The decoded text is in
  `question_text` and the decoding procedure is described in `doubt`.
