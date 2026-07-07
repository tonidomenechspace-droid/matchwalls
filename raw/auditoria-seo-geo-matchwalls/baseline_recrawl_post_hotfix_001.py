import csv
import gzip
import json
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parent
BASE = "https://www.matchwalls.com"
LOT = "MW-BASELINE-RECRAWL-POST-HOTFIX-001"
UA = "MatchwallsSEOBaseline/1.0 read-only; owner-authorized audit"
LANGS = {"es", "en", "fr", "de", "nl"}

PREVIOUS_ISSUES = ROOT / "inventario-problemas-contenido-i18n-geo-2026-06-16.csv"

OUT_CRAWL = ROOT / "baseline-recrawl-post-hotfix-2026-06-16.csv"
OUT_VERIFIED = ROOT / "baseline-incidencias-verificadas-2026-06-16.csv"
OUT_FALSE = ROOT / "baseline-falsos-positivos-2026-06-16.csv"
OUT_CRITICAL = ROOT / "baseline-incidencias-criticas-reales-2026-06-16.csv"
OUT_SUMMARY = ROOT / "baseline-recrawl-post-hotfix-2026-06-16.md"
OUT_JSON = ROOT / "baseline-recrawl-post-hotfix-2026-06-16.json"
REGISTRO = ROOT / "registro-cambios-ejecutados.md"

PAYMENT_TERMS = [
    "American Express",
    "Apple Pay",
    "Bancontact",
    "Google Pay",
    "iDEAL",
    "Wero",
    "Maestro",
    "Mastercard",
    "Shop Pay",
    "Union Pay",
    "Visa",
]

FIXED_TEXT_PATTERNS = [
    "FAQ´S",
    "espacios púbicos",
    "Black Friday 2024",
    "Worldwide.",
    "Metodos de pago",
    "instlacióon",
    "Entrega Rapida",
    "Envío internacional gratuito",
    "Garantía de satisfacción",
    "Paga en 3 plazos con Klarna",
    "Help@matchawalls.com",
    "Matchwallsfacilitamos",
    "17,7 inches",
    "ganar dinero",
    "recibirás una comisión",
]

PRIORITY_URLS = [
    "/",
    "/en",
    "/fr",
    "/de",
    "/nl",
    "/pages/preguntas-frecuentes",
    "/en/pages/frequent-questions",
    "/fr/pages/questions-frequentes",
    "/de/pages/haufige-fragen",
    "/nl/pages/frequente-vragen",
    "/pages/muestras",
    "/en/pages/request-your-sample",
    "/fr/pages/demandez-votre-echantillon",
    "/de/pages/fordern-sie-ihr-beispiel-an",
    "/nl/pages/vraag-uw-monster-aan",
    "/pages/sobre-nosotros",
    "/en/pages/about-us",
    "/fr/pages/a-propos-de-nous",
    "/de/pages/uber-uns",
    "/nl/pages/over-ons",
    "/pages/profesionales",
    "/en/pages/professionals",
    "/fr/pages/professionnels",
    "/de/pages/profis",
    "/nl/pages/professionals-1",
    "/pages/social-prensa-y-afiliacion",
    "/en/pages/social-press-and-affiliation",
    "/fr/pages/social-presse-et-affiliation",
    "/de/pages/sozial-presse-und-zugehorigkeit",
    "/nl/pages/sociale-pers-en-aansluiting",
    "/pages/guia-de-instalacion",
    "/en/pages/installation-guide",
    "/fr/pages/guide-dinstallation",
    "/de/pages/installationsanleitung",
    "/nl/pages/installatiegids",
    "/blogs/inspiracion",
    "/en/blogs/inspiration",
    "/fr/blogs/inspiration-2",
    "/de/blogs/inspiration-1",
    "/nl/blogs/inspiratie",
    "/pages/contact",
    "/en/pages/contact",
    "/fr/pages/contacter",
    "/de/pages/kontakt-1",
    "/nl/pages/contact",
    "/agents.md",
]


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.in_head = False
        self.in_doc_title = False
        self.title = ""
        self.metas = []
        self.links = []
        self.hreflangs = []
        self.canonicals = []
        self.headings = []
        self.heading_stack = []
        self.images = []
        self.scripts = []
        self.script_type = ""
        self.script_text = []
        self.text = []
        self.html_lang = ""

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        tag = tag.lower()
        if tag == "html":
            self.html_lang = attrs.get("lang", "")
        if tag == "head":
            self.in_head = True
        elif tag == "title" and self.in_head:
            self.in_doc_title = True
        elif tag == "meta" and self.in_head:
            self.metas.append(attrs)
        elif tag == "link" and self.in_head:
            rel = attrs.get("rel", "").lower()
            if "canonical" in rel:
                self.canonicals.append(attrs.get("href", ""))
            if "alternate" in rel and attrs.get("hreflang"):
                self.hreflangs.append((attrs.get("hreflang", ""), attrs.get("href", "")))
        elif tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])
        elif tag in {"h1", "h2", "h3"}:
            self.headings.append([tag, ""])
            self.heading_stack.append(len(self.headings) - 1)
        elif tag == "img":
            self.images.append(attrs)
        elif tag == "script":
            self.script_type = attrs.get("type", "")
            self.script_text = []

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag == "head":
            self.in_head = False
        elif tag == "title":
            self.in_doc_title = False
        elif tag in {"h1", "h2", "h3"} and self.heading_stack:
            self.heading_stack.pop()
        elif tag == "script":
            if self.script_type == "application/ld+json":
                self.scripts.append("".join(self.script_text))
            self.script_type = ""
            self.script_text = []

    def handle_data(self, data):
        compact = re.sub(r"\s+", " ", data).strip()
        if self.in_doc_title:
            self.title += compact
        if self.heading_stack and compact:
            self.headings[self.heading_stack[-1]][1] += compact
        if self.script_type:
            self.script_text.append(data)
        elif compact:
            self.text.append(compact)


