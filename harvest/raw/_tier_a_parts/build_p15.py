#!/usr/bin/env python3
"""p15: nowcoder threads reached by driving the site's own search API.

nowcoder.com/search is client-rendered, so earlier passes could only open
permalinks that some other source had already named. POSTing to
gw-c.nowcoder.com/api/sparta/pc/search returns the same result set as JSON,
which turned up threads no prior pass had seen — most importantly a dated HRT
FPGA-intern write-up that reproduces a whole one-hour phone screen.

Every permalink here fetches with plain curl and every source_quote below was
copied out of those bytes via pagetext.py, not retyped.
"""
import json
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "p15_nowcoder_api.jsonl")
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
        assert rec[k], "missing %s in %r" % (k, rec.get("question_text"))
    assert len(rec["source_quote"]) >= 20, "short quote: %r" % rec["source_quote"]
    rows.append(rec)


# ------------------------------------------------------------------------- HRT
# 小甜豆, 重庆邮电大学 FPGA工程师, 2022-12-13, "HRT---FPGA 实习生面经".
# A single dated write-up of one take-home plus one hour-long phone screen. The
# poster warns the recall may be incomplete ("下面是我记得的问题，可能会有不全").
HRT = "https://www.nowcoder.com/discuss/432302178204741632"
HRT_POSTER = ("nowcoder user 小甜豆, 重庆邮电大学, self-described FPGA工程师 posting from 重庆; "
              "write-up titled 'HRT---FPGA 实习生面经' (HRT FPGA intern interview experience)")
HRT_DOUBT = ("Self-reported and reconstructed from memory a while after the fact — the poster "
             "says outright '下面是我记得的问题，可能会有不全' (these are the questions I remember, "
             "there may be gaps), and describes the pace as 快问快答, so individual wordings are "
             "the poster's paraphrase rather than the interviewer's. ")

add(firm="Hudson River Trading", role_track="quant_developer", level="internship",
    office="unknown", round="take_home", round_name="第一轮Take Home Test",
    section_context="用6个小时写一个2-stage pipeline的ALU，自己写案例",
    question_type="coding_algorithms",
    question_text="用6个小时写一个2-stage pipeline的ALU，自己写案例，它规定了自我介绍的格式，规定要包含多少个记录。",
    question_text_en=("Spend six hours writing a 2-stage pipeline ALU and write your own test "
                      "cases; they specified the format of the write-up and how many records it "
                      "had to contain."),
    reported_answer=("因为要用linux下的iverilog和gtkwave，我琢磨了一下用virtual box装的ubuntu。"
                     "写完ALU用他提供的test测试，我还写了个python script生成一些随机的指令进行测试，"
                     "同时也用python写了个funcional model做direct test。"),
    source_url=HRT,
    source_quote="投简历之后两周收到第一轮Take Home Test: 用6个小时写一个2-stage pipeline的ALU，自己写案例，它规定了自我介绍的格式，规定要包含多少个记录。",
    post_date="2022-12-13", poster_context=HRT_POSTER,
    doubt=HRT_DOUBT + "This is the one item the poster clearly did rather than recalled, so it is the strongest line in the post.")

HRT_PHONE = dict(
    firm="Hudson River Trading", role_track="quant_developer", level="internship",
    office="unknown", round="phone_technical",
    round_name="电面，不开摄像头，分为软件硬件两部分，全程没聊简历和背景，时长一个小时",
    source_url=HRT, post_date="2022-12-13", poster_context=HRT_POSTER)

SW = "软件部分（一小时电面的前半段）"
HW = "硬件部分（一小时电面的后半段）"

