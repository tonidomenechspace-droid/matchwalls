import csv
import json
import re
from pathlib import Path

ROOT = Path(r"C:\Users\d.bermejo\OneDrive - Matchwalls\Documentos\Matchwalls Shopify")
AUDIT = ROOT / "auditoria-seo-geo-matchwalls"
INVENTORY = AUDIT / "inventario-urls.csv"
SITEMAP = AUDIT / "sitemap-urls.txt"
REGISTRO = AUDIT / "registro-cambios-ejecutados.md"

LANGS = {"es", "en", "fr", "de", "nl"}
PAYMENT_TERMS = [
    "American Express",
    "Apple Pay",
    "Bancontact",
    "Google Pay",
    "Maestro",
    "Mastercard",
    "PayPal",
    "Shop Pay",
    "Union Pay",
    "Visa",
]


def clean(value, limit=260):
    text = re.sub(r"\s+", " ", (value or "").replace("\r", " ").replace("\n", " ")).strip()
    return text if len(text) <= limit else text[: limit - 1] + "..."


def lang_from_url(url):
    match = re.search(r"matchwalls\.com/([a-z]{2})(?:/|$)", url or "")
    if match and match.group(1) in LANGS:
        return match.group(1)
    return "es"


def type_from_url(url):
    url = url or ""
    if "/products/" in url:
        return "producto"
    if "/collections/" in url:
        return "coleccion"
    if "/blogs/" in url:
        return "blog/articulo"
    if "/pages/" in url:
        return "pagina"
    if re.search(r"matchwalls\.com/(?:[a-z]{2})?/?$", url):
        return "home"
    return "otro"


def read_csv(path):
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def read_sitemap(path):
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", errors="ignore") as handle:
        return [line.strip() for line in handle if line.strip().startswith("http")]


def int_value(value, default=0):
    try:
        return int(float(value or default))
    except Exception:
        return default


def add_problem(items, tipo, idioma, recurso, problema, evidencia, url, prioridad, estado,
                impacto_seo, impacto_geo, impacto_comercial, recomendacion, fuente, lote):
    items.append({
        "id": f"MW-CONT-{len(items) + 1:04d}",
        "tipo_recurso": tipo,
        "idioma": idioma,
        "recurso": recurso,
        "problema": problema,
        "evidencia": clean(evidencia, 500),
        "url_o_archivo": url,
        "fuente": fuente,
        "estado": estado,
        "prioridad": prioridad,
        "impacto_seo": impacto_seo,
        "impacto_geo_llmo": impacto_geo,
        "impacto_comercial": impacto_comercial,
        "solucion_recomendada": recomendacion,
        "siguiente_lote_recomendado": lote,
    })


