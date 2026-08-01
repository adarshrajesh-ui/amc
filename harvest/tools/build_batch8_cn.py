#!/usr/bin/env python3
"""Optiver and SIG assessment content from two Chinese-language boards this machine cannot fetch.

nowcoder.com sits behind an Aliyun WAF and 1point3acres.com behind Cloudflare; both were
re-probed on 2026-08-01 and both return an interstitial rather than the post. The search
engine's cached extract is the only readable copy, preserved verbatim in
raw/pages/websearch_highlights_batch2.txt, so every record here is access="snippet_only".
Each source_quote is asserted to appear byte-for-byte in that file before it is emitted.
"""
import json
import re
import sys

SNIP = open('raw/pages/websearch_highlights_batch2.txt', encoding='utf-8').read()

BLOCK_NC = ('nowcoder.com is behind an Aliyun WAF for this machine — www, m. and the /discuss/ '
            'form all returned the "为了更好的访问体验，请进行验证" interstitial on 2026-08-01 — so the '
            'post could not be read directly and only the search engine\'s cached extract is '
            'available')
BLOCK_1P = ('1point3acres is Cloudflare-blocked to this machine and archive.org has no snapshot '
            'of this thread, so only the search engine\'s cached extract is available')
RECALL = ('written from memory after the fact, so wording is the poster\'s paraphrase rather '
          'than the assessment\'s own text')

R = []


def add(firm, role, level, cycle, office, rnd, rname, platform, section, qtype, qtext, qtext_en,
        quote, url, stype, lang, post_date, poster, doubt, answer=None, upstream=None):
    if quote not in SNIP:
        print('QUOTE NOT IN EVIDENCE FILE:', repr(quote[:90]), file=sys.stderr)
        sys.exit(1)
    R.append({
        'firm': firm, 'role_track': role, 'level': level, 'cycle': cycle, 'office': office,
        'round': rnd, 'round_name': rname, 'platform': platform, 'section_context': section,
        'question_type': qtype, 'question_text': qtext, 'question_text_en': qtext_en,
        'reported_answer': answer, 'source_url': url, 'source_type': stype,
        'source_quote': quote, 'source_language': lang, 'post_date': post_date,
        'access': 'snippet_only', 'retrieval_method': 'websearch_snippet',
        'upstream_source': upstream, 'poster_context': poster, 'doubt': doubt})


# ===================================================== Nowcoder — Optiver Shanghai SWE intern OA
NC = 'https://www.nowcoder.com/feed/main/detail/3d62edffa9dc40c883d3d019dd7f6789'
NC_POSTER = ('A 牛客网 (Nowcoder) feed post titled "985废柴挑战顶级量化optiver笔试" by a mainland '
             'Chinese undergraduate describing, module by module, the Optiver Shanghai Software '
             'Developer summer-internship online assessment they had just sat. The visible '
             'fragment of the header reads "5 Shanghai Software Developer Summer Internship".')
NC_D = BLOCK_NC + '. It is ' + RECALL + '. ' + \
       ('The cycle year is cut off mid-token in the cached extract ("5 Shanghai ..."), so the '
        'year is not established.')

add('Optiver', 'quant_developer', 'internship', 'unknown', 'Shanghai', 'online_assessment',
    'Optiver Shanghai Software Developer Summer Internship OA, part 1', 'HackerRank',
    'part 1 — the first of two HackerRank coding questions', 'coding_class_design',
    '第一道写一个newsProvider类，需要实现AddSubscription，RemoveSubscription，NewsReceived，HashMap方法。',
    ('The first one: write a newsProvider class; you have to implement AddSubscription, '
     'RemoveSubscription, NewsReceived and HashMap methods.'),
    '第一道写一个newsProvider类，需要实现AddSubscription，RemoveSubscription，NewsReceived，HashMap方法。',
    NC, 'nowcoder', 'zh', 'unknown', NC_POSTER,
    NC_D + ' The poster says they gave up on this section ("个人实力不济，选择躺平"), so the method '
           'list is what they read off the screen rather than what they implemented. "HashMap方法" '
           'is likely their garbling of a fourth API method; an independently posted copy of the '
           'same Optiver question on 1point3acres names the fourth method Publish.')