# Software half. Quotes are contiguous windows of the run-on list, each wide
# enough to clear the 20-character floor.
for qt, qen, quote, typ in [
    ("big endian 和 little endian的区别。",
     "The difference between big endian and little endian.",
     "软件部分：big endian 和 little endian的区别。Stack和Heap的区别。", "other"),
    ("Stack和Heap的区别。",
     "The difference between stack and heap.",
     "big endian 和 little endian的区别。Stack和Heap的区别。Compiler和interpreter的区别。", "other"),
    ("Compiler和interpreter的区别。",
     "The difference between a compiler and an interpreter.",
     "Stack和Heap的区别。Compiler和interpreter的区别。什么时候用stack什么时候用heap", "other"),
    ("什么时候用stack什么时候用heap，它们的区别是什么。",
     "When do you use the stack and when do you use the heap, and what is the difference?",
     "Compiler和interpreter的区别。什么时候用stack什么时候用heap，它们的区别是什么。", "other"),
    ("指针是什么，不当使用指针会有什么后果。",
     "What is a pointer, and what are the consequences of using pointers improperly?",
     "什么时候用stack什么时候用heap，它们的区别是什么。指针是什么，不当使用指针会有什么后果。", "other"),
    ("Thread和process的区别。",
     "The difference between a thread and a process.",
     "指针是什么，不当使用指针会有什么后果。Thread和process的区别。什么是OS。", "other"),
    ("什么是OS。",
     "What is an operating system?",
     "Thread和process的区别。什么是OS。Pipeline有什么好处，有什么问题。", "other"),
    ("Pipeline有什么好处，有什么问题。",
     "What are the benefits of pipelining, and what problems does it bring?",
     "什么是OS。Pipeline有什么好处，有什么问题。有哪几种pipeline hazard，怎么解决？", "other"),
    ("有哪几种pipeline hazard，怎么解决？",
     "What kinds of pipeline hazard are there, and how do you resolve them?",
     "Pipeline有什么好处，有什么问题。有哪几种pipeline hazard，怎么解决？什么是Cache，为什么要有cache。", "other"),
    ("什么是Cache，为什么要有cache。",
     "What is a cache, and why do we need caches?",
     "有哪几种pipeline hazard，怎么解决？什么是Cache，为什么要有cache。", "other"),
    ("set associative和direct map cache有什么区别。",
     "What is the difference between a set-associative and a direct-mapped cache?",
     "什么是Cache，为什么要有cache。set associative和direct map cache有什么区别。", "other"),
    ("Branch prediction有哪几种？",
     "What kinds of branch prediction are there?",
     "set associative和direct map cache有什么区别。Branch prediction有哪几种？", "other"),
    ("Register renaming你知道哪几种？",
     "What kinds of register renaming do you know?",
     "Branch prediction有哪几种？Register renaming你知道哪几种？", "other"),
    ("怎么用汇编语言实现OOP，object在内存中是怎么存储的。",
     "How would you implement OOP in assembly language, and how is an object stored in memory?",
     "Register renaming你知道哪几种？怎么用汇编语言实现OOP", "other"),
    ("怎么用C实现OOP。",
     "How would you implement OOP in C?",
     "object在内存中是怎么存储的。怎么用C实现OOP。RISC和CISC的区别。", "other"),
    ("RISC和CISC的区别。",
     "The difference between RISC and CISC.",
     "怎么用C实现OOP。RISC和CISC的区别。", "other"),
]:
    add(question_text=qt, question_text_en=qen, source_quote=quote, question_type=typ,
        section_context=SW, doubt=HRT_DOUBT +
        "Listed as one item in a run-on sequence of remembered questions, so the exact phrasing is the poster's.",
        **HRT_PHONE)

for qt, qen, quote in [
    ("FPGA里面有什么资源，他们分别都是怎么实现的，他们的作用都是什么。",
     "What resources are there inside an FPGA, how is each one implemented, and what is each one for?",
     "硬件部分：FPGA里面有什么资源，他们分别都是怎么实现的，他们的作用都是什么。"),
    ("比如实现某种逻辑，需要多少LUT。",
     "For example, to implement some given logic, how many LUTs would it take?",
     "他们的作用都是什么。比如实现某种逻辑，需要多少LUT。写逻辑表达式"),
    ("写逻辑表达式，跨时钟域有哪几种解决方法。",
     "Write the logic expression; what methods are there for handling clock-domain crossing?",
     "比如实现某种逻辑，需要多少LUT。写逻辑表达式，跨时钟域有哪几种解决方法。"),
    ("同步FIFO读指针写指针，空满信号的生成逻辑。",
     "The read and write pointers of a synchronous FIFO, and the logic that generates the empty and full flags.",
     "跨时钟域有哪几种解决方法。同步FIFO读指针写指针，空满信号的生成逻辑。"),
    ("synthesis和implementation都有哪些步骤，他们会生成什么。",
     "What steps do synthesis and implementation each consist of, and what do they generate?",
     "同步FIFO读指针写指针，空满信号的生成逻辑。synthesis和implementation都有哪些步骤，他们会生成什么。"),
    ("时序综合报告怎么看。",
     "How do you read a timing synthesis report?",
     "synthesis和implementation都有哪些步骤，他们会生成什么。时序综合报告怎么看。"),
    ("建立保持时间都是什么，怎么解决不正常的建立保持时间。",
     "What are setup and hold time, and how do you fix setup/hold violations?",
     "时序综合报告怎么看。建立保持时间都是什么，怎么解决不正常的建立保持时间。"),
    ("Verification有几种test的方法。",
     "How many kinds of test method are there in verification?",
     "怎么解决不正常的建立保持时间。Verification有几种test的方法。UVM是什么。"),
    ("UVM是什么。",
     "What is UVM?",
     "Verification有几种test的方法。UVM是什么。"),
]:
    add(question_text=qt, question_text_en=qen, source_quote=quote,
        question_type="other", section_context=HW, doubt=HRT_DOUBT +
        "Listed as one item in a run-on sequence of remembered questions, so the exact phrasing is the poster's.",
        **HRT_PHONE)

