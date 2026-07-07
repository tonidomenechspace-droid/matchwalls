# Resumen ejecutivo

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
- Al menos 541 URLs de muestras detectadas por patrones lingüísticos.
- 359 productos con handle terminado en `-1`.
- 70 URLs con `norid/noridcas`; 19 con `enchathed`.
- 34 páginas HTML válidas sin H1 y 15 con múltiples H1.
- 7 homes con `AggregateRating`; 0 páginas con `Review` schema en la muestra.
- 116 productos válidos con `Product`, `Offer` y `Brand`; 14 páginas con `FAQPage`.

## Prioridades

1. **Críticas:** retirar páginas de prueba; verificar el 500; corregir CSS visible, mezcla de idiomas y errores de marca; decidir la indexación de muestras; auditar la veracidad de `AggregateRating`.
2. **0-30 días:** QA editorial ES/EN/FR/DE/NL, H1, metadatos duplicados, handles obviamente erróneos y mapa de redirecciones propuesto.
3. **31-90 días:** inventario maestro producto/muestra/familia, validación hreflang completa, reglas de imagen/alt y datos estructurados.
4. **3-6 meses:** arquitectura de familias y entidades, casos B2B, guías expertas y automatización de QA antes de publicar.
5. **6-12 meses:** autoridad editorial, relaciones públicas, menciones de diseñadores/proyectos y medición continua de citaciones en IA.

## Actualización tras acceso interno de solo lectura

La revisión interna de Shopify confirmó 3.022 productos, 1.990 muestras, 109 colecciones, 55 páginas y 635 redirecciones. También permitió verificar incidencias críticas no visibles con suficiente detalle en el rastreo público:

- `Métodos de pago` y `Conoce nuestros productos` contienen cuerpos cruzados; varias traducciones recientes también están desalineadas.
- Las familias Serene Vista y Whispering Woods se han corregido solo parcialmente; permanecen traducciones de otros productos, campos desactualizados, handles débiles y alt de imagen deficientes.
- El tema principal publicado contiene un `AggregateRating` fijo de Organization con valor 4,5 y 13 reseñas, cuya fuente y elegibilidad deben demostrarse.
- IT y PT presentan una deuda de actualización considerable frente a ES, EN, FR, DE y NL.
- Existen cadenas de redirección y destinos entre productos aparentemente no equivalentes.

La auditoría interna completa y la revisión del trabajo reciente están documentadas en `auditoria-interna-shopify.md`, `hallazgos-internos-shopify.csv` y `revision-trabajo-reciente-claude.md`.
## Actualizacion 16 de junio de 2026

El tema `SEO schema hotfix - 2026-06-15` fue publicado manualmente por Daniel y verificado despues en modo lectura.

Estado del hotfix: `CORREGIDO Y VERIFICADO`.

Evidencia:

- Tema MAIN actual: `SEO schema hotfix - 2026-06-15`, `gid://shopify/OnlineStoreTheme/178383749496`.
- `SEO-GEO staging - 2026-06-15` permanece `UNPUBLISHED`.
- 35 URLs revisadas en escritorio y 35 en movil en ES, EN, FR, DE y NL.
- 0 errores JSON-LD.
- 0 `AggregateRating` corporativos fijos detectados.
- 0 GTIN/MPN falsos detectados.
- Productos probados con `Product` y 4 `Offer` completos.

Esto corrige el riesgo especifico del `AggregateRating` fijo y los identificadores falsos publicados por el tema anterior. No cierra la auditoria SEO/GEO global: siguen pendientes las plantillas de contenido, footer, FAQ, Profesionales, Muestras, Guia, catalogo completo, Search Console, Merchant Center, Core Web Vitals y revision editorial ES/EN/FR/DE/NL.
