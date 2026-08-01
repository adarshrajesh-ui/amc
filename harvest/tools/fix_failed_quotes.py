#!/usr/bin/env python3
"""Repair the three source_quotes that failed re-verification against the live page.

Two Taro quotes were stitched together by an earlier widening pass ("1. Detect
collinearity 2. Parse words 3. Market equilibrium") but the page lists the three items
as separate lines under a "Questions" heading, so the numbered form never existed.
One nowcoder quote dropped a space the page actually has ("\u4e9a\u7a33\u6001\uff0c \u5efa\u7acb\u65f6\u95f4").

Replacements below are copied from the cached page bytes, not retyped.
"""
import glob
import json
import os

FIX = {
    "1. Detect collinearity 2. Parse words 3. Market equilibrium":
        "Questions\n\nDetect collinearity\n\nParse words\n\nMarket equilibrium",
    ("\u4e00\u9762\u662f\u7535\u8bdd\u9762\uff0c\u95ee\u4e86\u4e0b\u9879\u76ee\uff0c\u8fd8\u6709\u6700"
     "\u5e38\u89c1\u7684FPGA\u9762\u8bd5\u9898\uff0c\u6bd4\u5982\u5355\u6bd4\u7279\u8de8\u65f6\u949f\uff0c"
     "\u591a\u6bd4\u7279\u8de8\u65f6\u949f\uff0c\u5f02\u6b65FIFO\u7ed3\u6784\uff0c\u4e9a\u7a33\u6001\uff0c"
     "\u5efa\u7acb\u65f6\u95f4\uff0c\u4fdd\u6301\u65f6\u95f4\u4ec0\u4e48\u7684\uff0c\u6211\u7528\u82f1"
     "\u8bed\u52c9\u5f3a\u8868\u8fbe\u4e86\u51fa\u6765\uff0c\u603b\u5171\u534a\u5c0f\u65f6\u3002"):
        ("\u4e00\u9762\u662f\u7535\u8bdd\u9762\uff0c\u95ee\u4e86\u4e0b\u9879\u76ee\uff0c\u8fd8\u6709\u6700"
         "\u5e38\u89c1\u7684FPGA\u9762\u8bd5\u9898\uff0c\u6bd4\u5982\u5355\u6bd4\u7279\u8de8\u65f6\u949f\uff0c"
         "\u591a\u6bd4\u7279\u8de8\u65f6\u949f\uff0c\u5f02\u6b65FIFO\u7ed3\u6784\uff0c\u4e9a\u7a33\u6001\uff0c "
         "\u5efa\u7acb\u65f6\u95f4\uff0c\u4fdd\u6301\u65f6\u95f4\u4ec0\u4e48\u7684\uff0c\u6211\u7528\u82f1"
         "\u8bed\u52c9\u5f3a\u8868\u8fbe\u4e86\u51fa\u6765\uff0c\u603b\u5171\u534a\u5c0f\u65f6\u3002"),
}

total = 0
for path in sorted(glob.glob("/workspace/harvest/raw/_tier_a_parts/p*.jsonl")):
    out, changed = [], 0
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line:
            continue
        o = json.loads(line)
        new = FIX.get(o.get("source_quote"))
        if new:
            o["source_quote"] = new
            changed += 1
        out.append(json.dumps(o, ensure_ascii=False))
    if changed:
        open(path, "w", encoding="utf-8").write("\n".join(out) + "\n")
        print("%s: fixed %d" % (os.path.basename(path), changed))
        total += changed
print("total %d" % total)
