# Tier B (broad) harvest log

Output: `/workspace/harvest/raw/tier_b_broad.jsonl` — **195 records, 26 firms**, all lines valid JSON, all controlled-vocabulary fields conforming, every record carries a non-empty `doubt`.

---

## 1. Method and network reality

`WebSearch` was the primary engine; its Highlights blocks return large verbatim excerpts from sites that refuse direct fetching, which is the only way material from 1point3acres reached this dataset. `WebFetch` was used to promote a candidate to `access: "full_text"` wherever the host allowed it.

**Confirmed fetchable this session** (used, yielded):
`wallstreetoasis.com` (the single largest source, 150 records), `nowcoder.com`, `cxyclub.cn`, `medium.com`, `gresearch.com` (PDFs, via `curl` + `pdftotext`), `cdn.mwam.com` (PDF).

**Confirmed blocked / unusable this session:**

| Host | Behaviour | How handled |
|---|---|---|
| `1point3acres.com` | blocked to WebFetch | search highlights only; all 17 records marked `snippet_only` + `websearch_snippet` |
| `reddit.com` | blocked | no records sourced from it |
| `zhihu.com`, `tieba.baidu.com` | blocked | no records |
| `glassdoor.com` | blocked | no records |
| `wallstreetoasis.com/company/virtu-financial/interview/quant-research` | fetch **timed out** (rest of the WSO domain was fine) | 2 Virtu records downgraded to `snippet_only` and the timeout noted in `doubt` |

A second, structural obstacle on 1point3acres: several threads put their body behind a karma wall (`本帖隐藏的内容需要积分高于 188`). For the Squarepoint NG QR and Point72 Cubist threads I could see only the first question or two before the wall; that truncation is recorded in each `doubt`.

---

## 2. Queries run (this session's continuation; ~20 distinct, on top of the earlier waves)

Searches marked **YIELD** produced at least one record.

### English, WSO/forum-targeted
1. `site:wallstreetoasis.com XTX Markets interview questions asked` — no XTX content returned; engine substituted IMC/HRT/Valkyrie pages.
2. `Maven Securities interview questions "they asked" trader intern wallstreetoasis` — surfaced only vendor pages, but revealed the WSO company page exists → **YIELD** (indirect)
3. `Mako Trading Global Markets interview questions asked wallstreetoasis graduate trader` — **YIELD**
4. `Vivienne Court Trading interview questions asked graduate trader experience` — firm marketing pages only, no candidate recall
5. `site:wallstreetoasis.com "Point72" OR "Cubist" quantitative researcher intern interview questions asked` — Point72 page fetched; fundamental-equity only, no quant items
6. `site:wallstreetoasis.com Balyasny quantitative researcher interview questions asked` — **YIELD**
7. `site:wallstreetoasis.com Bridgewater Associates investment associate interview questions asked` — **YIELD**
8. `site:wallstreetoasis.com Quantlab Financial OR "Radix Trading" OR "Vatic Labs" interview questions` — empty for all three
9. `site:wallstreetoasis.com "PDT Partners" OR "Voleon" OR "Arrowstreet" interview questions asked` — empty for all three
10. `site:wallstreetoasis.com "Maven Securities" interview` — **YIELD** (biggest single find of the session)
11. `site:wallstreetoasis.com "Tower Research" OR "Latour Trading" OR "Group One" OR "Chicago Trading Company" intern interview questions 2026` — all already covered, no new items
12. `site:wallstreetoasis.com "Man Group" OR "AHL" OR "Qube Research" quantitative analyst intern interview questions asked` — Qube items all already in the file
13. `site:wallstreetoasis.com "Quantlab" OR "Vatic" OR "Voleon" OR "Arrowstreet" interview "Interview Questions"` — empty
14. `XTX Markets "online assessment" OR "maths test" reddit "they asked" quant researcher graduate experience` — vendor pages only
15. `"Grasshopper" trading Singapore interview questions asked trader intern reddit experience` — firm blog + job boards only
16. `"Tibra" OR "Vivienne Court" OR "Optiver Sydney" graduate trader interview questions asked whirlpool OR reddit Australia` — surfaced the Whirlpool archive (see §5)

