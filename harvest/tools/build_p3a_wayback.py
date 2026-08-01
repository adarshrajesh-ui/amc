#!/usr/bin/env python3
"""Build JSONL records from 1point3acres threads recovered via the Wayback Machine.

Every source_quote is checked against the stored snapshot's decoded text before the
record is emitted; unverifiable records are dropped and reported on stderr.
"""
import html
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from p3a_extract2 import load  # noqa: E402

PAGES = 'raw/pages/wayback'
SNAP = {
    '1144112': ('20250912084409', '1p3a_1144112__20250912084409.html'),
    '1141209': ('20250910211053', '1p3a_1141209__20250910211053.html'),
    '1131152': ('20250630171445', '1p3a_1131152__20250630171445.html'),
    '1128313': ('20250614052758', '1p3a_1128313__20250614052758.html'),
    '1129259': ('20250911122118', '1p3a_1129259__20250911122118.html'),
    '1120333': ('20260701223244', '1p3a_1120333__20260701223244.html'),
    '1041382': ('20240714082418', '1p3a_1041382__20240714082418.html'),
    '1068784': ('20240804172016', '1p3a_1068784__20240804172016.html'),
    '1090786': ('20241205105027', '1p3a_1090786__20241205105027.html'),
    '1136901': ('20250809114158', '1p3a_1136901__20250809114158.html'),
}

_cache = {}


def page_text(tid: str) -> str:
    if tid not in _cache:
        s = load(os.path.join(PAGES, SNAP[tid][1]))
        s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S)
        s = re.sub(r'<br\s*/?>', '\n', s)
        s = re.sub(r'<[^>]+>', '\n', s)
        s = html.unescape(s)
        s = re.sub(r'[ \t\u00a0]+', ' ', s)
        _cache[tid] = re.sub(r'\n+', '\n', s)
    return _cache[tid]


WALL = ('本帖隐藏的内容需要积分高于 188 才可浏览 (a karma wall); only the portion of the post '
        'above/below the wall was recoverable')

R = []


def add(tid, **kw):
    kw['_tid'] = tid
    ts = SNAP[tid][0]
    kw.setdefault('source_url',
                  f'https://web.archive.org/web/{ts}/https://www.1point3acres.com/bbs/thread-{tid}-1-1.html')
    kw.setdefault('source_type', 'other')
    kw.setdefault('access', 'archive_only')
    kw.setdefault('retrieval_method', 'wayback')
    kw.setdefault('upstream_source', None)
    kw.setdefault('office', 'unknown')
    kw.setdefault('platform', 'unknown')
    kw.setdefault('reported_answer', None)
    R.append(kw)


P3A = ('1point3acres 海外面经版 recall thread, recovered from a Wayback Machine snapshot because '
       '1point3acres itself Cloudflare-blocks this machine')

# ============================ SIG — thread 1144112 ============================
# "2026 SIG Quant Research OA整理 【带答案】", OP 2025-09-04, snapshot 2025-09-12.
# The only source in this shard that reproduces the assessment's own English wording.
SIG_CTX = dict(
    firm='SIG', role_track='quant_researcher', level='new_grad', cycle='2026',
    round='online_assessment',
    round_name='SIG Quant Research OA — poster states it is 17 questions in 60 minutes',
    source_language='mixed', post_date='2025-09-04',
    poster_context=(P3A + '; forum metadata line reads "2025(7-9月) 金工类 硕士 全职 @ sig - 网上海投 '
                    '- 技术电面 … Pass | 应届毕业生" — a master\'s new-grad who passed'),
)
SIG_DOUBT = (
    'The poster is transcribing from memory after the fact and says "已经做了好几次了" (I have taken '
    'this OA several times), so the wording may be a composite across sittings rather than one '
    'paper; the answers are explicitly the poster\'s own ("自己写的答案和解释") and are not '
    'authoritative. The poster is also soliciting forum karma ("求加米"), which is an incentive to '
    'post a polished compilation. Against that: the English reads like assessment copy rather than '
    'a candidate paraphrase, and questions 1, 2 and 4 independently match fragments posted by other '
    'candidates to Telegram in 2024-2025 (t.me/usinterview/23247, /19241). ')

