#!/usr/bin/env python3
"""Fifth @usinterview batch — messages surfaced by a second sweep of the channel's ?q= search
(query terms: 概率题, 智力题, 期望, 做市, 骰子, 硬币, 扑克, 猜数, 拍卖, 心算, poker, estimation,
brain teaser, plus per-firm terms). Each cited message was then fetched individually so the
quote can be checked against a canonical per-message copy.
"""
import html
import json
import os
import re
import sys

PAGES = 'raw/pages/tgmsg'
BLOCKS = re.compile(
    r'<div class="(?:tgme_widget_message_text[^"]*|link_preview_title|link_preview_description)"'
    r'[^>]*>(.*?)</div>', re.S)
_cache = {}


def page_text(mid):
    if mid not in _cache:
        raw = open(os.path.join(PAGES, f'{mid}.html'), encoding='utf-8', errors='replace').read()
        parts = []
        for b in BLOCKS.findall(raw):
            t = re.sub(r'<script.*?</script>', ' ', b, flags=re.S)
            t = re.sub(r'<br\s*/?>', '\n', t)
            t = re.sub(r'<[^>]+>', '\n', t)
            parts.append(html.unescape(t))
        _cache[mid] = '\n'.join(parts)
    return _cache[mid]


TG = ('@usinterview is a public Telegram channel that auto-forwards new 1point3acres 海外面经 '
      'threads. The message carries the thread title, the firm/round/seniority tags the poster '
      'chose on the forum, and the opening of the post body as a link preview')
TRUNC = ('The Telegram link preview is cut off at a fixed length and visibly ends in "…", so only '
         'the opening of the recall is readable. 1point3acres Cloudflare-blocks this machine and '
         'the Wayback Machine has no 200 snapshot of this thread, so the rest is unrecoverable')
WHOLE = ('This preview is NOT truncated — it ends without an ellipsis — so unlike most records in '
         'this shard nothing is being hidden by the cut-off')

R = []


def add(mid, date, firm, role, level, cycle, rnd, rname, section, qtype, qtext, qtext_en,
        quote, poster, doubt, answer=None, office='unknown', lang='zh'):
    R.append({
        'firm': firm, 'role_track': role, 'level': level, 'cycle': cycle, 'office': office,
        'round': rnd, 'round_name': rname, 'platform': 'unknown', 'section_context': section,
        'question_type': qtype, 'question_text': qtext, 'question_text_en': qtext_en,
        'reported_answer': answer, 'source_url': f'https://t.me/usinterview/{mid}',
        'source_type': 'chat_telegram', 'source_quote': quote, 'source_language': lang,
        'post_date': date, 'access': 'full_text', 'retrieval_method': 'webfetch',
        'upstream_source': ('1point3acres thread auto-forwarded into the channel; the forum thread '
                            'itself is not readable from this machine'),
        'poster_context': poster, 'doubt': doubt, '_mid': mid})


def ctx(tags, extra=''):
    return TG + f'. Forum tags: {tags}' + (f'. {extra}' if extra else '')


# ============================================================ JUMP — complete, untruncated
JUMP = dict(mid='20370', date='2024-11-14', firm='Jump Trading', role='quant_researcher',
            level='experienced', cycle='2025', rnd='onsite',
            rname='Jump 面试 — tagged Onsite on the forum',
            poster=ctx('#jumptrading 金工类@全职 Onsite 在职跳槽 — quant track, full-time, onsite, '
                       'experienced hire changing jobs',
                       'The entire post body is two questions run together with no other prose'))
JUMP_DOUBT = (
    WHOLE + ', which makes this the cleanest chat-layer capture of a Jump interview in the shard. '
    'The cost is that the poster wrote the two questions as one unpunctuated run of characters '
    '("…求A找到小于200的所有质数"), so the split between them is my reading of the syntax, not a '
    'separator the poster supplied — a reader who disagrees could take it as a single compound '
    'question. Neither item carries any statement of what form the answer should take, and the '
    'post is so terse that it may be a memory-jog for the poster rather than a faithful '
    'transcription of how the interviewer phrased things.')

add(**JUMP, section='first of the two problems recorded in the post',
    qtype='linear_algebra_matrix_polynomial',
    qtext='A为R上的对称矩阵A满足多项式x^5+x^3+x=3求A',
    qtext_en=('A is a symmetric matrix over R. A satisfies the polynomial x^5 + x^3 + x = 3. Find '
              'A.'),
    quote='A为R上的对称矩阵A满足多项式x^5+x^3+x=3求A',
    doubt=('The statement is loose in a way that matters: "A satisfies the polynomial x^5+x^3+x=3" '
           'presumably means A^5 + A^3 + A = 3I, but the poster writes it with the scalar variable '
           'x and a bare 3, and does not say whether A is of fixed dimension or whether uniqueness '
           'is what is being asked for. I have transcribed it as written rather than repairing it. '
           + JUMP_DOUBT))

