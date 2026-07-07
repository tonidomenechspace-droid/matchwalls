# Auditoria contenido, i18n y GEO/LLMO - MW-AUDIT-CONTENIDO-I18N-GEO-001

Fecha: 16 de junio de 2026. Modo: solo lectura. Shopify no modificado.

## Fuentes verificadas

- `AGENTS.md` y registros del proyecto leidos y aplicados.
- Shopify Admin GraphQL en modo lectura: tema MAIN, locales publicados, menus, paginas, articulos, primera pagina de productos activos y colecciones.
- Tema MAIN verificado: `SEO schema hotfix - 2026-06-15`, `gid://shopify/OnlineStoreTheme/178383749496`, rol `MAIN`, sin procesamiento fallido.
- Render publico actual de 45 URLs prioritarias: home, FAQ, profesionales, muestras, guia, contacto, sobre nosotros, social/prensa/afiliacion y blog en ES, EN, FR, DE y NL.
- Inventario local existente: `inventario-urls.csv` y `sitemap-urls.txt`.

## Cobertura y limitaciones

- Sitemap local: 7932 URLs inventariadas. Distribucion por idioma: de: 1133, en: 1133, es: 3400, fr: 1133, nl: 1133.
- Inventario rastreado previo: 7932 filas. Se usa para detectar patrones de H1, title, meta, handles y muestras.
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

- Incidencias documentadas: 629.
- Matriz H1/metas: 35 filas.
- Por prioridad: ALTO: 45, CRITICO: 7, MEDIO: 577.
- Por idioma/recurso: DE/NL: 1, EN/DE/NL: 1, EN/FR/DE/NL: 1, ES/EN/FR/DE/NL: 10, de: 287, en: 204, es: 124, nl: 1.

## Entregables generados

- `inventario-problemas-contenido-i18n-geo-2026-06-16.csv`.
- `textos-fijos-plantilla-bloqueantes-2026-06-16.csv`.
- `h1-metadatos-i18n-geo-2026-06-16.csv`.
- `siguientes-lotes-contenido-i18n-geo-2026-06-16.md`.

## Decision recomendada

No ejecutar cambios masivos. El siguiente lote mas seguro y de mayor impacto es corregir footer/header global por idioma, porque afecta a todas las URLs y actualmente contamina SEO, confianza y GEO/LLMO.
