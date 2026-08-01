#!/usr/bin/env python3
"""Third t.me/usinterview batch — Optiver, Two Sigma and IMC. Quotes verified against
the stored message pages before emitting."""
import html
import json
import os
import re
import sys

PAGES = 'raw/pages/tgmsg'
BLOCKS = re.compile(
    r'<div class="(?:tgme_widget_message_text[^"]*|link_preview_title|link_preview_description)"'
    r'[^>]*>(.*?)</div>', re.S)


def page_text(mid):
    raw = open(os.path.join(PAGES, f'{mid}.html'), encoding='utf-8', errors='replace').read()
    parts = []
    for body in BLOCKS.findall(raw):
        t = re.sub(r'<br\s*/?>', '\n', body)
        t = re.sub(r'<[^>]+>', '', t)
        parts.append(html.unescape(t))
    return '\n'.join(parts)


CHANNEL = 'https://t.me/usinterview'
COMMON = {
    'source_type': 'chat_telegram', 'access': 'full_text', 'retrieval_method': 'webfetch',
    'upstream_source': ('Telegram channel @usinterview (北美跳槽面经) auto-reposts 1point3acres '
                        '海外面经版 threads; the quoted text is the Telegram link-preview of the '
                        'original forum post, which is itself Cloudflare-blocked to this machine'),
    'poster_context': ('candidate self-report posted to 1point3acres 海外面经版 and mirrored into '
                       'the Telegram channel'),
}
PREVIEW = ('The Telegram link preview truncates the original post, so what is recorded is a '
           'fragment of the poster\'s own paraphrase rather than the assessment wording. ')
SWE = ('The forum role tag on this post is 码农类General (generic software engineer) at a trading '
       'firm, mapped to quant_developer as the nearest controlled value, so the role label may '
       'overstate how "quant" the role is. ')

R = []


def add(mid, date, firm, role, level, cycle, office, rnd, rname, platform, section, qtype,
        qtext, qtext_en, answer, quote, lang, doubt):
    R.append(dict(firm=firm, role_track=role, level=level, cycle=cycle, office=office, round=rnd,
                  round_name=rname, platform=platform, section_context=section, question_type=qtype,
                  question_text=qtext, question_text_en=qtext_en, reported_answer=answer,
                  source_url=f'{CHANNEL}/{mid}', source_quote=quote, source_language=lang,
                  post_date=date, **COMMON, doubt=doubt))
    R[-1]['_mid'] = str(mid)


# ================================== Optiver ==================================
add(24895, '2025-08-20', 'Optiver', 'quant_developer', 'experienced', '2025', 'unknown',
    'online_assessment', 'optiver oa', 'unknown', 'OA question 1', 'coding_dates',
    '给两个日期求他们之间隔了多少天，每个月份多少天有现成得api可以调',
    'Given two dates, find how many days there are between them; there is a ready-made API you can '
    'call for how many days are in each month.',
    None,
    '[*]给两个日期求他们之间隔了多少天，每个月份多少天有现成得api可以调[*]给一组有向边，判断它是否是合法的二叉树，如果不是的话输出对应的错误类型（invalid input，存在',
    'zh',
    SWE + 'This independently corroborates a separate candidate\'s report of the same two-question '
    'Optiver C++ OA five weeks earlier (t.me/usinterview/24161, 2025-07-14), and adds a detail that '
    'recall lacked — that a month-length API is provided. Still a paraphrase, with no input format '
    'or edge-case spec (leap years, ordering, inclusivity).')

add(24895, '2025-08-20', 'Optiver', 'quant_developer', 'experienced', '2025', 'unknown',
    'online_assessment', 'optiver oa', 'unknown', 'OA question 2', 'coding_trees',
    '给一组有向边，判断它是否是合法的二叉树，如果不是的话输出对应的错误类型（invalid input，存在',
    'Given a set of directed edges, determine whether it is a valid binary tree; if it is not, '
    'output the corresponding error type (invalid input, there exists ... — preview truncated)',
    None,
    '[*]给两个日期求他们之间隔了多少天，每个月份多少天有现成得api可以调[*]给一组有向边，判断它是否是合法的二叉树，如果不是的话输出对应的错误类型（invalid input，存在',
    'zh',
    SWE + PREVIEW + 'Truncated inside the list of error types at "存在" (there exists…), so the '
    'error taxonomy — which is the actual difficulty of this problem — is incomplete. Corroborates '
    't.me/usinterview/24161, which reported the same question but framed the failure case '
    'differently (return a serialization if valid), so the two recalls do not fully agree.')

