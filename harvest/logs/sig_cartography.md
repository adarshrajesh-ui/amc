# SIG (Susquehanna) hiring-funnel cartography — run log

Scope: PROCESS MAP of Susquehanna International Group's hiring funnel, per track and level,
built only from first-person candidate accounts plus SIG's own job postings.
Priority track: Quantitative Trader INTERNSHIP.
Sibling artifact: `/workspace/harvest/logs/sig_1point3acres.md` (a parallel agent harvesting SIG
*questions* from 1point3acres). This log is independent; where I rely on a fact that agent also
found, I re-verified it with my own query and cite my own retrieval.

---

## Network reality as actually observed in this run

| Domain | WebFetch | Notes |
|---|---|---|
| wallstreetoasis.com | **works** | Occasional timeouts under rapid successive fetches; retry succeeds. This was the single richest source. |
| teamblind.com | **works** | Post bodies + top comments visible; deeper comments gated. |
| saykind.github.io | **works** | Personal blog; PDFs downloadable via `curl`. |
| 1point3acres.com | **BLOCKED** | Verified directly: `curl` returns `HTTP 403` with Cloudflare `Just a moment...` interstitial. `r.jina.ai` proxy also returned 403. **No 1point3acres page was fetched in this run**; every 1p3a datum below comes from a WebSearch "Highlights" snippet. |
| glassdoor.com | **not fetched** | But the WebSearch tool *side-loaded the full Glassdoor page text to disk* as a search artifact (`agent-tools/295a8006-…txt`, 418 lines). That file was read and is the source of the dated Glassdoor quotes below. This is a retrieval of real page content, not a fetch of glassdoor.com. |
| sig.com | partial | `sig.com/careers/students/` → 404. `sig.com/careers/quant/` and `sig.com/who-we-are/game-theory-decision-science/` returned via search but contain no interview-process detail. |

Nowcoder was searched but is a dead end for this firm: the token "SIG" collides with `signal`,
`SIGKILL`, Kubernetes SIGs, and the unrelated Chinese VC "SIG海纳亚洲". Zero Susquehanna hits.

---

## Queries run (in order)

English:
1. `SIG Susquehanna quant trader intern online assessment 17 questions 1 hour`
2. `site:reddit.com SIG Susquehanna quant trader internship online assessment format` → **zero results** (the `site:` operator returns nothing on this engine)
3. `reddit SIG Susquehanna OA quant trader intern "how many questions" experience`
4. `wallstreetoasis.com susquehanna-international-group interview intern "Bala Cynwd" 2025 prop trading`
5. `wallstreetoasis Susquehanna "Quant Trader Intern" interview Bala Cynwyd online assessment`
6. `Susquehanna Dublin trading online maths test "27 questions" probability HR telephone interview`
7. `glassdoor Susquehanna International Group "Quant Trader Intern" interview questions online assessment`
8. `glassdoor Susquehanna International Group Quantitative Researcher interview questions online assessment rounds`
9. `https://www.glassdoor.com/Interview/Susquehanna-International-Group-Quant-Trader-Intern-…` (exact-URL search; did not surface the page)
10. `"wallstreetoasis.com/company/susquehanna-international-group/interview" quant trader intern quantitative trading`
11. `reddit Susquehanna SIG superday onsite trading game market making poker quant trader intern experience`
12. `SIG Susquehanna online assessment calculator allowed scratch paper go back previous question proctored webcam`
13. `teamblind blind SIG Susquehanna online assessment quant trader interview process rounds`
14. `wallstreetoasis Susquehanna quant trader superday "final round" onsite interview trading game experience Bala Cynwyd`
15. `reddit r/quant SIG Susquehanna quant trader internship OA "17 questions" OR "16 questions" assessment`
16. `Susquehanna "Quantitative Analyst" OR "Quant Analyst" interview online assessment rounds glassdoor Dublin`
17. `Susquehanna SIG interview "personality test" OR "decision making questionnaire" OR "personality questionnaire" candidate assessment`
18. `"SIG" Susquehanna online assessment sequences test mental math separate section candidate reddit 2025 2026`
19. `SIG Susquehanna Hong Kong Sydney quant trader graduate interview process online assessment account`
20. `sig.com careers interview process "Online Assessment" "Office Interview" quantitative trader internship application steps`
21. `Susquehanna Dublin London graduate trader online test "how many questions" maths test 2025 2026 candidate experience forum`
22. `"susquehanna" OR "SIG" quant trader intern reddit r/quantfinance OA rejected superday timeline weeks heard back`

