#!/usr/bin/env python3
"""Optiver assessment content recovered from archived and cached copies of 1point3acres.

1point3acres Cloudflare-blocks this machine outright (direct fetch and the r.jina.ai text proxy
both return the security interstitial). Two of the four threads below survive as Wayback
snapshots and were read in full from the archive; the other two have no snapshot at all
(archive.org/wayback/available and a CDX sweep both empty) and are readable only as a search
engine's cached extract, which is preserved verbatim in
raw/pages/websearch_highlights_1p3a.txt and marked access="snippet_only".

Quotes are checked against the stored copy of whichever artefact they came from.
"""
import html
import json
import re
import sys

SNIP = open('raw/pages/websearch_highlights_1p3a.txt', encoding='utf-8').read()
_wb = {}


def wb(tid):
    if tid not in _wb:
        # Discuz serves these pages as GBK; reading them as UTF-8 turns every Chinese run to mojibake.
        raw = open(f'raw/pages/wayback/p3a_{tid}.html', 'rb').read().decode('gbk', errors='replace')
        s = re.sub(r'<script.*?</script>', ' ', raw, flags=re.S)
        s = re.sub(r'<br\s*/?>', '\n', s)
        s = re.sub(r'<[^>]+>', ' ', s)
        s = html.unescape(s)
        _wb[tid] = re.sub(r'[ \t\u00a0]+', ' ', s)
    return _wb[tid]


BLOCK = ('1point3acres is Cloudflare-blocked to this machine — a direct fetch and the r.jina.ai '
         'text proxy both return the "Performing security verification" interstitial, verified '
         'the same day')
KARMA = ('1point3acres hides the rest of the post behind a 188-karma wall, so an unknown amount of '
         'the recall is not readable at all')

R = []


def add(src, tid, firm, role, level, cycle, rnd, rname, section, qtype, qtext, qtext_en,
        quote, poster, doubt, answer=None, office='unknown', lang='zh', post_date='unknown',
        wburl=None):
    R.append({
        'firm': firm, 'role_track': role, 'level': level, 'cycle': cycle, 'office': office,
        'round': rnd, 'round_name': rname, 'platform': 'unknown', 'section_context': section,
        'question_type': qtype, 'question_text': qtext, 'question_text_en': qtext_en,
        'reported_answer': answer,
        'source_url': f'https://www.1point3acres.com/bbs/thread-{tid}-1-1.html',
        'source_type': 'other', 'source_quote': quote, 'source_language': lang,
        'post_date': post_date,
        'access': 'archive_only' if src == 'wb' else 'snippet_only',
        'retrieval_method': 'wayback' if src == 'wb' else 'websearch_snippet',
        'upstream_source': None, 'poster_context': poster, 'doubt': doubt,
        '_src': src, '_tid': tid})


# ======================================================== thread 1164459 — Wayback, Number Logic
WB_1164459 = ('Read from the Wayback Machine snapshot '
              'http://web.archive.org/web/20260210113710/https://www.1point3acres.com/bbs/'
              'thread-1164459-1-1.html. ' + BLOCK)
CTX_1164459 = ('Posted to the 1point3acres 海外面经 board under the structured tags '
               '"2026(1-3月) 金工类 博士 其他@optiver - 网上海投 - 在线笔试 | 😐 Neutral 😣 Hard | '
               'Fail | 其他" — a PhD applying speculatively on the quant track, online written '
               'test, found it hard, failed. They close with 做完感悟是自己不适合搞quant ：） '
               '(having finished it, my takeaway is that I am not cut out for quant). '
               + WB_1164459)
D_1164459 = ('The poster is explicit that these are reconstructed from their scratch paper and that '
             'they are not sure of the answers — 草稿纸上还记得的一些比较confused的题（不保证答案'
             '是对的）, "some of the more confusing questions I can still remember from my scratch '
             'paper (no guarantee the answers are right)". So the terms could be misremembered or '
             'mis-ordered, and the numbers after the ？ are the poster\'s own attempted answers, not '
             'given solutions. A replier disputes one of them outright. Only three of the four '
             'sections are described before the karma wall cuts in. ' + KARMA)

