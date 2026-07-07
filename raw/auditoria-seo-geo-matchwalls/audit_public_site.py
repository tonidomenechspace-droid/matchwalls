import csv
import gzip
import json
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parent
BASE = "https://www.matchwalls.com"
UA = "MatchwallsSEOAudit/1.0 (read-only; contact: website owner)"
LANG_PATHS = {"es": "", "en": "/en", "fr": "/fr", "de": "/de", "nl": "/nl", "it": "/it", "pt-PT": "/pt"}
MAX_PER_TYPE_LANG = 90


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ""
        self._in_title = False
        self.metas = []
        self.links = []
        self.hreflangs = []
        self.canonicals = []
        self.headings = []
        self.images = []
        self.scripts = []
        self._script_type = ""
        self._script_text = []
        self.text = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "title":
            self._in_title = True
        elif tag == "meta":
            self.metas.append(attrs)
        elif tag == "link":
            rel = attrs.get("rel", "").lower()
            if "canonical" in rel:
                self.canonicals.append(attrs.get("href", ""))
            if "alternate" in rel and attrs.get("hreflang"):
                self.hreflangs.append((attrs.get("hreflang", ""), attrs.get("href", "")))
        elif tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])
        elif tag in {"h1", "h2", "h3"}:
            self.headings.append([tag, ""])
        elif tag == "img":
            self.images.append(attrs)
        elif tag == "script":
            self._script_type = attrs.get("type", "")
            self._script_text = []

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        elif tag == "script":
            if self._script_type == "application/ld+json":
                self.scripts.append("".join(self._script_text))
            self._script_type = ""
            self._script_text = []

    def handle_data(self, data):
        clean = re.sub(r"\s+", " ", data).strip()
        if self._in_title:
            self.title += clean
        if self.headings and self.lasttag == self.headings[-1][0]:
            self.headings[-1][1] += clean
        if self._script_type:
            self._script_text.append(data)
        elif clean:
            self.text.append(clean)


def fetch(url, timeout=25):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
    start = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            raw = r.read()
            if r.headers.get("Content-Encoding") == "gzip":
                raw = gzip.decompress(raw)
            return {
                "requested_url": url,
                "final_url": r.geturl(),
                "status": r.status,
                "headers": dict(r.headers),
                "body": raw,
                "elapsed_ms": int((time.time() - start) * 1000),
                "error": "",
            }
    except Exception as e:
        return {
            "requested_url": url,
            "final_url": "",
            "status": getattr(e, "code", 0),
            "headers": {},
            "body": b"",
            "elapsed_ms": int((time.time() - start) * 1000),
            "error": str(e)[:300],
        }


def parse_sitemap(url, seen=None):
    seen = seen or set()
    if url in seen:
        return []
    seen.add(url)
    res = fetch(url)
    if res["status"] != 200:
        return []
    try:
        root = ET.fromstring(res["body"])
    except ET.ParseError:
        return []
    locs = [el.text.strip() for el in root.iter() if el.tag.endswith("loc") and el.text]
    if root.tag.endswith("sitemapindex"):
        out = []
        for loc in locs:
            out.extend(parse_sitemap(loc, seen))
            time.sleep(0.08)
        return out
    return locs


def classify(url):
    path = urllib.parse.urlparse(url).path
    clean = re.sub(r"^/(en|fr|de|nl|it|pt)(/|$)", "/", path)
    if "/products/" in clean:
        return "product"
    if "/collections/" in clean:
        return "collection"
    if "/blogs/" in clean:
        return "article"
    if "/pages/" in clean:
        return "page"
    if clean in {"", "/"}:
        return "home"
    return "other"


def lang_from_url(url):
    path = urllib.parse.urlparse(url).path
    m = re.match(r"^/(en|fr|de|nl|it|pt)(/|$)", path)
    return {"pt": "pt-PT"}.get(m.group(1), m.group(1)) if m else "es"


def meta_value(metas, key, value):
    for m in metas:
        if m.get(key, "").lower() == value.lower():
            return m.get("content", "")
    return ""