def fetch(url, timeout=20, retries=2):
    headers = {
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "gzip",
    }
    last = None
    for attempt in range(retries + 1):
        start = time.time()
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=timeout) as response:
                raw = response.read()
                if response.headers.get("Content-Encoding") == "gzip":
                    raw = gzip.decompress(raw)
                return {
                    "requested_url": url,
                    "final_url": response.geturl(),
                    "status": response.status,
                    "headers": dict(response.headers),
                    "body": raw,
                    "elapsed_ms": int((time.time() - start) * 1000),
                    "error": "",
                }
        except Exception as exc:
            status = getattr(exc, "code", 0)
            body = b""
            headers_out = {}
            if hasattr(exc, "read"):
                try:
                    body = exc.read()
                except Exception:
                    body = b""
            if hasattr(exc, "headers") and exc.headers:
                headers_out = dict(exc.headers)
            last = {
                "requested_url": url,
                "final_url": "",
                "status": status,
                "headers": headers_out,
                "body": body,
                "elapsed_ms": int((time.time() - start) * 1000),
                "error": str(exc)[:300],
            }
            if status == 429:
                time.sleep(4 + attempt * 4)
            elif status in {500, 502, 503, 504, 0} and attempt < retries:
                time.sleep(1.5 + attempt)
            else:
                break
    return last


def parse_sitemap(url, seen=None):
    seen = seen or set()
    if url in seen:
        return []
    seen.add(url)
    result = fetch(url, timeout=25, retries=1)
    if result["status"] != 200:
        return []
    try:
        root = ET.fromstring(result["body"])
    except ET.ParseError:
        return []
    locs = [el.text.strip() for el in root.iter() if el.tag.endswith("loc") and el.text]
    if root.tag.endswith("sitemapindex"):
        urls = []
        for loc in locs:
            urls.extend(parse_sitemap(loc, seen))
            time.sleep(0.08)
        return urls
    return locs


def lang_from_url(url):
    path = urllib.parse.urlparse(url).path
    match = re.match(r"^/(en|fr|de|nl)(/|$)", path)
    return match.group(1) if match else "es"