add(**JUMP, section='second of the two problems recorded in the post',
    qtype='coding_prime_sieve',
    qtext='找到小于200的所有质数',
    qtext_en='Find all the prime numbers less than 200.',
    quote='找到小于200的所有质数',
    doubt=('Six characters, and on its face an elementary sieve exercise, which is surprising for a '
           'quant-track onsite — the interesting part of such a question at Jump would be the '
           'follow-up on method or efficiency, and none is recorded. It is impossible to tell from '
           'the post whether this was a warm-up, a whiteboard-coding prompt, or a mental-arithmetic '
           'task. ' + JUMP_DOUBT))

# ============================================================ CITADEL
add('19118', '2024-08-09', 'Citadel', 'quant_developer', 'experienced', '2025',
    'online_assessment', 'Citadel OA (the poster misspells it "citedal oa")',
    'the coding question, quoted at enough length to show the input format',
    'coding_event_log_parsing',
    ('实现一个简单的会议助手。提供一个字符串列表 events[n]，每个字符串的格式为 " "，其中 person_name '
     '从 start 到 end 执行 action，包括起始和结束时间。时间格式为 HH:'),
    ('Implement a simple meeting assistant. You are given a list of strings events[n], each of the '
     'format " ", where person_name performs action from start to end, inclusive of the start and '
     'end times. The time format is HH: …'),
    ('实现一个简单的会议助手。提供一个字符串列表 events[n]，每个字符串的格式为 " "，其中 person_name '
     '从 start 到 end 执行 action，包括起始和结束时间。时间格式为 HH:'),
    ctx('#citadel 码农类General@全职 在线笔试 在职跳槽 — engineering track, full-time, online '
        'written test, experienced hire'),
    ('The record format the whole question turns on is literally empty in the source: the poster '
     'wrote it as \'每个字符串的格式为 " "\' — the field names inside the quotation marks were lost '
     'when the forum or the Telegram preview stripped the angle-bracket placeholders, so the '
     'schema is "person_name / action / start / end" only by inference from the sentence that '
     'follows. The preview then cuts off at "HH:" before the time format is given, and what the '
     'assistant must actually compute is never stated. ' + TRUNC),
    lang='mixed')

add('21276', '2025-02-07', 'Citadel', 'quant_developer', 'experienced', '2025',
    'online_assessment', 'Citadel OA — two questions',
    'the second question, given a title and a partial specification',
    'coding_token_expiry_simulation',
    ('第二题: ```认证令牌 用户登录后会拿到一个令牌（token)。如果过了系统设定的期限（expiryLimit) '
     '令牌就会失效。不过在期限内重置的话，期限会'),
    ('Question 2: "Authentication token". After a user logs in they receive a token. If the '
     'system-set expiry limit (expiryLimit) passes, the token becomes invalid. However if it is '
     'reset within the limit, the limit will …'),
    ('第二题: ```认证令牌 用户登录后会拿到一个令牌（token)。如果过了系统设定的期限（expiryLimit) '
     '令牌就会失效。不过在期限内重置的话，期限会'),
    ctx('#Citadel 码农类General@全职 在线笔试 在职跳槽'),
    ('The preview is severed at "期限会" — precisely at the clause that would have defined the '
     'renewal semantics, which is the entire substance of this problem (whether resetting extends '
     'from now or from the original expiry). The query interface and what must be returned are '
     'also absent. The first question is given only as an obfuscated LeetCode reference ("LC 遛姒'
     '戚", a homophone substitution I have not decoded and will not guess at), so no record is '
     'made for it. ' + TRUNC),
    lang='mixed')

add('21556', '2025-02-26', 'Citadel', 'quant_developer', 'experienced', '2025',
    'online_assessment', 'Citadel NXT OA — 14 multiple choice plus one coding exercise',
    'the topics covered by the multiple-choice section',
    'mcq_systems_topics',
    ('14mcq，一道coding exercise. Mcq have cache management,proxy servers,analyse time and space '
     'complexity,debugging code.'),
    ('14 MCQs and one coding exercise. The MCQs have cache management, proxy servers, analysing '
     'time and space complexity, debugging code.'),
    ('14mcq，一道coding exercise. Mcq have cache management,proxy servers,analyse time and space '
     'complexity,debugging code.'),
    ctx('#citadel 码农类General@全职 在线笔试 在职跳槽'),
    ('This is a topic inventory, not a question — no individual MCQ is reproduced, and the coding '
     'exercise is mentioned but not described at all. Its value is corroborative: three other '
     'independently posted Citadel NXT recalls in this same batch (t.me/usinterview/19290, 22910, '
     '23774) describe the same MCQ-plus-one-coding shape with overlapping topics, which is good '
     'evidence about the format of the test even though it yields no question text. ' + WHOLE),
    lang='mixed')

