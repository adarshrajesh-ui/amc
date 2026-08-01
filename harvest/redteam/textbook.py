"""Local textbook-overlap matcher.

Corpora:
  * Green Book (Xinfeng Zhou) ch.2 Brain Teasers - 139 real problem statements
  * Brainstellar - 275 puzzles scraped live
  * Curated classic-problem signatures (Mosteller / Crack / Joshi / folklore)

Matching is signature-based (concept fingerprints), not string overlap, because
recall wording never matches book wording verbatim.
"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))

# (label, source, regex-signature). Signatures are deliberately conjunctive.
CLASSICS = [
 ("Bridge/torch crossing (4 people, 1/2/5/10 min)", "Green Book 2.2 (also Crack HotS)",
  r"(bridge|cross(ing)? (the )?(river|bridge))[\s\S]{0,140}(torch|flashlight|lamp)|4 people crossing bridge|four people[\s\S]{0,60}bridge"),
 ("Burning ropes / measure 45 min", "Green Book 2.2; Brainstellar",
  r"(rope|fuse|cord)s?[\s\S]{0,120}(burn|烧)[\s\S]{0,120}(hour|60 min|45|一小时|小时)"),
 ("100 prisoners & hats / colored hats", "Green Book 2.3; Brainstellar",
  r"(prisoner|囚犯)[\s\S]{0,120}(hat|帽子)|(hat|帽子)[\s\S]{0,80}(red|blue|black|white|红|蓝|黑|白)[\s\S]{0,120}(guess|猜)"),
 ("Pirates splitting 100 coins", "Green Book 2.3; Brainstellar",
  r"(pirate|海盗)[\s\S]{0,140}(coin|gold|金币|100)"),
 ("Poisoned wine / 1000 bottles, rats", "Green Book 2.3; Brainstellar",
  r"(1000|一千)\s*(bottle|瓶)[\s\S]{0,120}(poison|毒)|poison(ed)? (wine|bottle)[\s\S]{0,120}(rat|prisoner|mice|老鼠)"),
 ("Boys/girls birth-ratio (all-girls world)", "Green Book 2.3; Brainstellar",
  r"(stop having (children|kids)|until (they|she) (has|have) a (boy|girl))|all girls world|(boy|girl)[\s\S]{0,60}ratio[\s\S]{0,80}(country|kingdom|village)"),
 ("Monty Hall", "Mosteller-adjacent; Green Book 4.2",
  r"(monty hall)|(three|3) doors?[\s\S]{0,120}(goat|car)|(换门|三扇门)"),
 ("Birthday problem / shared birthday", "Mosteller #31; Green Book 4.1",
  r"birthday[\s\S]{0,120}(same|share|probability|至少两人)|(生日)[\s\S]{0,60}(相同|概率)"),
 ("Gambler's ruin / random walk to N", "Green Book 4.4; Crack HotS",
  r"gambler'?s ruin|(random walk)[\s\S]{0,100}(absorb|hit|reach)|(bet)[\s\S]{0,80}(until (you )?(reach|go broke|run out))"),
 ("Expected tosses for pattern HH vs HT", "Green Book 4.4; Brainstellar (Consecutive Heads)",
  r"(expected (number of )?(tosses|flips)|期望.{0,6}(次数|抛))[\s\S]{0,140}(HH|HT|THH|two (consecutive )?heads|consecutive heads|连续)"),
 ("Coupon collector", "Green Book 4.3; folklore",
  r"coupon collector|(collect|集齐)[\s\S]{0,100}(all (n|\d+) (coupons|toys|cards|stickers)|全部|所有.{0,4}(种|张))"),
 ("Broken stick / triangle from 3 pieces", "Mosteller #42; Brainstellar (Stick to Triangle)",
  r"(break|breaking|broken|折断|断成)[\s\S]{0,80}(stick|rod|棍|木棒)[\s\S]{0,120}(triangle|三角形)"),
 ("Drunk passenger / airplane seat", "Brainstellar (Drunk Passenger); Green Book 4.2",
  r"(drunk|first) passenger[\s\S]{0,140}(seat)|(100|一百)\s*passengers[\s\S]{0,140}seat|airplane seat(ing)? (problem|puzzle)"),
 ("Ants on a triangle/polygon collision", "Green Book 4.1; Brainstellar",
  r"ants?[\s\S]{0,100}(corner|vertex|triangle|square|polygon)[\s\S]{0,120}(collide|collision|meet)|蚂蚁[\s\S]{0,60}(碰|相遇)"),
 ("Two-envelope / envelope switching", "Crack HotS; Green Book 4.2",
  r"(two|2) envelopes?[\s\S]{0,140}(switch|swap|double|twice)"),
 ("Bayes: biased/two-headed coin picked at random", "Green Book 4.2; Crack HotS",
  r"(two[- ]headed|double[- ]headed|only heads|fair coin.{0,60}(biased|unfair)|3 (biased )?coins)[\s\S]{0,180}(probability|posterior|what is the (chance|prob))"),
 ("Expected value of a die roll with re-roll option", "Green Book 4.3; Brainstellar",
  r"(re-?roll|roll again|再[摇掷]|重[摇掷])[\s\S]{0,140}(expect|期望)|(expected value)[\s\S]{0,120}(option to (re-?roll|roll again))"),
 ("Chicken/cow/spider legs (linear Diophantine)", "classic school algebra (not a quant book)",
  r"(spider|蜘蛛)[\s\S]{0,100}(chicken|鸡)[\s\S]{0,100}(cow|牛)|legs?[\s\S]{0,60}(520|总共)[\s\S]{0,60}(leg|脚)"),
 ("Round-table seating constraint puzzle", "generic logic-grid puzzle (LSAT/GRE style)",
  r"(round table|圆桌|circular table)[\s\S]{0,200}(won'?t sit|不跟|not sit next to|refuses to sit)"),
 ("Lattice paths with no 3 consecutive same steps", "competition combinatorics (not a quant book)",
  r"(1 unit up|1 unit to the right|向上|向右)[\s\S]{0,200}(three steps in the same direction|连续三次|同方向连续)"),
 ("Balance-scale / weight of shapes", "primary-school algebra / puzzle books",
  r"(balance[sd]?|balanced)[\s\S]{0,120}(triangle|square|circle|shape)[\s\S]{0,80}(weigh|weight|pounds|lb)|(重量)[\s\S]{0,40}(三角形|方块)"),
 ("Two trains / river current relative speed", "classic algebra word problem (Crack HotS ch.2)",
  r"(upstream|downstream|逆流|顺流)[\s\S]{0,200}(current|speed|mph|miles)"),
 ("Uniform overlap probability (two random intervals)", "Green Book 4.2; Mosteller #35 (Meeting problem)",
  r"(uniformly at random)[\s\S]{0,200}(overlap|both (are )?in bloom|meet|同时)|(bloom)[\s\S]{0,180}(overlap|same time|both)"),
 ("Dice: EV of max / sum with re-roll", "Green Book 4.3; Brainstellar",
  r"(roll|throw|扔|掷)[\s\S]{0,60}(three|3|two|2|两|三)[\s\S]{0,40}(dice|骰子)[\s\S]{0,200}(earn|win|expected|收益|期望)"),
 ("Spinner / expected spins to see distinct regions", "coupon-collector variant",
  r"spinner[\s\S]{0,200}(expected number of spins)"),
 ("Card game: expected number of correct guesses", "Green Book 4.3 (card guessing); Mosteller",
  r"(deck|52|扑克)[\s\S]{0,200}(guess|choose|select|pick)[\s\S]{0,160}(expected|dollar|期望|块钱)"),
 ("Ballot problem / random walk stays positive", "Green Book 4.4; Mosteller #38",
  r"ballot problem|(votes?)[\s\S]{0,120}(always ahead|stays? ahead)"),
 ("St Petersburg / doubling bet", "Crack HotS; folklore",
  r"(double (your|the) bet|martingale)[\s\S]{0,140}(until (you )?win)"),
 ("Fair division / cake cutting", "Green Book 2.3",
  r"(cut the cake|cake cutting|divide the cake)[\s\S]{0,120}(fair|envy)"),
 ("Light switches / bulbs", "Brainstellar (Which Switch?); Green Book 2.3",
  r"(switch(es)?)[\s\S]{0,120}(bulb|light)[\s\S]{0,120}(room|which)"),
 ("Weighing balls to find the odd one", "Green Book 2.2; folklore",
  r"(\d+|twelve|eight|nine)\s*(balls|coins)[\s\S]{0,140}(balance|scale|weigh)[\s\S]{0,120}(heavier|lighter|odd|fake|counterfeit)"),
 ("Clock hands angle/overlap", "Crack HotS ch.2",
  r"(clock)[\s\S]{0,120}(hands?)[\s\S]{0,120}(overlap|angle|coincide|时针|分针)"),
 ("Fermi estimation (piano tuners / gas stations)", "Crack HotS ch.3 'Thinking Questions'",
  r"(how many)[\s\S]{0,80}(piano tuners|gas stations|golf balls|windows|ping[- ]pong balls|manholes)|(估计|預估)[\s\S]{0,60}(數量|数量)"),
 ("Optimal stopping / secretary problem", "Green Book 4.4; Brainstellar",
  r"(secretary problem)|(interview|见)[\s\S]{0,100}(candidates?)[\s\S]{0,140}(best|optimal stopping)"),
 ("Russian roulette / bullets in chamber", "Green Book 4.2; Brainstellar (Rolling the bullet)",
  r"(revolver|russian roulette|chamber)[\s\S]{0,140}(bullet|spin)"),
 ("Snake eyes / conditional dice paradox", "Green Book 4.2",
  r"(snake eyes)|(at least one (six|6))[\s\S]{0,120}(both|other)"),
 ("Random chord / Bertrand paradox", "Mosteller; Green Book 4.2",
  r"(random chord)|bertrand paradox"),
 ("Brownian motion / option pricing basics", "Joshi ch.2-3; Green Book ch.5-6",
  r"(black[- ]scholes|binomial (option )?pricing|delta hedg|implied volatility|put[- ]call parity)"),
 ("Matching problem / derangements", "Mosteller #10 (hats); Green Book 4.3",
  r"(derangement)|(hats?)[\s\S]{0,100}(random)[\s\S]{0,100}(none|no one) (gets|receives) (their|his) own|(letters?)[\s\S]{0,80}(envelopes?)[\s\S]{0,100}(random)"),
 ("Penney's game: HTH vs HHT stopping pattern", "Green Book 4.4; Brainstellar (Guess the Toss)",
  r"(HTH|HHT|THH|HHH|TTT)[\s\S]{0,80}(HTH|HHT|THH|HHH|TTT)|扔硬[幣币][\s\S]{0,40}(HTH|HHT)"),
 ("Umbrella / Markov chain between home and office", "Green Book 4.4 (classic Markov exercise)",
  r"(umbrella|雨伞|把[傘伞])[\s\S]{0,160}(office|办公室|home|家)|(N 把[傘伞])"),
 ("Knights and knaves truth-teller/liar", "Smullyan; Green Book 2.3",
  r"(knights?|knaves?)[\s\S]{0,120}(truth|lie)|(骑士|说谎者)[\s\S]{0,60}(真话|假话)|(one (always )?(tells the )?truth)[\s\S]{0,80}(one (always )?lies)"),
 ("Random chords dividing a circle into regions", "classic combinatorics (Green Book 2.1 / AoPS)",
  r"(chords?|lines?)[\s\S]{0,120}(circle|圆)[\s\S]{0,120}(regions?|pieces?|divide|分成|块)|圆[里内][\s\S]{0,20}随机画"),
 ("Waiting-for-the-bus / memoryless waiting time", "Green Book 4.3 (explicitly named by a candidate)",
  r"waiting for the bus|等(公交|巴士|车)|bus (arrival|waiting) (time|problem)"),
 ("Poisson rate rescaling (car on highway / shooting star)", "Green Book 4.2 problem 'Cars on a highway'",
  r"(probability of seeing|at least one)[\s\S]{0,90}(in (1 |one )?hour|in \d+ minutes)[\s\S]{0,140}(30 minutes|\d+ minutes|half)"),
 ("Two-people-meet-in-an-interval (uniform arrival)", "Green Book 4.2 'Meeting problem'; Mosteller",
  r"(each|both)[\s\S]{0,80}(independently|uniformly)[\s\S]{0,120}(random time|时间)[\s\S]{0,160}(wait|meet|等|见面)"),
 ("Painted-cube / Bayes on a die-like object", "Green Book 4.2; Brainstellar",
  r"(rubik|cube)[\s\S]{0,120}(painted|paint)[\s\S]{0,140}(probability|face)"),
 ("Markov two-state good-day/bad-day chain", "Green Book 4.4 (Markov chains)",
  r"(good|bad)\s*(day)[\s\S]{0,140}(chance|probability)[\s\S]{0,120}(next day)"),
 ("Chuck-a-luck / dice payout game", "Brainstellar (Chuck a Luck); Green Book 4.3",
  r"(roll|throw)[\s\S]{0,60}(three|3)[\s\S]{0,30}dice[\s\S]{0,160}(earn|pay|win)\s*\$?\d"),
 ("Sequential-selection card guessing (52-card deck)", "Green Book 4.3 'Card game'; Mosteller",
  r"(52|扑克牌)[\s\S]{0,200}(choose|select|pick|选择)[\s\S]{0,200}(dollar|块钱|expected)"),
 ("Average-of-three from 1..n", "classic olympiad counting",
  r"(three numbers|3 numbers)[\s\S]{0,80}(1 to \d+)[\s\S]{0,120}(average)"),
 ("Torpedo / repeated Bernoulli trials until success", "Brainstellar; Green Book 4.3",
  r"(torpedo|missile|shot)[\s\S]{0,140}(hits?)[\s\S]{0,120}(probability|1/\d)"),
 ("Betting to reach a target before ruin (bold play)", "Green Book 4.4 gambler's ruin / Dubins-Savage",
  r"(tokens?|chips?|dollars?)[\s\S]{0,120}(goal|reach)[\s\S]{0,60}(\d+)[\s\S]{0,120}(before running out|before you go broke|破产)"),
 ("Balls-in-urn / widgets from two factories (Bayes)", "Green Book 4.2 (classic urn Bayes)",
  r"(factory a|factory b|工厂)[\s\S]{0,200}(red|black|widget)[\s\S]{0,160}(probability)"),
 ("Consecutive-heads expected waiting time", "Green Book 4.4; Brainstellar (Consecutive Heads)",
  r"(expected)[\s\S]{0,100}(flips|tosses)[\s\S]{0,120}(consecutive|in a row|连续)"),
 ("25 horses, 5 lanes, find top 3", "Green Book 2.2 (named as a Green Book question by the candidate)",
  r"25 horses|25 匹马|twenty-?five horses"),
 ("Self-declared: candidate says the question is Green Book material", "Green Book (candidate's own attribution)",
  r"green ?book|\u7eff\u76ae\u4e66|\u7da0\u76ae\u66f8"),
]


def load_local():
    gb = []
    p = os.path.join(HERE, 'books', 'greenbook_problems.js')
    if os.path.exists(p):
        t = open(p, encoding='utf-8').read()
        for m in re.finditer(r'(?:question|problem|statement|body):\s*"((?:[^"\\]|\\.)*)"', t):
            s = m.group(1)
            if len(s) > 60:
                gb.append(s)
    bs = []
    p2 = os.path.join(HERE, 'brainstellar.json')
    if os.path.exists(p2):
        for o in json.load(open(p2)):
            bs.append((o['url'], o['text']))
    return gb, bs


def shingles(t, k=4):
    w = re.findall(r'[a-z0-9]+', (t or '').lower())
    return {' '.join(w[i:i + k]) for i in range(max(0, len(w) - k + 1))}


def match(text_en, text_raw=''):
    """Return list of (label, source, how)."""
    blob = ((text_en or '') + ' ' + (text_raw or ''))
    out = []
    for label, src, sig in CLASSICS:
        if re.search(sig, blob, re.I):
            out.append((label, src, 'signature'))
    return out


def ngram_hits(text_en, gb, bs, thresh=3):
    """Verbatim-ish overlap with the local Green Book / Brainstellar corpora."""
    s = shingles(text_en)
    if len(s) < 6:
        return []
    hits = []
    for g in gb:
        ov = s & shingles(g)
        if len(ov) >= thresh:
            hits.append(('GreenBook', len(ov), g[:140], sorted(ov)[:4]))
    for u, t in bs:
        ov = s & shingles(t)
        if len(ov) >= thresh:
            hits.append(('Brainstellar', len(ov), u, sorted(ov)[:4]))
    hits.sort(key=lambda h: -h[1])
    return hits[:4]