add('1144112', **SIG_CTX,
    section_context='OA question 1 of 17 (poster says questions 1-9 are the easier half)',
    question_type='brainteaser_algebra',
    question_text=('You walk into a barn and see a collection of spiders, chickens, and cows. You '
                   'notice that there are 520 legs in total. The number of chickens is twice the '
                   'number of cows and the number of spiders is twice the number of chickens. '
                   'Compute the number of spiders.'),
    question_text_en=('You walk into a barn and see a collection of spiders, chickens, and cows. You '
                      'notice that there are 520 legs in total. The number of chickens is twice the '
                      'number of cows and the number of spiders is twice the number of chickens. '
                      'Compute the number of spiders.'),
    reported_answer='52',
    source_quote=('Question 1:\nYou walk into a barn and see a collection of spiders, chickens, and '
                  'cows. You notice that there are 520 legs in total. The number of chickens is '
                  'twice the number of cows and the number of spiders is twice the number of '
                  'chickens. Compute the number of spiders.\n答案：52， 变形的“鸡兔同笼”问题'),
    doubt=SIG_DOUBT + ('Note the reported answer 52 is arithmetically wrong for the stated numbers '
                       '(cows c, chickens 2c, spiders 4c gives 4c+4c+32c=40c=520, c=13, spiders=52 '
                       '— actually consistent), so this one checks out; flagged only because other '
                       'answers in the same post are the poster\'s own working.'))

add('1144112', **SIG_CTX,
    section_context='OA question 2 of 17',
    question_type='logic_seating_puzzle',
    question_text=('I need to seat 5 toddlers (Anna, Brian, Charlie, Dixie, Eva) at a round table '
                   'with these rules:\ni) Anna won’t sit next to Brian or Eva.\nii) Brian won’t sit '
                   'next to Charlie.\niii) Dixie won’t sit next to Eva or Charlie.\nIf Dixie is '
                   'sitting to the left of Anna, who is sitting to the left of Brian?'),
    question_text_en=('I need to seat 5 toddlers (Anna, Brian, Charlie, Dixie, Eva) at a round table '
                      'with these rules: i) Anna won\'t sit next to Brian or Eva. ii) Brian won\'t '
                      'sit next to Charlie. iii) Dixie won\'t sit next to Eva or Charlie. If Dixie '
                      'is sitting to the left of Anna, who is sitting to the left of Brian?'),
    reported_answer='Eva, B–D–A–C–E',
    source_quote=('Question 2:\nI need to seat 5 toddlers (Anna, Brian, Charlie, Dixie, Eva) at a '
                  'round table with these rules:\ni) Anna won’t sit next to Brian or Eva.\nii) Brian '
                  'won’t sit next to Charlie.\niii) Dixie won’t sit next to Eva or Charlie.\nIf '
                  'Dixie is sitting to the left of Anna, who is sitting to the left of Brian?\n'
                  '答案: Eva, B–D–A–C–E'),
    doubt=SIG_DOUBT + ('The stated answer arrangement B–D–A–C–E puts D next to A and B, but rule (i) '
                       'forbids Anna next to Brian only, so the cycle needs checking; a Telegram '
                       'repost of a different candidate\'s 2025-05 recall gives the same puzzle with '
                       'different letter constraints, so the constraint list may drift between '
                       'sittings.'))

add('1144112', **SIG_CTX,
    section_context='OA question 3 of 17',
    question_type='conditional_probability_table',
    question_text=('1000 people were surveyed about their preferred method of exercise. The table '
                   'shows results by age group.\nIf you meet a 33-year-old who took the survey, '
                   'compute the probability she prefers swimming.\n[table, columns 18-22 / 23-27 / '
                   '28-32 / 33-37 / Total] Run 54 40 42 66 202; Bike 77 68 90 70 305; Swim 28 43 50 '
                   '52 173; Other 90 78 71 81 320; Total 249 229 253 269 1000'),
    question_text_en=('1000 people were surveyed about their preferred method of exercise. The table '
                      'shows results by age group. If you meet a 33-year-old who took the survey, '
                      'compute the probability she prefers swimming. (Run 54/40/42/66; Bike '
                      '77/68/90/70; Swim 28/43/50/52; Other 90/78/71/81; column totals '
                      '249/229/253/269 = 1000.)'),
    reported_answer='52/269',
    source_quote=('Question 3:\n1000 people were surveyed about their preferred method of exercise. '
                  'The table shows results by age group.\nIf you meet a 33-year-old who took the '
                  'survey, compute the probability she prefers swimming.'),
    doubt=SIG_DOUBT + ('The table itself renders in the snapshot as a bare sequence of numbers with '
                       'the header row separated from the data, so my reconstruction of which number '
                       'belongs in which cell is an interpretation of the flattened HTML, not '
                       'something the page states explicitly. The verified quote is the prose stem '
                       'only.'))

add('1144112', **SIG_CTX,
    section_context='OA question 4 of 17 (headed "Questions 4" in the original)',
    question_type='visual_weight_puzzle',
    question_text=('Compute the weight of the green triangle in pounds if the following system is '
                   'balanced and weighs 96 pounds in total.'),
    question_text_en=('Compute the weight of the green triangle in pounds if the following system is '
                      'balanced and weighs 96 pounds in total.'),
    reported_answer='6',
    source_quote=('Questions 4\nCompute the weight of the green triangle in pounds if the following '
                  'system is balanced and weighs 96 pounds in total.\n答案：6。确定红圈三角的重量就行，'
                  '系统平衡，所以三角形 = 96/2/2/2/2'),
    doubt=SIG_DOUBT + ('The question depends on a balance diagram that is an image attachment; the '
                       'image is not in the snapshot, so the problem cannot be solved from this text '
                       'alone. A candidate on Telegram (t.me/usinterview/19241, 2024-08) '
                       'independently reported "求绿色三角形的重量（6lb)" — same question, same '
                       'answer, over a year earlier.'))

