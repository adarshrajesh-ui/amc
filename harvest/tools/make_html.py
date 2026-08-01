#!/usr/bin/env python3
"""Render the answer key as one self-contained HTML file.

A raw .md is awkward to study from outside an editor, and this set is meant to be
practised against. The output is a single file with no external assets, so it works
offline, prints, and opens on a phone.

Answers are collapsed behind a toggle by default: a question set whose answers are
visible while you read the question is not a practice set.
"""
from __future__ import annotations

import html
import pathlib
import re
import sys

import markdown

HARVEST = pathlib.Path(__file__).resolve().parent.parent

CSS = """
:root { --fg:#1a1a1a; --muted:#666; --line:#e3e3e3; --accent:#0b5fa5; --warn:#a5340b;
        --bg:#fff; --card:#fafafa; }
@media (prefers-color-scheme: dark) {
  :root { --fg:#e6e6e6; --muted:#9a9a9a; --line:#333; --accent:#6db3f2; --warn:#f0916b;
          --bg:#161616; --card:#1e1e1e; }
}
* { box-sizing:border-box }
body { max-width:52rem; margin:0 auto; padding:2rem 1.2rem 6rem;
       font:16px/1.62 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",sans-serif;
       color:var(--fg); background:var(--bg); }
h1 { font-size:1.9rem; line-height:1.2; margin:0 0 .4rem }
h2 { font-size:1.35rem; margin:3rem 0 .2rem; padding-top:1rem; border-top:2px solid var(--line) }
h3 { font-size:1rem; font-weight:600; margin:2rem 0 .6rem; color:var(--muted);
     font-variant-numeric:tabular-nums }
hr { display:none }
sub { display:block; color:var(--muted); font-size:.8rem; margin:.35rem 0 0 }
sub a { color:var(--muted) }
a { color:var(--accent) }
blockquote { margin:.8rem 0; padding:.6rem .9rem; border-left:3px solid var(--warn);
             background:var(--card); color:var(--fg) }
code { background:var(--card); padding:.1rem .3rem; border-radius:3px; font-size:.87em }
em { color:var(--muted) }
details { margin:.6rem 0 1rem; border:1px solid var(--line); border-radius:6px;
          background:var(--card); padding:.5rem .9rem }
details[open] { padding-bottom:.9rem }
summary { cursor:pointer; font-weight:600; color:var(--accent); user-select:none;
          list-style:none; padding:.15rem 0 }
summary::-webkit-details-marker { display:none }
summary::before { content:"▸ "; }
details[open] summary::before { content:"▾ "; }
.bar { position:sticky; top:0; background:var(--bg); border-bottom:1px solid var(--line);
       padding:.7rem 0; margin:-2rem 0 1.5rem; z-index:9; display:flex; gap:.6rem;
       flex-wrap:wrap; align-items:center }
.bar button { font:inherit; font-size:.85rem; padding:.35rem .8rem; cursor:pointer;
              border:1px solid var(--line); background:var(--card); color:var(--fg);
              border-radius:5px }
.bar button:hover { border-color:var(--accent); color:var(--accent) }
.bar input { font:inherit; font-size:.85rem; padding:.35rem .6rem; flex:1; min-width:9rem;
             border:1px solid var(--line); border-radius:5px; background:var(--card);
             color:var(--fg) }
.q { scroll-margin-top:4rem }
.hidden { display:none !important }
@media print { .bar{display:none} details{border:none;background:none} details>*{display:block!important} }
"""

JS = """
const q = s => document.querySelectorAll(s);
document.getElementById('open').onclick  = () => q('details').forEach(d => d.open = true);
document.getElementById('close').onclick = () => q('details').forEach(d => d.open = false);
document.getElementById('find').oninput = e => {
  const t = e.target.value.trim().toLowerCase();
  q('.q').forEach(el => {
    el.classList.toggle('hidden', t && !el.textContent.toLowerCase().includes(t));
  });
  q('h2').forEach(h => {
    let n = h.nextElementSibling, any = false;
    while (n && n.tagName !== 'H2') { if (n.classList.contains('q') && !n.classList.contains('hidden')) any = true; n = n.nextElementSibling; }
    h.classList.toggle('hidden', t && !any);
  });
};
"""


def main() -> int:
    src = HARVEST / "QTRADER_ANSWERED.md"
    text = src.read_text(encoding="utf-8")

    body = markdown.markdown(text, extensions=["tables", "sane_lists"])

    # Wrap each question block in a container so search can show/hide whole items,
    # and fold the answer behind a toggle so the file is usable as practice.
    parts = re.split(r"(?=<h3)", body)
    out = []
    for p in parts:
        if not p.startswith("<h3"):
            out.append(p)
            continue
        m = re.search(r"(<p><strong>Answer:</strong>)", p)
        if m:
            head, tail = p[: m.start()], p[m.start():]
            p = (head + "<details><summary>Show answer</summary>" + tail + "</details>")
        out.append('<div class="q">' + p + "</div>")
    body = "".join(out)

    doc = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Quant trader questions with answers</title>
<style>{CSS}</style></head><body>
<div class="bar">
  <button id="open">Show all answers</button>
  <button id="close">Hide all answers</button>
  <input id="find" type="search" placeholder="Filter questions, e.g. SIG, Bayes, market making">
</div>
{body}
<script>{JS}</script>
</body></html>"""

    out_path = HARVEST / "QTRADER_ANSWERED.html"
    out_path.write_text(doc, encoding="utf-8")
    kb = out_path.stat().st_size / 1024
    print(f"{out_path}  ({kb:.0f} KB, self-contained)")
    print(f"  questions wrapped: {doc.count('class=\"q\"')}")
    print(f"  answers folded   : {doc.count('<details>')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
