#!/usr/bin/env python3
"""Build JSONL records from harvested t.me message pages, verifying every quote
against the stored page HTML before emitting."""
import html
import json
import os
import re
import sys

PAGES = 'raw/pages/tgmsg'
BLOCKS = re.compile(
    r'<div class="(?:tgme_widget_message_text[^"]*|link_preview_title|link_preview_description)"[^>]*>(.*?)</div>',
    re.S,
)


def page_text(mid: str) -> str:
    raw = open(os.path.join(PAGES, f'{mid}.html'), encoding='utf-8', errors='replace').read()
    parts = []
    for body in BLOCKS.findall(raw):
        t = re.sub(r'<br\s*/?>', '\n', body)
        t = re.sub(r'<[^>]+>', '', t)
        parts.append(html.unescape(t))
    return '\n'.join(parts)


CHANNEL = 'https://t.me/usinterview'
COMMON = {
    'source_type': 'chat_telegram',
    'access': 'full_text',
    'retrieval_method': 'webfetch',
    'upstream_source': ('Telegram channel @usinterview (北美跳槽面经) auto-reposts 1point3acres '
                        '海外面经版 threads; the quoted text is the Telegram link-preview of the '
                        'original forum post, which is itself Cloudflare-blocked to this machine'),
    'poster_context': ('candidate self-report posted to 1point3acres 海外面经版 and mirrored into '
                       'the Telegram channel'),
}

# (msg_id, date, firm, role, level, cycle, office, round, round_name, platform,
#  section, qtype, qtext, qtext_en, answer, quote, lang, doubt)
R = []


def add(mid, date, firm, role, level, cycle, office, rnd, rname, platform, section,
        qtype, qtext, qtext_en, answer, quote, lang, doubt):
    R.append(dict(
        firm=firm, role_track=role, level=level, cycle=cycle, office=office, round=rnd,
        round_name=rname, platform=platform, section_context=section, question_type=qtype,
        question_text=qtext, question_text_en=qtext_en, reported_answer=answer,
        source_url=f'{CHANNEL}/{mid}', source_quote=quote, source_language=lang,
        post_date=date, **COMMON, doubt=doubt))
    R[-1]['_mid'] = str(mid)


SWE_DOUBT = ('post is tagged 码农类General (generic software-engineer track) at a trading firm; '
             'mapped to quant_developer as the nearest controlled value, so the role label may '
             'overstate how "quant" the role is. ')
PREVIEW_DOUBT = ('The Telegram link preview truncates the original post, so the question is a '
                 'fragment of the poster\'s own paraphrase rather than the assessment wording. ')

# ---------------- SIG ----------------
add(23247, '2025-05-19', 'SIG', 'quant_researcher', 'experienced', '2025', 'unknown',
    'online_assessment', 'SIG OA', 'unknown', 'OA quantitative section', 'brainteaser_algebra',
    '笼子里520只脚，有鸡牛蜘蛛，问蜘蛛数量。',
    'In a cage there are 520 legs, with chickens, cows and spiders; how many spiders are there?',
    None,
    '几乎全都是以前oa原题，数字略有变动。[*]笼子里520只脚，有鸡牛蜘蛛，问蜘蛛数量。',
    'zh',
    PREVIEW_DOUBT + 'The poster explicitly says the questions are recycled 原题 with changed '
    'numbers, so 520 may not be the number any individual candidate saw. Underdetermined as '
    'stated (three unknowns, one equation), which suggests detail was lost in the recall.')

add(23247, '2025-05-19', 'SIG', 'quant_researcher', 'experienced', '2025', 'unknown',
    'online_assessment', 'SIG OA', 'unknown', 'OA logic section', 'logic_seating_puzzle',
    '5个toddler围着圆桌坐，A不跟BE坐，B不跟c坐，d不跟EC坐。已知D坐A旁边，问谁做B左边',
    'Five toddlers sit around a round table. A will not sit next to B or E, B will not sit next '
    'to C, D will not sit next to E or C. Given that D sits next to A, who sits on B\'s left?',
    None,
    '[*]5个toddler围着圆桌坐，A不跟BE坐，B不跟c坐，d不跟EC坐。已知D坐A旁边，问谁做B左',
    'zh',
    PREVIEW_DOUBT + 'The preview cuts off mid-sentence at "问谁做B左", so the final clause '
    '("左边"/"左手边") is my reconstruction and the constraint list may be incomplete.')

add(19241, '2024-08-23', 'SIG', 'quant_researcher', 'experienced', '2024', 'unknown',
    'online_assessment', 'SIG QR 17题OA', 'unknown', 'OA — poster flags these as new questions',
    'visual_weight_puzzle',
    '求绿色三角形的重量（6lb)',
    'Find the weight of the green triangle (6 lb).',
    '6lb',
    '新题库…感觉还挺难的…还有两道新题是地里的，求绿色三角形的重量（6lb)，',
    'zh',
    PREVIEW_DOUBT + 'This is a one-line label for a question that was almost certainly a '
    'picture-based balance puzzle; the actual diagram is not in the quoted text, so the question '
    'is not reconstructable from this evidence alone.')

add(19241, '2024-08-23', 'SIG', 'quant_researcher', 'experienced', '2024', 'unknown',
    'online_assessment', 'SIG QR 17题OA', 'unknown', 'OA — poster flags these as new questions',
    'expected_value_dice',
    '扔2次骰子获得最大收益',
    'Roll a die twice to obtain the maximum payoff.',
    None,
    '求绿色三角形的重量（6lb)， 扔2次骰子获得最大收益还有2种饼干，A有6个，B有8个，7个排成一排有多少排列组合 2^7-1还',
    'zh',
    PREVIEW_DOUBT + 'Only a six-character label survives; the payoff rule and whether re-rolling '
    'is optional are absent, so this cannot be solved as quoted.')

add(19241, '2024-08-23', 'SIG', 'quant_researcher', 'experienced', '2024', 'unknown',
    'online_assessment', 'SIG QR 17题OA', 'unknown', 'OA — poster flags these as new questions',
    'combinatorics',
    '2种饼干，A有6个，B有8个，7个排成一排有多少排列组合 2^7-1',
    'Two kinds of cookie, 6 of type A and 8 of type B; how many arrangements of 7 in a row are '
    'there? 2^7-1',
    '2^7-1',
    '还有2种饼干，A有6个，B有8个，7个排成一排有多少排列组合 2^7-1还',
    'zh',
    PREVIEW_DOUBT + 'The reported answer 2^7-1 = 127 does not obviously match the stated counts '
    '(2^7 = 128 arrangements of 7 binary slots, minus one), which suggests either the recall or '
    'the answer is garbled.')

