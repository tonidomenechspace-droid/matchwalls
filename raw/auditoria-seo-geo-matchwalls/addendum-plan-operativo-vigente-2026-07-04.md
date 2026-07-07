# Addendum operativo vigente SEO/GEO/AGEO MatchWalls

Fecha: 2026-07-04  
Documento base: `plan-operativo-vigente-y-cola-lotes-seo-geo-2026-06-30.md`  
Estado global: `INCOMPLETO`  
Idiomas prioritarios: ES, EN, FR, DE, NL  
IT/PT: fuera de prioridad activa salvo autorizacion expresa  
Yandex: `STANDBY`

## Criterio de trabajo

El plan historico continua vigente, pero la verdad operativa actual se determina por:

1. Estado real de Shopify/Admin/storefront comprobado.
2. Registro de cambios ejecutados.
3. Evidencia publica y QA.
4. Cola maestra, solo como guia si no contradice evidencia mas reciente.

No se ejecutara ninguna escritura sin aprobacion exacta `APROBADO LOTE [NOMBRE]`.

## Objetivo SEO/GEO/AGEO

Maximizar elegibilidad de MatchWalls para rastreo, indexacion, comprension y citacion en:

- Buscadores: Google, Bing, Yahoo, Brave Search y motores principales.
- Navegadores/capas: Chrome, Edge, Opera, Brave y navegadores modernos.
- IA/GEO/AGEO: ChatGPT, Gemini, Copilot, Claude, Perplexity/Comet, Grok, Meta AI y sistemas que usen web/crawling.

No se garantizan rankings, trafico, indexacion ni citas IA. Si se puede cerrar el trabajo controlable: HTML visible, URLs valiosas, indexabilidad limpia, contenido factual, schema coherente, enlaces internos, multilingualidad y medicion.

## Cerrado desde el plan base

### Landings pais Espana/Francia

| Lote | Estado | Resultado |
|---|---|---|
| `MW-GEO-LANDINGS-CONTENT-REVIEW-012E` | `VERIFICADO Y CORRECTO` | Revision de borradores sin escritura. |
| `MW-GEO-LANDINGS-SPAIN-FRANCE-PAGE-UPDATE-012F` | `CORREGIDO Y VERIFICADO` | Contenido base mejorado en paginas pais. |
| `MW-GEO-LANDINGS-I18N-LANGSHOP-UPDATE-SPAIN-FRANCE-012H` | `CORREGIDO Y VERIFICADO` | Traducciones EN/FR/DE/NL trabajadas en LangShop. |
| `MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-CACHE-STABILITY-RECHECK-012J4F` | `VERIFICADO Y CORRECTO` | Incidencia meta/cache resuelta tras purge/same-value. |
| `MW-GEO-LANDINGS-SPAIN-FRANCE-SCHEMA-MAIN-MANUAL-CODE-012L6B` | `CORREGIDO Y VERIFICADO` | Schema WebPage/FAQPage/Breadcrumb compatible aplicado en MAIN. |
| `MW-GEO-LANDINGS-SPAIN-FRANCE-RICH-RESULTS-POSTCHECK-012L7` | `VERIFICADO Y CORRECTO` | Schema validado publicamente; FAQPage util para GEO aunque Google limite rich results FAQ. |
| `MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-QA-012M` | `VERIFICADO PERO MEJORABLE` | Falta enlazado editorial visible entre landings. |
| `MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-COPY-MAP-012N` | `VERIFICADO Y CORRECTO` | Copy map preparado para ES/EN/FR/DE/NL. |
| `MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-PAGE-BLOCK-012O` | `INCOMPLETO` | Admin correcto, storefront publico no sincronizado. |
| `MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-SYNC-DIAG-012O2` | `VERIFICADO PERO MEJORABLE` | Diagnostico confirma desfase Admin/publico; no hubo escritura. |
| `MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-SAME-VALUE-PURGE-012O3` | `INCOMPLETO` | Same-value aceptado por Shopify, pero sin cambio de `updatedAt`; storefront publico sigue inestable. |
| `MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-WHITESPACE-BUMP-PURGE-012O4` | `INCOMPLETO` | Cambio real invisible aplicado; Admin correcto y traducciones `outdated:false`, pero storefront publico sigue sirviendo versiones mezcladas. |
| `MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-RENDER-SHARD-DIAG-012O5` | `VERIFICADO Y CORRECTO` | Diagnostico de solo lectura completado; 80 solicitudes publicas confirman que `012O` sigue inestable en storefront. |
| `MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-SUPPORT-EVIDENCE-012O6` | `VERIFICADO Y CORRECTO` | Paquete de soporte y tickets Shopify/LangShop preparados; no enviados. |
| `MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-STABILITY-RECHECK-012O5B` | `VERIFICADO Y CORRECTO` | Recheck de propagacion completado; 80 solicitudes, 14 PASS / 66 FAIL; `012O` sigue inestable. |

## Bloqueador activo

### `012O` no esta cerrado publicamente

Hechos verificados:

- Shopify Admin contiene el bloque de enlazado Espana <-> Francia.
- Traducciones EN/FR/DE/NL contienen el bloque y constan `outdated:false`.
- `012O3` same-value aceptado por Shopify, pero no genero cambio de `updatedAt`.
- `012O4` genero cambio real de `updatedAt` y nuevo digest, pero el storefront publico siguio inestable.
- `012O5` confirma el desfase con matriz publica ampliada:
  - 80 solicitudes.
  - 11 PASS.
  - 69 FAIL.
  - 0 `noindex`.
  - 0 canonicals incorrectos.
  - Tema publico mayoritario `178399019384`.