add('1144112', **SIG_CTX,
    section_context='OA question 5 of 17',
    question_type='bayes_probability',
    question_text=('Factory A makes 40% red widgets and 60% black widgets. Factory B makes 80% red '
                   'widgets and 20% black widgets. Two widgets are sampled uniformly at random from '
                   'one of the companies, also selected uniformly at random. The widgets are both '
                   'red. Compute the probability they were from Factory A.'),
    question_text_en=('Factory A makes 40% red widgets and 60% black widgets. Factory B makes 80% '
                      'red widgets and 20% black widgets. Two widgets are sampled uniformly at '
                      'random from one of the companies, also selected uniformly at random. The '
                      'widgets are both red. Compute the probability they were from Factory A.'),
    reported_answer='1/5',
    source_quote=('Question 5:\nFactory A makes 40% red widgets and 60% black widgets. Factory B '
                  'makes 80% red widgets and 20% black widgets. Two widgets are sampled uniformly at '
                  'random from one of the companies, also selected uniformly at random. The widgets '
                  'are both red. Compute the probability they were from Factory A.\n答案：1/5， '
                  '最典型的贝叶斯问题，和袋子里抽球一样。'),
    doubt=SIG_DOUBT + ('0.4²/(0.4²+0.8²) = 1/5 matches the stated answer, which is a consistency '
                       'check in the source\'s favour.'))

add('1144112', **SIG_CTX,
    section_context='OA question 6 of 17 — the last question above the forum karma wall',
    question_type='expected_value_dice',
    question_text=('You roll three fair 6-sided dice. If they all show the same number, you earn '
                   '$20. If exactly two of the numbers are the same, you earn $10. If all of the '
                   'numbers are different, you lose $2. Compute your expected return per roll in '
                   'dollars. (Round to the nearest cent.)'),
    question_text_en=('You roll three fair 6-sided dice. If they all show the same number, you earn '
                      '$20. If exactly two of the numbers are the same, you earn $10. If all of the '
                      'numbers are different, you lose $2. Compute your expected return per roll in '
                      'dollars. (Round to the nearest cent.)'),
    reported_answer=None,
    source_quote=('Question 6:\nYou roll three fair 6-sided dice. If they all show the same number, '
                  'you earn $20. If exactly two of the numbers are the same, you earn $10. If all of '
                  'the numbers are different, you lose $2. Compute your expected return per roll in '
                  'dollars. (Round to the nearest cent.)'),
    doubt=SIG_DOUBT + f'The poster\'s answer for this item sits immediately behind {WALL}, so only '
                      'the question survives.')

add('1144112', **SIG_CTX,
    section_context='OA question 16 of 17 (poster says questions 10-17 are the harder half)',
    question_type='gamblers_ruin',
    question_text=('Suppose you have 3 tokens for a betting game and your goal is to reach 5 tokens '
                   'before running out. Each turn you bet as many tokens as possible but not more '
                   'than needed to reach 5. You win each bet with probability 2/3​. Compute the '
                   'probability you reach 5 tokens before running out. (Give your answer as a '
                   'reduced fraction.)'),
    question_text_en=('Suppose you have 3 tokens for a betting game and your goal is to reach 5 '
                      'tokens before running out. Each turn you bet as many tokens as possible but '
                      'not more than needed to reach 5. You win each bet with probability 2/3. '
                      'Compute the probability you reach 5 tokens before running out. (Give your '
                      'answer as a reduced fraction.)'),
    reported_answer='62/77',
    source_quote=('Question 16:\nSuppose you have 3 tokens for a betting game and your goal is to '
                  'reach 5 tokens before running out. Each turn you bet as many tokens as possible '
                  'but not more than needed to reach 5. You win each bet with probability 2/3​. '
                  'Compute the probability you reach 5 tokens before running out. (Give your answer '
                  'as a reduced fraction.)'),
    doubt=SIG_DOUBT + ('This item and question 17 sit below the karma wall and were readable only '
                       'because the wall is inserted mid-post; the questions between 7 and 15 are '
                       'not recoverable. The poster\'s own state equations as rendered in the '
                       'snapshot are mangled by MathJax fallback text.'))