add('Optiver', 'quant_developer', 'internship', 'unknown', 'Shanghai', 'online_assessment',
    'Optiver Shanghai Software Developer Summer Internship OA, part 1', 'HackerRank',
    'part 1 — the second of two HackerRank coding questions', 'coding_class_design',
    '卫星网络的类，要实现SatelliteConnected，RelationshipEstablished，MessageReceived三个方法。',
    ('A satellite-network class; you have to implement the three methods SatelliteConnected, '
     'RelationshipEstablished and MessageReceived.'),
    '卫星网络的类，要实现SatelliteConnected，RelationshipEstablished，MessageReceived三个方法。',
    NC, 'nowcoder', 'zh', 'unknown', NC_POSTER,
    NC_D + ' Only the class name and the three method names survive; the poster records no '
           'problem statement, constraints or semantics for this question.')

# part 2 — the twenty multiple-choice items, each recalled as a one-line topic
MCQ = [
    ('多线程利用多CPU架构', 'how multithreading exploits a multi-CPU architecture', 'concurrency'),
    ('关系数据库中规范化是什么', 'what normalisation is in a relational database', 'databases'),
    ('二维数组两种遍历方式的快慢',
     'which of two traversal orders over a 2-D array is faster', 'memory_locality'),
    ('哈希一些操作的时间复杂度',
     'the time complexity of various hash-table operations', 'complexity'),
    ('Linux的system call时间开销为50ns',
     'a Linux system call costs 50 ns [premise of the question]', 'systems_estimation'),
    ('对于动态数组，哪项平均时间复杂度最低',
     'for a dynamic array, which operation has the lowest average time complexity', 'complexity'),
    ('小明想学python和java，不推荐哪本书',
     'Xiao Ming wants to learn Python and Java — which book would you not recommend', 'other'),
    ('子网掩码定义同一网络的IP地址范围',
     'a subnet mask defines the range of IP addresses on the same network', 'networking'),
    ('UDP传输会发生什么情况', 'what can happen during UDP transmission', 'networking'),
    ('四个16进制数哪些小于100',
     'which of four hexadecimal numbers are less than 100', 'number_bases'),
    ('给栈操作选最后栈的内容',
     'given a sequence of stack operations, choose the final contents of the stack',
     'data_structures'),
    ('选择邻接矩阵比领接链表的优势',
     'choose the advantage of an adjacency matrix over an adjacency list', 'data_structures'),
    ('在多线程程序中修复错误共享',
     'fixing false sharing in a multithreaded program', 'concurrency'),
    ('二进制表示16位整数需要多少位',
     'how many bits are needed to represent a 16-bit integer in binary', 'number_bases'),
    ('TCP/IP在哪些情况下不是好的选择',
     'in which situations is TCP/IP not a good choice', 'networking'),
    ('位运算', 'bit manipulation', 'bit_manipulation'),
    ('哪一个概念不用于多线程中的同步',
     'which one of these concepts is not used for synchronisation in multithreading',
     'concurrency'),
    ('在给的一个二叉搜索树中对随机的一个node平均比较几次',
     'in a given binary search tree, how many comparisons on average to reach a random node',
     'data_structures'),
    ('向空堆中插入65个元素，深度是多少',
     'inserting 65 elements into an empty heap — what is the depth', 'data_structures'),
    ('哪些协议用于Linux进程间通信',
     'which protocols are used for inter-process communication on Linux', 'systems'),
]
for i, (zh, en, topic) in enumerate(MCQ, 1):
    add('Optiver', 'quant_developer', 'internship', 'unknown', 'Shanghai', 'online_assessment',
        'Optiver Shanghai Software Developer Summer Internship OA, part 2', 'unknown',
        f'part 2 — item {i} of the 20 multiple-answer CS-fundamentals questions the poster listed',
        'cs_fundamentals_mcq_' + topic,
        zh, en, zh, NC, 'nowcoder', 'zh', 'unknown', NC_POSTER,
        NC_D + ' This is a one-line topic label the poster wrote down for one of twenty '
               'multiple-answer questions ("不定项选择题"), not the question as it was worded on '
               'screen; the options are not recorded, so the item cannot be answered from this '
               'text alone.')

add('Optiver', 'quant_developer', 'internship', 'unknown', 'Shanghai', 'online_assessment',
    'Optiver Shanghai Software Developer Summer Internship OA, part 2', 'unknown',
    'part 2 as a whole', 'assessment_format',
    'part2是20道不定项选择题', 'Part 2 is 20 multiple-answer multiple-choice questions.',
    'part2是20道不定项选择题', NC, 'nowcoder', 'zh', 'unknown', NC_POSTER,
    NC_D + ' A structural note rather than a question. "不定项选择题" means the number of correct '
           'options per item is not fixed, which the poster does not elaborate on.')

