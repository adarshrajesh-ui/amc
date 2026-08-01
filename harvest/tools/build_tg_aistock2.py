#!/usr/bin/env python3
"""Second @aistockanalyst batch.

@aistockanalyst is a public Chinese-language Telegram channel that aggregates quant-careers
material. A second sweep of its ?q= search (面試, 笔试, 真题, 校招, OA, 概率, 一面/二面/三面 …)
surfaced long first-person interview write-ups that the earlier pass never reached, several of
which quote the questions verbatim rather than summarising them.
"""
import html
import json
import os
import re
import sys

PAGES = 'raw/pages/tgmsg2'
TEXT = re.compile(r'<div class="tgme_widget_message_text[^"]*"[^>]*>(.*?)</div>', re.S)
_cache = {}


def page_text(mid):
    if mid not in _cache:
        raw = open(os.path.join(PAGES, f'aistock_{mid}.html'), encoding='utf-8',
                   errors='replace').read()
        parts = []
        for b in TEXT.findall(raw):
            t = re.sub(r'<br\s*/?>', '\n', b)
            t = re.sub(r'<[^>]+>', '', t)
            parts.append(html.unescape(t))
        _cache[mid] = '\n'.join(parts)
    return _cache[mid]


CH = ('Posted into @aistockanalyst, a public Chinese-language Telegram channel aggregating '
      'quant-careers material, readable at t.me/s/aistockanalyst with no account')
NOATTR = ('The message carries no forwarded-from header and no link to an original venue, so who '
          'wrote it and where it first appeared cannot be established from the page — the channel '
          'is an aggregator and this is very likely a copy-paste of someone else\'s write-up. That '
          'is the single biggest reason to distrust it: the chain of custody between the interview '
          'room and this page is one unverifiable hop long')

R = []


def add(mid, date, firm, role, level, cycle, rnd, rname, section, qtype, qtext, qtext_en,
        quote, poster, doubt, answer=None, office='unknown', lang='zh', upstream=None):
    R.append({
        'firm': firm, 'role_track': role, 'level': level, 'cycle': cycle, 'office': office,
        'round': rnd, 'round_name': rname, 'platform': 'unknown', 'section_context': section,
        'question_type': qtype, 'question_text': qtext, 'question_text_en': qtext_en,
        'reported_answer': answer, 'source_url': f'https://t.me/aistockanalyst/{mid}',
        'source_type': 'chat_telegram', 'source_quote': quote, 'source_language': lang,
        'post_date': date, 'access': 'full_text', 'retrieval_method': 'webfetch',
        'upstream_source': upstream, 'poster_context': poster, 'doubt': doubt, '_mid': mid})


# ==================================================== 881: Optiver Quantitative Trader
OPT_POST = (CH + '. The write-up is headed "Optiver - Quantitative Trader" and walks through the '
            'pipeline stage by stage (第一關 算數學, 第二關 算機率 + 下注遊戲, 第三關 Behavior). '
            'The same author covers WorldQuant lower down the message and elsewhere mentions '
            'graduating and compulsory military service, so they are a new graduate')

add('881', '2025-04-14', 'Optiver', 'quant_trader', 'new_grad', '2025', 'math_sequences_test',
    'Optiver 第一關 (first stage) — the timed numerical test',
    'the format and content of the whole first stage',
    'numerical_reasoning_charts',
    ('內容真的就蠻像 GRE 圖表題的考法，只是時間限制非常緊，有些 90 秒有些 75 秒，雖然可以用計算機但還'
     '是讓人手忙腳亂'),
    ('The content really is a lot like the way GRE chart questions are set, except the time limit '
     'is extremely tight — some 90 seconds, some 75 seconds — and although you may use a '
     'calculator it still leaves you flustered.'),
    ('內容真的就蠻像 GRE 圖表題的考法，只是時間限制非常緊，有些 90 秒有些 75 秒，雖然可以用計算機但還'
     '是讓人手忙腳亂'),
    OPT_POST,
    ('No individual question is reproduced — this describes the format (chart/table reading under '
     'a 75-90 second per-question clock, calculator permitted) rather than quoting a prompt, so '
     'nothing here is answerable. The per-question timings and the calculator allowance are '
     'specific enough to be falsifiable, which is what makes it worth keeping. ' + NOATTR),
    lang='mixed')