Chinese:
23. `SIG 面试流程 量化 交易员 实习 面经`
24. `1point3acres SIG OA 17题 量化 面经`
25. `1point3acres "SIG QT Internship OA" HR Round 面经`
26. `1point3acres "SIG OA Quant Researcher" "14/17" 需要至少 100 分`
27. `SIG OA 几道题 笔试 时间限制 量化 交易 一亩三分地 2025`
28. `1point3acres "SIG SWE OA" Fresh Grad 面经 四道题 codesignal`
29. `1point3acres 一亩三分地 SIG QT QR Online assessment 面经 17题 一小时 计算器`
30. `SIG 网测 海纳国际 笔试 面经 实习 应届生`
31. `一亩三分地 SIG QT Internship OA HR Round 量化交易 实习 面经 2025 2026`
32. `1point3acres SIG Phone Onsite 面经 vo 全套 量化 派对 trading game 扑克`
33. `一亩三分地 SIG Trader OA 新人求米 bakery croissant muffin 5 people waiting in line 面经`
34. `1point3acres 2026 SIG Quant Research OA整理 带答案 17题 Question 17`
35. `SIG 笔试` (via nowcoder site search) → noise only

Direct site search: `nowcoder.com/search?type=post&query=SIG 笔试` (fetched; noise only).

---

## URLs actually retrieved (content read)

**Wall Street Oasis (fetched):**
- `https://www.wallstreetoasis.com/company/susquehanna-international-group/interview/graduate-quant-trader`
- `https://www.wallstreetoasis.com/company/susquehanna-international-group` (company overview)
- `https://www.wallstreetoasis.com/company/susquehanna-international-group/interview` (index; 258 interviews, 26 pages — but only the 10 most recent carry full text; `?page=N` re-pages the summary *table* only, not the detail blocks)
- `https://www.wallstreetoasis.com/company/susquehanna-international-group/interview?page=1`
- `…/interview/trading-systems-engineer-intern`
- `…/interview/quant-trader-intern`
- `…/interview/quantitative-trader-intern`
- `…/interview/quantitative-trading-intern`
- `…/interview/trader-intern`
- `…/interview/quantitative-research`

**Blind (fetched):**
- `https://www.teamblind.com/post/SIG-Interview-Process-w22t1O4b`
- `https://www.teamblind.com/post/DD41JZvG`