add(10230, '2022-02-04', 'SIG', 'quant_developer', 'experienced', 'unknown', 'unknown',
    'online_assessment', 'SIG OA (12 questions, 1 coding)', 'unknown',
    'OA question 1 of 12 — the only coding item', 'coding_simulation',
    '要写一个银行帐户的操作，包含deposit和withdraw。比较复杂的是withdraw的时候，在24小时之后会有一个cashback = 2% * withdraw amount。',
    'Implement bank-account operations including deposit and withdraw. The tricky part is that '
    'on a withdrawal, 24 hours later a cashback of 2% * withdraw amount is credited.',
    None,
    'OA共有12题，只有第一题是coding。要写一个银行帐户的操作，包含deposit和withdraw。比较复杂的是withdraw的时候，在24小时之后会有一个cashback = 2% * withdraw amount。',
    'zh',
    SWE_DOUBT + 'This is a well-known HackerRank "banking system" template used by many firms, so '
    'it may be a platform stock problem rather than SIG-authored.')

add(3622, '2020-10-18', 'SIG', 'quant_developer', 'experienced', 'unknown', 'unknown',
    'online_assessment', 'Susquehanna International Group OA', 'unknown',
    'OA question 1 of 3, Python', 'coding_numerical',
    '第一题是给一个joint probability table写出cross entropy要小心有runtime限制，不能用python自带的loop来写要用numpy来处理所有的计算',
    'Question 1: given a joint probability table, compute the cross entropy. Watch out for the '
    'runtime limit — you cannot use plain Python loops, you must do all the computation with numpy.',
    None,
    '三题python第一题是给一个joint probability table写出cross entropy要小心有runtime限制，不能用python自带的loop来写要用numpy来处理所有的计算',
    'zh',
    SWE_DOUBT + 'Six years old (2020), so almost certainly retired; the poster gives no problem '
    'statement beyond the one-line summary.')

add(25098, '2025-09-02', 'SIG', 'quant_developer', 'experienced', '2025', 'unknown',
    'phone_technical', 'SIG 店面 (phone screen)', 'unknown', 'phone screen coding',
    'cpp_implementation',
    'Implement vector in C++',
    'Implement vector in C++',
    None,
    'Susquehanna店面Implement vector in C++',
    'mixed',
    SWE_DOUBT + 'One line with no follow-ups recorded; "implement std::vector" is the single most '
    'common C++ buy-side screen question industry-wide, so it carries little firm-specific signal.')

add(28975, '2026-06-29', 'SIG', 'quant_developer', 'experienced', '2026', 'unknown',
    'phone_technical', 'SIG phone screen (90 min scheduled)', 'unknown',
    'first-round phone screen, C++', 'cpp_implementation',
    '第一面phone screen是实现std::vector，主要考点是placement new,operator::new，扩容，move等非常常见的内容',
    'The first phone screen was to implement std::vector; the focus was placement new, '
    'operator::new, growth/reallocation, move semantics — all very standard material.',
    None,
    '最近通过猎头投递的SIG，约面试很迅速。第一面phone screen是实现std::vector，主要考点是placement new,operator::new，扩容，move等非常常见的内容，本来是90min，但',
    'zh',
    SWE_DOUBT + 'Describes the topic list rather than the interviewer\'s literal prompt.')

add(26028, '2025-10-26', 'SIG', 'quant_developer', 'experienced', '2025', 'unknown',
    'phone_technical', 'SIG 电面', 'unknown', 'phone screen coding', 'cpp_implementation',
    '实现一个vector，只需要基本的功能，比如push back。',
    'Implement a vector; only the basic functionality is needed, e.g. push_back.',
    None,
    '实现一个vector，只需要基本的功能，比如push back。面完了发现地里有面经',
    'zh',
    SWE_DOUBT + 'Duplicate of the same recurring question reported by other candidates; adds '
    'corroboration but no new content.')

add(27493, '2026-03-10', 'SIG', 'quant_developer', 'experienced', '2026', 'unknown',
    'onsite', 'SIG Onsite — OOD round', 'unknown', 'onsite object-oriented design round',
    'ood_design',
    'Onsite的OOD轮面的是设计超市收银台',
    'The onsite OOD round was to design a supermarket checkout counter.',
    None,
    '电面就是Movie Theatre那道题。Onsite的OOD轮面的是设计超市收银台，coding面的是新闻标题提取股票关键词那道题。都是地里的题，我感觉他们家永远就面这几道题。',
    'zh',
    SWE_DOUBT + 'A title-level reference ("design a supermarket checkout"), not the interviewer\'s '
    'wording; the poster is explicitly summarising known 面经 rather than transcribing.')

add(27493, '2026-03-10', 'SIG', 'quant_developer', 'experienced', '2026', 'unknown',
    'onsite', 'SIG Onsite — coding round', 'unknown', 'onsite coding round', 'coding_strings',
    'coding面的是新闻标题提取股票关键词那道题',
    'The onsite coding round was the problem about extracting stock keywords from news headlines.',
    None,
    'Onsite的OOD轮面的是设计超市收银台，coding面的是新闻标题提取股票关键词那道题。都是地里的题',
    'zh',
    SWE_DOUBT + 'Referred to only by nickname; no input/output spec is given, so the actual task '
    'is not recoverable from this source.')

add(29149, '2026-07-31', 'SIG', 'quant_developer', 'experienced', '2026', 'unknown',
    'phone_technical', 'SIG 电面', 'unknown', 'phone screen coding/design', 'design_query_api',
    '电面就是很经典的电影查找题，大概就是给你一个csv格式的电影列表，让你设计一',
    'The phone screen was the classic movie-lookup problem: you are given a movie list in CSV '
    'format and asked to design a ... (preview truncated)',
    None,
    '5月份有sig的人reach out，我就想试试，于是约了recruiter call，然后很快就就安排了电面。电面就是很经典的电影查找题，大概就是给你一个csv格式的电影列表，让你设计一',
    'zh',
    SWE_DOUBT + 'The Telegram preview truncates exactly where the task is stated ("让你设计一…"), '
    'so what had to be designed is unknown. Posted 2026-07-31, one day before harvest.')

