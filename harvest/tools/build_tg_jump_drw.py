#!/usr/bin/env python3
"""Build JSONL records for Jump Trading, DRW and D. E. Shaw from harvested t.me
message pages. Every quote is verified against the stored page HTML before emitting.
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

PREVIEW = ('The Telegram link preview truncates the original post, so what is recorded is a '
           'fragment of the poster\'s own paraphrase rather than the assessment wording. ')
SWE = ('The forum role tag on this post is 码农类General (generic software engineer) at a trading '
       'firm, mapped to quant_developer as the nearest controlled value, so the role label may '
       'overstate how "quant" the role is. ')

R = []


def add(mid, date, firm, role, level, cycle, office, rnd, rname, platform, section, qtype,
        qtext, qtext_en, answer, quote, lang, doubt):
    R.append(dict(
        firm=firm, role_track=role, level=level, cycle=cycle, office=office, round=rnd,
        round_name=rname, platform=platform, section_context=section, question_type=qtype,
        question_text=qtext, question_text_en=qtext_en, reported_answer=answer,
        source_url=f'{CHANNEL}/{mid}', source_quote=quote, source_language=lang,
        post_date=date, **COMMON, doubt=doubt))
    R[-1]['_mid'] = str(mid)


# ================================ Jump Trading ================================
add(987, '2020-03-28', 'Jump Trading', 'quant_developer', 'experienced', 'unknown', 'unknown',
    'online_assessment', 'Jump Trading 2020 OA C++', 'unknown', 'OA question 1 of 3, 80 minutes',
    'coding_combinatorics',
    '第一题就是找到kth permutation',
    'Question 1 was just to find the kth permutation.',
    None,
    '刚做完Jump Trading的oa,3题80分钟，挺来不及的。 感觉是跪了，leetcode中难水平吧第一题就是找到kth permutation',
    'zh',
    SWE + 'Six years old (2020) and a bare topic label — no input format, no constraints. The '
    'remaining two questions are behind the forum\'s hidden-content marker '
    '("**** 本内容被作者隐藏 ****"), visible in the preview.')

add(4750, '2021-01-26', 'Jump Trading', 'quant_developer', 'experienced', 'unknown', 'unknown',
    'online_assessment', 'JUMP 2021 C++ OA — 4 questions in 4 hours', 'unknown',
    'OA question 1 of 4', 'coding_arrays',
    '给一个数，比如 318， 返回数字重新排列后最大值 831.',
    'Given a number, e.g. 318, return the largest value obtainable by rearranging its digits: 831.',
    '831 for the example input 318',
    '4道题，一共4小时。1. 给一个数，比如 318， 返回数字重新排列后最大值 831.',
    'zh',
    SWE + 'Five years old (2021). The statement as recalled is trivially "sort the digits '
    'descending", which suggests the real constraints (negative numbers? leading zeros? '
    'next-greater rather than greatest?) were dropped in the recall.')

add(4750, '2021-01-26', 'Jump Trading', 'quant_developer', 'experienced', 'unknown', 'unknown',
    'online_assessment', 'JUMP 2021 C++ OA — 4 questions in 4 hours', 'unknown',
    'OA question 2 of 4', 'coding_stack_machine',
    '2. Word Machine，see https://leetcode.com/discuss/interview-question/algorithms/83',
    'Question 2: "Word Machine", see the LeetCode discuss interview-question thread (URL truncated '
    'in the preview).',
    None,
    '2. Word Machine，see  https://leetcode.com/discuss/interview-question/algorithms/83',
    'zh',
    SWE + PREVIEW + 'The poster does not restate the problem at all — they point at an external '
    'LeetCode discuss thread whose URL is itself cut off mid-ID by the preview, so the question is '
    'identified only by the name "Word Machine".')

add(5747, '2021-03-17', 'Jump Trading', 'quant_developer', 'experienced', 'unknown', 'NYC',
    'phone_technical', '【NYC】Jump Trading 奇葩电面 — atypical phone screen', 'unknown',
    'phone screen run by a Quant Researcher hiring an engineer for their desk',
    'debugging_log_analysis',
    '面试是非典型面试，不直接问你题，一上给你一个 .tar.gz 的 logs file',
    'The interview was atypical: rather than asking you a question directly, they immediately give '
    'you a .tar.gz logs file ... (preview truncated)',
    None,
    '分享一个前几周的 Jump Trading 电面。面试官是 Quant Researcher，要给他们组招一个 engineer。面试是非典型面试，不直接问你题，一上给你一个 .tar.gz 的 logs file',
    'zh',
    SWE + PREVIEW + 'Cut off exactly where the task would be stated — we learn only that the '
    'candidate was handed a compressed log archive, not what they had to find in it. Five years old '
    '(2021).')

add(9186, '2021-12-11', 'Jump Trading', 'quant_trader', 'experienced', 'unknown', 'unknown',
    'online_assessment', 'Jump Crypto Quant Trader OA', 'unknown',
    'OA format report for the trader track (not a question)', 'assessment_format',
    '他们trader的coding test都不太考纯算法，都带一点brain te',
    'Their trader coding test does not really test pure algorithms; every question has a bit of '
    'brain te[aser] in it ... (preview truncated)',
    None,
    '之前找jump trading的面经好像都没几个，jump crypto根本没有面经，贡献个数据点希望能帮助到地里的小伙伴吧。他们trader的coding test都不太考纯算法，都带一点brain te',
    'zh',
    'Format datapoint only, no question. Also note the entity is Jump Crypto, a separate business '
    'from Jump Trading, and the firm label here follows the poster\'s framing. From 2021.')

add(13726, '2022-07-05', 'Jump Trading', 'quant_developer', 'experienced', 'unknown', 'Singapore',
    'onsite', 'Jump Trading C++ VO (video onsite), 50 minutes', 'unknown',
    'the ~30-minute coding portion of a 50-minute video round', 'cpp_implementation',
    '实现一个Vector类如下，template Vector {  void ...',
    'Implement a Vector class as follows: template Vector { void ... (preview truncated)',
    None,
    '投了新加坡的C++岗，他们家响应速度挺慢的，面完了一个多星期才回复。总共聊了50分钟，中间30多分钟做一道题，实现一个Vector类如下，template Vector {  void ...',
    'zh',
    SWE + PREVIEW + 'The class skeleton is cut off at the first member, so which operations were '
    'required is unknown. "Implement std::vector" is the single most common C++ buy-side screen '
    'question industry-wide and carries little firm-specific signal — the same question is '
    'independently reported at SIG and Akuna elsewhere in this file.')

add(13952, '2022-07-20', 'Jump Trading', 'quant_developer', 'experienced', 'unknown', 'unknown',
    'onsite', 'Jump Trading VO — 2 questions in 90 minutes', 'unknown', 'VO question 1 of 2',
    'coding_strings',
    '第一题，类似于string compression. 给一个string,还有Integer k,每次可以删掉连续的k个一样的字母，返回最终结果。',
    'Question 1, similar to string compression: given a string and an integer k, each time you may '
    'delete k consecutive identical letters; return the final result.',
    None,
    '刚刚结束的VO，两道题，90分钟。没有原题第一题，类似于string compression. 给一个string,还有Integer k,每次可以删掉连续的k个一样的字母，返回最终结果。第二题， ',
    'zh',
    SWE + 'The poster says explicitly "没有原题" (none of these were recycled questions), which is a '
    'point in favour of authenticity, but the second question is cut off by the preview at "第二题，". '
    'From 2022.')

add(14079, '2022-07-29', 'Jump Trading', 'quant_developer', 'experienced', 'unknown', 'unknown',
    'online_assessment', 'Jump Trading PE/SRE OA — 40 minutes', 'unknown',
    'OA format report (not a question)', 'assessment_format',
    '一共四十分钟。准备的面经都没用上，十道shell的单选题+一道编程题。选择题答案可能有错，仅供参考。1. 如何',
    'Forty minutes in total. None of the interview recalls I had prepared were any use: ten '
    'multiple-choice shell questions plus one programming question. My answers to the '
    'multiple-choice may be wrong, for reference only. 1. How to ... (preview truncated)',
    None,
    '看网上应该还没有人发过PE/SRE的OA。来贡献一下DP。一共四十分钟。准备的面经都没用上，十道shell的单选题+一道编程题。选择题答案可能有错，仅供参考。1. 如何',
    'zh',
    SWE + PREVIEW + 'Cut off at "1. 如何" (1. How to …), so not one of the eleven items is actually '
    'recoverable. The structure claim — ten shell multiple-choice plus one coding question in 40 '
    'minutes for the Production Engineering / SRE track — is the only usable content. From 2022.')

add(15102, '2022-11-10', 'Jump Trading', 'quant_developer', 'experienced', 'unknown', 'unknown',
    'phone_technical', 'Jump Trading cpp 在线面试', 'unknown', 'systems and C++ round, three items',
    'cpp_concepts',
    '1 heap、stack区别，有哪些场景应用；如何申请内存的， 谁快谁慢2 TCP UDP区别 3 coding 实现个 vector',
    '1. The difference between heap and stack, what scenarios each is used in, how memory is '
    'requested, which is faster. 2. The difference between TCP and UDP. 3. Coding: implement a '
    'vector.',
    None,
    '总体来说不算难，但是感觉没答好1 heap、stack区别，有哪些场景应用；如何申请内存的， 谁快谁慢2 TCP UDP区别 3 coding 实现个 vector',
    'zh',
    SWE + 'This is the whole post — three topic labels, no interviewer wording. Heap-vs-stack and '
    'TCP-vs-UDP are generic systems-interview staples with no firm-specific signal. From 2022.')

add(17398, '2024-01-31', 'Jump Trading', 'quant_developer', 'experienced', '2024', 'unknown',
    'online_assessment', 'Jump Trading PE (Production Engineering) OA — 150 minutes', 'unknown',
    'the Python coding item in an OA of 10 shell multiple-choice plus coding', 'coding_arrays',
    '一道python，三个数组，一个int数组prices代表股票',
    'One Python question: three arrays, one int array "prices" representing stock ... (preview '
    'truncated)',
    None,
    '海投的，HR聊了一下就OA， 因为没看C++已经跪了。150分钟， 单选10道，shell问题，和坛子上那个PE面经贴的一样一道python，三个数组，一个int数组prices代表股票',
    'zh',
    SWE + PREVIEW + 'Truncated at "代表股票" (representing stock…), so the other two arrays and the '
    'actual task are unknown. The poster also says the multiple-choice section was identical to an '
    'earlier forum PE recall, which means Jump recycles this OA — useful, but it also means the '
    'poster may be describing the earlier post rather than their own paper.')

add(20375, '2024-11-14', 'Jump Trading', 'quant_developer', 'experienced', '2024', 'unknown',
    'onsite', 'Jump Trading onsite — infrastructure team, no superday', 'unknown',
    'onsite coding round 1', 'coding_matrix',
    'coding 1一个矩阵有数字，输出数字按snake 顺序（从上到下，',
    'Coding 1: a matrix contains numbers; output the numbers in snake order (from top to bottom, '
    '... (preview truncated)',
    None,
    '是某个做infra的组在招，不是quant dev，纯码农没有superday，就是过几天面一个人过几天面一个人这样子coding 1一个矩阵有数字，输出数字按snake 顺序（从上到下，',
    'zh',
    SWE + PREVIEW + 'Cut off mid-definition of "snake order", which is the entire content of the '
    'problem. The poster states outright that this was an infrastructure team and "不是quant dev" '
    '(not quant dev), so it is the least quant-relevant record here.')

add(24503, '2025-08-01', 'Jump Trading', 'quant_developer', 'experienced', '2025', 'unknown',
    'online_assessment', 'Jump Trading OA — 2 questions in 125 minutes', 'unknown',
    'OA question 1 of 2', 'coding_pattern_matching',
    '买卖股票，给一个[stork price],一个[sell pattern],一个. 其中sell pattern和buy pattern是由-1，1的数组组成，1代表上涨，-1代表下跌，例如',
    'Buying and selling stock: you are given a [stock price] array, a [sell pattern], and a ... '
    'where the sell pattern and buy pattern are arrays of -1 and 1, with 1 meaning a rise and -1 '
    'meaning a fall, for example ... (preview truncated)',
    None,
    '两个问题，一共125分钟[*]买卖股票，给一个[stork price],一个[sell pattern],一个. 其中sell pattern和buy pattern是由-1，1的数组组成，1代表上涨，-1代表下跌，例如',
    'zh',
    SWE + PREVIEW + 'The third input is literally elided in the source ("一个." — "a ."), and the '
    'worked example is cut off, so the task is not reconstructable. The forum role tag on this post '
    'is MachineLearningEng, not a quant tag.')

add(25780, '2025-10-13', 'Jump Trading', 'quant_developer', 'experienced', '2025', 'unknown',
    'phone_technical', 'jump店面 (phone screen) — quant dev', 'unknown',
    'phone screen debugging question, 12 test cases, problem shown as a screenshot',
    'debugging_workflow',
    'debugging的题 有点莫名其妙的一题 可以看截图一共12个testcase … Consider a workflow management',
    'A debugging question — a rather baffling one, you can look at the screenshot; 12 test cases in '
    'total. … "Consider a workflow management ..." (preview truncated)',
    None,
    'jump trading quant dev面筋 debugging的题 有点莫名其妙的一题 可以看截图一共12个testcase 祝各位好运以及多多求米!!!!!!!!!!!!!Consider a workflow management ',
    'mixed',
    SWE + 'The actual problem was posted as a screenshot the poster tells readers to look at '
    '("可以看截图"), and the preview cuts off after the first four words of the visible English text '
    '("Consider a workflow management"). I did not see the screenshot. Corroborated by an '
    'independent 2026-02 recall (t.me/usinterview/27084) that also names a "workflow management '
    'system debug" item, so the question appears to be a recurring Jump screen.')

add(27084, '2026-02-01', 'Jump Trading', 'quant_developer', 'experienced', '2026', 'unknown',
    'online_assessment', 'Jump Trading OA', 'unknown', 'OA, two items', 'coding_mixed',
    '[*]source file and destination file comparison，有更改就return[*]workflow management system debug 嵌套input处理',
    'source file and destination file comparison — return if there is any change; workflow '
    'management system debug — handling nested input.',
    None,
    '[*]source file and destination file comparison，有更改就return[*]workflow management system debug 嵌套input处理',
    'mixed',
    SWE + 'This is the entire post: two headline labels with no problem statements, input formats '
    'or examples. Its value is corroborative — the "workflow management system debug" item matches '
    'the screenshot-only phone-screen question another candidate reported four months earlier '
    '(t.me/usinterview/25780).')

add(29064, '2026-07-26', 'Jump Trading', 'quant_developer', 'experienced', '2026', 'unknown',
    'online_assessment', 'Jump Trading C++ Developer, Crypto Team 2026 — OA of 3 questions',
    'unknown', 'OA questions 1 and 2 of 3', 'coding_mixed',
    'OA (3 questions,all relatively easy):Find the largest number of equal fractions.Find the size '
    'of the largest subset such t',
    'OA (3 questions, all relatively easy): Find the largest number of equal fractions. Find the '
    'size of the largest subset such t... (preview truncated)',
    None,
    'Process: OA + 3 technical roundsOA (3 questions,all relatively easy):Find the largest number of equal fractions.Find the size of the largest subset such t ',
    'en',
    SWE + PREVIEW + 'The second item is cut off at "such t…", which is where its defining condition '
    'would be, and the third question is not visible at all. Posted 2026-07-26, six days before '
    'this harvest, so it is the freshest Jump datapoint here.')

# ==================================== DRW ====================================
add(4559, '2021-01-11', 'DRW', 'quant_researcher', 'experienced', 'unknown', 'unknown',
    'onsite', 'DRW desk quant video interview with two team members', 'unknown',
    'resume-driven technical discussion', 'modelling_discussion',
    '问了简历内容，包括一些model的具体细节，主要是interest rate curv',
    'They asked about the content of my resume, including specific details of some models, mainly '
    'interest rate curv[es] ... (preview truncated)',
    None,
    '发个面经回馈地里。面的是一个desk quant岗位， 具体步骤是过了HR简历筛选以后和组里两位成员视频面试，问了简历内容，包括一些model的具体细节，主要是interest rate curv',
    'zh',
    PREVIEW + 'Cut off at "interest rate curv…". This describes the round\'s subject matter — a '
    'resume-driven interest-rate-curve modelling discussion for a desk quant role — but contains no '
    'question. Five years old (2021).')

add(16104, '2023-07-26', 'DRW', 'quant_developer', 'experienced', 'unknown', 'unknown',
    'online_assessment', 'DRW OA, July 2023 — 3 questions, 2-hour limit', 'unknown',
    'OA topic list (not question statements)', 'coding_mixed',
    '第一道题：Graph第二道题：Graph第三道题：String + Hashmap',
    'Question 1: Graph. Question 2: Graph. Question 3: String + Hashmap.',
    None,
    '很简单，三道题，限时两小时但能在半小时内完成。并不像其他楼主说的那么难。第一道题：Graph第二道题：Graph第三道题：String + Hashmap',
    'zh',
    SWE + 'Three bare topic tags — "Graph", "Graph", "String + Hashmap" — with no problem '
    'statements whatsoever. Included because it is the only DRW OA structural datapoint recovered '
    '(3 questions / 2 hours) and because it directly contradicts other forum posters who called the '
    'DRW OA hard. From 2023.')

add(19697, '2024-10-04', 'DRW', 'quant_developer', 'experienced', '2024', 'unknown',
    'online_assessment', 'DRW Codility screen — 1 question in 30 minutes', 'Codility',
    'a candidate asking whether this round is new (not a question)', 'assessment_format',
    '有没有做了DRW 30分钟一道题的Codility的，地里没看到过，是新出的环节吗',
    'Has anyone done the DRW Codility with one question in 30 minutes? I have not seen it on the '
    'forum — is it a newly added stage?',
    None,
    '有没有做了DRW 30分钟一道题的Codility的，地里没看到过，是新出的环节吗',
    'zh',
    'This is a question *from* a candidate to the forum, not an assessment question. It records '
    'that DRW added a one-question 30-minute Codility screen around October 2024, and that this was '
    'novel enough that the candidate could find no prior recall of it. No problem content at all.')

add(23427, '2025-05-29', 'DRW', 'quant_developer', 'experienced', '2025', 'unknown',
    'phone_technical', 'drw 店面挂经 (failed phone screen)', 'unknown',
    'phone screen — mostly rote fundamentals', 'systems_concepts',
    '考的是八股多一些，以及iso protocol没怎么准备，所以也不意外会不过',
    'What was tested was mostly rote fundamentals ("八股"), plus ISO protocol, which I had not really '
    'prepared, so it is no surprise I did not pass.',
    None,
    '考的是八股多一些，以及iso protocol没怎么准备，所以也不意外会不过',
    'zh',
    'This is the complete post. The only concrete content is that "ISO protocol" came up, and even '
    'that is ambiguous — the candidate may mean ISO 8583, an ISO-standard messaging protocol, or '
    'something else entirely. Recorded as a topic datapoint, not a question. The forum role tag is '
    '工程类 (engineering), not a quant tag.')

add(23146, '2025-05-14', 'DRW', 'quant_developer', 'experienced', '2025', 'unknown',
    'take_home', 'DRW Software Engineer (full stack) take-home', 'unknown',
    'take-home assignment (not a question statement)', 'assessment_format',
    '给我搞了个take home，是这个： https://www.glassdoor.com/Interview/DRW-Software-Engineer-Interview-Questions-EI',
    'They gave me a take-home, which was this one: https://www.glassdoor.com/Interview/'
    'DRW-Software-Engineer-Interview-Questions-EI... (URL truncated in the preview)',
    None,
    '面了DRW 的software engineer，不是c++是full stack。给我搞了个take home，是这个： https://www.glassdoor.com/Interview/DRW-Software-Engineer-Interview-Questions-EI',
    'zh',
    'The poster does not describe the take-home at all — they simply point at a Glassdoor page, '
    'whose URL the preview truncates, and Glassdoor is Cloudflare-blocked to this machine. So the '
    'assignment content is unrecovered. The one solid fact is that DRW\'s 2025 full-stack SWE '
    'pipeline used a take-home that candidates believed was already published on Glassdoor.')

# ================================= D. E. Shaw =================================
add(26465, '2025-11-25', 'D. E. Shaw', 'quant_developer', 'experienced', '2025', 'unknown',
    'phone_technical', 'd.e. shaw 几轮电面 — SWE genAI role, several phone rounds', 'unknown',
    'post recording that content is hidden (not a question)', 'assessment_format',
    '有猎头reach out就面了一下de shaw 的swe genAI 岗位不知道大家对于这种公司的swe或者AI岗位有什么了解。**** 本内容被作者隐藏 ****目前面下来感觉也没有很难，',
    'A headhunter reached out so I interviewed for D. E. Shaw\'s SWE genAI role. I wonder what '
    'people know about SWE or AI roles at this kind of firm. **** This content has been hidden by '
    'the author **** So far the interviews have not felt very hard,',
    None,
    '有猎头reach out就面了一下de shaw 的swe genAI 岗位不知道大家对于这种公司的swe或者AI岗位有什么了解。**** 本内容被作者隐藏 ****目前面下来感觉也没有很难， ',
    'zh',
    'NO QUESTION CONTENT. This is the only D. E. Shaw recall in the entire Telegram mirror with any '
    'readable text, and its substance is explicitly hidden by the author '
    '("**** 本内容被作者隐藏 ****"). It is recorded so the file shows what was searched and found '
    'rather than implying D. E. Shaw was not looked for; the firm is effectively a blank in this '
    'shard.')

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

if missing:
    sys.stderr.write('QUOTE NOT FOUND ON PAGE:\n')
    for m in missing:
        sys.stderr.write(f'  {m}\n')

with open('raw/chat_and_archive.jsonl', 'a', encoding='utf-8') as f:
    for rec in out:
        f.write(json.dumps(rec, ensure_ascii=False) + '\n')
print(f'verified+written={len(out)}  failed={len(missing)}')
