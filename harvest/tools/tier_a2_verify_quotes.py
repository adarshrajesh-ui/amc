#!/usr/bin/env python3
"""Re-fetch each source_url and assert the source_quote actually appears on the page.

Mirrors what the downstream verifier will do, so failures get caught before hand-off.
Bot-blocked hosts (reddit, 1p3a, glassdoor, ...) are reported as UNCHECKABLE rather
than failures, since those records are honestly labelled access=snippet_only.
"""
import html
import json
import os
import re
import subprocess
import sys
import unicodedata

CACHE = "/workspace/harvest/.verify_cache"
os.makedirs(CACHE, exist_ok=True)

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

BLOCKED_HOSTS = ("reddit.com", "1point3acres.com", "zhihu.com",
                 "leetcode.com", "tieba.baidu.com", "quizlet.com", "xiaohongshu.com",
                 # AWS WAF human-verification interstitial; text came from a search extract.
                 "efinancialcareers",
                 # Cloudflare interstitial to curl; text came through the WebFetch renderer.
                 "quantnet.com")


def slug(u):
    return re.sub(r"[^A-Za-z0-9]+", "_", u)[:150]


def _curl(url):
    try:
        r = subprocess.run(["curl", "-sL", "--max-time", "50", "--compressed", "-A", UA, url],
                           capture_output=True)
        return r.stdout.decode("utf-8", errors="replace")
    except Exception:
        return ""


def fetch(url):
    p = os.path.join(CACHE, slug(url) + ".txt")
    if os.path.exists(p):
        return open(p, encoding="utf-8", errors="replace").read()
    raw = _curl(url)
    # Cloudflare-challenged (WSO etc.): retry through the r.jina.ai text proxy.
    if is_challenge(norm(raw)):
        raw = _curl("https://r.jina.ai/" + url) or raw
    open(p, "w", encoding="utf-8").write(raw)
    return raw


CHALLENGE_MARKERS = ("just a moment", "enable javascript and cookies", "attention required",
                     "checking your browser", "cf-browser-verification", "access denied",
                     "verify you are human", "请开启javascript")


def is_challenge(body_norm):
    return len(body_norm) < 4000 and any(m in body_norm for m in CHALLENGE_MARKERS)


def norm(s, strip_tags=True):
    """Strip HTML, unescape entities, collapse whitespace, fold quote/dash variants.

    strip_tags must be False for quote text: a quote like "n<=100000), ... |i-j|>1"
    contains angle brackets that a tag-stripper would eat.
    """
    if strip_tags:
        s = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", s)
        s = re.sub(r"(?s)<[^>]+>", " ", s)
    s = html.unescape(s)
    # r.jina.ai returns markdown; collapse [label](url) to label so quotes match the rendered page.
    for _ in range(3):
        s = re.sub(r"\[([^\[\]]*?)\]\((?:[^()\s]|\([^()]*\))*\)", r"\1", s)
    s = re.sub(r"!\[[^\]]*\]", " ", s)
    s = s.replace("\\u002F", "/").replace("\\/", "/").replace('\\"', '"').replace("\\n", " ")
    s = unicodedata.normalize("NFKC", s)
    for a, b in [("\u2018", "'"), ("\u2019", "'"), ("\u201c", '"'), ("\u201d", '"'),
                 ("\u2013", "-"), ("\u2014", "-"), ("\u2026", "..."), ("\u00a0", " ")]:
        s = s.replace(a, b)
    s = re.sub(r"\s+", " ", s)
    return s.lower()


def main(paths):
    ok = fail = uncheck = 0
    failures = []
    for path in paths:
        for i, line in enumerate(open(path, encoding="utf-8"), 1):
            line = line.strip()
            if not line:
                continue
            o = json.loads(line)
            url, q = o["source_url"], o["source_quote"]
            tag = "%s:%d %s" % (os.path.basename(path), i, o["firm"])
            if any(h in url for h in BLOCKED_HOSTS):
                uncheck += 1
                continue
            body = norm(fetch(url))
            if not body.strip() or is_challenge(body):
                uncheck += 1
                continue
            if norm(q, strip_tags=False) in body:
                ok += 1
            else:
                fail += 1
                failures.append((tag, url, q[:110]))
    print("VERIFIED OK : %d" % ok)
    print("FAILED      : %d" % fail)
    print("UNCHECKABLE : %d (bot-blocked host or empty fetch)" % uncheck)
    for t, u, q in failures:
        print("\n  FAIL %s\n    %s\n    quote: %s" % (t, u, q))
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
