# Quant OA & Interview Question Harvest — Evidence Factory Prompt

A single copy-pasteable prompt for an agentic tool (Cursor Cloud Agent, Claude Code, Codex, etc.)
with web access and the ability to spawn many parallel subagents and run Python.

> **Using Cursor?** Prefer the skill at `.cursor/skills/quant-question-harvest/`, which is the same
> method as an invocable, parameterized `/quant-question-harvest <firm and role>` with the source
> lists split into on-demand references. This file is the standalone variant for tools without skill
> support, and hardcodes SIG quant trader internship as the target.

It harvests **actually-asked** quant online-assessment and interview questions from first-person
candidate recall posts — English forums, the much larger Chinese 面经/笔经 ecosystem, and the public
chat layer — and publishes them as many parallel per-source **streams** for a human with real
domain experience to triage by eye.

Two design assumptions:

1. The hard problem is not finding questions. It is that a language model will cheerfully invent 400
   plausible SIG questions, and plausible is indistinguishable from real by inspection. So every
   mechanism here exists to make fabrication *mechanically* detectable: verbatim quotes re-checked
   against live pages by script, plus seeded forgeries and positive controls that measure the
   filter's precision and recall.
2. The division of labor is that **the machine guarantees provenance and the human judges
   plausibility.** That inverts the usual instinct to hand back a small, confidently-filtered set.
   The agent is explicitly forbidden from discarding a provenance-verified question just because it
   doubts it; it labels the doubt and ships, so the human's option set is never silently narrowed.

Copy everything below the horizontal rule.

---

# MISSION

You are the **Chief Archivist** of an evidence factory. Your product is not an essay and not a
study guide. It is a **provenance-complete corpus of real quantitative-finance assessment
questions**, shipped as a git repository, where every single question is traceable to a specific
human being who said, in public, on a dated post, that they were asked it.

The corpus must answer: *what is actually on the test, at which firm, for which role, in which
round, in which recruiting cycle?*

**Primary target, non-negotiable:** Susquehanna International Group (SIG), **Quantitative Trader
internship** pipeline — the intern-track online assessments specifically, not full-time, not the
software-engineering track, not the general "SIG interview questions" slop. If this shard comes back
thin, you have failed the assignment regardless of how good the rest of the corpus is. Treat SIG QT
intern as its own mission with its own agents, its own dead-end log, and its own section in the
report.

**Budget is not a constraint.** Spend agents, tokens, wall-clock, and search queries freely.
Under-spending is a defect. Do not ask me questions — resolve ambiguity by collecting more evidence
and reporting the disagreement.

## The division of labor — read this twice

**You are not the final judge of whether a question is real. I am.** I have sat these assessments
and I can tell a genuine SIG sequences item from a laundered textbook problem by looking at it. What
I cannot do is check four hundred URLs.

So the split is:

- **You guarantee provenance.** That a specific human posted this specific text, at this specific
  live URL, on this specific date, describing this specific firm and round. This is a factual claim
  you can verify mechanically, and you are held to it absolutely.
- **I judge plausibility.** Whether the question smells like the real test.

Two consequences, and they cut in opposite directions, so hold both:

1. **Fabrication is fatal.** Delivering 150 provenance-verified questions is a success. Delivering
   500 of which 80 are invented is a *total* failure — one fake I catch means I cannot trust the
   other 499, and the whole artifact goes in the bin. Every question you write must be one you read
   at a URL you actually opened.
2. **Over-filtering is nearly as bad.** Do not throw away a question because *you* find it
   implausible. Your taste is worse than mine here. If the provenance is real, it ships — tagged
   with your doubts, sorted below the strong material, but it ships. A question you silently dropped
   is one I never get to judge.

The corpus should therefore be **wide**. Many parallel streams, high volume, every item carrying its
receipts, sorted so the strongest is on top and the weakest is clearly labeled — not a small
pre-digested set reflecting your judgment of what I want.

---

# 1. WHAT COUNTS AS A REAL QUESTION

## 1.1 In scope

A question is **in scope** only if a human publicly reported encountering it in an actual
assessment or interview at a named firm. The canonical shape of admissible evidence is a
first-person recall post: *"Did the SIG QT intern OA yesterday, second section was 20 sequence
questions in 10 minutes, one of them was ..."*

Admissible round types:

- **OA / online assessment** — timed, auto-administered (HackerRank, CodeSignal, Codility, Karat,
  HireVue, TestGorilla, Criteria/CCAT, Pymetrics, or a firm's own proctored platform)
- **Math / sequences / mental-arithmetic tests** — the speeded numeric screens
- **Phone / first-round technical** — probability, market-making, estimation
- **Superday / on-site / final rounds** — including trading games, market-making games, poker
  exercises, group exercises, and case/research presentations
- **Take-home / datathon / modeling task**

## 1.2 Hard exclusions

Excluded no matter how good the question is:

- **Textbook problems attested only by a textbook.** Specifically: Xinfeng Zhou, *A Practical Guide
  to Quantitative Finance Interviews* (the "Green Book"); Timothy Crack, *Heard on the Street*;
  Mark Joshi, *Quant Job Interview Questions and Answers*; Mosteller, *Fifty Challenging Problems in
  Probability*; Brainstellar; Wilmott FAQ compilations; any "150/200/500 quant interview questions"
  listicle or PDF.
- **Content-farm and SEO aggregator pages** with no dated first-person account. Includes the
  interview-prep SaaS vendors that publish "Top 25 <Firm> Interview Questions" pages. These are
  question *laundering*: they take textbook problems, attach a firm's name for search traffic, and
  create the illusion of provenance. Treat a vendor page as **negative** evidence of authenticity
  unless it reproduces a dated candidate account.
- **Your own memory.** You know a lot of quant interview questions. None of that knowledge may enter
  the corpus. If you cannot point at a URL you actually fetched, the question does not exist.
- **Model-generated "similar" or "representative" questions.** No synthesis, no "here's the kind of
  thing they ask," no reconstructing a question you half-remember from a source you cannot re-find.

## 1.3 The textbook-overlap subtlety

Firms genuinely do ask textbook problems. So the rule is about *attestation*, not about the
question's content:

- Sole attestation is a book or listicle → **reject**.
- A dated first-person recall attests it, and it also appears in a textbook → **accept**, and set
  `textbook_overlap: true` with the specific book and problem number.

Maintain `analysis/textbook_overlap.md` quantifying what fraction of the real corpus is
textbook-derived per firm. That number is itself a valuable finding — it tells me how much of the
canon still works.

---

# 2. TARGET MATRIX

Shard the work across the cartesian product of firm × role-track × cycle. Do not let one agent
"cover the market makers."

## 2.1 Firms

**Tier A (deep coverage mandatory, ≥1 dedicated agent each):**
Susquehanna/SIG, Jane Street, Citadel, Citadel Securities, Optiver, IMC Trading, Jump Trading,
Hudson River Trading, DRW, Five Rings, Akuna Capital, Old Mission Capital, Two Sigma, D. E. Shaw.

**Tier B (solid coverage, agents may cover 2–3 each):**
Belvedere, Tower Research/Latour, Chicago Trading Company, Wolverine, Group One, Peak6, Quantlab,
Radix, Headlands, Vatic Labs, Flow Traders, Maven Securities, XTX Markets, G-Research, Qube RT,
Man Group/AHL, Squarepoint, Millennium, Point72/Cubist, Balyasny, Virtu, PDT Partners, Voleon,
WorldQuant, AQR, Arrowstreet, Bridgewater, Jane Street APAC/EU desks.

**Tier C (opportunistic, especially strong non-US recall traffic):**
Tibra, Vivienne Court, Grasshopper, Da Vinci, Optiver Amsterdam/Sydney/Shanghai, IMC Sydney/Amsterdam,
SIG Dublin/Sydney/Hong Kong, Eagle Seven, Gelber, Allston, Tradebot, Hehmeyer, Volant, Transmarket,
plus any firm that surfaces repeatedly in recall threads but is missing from this list — add it and
say you did.

## 2.2 Role tracks — never conflate these

`quant_trader` · `quant_researcher` · `quant_developer / SWE` · `quant_analyst` ·
`data_scientist` · `discretionary_trader`

## 2.3 Level

`internship` (**prioritized**) · `new_grad` · `experienced` · `phd_new_grad`

An internship OA and a full-time OA at the same firm are frequently different tests. A record that
cannot establish which one it was gets `level: unknown` and is capped at Tier C. Never silently
promote a full-time question into the internship set — this is the single most common way these
corpora go wrong, and it is the specific failure mode I care most about avoiding.

## 2.4 Cycle

Tag every record with the recruiting cycle (e.g. `Summer 2026`, `Summer 2025`). **Weight recency
heavily**: current and prior cycle first, then back three cycles, then older only if the question
recurs. Firms rotate question pools and switch assessment vendors; a 2019 recall is archaeology, not
intelligence. Build `analysis/format_drift.md` recording, per firm, when the format demonstrably
changed (vendor switch, new section, changed timing) and cite the recalls that show it.

## 2.5 Quotas

Targets, not licenses to pad. Missing a quota honestly is fine and gets reported; hitting one with
invented records is the failure described in the mission. Because I do the plausibility filtering,
these counts are **all provenance-verified tiers combined (A through D)**, not Tier A+B only.

| Scope | Target | Floor below which the shard is reworked |
|---|---|---|
| SIG, quant trader, internship | 120 | 40 |
| Each remaining Tier-A firm | 50 | 15 |
| Each Tier-B firm | 20 | 5 |
| Corpus total | 900 | — |
| Distinct streams published | ≥60 | — |
| Chinese-sourced share of corpus | ≥40% | — |
| Current + prior cycle share | ≥50% | — |
| Tier A+B share | ≥40% | — |

Rework means sending fresh agents at the shard with different query formulations and different
source families — not relaxing the rubric until the number goes up.

---

# 3. WHERE REAL RECALLS ACTUALLY LIVE

Do not run five Google searches and declare the internet exhausted. Work every source family below,
and log coverage per family per firm in `SOURCES.md`, including the ones that produced nothing.

## 3.0 English-language sources

Reddit — r/quant, r/quantfinance, r/FinancialCareers, r/csMajors, r/leetcode, r/cscareerquestions,
and university subreddits (Waterloo, Berkeley, CMU, UIUC, GaTech, NYU, UMich, Cornell, Imperial,
Oxbridge, UNSW/USYD). Search Reddit natively, via `site:reddit.com`, via old.reddit, and via
third-party Reddit search mirrors. **Recall posts get deleted** — NDA nerves, moderator removal, or
the poster getting cold feet — so also check public deleted-content mirrors and cached copies for
threads whose titles survive in search results but whose bodies are gone. A removed post that a
mirror preserved is often the highest-signal evidence in the corpus.

Blind (teamblind.com) · Wall Street Oasis · QuantNet · Elite Trader · Hacker News threads ·
X/Twitter recruiting-season threads.

**Question-bank and coding platforms:**
LeetCode Discuss company tags · GeeksforGeeks interview-experience posts · HackerRank and CodeSignal
discussion threads · Glassdoor per-company pages filtered to the exact role title ·
Levels.fyi and Interviewing.io writeups where they contain real recall.

**Long tail:**
GitHub repos and gists collecting OA questions · public Google Docs and Sheets circulated by student
quant clubs · university career-center and quant-club prep documents · Quizlet decks built from real
assessments (search firm name plus "OA") · YouTube and TikTok videos where candidates narrate their
assessment · Medium and Substack writeups · personal blogs.

## 3.1 Chinese-language sources — the richest vein, worked hardest

Most real OA recall for these firms is written in Chinese by candidates from mainland/overseas
Chinese university pipelines. If your Chinese-language yield is not several times your
English-language yield, you have under-worked this section. Assign it more agents than English.

**Compiled recall sites (面经/笔经 aggregators — the core targets):**
一亩三分地 / 1point3acres (`instant.1point3acres.com` — the single densest source for US OA recall) ·
牛客网 / Nowcoder (`nowcoder.com` — 笔经/面经 discussion boards, huge campus-recruiting traffic) ·
应届生求职网 / Yingjiesheng (`yingjiesheng.com` — the classic 校招 board, deep 笔经 archives) ·
看准网 / Kanzhun (the Chinese Glassdoor) · 脉脉 / Maimai (the Chinese Blind, strong for anonymous
workplace and recruiting talk) · 实习僧 / Shixiseng (internship-specific) · 拉勾 · 大街网.

**Forum / BBS layer (the Chinese Reddit equivalents):**
百度贴吧 / Baidu Tieba (per-firm and per-university bars) · 豆瓣小组 / Douban groups (job-hunting
groups are active and searchable) · 水木社区 / newsmth (`newsmth.net` — the Tsinghua BBS; its
job-hunting and 校招 boards are an old, high-quality, frequently-overlooked archive) ·
北大未名 BBS and other university BBSes · 知乎 / Zhihu (long-form answers to "XX 的面试是什么体验") ·
V2EX · 虎扑 / Hupu · 小木虫 / muchong (academic job boards) · Chiphell.

**Social and video:**
小红书 / Xiaohongshu (RedNote — heavy recruiting-experience content, often as image posts, so read
the captions and comments) · 微博 / Weibo · Bilibili (candidates narrate whole OAs on video;
read the video description and the 弹幕/comments) · 抖音 / Douyin.

**Long-form article platforms:**
WeChat public accounts (`mp.weixin.qq.com`) · CSDN · 掘金 / Juejin · 简书 / Jianshu ·
博客园 / cnblogs · 知乎专栏.

**Shared compilation documents — high yield, usually missed:**
Students circulate compiled 面经 in public collaborative docs. Search for and follow public links to
语雀 / Yuque knowledge bases, 石墨文档, 飞书 / Lark docs, Google Docs and Sheets shared in Chinese
forums, and GitHub repos with Chinese names (search `面经`, `笔试`, `量化`, `实习`, `真题` as repo
and file names, not just English). These compilations are secondhand by nature, so treat the
compilation as a **pointer**: chase each item back to its original post where possible, and where
you cannot, ship it labeled `access: compilation_only`.

**Search craft — this is where most agents fail:**
Do not translate English queries. Use the native vocabulary and combine it as
firm × role × cycle × recall-type:
面经 (interview recall) · 笔经 (written-test recall) · 笔试 (written test) · 真题 (actual past
questions) · 题库 (question bank) · 手撕 (live coding) · OA · 网测 (online test) ·
实习 / 暑期实习 / 日常实习 (internship variants) · 校招 (campus recruiting) · 2026届 (2026 cohort) ·
量化交易员 (quant trader) · 量化研究员 (quant researcher) · 面试流程 (interview process) ·
时间限制 (time limit) · 几道题 (how many questions) · 挂了 (got rejected) · 求米 / 加米 (the
1point3acres points-economy phrases that appear in genuine recall posts).

Use Chinese firm names and nicknames alongside English ones: 世坤 (WorldQuant) · 简街 (Jane Street) ·
城堡 (Citadel) · 光速 (Jump, colloquial) · 千禧 (Millennium) · 德劭 (D. E. Shaw) · 两西格玛 /
两西 (Two Sigma) · 老虎 · plus firms that are simply written in Latin script inside Chinese posts
(SIG, Optiver, IMC, HRT, DRW), which means you must run mixed-script queries like
`SIG 量化 实习 面经` and `Optiver 笔试 2026届`.

**Use Chinese search engines, not just Google.** Baidu, Sogou (搜狗), and Bing China index Chinese
forum content Google misses entirely. Critically, **WeChat articles are not in Google's index** —
reach them through Sogou's WeChat search vertical or through direct `mp.weixin.qq.com` links posted
in forums. Also use each platform's *native* search (Zhihu, Xiaohongshu, Bilibili, Nowcoder,
1point3acres), which surfaces material no external crawler has.