GAMES = [
    ('Balloon',
     '1、Balloon，每次充气花费$0.1, 超过某个值会爆炸，爆炸前收回当前的金额。第一次有30轮，金额不限；第二次20轮，在上次获得的金额基础上打气。',
     ('Balloon: each puff of air costs $0.10; past some threshold the balloon bursts; you bank '
      'the amount accumulated before it bursts. The first run has 30 rounds with no cap on the '
      'amount; the second has 20 rounds, inflating on top of the amount won in the first.'),
     'risk_taking_game',
     'The poster adds that with an aggressive strategy they finished on $35.'),
    ('Skyscraper',
     '2、Skyscraper，类似汉诺塔，三个柱子，一些不同颜色的块移动到答案一致。',
     ('Skyscraper: like Towers of Hanoi — three pegs, a number of differently coloured blocks to '
      'be moved until the arrangement matches the target.'),
     'planning_puzzle_game', None),
    ('Shapeshift',
     '3、Shapeshift，考反应，出现矩形按左方向键，圆形按右方向键。',
     ('Shapeshift: a reaction test — when a rectangle appears press the left arrow key, when a '
      'circle appears press the right arrow key.'),
     'reaction_speed_game', None),
    ('the switch',
     '4、the switch，有两个框，上面看和是不是奇数，下面框看两组箭头是不是相同。',
     ('The switch: there are two boxes — in the top one you judge whether the sum is odd, in the '
      'bottom one whether two groups of arrows are the same.'),
     'task_switching_game', None),
    ('code compare',
     '5、code compare， 一个字符串，有四个选项，选相同字符串，每次估计就5-6秒。',
     ('Code compare: a string is shown with four options; pick the identical string. About 5-6 '
      'seconds per item.'),
     'perceptual_speed_game',
     'The poster says they could only hold the first three characters in memory.'),
    ('number Box',
     '6、number Box，四个数和中间的结果，通过加减乘除法计算出结果',
     ('Number Box: four numbers and a result in the middle; get to the result using addition, '
      'subtraction, multiplication and division.'),
     'mental_arithmetic_game', None),
    ('figure it out',
     '7、figure it out，猜盖住的牌。最多16种组合，图形，颜色，图纹，点。每次会显示和盖住的牌对比错误和正确几项。',
     ('Figure it out: guess the face-down card. At most 16 combinations across shape, colour, '
      'pattern and dots. After each guess it shows how many attributes you got right and wrong '
      'against the hidden card.'),
     'deduction_game', None),
]
for name, zh, en, qtype, extra in GAMES:
    add('Optiver', 'quant_developer', 'internship', 'unknown', 'Shanghai', 'online_assessment',
        'Optiver Shanghai Software Developer Summer Internship OA, part 3 — nine mini-games',
        'unknown', f'part 3 — the mini-game the poster calls "{name}"', qtype,
        zh, en, zh, NC, 'nowcoder', 'zh', 'unknown', NC_POSTER,
        NC_D + ' A game rather than a question with an answer; the description is the poster\'s '
               'own summary of what appeared on screen. They state they could not recall two of '
               'the nine games at all ("另外两个记不清了").' + ((' ' + extra) if extra else ''))

# ===================================================== 1point3acres 1147508 — the Optiver OA text
U1147508 = 'https://www.1point3acres.com/bbs/thread-1147508-1-1.html'
P1147508 = ('A 1point3acres 海外面经 thread titled (mojibaked in the cached extract) "Optiver OA '
            '题目", in which the poster says Optiver\'s OA has three parts and reproduces the '
            'first part\'s coding question verbatim in English.')
D1147508 = BLOCK_1P + '. '

