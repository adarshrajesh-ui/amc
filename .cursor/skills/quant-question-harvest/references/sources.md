# Source ecosystem and search craft

Load this at Phase 2. Work every family below and log coverage per family per firm in `SOURCES.md`,
including the ones that produced nothing. Five Google searches is not a reconnaissance pass.

## Firm target matrix

**Tier A — deep coverage, ≥1 dedicated agent each:**
Susquehanna/SIG, Jane Street, Citadel, Citadel Securities, Optiver, IMC Trading, Jump Trading,
Hudson River Trading, DRW, Five Rings, Akuna Capital, Old Mission Capital, Two Sigma, D. E. Shaw.

**Tier B — solid coverage, 2–3 firms per agent:**
Belvedere, Tower Research/Latour, Chicago Trading Company, Wolverine, Group One, Peak6, Quantlab,
Radix, Headlands, Vatic Labs, Flow Traders, Maven Securities, XTX Markets, G-Research, Qube RT,
Man Group/AHL, Squarepoint, Millennium, Point72/Cubist, Balyasny, Virtu, PDT Partners, Voleon,
WorldQuant, AQR, Arrowstreet, Bridgewater.

**Tier C — opportunistic, strong non-US recall traffic:**
Tibra, Vivienne Court, Grasshopper, Da Vinci, Optiver Amsterdam/Sydney/Shanghai, IMC
Sydney/Amsterdam, SIG Dublin/Sydney/Hong Kong, Eagle Seven, Gelber, Allston, Tradebot, Hehmeyer,
Volant, Transmarket. Add any firm that recurs in recall threads but is missing here, and say you did.

## English-language sources

**Reddit** — r/quant, r/quantfinance, r/FinancialCareers, r/csMajors, r/leetcode,
r/cscareerquestions, plus university subreddits (Waterloo, Berkeley, CMU, UIUC, GaTech, NYU, UMich,
Cornell, Imperial, Oxbridge, UNSW/USYD). Search natively, via `site:reddit.com`, via old.reddit, and
via third-party Reddit search mirrors.

**Recall posts get deleted** — NDA nerves, moderator removal, or the poster getting cold feet. Check
public deleted-content mirrors and caches for threads whose titles survive in search results but
whose bodies are gone. A removed post that a mirror preserved is often the highest-signal evidence
available.

**Forums** — Blind (teamblind.com), Wall Street Oasis, QuantNet, Elite Trader, Hacker News threads,
X/Twitter recruiting-season threads.

**Question banks and platforms** — LeetCode Discuss company tags, GeeksforGeeks interview-experience
posts, HackerRank and CodeSignal discussion threads, Glassdoor filtered to the exact role title,
Levels.fyi and Interviewing.io writeups that contain real recall.

**Long tail** — GitHub repos and gists, public Google Docs and Sheets circulated by student quant
clubs, university career-center and quant-club prep documents, Quizlet decks built from real
assessments (search firm name plus "OA"), YouTube and TikTok videos where candidates narrate their
assessment, Medium and Substack, personal blogs.

## Chinese-language sources — the richest vein

Most real OA recall for these firms is written in Chinese by candidates from mainland and overseas
Chinese university pipelines. Assign this more agents than English, sharded per platform.

**Compiled recall sites (面经/笔经 aggregators — the core targets):**

| Site | Why it matters |
|---|---|
| 一亩三分地 / 1point3acres (`instant.1point3acres.com`) | Densest single source for US OA recall |
| 牛客网 / Nowcoder | Huge campus-recruiting 笔经/面经 boards |
| 应届生求职网 / Yingjiesheng | The classic 校招 board, deep 笔经 archives |
| 看准网 / Kanzhun | The Chinese Glassdoor |
| 脉脉 / Maimai | The Chinese Blind — anonymous workplace and recruiting talk |
| 实习僧 / Shixiseng | Internship-specific |

Also 拉勾 and 大街网.

**Forum / BBS layer (the Chinese Reddit equivalents):**
百度贴吧 / Baidu Tieba (per-firm and per-university bars) · 豆瓣小组 / Douban groups ·
水木社区 / newsmth (`newsmth.net` — the Tsinghua BBS; its 求职 and 校招 boards are an old,
high-quality, routinely overlooked archive) · 北大未名 BBS and other university BBSes ·
知乎 / Zhihu (long-form answers to "XX 的面试是什么体验") · V2EX · 虎扑 / Hupu ·
小木虫 / muchong · Chiphell.

