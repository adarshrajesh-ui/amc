# Harvest log — SIG (+ peer quant firms) on the Chinese social / video / BBS layer

Output: `/workspace/harvest/raw/sig_chinese_social.jsonl` — **62 records**, 15 SIG + 47 Optiver,
drawn from **12 distinct source threads/indexes on 3 Chinese BBS platforms**.

Nothing in the JSONL was written from memory. Every `question_text` was read either out of HTML I
fetched in this session or out of a search-engine verbatim-highlight block quoting a URL I can name.
Where I saw only a fragment I said so in `doubt` rather than completing the stem.

Delivered in two passes. Pass 1 produced 40 records; pass 2 added 22 more from three Optiver threads
that **no sibling shard covers** (§9). Pass 2 also closed out two open questions from pass 1: the real
水木社区 board names, and whether Xiaohongshu is reachable at all (§10).

---

## 1. Headline outcome

| | |
|---|---|
| Records | 62 |
| Firms | SIG 15, Optiver 47 |
| Distinct source URLs | 12 |
| Platforms that actually yielded questions | 一亩三分地 (1point3acres) 30+3+2, 牛客网 (Nowcoder) 21, 交大门 (xjtu.app) 6 |
| Platforms that yielded **nothing** | 小红书, 知乎, Bilibili, 微博, 抖音, 百度贴吧, 豆瓣, 水木社区, V2EX, 虎扑, 小木虫 |
| Byte-verified (`full_text` / `webfetch`) | 31 |
| Search-highlight only (`snippet_only`) | 31 |
| Screenshot-transcribed | 0 (see §6) |

The single most important structural finding: **the 17-questions-in-60-minutes prior is confirmed by a
genuine candidate recall**, not just by vendors. See §4.

---

## 2. Network reality — what I actually established

I found that the **shell has unrestricted outbound network access**, which changed the whole approach:
instead of relying only on search snippets I could curl sites directly and scrape search engines myself.

### Directly fetched, status and outcome