## 3.2 Chat platforms — Discord, QQ, WeChat, Telegram

Real-time chat is where the freshest recall lands, often days before it reaches a forum. It is also
the hardest to reach honestly, so the rule is: **take what is genuinely public, and log the rest as
blocked rather than guessing at its contents.**

- **Discord** — quant-prep, trading, university quant-club, and OA-discussion servers. Find them via
  server-listing directories (Disboard and similar), via invite links posted in Reddit and forum
  threads, and via search engines indexing servers that expose public read-only channels or publish
  web-visible archives and transcripts. Some communities post recruiting-season recap channels
  publicly. Where a server needs an account to read, mark it `blocked: requires_membership` and move
  on — do not join, and do not speculate about what is inside.
- **QQ 群 and WeChat 群** — the dominant venue for Chinese campus-recruiting coordination. You will
  rarely read them directly. What you *can* do is catch their spillover: group numbers, screenshots,
  and pasted 面经 dumps get reposted into Tieba, Douban, Nowcoder, Xiaohongshu, and Yuque docs
  constantly. Hunt the spillover, cite the public repost, and record that its upstream was a chat
  group.
- **Telegram** — public quant and recruiting channels are web-readable at `t.me/s/<channel>` without
  an account. Search for firm names and 面经/OA vocabulary there.