add('881', '2025-04-14', 'Optiver', 'quant_trader', 'new_grad', '2025', 'trading_game',
    'Optiver 第二關 (second stage) — probability plus a betting game',
    'the betting-game half of the stage',
    'betting_game_with_justification',
    ('有一半是玩下賭注的遊戲，給定遊戲規則跟我們手上有的錢，你想要怎麼下注的問題，你決定好要怎麼下注之'
     '後還會問你為什麼要那樣下注'),
    ('Half of it was playing betting games: given the rules of the game and the money we have in '
     'hand, the question is how you want to bet, and once you have decided how to bet it then asks '
     'you why you bet that way.'),
    ('有一半是玩下賭注的遊戲，給定遊戲規則跟我們手上有的錢，你想要怎麼下注的問題，你決定好要怎麼下注之'
     '後還會問你為什麼要那樣下注'),
    OPT_POST,
    ('The actual game rules — which are the question — are never given, so this records the '
     'mechanic (bet sizing plus a forced justification of the bet) and not a problem. The '
     'follow-up demand for a rationale is the substantive detail. ' + NOATTR))

# ==================================================== 881: WorldQuant (same message)
WQ_POST = (CH + '. The second half of the same message is headed "WorldQuant - Quantitative '
           'Researcher" and describes an OA followed by video rounds with a VP Researcher and a '
           'Regional Research Director; the author names the interviewers only by title')
WQ_DOUBT = ('WorldQuant is not one of the named target firms. More importantly this is the '
            'candidate\'s recollection of a verbally posed puzzle, and they say plainly that they '
            'needed several hints, so the phrasing is a reconstruction. ' + NOATTR)

add('881', '2025-04-14', 'WorldQuant', 'quant_researcher', 'new_grad', '2025', 'phone_technical',
    'WorldQuant 第二關 video interview, with a VP Researcher',
    'the first of two puzzle questions after the behavioural section',
    'puzzle_coin_flipping_partition',
    ('第一題是問有 100 個硬幣，其中有 20 個是正面的，80 個是反面的，但是那些硬幣的正反面我無法得知，'
     '而且我可以去翻任意數量的硬幣，題目是問我要怎麼把硬幣分成兩堆，使得兩堆的「正面硬幣數目」一樣'),
    ('The first question asked: there are 100 coins, 20 of which are heads-up and 80 tails-up, but '
     'I cannot tell which way up any coin is, and I may flip any number of coins. The question is '
     'how I should split the coins into two piles such that the two piles have the same number of '
     'heads-up coins.'),
    ('第一題是問有 100 個硬幣，其中有 20 個是正面的，80 個是反面的，但是那些硬幣的正反面我無法得知，'
     '而且我可以去翻任意數量的硬幣，題目是問我要怎麼把硬幣分成兩堆，使得兩堆的「正面硬幣數目」一樣'),
    WQ_POST,
    ('This is a complete, self-contained and answerable statement — one of the few in this shard '
     'that needs no reconstruction. Against that: it is a very widely circulated puzzle, which '
     'cuts both ways — firms do reuse classics, but a fabricator would also reach for one. The '
     'poster gives no answer. ' + WQ_DOUBT))

add('881', '2025-04-14', 'WorldQuant', 'quant_researcher', 'new_grad', '2025', 'phone_technical',
    'WorldQuant video interview with a Regional Research Director',
    'the opening probability question',
    'probability_product_of_uniforms',
    '有一題是 uniform 的 X 跟 Y，問我 XY > 0.5 的機率',
    ('One question was: X and Y are uniform; it asked me for the probability that XY > 0.5.'),
    '有一題是 uniform 的 X 跟 Y，問我 XY > 0.5 的機率',
    WQ_POST,
    ('The support of the uniforms is not stated — the poster writes only "uniform 的 X 跟 Y". '
     'Standard uniforms on [0,1] are the obvious reading and the poster mentions needing an '
     'integral, but the interval is genuinely absent from the source and I am not supplying it. '
     'Independence is likewise assumed rather than stated. ' + WQ_DOUBT))

