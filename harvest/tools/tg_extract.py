#!/usr/bin/env python3
"""Extract message permalink, datetime and plain text from a t.me/s/<channel> HTML page."""
import html
import re
import sys

MSG_RE = re.compile(
    r'<div class="tgme_widget_message[^"]*"[^>]*data-post="([^"]+)"(.*?)(?=<div class="tgme_widget_message[^"]*"[^>]*data-post=|</section>)',
    re.S,
)
TEXT_RE = re.compile(r'<div class="tgme_widget_message_text[^"]*"[^>]*>(.*?)</div>', re.S)
PREV_RE = re.compile(
    r'<div class="link_preview_(?:site_name|title|description)"[^>]*>(.*?)</div>', re.S
)
TIME_RE = re.compile(r'<time[^>]*datetime="([^"]+)"')


def strip_tags(s: str) -> str:
    s = re.sub(r'<br\s*/?>', '\n', s)
    s = re.sub(r'</?(i|b|u|s|code|pre|span|tg-emoji|tg-spoiler)[^>]*>', '', s)
    s = re.sub(r'<a[^>]*>', '', s)
    s = s.replace('</a>', '')
    s = re.sub(r'<[^>]+>', '\n', s)
    s = html.unescape(s)
    s = re.sub(r'[ \t]+', ' ', s)
    s = re.sub(r'\n{3,}', '\n\n', s)
    return s.strip()


def main(path: str) -> None:
    raw = open(path, encoding='utf-8', errors='replace').read()
    for post, body in MSG_RE.findall(raw):
        times = TIME_RE.findall(body)
        when = times[-1] if times else '?'
        chunks = [strip_tags(t) for t in TEXT_RE.findall(body)]
        chunks += [strip_tags(t) for t in PREV_RE.findall(body)]
        text = '\n---\n'.join(c for c in chunks if c)
        print(f'=== https://t.me/{post}  [{when}]')
        print(text)
        print()


if __name__ == '__main__':
    main(sys.argv[1])
