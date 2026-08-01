#!/usr/bin/env python3
"""Repoint the three Akuna records that cite nowcoder's search-results page.

An earlier pass could only see those three write-ups through a rendered search
listing, so they were logged against https://www.nowcoder.com/search?... and had
to be downgraded to snippet_only: a search page is client-rendered, so a verifier
re-fetching it finds nothing.

Driving nowcoder's own search API (POST gw-c.nowcoder.com/api/sparta/pc/search)
returned the permalinks behind those three previews, and all three permalinks
fetch cleanly with curl. So each record can now point at the thread it actually
came from and be promoted back to full_text. The quotes below are re-copied from
the permalink bytes, not from the old search snippet.
"""
import json

PATH = "/workspace/harvest/raw/_tier_a_parts/p05_chinese.jsonl"

# old question_text prefix -> (permalink, replacement quote, poster, date)
REPOINT = {
    "第一题 求一个数的奇偶校验位": (
        "https://www.nowcoder.com/feed/main/detail/5363d0b8413448fdb1a2e0c48379aee8",
        "第一题 求一个数的奇偶校验位\n第二题 求二叉树节点最大值\n第三题 给一个函数，要求修改成线程安全的\n第四题 手写priority_queue（构造，析构，push,top,pop）",
        "nowcoder user wngynng, 浙江大学 算法工程师, posting under the #奥可纳Akuna# tag",
        "2022-08-03",
    ),
    "求int里1的个数是否为奇数 改错": (
        "https://www.nowcoder.com/discuss/397714545857376256",
        "全英面试，但一上来就做题，四题完了后就反问然后结束",
        "nowcoder user posting '2022-09-09-akuna-cpp开发一面'",
        "2022-09-09",
    ),
    "10选择必须20分钟": (
        "https://www.nowcoder.com/discuss/396088849078685696",
        "10选择必须20分钟，记了3题\n英语题打起来不用频繁切换中英文了\n6选择+2编程26min，这块选择没什么好记的",
        "nowcoder user 廿陆畵生, 上海交通大学 搜索算法, posting '2022-09-04-AkunaCapital笔试46min' from 上海",
        "2022-09-04",
    ),
}

NOTE = ("Recovered permalink: this record originally cited nowcoder's client-rendered search "
        "page and was marked snippet_only for that reason. Driving nowcoder's search API "
        "surfaced the underlying thread, which curl fetches in full, so the URL now resolves "
        "and the quote is machine-checkable. ")

out, hits = [], 0
for line in open(PATH, encoding="utf-8"):
    line = line.strip()
    if not line:
        continue
    o = json.loads(line)
    if "nowcoder.com/search" in o.get("source_url", ""):
        for prefix, (url, quote, poster, date) in REPOINT.items():
            if (o["question_text"] or "").startswith(prefix):
                o["source_url"] = url
                o["source_quote"] = quote
                o["access"] = "full_text"
                o["retrieval_method"] = "webfetch"
                o["post_date"] = date
                o["poster_context"] = poster
                d = o.get("doubt") or ""
                # drop the stale provenance complaint, it no longer applies
                d = d.split("PROVENANCE WEAKNESS")[0].rstrip()
                o["doubt"] = NOTE + d
                hits += 1
                break
        else:
            print("UNMATCHED:", (o["question_text"] or "")[:60])
    out.append(json.dumps(o, ensure_ascii=False))

open(PATH, "w", encoding="utf-8").write("\n".join(out) + "\n")
print("repointed %d records" % hits)
