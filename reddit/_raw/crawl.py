#!/usr/bin/env python3
"""Focused crawl: 5 manager subreddits -> rank by position in Reddit's `top`
listings -> fetch comment threads for the best 100.

RSS exposes no score, so value is inferred from rank within each top listing,
with older/wider windows weighted higher (top/all beats top/month)."""
import json, os, re, sys, time, urllib.request, urllib.error, html
from xml.etree import ElementTree as ET

BASE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(BASE, "raw2")
os.makedirs(RAW, exist_ok=True)

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
NS = {"a": "http://www.w3.org/2005/Atom"}
DELAY = 24.0
_last = [0.0]

def fetch(url, tries=5):
    for attempt in range(tries):
        w = DELAY - (time.time() - _last[0])
        if w > 0: time.sleep(w)
        req = urllib.request.Request(url, headers={
            "User-Agent": UA,
            "Accept": "application/atom+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9"})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                d = r.read().decode("utf-8", "replace")
            _last[0] = time.time()
            if len(d) > 400: return d
            time.sleep(25 * (attempt + 1))
        except urllib.error.HTTPError as e:
            _last[0] = time.time()
            back = float(e.headers.get("x-ratelimit-reset") or 25) + 5 if e.code == 429 else 10
            print(f"    HTTP {e.code} backoff {back}s", flush=True)
            time.sleep(back)
        except Exception as e:
            _last[0] = time.time(); print(f"    err {e}", flush=True); time.sleep(15)
    return None

def strip_html(s):
    s = html.unescape(s or "")
    s = re.sub(r"<br\s*/?>", "\n", s); s = re.sub(r"</p>", "\n\n", s)
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"\n{3,}", "\n\n", html.unescape(s)).strip()

def entries(xml):
    try: root = ET.fromstring(xml)
    except ET.ParseError: return []
    out = []
    for e in root.findall("a:entry", NS):
        g = lambda t: (e.find(f"a:{t}", NS).text or "") if e.find(f"a:{t}", NS) is not None else ""
        link, auth, cont = e.find("a:link", NS), e.find("a:author/a:name", NS), e.find("a:content", NS)
        out.append({"id": g("id"), "title": html.unescape(g("title")),
                    "url": link.get("href") if link is not None else "",
                    "updated": g("updated"),
                    "author": auth.text if auth is not None and auth.text else "",
                    "body": strip_html(cont.text if cont is not None else "")})
    return out

SUBS = ["managers", "ExperiencedManagers", "AskManagers", "leadership", "ExperiencedDevs"]
# (sort, window, weight) — lower weight = more authoritative signal of value
SORTS = [("top", "all", 0), ("top", "year", 120), ("top", "month", 260), ("hot", None, 420)]

def listings():
    pf, df = os.path.join(RAW, "posts.json"), os.path.join(RAW, "done.json")
    posts = json.load(open(pf)) if os.path.exists(pf) else {}
    done = set(json.load(open(df))) if os.path.exists(df) else set()
    for sub in SUBS:
        for sort, t, weight in SORTS:
            key = f"{sub}|{sort}|{t}"
            if key in done: continue
            url = f"https://www.reddit.com/r/{sub}/{sort}/.rss?limit=100" + (f"&t={t}" if t else "")
            xml = fetch(url); n = 0
            for rank, e in enumerate(entries(xml) if xml else []):
                if not e["id"]: continue
                val = rank + weight
                if e["id"] in posts:
                    posts[e["id"]]["value"] = min(posts[e["id"]]["value"], val)
                else:
                    posts[e["id"]] = {**e, "sub": sub, "value": val}; n += 1
            print(f"{key}: +{n} new (pool {len(posts)})", flush=True)
            done.add(key)
            json.dump(sorted(done), open(df, "w")); json.dump(posts, open(pf, "w"))
    print(f"LISTINGS DONE pool={len(posts)}", flush=True)
    return posts

def pick(posts, n=100):
    cand = []
    for p in posts.values():
        body, title = p["body"], p["title"]
        # need an actual situation to summarise: self-post with substance,
        # or a clear question in the title
        if len(body) < 180 and not title.rstrip().endswith("?"): continue
        if re.match(r"^https?://\S+$", body.strip()): continue
        cand.append(p)
    cand.sort(key=lambda p: p["value"])
    return cand[:n]

def comments(sel):
    tf = os.path.join(RAW, "threads.json")
    th = json.load(open(tf)) if os.path.exists(tf) else {}
    for i, p in enumerate(sel, 1):
        pid = p["id"].replace("t3_", "")
        if pid in th: continue
        xml = fetch(f"https://www.reddit.com/r/{p['sub']}/comments/{pid}/.rss?limit=40&sort=top")
        cs = [{"author": e["author"], "body": e["body"][:2500]}
              for e in (entries(xml) if xml else []) if e["id"].startswith("t1_") and e["body"]]
        th[pid] = {**p, "comments": cs}
        json.dump(th, open(tf, "w"), indent=1)
        print(f"[{i}/{len(sel)}] r/{p['sub']} v={p['value']} {len(cs)}c :: {p['title'][:65]}", flush=True)
    print(f"THREADS DONE n={len(th)}", flush=True)

if __name__ == "__main__":
    ps = listings()
    sel = pick(ps, 100)
    json.dump(sel, open(os.path.join(RAW, "selected.json"), "w"), indent=1)
    print(f"SELECTED {len(sel)}:", flush=True)
    for p in sel[:15]: print(f"   v={p['value']:4} r/{p['sub']:20} {p['title'][:60]}", flush=True)
    comments(sel)
