#!/usr/bin/env python3
"""Jane Street recall from two Cloudflare-blocked 1point3acres threads, plus assessment-format
facts from reddit posts that only the Arctic Shift mirror serves to this machine.

The 1point3acres records quote raw/pages/websearch_highlights_batch3.txt, the verbatim capture
of the search engine's cached extract; the reddit records quote raw/pages/arctic/posts.json,
the mirror snapshot, because reddit.com itself returns 403 here.
"""
import json
import sys

SNIP = open('raw/pages/websearch_highlights_batch3.txt', encoding='utf-8').read()
POSTS = json.load(open('raw/pages/arctic/posts.json', encoding='utf-8'))

R = []


def add(rec, quote, haystack):
    if quote not in haystack:
        print('QUOTE NOT FOUND:', repr(quote[:90]), file=sys.stderr)
        sys.exit(1)
    rec['source_quote'] = quote
    R.append(rec)


def p3a(firm, role, level, cycle, rnd, rname, section, qtype, qtext, qtext_en, quote, url,
        lang, post_date, poster, doubt, answer=None, office='unknown'):
    add({'firm': firm, 'role_track': role, 'level': level, 'cycle': cycle, 'office': office,
         'round': rnd, 'round_name': rname, 'platform': 'unknown', 'section_context': section,
         'question_type': qtype, 'question_text': qtext, 'question_text_en': qtext_en,
         'reported_answer': answer, 'source_url': url, 'source_type': 'other',
         'source_language': lang, 'post_date': post_date, 'access': 'snippet_only',
         'retrieval_method': 'websearch_snippet', 'upstream_source': None,
         'poster_context': poster, 'doubt': doubt}, quote, SNIP)


def rdt(pid, firm, role, level, cycle, rnd, rname, platform, section, qtype, qtext, quote,
        poster, doubt, answer=None, office='unknown'):
    p = POSTS[pid]
    url = 'https://www.reddit.com' + p['permalink']
    add({'firm': firm, 'role_track': role, 'level': level, 'cycle': cycle, 'office': office,
         'round': rnd, 'round_name': rname, 'platform': platform, 'section_context': section,
         'question_type': qtype, 'question_text': qtext, 'question_text_en': None,
         'reported_answer': answer, 'source_url': url, 'source_type': 'reddit_thread',
         'source_language': 'en', 'post_date': 'unknown', 'access': 'archive_only',
         'retrieval_method': 'webfetch', 'upstream_source': None, 'poster_context': poster,
         'doubt': doubt}, quote, (p.get('title') or '') + '\n' + (p.get('selftext') or ''))


BLOCK_1P = ('1point3acres is Cloudflare-blocked to this machine and archive.org was returning '
            'HTTP 429 to every snapshot lookup at the time, so only the search engine\'s cached '
            'extract is available')
RECALL = ('written from memory some time after the interview, so the wording is the poster\'s '
          'paraphrase and not the interviewer\'s')

# ============================================ 1p3a 473191 — Jane Street QT full-time phone rounds
U473191 = 'https://www.1point3acres.com/bbs/thread-473191-1-1.html'
P473191 = ('A 1point3acres 海外面经 thread titled "Jane Street Quant Trader电面", tagged '
           '"2019(10-12月) 金工类 本科 全职@janestreet - 网上海投 - 技术电面 | Fail | 应届毕业生". '
           'The poster says they interviewed at Jane Street twice — once for an internship, '
           'failing at round 3, and once full-time, starting from round 3 and failing again — '
           'and writes up rounds 1 through 3. Replies on the page are dated February 2019.')
D473191 = BLOCK_1P + '. ' + RECALL + '.'

p3a('Jane Street', 'quant_trader', 'new_grad', '2019', 'phone_technical',
    'Jane Street Round 1 (电面)', 'the first of the questions the poster lists under Round 1',
    'probability_coins',
    '4个硬币，2个正面的概率，偶数个正面的概率',
    ('Four coins: the probability of two heads, and the probability of an even number of heads.'),
    '4个硬币，2个正面的概率，偶数个正面的概率', U473191, 'zh', 'unknown', P473191,
    D473191 + ' The quote does not say the coins are fair, and gives no follow-up wording.')

p3a('Jane Street', 'quant_trader', 'new_grad', '2019', 'phone_technical',
    'Jane Street Round 1 (电面)', 'the second item in the poster\'s Round 1 list',
    'probability_coupon_collector',
    '扔骰子，6个数字全部出现时扔到次数的期望',
    ('Rolling a die: the expected number of rolls until all six numbers have appeared.'),
    '扔骰子，6个数字全部出现时扔到次数的期望', U473191, 'zh', 'unknown', P473191,
    D473191 + ' The poster runs this and the next question together on one line, so where one '
              'question ends and the next begins is an editorial judgement.')