add('881', '2025-04-14', 'WorldQuant', 'quant_researcher', 'new_grad', '2025', 'phone_technical',
    'WorldQuant video interview with a Regional Research Director',
    'the puzzle asked after the probability question',
    'puzzle_balance_weighings',
    ('後面問了一個益智遊戲，大綱主要是問有一堆一模一樣的球，其中有一顆是壞掉的，可能是比較重或是比較'
     '輕，問我要怎麼用一個天平來用最少的次數找出壞掉的球'),
    ('Afterwards it asked a puzzle; the gist is that there is a pile of identical balls, one of '
     'which is defective and may be either heavier or lighter, and it asked me how to find the '
     'defective ball using a balance scale in the fewest possible weighings.'),
    ('後面問了一個益智遊戲，大綱主要是問有一堆一模一樣的球，其中有一顆是壞掉的，可能是比較重或是比較'
     '輕，問我要怎麼用一個天平來用最少的次數找出壞掉的球'),
    WQ_POST,
    ('The number of balls is missing — the poster writes "一堆" (a pile) and prefixes the whole '
     'thing with "大綱主要是問" (the gist of what it asked), explicitly marking it as a summary. '
     'Without the count the question has no determinate answer. ' + WQ_DOUBT))

# ==================================================== 891: Optiver, staged OA pipeline
OPT891 = (CH + '. The message is headed "Optiver (Quantitative Trading)" and is structured as a '
          'numbered pipeline — OA-0, OA-1, OA-2, then BI/HR — with the length and time limit given '
          'for each stage')

add('891', '2025-04-14', 'Optiver', 'quant_trader', 'unknown', '2025', 'online_assessment',
    'Optiver OA-0 — 40 mathematical and programming questions in 3 hours',
    'the composition of the first assessment',
    'mixed_math_and_coding_inventory',
    ('0. OA-0, 40 Mathematical & Programming Questions, 3 hour\n機率與排組題為主，題目偏難，但標準似'
     '乎不用很高就會通過\n少數程式題都偏簡單'),
    ('0. OA-0, 40 Mathematical & Programming Questions, 3 hours. Mostly probability and '
     'combinatorics questions, on the hard side, but the bar for passing seems not to be very '
     'high. The few programming questions are all on the easy side.'),
    ('0. OA-0, 40 Mathematical & Programming Questions, 3 hour'),
    OPT891,
    ('A stage description: 40 questions in 3 hours, mostly probability and combinatorics. Not one '
     'question is reproduced, so nothing here is answerable. The quote is deliberately restricted '
     'to the header line, which is the part stated as fact rather than as the candidate\'s '
     'impression of difficulty. ' + NOATTR),
    lang='mixed')

add('891', '2025-04-14', 'Optiver', 'quant_trader', 'unknown', '2025', 'online_assessment',
    'Optiver OA-1 — a 24-question IQ test in 36 minutes',
    'the two example item types the poster remembered',
    'logic_constraint_seating',
    '包含給一堆 constraints，問六個人的座位的排序',
    ('Including: given a bunch of constraints, asking for the seating order of six people.'),
    '包含給一堆 constraints，問六個人的座位的排序',
    OPT891,
    ('The constraints — the entire content of a seating-order logic puzzle — are not given, only '
     'the shape of the item. The poster does supply hard format detail around it (24 questions in '
     '36 minutes, roughly 90 seconds each, each preceded by an English passage that has to be read '
     'fast), and says they finished with 9 seconds to spare. ' + NOATTR),
    lang='mixed')

add('891', '2025-04-14', 'Optiver', 'quant_trader', 'unknown', '2025', 'online_assessment',
    'Optiver OA-1 — a 24-question IQ test in 36 minutes',
    'the second example item type the poster remembered',
    'data_interpretation_chart_construction',
    '給每一季銷售量的關係，要畫出每季銷售量的圓餅圖',
    ('Given the relationships between the quarterly sales volumes, you have to draw the pie chart '
     'of sales by quarter.'),
    '給每一季銷售量的關係，要畫出每季銷售量的圓餅圖',
    OPT891,
    ('The relationships between the quarterly figures are not reproduced, so the pie chart cannot '
     'be reconstructed. Worth noting that "draw a pie chart" is an unusual response format for a '
     'timed online test and the poster does not explain how the answer was entered. ' + NOATTR),
    lang='mixed')