add(19879, '2024-10-13', 'SIG', 'quant_researcher', 'experienced', '2024', 'unknown',
    'online_assessment', 'SIG QR OA', 'unknown', 'OA format report (not a question)',
    'assessment_format',
    'OA一小时21道，题目太多了记不得了',
    'The OA was 21 questions in one hour; there were too many to remember them.',
    None,
    '7月初在Linkedin上看到SIG的job post，quant researcher，投了之后7月中联系我做OA。OA一小时21道，题目太多了记不得了。',
    'zh',
    'This is a format datapoint, not a question — the poster explicitly says they could not '
    'remember the items. Included only because the 21-in-60-minutes figure conflicts with the '
    '17-question and 9-question reports from other candidates.')

add(17365, '2024-01-27', 'SIG', 'quant_researcher', 'experienced', '2024', 'unknown',
    'online_assessment', 'SIG OA QR/QT 9题60分钟', 'unknown', 'OA format report (not a question)',
    'assessment_format',
    'SIG OA QR/QT 9题60分钟 — 刚做完新鲜出炉，大部分题目只是改了数字。',
    'SIG OA QR/QT, 9 questions in 60 minutes — just finished it, fresh; most of the questions '
    'only had the numbers changed.',
    None,
    '刚做完新鲜出炉，大部分题目只是改了数字。需要解题思路可以楼里回复。求大米！！！！蟹蟹！',
    'zh',
    'Format only; the actual 9 questions are behind the forum\'s karma wall and were not in the '
    'preview. The "9 questions / 60 min" figure is the load-bearing content.')

# ---------------- Jane Street ----------------
add(20871, '2025-01-06', 'Jane Street', 'quant_developer', 'experienced', '2025', 'unknown',
    'phone_technical', 'JS phone interview round 1', 'unknown', 'first-round phone coding',
    'coding_parsing',
    '实现一个代码折叠器。要求能将"{}"代表的代码折叠，并且显示Example:1   int main() {2      if (tru',
    'Implement a code folder. It must be able to fold the code delimited by "{}" and display it. '
    'Example: 1 int main() { 2 if (tru... (preview truncated)',
    None,
    'JS的一轮phone interview 面完直接发了superday题目：实现一个代码折叠器。要求能将"{}"代表的代码折叠，并且显示Example:1   int main() {2      if (tru ...',
    'zh',
    SWE_DOUBT + 'The worked example is cut off by the preview, so the exact folding semantics '
    '(what is displayed for a folded block) are missing.')

add(22137, '2025-03-27', 'Jane Street', 'quant_researcher', 'experienced', '2025', 'unknown',
    'phone_technical', 'Jane Street QR 一面', 'unknown', 'QR first round', 'modelling_openended',
    '给出一个数据集，口述分析建模的方式',
    'Given a dataset, talk through how you would analyse and model it.',
    None,
    '1. 给出一个数据集，口述分析建模的方式2. 给出一组数据，比较分析数据的pattern，给出理由',
    'zh',
    'Extremely compressed two-line recall; the dataset itself is not described, so this documents '
    'the round\'s style rather than a reproducible question.')

add(22137, '2025-03-27', 'Jane Street', 'quant_researcher', 'experienced', '2025', 'unknown',
    'phone_technical', 'Jane Street QR 一面', 'unknown', 'QR first round', 'data_reasoning',
    '给出一组数据，比较分析数据的pattern，给出理由',
    'Given a set of data, compare and analyse the patterns in it and justify your reasoning.',
    None,
    '1. 给出一个数据集，口述分析建模的方式2. 给出一组数据，比较分析数据的pattern，给出理由',
    'zh',
    'Same two-line post; no data is reproduced, so the question cannot be reconstructed. Note the '
    '1point3acres role tag on this post is "Other 其他", not the quant tag, so even the QR '
    'labelling rests on the thread title.')

add(19449, '2024-09-12', 'Jane Street', 'quant_researcher', 'experienced', '2024', 'unknown',
    'phone_technical', 'Jane Street MLE 面经', 'unknown', 'ML modelling discussion',
    'ml_model_design',
    '假如我们有minst dataset的variation，每张图片里有三个数字，求三个数字的和。不可以用OCR或者其他图像识别。',
    'Suppose we have a variation of the MNIST dataset where each image contains three digits; '
    'find the sum of the three digits. You may not use OCR or other image recognition.',
    None,
    'Jane street跪经。。求加米看帖问假如我们有minst dataset的variation，每张图片里有三个数字，求三个数字的和。不可以用OCR或者其他图像识别。 讲model design。',
    'zh',
    'The "no OCR or other image recognition" constraint is ambiguous as recalled (a CNN is image '
    'recognition), so the poster has probably compressed the interviewer\'s actual restriction.')

add(20583, '2024-12-03', 'Jane Street', 'quant_developer', 'experienced', '2024', 'unknown',
    'phone_technical', 'Jane Street SWE 电面', 'unknown', 'phone coding', 'api_design',
    'Implement APIs for a tree class backend — Tree node的定义已知，所有API已知（不用实现）class Node {  vector getAncestors',
    'Implement APIs for a tree class backend. The tree node definition is given and all APIs are '
    'given (you do not implement them): class Node { vector getAncestors... (preview truncated)',
    None,
    '实现一个tree class的backendImplement APIs for a tree class backendTree node的定义已知，所有API已知（不用实现）class Node {\xa0\xa0vector getAncestors ...',
    'mixed',
    SWE_DOUBT + 'The class definition is truncated mid-signature by the preview, so which APIs '
    'were actually required is unknown.')

