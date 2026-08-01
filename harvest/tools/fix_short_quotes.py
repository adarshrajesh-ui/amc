#!/usr/bin/env python3
"""Widen four source_quotes that were shorter than the 20-character floor.

Each replacement is the surrounding contiguous run from the same cached page, so the
quote stays verbatim — it just carries its neighbouring list items with it.
"""
import json
import os

PARTS = "/workspace/harvest/raw/_tier_a_parts"

FIX = {
    ("p05_chinese.jsonl", "第二题：递归实现求二叉树中的最大值"):
        "第二题：递归实现求二叉树中的最大值 第三题：实现账户转账的多线程版本，保证线程安全,可用伪代码",
    ("p07_taro.jsonl", "Detect collinearity"):
        "1. Detect collinearity 2. Parse words 3. Market equilibrium",
    ("p07_taro.jsonl", "Market equilibrium"):
        "1. Detect collinearity 2. Parse words 3. Market equilibrium",
    ("p07_taro.jsonl", "bowling scorecard"):
        "Right side of binary tree, below binary tree, bowling scorecard",
}

for fname in sorted({k[0] for k in FIX}):
    path = os.path.join(PARTS, fname)
    out, n = [], 0
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line:
            continue
        o = json.loads(line)
        new = FIX.get((fname, o.get("source_quote")))
        if new:
            o["source_quote"] = new
            n += 1
        out.append(json.dumps(o, ensure_ascii=False))
    open(path, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("%s: widened %d quotes" % (fname, n))