add('891', '2025-04-14', 'Optiver', 'quant_trader', 'unknown', '2025', 'online_assessment',
    'Optiver OA-2 — 20 mathematical and data-related problems in 1 hour, in four stages',
    'the data-analysis stage, the fourth and hardest of the four',
    'data_cleaning_under_time_pressure',
    ('主要是資料分析超難，總時間只有十五分鐘，共五小題，題目給了一個 40000 列的 csv 檔案，要我去分析'
     '這份資料，問題是資料裡面有一堆問題，包含缺漏、Overflow 的數值'),
    ('Mainly the data analysis was extremely hard: only fifteen minutes in total for five '
     'sub-questions. The question gave a 40,000-row CSV file and asked me to analyse the data; the '
     'problem is that the data has a pile of issues in it, including missing values and overflowed '
     'values.'),
    ('主要是資料分析超難，總時間只有十五分鐘，共五小題，題目給了一個 40000 列的 csv 檔案，要我去分析'
     '這份資料，問題是資料裡面有一堆問題，包含缺漏、Overflow 的數值'),
    OPT891,
    ('What the five sub-questions actually asked of the data is never said — only that the file '
     'was 40,000 rows and deliberately dirty. The poster admits they cleaned it in Excel, answered '
     'two of five, and then "直接亂猜" (just guessed) the rest, so their account of the later '
     'items is by their own admission unreliable. The four-stage structure (probability, '
     'probability, risk assessment, data analysis) is the durable part. ' + NOATTR),
    lang='mixed')

# ==================================================== 887: unidentified prop firm
U887 = ('unnamed proprietary trading firm (the author lists Citadel, Optiver, DRW, IMC and SIG '
        'among the firms applied to and says they joined a smaller one)')
P887 = (CH + '. A long guide to prop-trading recruitment written by someone who says they applied '
        'mainly to proprietary trading firms — naming Citadel, Optiver, DRW, IMC and SIG — and '
        'joined a smaller one, and who interned at an options market maker')

add('887', '2025-04-14', U887, 'quant_trader', 'new_grad', '2025', 'phone_technical',
    'the market-making segment of a trader technical interview',
    'the estimation prompts the author says they were given before being asked to quote a market',
    'estimation_then_two_sided_market',
    ('大部分時候，會要求面試者預估一個量，可以是機率或實際的數量 (我和面試官兩個人電腦裡加起來excel的'
     '總數，密西根湖一天平均停泊在港口的船隻數量，這次面試的總時長等等)，面試者需要說出推導出該數量的'
     '步驟和所有考慮的因素，然後開出一個two-sided market (bid/ask)'),
    ('Most of the time the interviewee is asked to estimate a quantity, which may be a probability '
     'or an actual count (the combined total number of Excel files on my and the interviewer\'s '
     'computers; the average number of ships docked in Lake Michigan\'s harbours in a day; the '
     'total length of this interview, and so on). The interviewee has to state the steps by which '
     'they derived the quantity and all the factors considered, and then quote a two-sided market '
     '(bid/ask).'),
    ('大部分時候，會要求面試者預估一個量，可以是機率或實際的數量 (我和面試官兩個人電腦裡加起來excel的'
     '總數，密西根湖一天平均停泊在港口的船隻數量，這次面試的總時長等等)，面試者需要說出推導出該數量的'
     '步驟和所有考慮的因素，然後開出一個two-sided market (bid/ask)'),
    P887,
    ('The firm is not identified for these specific prompts — the author is generalising across '
     'several interviews, so all that can honestly be said is that they came from one or more of '
     'the prop firms they applied to, and this record must NOT be read as attributing them to '
     'Citadel, Optiver, DRW, IMC or SIG individually. The three estimation subjects are concrete '
     'and personal enough (the interviewer\'s own Excel file count; the length of the interview '
     'in progress) that they read as genuinely encountered rather than generic. The follow-up '
     'mechanic is well specified: derive the number aloud, quote bid/ask, and the interviewer '
     'trades against your quote. ' + NOATTR),
    lang='mixed')

add('887', '2025-04-14', U887, 'quant_trader', 'new_grad', '2025', 'math_sequences_test',
    'the mental-maths online assessment used by prop firms the author applied to',
    'the item types and the timing',
    'mental_math_and_sequences',
    ('Mental math注重速度，題目為兩位數和兩位數的加減乘除(或者更多位數)和找出數列的規律。我收過的測驗'
     '大部分是8分鐘40題，或6分鐘30題'),
    ('Mental math stresses speed; the questions are two-digit by two-digit addition, subtraction, '
     'multiplication and division (or more digits) and finding the pattern in a sequence. Most of '
     'the tests I received were 40 questions in 8 minutes, or 30 questions in 6 minutes.'),
    ('Mental math注重速度，題目為兩位數和兩位數的加減乘除(或者更多位數)和找出數列的規律。我收過的測驗'
     '大部分是8分鐘40題，或6分鐘30題'),
    P887,
    ('Again not attributable to a single firm — the author says "我收過的測驗" (the tests I '
     'received), plural, across the prop firms they applied to. No individual item is reproduced. '
     'The value is the timing, which is specific and checkable: 40 questions in 8 minutes or 30 in '
     '6, i.e. about 12 seconds per question. ' + NOATTR),
    lang='mixed')