| Host | HTTP | Usable? | Notes |
|---|---|---|---|
| `www.nowcoder.com` | 200 | **YES — best source found** | Server-renders full post text into `window.__INITIAL_STATE__`. Author, exact epoch-ms timestamp, view count all machine-readable. Occasionally returns an empty JS shell; retry 2–3× and the SSR payload appears. |
| `xjtu.app` (交大门, XJTU BBS) | 200 | **YES** | Discourse-style, full thread HTML, no login wall. `/t/topic/N.json` 404s but `/t/topic/N` works. |
| `web.archive.org` | 200 | **YES (slow)** | The only way into 1point3acres. Snapshot served as **GB18030**, not the declared UTF-8 — decoding as UTF-8 fails and as GBK fails; `gb18030` works. CDX API took 82 s per query. |
| `www.xiaohongshu.com` | 200 | **NO** | `/search_result` returns 724 KB but the `__INITIAL_STATE__` search object is `"feeds":[]` — results load via a signed (`x-s`) API. `edith.xiaohongshu.com/api/sns/web/v1/search/notes` → 404. |
| `api.bilibili.com` | 200 | **YES, but empty** | Implemented WBI signing (nav → img/sub key → mixin-key permutation → md5). Verified working: `量化` returns 20 results, `numResults` 1000. But `SIG 面经`, `SIG OA`, `SIG 量化`, `Susquehanna`, `SIG 笔试`, `量化 OA`, `量化 笔试`, `quant 面经`, `对冲基金 面试`, `Jane Street`, `IMC 量化` **all return 0 results**. Bilibili genuinely has no SIG interview content. |
| `www.newsmth.net` | 200 | **NO content** | Site alive (169 000 users online) and GBK-encoded, but every job-board name I probed (`Job`, `JobInfo`, `Intern`, `WorkLife`, `Career`, `Employment`, `Quant`, `Finance`) returned 指定的版面不存在. Banner says the domain moved to `www.mysmth.net`; that host serves a redirect placeholder, and its `slist.json` returns an HTML shell, not JSON. I could not enumerate its board list and therefore **could not establish whether 水木 has SIG content at all**. |
| `www.douban.com/group/search` | 200 | **YES to fetch, nothing relevant** | Search for 量化面经 returns only law-firm 面经 (金杜, 君合, 汉坤) from 「Women in Law」. No quant content. |
| `www.v2ex.com`, `muchong.com` | 200 | not mined | Deprioritised after Douban showed the general-forum layer is barren for this topic. |
| `zhuanlan.zhihu.com`, `www.zhihu.com` | **403** | **NO** | Confirmed hard-blocked on every route I tried: desktop UA, iPhone UA, `www.zhihu.com/api/v4/articles/<id>` (`code 10003 请求参数异常`), `api.zhihu.com/articles/<id>` (`code 40362 您当前请求存在异常`), `r.jina.ai` proxy (returns "Target URL returned error 403"), `api.allorigins.win` (520). |
| `www.1point3acres.com` | **403** | **NO (direct)** | Reachable only via Wayback + search highlights. |
| `tieba.baidu.com` | **403** | **NO** | Also `tieba.baidu.com/f/search/res` and `tiebac.baidu.com` → 403. |
| `s.weibo.com` | 302 | **NO** | `weibo.com` itself: `Recv failure: Connection reset by peer`. |
| `mbd.baidu.com` (Baidu's article aggregator) | 200 | **NO** | Returns 百度安全验证 网络不给力 to both desktop and mobile UA. |

### Search engines I scraped from the shell

| Engine | Verdict |
|---|---|
| **Baidu** (`www.baidu.com/s`) | Best Chinese-content recall. Results embedded in JSON blobs; I wrote a parser plus a `baidu.com/link?url=` redirect resolver. Rate-limits after a few queries (later runs returned 0). |
| **Sogou** | Works, surfaced 微信公众号 and 今日头条 mirrors of quant 面经. |
| **DuckDuckGo HTML** | Works reliably, ~10 results/query. Found most of the 1point3acres threads. |
| **Bing HTML** (`cn.bing.com`) | JS shell only, 0 parseable results. |
| **Bing RSS** (`?format=rss`) | Parses fine but **silently ignores `site:`** and drifts to SIG Sauer firearms / MercadoLibre. Useless here. |

---

## 3. Every query run

### Cursor WebSearch tool (10)
1. `SIG 面经 小红书 量化 笔试`
2. `site:zhihu.com SIG Susquehanna 面试 面经 量化`
3. `SIG 笔试 17道题 60分钟 面经`
4. `site:xiaohongshu.com SIG 面经 量化`
5. `site:bilibili.com SIG 量化 OA 笔试`
6. `"2026 SIG Quant Research OA整理" 一亩三分地 带答案 Question`
7. `面经 SIG QR岗位OA面 知乎 九道固定的题目 贝叶斯 绿色三角形的重量`
8. `1point3acres SIG Quant Research OA 带答案 "Question 10" "Question 11" "Question 12" frog A(0,0) B(5,6)`
9. `小红书 SIG面试全记 细节攻略 OA 1小时 17道题`
10. `1point3acres "SIG" OA 带答案 "Question 8" "Question 9" "Question 13" "Question 14" 答案`
11. `小红书 SIG 量化 面经 笔记 #sig面试 #量化求职 OA 题目`
12. `"SIG面试全记" 细节攻略 在线评估 1小时内要完成17道题`
13. `知乎 SIG Quant Trader 面经 面试题 期望 概率 扑克 zhuanlan`
14. `知乎 近期量化机构面试 笔试题 zhuanlan 498681895 题目 猪 左上角 路径 答案`
15. `xiaohongshu.com 小红书 笔记 SIG Susquehanna 面试 OA 题 概率 心得 捕手`
16. `知乎 面经 SIG QT/QR岗位HR面 今日头条 Susquehanna 题目 具体`
17. `1point3acres 公司 sig tag 海外面经 SIG QR OA 题目 期望 概率 驰马 平均值 compute`

### Shell-scraped engines (each run against DDG + Sogou unless noted)
Batch 1 (`SIG 面经 量化 笔试` — run against Bing, Baidu, Sogou, DDG separately) — 4 queries.

Batch 2 (10 × 2 engines = 20 queries):
`SIG OA 17道题 面经 知乎` · `SIG 量化 实习 面经 小红书` · `SIG Susquehanna 笔试 真题 知乎` ·
`SIG 面经 水木社区` · `SIG 笔试 贴吧 量化` · `SIG 量化交易员 面经 2026届` · `SIG OA 真题 概率 面经` ·
`Susquehanna 面经 知乎 量化研究员` · `SIG 暑期实习 面经 量化` · `SIG 网测 题目 面经`

Batch 3 (5 × 2 = 10 queries):
`SIG面试全记 细节攻略 小红书` · `SIG QR面试全攻略 从初试到终审` · `SIG Quant面试攻略 速看 马尔可夫过程` ·
`xiaohongshu.com/explore SIG 量化 面经` · `小红书 SIG 面经 explore`

Batch 4 (10 queries, DDG):
`Optiver 80in8 笔试 面经 知乎` · `IMC 笔试 面经 知乎 量化` · `简街 Jane Street 面经 知乎 概率题` ·
`Citadel 城堡 面经 量化 笔试题` · `HRT 面经 知乎 笔试` · `Jump Trading 面经 知乎` ·
`site:newsmth.net 面经 量化` · `水木社区 面经 对冲基金 笔试` · `豆瓣小组 量化 面经 笔试题` · `v2ex 量化 面试 概率题`

Baidu with link resolution: `SIG 面经 量化 OA`; `SIG 面经 小红书 量化 OA 题`.

Bing RSS (5): `site:xiaohongshu.com SIG 面经` · `site:xiaohongshu.com 量化 面经 OA` ·
`site:zhihu.com SIG OA 面经` · `site:newsmth.net 面经` · `site:tieba.baidu.com 量化 笔试`

### Bilibili WBI search API (21 keywords, all Chinese/mixed)
`SIG 面经` · `SIG OA` · `SIG OA 量化` · `SIG 量化` · `SIG 笔试` · `Susquehanna` · `Susquehanna 面试` ·
`量化 面经 OA` · `量化面试题` · `量化 OA` · `量化 笔试` · `量化 笔试 真题` · `quant 面经` · `对冲基金 面试` ·
`Optiver` · `Optiver 面试` · `Jane Street` · `Jane Street 面试` · `简街` · `简街 面经` · `IMC 面试` · `IMC 量化` · `量化`

### Nowcoder search (11)
`SIG OA` · `SIG 量化 面经` · `SIG 笔试 量化` · `SIG quant` · `Susquehanna` · `Optiver 面经` ·
`Optiver OA` · `IMC 面经` · `Jane Street 面经` · `对冲基金 OA` · `量化 OA 面经`

**Total distinct queries: well over 110** (pass-1 queries above; pass-2 queries in §12).

---

## 4. The 17-in-60 consistency prior — result

**CONFIRMED by a genuine candidate recall, not just vendors.**

`1point3acres` thread-1144112, poster **IanZ**, 2025-09-04, tag line
`2025(7-9月) 金工类 硕士 全职 @ sig - 网上海投 - 技术电面 | Pass | 应届毕业生`:

> SIG 的OA万年不变，1小时17个题，已经做了好几次了。前9个偏简单，后面8个偏难。

("SIG's OA never changes: 1 hour, 17 questions, I've done it several times now. The first 9 are on the
easier side, the last 8 harder.") Read byte-for-byte out of Wayback snapshot `20250912084409`.

Three further 1point3acres thread titles corroborate the count independently:
`SIG QR 17题OA` (thread-1082367), `SIG QR OA 2024 秋 17题` (thread-1084760, poster: 刚做完，大部分题目
只是改了数字，题不难但是太多了，只有一小时，没有做完), `SIG Quant OA面经` (thread-1084480: SIG Quant 17题面经).

**One genuine contradiction, and I believe it is real rather than error.** 1point3acres thread-719224,
titled `SIG Quantitative Evaluation 2021. OA 2021-02最新`:

> 刚刚结束的sig（一家对冲基金）的quantitative developer 笔试！总时长20分钟，一共是16道题。

16 questions in 20 minutes. But note: different *test name* (Quantitative Evaluation, the older short
test, vs Problem Solving Assessment), different *role track* (quantitative developer, not QR), and
four years earlier. This looks like a genuine older/other product, not a bad recall. Recorded in the
JSONL with that reasoning in `doubt`.

---

## 5. Sources REJECTED as prep-vendor / content-farm

All of these carry SIG "面经" and some print plausible question text, but every one ends in a sales
pitch for 辅导 / 远程助攻 / 无痕联机 / 代面 / VIP题库. Excluded per the rules; listed so the exclusion is auditable.

- `programhelp.net` — multiple pages. Sells 语音实时助攻 / 远程联机陪练 / 无痕联机 OA 辅助. **Notable:** its
  page states 1小时，17道题 and prints a "Question 1" (barn / spiders / 520 legs) **identical** to the genuine
  1point3acres recall, plus Q3, Q4 (green triangle, 96 lbs), Q5 (Factory A/B widgets), Q6 (three dice
  $20/$10/−$2). Its own other page contradicts itself with "9 道题 / 60 分钟". I used it only as a
  cross-check, never as attestation; the barn question is in the JSONL sourced to 1point3acres.
- `jishuzhan.net` + its CSDN mirror `blog.csdn.net/2611_95078937` — same operator; "2026 亲身经历分享" framing
  but the CSDN profile advertises 一对一面试辅助.
- `interview-help.live` — title literally reads 面试代面 面试代做 面试辅导 oa/vo作弊.
- `csoahelp.com`, `attcareer.com`, `mianlingai.com`, `hwds868.com`, `zhitongguigu.com`, `bk.taobao.com`.
- English-language vendors encountered and excluded: `tradermath.org`, `tradinginterview.com`,
  `jobtestprep.com` / `.co.uk`, `quantt.co.uk`, `quantblueprint.com`, `aptitude-test-prep.com`,
  `interviewchamp.ai`, `scribd.com`.
- **Zhihu 专栏 lead-gen**: `zhuanlan.zhihu.com/p/715863668` (面经 | SIG Quant Trader岗位) and
  `zhuanlan.zhihu.com/p/1904129381674234394` (面经| SIG QR岗位OA面). These look like candidate write-ups but
  both truncate into 需要以上完整面经的同学 公众号后台回复【面经】即可领取 — a WeChat-account lead magnet, i.e. the
  content-farm tell. The second does assert `第一轮机考OA,一共 1h` + `九道固定的题目` + `两道新题，求绿色三角形的重量`,
  which is interesting but I did not admit it as attestation.

**Note on a screenshot source I did *not* use as a record:** `studyx.ai/homework/106555591` is OCR of a
photographed SIG test panel headed *"The Susquehanna Problem Solving Assessment"* with a question-number
strip running `…8 9 10 11 12 13 14 15 16 17` and "Question 17" carrying the frog stem with endpoint
**B(5,4)** rather than the B(5,6) in the 1point3acres recall. It independently corroborates both the
17-question count and the frog item, and shows SIG rotates the numbers. It is a US homework-help site,
not Chinese social, so it is cited inside `doubt` rather than given its own record.

---

## 6. Platform-by-platform: what I could not establish

**小红书 / Xiaohongshu — ZERO records. This is the biggest gap and it is a hard block, not laziness.**
The site returns 200 but paginates search through a signed API; the SSR state ships `"feeds":[]`.
Search engines do not index `xiaohongshu.com/explore/*` note pages — DDG, Sogou and Bing returned only
`xiaohongshu.com` user-profile shells and the site's own campus-recruiting portal. Baidu *does* index
XHS-style content, and I saw three emoji/hashtag-styled titles that are almost certainly XHS notes:
`SIG面试全记📈细节攻略` (snippet: SIG 的面试从在线评估(OA)开始,1小时内要完成17道题。题目不难,但覆盖面非常广),
`SIG Quant面试攻略,速看` (snippet: 📝第一轮在线评估(oa)：这一轮主要考察概率论和马尔可夫过程) and
`SIG QR面试全攻略:从初试到终审` (snippet ends `#sig面试 #量化求职 #量化研究 #quant #quant求职`). **I did not record
any of them**, for two reasons: Baidu served them through `mbd.baidu.com` aggregator links that answer
with 百度安全验证 to every fetch, so I could not reach the originals; and I could not prove they are
Xiaohongshu rather than 百家号 reposts. Attributing them to 小红书 would have been a guess. The first
snippet is a third independent-looking statement of 1小时17道题, so this is a real loss.
**No screenshots were transcribed — I never got a legible one.**

**知乎 / Zhihu — ZERO records.** Hard 403 on every endpoint and proxy (see §2). Everything the search
layer surfaced under a `zhihu.com` URL for SIG turned out to be 公众号 lead-gen (§5). Genuine-looking
Zhihu material I could see existing but not verify: `zhuanlan.zhihu.com/p/498681895`
(近期量化机构面试+笔试题, a candidate compiling recent quant written tests with his own answers — my
highlight query for it returned LeetCode-62 explainer pages instead), and
`zhihu.com/question/…` "在SIG Susquehanna上班是怎样的体验?" (4 answers, 53k views — Dublin intern experience,
no interview questions).

**Bilibili — ZERO records, and I am confident this is a true negative.** The WBI-signed API works
(verified against a control keyword) and returns nothing for any SIG phrasing. The closest artefacts:
`BV1iA411U771` *"Optiver - 量化交易岗 - 游戏通关之 80in8"* (JadaLLL, 2023-02-16, 960 views) — a real
candidate naming Optiver's 80-in-8 stage, but the video has an **empty description** and I could not
extract question text, so no record; and `BV1pL411U7Nz` 【概率论】某量化投资企业的笔试题 (NJU maths PhD
explaining a written-test probability problem his roommate sat) — genuine, but **the firm is never
named**, so it cannot enter a firm-keyed harvest.

**微博 / 抖音 / 贴吧 / 豆瓣 / 水木 / V2EX / 虎扑 / 小木虫 — ZERO records.** Weibo and Tieba are network-blocked;
Douban and newsmth are reachable but I found no quant-interview content on either (and for newsmth I
could not even enumerate the boards — see §2 — so "no SIG content on 水木" is **unestablished**, not proven).
One Weibo post did surface in a Sogou snippet — 体验了一把量化笔试 40分钟内做完包括概率论，统计，计量和编程的10道题 —
but again **no firm is named**.

**Peer firms.** Jane Street, Citadel, IMC, Jump and HRT produced no usable Chinese-social question text.
Citadel and Jane Street content in Chinese is overwhelmingly business journalism (Bilibili has a dozen
explainer videos on Jane Street's India ban and its 2025 earnings) or vendor pages. `1point3acres` has a
Citadel tag with real threads (e.g. thread-664035 城堡面试总结) but I did not get into them before finishing.

**Platform-taxonomy caveat that affects every record.** The `source_type` enum given to me has no bucket
for the two BBSes that actually produced the data — 一亩三分地 (1point3acres, an overseas-Chinese-student job
board) and 牛客网 (Nowcoder, a campus-recruiting community). I set `source_type: "university_bbs"` for all
40 records as the nearest student-BBS value and put the true site name in the `platform` field and in
`doubt` on every record. Only the six 交大门 (`xjtu.app`) records are literally a university BBS.
**Downstream consumers must read `platform`, not `source_type`.**

---

## 7. Source threads that produced the records (pass 1 = A–H; pass 2 = I–K, see §9)

| # | URL | Records | Access route |
|---|---|---|---|
| A | `1point3acres.com/bbs/thread-1144112-1-1.html` — 2026 SIG Quant Research OA整理【带答案】 | 6 | Wayback `20250912084409` (GB18030) for Q1–Q3 + Q14 replies; search highlights for Q16–Q17 |
| B | `1point3acres.com/bbs/thread-719224-1-1.html` — SIG Quantitative Evaluation 2021 | 2 | search highlights only |
| C | `1point3acres.com/bbs/tag/sig-905-15.html` and `-16.html` — SIG company tag index | 3 | search highlights only |
| D | `1point3acres.com/bbs/thread-1082367-1-1.html` — SIG QR 17题OA | 2 | search highlights; body behind the forum's 188-point paywall |
| E | `nowcoder.com/feed/main/detail/2a0a8e943c354078be335165597b6da4` — SIG OA | 2 | direct fetch, SSR JSON |
| F | `xjtu.app/t/topic/12756` — Optiver 挂经 & 反思总结 | 6 | direct fetch, full HTML |
| G | `nowcoder.com/feed/main/detail/21d4b025d67a421ba7b7273ecdb7f3ef` — #Optiver# 面试 | 9 | direct fetch, SSR JSON |
| H | `nowcoder.com/feed/main/detail/3d62edffa9dc40c883d3d019dd7f6789` — 985废柴挑战顶级量化optiver笔试 | 10 | direct fetch, SSR JSON (needed 3 attempts) |
| I | `1point3acres.com/bbs/thread-1141422-1-1.html` — 26 summer optiver OA | 15 | search highlights; body behind the 188-point paywall |
| J | `1point3acres.com/bbs/thread-1164459-1-1.html` — Optiver OA (2026, PhD, Fail) | 3 | search highlights; body behind the 188-point paywall |
| K | `1point3acres.com/bbs/thread-1141209-1-1.html` — Optiver 2026 Quantitative Research Intern-OA | 4 | search highlights; body behind the 188-point paywall |

**Total: 62 records across 12 distinct source URLs.**

Other real threads located but **not** mined (paywalled, structure-only, or ran out of runway):
`thread-1084760` (SIG QR OA 2024 秋 17题 — see §9, corroborates 17-in-60), `thread-1084480` (SIG Quant OA面经),
`thread-1009682` (SIG 2024 OA 附加第一题小思路 — 第一题是战船游戏，第二题是 Leetcode 98),
`thread-1137753` (Optiver QT 26 OA — see §9, corroborates Zap-N = 9 games),
`thread-1076649` (optiver sde 2025 intern oa — see §9, corroborates the 交大门 log-server problem),
`thread-1051693` (2024 SIG的OA Quantitative), `thread-1138927` (Optiver QT intern OA US 2026),
`thread-1030830` (Optiver SDE Intern 面经), `thread-664035` (城堡面试总结),
`1point3acres.com/bbs/tag/sig-905-1.html` (550 threads, 3698 replies),
`nowcoder.com/feed/main/detail/b7a85049954e4a5d9f5920fd09c83592` (Optiver FPGA Intern — timeline only),
`nowcoder.com/discuss/465910881050689536` (【2023暑实】optiver数据科学家 笔试 — fetched OK, but already
covered by the `sig_nowcoder_yingjiesheng` shard, so not duplicated here).

---

## 8. Known weaknesses in the delivered records

- **Six records carry a topic or a nickname rather than a stem** and say so explicitly in `doubt`:
  SIG Q14 (grid puzzle, known only from two users arguing about its answer), 力扣酒吧, 求绿色三角形的重量,
  速度2mile/h, and the two Optiver HackerRank problems from 交大门 (whose author states outright
  这部分内容本文不展开说). They are recorded as *evidence a question exists at that slot*, not as usable items.
- **SIG Q3's table body is missing** — the Wayback snapshot cut off after the column headers, so the
  question as transcribed is not answerable. The stem is byte-verified; the numbers were never seen.
- **The Optiver 20-MCQ battery is one record, not twenty.** The source compresses 20 questions into 20
  topic phrases with no options and no answers; splitting them would fake a fidelity the source lacks.
- **Nine records are behavioural**, not quantitative (Optiver's English HR screen). Real questions, low
  distinctiveness.
- **Group A's poster has taken the SIG OA several times** (已经做了好几次了) and is farming forum currency
  (求加米!!!), so it is a composite across sittings, and the 答案 values are his own working, not SIG's key.
  His stated answer to Q2 (B–D–A–C–E) does not obviously satisfy all three constraints under every
  left/right convention — flagged in that record.

Added by pass 2 (§9):

- **Only one of the 62 records carries a reported answer that is disputed rather than absent** — the
  `4 5 9 13 22 31 ？53` sequence, where a replier argues the answer should be 40. Both readings are in
  the record. Overwhelmingly, `reported_answer` is `not given`: these posters recall stems, not keys.
- **The four Optiver probability items in Group I are the shard's biggest textbook-contamination risk.**
  The poster labels the whole section Green-Book-style, and one item is word-for-word on a prep-vendor
  page. Kept per the no-over-filtering rule, but they should be the first thing a reviewer re-checks.
- **Group I's 8 sequences and Group J's 3 sequences are unverifiable in principle.** A single mis-keyed
  digit silently changes the intended rule and there are no answers to check against. Group J's poster
  explicitly disclaims accuracy and had failed the test.
- **Group K's two coding records are setups without tasks** — in one the poster admits he forgot the
  problem, in the other the highlight block cuts off before the question is stated.
- **The imbalance toward Optiver widened.** Pass 2 added 22 Optiver records and 0 SIG, taking the split
  to 15 SIG / 47 Optiver. SIG remains the shard's primary firm and its weakest coverage.

---

## 9. Second pass — three Optiver threads no sibling shard covers

Before finishing I diffed my `source_url` set against the other shards in `harvest/raw/`. That surfaced
a gap worth filling: several Optiver 面经 threads that had appeared in my searches were present in **no**
shard at all. All three were recovered the same way — the thread body is behind 1point3acres' 188-point
paywall to a logged-out reader, but the search index holds verbatim highlight blocks of it. Everything
below is `access: snippet_only`, `retrieval_method: websearch_snippet`.

### `thread-1141422` — "26 summer optiver OA" (15 records)

Tag line: `2025(7-9月) 金工类 硕士 实习@optiver - 网上海投 - 在线笔试 | 😃 Positive 😐 Average | Other | 应届毕业生`.
The richest single Optiver OA recall I found. Four modules (`一共4 个modulus`):

1. **找规律** — eight number sequences, transcribed digit-for-digit → 8 records.
2. **搬房子** — a minimum-moves rearrangement puzzle defined by an on-screen picture he does not reproduce → 1 record.
3. **连连看** — speeded 7–8 character string matching → 1 record. Independently corroborates the "code compare"
   game that the Nowcoder poster lists as game 5 of the nine-game Zap-N battery.
4. **概率** — four probability items, three of them quoted in **verbatim English** → 5 records (4 items plus
   one Heads-vs-Tails "race" fragment whose stem is clipped at both ends).

Caveat carried in every probability record: the poster himself calls the section
`中规中矩的绿皮书统计题` — Green-Book-style. These items therefore sit close to the textbook canon this
harvest is supposed to exclude. I kept them because the attestation is a candidate describing an OA he
sat (`都是真题`), not a textbook citation, and because the English wording is verbose and idiosyncratic in
a way that reads as copied off the screen. The `$63 bankroll` item in particular also appears verbatim on
prep-vendor pages — which could mean they scraped this forum, or that both draw on a common circulating
bank. Unresolvable either way; it is stated in `doubt`.

### `thread-1164459` — "Optiver OA" (3 records)

Tag line: `2026(1-3月) 金工类 博士 其他@optiver - 网上海投 - 在线笔试 | 😐 Neutral 😣 Hard | Fail | 其他`.
Gives a **three-part** structure taken in fixed order: `1）Number Logic 25min 2）Beat the Odds 45min
3) Likelihood Test 25min`. Two Number Logic sequences from the OP plus one from a replier who disputes
the answer (`4 5 9 13 22 31 ？53 这个答案是不是应该是40而不是53？` — so at least one of the two candidates
has that item wrong). The OP disclaims his own accuracy: `草稿纸上还记得的一些比较confused的题（不保证答案是对的）`,
and he failed, so these are specifically the items he could not solve.

### `thread-1141209` — "Optiver 2026 Quantitative Research Intern-OA" (4 records)

Four sections; Coding is 90 min on HackerRank with back-navigation and test runs allowed. Two coding
problems (a combinatorial count of arrangements of *m* a's and *n* b's; an order-array stock-trading
problem) and two dice items. Both coding records are weak by construction — the poster says outright
`题目有点记不清楚了` for the first, and for the second the highlight block ends before the task is stated,
leaving a setup with no question. The source also literally reads `1 代表买，-1 代表买` ("buy" twice),
an obvious typo for 卖 (sell); I preserved the error in `question_text` and flagged it in `doubt`.

### Structure-only, logged but **not** turned into records (no question text)

- `thread-1137753` "Optiver QT 26 OA + 求一面经验" — `三部分， numberlogic (sequence 找规律)， zap-N小游戏,
  和 beat the odds`. Valuable as **independent corroboration that Zap-N is nine games**: a replier writes
  `卧槽吓死了 之前看ZapN是9个我以为我只有三个是auto reject😭😭😭`. This is the third independent source for
  the nine-game count, after the Nowcoder recall and 交大门.
- `thread-1084760` "SIG QR OA 2024 秋 17题" — title alone corroborates 17-in-60, and the visible body reads
  `刚做完，大部分题目只是改了数字 题不难但是太多了，只有一小时，没有做完` ("just finished; most questions only
  had the numbers changed; not hard but far too many, only one hour, didn't finish"). **A fourth independent
  genuine attestation of the 17-in-60 prior**, and direct evidence the bank is recycled with numbers swapped.
  No question text is exposed, so no record.
- `thread-1076649` "optiver sde 2025 intern oa" — exposes the log-server problem statement verbatim
  (`Suppose you are responsible for building a log server... only return up to m logs from the last hour`,
  constraints `1 ≤ m ≤ 1000`, `1 ≤ q ≤ 10^6`). Not added as a new record because the same problem is
  **already** in this shard from 交大门 `xjtu.app/t/topic/12756`; instead it stands as strong
  cross-platform corroboration that the 交大门 recall is accurate.
- `thread-1051693` "2024 SIG的OA Quantitative" — index metadata only, body fully paywalled.

---

## 10. Two open questions from pass 1, now closed

### 水木社区 board names — **found**, but the boards are recruiter spam

Pass 1 failed because I guessed board names (`Job`, `JobInfo`, `Intern`, `WorkLife`…), all of which return
指定的版面不存在. The real section index is `https://www.newsmth.net/nForum/section/Career`, which fetches
200 and GB18030-decodes cleanly. Actual board names:

`Career_Campus` (校园招聘信息, 128 075 topics) · `Career_Investment` (求职投行) · `Career_PHD` (博士求职) ·
`Career_Plaza` (求职广场) · `Career_Servant` (公务员) · `Career_Upgrade` (社会招聘) · `ExecutiveSearch` (猎头招聘)

The search endpoint `nForum/s/article?ajax&b=<board>&q=<term>` returns 200 with a 水木社区-搜索结果 page but
a constant 16 389-byte body regardless of query — i.e. it renders results client-side, so I could not read
hits from it. What I *could* read of the boards is decisive on relevance: `Career_Plaza` and `ExecutiveSearch`
are wall-to-wall **recruiter advertisements** for domestic 量化私募 (`量化私募诚意高薪聘请：24/25/26届本硕博`,
`百亿量化私募高薪急招C++`), posted by a handful of repeat accounts (`Panslam1`, `pans11`, `seaokcs`). This is a
**job-ad board, not a 面经 board**. The brief's expectation that 水木 is an overlooked high-quality archive of
recall did not hold for these firms — the 面经 culture has moved to 牛客网 and 一亩三分地. I still cannot prove
水木 has *zero* SIG content, only that its Career boards are not where it would be.

### Xiaohongshu — **definitively unreachable**, on two independent grounds

1. **Not indexed.** Bing returns **zero** `xiaohongshu.com` URLs for `optiver 笔试 site:xiaohongshu.com`,
   `SIG 面经 量化 site:xiaohongshu.com`, or `Optiver OA 小红书 笔记`. Note the recurring confound that wasted
   a lot of pass-1 effort: 小红书 is itself a well-known *employer*, so almost every Chinese query pairing
   小红书 with 面经/笔试 returns interview recall **about working at Xiaohongshu**, not quant recall hosted on it.
2. **Not fetchable.** A note URL `https://www.xiaohongshu.com/explore/<id>` returns **HTTP 302** with a
   175-byte `Found` body under a mobile Safari UA — no `__INITIAL_STATE__`, no content. Combined with the
   pass-1 finding that `/search_result` renders `"feeds":[]` behind a signed `x-s` API, there is no
   unauthenticated route to note text.

Consequence: **zero `screenshot_only` records in this harvest.** The brief anticipated transcribing OA
screenshots from Xiaohongshu; I never obtained a single legible one, so nothing was transcribed. That is a
genuine gap, not a filtering decision.

---

## 11. Overlap with sibling shards — for downstream dedup

I share 5 URLs with two sibling shards. Dedup on `source_url`:

| URL | Also in |
|---|---|
| `1point3acres.com/bbs/thread-1144112-1-1.html` | `sig_1point3acres.jsonl` |
| `1point3acres.com/bbs/thread-1082367-1-1.html` | `sig_1point3acres.jsonl` |
| `1point3acres.com/bbs/thread-719224-1-1.html` | `sig_1point3acres.jsonl` |
| `nowcoder.com/feed/main/detail/3d62edffa9dc40c883d3d019dd7f6789` | `sig_nowcoder_yingjiesheng.jsonl` |
| `nowcoder.com/feed/main/detail/2a0a8e943c354078be335165597b6da4` | `sig_nowcoder_yingjiesheng.jsonl` |

Note that overlapping URLs do **not** imply duplicate questions — different shards extracted different
items from the same thread, and my versions were independently transcribed. The remaining 7 URLs
(including all three pass-2 threads) are unique to this shard.

One further note on `source_type`: **all 62 records carry `university_bbs`**, which is a forced fit. The
enum offers no value for 一亩三分地 (an overseas-student job BBS) or 牛客网 (a campus-recruiting community),
and neither is a university BBS in the strict sense. Only 交大门 genuinely is one. The true site name is
always in the `platform` field; filter on that, not on `source_type`.

---

## 12. Pass-2 queries

Batch-run from the shell across Baidu / Sogou / DuckDuckGo (`/tmp/harvestwork/qs1.txt`), all yielding only
the 小红书-as-employer confound described in §10:

`SIG 面经 小红书 笔试` · `SIG 量化 OA 真题 小红书` · `小红书 SIG 笔试 17道` · `SIG 网测 面经 概率题` ·
`知乎 SIG 量化研究员 面试 题目` · `SIG 量化 笔试 知乎 专栏` · `Optiver 笔试 小红书 面经` ·
`IMC 笔试 面经 小红书` · `Jane Street 面试 小红书 面经` · `简街 面经 知乎 笔试`

Highlight-engine queries (these are what produced the pass-2 records):

- `知乎 SIG Susquehanna 面试体验 量化 笔试 题目 概率`
- `小红书 SIG 量化 笔试 面经 OA 17道题 60分钟`
- `水木社区 newsmth SIG Optiver 量化 笔试 面经 求职版`
- `小红书 笔试 面经 Optiver IMC Jane Street 量化 实习 真题 回忆`
- `1point3acres 26 summer optiver OA 搬房子 连连看 找规律 bankroll $63 expected profit coin toss strategy`
- `哔哩哔哩 bilibili SIG Optiver 量化 OA 笔试 录屏 面经 视频 题目回忆`
- `知乎 专栏 SIG 面试 一面 二面 题目 骰子 硬币 期望 报价 make market 交易员 实习生`
- `xiaohongshu.com 探索 笔试 SIG Optiver 量化 OA 题目 截图 分享 小红书笔记`

Shell probes: `newsmth.net/nForum/section/Career`, `newsmth.net/nForum/board/Career_Campus`,
`newsmth.net/nForum/s/article?ajax&b=Career_Campus&q=Optiver`, `newsmth.net/nForum/s/article?ajax&q=SIG`,
`nowcoder.com/discuss/465910881050689536`, `xiaohongshu.com/explore/<id>`, plus three Bing `site:` probes.

### Additional sources rejected in pass 2

- **`meiguo.blog`** ("美国博客网USA") — carries a SIG QR three-round recall with specific content (the
  oranges/options/lending trading scenario, the 1-to-100 number game, acute-triangle and HHT-vs-HTH items).
  Rejected: it is a content-farm aggregator that **rewrites** 1point3acres posts rather than reposting them
  verbatim (emoji-bulleted, third-person "一位求职者"), and it is not a Chinese social platform in scope. I
  could not locate the underlying original. Worth a targeted look by whoever owns the 1p3a shard.
- **`prachub.com`** — lists the `$63 doubling strategy` and 3-flip items in near-identical wording to
  `thread-1141422`. Prep vendor; excluded, but noted because the overlap is evidence of scraping in one
  direction or the other.
- **`jishuzhan.net`**, **`programhelp.net`**, **`attcareer.com`**, **`oavoservice.com`**,
  **`quantt.co.uk`**, **`jobtestprep.co.uk`**, **`quantvault.org`**, **`techinterview.org`** — all
  prep-vendor or content-farm pages selling 辅导 / 代做 / 包过 / PrepPacks. Excluded. Several state
  1小时17道题 for SIG, which is consistent with the prior but carries no independent evidentiary weight.
