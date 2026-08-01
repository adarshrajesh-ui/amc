"""Paced multi-engine search with rotation, backoff, and a persistent result store.

Failures are never cached, so a query can be retried on a later pass.
"""
import hashlib, json, os, random, re, threading, time, urllib.parse
import net

HERE = os.path.dirname(os.path.abspath(__file__))
STORE = os.path.join(HERE, 'searchstore.json')
_lock = threading.Lock()
_store = {}
if os.path.exists(STORE):
    try:
        _store = json.load(open(STORE))
    except Exception:
        _store = {}

_last = {}
MIN_GAP = {'brave': 6.0, 'ddg': 8.0, 'mojeek': 10.0, 'marginalia': 4.0}


def _wait(eng):
    with _lock:
        t = _last.get(eng, 0)
        gap = MIN_GAP.get(eng, 5.0)
        d = gap - (time.time() - t)
        if d > 0:
            time.sleep(d + random.uniform(0, 0.8))
        _last[eng] = time.time()


def _raw(url, eng):
    _wait(eng)
    h = {'User-Agent': net.UA, 'Accept': 'text/html,*/*;q=0.8', 'Accept-Language': 'en-US,en;q=0.9'}
    import urllib.request
    try:
        req = urllib.request.Request(url, headers=h)
        with urllib.request.urlopen(req, timeout=30) as r:
            raw = r.read()
            if raw[:2] == b'\x1f\x8b':
                import gzip; raw = gzip.decompress(raw)
            return raw.decode('utf-8', 'ignore'), None
    except Exception as e:
        return '', str(e)


def _brave(q):
    h, err = _raw('https://search.brave.com/search?q=' + urllib.parse.quote(q), 'brave')
    if err or not h:
        return None
    if 'not a robot' in h[:6000] or 'captcha' in h[:6000].lower():
        return None
    txt = net.strip_html(h)
    if re.search(r"not find any results|No results found", txt, re.I):
        return []
    return net._extract_links(h)


def _ddg(q):
    h, err = _raw('https://html.duckduckgo.com/html/?q=' + urllib.parse.quote(q), 'ddg')
    if err or not h:
        return None
    if 'confirm this search was made by a human' in h:
        return None
    out = []
    for m in re.finditer(r'<a[^>]+class="result__a"[^>]*href="([^"]+)"', h):
        href = m.group(1)
        if 'uddg=' in href:
            href = urllib.parse.unquote(re.search(r'uddg=([^&]+)', href).group(1))
        out.append(href.rstrip('/'))
    if not out and re.search(r'No results|no results found', net.strip_html(h), re.I):
        return []
    return out


def _mojeek(q):
    h, err = _raw('https://www.mojeek.com/search?q=' + urllib.parse.quote(q), 'mojeek')
    if err or not h or '403' in h[:60]:
        return None
    if re.search(r'No results', net.strip_html(h), re.I):
        return []
    return [u.rstrip('/') for u in re.findall(r'<a href="(https?://[^"]+)"[^>]*class="ob"', h)] or \
           net._extract_links(h)[:20]


ENGINES = [('brave', _brave), ('ddg', _ddg), ('mojeek', _mojeek)]


def search(q, force=False):
    """Returns dict {engine, links, ok}. ok=False => every engine refused; unknown provenance."""
    k = hashlib.sha1(q.encode('utf-8')).hexdigest()[:20]
    if not force and k in _store:
        return _store[k]
    order = ENGINES[:]
    random.shuffle(order)
    for name, fn in order:
        try:
            r = fn(q)
        except Exception:
            r = None
        if r is not None:
            rec = {'q': q, 'engine': name, 'links': r, 'ok': True}
            with _lock:
                _store[k] = rec
                json.dump(_store, open(STORE, 'w'))
            return rec
    return {'q': q, 'engine': None, 'links': [], 'ok': False}


def flush():
    with _lock:
        json.dump(_store, open(STORE, 'w'))