add('wb', '1164459', 'Optiver', 'quant_researcher', 'unknown', '2026', 'online_assessment',
    'Optiver OA — three timed sections that must be taken in order',
    'the structure of the assessment as the poster gives it',
    'assessment_format',
    '一共三个部分必须按照顺序做：1）Number Logic 25min 2）Beat the Odds 45min 3) Likelihood Test 25min',
    ('There are three parts in total and they must be done in order: 1) Number Logic 25 min '
     '2) Beat the Odds 45 min 3) Likelihood Test 25 min.'),
    '一共三个部分必须按照顺序做：1）Number Logic 25min 2）Beat the Odds 45min 3) Likelihood Test 25min',
    CTX_1164459,
    ('Not a question — the section list and timings. It is worth logging because it independently '
     'corroborates, from a completely different platform and language, the module names and '
     'durations in the Optiver instruction table a reddit poster pasted (Number Logic 25 min, Beat '
     'The Odds 45 min, Likelihood-list ~25 min). The discrepancy is that this candidate got three '
     'sections where the reddit paste lists five, so the battery evidently varies by role or cycle.'),
    post_date='2026-02-08', lang='mixed')

for i, (seq, ans) in enumerate([
        ('1 2 3 16/5 25/8 36/13 ？ 49/21', None),
        ('2 2 3 4 5 8 8 ？16', '16 (the poster\'s own attempted answer)'),
        ('4 5 9 13 22 31 ？53', '53 (the poster\'s own attempted answer; a replier argues it is 40)'),
        ('3 2 4 4 12 36 ？396', '396 (the poster\'s own attempted answer)')]):
    add('wb', '1164459', 'Optiver', 'quant_researcher', 'unknown', '2026', 'online_assessment',
        'Optiver OA section 1, Number Logic, 25 minutes',
        f'sequence {i + 1} of the four the poster reconstructed from scratch paper',
        'number_sequence',
        seq,
        f'Complete the sequence: {seq.replace("？", "?")}',
        seq, CTX_1164459, D_1164459, answer=ans, lang='en')

add('wb', '1164459', 'Optiver', 'quant_researcher', 'unknown', '2026', 'online_assessment',
    'Optiver OA section 1, Number Logic, 25 minutes',
    'the fifth sequence, cut off mid-list by the karma wall',
    'number_sequence',
    '2 1 2 5 13',
    'Complete the sequence: 2 1 2 5 13 …',
    '2 1 2 5 13 您好！',
    CTX_1164459,
    ('Truncated: the karma-wall placeholder ("您好！本帖隐藏的内容需要积分高于 188 才可浏览") begins '
     'immediately after "13", so the rest of the sequence and the blank are not readable. Logged as '
     'a partial. ' + D_1164459),
    lang='en')

add('wb', '1164459', 'Optiver', 'quant_researcher', 'unknown', '2026', 'online_assessment',
    'Optiver OA section 1, Number Logic, 25 minutes',
    'a replier contesting the poster\'s answer to one of the sequences',
    'solution_discussion_only',
    '4 5 9 13 22 31 ？53\n\n这个答案是不是应该是40而不是53？',
    'For "4 5 9 13 22 31 ? 53" — shouldn\'t the answer be 40 rather than 53?',
    '4 5 9 13 22 31 ？53\n\n这个答案是不是应该是40而不是53？',
    ('A replier on the same 1point3acres thread, quoting the original poster\'s sequence back at '
     'them. ' + WB_1164459),
    ('Not a question but a dispute over one, and it is the most useful thing on the page for '
     'calibration: it shows the "answers" in the original post are the candidate\'s guesses, not the '
     'assessment\'s key, and that at least one of them is contested by another reader. Neither party '
     'gives a rule for the sequence.'),
    lang='mixed')

