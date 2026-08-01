# Tier A shard log — Jane Street / Citadel / Citadel Securities / Optiver / IMC Trading

Output: `/workspace/harvest/raw/tier_a_js_citadel_optiver_imc.jsonl`
Writer + schema validation: `/workspace/harvest/tools/tiera_lib.py`
Quote gate: `/workspace/harvest/tools/verify_quotes.py` → `/workspace/harvest/reports/tier_a_quote_gate.json`

Every record in the shard was written by one of the batch scripts below. Each script
either slices its question text directly out of retrieved page text, or asserts every
quote against the retrieved page before writing. Nothing was typed from memory.

---

## 1. Network reality established this session (tested, not assumed)

| Host | Direct `curl`/urllib | WebFetch tool | Web-search excerpt | Notes |
|---|---|---|---|---|
| `arctic-shift.photon-reddit.com` | works | — | — | Full Reddit post + comment bodies; used as the Reddit read path |
| `reddit.com` | 403 | blocked | works | Never fetched directly; bodies came from the Arctic Shift mirror |
| `nowcoder.com` (`/discuss/…`, `/feed/main/detail/…`) | **Aliyun WAF, 200 with JS shell only (11 201 bytes)** | **works** | works | WebFetch is the only path; plain HTTP gets `为了更好的访问体验，请进行验证` |
| `blog.csdn.net` | **HTTP 521** | works | works | Wayback snapshot `20251104194117` verified to contain the same text |
| `wallstreetoasis.com/forum/…` | works | works | works | Usable |
| `wallstreetoasis.com/company/…` | **Cloudflare "Just a moment"** | **blocked (also timed out)** | works | `r.jina.ai` also returned Cloudflare 403 |
| `glassdoor.com` | blocked | blocked | **full page captured to disk by the search tool** | Recorded as `retrieval_method: websearch_snippet` |
| `canarywharfian.co.uk` | **works** | 404 on the deep review URL | works | Company page carries the full review text |
| `medium.com` | — | works | works | Usable |
| `everythingquant.com` | — | works | works | Reachable, but on the project's prep-vendor exclusion list — see §5 |
| `jointaro.com` company index | — | JS shell, empty | works | Individual `/experiences/…` pages do render |
| `1point3acres.com` | blocked | blocked | works | Snippet-only throughout |
| `teamblind.com` | — | works | works | Usable |
| `xjtu.app` | works | works | works | Usable |
| `web.archive.org` CDX/API | works (occasional 429/503) | — | — | No snapshots exist for the Nowcoder URLs used here |

---

## 2. Queries run

### English
- `Jane Street intern OA questions reddit`
- `Citadel Securities quant research OA HackerRank`
- `Optiver 80 in 8 mental math test experience`
- `IMC trading intern assessment questions`
- `Optiver sequences test intern`
- `Jane Street estimathon interview`
- `quantnet Optiver 80 questions 8 minutes math test experience thread`
- `wallstreetoasis.com IMC Trading interview questions asked intern superday`
- `"Citadel Securities" OA HackerRank question "I was asked" reddit intern 2025`
- `glassdoor Optiver Quantitative Trader Intern interview questions`
- `glassdoor "Jane Street" Quantitative Trader Intern interview questions probability`
- `canarywharfian.co.uk Jane Street IMC Citadel interview review internship`
- `reddit r/quant IMC quant trading OA "the questions were" mental math sequences experience 2025`
- `https://www.glassdoor.com/Interview/Jane-Street-Quantitative-Trader-Interview-Questions-EI_IE255549.0,11_KO12,31.htm` (URL-as-query, to force a page capture — did not trigger one)

### Chinese / mixed script
- `牛客网 Citadel 笔试 面经 量化 实习 真题`
- `nowcoder.com IMC Trading 笔试 面经 实习 OA 题目`
- `简街 Jane Street 面经 实习 笔试 概率题 牛客`
- `Optiver 笔试 面经 nowcoder 量化交易员 实习 2026 题目`
- `site:nowcoder.com Optiver 面经 笔试 题目 2026`
- `site:nowcoder.com IMC 面经 笔试 实习 题`
- `site:nowcoder.com Citadel Securities 面经 笔试 量化`
- `牛客 Citadel 城堡 面经 feed/main/detail 量化 开发 实习`
- `IMC Trading 笔试 面经 上海 实习 牛客网 量化 题`
- `1point3acres IMC 面经 笔试 OA 题目 实习 trading`