# ---------------------------------------------------------------- Akuna 笔试
AK_OA = "https://www.nowcoder.com/discuss/396088849078685696"
AK_OA_POSTER = ("nowcoder user 廿陆畵生, 上海交通大学, 搜索算法 track, posting from 上海 under "
                "#奥可纳Akuna# #笔试# #23届秋招笔面经#; title dates the sitting to 2022-09-04")
AK_OA_DOUBT = ("The poster reconstructed the questions as C++ solution code after the fact rather "
               "than copying the prompts off the test screen, so the wording of each problem is "
               "their own summary; they also say plainly '记了3题' and '这块选择没什么好记的', "
               "i.e. the multiple-choice content is not recorded at all. ")

add(firm="Akuna Capital", role_track="quant_developer", level="unknown", cycle="2023",
    office="unknown", round="online_assessment", round_name="AkunaCapital笔试46min",
    section_context="10选择必须20分钟；6选择+2编程26min",
    question_type="coding_algorithms",
    question_text="// 1. 检查二叉搜索树中是否包含某个值 // 只需要实现in",
    question_text_en="1. Check whether a binary search tree contains a given value. You only need to implement `in`.",
    reported_answer=("int in(node* root, int val){\nwhile(root){\nif(root->val==val)return true;\n"
                     "else if(root->val<val) root=root->right;\nelse root=root->left;\n}\nreturn false;\n}"),
    source_url=AK_OA,
    source_quote="// 1. 检查二叉搜索树中是否包含某个值\n// 只需要实现in",
    post_date="2022-09-04", poster_context=AK_OA_POSTER, doubt=AK_OA_DOUBT)

add(firm="Akuna Capital", role_track="quant_developer", level="unknown", cycle="2023",
    office="unknown", round="online_assessment", round_name="AkunaCapital笔试46min",
    section_context="10选择必须20分钟；6选择+2编程26min",
    question_type="coding_algorithms",
    question_text="// 2. 求不超过某上限的最大连续子数组和",
    question_text_en="2. Find the largest sum of a contiguous subarray that does not exceed a given upper bound.",
    reported_answer=("unsigned f(unsigned n, unsigned b, unsigned p[]) {\nunsigned rb=0, maxrb=0;\n"
                     "for(int i=0,j=0;i<n;i++){\nrb+=p[i];\nwhile(j<=i&&rb>b) rb-=p[j++];\n"
                     "if(maxrb<rb) maxrb=rb;\n}\nreturn maxrb;\n}"),
    source_url=AK_OA,
    source_quote="// 2. 求不超过某上限的最大连续子数组和\nunsigned f(unsigned n, unsigned b, unsigned p[]) {",
    post_date="2022-09-04", poster_context=AK_OA_POSTER, doubt=AK_OA_DOUBT)

add(firm="Akuna Capital", role_track="quant_developer", level="unknown", cycle="2023",
    office="unknown", round="online_assessment", round_name="AkunaCapital笔试46min",
    section_context="6选择+2编程26min", question_type="other",
    question_text="Unit testing.",
    question_text_en="Unit testing.",
    source_url=AK_OA,
    source_quote="6选择+2编程26min，这块选择没什么好记的\nUnit testing.",
    post_date="2022-09-04", poster_context=AK_OA_POSTER,
    doubt=AK_OA_DOUBT + "This one is only a two-word topic label, not a question.")

# ------------------------------------------------------------ Akuna 一面 (2022-08)
AK_P = "https://www.nowcoder.com/feed/main/detail/5363d0b8413448fdb1a2e0c48379aee8"
AK_P_POSTER = "nowcoder user wngynng, 浙江大学, 算法工程师 track, posting under #奥可纳Akuna#"
AK_P_DOUBT = ("Short bulleted recall with no problem statements — each line names a task in a "
              "handful of characters. A commenter on the same post replies '都是典型的题啊' "
              "(these are all standard questions), which is consistent with, but not proof of, "
              "the recall being accurate. ")

