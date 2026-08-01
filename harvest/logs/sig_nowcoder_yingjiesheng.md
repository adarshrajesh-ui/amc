# Harvest log — SIG (+ Optiver / IMC / Jane Street / Citadel) on 牛客网 & 应届生求职网

Shard: **Susquehanna International Group (SIG)** primary; Optiver, IMC, Jane Street, Citadel
opportunistically. Sources in scope: nowcoder.com (牛客网), yingjiesheng.com (应届生求职网),
plus kanzhun.com (看准网), maimai.cn (脉脉), shixiseng.com (实习僧).

Output: `/workspace/harvest/raw/sig_nowcoder_yingjiesheng.jsonl`

---

## 1. Access: what worked, what was gated

| Target | Plain `curl` | `WebFetch` | `r.jina.ai` reader | Verdict |
| --- | --- | --- | --- | --- |
| `www.nowcoder.com` post pages | **blocked** — Aliyun WAF JS challenge, every request returns the same 11,201-byte interstitial | **works**, full post body rendered | **works**, full page as markdown | fully readable |
| `www.nowcoder.com/search?type=post&query=…` | blocked (same WAF) | works | works, and supports `&page=N` | fully searchable |
| `bbs.yingjiesheng.com` forum index | works (GBK) | works | works | index only |
| `bbs.yingjiesheng.com` **boards** (`forum-<fid>-1.html`, `forum.php?mod=forumdisplay&fid=…`) | **gated** — every board id returns 「抱歉，指定的版块不存在」 | **gated**, identical message | gated | **no thread lists** |
| `bbs.yingjiesheng.com` **threads** (`thread-<tid>-1-1.html`) | **gated** — 「抱歉，指定的主题不存在或已被删除或正在被审核」 for every tid tried | gated | gated | **no post bodies** |
| `bbs.yingjiesheng.com/search.php` | **disabled** — returns a 20-byte empty body for both GET and POST, with or without cookies; no `formhash` is ever emitted | — | — | **no search** |
| `www.yingjiesheng.com` | works | works | works | job board only, no 笔经/面经 archive |
| `www.yingjiesheng.com/sitemap.html`, `/bishi/`, `/mianjing/` | `/bishi/` and `/mianjing/` are **404**; `sitemap.html` returns a **瑞数 anti-bot challenge** (`{"l1":"var arg1='…'"}` + an encrypted blob, identical body for every path) | — | — | no crawlable index |
| `q.yingjiesheng.com/pc/search?keyword=…` (the live search, now 51job-operated; `s.yingjiesheng.com/search.php` redirects here) | **blocked** by the same 瑞数 `arg1` challenge — same 12,203-byte body for `SIG`, `Optiver`, `量化` | — | **penetrates the challenge and renders the page** | renders, but it is a **job-listing** search only: no 笔经/面经 surface, and zero hits for Optiver or SIG |
| `www.kanzhun.com` | JS SPA, no content in HTML | — | reader returns only the site footer | nothing retrievable |
| `www.shixiseng.com` | works | — | works | internship **job listings** only, no interview recalls |
| `maimai.cn` | 200 on homepage | — | reader refuses the domain (`AbuseAlleviationError`, anonymous access blocked) | nothing retrievable |

**Answer to the brief's question:** WebFetch *does* work on nowcoder.com — it renders full post
bodies and full search-result pages. WebFetch also "works" on yingjiesheng.com in the sense of
returning HTTP 200 and readable markup, but every board and every thread is behind an anonymous-access
gate, so it yields no content. All 53 harvested records therefore come from nowcoder.
Nothing in this harvest is `snippet_only`; everything is `full_text`.

### Search engines

