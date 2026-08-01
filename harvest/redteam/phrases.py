"""Extract distinctive searchable phrases from question_text for provenance attacks."""
import re

STOP = set("""the a an and or of to in for with on at by is are was were be been being that this these those
it its as from if then than so but not no we you they he she i my your our their there here what which who
whom how when where why can could will would should may might must do does did have has had""".split())


def distinctive(text, maxwords=12, minwords=5):
    """Longest run of content-bearing words - good for exact-phrase search."""
    t = re.sub(r'\s+', ' ', (text or '')).strip()
    t = re.sub(r'^(Question\s*\d+[:.)]?\s*|Q\d+[:.)]?\s*)', '', t, flags=re.I)
    # prefer a clause with rare nouns/numbers
    words = re.findall(r"[A-Za-z0-9''\-\.]+", t)
    if len(words) < minwords:
        return None
    best, bestscore = None, -1
    for n in (maxwords, 10, 8, 6):
        if len(words) < n:
            continue
        for i in range(0, min(len(words) - n + 1, 40)):
            w = words[i:i + n]
            content = [x for x in w if x.lower() not in STOP]
            score = len(set(x.lower() for x in content))
            if any(re.search(r'\d', x) for x in w):
                score += 1
            if score > bestscore:
                bestscore, best = score, ' '.join(w)
        if best:
            break
    return best


def cjk_phrase(text, n=16):
    t = re.sub(r'\s+', '', text or '')
    cj = re.findall(r'[\u4e00-\u9fff0-9A-Za-z]+', t)
    s = ''.join(cj)
    return s[:n] if len(s) >= 8 else None


def is_cjk(t):
    return len(re.findall(r'[\u4e00-\u9fff]', t or '')) >= 4