add(23478, '2025-05-31', 'Jane Street', 'quant_developer', 'experienced', '2025', 'unknown',
    'phone_technical', 'Jane Street 电面 (1 hour, first round)', 'unknown',
    'phone coding — poster says the emphasis is API design and clean code', 'ood_design',
    'Design a supermarket queue. Operations: add customer, change cu',
    'Design a supermarket queue. Operations: add customer, change cu... (preview truncated)',
    None,
    '我是一面，1小时时间。难度还好，感觉Jane Street面试更多是考API design和clean code，算法难度中等Design a supermarket queue.Operations: add customer,change cu ...',
    'mixed',
    SWE_DOUBT + 'The operation list is cut off after the second item. Note SIG was independently '
    'reported to ask a "design a supermarket checkout" OOD question, so nickname-level recalls '
    'like this one risk being attributed to the wrong firm.')

add(24268, '2025-07-20', 'Jane Street', 'quant_developer', 'experienced', '2025', 'unknown',
    'phone_technical', 'Jane Street 店面', 'unknown', 'phone coding, described as DP',
    'coding_simulation',
    'Implement 一个connect four的游戏，区别在于新放进去球会掉在最底下，然后把上面球顶上去。',
    'Implement a Connect Four game, except that a newly inserted ball drops to the very bottom '
    'and pushes the balls above it up.',
    None,
    '给大家发一个Jane Street 店面的DPImplement 一个connect four的游戏，区别在于新放进去球会掉在最底下，然后把上面球顶上去。求加米看帖子：）',
    'zh',
    SWE_DOUBT + 'The poster labels it "DP" but describes a simulation; win-condition and board '
    'size are unstated.')

add(23284, '2025-05-20', 'Jane Street', 'quant_developer', 'experienced', '2025', 'unknown',
    'phone_technical', 'Jane Street Production Engineer 电面', 'unknown', 'phone coding',
    'data_structure_design',
    '实现一个类似于Candy Crush游戏一样的数据结构。输入给一个按列存储的二维数据结构，每个元素是整数，代表游戏里不同的颜色',
    'Implement a data structure like the game Candy Crush. The input is a two-dimensional '
    'structure stored by column, each element an integer representing a different colour in the '
    'game.',
    None,
    '电面 Coding题目是实现一个类似于Candy Crush游戏一样的数据结构。这题好像金融公司时常面到。输入给一个按列存储的二维数据结构，每个元素是整数，代表游戏里不同的颜色',
    'zh',
    SWE_DOUBT + 'The poster themself notes this problem circulates across finance firms, so it is '
    'not distinctive to Jane Street; the match/clear rule is not stated.')

add(14711, '2022-09-19', 'Jane Street', 'quant_developer', 'experienced', 'unknown', 'unknown',
    'phone_technical', 'Jane Street phone', 'unknown', 'phone coding part 1', 'coding_parsing',
    '算数part 1: input是一个算数组，求结果只考虑+-x /eg. (4 + 5) x 6 = ? parser的部分不用写直接求结果',
    'Arithmetic, part 1: the input is an arithmetic array; compute the result considering only '
    '+ - x /, e.g. (4 + 5) x 6 = ? You do not need to write the parser, just produce the result.',
    None,
    '电话： 算数part 1: input是一个算数组，求结果只考虑+-x /eg. (4 + 5) x 6 = ?parser的部分不用写直接求结果',
    'zh',
    SWE_DOUBT + 'Four years old (2022) and the input representation ("一个算数组") is garbled in '
    'the recall, so the exact input format is unclear.')

# ---------------- Citadel ----------------
add(28247, '2026-04-28', 'Citadel', 'quant_researcher', 'experienced', '2026', 'unknown',
    'phone_technical', 'Citadel GQS Quant Researcher round 1', 'unknown',
    '30 min resume discussion then one technical question', 'optimization_theory',
    'min x^\\top Q x + c^\\top x, Q 和 c 都是实数，讨论什么时候，这个问题有finit',
    'Minimise x^T Q x + c^T x, where Q and c are real. Discuss when this problem has a finite '
    '(minimum) ... (preview truncated)',
    None,
    '2026 Citadel GQS QR全职，第一轮面试先讨论简历内容30分钟，只考了一个techiniacl questionmin x^\\top Q x + c^\\top xQ 和 c 都是实数讨论什么时候，这个问题有finit',
    'mixed',
    'The preview truncates at "有finit", so the exact property being asked about (finite minimum? '
    'finite solution set?) is inferred. The poster wrote the LaTeX themself, so spacing/notation '
    'is their reconstruction, not the interviewer\'s.')

add(28985, '2026-06-30', 'Citadel', 'quant_developer', 'experienced', '2026', 'unknown',
    'phone_technical', 'Citadel GQS SWE 电面', 'unknown',
    'whiteboard discussion, no code written; interviewer was a quant developer', 'coding_search',
    'Find all elements equal to K in a sorted array.',
    'Find all elements equal to K in a sorted array.',
    None,
    '面试官是quant developer 很有趣的面试体验 全程都没有写代码一直是白板讨论Problem1Find all elements equal to K in a sorted array.',
    'mixed',
    SWE_DOUBT + 'This is the opening of a staged question ("Step 1 最直接的回答") and the preview '
    'cuts off before the follow-ups, which are where the difficulty lives.')

add(26211, '2025-11-07', 'Citadel', 'quant_developer', 'experienced', '2025', 'unknown',
    'phone_technical', 'CTC 电面 (Citadel Securities phone)', 'unknown', 'phone coding',
    'cpp_implementation',
    '用c++写一个shared pointer class',
    'Write a shared pointer class in C++.',
    None,
    '用c++写一个shared pointer class有一个test case没过，死活debug不出来。',
    'zh',
    SWE_DOUBT + 'A stock C++ interview exercise; the thread title says CTC but the 1point3acres '
    'tag is #citadel, and Citadel and Citadel Securities are distinct entities that this recall '
    'does not disambiguate.')

add(26997, '2026-01-25', 'Citadel', 'quant_developer', 'experienced', '2026', 'unknown',
    'phone_technical', 'Citsec phone interview', 'unknown', 'phone coding, three parts',
    'data_structure_design',
    '[*]LRU implementation[*]LFU implementation[*]Customized Evict fu',
    'LRU implementation; LFU implementation; customised evict fu... (preview truncated)',
    None,
    'Citsec面试总是有一种，并不是很难，但是里面的人就打死都不想让你过的感觉。虽然还是过了[*]LRU implementation[*]LFU implementation[*]Customized Evict fu ...',
    'mixed',
    SWE_DOUBT + 'The third and most interesting item ("Customized Evict fu…") is truncated by the '
    'preview. LRU/LFU are ubiquitous and carry no firm-specific signal.')