# ==================================================== 906: unidentified superday
U906 = ('unidentified firm (the message is a general industry overview and never names the '
        'employer whose superday it describes)')
P906 = (CH + '. A long overview of the quant industry that switches partway into a first-person '
        'account of one firm\'s process — "第一輪hackerrank 再來HR輪 再來superday" — and then '
        'describes the superday games')
D906 = ('The firm is never named. Worse, the message ends with advice to read Ray Dalio\'s '
        'Principles because "他們完全遵從裡面的理念", which points at Bridgewater, but that remark '
        'sits after a paragraph about a different-sounding round, so I cannot tell whether the '
        'card/dice/market-making superday belongs to the same employer. Treat the firm as unknown '
        'rather than inferring one. ' + NOATTR)

add('906', '2025-04-22', U906, 'quant_trader', 'unknown', '2025', 'trading_game',
    'superday — the first of three games (cards, dice, market making)',
    'the card game, described with the stake and the re-betting rule',
    'card_betting_game',
    ('講講卡牌 主要就是放四張A在桌上，你有100塊來猜花色，看你想怎麼bet。牌會依次揭開，每次可以重新'
     '下注'),
    ('On the card game: basically four aces are placed on the table and you have 100 dollars with '
     'which to guess the suit — you bet however you want. The cards are turned over one at a time '
     'and you may re-bet each time.'),
    ('講講卡牌 主要就是放四張A在桌上，你有100塊來猜花色，看你想怎麼bet。牌會依次揭開，每次可以重新'
     '下注'),
    P906,
    ('The betting rules are only sketched — whether the stake compounds, what the payout odds are, '
     'and whether you must bet on every card are all unstated, and those determine the answer. The '
     'poster reports reaching an expected value of 800/3 after the interviewer asked them to '
     'reduce variance, and separately warns that waiting until three cards are revealed and then '
     'betting is a bad move despite guaranteeing a double; I have kept that reasoning out of '
     'reported_answer because it answers a version of the game whose rules are not fully on the '
     'page. ' + D906))

add('906', '2025-04-22', U906, 'quant_trader', 'unknown', '2025', 'trading_game',
    'superday — the market-making game, the third of the three',
    'the market-making prompt',
    'market_making_estimation',
    '造市問題比較有趣，以前沒遇過，問題聽說很經典，給你大樓電梯，如何造市',
    ('The market-making question was more interesting, I had not met it before, and apparently it '
     'is a classic: you are given a building\'s lifts — how do you make a market?'),
    '造市問題比較有趣，以前沒遇過，問題聽說很經典，給你大樓電梯，如何造市',
    P906,
    ('"給你大樓電梯" (you are given a building\'s lifts) does not say what quantity is to be '
     'quoted — the number of lifts, the wait time, the number of trips per day — so the prompt as '
     'recorded is incomplete, and the poster themselves say the three games were open-ended and '
     'hard to describe ("都是open ended的問題有點難描述"). They also admit they do not know '
     'whether their answers were right. ' + D906))

# ==================================================== 1072: Morgan Stanley phone rounds
MS_POST = (CH + '. A detailed timeline write-up headed "Morgan Stanley Quant Finance": CV in early '
           'October, OA, then in early November phone interviews with two groups (commodity '
           'trading and AlphaWise), then two further additional interviews. The questions are '
           'written out in English as bare one-line prompts')
MS_DOUBT_BASE = (
    'Morgan Stanley is a sell-side bank and is not one of the named target firms; the author says '
    'so themselves ("但總歸還是sellside quant"). The questions are recorded as one-line prompts '
    'with no restatement of givens, so anything the interviewer said to set them up is lost. '
    'Against that, this is one of the very few sources in the shard where the candidate wrote the '
    'questions out in the interview\'s own language rather than paraphrasing into Chinese. ' +
    NOATTR)

MS1 = dict(mid='1072', date='2026-01-25', firm='Morgan Stanley', role='quant_researcher',
           level='unknown', cycle='2026', rnd='phone_technical',
           rname='Morgan Stanley phone interview, first pair of groups (commodity trading and '
                 'AlphaWise) — both interviewers PhDs',
           poster=MS_POST, lang='mixed')