**Social and video:**
小红书 / Xiaohongshu (heavy recruiting-experience content, often image posts — read captions and
comments) · 微博 / Weibo · Bilibili (candidates narrate whole OAs on video; read the description and
the 弹幕/comments) · 抖音 / Douyin.

**Long-form article platforms:**
WeChat public accounts (`mp.weixin.qq.com`) · CSDN · 掘金 / Juejin · 简书 / Jianshu ·
博客园 / cnblogs · 知乎专栏.

**Shared compilation documents — high yield, usually missed:**
Students circulate compiled 面经 in public collaborative docs. Follow public links to
语雀 / Yuque knowledge bases, 石墨文档, 飞书 / Lark docs, and Google Docs and Sheets shared in
Chinese forums. Search GitHub for Chinese repo and file names — `面经`, `笔试`, `量化`, `实习`,
`真题` — not just English ones.

Compilations are secondhand by nature. Treat one as a **pointer**: chase each item back to its
original post where possible; where you cannot, ship it as `access: compilation_only`.

## Search craft

**Do not translate English queries.** Use native vocabulary, combined as firm × role × cycle ×
recall-type.

| Term | Meaning |
|---|---|
| 面经 | interview recall |
| 笔经 | written-test recall |
| 笔试 / 网测 | written test / online test |
| 真题 | actual past questions |
| 题库 | question bank |
| 手撕 | live coding |
| 校招 | campus recruiting |
| 2026届 | 2026 graduating cohort |
| 实习 / 暑期实习 / 日常实习 | internship variants |
| 量化交易员 / 量化研究员 | quant trader / quant researcher |
| 面试流程 | interview process |
| 时间限制 / 几道题 | time limit / how many questions |
| 挂了 | got rejected |
| 求米 / 加米 | 1point3acres points-economy phrases that appear in genuine recall posts |

**Chinese firm names and nicknames:** 世坤 (WorldQuant) · 简街 (Jane Street) · 城堡 (Citadel) ·
光速 (Jump, colloquial) · 千禧 (Millennium) · 德劭 (D. E. Shaw) · 两西格玛 / 两西 (Two Sigma).

Many firms are simply written in Latin script inside Chinese posts (SIG, Optiver, IMC, HRT, DRW), so
run **mixed-script queries**: `SIG 量化 实习 面经`, `Optiver 笔试 2026届`, `Jane Street 面经 实习`.

**Use Chinese search engines.** Baidu, Sogou (搜狗), and Bing China index forum content Google misses
entirely. Critically, **WeChat articles are not in Google's index** — reach them through Sogou's
WeChat search vertical or via `mp.weixin.qq.com` links posted in forums.

**Use each platform's native search** (Zhihu, Xiaohongshu, Bilibili, Nowcoder, 1point3acres). It
surfaces material no external crawler has.

## Chat platforms

Real-time chat carries the freshest recall, often days ahead of the forums, and is the hardest to
reach honestly. Rule: **take what is genuinely public, log the rest as blocked.**

- **Discord** — quant-prep, trading, university quant-club, and OA-discussion servers. Find them via
  server-listing directories (Disboard and similar), via invite links posted in Reddit and forum
  threads, and via search engines indexing servers with public read-only channels or web-visible
  archives. Some communities post recruiting-season recap channels publicly. Where a server requires
  an account, mark `blocked: requires_membership` and move on. Do not join.
- **QQ 群 and WeChat 群** — the dominant venue for Chinese campus-recruiting coordination, rarely
  readable directly. Catch the spillover instead: group numbers, screenshots, and pasted 面经 dumps
  get reposted into Tieba, Douban, Nowcoder, Xiaohongshu, and Yuque docs constantly. Cite the public
  repost and record that its upstream was a chat group.
- **Telegram** — public channels are web-readable at `t.me/s/<channel>` without an account.

Screenshot evidence is strong about content but cannot be byte-verified as a quote. Transcribe it,
mark `access: screenshot_only`, cap at Tier C.

## Access discipline

Publicly reachable pages only. No account creation, no joining private servers, no defeating logins
or paywalls, no hammering — respect rate limits and back off on 429s.

When a source is login-walled (Glassdoor, 1point3acres, and Nowcoder frequently gate full threads),
record what the public snippet shows and mark `access: snippet_only`. Snippet-only evidence is real
evidence and it ships. Pretending you read the full thread is fabrication.