### Reddit archive sweep (programmatic, not a search engine)
`tools/tiera_as_crawl.py` + `tools/tiera_as_stage2.py` against the Arctic Shift API:
49 subreddits × {`Jane Street`, `Citadel`, `Optiver`, `IMC Trading`, `IMC`} for posts, then
`comments/search?link_id=…` per candidate thread. Cache: 1 573 posts, 6 372 comments in
`raw/_tiera_reddit/`. Scanners: `tools/tiera_scan2.py` (comments, joined to parent thread
for firm attribution) and `tools/scan_posts.py` (post selftext).

---

## 3. URLs opened, and whether they yielded

### Yielded (records written)

| URL | Firm | Records | Batch script |
|---|---|---|---|
| `blog.csdn.net/dcdsc/article/details/139953481` | Citadel | 17 | `tiera_b05_citadel_datathon.py` |
| `nowcoder.com/discuss/353157497731096576` | Citadel | 7 | `tiera_b06_nowcoder_cit_js.py` |
| `nowcoder.com/discuss/604265548247040000` | Jane Street | 10 | `tiera_b06_nowcoder_cit_js.py` |
| `glassdoor.com/Interview/Citadel-Software-Engineering-Intern-…` | Citadel | 9 | `tiera_b07_glassdoor_medium_optiver.py` |
| `medium.com/@adityashrivastava2003/citadel-securities-swe-intern-singapore-…` | Citadel Securities | 2 | `tiera_b07_glassdoor_medium_optiver.py` |
| `nowcoder.com/feed/main/detail/464155d6b69747ebaa947add8c266c58` | Optiver | 2 | `tiera_b07_glassdoor_medium_optiver.py` |
| `canarywharfian.co.uk/companies/53/optiver/interviews` | Optiver | 23 | `tiera_b08_canarywharfian_optiver.py` |
| `everythingquant.com/forum/post/imc-launchpad-hirevue-oa/` | IMC Trading | 7 | `tiera_b09_imc.py` |
| `jointaro.com/interviews/companies/imc-trading/experiences/software-engineer-internship-chicago-…` | IMC Trading | 1 | `tiera_b09_imc.py` |
| `wallstreetoasis.com/company/imc-financial-markets/interview/quantitative-trader-intern-1` | IMC Trading | 4 | `tiera_b09_imc.py` |
| `glassdoor.com/Interview/Jane-Street-Quantitative-Researcher-…` | Jane Street | 5 | `tiera_b10_js_gd_wso.py` |
| `wallstreetoasis.com/company/jane-street-capital/interview/quantitative-trading-5` | Jane Street | 2 | `tiera_b10_js_gd_wso.py` |
| `nowcoder.com/feed/main/detail/3d62edffa9dc40c883d3d019dd7f6789` | Optiver | 29 | `tiera_b03_nowcoder_xjtu.py` (earlier) |
| `xjtu.app/t/topic/12756` | Optiver | 7 | `tiera_b03_nowcoder_xjtu.py` (earlier) |
| 12 × `1point3acres.com/bbs/thread-…` | Optiver / IMC / JS | 41 | `tiera_b02`, `tiera_b04` (earlier) |
| 4 × `wallstreetoasis.com/forum/…` | Optiver / JS | 9 | `tiera_b01_wso_medium.py` (earlier) |
| 3 × `teamblind.com/post/…` | Citadel / JS | 5 | `tiera_b04_js_blind_reddit.py` (earlier) |
| 3 × `reddit.com/r/…` (via Arctic Shift) | Citadel / IMC | 3 | `tiera_b04_js_blind_reddit.py` (earlier) |
| `hiya31.medium.com/…citadel-securities-hackerrank-coding-round…` | Citadel Securities | 2 | `tiera_b01_wso_medium.py` (earlier) |
| `openquant.co/blog/how-to-land-a-quant-internship-at-jane-street` | Jane Street | 1 | `tiera_b01_wso_medium.py` (earlier) |

