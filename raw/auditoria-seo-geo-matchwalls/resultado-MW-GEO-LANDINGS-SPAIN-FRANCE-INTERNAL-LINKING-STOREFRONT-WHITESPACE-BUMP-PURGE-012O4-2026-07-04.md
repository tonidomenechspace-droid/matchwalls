# Resultado lote `MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-WHITESPACE-BUMP-PURGE-012O4`

Fecha: 2026-07-04  
Estado final: `INCOMPLETO`

## Aprobacion

Daniel aprobo exactamente:

`APROBADO LOTE MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-WHITESPACE-BUMP-PURGE-012O4`

## Alcance ejecutado

Escritura tecnica controlada sobre:

- `gid://shopify/Page/687276622200` / `papel-pintado-espana`
- `gid://shopify/Page/687276654968` / `papel-pintado-francia`

Idiomas:

- ES base Shopify.
- EN, FR, DE y NL mediante `translationsRegister`.

Campos tratados:

- `body` ES de ambas paginas.
- `body_html` EN/FR/DE/NL de ambas paginas.

Cambio:

- Se inserto una linea en blanco extra invisible antes del bloque FAQ para forzar cambio real de `body_html`.
- No se cambio contenido visible, enlaces, headings, URLs, handles, titulos ni metadatos.

## Campos no tocados

- Handles.
- URLs.
- Titulos.
- SEO title.
- Meta description.
- Canonicals.
- Hreflang.
- Schema.
- Menus.
- Home.
- Footer.
- Tema.
- Productos.
- Colecciones.
- Redirecciones.
- Precios.
- Inventario.

## Respaldo

- `backup-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-WHITESPACE-BUMP-PURGE-012O4-2026-07-04.md`

## Resultado Admin

`VERIFICADO Y CORRECTO`

Operaciones:

- `pageUpdate` Espana: `userErrors: []`.
- `pageUpdate` Francia: `userErrors: []`.
- `translationsRegister` Espana EN/FR/DE/NL: `userErrors: []`.
- `translationsRegister` Francia EN/FR/DE/NL: `userErrors: []`.

Cambios reales confirmados:

- Espana `updatedAt`: `2026-07-04T14:38:21Z`.
- Francia `updatedAt`: `2026-07-04T14:39:03Z`.
- Espana nuevo digest `body_html`: `746c832dbeacf56abf7095b8edb5774803e1243046aec5e55ae20ee10fc2f7a8`.
- Francia nuevo digest `body_html`: `1e4ecb69b20f08101ebc238004b89f63143aab91f16e4b6083ebe158847e623d`.
- Traducciones Espana EN/FR/DE/NL: `outdated:false`, `updatedAt` `2026-07-04T14:40:39Z`.
- Traducciones Francia EN/FR/DE/NL: `outdated:false`, `updatedAt` `2026-07-04T14:41:48Z`.
- Handles y titulos intactos.

## Resultado publico

`INCOMPLETO`

Archivos QA:

- `qa-publico-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-WHITESPACE-BUMP-PURGE-012O4-2026-07-04.csv`
- `qa-publico-recheck2-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-WHITESPACE-BUMP-PURGE-012O4-2026-07-04.csv`
- `qa-publico-recheck3-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-WHITESPACE-BUMP-PURGE-012O4-2026-07-04.csv`

Resultados:

- QA inicial: 2/20 PASS.
- Recheck2 normal: 2/10 PASS.
- Recheck3 browser + Googlebot: 3/20 PASS.

Las URLs responden `200`, sin `noindex` y con canonicals intactos, pero el bloque de enlazado interno no aparece de forma estable.

## Evidencia tecnica relevante

- Las respuestas publicas indican `theme;desc="178399019384"` y `pageType;desc="page"`.
- `cf-cache-status: DYNAMIC`; no se observa un simple HIT de CDN Cloudflare.
- La variacion por `servedBy`, idioma y user-agent sugiere capa de render/storefront/translation cache o shard interno, no un fallo del contenido Admin.

## Conclusion

No se puede cerrar `012O` ni `012O4` como `CORREGIDO Y VERIFICADO`.

El cambio real se aplico y esta correcto en Admin, pero la web publica sigue sirviendo versiones antiguas/inconsistentes segun idioma y user-agent.

No conviene seguir haciendo escrituras de contenido a ciegas. El siguiente paso debe ser diagnostico/evidencia de render layer y soporte.

## Siguiente lote recomendado

`MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-RENDER-SHARD-DIAG-012O5`

Tipo: solo lectura.

Objetivo:

1. Recoger matriz de headers publicos con `requestID`, `servedBy`, `theme`, idioma y user-agent.
2. Comparar Admin GraphQL vs storefront por idioma.
3. Preparar evidencia para Shopify/LangShop si el desfase persiste.
4. No escribir en Shopify ni LangShop.

## Reversion

No se ejecuta rollback porque:

- Admin esta correcto.
- La web publica no esta peor que antes: sigue sirviendo contenido anterior valido en la mayoria de shards.
- El cambio es invisible y reversible.

Si se requiere revertir:

1. Retirar la linea en blanco extra en ES.
2. Leer nuevo digest.
3. Re-registrar traducciones EN/FR/DE/NL con los valores previos.
4. Verificar Admin y publico.