For every chat source, record `source_type: chat_*` and treat screenshot-only evidence as its own
access class (§7.2): a legible screenshot of an OA is strong evidence about content but you cannot
byte-verify a quote from it, so it ships labeled and cannot reach the top tier on its own.

## 3.3 Access discipline

Stick to publicly reachable pages. Do not create accounts, defeat logins, bypass paywalls, or hammer
sites — respect rate limits and back off on 429s. When a source is login-walled (Glassdoor,
1point3acres, and Nowcoder frequently gate full threads), record what the public search snippet
shows, mark `access: snippet_only`, and label the record accordingly. Snippet-only evidence is real
evidence and it ships; pretending you read the full thread is fabrication.

---

# 4. THE FACTORY

Stations at the same tier run **in parallel** as independent subagents with isolated context. Every
handoff is a schema-valid file on disk. No station consumes another station's prose. Every station
writes a `station_report.md` covering what it did, what it could not reach, and its own confidence.

**S0 — Spec, schema, and controls.** Define `question.schema.json`, `evidence.schema.json`, and
`firm_process.schema.json`; the tiering rubric (§5); the acceptance gates. Scaffold the repo. Then
build the **control sets** described in §6 and seal them so that no collector or adjudicator can see
which items are controls. Nothing downstream starts until schemas validate.

**S1 — Process cartography (one agent per Tier-A firm).** *Before* collecting questions, map each
firm's funnel from recall posts: how many rounds, what each is called, which vendor platform, how
many sections, how many questions per section, the time limits, whether a calculator or scratch
paper is permitted, whether it is proctored. Output `firms/<firm>.yaml`. This map is load-bearing
twice over: it tells collectors what to search for, and it gives adjudicators a consistency prior —
a "SIG QT intern OA question" that claims a format contradicting every mapped account of that OA is
probably fabricated.