p3a('Jane Street', 'quant_trader', 'new_grad', '2019', 'phone_technical',
    'Jane Street Round 1 (电面)', 'the third item in the poster\'s Round 1 list, with its follow-up',
    'probability_and_calibration',
    ('两个骰子，积是完全平方数的概率，自信程度，是否接受打赌（因为我一开始算错了，就问了我这个问题）'),
    ('Two dice: the probability that the product is a perfect square; how confident are you; '
     'would you take a bet on it. (They asked me this because I got it wrong at first.)'),
    '两个骰子，积是完全平方数的概率，自信程度，是否接受打赌（因为我一开始算错了，就问了我这个问题）',
    U473191, 'zh', 'unknown', P473191,
    D473191 + ' The confidence and betting follow-ups were, by the poster\'s own account, '
              'triggered by their initial wrong answer, so they may not be part of the standard '
              'script.')

p3a('Jane Street', 'quant_trader', 'new_grad', '2019', 'phone_technical',
    'Jane Street Round 1 (电面)', 'the poster\'s summary of Round 1 as a whole', 'assessment_format',
    '基本就是一些简单的Mental Math和概率题',
    'Basically just some simple mental-math and probability questions.',
    '基本就是一些简单的Mental Math和概率题', U473191, 'zh', 'unknown', P473191,
    BLOCK_1P + '. A characterisation of the round rather than a question from it.')

p3a('Jane Street', 'quant_trader', 'new_grad', '2019', 'phone_technical',
    'Jane Street Round 2 (电面)', 'a replier posting their answers to the Round 2 questions',
    'solution_discussion_only',
    ('Round 2的第2题我的答案是87.28855，第三题的答案是956.7521。不知道对不对。 Round 2的第4题完全没有思路。'
     '有没有人最近在准备J家trader的面试，有几道题想交流一下。'),
    ('For Round 2 question 2 my answer is 87.28855, and for question 3, 956.7521 — not sure if '
     'they are right. I have no idea at all how to do Round 2 question 4. Is anyone else '
     'preparing for a J-Street trader interview at the moment? I have a few questions I would '
     'like to talk through.'),
    ('Round 2的第2题我的答案是87.28855，第三题的答案是956.7521。不知道对不对。 Round 2的第4题完全没有思路。'
     '有没有人最近在准备J家trader的面试，有几道题想交流一下。'),
    U473191, 'zh', '2019-02-14', P473191,
    BLOCK_1P + ('. Not a question but a discussion of one, and the only readable trace of Round 2: '
                'the Round 2 question texts themselves are in the part of the post the cached '
                'extract elides, so the numeric answers cannot be matched to any question. They '
                'do establish that Round 2 contained at least four questions with numeric '
                'answers.'))

p3a('Jane Street', 'quant_trader', 'new_grad', '2019', 'phone_technical',
    'Jane Street Round 3 (电面, full-time track)',
    'a replier reconstructing the answer to the first Round 3 question',
    'solution_discussion_only',
    ('R2P4 大概会根据密度函数的变化导致期望靠拢50，具体计算量太大。 R3Full-time P1 应该是24。'
     '个人理解：当我是最小的数字或最大的数字时，根据对称性，我的期望都是0。只考虑我是第二大或者第三大的情况，'
     '用次序统计量来计算，概率再乘以当我是第二or第三大时余下三个数字分布的期望而得到的收益。'
     '画出的三次多项式曲线和simulation的曲线大致相同。最值也是在7(min)与24(max)处取到。'),
    ('R2 P4: roughly, changes in the density function pull the expectation towards 50; the actual '
     'computation is too heavy. R3 full-time P1 should be 24. My reading: when I am the smallest '
     'or the largest number, by symmetry my expectation is 0 either way. Consider only the cases '
     'where I am second- or third-largest, compute with order statistics, and multiply the '
     'probability by the payoff from the expected distribution of the remaining three numbers. '
     'The cubic curve I plotted matches the simulation curve closely. The extrema are at 7 (min) '
     'and 24 (max).'),
    ('R2P4 大概会根据密度函数的变化导致期望靠拢50，具体计算量太大。 R3Full-time P1 应该是24。'
     '个人理解：当我是最小的数字或最大的数字时，根据对称性，我的期望都是0。只考虑我是第二大或者第三大的情况，'
     '用次序统计量来计算，概率再乘以当我是第二or第三大时余下三个数字分布的期望而得到的收益。'
     '画出的三次多项式曲线和simulation的曲线大致相同。最值也是在7(min)与24(max)处取到。'),
    U473191, 'zh', 'unknown', P473191,
    BLOCK_1P + ('. Not a question but a worked answer to one whose text is behind the elision — '
                'it establishes that Round 3 question 1 involved five players holding numbers and '
                'a payoff depending on one\'s rank among them, and that Round 2 question 4 had an '
                'expectation tending towards 50, but neither prompt is readable.'),
    answer='The replier gives 24 for Round 3 full-time question 1.')