# ======================================================== thread 1141209 — Wayback, QR intern OA
WB_1141209 = ('Read from the Wayback Machine snapshot '
              'http://web.archive.org/web/20250910211053/https://www.1point3acres.com/bbs/'
              'thread-1141209-1-1.html. ' + BLOCK)
CTX_1141209 = ('Posted to 1point3acres 海外面经 as "Optiver 2026 Quantitative Research Intern-OA" on '
               '2025-08-13. The poster says the OA is mass-mailed on application (刚投递就收到OA了), '
               'has four sections, is 强度很大 (very intense), and that although the email does not '
               'say so the sections can be taken on separate days. They were rejected the day after '
               'finishing. ' + WB_1141209)
D_1141209 = ('The poster paraphrases rather than reproducing prompts, and says of the first coding '
             'question outright 题目有点记不清楚了 (I cannot quite remember the question). The middle '
             'of the post is behind the karma wall, so the section boundaries around the probability '
             'items are inferred from position rather than stated. ' + KARMA)

add('wb', '1141209', 'Optiver', 'quant_researcher', 'internship', '2026', 'online_assessment',
    'Optiver 2026 Quantitative Research Intern OA — four sections; the coding section is 90 minutes '
    'on HackerRank',
    'coding question 1 of the 90-minute HackerRank section',
    'combinatorics_arrangements',
    '第一题：题目有点记不清楚了，但是不难，核心考点是考m个a和n个b的排列组合有多少个',
    ('Question 1: I cannot quite remember the question, but it was not hard — the core point being '
     'tested is how many arrangements there are of m a\'s and n b\'s.'),
    '第一题：题目有点记不清楚了，但是不难，核心考点是考m个a和n个b的排列组合有多少个',
    CTX_1141209,
    ('The poster states in the same breath that they cannot remember the question, so what is logged '
     'here is their reading of what it tested, not the prompt. Whether the arrangements were '
     'unrestricted or subject to some adjacency or ordering constraint — the thing that would make it '
     'a real problem rather than a binomial coefficient — is exactly what is missing. ' + D_1141209),
    post_date='2025-08-13', lang='mixed')

add('wb', '1141209', 'Optiver', 'quant_researcher', 'internship', '2026', 'online_assessment',
    'Optiver 2026 Quantitative Research Intern OA — four sections; the coding section is 90 minutes '
    'on HackerRank',
    'coding question 2 of the 90-minute HackerRank section',
    'orderbook_simulation',
    ('第二题：股票交易，给你一个orders, 是一个2d array, 里面有 [1, 15]; [-1; 30]....1 代表买，-1 代表买，'
     '后面是价格；'),
    ('Question 2: stock trading. You are given orders, a 2-D array containing [1, 15]; [-1; 30]…; 1 '
     'means buy, -1 means buy [sic], and the number after it is the price.'),
    ('第二题：股票交易，给你一个orders, 是一个2d array, 里面有 [1, 15]; [-1; 30]....1 代表买，-1 代表买，'
     '后面是价格；'),
    CTX_1141209,
    ('The input format is given concretely but the task is not — the post runs straight into the '
     'karma wall after "后面是价格；", so what you are supposed to compute from the order list is '
     'entirely missing. The poster also plainly mistypes the encoding: they write "1 代表买，-1 代表买" '
     '(1 means buy, -1 means buy), where -1 must mean sell. ' + D_1141209),
    post_date='2025-08-13', lang='mixed')

add('wb', '1141209', 'Optiver', 'quant_researcher', 'internship', '2026', 'online_assessment',
    'Optiver 2026 Quantitative Research Intern OA — the probability section',
    'a probability item listed after the karma wall',
    'probability_dice_expectation',
    '骰子掷出每个面的平均次数',
    'The average number of throws for a die to show every face.',
    '骰子掷出每个面的平均次数',
    CTX_1141209,
    ('Seven characters. This is a topic label, not a prompt: it reads as the coupon-collector '
     'expectation for a die, but "平均次数" could equally mean the expected count of each face in a '
     'fixed number of throws, and the poster gives nothing that would disambiguate. No answer. '
     + D_1141209),
    post_date='2025-08-13', lang='zh')