add(27143, '2026-02-06', 'Citadel', 'quant_developer', 'experienced', '2026', 'unknown',
    'online_assessment', 'Citadel OA 优化题', 'unknown', 'OA optimisation question, C++',
    'code_optimization',
    '/// Refactor and speed up the code below /// The current implementation is correct but slow '
    'int root_node(std::vector out',
    'Refactor and speed up the code below. The current implementation is correct but slow. '
    'int root_node(std::vector out... (preview truncated)',
    None,
    '这个样板代码非常的奇葩#include /// Refactor and speed up the code below/// The current implementation is correct but slowint root_node(std::vector out ...',
    'mixed',
    SWE_DOUBT + 'The starter code is cut off at the first function signature, so the actual slow '
    'implementation that had to be optimised is not visible.')

add(27466, '2026-03-08', 'Citadel', 'quant_developer', 'experienced', '2026', 'unknown',
    'phone_technical', 'Citadel Securities 一面', 'unknown',
    'C++ Software Engineer, 1 hour: 30 min resume then 30 min OOD', 'concurrency_design',
    '后30分钟一道很简单的ood，实现一个Single Producer Multiple Consume',
    'The last 30 minutes was a very simple OOD: implement a single-producer multiple-consumer '
    '... (preview truncated)',
    None,
    '面试官是一个工作多年的中国人，岗位是C++ Software Engineer,一个小时面试时间，前30分钟拷打简历，后30分钟一道很简单的ood，实现一个Single Producer Multiple Consume ...',
    'zh',
    SWE_DOUBT + 'Truncated at "Consume"; whether a queue, buffer or full framework was required '
    'is not stated.')

add(26954, '2026-01-21', 'Citadel', 'quant_developer', 'experienced', '2026', 'unknown',
    'online_assessment', 'Citadel EQR OA (HackerRank)', 'HackerRank',
    'OA, three questions in 30 minutes', 'coding_mixed',
    'OA hackerrank，1个palindrome，1个lazy delete算token valid，最后一个bfs找tree的最长直径上的点',
    'HackerRank OA: one palindrome question, one lazy-delete "is this token valid" question, and '
    'a last one using BFS to find the points on the longest diameter of a tree.',
    None,
    '1.5 YOE hf devrecruiter reach outOA hackerrank,1个palindrome，1个lazy delete算token valid，最后一个bfs找tree的最长直径上的点，半小时三个都秒了',
    'zh',
    SWE_DOUBT + 'Topic labels only, no problem statements; "lazy delete 算 token valid" is too '
    'compressed to reconstruct.')

add(28725, '2026-06-06', 'Citadel', 'quant_developer', 'experienced', '2026', 'unknown',
    'online_assessment', '城堡 EQR OA', 'unknown', 'OA, three medium questions', 'coding_mixed',
    '三道medium[*]留斯奇: 但是注意最后要返回unique的子字符串[*]幺漆酒漆：比这道LC稍微简单一点，hashmap+list遍历[*]幺而丝雾：求树的直径的经典题',
    'Three mediums: [LeetCode number, homophone-obfuscated] but note you must return unique '
    'substrings at the end; [second LeetCode number], slightly easier than that LC problem, '
    'hashmap + list traversal; [third LeetCode number], the classic tree-diameter problem.',
    None,
    '三道medium[*]留斯奇: 但是注意最后要返回unique的子字符串[*]幺漆酒漆：比这道LC稍微简单一点，hashmap+list遍历[*]幺而丝雾：求树的直径的经典题',
    'zh',
    'The questions are named only by deliberately homophone-obfuscated LeetCode numbers '
    '(留斯奇/幺漆酒漆/幺而丝雾), a convention Chinese posters use to evade search. I have not '
    'decoded them and am not guessing, so no actual problem statement is recovered here.')

# ---------------- HRT ----------------
add(20369, '2024-11-14', 'HRT', 'quant_analyst', 'experienced', '2024', 'unknown',
    'phone_technical', 'HRT 面试 (video)', 'unknown', 'quant video interview', 'probability_coins',
    '我扔10个硬币，你扔九个，我的head比你多的概率',
    'I toss 10 coins and you toss nine; what is the probability that I get more heads than you?',
    None,
    '我扔10个硬币，你扔九个，我的head比你多的概率thread和process的区别一道bayes公式的口算',
    'zh',
    'This is a very well-known classic (answer 1/2 by symmetry) that appears in standard '
    'brainteaser collections, so its appearance here corroborates rather than reveals; the '
    'post is a three-item list with no interviewer wording.')

add(20369, '2024-11-14', 'HRT', 'quant_analyst', 'experienced', '2024', 'unknown',
    'phone_technical', 'HRT 面试 (video)', 'unknown', 'quant video interview',
    'probability_mental_math',
    '一道bayes公式的口算',
    'A mental-arithmetic question using Bayes\' formula.',
    None,
    '我扔10个硬币，你扔九个，我的head比你多的概率thread和process的区别一道bayes公式的口算',
    'zh',
    'The candidate records only that a Bayes mental-math question was asked, not what it was; '
    'this is a topic datapoint, not a question.')

add(20780, '2024-12-20', 'HRT', 'quant_developer', 'experienced', '2024', 'unknown',
    'online_assessment', 'HRT 水OA', 'unknown', 'OA', 'coding_arrays',
    '实现两个function: CountGreater (x) 求一个array里面多少个数大于x；CountLess (x) 求一个array里面多少个数小于x',
    'Implement two functions: CountGreater(x), how many numbers in an array are greater than x; '
    'CountLess(x), how many numbers in an array are less than x.',
    None,
    '[*]实现两个function:CountGreater (x) 求一个array里面多少个数大于xCountLess (x) 求一个array里面多少个数小于x[*]求一个字符串里面有多少个字母是重复出',
    'zh',
    SWE_DOUBT + 'No complexity requirement or update semantics are recorded, which is what would '
    'make this non-trivial.')