add('22910', '2025-05-03', 'Citadel', 'quant_developer', 'experienced', '2025',
    'online_assessment', 'Citadel NXT Backend OA, sent after a recruiter reached out',
    'the multiple-choice section',
    'mcq_complexity_and_debugging',
    ('大概15道选择题包括time / space 复杂度分析（多个，问哪个算法复杂度高/低），debug有一道问你怎么改'
     '是对的（给你几个改正的code）， os/networ'),
    ('Roughly 15 multiple-choice questions including time/space complexity analysis (several of '
     'them, asking which algorithm has higher/lower complexity), and one debugging question asking '
     'how to fix it correctly (giving you several corrected versions of the code); OS/networ… '),
    ('大概15道选择题包括time / space 复杂度分析（多个，问哪个算法复杂度高/低），debug有一道问你怎么改'
     '是对的（给你几个改正的code）， os/networ'),
    ctx('#citadel 码农类General@全职 在线笔试 在职跳槽'),
    ('Again a description of question types rather than any question: no code snippet, no answer '
     'options and no algorithms named. The preview dies mid-word on "os/networ". Kept because it '
     'independently corroborates the ~15-MCQ Citadel NXT format reported in three other threads. ' +
     TRUNC),
    lang='mixed')

add('23774', '2025-06-19', 'Citadel', 'quant_developer', 'experienced', '2025',
    'online_assessment', 'Citadel OA — "十几道选择题＋一道编程题" (a dozen-odd MCQ plus one coding)',
    'the subject matter of the multiple-choice section',
    'mcq_system_design_topics',
    '选择题涵盖：系统设计（pull/push mode,forward/reverse proxy），数据库相关问题，',
    ('The multiple-choice questions covered: system design (pull/push mode, forward/reverse '
     'proxy), database-related questions, …'),
    '选择题涵盖：系统设计（pull/push mode,forward/reverse proxy），数据库相关问题，',
    ctx('#citadel 码农类General@全职 技术电面 在职跳槽',
        'The poster is openly farming karma — "顺便求米，真的很缺米……" (also begging for rice, I '
        'am really short of rice)'),
    ('A topic list. "pull/push mode" and "forward/reverse proxy" are the only concrete items and '
     'they are named as subject areas, not as questions. The karma-farming motive is worth noting: '
     'on 1point3acres a poster is rewarded for volume of recall, which is a standing incentive to '
     'pad, though it cuts against fabrication here since padding with topic names earns little. ' +
     TRUNC),
    lang='mixed')

add('19290', '2024-08-28', 'Citadel', 'quant_developer', 'experienced', '2025',
    'online_assessment', 'Citadel NXT OA — 15 MCQ plus one large coding question, 90 minutes',
    'the multiple-choice section',
    'mcq_computer_systems',
    ('选择题感觉需要对computer system非常熟悉，然后也问了一些code snippet让比较time space '
     'complexity'),
    ('The multiple-choice section felt like it needed you to be very familiar with computer '
     'systems, and it also gave some code snippets and asked you to compare time and space '
     'complexity.'),
    ('选择题感觉需要对computer system非常熟悉，然后也问了一些code snippet让比较time space '
     'complexity'),
    ctx('#citadel 码农类General@全职 在线笔试 在职跳槽'),
    ('The code snippets that the question is entirely about are not reproduced, so nothing here '
     'can be answered — this is the candidate\'s impression of the section. ' + TRUNC),
    lang='mixed')

add('24202', '2025-07-16', 'Citadel', 'quant_developer', 'experienced', '2026',
    'online_assessment', 'Citadel NXT OA',
    'the coding question, which the poster says is identical to one in an earlier forum thread',
    'coding_meeting_scheduling',
    'OA看之前的帖子coding一摸一样，就是找到最早meeting',
    ('For the OA, look at the earlier posts — the coding question is exactly the same, it is just '
     'finding the earliest meeting.'),
    'OA看之前的帖子coding一摸一样，就是找到最早meeting',
    ctx('#citadel 码农类General@全职 在线笔试 在职跳槽',
        'The poster says a recruiter reached out in April but did not submit them for lack of '
        'years of experience, then came back after a promotion post on LinkedIn'),
    ('A back-reference plus a five-character gloss ("找到最早meeting", find the earliest meeting). '
     'What the inputs are, what "earliest" ranks over and what must be returned are all absent. It '
     'is nevertheless a useful cross-check: an earlier independent thread in this same batch '
     '(t.me/usinterview/19118) describes a Citadel OA coding question about parsing a list of '
     'timed events, and another (20907) calls the Citadel coding question "the meeting-room one '
     'lots of people have uploaded" — three separate candidates pointing at a recurring '
     'meeting/interval question in Citadel\'s bank. ' + TRUNC),
    lang='mixed')