add('Optiver', 'quant_developer', 'unknown', 'unknown', 'unknown', 'online_assessment',
    'Optiver OA part 1 — coding', 'unknown',
    'the opening statement of the NewsProvider coding question', 'coding_system_design',
    ('As the provider of a news aggregation service, you aim to provide your customers with a '
     'system that is as easy to use as possible. There are many different news providers, and it '
     'is tedious for users to subscribe to all of them manually, so you want to provide a single '
     'subscription that manages all the news providers for each customer.'),
    None,
    ('As the provider of a news aggregation service, you aim to provide your customers with a '
     'system that is as easy to use as possible. There are many different news providers, and it '
     'is tedious for users to subscribe to all of them manually, so you want to provide a single '
     'subscription that manages all the news providers for each customer.'),
    U1147508, 'other', 'en', 'unknown', P1147508,
    D1147508 + ('The cached extract elides the middle of the page, so this is the question\'s '
                'opening paragraph rather than the whole prompt. It is corroborated independently: '
                'a Nowcoder poster describing the Optiver Shanghai SWE intern OA lists a '
                '"newsProvider" class with AddSubscription / RemoveSubscription / NewsReceived '
                'methods as their first HackerRank question. Prep-vendor sites also host versions '
                'of this problem, but they postdate and cite the forum recall rather than the '
                'other way round.'))

add('Optiver', 'quant_developer', 'unknown', 'unknown', 'unknown', 'online_assessment',
    'Optiver OA part 1 — coding', 'unknown',
    'the filtering rules stated in the NewsProvider coding question', 'coding_requirement',
    ('Each subscriber is only interested in a certain set of topics, and should only receive news '
     'about those topics. Each news item has an interest score and each subscriber nominates '
     'their minimum interest score.'),
    None,
    ('Each subscriber is only interested in a certain set of topics, and should only receive news '
     'about those topics. Each news item has an interest score and each subscriber nominates '
     'their minimum interest score.'),
    U1147508, 'other', 'en', 'unknown', P1147508,
    D1147508 + ('Part of the same coding question as the record above rather than a separate '
                'question; recorded separately because the cached extract gives it as its own '
                'contiguous block and it states the substantive rule the candidate must '
                'implement. The sentence continues past the quoted text into a run the search '
                'engine mojibaked ("subscriber鈥檚 minimum"), so the quote stops at the last '
                'byte-clean sentence.'))

add('Optiver', 'quant_developer', 'unknown', 'unknown', 'unknown', 'online_assessment',
    'Optiver OA part 1 — coding', 'unknown',
    'the custom-testing input format of the NewsProvider coding question', 'coding_io_spec',
    ('Input Format for Custom Testing\nEach line of input begins with a keyword followed by one '
     'or more parameters separated by whitespace, per the order described above. The keywords '
     'are:'),
    None,
    ('Input Format for Custom Testing\nEach line of input begins with a keyword followed by one '
     'or more parameters separated by whitespace, per the order described above. The keywords '
     'are:'),
    U1147508, 'other', 'en', 'unknown', P1147508,
    D1147508 + ('The four keywords that follow ("subscribe", "unsubscribe", "news", "publish", '
                'mapping to AddSubscription, RemoveSubscription, NewsReceived and Publish) are '
                'broken up in the cached extract by repeated mojibaked "复制代码" copy-button '
                'labels, so they cannot be quoted as one contiguous run and are described here '
                'instead of quoted.'))

# ===================================================== 1point3acres 686183 — SIG round 1 and 2
U686183 = 'https://www.1point3acres.com/bbs/thread-686183-1-1.html'
P686183 = ('A 1point3acres 海外面经 thread titled "SIG 1轮+2轮面经" in which the poster lists the '
           'questions from their first and second SIG rounds; the visible timestamp on the '
           'opening post is 2020-11-11 and the earliest reply is 2020-11-25.')
D686183 = (BLOCK_1P + ' (archive.org/wayback/available reports no snapshot for this thread and '
                      'the CDX endpoint returned HTTP 503 to this machine). ')

add('SIG', 'quant_researcher', 'unknown', 'unknown', 'unknown', 'phone_technical',
    'SIG 第一轮 (first round)', 'unknown', 'question 1 of the first round', 'probability_expectation',
    '1. 圆里随机画n条线，问能把圆分成几分 （期望）？ 把分成的份数和交点个数对应起来，然后算交点个数的期望。',
    ('1. Draw n lines at random inside a circle — into how many pieces do they divide the circle '
     '(in expectation)? Match the number of pieces to the number of intersection points, then '
     'compute the expected number of intersection points.'),
    '1. 圆里随机画n条线，问能把圆分成几分 （期望）？ 把分成的份数和交点个数对应起来，然后算交点个数的期望。',
    U686183, 'other', 'zh', '2020-11-11', P686183,
    D686183 + ('The second sentence is the poster\'s own hint about how to attack it, not part of '
               'the interviewer\'s wording, and the quote does not say whether the "lines" are '
               'chords with endpoints uniform on the circumference — a replier supplies that '
               'reading. ' + RECALL + '.'),
    answer=('A replier derives n + 1 + n*(n-1)/6, using P(two chords cross) = 1/3 and '
            '#regions = n + #intersections + 1; the same derivation is repeated independently on '
            '1point3acres thread-1042392.'))