def flatten_schema_types(obj):
    types = []
    if isinstance(obj, dict):
        typ = obj.get("@type")
        if isinstance(typ, list):
            types.extend(str(x) for x in typ)
        elif typ:
            types.append(str(typ))
        for value in obj.values():
            types.extend(flatten_schema_types(value))
    elif isinstance(obj, list):
        for item in obj:
            types.extend(flatten_schema_types(item))
    return types


def language_signals(text, lang):
    patterns = {
        "es": [" envío ", " papel pintado ", " comprar ", " nosotros ", " precio "],
        "en": [" shipping ", " wallpaper ", " buy ", " about us ", " price "],
        "fr": [" livraison ", " papier peint ", " acheter ", " prix ", " nous "],
        "de": [" versand ", " tapete ", " kaufen ", " preis ", " über uns "],
        "nl": [" verzending ", " behang ", " kopen ", " prijs ", " over ons "],
        "it": [" spedizione ", " carta da parati ", " acquistare ", " prezzo "],
        "pt-PT": [" envio ", " papel de parede ", " comprar ", " preço "],
    }
    lower = f" {text.lower()} "
    scores = {code: sum(lower.count(p) for p in pats) for code, pats in patterns.items()}
    other = sorted(((v, k) for k, v in scores.items() if k != lang), reverse=True)
    return scores.get(lang, 0), other[0][1] if other else "", other[0][0] if other else 0