add('25119', '2025-09-03', 'Citadel', 'quant_developer', 'experienced', '2026', 'phone_technical',
    'first interview immediately after passing the Citadel NXT OA — 45 minutes',
    'the whole of the 45-minute session',
    'coding_orderbook_construction',
    'OA过了之后马上第一场面试，直接45分钟order book创建（用min max heap就好）',
    ('After passing the OA there was an interview straight away: 45 minutes, building an order '
     'book outright (a min/max heap is all you need).'),
    'OA过了之后马上第一场面试，直接45分钟order book创建（用min max heap就好）',
    ctx('#citadel 码农类General@全职 技术电面 在职跳槽'),
    ('"Order book creation" is a task name, not a specification — which order types must be '
     'supported, what the input stream looks like and what has to be queryable are all unstated. '
     'The parenthetical "用 min max heap就好" is the poster\'s own solution hint rather than '
     'anything the interviewer said, and I have kept it inside the quote rather than promoting it '
     'to reported_answer because it answers a question that was never fully posed. ' + WHOLE),
    lang='mixed')

add('18101', '2024-04-21', 'Citadel', 'quant_researcher', 'experienced', '2024',
    'online_assessment', 'Citadel quant research OA — 70 minutes, two questions',
    'the two OA questions, named but not specified',
    'coding_named_problems',
    'OA 70分钟两题，disk space analysis，visiting cities，test',
    ('OA: 70 minutes, two questions — disk space analysis, visiting cities, test…'),
    'OA 70分钟两题，disk space analysis，visiting cities，test',
    ctx('#citadel 金工类@全职 在线笔试 视频面试 在职跳槽 — quant track, full-time, both online test '
        'and video interview',
        'The thread title promises code ("附代码求加米", code attached, please add rice), so the '
        'poster claims to have posted their solutions behind the karma wall'),
    ('Two problem names with no statements attached, and the preview cuts off on the word "test". '
     'Because the titles are generic ("disk space analysis", "visiting cities") they are not even '
     'reliably identifiable against other firms\' banks. The thread reportedly contains the '
     'poster\'s code, which would settle what the problems were, but it is behind 1point3acres\' '
     'karma wall and the thread has no Wayback snapshot. ' + TRUNC),
    lang='mixed')

# ============================================================ OPTIVER
add('14640', '2022-09-12', 'Optiver', 'quant_developer', 'experienced', '2023',
    'online_assessment', 'Optiver OA for an experienced software engineer',
    'a coding question, quoted with its concrete example inputs',
    'coding_fuel_cost_optimisation',
    ('给定两个输入一个gas station distance {10,20,5,20} 一个对应station的gas price {3,4,2,3} 求从'
     'station 0出发到终点的最低价格 期间油箱大小最多50 liters且每升能'),
    ('Given two inputs — gas station distances {10,20,5,20} and the corresponding gas prices per '
     'station {3,4,2,3} — find the minimum cost of travelling from station 0 to the destination, '
     'where the tank holds at most 50 litres and each litre can …'),
    ('给定两个输入一个gas station distance {10,20,5,20} 一个对应station的gas price {3,4,2,3} 求从'
     'station 0出发到终点的最低价格 期间油箱大小最多50 liters且每升能'),
    ctx('#AkunaCapitalOptiver 码农类General@全职 在线笔试 在职跳槽 — note the tag string merges two '
        'firm names, but the thread title says Optiver'),
    ('The preview breaks off at "每升能" — exactly where the litres-per-distance conversion would '
     'have been given — so the problem as recorded is unsolvable: without the fuel-consumption '
     'rate the tank capacity of 50 litres cannot be related to the distances. The concrete arrays '
     'are the strongest part of the record. A secondary worry is the merged hashtag '
     '"#AkunaCapitalOptiver", which leaves a little doubt about which firm the forum thread was '
     'filed under, though the title is unambiguous. ' + TRUNC),
    lang='mixed')