add(**MS1, section='the run of probability questions that opened the round after a brief self-intro',
    qtype='probability_dice_ordering',
    qtext="Rolling dice three time, what's the probability of getting strictly increase number?",
    qtext_en="Rolling dice three times, what's the probability of getting strictly increasing numbers?",
    quote="Rolling dice three time, what's the probability of getting strictly increase number?",
    doubt=('Complete and answerable as posed, assuming a fair six-sided die — which the prompt '
           'does not actually say. ' + MS_DOUBT_BASE))

add(**MS1, section='the run of probability questions that opened the round',
    qtype='probability_min_expectation',
    qtext="Given two iid RV X and Y N~(mu,sig), what's the min Expectation value of X+Y?",
    qtext_en=("Given two i.i.d. random variables X and Y distributed N(mu, sig), what's the "
              "minimum expectation value of X+Y?"),
    quote="Given two iid RV X and Y N~(mu,sig), what's the min Expectation value of X+Y?",
    doubt=('As written this is odd: if X and Y are i.i.d. normal then E[X+Y] = 2mu and there is '
           'nothing to minimise, so the prompt is either garbled in transcription or is missing a '
           'condition the interviewer stated aloud (a plausible intended reading is min(X,Y), but '
           'that is my speculation and is not asserted). Recorded verbatim rather than repaired. ' +
           MS_DOUBT_BASE))

add(**MS1, section='the run of probability questions that opened the round',
    qtype='probability_bayes_coins',
    qtext='Given 99 unbiased coin and 1 two headed coin, P(H|2H)?',
    qtext_en=('Given 99 unbiased coins and 1 two-headed coin, what is P(H | 2H)?'),
    quote='Given 99 unbiased coin and 1 two headed coin, P(H|2H)?',
    doubt=('The notation "P(H|2H)" is the candidate\'s shorthand and is ambiguous — it is not '
           'stated whether the conditioning event is "two heads observed in two tosses of a '
           'randomly drawn coin", nor what the query event is. The setup (99 fair coins plus one '
           'double-headed) is unambiguous; the question asked of it is not. ' + MS_DOUBT_BASE))

add(**MS1, section='the run of probability questions that opened the round',
    qtype='probability_meeting_problem',
    qtext=('Two people meet at bus stop, only wait for 15 min and leave, probability of they meet? '
           '(Poisson Distribution)?'),
    qtext_en=('Two people meet at a bus stop, each only waits 15 minutes and then leaves — what is '
              'the probability that they meet? (Poisson distribution?)'),
    quote=('Two people meet at bus stop, only wait for 15 min and leave, probability of they meet? '
           '(Poisson Distribution)?'),
    doubt=('The window over which the two arrivals are distributed is missing, and without it the '
           'probability is undetermined. The trailing "(Poisson Distribution)?" appears to be the '
           'candidate\'s own guess at the machinery rather than part of the prompt — note that the '
           'classic form of this problem uses uniform arrivals, so the parenthetical may be a '
           'misremembering. ' + MS_DOUBT_BASE))

MS2 = dict(mid='1072', date='2026-01-25', firm='Morgan Stanley', role='quant_researcher',
           level='unknown', cycle='2026', rnd='phone_technical',
           rname='Morgan Stanley additional phone interview with the Netherlands AlphaWise team',
           poster=MS_POST, lang='mixed')

add(**MS2, section='model discussion prompted by logistic regression on the candidate\'s CV',
    qtype='explain_model_to_layperson',
    qtext='how do you explain logistic regression to your boss who know nothing ?',
    qtext_en='How do you explain logistic regression to your boss, who knows nothing?',
    quote='how do you explain logistic regression to your boss who know nothing ?',
    doubt=('Complete as posed and needs no reconstruction. The candidate flags it as the first '
           'time they had met this kind of question and says it was surprisingly hard to answer. ' +
           MS_DOUBT_BASE))

