# Tier A harvest log — HRT / Jump / DRW / Five Rings / Akuna / Old Mission / Two Sigma / D. E. Shaw

Shard: Tier-A prop and quant firms, all role tracks, **internship prioritised**, English + Chinese.

Deliverable: `raw/tier_a_hrt_jump_drw_others.jsonl` — **627 records across 252 distinct
source URLs**.

Every `source_quote` was string-matched against bytes actually fetched into
`.verify_cache`. Final gate (`tools/tier_a2_verify_quotes.py`, re-run against the assembled file):

```
VERIFIED OK : 511
FAILED      : 0
UNCHECKABLE : 116   (every one on a host that refuses this box)
```

The 116 uncheckable records map **exactly** onto the 116 records whose host blocks
automated re-fetch (1point3acres 73, reddit 35, glassdoor 24 — minus overlap — plus
quantnet 4 and efinancialcareers 4). Zero records claim `full_text` on a host I could
not actually read, and no record survived that failed a re-fetch.

---

## 1. Network reality, as measured from this box

| Host | Direct `curl` | Verdict |
| --- | --- | --- |
| `wallstreetoasis.com` | Cloudflare challenge | Reachable **only** through `r.jina.ai`. 215 records. |
| `jointaro.com` | 200 | Reachable. 94 records. |
| `geeksforgeeks.org` | 200 | Reachable. 82 records. |
| `nowcoder.com/discuss/<id>` | 200, SSR payload carries the post body | Reachable. 53 records. |
| `nowcoder.com/search?...` (HTML) | **0 bytes** | Client-rendered, unusable. |
| `nowcoder.com` **POST search API** | 200 JSON | Found this session; see §4. |
| `teamblind.com` | 200, ~420 KB, full thread + comments in HTML | Reachable. 32 records from 234 cached threads. |
| `codeforces.com` | 200 | Reachable. 3 records. |
| `hudsonrivertrading.com` | 200 | Reachable (firm's own careers blog). 3 records. |
| `ecedplacement.wordpress.com` | 200 | Reachable. 5 records. |
| `quantnet.com` | **403 to curl** | WebFetch renders it; quotes taken that way, records marked uncheckable. |
| `glassdoor.com` | Blocked | `r.jina.ai` + WebSearch full-page dumps. `snippet_only`. |
| `1point3acres.com` | Blocked (Cloudflare **and** a 188-point paywall) | WebSearch snippets only. `snippet_only`. |
| `reddit.com`, `old.reddit.com/.json` | **403** | Blocked. Reached only via the Arctic Shift archive. |
| `api.pullpush.io` | **403 Cloudflare** | Blocked. |
| `arctic-shift.photon-reddit.com` | Works for `subreddit`+`author` scoped queries; full-text `body=` search times out | Partially usable; see §5. |
| `efinancialcareers*.com` | AWS WAF human-verification interstitial | WebSearch extract only. `compilation_only`. |
| `medium.com` | 200 but 5.8 KB JS shell | Article bodies not retrievable. **No records.** |
| `elitetrader.com` | 404 on every thread tried | **No records.** |
| `zhihu.com`, `xiaohongshu.com`, `tieba.baidu.com`, `leetcode.com/discuss`, `quizlet.com` | Blocked | **No records.** |

## 2. Yield by host

| host | records | distinct URLs used | how reached |
| --- | --- | --- | --- |
| `www.wallstreetoasis.com` | 215 | 74 (of 132 permalinks + 9 listing pages fetched) | `r.jina.ai` proxy |
| `www.jointaro.com` | 94 | 78 | direct curl |
| `www.geeksforgeeks.org` | 82 | 14 (of 50 cached) | direct curl |
| `www.1point3acres.com` | 73 | 26 | **BLOCKED** — WebSearch snippets |
| `www.nowcoder.com` | 53 | 11 | direct curl (SSR payload) |
| `www.reddit.com` | 35 | 23 | Arctic Shift archive dumps |
| `www.teamblind.com` | 32 | 16 (of 234 cached) | direct curl |
| `www.glassdoor.com` | 24 | 4 | **BLOCKED** — proxy + WebSearch dumps |
| `ecedplacement.wordpress.com` | 5 | 1 | direct curl |
| `quantnet.com` | 4 | 2 | WebFetch only |
| `www.efinancialcareers-canada.com` | 4 | 1 | **BLOCKED** — WebSearch extract |
| `codeforces.com` | 3 | 1 | direct curl |
| `www.hudsonrivertrading.com` | 3 | 2 | direct curl |

`jointaro.com`, `geeksforgeeks.org` and `hudsonrivertrading.com` are typed
`source_type: "blog"` because none appears in the controlled vocabulary. The first two
host per-candidate, per-date first-person write-ups rather than editorial listicles,
which is why they were kept; the third is the firm's own careers blog and is labelled as
such in `poster_context`. `ecedplacement.wordpress.com` is typed `university_bbs` — it is
a college Electronics & Communication department's placement-experience blog, which
credits the student by name.

## 3. Counts

| firm | records | internship | new grad | experienced | unknown |
| --- | --- | --- | --- | --- | --- |
| Hudson River Trading | 105 | 74 | 5 | 5 | 21 |
| D. E. Shaw | 102 | 88 | 11 | 1 | 2 |
| Akuna Capital | 98 | 37 | 21 | 2 | 38 |
| Jump Trading | 82 | 44 | 1 | 5 | 32 |
| DRW | 67 | 45 | 3 | 1 | 18 |
| Five Rings | 64 | 44 | 1 | 1 | 18 |
| Two Sigma | 61 | 28 | 4 | 4 | 25 |
| Old Mission Capital | 48 | 20 | 5 | 3 | 20 |
| **total** | **627** | **380** | **51** | **22** | **174** |

Role track: `quant_developer` 354, `quant_trader` 133, `quant_researcher` 106,
`unknown` 29, `data_scientist` 4, `quant_analyst` 1.

Round: `phone_technical` 287, `online_assessment` 209, `onsite` 98, `superday` 11,
`unknown` 9, `take_home` 8, `trading_game` 3, `math_sequences_test` 2.

Question type: `coding_algorithms` 281, `other` 94, `probability` 65,
`statistics_regression` 25, `logic_brainteaser` 25, `mental_math_speed` 23,
`behavioral` 21, `combinatorics` 14, `fermi_estimation` 13, `ml_modeling` 13,
`expected_value` 13, `market_making` 11, `linear_algebra` 9, `poker_game_theory` 6,
`sql_data` 5, `options_theory` 4, `betting_odds_arbitrage` 3, `stochastic_calculus` 1,
`sequences` 1.

Access: `full_text` 549, `snippet_only` 74, `compilation_only` 4.
Retrieval: `webfetch` 524, `websearch_snippet` 103.
Language: `en` 506, `zh` 81, `mixed` 40.
Platform named by the source: `HackerRank` 76, `CodeSignal` 4, `Codility` 3,
`VidCruiter` 2, otherwise unknown.

---

## 4. Queries run

### 4.1 WebSearch — English

| Query | Outcome |
| --- | --- |
| `site:reddit.com Hudson River Trading intern OA questions asked` | No results at all. |
| `reddit Jump Trading quant intern online assessment "they asked" probability` | No Reddit. Surfaced quantnet.com/threads/technical-test-at-top-prop-shop.18878 → **3 DRW records**. |
| `reddit "Five Rings" intern math test questions experience` | No Reddit. Only aptitude-test-prep / quantblueprint / a Harvard job posting. No yield. |
| `reddit DRW online assessment quant trading intern what questions` | WSO DRW page (already mined). Rest vendor. |
| `"r/quant" OR "r/csMajors" Akuna Capital intern interview "asked me" options` | No yield. |
| `reddit.com/r/quant Two Sigma quant researcher intern interview questions thread` | Blind two-sigma-quant-research-interview-asyhkqpz (fetched — a question-*asking* post, no recall) + a paywalled 1p3a thread. |
| `quantnet.com forum Hudson River Trading interview questions asked thread` | Prep-vendor guides + a study-programme thread. No yield. |
| `site:teamblind.com Hudson River Trading OR "Jump Trading" OR DRW interview questions asked` | 6 Blind URLs fetched → **2 Jump records**. |
| `teamblind.com "D. E. Shaw" OR "DE Shaw" interview OA question intern` | Surfaced codeforces.com/blog/entry/145050 → **3 D. E. Shaw records**. |
| `codeforces.com/blog "D. E. Shaw" OR "DE Shaw" online assessment questions writeup` | Same entry; no further Codeforces posts. |
| `"Old Mission Capital" interview trading intern "they asked" probability mental math experience` | WSO Old Mission listing page, already mined. |
| `reddit r/quant "Five Rings" OR "Old Mission" OA questions remember 2025` | HuggingFace brainteaser dataset — **rejected, §6**. |
| `reddit "Akuna" OA "order book" OR "minimum swaps" question intern software engineer` | All hits banned content farms. |
| `reddit r/quant "DRW" OA 6 questions 45 minutes "i got" remember question` | Quantnet thread again. |
| `leetcode discuss Hudson River Trading OR "Jump Trading" OA intern question 2025` | No LeetCode Discuss results at all. |
| `"Old Mission Capital" intern interview questions probability mental math reddit` | WSO listing + two login-walled 1p3a threads (`/interview/thread/1155392`, `/interview/thread/1010183`) + quantblueprint/quantvault (**rejected**). Confirmed WSO permalinks were the seam. |
| `Old Mission Capital trading intern online assessment "they asked" experience 2025` | Same WSO listing highlights; a LinkedIn profile; Lensa job ad. No new question text. |
| `site:teamblind.com Five Rings OR "Old Mission" interview assessment questions` | Blind company index pages; all threads already cached. The three unmined Old Mission threads were re-read and contain **no** question recall — they are "what should I expect?" posts. |
| `"Akuna Capital" VidCruiter video assessment intern "what I was asked" experience` | tradermath / tradinginterview / oavoservice / cookd.ai — **all rejected**. No first-person source found for VidCruiter beyond what is already in the file. |
| `Two Sigma quant researcher intern interview "they asked me" probability question 2025 blog` | techinterview.org, datainterview, getsmartresume, myntbit — **all rejected**. No yield. |
| `github quant interview experience log HRT Jump DRW "Five Rings" onsite questions notes` | quantblueprint / oavoservice / tradermath, plus the Five Rings WSO permalink already captured. No GitHub repo with recalls. |

### 4.2 WebSearch — Chinese and mixed-script

| Query | Outcome |
| --- | --- |
| `Akuna Capital 面经 实习 期权 笔试 题目` | programhelp.net + oavoservice.com — **both banned**. |
| `nowcoder.com/discuss Akuna 面经 笔试 实习` | One thread (`377107534111408128`) but it is an Akuna recruiting advertisement. |
| `1point3acres Jump Trading 面经 实习 OA 题` | **Yielded.** The `bbs/tag/jumptrading-8699-1.html` listing exposes each thread's opening ~100 chars, which is where posters put the questions → 2 Jump records (C++ order-book keeping; buy/sell pattern arrays). |
| `德劭 面经 D.E.Shaw 量化 实习 面试 题目` | GeeksforGeeks (mined) + interview-help.live (**banned 代做**). |
| `HRT Hudson River Trading 面经 实习 笔试 求米 2026` | 1point3acres.com/interview/thread/1141239 → **3 HRT Algo-Dev intern OA records**. |
| `1point3acres.com/bbs/tag/ hudsonrivertrading 面经 HRT OA 题` | Same thread + hackerprep.io (vendor). |
| `1point3acres.com/bbs/tag/ twosigma 面经 OA 量化 实习` | **Biggest Chinese yield.** Four Two Sigma tag pages (`-5`, `-8`, `-22`, `-30`) → 11 Two Sigma records. |
| `1point3acres 面经 "Akuna" OR "Old Mission" OR "Five Rings" OA 题目 实习` | Five Rings tag page → 2 records (broken-stick triangle probability; the 30-second HR answer clock). |
| `1point3acres.com/bbs/tag/ deshaw 德劭 面经 OA 题` | Codeforces + GFG (mined) + desiqna.in (login-walled) + datalemur (vendor). |
| `nowcoder "AkunaCapital笔试" OR "akuna-cpp开发一面" 牛客 帖子` | Could not recover the permalinks behind three Akuna records; see §6. |
| `Old Mission Capital 面经 实习 量化` | quantt.co.uk (vendor) + two login-walled 1p3a threads. **Old Mission has essentially no Chinese-language footprint** — no Shanghai office, so no 校招 traffic. |
| `Five Rings 笔试 面经 实习 2026届 题` | **Yielded confirmation.** `1point3acres.com/bbs/thread-1141524-1-1.html` (already in the file, 4 records) — the visible replies carry `P(sum of two dice > their product)`, 单位球上的 Var(X), and 微积分求 arc length. |
| `Akuna Capital 面经 期权 笔试 实习 题目` | programhelp.net (banned, incl. its dev.to mirror), oavoservice.com (banned). |
| `德劭 D.E. Shaw 面经 量化 实习 笔试题` | **Yielded.** `ecedplacement.wordpress.com/2021/04/18/de-shaw-2/` — a college ECE department placement blog → 5 records. Also two unmined GFG pages. |
| `HRT Hudson River Trading 面经 实习 OA 手撕 题` | `learncswithus.com/2025/09/28/hrt-intern/` — looked like a genuine 面经 with a real BFS-with-keys problem, but the page header reads **代面试｜零订金保OFFER｜VO代面｜VO辅助｜OA代写｜OA辅导**. **Rejected**, see §6. |
| `Jump Trading 笔试 量化 面经 2026 实习 概率` | 1p3a Jump tag page (mined; the 165-minute 3-question OA with the OOD `FILE` abstract class is already recorded) + techinterview/tradermath/myntbit/quantt (**rejected**). |

### 4.3 Programmatic sweeps (not WebSearch)

**Nowcoder POST search API** (`tools/nc_search.py`, then `tools/nc_search2.py`). The HTML search page
returns 0 bytes, but the JSON API behind it responds. Two passes:

- Pass 1: 18 firm spellings × 9 suffixes (`""`, ` 面经`, ` 笔试`, ` OA`, ` 实习`, ` 量化`,
  ` 笔经`, ` 面试`, ` 真题`) = 162 queries → 227 posts, 19 carrying a firm plus recall
  language.
- Pass 2 with vocabulary pass 1 never tried: 18 firms (adding 奥可纳, 哈德逊, 光速, 五环,
  老任务, 两西) × 16 suffixes (网测, 手撕, 校招, 暑期实习, 2026届, 2025届, 量化交易员,
  量化研究员, 挂了, 求米, hackerrank, codesignal, 题目, 面试题, 实习面经, 秋招) = 288
  queries.

Roughly **450 Nowcoder API queries**, 732 result lines logged, → 53 records from 21
threads. Most Nowcoder hits for these firms are recruiting ads or 拼多多/字节 posts that
merely name-drop a US firm; the genuine Tier-A 面经 traffic is on 1point3acres, not
Nowcoder.

**Reddit via Arctic Shift** (`tools/reddit_sweep.py`, `tools/reddit_sweep2.py`, `tools/reddit_threads.py`,
`tools/reddit_comments.py`). Reddit itself and PullPush both 403 this box. Arctic Shift's
full-text `body=` endpoint times out, but `subreddit`+`title`+date-window queries work,
so the sweep was rebuilt as a windowed crawl: 26 subreddits (`csMajors`,
`cscareerquestions`, `internships`, `quant`, `quantfinance`, `FinancialCareers`,
`algotrading`, `leetcode`, `developersIndia`, `statistics`, plus a dozen university subs)
× 9 firm terms × 11 annual windows 2016–2027 = **2,574 windowed jobs**. Results: 904
cached comment bundles and 261 thread dumps, scanned with `tools/reddit_scan.py` /
`tools/reddit_cscan.py` / `tools/reddit_grep.py` → **35 records**. Quotes were verified against the
archive JSON with `tools/verify_reddit.py` rather than against reddit.com, which 403s.

**WallStreetOasis permalinks** (`tools/wso_sitemap.py`, `tools/wso_pages.py`, `tools/wso_perm.py`,
`tools/wso_diff.py`). The company listing pages truncate each write-up; each submission also
has a permalink that serves it whole. 132 permalinks were fetched through `r.jina.ai`.
Because WSO serves the same submission at both URLs, `tools/wso_diff.py` and a post-build
overlap check were used to keep the two from double-counting; **10 permalink records were
dropped in the final pass** as literal restatements of questions already recorded from the
listing pages, and 10 surviving records carry an explicit note in `doubt` that they are
the same account as a listing-page record.

**Teamblind bulk** (`tools/blind_fetch.sh`, `tools/blind_comments.py`, `tools/blind_next.py`,
`tools/blind_scan.py`, `tools/blind_scan2.py`). 234 threads cached from the eight firms' company
pages. Comments had to be parsed out of the `__NEXT_DATA__` payload rather than the
JSON-LD block, because Blind omits replies from "company page" users in JSON-LD and that
silently lost real recalls. 32 records.

**GeeksforGeeks** (`tools/gfg_read.py`). 50 D. E. Shaw interview-experience pages cached;
14 mined. GFG buries ~2 kB of account inside ~160 kB of nav and course ads, so the reader
slices between the `Last Updated :` line and the `Comment`/`Explore` footer.

---

## 5. Strongest finds

1. **`codeforces.com/blog/entry/145050`** — a competitive programmer's write-up of a
   D. E. Shaw online assessment, with the problems stated in full and dated. Fetchable,
   attributed to a named handle, and the author has no product to sell.
2. **`www.wallstreetoasis.com/company/old-mission-capital/interview`** — the July 2024
   Quant Trader submission on the Old Mission listing page is the only substantial public
   account of that firm's two-part OA: a ~35-question math section, then a coding question
   the poster remembers as running median, followed by a market-making round on *the total
   number of Olympic gold medals the US has won*. That last one is specific enough that it
   is very unlikely to be confabulated. (The same submission also has a permalink at
   `/interview/quant-trader`; the records are filed under the listing URL, which is where
   they were first read, and the permalink was dropped to avoid double-counting.)
3. **`www.geeksforgeeks.org/interview-experiences/d-e-shaw-internship-interview-experience-on-campus-2022/`**
   — a QTE intern who was selected, reproducing nine distinct problems across three
   rounds with the interviewers' follow-ups, including the `getManager`/`getCManager`
   lowest-common-manager problem where the tree structure is deliberately withheld.

Honourable mention: `1point3acres.com/bbs/thread-1141524-1-1.html`, where the original
poster's questions sit behind a 188-point paywall but two *replies* quote them in the
open — `P(sum of two dice > their product)` and the variance of a coordinate on the unit
sphere — which is how the Five Rings 2026 QR OA got documented at all.

---

## 6. Rejected sources (negative evidence of authenticity)

None of these contributed a single record.

**Banned by name in the brief:** `programhelp.net` (including its
`dev.to/net_programhelp_*` mirror), `quantblueprint.com`, `tradermath.org`,
`tradinginterview.com`, `everythingquant.com`, `theinterviewden`, `techinterview.org`,
`howtoanalyzedata`, `prepfully`, `interviewquery`, `tryexponent`, `jobtestprep`.

**Chinese 代做 / 保过 / 代面试 vendors** — the tell is a page selling assistance rather
than recounting an experience: `oavoservice.com` ("OA VO Service"), `csoahelp.com`
("OA 代做 – 面试辅助"), `interview-help.live` (title reads 面试代面 面试代做 oa/vo作弊),
and newly this session **`learncswithus.com`**, whose masthead reads
`代面试｜零订金保OFFER｜VO代面｜VO辅助｜OA代写｜OA辅导`. The `learncswithus` page is worth
flagging specifically: it is written in the first person, names a plausible HRT Python
intern round, and states a coherent BFS-with-key-bitmask problem. It is exactly the shape
of a genuine 面经 and would have passed a casual read. Rejected on the vendor tell alone.

**Content farms / AI-generated question hubs:** `quantt.co.uk`, `quantvault.org`,
`myntbit.com`, `interviewsense.org`, `interviewchamp.ai`, `leakcode.dev`,
`interviewfox.ai`, `hackerprep.io`, `prachub.com`, `lodely.com`, `linkjob.ai`,
`applr.ai`, `getsmartresume.com`, `datainterview.com`, `cookd.ai`, `dragganaitool.com`,
`aptitude-test-prep.com`, `extern.com`, `datalemur.com`, `dev.to/interviewshow-cs`,
`lensa.com`.

Judgement calls worth recording:

- **`huggingface.co/datasets/ReinforceNow/quantqa`** — a brainteaser bank whose rows carry
  a `firms` tag (e.g. `"firms": ["Five Rings"]`). There is **no attestation of any kind**
  behind the tags: no candidate, no date, no thread. This is the "N quant questions
  listicle" the brief excludes. Rejected.
- **`quantvault.org/old-mission-interview-questions.html`** — advertises "68 Real Problems"
  with per-question "last reported" months, which is more provenance discipline than most
  vendors show, but it states outright that it rewrites every prompt and does not claim
  the wording is verbatim. Nothing quotable. Rejected.
- **`desiqna.in`** — D. E. Shaw OA pages with real-looking titles but login-walled bodies.
  Nothing to quote. Rejected.
- **`interviewfox.ai`** — cites 1point3acres and Taro thread-by-thread and reads as
  first-person ("I sat the standard Akuna Capital coding OA"), but is a synthesised
  aggregation. Rejected, and its cited primary sources were pursued directly instead.

**Retrieved but out of shard scope**, so deliberately not recorded: the D. E. Shaw
fundamental-equities, fundamental-research-analyst, compliance-analyst, rotational-associate
and strategy-and-business-development WSO permalinks, and the Two Sigma
product-and-capital-strategy intern permalink. These are real accounts of real interviews,
but they are fundamental-investing and corporate tracks, not quant role tracks. Listing
them here so the omission is visible rather than silent.

---

## 7. What I could NOT establish

1. **Reddit is under-represented and was extremely expensive.** 35 records, all reached
   through the Arctic Shift archive rather than reddit.com. Reddit 403s this box,
   PullPush is Cloudflare-walled, and Arctic Shift's full-text search times out, so the
   only workable route was a 2,574-job windowed crawl by subreddit and title. Anything
   whose firm name appears only in the comment body — which is most of it — is invisible
   to that method. The brief expected Reddit to be a primary seam; it was a marginal one.

2. **1point3acres thread bodies remain unreadable.** All 73 1p3a records come from tag-page
   row previews or from replies that quote the original post, and the previews truncate at
   roughly 100 characters — several questions cut off mid-sentence (`第一题：missin`, `一个.`).
   Full posts sit behind a 188-point paywall. These are honestly labelled `snippet_only`.

3. **Three Akuna records cite a Nowcoder *search* URL**, not a thread permalink. The
   bodies are plainly real — usernames, universities, post titles like
   `2022-09-04-AkunaCapital笔试46min` — but the page is client-rendered, so an automated
   re-fetch will not find the quote. The permalinks could not be recovered even with the
   POST API. They are downgraded to `access: snippet_only` /
   `retrieval_method: websearch_snippet` with the defect written into `doubt`. Treat these
   three as the weakest provenance in the file.

4. **D. E. Shaw's 102 records are overwhelmingly the India campus pipeline.** 82 of them
   are GeeksforGeeks and 5 are a college placement blog, i.e. SDE / QTE / Quality Test
   Engineer intern drives at Indian colleges. That is a real and well-attested pipeline,
   and every such record says so in `doubt`, but it is **not** the New York quantitative
   research seat that most English-language "D. E. Shaw quant" discussion means. The
   research-side interview is barely evidenced here.

5. **Old Mission Capital is still the thinnest firm at 48 records**, and 40 of those are
   WallStreetOasis. The firm has no Chinese-language footprint at all (no Shanghai office,
   so no 校招 traffic on Nowcoder or 1p3a), the Blind threads about it are people asking
   what to expect rather than reporting what happened, and its Glassdoor intern page has
   nothing minable. Six searches this session produced one genuinely new seam (WSO
   permalinks) and nothing else.

6. **`question_type` is 45% `coding_algorithms`.** That reflects where the evidence is —
   Taro, GeeksforGeeks, Blind and WSO all skew to engineering candidates — not the actual
   balance of these firms' interviews. Trader-side content (`market_making` 11,
   `mental_math_speed` 23, `options_theory` 4) is thin, and the Akuna options-theory
   reputation in particular is far better attested by prep vendors than by anyone who
   actually sat the screen.