add('1144112', **SIG_CTX,
    section_context='OA question 17 of 17 — the final question',
    question_type='combinatorics_lattice_paths',
    question_text=('A frog is traveling from point A(0,0) to point B(5,6) but each step can only be '
                   '1 unit up or 1 unit to the right. Additionally, the frog refuses to move three '
                   'steps in the same direction consecutively. Compute the number of ways the frog '
                   'can move from A to B.'),
    question_text_en=('A frog is traveling from point A(0,0) to point B(5,6) but each step can only '
                      'be 1 unit up or 1 unit to the right. Additionally, the frog refuses to move '
                      'three steps in the same direction consecutively. Compute the number of ways '
                      'the frog can move from A to B.'),
    reported_answer=None,
    source_quote=('Question 17:\nA frog is traveling from point A(0,0) to point B(5,6) but each step '
                  'can only be 1 unit up or 1 unit to the right. Additionally, the frog refuses to '
                  'move three steps in the same direction consecutively. Compute the number of ways '
                  'the frog can move from A to B.'),
    doubt=SIG_DOUBT + ('The poster gives no numeric answer, saying only "这个问题我每次都是手算出来的" '
                       '(I always work it out by hand each time) — which is itself evidence they '
                       'have sat this OA repeatedly, and therefore that the specific coordinates '
                       '(5,6) may not be constant across sittings.'))

# ======================= Optiver — thread 1141209 =======================
OPT_CTX = dict(
    firm='Optiver', role_track='quant_researcher', level='internship', cycle='2026',
    round='online_assessment', platform='HackerRank',
    round_name='Optiver 2026 Quantitative Research Intern OA — four sections',
    source_language='zh', post_date='2025-08-13',
    poster_context=(P3A + '; forum metadata line reads "2025(7-9月) 码农类General 博士 实习 @ optiver '
                    '- 网上海投 - 在线笔试 … Fail | 应届毕业生" — a PhD intern applicant who was '
                    'rejected the next day'),
)
OPT_DOUBT = ('The forum role tag on this post is 码农类General (generic software engineer) while the '
             'thread title says "Quantitative Research Intern", so the role_track here follows the '
             'title, not the tag. ')

add('1141209', **OPT_CTX,
    section_context='OA coding section, 90 minutes on HackerRank, question 1 of at least 2',
    question_type='combinatorics',
    question_text='第一题：题目有点记不清楚了，但是不难，核心考点是考m个a和n个b的排列组合有多少个',
    question_text_en=('Question 1: I cannot quite remember the problem, but it was not hard; the '
                      'core point being tested is how many arrangements there are of m copies of a '
                      'and n copies of b.'),
    source_quote=('第一题：题目有点记不清楚了，但是不难，核心考点是考m个a和n个b的排列组合有多少个'),
    doubt=OPT_DOUBT + ('The poster states outright that they cannot remember the problem '
                       '("题目有点记不清楚了") and gives only what they believe the underlying concept '
                       'was, so this is a topic label, not a question.'))

add('1141209', **OPT_CTX,
    section_context='OA coding section, 90 minutes on HackerRank, question 2',
    question_type='order_book_simulation',
    question_text=('第二题：股票交易，给你一个orders, 是一个2d array, 里面有 [1, 15]; [-1; 30]....1 '
                   '代表买，-1 代表买，后面是价格；'),
    question_text_en=('Question 2: stock trading. You are given orders as a 2D array containing '
                      '[1, 15]; [-1, 30]... where 1 means buy and -1 means buy [sic — the poster '
                      'evidently meant sell], and the following number is the price;'),
    source_quote=('第二题：股票交易，给你一个orders, 是一个2d array, 里面有 [1, 15]; [-1; 30]....1 '
                  '代表买，-1 代表买，后面是价格；'),
    doubt=OPT_DOUBT + (f'The statement is cut off by {WALL} exactly where the task would be stated — '
                       'we learn the input format but never what has to be computed. The poster also '
                       'writes "1 代表买，-1 代表买" (1 means buy, -1 means buy), an obvious slip.'))

add('1141209', **OPT_CTX,
    section_context='OA probability/maths section (below the karma wall)',
    question_type='expected_value_dice',
    question_text='骰子掷出每个面的平均次数',
    question_text_en='The average number of rolls to see every face of a die.',
    source_quote='骰子掷出每个面的平均次数',
    doubt=OPT_DOUBT + ('Nine characters with no setup: number of dice, number of faces and what '
                       '"平均次数" is averaged over are all absent. This is a heading in the poster\'s '
                       'own list, not a question statement. (It reads like the coupon-collector '
                       'problem, but the source does not say that and I am not asserting it.)'))

add('1141209', **OPT_CTX,
    section_context='OA probability/maths section (below the karma wall)',
    question_type='probability_dice',
    question_text='掷 4 个骰子，乘积是奇数的概率',
    question_text_en='Roll 4 dice; the probability that the product is odd.',
    source_quote='掷 4 个骰子，乘积是奇数的概率',
    doubt=OPT_DOUBT + ('A one-line label from the poster\'s bullet list rather than the assessment '
                       'wording; no answer is given and whether the dice are fair six-sided is not '
                       'stated.'))