| Engine | Result |
| --- | --- |
| Built-in WebSearch | usable; good index, but for SIG it returns almost exclusively prep-vendor pages (programhelp.net, quantblueprint, jobtestprep, tradermath, tradinginterview, techinterview.org, jishuzhan.net, interviewchamp.ai, dataford.io) — all excluded by the brief. Did surface the yingjiesheng board-group pages. |
| Sogou 搜狗 (scraped) | works and parses; its nowcoder deep-link index is shallow, surfaced nothing new |
| Baidu | **captcha** — `百度安全验证` on every query |
| Bing | returns a JS shell with no `b_algo` result blocks to a scraper |
| DuckDuckGo html endpoint | parses, but its nowcoder pages are all WAF interstitials ("Access Verification") |
| Wayback CDX | zero archived `yingjiesheng.com` URLs matching sig/susquehanna/optiver; zero matching archived `bbs.yingjiesheng.com` URLs |

A note on the `site:nowcoder.com SIG` trap: that query is dominated by **Tencent CSIG**
(腾讯云与智慧产业事业群) and by C's `SIG_DFL`/`SIGKILL`/`signal()` macros, `PCI-SIG`,
`SIGCOMM`, `utf-8-sig`, Kubernetes `SIG` chairs, the VC firm **SIG海纳亚洲** (ByteDance investor),
and 康美包SIG (a Swiss packaging company). Every one of those had to be filtered out by hand.

---

## 2. Queries run

### Wave 1 — firm names & generic quant vocabulary  (15 distinct queries)

Endpoint: `https://www.nowcoder.com/search?type=post&query=<q>`  ·  pages 1–1 each

- `Optiver`
- `IMC 面经`
- `Jane Street`
- `简街`
- `Citadel 面经`
- `量化交易员 面经`
- `量化 笔试 面经`
- `外资量化 面经`
- `量化实习 面经`
- `对冲基金 面经`
- `SIG`
- `Susquehanna`
- `海纳国际`
- `量化 OA 概率`
- `交易员 笔试 概率`

### Wave 2 — firm + assessment vocabulary  (26 distinct queries)

Endpoint: `https://www.nowcoder.com/search?type=post&query=<q>`  ·  pages 1–1 each

- `SIG OA`
- `SIG 笔试`
- `SIG 暑期实习`
- `SIG 面试`
- `Optiver 笔试`
- `Optiver 面经`
- `Optiver 交易`
- `IMC 笔试`
- `IMC Trading`
- `IMC 实习`
- `Jane Street 面经`
- `Jane Street 笔试`
- `Citadel 笔试`
- `Citadel Securities`
- `Citadel 实习`
- `量化 面经 概率`
- `quant 面经`
- `trader 面经`
- `做市商 面经`
- `期权 交易员 实习`
- `海外量化 实习`
- `量化研究员 面经`
- `量化交易 暑期实习`
- `外资 交易员 笔试`
- `心算 笔试 交易`
- `概率题 面试 量化`

### Wave 3 — SIG-specific variants + peer firms  (31 distinct queries)

Endpoint: `https://www.nowcoder.com/search?type=post&query=<q>`  ·  pages 1–1 each

- `SIG 香港`
- `SIG 全职`
- `SIG quant`
- `SIG trading`
- `SIG 交易`
- `SIG 网测`
- `SIG 测评`
- `SIG 电面`
- `SIG 挂了`
- `SIG 概率`
- `SIG 智力题`
- `SIG 心算`
- `Susquehanna 面试`
- `海纳国际集团`
- `萨斯奎哈纳`
- `Optiver 面试 概率`
- `Optiver 交易员`
- `Optiver 网测`
- `IMC 面试 交易`
- `IMC 网测`
- `Jane Street 实习`
- `Jane Street OA`
- `Citadel OA`
- `Citadel 量化`
- `Akuna`
- `Tower Research`
- `Jump Trading`
- `Flow Traders`
- `optiver 小游戏`
- `量化 笔试 智力题`
- `交易员 群面 做市`

### Wave 4 — deep pagination (pages 1-4 each)  (10 distinct queries)

Endpoint: `https://www.nowcoder.com/search?type=post&query=<q>`  ·  pages 1–4 each

- `SIG`
- `SIG OA`
- `Optiver`
- `IMC 面经`
- `Jane Street`
- `Citadel 面经`
- `量化 面经`
- `quant 面经`
- `量化 实习 面经`
- `交易员`

### Wave 5 — SIG exhaustion (pages as noted)  (4 distinct queries)