7. **`level` is `unknown` for 174 of 627 records.** Where the source did not state
   internship / new-grad / experienced, it was left `unknown` rather than guessed. Most are
   WSO entries whose role heading names a title but no seniority, and 1p3a previews that
   truncate before the poster says which cycle they were in.

8. **`cycle` is `unknown` for 590 of 627.** Sources overwhelmingly date the *post*, not the
   recruiting cycle, so `post_date` is populated but `cycle` usually is not.

9. **No records at all for these source types**, despite being in the controlled
   vocabulary: `leetcode_discuss`, `zhihu`, `xiaohongshu`, `bilibili`, `tieba`, `newsmth`,
   `youtube`, `student_doc`, `github_repo`, `elitetrader`. The GitHub repos that surfaced
   (`bualpha/Resources`, `anuroopsaini/2026QuantInternships`) are link directories and
   application trackers, not question recalls. Medium articles render as a 5.8 kB JS shell.

10. **52 of 627 quotes are under the 40-character target** (minimum 22). These are cases
    where the source itself is terse — a WSO question block reading only
    `Implement a trie in C++.` — and padding them would have meant stitching
    non-contiguous text. Per the brief, shorter and honest was preferred.

11. **One record carries a date that cannot be right.** WSO shows
    `drw/interview/trader-intern-1` as "Interviewed October 2026", which is in the future
    relative to retrieval (August 2026). The submitter's date entry is wrong; `post_date`
    reproduces what the page says and `doubt` records the impossibility.