add(24673, '2025-08-08', 'Optiver', 'quant_developer', 'experienced', '2025', 'unknown',
    'phone_technical', 'Optiver 店面 (phone screen)', 'unknown', 'phone screen design question',
    'data_structure_design',
    'Design a queue,discuss the performance tradeoff.',
    'Design a queue, discuss the performance tradeoff.',
    None,
    'Design a queue,discuss the performance tradeoff.求加米！',
    'en',
    SWE + 'This is the entire post — one sentence plus a karma request. It is complete rather than '
    'truncated, which is unusual here, but it is so generic that it carries almost no '
    'firm-specific signal, and there is no record of what follow-ups were asked.')

add(24735, '2025-08-12', 'Optiver', 'quant_developer', 'experienced', '2025', 'unknown',
    'online_assessment', 'Optiver OA', 'unknown', 'OA format report (not a question)',
    'assessment_format',
    '这个部分是 2 道中等难度的编程题 + 1 道近似解题（Approximate Solution），90 分钟做完。题型偏 DP（动态规划）、heap（堆）之类，考的就是数学',
    'This section is 2 medium-difficulty programming questions plus 1 approximate-solution question, '
    'to be finished in 90 minutes. The question types lean towards DP and heap; what is being tested '
    'is maths... (preview truncated)',
    None,
    'Optiver OA还是挺难的，这个部分是 2 道中等难度的编程题 + 1 道近似解题（Approximate Solution），90 分钟做完。题型偏 DP（动态规划）、heap（堆）之类，考的就是数学',
    'zh',
    'Format only, no question. Worth keeping because the "2 coding + 1 Approximate Solution in 90 '
    'minutes" structure is specific and matches the four-section OA another Optiver candidate '
    'described (t.me/usinterview/... / 1p3a thread 1141209). CAUTION: identical phrasing about a '
    '"2 coding + 1 Approximate Solution, 90 minutes" Optiver section also appears on the '
    'prep-vendor site programhelp.net, so I cannot rule out that this forum post and that vendor '
    'page share an origin.')

add(24329, '2025-07-23', 'Optiver', 'quant_developer', 'experienced', '2025', 'Shanghai',
    'online_assessment', 'Optiver SH (Shanghai) OA then phone screen', 'unknown',
    'OA format report (not a question)', 'assessment_format',
    '先是3道OA题目给了3hrs。之后给了电面，当场做题，没有能立刻pass所有testcases',
    'First there were 3 OA questions with 3 hours given. Then there was a phone screen with live '
    'coding; I could not immediately pass all the test cases.',
    None,
    '靠猎头拿到的 Optiver SH 的机会，先是3道OA题目给了3hrs。之后给了电面，当场做题，没有能立刻pass所有testcases，聊的还行，没有问technical 的问题。过了两天发了好',
    'zh',
    'Format only. Notable because the Shanghai pipeline (3 questions / 3 hours) differs from the '
    'Amsterdam and US OA formats other candidates report, but no question content survives.')

add(24044, '2025-07-07', 'Optiver', 'quant_developer', 'experienced', '2025', 'unknown',
    'online_assessment', 'Optiver OA C++', 'unknown', 'OA format report (not a question)',
    'assessment_format',
    '2道题，一共120min的时间，实际90+min完成，总体难度中等偏上~',
    '2 questions, 120 minutes in total; I actually finished in 90-odd minutes. Overall difficulty '
    'moderately hard.',
    None,
    '2道题，一共120min的时间，实际90+min完成，总体难度中等偏上~**** 本内容被作者隐藏 ****',
    'zh',
    'Format only — the preview ends at the forum\'s hidden-content marker '
    '("**** 本内容被作者隐藏 ****"), so the two questions are behind the author\'s own hide tag and '
    'were never visible.')

