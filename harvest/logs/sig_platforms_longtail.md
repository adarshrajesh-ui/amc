# SIG — platform / question-bank / long-tail shard — collection log

Firm: **Susquehanna International Group (SIG)**, all quant tracks, internship prioritised.
Output: `/workspace/harvest/raw/sig_platforms_longtail.jsonl`
Log written: 2026-08-01.

**Result: 204 JSONL records.** By `source_type`: `glassdoor` 185, `blog` 11, `github_repo` 6,
`student_doc` 2. Across 183 distinct Glassdoor review URLs plus 8 non-Glassdoor URLs.

---

## 1. Retrievability map (what actually worked from this host)

| Host | Direct `WebFetch` | `r.jina.ai` proxy | Verdict |
|---|---|---|---|
| glassdoor.com | times out / blocked | **200, full markdown** | `full_text` via proxy |
| wallstreetoasis.com | blocked | **200, full markdown** | `full_text` via proxy |
| linkedin.com public post | **200, full post text** | 200 (same text) | `full_text` |
| github.com / raw.githubusercontent.com | **200** | n/a | `full_text` |
| api.github.com code search | 200 (secondary rate limit, needs retry-after backoff) | n/a | usable |
| math.stackexchange.com | **200** | n/a | `full_text` |
| quizlet.com | Cloudflare "One more step…" challenge | Cloudflare CAPTCHA | **blocked** → `snippet_only` |
| youtube.com (page) | JS shell only, 401/403 | JS shell only | **blocked** |
| YouTube transcripts (`youtube-transcript-api`, `youtubetotranscript.com`) | `RequestBlocked` / HTTP 403 | n/a | **blocked** |
| 1point3acres.com | blocked | partial (paywall at 188 points) | `snippet_only` |
| web.archive.org CDX API | 503 / timeout; `wayback/available` 429 | n/a | **unavailable this session** |
| lite.duckduckgo.com | HTTP 202 challenge | n/a | **blocked** |

Notes:
- Glassdoor and WSO were reached **through the `r.jina.ai` text proxy**, not by a plain browser
  fetch. Records from them are marked `retrieval_method: webfetch` / `access: full_text` because
  the full page body was genuinely retrieved, but the proxy hop is disclosed here.
- Quizlet decks are Cloudflare-walled to both fetch paths **and** absent from the Wayback Machine
  (deck 932271215 returned `{"archived_snapshots": {}}`; decks 928572850 and 240587160 returned 404
  on `web.archive.org/web/2025id_/`). Only the single "hero" card each deck exposes to search
  crawlers was obtainable, so only one card per deck is recorded, as `snippet_only`.

---

## 2. Queries run

### Glassdoor (role-filtered, earlier phase of this shard)
Seventeen exact role-title Glassdoor interview pages were paginated through the proxy
(`https://www.glassdoor.com/Interview/<slug>.htm` and `..._IP<n>.htm`), 99 pages total:

```
Susquehanna-International-Group-Assistant-Trader-...-KO32,48            (14 pages)
Susquehanna-International-Group-Quantitative-Researcher-...-KO32,55     (13 pages)
Susquehanna-International-Group-Trader-...-KO32,38                      (11 pages)
Susquehanna-International-Group-Quant-Trader-Intern-...-KO32,51         ( 8 pages)
Susquehanna-International-Group-Trading-Intern-...-KO32,46              ( 8 pages)
Susquehanna-International-Group-Intern-...-KO32,38                      ( 8 pages)
Susquehanna-International-Group-Quantitative-Trader-...-KO32,51         ( 6 pages)
Susquehanna-International-Group-Internship-...-KO32,42                  ( 6 pages)
Susquehanna-International-Group-Junior-Trader-...-KO32,45               ( 4 pages)
Susquehanna-International-Group-Quantitative-Trading-Intern-...-KO32,59 ( 4 pages)
Susquehanna-International-Group-Summer-Intern-...-KO32,45               ( 4 pages)
Susquehanna-International-Group-Quantitative-Analyst-...-KO32,52        ( 3 pages)
Susquehanna-International-Group-Graduate-Quant-Trader-...-KO32,53       ( 2 pages)
Susquehanna-International-Group-Graduate-Trader-...-KO32,47             ( 2 pages)
Susquehanna-International-Group-Quantitative-Research-...-KO32,53       ( 2 pages)
Susquehanna-International-Group-Quant-Researcher-...-KO32,48            ( 2 pages)
Susquehanna-International-Group-Quantitative-Research-Associate-...-KO32,63 ( 2 pages)
```