add(**MS2, section='the statistics run — SLR assumptions, t-test, p-value, hypothesis testing',
    qtype='statistics_f_test_interpretation',
    qtext='what if F test give you value 50, how would you interpret it?',
    qtext_en='What if the F-test gives you a value of 50 — how would you interpret it?',
    quote='what if F test give you value 50, how would you interpret it?',
    answer=('the candidate did not answer in the interview; afterwards they wrote "F distribution '
            'super skewed, so always close to zero => we can reject the null hypo"'),
    doubt=('The candidate explicitly failed this question in the room and looked the answer up '
           'afterwards, so what is in reported_answer is their own later reading, not the '
           'interviewer\'s. The degrees of freedom, which any interpretation of an F statistic '
           'needs, are not given. ' + MS_DOUBT_BASE))

add(**MS2, section='the closing algorithm question',
    qtype='coding_find_peak',
    qtext='最後問演算法，find peak，相對簡單，先給了o(n) 問能更快嗎？',
    qtext_en=('Finally it asked an algorithm question, find peak, relatively simple; I first gave '
              'O(n) and it asked whether it could be faster.'),
    quote='最後問演算法，find peak，相對簡單，先給了o(n) 問能更快嗎？',
    answer='the candidate answered O(log n) via binary search, which the interviewer accepted',
    doubt=('"find peak" is a task name; whether the array was guaranteed to have no equal '
           'neighbours, and whether any peak or the global maximum was wanted, is unstated. The '
           'follow-up structure (give O(n), then be pushed for better) is the informative part. '
           'Note the candidate wrote their accepted answer as "BST O(ln(n))", which is a slip — '
           'binary search, not a binary search tree — so I have described it rather than quoted '
           'it. ' + MS_DOUBT_BASE))

MS3 = dict(mid='1072', date='2026-01-25', firm='Morgan Stanley', role='quant_researcher',
           level='unknown', cycle='2026', rnd='phone_technical',
           rname='Morgan Stanley additional interview with the fixed income strats team',
           poster=MS_POST, lang='mixed')

add(**MS3, section='the technical Q&A, focused on models, time series and data handling',
    qtype='statistics_high_dimensional_regression',
    qtext='What if your have large variable but small sample?',
    qtext_en='What if you have a large number of variables but a small sample?',
    quote='What if your have large variable but small sample?',
    answer=('the candidate offered PCA for dimensionality reduction, was pushed for another '
            'method, and hesitantly suggested F-test feature selection'),
    doubt=('A one-line prompt with no context about the modelling goal. The interviewer '
           'immediately followed with the reverse case, so this was a paired probe rather than a '
           'standalone problem. ' + MS_DOUBT_BASE))

add(**MS3, section='the technical Q&A, focused on models, time series and data handling',
    qtype='data_preprocessing_transformation',
    qtext=('Assume our input data has one part is normally distribute at zero (can be positive & '
           'negative) and the other part is strictly positive to very large number, what would you '
           'do before input it to our model ?'),
    qtext_en=('Assume our input data has one part that is normally distributed at zero (can be '
              'positive and negative) and another part that is strictly positive up to very large '
              'numbers — what would you do before feeding it into our model?'),
    quote=('Assume our input data has one part is normally distribute at zero (can be positive & '
           'negative) and the other part is strictly positive to very large number, what would you '
           'do before input it to our model ?'),
    answer=('the candidate said divide each value by the max; the interviewer replied "hmm yeah '
            'kinda"'),
    doubt=('This is the most fully specified question in the message and is answerable as written. '
           'The candidate\'s English is non-native and lightly ungrammatical, which is consistent '
           'with them typing out what they remembered hearing rather than copying a written '
           'prompt. ' + MS_DOUBT_BASE))

add(**MS3, section='the time-series portion, which the candidate says went badly',
    qtype='time_series_missing_data',
    qtext='Given time series data, what would you do for missing value ?',
    qtext_en='Given time series data, what would you do about missing values?',
    quote='Given time series data, what would you do for missing value ?',
    doubt=('Complete as an open prompt, though deliberately unconstrained — no series, no '
           'missingness mechanism, no downstream model. The candidate says this section went badly '
           'and that they cannot recall it exactly ("大致這樣確切不記得"), which is an explicit '
           'reliability warning attaching to this question and the next. ' + MS_DOUBT_BASE))

add(**MS3, section='the time-series portion, which the candidate says went badly',
    qtype='model_selection_metrics',
    qtext=('Which would you choose to estimate your time series model? R squared, MSE, RMSE, MAE?'),
    qtext_en=('Which would you choose to estimate your time series model: R squared, MSE, RMSE or '
              'MAE?'),
    quote=('Which would you choose to estimate your time series model? R squared, MSE, RMSE, MAE?'),
    doubt=('Complete, with the option set given. Carries the same explicit caveat as the previous '
           'item: the candidate wrote "大致這樣確切不記得" (roughly like this, I do not remember '
           'exactly) immediately after this section. ' + MS_DOUBT_BASE))