# ============================================ 1p3a 1149543 — Jane Street QR intern first round
U1149543 = 'https://www.1point3acres.com/bbs/thread-1149543-1-1.html'
P1149543 = ('A 1point3acres 海外面经 thread titled "Jane Street QR Intern 一面", tagged '
            '"2025(10-12月) 码农类General 本科 实习@janestreet - 网上海投 - 技术电面 | Neutral | '
            'Hard | Pass | 应届毕业生". The poster passed and was told of a second round two days '
            'later; an edit is timestamped 2025-10-12.')

p3a('Jane Street', 'quant_researcher', 'internship', '2026', 'phone_technical',
    'Jane Street QR Intern 一面 (first round)', 'the whole of the 45-minute first round',
    'assessment_format',
    '45分钟，两道题，无拷打简历环节 第一题比较简单，经典的可以和casino互动bet骰子的题。由于印象不是很深刻就不放了避免误导人 第二题：',
    ('45 minutes, two questions, no resume grilling. The first was fairly easy — the classic one '
     'where you can interact with a casino and bet on dice. I don\'t remember it clearly enough '
     'so I won\'t write it out, to avoid misleading people. The second question:'),
    '45分钟，两道题，无拷打简历环节 第一题比较简单，经典的可以和casino互动bet骰子的题。由于印象不是很深刻就不放了避免误导人 第二题：',
    U1149543, 'zh', '2025-10-12', P1149543,
    BLOCK_1P + ('. The poster deliberately withholds question 1 ("I don\'t remember it clearly '
                'enough so I won\'t write it out"), and the text of question 2 is behind the '
                'forum\'s karma wall — the cached extract stops at the colon. So this documents '
                'the shape of the round and a one-line gloss of question 1, not the questions '
                'themselves. The cycle is inferred from an autumn-2025 posting for a summer '
                'internship.'))

# ============================================================ reddit — assessment-format facts
rdt('1f28jed', 'Akuna', 'quant_researcher', 'internship', 'unknown', 'online_assessment',
    'Akuna Capital Quant Research Intern — the maths stage after the coding challenge',
    'EasyHire', 'the stage the poster had just been sent', 'assessment_format',
    ('They asked me to finish the online Easyhire mathematics assessment, including 5 multiple '
     'choice questions.'),
    ('They asked me to finish the online Easyhire mathematics assessment, including 5 multiple '
     'choice questions.'),
    ('A r/csMajors post titled "Akuna Capital Quant Research Intern OA" by a candidate who has '
     'just passed Akuna\'s coding virtual challenge and been invited to the maths stage.'),
    ('reddit.com returns 403 to this machine, so this was read from the Arctic Shift mirror '
     'rather than from reddit itself. It states the shape of the stage — platform, five '
     'multiple-choice items — but not a single question from it; the poster is asking what to '
     'expect, having not yet sat it.'))

rdt('1qdl0q9', 'Akuna', 'quant_developer', 'internship', '2025-2026', 'online_assessment',
    'Akuna Capital C++ SWE Intern Round 1 OA', 'unknown',
    'the number of questions in round 1 and the existence of a second OA', 'assessment_format',
    ('I recently gave the Online Assessment for Akuna Capital 2025-2026 C++ SWE Intern\u00a0Round '
     '1, passed the first question with all test cases but couldn\'t pass the second and third '
     'questions with all the test cases.'),
    ('I recently gave the Online Assessment for Akuna Capital 2025-2026 C++ SWE Intern\u00a0Round '
     '1, passed the first question with all test cases but couldn\'t pass the second and third '
     'questions with all the test cases.'),
    ('A r/csMajors post titled "Akuna Capital SWE Internship C++" by a candidate who has just sat '
     'Akuna\'s round 1 C++ OA and been sent a link to schedule a round 2 OA.'),
    ('reddit.com returns 403 to this machine, so this was read from the Arctic Shift mirror. '
     'The poster establishes that round 1 had three test-case-graded coding questions and that a '
     'round 2 OA follows, but gives no problem statements at all.'))

rdt('1sus9st', 'IMC', 'quant_trader', 'new_grad', 'unknown', 'online_assessment',
    'IMC Graduate Trader video assessment', 'Spark Hire',
    'the maths item at the end of the video assessment', 'assessment_format',
    'Since that assessment includes a math problem at the end',
    'Since that assessment includes a math problem at the end',
    ('A r/quantfinance post titled "IMC Graduate Trader – Video Assessment Math Topics" by a '
     'candidate who has been invited to IMC\'s Spark Hire video assessment and is asking which '
     'topics the closing maths item covers.'),
    ('reddit.com returns 403 to this machine, so this was read from the Arctic Shift mirror. The '
     'poster has not yet sat the assessment — they know only that it ends with a maths problem, '
     'and the list of topics they go on to give is their own guess, not recall, so none of it is '
     'recorded here.'))

with open('raw/chat_and_archive.jsonl', 'a', encoding='utf-8') as f:
    for r in R:
        f.write(json.dumps(r, ensure_ascii=False) + '\n')
print('appended', len(R), 'records')