### WebSearch queries (this phase)
1. `site:leetcode.com/discuss Susquehanna SIG OA interview experience`
2. `geeksforgeeks Susquehanna interview experience SIG`
3. `quizlet Susquehanna SIG quant trading interview flashcards`
4. `"Susquehanna" OA 面经 github 笔试 真题 量化 实习`
5. `quizlet "SIG QT Intern Interview Questions" expected value dice probability`
6. `quizlet 928572850 SIG QT Intern market making spread coin flip`
7. `"SIG Quant Trading" quizlet 932271215 flashcards questions`
8. `site:quizlet.com susquehanna OR SIG trading interview flashcards`
9. `"Susquehanna" interview experience geeksforgeeks campus placement questions`
10. `medium.com SIG Susquehanna quant trading internship online assessment my experience`
11. `1point3acres Susquehanna OA 17 questions frog spinner 题目 回忆`
12. `语雀 yuque.com SIG Susquehanna 面经 量化 OA`
13. `docs.google.com spreadsheet quant trading internship interview questions SIG Susquehanna student club`
14. `substack SIG Susquehanna quant trader interview superday my experience questions asked`
15. `youtube "SIG" OR Susquehanna quant trading internship interview "I got asked" questions video`
16. `"Susquehanna" CodeSignal OR HackerRank online assessment 70 minutes 4 questions discussion thread`
17. `geeksforgeeks.org Susquehanna International Group interview experience internship round`
18. `SIG Susquehanna quant trader intern superday "they asked" probability question blog post 2025`
19. `"Susquehanna" 面经 量化交易 实习 OA 题目 概率 回忆 2025 2026`
20. `linkedin.com/posts Susquehanna SIG online assessment quantitative trader intern questions experience`
21. `leetcode discuss "Susquehanna" OA questions asked interview experience SIG intern`
22. `石墨文档 OR 飞书 OR 语雀 SIG Susquehanna 量化 OA 题目 汇总` (earlier phase)

### GitHub code-search queries (api.github.com/search/code)
23. `Susquehanna 面经` (40 hits)
24. `Susquehanna 笔试`
25. `Susquehanna 真题`
26. `Susquehanna 面试 概率`
27. `Susquehanna OA 题`
28. `Susquehanna 实习 量化`
29. `Susquehanna interview questions probability`
30. `Susquehanna online assessment`
31. `Susquehanna quant trader intern interview`
32. `Susquehanna 期望 硬币`
33. `"SIG" 笔试 量化` — 2,028 hits, **discarded as unusable**: the token `SIG` matches
    `intsig`, `腾讯 CSIG`, `SIGIR`, BERT `vocab.txt` files, kerning-pair corpora etc.
    Lesson recorded: for GitHub code search only `Susquehanna` is a usable discriminator.

174 unique files surfaced across those searches; 19 plausible ones were fetched raw and grepped
for `Susquehanna|SIG|Susq`. Only one was substantive (see §4).

### Other API probes
34. GitHub tree listing `Leader-board/OA-and-Interviews` (`/git/trees/main?recursive=1`) — 135 paths,
    exactly **one** SIG directory (`Application experiences/2021-22/SIG/`), already harvested.
35. GitHub tree listing `ldvyyc/InterviewPrep` — 28 docs, one SIG-specific (`game_theory_sig.html`).
36. LeetCode GraphQL `categoryTopicList(keywords:...)` → HTTP 400, `Unknown argument "keywords"`.
    LeetCode's discuss search schema has changed; no working unauthenticated search path found.
37. Quizlet internal `webapi/3.4/studiable-item-documents?filters[studiableContainerId]=928572850`
    → HTTP 403 Captcha Challenge.
38. `youtube-transcript-api` on `d3jtd0jDU7o`, `VmvSlVS6mNk` → `RequestBlocked` (IP-level).

---

## 3. URLs opened

**Yielded records (8 new this phase, on top of the Glassdoor corpus):**
- `https://www.linkedin.com/posts/ameybhangire_susquehanna-codingassessments-techinterviews-activity-7376188983250186240-aFhF` — 4 records
- `https://www.glassdoor.com/Interview/Susquehanna-International-Group-Interview-RVW85406907.htm` — 1 record
- `https://quizlet.com/928572850/sig-qt-intern-interview-questions-flash-cards/` — 1 record
- `https://quizlet.com/240587160/sig-interview-flash-cards/` — 1 record
- `https://github.com/ldvyyc/InterviewPrep/blob/main/public/docs/game_theory_sig.html` — 1 record