Endpoint: `https://www.nowcoder.com/search?type=post&query=<q>`  ·  pagination as recorded

- `SIG`
- `SIG 面试`
- `SIG 实习`
- `sig oa`

### Wave 6 — peer firms, pages 1-2 each  (12 distinct queries)

Endpoint: `https://www.nowcoder.com/search?type=post&query=<q>`  ·  pages 1–2 each

- `IMC Trading`
- `IMC 交易`
- `IMC 暑期实习`
- `Jane Street 面试`
- `简街 面试`
- `Optiver 笔试`
- `Optiver 暑期实习`
- `Akuna 面经`
- `量化 OA`
- `做市 面试`
- `期权 做市商 面经`
- `概率 智力题 面试 交易`

### Wave 7 — SIG long tail + search-recall control  (14 distinct queries)

Endpoint: `https://www.nowcoder.com/search?type=post&query=<q>`  ·  pages 1–1 each

- `岛屿问题的变种`
- `SIG 一面`
- `SIG 二面`
- `SIG superday`
- `SIG hr面`
- `SIG 都柏林`
- `SIG 悉尼`
- `SIG 期权`
- `SIG 做市`
- `SIG 扑克`
- `SIG 面经 量化交易`
- `海纳 交易 面试`
- `SIG quantitative`
- `SIG problem solving`

### Wave 8 — assessment-format fingerprints  (10 distinct queries)

Endpoint: `https://www.nowcoder.com/search?type=post&query=<q>`  ·  pages 1–1 each

- `80题 8分钟`
- `心算 8分钟`
- `17道题 60分钟`
- `交易游戏 面试`
- `market making 面试`
- `报价 做市 面试题`
- `trading game 面试`
- `量化 心算测试`
- `数学测试 8分钟 交易`
- `IMC 笔试 面经`

### Wave 9 — final SIG name-variant and channel sweep  (10 distinct queries)

Endpoint: `https://www.nowcoder.com/search?type=post&query=<q>`  ·  pages 1–1 each

- `SIG 笔经` — 0 hits
- `SIG 面经` — 17 hits, all `sig_atomic_t` / `SIG_IGN` / Kubernetes-SIG noise
- `SIG 秋招` — 18 hits, all noise (incl. 康美包SIG, a Swiss packaging firm in Suzhou)
- `SIG 春招` — 18 hits, all noise (incl. SIG海纳亚洲 as a MetaApp investor)
- `SIG codesignal` — 0 hits
- `SIG 在线测评` — 0 hits
- `SIG 量化` — 2 hits, both noise (a finance knowledge-graph tutorial; `PCI-SIG` SR-IOV)
- `萨斯奎汉纳` — 0 hits (the other transliteration, `萨斯奎哈纳`, was already 0 in wave 3)
- `Susquehanna 实习` — 0 hits
- `IMC` (bare) — 20 hits, all 整合营销传播 / 国际大学生数学竞赛 / 欧莱雅-业务面 noise

**Total distinct Nowcoder search queries: 132**, across ~200 rendered search/post page fetches.

### Nowcoder endpoint shapes probed

- `https://www.nowcoder.com/search?type=post&query=…` — works; the workhorse
- `https://www.nowcoder.com/search?type=post&query=…&page=N` — works; pagination confirmed to return different result sets
- `https://www.nowcoder.com/search?type=all&query=SIG%20OA` — works, same corpus
- `https://www.nowcoder.com/search?type=question&query=SIG` — works, returns 题库 items, nothing SIG-related
- `https://www.nowcoder.com/search?type=company&query=Optiver` — 404 — 页面找不到了; no company-scoped search
- `https://www.nowcoder.com/interview/center?query=Optiver` — renders the generic 面经 centre, query is ignored
- `https://www.nowcoder.com/creation/subject/<uuid>` — topic-tag pages; render but only expose the first item or two to a non-JS reader

### Non-Nowcoder searches