add('1141209', **OPT_CTX,
    section_context='OA game section — the poster describes it only as relaxed',
    question_type='assessment_format',
    question_text='小游戏\n比较放松了，比大小，看区别，轻松做了',
    question_text_en=('Mini-games: fairly relaxed — compare which is bigger, spot the difference; I '
                      'did them easily.'),
    source_quote='小游戏\n比较放松了，比大小，看区别，轻松做了',
    doubt=('This is a format datapoint, not a question: it records that Optiver\'s 2026 QR intern OA '
           'contained a cognitive-game section of magnitude-comparison and spot-the-difference '
           'tasks, but no individual item is described. ' + OPT_DOUBT))

# ======================= Jane Street — thread 1131152 =======================
JS1_CTX = dict(
    firm='Jane Street', role_track='quant_developer', level='experienced', cycle='2025',
    round='phone_technical', round_name='Jane Street 电面 — first round, 1 hour',
    source_language='mixed', post_date='2025-06-01',
    poster_context=(P3A + '; forum metadata line reads "2025(1-3月) 码农类General 本科 全职 @ '
                    'janestreet - 内推 - 技术电面 … 在职跳槽" — a bachelor\'s-degree experienced hire '
                    'who came in through a referral'),
)
JSD = ('Role is tagged 码农类General (generic software engineer) at a trading firm and mapped to '
       'quant_developer as the nearest controlled value, so the label may overstate how "quant" the '
       'role is. ')

add('1131152', **JS1_CTX,
    section_context='phone coding/design round; poster says the emphasis is API design and clean code',
    question_type='ood_design',
    question_text=('Design a supermarket queue. … [karma wall] … r customers? How to implement? (Use '
                   'a red-black tree)'),
    question_text_en=('Design a supermarket queue. ... How to implement? (Use a red-black tree)'),
    source_quote=('我是一面，1小时时间。难度还好，感觉Jane Street面试更多是考API design和clean code，'
                  '算法难度中等'),
    doubt=JSD + (f'The problem statement is split by {WALL}: the snapshot shows "Design a supermarket '
                 'qu" before the wall and "r customers? How to implement? (Use a red-black tree)" '
                 'after it, so the operation list in between is lost. The verified quote here is the '
                 'poster\'s framing sentence, because the question fragment itself is interrupted by '
                 'the wall markup and is not one contiguous string in the page. A separate reply on '
                 'the same thread quotes the hidden text as "customers can go between other '
                 'customers", recorded as its own record.'))

add('1131152', **JS1_CTX,
    section_context='follow-up to the supermarket-queue design, quoted by a replier from behind the wall',
    question_type='ood_design_followup',
    question_text=('“customers can go between other customers”是不是说新进来的顾客可以插到队伍中间？'
                   '为啥一定要用红黑树，其他数据结构不行吗？'),
    question_text_en=('Does "customers can go between other customers" mean a newly arriving customer '
                      'can cut into the middle of the queue? And why must a red-black tree be used — '
                      'would no other data structure do?'),
    source_quote=('follow‑up具体指什么？“customers can go between other customers”是不是说新进来的'
                  '顾客可以插到队伍中间？为啥一定要用红黑树，其他数据结构不行吗？求科普～'),
    doubt=JSD + ('This is a *replier* quoting the karma-walled portion of the original post, so the '
                 'English phrase "customers can go between other customers" is second-hand: it is '
                 'real text from the recall, but it reached me through someone else\'s copy-paste, '
                 'and the question mark and framing are the replier\'s, not the interviewer\'s.'))

# ======================= Jane Street — thread 1128313 =======================
JS2_CTX = dict(
    firm='Jane Street', role_track='quant_developer', level='experienced', cycle='2025',
    round='onsite', round_name='Jane Street SWE On-site — two one-hour rounds, two SWE interviewers each',
    source_language='mixed', post_date='2025-05-12',
    poster_context=(P3A + '; forum metadata line reads "2025(1-3月) 码农类General 本科 全职 @ '
                    'janestreet - 内推 - Onsite … Fail | 在职跳槽" — an experienced-hire referral who '
                    'was told on the day that he had not passed'),
)

add('1128313', **JS2_CTX,
    section_context='onsite round 1, open-ended API/abstraction design',
    question_type='data_structure_design',
    question_text=('First interview: Design a ring buffer / rotational filesystem\nGiven a buffer in '
                   'the form of a ring, we want to design a class that let us read and write into '
                   'that buffer. Say we have a head that'),
    question_text_en=('First interview: Design a ring buffer / rotational filesystem. Given a buffer '
                      'in the form of a ring, we want to design a class that lets us read and write '
                      'into that buffer. Say we have a head that ... (cut off by the forum karma '
                      'wall)'),
    source_quote=('First interview: Design a ring buffer / rotational filesystem\nGiven a buffer in '
                  'the form of a ring, we want to design a class that let us read and write into '
                  'that buffer. Say we have a head that'),
    doubt=JSD + (f'Cut off mid-sentence at "Say we have a head that" by {WALL}, so the read/write '
                 'semantics and the overwrite policy — the entire substance of a ring-buffer '
                 'question — are missing.'))