add('SIG', 'quant_researcher', 'unknown', 'unknown', 'unknown', 'phone_technical',
    'SIG 第一轮 (first round)', 'unknown', 'question 2 of the first round', 'probability_stopping_time',
    '2. 扔硬币 进入 HTH HHT 之一就结束，问进入每一个的概率是多大？（不太记得具体ending state是啥了）',
    ('2. Flip a coin; the game ends as soon as you hit either HTH or HHT. What is the probability '
     'of ending on each of them? (I don\'t remember exactly what the ending states were.)'),
    '2. 扔硬币 进入 HTH HHT 之一就结束，问进入每一个的概率是多大？（不太记得具体ending state是啥了）',
    U686183, 'other', 'zh', '2020-11-11', P686183,
    D686183 + ('The poster explicitly flags that they are unsure which two ending patterns were '
               'used ("不太记得具体ending state是啥了"), so HTH/HHT may not be the exact pair asked. '
               'A third question exists on the page but the cached extract cuts off at "3. 三".'))

# ===================================================== 1point3acres 1042392 — SIG OA + rounds
U1042392 = 'https://www.1point3acres.com/bbs/thread-1042392-1-1.html'
P1042392 = ('A 1point3acres 数科面经 thread titled "SIG OA和一面/二面挂经" — a rejection write-up '
            'covering the SIG online assessment and the first and second interview rounds for a '
            'QR position; replies on the page are dated February 2024.')
D1042392 = BLOCK_1P + ' and the body is additionally behind the forum\'s 188-karma wall, so an ' \
                      'unknown amount of the write-up is not in the cached extract either. '

add('SIG', 'quant_researcher', 'unknown', 'unknown', 'unknown', 'online_assessment',
    'SIG OA', 'unknown', 'the poster\'s characterisation of the OA as a whole', 'assessment_format',
    'OA就很简单 都是题库里的内容最多变了变数字 只要地里的题全都会做了，oa肯定没有问题的。',
    ('The OA was very easy — it is all material from the question bank, with at most the numbers '
     'changed. As long as you can do all the questions on this forum, the OA will be no problem.'),
    'OA就很简单 都是题库里的内容最多变了变数字 只要地里的题全都会做了，oa肯定没有问题的。',
    U1042392, 'other', 'zh', 'unknown', P1042392,
    D1042392 + ('A claim about the OA, not a question from it, and an unverifiable one: "题库" '
                'and "地里的题" refer to the forum\'s own accumulated recall, so this is a '
                'candidate asserting that SIG reuses previously leaked items.'))

add('SIG', 'quant_researcher', 'unknown', 'unknown', 'unknown', 'onsite',
    'SIG 二面 (second round)', 'unknown', 'the whole of the second round', 'behavioural',
    '二面就纯bq，问了一些地里其他一样的bq，类似与why QR? why SIG这种之类的。',
    ('The second round was purely behavioural — the same BQs as others on this forum have had, '
     'along the lines of "why QR?", "why SIG?" and so on.'),
    '二面就纯bq，问了一些地里其他一样的bq，类似与why QR? why SIG这种之类的。',
    U1042392, 'other', 'mixed', 'unknown', P1042392,
    D1042392 + ('"why QR?" and "why SIG?" are given as examples of the kind of question asked '
                '("类似与...这种之类的"), not as a verbatim list, so the exact wording is not '
                'established.'))