add('5162', '2021-02-18', 'Optiver', 'quant_developer', 'experienced', '2021',
    'online_assessment', 'Optiver OA for an SDE role — HackerRank, 3 hours, 2 questions',
    'the first question, which the poster spent 20 minutes decoding',
    'coding_string_index_search',
    ('第一题我看了二十分钟才明白说的是什么，题目描述的很复杂，什么折叠蛋白质，实际就是给一个字符串，'
     '找出所有的index，满足以'),
    ('Question 1 took me twenty minutes just to understand. The description is very complicated, '
     'something about protein folding, but really it just gives you a string and asks you to find '
     'all the indices satisfying …'),
    ('第一题我看了二十分钟才明白说的是什么，题目描述的很复杂，什么折叠蛋白质，实际就是给一个字符串，'
     '找出所有的index，满足以'),
    ctx('#optiver @全职 在线笔试 在职跳槽'),
    ('The preview cuts off at "满足以" — at the start of the predicate the indices have to satisfy, '
     'which is the entire question. What survives is the disguise (a protein-folding cover story '
     'over a string problem) and the format, not the problem. Note also that this is the poster\'s '
     'de-obfuscation of the prompt, not the prompt itself. ' + TRUNC),
    lang='mixed')

add('15503', '2023-02-11', 'Optiver', 'quant_developer', 'experienced', '2023',
    'online_assessment', 'Optiver SDE OA — 5 multiple choice and 3 coding, 48 hours',
    'the third coding question',
    'coding_shortest_path_directed_graph',
    '第三道是有向图找最短路径，题目不难但有特殊的输入输出和错误处理要求',
    ('The third is finding the shortest path in a directed graph; the problem is not hard but it '
     'has special input/output and error-handling requirements.'),
    '第三道是有向图找最短路径，题目不难但有特殊的输入输出和错误处理要求',
    ctx('#optiver 码农类General@全职 在线笔试 在职跳槽'),
    ('The distinguishing feature the poster flags — the "special input/output and error-handling '
     'requirements" — is exactly what is not described, and at Optiver that is usually the point '
     'of the question rather than the graph algorithm. The second coding question is given only as '
     '"如图" (see the image), and no image survives in the preview. ' + WHOLE),
    lang='mixed')

add('26345', '2025-11-18', 'Optiver', 'quant_developer', 'experienced', '2026',
    'online_assessment', 'Optiver OA — three programming problems',
    'the three problems, reproduced by their exact given titles',
    'coding_named_problems',
    ('三道编程题Problem 1: Trading Sequence CountingProblem 2: Proportional Allocation Backtest'
     'Problem 3: Order Book Matching Simulation'),
    ('Three programming problems. Problem 1: Trading Sequence Counting. Problem 2: Proportional '
     'Allocation Backtest. Problem 3: Order Book Matching Simulation.'),
    ('三道编程题Problem 1: Trading Sequence CountingProblem 2: Proportional Allocation Backtest'
     'Problem 3: Order Book Matching Simulation'),
    ctx('#optiver 工程类@合同工 在线笔试 在职跳槽 — engineering track, contractor, online written '
        'test',
        'The post opens "求加米，不加米不下载" (add rice; if you do not add rice I will not upload), '
        'i.e. the actual problem statements were withheld pending karma'),
    ('These are the problems\' own titles rather than a candidate\'s paraphrase, which is unusual '
     'and makes them useful for identifying the same test elsewhere — but titles are all there is: '
     'no statement, no input format, no constraints. The poster explicitly conditioned uploading '
     'the real content on receiving karma, so the substance may never have been posted at all. '
     'The three titles are strikingly domain-specific for an OA (trading sequences, proportional '
     'allocation backtest, order-book matching), which is consistent with Optiver but is also '
     'exactly what an invented post would look like. ' + TRUNC),
    lang='mixed')

add('28811', '2026-06-15', 'Optiver', 'quant_developer', 'experienced', '2026',
    'online_assessment', 'Optiver Experienced Software Engineer OA — 72-hour window',
    'the second question, quoted with its example input',
    'coding_tree_construction',
    ('第二题：Construct Binary Tree from InputInput: (A,B) (B,C) (A,D)每组里面Parent在前Child在后 '
     '要求'),
    ('Question 2: Construct Binary Tree from Input. Input: (A,B) (B,C) (A,D). Within each pair the '
     'parent comes first and the child second. The requirement …'),
    ('第二题：Construct Binary Tree from InputInput: (A,B) (B,C) (A,D)每组里面Parent在前Child在后 '
     '要求'),
    ctx('#optiver 码农类General@全职 在线笔试 在职跳槽',
        'The poster gives the window as 72 hours and says it actually took about 2 hours'),
    ('Cut off at "要求" (the requirement), which is where the output format and the error cases — '
     'the part that makes a parent/child-pair tree question non-trivial — would have been. The '
     'example input is concrete and is the strongest part. Question 1 is given only as "力扣1360" '
     '(LeetCode 1360), a bare problem number that I am not resolving to a title from memory, so no '
     'record is made for it. ' + TRUNC),
    lang='mixed')