add('wb', '1141209', 'Optiver', 'quant_researcher', 'internship', '2026', 'online_assessment',
    'Optiver 2026 Quantitative Research Intern OA — the probability section',
    'a probability item listed after the karma wall',
    'probability_dice',
    '掷 4 个骰子，乘积是奇数的概率',
    'Throw 4 dice; the probability that the product is odd.',
    '掷 4 个骰子，乘积是奇数的概率',
    CTX_1141209,
    ('Short but genuinely self-contained — four dice, probability the product is odd — which is '
     'unusual for this genre. Still a paraphrase in the poster\'s words rather than the assessment\'s, '
     'and no answer is given. ' + D_1141209),
    post_date='2025-08-13', lang='zh')

add('wb', '1141209', 'Optiver', 'quant_researcher', 'internship', '2026', 'online_assessment',
    'Optiver 2026 Quantitative Research Intern OA — the games section',
    'the fourth section',
    'assessment_format',
    '小游戏 \n\n比较放松了，比大小，看区别，轻松做了',
    ('Mini-games: fairly relaxed — comparing magnitudes, spotting differences; got through them '
     'easily.'),
    '小游戏 \n\n比较放松了，比大小，看区别，轻松做了',
    CTX_1141209,
    ('A format note, not a question. "比大小" (compare which is bigger) and "看区别" (spot the '
     'difference) are the poster\'s own shorthand for two reaction-speed games; they do not name them '
     'and do not give timings. Consistent with the "连连看"/spot-the-match game another Optiver '
     'candidate describes in this corpus, but that is my inference, not their claim.'),
    post_date='2025-08-13', lang='zh')

# ======================================================== thread 1141422 — snippet only
CTX_1141422 = ('Posted to 1point3acres 海外面经 as "26 summer optiver OA" under the structured tags '
               '"2025(7-9月) 金工类 硕士 实习@optiver - 网上海投 - 在线笔试 | 😃 Positive 😐 Average | '
               'Other | 应届毕业生" — a master\'s student applying for a summer quant internship, '
               'online written test. They sign off 都是真题，觉得有帮助麻烦点赞支持下~求米求米求米 '
               '("these are all real questions; if you found it useful please upvote"). Readable '
               'only as a search engine\'s cached extract: ' + BLOCK + ', and neither '
               'archive.org/wayback/available nor a CDX query for thread-1141422* returns any '
               'snapshot')
D_1141422 = ('SNIPPET ONLY — I could not open this page. Everything here comes from a search '
             'engine\'s cached extract of it, preserved verbatim in '
             'raw/pages/websearch_highlights_1p3a.txt, so I cannot see what surrounds these lines, '
             'cannot tell whether the extract skipped text mid-list (the extract is visibly '
             'elided with "..." between blocks), and cannot rule out that part of the page was '
             'behind the forum\'s karma wall. The poster\'s own claim 都是真题 ("these are all real '
             'questions") is exactly the sort of assertion that cannot be checked. That said, the '
             'four probability items below are reproduced in full English sentences with the '
             'assessment\'s own phrasing and punctuation quirks, which is much more consistent with '
             'copying than with reconstruction.')

add('snip', '1141422', 'Optiver', 'quant_trader', 'internship', '2026', 'online_assessment',
    'Optiver summer quant internship OA — four modules',
    'the structure of the assessment and the poster\'s description of module 1',
    'assessment_format',
    ('一共4 个modulus ​一、找规律 单选题，大部分都很straightforward，不会立马skip留到最后做，时间充足'
     '最后能有个五分钟检查'),
    ('Four modules in total. 1. Find the pattern — multiple choice, mostly very straightforward; if '
     'you cannot do one, skip it immediately and leave it to the end. There is plenty of time — I had '
     'about five minutes at the end to check.'),
    ('一共4 个modulus ​一、找规律 单选题，大部分都很straightforward，不会立马skip留到最后做，时间充足'
     '最后能有个五分钟检查'),
    CTX_1141422, D_1141422, post_date='2025-08-04', lang='mixed')

