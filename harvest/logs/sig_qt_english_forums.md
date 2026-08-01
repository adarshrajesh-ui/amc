# Harvest log — SIG / Susquehanna, quant-trader track, English-language forums

Output: `/workspace/harvest/raw/sig_qt_english_forums.jsonl` — **96 records**
Run date: 2026-08-01 (UTC)
Shard scope: Reddit, Wall Street Oasis, Blind/teamblind, QuantNet, Elite Trader, Hacker News.

Record distribution:

| Dimension | Breakdown |
|---|---|
| Round | online_assessment 46 · phone_technical 39 · onsite 5 · unknown 3 · math_sequences_test 2 · take_home 1 |
| Level | internship 45 · unknown 36 · new_grad 13 · experienced 2 |
| Source | reddit_thread 72 · wso 14 · trade2win 4 · quantnet 3 · elitetrader 3 |
| Question type | probability 33 · other 29 · expected_value 11 · behavioral 6 · logic_brainteaser 5 · combinatorics 4 · mental_math_speed 3 · options_theory 2 · poker_game_theory 2 · market_making 1 |
| Office | unknown 66 · Dublin 10 · Philadelphia 7 · Bala Cynwyd 3 · New York 3 · North America 3 · Australia 2 · Sydney 1 · Europe 1 |
| Post year | 2004:2 2006:4 2008:2 2009:1 2017:1 2018:4 2019:2 2020:3 2021:1 2022:9 2023:10 2024:9 2025:17 **2026:31** |

---

## 1. Method

Three retrieval channels.

1. **WebSearch** — 33 distinct queries (§2). Its "Highlights" blocks carry verbatim page text
   including from Cloudflare-blocked hosts. For this particular firm the channel proved close to
   worthless: see §4, "search-engine saturation".
2. **WebFetch** on hosts that permit it — wallstreetoasis.com, quantnet.com, elitetrader.com,
   trade2win.com and (intermittently) teamblind.com.
3. **Arctic Shift Reddit archive API** (`arctic-shift.photon-reddit.com`). reddit.com is
   Cloudflare-blocked for WebFetch, but this archive mirror serves full post and comment bodies
   over JSON.

Final crawl scale: **1,723 posts + 353 megathread posts, 842 comment trees, 13,505 comments**
cached under `raw/_reddit_cache/`. That is roughly a 5× expansion over the mid-run state.

Tooling: `tools/as_crawl.py`, `as_crawl2.py` (post search), `as_comments.py`, `as_comments3.py`
(comment trees), `as_mega2.py` (megathread trees), `as_bodysearch.py` (abandoned, see §4),
`dump.py`, `scan.py`…`scan5.py` (progressively tighter extraction sweeps), `emit.py` (emitter).

### Quote fidelity

`emit.py` does not accept a hand-typed quote. Every Reddit record's `source_quote` is produced by
slicing the cached body between two anchors, and the emitter **exits with an error** if an anchor
is not found, so a Reddit quote cannot drift from source. Independent post-run verification:

- **72 / 72 Reddit quotes** re-checked against the local archive cache — all exact, 0 mismatches.
- **24 / 24 non-Reddit quotes** (WSO, QuantNet, Elite Trader, Trade2Win) re-fetched live through
  the `r.jina.ai` text proxy and matched after Unicode/whitespace normalisation — all 24 found,
  0 misses.

All 96 records were also schema-validated: every mandatory field present, and `doubt`,
`question_text` and `source_quote` non-empty on every line.

---

## 2. Every search query run

### WebSearch (33)

Queries 1–26 were run in the first half of the session; 27–33 in the second.

