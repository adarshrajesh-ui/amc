#!/usr/bin/env python3
"""Pull the exact text of individual t.me messages (post body + link-preview block)."""
import html
import json
import os
import re
import sys
import time
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from indep_check import norm, longest_common_prefix_frac  # noqa: E402

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
CACHE = "/workspace/harvest/.indep_cache"
os.makedirs(CACHE, exist_ok=True)


def get(url):
    key = os.path.join(CACHE, "tg_" + re.sub(r"\W+", "_", url) + ".html")
    if os.path.exists(key):
        return open(key, encoding="utf-8", errors="replace").read()
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    body = urllib.request.urlopen(req, timeout=90).read().decode("utf-8", "replace")
    open(key, "w", encoding="utf-8").write(body)
    time.sleep(2)
    return body


def untag(frag):
    frag = re.sub(r"(?i)<br\s*/?>", "\n", frag)
    frag = re.sub(r"(?s)<[^>]+>", "", frag)
    return html.unescape(frag)


def message_text(url):
    """Return (whole-page-text, text of the single addressed message)."""
    chan, mid = re.match(r"https?://t\.me/([^/]+)/(\d+)", url).groups()
    page = get(f"https://t.me/s/{chan}/{mid}")
    blocks = re.split(r'(?=<div class="tgme_widget_message[ "])', page)
    mine = ""
    for b in blocks:
        m = re.search(r'data-post="([^"]+)"', b)
        if m and m.group(1) == f"{chan}/{mid}":
            mine = untag(b)
    return untag(page), mine


def main():
    sample = json.load(open("/workspace/harvest/reports/_sample45.json"))["sample"]
    want = set(sys.argv[1:]) if len(sys.argv) > 1 else None
    for s in sample:
        if "t.me/" not in s["source_url"]:
            continue
        if want and s["id"] not in want:
            continue
        try:
            whole, mine = message_text(s["source_url"])
        except Exception as e:
            print(f"{s['id']} ERROR {e}\n")
            continue
        nq = norm(s["source_quote"])
        f_mine, n_mine = longest_common_prefix_frac(s["source_quote"], mine)
        f_page, n_page = longest_common_prefix_frac(s["source_quote"], whole)
        print("=" * 100)
        print(f"{s['id']}  {s['source_url']}   quote_len={len(nq)}")
        print(f"  in THIS message : {f_mine:.1%} ({n_mine}/{len(nq)})")
        print(f"  anywhere on page: {f_page:.1%} ({n_page}/{len(nq)})")
        body = re.sub(r"\n{2,}", "\n", mine).strip()
        print("  --- message text as published ---")
        print("  " + body[:1400].replace("\n", "\n  "))
        if f_mine < 1.0:
            print(f"  QUOTE matched head: ...{nq[max(0, n_mine - 60):n_mine]!r}")
            print(f"  QUOTE diverges at : {nq[n_mine:n_mine + 120]!r}")
        print()


if __name__ == "__main__":
    main()