# ==================================================== 883 / 885: Kronos Research
KR_DOUBT = ('Kronos Research is a Taiwan-based quant firm and is not one of the named target '
            'firms. ' + NOATTR)

add('883', '2025-04-14', 'Kronos Research', 'quant_researcher', 'new_grad', '2025',
    'phone_technical',
    'Kronos Quantitative 第二關, second round — a single more senior interviewer',
    'the coding question that grew out of a probability question',
    'coding_next_permutation',
    ('因為我不確定 C++ 的 next_permutation 要怎麼 call，就問說能不能先寫一個樣子，結果面試官就說可以'
     '請我寫一個 next_permutation'),
    ('Because I was not sure how to call C++\'s next_permutation, I asked whether I could just '
     'write a placeholder for it; the interviewer said sure — and asked me to write a '
     'next_permutation.'),
    ('因為我不確定 C++ 的 next_permutation 要怎麼 call，就問說能不能先寫一個樣子，結果面試官就說可以'
     '請我寫一個 next_permutation'),
    CH + '. The message is a stage-by-stage account of interviewing at Kronos for Quantitative '
         'Researcher, by a final-year student who also describes the Optiver and WorldQuant '
         'processes in neighbouring messages',
    ('This question arose improvised, out of the candidate admitting they could not recall the '
     'library call — so it is genuinely a question that was asked, but it was not part of a '
     'prepared bank and would not recur. The original probability question it extended is not '
     'reproduced. The interviewer later let them substitute a DFS. ' + KR_DOUBT),
    lang='mixed')

add('885', '2025-04-14', 'Kronos Research', 'quant_developer', 'new_grad', '2025',
    'phone_technical',
    'Kronos infrastructure team, added round 1 of 2',
    'the whole of the first infra round',
    'coding_trading_system_implementation',
    '第一關是先問我怎麼實作一個簡單的交易系統',
    'The first round began by asking me how to implement a simple trading system.',
    '第一關是先問我怎麼實作一個簡單的交易系統',
    CH + '. The same author\'s account of an extra infrastructure-team loop that HR offered them '
         'after their researcher rounds; they describe the infra role as essentially backend '
         'engineering, building a virtual exchange interface for researchers',
    ('"How to implement a simple trading system" is as much of the prompt as is recorded — no '
     'requirements, no interface, no scope. The candidate says it was solvable with the C++ STL '
     'and that the interviewer prompted them when they made mistakes, which suggests a live coding '
     'exercise rather than a design discussion, but the problem statement itself is absent. ' +
     KR_DOUBT),
    lang='mixed')

add('885', '2025-04-14', 'Kronos Research', 'quant_developer', 'new_grad', '2025',
    'phone_technical',
    'Kronos infrastructure team, added round 2, with the infra team lead',
    'the C++ semantics questions',
    'language_cpp_copy_semantics',
    ('面試官會問一些比如說這個變數會不會被 copy，或是怎樣寫才不會被 copy，以及他們的好壞等等的'),
    ('The interviewer would ask things like whether this variable will be copied, or how to write '
     'it so that it will not be copied, and the pros and cons of each.'),
    ('面試官會問一些比如說這個變數會不會被 copy，或是怎樣寫才不會被 copy，以及他們的好壞等等的'),
    CH + '. The second infra round, which the author says focused on low-level C++ — how to write '
         'C++ so that it runs faster, and what behaviour a given way of writing it produces',
    ('The variable and the code under discussion are not shown, so the question is recorded at the '
     'level of "copy semantics were probed" rather than as a specific prompt. The author is '
     'reporting a pattern across the round ("會問一些比如說", would ask things like), not a single '
     'question. ' + KR_DOUBT),
    lang='mixed')

# ==================================================== verify + emit
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
        bad.append((mid, rec['firm'], rec['source_quote'][:70]))

for b in bad:
    sys.stderr.write(f'QUOTE NOT FOUND: {b}\n')

with open('raw/chat_and_archive.jsonl', 'a', encoding='utf-8') as f:
    for rec in ok:
        f.write(json.dumps({k: rec[k] for k in ORDER}, ensure_ascii=False) + '\n')
print(f'verified+written={len(ok)}  failed={len(bad)}')