add('1128313', **JS2_CTX,
    section_context='onsite round 2 follow-ups (the poster lists these as "and follow ups")',
    question_type='system_design',
    question_text=('- How would you design the abstractions for exchanges and instruments?\n- How do '
                   'you ensure performance when there are 10^6 quote updates across instruments and '
                   'exchanges every second?'),
    question_text_en=('How would you design the abstractions for exchanges and instruments? How do '
                      'you ensure performance when there are 10^6 quote updates across instruments '
                      'and exchanges every second?'),
    source_quote=('- How would you design the abstractions for exchanges and instruments?\n- How do '
                  'you ensure performance when there are 10^6 quote updates across instruments and '
                  'exchanges every second?'),
    doubt=JSD + ('These are the two follow-ups the poster chose to write down after the wall; the '
                 'base question for the second round is behind the wall, so what system these '
                 'abstractions were being added to is unknown. Two bullets covering a full hour of '
                 'interview is a heavy compression.'))

# ======================= HRT — thread 1129259 =======================
HRT1_CTX = dict(
    firm='HRT', role_track='quant_developer', level='experienced', cycle='2025',
    round='phone_technical', round_name='HRT C++ dev 面经 — phone technical via a headhunter',
    source_language='mixed', post_date='2025-05-17',
    poster_context=(P3A + '; forum metadata line reads "2025(1-3月) 码农类General 本科 全职 @ '
                    'hudson-river-trading - 猎头 - 技术电面 … Fail | 在职跳槽"'),
)

add('1129259', **HRT1_CTX,
    section_context='C++/systems fundamentals portion of the phone screen',
    question_type='cpp_concepts',
    question_text=('Inline in cpp\n- For functions; advantage vs disadvantage\n- For member '
                   'variables\nSegfaults \n- MMU how does it work; how does it translate between '
                   'virtual and physical addre'),
    question_text_en=('Inline in C++: for functions — advantages vs disadvantages; for member '
                      'variables. Segfaults. MMU — how does it work, how does it translate between '
                      'virtual and physical addre... (cut off by the forum karma wall)'),
    source_quote=('Inline in cpp\n- For functions; advantage vs disadvantage\n- For member '
                  'variables\nSegfaults \n- MMU how does it work; how does it translate between '
                  'virtual and physical addre'),
    doubt=('This is the candidate\'s own topic checklist, not the interviewer\'s wording, and it is '
           f'truncated mid-word ("physical addre") by {WALL}. ' + JSD))

add('1129259', **HRT1_CTX,
    section_context='coding portion of the phone screen (only the tail of the statement survives the wall)',
    question_type='coding_arrays',
    question_text=' up to target.\n经典的two sum problem, 用hash map O(n) 解',
    question_text_en=('... up to target. [The candidate comments:] the classic two-sum problem, '
                      'solved with a hash map in O(n).'),
    reported_answer='hash map, O(n)',
    source_quote=' up to target.\n经典的two sum problem, 用hash map O(n) 解',
    doubt=('Only the last three words of the problem statement survive the karma wall; everything '
           'identifying it as two-sum is the candidate\'s own gloss afterwards. I am recording the '
           'fragment rather than the inferred question because the question itself was not '
           'readable. ' + JSD))

# ======================= HRT — thread 1120333 =======================
HRT2_CTX = dict(
    firm='HRT', role_track='quant_developer', level='experienced', cycle='2025',
    round='phone_technical', round_name='2025 HRT Algo Engineer 电面 (30 min), after a 130-min 3-question OA',
    source_language='zh', post_date='2025-03-27',
    poster_context=(P3A + '; forum metadata line reads "2025(1-3月) 码农类General 硕士 全职 @ '
                    'hudson-river-trading - 猎头 - 技术电面 … Fail | 在职跳槽"'),
)

add('1120333', **HRT2_CTX,
    section_context='30-minute phone screen; the candidate says they misread the problem entirely',
    question_type='coding_simulation',
    question_text=('电面30min，我好像完全理解错题了 … 今天碰巧看到leetcode 有这道题，而我好像当成OOD了'
                   '设计了一个Wordle。。'),
    question_text_en=('30-minute phone screen; I think I completely misunderstood the problem. … '
                      'Today I happened to see this exact problem on LeetCode — I had apparently '
                      'treated it as an OOD question and designed a Wordle.'),
    source_quote=('今天碰巧看到leetcode 有这道题，而我好像当成OOD了设计了一个Wordle。。'),
    doubt=('The problem statement itself is behind the karma wall; all that is readable is that the '
           'phone screen problem was Wordle-related and also exists on LeetCode. The candidate says '
           'they misunderstood it, so even their framing is unreliable. Retained because a second, '
           'independent candidate reported a Wordle question at HRT (t.me/usinterview/25282, '
           '2025-09-13), which makes the topic corroborated even though the wording is not.'))