- WebSearch: `SIG 牛客 面经 OA 笔试`
- WebSearch: `site:nowcoder.com SIG 笔试 真题`
- WebSearch: `海纳国际 SIG 面经 牛客网 量化`
- WebSearch: `Susquehanna SIG 量化交易员 笔试 17道题 60分钟`
- WebSearch: `牛客网 SIG 面经 量化 交易员 实习 nowcoder.com`
- WebSearch: `应届生求职网 yingjiesheng SIG Susquehanna 笔经 面经 量化`
- WebSearch: `site:bbs.yingjiesheng.com 量化 交易 面经 Optiver IMC`
- Sogou: `SIG 面经 牛客`, `SIG OA 牛客网`, `SIG 笔试 牛客`, `Optiver 笔试 牛客网 面经`, `应届生 SIG 面经 量化`, `site:yingjiesheng.com 笔经`, `bbs.yingjiesheng.com 量化 笔经`, `bbs.yingjiesheng.com thread 面经 外资`
- Bing: `site:nowcoder.com SIG 面经`, `site:nowcoder.com SIG 量化`
- DuckDuckGo: `site:nowcoder.com Susquehanna`, `nowcoder SIG 量化 面经`
- Baidu: `site:nowcoder.com SIG 量化`
- Wayback CDX: `yingjiesheng.com*` filtered on sig / susquehanna / optiver; `bbs.yingjiesheng.com*` full URL list

---

## 3. Every Nowcoder post / topic page opened

- `https://www.nowcoder.com/creation/subject/1af7c0d5c7184826aa7019504b6c94e7`
  - topic page `#JaneStreet#` — only 1 post exposed (the same Jane Street one).
- `https://www.nowcoder.com/creation/subject/55fb06a0881a45e8aa06107c6efc0020`
  - topic page `#量化面经#` — only 1 post exposed to a non-JS reader (the Jane Street one).
- `https://www.nowcoder.com/creation/subject/c4b74f6d5cc94d0f9e3cc9e100bed05b`
  - topic page `#量化私募#` — 6 posts exposed, all recruiter job ads, no recalls.
- `https://www.nowcoder.com/discuss/353157497731096576`
  - **Citadel** HK 量化实习 two phone screens, 2021-01-26 — ✅ HARVESTED (7 questions).
- `https://www.nowcoder.com/discuss/465910881050689536`
  - **Optiver** 2023 暑实 数据科学家 笔试, 2023-03-16 — ✅ HARVESTED (2 coding questions + format facts: 2h, HackerRank).
- `https://www.nowcoder.com/discuss/469252506288128000`
  - Optiver 2023 暑期实习 IT Developer — ❌ no questions, timeline/status only.
- `https://www.nowcoder.com/discuss/604265548247040000`
  - **Jane Street** 面试题汇总, 2024-04-01 — ✅ HARVESTED (10 questions) **but flagged**: poster is a 公众号/知识星球 operator monetising the content.
- `https://www.nowcoder.com/feed/main/detail/0dbaf3b464564185a7ab3a0d1349b616`
  - 「Optiver OA做完之后多久出结果呢？」 — ❌ one line, no questions.
- `https://www.nowcoder.com/feed/main/detail/116a865d3e564be4a175d6ba580d1fc7`
  - **Citadel** vo2026 终面, undated (07-20) — ✅ HARVESTED (3 questions) **but heavily flagged**: poster sells 北美 OA/VO 「辅助」 (interview-assist) services; likely marketing fiction.
- `https://www.nowcoder.com/feed/main/detail/2a0a8e943c354078be335165597b6da4`
  - **SIG OA**, 2024-05-25 — ✅ HARVESTED (2 questions). The only genuine SIG recall found on Nowcoder.
- `https://www.nowcoder.com/feed/main/detail/3d62edffa9dc40c883d3d019dd7f6789`
  - **Optiver** 2025 Shanghai SDE Summer Internship 笔试, 2025-03-18 — ✅ HARVESTED (29 questions: 2 coding, 20 MCQ, 7 games).
- `https://www.nowcoder.com/feed/main/detail/42b891d6a195451d8565e20e03bcf27e`
  - Optiver 上海 IT intern, 2024-04-23 — ❌ no questions; process only (笔试 = code + MCQ + 小games, HR call in English, two English tech rounds).