add(23512, '2025-06-03', 'Optiver', 'quant_analyst', 'experienced', '2025', 'unknown',
    'phone_technical', 'Optiver Technical interview — Trading Risk Analyst', 'unknown',
    'section 1 of 3: background questions', 'behavioural',
    '背景相关问题：日常工作，为什么选择Trading，问我是不是更喜欢创造PNL(为了解释，这个工作不是创造任何PNL的)，问我如果Optiver有专门的Prop Tra',
    'Background questions: day-to-day work; why choose trading; whether I prefer generating PnL (to '
    'explain, this job does not generate any PnL); asked me, if Optiver had a dedicated Prop '
    'Tra... (preview truncated)',
    None,
    '面试主要分为三部分：[*]背景相关问题：日常工作，为什么选择Trading，问我是不是更喜欢创造PNL(为了解释，这个工作不是创造任何PNL的)，问我如果Optiver有专门的Prop Tra',
    'zh',
    'Behavioural, not quantitative, and truncated mid-question at "Prop Tra…". The forum role tag '
    'is 分析|数据科学类 (analysis / data science), mapped to quant_analyst. Sections 2 and 3 of the '
    'interview, which is where any technical content would be, are not visible.')

# ================================== Two Sigma ==================================
add(26349, '2025-11-18', 'Two Sigma', 'quant_developer', 'experienced', '2025', 'unknown',
    'onsite', 'Two Sigma VO — one algorithms round, one system design round', 'unknown',
    'the algorithms round', 'coding_trees',
    '算法：给你一个人们之间是否认识的关系网，保证人们之间认识情况建出的图是一棵树，请问我最多在图里选择多少人，',
    'Algorithms: you are given a network of who knows whom among a group of people, and it is '
    'guaranteed that the graph built from these acquaintance relations is a tree. What is the '
    'maximum number of people I can select from the graph such that ... (preview truncated)',
    None,
    '一轮算法一轮system designsystem design见其他帖子算法：给你一个人们之间是否认识的关系网，保证人们之间认识情况建出的图是一棵树，请问我最多在图里选择多少人，',
    'zh',
    SWE + PREVIEW + 'Cut off exactly at the selection constraint ("最多在图里选择多少人，…"), which '
    'is the whole problem — without it this is not solvable. The setup (tree, maximise a selected '
    'set) is enough to identify the family of problem but not the problem.')

add(27929, '2026-04-08', 'Two Sigma', 'quant_developer', 'experienced', '2026', 'unknown',
    'phone_technical', 'Two Sigma OA then 店面 (phone screen)', 'unknown',
    'the phone screen, described as an in-memory database design/implementation',
    'database_implementation',
    "店面：遇到了in memory DB要求能support 1. create table 'tabl",
    "Phone screen: I got the in-memory DB question — it has to support 1. create table 'tabl... "
    "(preview truncated)",
    None,
    "都是题库里的，店面遇到了还真的是写不完，虽然也没要求我能写完整[hide=200]OA:下水道 + IPO 秒了店面：遇到了in memory DB要求能support 1. create table 'tabl",
    'mixed',
    SWE + 'Cut off in the middle of the first supported operation, and the rest of the post is '
    'behind the forum\'s [hide=200] karma tag. The poster says explicitly "都是题库里的" — these are '
    'all from the (forum) question bank — which means they are describing recycled questions they '
    'had already seen, so this is corroboration of a known bank rather than fresh recall.')