### Chinese / mixed-script
17. `世坤 WorldQuant 面经 实习 笔试 真题 算法` — **YIELD** (cxyclub written test)
18. `Flow Traders 笔试 面经 实习 序列 sequences 题` — **YIELD** (1point3acres HK trader intern OA)
19. `Squarepoint Capital 面经 OR Qube OR "G-Research" 笔试 题 实习 量化 牛客` — **YIELD** (1point3acres `sqp` collection page)
20. `1point3acres Squarepoint qr intern 面经 coding 概率 面试题` — **YIELD**
21. `1point3acres "Cubist" OR "Point72" quant researcher 面经 题 实习 概率` — **YIELD** (Cubist ML pod thread)
22. `XTX Markets 笔试 面经 实习 量化` — nothing but vendor pages
23. `nowcoder 牛客 Tower Research OR Qube OR "Jump Trading" OR "Optiver" 量化 实习 面经 概率题 2026` — vendor pages only
24. `nowcoder.com 面经 Millennium 千禧 OR "Tower Research" OR "Squarepoint" 量化 实习 一面 题目` — one 1point3acres industry-overview thread, no questions
25. `"Da Vinci" OR "Flow Traders" OR "IMC" 香港 新加坡 trader intern OA 面经 1point3acres 序列题 心算` — vendor pages only

---

## 3. URLs opened, and whether they yielded

| URL | Method | Yield |
|---|---|---|
| `wallstreetoasis.com/company/mako-global/interview` | webfetch | **10 records** |
| `wallstreetoasis.com/company/maven-securities/interview` | webfetch | **20 records** |
| `wallstreetoasis.com/company/squarepoint-capital/interview` | webfetch | **11 records** |
| `wallstreetoasis.com/company/balyasny-asset-management/interview` | webfetch | **6 records** |
| `wallstreetoasis.com/company/bridgewater/interview` | webfetch | **3 records** |
| `wallstreetoasis.com/company/point72/interview` | webfetch | 0 — 213 entries, all fundamental/discretionary; the only quant-adjacent line is "Leetcode medium" with no problem attached |
| `wallstreetoasis.com/company/virtu-financial/interview/quant-research` | webfetch **timed out** | 2 records via search highlight instead |
| `wallstreetoasis.com/company/qube-research-and-technologies/interview` | (earlier) | already fully harvested; re-check found no new items |
| `1point3acres.com/bbs/collection/253315` (`sqp`) | snippet | **6 Squarepoint records** |
| `1point3acres.com/bbs/thread-1116580-1-1.html` (Squarepoint NG QR) | snippet | 2 records |
| `1point3acres.com/bbs/thread-1175215-1-1.html` (Point72 Cubist ML 电面) | snippet | **2 records** |
| `1point3acres.com/bbs/thread-1150816-1-1.html` (Flow Traders HK trader intern) | snippet | 1 record |
| `nowcoder.com/discuss/481798326732455936` (WorldQuant 量化分析师 一面) | webfetch | already harvested earlier; re-verified verbatim |
| `cxyclub.cn/n/8051/` (WorldQuant 笔试题) | webfetch | **4 records**, all `compilation_only` |
| `forums.whirlpool.net.au/archive/762684` | webfetch (181 KB) | 0 for this shard — see §5 |
| `wallstreetoasis.com/company/vatic-labs` | snippet | 0 — one 2017 Developer entry, no questions |
| `wallstreetoasis.com/company/pdt-partners` | snippet | 0 — two entries (2013, 2015), no questions |
| `wallstreetoasis.com/company/arrowstreet-capital-limited-partnership` | snippet | 0 — one 2025 Intern entry, no questions |
| `grasshopperasia.com/a-day-in-the-life-of-a-grasshopper-quant/` | snippet | 0 — employee profile, no assessment content |
| `vivcourt.jp/graduate-trader.html`, `vivcourt.com/*` | snippet | 0 — firm-authored process description ("Online technical – sequences, probability, statistics"), no questions |