**S2 — English collection (≥25 parallel agents, sharded by firm × source-family).** Each agent works
its shard exhaustively: multiple query formulations, multiple search engines, pagination past page
one, following intra-thread links and "see my other post" references, and mining the comment trees
where the actual questions usually are. Each agent must log every query it ran and every URL it
opened, including the duds.

**S3 — Chinese collection (≥20 parallel agents — more than S2, deliberately).** Same firm shards,
but sharded again across the §3.1 platform families so that 1point3acres, Nowcoder, Yingjiesheng,
Xiaohongshu, Zhihu, Tieba, newsmth, Bilibili, WeChat-via-Sogou, and the shared-doc layer each get a
dedicated agent rather than one agent nominally "covering Chinese sources." Run native-language
queries only. Preserve original text verbatim in `source_quote`; put the English rendering in
`question_text_en`. Never overwrite the original with a translation — I want to read the Chinese.

**S3b — Chat-layer collection (≥4 agents).** Discord directories and publicly readable servers,
`t.me/s/` channels, and systematic hunting of QQ/WeChat-group spillover reposted into public forums
and shared docs, per §3.2.

**S4 — Extraction and normalization.** Convert each find into a schema-valid record (§7). One record
per question. Preserve the reported wording; do not "clean up" a question into textbook prose,
because the awkward specificity of real recall is itself evidence.

**S5 — Deduplication and clustering.** The same question surfaces in many wordings. Cluster
near-duplicates (embedding similarity plus numeric-parameter matching), pick a canonical statement,
and **keep every attestation attached to the cluster** — independent attestation count is the main
input to tiering, so collapsing duplicates without preserving their sources destroys the signal.
Flag cross-firm reuse explicitly: shared vendor question pools mean the same item legitimately
appears at multiple firms, and that is a finding, not a bug.

**S6 — Authenticity adjudication.** Apply §5 to assign every cluster a tier, with written reasoning.
Runs blind to the control sets.

**S7 — Textbook contamination screen.** Check every candidate against the §1.2 corpora and the
listicle ecosystem. Set `textbook_overlap`, and reject anything whose only attestation is a book or
an aggregator.

**S8 — Red team / forgery detection.** An adversarial agent whose mandate is to *prove each question
fake*: hunt for the question's earliest appearance online, check whether the "recall" post is
actually copy-paste from a listicle, check whether the account is a prep-service marketer, check
whether the claimed format contradicts S1's process map, check whether the "candidate" posted
seventeen different firms' OAs in one day. Every Tier-A/B question must survive a documented attack.

**S9 — Mechanical quote verification.** Independent of every collector: re-fetch each cited URL and
assert `source_quote` appears verbatim in the fetched text. This is a script, not a judgment call —
see §6.1. Records that fail are quarantined, not deleted, with the failure reason recorded.

**S10 — Answer keys (separate artifact).** Produce worked solutions in `solutions/`, never inside the
question files, so the corpus stays usable as a blind practice set. Mark each solution
`verified_by_source` when the source thread contained the answer or an argued consensus, versus
`derived_by_agent` when you solved it yourself. Where a thread argues about the answer, record the
dispute rather than picking a winner silently.

**S11 — Mock reconstruction.** For each firm with a well-mapped OA, assemble `mocks/<firm>_<role>.md`:
a timed paper matching the *real* section structure, question counts, and time limits from S1, drawn
only from Tier A/B questions. This is the deliverable I will actually practice against, so the
timing and section shape matter as much as the content.

**S12 — Stream publication and report.** Build the triage deck (§8) and the report (§9).

Track and report factory metrics: queries run, URLs fetched, candidates screened, records admitted,
rejects by reason, per-station defect rate, control-set performance, rework loops.

---

# 5. THE AUTHENTICITY RUBRIC

Score every cluster on evidence, then tier it. Write the reasoning down; an unreasoned tier is a
defect.

## 5.1 Positive signals

- **Independent attestation count** — the strongest signal by far. Two unrelated posters, on two
  different platforms, in the same cycle, describing the same question, is very hard to fake.
- **First-person incidental detail** — the timer, the UI, the proctoring webcam, which section they
  bombed, that they ran out of time on question 14. Fabricators write questions; real candidates
  write *experiences* with questions embedded in them.
- **Odd, specific parameters.** Real assessment questions have ugly numbers — a 7-sided die,
  \$3.75, 17 boxes, 63 seconds. Textbook and invented questions have clean ones. Weight ugliness as
  authenticity.
- **Platform-specific artifacts** — vendor name, section names, question-count-and-timer combos that
  match S1's process map, "it wouldn't let me go back," score-report screenshots.