add(27929, '2026-04-08', 'Two Sigma', 'quant_developer', 'experienced', '2026', 'unknown',
    'online_assessment', 'Two Sigma OA', 'unknown', 'OA — named by nickname only',
    'coding_mixed',
    'OA:下水道 + IPO 秒了',
    'OA: "the sewer" + "IPO" — solved them instantly.',
    None,
    'OA:下水道 + IPO 秒了',
    'zh',
    SWE + 'The two questions are referred to only by forum nicknames — 下水道 ("the sewer") and IPO '
    '— with no problem statements at all. NO QUESTION CONTENT IS RECOVERED HERE. Its value is that '
    'the same pair is named independently by another candidate seven months earlier '
    '(t.me/usinterview/25382, 2025-09-19), establishing that Two Sigma reused this OA across at '
    'least 2025-09 to 2026-04.')

add(25382, '2025-09-19', 'Two Sigma', 'quant_developer', 'experienced', '2025', 'unknown',
    'online_assessment', 'Two sigma OA 汇总 (a candidate\'s compilation of collected OA questions)',
    'unknown', 'a compiled list of Two Sigma OA questions, given by nickname and forum link',
    'compilation_index',
    'IPO + 下水道：https://www.1point3acres.com/bbs/thread-939983-1-1.html[*]Serve',
    'IPO + "the sewer": https://www.1point3acres.com/bbs/thread-939983-1-1.html; Serve... (preview '
    'truncated)',
    None,
    '刚面完Two sigma OA，总结一下我收集到的OA题吧，造福地里，帮大家省时间了。[*]IPO + 下水道：https://www.1point3acres.com/bbs/thread-939983-1-1.html[*]Serve',
    'zh',
    SWE + 'This is explicitly a COMPILATION — the poster says "总结一下我收集到的OA题" (let me '
    'summarise the OA questions I have collected), i.e. an index of other people\'s threads, not '
    'their own recall. No question text is present, only nicknames and a link to thread 939983 '
    'which I did not retrieve. Recorded as a pointer, not as evidence of a question.')

add(27446, '2026-03-06', 'Two Sigma', 'quant_developer', 'experienced', '2026', 'unknown',
    'phone_technical', 'Two Sigma quantitative software engineer 店面 coding', 'unknown',
    'phone screen coding', 'coding_dp',
    '力扣跳跃游戏系列',
    'The LeetCode jump-game series.',
    None,
    '力扣跳跃游戏系列有人一起准备onsite吗 可以私信我 听说qse和general se考的不太一样',
    'zh',
    SWE + 'Six characters of content — the candidate names a LeetCode problem family ("jump game '
    'series") and nothing else. No statement, no variant, no constraints. The rest of the post is a '
    'request for study partners. Included only because it is the one datapoint on the Two Sigma '
    '"quantitative software engineer" track specifically, which the poster says is tested '
    'differently from general SWE.')

add(29040, '2026-07-24', 'Two Sigma', 'quant_developer', 'new_grad', '2026', 'unknown',
    'online_assessment', 'Two Sigma NG SWE OA — 2 questions, single combined time limit',
    'unknown', 'OA format report (not a question)', 'assessment_format',
    '申的是Two Sigma 的NG SWE，本来没抱太大希望，海投之后没多久就约了OA，两道题限时一起做。投之前听说这家挂经比较多，专门跑去翻了下地里做功课，好几个帖说OA地里都是',
    'I applied to Two Sigma\'s NG SWE role. I did not have high hopes; not long after applying '
    'cold, an OA was scheduled — two questions under a single combined time limit. Before applying '
    'I had heard this firm produces a lot of rejection posts, so I went and dug through the forum '
    'to do my homework; several posts said the OA questions are all already on the forum... '
    '(preview truncated)',
    None,
    '申的是Two Sigma 的NG SWE，本来没抱太大希望，海投之后没多久就约了OA，两道题限时一起做。投之前听说这家挂经比较多，专门跑去翻了下地里做功课，好几个帖说OA地里都是',
    'zh',
    'Format only, no question. The load-bearing content is the claim, repeated by several posters, '
    'that the Two Sigma OA questions are entirely recycled from ones already published on the '
    'forum. Posted 2026-07-24, eight days before this harvest.')