add('SIG', 'quant_researcher', 'unknown', 'unknown', 'unknown', 'phone_technical',
    'SIG 一面 (first round)', 'unknown',
    'a replier reconstructing the solution to the circle-cutting question', 'solution_discussion_only',
    ('为什么两刀相交的概率是1/3呀 就是我们考虑圆上任意四个点（因为两刀两个点，三个点的情况测度为0，'
     '比起两刀四个点，可以忽略掉在算期望的时候）；用两条线连起来这四个点的方式一共三种，两种情况下'
     '这两刀是平行的，第三种情况是两刀是相交的，所以两刀相交的概率就是1/3.'),
    ('Why is the probability that two cuts intersect 1/3? Consider any four points on the circle '
     '(two cuts give two points each; the three-point case has measure zero and can be ignored '
     'when taking the expectation). There are three ways to join those four points with two '
     'lines; in two of them the cuts are parallel, in the third they intersect — so the '
     'probability that two cuts intersect is 1/3.'),
    ('为什么两刀相交的概率是1/3呀 就是我们考虑圆上任意四个点（因为两刀两个点，三个点的情况测度为0，'
     '比起两刀四个点，可以忽略掉在算期望的时候）；用两条线连起来这四个点的方式一共三种，两种情况下'
     '这两刀是平行的，第三种情况是两刀是相交的，所以两刀相交的概率就是1/3.'),
    U1042392, 'other', 'zh', 'unknown', P1042392,
    D1042392 + ('Not a question but the discussion of one: it is the independent corroboration '
                'that SIG asks the circle-cutting expectation question recorded from '
                'thread-686183, since this thread reaches the same answer '
                '("/3*C^2_n 然后用交点个数算块数=刀数+交点数+1就完事了") on a different board four '
                'years later. A later reply on this same page corrects "平行" to "在圆内不相交".'))

# ===================================================== 1point3acres 1118978 — SIG QR phone screen
U1118978 = 'https://www.1point3acres.com/bbs/thread-1118978-1-1.html'
P1118978 = ('A 1point3acres 数科面经 thread titled "SIG第一轮电面 面经", posted by a QR candidate '
            'immediately after their first-round SIG phone interview; a reply is dated 2025-03-20.')

add('SIG', 'quant_researcher', 'unknown', 'unknown', 'unknown', 'phone_technical',
    'SIG 第一轮电面 (first-round phone interview)', 'unknown',
    'the second part of the second of two questions', 'probability_uniform_partial',
    ('才结束的电话面试，一共俩题，第一题地里原题就不多啰嗦了，第二题第一部分也是地里的，第二部分算扩展我写下来： '
     'X is uniformly [0,'),
    ('Just finished the phone interview, two questions in total. The first was an existing '
     'question from this forum so I won\'t go on about it; the first part of the second was also '
     'from this forum, and the second part counts as an extension, which I\'ll write down here: '
     'X is uniformly [0,'),
    ('才结束的电话面试，一共俩题，第一题地里原题就不多啰嗦了，第二题第一部分也是地里的，第二部分算扩展我写下来： '
     'X is uniformly [0,'),
    U1118978, 'other', 'mixed', 'unknown', P1118978,
    BLOCK_1P + ('. The question itself is truncated: the forum\'s 188-karma wall cuts in at '
                'exactly the point where the problem is stated, so all that survives is the '
                'opening "X is uniformly [0,". This record exists to document that the question '
                'was asked and that its stated answer is contested — it is not a usable question. '
                'Two respondents disagree on the answer (2/3 versus 3/4), which is itself evidence '
                'the missing text matters.'),
    answer=('The poster reports 2/3; a later replier who says they have just sat the same '
            'interview argues it is 3/4 (=2/3 * 3/4+1 * 1/4).'))

add('SIG', 'quant_researcher', 'unknown', 'unknown', 'unknown', 'phone_technical',
    'SIG 第一轮电面 (first-round phone interview)', 'unknown',
    'a replier disputing the answer to the second question', 'solution_discussion_only',
    '最近刚面完，我想说第二部分答案不是2/3，而是3/4 =2/3 * 3/4+1 * 1/4，真的被版主误导了。。。哎',
    ('I sat it recently too, and I want to say the answer to the second part is not 2/3 but 3/4 '
     '= 2/3 * 3/4 + 1 * 1/4 — I was genuinely misled by the moderator... sigh.'),
    '最近刚面完，我想说第二部分答案不是2/3，而是3/4 =2/3 * 3/4+1 * 1/4，真的被版主误导了。。。哎',
    U1118978, 'other', 'zh', 'unknown', P1118978,
    BLOCK_1P + ('. Not a question but a dispute about one, and it is the only independent '
                'confirmation on the page that a second candidate sat the same SIG phone question; '
                'the question text it refers to is itself behind the karma wall and unreadable.'))

with open('raw/chat_and_archive.jsonl', 'a', encoding='utf-8') as f:
    for r in R:
        f.write(json.dumps(r, ensure_ascii=False) + '\n')
print('appended', len(R), 'records')
