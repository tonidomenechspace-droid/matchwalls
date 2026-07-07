# Diagnóstico MW-INDEXABILITY-GEO-COLLECTIONS-DECISION-011E

Fecha: 2026-06-27  
Estado global: `REQUIERE DECISION HUMANA`

## Documentos y evidencias leídas

- `AGENTS.md`.
- `registro-cambios-ejecutados.md`.
- `diagnostico-MW-INDEXABILITY-REMAINING-CLASSIFICATION-DIAG-011C-2026-06-27.md`.
- `classification-master-MW-INDEXABILITY-REMAINING-CLASSIFICATION-DIAG-011C-2026-06-27.csv`.
- `geo-collections-candidates-MW-INDEXABILITY-REMAINING-CLASSIFICATION-DIAG-011C-2026-06-27.csv`.
- `qa-publico-muestra-MW-INDEXABILITY-GEO-COLLECTIONS-DECISION-011E-2026-06-27.csv`.
- `qa-sitemap-geo-MW-INDEXABILITY-GEO-COLLECTIONS-DECISION-011E-2026-06-27.csv`.
- `admin-muestra-MW-INDEXABILITY-GEO-COLLECTIONS-DECISION-011E-2026-06-27.csv`.

## Alcance

Diagnóstico de solo lectura sobre las colecciones geográficas detectadas en sitemap.  
No se han modificado colecciones, handles, redirecciones, traducciones, productos, temas, canonicals ni metafields.

## Estado real comprobado

`VERIFICADO PERO MEJORABLE`

- Hay 346 URLs de colecciones geográficas actualmente presentes en sitemaps de colecciones.
- Distribución actual en sitemap:
  - ES: 58.
  - EN: 56.
  - FR: 56.
  - NL: 52.
  - DE: 41.
  - PT: 55.
  - IT: 28.
- Los siete sitemaps de colecciones revisados responden 200.
- Cada sitemap de colecciones revisado contiene 106 URLs.
- Las 346 URLs candidatas siguen presentes en sitemap tras el noindex Black Friday.
- Todas tienen `lastmod` de sitemap `2026-06-15T14:49:07+02:00`.

## Comprobación pública

`VERIFICADO PERO MEJORABLE`

Muestra controlada: 28 URLs públicas en ES, EN, FR, DE y NL sobre Madrid, Barcelona, París, Toulouse, Álava y Albacete.

- 28/28 responden 200.
- 28/28 no tienen meta robots `noindex`.
- 28/28 tienen canonical self.
- 28/28 son por tanto elegibles para indexación y rastreo.
- Las huellas de producto se repiten por idioma:
  - ES: misma huella en 6/6 páginas de muestra.
  - EN: misma huella en 6/6.
  - FR: misma huella en 6/6.
  - DE: misma huella en 5/5.
  - NL: misma huella en 5/5.
- En la muestra pública, ES muestra 148 enlaces de producto; EN/FR 144; DE/NL 31. La repetición por idioma indica que no hay surtido local diferenciado por ciudad/provincia en la muestra.

## Comprobación Admin

`VERIFICADO PERO MEJORABLE`

Consulta Admin GraphQL validada y ejecutada en lectura.

Colecciones verificadas como muestra representativa:

- `gid://shopify/Collection/443626914019` — `comprar-papel-pintado-alava`.
- `gid://shopify/Collection/646109593976` — `comprar-papel-pintado-albacete`.
- `gid://shopify/Collection/646109626744` — `comprar-papel-pintado-alicante`.
- `gid://shopify/Collection/646109659512` — `comprar-papel-pintado-almeria`.
- `gid://shopify/Collection/646109757816` — `comprar-papel-pintado-badajoz`.
- `gid://shopify/Collection/646109856120` — `comprar-papel-pintado-burgos`.
- `gid://shopify/Collection/646109790584` — `comprar-papel-pintado-barcelona`.
- `gid://shopify/Collection/443626979555` — `comprar-papel-pintado-madrid`.
- `gid://shopify/Collection/646199804280` — `comprar-papel-pintado-paris`.
- `gid://shopify/Collection/646199837048` — `comprar-papel-pintado-toulouse`.

Patrón común verificado:

- `productsCount`: 73 exactos.
- `resourcePublicationsCount`: 9 exactas.
- `sortOrder`: `MANUAL`.
- `seo.hidden`: `null`.
- Primeros 8 productos idénticos en todas las colecciones verificadas.
- `updatedAt`: `2026-06-15T12:49:07Z` en todas las verificadas.

## Problemas de calidad observados

`INCORRECTO`

- Generación masiva de páginas geográficas indexables con estructura, productos y fechas homogéneas.
- Handles traducidos con sufijos `-1`/`-2` en algunos idiomas, especialmente DE/NL.
- Traducciones de cuerpo con calidad irregular detectada en Admin:
  - EN incluye expresiones literales como “medieval helmet” para casco/casco antiguo.
  - EN/DE/NL contienen fórmulas antinaturales como “free wallpaper of wallpaper”.
  - NL/DE muestran traducciones literales y mezcla semántica en descripciones locales.
- En algunas URLs hay diferencias por acentos o traducción de topónimos entre handle, H1 y title; no es necesariamente un fallo técnico, pero confirma que no puede hacerse una limpieza por patrón simple sin revisión.

## Riesgo SEO/GEO

`RIESGO CRITICO`

Estas URLs son elegibles para Google, Bing, Yahoo, Copilot y sistemas IA que dependan del rastreo web. El riesgo no es que estén caídas; el riesgo es que estén demasiado disponibles siendo páginas repetitivas, con poco valor diferencial, traducciones mejorables y señales potenciales de doorway/geolocalización artificial.

Impacto:

- Dilución de crawl budget en colecciones de baja calidad.
- Canibalización de colecciones comerciales reales.
- Señal editorial débil para buscadores y motores IA.
- Riesgo de que IA cite páginas geográficas con frases o traducciones poco naturales.
- Dificulta priorizar páginas útiles, guías, categorías y productos principales.

## Datos no accesibles en este diagnóstico

`NO ACCESIBLE`

- Search Console: impresiones, clics, consultas y cobertura real de estas URLs.
- GA4/Shopify Analytics: ventas, ingresos o conversiones atribuidas a estas páginas.
- Bing Webmaster Tools.
- Citas reales en Copilot, Perplexity, Gemini, Claude, Grok o ChatGPT.

## Criterio recomendado

`REQUIERE DECISION HUMANA`

Política recomendada:

1. No cambiar handles ni redirecciones ahora.
2. No eliminar colecciones.
3. No mantener indexables por defecto las páginas geográficas repetitivas.
4. Mantener en `STANDBY` las ciudades estratégicas o potencialmente comerciales: Madrid, Barcelona, París, Toulouse, Bordeaux/Burdeos y similares.
5. Mantener indexable una página geográfica solo si supera evidencia mínima:
   - contenido local único y revisado por idioma;
   - intención comercial clara;
   - calidad lingüística nativa o revisada;
   - no duplicación masiva de productos;
   - evidencia de demanda, tráfico, enlaces o conversión;
   - coherencia de title, H1, canonical, hreflang y schema.
6. Ejecutar un piloto reversible de noindex sobre un bloque pequeño de colecciones geográficas no estratégicas antes de ampliar.

## Siguiente lote recomendado

`MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-PILOT-011E1`

Objetivo: aplicar `seo.hidden=1` solo a 6 colecciones geográficas no estratégicas y verificar que sus URLs localizadas salen de sitemap y muestran robots `noindex,nofollow`.

No ejecutar sin aprobación exacta:

`APROBADO LOTE MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-PILOT-011E1`