for i, seq in enumerate(['12,28,36,84,88,168,？', '4/3,1,5,8,23,47,?', '3,1,2,6,12,144,?',
                         '1/5,2/3,3/11,3/6,5/17,4/9,?', '7,14,24,6,12,22,?',
                         '19,18,20,60,15,14,16,?', '4,2,6,6,30,150,?', '1,3,7,17,41,99,?']):
    add('snip', '1141422', 'Optiver', 'quant_trader', 'internship', '2026', 'online_assessment',
        'Optiver summer quant internship OA, module 1 — 找规律 (find the pattern), multiple choice',
        f'sequence {i + 1} of the eight the poster lists',
        'number_sequence', seq, f'Complete the sequence: {seq.replace("？", "?")}', seq,
        CTX_1141422,
        ('No answers are given for any of the eight, and no options either, even though the poster '
         'says the module was multiple choice — so what a candidate actually saw on screen was a '
         'sequence plus four choices, and only the stem survives. ' + D_1141422),
        post_date='2025-08-04', lang='en')

add('snip', '1141422', 'Optiver', 'quant_trader', 'internship', '2026', 'online_assessment',
    'Optiver summer quant internship OA, module 2 — 搬房子 (moving houses)',
    'module 2 of four',
    'puzzle_rearrangement_minimum_moves',
    '二、搬房子 用最少的次数从下面变成上面的样子，似乎没有时间限制，想好再动手！！建议先把一楼的房子搞对，再234楼',
    ('2. Moving houses: turn the bottom configuration into the top one in the fewest moves. There '
     'seems to be no time limit — think before you act!! I suggest getting the first floor right '
     'first, then floors 2, 3 and 4.'),
    '二、搬房子 用最少的次数从下面变成上面的样子，似乎没有时间限制，想好再动手！！建议先把一楼的房子搞对，再234楼',
    CTX_1141422,
    ('The puzzle is graphical — "turn the bottom into the top" refers to a picture that is not in the '
     'text and is certainly not in a search snippet — so the actual instance is unrecoverable. What '
     'survives is the mechanic (minimum-move rearrangement over four floors, untimed) and the '
     'poster\'s heuristic. ' + D_1141422),
    post_date='2025-08-04', lang='zh')

add('snip', '1141422', 'Optiver', 'quant_trader', 'internship', '2026', 'online_assessment',
    'Optiver summer quant internship OA, module 3 — 连连看 (matching game)',
    'module 3 of four',
    'perceptual_speed_matching',
    ('三、连连看 从四个选项中找到和example一样的那个，7-8位数字+字母有点类似车牌号，考反应速度，越往后越快'),
    ('3. Matching game: from four options, find the one identical to the example. 7-8 characters of '
     'digits plus letters, a bit like a licence plate. It tests reaction speed, and gets faster as '
     'you go.'),
    ('三、连连看 从四个选项中找到和example一样的那个，7-8位数字+字母有点类似车牌号，考反应速度，越往后越快'),
    CTX_1141422,
    ('A description of the mechanic with no instance — no example string and no options are given, so '
     'nothing here is answerable. The detail that the strings are 7-8 alphanumeric characters and '
     'that the pace accelerates is specific enough to be checkable by anyone who sits it. '
     + D_1141422),
    post_date='2025-08-04', lang='zh')