add(28458, '2026-05-13', 'HRT', 'quant_developer', 'experienced', '2026', 'unknown',
    'phone_technical', '哈家两轮店面 (HRT, two phone rounds)', 'coderpad',
    'round 1; interviewer dictated the problem verbally and the candidate had to take notes',
    'coding_simulation',
    '一维数组，N 个玩家向右走，watcher 从初始位置出发盯着玩家，被盯的玩家不能移动，watcher 会按给定时间戳',
    'A one-dimensional array; N players walk to the right; a watcher starts from an initial '
    'position and watches the players; a watched player cannot move; the watcher moves according '
    'to given timestamps ... (preview truncated)',
    None,
    '两轮都是面试官口述，要做笔记，参数漏一个就麻烦了。第一轮：一维数组，N 个玩家向右走，watcher 从初始位置出发盯着玩家，被盯的玩家不能移动，watcher 会按给定时间戳',
    'zh',
    SWE_DOUBT + 'The poster stresses the problem was dictated aloud and easy to mis-transcribe, '
    'and the preview cuts off before the watcher\'s movement rule is complete — so parameters are '
    'certainly missing. A second candidate (t.me/usinterview/26730, 2025-12-22) independently '
    'describes the same watcher problem, which supports it being real.')

add(25282, '2025-09-13', 'HRT', 'quant_analyst', 'experienced', '2025', 'unknown',
    'phone_technical', 'HRT 一面', 'unknown', 'first-round video interview', 'coding_simulation',
    '写Wordle。写出来但是挂了要求最后run。',
    'Write Wordle. I wrote it but failed — it was required to actually run at the end.',
    None,
    '问了一个题写Wordle。写出来但是挂了要求最后run。攒人品求米求米！',
    'zh',
    'One line; "write Wordle" leaves the required interface entirely unspecified. Tagged 金工类 '
    '(quant) on the forum despite being a coding task, hence the quant_analyst label.')

add(29079, '2026-07-28', 'HRT', 'quant_developer', 'experienced', '2026', 'unknown',
    'onsite', 'HRT 面筋 — onsite', 'unknown', 'system design round', 'system_design',
    '系统设计 多个simulator client 读一个 NFS，如何增加read throughput',
    'System design: multiple simulator clients read from one NFS — how do you increase read '
    'throughput?',
    None,
    '系统设计 多个simulator client 读一个 NFS,如何增加read throughput. 似乎面试官要讨论low level network知识，增加带宽，我不知道',
    'zh',
    SWE_DOUBT + 'The candidate says they did not know the answer and was guessing at what the '
    'interviewer wanted, so their framing of the question may be off. Posted 2026-07-28.')

add(23218, '2025-05-17', 'HRT', 'quant_developer', 'experienced', '2025', 'unknown',
    'phone_technical', 'HRT C++ dev 面经', 'unknown', 'C++ fundamentals round', 'cpp_concepts',
    'Inline in cpp - For functions; advantage vs disadvantage - For member variables. Segfaults. '
    'MMU how does it work; how does it translate between virtual and ph',
    'Inline in C++ — for functions: advantages vs disadvantages; for member variables. Segfaults. '
    'MMU: how does it work, how does it translate between virtual and ph... (preview truncated)',
    None,
    'Inline in cpp-For functions; advantage vs disadvantage-For member variablesSegfaults-MMU how does it work; how does it translate between virtual and ph ...',
    'en',
    SWE_DOUBT + 'A topic checklist written by the candidate, not interviewer wording, and cut off '
    'mid-item by the preview.')

add(28842, '2026-06-17', 'HRT', 'quant_developer', 'experienced', '2026', 'unknown',
    'online_assessment', 'HRT Software Engineer OA', 'CodeSignal',
    '4 questions / 70 min, Python required, ID upload and camera on throughout', 'coding_arrays',
    '类似lc一溜儿，输入是一个一维数组，找满足numbers < numbers和',
    'Similar to a LeetCode problem: the input is a one-dimensional array, find those satisfying '
    'numbers < numbers and ... (preview truncated)',
    None,
    'OA有四道题，总共70分钟，要求用Python，CodeSignal要上传ID，全程需要开摄像头好像都是没见过的新题[*]类似lc一溜儿，输入是一个一维数组，找满足numbers < numbers和',
    'zh',
    SWE_DOUBT + 'The condition is mangled — "numbers < numbers" is missing its array indices, '
    'almost certainly because square-bracket subscripts were stripped as BBCode by the forum. '
    'The proctoring detail (CodeSignal, ID upload, camera on) is the reliable part.')

# ---------------- IMC ----------------
add(26123, '2025-11-01', 'IMC', 'quant_trader', 'experienced', '2025', 'unknown',
    'onsite', 'IMC trading VO (virtual onsite)', 'unknown', 'trader video onsite',
    'probability_order_statistics',
    "Two RVs following uniform[0,1]. What's the probability of the smaller RV is less than the",
    "Two random variables following Uniform[0,1]. What is the probability that the smaller "
    "random variable is less than ... (preview truncated)",
    None,
    "IMC trading VO：[*]Why trading[*]What‘s your biggest achievement[*]Two RVs following uniform[0,1]. What's the probability of the smaller RV is less than the  ...",
    'en',
    'The preview truncates exactly at the threshold value ("less than the …"), so the question is '
    'incomplete — the specific bound is the whole content of the problem.')

add(26504, '2025-12-01', 'IMC', 'quant_trader', 'experienced', '2026', 'unknown',
    'phone_technical', 'IMC graduate trader technical interview (with HR)', 'unknown',
    'technical section of an HR-run interview', 'expected_value',
    '算渔获平均期望',
    'Compute the average/expected value of a fishing catch.',
    None,
    '跟hr做technical interview[*]Behavior：楼主在amazon做mle想半路出家做trader，所以问了很多这方面的问题（ps，amzn这破地儿真不想待了）[*]Technical：算渔获平均期望',
    'zh',
    'Five characters of description with no setup at all; unusable as a question, retained only '
    'as evidence that IMC\'s graduate-trader HR round contains an expected-value item. Labelled '
    '"graduate trader" but the forum tag is 全职/在职跳槽 (experienced), which conflicts.')