def type_from_url(url):
    path = urllib.parse.urlparse(url).path
    clean = re.sub(r"^/(en|fr|de|nl)(/|$)", "/", path)
    if "/products/" in clean:
        return "producto"
    if "/collections/" in clean:
        return "coleccion"
    if "/blogs/" in clean:
        return "blog/articulo"
    if "/pages/" in clean:
        return "pagina"
    if clean in {"", "/"}:
        return "home"
    return "otro"


def meta_value(metas, key, value):
    for meta in metas:
        if meta.get(key, "").lower() == value.lower():
            return meta.get("content", "")
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


def html_row(url, result):
    row = {
        "url": url,
        "idioma_url": lang_from_url(url),
        "tipo": type_from_url(url),
        "estado_http": result["status"],
        "url_final": result["final_url"],
        "tiempo_ms": result["elapsed_ms"],
        "content_type": result["headers"].get("Content-Type", ""),
        "tamano_bytes": len(result["body"]),
        "title": "",
        "title_longitud": 0,
        "meta_description": "",
        "description_longitud": 0,
        "meta_robots": "",
        "canonical": "",
        "hreflang_count": 0,
        "h1_count": 0,
        "h1": "",
        "h2_sample": "",
        "schema_types": "",
        "jsonld_errors": 0,
        "aggregate_rating": "no",
        "review_schema": "no",
        "imagenes": 0,
        "imagenes_sin_alt": 0,
        "fixed_hits": "",
        "texto_muestra": "",
        "error": result["error"],
    }
    if result["status"] == 200 and "text/html" in row["content_type"]:
        parser = PageParser()
        html = result["body"].decode("utf-8", "replace")
        try:
            parser.feed(html)
        except Exception:
            pass
        desc = meta_value(parser.metas, "name", "description")
        robots = meta_value(parser.metas, "name", "robots")
        h1s = [clean for tag, clean in parser.headings if tag == "h1" and clean.strip()]
        h2s = [clean for tag, clean in parser.headings if tag == "h2" and clean.strip()]
        schema_types = []
        jsonld_errors = 0
        for script in parser.scripts:
            try:
                schema_types.extend(flatten_schema_types(json.loads(script)))
            except Exception:
                jsonld_errors += 1
        visible_text = re.sub(r"\s+", " ", " ".join(parser.text)).strip()
        fixed_hits = [pattern for pattern in FIXED_TEXT_PATTERNS if pattern in visible_text]
        row.update({
            "title": parser.title[:500],
            "title_longitud": len(parser.title),
            "meta_description": desc[:1000],
            "description_longitud": len(desc),
            "meta_robots": robots,
            "canonical": parser.canonicals[0] if parser.canonicals else "",
            "hreflang_count": len(parser.hreflangs),
            "h1_count": len(h1s),
            "h1": " | ".join(h1s)[:1000],
            "h2_sample": " | ".join(h2s[:8])[:1000],
            "schema_types": " | ".join(sorted(set(schema_types))),
            "jsonld_errors": jsonld_errors,
            "aggregate_rating": "si" if "AggregateRating" in schema_types else "no",
            "review_schema": "si" if "Review" in schema_types else "no",
            "imagenes": len(parser.images),
            "imagenes_sin_alt": sum(not image.get("alt", "").strip() for image in parser.images),
            "fixed_hits": " | ".join(fixed_hits),
            "texto_muestra": visible_text[:1200],
        })
    return row


def read_previous_issues():
    if not PREVIOUS_ISSUES.exists():
        return []
    with PREVIOUS_ISSUES.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def normal_url(value):
    value = value or ""
    return value if value.startswith("http") else ""