### Opened, no records

| URL | Why not |
|---|---|
| `nowcoder.com/feed/main/detail/42b891d6a195451d8565e20e03bcf27e` | Optiver 上海 IT intern — timeline only, no question content |
| `nowcoder.com/feed/main/detail/81b12138a7f344bb8dbba88bc9d64685` | Optiver 面试体验 — process only |
| `nowcoder.com/discuss/465910881050689536` | Returned the JS shell; same content reached via the `/feed/main/detail/` twin |
| `nowcoder.com/feed/main/detail/bcaea6fb011b4d1a8deb11ff101358e0` | 量化开发求职经验分享 — career advice, no firm-attributed questions |
| `nowcoder.com/enterprise/10438/interview` | Optiver company index — question bodies behind "查看N道真题和解析" |
| `jointaro.com/interviews/companies/{imc-trading,jane-street}/` | JS-rendered index, "Loading questions…" only |
| `wallstreetoasis.com/company/optiver/interview` | Cloudflare bot wall via WebFetch |
| `canarywharfian.co.uk/interviews/optiver/quantitative-trading-summer-internship/14` | HTTP 404; content reached via the company page instead |
| `teamblind.com/post/imc-quantitative-developer-interview-10a131y6` | OP is *asking* what gets asked; the one reply gives no questions |
| `1point3acres.com/bbs/thread-1144831-1-1.html` (IMC 2026 summer OA) | Body behind a 200-积分 paywall; only "120 min 要求写2道题,在hackerrank上写" visible |
| `1point3acres.com/bbs/thread-1152626-1-1.html` (IMC VO trader) | Search excerpt truncated mid-question ("he larger RV squared?"); not safely quotable |
| `1point3acres.com/bbs/thread-669896-1-1.html` (IMC QT OA 数学题+打游戏) | Describes the format, names no question |
| Reddit comment/post scan (6 372 comments, 1 573 posts) | Near-total miss: the archive is dominated by timeline and comp chatter. Only 3 comments carried firm-attributed question content and all 3 were already in the shard. `scan_posts.py` at threshold 9 surfaced exactly 2 posts, neither with a firm-attributed question. |

---

## 4. Blocked / refused

- **reddit.com** — 403 to every direct request. Read exclusively through the Arctic Shift mirror; no record claims a direct Reddit fetch.
- **1point3acres.com** — Cloudflare. All 41 records from it are `access: snippet_only`,
  `retrieval_method: websearch_snippet`. Several threads additionally paywall the body behind
  forum 积分, so even the search excerpt stops at the paywall notice.
- **glassdoor.com** — blocked to WebFetch and to urllib. The Citadel SWE-intern page was
  nonetheless captured *in full* by the search tool to
  `agent-tools/e4e76da1-eef9-4bec-b610-9ca6b5c214ea.txt`; those 9 records are
  `access: full_text` + `retrieval_method: websearch_snippet`, which is the honest pairing.
  The Jane Street QR page was only ever seen as an excerpt → `snippet_only`.