Q_EN = [
    ('probability_coin',
     'You flip a coin 3 times. What is the probability that the outcome is the same for all flips? '
     'all Heads or all Tails.'),
    ('probability_dice',
     'You throw one dice two times. What is the probability that the 2nd throw has a different face '
     'value than the first throw?'),
    ('probability_martingale_bankroll',
     'ss. Once you have won a toss, your strategy has been implemented, and you stop. If you have a '
     'total bankroll of $63 available to implement this strategy, what is your expected profit?'),
    ('probability_gamblers_ruin',
     'You will play a coin game against an opponent. A biased coin will be continually flipped where '
     'there is a 2/3 chance of Heads and a 1/3 chance of Tails. If Heads is flipped then you receive '
     '$1 from your opponent. If Tails is flipped then you pay $1 to your opponent. You start with '
     '$10 and your opponent starts with $20. You keep playing until one of you is bankrupt (= has $0 '
     'left); they will be declared the loser, the other will be declared the winner. What is the '
     'probability that you win?'),
]
for qt, qtext in Q_EN:
    extra = ''
    if qt == 'probability_martingale_bankroll':
        extra = (' This one in particular is visibly decapitated: it begins mid-word at "ss." — the '
                 'tail of some earlier word — so the entire setup, including what the strategy is and '
                 'what you stake, is missing. Only the bankroll figure ($63, which is 2^6 - 1 and '
                 'therefore suggests a doubling scheme) and the question survive. It must not be '
                 'treated as a complete prompt.')
    add('snip', '1141422', 'Optiver', 'quant_trader', 'internship', '2026', 'online_assessment',
        'Optiver summer quant internship OA, module 4 — 概率 (probability), multiple choice, which '
        'the poster calls 中规中矩的绿皮书统计题 (bog-standard Green Book statistics questions)',
        'one of the probability items the poster reproduces in English',
        qt, qtext, qtext, qtext, CTX_1141422,
        ('No answer and no answer options are given, although the poster says the module was multiple '
         'choice. The poster also characterises the whole module as 中规中矩的绿皮书统计题 — '
         '"bog-standard Green Book statistics questions" — which is a real problem for this record: '
         'these are textbook-shaped, and a poster who had just been revising from the Green Book '
         'could produce something very like them from memory of the book rather than the test. What '
         'argues against that is that they are written out in full English sentences with the '
         'assessment\'s own awkwardness intact ("You throw one dice two times", the redundant gloss '
         '"(= has $0 left)"), which reads like transcription.' + extra + ' ' + D_1141422),
        post_date='2025-08-04', lang='en')

# ======================================================== thread 1019756 — snippet only
CTX_1019756 = ('Posted to 1point3acres 海外面经 as "Optiver 2024 Summer Quant Trader Intern OA'
               '【新人求米】" — a first-time poster asking for karma. They say the whole thing took '
               'nearly 3 hours, of which the games alone took over an hour. Readable only as a '
               'search engine\'s cached extract: ' + BLOCK + ', and neither '
               'archive.org/wayback/available nor a CDX query for thread-1019756* returns any '
               'snapshot')

add('snip', '1019756', 'Optiver', 'quant_trader', 'internship', '2024', 'online_assessment',
    'Optiver 2024 Summer Quant Trader Intern OA — nearly 3 hours in total',
    'section 1 of the battery',
    'assessment_format_mental_math',
    '1. 8-80。 8分钟80道算术题。选择题。有分数和小数。感觉有点难。本人zeta mac得分30+。',
    ('1. 8-80: 80 arithmetic questions in 8 minutes. Multiple choice. There are fractions and '
     'decimals. Felt a bit hard. My own Zetamac score is 30-something.'),
    '1. 8-80。 8分钟80道算术题。选择题。有分数和小数。感觉有点难。本人zeta mac得分30+。',
    CTX_1019756,
    ('Not a question — the parameters of the arithmetic sprint (80 items, 8 minutes, multiple choice, '
     'fractions and decimals included) plus the poster\'s Zetamac benchmark. This is the section '
     'another candidate elsewhere in this corpus calls "80 in 8" and was disappointed not to get, '
     'which is decent mutual corroboration that the name and format are real. SNIPPET ONLY — see the '
     'stored extract in raw/pages/websearch_highlights_1p3a.txt; I could not open the page and '
     'sections 2 through 4 are behind the forum\'s 188-karma wall in the extract.'),
    post_date='2023-10-12', lang='mixed')