add('29070', '2026-07-27', 'Optiver', 'quant_developer', 'experienced', '2026',
    'online_assessment', 'Optiver senior SWE OA — two hours',
    'the single design task',
    'system_design_event_engine',
    'design a news subscription process engine两个小时',
    'Design a news subscription process engine. Two hours.',
    'design a news subscription process engine两个小时',
    ctx('#optiver 码农类General@全职 在线笔试 在职跳槽',
        'The poster complains that trying to use ChatGPT made it harder than writing it by hand '
        'and that two hours was tight'),
    ('A one-line brief. The poster goes on to sketch component names ("大概设计 newrechieved，ad…") '
     'but the preview is cut off there and the fragment is too garbled to transcribe as a '
     'requirement, so I have not. What must be designed — throughput targets, delivery semantics, '
     'interfaces — is entirely unstated. ' + TRUNC),
    lang='mixed')

add('18319', '2024-05-13', 'Optiver', 'quant_developer', 'experienced', '2024',
    'online_assessment',
    'Optiver Infra Engineer OA — HackerRank, no time limit',
    'the composition of the coding section',
    'coding_topic_inventory',
    ('OA：hackerrank 4 python coding (1 topological sorting,1 regex,1 python generator,1 prefix '
     'sum) + 1 system design 无时间限制'),
    ('OA: HackerRank, 4 Python coding questions (1 topological sorting, 1 regex, 1 Python '
     'generator, 1 prefix sum) plus 1 system design. No time limit.'),
    ('OA：hackerrank 4 python coding (1 topological sorting,1 regex,1 python generator,1 prefix '
     'sum) + 1 system design 无时间限制'),
    ctx('#optiver 码农类General@全职 HR筛选 技术电面 在线笔试 在职跳槽'),
    ('Five questions identified only by technique. No statement, no input, no constraint is given '
     'for any of them, so nothing here is answerable; it is an inventory of what the test covers. '
     'The "no time limit" claim is unusual enough to be worth flagging as unverified. ' + TRUNC),
    lang='mixed')

add('15529', '2023-03-16', 'Optiver', 'quant_analyst', 'new_grad', '2023', 'online_assessment',
    'Optiver Graduate Equity Analyst assessment',
    'the basic-finance portion of the test',
    'finance_credit_ratings',
    '还有问一些基础的的finance比如non-ig grade 和 IG是什么评级上下这种',
    ('It also asked some basic finance, for example what non-IG grade and IG are as ratings, above '
     'and below, that sort of thing.'),
    '还有问一些基础的的finance比如non-ig grade 和 IG是什么评级上下这种',
    ctx('#optiver 金工类@全职 在线笔试 在职跳槽',
        'The poster says there were many accounting questions, little time, and that fluent '
        'accounting knowledge was required'),
    ('The poster is giving an example of a question type ("what IG and non-IG mean as ratings, and '
     'where the boundary sits") rather than quoting one, and hedges it with "这种" (that sort of '
     'thing). The accounting questions that dominated the test are not described at all. ' + TRUNC),
    lang='mixed')

# ============================================================ SIG
add('16470', '2023-09-25', 'SIG', 'quant_developer', 'experienced', '2024', 'online_assessment',
    'SIG 网测 (the poster writes 四哥, a nickname for SIG)',
    'the question the poster spent twenty minutes reading',
    'coding_account_balance_requests',
    ('题目大概是说给一个list of account balances， 和list of requests， request里面有时间，操作'
     '（取/存），ac'),
    ('The question roughly says: you are given a list of account balances and a list of requests; '
     'a request contains a time, an operation (withdraw/deposit), and ac…'),
    ('题目大概是说给一个list of account balances， 和list of requests， request里面有时间，操作'
     '（取/存），ac'),
    ctx('#sig 码农类General@全职 在线笔试 在职跳槽',
        'The poster opens by saying reading the problem is their weak point and that twenty '
        'minutes went by before they had understood it'),
    ('Cut off mid-word at "ac" — almost certainly the start of "account id", but I will not '
     'complete it. The poster prefixes the whole thing with "大概是说" (roughly says), marking it '
     'as their own recollection, and the output requirement — what must be computed from the '
     'balances and requests — is entirely missing. ' + TRUNC),
    lang='mixed')

# ============================================================ D. E. SHAW
DES = dict(firm='D. E. Shaw', role='quant_developer', level='experienced')