for qt, qen, quote, typ in [
    ("第一题 求一个数的奇偶校验位", "Question 1: compute the parity bit of a number.",
     "直接做题 没有自我介绍\n第一题 求一个数的奇偶校验位", "coding_algorithms"),
    ("第二题 求二叉树节点最大值", "Question 2: find the maximum node value in a binary tree.",
     "第一题 求一个数的奇偶校验位\n第二题 求二叉树节点最大值", "coding_algorithms"),
    ("第三题 给一个函数，要求修改成线程安全的",
     "Question 3: given a function, modify it to be thread-safe.",
     "第二题 求二叉树节点最大值\n第三题 给一个函数，要求修改成线程安全的", "coding_algorithms"),
    ("第四题 手写priority_queue（构造，析构，push,top,pop）",
     "Question 4: hand-write a priority_queue (constructor, destructor, push, top, pop).",
     "第三题 给一个函数，要求修改成线程安全的\n第四题 手写priority_queue（构造，析构，push,top,pop）",
     "coding_algorithms"),
]:
    add(firm="Akuna Capital", role_track="quant_developer", level="unknown",
        office="unknown", round="phone_technical", round_name="akuna一面",
        section_context="直接做题 没有自我介绍，四题，做完题反问",
        question_type=typ, question_text=qt, question_text_en=qen,
        source_url=AK_P, source_quote=quote, post_date="2022-08-03",
        poster_context=AK_P_POSTER, doubt=AK_P_DOUBT)

# ------------------------------------------------------------------ Jump OA
JP = "https://www.nowcoder.com/feed/main/detail/0756d4d7b35848dea1fe94ca310dd663"
add(firm="Jump Trading", role_track="quant_developer", level="internship",
    office="unknown", round="online_assessment", round_name="oa",
    section_context="三个题", question_type="coding_algorithms",
    question_text="三个题不考算法，纯考写业务逻辑，最后十秒改了个bug把样例过了",
    question_text_en=("Three questions, none of them algorithmic — purely about writing business "
                      "logic. With ten seconds left I fixed a bug and got the sample to pass."),
    source_url=JP,
    source_quote="有无同学投了jump trading实习？我今天刚做完oa\n\n三个题不考算法，纯考写业务逻辑，最后十秒改了个bug把样例过了",
    post_date="2024-04-04",
    poster_context=("nowcoder user 感谢信收割机666, Java track, posting the same day they sat the "
                    "OA ('我今天刚做完oa'); edited 2024-04-04 to add '收到约面的邮件了'"),
    doubt=("Same-day and therefore fresh, but purely topic-level: the poster characterises the "
           "three questions as business-logic rather than algorithmic and never says what any of "
           "them asked, so no question content survives."))

add(firm="Jump Trading", role_track="quant_developer", level="internship",
    office="unknown", round="phone_technical", round_name="1面是hr面",
    question_type="other",
    question_text="1面是hr面, 貌似不难拿. 2面tech面刷人比较多",
    question_text_en=("Round 1 is an HR interview, which does not seem hard to get. Round 2 is the "
                      "technical interview and cuts a lot of people."),
    source_url=JP, source_quote="1面是hr面, 貌似不难拿. 2面tech面刷人比较多",
    post_date="2024-03-31",
    poster_context=("commenter 牛客111514817号, 东南大学 算法工程师, replying from 北京 to the OP's "
                    "Jump Trading intern OA post"),
    doubt=("Process description, not a question, and the commenter hedges with 貌似 ('seems'), so "
           "they may be relaying hearsay rather than their own loop."))

# ----------------------------------------------------- Akuna all-English screen
AK_CPP = "https://www.nowcoder.com/discuss/353153972942872576"
add(firm="Akuna Capital", role_track="quant_developer", level="unknown",
    office="unknown", round="phone_technical", round_name="akuna capital【1面跪，全程英文】",
    question_type="other",
    question_text="自我介绍。可以去一亩三分地论坛上搜akuna的面经，基本都是类似的那种问题，反正全都是概念。",
    question_text_en=("Introduce yourself. You can search 1point3acres for Akuna interview "
                      "write-ups — they are basically all the same sort of question, all concepts."),
    source_url=AK_CPP,
    source_quote="akuna capital【1面跪，全程英文】\n\n自我介绍。",
    post_date="unknown",
    poster_context=("nowcoder poster of '运气流选手的秋招C++面经总结', a C++ autumn-recruiting "
                    "round-up; says of this round '三种情况：1听不懂，2听懂了不会，3会但不知道英语怎么讲'"),
    doubt=("Topic-level only: the poster names no question beyond 自我介绍 and explicitly redirects "
           "readers to another forum for the content, so this attests the round's character "
           "(all-English, all conceptual) rather than any specific question."))

with open(OUT, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print("wrote %d -> %s" % (len(rows), OUT))