- `https://www.nowcoder.com/feed/main/detail/59bd0ec09c864e92ab07187553aa852c`
  - 24年实习小结 (IC front-end), 2024-10-25 — ❌ no questions; corroborates Optiver FPGA round lengths (二面 1.5 h, 三面 3 h).
- `https://www.nowcoder.com/feed/main/detail/76bf6fb2ccaf44c9bc04a894b3fb785e`
  - Optiver 2023 暑假实习 第三轮 — ❌ one line, no questions.
- `https://www.nowcoder.com/feed/main/detail/7e2d9a858ee44993a8747aabbcc14e5a`
  - Optiver 2024 暑期实习 IT, 2024-04-22 — ❌ no questions; process only (OA to be completed within 5 days; tech screen billed 60–90 min, ran 2 h).
- `https://www.nowcoder.com/feed/main/detail/b7a85049954e4a5d9f5920fd09c83592`
  - Optiver FPGA Intern, 2024-05-10 — ❌ no questions; useful process only (OA 3.24 → HR phone 4.3 → tech 4.12 → final tech 4.23 → onsite behavioural 4.29 → OC 5.6).
- `https://www.nowcoder.com/feed/main/detail/e2457644c83b4429bbed78a3ba73f377`
  - 杭州光弦智能 C++量化 笔试 — ❌ **out of shard scope** (domestic Chinese quant shop, not SIG/Optiver/IMC/JS/Citadel). Real and question-rich; left for whoever owns the domestic-quant shard.
- `https://www.nowcoder.com/feed/main/detail/e58a646a5a434563be0c86b7b1986f93`
  - Optiver DS offer, 2023-05-16 (Tsinghua, 量化分析) — ❌ no questions; full timeline incl. a **Takehome Assignment** stage.
- `https://www.nowcoder.com/discuss/360131208938786816`
  - 「2022春招（实习）个人面经/进展汇总」, surfaced by the wave-9 `SIG 秋招`/`SIG 春招` queries — ❌ **not SIG**. A long, genuine, question-rich recall, but of 美团 / 字节跳动 / 阿里 / 华为 C++ backend interviews. The `SIG` match is `SIGKILL`/`SIGINTR` inside the IPC answer. Textbook example of the false-positive class described in §1.

Also opened (non-Nowcoder): `https://bbs.yingjiesheng.com/` (index), `/forum-{57,60,61,63,436,683,3168}-1.html`, `/forum.php?mod=forumdisplay&fid=60`, `/forum.php?gid={2,841,850,1967,2933}`, `/search.php`, `/thread-{99812,350390,1621947,2156530}-1-1.html`, `https://www.yingjiesheng.com/`, `/about/map/`, `/search/?keyword=SIG`; `https://www.kanzhun.com/search?query=SIG`, `/search/?query=Optiver`, `/interview/`; `https://www.shixiseng.com/interns?keyword=Optiver`; `https://maimai.cn/web/search_center?type=feed&query=SIG`.

---

## 4. The key negative result: SIG is nearly absent from Nowcoder

After 132 distinct queries I found **exactly one** genuine SIG recall on Nowcoder.
Before treating that as a scraping failure I ran a **search-recall control**: I searched Nowcoder for
`岛屿问题的变种` — a phrase that appears only in the *body* of the SIG OA post, never in its title.
The search returned that post. So Nowcoder's search **is full-text over post bodies**, and the
absence of other SIG material is a property of the corpus, not of my method.

Two further corroborating signals:

- `Susquehanna` returns **未找到相关结果** (zero results) on Nowcoder. Not one post on the site
  contains the company's full name.
- `SIG superday`, `SIG quantitative`, `SIG problem solving`, `SIG 悉尼` return zero results;
  `SIG 一面`, `SIG 二面`, `SIG hr面`, `SIG 都柏林`, `SIG 扑克`, `SIG 做市`, `SIG 期权` return only
  the `signal.h` / Tencent-CSIG / SIG海纳亚洲-VC noise described above.