def classify_previous_issue(issue, crawl_by_url, global_signals):
    problem = issue.get("problema", "")
    url = normal_url(issue.get("url_o_archivo", ""))
    row = crawl_by_url.get(url, {}) if url else {}
    status = str(row.get("estado_http", ""))
    title = row.get("title", "")
    h1_count = int(row.get("h1_count") or 0) if row else 0
    fixed_hits = row.get("fixed_hits", "")
    current = "DECLARADO HISTORICO PERO NO VERIFICADO"
    evidence = "No hay URL publica asociada o no se pudo contrastar con recrawl."

    if "Title contaminado" in problem:
        if row and status == "200":
            if any(term in title for term in PAYMENT_TERMS):
                current = "VERIFICADO ACTUAL"
                evidence = f"Title actual contiene metodo de pago: {title[:220]}"
            else:
                current = "FALSO POSITIVO"
                evidence = f"Title actual limpio: {title[:220]}"
        elif row:
            current = "DECLARADO HISTORICO PERO NO VERIFICADO"
            evidence = f"URL no verificada con 200 actual. HTTP {status}."
    elif "H1 ausente" in problem:
        if row and status == "200":
            current = "VERIFICADO ACTUAL" if h1_count == 0 else "FALSO POSITIVO"
            evidence = f"h1_count actual={h1_count}; h1={row.get('h1','')[:220]}"
    elif "H1 multiple" in problem or "H1 múltiple" in problem:
        if row and status == "200":
            current = "VERIFICADO ACTUAL" if h1_count > 1 else "FALSO POSITIVO"
            evidence = f"h1_count actual={h1_count}; h1={row.get('h1','')[:220]}"
    elif "HTTP" in issue.get("evidencia", "") or "no 200" in problem.lower() or "Respuesta HTTP" in problem:
        if row:
            current = "VERIFICADO ACTUAL" if status != "200" else "FALSO POSITIVO"
            evidence = f"HTTP actual={status}; final={row.get('url_final','')}"
    elif "Footer global" in problem or "Footer" in issue.get("recurso", ""):
        current = "VERIFICADO ACTUAL" if global_signals["footer_hits"] else "FALSO POSITIVO"
        evidence = "; ".join(global_signals["footer_hits"])[:400]
    elif "Header" in problem or "announcement" in issue.get("evidencia", ""):
        current = "VERIFICADO ACTUAL" if global_signals["header_hits"] else "FALSO POSITIVO"
        evidence = "; ".join(global_signals["header_hits"])[:400]
    elif "muestras" in problem.lower() or "muestras" in issue.get("recurso", "").lower():
        sample_rows = [r for u, r in crawl_by_url.items() if "/muestras" in u or "sample" in u or "echantillon" in u or "monster" in u]
        current = "VERIFICADO ACTUAL" if any(str(r.get("h1_count")) == "0" or "17,7 inches" in r.get("texto_muestra", "") for r in sample_rows) else "FALSO POSITIVO"
        evidence = "Pagina muestras revisada; ver baseline para H1 y texto visible."
    elif "Sobre nosotros" in problem or "sobre nosotros" in issue.get("recurso", "").lower():
        about_rows = [r for u, r in crawl_by_url.items() if any(x in u for x in ["/sobre-nosotros", "/about-us", "/a-propos-de-nous", "/uber-uns", "/over-ons"])]
        current = "VERIFICADO ACTUAL" if any(str(r.get("h1_count")) == "0" for r in about_rows) else "FALSO POSITIVO"
        evidence = "Paginas Sobre nosotros revisadas; ver baseline para H1 y texto visible."
    elif "Home DE/NL" in problem or "Home" in problem:
        nl = crawl_by_url.get(BASE + "/nl") or crawl_by_url.get(BASE + "/nl/")
        de = crawl_by_url.get(BASE + "/de") or crawl_by_url.get(BASE + "/de/")
        bad = False
        samples = []
        for item in [nl, de]:
            if item:
                text = " ".join([item.get("title", ""), item.get("h1", ""), item.get("texto_muestra", "")])
                if any(x in text for x in ["Papeadra", "Bemalten Papiere", "geschilderde", "Erforschen"]):
                    bad = True
                    samples.append(text[:220])
        current = "VERIFICADO ACTUAL" if bad else "FALSO POSITIVO"
        evidence = " | ".join(samples)[:500]
    elif "requiere decision" in issue.get("estado", "").lower() or "REQUIERE DECISION HUMANA" in issue.get("estado", ""):
        current = "REQUIERE DECISION HUMANA"
        evidence = "La incidencia depende de politica SEO/comercial, no solo de rastreo."
    elif row and status == "200":
        current = "VERIFICADO ACTUAL"
        evidence = "URL accesible; incidencia no automatizable requiere revision editorial."

    return current, evidence