---

## 4. Firms that came back COMPLETELY EMPTY (a real finding)

Eleven of the named shard firms produced **zero** harvestable questions:

| Firm | What I established | Why nothing |
|---|---|---|
| **XTX Markets** | Six searches, English and Chinese. **Every single result was a prep vendor** — techinterview.org, quantt.co.uk, quantblueprint.com, scoutify.com. Not one first-person recall exists in the indexed web. | XTX appears to have unusually effective NDA discipline, or the very low reported pass rate means few candidates get far enough to have anything to report. The much-discussed "distinctive maths test" is described only by vendors, never by a candidate. **Treat all XTX question content in circulation as vendor-manufactured until a real recall surfaces.** |
| **Quantlab** | No WSO company page with questions; nothing on forums | genuinely absent |
| **Radix Trading** | One WSO forum thread, which is a person *asking* about the process, not describing it | genuinely absent |
| **Vatic Labs** | WSO page exists; one 2017 Developer entry with no question text | genuinely absent |
| **PDT Partners** | WSO page exists; entries from 2013 and 2015, no question text | genuinely absent |
| **Voleon** | nothing anywhere | genuinely absent |
| **Arrowstreet** | WSO page exists; one 2025 Investment Research intern entry with no question text | genuinely absent |
| **Vivienne Court / VivCourt** | Rich *firm-authored* content (careers pages, graduate Q&As) naming the stages — "Online technical – sequences, probability, statistics" — but no candidate ever states a question | firm markets itself heavily; candidates don't post |
| **Grasshopper (Asia)** | Careers pages, a "Day in the Life of a Grasshopper Quant" blog, Greenhouse postings. No recall anywhere. | small Singapore firm, low candidate volume |
| **Latour Trading** | no distinct presence separate from Tower | — |
| **Point72 (discretionary side)** | 213 WSO entries fetched in full. Wonderlic + case study + stock pitch throughout; **not one quantitative item**. | The quant hiring happens under **Cubist**, which is where the 2 records I did get came from. Anyone treating "Point72" and "Cubist quant" as one pipeline is wrong. |

Two more shard firms are present but thin: **Man Group** (1), **Headlands** (1), **Millennium** (3), **PEAK6** (3), **Belvedere** (3), **AQR** (3).

---

## 5. Sources rejected, and why

**Prep vendors / content farms (hard exclusions, treated as negative evidence).** These dominated results for XTX, Maven, Mako, Flow Traders and Da Vinci:
`tradinginterview.com`, `tradermath.org`, `quantt.co.uk`, `quantblueprint.com`, `techinterview.org`, `scoutify.com`, `prachub.com`, `myntbit.com`, `interviewchamp.ai`, `quantvault.org`, `quantprep.io`, `jorb.ai`, `attcareer.com`, `ftp.kontos.com`.

`attcareer.com` deserves a specific note: its "G-Research 量化研究员求职完全攻略 2026：真题解析" markets itself as 真题 (real past questions) in the title, then closes by selling a "Quant Track" with a G-Research module. That is the Chinese-language vendor tell exactly as described in the brief. **Rejected.**

**Whirlpool `forums.whirlpool.net.au/archive/762684`** (181 KB, 4,552 lines) is a genuine, high-quality Australian first-person thread — but it is about **Optiver**, which is another shard's firm. It mentions Tibra 19 times, all of it about the Optiver-v-Tibra litigation. The one apparent Tibra question in it is a **trap**: user "Roohif," evidently a Tibra insider, walks through a cricket-match market-making exercise and then says *"It took me a while to think up the cricket example, and I'm starting to think that if I think of another good example, I might actually put it in the Tibra test"* — future tense. It is his own invention, **not an asked question. Rejected.** I flag this because the passage would read to a careless harvester like a genuine Tibra recall.

