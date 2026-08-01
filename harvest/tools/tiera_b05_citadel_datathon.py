#!/usr/bin/env python3
"""Citadel Datathon OA (2024-03-30), 17 multiple-choice items from a CSDN write-up.

The question stems and option lists are sliced straight out of the archived page text
rather than retyped, so every `source_quote` is a byte-exact substring of what the
verifier will re-fetch. Hand-copying CJK-adjacent English with escaped underscores and
full-width punctuation is exactly where paraphrase creeps in.

blog.csdn.net answers plain HTTP clients with 521, so the text comes from the Wayback
snapshot; the verifier's own wayback strategy reaches the same bytes.
"""
import html
import re
import sys
import urllib.request

sys.path.insert(0, "/workspace/harvest/tools")
import tiera_lib

URL = "https://blog.csdn.net/dcdsc/article/details/139953481"
SNAP = "https://web.archive.org/web/20251104194117/" + URL


def page_text():
    req = urllib.request.Request(SNAP, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=90) as r:
        raw = r.read().decode("utf-8", "replace")
    raw = re.sub(r"(?is)<(script|style|noscript|svg)\b[^>]*>.*?</\1>", " ", raw)
    raw = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</li>|</tr>", "\n", raw)
    t = html.unescape(re.sub(r"<[^>]+>", " ", raw))
    t = re.sub(r"[ \t\xa0]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return t


TXT = page_text()

# Blocks run from one 题目N heading to the next; the last one ends at the sign-off.
# The date in the title ("Citadel datathon OA题目20240330") matches the same shape, so
# only headings numbered within the actual run are kept.
starts = [(int(m.group(1)), m.end()) for m in re.finditer(r"题目(\d+)\s*\n", TXT)
          if 1 <= int(m.group(1)) <= 30]
end_all = TXT.find("其他思路或想法欢迎在留言区交流补充")
blocks = {}
for i, (num, s) in enumerate(starts):
    e = starts[i + 1][1] - len(f" 题目{starts[i + 1][0]} \n") if i + 1 < len(starts) else end_all
    e = starts[i + 1][1] if i + 1 < len(starts) else end_all
    body = TXT[s:e]
    body = re.sub(r"\s*题目\d+\s*$", "", body).strip()
    blocks[num] = body

assert len(blocks) == 17, sorted(blocks)


def split(num):
    """Return (stem+options, reported answer letter or None) for one item."""
    b = blocks[num]
    m = re.search(r"【参考答案】\s*([A-E])", b)
    ans = m.group(1) if m else None
    q = b[: m.start()].strip() if m else b.strip()
    return q, ans


# Per-item labelling. Everything else on the record is shared, because all 17 items come
# from the same sitting of the same test.
TYPES = {
    1: "coding_algorithms", 2: "coding_algorithms", 3: "coding_algorithms",
    4: "ml_modeling", 5: "probability", 6: "ml_modeling", 7: "ml_modeling",
    8: "ml_modeling", 9: "statistics_regression", 10: "probability",
    11: "probability", 12: "other", 13: "statistics_regression", 14: "other",
    15: "ml_modeling", 16: "probability", 17: "logic_brainteaser",
}

INTRO = ("申请完Datathon后就会发OA，时间60min 15道选择题，题目相较以往有一些变化，但是不多，"
         "整体不算难，以数理统计、机器学习和python编程为主，下面给个汇总版。")

POSTER = ("CSDN blog '量化投资和人工智能' (blog.csdn.net/dcdsc), a WeChat-public-account "
          "operator who republishes 笔试 recalls submitted by readers ('欢迎同学们在 公众号后台 "
          "留言投稿'); the post is titled 最新！Citadel datathon OA题目20240330 and says the OA "
          "arrives after applying to the Datathon.")

DOUBT = ("Compilation, not a first-person recall: the blogger aggregates reader-submitted "
         "笔试 and solicits submissions with a cash/奶茶 reward and a paid 知识星球, so the "
         "item list is second-hand and could have been padded from a question bank; the "
         "intro also says 15 questions while 17 are listed, which means at least the count "
         "is unreliable.")

recs = []
for num in sorted(blocks):
    q, ans = split(num)
    recs.append({
        "firm": "Citadel",
        "role_track": "unknown",
        "level": "unknown",
        "cycle": "2024",
        "office": "unknown",
        "round": "datathon",
        "round_name": "Datathon OA",
        "platform": "unknown",
        "section_context": "60min 15道选择题 (60 minutes, multiple choice; 17 items are actually listed)",
        "question_type": TYPES[num],
        "question_text": q,
        "question_text_en": None,
        "reported_answer": (f"【参考答案】{ans}" if ans else None),
        "source_url": URL,
        "source_type": "blog",
        "source_quote": q,
        "source_language": "mixed",
        "post_date": "2024-06-25",
        "access": "full_text",
        "retrieval_method": "webfetch",
        "poster_context": POSTER,
        "doubt": DOUBT,
    })

# One extra record is not a question: keep the framing sentence out of the corpus but
# assert it was read, so the section_context above is traceable.
assert INTRO in TXT

tiera_lib.write(recs)