Interpretation: SIG does not run a mainland-China campus pipeline that funnels through 牛客,
so Chinese-language SIG recall traffic lives on 一亩三分地 (1point3acres) and Reddit/Wall Street Oasis
instead — which is outside this shard. The single Nowcoder post that exists is an **algorithmic**
OA (two coding problems), not the 17-question/60-minute probability Problem Solving Assessment.

### On the 17-in-60 consistency prior

I could **not** confirm or contradict the 17-questions-in-60-minutes figure from either assigned
source. Nowcoder's one SIG post gives no count and no time limit. Yingjiesheng yields nothing at all.
The only pages I saw asserting a question count were out-of-scope prep vendors, and they
contradicted each other exactly as the brief predicted (tradinginterview.com and tradermath.org say
17-in-60 for the Problem Solving Assessment and 20 min for the Quantitative Evaluation;
jobtestprep says 9 questions; quantblueprint says 50–80 questions in 60–90 min with negative
marking). None of these were used as evidence and none produced a record.

---

## 5. Yingjiesheng: zero yield, for two independent reasons

1. **Structural.** I pulled the full board list off the forum index (2,536 board links). There is
   **no board for SIG, Susquehanna, Optiver, IMC, Jane Street, Citadel, or any prop/market-making
   firm.** The finance groups are banks and domestic brokers only: `gid=1967` (外资银行/投行) covers
   Goldman/MS/JPM/UBS/HSBC/Barclays/DB/CS etc.; `gid=850` (证券/基金类公司) covers 平安, 上交所,
   华夏基金, 易方达, 汇添富, 鹏华, 安信 etc. The nearest quant threads visible in the board summaries
   are 「汇添富量化及指数面试」 and 「2022秋招-量化研究员二面通过情况」 — both domestic asset managers,
   out of scope.
2. **Access.** Even if such a board existed, anonymous users cannot read it. Every
   `forum-<fid>-1.html` returns 「抱歉，指定的版块不存在」 and every `thread-<tid>-1-1.html` returns
   「抱歉，指定的主题不存在或已被删除或正在被审核」, while the same session renders the index fine —
   i.e. a permission gate reported as a not-found. `search.php` is switched off entirely (20-byte
   empty response, no `formhash` in the page, GET and POST alike). The Wayback Machine has no
   archived SIG/Optiver/Susquehanna URLs on either host.
3. **The modern site has no 笔经/面经 surface at all.** The BBS is the only place Yingjiesheng ever
   hosted interview recalls. The live site is now run on 51job infrastructure: `/bishi/` and
   `/mianjing/` are 404, `s.yingjiesheng.com/search.php` redirects to `q.yingjiesheng.com/pc/search`,
   and that search is a **job-listing** search — filters for 学历/薪资/公司性质/行业, no recall content
   in the schema. It is additionally wrapped in a 瑞数 `arg1` JS anti-bot challenge that returns an
   identical 12,203-byte encrypted body to plain `curl` for every keyword. I got **through** that wall
   with the JS-rendering reader, so this is a confirmed read, not a block: the rendered page returns
   **zero listings for `Optiver` and zero for `SIG`**, and exposes no interview-recall section.

So `source_type: "yingjiesheng"` appears **zero** times in the output. This is a real absence,
not an untried avenue: the one wall I could not climb (the BBS permission gate) sits in front of a
board list that provably contains no SIG/Optiver/IMC/Jane Street/Citadel board anyway.

---

## 6. What I deliberately did NOT write down

- Every prep-vendor page the search engines pushed at me: programhelp.net (multiple SIG pages,
  selling 「无痕联机 OA 辅助」), quantblueprint.com, jobtestprep.com, tradermath.org,
  tradinginterview.com, techinterview.org, interviewchamp.ai, dataford.io, jishuzhan.net,
  dev.to/programhelp-cs, meiguo.blog. Several of these contain long lists of plausible SIG questions
  (Penney's game HHT vs HTH, three points on a unit circle, 1–20 pick-three, median of three U(0,3),
  poker blind raise…). **None of it is in the output.** It is unattributed, unsourced, and sold.
- 1point3acres threads that surfaced (e.g. `thread-1084760` "SIG QR OA 2024 秋 17题"). Real
  provenance and directly on-prior, but the content is points-gated and it is a different shard's
  source; I did not read the questions, so I did not record them.