**WSO's own editorial pages** (`/resources/interviews/*`) are listicles with sample answers, not recall. Rejected wherever the search engine surfaced them.

---

## 6. Firms ADDED that were not on the shard list

Carried over from the earlier waves and retained: **Marshall Wace** (7, from the firm's own Quant Associate Programme Process Guide PDF on `cdn.mwam.com` — official-document provenance, the strongest class in the file), **Valkyrie Trading** (1), **Ingensoma Arbitrage** (1), **Da Vinci Derivatives** (14 — Da Vinci *is* on the APAC/EU list). Each carries an off-shard note in its `doubt`.

---

## 7. What I could NOT establish

- **No individual item from any speeded mental-math or sequences test, at any firm.** I have the shape of many of them and can now state it with multi-source confidence — Flow Traders 60-in-6 plus 26 sequences in 25 min (Hong Kong intern, 2025); Maven 18 probability in 30 min with negative marking, then two 6-minute mental-math/sequences tests (London intern, 2025), corroborated independently by a Chicago grad candidate in Jan 2026; Mako 37-in-15. **But nobody ever reproduces a question.** These are the most-discussed and least-documented assessments in quant recruiting, and the vacuum is exactly the niche the vendors occupy.
- **Whether the three polished Maven QR-intern questions are real.** They are the best-written questions in the entire file (optimal stopping on a random walk, adverse-selection quoting, Bayesian coin) and I do not trust the wording. All three come from one WSO submission whose register is uniformly second-person textbook prose, unlike every other entry on that page, and which was filed 14 months after the interview. Provenance is real (dated, division-specific, outcome-stated), so per the brief they are in — but each `doubt` says plainly that the wording may be AI-assisted reconstruction. **Do not treat these as verbatim.**
- **Levels for 75 of 195 records (38%).** WSO's job-title field frequently does not distinguish internship from new-grad ("Junior Trader", "Quant", "Analyst"). I used `unknown` rather than guess. Internships are 71 records across 16 firms.
- **Dates for the 1point3acres records.** The site shows an interview-window tag (e.g. `2025(10-12月)`) or an edit timestamp, but often no post date; those are `post_date: "unknown"`.
- **Whether any XTX candidate recall exists at all.** See §4. This is the largest single coverage gap and I do not believe it is a search-craft failure.

## 8. Verifier notes

- 35 records are `snippet_only`. For the 17 on 1point3acres, **a verifier re-fetching the URL will fail** — the host blocks bots and karma-walls the bodies. The quoted text is what the search engine returned as a verbatim highlight; nothing was paraphrased. Every such record says so in `doubt`.
- 4 records (`cxyclub.cn`) are `compilation_only`: a 2011 forum repost of a c.2007 WorldQuant China written test that the poster says outright he found online. I fetched that page in full, so the quotes verify, but the *attestation* is second-hand and the questions are ~19 years old.
- One WorldQuant record's source page renders part of the original Chinese with stray Cyrillic characters; the surviving clean text was used for `source_quote`.
- **Nine `source_quote` values are under 40 characters, deliberately.** Five are Chinese (17–38 chars, which is 50–115 bytes and highly specific), and four are short English question items quoted exactly out of WSO's structured "Interview Questions" field (e.g. `Which one is larger 10^40 or 40!?`). In every one of these cases the adjacent text on the page sits across a paragraph break, so padding the quote to clear 40 characters would have meant splicing a non-contiguous run and *causing* a verification failure. Each of these is exact, contiguous, and directly attests the question rather than describing it. The Chinese forum quotes in particular could not be lengthened at all: 1point3acres injects anti-scraping tokens (`.1point 3acres`, `.google и`) between adjacent recall items, so the per-item fragment is the longest safely contiguous run available.