| # | Query | Yield |
|---|---|---|
| 1 | `site:wallstreetoasis.com Susquehanna SIG trading internship interview questions asked` | **Yes** — WSO company interview index + Graduate Quant Trader review |
| 2 | `"SIG" OR "Susquehanna" online assessment "frog" problem question lily pads reddit` | **Yes** — Saykin blog + 1point3acres frog corroboration (both out of shard, §5) |
| 3 | `site:teamblind.com Susquehanna SIG quant trader interview question` | No usable question |
| 4 | `site:quantnet.com Susquehanna SIG interview trading question asked me` | **Yes** — QuantNet thread 2065 |
| 5 | `wallstreetoasis.com Susquehanna "frog" "three steps in the same direction" grid paths interview` | Partial — frog text found only on non-shard hosts |
| 6 | `reddit SIG Susquehanna superday final round trading game market making game intern experience` | No — all vendor pages |
| 7 | `"SIG" Susquehanna quant trading internship OA 2026 questions "expected number" OR "probability that" reddit r/quant` | No — all vendor pages |
| 8 | `site:wallstreetoasis.com SIG Susquehanna "asked me" OR "they asked" probability question trading interview forum` | No SIG-specific question |
| 9 | `reddit r/quant Susquehanna SIG first round phone interview probability question they asked dice coin` | No — vendor pages |
| 10 | `SIG Susquehanna Dublin trading internship interview questions reddit r/ireland r/DevelEire experience` | No |
| 11 | `elitetrader.com Susquehanna SIG trading interview questions asked probability` | No results on this phrasing (later superseded — see #27) |
| 12 | `news.ycombinator.com Susquehanna SIG interview question trading quant asked` | No |
| 13 | `reddit "SIG" Susquehanna assistant trader intern OA "17 questions" what were the questions 2025` | Partial — 17-in-60 corroboration via Glassdoor (other shard) |
| 14 | `"wallstreetoasis.com/company/susquehanna-international-group/interview/" trading intern assistant trader quantitative` | No new slugs |
| 15 | `reddit SIG Susquehanna "quant trading" internship OA "spinner" OR "widgets" OR "cookies" OR "snickerdoodle" question` | No Reddit hit at the time — but see §6, the snickerdoodle question was later found *inside the Reddit archive*, not via search |
| 16 | `wallstreetoasis Susquehanna SIG trading internship superday Bala Cynwyd "what I remember" questions poker game round` | No |
| 17 | `wallstreetoasis forum SIG Susquehanna trading interview "first round" questions I got asked probability expected value thread` | No |
| 18 | `teamblind Susquehanna SIG OA online assessment quant trader 17 questions experience post` | No |
| 19 | `reddit r/csMajors OR r/cscareerquestions SIG Susquehanna quant trader OA "mettl" logic test questions what was on it` | No |
| 20 | `"SIG" Susquehanna trading intern interview reddit "make a market" OR "quote me a market" question round` | No first-person account |
| 21 | `reddit SIG Susquehanna Sydney Hong Kong trading intern discovery day interview questions asked` | No |
| 22 | `"SIG" OR "Susquehanna" reddit removed deleted post "OA questions" quant trading archive unddit reveddit` | No — Unddit/Reveddit defunct |
| 23 | `wallstreetoasis.com forum "susquehanna" trading interview brainteaser "they asked me" OR "I was asked" 2024 2025 thread trading` | No |
| 24 | `reddit r/quant "SIG" superday final round trading intern "poker" round experience what happened` | No first-person account |
| 25 | `"SIG" interview "25 horses" OR "horses 5 lanes" quant trader intern wallstreetoasis Susquehanna` | Deliberate negative check — see §6 |
| 26 | `reddit "just did the SIG" OR "took the SIG OA" quant trading questions remember one was about` | No |
| 27 | `reddit SIG Susquehanna superday trading game interview what questions` | No — 5/5 results were vendor pages (theinterviewden, quantt.co.uk, interviewchamp.ai, programhelp via DEV.to, tradermath) |
| 28 | `site:reddit.com SIG online assessment "17 questions" OR "one hour" quant trading` | **Zero results returned** |
| 29 | `reddit r/quant "SIG" OA "the question" probability intern 2025` | No — 5/5 vendor pages (everythingquant, programhelp, jobtestprep, quantblueprint, oavoservice) |
| 30 | `site:teamblind.com Susquehanna SIG quant trader interview` | No question content; 5 Blind posts identified, all comp/SWE/advice |
| 31 | `site:quantnet.com susquehanna SIG interview questions asked` | **Yes** — surfaced QuantNet thread 61588, the one new QuantNet record |
| 32 | `wallstreetoasis susquehanna SIG trading intern superday "they asked" probability question` | No — 5/5 vendor pages |
| 33 | `"SIG" OR "Susquehanna" trading intern interview "they asked me" dice OR coins OR cards reddit 2025` | No — 5/5 vendor pages |

### Hacker News Algolia API (3 queries, direct)

`hn.algolia.com/api/v1/search?query=…` for `Susquehanna interview` (3 hits),
`SIG trading interview` (2 hits), `Susquehanna trader` (13 hits).
The only interview-adjacent hit is comment `14652684` on "Take Naps at Work": a user mentions a
Susquehanna phone interview and a "day in the life" sheet, but reports **no question**. Everything
else is HFT news commentary or a 2018 "Who is hiring?" job ad. **Hacker News: confirmed zero.**

### Arctic Shift archive queries

- **`posts/search`** across `r/quant`, `r/quantfinance`, `r/FinancialCareers`,
  `r/cscareerquestions`, `r/csMajors`, `r/algotrading`, `r/poker`, `r/options`, `r/statistics`,
  `r/AskStatistics`, `r/askmath`, `r/probabilitytheory`, `r/learnmath`, `r/HomeworkHelp`,
  `r/puzzles`, `r/riddles`, `r/brainteasers`, `r/ireland`, `r/AusFinance`, `r/UKJobs`, and ~30
  university subreddits (`r/uwaterloo`, `r/berkeley`, `r/UIUC`, `r/nyu`, `r/cmu`, `r/UPenn`,
  `r/mit`, `r/Cornell`, `r/columbia`, `r/gatech`, `r/unimelb`, `r/UNSW`, `r/unsw`, `r/UBC`,
  `r/Purdue`, `r/trinitycollegedublin`, `r/ucd`, `r/imperialcollege`, `r/cambridge_uni`,
  `r/Oxforduni`, `r/UTAustin` …) × terms {SIG, SIG OA, SIG assessment, SIG discovery,
  SIG final round, SIG intern, SIG interview, SIG market making, SIG phone, SIG quant,
  SIG superday, SIG trading, SIG trading game, Susquehanna, Susquehanna OA, Susquehanna intern,
  Susquehanna interview}. **This pass completed**, unlike at mid-run.
- **`comments/search?link_id=…`** against 739 threads, prioritised by a title-relevance score.
  494 of them are SIG-titled.
- **Megathread pass** (`as_mega2.py`): r/quant's "Weekly Megathread: Education, Early Career and
  Hiring/Interview Advice" series plus r/FinancialCareers and r/csMajors equivalents — 353
  megathread posts identified, ~90 comment trees pulled. Rationale: r/quant moderators funnel all
  "what's on the OA" traffic into these, so SIG recalls sit in threads whose titles never say SIG.
  **Yield was poor** — 28 SIG-mentioning comments, almost all requests for help rather than
  recalls. It produced exactly one record (`mm9kfjd`).

---

## 3. Every URL opened

### Fetched in full (WebFetch / curl, `access: full_text`)

| URL | Yield |
|---|---|
| `wallstreetoasis.com/company/susquehanna-international-group/interview` | **Yes** — 10 dated candidate reviews. 10 records. |
| `wallstreetoasis.com/company/susquehanna-international-group/interview?page=1` | No — pagination changes summary rows only, not the write-ups |
| `wallstreetoasis.com/company/susquehanna-international-group/interview/graduate-quant-trader` | **Yes** — Aug 2024 Philadelphia: "17 questions in 1 hour". 4 records. |
| `wallstreetoasis.com/forum/trading/susquehanna-trading` | No — comp/exits only |
| `wallstreetoasis.com/forum/prop-trading/susquehanna-sig-superday-trading-game` | **Fetch timed out** (twice). Not recovered. |
| `quantnet.com/threads/sig-phone-interview.2065/` | **Yes** — 2 records |
| `quantnet.com/threads/received-code-signal-test-after-sig-oa.61588/` | **Yes** — 1 record (2025 Graduate Quant Researcher/Trader; OA → 70-min CodeSignal). No replies. |
| `elitetrader.com/et/threads/phone-interview-with-sig.67976/` | **Yes** — 2 records (2006 deck-of-cards three-of-a-kind question) |
| `elitetrader.com/et/threads/susquehanna-interview.169258/` | **Yes** — 1 record (2009 poker-probability recollection) |
| `trade2win.com/threads/susquehanna.8145/` | **Yes** — 4 records (2004–2006 Assistant Trader route, incl. Dublin) |
| `teamblind.com/post/Prepare-for-Quant-roles-in-Jane-Street-Citadel-SIG-etc-mtrs838e` | No — generic advice, comments partly gated behind "Sign up to see all comments" |
| `teamblind.com/search/Susquehanna%20trader%20interview` | **Fetch timed out** |
| `hn.algolia.com/api/v1/search` × 3 | No question content |

### Read via WebSearch full-page-text dumps (not cited)

`quantnet.com/threads/susquehanna-international-group-internship.4501/`,
`quantnet.com/threads/study-programme-for-quant-researcher-interviews.50152/`,
`quantnet.com/threads/jane-street-interview-questions.3039/`,
`teamblind.com/post/quant-interview-prep-a6dxbmua`, `thenewcritic.com/p/pdoom`,
`quantt.co.uk/resources/sig-interview` (×3), `prachub.com/companies/sig-susquehanna/…` (×2).
None contains a first-person SIG QT question recall. The last two are vendors (§5).

### Reddit threads read in full from the archive

First half: `tzyuhp` (GDPR), `poq8uc`, `1e0fczr`, `1gr8l9m`, `1m8p4gg`, `1kxxac7`, `16hsy28`,
`1mm84w6`, `1hyfzor`, `1p6ik4b`, `1tqn589`, `1gi1o24`, `9f2i7v`, `issavu`, `9sd7h0`, `jpwdzb`,
`7kua8t`, `eox8vy`, `9ceux2`, `1ccz2u1`, `w389cc`, `1asgplz`, `1t40fjo`, `swwui9`, `165049h`,
`icqo2t`, `18in839`, `x49u2i`, `wk0tt9`, `xqqien`, `wt18ql`, `wqouyq`, `15qno7e`, `jkrecb`.

Second half (all r/quantfinance 2026 unless noted) — **this is where the yield was**:
`1u4b26p` (SIG OA to PI Timeline — snickerdoodle), `1tx1a6o` (Sig assessment / Mettl 2027),
`1tqnaos` (SIG OA), `1tx1bvf` (SIG Phone Interview), `1uahwew` (SIG Second Round QT),
`1uzb09f` (SIG Codesignal OA), `1v5cal7` (Sig quant trading 2027 summer intern OA),
`1v57y8l` (SIG Quantitative Research Assessment), `1v5qhx3` (SIG QT OA post recruiter call),
`1v6fyh8` (sig qt '27 final round), `1v7yqyo` (Susquehanna Trading Intern OA),
`1u3y6ej` (SIG OA QT Intern 2027), `1u6kw40` (Math PhD — trapezium), `1q8osml` (Susquehanna
Phone Interview Tips), `1tlezc9` (Sig 2027 Intern US OA), `1v28pnv` (SIG Interview Question —
rejected, §5), `1v39kqd` (Mettl 10-day window), `1amigp4` (r/FinancialCareers, Hedge Funds OA
Summaries), `e9z85g` + `e9qmtp` (r/FinancialCareers 2019, SIG intern onsite),
`1n1583k` (r/csMajors, SWE — out of role track), `1jtedsn` (r/quant megathread),
`1mu093d` (r/quantfinance 2025-08, "First phone call with SIG. What to expect?" — 3 records),
`9qv6eq` (r/poker 2018, SIG poker tournament — read, not cited, see §5).

---

## 4. Blocked, dead, or empty sources

- **reddit.com — Cloudflare-blocked for WebFetch.** Worked around entirely via Arctic Shift. All
  Reddit records carry a `retrieval_note` naming the archive endpoint. No page was fetched from
  reddit.com itself.
- **Search-engine saturation is the defining obstacle for this firm.** Of the seven WebSearch
  queries run in the second half, **five returned 5/5 prep-vendor results and one returned zero
  results.** Queries phrased to find candidate recalls ("they asked me", "17 questions") return
  `tradermath.org`, `quantblueprint.com`, `programhelp.net`, `everythingquant.com`,
  `jobtestprep.co.uk`, `prachub.com`, `quantt.co.uk`, `interviewchamp.ai`, `oavoservice.com` and
  `theinterviewden.com` — and essentially nothing else. **WebSearch was not the primary yielding
  channel for this shard; the Reddit archive crawl was.** Every one of the 31 records dated 2026
  came from crawling, not from search.
- **Arctic Shift comment full-text (`body=`) search is unusable at scale.** `as_bodysearch.py`
  attempted `comments/search?subreddit=…&body=Susquehanna` to reach SIG mentions inside
  generic-titled threads. Every request to a large subreddit returned `Timeout. Maybe slow down a
  bit`, even at a 9-second inter-request gap with 7 retries and escalating backoff. The crawler
  was abandoned. The megathread crawl (§2) was the fallback, and it under-delivered. **This means
  SIG recalls sitting inside threads whose titles do not mention SIG remain largely unreachable**
  — a structural blind spot, not a laziness gap.
- **glassdoor.com, 1point3acres.com — Cloudflare-blocked**, and both belong to other shards
  (`sig_platforms_longtail.jsonl`, `sig_1point3acres.jsonl`). Not harvested here.
- **Blind / teamblind.com — fetchable but substantively empty. Confirmed twice.** A second pass
  this session searched Blind and fetched a post in full. Blind's SIG traffic is compensation
  discussion, SWE hiring-bar chat, and one user advertising a paid question bank. Its comment
  threads are additionally gated ("Sign up for free to see all comments"). Two of three Blind
  fetch attempts timed out. **Zero Blind records — a genuine null result for the QT track.**
- **Hacker News — confirmed zero** via the Algolia API rather than by search phrasing alone (§2).
- **Elite Trader — thin but non-zero.** Query 11's phrasing found nothing; direct thread fetches
  found two SIG threads, both from 2006–2009. **3 records.** Elite Trader's SIG discussion is
  retail-trader-era and predates the modern campus pipeline entirely.
- **WSO detailed reviews beyond the first 10.** The company page advertises 258 entries across 26
  pages; only 10 full write-ups are exposed, the rest behind "Add your data to unlock".
  `curl` with a browser UA hits the Cloudflare interstitial. **~248 WSO reviews unreachable.**
- **WSO forum threads render reply counts but not reply bodies** under WebFetch (JS-gated), so
  WSO's forum side is effectively closed even where the company-review side is open.
- **Unddit / Reveddit** — defunct since Reddit's API changes; deleted bodies unrecoverable.
  `[removed]`/`[deleted]` stubs were seen in `1m8p4gg`, `1kxxac7`, `icqo2t` (whose OP body is
  gone), `1v28pnv` and `1tx1a6o`.
- **Image-only evidence, unreadable.** u/ThatsNoiceDude posted a screenshot of SIG's own sample
  questions at `preview.redd.it/kk8xgh0b9lug1.jpeg` (thread `1m8p4gg`). Separately, the OP of
  `1v28pnv` ("SIG Interview Question") posted a **body-less** thread — the question itself was in
  an image or a link, and the archived `selftext` is the empty string. In both cases the question
  text was never in any text I retrieved.

---

## 5. Sources deliberately NOT cited

### Prep vendors and content farms (treated as negative evidence)

Excluded on sight: `tradermath.org`, `quantblueprint.com`, `tradinginterview.com`,
`theinterviewden.com`, `techinterview.org`, `everythingquant.com`, `programhelp.net` (and its
DEV.to mirror `dev.to/net_programhelp_e160eef28`), `prachub.com`, `interviewsense.org`,
`interviewchamp.ai`, `dataford.io`, `quantt.co.uk`, `jobtestprep.co.uk`, `oavoservice.com`,
`aptitude-test-prep.com`, `quantquestions.com`, `extern.com`, `linkjob.ai`, `studyx.ai`,
`interviews.chat`, `quantgrind`, `beyz`, `lifegood4u.org`, `financeandquantsociety.org`.

**Vendor bots operating inside the forums themselves** — the more dangerous case, because the
content arrives wearing a candidate's voice. `scan5.py` filters these by regex. Identified:

- **u/akornato** (links `interviews.chat`) posts long, fluent, confident "here is what SIG's
  round X is like" answers across at least six 2026 SIG threads (`1uatsal`, `1uahwew`, `1u3y6ej`,
  `1uzb09f`, `1v5qhx3`, `1v6fyh8`, `1u4b26p`). The prose is plausible and entirely unsourced.
  **All excluded.** Anyone mining r/quantfinance for SIG content will hit these first.
- **u/QuantGrindApp** (self-identified founder of a prep site), **u/nian2326076** and **u/Leo_0**
  (`prachub.com`, UTM-tagged), **u/Haunting_Month_4971** (Beyz), **u/Poszukwiany**
  (`lifegood4u.org`). All excluded.
- **u/ShlomikSilbiger** (`aptitude-test-prep.com`) — a 2024-05-01 comment in `poq8uc` that reads
  like a debrief and contains two fully-worked problems (an Alice/Bob card-betting problem and
  "You roll 4 dice. What is the probability that at least three dice show the same number?").
  It is an advertisement. **Both questions rejected.**
- **u/Nero-Tulip** (`tradermath.org`) — *is* cited, three times, because his content is oddly
  specific and unglamorous and his 16-in-20 format is independently corroborated. Every one of
  those three records carries the promotion caveat in its `doubt` field.

### Rejected: r/quantfinance `1v28pnv`, "SIG Interview Question" (2026-07-21)

Worth recording explicitly because it looks like the best find in the shard and is not one. The
thread is titled "SIG Interview Question", drew 15 substantive replies working the problem
(bid `b` for a company of uniform value `v`, payout `1.5v`), and would have made a strong record.
It was rejected for two independent reasons:

1. **The OP names a question bank as the source.** His own first comment reads: "Here's the
   source of the question too: `quantnet.com/threads/quantitative-interview-questions-and-answers.437/`",
   alongside a plug for `financeandquantsociety.org`. Attestation is a compiled bank, not a
   candidate recall — squarely inside the brief's hard exclusion.
2. **The question text was never in any retrieved text.** The archived `selftext` is empty; the
   prompt was in an image or link. Every version of the problem I can see is a *commenter's
   paraphrase* while solving it. Writing a `question_text` here would mean reconstructing a
   question I never read, which Rule One forbids outright.

A commenter (u/Technical_Laugh_9040) also identifies it as "the jane street painting question".

### Read but not admissible: r/poker `9qv6eq` (2018), SIG's poker programme

The thread "TIL that SIG … holds an annual poker tournament and has used poker as a recruiting
tool" contains the only first-person account anywhere in this run of SIG's poker practice, from
u/skeeter_tp: "I'm currently in their training program to become a trader. We play several hours
a week as part of the program. Currently we play exclusively 7 card stud … Jerrod Ankenman (WSOP
bracket holder and author of 'The Mathematics of Poker') oversees the poker side of education."

**Not cited**, because this is post-offer *training*, not an assessment or interview round, and
the brief admits only questions from a real assessment. It is logged because it is frequently
mistaken online for evidence about the interview: vendor pages cite SIG's poker culture as proof
of a "poker round" in the interview loop, and this thread shows the culture is real while saying
nothing whatsoever about what candidates are asked.

### Out-of-shard sources found but left for other harvesters

- **`saykind.github.io/interviews/quant-SIG/` — David Saykin, personal blog.** Still the single
  richest SIG source encountered anywhere in this run. He took the Problem Solving Assessment
  (1 hour, 17 questions) and reproduces **ten** problems verbatim. Extraction saved at
  `logs/sig_problem_solving_assessment_saykin_extract.txt`. It is a blog, not a forum, and
  `source_type` has no admissible value for it. **Should be picked up by the blogs/long-tail
  shard.**
- `github.com/Leader-board/OA-and-Interviews` — already in `sig_platforms_longtail.jsonl`; the
  Reddit originals by the same author are cited here.
- 1point3acres thread 1146142 and the Glassdoor QT pages — other shards.

### In-scope but wrong role track (excluded to avoid mislabelling)

`role_track` is fixed to `quant_trader`, so these were dropped rather than mislabelled. All are
real, dated, and worth capturing under their own track:

- **r/FinancialCareers `1mm84w6`**, u/Correct_Bat7679, 2025-11-18 — a detailed three-section
  recall of the **Macro / Equity / Credit Analysis** OA (25 minutes): "fair price calculation,
  implied probability of approval calculation, basic probability using a table, dice roll
  probability, expected sum, stock price calculation" and "cash flow from operations, incremental
  EBITDA margin calculation, factors of option valuation, Sum-Of-The-Parts model, impact of
  tariff". Tempting — the first section is quantitative — but the OP states plainly that he
  applied to Macro/Equity/Credit Analysis, so it is a different paper.
- **r/FinancialCareers `1gi1o24`** — SIG **Capital Markets** OA: "25 minute assessment.
  15 questions on Probability, rest on Finance (EV, EBIT & Equity)".
- **r/FinancialCareers `w389cc`** — SIG **Equity Research**: "Bayesian statistics and the
  technicals of certain securities".
- **r/csMajors `1n1583k`**, 2025-08-27 — a full four-round **SWE** process write-up including a
  90-minute code-optimisation round. Genuinely useful, wrong track.
- **r/quantfinance `1u5eeu5`, `1uzb09f` (partly), r/quant `1v1d0xr`** — Quantitative Strategy
  Developer / QSD threads.
- **WSO** entries for Trading Systems Engineer Intern, Quant Researcher, Operations Analyst,
  Equity Research.

---

## 6. Consistency checks performed

- **17 questions in 60 minutes is now the best-established fact in the shard,** confirmed by
  **eight** mutually independent in-shard witnesses spanning 2024–2026: u/stefano31214 (2024-09,
  QT internship OA), u/Dramatic-Rub-9185 (2024-08), u/Michael_900222 (2026-04, FT), the WSO
  Graduate Quant Trader review (Philadelphia, Aug 2024), and — new this session —
  u/slicethatmango ("60 minutes 17 questions", QT NA 2027), u/DINOBOIZ69 ("maybe 15/17"),
  u/TheClashofClans1 ("16/17 or 17"), u/Specific-Serve-2324 ("confident I got 17/17"), and
  u/BothMarionberry8063 ("17 questions to be completed within 60 minutes", QR, Australia).
  Out of shard, 1point3acres and Glassdoor agree. The brief's consistency prior is vindicated.
- **The calculator dispute is resolved, and the earlier evidence was wrong.** Several 2022–2023
  posters said no calculator was permitted. In the 2027 cycle the invitation email itself says
  otherwise — u/SizeSea7029 quotes it: "It says it's 60 mins and you can use a pen paper and
  calc." u/Sufficient_Damage_77 assumed none was allowed and did the arithmetic by hand; a
  co-candidate corrected him in-thread ("Yeah your allowed a calculator"). Both sides are
  recorded, with the contradiction stated in each `doubt`.
- **Mettl is confirmed as the trading-assessment platform** by two independent 2026 posters who
  name it in thread titles (`1tx1a6o`, `1v39kqd`). This contradicts u/snoopy_priesthood's "runs
  on their own janky platform" and u/Admirable_Rain983's "they use their own platform" — both
  also recorded, with the conflict flagged.
- **A CodeSignal coding round now follows the probability OA on the trading track.** Attested
  independently by u/DINOBOIZ69 (C++), u/TheClashofClans1 (520/600), u/Formal-Region-6894, the
  thread `1u29ykg` title, and QuantNet's jmckevitt (70-minute test, 2025). This is new since the
  older recalls and worth flagging to downstream consumers as a process change.
- **The snickerdoodle question** (`1u4b26p`) is the only place in this shard where a named SIG OA
  problem is given with a worked answer — u/TimeGone43: "snicker doodle was just 7C0 + 7C1 + ...
  + 7C6 = 2\^7 - 1". Two posters recognise it independently. Note that `tradermath.org` lists a
  "Baked Goods Probability Puzzle" in its SIG brainteaser index; that is suggestive of the same
  item leaking into vendor material, but a vendor index entry is not evidence and was not used.
- **A second, shorter paper exists.** 16 questions in 20 minutes (u/Nero-Tulip 2023, four posters
  in `165049h`, a Glassdoor QT review) and 14 in 20 minutes (u/weIBnow 2022, u/Leader-board).
  Vendors call this the *Quantitative Evaluation* as opposed to the 60-minute *Problem Solving
  Assessment*. Both formats appear real; length varies by cycle.
- **Contradictory counts are recorded, not suppressed**, per the no-over-filtering rule:
  27 questions (WSO Dublin, Sept 2025), 12 in 36 minutes (u/is_quant, 2020), 9 in 60 minutes
  (u/Previous-Salary7925, 2024), 10 questions (u/future_gcp_poweruser, 2024, Europe), 23 in 25
  minutes (equity-markets paper). Each carries an explicit `doubt` naming the disagreement.
- **Difficulty calibration, two independent readings.** u/Specific-Serve-2324 (Putnam top 100,
  2×USAMO): "AMC 10/12 probability questions, with the last few being AIME 1-5 level".
  u/future_gcp_poweruser (2024, Europe): "These questions resemble typical maths competition tests
  the most." Two strangers two years apart reaching for the same comparison.
- **The frog problem** is attested twice in-shard (u/stefano31214 2024-09; u/n0obmaster699
  2025-01) and neither writes it out. u/AffectionateStore225, sitting the same paper the same
  week as the first, replied "No frog for me" — the paper varies between candidates.
- **The 25-horses question was checked for laundering** (query 25). It is a decades-old classic
  reproduced by many vendors. The WSO submission is dated and role-tagged (Quant Trader Intern,
  Bala Cynwyd, Sept 2025, Declined Offer) so it is kept — with a `doubt` saying plainly that the
  candidate may be reciting a famous puzzle rather than the one he was set.
- **Cutoff claims are mutually inconsistent and should all be distrusted.** "70% bar (12 up)";
  rejection at 12-13/16; "~9-10/16 passed"; "520/600 passes"; "I've seen people move on with 3-4
  wrong". Nobody outside SIG can know these. All are recorded with the conflict noted.

---

## 7. What I could NOT establish — honest gaps

1. **Still almost no verbatim OA question text from an English-language forum.** After a 5×
   larger crawl, exactly one named problem with a worked answer emerged (snickerdoodle, and even
   there the *prompt* is absent — only the binomial sum survives). Candidates in these
   communities self-censor systematically: u/stefano31214 "I'm not sure if we're allowed to
   discuss the problems"; u/weIBnow "I'm really not at liberty to share too much information";
   u/SidKT746 "I don't think I can answer that on a subreddit"; u/Sushi3124 "I will reject anyone
   asking anything about the OA". The 2026 threads are full of people asking for questions and
   almost nobody supplying them; the exchange happens in DMs. **Every fully-worded SIG OA
   question I saw in this entire run came from outside this shard** (a personal blog,
   1point3acres, Glassdoor) or from a prep vendor. This is the shard's defining limitation and
   more crawling will not fix it.
2. **Superday, trading-game, market-making and poker rounds remain effectively undocumented.**
   Only 5 `onsite` records, 1 `market_making`, 2 `poker_game_theory` (both from 2004–2009
   Trade2Win/Elite Trader), 0 `trading_game`, 0 `fermi_estimation`, 0 `sequences`. A targeted
   regex sweep of all 11,436 cached comments for first-person superday recall returned 10 hits,
   of which the only usable ones describe the *timetable* (`e9z85g`) or the *phone screen*
   (`famt3pp`). The 2019 thread "What's SIG's intern onsite like?" **drew zero replies**, and its
   deleted twin drew one. Everything confidently asserted online about SIG's poker round and
   group trading game traces to prep vendors, not to a candidate saying what happened to them.
   **This is the largest substantive hole and it is a property of the sources, not the search.**
3. **Blind and Hacker News produced zero records** after two passes each. Two of the six named
   sources in this shard are empty for the QT track.
4. **Comment-body full-text search is unavailable** (§4), so SIG recalls inside generically-titled
   threads are largely unreachable. The megathread workaround produced one record from ~90 trees.
5. **~248 of 258 WSO interview submissions are paywalled**, and WSO forum reply bodies do not
   render under WebFetch.
6. **Level attribution is imperfect:** 36 of 96 records are `level: unknown` because the poster
   never said. Where a thread title said "internship" but the individual commenter did not, the
   record follows the commenter's own words, not the thread's.
7. **Office attribution is mostly unknown** (66 of 96). SIG appears to run region-specific papers
   — the Dublin 27-question report and the European 10-question report may be evidence of that —
   and this shard cannot resolve it.
8. **Geographic coverage is thin outside the US and Ireland.** Hong Kong and Singapore: nothing.
   London: nothing first-person. Sydney: one Discovery Day record (behavioural only). Australia:
   two, both from one poster.
9. **`reported_answer` is filled on only two records** — the snickerdoodle binomial sum and the
   2006 Elite Trader three-of-a-kind answer (whose arithmetic is wrong, as its `doubt` notes).
   Forum posters report *scores*, not solutions.
10. **The 2026 material is heavily weighted to one cycle and one subreddit.** 31 of 96 records are
    from 2026 and 31 of 72 Reddit records are from r/quantfinance, mostly the Summer 2027 QT
    intern cycle running at the time of the crawl. That is a strength for currency and a weakness
    for independence: several posters (u/Formal-Region-6894, u/SidKT746) appear in multiple
    records, and repeat appearances by the same person are **not** independent corroboration.
    `poster_context` names the poster on every record so this can be audited downstream.
11. **The crawlers were still running when this file was written** (`as_comments.py` at ~288/949
    threads on its final queue). Coverage is far better than mid-run but not exhaustive.