# ---------------- Optiver ----------------
add(23610, '2025-06-10', 'Optiver', 'quant_developer', 'experienced', '2025', 'APAC / China',
    'online_assessment', 'Optiver China Software Engineer Test - APAC - Online Assessment',
    'unknown', 'OA', 'coding_matrix_search',
    'Given a two-dimensional character matrix, create a function that identifies how many times '
    'the sequence "OPTIVER" appears. Matches can be found in straight lin',
    'Given a two-dimensional character matrix, create a function that identifies how many times '
    'the sequence "OPTIVER" appears. Matches can be found in straight lin... (preview truncated)',
    None,
    'Given a two-dimensional character matrix,create a function that identifies how many times the sequence "OPTIVER" appears. Matches can be found in straight lin ...',
    'en',
    SWE_DOUBT + 'Truncated at "straight lin…", so which directions count (rows/columns/diagonals, '
    'reversed) is missing — and that is the entire substance of the problem.')

add(24161, '2025-07-14', 'Optiver', 'quant_developer', 'experienced', '2025', 'unknown',
    'online_assessment', 'Optiver OA C++', 'unknown', 'OA question 1', 'coding_dates',
    '第一题是计算两个日期之间差了多少天',
    'Question 1: compute how many days there are between two dates.',
    None,
    '给大家提供一个Optiver OA C++的dp第一题是计算两个日期之间差了多少天第二题是验证给定的graph edges是不是一棵二叉树。如果是，返回二叉树的serialization；如果不是',
    'zh',
    SWE_DOUBT + 'No date range, calendar or format constraints are recorded.')

add(24161, '2025-07-14', 'Optiver', 'quant_developer', 'experienced', '2025', 'unknown',
    'online_assessment', 'Optiver OA C++', 'unknown', 'OA question 2', 'coding_trees',
    '第二题是验证给定的graph edges是不是一棵二叉树。如果是，返回二叉树的serialization；如果不是',
    'Question 2: verify whether the given graph edges form a binary tree. If so, return the '
    'serialization of the binary tree; if not, ... (preview truncated)',
    None,
    '第一题是计算两个日期之间差了多少天第二题是验证给定的graph edges是不是一棵二叉树。如果是，返回二叉树的serialization；如果不是',
    'zh',
    SWE_DOUBT + 'Truncated before the failure case is specified, and the required serialization '
    'format is not given.')

# ---------------- Akuna ----------------
add(25781, '2025-10-13', 'Akuna', 'quant_developer', 'experienced', '2025', 'unknown',
    'online_assessment', 'Akuna OA', 'unknown', 'OA', 'coding_matching_engine',
    'Write an exchange order Matching Engine. The supported operations are: BUY SELL CANCEL '
    'MODIFY PRINT',
    'Write an exchange order matching engine. The supported operations are: BUY, SELL, CANCEL, '
    'MODIFY, PRINT.',
    None,
    'Write an exchange order Matching Engine',
    'en',
    SWE_DOUBT + 'The Telegram preview contains zero-width characters between the operation names '
    'and truncates at "If th…", so the matching rules and output format are missing. The matching '
    'engine is a stock Akuna question reported for years.')

add(19777, '2024-10-08', 'Akuna', 'quant_developer', 'experienced', '2024', 'unknown',
    'online_assessment', 'Akuna Capital OA #1 SWE', 'unknown', 'OA, problem 11 "3s Wild"',
    'coding_card_game',
    '11. 3s Wild — Description: Sabrina and Mikhail are playing a card game with a deck of custom '
    'cards, each of which contains a sin',
    '11. 3s Wild — Description: Sabrina and Mikhail are playing a card game with a deck of custom '
    'cards, each of which contains a sin... (preview truncated)',
    None,
    'This is one of the problems. 11. 3s WildDescriptionSabrina and Mikhail are playing a card game with a deck of custom cards,each of which contains a sin ...',
    'en',
    SWE_DOUBT + 'This is genuinely the assessment\'s own wording (numbered problem with a '
    '"Description" header) but the preview cuts it off after 25 words, so the rules of "3s Wild" '
    'are not recovered.')

add(26126, '2025-11-02', 'Akuna', 'quant_developer', 'experienced', '2025', 'unknown',
    'phone_technical', 'Akuna trading system developer', 'unknown', 'OOD round', 'ood_design',
    "设计一个 Enemy 工厂，用于返回不同的 enemy instance. Let's suppose you are working for a very big "
    "online, micro-, multiplayer game company",
    "Design an Enemy factory that returns different enemy instances. Let's suppose you are "
    "working for a very big online, micro-, multiplayer game company... (preview truncated)",
    None,
    "设计一个 Enemy 工厂， 用于返回不同的 enemy instance.Let's suppose you are working for a very big online,micro-,multiplayer game company. company. And for th ...",
    'mixed',
    SWE_DOUBT + 'The English text has a duplicated word ("company. company.") suggesting sloppy '
    'copying, and is truncated at "And for th…".')

add(26984, '2026-01-24', 'Akuna', 'quant_developer', 'experienced', '2026', 'unknown',
    'onsite', 'Akuna Virtual Onsite', 'unknown', 'onsite question 1', 'ood_design',
    'Question 1. Task: To design and implement a class which can be used by client in their '
    'trading engine code to check if they can send ou',
    'Question 1. Task: To design and implement a class which can be used by a client in their '
    'trading engine code to check if they can send ou... (preview truncated)',
    None,
    '果然是最水quant厂哈哈哈Question 1.TaskTo design and implement a class which can be used by client in their trading engine code to check if they can send ou ...',
    'en',
    SWE_DOUBT + 'Truncated at "send ou…" — almost certainly an order-rate-limiter/throttle '
    'question, but I am not asserting that because the text does not say it.')

add(19607, '2024-09-27', 'Akuna', 'quant_developer', 'experienced', '2024', 'unknown',
    'online_assessment', 'Akuna C++ Engineer — HackerRank OA then coderpad phone',
    'HackerRank', 'OA then phone', 'coding_matching_engine',
    'hacker rank实现order book。2周后收到coderpad技术电面实现stl vector，用bytes提前占位，优化vector dynamic allocation效率',
    'HackerRank: implement an order book. Two weeks later, a coderpad technical phone screen: '
    'implement STL vector, pre-reserving bytes, optimising the efficiency of vector dynamic '
    'allocation.',
    None,
    '海投，hacker rank实现order book。2周后收到coderpad技术电面实现stl vector，用bytes提前占位，优化vector dynamic allocation效率。standard stl vector 15分钟写完',
    'zh',
    SWE_DOUBT + 'Two separate rounds compressed into one line; neither problem statement is '
    'given, only the topic.')