- **Thread argument.** Replies disputing the answer, correcting the poster, or saying "I got the same
  one but with 5 instead of 6" are strong authenticity signals. Nobody argues about a fake question.
- **Dated, and consistent with the firm's actual recruiting calendar** for that role and cycle.
- **Poster history** consistent with being a candidate — other posts about the same recruiting season,
  a university affiliation, other firms' processes at plausible dates.

## 5.2 Negative signals

- Polished textbook English, or a question phrased as a puzzle rather than as a recollection.
- Appears verbatim in a §1.2 book, or on a listicle predating the "recall" post.
- No date, or a date that cannot be established.
- Source is a prep vendor, a content farm, an AI-generated blog, or a "Top N questions" page.
- Round-number parameters plus a clean canonical answer.
- Claimed process contradicts S1's map for that firm, role, and cycle.
- A single post claiming implausible breadth — every section of every firm's OA, perfectly recalled.
- Answer reads as though written by a language model.

## 5.3 Tiers are sort order, not a gate

Per §MISSION, tiers rank what I look at first. They are **not** permission to delete. Everything with
real provenance ships somewhere.

- **Tier A — Confirmed.** ≥2 independent first-person attestations, dated within three cycles, at
  least one with full-text access, consistent with the process map, survived the S8 attack.
- **Tier B — Probable.** One strong first-person attestation with rich incidental detail, dated,
  consistent with the process map, survived the S8 attack.
- **Tier C — Reported.** Attested but weakly — snippet-only, undated, secondhand via a compilation,
  screenshot-only, or role/level ambiguous. Ships in its own clearly labeled section.
- **Tier D — Unfiltered.** Provenance checks out but the §5.2 negative signals fire hard, or you
  simply doubt it. Ships anyway, in `streams/tier_d/`, with your doubt stated in one line. This tier
  exists specifically so your skepticism cannot silently shrink my option set.

**Rejected** is reserved for the four mechanical failures only: no URL; the quote does not verify
against the page; sole attestation is a textbook or listicle; or the record is a duplicate already
counted in a cluster. Rejects go to `rejects/` with reasons, because over-filtering is a failure
mode I can only catch if the pile is visible.

Report the tier distribution per firm. A firm that comes back 90% Tier C or D means that shard needs
rework, not that the firm has weak questions.

---

# 6. CALIBRATION — HOW I KNOW THE FILTER WORKS

Self-reported confidence is worthless. Measure the filter instead. This section is the reason to
trust the corpus, so it is a hard gate, not an appendix.

## 6.1 Mechanical quote gate (automated, blocking)

Ship `tools/verify_quotes.py`. For every record it re-fetches `source_url` and asserts that
`source_quote` appears as a normalized substring of the page text (whitespace-collapsed,
unicode-normalized). It records `http_status`, `retrieved_at`, and a `content_hash`, and submits
every URL to the Wayback Machine save endpoint so the evidence survives thread deletion.

**Gate: 100% of Tier A and Tier B records pass, or the pipeline does not ship.** No exceptions, no
"the site changed." A quote you cannot re-find is a quote you cannot prove you read. Records where
the page is genuinely gone but a pre-existing archive snapshot contains the quote pass on the
archive, with `access: archive_only` recorded.

## 6.2 Seeded forgeries (precision)

S0 mints **20 synthetic questions** engineered to be maximally plausible — correct firm vocabulary,
realistic parameters, fabricated-but-well-formed source URLs and post text — and injects them into
the pool that S6 and S8 adjudicate blind.

**Gate: ≥19 of 20 forgeries rejected.** Below that, the adjudication threshold is miscalibrated,
and every Tier assignment in the run is void and must be redone with a tightened rubric. Report the
exact score. If a forgery survives, quote it in the report and explain what fooled the adjudicator —
that is the most useful diagnostic in the entire artifact.

## 6.3 Positive controls (recall)

S0 also seeds **20 known-real questions** it verified by hand, injected blind. Measure how many the
pipeline admits at Tier A/B.

**Gate: ≥16 of 20 admitted.** Below that, the filter is over-tight and is silently discarding real
questions; loosen and rerun. Report the score.

## 6.4 Published error bars

`REPORT.md` states the measured precision and recall from §6.2 and §6.3 in the first section, in
numbers. "Carefully verified" is not a claim; "19/20 forgeries caught, 17/20 real questions
retained" is.

---

# 7. RECORD SCHEMA

One YAML file per question at `questions/<firm>/<role>/<id>.yaml`:

```yaml
id: sig-qt-intern-0042
firm: Susquehanna International Group
firm_aliases: [SIG, Susquehanna]
role_track: quant_trader
level: internship
cycle: Summer 2026
office: Bala Cynwyd
round: online_assessment
round_name: "Quant Test - Section 2"     # as candidates actually call it
platform: "SIG proprietary portal"
section_context:
  section_index: 2
  questions_in_section: 20
  time_limit_min: 10
  calculator_allowed: false
question_type: sequences                  # see §7.1
question_text: "…as reported, wording preserved…"
question_text_en: "…only if the original is not English…"
answer_format: numeric
reported_answer: "…if the source gives one…"
answer_status: verified_by_source         # | derived_by_agent | disputed | unknown
attestations:
  - source_url: https://…
    source_type: reddit_thread            # see §7.2
    source_quote: "…verbatim, byte-checkable substring of the fetched page…"
    source_language: en
    post_date: 2026-01-14
    retrieved_at: 2026-02-02T11:04:00Z
    archive_url: https://web.archive.org/…
    access: full_text                     # see §7.3
    poster_context: "…account history, university, other recall posts…"
independent_attestation_count: 2
tier: A
textbook_overlap: false
textbook_overlap_detail: null
cross_firm_reuse: []
red_team_attack: "…what S8 tried, and why it failed to break this record…"
adjudication_notes: "…which §5 signals fired…"
confidence_notes: "…residual doubt, stated plainly…"
```

## 7.1 `question_type` vocabulary

`mental_math_speed` · `sequences` · `probability` · `combinatorics` · `expected_value` ·
`market_making` · `betting_odds_arbitrage` · `poker_game_theory` · `fermi_estimation` ·
`logic_brainteaser` · `statistics_regression` · `options_theory` · `stochastic_calculus` ·
`linear_algebra` · `coding_algorithms` · `coding_simulation` · `sql_data` · `ml_modeling` ·
`pattern_recognition_iq` · `trading_game` · `behavioral` · `personality_assessment`

## 7.2 `source_type` vocabulary

**English:** `reddit_thread` · `blind` · `wso` · `quantnet` · `elitetrader` · `glassdoor` ·
`leetcode_discuss` · `geeksforgeeks` · `github_repo` · `student_doc` · `youtube` · `blog` ·
`x_twitter` · `hackernews`

**Chinese:** `1point3acres` · `nowcoder` · `yingjiesheng` · `kanzhun` · `maimai` · `shixiseng` ·
`zhihu` · `xiaohongshu` · `weibo` · `bilibili` · `douyin` · `tieba` · `douban` · `newsmth` ·
`university_bbs` · `v2ex` · `hupu` · `muchong` · `wechat_article` · `csdn` · `juejin` · `jianshu` ·
`cnblogs` · `yuque` · `shimo` · `lark_doc`

**Chat:** `chat_discord` · `chat_telegram` · `chat_qq_repost` · `chat_wechat_repost` · `chat_slack`

**Other:** `other` — and if you use it more than a handful of times, the vocabulary is wrong; extend
it and say so.

## 7.3 `access` vocabulary

`full_text` — you fetched and read the whole page.
`snippet_only` — login-walled; you have the public search snippet.
`archive_only` — original is gone; an archive snapshot carries the quote.
`compilation_only` — found in a secondhand compilation, original post not locatable.
`screenshot_only` — the question is legible in an image, so no byte-verifiable text quote exists.
Transcribe it, mark it, and cap at Tier C: strong evidence about content, unverifiable as a quote.

---

# 8. THE STREAM DECK — THE PRIMARY DELIVERABLE

This is what I actually consume. Everything else in the repo is supporting evidence. Build it for
one purpose: **maximum questions per minute of my attention**, so I can run down them and call real
or fake by eye.

## 8.1 Streams

Publish one file per stream at `streams/<firm>/<role>_<level>__<source_family>.md`, e.g.
`streams/sig/quant_trader_internship__1point3acres.md`. Keeping source families separate rather than
merged is deliberate: sources have characteristic reliability, and once I have read twenty items from
a stream I can judge the whole stream, which is far faster than judging items one at a time.

Each stream file opens with a five-line header — source family, firm, role, item count, date range,
tier mix — and then lists items in this exact shape, sorted best-first:

```
### Q17 · Tier B · Summer 2026 · OA section 2 (20 questions / 10 min)

<the question, exactly as reported, Chinese preserved with English underneath>

> verbatim source quote
— 1point3acres, posted 2026-01-14, retrieved 2026-02-02, full text · [link] · [archive]
  1 attestation · doubt: single poster, no corroboration found
```

Question first and prominent, evidence directly beneath, everything else compressed to one line. Do
not bury questions under paragraphs of adjudication prose — your reasoning belongs in the YAML
records, not in my reading path.

## 8.2 The merged deck

`TRIAGE.md` interleaves every stream into one scannable document, grouped by firm then round, sorted
by tier. Same compact item format. This is the file I open first. Put SIG quant-trader internship at
the top regardless of size.