add('snip', '1019756', 'Optiver', 'quant_trader', 'internship', '2024', 'online_assessment',
    'Optiver 2024 Summer Quant Trader Intern OA',
    'a probability item, whose opening is swallowed by the karma-wall placeholder',
    'probability_expectation_family',
    '道女孩数量大于男孩，问生孩子个数的期望。',
    ('…where the number of girls exceeds the number of boys; asked for the expected number of '
     'children.'),
    '道女孩数量大于男孩，问生孩子个数的期望。',
    CTX_1019756,
    ('Decapitated. The karma-wall placeholder runs straight into this line, so the sentence begins '
     'mid-word at "道" (the tail of a question counter) and the entire stopping rule — the thing that '
     'defines the problem — is missing. All that is recoverable is that some family-planning '
     'expectation question involving girls outnumbering boys was asked. It must not be treated as a '
     'complete prompt. SNIPPET ONLY.'),
    post_date='2023-10-12', lang='zh')

add('snip', '1019756', 'Optiver', 'quant_trader', 'internship', '2024', 'online_assessment',
    'Optiver 2024 Summer Quant Trader Intern OA — a replier reports a different three-section battery',
    'the assessment platform\'s own descriptions of its three tests, quoted by a replier',
    'assessment_format',
    ('1. ERQ This test will assess your knowledge of equity research and wider financial markets. The '
     'test takes approximately 20 minutes. 2. ZAP N This assessment consists of 9 short '
     'neuro-assessment games. Each game lasts between 2 and 15 minutes. The assessment takes about 60 '
     'minutes to complete overall. 3. ZAP Q Personality questionnaire to measure your personal '
     'talents. The duration is 20 minutes.'),
    None,
    ('1. ERQ This test will assess your knowledge of equity research and wider financial markets. The '
     'test takes approximately 20 minutes. 2. ZAP N This assessment consists of 9 short '
     'neuro-assessment games. Each game lasts between 2 and 15 minutes. The assessment takes about 60 '
     'minutes to complete overall. 3. ZAP Q Personality questionnaire to measure your personal '
     'talents. The duration is 20 minutes.'),
    ('A replier (u/AlexanderIDTB, posting 2023-10-12 20:41) on the same 1point3acres thread, who says '
     '我们的题目好像不太一样。我的只有三个部分 (our tests seem to be different — mine had only three '
     'parts) and pastes what they were sent. ' + BLOCK),
    ('Not a question — Optiver\'s own instruction text for three modules, pasted by a replier. It is '
     'valuable for two reasons: it names ZAP N and ZAP Q, and a reddit commenter elsewhere in this '
     'corpus independently reports being sent "Zap-N" alongside Number Logic and Beat the Odds, which '
     'is cross-platform corroboration of an otherwise obscure product name. It also documents that '
     'ZAP Q explicitly does not count towards the result. SNIPPET ONLY — I could not open the page, '
     'and the extract may have elided text inside this block.'),
    post_date='2023-10-12', lang='en')

# ------------------------------------------------------------------ emit with verification
fails, out = [], []
for rec in R:
    src, tid = rec.pop('_src'), rec.pop('_tid')
    hay = wb(tid) if src == 'wb' else SNIP
    if rec['source_quote'] not in hay:
        fails.append((tid, rec['question_type'], rec['source_quote'][:60]))
        continue
    out.append(rec)

with open('raw/chat_and_archive.jsonl', 'a', encoding='utf-8') as fh:
    for rec in out:
        fh.write(json.dumps(rec, ensure_ascii=False) + '\n')

print(f'appended {len(out)} records; {len(fails)} quote failures')
for f in fails:
    print('  FAIL', f, file=sys.stderr)
