#!/usr/bin/env python3
"""p10: nowcoder threads fetched directly (curl reaches nowcoder's SSR payload,
so these are access=full_text) — mostly Akuna Capital, which recruits in Shanghai
and is therefore the one Tier-A firm with real depth on nowcoder.
"""
import json
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "p10_nowcoder.jsonl")
rows = []


def add(**kw):
    rec = {
        "firm": None, "role_track": "unknown", "level": "unknown", "cycle": "unknown",
        "office": "unknown", "round": "unknown", "round_name": None, "platform": "unknown",
        "section_context": None, "question_type": "other", "question_text": None,
        "question_text_en": None, "reported_answer": None, "source_url": None,
        "source_type": "nowcoder", "source_quote": None, "source_language": "zh",
        "post_date": "unknown", "access": "full_text", "retrieval_method": "webfetch",
        "poster_context": None, "doubt": None,
    }
    rec.update(kw)
    for k in ("firm", "question_text", "source_url", "source_quote", "doubt"):
        assert rec[k], "missing %s" % k
    rows.append(rec)


NC_DOUBT = ("nowcoder posts are pseudonymous 面经 write-ups with no verification; the poster "
            "is recalling questions after the fact, so wording is theirs rather than the "
            "interviewer's.")

# =====================================================================================
# Akuna Capital — FPGA developer, 2020 校招, Shanghai. Original post by 毕业过过过.
# (A second nowcoder post, discuss/353148043191066624, reproduces this text with the
#  author's permission — "来自牛客网网友毕业过过过授权转发" — which is why the same
#  recall appears twice in the cache.)
# =====================================================================================
FPGA = "https://www.nowcoder.com/discuss/353155979133001728"
FPGA_CTX = ("毕业过过过, 北京邮电大学 芯片研发, posted 2019-12-18 15:59; 985本211硕 with a year and a "
            "half of FPGA work; interviewed 寒武纪 / akuna capital / 百度 / 华为 / 英伟达 / OPPO and "
            "was rejected by Akuna at the second round (二面挂)")
FPGA_SEC = ("这是个规模200人左右的跨国金融科技公司，做量化交易高频交易之类的，需要FPGA做加速。"
            "总部在芝加哥，上海有分部，其中只有六七个做FPGA的，笔试倒不难，但面试全程英语。")

add(firm="Akuna Capital", role_track="quant_developer", level="new_grad", cycle="2020",
    office="上海", round="phone_technical", round_name="一面是电话面",
    section_context="总共半小时，全程英语", question_type="other",
    question_text="还有最常见的FPGA面试题，比如单比特跨时钟，多比特跨时钟，异步FIFO结构，亚稳态，建立时间，保持时间什么的",
    question_text_en="Plus the most common FPGA interview questions — for example single-bit clock-domain crossing, multi-bit clock-domain crossing, asynchronous FIFO structure, metastability, setup time, hold time, and so on.",
    source_url=FPGA, source_quote="一面是电话面，问了下项目，还有最常见的FPGA面试题，比如单比特跨时钟，多比特跨时钟，异步FIFO结构，亚稳态，建立时间，保持时间什么的，我用英语勉强表达了出来，总共半小时。",
    source_language="zh", post_date="2019-12-18", poster_context=FPGA_CTX,
    doubt=NC_DOUBT + " This is a list of standing FPGA-interview topics ('最常见的FPGA面试题'), so the poster is naming a genre rather than reproducing what was asked; it is also a hardware role at Akuna's Shanghai office, not a quant-trading screen.")

add(firm="Akuna Capital", role_track="quant_developer", level="new_grad", cycle="2020",
    office="上海", round="phone_technical", round_name="二面用zoom远程面",
    section_context=FPGA_SEC, question_type="other",
    question_text="一上来就让搭电路，用二选一选择器搭与门，或门，非门，异或门",
    question_text_en="Right at the start they had me build circuits: use 2-to-1 multiplexers to build an AND gate, an OR gate, a NOT gate and an XOR gate.",
    source_url=FPGA, source_quote="二面用zoom远程面，一上来就让搭电路，用二选一选择器搭与门，或门，非门，异或门，花了我挺长时间。",
    source_language="zh", post_date="2019-12-18", poster_context=FPGA_CTX,
    doubt=NC_DOUBT + " Specific and plausible for an FPGA screen, but this is Akuna's Shanghai hardware track — it should not be read as evidence about Akuna's Chicago trader interviews.")