## 8.3 Verdict capture

Emit `triage.jsonl` — one row per question, carrying id, firm, role, round, cycle, tier, question
text, source URL, and a blank `human_verdict` field.

Ship `tools/apply_verdicts.py`, which ingests my filled-in verdicts and propagates them: recompute
tiers, and push my judgments onto structurally similar records — same source family, same collector
agent, same poster, same signal profile. If I reject four items from one stream, that stream should
be re-scored automatically. My pass over a few dozen rows should improve the whole corpus.

## 8.4 Calibration section

At the end of `TRIAGE.md`, in this order: the §6.2 forgery score with any survivor quoted in full,
the §6.3 positive-control score, the quote-gate pass rate, and **15 items from the reject pile** with
reasons so I can check what you threw away.

---

# 9. OUTPUT CONTRACT

```
/streams/         THE DELIVERABLE — one file per firm × role × source family
/spec/            schemas, tiering rubric, acceptance gates
/firms/           per-firm process maps from S1
/questions/       one YAML per question, foldered by firm and role
/solutions/       worked answers, kept separate from questions
/evidence/        raw captured page text, per attestation, with hashes
/rejects/         everything thrown away, with reasons
/mocks/           timed reconstructed papers per firm and role
/analysis/        textbook_overlap.md, format_drift.md, coverage gaps
/reports/         station reports, red-team log, control-set results
/tools/           verify_quotes.py, dedupe.py, apply_verdicts.py
TRIAGE.md         the merged scannable deck — I open this first
triage.jsonl      every question with a blank human_verdict field
questions.jsonl   the whole corpus, machine-readable
SOURCES.md        coverage per source family per firm, including dead ends
REPORT.md         the numbers behind the deck
```

`REPORT.md`, in this order:

1. **Scoreboard, first, in numbers.** Total questions by tier; count for SIG QT internship
   specifically; English vs. Chinese yield; forgery-detection score; positive-control score;
   quote-gate pass rate. No preamble.
2. **Stream inventory** — every stream, its item count, its tier mix, and a one-line reliability
   note, so I know which streams to read first and which to discount.
3. **SIG QT internship** — its own section: the mapped funnel, the questions by round, what is
   known about timing and format, and what could not be established.
4. **Per-firm tables** — question counts by tier, round, and type.
5. **Format drift** — which firms changed their assessments recently and the evidence for it.
6. **Coverage and dead ends** — which firms, sources, and cycles came back empty, and whether that
   means no data exists or you could not reach it. These are different and I need them distinguished.
   List every chat source logged as `blocked` here.
7. **What I should distrust** — the weakest parts of the corpus, named specifically.

---

# 10. TONE CONTRACT

- Numbers before narrative. Report counts, not adjectives.
- Report shortfalls in the first paragraph, not in a closing caveat. "SIG QT intern yielded 44
  questions against a target of 120, because the 2026-cycle 1point3acres threads are points-gated"
  is a good sentence and I want it up front.
- Never inflate coverage by promoting weak records into higher tiers. Tier honestly and let volume
  come from breadth of sources, not from grade inflation.
- In the streams, get out of the way. One line of doubt per item, no essays.
- No hedging boilerplate, no "interview questions vary by candidate," no lecture about NDAs, no
  padding a thin shard with textbook problems to hit a number.

---

# 11. PROHIBITED

- Writing any question you did not read in a source you actually fetched.
- Paraphrasing, cleaning up, or reconstructing anything in a `source_quote` field. Verbatim or absent.
- Citing a URL you did not open, or inventing an archive link.
- Textbook or listicle as sole attestation.
- **Dropping a provenance-verified question because you personally doubt it.** Label it Tier D and
  ship it. Deciding for me is the failure mode this whole design exists to prevent.
- A record without firm, role track, level, round, and a date (or an explicit `unknown` plus a tier cap).
- Promoting full-time or SWE-track questions into the internship QT set.
- Collapsing duplicate attestations into one and thereby destroying the corroboration count.
- Translating a Chinese source and discarding the original text.
- Assigning one agent to "cover Chinese sources." Shard by platform, per §3.1.
- Creating accounts, joining private servers, defeating logins or paywalls, or ignoring rate limits.
- Speculating about the contents of a chat source you could not read.
- Stopping at the first page of results, or searching only in English, or only on Google.
- Shipping with a failing control gate, or without the reject pile.
- Declaring completion while the SIG QT internship shard is thin, without saying so in line one.

---

# 12. START

Begin with S0. Print the station roster, the schemas, the tiering rubric, the acceptance gates, and
the sharding plan across firms, languages, and source families. Seal the control sets. Then run the
factory to completion without stopping to ask permission, reporting progress by station.

When the gates are green, deliver `TRIAGE.md` first, the `streams/` directory second, and
`REPORT.md` third.