**Personal blog + PDFs (fetched / curl'd):**
- `https://saykind.github.io/interviews/quant-SIG/`
- `https://saykind.github.io/files/interviews/quant-SIG-problems.pdf` (extracted → `sig_problem_solving_assessment_saykin_extract.txt`)
- `https://saykind.github.io/files/interviews/quant-SIG-solutions.pdf`
- `https://saykind.github.io/sitemap.xml` (used to date the post: **2024-11-29**)

**Glassdoor (full page text side-loaded by the search tool, then read):**
- `https://www.glassdoor.com/Interview/Susquehanna-International-Group-Quantitative-Trader-Interview-Questions-EI_IE24446.0,31_KO32,51.htm`

**SIG's own postings (retrieved via search result + side-loaded file):**
- `https://simplify.jobs/p/d11d99ce-06a3-4c8c-b15f-e6d562a1190a/Graduate-Quantitative-Trader` (Sydney)
- `https://au.gradconnection.com/employers/susquehanna-international-group/jobs/susquehanna-international-group-quantitative-trader-internship-november-2026-3/`
- `https://www.quantblueprint.com/jobs/sig-quantitative-trading-internship-november-2026-expression-of-interest` (reposts SIG's own process text)

**1point3acres (SNIPPET ONLY — never fetched):**
- `/bbs/tag/sig-905-1.html`, `/bbs/tag/sig-905-15.html`, `/bbs/tag/sig-905-16.html` (thread inventories; 534 threads, 407 面经)
- `/bbs/thread-1084760-1-1.html` — "SIG QR OA 2024 秋 17题"
- `/bbs/thread-1082367-1-1.html` — "SIG QR 17题OA"
- `/bbs/thread-1166650-1-1.html` — "SIG QT QR Online assessment"
- `/bbs/thread-1086565-1-1.html` — "SIG Trader OA 新人求米！"
- `/bbs/thread-1084480-1-1.html` — "SIG Quant OA面经" ("SIG Quant 17题面经")
- `/bbs/thread-1144112-1-1.html` + `/interview/thread/1144112` — "2026 SIG Quant Research OA整理【带答案】"
- `/bbs/thread-1143725-1-1.html` — "sig 最新oa" (SWE full-time)
- `/bbs/thread-1089922-1-1.html` — "求海纳国际 SIG qr intern final 面经"
- `/bbs/thread-1157580-1-1.html` — "SIG 求Quant Research and Sys Trading的recruiter call经验"
- `/bbs/thread-1167082-1-1.html` — "SIG 26 OA"
- `/bbs/thread-1009682-1-1.html` — "SIG 2024 OA 附加第一题小思路"
- `/bbs/thread-1023600-4-1.html` — "Sig quant OA"

---

## The decisive artifact

`https://saykind.github.io/files/interviews/quant-SIG-problems.pdf`, by a named author
(David Saykin), post dated 2024-11-29, page 1 header, verbatim:

> David Saykin saykind@itp.ac.ru
> **The Susquehanna Problem Solving Assessment**
> **Duration: 1 hour**
> **Test had 17 questions, but you're not expected to solve all of it.**
> Here I reproduce some of the questions.

Then ten problems, all free-response ("Compute the probability…", "Compute the expected
payoff…"). The blog post explains he was contacted for QUANT RESEARCH: "A quant recruiter
reached out to me on Linkedin asking if I'm interested in internship, I said that I'm currently
looking for full-time positions only… They sent me an email saying that I should complete The
Susquehanna Problem Solving Assessment."

This single source establishes, from a candidate's own hands: the official test NAME, the
duration, the question count, the free-response answer format, and that the test is
over-length by design.

---

## Cross-link proving QT and QR sit the SAME assessment

Saykin's QR **Problem 3** (bakery, 70% croissant / 30% muffin, 2 muffins left, 5 in line)
appears verbatim as question 1 of 1point3acres thread-1086565, whose title is
**"SIG Trader OA"** and whose author writes, verbatim:

> Trader OA 与QR相似，分享一下面经，求大家赏赐大米。感谢！ 1. Assume that in a bakery, each
> customer buys only one item at a time. There is a 70% chance a customer will buy a croissant
> and a 30% chance a customer will buy a muffin. There are only 2 muffins left and 5 people are
> still waiting in line. Compute the probability that these two m…

("Trader OA is similar to QR, sharing my experience.") A trader-track candidate and a
research-track candidate sat the same question. Additionally the 1p3a thread title
**"SIG QT QR Online assessment"** (thread-1166650) names both tracks for one test.

Saykin's **Problem 9** (3 tokens, bold betting to reach 5) and **Problem 10** (frog
A(0,0)→B(5,4), no three consecutive same-direction steps) reappear as **Question 16** and
**Question 17** of 1p3a thread-1144112 "2026 SIG Quant Research OA整理", with the numbers
changed (win probability 3/4 → 2/3; destination B(5,4) → B(5,6)). The numbering to exactly
17 independently corroborates the count. The English mirror `/interview/thread/1144112` is
titled "Comprehensive 2026 SIG Quantitative Research OA with **17** detailed questions".

This is also exactly what the Feb-2026 candidate described (thread-1166650):
> 17题，题型是地里一样的，但是很多数字有改动，有的表述细节稍有变动，而且有的数字改动之后计算量明显增加

---

## What I could NOT establish

1. **The vendor platform, from any candidate account.** Every "Mercer Mettl" / "HackerEarth" /
   "Mercer" attribution I found traces to a prep vendor (jobtestprep, aptitude-test-prep,
   tradermath, quantblueprint, extern). Not one candidate account I retrieved names the platform
   for the *math* OA. (CodeSignal for the *coding* OA IS candidate-attested — see below.)
2. **Whether a calculator is permitted.** Claimed by jobtestprep, aptitude-test-prep and
   tradermath. Zero candidate corroboration. Note the tension: Saykin's reproduced problems are
   heavy symbolic/combinatorial work, not arithmetic, which is consistent with a calculator being
   irrelevant either way.
3. **Negative marking.** Claimed only by quantblueprint. No candidate mentions it anywhere.
   Weak counter-signal: the 1p3a thread title "SIG OA Quant Researcher 14/17 道题。需要至少 100
   分。" implies a *points* total (≥100) rather than a raw count — but the body is paywalled, so
   the scoring model is unknown.
4. **Whether you can navigate back between questions.** aptitude-test-prep says yes;
   programhelp says the opposite ("做完就进入下一题，不能回看" — no going back). Neither is a
   candidate. Indirect candidate evidence favours "yes, you can": the Feb-2026 candidate talks
   about *re-verifying the earlier easy questions* ("如果前面的简单题反复验算会…"), which
   presupposes free navigation, and multiple candidates report not finishing, implying they
   budget time across the whole paper.
5. **Proctoring / webcam for the math OA.** Nothing. For the CodeSignal coding OA there is one
   oblique candidate signal: a 1p3a reply advising "建议做OA时别在同一个浏览器上开LC"
   (don't have LeetCode open in the same browser during the OA), implying tab/focus detection.
6. **A separate sequences test, a separate mental-math test, or a personality/decision
   questionnaire as distinct stages.** No candidate account describes any of these as a separate
   assessment. "Sequences" and "mental math" appear only as *question types inside* the single
   OA. The one non-vendor trace of a personality component is the WSO Aug-2024 Graduate Quant
   Trader submission, which has "Personality Test" ticked in its structured
   "What did the interview consist of?" checkbox list — but the free-text body describes only an
   OA and a phone interview, so the checkbox is uncorroborated by its own author's prose.
7. **The superday/onsite structure for quant traders, in any detail, from a first-person
   account.** This is the biggest gap. Group trading games, market-making games and poker
   rounds are asserted confidently by ~six prep vendors and by SIG's own *culture* marketing,
   but the only candidate-side traces I could retrieve are: (a) a Blind comment on a QR thread,
   "A lot of the interview process includes playing betting games"; (b) WSO 2014-era mentions of
   "4 interviews with actual traders" / "6 or so interviews"; (c) a Glassdoor Aug-2024 NY
   candidate saying only "Multiple technical rounds with traders… 2 behavioral rounds woven in
   between". **No candidate I retrieved describes playing poker or a group market-making game at
   a SIG interview.** Treat any question claiming to be from "the SIG superday poker round" as
   unverified.
8. **Office-by-office differences.** Too thin to map. Dublin, Sydney, NY, Philadelphia and
   Bala Cynwyd accounts all show the same OA→phone→technical→office-interview shape; the
   observed numeric spread (16/17/20ish/27) does not correlate cleanly with office.
9. **Quant Analyst as a distinct track.** SIG posts "Operations Analyst", "Macro Analyst",
   "Equity Analyst" and "Quantitative Strategy Developer", and 1p3a has "SIG Power Analyst
   hr轮挂经", but I found no candidate account of anything branded "Quant Analyst" with a
   distinct assessment. The quantblueprint claim that SIG "hire[s] across Quant Trading, Quant
   Research, Quant Analyst, and Quant Developer" is not reflected in SIG's own posting titles
   I saw.
10. **Whether internship and full-time get different OAs.** tradermath asserts a
    trading-internship/full-time split and then immediately undercuts itself ("we have heard of
    cases where those applying full-time actually receive the Quantitative Evaluation and those
    applying for the internship receive the 60-minute Problem Solving Assessment"). My candidate
    data shows the split is by DATE, not by level — see the drift section in `sig.yaml`.
11. **Reddit.** Despite five differently-phrased attempts, the search engine surfaced no Reddit
    thread content for SIG at all in this run. Zero Reddit evidence is in the map.

---

## Evidence inventory (final)

- 35 searches run (22 English, 13 Chinese), plus 1 direct site search on nowcoder.
- 71 evidence items in `sig.yaml`, every one carrying both a URL and a verbatim quote
  (validated programmatically: zero URL-without-quote entries).
- 9 conflicts recorded; 3 of them resolved in favour of a *vendor* being partly right
  (the 16-in-20 format and the CodeSignal coding OA are real, just mis-scoped), 4 resolved
  in favour of candidate accounts, 1 left explicitly UNRESOLVED (the Dublin 27-question outlier),
  1 resolved as a track split.
- 3 format-drift entries, each with dated before/after candidate accounts.
- 12 vendor claims adjudicated: 6 rejected outright, 6 partly or wholly upheld.

## Distinct first-person accounts underpinning the map

Wall Street Oasis (10): Graduate Quant Trader Philadelphia 2024-08; Trading Systems Engineer
Intern Bala Cynwd 2025-12; Quant Researcher Philadelphia 2025-12; Discovery Day Sydney 2025-06;
internship Dublin 2024-12; Operations Analyst Bala Cynwyd 2025-07; Intern equity research Dublin
2025-10; Trading Dublin 2025-09; Trader Intern New York 2024-09; equity summer analyst Bala
Cynwyd 2025-08; Quant Trader Intern bala cynwyd 2025-09; plus archive slugs Quant Trader Intern
Dublin 2020-09, Quantitative Trader Intern Philadelphia 2024-02, Quantitative Trading Intern Bala
Cynwyd 2014-03, Trader Intern Bala Cynwyd 2014-11, Quantitative research Bala Cynwyd 2014-02.

Glassdoor (9 dated Quantitative Trader entries): 2025-06-30; 2025-03-23 Dublin; 2025-03-12
Dublin; 2024-10-28; 2024-10-09 New York; 2025-01-10; 2024-08-16 New York; 2024-09-27;
2024-03-17 Sydney; 2024-01-31.

Personal blog (1): David Saykin, Quant Research full-time, 2024-11-29, incl. the reproduced
assessment PDF.

Blind (2 threads, ~5 useful comments): 2023-07-24 QR; 2023-08-14 tech incl. 2023-08-21,
2025-06-05 and 2026-05-15 comments.

1point3acres (13 threads + 3 tag-page inventories, snippet-only).

SIG's own postings (3 mirrors of one process boilerplate).