def main():
    ROOT.mkdir(parents=True, exist_ok=True)
    robots = fetch(f"{BASE}/robots.txt")
    (ROOT / "robots.txt.evidence").write_bytes(robots["body"])

    all_urls = parse_sitemap(f"{BASE}/sitemap.xml")
    all_urls = sorted(set(u for u in all_urls if "matchwalls.com" in u))
    by_bucket = defaultdict(list)
    for url in all_urls:
        by_bucket[(lang_from_url(url), classify(url))].append(url)

    selected = set()
    for lang in LANG_PATHS:
        selected.add(f"{BASE}{LANG_PATHS[lang]}/")
    for bucket, urls in by_bucket.items():
        typ = bucket[1]
        limit = MAX_PER_TYPE_LANG if typ == "product" else min(len(urls), 160)
        if len(urls) <= limit:
            selected.update(urls)
        else:
            step = len(urls) / limit
            selected.update(urls[int(i * step)] for i in range(limit))
    special_terms = ("serene-vista", "whispering-woods", "sample", "muestra", "echantillon", "muster", "staal")
    selected.update(u for u in all_urls if any(t in u.lower() for t in special_terms))

    rows = []
    detail_findings = []
    title_groups = defaultdict(list)
    desc_groups = defaultdict(list)
    canonical_groups = defaultdict(list)

    for idx, url in enumerate(sorted(selected)):
        res = fetch(url)
        content_type = res["headers"].get("Content-Type", "")
        row = {
            "url": url,
            "idioma_url": lang_from_url(url),
            "tipo": classify(url),
            "estado_http": res["status"],
            "url_final": res["final_url"],
            "tiempo_ms": res["elapsed_ms"],
            "content_type": content_type,
            "tamano_bytes": len(res["body"]),
            "title": "",
            "title_longitud": 0,
            "meta_description": "",
            "description_longitud": 0,
            "meta_robots": "",
            "canonical": "",
            "hreflang_count": 0,
            "hreflangs": "",
            "h1_count": 0,
            "h1": "",
            "schema_types": "",
            "aggregate_rating": "no",
            "review_schema": "no",
            "imagenes": 0,
            "imagenes_sin_alt": 0,
            "enlaces_internos": 0,
            "texto_caracteres": 0,
            "posible_mezcla_idioma": "no",
            "idioma_dominante_alterno": "",
            "error": res["error"],
        }
        if res["status"] == 200 and "text/html" in content_type:
            html = res["body"].decode("utf-8", "replace")
            p = PageParser()
            try:
                p.feed(html)
            except Exception:
                pass
            desc = meta_value(p.metas, "name", "description")
            robots_meta = meta_value(p.metas, "name", "robots")
            h1s = [v for tag, v in p.headings if tag == "h1"]
            schema_types = []
            for script in p.scripts:
                try:
                    schema_types.extend(flatten_schema_types(json.loads(script)))
                except Exception:
                    schema_types.append("INVALID_JSON_LD")
            visible_text = " ".join(p.text)
            expected, alt_lang, alt_score = language_signals(visible_text, row["idioma_url"])
            possible_mix = alt_score >= 3 and alt_score > expected
            internal_links = [
                x for x in p.links
                if x.startswith("/") or "matchwalls.com" in x
            ]
            row.update({
                "title": p.title[:500],
                "title_longitud": len(p.title),
                "meta_description": desc[:1000],
                "description_longitud": len(desc),
                "meta_robots": robots_meta,
                "canonical": p.canonicals[0] if p.canonicals else "",
                "hreflang_count": len(p.hreflangs),
                "hreflangs": " | ".join(f"{a}:{b}" for a, b in p.hreflangs),
                "h1_count": len(h1s),
                "h1": " | ".join(h1s)[:1000],
                "schema_types": " | ".join(sorted(set(schema_types))),
                "aggregate_rating": "sí" if "AggregateRating" in schema_types else "no",
                "review_schema": "sí" if "Review" in schema_types else "no",
                "imagenes": len(p.images),
                "imagenes_sin_alt": sum(not im.get("alt", "").strip() for im in p.images),
                "enlaces_internos": len(internal_links),
                "texto_caracteres": len(visible_text),
                "posible_mezcla_idioma": "sí" if possible_mix else "no",
                "idioma_dominante_alterno": alt_lang if possible_mix else "",
            })
            if p.title:
                title_groups[p.title.strip()].append(url)
            if desc:
                desc_groups[desc.strip()].append(url)
            if row["canonical"]:
                canonical_groups[row["canonical"]].append(url)
        rows.append(row)
        if idx % 50 == 0:
            print(f"rastreadas {idx + 1}/{len(selected)}")
        time.sleep(0.10)

    fields = list(rows[0].keys()) if rows else []
    with (ROOT / "inventario-urls.csv").open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    summary = {
        "sitemap_urls_total": len(all_urls),
        "rastreadas": len(rows),
        "por_idioma_tipo_sitemap": {f"{k[0]}|{k[1]}": len(v) for k, v in sorted(by_bucket.items())},
        "http": dict(Counter(str(r["estado_http"]) for r in rows)),
        "schema": dict(Counter(t for r in rows for t in r["schema_types"].split(" | ") if t)),
        "aggregate_rating_pages": sum(r["aggregate_rating"] == "sí" for r in rows),
        "review_schema_pages": sum(r["review_schema"] == "sí" for r in rows),
        "possible_language_mix": sum(r["posible_mezcla_idioma"] == "sí" for r in rows),
        "missing_description": sum(not r["meta_description"] for r in rows if r["estado_http"] == 200),
        "missing_canonical": sum(not r["canonical"] for r in rows if r["estado_http"] == 200),
        "missing_h1": sum(r["h1_count"] == 0 for r in rows if r["estado_http"] == 200),
        "multiple_h1": sum(r["h1_count"] > 1 for r in rows if r["estado_http"] == 200),
        "duplicate_titles": {k: v for k, v in title_groups.items() if len(v) > 1},
        "duplicate_descriptions": {k: v for k, v in desc_groups.items() if len(v) > 1},
        "shared_canonicals": {k: v for k, v in canonical_groups.items() if len(v) > 1},
    }
    (ROOT / "crawl-summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    (ROOT / "sitemap-urls.txt").write_text("\n".join(all_urls), encoding="utf-8")
    print(json.dumps({k: v for k, v in summary.items() if not isinstance(v, dict)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