12. **Search itself is now saturated with prep vendors.** By the end of this session,
    a query like `"Akuna Capital" VidCruiter video assessment intern "what I was asked"` —
    phrased specifically to surface first-person language — returned four results, all
    four of them vendors. The marginal cost of one more real question through WebSearch is
    now very high, and the remaining seams are all sites that block automated fetching.

---

## 8. Tooling written across this harvest

| File | Purpose |
| --- | --- |
| `tools/assemble_tier_a.py` | Concatenate part files, dedupe on `(firm, url, normalised question_text)`, and fail loudly on any controlled-vocabulary violation. |
| `tools/tier_a2_verify_quotes.py` | Re-fetch every `source_url` and assert the quote appears; classify bot-blocked hosts as UNCHECKABLE rather than FAILED. |
| `tools/verify_reddit.py` | Same gate for Reddit records, run against the Arctic Shift archive JSON since reddit.com 403s. |
| `tools/pagetext.py` | Render a cached page to readable text so quotes are copied from the exact bytes the verifier will see. |
| `tools/wso_sitemap.py`, `tools/wso_pages.py`, `tools/wso_perm.py`, `tools/wso_diff.py` | Enumerate, fetch and read WallStreetOasis permalinks; diff them against what the listing pages already gave. |
| `tools/blind_fetch.sh`, `tools/blind_comments.py`, `tools/blind_next.py`, `tools/blind_scan.py`, `tools/blind_scan2.py` | Bulk-fetch Teamblind threads and parse comments out of the `__NEXT_DATA__` payload. |
| `tools/nc_search.py`, `tools/nc_search2.py`, `tools/nc_triage.py`, `tools/nc_context.py`, `tools/extract_nowcoder.py` | Drive Nowcoder's POST search API, triage candidates, and read the SSR post bodies. |
| `tools/reddit_arctic.py`, `tools/reddit_sweep.py`, `tools/reddit_sweep2.py`, `tools/reddit_threads.py`, `tools/reddit_comments.py`, `tools/reddit_scan.py`, `tools/reddit_cscan.py`, `tools/reddit_grep.py`, `tools/reddit_firm.py` | Windowed Arctic Shift crawl and the scanners over its output. |
| `tools/gfg_read.py` | Slice the GeeksforGeeks write-up out of its surrounding nav and ad furniture. |
| `tools/gd_extract.py`, `tools/extract_taro.py`, `tools/wso_extract.py` | Per-source readers for Glassdoor, Taro and WSO listing pages. |
| `tools/fix_search_url.py`, `tools/fix_failed_quotes.py`, `tools/fix_short_quotes.py`, `tools/repoint_nc_search.py` | Targeted repairs: downgrade unverifiable-URL records, fix quotes that failed re-verification, repoint Nowcoder search URLs at permalinks where one could be found. |
| `raw/_tier_a_parts/build_p06.py` … `build_p27.py` | Emit the records, one part file per seam (p01–p05 were written before the build scripts were split out). |