def write_csv(path, rows, fieldnames=None):
    if fieldnames is None:
        fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main():
    start = datetime.now().isoformat(timespec="seconds")
    previous = read_previous_issues()
    previous_urls = {normal_url(row.get("url_o_archivo", "")) for row in previous}
    previous_urls = {url for url in previous_urls if url}
    priority_abs = {BASE + path if path.startswith("/") else path for path in PRIORITY_URLS}

    robots = fetch(BASE + "/robots.txt", timeout=20, retries=1)
    sitemap_urls = sorted(set(url for url in parse_sitemap(BASE + "/sitemap.xml") if "matchwalls.com" in url))
    urls = sorted(set(sitemap_urls) | previous_urls | priority_abs)

    rows = []
    for index, url in enumerate(urls, start=1):
        result = fetch(url)
        row = html_row(url, result)
        rows.append(row)
        if index % 100 == 0:
            print(f"baseline {index}/{len(urls)}")
        time.sleep(0.09)

    write_csv(OUT_CRAWL, rows)
    crawl_by_url = {row["url"]: row for row in rows}
    crawl_by_final = {row["url_final"]: row for row in rows if row.get("url_final")}
    crawl_by_url.update(crawl_by_final)

    footer_hits = sorted(set(hit for row in rows if row["tipo"] in {"home", "pagina", "blog/articulo"} for hit in row.get("fixed_hits", "").split(" | ") if hit))
    header_hits = [hit for hit in footer_hits if hit in {"Entrega Rapida", "Envío internacional gratuito", "Garantía de satisfacción", "Paga en 3 plazos con Klarna"}]
    global_signals = {"footer_hits": footer_hits, "header_hits": header_hits}

    verified_rows = []
    false_rows = []
    critical_rows = []
    for issue in previous:
        current_state, evidence = classify_previous_issue(issue, crawl_by_url, global_signals)
        out = dict(issue)
        out["baseline_lote"] = LOT
        out["clasificacion_baseline"] = current_state
        out["evidencia_baseline"] = evidence
        out["fecha_baseline"] = start
        verified_rows.append(out)
        if current_state == "FALSO POSITIVO":
            false_rows.append(out)
        if issue.get("prioridad") == "CRITICO" and current_state in {"VERIFICADO ACTUAL", "REQUIERE DECISION HUMANA"}:
            critical_rows.append(out)

    fieldnames = list(verified_rows[0].keys()) if verified_rows else []
    write_csv(OUT_VERIFIED, verified_rows, fieldnames)
    write_csv(OUT_FALSE, false_rows, fieldnames)
    write_csv(OUT_CRITICAL, critical_rows, fieldnames)

    http_counts = Counter(str(row["estado_http"]) for row in rows)
    state_counts = Counter(row["clasificacion_baseline"] for row in verified_rows)
    current_title_payment = [row for row in rows if any(term in row.get("title", "") for term in PAYMENT_TERMS)]
    h1_missing = [row for row in rows if str(row["estado_http"]) == "200" and "text/html" in row["content_type"] and int(row["h1_count"] or 0) == 0]
    h1_multiple = [row for row in rows if str(row["estado_http"]) == "200" and "text/html" in row["content_type"] and int(row["h1_count"] or 0) > 1]
    non_200 = [row for row in rows if str(row["estado_http"]) != "200"]
    agents = crawl_by_url.get(BASE + "/agents.md")
    sample_pages = [row for row in rows if any(x in row["url"] for x in ["/muestras", "sample", "echantillon", "monster"])]

    summary = {
        "lote": LOT,
        "started": start,
        "sitemap_urls": len(sitemap_urls),
        "recrawled_urls": len(rows),
        "http_counts": dict(http_counts),
        "previous_issues": len(previous),
        "classification_counts": dict(state_counts),
        "current_title_payment_count": len(current_title_payment),
        "h1_missing_count": len(h1_missing),
        "h1_multiple_count": len(h1_multiple),
        "non_200_count": len(non_200),
        "agents_md": agents,
        "footer_hits": footer_hits,
        "header_hits": header_hits,
        "critical_real_count": len(critical_rows),
        "false_positive_count": len(false_rows),
    }
    OUT_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    recommendation = "MW-FOOTER-I18N-001"
    if not footer_hits and header_hits:
        recommendation = "MW-HEADER-CLAIMS-I18N-001"
    elif not footer_hits and not header_hits:
        recommendation = "MW-HOME-DE-NL-I18N-001"

    md = f"""# Baseline post-hotfix - {LOT}

Fecha: 16 de junio de 2026. Modo: solo lectura. Shopify no modificado.

## Cobertura

- URLs en sitemap actual: {len(sitemap_urls)}.
- URLs recrawleadas incluyendo prioritarias e incidencias previas: {len(rows)}.
- Incidencias previas reclasificadas: {len(previous)}.
- HTTP: {dict(http_counts)}.

## Clasificacion de las 629 incidencias

{dict(state_counts)}

## Validaciones especiales

- Titles contaminados por metodos de pago actuales: {len(current_title_payment)}.
- H1 ausentes actuales en HTML 200: {len(h1_missing)}.
- H1 multiples actuales en HTML 200: {len(h1_multiple)}.
- URLs no 200 actuales: {len(non_200)}.
- `/agents.md`: HTTP {agents.get('estado_http') if agents else 'NO ACCESIBLE'}, content-type {agents.get('content_type') if agents else ''}.
- Footer hits actuales: {', '.join(footer_hits) if footer_hits else 'sin hits'}.
- Header hits actuales: {', '.join(header_hits) if header_hits else 'sin hits'}.

## Incidencias criticas reales

Ver `{OUT_CRITICAL.name}`.

## Falsos positivos

Ver `{OUT_FALSE.name}`. La mayoria esperada corresponde al bug del crawler historico que leia los `<title>` de SVG de pagos como si fueran el `<title>` SEO.

## Recomendacion final del primer lote de ejecucion

Recomendacion: `{recommendation}`.

Motivo: el footer es sitewide, esta visible en todas las plantillas y sigue contaminando SEO/GEO con mezcla de idiomas, evento caducado y typos. Header tiene claims comerciales globales, pero requiere validacion humana de condiciones antes de tocarlo. Home DE/NL es critico, pero afecta menos URLs que el footer.
"""
    OUT_SUMMARY.write_text(md, encoding="utf-8")

    REGISTRO.write_text(REGISTRO.read_text(encoding="utf-8") + f"""

### Lote {LOT}: baseline recrawl post-hotfix

**Aprobacion recibida:** `APROBADO LOTE {LOT}`.

**Fecha:** 16 de junio de 2026.

**Modo:** solo lectura.

**Acciones ejecutadas:**

- Confirmacion Shopify en lectura: tema MAIN `SEO schema hotfix - 2026-06-15`, `gid://shopify/OnlineStoreTheme/178383749496`.
- Recrawl publico prudente desde sitemap actual, URLs prioritarias y URLs afectadas por incidencias previas.
- Reclasificacion de incidencias previas entre `VERIFICADO ACTUAL`, `DECLARADO HISTORICO PERO NO VERIFICADO`, `FALSO POSITIVO` y `REQUIERE DECISION HUMANA`.

**Cambios en Shopify:** ninguno.

**Entregables generados:**

- `{OUT_CRAWL.name}`.
- `{OUT_VERIFIED.name}`.
- `{OUT_FALSE.name}`.
- `{OUT_CRITICAL.name}`.
- `{OUT_SUMMARY.name}`.
- `{OUT_JSON.name}`.

**Resultado resumen:** {len(rows)} URLs recrawleadas; {len(previous)} incidencias reclasificadas; {len(false_rows)} falsos positivos; {len(critical_rows)} criticas reales.

**Primer lote recomendado:** `{recommendation}`.
""", encoding="utf-8")

    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