HRT2_OA = dict(HRT2_CTX, round='online_assessment', round_name='2025 HRT Algo Engineer OA')
add('1120333', **HRT2_OA,
    section_context='OA format report (not a question)',
    question_type='assessment_format',
    question_text='OA 3道题目130min 和前面差不多',
    question_text_en=('The OA was 3 questions in 130 minutes, much the same as previous ones '
                      '[reported on the forum].'),
    source_quote='OA 3道题目130min 和前面差不多',
    doubt=('Format only — the three questions are behind the karma wall. Included because the '
           '3-questions/130-minutes figure is a concrete, checkable claim about HRT\'s Algo Engineer '
           'OA and differs from the 4-questions/70-minutes CodeSignal format another candidate '
           'reported for HRT Software Engineer in 2026.'))

# ======================= SIG — thread 1041382 (solution-only recovery) ======
add('1041382',
    firm='SIG', role_track='quant_researcher', level='experienced', cycle='2024',
    round='online_assessment', round_name='SIG OA QR/QT — 9 questions in 60 minutes',
    section_context='thread replies discussing question 1; the question itself is behind the karma wall',
    question_type='solution_discussion_only',
    question_text=('两步走\n1. 一共21步，根据题目要求，路径只能是1开头1结尾：1 4 1 4 1 4 1 4 1\n'
                   '不能是4开头，否则到不了或者超步数\n2. 向上的一共是8步，只能是两种分配情况。'
                   '一是用两个4步走完，这是4选2；二是用一个4步，四个1步，这是4选1 乘上 5选4。\n'
                   '加起来答案即是26。'),
    question_text_en=('Two steps. 1. There are 21 steps in total; per the problem the path can only '
                      'begin and end with 1: 1 4 1 4 1 4 1 4 1. It cannot start with 4, or you '
                      'either cannot arrive or exceed the step count. 2. There are 8 upward steps in '
                      'total, and only two ways to allocate them: either two 4-steps, which is '
                      '4-choose-2; or one 4-step and four 1-steps, which is 4-choose-1 times '
                      '5-choose-4. Added together the answer is 26.'),
    reported_answer='26',
    source_quote=('两步走\n1. 一共21步，根据题目要求，路径只能是1开头1结尾：1 4 1 4 1 4 1 4 1\n'
                  '不能是4开头，否则到不了或者超步数\n2. 向上的一共是8步，只能是两种分配情况。'
                  '一是用两个4步走完，这是4选2；二是用一个4步，四个1步，这是4选1 乘上 5选4。\n'
                  '加起来答案即是26。'),
    source_language='zh', post_date='2024-02-14',
    poster_context=(P3A + '; a replier explaining question 1 to another candidate who asked "Q1 我用'
                    '动态规划的方法做，答案怎么会离奇的大" (I did Q1 with DP, why is my answer '
                    'bizarrely large). Thread metadata: "2023(1-3月) 金工类 硕士 全职 @ sig - 网上海投 '
                    '- 在线笔试 … 在职跳槽"'),
    doubt=('THIS IS NOT A QUESTION STATEMENT. The original post is entirely behind the forum karma '
           'wall and only the replies survive, so all that is recoverable is a solution sketch — a '
           '21-step lattice path made of moves of size 1 and 4, with 8 units of upward travel, '
           'answer 26. I am recording the verbatim solution rather than reconstructing the question '
           'from it, because reconstructing it would be fabrication. Downstream consumers should '
           'treat this as a lead, not an item.'))

add('1068784',
    firm='SIG', role_track='quant_researcher', level='experienced', cycle='2024',
    round='online_assessment', round_name='SIG QR full time OA',
    section_context='thread replies debating the answers; all questions are behind the karma wall',
    question_type='answer_key_fragment_only',
    question_text='你再算算呢，这个应该没错，我记得A20 C27 B34',
    question_text_en=('Work it out again — this should be right, I remember A20 C27 B34. [In answer '
                      'to: "why is question 4 27? I get 40".]'),
    reported_answer='A=20, C=27, B=34',
    source_quote='你再算算呢，这个应该没错，我记得A20 C27 B34',
    source_language='zh', post_date='2024-06-01',
    poster_context=(P3A + '; the thread author answering a reader who challenged the answer to '
                    'question 4. Thread metadata: "2024(4-6月) 金工类 博士 全职 @ sig - 网上海投 - '
                    '在线笔试 … 在职跳槽"'),
    doubt=('THIS IS NOT A QUESTION STATEMENT — the OP is behind the karma wall and only the answer '
           'debate survives. It establishes that SIG\'s 2024 full-time QR OA contained an item whose '
           'answer is a triple of values labelled A, B and C (20/34/27), which is consistent with '
           'the balance-puzzle style seen elsewhere in this shard, but the question is not '
           'recoverable and I am not guessing at it.'))

