# Shard log — the chat layer, and deleted / archived recall

Output: `/workspace/harvest/raw/chat_and_archive.jsonl` — **344 records**.
All fetches were made from this machine on **2026-08-01**.

## Verification

Every `source_quote` in the JSONL is machine-checked against a stored local copy of the page
it came from. `tools/verify_all_chat.py` is an *independent* re-check: it re-derives the local
text for each `source_url` from scratch, without reusing any builder's parsing, and separately
enforces the field set and the controlled vocabularies.

```
records: 344
schema problems:   0
vocabulary problems: 0
no local copy of source: 0
QUOTE MISMATCHES:  0
```

`no local copy of source: 0` is the load-bearing line. It means there is no record whose
provenance could not be re-opened and re-checked — the verifier resolves every URL shape used
in the file (`t.me/<ch>/<id>` → the saved message HTML; `web.archive.org/.../1point3acres` →
the saved GB18030 snapshot; `1point3acres.com` and `nowcoder.com` → either a saved snapshot or
the verbatim WebSearch-highlight capture; `reddit.com` → the Arctic Shift mirror snapshot) and
reports anything it cannot resolve as a failure rather than skipping it.

## 1. What was collected

| source_type | records |
|---|---|
| `chat_telegram` | 217 |
| `other` (1point3acres threads, via Wayback or cached extract) | 69 |
| `nowcoder` | 30 |
| `reddit_thread` (via the Arctic Shift mirror) | 25 |
| `chat_wechat_repost` | 3 |
| **total** | **344** |

| access | records |
|---|---|
| `full_text` | 220 |
| `snippet_only` | 65 |
| `archive_only` | 59 |

By firm: Optiver 102, SIG 42, Citadel 34, HRT 33, Jane Street 31, Jump Trading 22,
Two Sigma 20, Akuna 11, Morgan Stanley 11, D. E. Shaw 7, IMC 6, DRW 5, Five Rings 4,
WorldQuant 3, Kronos Research 3, plus single records for Belvedere, Eclipse Trading, CTC and
four unidentified Chinese firms.

202 distinct source URLs.

**62 of the 344 records are not question statements**, and each says so in its `doubt` field:
they are `assessment_format` datapoints, `solution_discussion_only` replies, `coding_requirement`
and `coding_io_spec` fragments, and `answer_key_fragment_only` scraps recovered from posts
whose question text was behind a karma wall or in an unarchived image. They are kept under the
do-not-over-filter rule and typed so a consumer can drop them in one pass. The remaining 282
records state a question.

---

## 2. Job 1 — the chat layer

### 2.1 Telegram — the productive channel

`https://t.me/s/<channel>` works from this machine with no account, and its `?q=` parameter
searches a channel's history. **31 candidate handles probed; 6 readable; 2 productive; 25
blocked.**

- **`@usinterview` (北美跳槽面经) — 190 records, the largest single source in the shard.**
  It auto-reposts every new thread from the 1point3acres 海外面经 board together with the
  forum's own link preview, and that preview carries the opening of the post body. Because
  1point3acres Cloudflare-blocks this machine, *the Telegram repost is the only readable copy
  of most of these posts.*
  A pagination bug cost most of the channel's history on the first pass: Telegram only honours
  `before=` when it precedes `q=` in the query string, so every search was silently returning
  the same first page of 22 results. After fixing the parameter order in `tools/tg_paginate.py`
  the sweep reached message id 29153 and 184 distinct messages, which is where the second half
  of the Telegram records came from.
- **`@aistockanalyst` — 30 records.** A Chinese-language finance channel that reposts group
  chat dumps. Message 1288 is a speaker-tagged (`【Alice】` / `【Bob】`) transcript — a QQ/WeChat
  群 conversation pasted onward — which is why those records carry
  `source_type: chat_wechat_repost` and an `upstream_source` noting the chat itself was
  unreadable.

Readable but carrying no target-firm assessment content (probed, read, discarded):
`@QuantQuestions` (Indian aptitude quiz channel), `@quantitativefinance` (Persian-language),
`@quantoa` (2 messages, empty), `@usaoa` (2 messages, empty), `@interviewquestions`
("Interview Questions .Net").

### 2.2 Discord — blocked in full, zero records

