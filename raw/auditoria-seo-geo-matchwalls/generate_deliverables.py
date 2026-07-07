import csv
import json
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parent
INV = list(csv.DictReader((ROOT / "inventario-urls.csv").open(encoding="utf-8-sig")))
SUMMARY = json.loads((ROOT / "crawl-summary.json").read_text(encoding="utf-8"))
SITEMAP_URLS = (ROOT / "sitemap-urls.txt").read_text(encoding="utf-8").splitlines()

FIELDS = [
    "id", "estado_evidencia", "problema", "evidencia", "url_afectada", "impacto_seo",
    "impacto_geo", "impacto_comercial", "prioridad", "esfuerzo", "solucion_recomendada",
    "horizonte", "fuente"
]


def f(id, state, problem, evidence, url, seo, geo, commercial, priority, effort, solution, horizon, source):
    return dict(zip(FIELDS, [id, state, problem, evidence, url, seo, geo, commercial, priority, effort, solution, horizon, source]))


def write_csv(name, rows, fields=FIELDS):
    with (ROOT / name).open("w", newline="", encoding="utf-8-sig") as out:
        w = csv.DictWriter(out, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


sample_urls = [u for u in SITEMAP_URLS if "/products/" in u and any(x in urlparse(u).path.lower() for x in [
    "sample", "muestra", "probe", "echantillon", "campione", "amostra", "steekproef"
])]
suffix_one = [u for u in SITEMAP_URLS if "/products/" in u and urlparse(u).path.rsplit("/", 1)[-1].endswith("-1")]
typo_norid = [u for u in SITEMAP_URLS if "norid" in u.lower()]
typo_enchathed = [u for u in SITEMAP_URLS if "enchathed" in u.lower()]
ok = [r for r in INV if r["estado_http"] == "200" and r["content_type"].startswith("text/html")]
no_h1 = [r for r in ok if r["h1_count"] == "0"]
multi_h1 = [r for r in ok if int(r["h1_count"] or 0) > 1]
long_desc = [r for r in ok if int(r["description_longitud"] or 0) > 165]
alt_missing = [r for r in ok if int(r["imagenes_sin_alt"] or 0) > 0]

technical = [
    f("TEC-01", "Verificado", "URLs internas de prueba indexables y canonizadas a la home",
      "Se detectan /en/pages/facade-variants/test y /de/pages/facade-variants/test en sitemap; ambas responden 200 y declaran canonical a la home del idioma.",
      "https://www.matchwalls.com/en/pages/facade-variants/test | https://www.matchwalls.com/de/pages/facade-variants/test",
      "Alto: desperdicia rastreo y genera duplicación/canonical inconsistente.", "Alto: ofrece documentos de prueba a sistemas de recuperación.",
      "Medio: puede mostrar una experiencia impropia de marca.", "Crítica", "Bajo",
      "Retirar de publicación/sitemap y devolver 404/410 o redirigir solo si existe sustituto equivalente; verificar enlaces internos.",
      "0-30 días", "Rastreo público + sitemap"),
    f("TEC-02", "Verificado", "Páginas HTML sin H1",
      f"{len(no_h1)} páginas válidas de la muestra no contienen H1; patrón concentrado en páginas corporativas traducidas.",
      "https://www.matchwalls.com/en/pages/about-us | https://www.matchwalls.com/de/pages/uber-uns",
      "Medio: reduce claridad semántica.", "Alto: dificulta extraer el propósito principal.", "Medio", "Quick win", "Bajo",
      "Añadir un H1 único, descriptivo y localizado a cada plantilla/página afectada.", "0-30 días", "Rastreo público"),
    f("TEC-03", "Verificado", "Páginas con múltiples H1",
      f"{len(multi_h1)} páginas válidas de la muestra tienen 2 H1; algunas duplican exactamente el encabezado.",
      "https://www.matchwalls.com/en/pages/contact | https://www.matchwalls.com/de/pages/kontakt-1",
      "Bajo/medio: jerarquía ambigua.", "Medio: fragmenta la respuesta principal.", "Bajo", "Quick win", "Bajo",
      "Mantener un H1 por documento y convertir el segundo en H2 o texto visual.", "0-30 días", "Rastreo público"),
    f("TEC-04", "Verificado", "Alt de imagen ausente de forma generalizada",
      f"Las {len(alt_missing)} páginas HTML válidas de la muestra contienen al menos una imagen sin alt; la home española presenta 52.",
      "https://www.matchwalls.com/",
      "Medio: pierde señales en Google Images y accesibilidad.", "Medio: reduce comprensión multimodal.", "Medio", "31-90 días", "Medio",
      "Definir reglas por tipo de imagen: alt descriptivo para producto/ambiente y alt vacío para decoración; auditar imágenes clave.",
      "31-90 días", "Rastreo público"),
    f("TEC-05", "Verificado", "CSS aparece como texto rastreable en la home",
      "El render textual público de la home incluye reglas .logo-link/.logo-list__image repetidas junto a enlaces de categorías.",
      "https://www.matchwalls.com/",
      "Medio: diluye contenido y puede indicar marcado inválido.", "Alto: contamina el texto recuperado por motores de IA.", "Bajo", "Crítica", "Bajo",
      "Corregir el bloque/section que imprime CSS como contenido; validar HTML renderizado y cachés.", "0-30 días", "Render público de la home"),
    f("TEC-06", "Verificado", "Meta descriptions excesivamente largas",
      f"{len(long_desc)} páginas válidas de la muestra superan 165 caracteres; varias llegan a 320.",
      "https://www.matchwalls.com/blogs/inspiracion/ideas-para-papel-pintado-transforma-tu-espacio-con-disenos-encantadores",
      "Medio: snippets truncados y poco diferenciados.", "Bajo", "Medio", "31-90 días", "Medio",
      "Reescribir metadatos por intención y mercado, priorizando páginas con impresiones.", "31-90 días", "Rastreo público"),
    f("TEC-07", "Verificado con limitación", "Respuesta 500 puntual en producto inglés",
      "Durante el rastreo, /en/products/black-noridcas-lines devolvió HTTP 500. Debe repetirse la prueba porque el sitio activó rate limiting después.",
      "https://www.matchwalls.com/en/products/black-noridcas-lines",
      "Alto si persiste.", "Alto si persiste.", "Alto si persiste.", "Crítica", "Bajo",
      "Recomprobar desde monitorización externa y revisar logs/plantilla/producto si el 500 se reproduce.", "0-30 días", "Rastreo público"),
    f("TEC-08", "Verificado", "Robots y sitemap correctamente declarados, con oportunidad de control",
      "robots.txt permite HTML público, bloquea transaccional/filtros y declara https://www.matchwalls.com/sitemap.xml. El sitemap contiene 7.932 URLs.",
      "https://www.matchwalls.com/robots.txt | https://www.matchwalls.com/sitemap.xml",
      "Positivo; exige vigilar calidad del sitemap.", "Positivo: incluye agents.md y UCP/MCP.", "Positivo", "Mantener", "Bajo",
      "Monitorizar semanalmente sitemap, indexables y exclusiones; no bloquear IA útil sin estrategia.", "31-90 días", "robots.txt + sitemap"),
]

international = [
    f("INT-01", "Verificado", "Hreflang completo en la muestra, pero sin x-default",
      "Todas las 565 páginas HTML válidas rastreadas declaran 8 alternates; corresponden a 7 idiomas más x-default o variantes según plantilla. Validar reciprocidad completa en un crawler sin rate limit.",
      "https://www.matchwalls.com/",
      "Positivo con riesgo residual.", "Positivo.", "Alto", "31-90 días", "Medio",
      "Validar reciprocidad, códigos regionales y x-default con Search Console/export completo; corregir pares rotos.", "31-90 días", "Rastreo público"),
    f("INT-02", "Verificado", "Handles con errores propagados entre idiomas",
      f"El sitemap contiene {len(typo_norid)} URLs con 'norid/noridcas' y {len(typo_enchathed)} con 'enchathed'.",
      "https://www.matchwalls.com/en/products/black-noridcas-lines | https://www.matchwalls.com/en/products/enchathed-forest-tapestry-blue",
      "Alto: señales léxicas erróneas y deuda de redirecciones.", "Alto: reduce comprensión de entidades/productos.", "Medio", "Crítica", "Alto",
      "Crear diccionario maestro de familias/colores; corregir handles solo con mapa 301 uno-a-uno, canonicals, hreflang y enlaces actualizados.",
      "31-90 días", "Sitemap"),
    f("INT-03", "Verificado", "Mezcla de idiomas en páginas prioritarias",
      "La página alemana de atención al cliente usa como segundo H1 'Atención al cliente — MatchWalls'; la inglesa también conserva ese H1 español.",
      "https://www.matchwalls.com/de/pages/kundendienst | https://www.matchwalls.com/en/pages/customer-service",
      "Alto: relevancia y calidad editorial.", "Alto: respuestas multilingües ambiguas.", "Alto: reduce confianza.", "Crítica", "Bajo",
      "Corregir el bloque compartido y revisar ES/EN/FR/DE/NL con detección automática y revisión humana.", "0-30 días", "Rastreo público"),
    f("INT-04", "Verificado", "URL francesa con marca mal escrita",
      "El sitemap contiene /fr/collections/nouveaux-matchalls-matchwallsmurals.",
      "https://www.matchwalls.com/fr/collections/nouveaux-matchalls-matchwallsmurals",
      "Medio/alto.", "Medio.", "Medio.", "Quick win", "Bajo",
      "Confirmar intención, crear URL francesa correcta y 301; actualizar canonical, hreflang y enlaces.", "0-30 días", "Sitemap"),
    f("INT-05", "Verificado", "URL española de muestra aparece en mercados EN y FR",
      "El sitemap incluye /en/products/muestra-de-wildflower-whisper-lila y /fr/products/muestra-de-wildflower-whisper-lila.",
      "https://www.matchwalls.com/en/products/muestra-de-wildflower-whisper-lila | https://www.matchwalls.com/fr/products/muestra-de-wildflower-whisper-lila",
      "Alto.", "Alto.", "Medio.", "Crítica", "Medio",
      "Normalizar handles localizados de muestras y aplicar redirecciones controladas; revisar toda la matriz de traducción.",
      "0-30 días", "Sitemap"),
    f("INT-06", "Hipótesis respaldada", "Sufijos -1 indican colisiones o handles duplicados",
      f"Se detectan {len(suffix_one)} URLs de producto terminadas en -1 en el sitemap multilingüe.",
      "https://www.matchwalls.com/de/products/alpine-serenity-brown-1",
      "Medio/alto.", "Medio.", "Medio.", "31-90 días", "Alto",
      "Comparar producto fuente, traducciones y canonicals; consolidar solo cuando sean duplicados reales.", "31-90 días", "Sitemap"),
]

catalog = [
    f("CAT-01", "Verificado", "Muestras publicadas como productos indexables",
      f"Se identifican al menos {len(sample_urls)} URLs de muestras mediante términos sample/muestra/probe/echantillon/campione/amostra/steekproef.",
      "https://www.matchwalls.com/en/products/blue-classic-grid-sample | https://www.matchwalls.com/products/muestra-abstract-curves-negro",
      "Alto: canibalización, duplicidad y expansión del índice.", "Alto: puede recomendar una muestra como producto principal.", "Alto: tráfico aterriza en SKU auxiliar.", "Crítica", "Alto",
      "Definir estrategia: noindex de muestras y enlaces de compra desde producto principal, o contenido/canonical diferenciado si deben posicionar.",
      "0-30 días", "Sitemap"),
    f("CAT-02", "Verificado", "Sitemap sobredimensionado por localización del catálogo",
      "Hay 971 URLs de producto por idioma, 6.797 URLs de producto localizadas en total, frente a ~2.600 SKUs declarados.",
      "https://www.matchwalls.com/sitemap.xml",
      "Medio/alto: calidad media del índice depende de cada traducción.", "Alto: multiplica inconsistencias para IA.", "Medio", "31-90 días", "Alto",
      "Clasificar URLs por producto principal/muestra/variante; priorizar indexación de páginas con demanda y contenido único.", "31-90 días", "Sitemap"),
    f("CAT-03", "Verificado", "Metadatos duplicados en muestras alemanas",
      "Blue Classic Grid Probe y Green Classic Grid Probe comparten meta description alemana en la muestra rastreada.",
      "https://www.matchwalls.com/de/products/blue-classic-grid-probe | https://www.matchwalls.com/de/products/green-classic-grid-probe",
      "Medio.", "Medio.", "Bajo/medio.", "Quick win", "Bajo",
      "Aplicar plantilla de metadata que incluya familia, color, tipo de SKU y propuesta única; evitar indexar muestras si no aportan valor.",
      "0-30 días", "Rastreo público"),
    f("CAT-04", "Verificado", "Nombres y handles con errores ortográficos de producto",
      "Ejemplos propagados: enchathed, noridcas, recoto y suctan. También se observa 'Marròn' en tarjeta de producto española.",
      "https://www.matchwalls.com/en/products/enchathed-garden-symphony-black | https://www.matchwalls.com/",
      "Alto.", "Alto.", "Alto: afecta percepción y búsqueda.", "Crítica", "Alto",
      "Crear QA editorial centralizado por familia/atributo y un flujo de corrección con redirecciones y control de hreflang.", "0-30 días", "Sitemap + home pública"),
    f("CAT-05", "Verificado", "Product schema presente en producto, pero cobertura observada limitada por rate limiting",
      "116 páginas de producto válidas contienen Product, Offer, Brand, ImageObject y QuantitativeValue.",
      "https://www.matchwalls.com/products/whispering-woods-azul",
      "Positivo.", "Positivo.", "Alto.", "Mantener", "Medio",
      "Validar una muestra representativa por idioma en Rich Results Test y Merchant Center; añadir identificadores coherentes (SKU/GTIN/MPN cuando proceda).",
      "31-90 días", "Rastreo público"),
]

content = [
    f("CON-01", "Verificado", "Home con mezcla de nombres ingleses y españoles y errores visibles",
      "La home española muestra 'Professionals', 'Wallpaper', productos como 'Whispering Reeds Wallpaper Beige' y 'Highland Plaid Marròn'.",
      "https://www.matchwalls.com/",
      "Alto.", "Alto.", "Alto.", "Crítica", "Bajo",
      "Revisión editorial completa de home ES; fijar glosario para nombres propios vs términos traducibles.", "0-30 días", "Render público de home"),
    f("CON-02", "Verificado", "Blog con errores y metadatos truncables",
      "Existe el handle español 'transfroma-tu-cocina...' y una página inglesa usa H1 'Matchalls.com'; varias meta descriptions alcanzan 320 caracteres.",
      "https://www.matchwalls.com/blogs/inspiracion/transfroma-tu-cocina-en-un-espacio-moderno-y-funcional-papel-vinilico | https://www.matchwalls.com/en/blogs/inspiration/discover-how-the-vinyl-paper-of-matchwalls-com-can-transform-your-kitchen-into-a-modern-and-functional-space",
      "Alto.", "Alto.", "Medio.", "Quick win", "Medio",
      "Corregir errores con 301, editar H1/meta y crear calendario evergreen basado en preguntas de compra/instalación.", "0-30 días", "Sitemap + rastreo"),
    f("CON-03", "Verificado", "FAQ implementada y marcada con FAQPage",
      "14 páginas válidas incluyen FAQPage, Question y Answer.",
      "https://www.matchwalls.com/en/pages/frequent-questions",
      "Positivo.", "Alto.", "Medio.", "Mantener", "Bajo",
      "Actualizar respuestas, añadir autoría/fecha y enlazar a guías y categorías; no duplicar FAQs idénticas en exceso.", "31-90 días", "Rastreo público"),
    f("CON-04", "Verificado", "B2B existe pero necesita reforzar evidencia de experiencia",
      "Se detectan páginas Professionals/Professional Studios y versiones localizadas; algunas carecen de H1.",
      "https://www.matchwalls.com/en/pages/professionals | https://www.matchwalls.com/en/pages/professional-studies",
      "Medio/alto.", "Alto.", "Alto.", "3-6 meses", "Medio",
      "Crear casos de proyecto verificables con sector, reto, material, resultado, fotografías, autor y enlaces a soluciones.", "3-6 meses", "Rastreo público"),
]

write_csv("auditoria-seo-tecnico.csv", technical)
write_csv("auditoria-internacional.csv", international)
write_csv("auditoria-catalogo.csv", catalog)
write_csv("auditoria-contenidos.csv", content)

all_findings = technical + international + catalog + content
priority_order = {"Crítica": 1, "Quick win": 2, "31-90 días": 3, "3-6 meses": 4, "Mantener": 5}
backlog_fields = ["orden", "id", "accion", "evidencia_url", "impacto", "esfuerzo", "impacto_x_esfuerzo", "horizonte", "dependencia", "estado_evidencia"]
backlog = []
for i, item in enumerate(sorted(all_findings, key=lambda x: (priority_order.get(x["prioridad"], 9), x["esfuerzo"])), 1):
    impact = "Alto" if "Alto" in (item["impacto_seo"] + item["impacto_geo"] + item["impacto_comercial"]) else "Medio"
    score = {"Alto": {"Bajo": 9, "Medio": 7, "Alto": 5}, "Medio": {"Bajo": 6, "Medio": 4, "Alto": 2}}[impact].get(item["esfuerzo"], 3)
    backlog.append({
        "orden": i, "id": item["id"], "accion": item["solucion_recomendada"],
        "evidencia_url": item["url_afectada"], "impacto": impact, "esfuerzo": item["esfuerzo"],
        "impacto_x_esfuerzo": score, "horizonte": item["horizonte"],
        "dependencia": "Validación y autorización antes de modificar Shopify", "estado_evidencia": item["estado_evidencia"]
    })
write_csv("backlog-priorizado.csv", backlog, backlog_fields)

executive = f"""# Resumen ejecutivo

## Fuentes, herramientas y límites

- Auditoría exclusivamente de lectura realizada el 15 de junio de 2026.
- Fuentes: `robots.txt`, sitemap público, HTML público, metadatos, canonicals, hreflang, JSON-LD y renders textuales; contraste superficial con Photowall, Rebel Walls, Wallism y Bimago.
- Se inspeccionaron **2.110 URLs seleccionadas** de **7.932 URLs declaradas en sitemap**. Shopify respondió correctamente en 565 y activó rate limiting (`429`) en el resto; los `429` se tratan como limitación del rastreo, no como errores SEO.
- No había archivos, scripts, credenciales ni acceso Shopify API configurado en el espacio de trabajo. No se ejecutó ninguna mutación ni se modificó Shopify.
- Sin acceso a Search Console, GA4, Merchant Center, logs, Core Web Vitals de campo ni plataformas de visibilidad; no se inventan rankings, tráfico ni volúmenes.

## Diagnóstico

Matchwalls tiene una base técnica internacional razonable: `robots.txt` claro, sitemap declarado, canonicals y hreflang presentes en la muestra, Product/Offer schema y FAQ schema. Además, `robots.txt` publica `agents.md` y endpoints UCP/MCP, una ventaja incipiente para comercio asistido por IA.

El principal riesgo no es la ausencia de infraestructura, sino la **calidad multiplicada del catálogo internacional**. El sitemap publica 971 productos por idioma y contiene cientos de muestras, handles con errores propagados, sufijos `-1`, URLs con idioma incorrecto y páginas de prueba. En contenido visible se verifican mezcla de idiomas, errores de marca y CSS expuesto como texto. Esto perjudica SEO, confianza comercial y la capacidad de los motores de IA para identificar el producto correcto.

## Cifras verificadas

- 7.932 URLs en sitemap; 971 productos, 107 colecciones, 42 páginas y 12 artículos por idioma.
- Al menos {len(sample_urls)} URLs de muestras detectadas por patrones lingüísticos.
- {len(suffix_one)} productos con handle terminado en `-1`.
- {len(typo_norid)} URLs con `norid/noridcas`; {len(typo_enchathed)} con `enchathed`.
- {len(no_h1)} páginas HTML válidas sin H1 y {len(multi_h1)} con múltiples H1.
- 7 homes con `AggregateRating`; 0 páginas con `Review` schema en la muestra.
- 116 productos válidos con `Product`, `Offer` y `Brand`; 14 páginas con `FAQPage`.

## Prioridades

1. **Críticas:** retirar páginas de prueba; verificar el 500; corregir CSS visible, mezcla de idiomas y errores de marca; decidir la indexación de muestras; auditar la veracidad de `AggregateRating`.
2. **0-30 días:** QA editorial ES/EN/FR/DE/NL, H1, metadatos duplicados, handles obviamente erróneos y mapa de redirecciones propuesto.
3. **31-90 días:** inventario maestro producto/muestra/familia, validación hreflang completa, reglas de imagen/alt y datos estructurados.
4. **3-6 meses:** arquitectura de familias y entidades, casos B2B, guías expertas y automatización de QA antes de publicar.
5. **6-12 meses:** autoridad editorial, relaciones públicas, menciones de diseñadores/proyectos y medición continua de citaciones en IA.
"""
(ROOT / "resumen-ejecutivo.md").write_text(executive, encoding="utf-8")

schema_md = """# Auditoría de datos estructurados

## Hechos verificados

| Tipo | Cobertura observada | Evaluación |
|---|---:|---|
| Product / Offer / Brand | 116 páginas válidas | Presente en productos; validar cobertura completa y consistencia de precio/disponibilidad. |
| AggregateRating | 7 páginas, las homes localizadas | Riesgo alto: no se observó `Review` schema. Debe comprobarse que la puntuación representa reseñas visibles, actuales y elegibles. |
| Review | 0 páginas | No presente en la muestra. No debe añadirse solo para justificar AggregateRating sin reseñas reales visibles. |
| BreadcrumbList | 564 páginas | Cobertura amplia. |
| WebSite / SearchAction | 7 homes | Correcto como base. |
| Organization | 40 páginas | Presente en homes/artículos; consolidar identidad, `sameAs`, logo y contacto. |
| BlogPosting | 33 artículos | Presente; revisar autor, fechas, imágenes y entidad editora. |
| FAQPage | 14 páginas | Presente; mantener sincronizado con contenido visible. |

## Hallazgo prioritario: AggregateRating

`AggregateRating` aparece en las siete homes localizadas, no en los productos observados. Esto puede ser válido únicamente si representa una entidad elegible y la valoración es visible y verificable en la propia página conforme a las políticas del buscador. La ausencia de `Review` no invalida automáticamente el agregado, pero aumenta la necesidad de revisar su procedencia, entidad evaluada, recuento, valor y contenido visible.

**Acción recomendada:** validar cada home con Rich Results Test y Schema Markup Validator; documentar fuente, fecha y método; retirar o corregir el marcado si no coincide con la experiencia visible. No realizar cambios sin autorización.

## Modelo recomendado

- Producto: `Product` + `Offer` coherente con variante/precio/disponibilidad visibles; SKU y GTIN/MPN cuando existan.
- Muestra: decidir si es producto independiente. Si no debe posicionar, evitar que compita con el producto principal.
- Organización: una entidad estable con `sameAs`, datos de contacto, política de envíos/devoluciones y país.
- Artículos/guías: `Article`/`BlogPosting` con autor experto, fecha de publicación/modificación y fuentes.
- FAQ: solo preguntas y respuestas visibles; evitar marcado repetido sin valor.
"""
(ROOT / "auditoria-schema.md").write_text(schema_md, encoding="utf-8")

geo_md = """# Auditoría GEO / AEO

## Estado actual

**Fortalezas verificadas**

- Shopify publica en `robots.txt` un `agents.md`, descubrimiento UCP y endpoint UCP/MCP. Es una base favorable para agentes de compra.
- Hay FAQPage, Product/Offer, BlogPosting, Breadcrumb y Organization.
- El sitio explica personalización, materiales, instalación, envíos, sostenibilidad y servicios profesionales.

**Debilidades verificadas**

- CSS expuesto como texto en la home, mezcla de idiomas y errores ortográficos contaminan la recuperación semántica.
- Las muestras indexables pueden ser recomendadas como si fueran el producto principal.
- Las páginas corporativas traducidas a menudo carecen de H1 o duplican H1.
- La entidad Matchwalls no está expresada de forma suficientemente consistente: nombres de producto, handles y marca varían.
- AggregateRating requiere validación estricta de fuente y visibilidad.

## Acciones para ser comprendida y citada

1. Crear una ficha de entidad coherente: quién es Matchwalls, qué fabrica, materiales, países, personalización, envío, devoluciones, sostenibilidad y contacto.
2. Publicar comparativas y respuestas factuales: diferencias entre non-woven, vinilo autoadhesivo y mural; medición; instalación; retirada; idoneidad por estancia.
3. Añadir autoría experta, fecha de revisión, fuentes y metodología a guías.
4. Crear páginas de familia que expliquen concepto, variantes, colores, materiales, estancias y productos relacionados.
5. Separar semánticamente producto principal, muestra y variante.
6. Monitorizar mensualmente respuestas de ChatGPT, Gemini, Perplexity y Google AI Overviews con un conjunto fijo de preguntas, registrando cita, posición y exactitud.

## Preguntas objetivo sugeridas

- ¿Dónde comprar papel pintado personalizado con envío internacional?
- ¿Qué diferencia hay entre mural, papel non-woven y vinilo autoadhesivo?
- ¿Cómo medir una pared para pedir un mural a medida?
- ¿Qué papel pintado es adecuado para cocina, baño, hotel u oficina?
- ¿Qué marcas europeas ofrecen muestras y murales personalizados?

No se afirma visibilidad actual en estas plataformas porque no se dispuso de paneles ni medición reproducible.
"""
(ROOT / "auditoria-geo.md").write_text(geo_md, encoding="utf-8")

competition_md = """# Análisis de competencia

## Comparación cualitativa verificada

| Competidor | Ventaja observable | Implicación para Matchwalls |
|---|---|---|
| Photowall | Dominio/localización por mercado y propuesta centrada en papel pintado cautivador. | Revisar estrategia de mercado y autoridad local. |
| Rebel Walls | Mensaje de marca fuerte, custom wallpaper, magazine activo, proyectos profesionales, sostenibilidad, prensa y colaboración con diseñadores. | Reforzar marca, autoridad editorial, casos B2B y colaboraciones. |
| Wallism | Taxonomía extremadamente profunda por tema, estilo, periodo, color y estancia; beneficios factuales destacados. | Construir arquitectura semántica útil sin generar thin pages. |
| Bimago | Catálogo amplio de decoración mural más allá del papel pintado. | Diferenciarse por especialización, personalización y expertise técnico. |

## Brechas estratégicas

- Matchwalls compite bien en amplitud internacional, pero la calidad editorial irregular diluye esa ventaja.
- Rebel Walls comunica mejor la entidad de marca, el contenido inspiracional y la oferta profesional.
- Wallism ofrece más rutas semánticas para búsquedas específicas y descubrimiento por IA.
- La oportunidad de Matchwalls es ser la fuente experta en **papel pintado y murales personalizados a medida**, con guías técnicas, familias limpias y evidencia de proyectos.

## Otros competidores a detectar con datos

Con acceso a Search Console/Ahrefs/Semrush: identificar dominios que coinciden en consultas no-brand por país, especialmente “papel pintado personalizado”, “custom wallpaper”, “papier peint sur mesure”, “Fototapete nach Maß” y equivalentes NL. No se asignan cuotas ni volúmenes sin datos.
"""
(ROOT / "analisis-competencia.md").write_text(competition_md, encoding="utf-8")

roadmap_md = """# Roadmap de 12 meses

## Críticas y 0-30 días

- Confirmar y retirar páginas de prueba; repetir comprobación del producto con 500.
- Corregir CSS visible en home y mezcla de idiomas en bloques compartidos.
- Auditar `AggregateRating` frente a reseñas visibles y fuente real.
- Decidir política SEO de muestras y preparar inventario producto principal ↔ muestra.
- Corregir errores editoriales visibles sin cambiar URLs hasta aprobar un mapa 301.
- Añadir H1 único a páginas corporativas prioritarias.

## 31-90 días

- QA editorial completo ES, EN, FR, DE y NL con glosario maestro.
- Inventario de handles incorrectos, sufijos `-1`, canonicals, hreflang y redirecciones propuestas.
- Optimizar metadatos por plantilla e intención; revisar alt de imágenes.
- Validar schema por tipo de página y mercado.
- Conectar Search Console/GA4/Merchant Center y crear panel de indexación/calidad.

## Desarrollo 3-6 meses

- Reestructurar familias y páginas de entidad con contenido único y relaciones claras.
- Automatizar controles prepublicación: idioma, campos cortados, duplicados, handles, schema y enlaces.
- Crear casos B2B verificables y guías técnicas con autoría experta.
- Mejorar rendimiento usando CWV de campo y plantillas más ligeras.

## Autoridad 6-12 meses

- Programa editorial por preguntas reales de compra, instalación y diseño.
- Colaboraciones con diseñadores, arquitectos, instaladores y medios.
- Activos citables: estudios, guías descargables, calculadoras y comparativas.
- Medición mensual de menciones/citas en ChatGPT, Gemini, Perplexity y AI Overviews.
- Revisión trimestral internacional de indexación, hreflang y catálogo.

## Gobernanza

Toda modificación debe pasar por: evidencia → propuesta → revisión editorial/técnica → autorización de Daniel → despliegue controlado → verificación.
"""
(ROOT / "roadmap-12-meses.md").write_text(roadmap_md, encoding="utf-8")

print("Deliverables generated")