def main():
    rows = read_csv(INVENTORY)
    sitemap_urls = read_sitemap(SITEMAP)
    problems = []
    h1_meta = []

    for row in rows:
        url = row.get("url", "")
        if "matchwalls.com" not in url:
            continue
        idioma = row.get("idioma_url") or lang_from_url(url)
        if idioma not in LANGS:
            continue
        tipo = row.get("tipo") or type_from_url(url)
        status = str(row.get("estado_http", "")).strip()
        title = row.get("title", "")
        meta = row.get("meta_description", "")
        h1 = row.get("h1", "")
        h1_count = int_value(row.get("h1_count"))
        title_len = int_value(row.get("title_longitud"), len(title))
        meta_len = int_value(row.get("description_longitud"), len(meta))

        if status in {"500", "0"}:
            add_problem(
                problems, tipo, idioma, "URL rastreada", "Respuesta HTTP no 200 en inventario rastreado",
                f"HTTP {status}", url, "ALTO", "INCORRECTO",
                "Puede impedir indexacion o transferir senales a URL incorrectas.",
                "IA y buscadores no pueden citar una URL no accesible de forma estable.",
                "Riesgo de perdida de sesiones organicas y ventas.",
                "Revisar destino, redireccion, canonical y enlazado interno.",
                "inventario-urls.csv", "MW-TECH-404-REDIRECTS-001",
            )
            continue

        # Empty status means the URL came from sitemap expansion but was not crawled.
        # 429 means Shopify rate-limited the previous crawl. Neither is a verified page-quality error.
        if status not in {"200", "200.0"}:
            continue

        if h1_count == 0:
            add_problem(
                problems, tipo, idioma, "H1", "H1 ausente", f"h1_count=0; title={title}", url,
                "ALTO", "INCORRECTO",
                "Reduce claridad semantica e intencion principal.",
                "Los sistemas IA reciben menos senal estructurada sobre el tema principal.",
                "Menor claridad para usuarios y menor conversion.",
                "Anadir un unico H1 descriptivo, localizado y alineado con la busqueda principal.",
                "inventario-urls.csv", "MW-H1-METAS-I18N-001",
            )
            h1_meta.append({
                "url": url, "idioma": idioma, "tipo": tipo, "problema": "H1 ausente",
                "evidencia": f"h1_count={h1_count}", "title": title,
                "meta_description": meta, "prioridad": "ALTO",
            })
        elif h1_count > 1:
            add_problem(
                problems, tipo, idioma, "H1", "H1 multiple", f"h1_count={h1_count}; h1={h1}", url,
                "MEDIO", "VERIFICADO PERO MEJORABLE",
                "Puede diluir la jerarquia de contenidos.",
                "Dificulta extraer una respuesta principal clara.",
                "Puede confundir en landings transaccionales.",
                "Dejar un solo H1 y convertir el resto en H2/H3.",
                "inventario-urls.csv", "MW-H1-METAS-I18N-001",
            )

        if any(term in title for term in PAYMENT_TERMS):
            # Historical crawler artifact: the current public render of 45 priority URLs
            # showed clean document.title values after the hotfix. Keep as re-crawl evidence,
            # not as a confirmed current Shopify defect.
            add_problem(
                problems, tipo, idioma, "Meta title", "Title contaminado por metodos de pago en inventario historico",
                title, url, "MEDIO", "DECLARADO PERO NO VERIFICADO",
                "Debe revalidarse con un rastreo post-hotfix antes de corregir plantillas.",
                "No se debe alimentar una decision GEO con evidencia historica refutada por render actual parcial.",
                "Evita priorizar un falso positivo sobre problemas visibles actuales.",
                "Re-rastrear titles actuales; si se confirma, abrir lote tecnico especifico.",
                "inventario-urls.csv historico + render publico parcial 2026-06-16", "MW-RECRAWL-TITLES-001",
            )
            continue
        if not title.strip():
            add_problem(
                problems, tipo, idioma, "Meta title", "Title ausente", "Sin title", url,
                "CRITICO", "INCORRECTO", "Pagina sin titulo SEO.", "Se pierde senal principal para resumen/citacion.",
                "CTR bajo o snippet pobre.", "Definir title localizado unico.",
                "inventario-urls.csv", "MW-H1-METAS-I18N-001",
            )
        elif title_len < 28:
            add_problem(
                problems, tipo, idioma, "Meta title", "Title demasiado corto o debil", title, url,
                "MEDIO", "VERIFICADO PERO MEJORABLE", "No aprovecha la intencion de busqueda.",
                "Poca entidad semantica para IA.", "Menor CTR potencial.",
                "Ampliar title con producto/categoria + marca sin sobreoptimizar.",
                "inventario-urls.csv", "MW-H1-METAS-I18N-001",
            )
        elif title_len > 70:
            add_problem(
                problems, tipo, idioma, "Meta title", "Title largo", title, url,
                "MEDIO", "VERIFICADO PERO MEJORABLE", "Riesgo de truncado y baja claridad en SERP.",
                "Resumen menos preciso para IA.", "CTR menor.",
                "Reducir a propuesta clara de 45-65 caracteres por idioma.",
                "inventario-urls.csv", "MW-H1-METAS-I18N-001",
            )

        if not meta.strip():
            add_problem(
                problems, tipo, idioma, "Meta description", "Meta description ausente", "Sin meta description", url,
                "ALTO", "INCORRECTO", "Snippet menos controlado.", "Menos contexto para resumen IA.",
                "Menor CTR potencial.", "Definir meta description unica y localizada.",
                "inventario-urls.csv", "MW-H1-METAS-I18N-001",
            )
        elif meta_len < 70:
            add_problem(
                problems, tipo, idioma, "Meta description", "Meta description corta o poco informativa", meta, url,
                "MEDIO", "VERIFICADO PERO MEJORABLE", "Desaprovecha snippet e intencion.",
                "Poca explicacion para IA.", "Puede reducir CTR.",
                "Redactar 120-155 caracteres con beneficio, producto e intencion.",
                "inventario-urls.csv", "MW-H1-METAS-I18N-001",
            )
        elif meta_len > 170:
            add_problem(
                problems, tipo, idioma, "Meta description", "Meta description larga", meta, url,
                "MEDIO", "VERIFICADO PERO MEJORABLE", "Riesgo de truncado y mensajes inconsistentes.",
                "IA puede recibir contenido redundante o cortado.", "CTR menor.",
                "Reducir a 120-155 caracteres por idioma.",
                "inventario-urls.csv", "MW-H1-METAS-I18N-001",
            )

        if row.get("posible_mezcla_idioma", "").lower() in {"si", "yes", "true", "1"}:
            add_problem(
                problems, tipo, idioma, "Contenido visible", "Posible mezcla de idioma detectada en rastreo",
                f"title={title}; h1={h1}", url, "ALTO", "INCOMPLETO",
                "Puede afectar relevancia internacional y calidad percibida.",
                "Reduce confianza de sistemas IA al resumir/citar en el idioma correcto.",
                "Disminuye confianza y conversion.",
                "Revision humana por idioma y correccion controlada.",
                "inventario-urls.csv", "MW-I18N-CONTENT-FIX-001",
            )
        if row.get("handle_sospechoso", "").lower() in {"si", "yes", "true", "1"}:
            add_problem(
                problems, tipo, idioma, "URL/handle", "Handle sospechoso o inconsistente", url, url,
                "ALTO", "VERIFICADO PERO MEJORABLE",
                "Puede afectar CTR, relevancia e intencion si el slug contiene typos o idioma incorrecto.",
                "Las IA leen slugs como senal semantica adicional.",
                "Riesgo de baja confianza y mala comparticion.",
                "No cambiar URL sin analisis de trafico/redireccion; preparar lote especifico.",
                "inventario-urls.csv", "MW-HANDLES-URL-GOVERNANCE-001",
            )
        if row.get("patron_muestra", "").lower() in {"si", "yes", "true", "1"}:
            add_problem(
                problems, tipo, idioma, "Producto muestra",
                "Muestra potencialmente indexable o competidora del producto principal",
                f"patron_muestra={row.get('patron_muestra')}; title={title}", url,
                "ALTO", "REQUIERE DECISION HUMANA",
                "Puede canibalizar producto principal y multiplicar thin content.",
                "IA puede citar muestras en lugar del mural/rollo principal.",
                "Usuarios pueden aterrizar en producto de bajo ticket o incompleto.",
                "Decidir politica: indexar con contenido unico o subordinarlas/noindex/canonical.",
                "inventario-urls.csv", "MW-SAMPLES-SEO-POLICY-001",
            )

    status_blank = sum(1 for row in rows if not str(row.get("estado_http", "")).strip())
    status_429 = sum(1 for row in rows if str(row.get("estado_http", "")).strip() == "429")
    if status_blank or status_429:
        add_problem(
            problems, "rastreo", "ES/EN/FR/DE/NL", "Cobertura de rastreo",
            "Parte del inventario local no tiene verificacion HTTP 200 actual",
            f"URLs sin estado HTTP: {status_blank}; URLs con 429 en rastreo previo: {status_429}. No se tratan como errores editoriales actuales.",
            "inventario-urls.csv", "MEDIO", "INCOMPLETO",
            "Hace falta recrawl prudente post-hotfix para cerrar H1/metas de todo el sitemap.",
            "Sin recrawl completo, no se puede afirmar calidad GEO del 100% de URLs.",
            "Evita priorizar falsos positivos y permite ordenar siguientes lotes por evidencia real.",
            "Ejecutar rastreo paginado y lento, con backoff, y comparar contra sitemap actual.",
            "inventario-urls.csv", "MW-RECRAWL-CONTENIDO-I18N-001",
        )

    verified = [
        ("tema/header", "ES/EN/FR/DE/NL", "sections/header-group.json",
         "Claims globales fijos en announcement bar",
         "Textos fijos: 'Envio internacional gratuito', 'Paga en 3 plazos con Klarna', 'Garantia de satisfaccion', 'Entrega Rapida'.",
         "CRITICO", "RIESGO CRITICO", "MW-HEADER-CLAIMS-I18N-001"),
        ("tema/footer", "ES/EN/FR/DE/NL", "sections/footer-group.json + menus footer",
         "Footer global con errores y mezcla de idiomas",
         "Render ES: 'espacios pubicos' con tilde correcta en publico pero en menu Admin consta 'espacios púbicos'; tambien 'FAQ´S', 'Black Friday 2024', 'Worldwide.', 'Metodos', 'instlacioon'.",
         "CRITICO", "INCORRECTO", "MW-FOOTER-I18N-001"),
        ("pagina FAQ", "ES/EN/FR/DE/NL", "templates/page.faq.json",
         "FAQ visible mezcla contenido guardado y bloques fijos del tema",
         "Plantilla contiene FAQ fijas sobre envios, pagos, pedidos, PayPal/Amazon Pay/financiacion, garantia y email erroneo 'Help@matchawalls.com'.",
         "CRITICO", "RIESGO CRITICO", "MW-FAQ-TEMPLATE-I18N-001"),
        ("pagina muestras", "ES/EN/FR/DE/NL", "templates/page.muestras-2.json",
         "Pagina de muestras sin H1 y gobernada por plantilla fija",
         "Render publico: h1_count=0 en ES/EN/FR y textos de plantilla; evidencia: '17,7 inches' para 29,7 cm x 21 cm, main-page disabled true.",
         "CRITICO", "INCORRECTO", "MW-MUESTRAS-I18N-H1-001"),
        ("pagina guia", "ES/EN/FR/DE/NL", "templates/page.guias-de-instalacion.json",
         "Guia de instalacion depende de PDFs y plantilla fija",
         "main-page disabled true; texto fijo 'Descarga y escoge...' con comilla final extra; enlaces file:/// en bloques desactivados; poco HTML instructivo indexable.",
         "ALTO", "INCOMPLETO", "MW-GUIA-INSTALACION-GEO-001"),
        ("pagina profesionales", "ES/EN/FR/DE/NL", "templates/page.profesionales.json",
         "Contenido B2B parcialmente fijo y no gobernado por una sola fuente",
         "Plantilla fija: hero, tipos de cuenta, CTA, enlaces a tiendas/horeca/estudios; h0 en hero y bloques localizados por app/tema.",
         "ALTO", "INCOMPLETO", "MW-PROFESIONALES-I18N-GEO-001"),
        ("pagina social/prensa/afiliacion", "ES/EN/FR/DE/NL", "templates/page.social_prensa_afiliacion.json",
         "Afiliacion/prensa muestra promesas y testimonios no validados",
         "Render ES: 'ganar dinero', 'recibiras una comision'. Plantilla contiene quotes con rating 4 y autores @ArtGallery, Dani, @GourmetBistro.",
         "CRITICO", "RIESGO CRITICO", "MW-SOCIAL-PRESS-AFFILIATE-001"),
        ("pagina sobre nosotros", "ES/EN/FR/DE/NL", "render publico",
         "Sobre nosotros sin H1 y traducciones automaticas visibles",
         "Render: h1_count=0 en ES/EN/FR/DE/NL. FR: 'Nous sommes des matchs d’allumettes'. NL/DE con frases literales.",
         "ALTO", "INCORRECTO", "MW-ABOUT-ENTITY-I18N-001"),
        ("home", "DE/NL", "render publico",
         "Home DE/NL con traduccion automatica deficiente",
         "DE H1: 'Bemalten Papiere für Wände und Wandgemälde'. NL H1: 'Matchwalls: Papeadra Papel -specialisten'; title NL sigue en espanol.",
         "CRITICO", "INCORRECTO", "MW-HOME-DE-NL-I18N-001"),
        ("blog", "EN/FR/DE/NL", "render publico + articulos Admin",
         "Blog con traducciones literales y articulos sin auditoria individual",
         "Render blog: EN literal; FR 'n'abonnez pas'; Admin: 11 articulos publicados, uno con handle 'transfroma'.",
         "ALTO", "INCOMPLETO", "MW-BLOG-I18N-ARTICLE-001"),
        ("paginas geograficas", "EN/DE/NL", "Admin lectura previa + inventario",
         "Paginas geograficas con traduccion literal de toponimos y bajo valor",
         "Papel Pintado Espana/Francia: EN/DE/NL traducen ciudades como Cuenca/Basin/Becken, Granada/Grenade/Granate, Leon/Lion/Lowe, Nice/Hubsch/Leuk; enlaces internos a URLs ES.",
         "ALTO", "INCORRECTO", "MW-GEO-PAGES-GOVERNANCE-001"),
        ("catalogo/muestras", "ES/EN/FR/DE/NL", "sitemap + inventario",
         "Politica SEO de muestras no definida",
         "Sitemap/inventario incluye muchas URLs de producto y muestras; patron_muestra pendiente.",
         "ALTO", "REQUIERE DECISION HUMANA", "MW-SAMPLES-SEO-POLICY-001"),
    ]

    for tipo, idioma, archivo, problema, evidencia, prioridad, estado, lote in verified:
        add_problem(
            problems, tipo, idioma, archivo, problema, evidencia, archivo, prioridad, estado,
            "Afecta a indexabilidad, relevancia, arquitectura semantica o calidad del snippet.",
            "Afecta a comprension, respuesta y citabilidad por sistemas IA.",
            "Afecta a confianza, conversion o captacion B2B.",
            "Preparar lote pequeno, valores actuales/propuestos y QA ES/EN/FR/DE/NL antes de tocar Shopify.",
            "Shopify Admin + render publico 2026-06-16", lote,
        )

    fixed_rows = [
        ("sections/header-group.json", "announcement-bar",
         "Envio internacional gratuito / Paga en 3 plazos con Klarna / Garantia de satisfaccion / Entrega Rapida",
         "ES/EN/FR/DE/NL", "Claims globales fijos sin validacion por mercado; typo Entrega Rapida", "RIESGO CRITICO", "CRITICO",
         "Validar condiciones reales y localizar por mercado."),
        ("sections/footer-group.json", "newsletter + text-with-icons",
         "NOTICIAS, INSPIRACION, REGALOS Y NOVEDADES; Worldwide.; Metodos de pago seguros y financiacion.; Descargate nuestras guias de facil instlacioon.",
         "ES/EN/FR/DE/NL", "Texto fijo global, mezcla ES/EN, typos y claims no validados.", "INCORRECTO", "CRITICO",
         "Corregir y localizar footer global."),
        ("menus footer/footer-profesional/footer-brand", "menus",
         "espacios pubicos/púbicos; FAQ´S; Black Friday 2024; Professionals; PROFESIONALES/EMPRESA en NL/FR",
         "ES/EN/FR/DE/NL", "Menus visibles con typos, evento caducado y mezcla de idiomas.", "INCORRECTO", "CRITICO",
         "Revisar menus y traducciones publicadas por idioma."),
        ("templates/page.faq.json", "faq_8qxHKU / faq_QqAKyK / faq_XqEQcD",
         "FAQ fijas de envios, pagos, pedidos, PayPal, Amazon Pay, financiacion, garantia, Help@matchawalls.com",
         "ES/EN/FR/DE/NL", "Bloques fijos pueden sobrescribir o duplicar contenido guardado; claims no validados.", "RIESGO CRITICO", "CRITICO",
         "Unificar FAQ en una fuente gobernada y validar claims."),
        ("templates/page.muestras-2.json", "main disabled + rich_text + multi_column",
         "Acerca de nuestras muestras; 29,7cm x 21cm / 17,7 inches x 8,3 inches; Elije; Non-Woven, Vinyl, Metallic, Peel & Stick",
         "ES/EN/FR/DE/NL", "Sin H1 visible; medidas incorrectas; textos y claims fijos no validados.", "INCORRECTO", "CRITICO",
         "Corregir H1, medidas, claims y traducciones humanas."),
        ("templates/page.guias-de-instalacion.json", "main disabled + accordion + disabled file links",
         "Descarga y escoge nuestras guias...; file:///C:/Users/esthe/Downloads/...; Play MatchWalls",
         "ES/EN/FR/DE/NL", "Contenido HTML pobre, dependencia de PDF, enlaces locales en bloques desactivados.", "INCOMPLETO", "ALTO",
         "Crear guia HTML localizable con PDFs como soporte."),
        ("templates/page.profesionales.json", "hero + multi_column + CTAs",
         "EL EQUIPO QUE TE ACOMPANA...; TIPOS DE CUENTA; beneficios unicos; DESCUBRIR VENTAJAS",
         "ES/EN/FR/DE/NL", "B2B clave con bloques fijos y claims sin evidencia comercial.", "INCOMPLETO", "ALTO",
         "Revisar propuesta B2B y localizar humanamente."),
        ("templates/page.social_prensa_afiliacion.json", "tabs / media / press",
         "ganar dinero; recibiras una comision; quotes con rating 4; Share; Social@matchwalls.com",
         "ES/EN/FR/DE/NL", "Promesas de afiliacion, resenas y uso de imagenes no validados.", "RIESGO CRITICO", "CRITICO",
         "Reconstruir como prensa/colaboraciones con condiciones validadas."),
    ]

    output_problems = AUDIT / "inventario-problemas-contenido-i18n-geo-2026-06-16.csv"
    output_fixed = AUDIT / "textos-fijos-plantilla-bloqueantes-2026-06-16.csv"
    output_h1 = AUDIT / "h1-metadatos-i18n-geo-2026-06-16.csv"
    output_md = AUDIT / "auditoria-contenido-i18n-geo-2026-06-16.md"
    output_lotes = AUDIT / "siguientes-lotes-contenido-i18n-geo-2026-06-16.md"

    with output_problems.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(problems[0].keys()))
        writer.writeheader()
        writer.writerows(problems)

    with output_fixed.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=[
            "archivo", "bloque", "texto", "idiomas_afectados", "problema",
            "estado", "prioridad", "accion",
        ])
        writer.writeheader()
        for row in fixed_rows:
            writer.writerow({
                "archivo": row[0], "bloque": row[1], "texto": row[2],
                "idiomas_afectados": row[3], "problema": row[4],
                "estado": row[5], "prioridad": row[6], "accion": row[7],
            })

    with output_h1.open("w", encoding="utf-8-sig", newline="") as handle:
        fieldnames = ["url", "idioma", "tipo", "problema", "evidencia", "title", "meta_description", "prioridad"]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(h1_meta)

    by_priority = {}
    by_lang = {}
    for problem in problems:
        by_priority[problem["prioridad"]] = by_priority.get(problem["prioridad"], 0) + 1
        by_lang[problem["idioma"]] = by_lang.get(problem["idioma"], 0) + 1

    lang_counts = {lang: 0 for lang in LANGS}
    for url in sitemap_urls:
        lang = lang_from_url(url)
        if lang in lang_counts:
            lang_counts[lang] += 1

    md = f"""# Auditoria contenido, i18n y GEO/LLMO - MW-AUDIT-CONTENIDO-I18N-GEO-001

Fecha: 16 de junio de 2026. Modo: solo lectura. Shopify no modificado.

## Fuentes verificadas

- `AGENTS.md` y registros del proyecto leidos y aplicados.
- Shopify Admin GraphQL en modo lectura: tema MAIN, locales publicados, menus, paginas, articulos, primera pagina de productos activos y colecciones.
- Tema MAIN verificado: `SEO schema hotfix - 2026-06-15`, `gid://shopify/OnlineStoreTheme/178383749496`, rol `MAIN`, sin procesamiento fallido.
- Render publico actual de 45 URLs prioritarias: home, FAQ, profesionales, muestras, guia, contacto, sobre nosotros, social/prensa/afiliacion y blog en ES, EN, FR, DE y NL.
- Inventario local existente: `inventario-urls.csv` y `sitemap-urls.txt`.

## Cobertura y limitaciones

- Sitemap local: {len(sitemap_urls)} URLs inventariadas. Distribucion por idioma: {', '.join(f'{k}: {v}' for k, v in sorted(lang_counts.items()))}.
- Inventario rastreado previo: {len(rows)} filas. Se usa para detectar patrones de H1, title, meta, handles y muestras.
- La auditoria editorial completa producto a producto para los cerca de 2.600 SKUs y sus traducciones no queda cerrada con este lote: requiere exportacion/API paginada especifica y revision humana por familias. Estado: `INCOMPLETO`.
- No se validaron datos externos como Search Console, Bing Webmaster Tools, Merchant Center, Trustpilot o condiciones legales/pagos. Los claims comerciales quedan como `DECLARADO PERO NO VERIFICADO` o `RIESGO CRITICO` cuando se usan globalmente.

## Estado verificado

- El hotfix de schema esta publicado como MAIN y el QA anterior lo dejo `CORREGIDO Y VERIFICADO` para GTIN/MPN falsos y AggregateRating corporativo fijo.
- El programa SEO/GEO sigue `EN CURSO - NO CERRADO`: quedan pendientes footer, paginas corporativas/B2B, blog, muestras, guia, colecciones, catalogo e internacionalizacion DE/NL.
- Idiomas publicados en Shopify: ES primario, EN, FR, DE, NL, IT y PT-PT. Este lote audita ES/EN/FR/DE/NL.

## Hallazgos principales

### Footer global incorrecto
Afecta a todas las paginas. Se verifican errores `espacios púbicos`, `FAQ´S`, `Black Friday 2024`, `Worldwide.`, `Metodos`, `instlacioon` y mezcla de cabeceras ES en NL/FR.

### Header con claims comerciales globales
`Envio internacional gratuito`, `Paga en 3 plazos con Klarna`, `Garantia de satisfaccion` y `Entrega Rapida` aparecen como texto fijo de tema. Requieren validacion por mercado.

### Home DE/NL no apta para mercado
DE muestra `Bemalten Papiere fuer Waende und Wandgemaelde`; NL mantiene title ES y H1 `Papeadra Papel -specialisten`. Es critico para SEO internacional.

### Muestras sin H1 y con datos incorrectos
La pagina `/pages/muestras` y variantes EN/FR verificadas tienen `h1_count=0`; contiene conversion erronea `29,7cm x 21cm / 17,7 inches x 8,3 inches`.

### Sobre nosotros sin H1 en cinco idiomas
La pagina de entidad de marca no tiene H1 y en FR/NL/DE muestra traduccion automatica/literal, danando GEO/LLMO.

### Social/Prensa/Afiliacion con promesas no validadas
Se muestran `ganar dinero`, `recibiras una comision` y testimonios/ratings de plantilla. Riesgo critico.

### FAQ con bloques fijos y claims no validados
Plantilla contiene envios, pagos, PayPal/Amazon Pay, financiacion, garantia y email erroneo `Help@matchawalls.com`.

### Guia de instalacion pobre para GEO
Depende de PDFs, main-page desactivado y texto HTML corto. Necesita guia HTML paso a paso por idioma.

### Blog pendiente de auditoria articulo a articulo
Hay 11 articulos publicados; render del blog muestra traducciones literales y Admin confirma handle con typo `transfroma`.

### Arquitectura de colecciones y muestras sin decision
Coleccion `/collections/murales` se llama `Todos los Papeles Pintados`; las muestras pueden canibalizar productos principales.

## Resumen cuantitativo

- Incidencias documentadas: {len(problems)}.
- Matriz H1/metas: {len(h1_meta)} filas.
- Por prioridad: {', '.join(f'{k}: {v}' for k, v in sorted(by_priority.items()))}.
- Por idioma/recurso: {', '.join(f'{k}: {v}' for k, v in sorted(by_lang.items()))}.

## Entregables generados

- `{output_problems.name}`.
- `{output_fixed.name}`.
- `{output_h1.name}`.
- `{output_lotes.name}`.

## Decision recomendada

No ejecutar cambios masivos. El siguiente lote mas seguro y de mayor impacto es corregir footer/header global por idioma, porque afecta a todas las URLs y actualmente contamina SEO, confianza y GEO/LLMO.
"""
    output_md.write_text(md, encoding="utf-8")

    output_lotes.write_text("""# Siguientes lotes recomendados - contenido i18n GEO

Modo recomendado: lotes pequeños, reversibles y con QA publico ES/EN/FR/DE/NL.

## 1. MW-FOOTER-I18N-001 - CRITICO
Alcance: footer menus, newsletter/footer trust blocks y traducciones visibles. Corregir `espacios púbicos`, `FAQ´S`, `Black Friday 2024`, `Worldwide.`, `Metodos`, `instlacioon` y cabeceras ES en NL/FR.

## 2. MW-HEADER-CLAIMS-I18N-001 - CRITICO
Alcance: announcement bar. Validar o condicionar `Envio internacional gratuito`, `Klarna`, `Garantia de satisfaccion`, `Entrega Rapida` por mercado.

## 3. MW-HOME-DE-NL-I18N-001 - CRITICO
Alcance: home DE/NL. Reescritura humana de H1, hero, categorias, CTAs y metadatos; corregir title NL en espanol.

## 4. MW-MUESTRAS-I18N-H1-001 - CRITICO
Alcance: pagina de muestras ES/EN/FR/DE/NL. Añadir H1, corregir medidas, validar calidades/materiales y localizar contenido visible.

## 5. MW-FAQ-TEMPLATE-I18N-001 - CRITICO
Alcance: FAQ visible + schema FAQPage. Retirar duplicidades, corregir `Help@matchawalls.com`, validar pagos, envios, plazos, financiacion y garantia.

## 6. MW-ABOUT-ENTITY-I18N-001 - ALTO
Alcance: Sobre nosotros ES/EN/FR/DE/NL. Añadir H1 y reescribir entidad de marca para SEO/GEO con claims verificables.

## 7. MW-SOCIAL-PRESS-AFFILIATE-001 - CRITICO
Alcance: Social/prensa/afiliacion. Eliminar o validar promesas de comisiones, testimonios/ratings y permisos de imagen.

## 8. MW-GUIA-INSTALACION-GEO-001 - ALTO
Alcance: guia instalacion. Crear contenido HTML paso a paso por idioma y dejar PDFs como soporte.

## 9. MW-BLOG-I18N-ARTICLE-001 - ALTO
Alcance: 11 articulos publicados. Auditoria individual ES/EN/FR/DE/NL de titles, H1/H2, traduccion, enlaces y handles con typos.

## 10. MW-SAMPLES-SEO-POLICY-001 - ALTO
Alcance: politica de indexacion/canonical/noindex/contenido para muestras y relacion con producto principal.
""", encoding="utf-8")

    REGISTRO.write_text(REGISTRO.read_text(encoding="utf-8") + f"""

### Lote MW-AUDIT-CONTENIDO-I18N-GEO-001: auditoria de contenidos visibles, i18n y GEO

**Aprobacion recibida:** `APROBADO LOTE MW-AUDIT-CONTENIDO-I18N-GEO-001`.

**Fecha:** 16 de junio de 2026.

**Modo:** solo lectura.

**Acciones ejecutadas:**

- Lectura de `AGENTS.md` y registros prioritarios del proyecto.
- Consultas Shopify Admin GraphQL exclusivamente de lectura.
- Verificacion del tema MAIN: `SEO schema hotfix - 2026-06-15`, `gid://shopify/OnlineStoreTheme/178383749496`.
- Lectura de locales, menus, paginas publicadas, articulos publicados, primera pagina de productos activos y colecciones.
- Lectura de archivos criticos de tema: header, footer, FAQ, Profesionales, Muestras, Guia y Social/Prensa/Afiliacion.
- Render publico de 45 URLs prioritarias en ES, EN, FR, DE y NL mediante navegador, sin enviar formularios ni modificar datos.
- Analisis del inventario local `inventario-urls.csv` y `sitemap-urls.txt`.

**Cambios en Shopify:** ninguno. No se ejecutaron mutaciones, publicaciones, ediciones de tema, productos, colecciones, paginas, traducciones, menus, apps, mercados, URLs, handles, precios, imagenes, variantes ni inventario.

**Entregables generados:**

- `auditoria-contenido-i18n-geo-2026-06-16.md`.
- `inventario-problemas-contenido-i18n-geo-2026-06-16.csv`.
- `textos-fijos-plantilla-bloqueantes-2026-06-16.csv`.
- `h1-metadatos-i18n-geo-2026-06-16.csv`.
- `siguientes-lotes-contenido-i18n-geo-2026-06-16.md`.

**Estado final:** `INCOMPLETO` para la optimizacion global; `VERIFICADO PERO MEJORABLE` / `INCORRECTO` / `RIESGO CRITICO` en incidencias documentadas.

**Proximo lote recomendado:** `MW-FOOTER-I18N-001` o `MW-HEADER-CLAIMS-I18N-001`, ambos requieren aprobacion explicita antes de cualquier cambio.
""", encoding="utf-8")

    print(json.dumps({
        "rows_inventory": len(rows),
        "sitemap_urls": len(sitemap_urls),
        "problems": len(problems),
        "h1_meta_rows": len(h1_meta),
        "outputs": [
            str(output_md),
            str(output_problems),
            str(output_fixed),
            str(output_h1),
            str(output_lotes),
        ],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