- `012O6` confirma con recheck adicional:
  - 40 solicitudes.
  - 6 PASS.
  - 34 FAIL.
  - Respuestas relevantes `200`.
  - 0 `noindex`.
  - Canonicals correctos.
  - Tema publico `178399019384`.
- `012O5B` confirma que no se ha estabilizado:
  - 80 solicitudes.
  - 14 PASS.
  - 66 FAIL.
  - 0 `noindex`.
  - Respuestas relevantes `200`.
  - Tema publico `178399019384`.
- Las URLs publicas responden `200`, sin `noindex` y con canonicals intactos.
- Las respuestas publicas muestran `theme;desc="178399019384"`, `pageType;desc="page"` y `cf-cache-status: DYNAMIC`.

Estado:

- Admin: `VERIFICADO Y CORRECTO`
- Storefront publico: `INCOMPLETO`

Decision operativa:

- No avanzar con nuevos cambios visibles de contenido pais hasta resolver este desfase.
- No hacer rollback ahora, porque Admin esta correcto y la web publica sigue mostrando contenido antiguo valido.
- No seguir haciendo escrituras de contenido a ciegas: el siguiente paso debe ser diagnostico de render/storefront/translation cache o shard.

## Siguiente decision segura

`REQUIERE DECISION HUMANA`

El paquete `012O6` ya esta preparado. No se debe seguir escribiendo contenido a ciegas.

Opciones:

1. Enviar manualmente los tickets Shopify/LangShop preparados en `012O6`.
2. Adjuntar tambien el CSV `012O5B` si soporte necesita evidencia actualizada.
3. Mantener `012O` bloqueado y avanzar solo con lotes no dependientes de estas landings.

Tickets preparados:

- `ticket-shopify-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-SUPPORT-EVIDENCE-012O6-2026-07-04.md`.
- `ticket-langshop-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-SUPPORT-EVIDENCE-012O6-2026-07-04.md`.

Recheck de propagacion:

- `MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-STABILITY-RECHECK-012O5B` ejecutado y no estable.

No se tocara:

- Shopify.
- LangShop.
- Tema.
- Paginas.
- Handles.
- URLs.
- Titulos.
- SEO meta.
- Canonicals.
- Hreflang.
- Schema.
- Menus.
- Home.
- Footer.
- Productos.
- Colecciones.
- Redirecciones.
- Precios.
- Inventario.

El envio a soporte, purge/flush externo o cualquier cambio alternativo requiere decision humana y/o aprobacion exacta si implica escritura.

## Cola posterior cuando 012O este cerrado

Orden recomendado:

1. Enviar/continuar tickets `012O6`, adjuntando tambien evidencia `012O5B` si el canal lo permite.
2. Si soporte confirma purge/flush, ejecutar un nuevo recheck publico antes de cerrar `012O`.
3. Si un recheck posterior demuestra estabilidad 10/10, cerrar `012O` como `CORREGIDO Y VERIFICADO`.
4. Si el desfase persiste tras soporte, plantear alternativa tecnica reversible con lote formal.
5. Cuando `012O` quede cerrado publicamente, pasar a landings pais siguientes:
   - Alemania brief/copy DE.
   - Paises Bajos brief/copy NL.
   - UK brief/copy EN-UK.
   - Belgica arquitectura bilingue FR/NL.
5. Reanudar indexabilidad estructural:
   - `MW-INDEXABILITY-GEO-COLLECTIONS-NOINDEX-ROLLING-011E3` solo con propuesta formal y bloque pequeno.
   - Canonicals/hreflang post-cambios si cambia cualquier arquitectura.
6. Buscadores y crawlers:
   - `MW-CRAWLERS-SEARCH-AI-POLICY-DIAG-012D1`.
   - Bing Webmaster / Yahoo / Copilot.
   - IndexNow diseno e implementacion.
   - Politica de bots IA separando busqueda/cita de entrenamiento.
7. Entidad factual y schema global:
   - `MW-ENTITY-EVIDENCE-013A`.
   - `MW-ENTITY-CONTENT-I18N-013B`.
   - `MW-SCHEMA-GLOBAL-AUDIT-013C`.
8. Contenido citable:
   - Guias de medicion e instalacion.
   - Mural vs papel pintado en rollo.
   - Non-woven vs vinilo vs autoadhesivo.
   - FAQs de compra, mantenimiento y retirada.
   - Casos B2B verificables.
9. Panel CEO/CMO:
   - Solo cuando existan accesos o exportaciones reales de GSC, GA4, Bing, CrUX, Merchant Center y datos comerciales.

## Estado de publicacion posible ahora

Publicable/cerrado:

- H1 semantico.
- Deuda tecnica 010P.
- Limpiezas principales de indexabilidad ya verificadas.
- Schema pais Espana/Francia 012L6B.
- Copy/i18n landings Espana/Francia 012F/012H.

No publicar nuevos cambios visibles todavia:

- Bloque de enlazado interno 012O hasta resolver sync publico.
- Nuevas landings DE/NL/UK/BE hasta cerrar Espana/Francia.
- Noindex geograficas rolling hasta propuesta formal.
- Crawlers/IndexNow hasta diagnostico y aprobacion.

## Nota sobre idiomas

Cada avance visible debe contemplar ES, EN, FR, DE y NL. Las traducciones pueden trabajar con Shopify Translate y LangShop, pero se verificaran contra el estado real de Shopify/Admin y storefront publico.