**No Discord message content was readable and no Discord record appears in the JSONL.**
Discord publishes no anonymous web view of channel history. The only endpoints reachable
without an account are the guild widget (`/api/v10/guilds/<id>/widget.json`) and invite
metadata (`/api/v10/invites/<code>`), and **neither returns messages** — this was verified
rather than assumed, on 11 servers found through Reddit-posted invites and directory listings.

Three widgets were actually enabled, which is the strongest form of the negative result: even
with the widget on, the JSON contains only `channels`, `members`, `presence_count`,
`instant_invite` and `name`. There is no `messages` key. QuantQuestionsIO's enabled widget
exposes exactly one channel name ("General") and 100 online usernames.

I searched specifically for the thing the brief hoped for — servers publishing web-visible
transcripts or public recruiting-season recap channels. **I found none.** The only hits were
Discord's own data-export documentation and its engineering blog.

### 2.3 QQ 群 / WeChat 群 spillover — mostly blocked, one large win

Direct reading of QQ/WeChat groups is impossible, as expected. Hunting the spillover on the
public Chinese web hit a block on nearly every platform named in the brief (see the register),
but two routes produced records:

- **Nowcoder, via cached extract — 30 records.** `nowcoder.com` sits behind an Aliyun WAF
  (`www`, `m.` and the `/discuss/` form all return the
  `为了更好的访问体验，请进行验证` interstitial; `m.nowcoder.com` returns the page title and
  nothing else). The post
  [985废柴挑战顶级量化optiver笔试](https://www.nowcoder.com/feed/main/detail/3d62edffa9dc40c883d3d019dd7f6789)
  is a module-by-module write-up of the **Optiver Shanghai Software Developer summer
  internship OA**: two HackerRank class-design questions, twenty CS-fundamentals
  multiple-answer items listed one by one, and nine mini-games of which seven are described by
  name and mechanic. The search engine's cached extract is the only copy this machine can
  read, so all 30 are `snippet_only` and quote
  `raw/pages/websearch_highlights_batch2.txt` verbatim.
- **The `@aistockanalyst` Telegram repost of a pasted group chat** (§2.1), 3 records.

### 2.4 Slack — nothing found

No publicly archived Slack workspace carrying quant assessment recall was located. A null
result, not a block.

---

## 3. Job 2 — deleted and archived recall

### 3.1 Reddit — the removal pattern, measured

`reddit.com` returns 403 to this machine throughout, so everything went through
`web.archive.org` and the Arctic Shift mirror (`arctic-shift.photon-reddit.com`, reachable but
rate-limiting).

**The central negative finding, now quantified.** r/quant and r/quantfinance route OA traffic
into weekly megathreads and automod-remove standalone recall threads. `tools/arctic_removed.py`
swept 8 subreddits × 14 firm keywords and kept every post whose body survived in the mirror:
**1,878 posts, of which only 96 were actually removed on reddit** (92 `automod_filtered`, 3
`deleted`, 1 `reddit`). Scanning those 96 for question text
(`tools/removed_qscan.py`) matched 8, and reading all 8 found **zero assessment questions** —
they are compensation, culture and firm-comparison threads that tripped a filter.

The same holds for the archive side. Eight Reddit threads whose *titles* read as recall were
fetched from the Wayback Machine; in every case the snapshot post-dates the removal and
preserves the removal notice rather than the post:

| thread | snapshot | what the archive contains |
|---|---|---|
| r/quantfinance `1gqef21` "SIG quant interview problem" | 2025-07-26 (×2) | "Sorry, this post was deleted by the person who originally posted it." Mirror `selftext` empty |
| r/quant `144mmv3` "The SIG Problem Solving Assessment" | 2023-06-08 | `[removed]`, awaiting moderator approval |
| r/quant `18ew6eq` "SIG problem solving test." | 2025-01-19 | automod megathread notice only |
| r/quant `16kgyzc` "Akuna OA for quant research intern" | 2023-09-16 | `[removed]` by moderators |
| r/quant `1glb5y2` "Susquehanna OA for quant position what to expect?" | 2025-03-10 | megathread notice |
| r/quant `1gk9j5j` "DRW 45 minute assessment for Quant Trading Analyst" | 2025-03-21 and 2025-03-27 | automod notice in both |
| r/quantfinance `1f0vq12` "Jane Street Quant Interview Question - Modified Even Coins" | 2025-08-06 | body is an image; top reply is a quantquestions.io advert |
| r/quantfinance `1gc8shm` "Citadel Live Mathematical Assessment Intern HELP" | 2024-12-08 | body intact but it is a request for advice, not recall |

**Deleted-and-recovered posts containing question text: 0.** What the mirror *did* yield is 25
records from posts that are live but unreachable from here — Optiver's five-test QR intern
battery, the Five Rings QT intern OA format, a shrinkage question attributed to
Citadel/Two Sigma/Tower/Arrowstreet, Akuna's EasyHire and C++ round-1 structure, IMC's Spark
Hire video assessment. Those are `archive_only` because the mirror, not reddit, is the source.

**A contamination finding worth recording.** A 260-thread comment sweep
(`tools/arctic_threadcmts2.py`) pulled ~2,100 replies. Of the 17 that matched on question-like
phrasing, **15 were AI-written advice replies from accounts marketing interviews.chat,
QuantGrind or Beyz** — same structure every time, two paragraphs of generic topic advice
closing on a product link; one even ends with the string `test injection`. They were rejected
under the prep-vendor exclusion. Only 2 comments survived, both format descriptions rather
than questions, both flagged accordingly. Recall in these subreddits is now substantially
synthetic, which matters for anyone mining them.

### 3.2 1point3acres — 69 records across two access routes

`1point3acres.com` is Cloudflare-blocked to this machine; a direct fetch and the `r.jina.ai`
text proxy both return the "Performing security verification" interstitial. Two routes worked.

**Wayback (47 records, `archive_only`).** A CDX sweep produced 153,275 archived
`thread-*-1-1.html` URLs; 31 target-firm threads were fetched with backoff and decoded from
GB18030 — decoding them as UTF-8 turns every Chinese run to mojibake, which silently corrupted
an early batch until it was caught.

The best single find is
[thread 1144112, "2026 SIG Quant Research OA整理 【带答案】"](https://web.archive.org/web/20250912084409/https://www.1point3acres.com/bbs/thread-1144112-1-1.html),
which reproduces eight SIG Quant Research OA questions **in the assessment's own English
wording** with the poster's answers — questions 1–6 and 16–17 of a stated 17-question,
60-minute paper. Questions 1, 2 and 4 match fragments different candidates posted to Telegram
in 2024 and 2025.

**Cached search extract (22 records, `snippet_only`).** Six threads have no Wayback snapshot
at all, and by the time the last two were checked archive.org had escalated from HTTP 503 to
HTTP 429 on every `wayback/available` call, so no lookup was possible. Their extracts are
preserved verbatim in `raw/pages/websearch_highlights_1p3a.txt`, `..._batch2.txt` and
`..._batch3.txt`, and every quote is checked against those files.

Two structural caveats apply to all 69 and are repeated in their `doubt` fields:

- **The 188-karma wall.** 1point3acres hides most of each recall post behind
  `本帖隐藏的内容需要积分高于 188 才可浏览`. Snapshots preserve the wall, not the content. In
  thread 1144112 the wall falls between questions 6 and 15, which is exactly why 1–6 and 16–17
  survived. In thread 1118978 it cuts in mid-question, leaving a SIG QR phone question
  truncated at `X is uniformly [0,` — recorded as evidence that the question exists and that
  its answer is contested (2/3 versus 3/4), explicitly not as a usable question.
- **Image attachments are not archived.** Several questions exist only as images the snapshot
  did not capture. No `screenshot_only` record was created for any of them, because I did not
  see them.

### 3.3 Cross-source corroboration

Three findings are attested by independent sources, which is the strongest signal available
here:

- Optiver's **NewsProvider** OA coding question — the English problem statement on 1point3acres
  thread 1147508, and independently a Nowcoder poster listing a `newsProvider` class with
  `AddSubscription` / `RemoveSubscription` / `NewsReceived` as their first HackerRank question
  in the Shanghai SWE intern OA.
- SIG's **circle-cutting expectation** question — 1point3acres thread 686183 (2020, 海外面经
  board) and thread 1042392 (2024, 数科 board), four years and two boards apart, reaching the
  same answer.
- SIG OA questions 1, 2 and 4 from thread 1144112 matching Telegram fragments from 2024–25.

---

## 4. BLOCKED REGISTER

Everything below was identified as existing and could **not** be read. **62 entries.**

### 4.1 Discord — 11 servers, 3 directory URLs (14)

| # | server | guild / invite | probe result | reason blocked |
|---|---|---|---|---|
| 1 | QuantQuestionsIO | `1215463613519634482`, ~5,403 members | widget **200** — `channels: ["General"]`, 275 online, **no `messages` key** | reading requires joining. Also **vendor-run** (quantquestions.io) |
| 2 | Quant Data | `701257937209000066`, ~20,507 members | widget **200** — `channels: []`, 1,849 online, no messages | no channels exposed; options-flow server, not recall |
| 3 | BLOCKWISE | `786425018485571624` | widget **200** — `channels: []`, 38 online, no messages | no channels exposed |
| 4 | Quant Talk | `823943906008891403` | widget **403** `{"message":"Widget Disabled","code":50004}` | membership required |
| 5 | The Exchange Society | `1406740892378730536` | widget **403** Widget Disabled | membership required; self-described "exclusive" |
| 6 | Quant Trading App | `753977356867076116` | widget **403** Widget Disabled | membership required |
| 7 | QUANT IMPERIUM | `1313754273028374578` | widget **403** Widget Disabled | membership required; algo-trading vendor |
| 8 | Tech Interview Prep | `1194088363297353738`, ~23,961 members | invite 200, widget **403** Widget Disabled | membership required |
| 9 | Figgie Game Server | `1375186666473390221`, 55 members | invite 200, widget **403** Widget Disabled | membership required |
| 10 | Yale Undergraduate Trading Competition | `1447480707609006220`, 244 members | invite 200, widget **403** Widget Disabled | membership required — the university quant-club case the brief names |
| 11 | SolveFire Official | `1467337163694805167`, 433 members | invite 200, widget **403** Widget Disabled | membership required |
| 12 | QuantVault prep server | invite `quantvault-prep` | **404 Unknown Invite** | dead invite, advertised on quantvault.org |
| 13 | Mathematical Finance / QuantNet study group | invite `SPYUnKJecw`, and `CYaAWFHvWU`, `MH49bXWSxV`, `zDcS7Gdy` from Reddit threads | **404 "Invite is expired." / "Unknown Invite"** | dead invites |
| 14 | `disboard.org/servers/tag/quant`, `.../quant-finance`, `discord.com/servers/quant-talk-823943906008891403` | **403 Cloudflare** ×2; 200 but blurb + channel names only ×1 | directories unreadable or messageless |

### 4.2 Telegram — 25 channels (15–39)

All return HTTP 200 at `t.me/s/<handle>` with **zero message elements**, meaning private,
a user account, or unregistered. Not joinable under the rules of this task:

`@quantjobs`, `@quantjob`, `@quant_interview`, `@quantinterview`, `@mianjing`,
`@beimeimianjing`, `@naoffer`, `@offershow`, `@oa_share`, `@cs_interview`, `@leetcode`,
`@QuantFinanceJobs`, `@quantfinancejobs`, `@quant_finance`, `@hedgefundjobs`, `@quantnews`,
`@tradinginterview`, `@BayAreaJobs`, `@uscareers`, `@nacs`, `@NAmianjing`, `@codetop`,
`@oneacre`, `@diliOffer`, `@1point3acres`.

### 4.3 QQ / WeChat spillover platforms — 7 (40–46)

| # | platform | probe | result |
|---|---|---|---|
| 40 | `tieba.baidu.com/f/search/res?qw=Optiver 笔试` | GET | **403** bot-blocked |
| 41 | `zhihu.com/search?q=SIG OA` | GET | **403** bot-blocked |
| 42 | `nowcoder.com` (`www`, `m.`, `/discuss/`, `/feed/main/detail/`) | GET ×5 | **200 carrying an Aliyun WAF challenge** — `aliyun_waf_aa`/`aliyun_waf_bb` meta tags, sceneId `19x5u7lo`, body `为了更好的访问体验，请进行验证`. `m.` returns the title only. Worked around via cached extract (§2.3) |
| 43 | `xiaohongshu.com/search_result?keyword=SIG面经` | GET | **200, 724 KB**, but a client-side shell — `__INITIAL_STATE__` holds no note data, `noteCard` count 0 |
| 44 | `douban.com/search?q=SIG 面经` | GET | **200**, renders, **zero results** to a logged-out client |
| 45 | `yuque.com/explore/search?q=量化 面经` | GET | **404** — search endpoint not public |
| 46 | QQ 群 / WeChat 群 themselves | — | not readable by any public URL; no group was joined. Only spillover was pursued |

### 4.4 Archived URLs with no usable snapshot — 16 (47–62)

**Reddit (8, entries 47–54)** — the eight threads tabulated in §3.1. Every snapshot
post-dates the removal, so the archive holds the removal notice rather than the recall. This
includes `1gqef21` and `144mmv3`, both SIG, the highest-priority firm in the brief.

**1point3acres (8, entries 55–62)** — threads fetched from the archive whose content is wholly
behind the karma wall, or whose snapshot captured a Discuz error page instead of the thread:

| thread | title | state |
|---|---|---|
| `1112822` | Optiver OA (tagged citadel) | 200-karma wall, nothing above it |
| `1114677` | Akuna Quantitative Researcher 挂经 | wall after "新加坡的岗位 第一面直接和APAC Head" |
| `1118118` | 求米\|Optiver OA | wall immediately after the edit stamp |
| `1139954` | Akuna Shanghai C++ Developer | wall only |
| `1002184` | sig virtual onset | wall after one English sentence |
| `1091467` | SIG：HR面->终面所有面经+总结的历年面经 | all questions are in a **login-gated file attachment**; only the OA-format line survives |
| `1040027` | (SIG) | archive captured 提示信息 — a Discuz error page |
| `1136455` | Optiver OA 2026 | archive captured 提示信息 — error page |

**Threads with no snapshot at all** (read only as cached extract, not counted again above
since they did produce records): `686183`, `1042392`, `1118978`, `1147508`, `1141422`,
`1019756`, `473191`, `1149543`. For `686183`, `archive.org/wayback/available` returned
`{"archived_snapshots": {}}` on three spaced attempts and the CDX endpoint returned **503**;
for `1042392`, `1118978` and the two Jane Street threads, archive.org returned **429 "You have
sent too many requests"** on every attempt.

### 4.5 Other standing blocks

- `reddit.com` direct fetch — **403** from this machine throughout; all Reddit content came
  from the Arctic Shift mirror or the Wayback Machine.
- `1point3acres.com` direct fetch — **Cloudflare**; the `r.jina.ai` text proxy is blocked too.
- `glassdoor.com` — **Cloudflare**. Relevant because one DRW candidate describes their
  take-home only as "the one on Glassdoor" (record retained, content unrecovered).
- `archive.org` — reachable but **rate-limiting hard**, escalating 503 → 429 over the session.
  Every fetch is paced with backoff; several lookups were abandoned rather than hammered.
- Image attachments across all sources — the SIG balance-puzzle diagram (thread 1144112 Q4),
  the SIG SDE grid problems (thread 1090786), the Jump debugging screenshot
  (`t.me/usinterview/25780`). Present in the source, absent from the archive. **No
  `screenshot_only` record was created for any of them, because I did not see them.**

---

## 5. Rejected on the hard-exclusion list

Read and discarded, nothing taken into the output: `programhelp.net` (many SIG / Optiver /
Jane Street / Two Sigma "真题解析" pages, plus its `dev.to/programhelp-cs` reposts),
`jishuzhan.net`, `attcareer.com`, `linkjob.ai`, `prachub.com`, `oavoservice.com`,
`quantblueprint.com`, `quantt.co.uk`, `dataford.io`, `everythingquant.com`,
`quantquestions.io`, `quantprof.org`, `quantprep.io`, `tradermath.org`, `myntbit.com`,
`interviews.chat`, `quantable.io`.

Three patterns are worth naming because they are dressed as recall:

1. **OA-proxy vendors.** programhelp.net and oavoservice.com publish long, plausible 面经
   write-ups that terminate in an advert for a paid OA-cheating service
   (`OA无痕联机代写：通过远程控制实现无痕操作`). Highest-risk contamination in this space.
2. **The Reddit image cluster.** A run of 39 image posts of "quant interview questions" turned
   out to trace to a handful of accounts marketing quantprof.org, quantprep.io and
   tradermath.org. Rejected as marketing. One image — a SIG balance puzzle — was kept
   *only* because the same problem is independently attested by a Telegram record, and its
   `doubt` field says the image itself is a vendor reproduction.
3. **AI-generated advice replies** (§3.1), the newest and least obvious of the three.

---

## 6. Query and URL log

**Telegram.** `t.me/s/usinterview?q=` for SIG, Jane Street, Citadel, Optiver, IMC, HRT, Hudson
River, Jump Trading, DRW, D.E. Shaw, Five Rings, Akuna, Two Sigma, XTX, Tower Research, Old
Mission, Virtu, Radix, quant, 量化, 笔试 — then deep `before=`/`q=` pagination back to message
id 29153 (`tools/tg_paginate.py`), 184 distinct messages held, followed by
`t.me/usinterview/<id>?embed=1` for each message quoted. `t.me/s/aistockanalyst?q=` for 笔试,
量化, 面经. 31 handles probed with `tools/tg_probe.py`.

**Discord.** `discord.com/api/v10/guilds/<id>/widget.json` × 11;
`discord.com/api/v10/invites/<code>?with_counts=true` × 11; `disboard.org` × 2;
`discord.com/servers/...` × 1. Invite codes were harvested from Reddit thread bodies in the
mirror rather than guessed.

**Wayback.** CDX sweep of `1point3acres.com/bbs/thread-*` (200,000 rows scanned, 153,275 with
HTTP 200); 31 distinct target-firm threads fetched. CDX + snapshot fetch for 8 Reddit thread slugs.
`archive.org/wayback/available` for `686183`, `1042392`, `1118978`, `1147508` with escalating
backoff — all failed (see §4.4).

**Arctic Shift.** `posts/search` across 8 subreddits × 14 firm keywords (1,878 posts with
intact bodies kept); `comments/search?link_id=` for 141 + 260 named recall threads (~4,000
comments); free-text `comments/search` across r/quant and r/quantfinance × 31 query strings.

**Chinese platforms.** Direct fetches against tieba, zhihu, nowcoder (5 URL forms),
xiaohongshu, douban and yuque as tabulated in §4.3.

**Web searches.** Discovery, and — for the Cloudflare/WAF-blocked pages only — verbatim
"Highlights" capture: `quant trading interview discord server invite`;
`telegram channel quant interview 面经 OA t.me 量化 笔试`;
`site:disboard.org quant trading interview server`;
`discord message archive transcript SIG Optiver online assessment`;
`reddit "discord.gg" quant interview prep server invite`;
`SIG 笔试 面经 真题 群 分享 概率题`; `牛客网 Optiver 笔试 面经 真题 数字推理`;
`牛客网 optiver 笔试 newsProvider AddSubscription RemoveSubscription NewsReceived 卫星`;
`1point3acres SIG 1轮+2轮面经 圆里随机画n条线 扔硬币 HTH HHT`;
`量化 面经 微信群 截图 Jane Street 笔试 真题 分享 知乎专栏`;
`语雀 yuque 量化 面经 汇总 Citadel Optiver Jane Street 真题`;
`贴吧 OR 豆瓣 SIG Susquehanna 笔试 面经 真题 群 转发`;
`小红书 Optiver 笔试 真题 量化 面经 截图 xiaohongshu`.

**Evidence files.** Verbatim highlight captures live at
`raw/pages/websearch_highlights_1p3a.txt`, `raw/pages/websearch_highlights_batch2.txt` and
`raw/pages/websearch_highlights_batch3.txt`; Wayback snapshots at `raw/pages/wayback/`;
Telegram message pages at `raw/pages/tgmsg/` and `raw/pages/tgmsg2/`; the Arctic Shift
snapshot at `raw/pages/arctic/`; Discord probe JSON at `raw/pages/discord*/`. Every
`source_quote` resolves into one of these.