add('23220', '2025-05-17', **DES, cycle='2025', rnd='take_home',
    rname='D. E. Shaw take-home coding test, before the second phone round',
    section='first of the two take-home tasks',
    qtype='coding_bignum_arithmetic',
    qtext='Take Home Coding Test-Addition on big numbers',
    qtext_en='Take-home coding test: addition on big numbers.',
    quote='Take Home Coding Test-Addition on big numbers',
    poster=ctx('#deshaw 码农类General@全职 技术电面 在职跳槽',
               'The post is laid out as a bulleted itinerary of the round: take-home coding test, '
               'then technical interview'),
    doubt=('A task title only — no bound on the size of the operands, no statement about whether '
           'library big-integer types are barred (which is the only thing that makes this a '
           'question), and no interface. ' + TRUNC),
    lang='mixed')

add('23220', '2025-05-17', **DES, cycle='2025', rnd='take_home',
    rname='D. E. Shaw take-home coding test, before the second phone round',
    section='second of the two take-home tasks',
    qtype='coding_vwap',
    qtext='Calculate Volume weighted average price (VWAP)',
    qtext_en='Calculate volume weighted average price (VWAP).',
    quote='Calculate Volume weighted average price (VWAP)',
    poster=ctx('#deshaw 码农类General@全职 技术电面 在职跳槽',
               'Listed immediately after the big-number addition task in the same bulleted list'),
    doubt=('A title only. VWAP is a one-line formula, so as stated this is trivial; whatever made '
           'it an assessment question — streaming input, time bucketing, handling of bad ticks — '
           'is not in the text. It is at least the one genuinely finance-flavoured item in this '
           'D. E. Shaw round. ' + TRUNC),
    lang='mixed')

add('14214', '2022-08-08', **DES, cycle='2022', rnd='phone_technical',
    rname='D. E. Shaw 店面 (phone interview)',
    section='the first technical question after the background discussion',
    qtype='concept_pure_functions',
    qtext='然后开始问memorization,问什么东西可以given the same input,always give the same output',
    qtext_en=('Then they started asking about memo[i]zation, asking what kind of thing can, given '
              'the same input, always give the same output.'),
    quote='然后开始问memorization,问什么东西可以given the same input,always give the same output',
    poster=ctx('#Deshaw 码农类General@全职 技术电面 在职跳槽',
               'The poster says they did not know the answer and that the interviewer was nice '
               'about it'),
    doubt=('The poster writes "memorization" where the context (same input always yields the same '
           'output) indicates memo[i]zation and pure functions; I have transcribed their spelling '
           'and flagged it rather than silently correcting it, but that slip means the wording of '
           'the question cannot be trusted closely. The preview cuts off just after. ' + TRUNC),
    lang='mixed')

add('3138', '2020-09-07', **DES, cycle='2020', rnd='phone_technical',
    rname='D. E. Shaw 面经 — an engineering-leaning phone interview',
    section='asked after the project discussion',
    qtype='open_ended_experience',
    qtext='然后问了个问题: what is the most surprising thing you find when you use',
    qtext_en='Then they asked a question: what is the most surprising thing you find when you use …',
    quote='然后问了个问题: what is the most surprising thing you find when you use',
    poster=ctx('# @全职 技术电面 在职跳槽 — the firm tag is empty on this old thread; the title says '
               'DE Shaw',
               'This is a 2020 thread on the older 美国面经版 board, addressed by forum.php?tid= '
               'rather than the modern thread- URL'),
    doubt=('The preview breaks off on the word "use", so the object of the question — what tool, '
           'language or system the candidate was being asked about — is missing, and that object '
           'is the whole question. Kept only as evidence that D. E. Shaw opens with open-ended '
           'experience probes. ' + TRUNC),
    lang='mixed')

add('2595', '2020-07-20', **DES, cycle='2020', rnd='phone_technical',
    rname='D. E. Shaw 电面过经 (a phone screen the poster passed)',
    section='the bulk of the call',
    qtype='system_design_distributed',
    qtext='面试官问了很多distributed system fundamental design principles / projects deep dive',
    qtext_en=('The interviewer asked a lot about distributed system fundamental design principles '
              '/ project deep dives.'),
    quote='面试官问了很多distributed system fundamental design principles / projects deep dive',
    poster=ctx('#DE Shaw @全职 技术电面 在职跳槽',
               'The poster says the caller sounded like an engineer from the UK office and that '
               'they themselves work on distributed systems'),
    doubt=('A summary of subject matter, not a question — "a lot about distributed system '
           'fundamental design principles" identifies no individual prompt. The round is also '
           'plainly tailored to this candidate\'s own background, so it says little about what '
           'D. E. Shaw asks generally. ' + TRUNC),
    lang='mixed')