add(firm="Akuna Capital", role_track="quant_developer", level="new_grad", cycle="2020",
    office="上海", round="phone_technical", round_name="二面用zoom远程面",
    section_context=FPGA_SEC, question_type="other",
    question_text="然后又问怎样实现将一个数x乘以124倍最快最省资源",
    question_text_en="Then they asked how to multiply a number x by 124 in the fastest and most resource-efficient way.",
    reported_answer="我是说先向左移7位再减去左移2位，他问为什么，我没说出来 (the poster answered: shift left 7 then subtract shift left 2 — i.e. 128x - 4x — but could not explain why when pushed)",
    source_url=FPGA, source_quote="然后又问怎样实现将一个数x乘以124倍最快最省资源，我是说先向左移7位再减去左移2位，他问为",
    source_language="zh", post_date="2019-12-18", poster_context=FPGA_CTX,
    doubt=NC_DOUBT + " The one character after '他问为' renders as a mojibake box in the cached page, so my quote stops there; the poster's own answer is recorded but he says he failed the follow-up.")

# =====================================================================================
# Akuna Capital — C++ developer first round, Sept 2022. Two independent posters
# describe the same four questions; this record set points at the thread URL, which
# also carries the interviewer's actual code skeleton.
# =====================================================================================
CPP = "https://www.nowcoder.com/discuss/397714545857376256"
CPP_CTX = ("廿陆畵生, 上海交通大学 搜索算法, 发布于上海, posted 2022-09-20 16:39, thread titled "
           "'2022-09-09-akuna-cpp开发一面'; tagged #奥可纳Akuna# #23届秋招#. In a follow-up "
           "comment the poster adds 'akuna突然打电话来20分钟英语沟通了下'.")
CPP_SEC = "全英面试，但一上来就做题，四题完了后就反问然后结束；都是给了一些代码然后填充实现的"
CPP_DOUBT_BASE = (NC_DOUBT + " Corroborated by an independent nowcoder poster who lists the same "
                  "four questions for an 'akuna capital一面9.30（60min）' "
                  "(https://www.nowcoder.com/discuss/434715907903008768), which raises confidence "
                  "in the set; ")

add(firm="Akuna Capital", role_track="quant_developer", level="new_grad", cycle="2023届秋招",
    office="上海", round="phone_technical", round_name="akuna-cpp开发一面",
    section_context=CPP_SEC, question_type="coding_algorithms",
    question_text="求int里1的个数是否为奇数",
    question_text_en="Find whether the number of 1 bits in an int is odd.",
    source_url=CPP, source_quote="求int里1的个数是否为奇数 改错，求二叉树最大值（看成了二叉搜索树，写完后提示后再改的）",
    source_language="zh", post_date="2022-09-20", poster_context=CPP_CTX,
    doubt=CPP_DOUBT_BASE + "the poster's phrasing is compressed shorthand, so the exact prompt wording is lost.")

add(firm="Akuna Capital", role_track="quant_developer", level="new_grad", cycle="2023届秋招",
    office="上海", round="phone_technical", round_name="akuna-cpp开发一面",
    section_context=CPP_SEC, question_type="coding_algorithms",
    question_text="改错，求二叉树最大值（看成了二叉搜索树，写完后提示后再改的）",
    question_text_en="Fix the bug: find the maximum value of a binary tree (I mistook it for a binary search tree, and only corrected it after being prompted once I had finished).",
    source_url=CPP, source_quote="改错，求二叉树最大值（看成了二叉搜索树，写完后提示后再改的）",
    source_language="zh", post_date="2022-09-20", poster_context=CPP_CTX,
    doubt=CPP_DOUBT_BASE + "the parenthetical is the poster's own mistake, not part of the question.")