- Nowcoder posts with no questions in them (timelines, 「许愿」 posts, offer-comparison threads,
  recruiter ads). Listed in §3 with an ❌.
- The 杭州光弦智能 C++ quant written test — genuine and detailed, but a domestic Chinese quant firm,
  outside this shard's firm list.

---

## 7. Records written

| Firm | Records |
| --- | --- |
| Optiver | 31 |
| Citadel | 10 |
| Jane Street | 10 |
| Susquehanna International Group (SIG) | 2 |
| **Total** | **53** |

All 53 records are `source_type: nowcoder`, `access: full_text`, `retrieval_method: webfetch`.
Every record carries a non-empty `doubt`.

### Confidence tiers

**Tier A — first-person recall by an identifiable candidate account, no commercial motive** (40 records)

- SIG OA (2) · Optiver 2025 SDE 笔试 (29) · Optiver 2023 DS 笔试 (2) · Citadel HK quant intern (7)

**Tier C — real URL and real text, but the poster is selling something** (13 records)

- Jane Street 面试题汇总 (10) — 知识星球 operator; several questions are widely-circulated classics
  that may have been lifted from a question bank rather than recalled from a Jane Street interview.
- Citadel vo2026 (3) — an OA/VO interview-assist vendor; treat as probable marketing fiction.

Both tiers are in the file per the brief's instruction to put doubt in the `doubt` field rather than
over-filter, but the `doubt` text on the Tier C records says plainly that they should probably be
dropped by a stricter consumer.

### Anti-fabrication verification

Every record was re-checked mechanically against the cached page text it claims to come from. For
all 53 records, both `question_text` and every line of `source_quote` are **exact substrings**
(whitespace-normalised) of the retrieved body of the URL in `source_url`. **0 mismatches.** Nothing
in this file was written from memory; if a question is here, it was read off a page that was fetched.

Note on `firm`: the Citadel records come from a post that names the firm only by its Chinese nickname
「城堡」/「大城堡」. `firm` is normalised to `Citadel` so the field groups cleanly, and the fact that
the source never wrote the English name is recorded in both `poster_context` and `doubt`.

---

## 8. Things I could not establish

- **SIG's role-track split on Chinese boards.** The one SIG post names no track, so I could not
  populate `role_track` for SIG at all. I refused to infer "quant trader" from the firm's reputation.
- **Whether SIG's Nowcoder OA is the dev pipeline or the quant pipeline.** Two coding problems is
  consistent with a CodeSignal/HackerRank SDE screen, not with a probability paper, but the post
  never says.
- **Any SIG question count or time limit** from an in-scope source (see §4).
- **Any IMC content whatsoever.** Zero IMC recalls exist on Nowcoder. Every `IMC` hit is either
  整合营销传播 (Integrated Marketing Communications), the 国际大学生数学竞赛 (IMC maths olympiad),
  a networking paper venue, or a recruiter's copy-pasted list of quant employers. Searched:
  `IMC 面经`, `IMC 笔试`, `IMC Trading`, `IMC 实习`, `IMC 交易`, `IMC 网测`, `IMC 暑期实习`,
  `IMC 面试 交易`, `IMC 笔试 面经`, and bare `IMC`.
- **Optiver quant-trader (as opposed to SDE/DS/FPGA) content.** Every Optiver recall on Nowcoder is
  a technology or data role. The famous 80-questions-in-8-minutes mental-arithmetic test does not
  appear; `80题 8分钟`, `心算 8分钟`, `数学测试 8分钟 交易` all return nothing.
- **Kanzhun / Maimai / Shixiseng.** No retrievable interview-recall content for any of these firms:
  Kanzhun is a JS app that serves no content to a fetcher, Maimai refuses anonymous reader access,
  and Shixiseng only carries job postings.
- **Answers.** Almost nothing in this corpus reports an answer. `reported_answer` is
  "未给答案"/not-reported on the large majority of records; the exceptions are inline hints the
  poster happened to write down (XᵀX is d×d; adding noise ≡ regularisation; median not mean;
  matrix fast exponentiation).