# ---------------- Five Rings ----------------
add(16534, '2023-10-01', 'Five Rings', 'quant_researcher', 'experienced', 'unknown', 'unknown',
    'phone_technical', 'Five Rings QR', 'unknown',
    'QR phone round — poster notes questions were asked rapidly under stress', 'geometry_probability',
    'Cut a square in the unit circle, find the area ratio of the unit circle.',
    'Cut a square in the unit circle, find the area ratio of the unit circle.',
    None,
    'Questions asked quickly. Need to respond under stress. Rice please![hide=188]-Cut a square in the unit circle,find the area ratio of the unit circle.',
    'en',
    'The wording is the candidate\'s ungrammatical English paraphrase ("find the area ratio of '
    'the unit circle" — ratio to what?), and the rest of the list sits behind the forum\'s '
    '[hide=188] karma tag, visible only as the first bullet in the Telegram preview.')

# ---------------- Two Sigma ----------------
add(15384, '2023-01-22', 'Two Sigma', 'quant_researcher', 'experienced', 'unknown', 'unknown',
    'online_assessment', 'Two Sigma QR OA', 'unknown', 'OA, two questions', 'coding_numerical',
    '就是地里常见的两道题，interpolation和linear regression',
    'The two questions commonly reported on the forum: interpolation and linear regression.',
    None,
    '22年十一月份被猎头搭讪，跟recruiter聊了聊。十二月份OA，就是地里常见的两道题，interpolation和linear regression。',
    'zh',
    'Topic names only; the poster is pointing at a shared forum question bank rather than '
    'describing the problems, and this is from December 2022.')

add(20368, '2024-11-14', 'Two Sigma', 'quant_researcher', 'experienced', '2024', 'unknown',
    'onsite', 'Two Sigma 面试 (onsite)', 'unknown', 'quant onsite', 'modelling_and_stats',
    'twitter 预测股价；纽约出租车供应和需求建模；线性回归解析解；lasso、ridge；lasso的最小角算法的几何解释',
    'Predict stock prices from Twitter; model New York taxi supply and demand; the closed-form '
    'solution of linear regression; lasso and ridge; the geometric interpretation of the least '
    'angle algorithm for lasso.',
    None,
    'twitter 预测股价纽约出租车供应和需求建模线性回归解析解lassoridgelasso的最小角算法的几何解释',
    'zh',
    'A run-on list with no punctuation, so my splitting into five separate topics is an '
    'interpretation; none of the items has an actual problem statement.')

add(15577, '2023-03-28', 'Two Sigma', 'quant_developer', 'experienced', 'unknown', 'unknown',
    'online_assessment', 'Two Sigma OA (75 min, 2 questions)', 'unknown', 'OA', 'coding_mixed',
    '75分钟，2道题，IPO和split tree，题目描述巨长，IPO就是排序以后iterate，相同price的计两个数',
    '75 minutes, 2 questions, "IPO" and "split tree"; the problem statements are extremely long. '
    'IPO is: sort then iterate, counting two numbers for equal prices.',
    None,
    '75分钟，2道题，IPO和split tree,感觉之前要是没看过，现想的话还挺费时间的，题目描述巨长，光看和理解描述花了10分钟，IPO就是排序以后iterate，相同price的计两个数，b',
    'zh',
    SWE_DOUBT + 'The poster explicitly says the real statements are "extremely long" and gives '
    'only their solution sketch, so the questions are not reproduced. From 2023.')

add(15135, '2022-11-17', 'Two Sigma', 'quant_developer', 'experienced', 'unknown', 'unknown',
    'phone_technical', 'Two Sigma phone', 'unknown', 'phone coding', 'coding_algorithms',
    '手寫Huffman Encoding',
    'Hand-write Huffman encoding.',
    None,
    'Two Sigma 手寫Huffman Encoding （但面試官好人）',
    'zh',
    SWE_DOUBT + 'Three characters of question. The same post advertises a third-party GitBook '
    '"question bank" for Two Sigma, which raises the possibility the poster is recycling that '
    'bank rather than reporting their own interview. From 2022.')

# ---------------- Belvedere ----------------
add(25867, '2025-10-17', 'Belvedere Trading', 'quant_researcher', 'experienced', '2025',
    'unknown', 'online_assessment', 'Belvedere Trading QR OA', 'unknown',
    'OA: 20 multiple choice + 1 coding', 'coding_data_analysis',
    'Coding题是给三只股票A,B,C,给出ABC的每日return和每日PnL，将ABC按照对PnL的影响排序',
    'The coding question gives three stocks A, B, C with their daily returns and daily PnL, and '
    'asks you to rank A, B and C by their contribution to PnL.',
    None,
    '20 道多选 1 道coding**** 本内容被作者隐藏 ****Coding题是给三只股票A,B,C,给出ABC的每日return和每日PnL，将ABC按照对PnL的影响排序打字不易，求米求米求米',
    'zh',
    'Belvedere is outside the named target-firm list. The 20 multiple-choice questions are behind '
    'the forum\'s hidden-content wall ("本内容被作者隐藏"); only the coding item leaked into the '
    'preview, and "影响" (contribution/impact) is not defined.')
# ---------------- emit ----------------
missing = []
out = []
for rec in R:
    mid = rec.pop('_mid')
    txt = page_text(mid)
    norm_txt = txt.replace('\u00a0', ' ').replace('\u200b', '')
    q = rec['source_quote'].replace('\u00a0', ' ').replace('\u200b', '')
    if q not in norm_txt:
        missing.append((mid, rec['firm'], q[:70]))
        continue
    out.append(rec)

if missing:
    sys.stderr.write('QUOTE NOT FOUND ON PAGE:\n')
    for m in missing:
        sys.stderr.write(f'  {m}\n')

os.makedirs('raw', exist_ok=True)
with open('raw/chat_and_archive.jsonl', 'a', encoding='utf-8') as f:
    for rec in out:
        f.write(json.dumps(rec, ensure_ascii=False) + '\n')
print(f'verified+written={len(out)}  failed={len(missing)}')
