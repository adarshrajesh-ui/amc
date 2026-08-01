"""Fetch + search helpers for the red-team sweep. Caches everything to redteam/cache."""
import hashlib, json, os, re, time, urllib.parse, random
import urllib.request, urllib.error

CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cache')
os.makedirs(CACHE, exist_ok=True)

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36")


def _key(tag, s):
    return os.path.join(CACHE, tag + '_' + hashlib.sha1(s.encode('utf-8', 'ignore')).hexdigest()[:20] + '.txt')


def fetch(url, tag='p', timeout=30, force=False, headers=None):
    k = _key(tag, url)
    if os.path.exists(k) and not force:
        return open(k, encoding='utf-8', errors='ignore').read()
    h = {'User-Agent': UA, 'Accept': 'text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8',
         'Accept-Language': 'en-US,en;q=0.9'}
    if headers:
        h.update(headers)
    body = ''
    try:
        req = urllib.request.Request(url, headers=h)
        with urllib.request.urlopen(req, timeout=timeout) as r:
            raw = r.read()
            try:
                import gzip
                if raw[:2] == b'\x1f\x8b':
                    raw = gzip.decompress(raw)
            except Exception:
                pass
            body = raw.decode('utf-8', 'ignore')
    except urllib.error.HTTPError as e:
        try:
            body = 'HTTPERROR %d\n' % e.code + e.read().decode('utf-8', 'ignore')
        except Exception:
            body = 'HTTPERROR %d' % e.code
    except Exception as e:
        body = 'FETCHERROR %s' % e
    open(k, 'w', encoding='utf-8').write(body)
    return body


def jina(url, tag='j', **kw):
    """Text-extraction proxy; often bypasses light bot walls."""
    return fetch('https://r.jina.ai/' + url, tag=tag, **kw)


def strip_html(h):
    h = re.sub(r'(?is)<(script|style|noscript)[^>]*>.*?</\1>', ' ', h)
    h = re.sub(r'(?s)<!--.*?-->', ' ', h)
    h = re.sub(r'(?s)<[^>]+>', ' ', h)
    import html as _h
    h = _h.unescape(h)
    return re.sub(r'[ \t\xa0]+', ' ', h)


def ddg(q, tag='ddg', force=False):
    """DuckDuckGo HTML endpoint."""
    u = 'https://html.duckduckgo.com/html/?q=' + urllib.parse.quote(q)
    h = fetch(u, tag=tag, force=force, headers={'Referer': 'https://duckduckgo.com/'})
    out = []
    for m in re.finditer(r'<a[^>]+class="result__a"[^>]*href="([^"]+)"[^>]*>(.*?)</a>', h, re.S):
        href, title = m.group(1), strip_html(m.group(2)).strip()
        if 'uddg=' in href:
            href = urllib.parse.unquote(re.search(r'uddg=([^&]+)', href).group(1))
        out.append((href, title))
    if not out:
        for m in re.finditer(r'href="(https?://[^"]+)"[^>]*class="result__a"', h):
            out.append((m.group(1), ''))
    return out, h


def bing(q, tag='bing', force=False):
    u = 'https://www.bing.com/search?q=' + urllib.parse.quote(q) + '&setlang=en&count=30'
    h = fetch(u, tag=tag, force=force, headers={'Referer': 'https://www.bing.com/'})
    out = []
    for m in re.finditer(r'<li class="b_algo".*?<h2>\s*<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', h, re.S):
        out.append((m.group(1), strip_html(m.group(2)).strip()))
    return out, h


ENGINE_NOISE = ('brave.com', 'duckduckgo.com', 'mojeek.com', 'marginalia.nu', 'bing.com',
                'microsoft.com', 'google.com', 'startpage.com', 'ecosia.org', 'yandex.',
                'w3.org', 'schema.org', 'gstatic', 'msn.com', 'hackerone', 'brave.app',
                'searx', 'archive.org/donate')


def _extract_links(html):
    out, seen = [], set()
    for m in re.finditer(r'href="(https?://[^"#]+)"', html):
        u = m.group(1)
        if any(n in u for n in ENGINE_NOISE):
            continue
        u = u.rstrip('/')
        if u in seen:
            continue
        seen.add(u)
        out.append(u)
    return out


def brave(q, tag='brv', force=False):
    u = 'https://search.brave.com/search?q=' + urllib.parse.quote(q)
    h = fetch(u, tag=tag, force=force)
    if 'HTTPERROR' in h[:40] or 'not a robot' in h[:4000]:
        return None, h
    txt = strip_html(h)
    if re.search(r'not find any results|No results found', txt, re.I):
        return [], h
    return _extract_links(h), h


def search_multi(q, force=False):
    """Try engines in order; return (engine, links, ok). ok=False means all engines blocked."""
    r, h = brave(q, force=force)
    if r is not None:
        return 'brave', r, True
    try:
        d, hh = ddg(q, force=force)
        if d and 'confirm this search was made by a human' not in hh:
            return 'ddg', [u for u, _ in d], True
    except Exception:
        pass
    u = 'https://search.marginalia.nu/search?query=' + urllib.parse.quote(q)
    h = fetch(u, tag='mrg', force=force)
    if 'HTTPERROR' not in h[:40]:
        return 'marginalia', _extract_links(h), True
    return None, [], False


def wayback_cdx(url, tag='cdx', force=False, limit=200):
    q = ('https://web.archive.org/cdx/search/cdx?url=' + urllib.parse.quote(url, safe='') +
         '&output=json&fl=timestamp,original,statuscode,digest&collapse=digest&limit=%d' % limit)
    t = fetch(q, tag=tag, force=force)
    try:
        return json.loads(t)
    except Exception:
        return []


def norm(s):
    return re.sub(r'[^0-9a-z\u4e00-\u9fff]+', '', (s or '').lower())