**Already-harvested sources carried in the file from the earlier phase:**
- `https://github.com/Leader-board/OA-and-Interviews/blob/main/Application%20experiences/2021-22/SIG/Quantitative%20Trader%20-%202022%20Programme.md` (+ `media/sig1-7.png` scorecard screenshots)
- `https://www.wallstreetoasis.com/company/susquehanna-international-group/interview/graduate-quant-trader`
- `https://www.wallstreetoasis.com/company/susquehanna-international-group/interview/trading-systems-engineer-intern`
- `https://www.1point3acres.com/bbs/thread-1146142-1-1.html`
- 183 distinct `glassdoor.com/Interview/...RVW*.htm` review URLs

**Opened, produced nothing usable:**
- `https://math.stackexchange.com/questions/4960759/...` — full text retrieved. Contains the SIG OA
  frog problem almost verbatim (asked 2024-08-20, endpoint (5,6) vs the 1point3acres recall's (5,4)),
  **but the asker never mentions SIG**, so it is not an attestation. Not recorded. Noted here only
  as circumstantial support for the existing 1point3acres frog record.
- `https://www.wallstreetoasis.com/company/susquehanna-international-group/interview` (index, 258 entries)
- `https://api.github.com/...` file fetches for: `Messiahhh/blog`, `Airtnp/Notes`,
  `lingduoduo/Leetcode`, `vermavarun/hft`, `pb0316/thuhole_memories`, `bzsgbq/logseq-publish`,
  `ESwordCn/Intern_0ffers`, `cybergeekgyan/Quant-Developers-Resources`, `garymmmjw/QuantGym`,
  `HuskyBin/Need-To-Do`, `quant-bobby/quant-jobs`, `hxh5/nowcoder` (5 daily digests),
  `MasterAgentAI/QuantPath`, `LLMQuant/quant-wiki`. Every `SIG` hit in these was either
  Tencent **CSIG**, a firm-name list entry, or an alias array — **no question content**.

---

## 4. Rejected sources and why

**Hard-excluded prep-vendor / content-farm pages** (treated as negative evidence; none recorded):
`techinterview.org`, `quantblueprint.com`, `tradermath.org`, `theinterviewden.com`,
`interviewquery.com`, `everythingquant.com`, `prepfully`, plus these additional ones encountered
that behave identically: `quantt.co.uk`, `dataford.io`, `interviewsense.org`, `interviewchamp.ai`,
`extern.com`, `aptitude-test-prep.com`, `linkjob.ai`, `prachub.com`, `gauthmath.com`.

**`programhelp` network — rejected across five domains.** The same operator publishes SIG "面经"
under multiple identities, each ending in a pitch for paid real-time interview assistance:
- `https://jishuzhan.net/article/2054023766773600257` (byline `programhelp_`; also returned
  HTTP 404 behind the proxy)
- `https://dev.to/programhelp-cs/sig-2026-quant-susquehanna-oa-full-guide-5ea`
- `https://dev.to/net_programhelp_e160eef28/sig-susquehanna-international-group-interview-experience-24jk`
- `https://dev.to/net_programhelp_e160eef28/sig-2026-oa-review-susquehanna-coding-assessment-breakdown-key-patterns-3k8o`
- `https://programhelp.net/vo/sig-quant-interview-guide/` and `/en/vo/sig-quant-interview-guide/`
- `https://gitcode.csdn.net/69cf72a354b52172bc66b081.html` (byline `programhelp_`)

This matters because the dev.to "full guide" carries a ~20-item list of specific probability
problems (obtuse triangle on a unit circle, Penney's Game HHT vs HTH, bus-waiting U(0,10)/U(0,20),
blue-ball urn, painted-cube slicing, eight-at-a-round-table adjacency, chord length on a unit
circle…). It is the single richest-looking "SIG question list" on the open web and it is
**entirely unusable** — it is an advertisement, it cites no candidate, no date and no round, and
its own sibling pages contradict each other on the OA format. Recorded here explicitly so a later
pass does not re-find it and mistake it for a source.

**`https://www.youtube.com/watch?v=Rc1NcUdOti4` — "2024 SIG Quant Trading Interview!"** — rejected.
The description timestamps do expose two concrete questions ("In a 3-set tennis game, would you bet
on it finishing in 2 sets or 3 sets?" at 08:47; "Two players are at deuce … player 1 has a 60%
chance of winning the point … what are the odds of player 1 winning?" at 13:49), but the channel is
**Quant Blueprint**, an explicitly excluded prep vendor, and the video is their own mock interview,
not a candidate's recall of an SIG round.

**`ldvyyc/InterviewPrep` — included, but with the heaviest doubt in the file.** One item only. The
document is a self-authored cheat sheet whose worked examples are all textbook games, and it
contains a visible LLM self-correction left in the published text (`p = 4/3 ?? … Wait: 让 B 无差异
需要调整 A 的混合`). Only the single item the document itself frames as `SIG 面试口头题` (an SIG
spoken interview question) was taken; every `SIG★` elsewhere in the doc is a topic tag, not a
question, and none of it was recorded.

**Not recorded because another shard already holds it:** the Nowcoder post by 牛客414065333号
(2024-05-25, 英雄游戏_开发, "SIG OA": divisible-by-k subset counting; matrix flood-fill/islands
variant). Verified present in `sig_nowcoder_yingjiesheng.jsonl` and `sig_chinese_social.jsonl`.

---

## 5. What I could not establish

- **LeetCode Discuss company tag for SIG/Susquehanna — zero results.** `site:` search returned only
  Optiver / Squarepoint / Goldman threads, and the GraphQL discuss-search endpoint has changed
  shape (HTTP 400). I cannot say whether SIG threads exist there and are unindexed, or whether the
  company tag is genuinely empty. **This is the largest uncovered source in my shard.**
- **GeeksforGeeks — no SIG interview-experience article found.** Repeated site-scoped queries
  returned only vendor guides. GfG's SIG coverage appears not to exist rather than to be blocked.
- **Quizlet decks 928572850 (85 terms) and 240587160 (12 terms): 95 of 97 cards unread.** Deck
  932271215 ("SIG Quant Trading/ Sell Side Research", 13 terms) yielded no card text at all — only
  its title and term count are established. All three are Cloudflare-walled and unarchived.
- **YouTube / TikTok candidate narrations: nothing established.** Transcripts blocked at IP level
  by three independent routes. The only SIG assessment video surfaced was the excluded vendor mock.
- **Public Google Docs / Sheets from student quant clubs: none found.** No `docs.google.com` result
  surfaced for any SIG-scoped query.
- **语雀 / 石墨文档 / 飞书 public compilation docs: none found.** Every Chinese-language query routed
  back to the `programhelp` network, 1point3acres, or Nowcoder mirrors.
- **Medium / Substack: no genuine first-person SIG post found.** The nearest genuine hit was on
  LinkedIn instead, which is why LinkedIn was mined despite not being on the shard's source list.
- **1point3acres thread 1146142 is only ~15% readable.** The visible fragment establishes
  "Overview: 60min, 17questions / Difficulty in increasing order", Q17 (frog) and Q12 (spinner);
  Q1–Q11 and Q13–Q16 sit behind a 188-point paywall. The reply "楼主你好，求分享Susquehanna OA
  的其他几个题目啊" confirms further questions were posted and are unread.
- **Exact post date of the LinkedIn OA post is inferred, not stated.** LinkedIn renders "10mo";
  the attached media asset's epoch (`1758620494638`) gives 2025-09-23, which is what I used.

---

## 6. Consistency-prior reconciliation

The prior (17 questions / 60 minutes) is **directly corroborated** by sources in this shard:
- WSO Graduate Quant Trader, Philadelphia, Aug 2024: *"standard online assessment, 17 questions in
  1 hour, probability, basic calculus"*
- 1point3acres thread 1146142: *"Overview: 60min, 17questions"*
- Glassdoor QT: *"Online probability assessment with 17 questions to be completed in an hour. The
  topics covered are bayes rule, logic, and markov chains"* and *"Online assessment with 17
  questions for an hour. Topics are mostly math, logic, probability, and a bit of calculus"*

The separate **70-minute / 4-question CodeSignal developer OA** is now corroborated by a named,
non-anonymous first-person source for the first time in this shard (the LinkedIn post), which is
independent of the vendor pages that also assert it.

A **third, shorter test** is attested by genuine dated sources and is not the same as either:
`Leader-board/OA-and-Interviews` (Dublin, Sep 2021) reports *"14 questions … only 20 minutes in
total"*, and Glassdoor (Sydney, Feb 2024) reports *"16 problems in 20 minutes"*. These do not
contradict the 17-in-60 prior so much as indicate SIG runs at least two quant screens — a short
"Quantitative Evaluation" and a longer "Problem Solving Assessment". That reconciliation is my
inference; no single retrieved source states it, and each affected record carries it in `doubt`.