add(firm="Akuna Capital", role_track="quant_developer", level="new_grad", cycle="2023届秋招",
    office="上海", round="phone_technical", round_name="akuna-cpp开发一面",
    section_context=CPP_SEC, question_type="coding_algorithms",
    question_text="让修改账户balance值函数变成线程安全的（直接加了两个锁，伪代码）",
    question_text_en="Make the function that modifies an account balance thread-safe (I just added two locks, in pseudocode).",
    source_url=CPP, source_quote="让修改账户balance值函数变成线程安全的（直接加了两个锁，伪代码）",
    source_language="zh", post_date="2022-09-20", poster_context=CPP_CTX,
    doubt=CPP_DOUBT_BASE + "the second poster words this as '实现账户转账的多线程版本' (account transfer), so the two recollections differ on whether it was a balance update or a transfer.")

add(firm="Akuna Capital", role_track="quant_developer", level="new_grad", cycle="2023届秋招",
    office="上海", round="phone_technical", round_name="akuna-cpp开发一面",
    section_context=CPP_SEC, question_type="coding_algorithms",
    question_text="实现一个模板最小堆 都是给了一些代码然后填充实现的",
    question_text_en="Implement a templated min-heap. All of these gave you some code and asked you to fill in the implementation.",
    reported_answer="Poster pasted his filled-in PriorityQueue<T> back into the thread, beginning '// Complete the incomplete functions below as part of a Min Heap'.",
    source_url=CPP, source_quote="// Complete the incomplete functions below as part of a Min Heap",
    source_language="mixed", post_date="2022-09-20", poster_context=CPP_CTX,
    doubt=CPP_DOUBT_BASE + "my source_quote is the comment line from the skeleton the poster pasted back, which is the strongest verbatim artefact here but is the interviewer's code rather than the spoken question.")

# =====================================================================================
# Akuna Capital — quant OA, 春招 (spring recruiting) recall
# =====================================================================================
CHUN = "https://www.nowcoder.com/discuss/353154366230175744"
add(firm="Akuna Capital", role_track="quant_analyst", level="unknown", cycle="unknown",
    office="unknown", round="online_assessment", round_name="Akuna 量化（笔试挂）",
    question_type="coding_algorithms",
    question_text="又是全部是编程题，不擅长。。。一题没AC",
    question_text_en="Again it was all programming questions, which I'm not good at... I didn't AC a single one.",
    source_url=CHUN, source_quote="Akuna 量化（笔试挂）： 又是全部是编程题，不擅长。。。一题没AC",
    source_language="zh", post_date="2020-04", poster_context=(
        "Poster recapping a 春招 (spring) season across 网易游戏 / 头条 / 京东 / Paypal / Akuna / "
        "拼多多 / 携程 / 爱奇艺 / 招行信用卡, applying to 算法 and 数据分析 roles; the thread is "
        "tagged #春招# and the first comment is dated 2020-04-02"),
    doubt=NC_DOUBT + " The poster records only that Akuna's quant written test was entirely programming questions and that they solved none — no question content survives, so this attests format only.")

# =====================================================================================
# Akuna Capital — onsite question asked in 2016 (thread is a request for advice, and
# the only substantive reply is another candidate's failure at the phone screen)
# =====================================================================================
ONS = "https://www.nowcoder.com/discuss/353153964797534208"
add(firm="Akuna Capital", role_track="quant_developer", level="unknown", cycle="unknown",
    office="unknown", round="onsite", round_name="申的C++ Junior Dev，似乎要on-site了",
    question_type="other",
    question_text="申的C++ Junior Dev，似乎要on-site了，有人面过么？求点经验，感觉略虚，还是E文的。",
    question_text_en="I applied for C++ Junior Dev and it looks like I'm going to on-site. Has anyone interviewed? Looking for some experience — I feel a bit shaky, and it's in English too.",
    source_url=ONS, source_quote="申的C++ Junior Dev，似乎要on-site了，有人面过么？求点经验，感觉略虚，还是E文的。",
    source_language="zh", post_date="2016-10-25",
    poster_context="牛客862030号, 算法工程师, posted 2016-10-25 20:26; the one reply, from cnfuyu (华中科技大学), reads '恭喜楼主啊，电话面试一面就挂了，英语捉急😭'",
    doubt=NC_DOUBT + " This is a request for advice, not a recall — it contains no question. It is included only because it independently attests that Akuna ran an English-language C++ Junior Dev onsite for Chinese candidates in 2016, and that its phone screen was failing people on English.")


with open(OUT, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print("wrote %d -> %s" % (len(rows), OUT))