add('27858', '2026-04-03', 'D. E. Shaw', 'quant_developer', 'experienced', '2026',
    'phone_technical', 'D. E. Shaw product engineer 店面 (phone interview)',
    'the one technical question in an otherwise behavioural round',
    'tradeoff_llm_inference_cost',
    '唯一有效问题针对AI问了对于expensive but fast token vs. cheap but slow t',
    ('The only substantive question was about AI: it asked about expensive but fast tokens vs. '
     'cheap but slow t…'),
    '唯一有效问题针对AI问了对于expensive but fast token vs. cheap but slow t',
    ctx('#google 码农类General@全职 技术电面 在职跳槽 — the firm hashtag says google, which is '
        'wrong; the thread title says DEShaw product engineer',
        'The poster says the round was otherwise entirely behavioural questions off the resume'),
    ('Two problems. First, the preview is cut off mid-word at "slow t", so the actual question '
     'about the fast/expensive versus slow/cheap token trade-off — what is to be decided, and on '
     'what basis — is missing. Second, the forum hashtag on this thread is #google, not #deshaw; '
     'that is very likely the poster mis-tagging, since the title and body both say DEShaw, but it '
     'is a real inconsistency in the source and I have not resolved it. ' + TRUNC),
    lang='mixed')

# ============================================================ IMC / AKUNA
add('26849', '2026-01-10', 'IMC', 'quant_developer', 'new_grad', '2026', 'phone_technical',
    'IMC early-career SDE HR interview, 30 minutes, after a HackerRank test',
    'a technical question inside an otherwise HR screen',
    'concept_data_structure_choice',
    '先做了hackerank 然后hr30mins，还问了一个什么时候用dict说呢么时候用array',
    ('First I did a HackerRank, then a 30-minute HR call, and it also asked one question: when to '
     'use a dict and when to use an array.'),
    '先做了hackerank 然后hr30mins，还问了一个什么时候用dict说呢么时候用array',
    ctx('#imc 码农类General@全职 HR筛选 在职跳槽 — tagged HR screen',
        'The whole post is this single sentence'),
    ('The post is one sentence with a visible typo ("说呢么时候" for 什么时候), so the wording is '
     'the poster\'s hurried recollection. The question itself — when to use a dict versus an array '
     '— is complete and answerable as stated, which is rare in this batch, but it is elementary '
     'and was asked inside an HR call, so it is weak evidence about IMC\'s technical bar. Also '
     'note the level: "early career" is the poster\'s word, and I have read that as new grad. ' +
     WHOLE),
    lang='mixed')

add('21573', '2025-02-27', 'Akuna', 'quant_researcher', 'experienced', '2025', 'phone_technical',
    'first round for a Singapore Akuna QR role, with the APAC Head of Quant',
    'the one technical question in an otherwise background conversation',
    'statistics_variance',
    '第一面直接和APAC Head of Quant聊了背景 问了简单的Variance 脑子短路了没答上来',
    ('The first round was straight with the APAC Head of Quant, talking about background; he asked '
     'a simple variance question and my brain short-circuited, I could not answer it.'),
    '第一面直接和APAC Head of Quant聊了背景 问了简单的Variance 脑子短路了没答上来',
    ctx('#akunacapital 金工类@全职 技术电面 在职跳槽',
        'The poster adds that the desk does options trading'),
    ('"简单的Variance" (a simple variance question) is a category, not a question — the poster '
     'froze and did not answer, which is presumably why they did not record what was actually '
     'asked. Nothing here is answerable. It is kept because the round metadata is specific and '
     'checkable: Singapore office, first round conducted by the APAC Head of Quant, options desk. '
     + WHOLE),
    office='Singapore', lang='mixed')

# ============================================================ verify + emit
ORDER = ['firm', 'role_track', 'level', 'cycle', 'office', 'round', 'round_name', 'platform',
         'section_context', 'question_type', 'question_text', 'question_text_en',
         'reported_answer', 'source_url', 'source_type', 'source_quote', 'source_language',
         'post_date', 'access', 'retrieval_method', 'upstream_source', 'poster_context', 'doubt']


def norm(s):
    return re.sub(r'\s+', '', s.replace('\u00a0', ' ').replace('\u200b', ''))


ok, bad = [], []
for rec in R:
    mid = rec.pop('_mid')
    if norm(rec['source_quote']) in norm(page_text(mid)):
        ok.append(rec)
    else:
        bad.append((mid, rec['firm'], rec['source_quote'][:60]))

for b in bad:
    sys.stderr.write(f'QUOTE NOT FOUND: {b}\n')

with open('raw/chat_and_archive.jsonl', 'a', encoding='utf-8') as f:
    for rec in ok:
        f.write(json.dumps({k: rec[k] for k in ORDER}, ensure_ascii=False) + '\n')
print(f'verified+written={len(ok)}  failed={len(bad)}')
