# Record schema and controlled vocabularies

Load this at Phase 3. One YAML file per question at `questions/<firm>/<role>/<id>.yaml`.

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
question_type: sequences
question_text: "…as reported, wording preserved…"
question_text_en: "…only if the original is not English…"
answer_format: numeric
reported_answer: "…if the source gives one…"
answer_status: verified_by_source         # | derived_by_agent | disputed | unknown
attestations:
  - source_url: https://…
    source_type: 1point3acres
    source_quote: "…verbatim, byte-checkable substring of the fetched page…"
    source_language: zh
    post_date: 2026-01-14
    retrieved_at: 2026-02-02T11:04:00Z
    archive_url: https://web.archive.org/…
    access: full_text
    poster_context: "…account history, university, other recall posts…"
independent_attestation_count: 2
tier: A
textbook_overlap: false
textbook_overlap_detail: null
cross_firm_reuse: []
red_team_attack: "…what the red team tried, and why it failed to break this record…"
adjudication_notes: "…which authenticity signals fired…"
confidence_notes: "…residual doubt, stated plainly…"
```

Preserve the reported wording. Do not clean a question up into textbook prose — the awkward
specificity of real recall is itself evidence.

## `round`

`online_assessment` · `math_sequences_test` · `phone_technical` · `superday` · `onsite` ·
`trading_game` · `take_home` · `datathon` · `final`

## `role_track`

`quant_trader` · `quant_researcher` · `quant_developer` · `quant_analyst` · `data_scientist` ·
`discretionary_trader`

## `level`

`internship` · `new_grad` · `experienced` · `phd_new_grad`

An internship OA and a full-time OA at the same firm are frequently different tests. A record that
cannot establish which one it was gets `level: unknown` and is capped at Tier C. Never silently
promote a full-time question into an internship set.

## `question_type`

`mental_math_speed` · `sequences` · `probability` · `combinatorics` · `expected_value` ·
`market_making` · `betting_odds_arbitrage` · `poker_game_theory` · `fermi_estimation` ·
`logic_brainteaser` · `statistics_regression` · `options_theory` · `stochastic_calculus` ·
`linear_algebra` · `coding_algorithms` · `coding_simulation` · `sql_data` · `ml_modeling` ·
`pattern_recognition_iq` · `trading_game` · `behavioral` · `personality_assessment`

## `source_type`

**English:** `reddit_thread` · `blind` · `wso` · `quantnet` · `elitetrader` · `glassdoor` ·
`leetcode_discuss` · `geeksforgeeks` · `github_repo` · `student_doc` · `youtube` · `blog` ·
`x_twitter` · `hackernews`

**Chinese:** `1point3acres` · `nowcoder` · `yingjiesheng` · `kanzhun` · `maimai` · `shixiseng` ·
`zhihu` · `xiaohongshu` · `weibo` · `bilibili` · `douyin` · `tieba` · `douban` · `newsmth` ·
`university_bbs` · `v2ex` · `hupu` · `muchong` · `wechat_article` · `csdn` · `juejin` · `jianshu` ·
`cnblogs` · `yuque` · `shimo` · `lark_doc`

**Chat:** `chat_discord` · `chat_telegram` · `chat_qq_repost` · `chat_wechat_repost` · `chat_slack`

**Other:** `other` — if you use it more than a handful of times the vocabulary is wrong. Extend it
and say so.

## `access`

| Value | Meaning |
|---|---|
| `full_text` | Fetched and read the whole page |
| `snippet_only` | Login-walled; you have the public search snippet |
| `archive_only` | Original gone; an archive snapshot carries the quote |
| `compilation_only` | Found in a secondhand compilation, original post not locatable |
| `screenshot_only` | Legible in an image, so no byte-verifiable text quote exists. Transcribe, mark, cap at Tier C |

## `cycle`

Tag every record with its recruiting cycle (`Summer 2026`, `Summer 2025`). Weight recency heavily:
current and prior cycle first, then back three cycles, then older only if the question recurs. Firms
rotate question pools and switch assessment vendors, so a 2019 recall is archaeology, not
intelligence.

Maintain `analysis/format_drift.md` recording, per firm, when the format demonstrably changed —
vendor switch, new section, changed timing — citing the recalls that show it.

## Cross-firm reuse

Vendor question pools are shared, so the same item can legitimately appear at multiple firms. Record
it in `cross_firm_reuse` rather than treating it as a contradiction. It is a finding, not a bug.