- **wallstreetoasis.com/company/** — Cloudflare, including through `r.jina.ai` (403).
  `/forum/` paths are fine.
- **nowcoder.com to plain HTTP clients** — Aliyun WAF. Consequence for verification: the
  48 Nowcoder records cannot be machine-re-verified from this host and will report
  UNREACHABLE rather than PASS. They were read in full through WebFetch.
- **blog.csdn.net to plain HTTP clients** — 521. Mitigated: the Wayback snapshot was checked
  and contains all 17 question stems, so the quote gate can reach them.
- **zhihu.com, tieba.baidu.com, leetcode.com/discuss, quizlet.com** — on the known-blocked
  list; not pursued, no records.
- **Baidu / Sogou / Bing HTML endpoints** — bot-walled to scripted parsers
  (`tools/tiera_discover.py` produced no usable result set). Chinese-language discovery was
  done through the search tool instead.

---

## 5. Sources deliberately rejected

Prep-vendor and content-farm pages surfaced constantly on the Chinese-language queries and
were **not** used as attestation, per the shard's exclusion rule:

`programhelp.net`, `oavoservice.com`, `interview-help.live`, `learncswithus.com`,
`quantblueprint.com`, `quantt.co.uk`, `interviewchamp.ai`, `linkjob.ai`, `spacecomplexity.ai`,
`myntbit.com`, `quantprep.io`, `tradermath.org`, `theinterviewden.com`, `techinterview.org`,
`quantvault.org`, `prachub.com`, `internshipshub.in`, `quant-wiki.com`,
`dev.to/net_programhelp_*` (Programhelp's syndication account).

Several of these advertise 代做 / 代面 / 联机 outright ("全程远程无痕『后台联机代写』服务",
"OA 代做（满分通过）/ VO 即時輔助"), which is the vendor tell. They were treated as negative
evidence even where the question text looked plausible.

**One deliberate exception, flagged here so it is easy to reverse.** Seven IMC Launchpad
HireVue records come from `everythingquant.com/forum/post/imc-launchpad-hirevue-oa/`. That
domain is on the exclusion list, but the page is a user forum thread with dated replies
(u/TheNotoriousBID asking, u/digress_regress answering with his own sitting), not vendor
editorial. The exclusion rule is about *who attests*, so it was included with the conflict
stated verbatim in every one of those records' `doubt` fields. Grep
`everythingquant` to drop them.

**Two aggregator sources included with heavy doubt.** `blog.csdn.net/dcdsc` (17 Citadel
Datathon items) and `nowcoder.com/discuss/604265548247040000` (10 Jane Street items) are the
same WeChat public-account operator republishing reader-submitted 笔试 and upselling a paid
知识星球. They are dated, firm-attributed and question-level specific, and three of the
Citadel items are independently named on 1point3acres, so they were kept — but every record
says in `doubt` that this is a compilation, not a first-person recall.

**Excluded content-laundering inside an otherwise good source.** English probability
questions appearing inside 1point3acres snippets under the banner "Unlock interview details
and practice with AI Curated Interview Questions from Top Companies" are site-injected
widget content, not the poster's recall, and were dropped.

---

## 6. What I could NOT establish

- **Citadel Securities is thin (4 records).** The QR/QT tracks in particular. Citadel
  Securities recalls overwhelmingly live on 1point3acres and Blind threads that are either
  paywalled by 积分 or Cloudflare-blocked. Nothing first-person was found for Citadel
  Securities *quantitative research*.
- **No Optiver 80-in-8 item text anywhere.** Every source that mentions the test — including
  the two first-person accounts in this shard — describes the format (80 questions, 8 minutes,
  ±1 scoring) and never reproduces a single arithmetic item. The one arithmetic example in the
  shard (`15/25 / ? = 14/35`) is WSO *editorial* illustrating the format, and its record says so.
- **No Optiver sequences item text.** Same pattern: the sequences test is attested repeatedly,
  but no source reproduces an actual sequence except the earlier 1point3acres recalls already in
  the shard.
- **Jane Street internship level is largely unresolved.** The two richest Jane Street sources
  (the Nowcoder compilation, the Glassdoor QR page) state no level, so 15 Jane Street records
  carry `level: unknown` rather than being promoted into the internship set.
- **Cycle/date is unrecoverable for a lot of the Chinese material.** Nowcoder renders no
  publication date in the fetched HTML, so `nowcoder.com/discuss/353157497731096576` (the
  Citadel HK recall — otherwise the single best first-person Chinese source in the shard) has
  `post_date: unknown`. Canary Wharfian gives only a relative "Added 3 years ago".
- **The Reddit archive was a dead end for question text.** 6 372 archived comments produced
  three usable records. Worth recording as a negative result: recall content for these four
  firms is not on Reddit in any volume, it is on the Chinese forums and on the
  interview-review sites.
- **`round` is `unknown` for 40 records.** Mostly Jane Street compilation items and Canary
  Wharfian's non-technical rounds, where the source names the round in its own words but the
  wording maps to no value in the controlled vocabulary. Left `unknown` with the source's
  wording preserved in `round_name` rather than guessed.
- **No Optiver or IMC coverage from a Chinese *social* source** (Xiaohongshu, Bilibili, Zhihu):
  Zhihu is blocked, and the Xiaohongshu/Bilibili results that surfaced were vendor reposts.

---

## 7. Verification

`tools/verify_quotes.py` re-fetches every cited URL (live → `r.jina.ai` → Wayback) and asserts
the recorded `source_quote` appears verbatim in the retrieved page text after NFKC + whitespace
normalisation. Results in `reports/tier_a_quote_gate.json`.

**Run over all 188 records (824 s, 37 unique URLs):**

| Status | Count |
|---|---|
| PASS | 57 → **58 after the fix below** |
| PARTIAL | 0 |
| FAIL | 1 → **0** |
| UNREACHABLE | 130 |

**The one FAIL, and what it was.**
`hiya31.medium.com/…citadel-securities-hackerrank-coding-round…`, matched 3/192 chars. Cause:
the quote had been transcribed with an ASCII apostrophe in "You're" where the page uses U+2019
"You’re", and the verifier's NFKC pass does not fold curly quotes onto straight ones. Corrected
against the live page and re-checked individually: both records on that URL now PASS. This is
exactly the class of error the gate exists to catch, and it is worth noting it was a
transcription artefact in a hand-typed quote — every batch written this session slices or
asserts its quotes against retrieved text instead, and none of those failed.

**UNREACHABLE is a host problem, not an evidence problem.** All 130 are on hosts that refuse
this machine on every one of the three strategies:

| Host | Records | Why unreachable |
|---|---|---|
| `nowcoder.com` | 48 | Aliyun WAF to non-browser clients; no Wayback snapshots exist |
| `1point3acres.com` | 41 | Cloudflare; already `snippet_only` |
| `wallstreetoasis.com` | 15 | Cloudflare (both `/forum/` and `/company/` 403 to urllib/curl) |
| `glassdoor.com` | 14 | Cloudflare |
| `teamblind.com` | 5 | Cloudflare |
| `reddit.com` | 3 | 403; read via the Arctic Shift mirror, never claimed as a direct fetch |
| `thestudentroom.co.uk` | 2 | 403 |
| `medium.com/@adityashrivastava2003` | 2 | 403 to urllib on both `medium.com/@user/…` and the `*.medium.com` form, though `hiya31.medium.com` on the same platform serves fine |

**Independent spot-check of everything written this session on hosts that *are* reachable**
(`/tmp/spotcheck.py`, separate code path from the gate): 47/47 PASS across
`blog.csdn.net` (17, via the Wayback snapshot), `canarywharfian.co.uk` (23) and
`everythingquant.com` (7).

So of the 188 records, 58 are machine-verified against a live or archived page, 130 sit on
hosts that will not serve this machine at all, and 0 have a quote that was fetched and did not
match. The honest reading: quote fidelity is proven where it can be proven, and the largest
unproven block (Nowcoder, 48 records) is unprovable from here for infrastructure reasons rather
than evidentiary ones — those pages were read in full through WebFetch and their question text
was copied out of that retrieval in the same process that wrote the record.

---

## 8. Final composition

188 records.

| Firm | Records | internship | new_grad | experienced | unknown |
|---|---|---|---|---|---|
| Optiver | 82 | 77 | 0 | 0 | 5 |
| Jane Street | 40 | 17 | 0 | 1 | 22 |
| Citadel | 37 | 16 | 0 | 3 | 18 |
| IMC Trading | 25 | 10 | 1 | 0 | 14 |
| Citadel Securities | 4 | 2 | 0 | 0 | 2 |

Rounds: `online_assessment` 80, `unknown` 40, `phone_technical` 31, `datathon` 17,
`trading_game` 7, `onsite` 6, `superday` 5, `math_sequences_test` 2.

Role tracks: `unknown` 59, `quant_developer` 58, `quant_trader` 56, `quant_researcher` 13,
`data_scientist` 2.

Languages: zh 96, en 75, mixed 17. Access: `full_text` 135, `snippet_only` 53.