add('1068784',
    firm='SIG', role_track='quant_researcher', level='experienced', cycle='2024',
    round='online_assessment', round_name='SIG QR full time OA',
    section_context='thread replies; two candidates report different OA lengths in the same season',
    question_type='assessment_format',
    question_text='有人跟我一样收到的OA是60分钟21道题么。。',
    question_text_en=('Did anyone else get an OA that was 21 questions in 60 minutes? … [reply:] Me '
                      'too, and the difficulty was not low, it is simply impossible to finish.'),
    source_quote='有人跟我一样收到的OA是60分钟21道题么。。',
    source_language='zh', post_date='2024-07-16',
    poster_context=(P3A + '; a reply on the SIG QR full-time OA thread, answered by the OP who says '
                    '"60min九道题" (60 minutes, nine questions) elsewhere in the same thread'),
    doubt=('Format only, no question content. Recorded because the same thread contains two '
           'mutually inconsistent descriptions of the same firm\'s OA in the same season — 9 '
           'questions in 60 minutes and 21 questions in 60 minutes — which is direct evidence that '
           'SIG runs more than one OA form and that "the SIG OA" is not a single fixed paper.'))

add('1090786',
    firm='SIG', role_track='quant_developer', level='unknown', cycle='2024',
    round='online_assessment', round_name='SIG SDE OA — two coding questions posted as screenshots',
    section_context='a replier solving question 2 for the OP; the question was posted as an image attachment',
    question_type='solution_discussion_only',
    question_text=('第二题就是计算"#"或者底部"-"与最近的"F"纵向距离最小值\n把所有的最小值再求一个最小值，'
                   '得到距离d。。\n然后把所有的"F"位置提取出来，再改写成"-"\n最后把上面的坐标(x, y)'
                   '对应新坐标(x, y+d)的cell改写成"F"'),
    question_text_en=('Question 2 is just computing the minimum vertical distance between a "#" (or a '
                      '"-" at the bottom) and the nearest "F". Take the minimum of all those minima '
                      'to get a distance d. Then extract all the "F" positions and rewrite them as '
                      '"-". Finally rewrite the cell at the new coordinate (x, y+d) corresponding to '
                      'each old coordinate (x, y) as "F".'),
    source_quote=('第二题就是计算"#"或者底部"-"与最近的"F"纵向距离最小值\n把所有的最小值再求一个最小值，'
                  '得到距离d。。\n然后把所有的"F"位置提取出来，再改写成"-"\n最后把上面的坐标(x, y)'
                  '对应新坐标(x, y+d)的cell改写成"F"'),
    source_language='zh', post_date='2024-10-10',
    poster_context=(P3A + '; the OP wrote only "请大家指教，谢谢！！" (please advise, thank you) and '
                    'attached the two questions as images, which the Wayback snapshot does not '
                    'contain; this is a replier working out question 2 from those images'),
    doubt=('THIS IS NOT A QUESTION STATEMENT. The questions were image attachments that the archive '
           'did not capture, so only a replier\'s solution survives. It tells us the item was a '
           'character-grid simulation using "#", "-" and "F" glyphs, which is unusually specific, '
           'but the actual prompt is unrecoverable and I have not reconstructed it.'))

# ---------------------------------------------------------------- emit
missing, out = [], []
for rec in R:
    tid = rec.pop('_tid')
    if 'source_quote' not in rec:
        sys.stderr.write(f'NO QUOTE FIELD: {tid} {rec.get("section_context")!r}\n')
        continue
    txt = page_text(tid)
    norm = txt.replace('\u00a0', ' ')
    q = rec['source_quote'].replace('\u00a0', ' ')
    # the page text collapses runs of markup into single newlines; compare on
    # whitespace-insensitive forms so table/BBCode noise does not defeat the check
    if q in norm or re.sub(r'\s+', '', q) in re.sub(r'\s+', '', norm):
        out.append(rec)
    else:
        missing.append((tid, rec['firm'], q[:80]))

if missing:
    sys.stderr.write('QUOTE NOT FOUND IN SNAPSHOT:\n')
    for m in missing:
        sys.stderr.write(f'  {m}\n')

order = ['firm', 'role_track', 'level', 'cycle', 'office', 'round', 'round_name', 'platform',
         'section_context', 'question_type', 'question_text', 'question_text_en', 'reported_answer',
         'source_url', 'source_type', 'source_quote', 'source_language', 'post_date', 'access',
         'retrieval_method', 'upstream_source', 'poster_context', 'doubt']
with open('raw/chat_and_archive.jsonl', 'a', encoding='utf-8') as f:
    for rec in out:
        f.write(json.dumps({k: rec[k] for k in order}, ensure_ascii=False) + '\n')
print(f'verified+written={len(out)}  failed={len(missing)}')