# ==================================== IMC ====================================
add(17648, '2024-03-01', 'IMC', 'quant_researcher', 'experienced', '2024', 'Sydney',
    'phone_technical', 'IMC Quant in Sydney HR Phone Screen', 'unknown',
    'HR phone screen for a Quantitative Researcher role (not a question)', 'assessment_format',
    'Applying for the Quantitative Researcher position at IMC Trading in Sydney,I received an HR '
    'Phone Screen notification three days later. The interview went as f',
    'Applying for the Quantitative Researcher position at IMC Trading in Sydney, I received an HR '
    'Phone Screen notification three days later. The interview went as f... (preview truncated)',
    None,
    'Applying for the Quantitative Researcher position at IMC Trading in Sydney,I received an HR Phone Screen notification three days later. The interview went as f',
    'en',
    'The preview cuts off at exactly the point where the interview content would begin ("The '
    'interview went as f[ollows]"), so not a single question is recovered. Retained because it is '
    'one of only three IMC quant-track datapoints in this shard and it fixes the office (Sydney), '
    'role (Quantitative Researcher) and turnaround (three days) precisely.')

add(3103, '2020-09-03', 'IMC', 'quant_trader', 'experienced', 'unknown', 'unknown',
    'onsite', 'IMC Quant Trader Video Interview', 'unknown',
    'report that the video interview reused an earlier candidate\'s questions verbatim',
    'assessment_format',
    '题目是跟之前一个帖子里的一摸一样的、感觉这就是今年秋招题没跑了',
    'The questions were exactly the same as in an earlier thread — it seems certain these are this '
    'autumn\'s recruiting questions.',
    None,
    '刚面完IMC的video、发面筋攒人品、题目是跟之前一个帖子里的一摸一样的、感觉这就是今年秋招题没跑了、详情请见：https://www.1point3acres.com/bbs ... MC%2Bquant%2Btr ...',
    'zh',
    'NO QUESTION CONTENT — the poster deliberately does not restate the questions, only points at '
    'an earlier thread whose URL the preview mangles into an unusable fragment. Six years old '
    '(2020). Included because "identical to the earlier thread" is direct evidence that IMC ran a '
    'fixed video-interview question set across a recruiting season, which is a structural claim '
    'worth having on record.')

add(25976, '2025-10-23', 'SIG', 'quant_developer', 'experienced', '2025', 'unknown',
    'phone_technical',
    'multi-firm compilation covering Jump, Tower, SIG, Two Sigma, IMC, Citadel and Optiver',
    'unknown', 'the question the poster names as the highest-frequency one across all these firms',
    'cpp_implementation',
    'implement vector in c++',
    'implement vector in c++',
    None,
    'implement vector in c++半年来面了十几家买方公司c++ quant dev，能叫上名字来的top tier基本都面了个遍 最后拿了三家offerimplement vector in c++ 是一道高频题，考',
    'mixed',
    'THIS IS A COMPILATION POST, not a single-interview recall: the poster says they interviewed at '
    'a dozen-plus buy-side firms for C++ quant dev over six months and is summarising across all of '
    'them, so "implement vector in c++" cannot be pinned to any one firm. I have filed it under SIG '
    'because SIG is named in the thread title and because three separate SIG-specific recalls in '
    'this same file report exactly this question (t.me/usinterview/25098, /26028, /28975) — but the '
    'attribution is mine, not the source\'s, and a reader should treat the firm field here as '
    'weakly supported.')

# ---------------------------------------------------------------- emit
missing, out = [], []
for rec in R:
    mid = rec.pop('_mid')
    txt = page_text(mid).replace('\u00a0', ' ').replace('\u200b', '')
    q = rec['source_quote'].replace('\u00a0', ' ').replace('\u200b', '')
    if q in txt or re.sub(r'\s+', '', q) in re.sub(r'\s+', '', txt):
        out.append(rec)
    else:
        missing.append((mid, rec['firm'], q[:80]))

for m in missing:
    sys.stderr.write(f'QUOTE NOT FOUND: {m}\n')

with open('raw/chat_and_archive.jsonl', 'a', encoding='utf-8') as f:
    for rec in out:
        f.write(json.dumps(rec, ensure_ascii=False) + '\n')
print(f'verified+written={len(out)}  failed={len(missing)}')
