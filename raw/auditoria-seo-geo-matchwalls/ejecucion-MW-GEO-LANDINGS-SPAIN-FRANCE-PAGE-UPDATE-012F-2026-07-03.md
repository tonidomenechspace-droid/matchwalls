# Ejecución — MW-GEO-LANDINGS-SPAIN-FRANCE-PAGE-UPDATE-012F

Fecha: 2026-07-03  
Estado final del alcance aprobado: `CORREGIDO Y VERIFICADO`  
Cambios Shopify: sí, acotados a páginas país España/Francia.  

## 1. Aprobaciones

Aprobación de lote recibida:

`APROBADO LOTE MW-GEO-LANDINGS-SPAIN-FRANCE-PAGE-UPDATE-012F`

Aprobación de ajuste editorial recibida:

`APROBADO AJUSTE 012F SIN NOTA PUBLICA ALICANTE`

Motivo del ajuste: Alicante está `noindex,nofollow`; se excluye del texto visible y queda solo como decisión interna pendiente. No se publicó ninguna nota técnica sobre Alicante.

## 2. Recursos modificados

| Recurso | ID | Campos modificados |
|---|---|---|
| Página España | `gid://shopify/Page/687276622200` | `title`, `body` |
| Página Francia | `gid://shopify/Page/687276654968` | `title`, `body` |
| Traducción FR de página Francia | `gid://shopify/Page/687276654968` | `fr.title`, `fr.body_html` |

No se modificaron:

- handles;
- redirects;
- colecciones;
- productos;
- precios;
- inventario;
- tema/Liquid;
- robots;
- schema;
- sitemap manual;
- traducciones EN/DE/NL;
- traducción FR de la página España.

## 3. Backup

Backup previo creado:

`backup-pre-MW-GEO-LANDINGS-SPAIN-FRANCE-PAGE-UPDATE-012F-2026-07-03.md`

Contiene títulos y bodies anteriores de España/Francia y traducción FR anterior de Francia.

## 4. Operaciones ejecutadas

1. `pageUpdate` España:
   - ID: `gid://shopify/Page/687276622200`
   - Resultado: 0 `userErrors`
   - Updated at: `2026-07-03T11:56:37Z`

2. `pageUpdate` Francia base:
   - ID: `gid://shopify/Page/687276654968`
   - Resultado: 0 `userErrors`
   - Updated at: `2026-07-03T11:57:06Z`

3. `translationsRegister` Francia FR:
   - ID: `gid://shopify/Page/687276654968`
   - Locale: `fr`
   - Keys: `title`, `body_html`
   - Resultado: 0 `userErrors`
   - Updated at: `2026-07-03T11:58:08Z`

## 5. QA Admin

Admin post-ejecución:

- España:
  - Título actualizado.
  - Body actualizado.
  - Página publicada.
  - Traducción FR de España queda `outdated=true` por cambio de base.

- Francia:
  - Título base actualizado.
  - Body base actualizado.
  - Traducción FR actualizada.
  - Traducción FR `outdated=false`.
  - Handle FR existente conservado: `/fr/pages/papier-peint-en-france`.

## 6. QA público

URLs verificadas:

- `https://www.matchwalls.com/pages/papel-pintado-espana?mwqa=012f`
  - 200
  - H1 nuevo visible
  - canonical propio
  - sin `noindex`
  - texto antiguo de envíos no visible
  - Alicante no visible

- `https://www.matchwalls.com/pages/papel-pintado-francia?mwqa=012f`
  - 200
  - H1 nuevo visible
  - canonical propio
  - sin `noindex`
  - texto antiguo de envíos no visible

- `https://www.matchwalls.com/fr/pages/papier-peint-en-france?mwqa=012f`
  - 200
  - H1 FR nuevo visible
  - canonical propio
  - sin `noindex`
  - enlaces FR verificados

- `https://www.matchwalls.com/fr/pages/papier-peint-france?mwqa=012f`
  - 404
  - correcto porque no se ha usado el handle incorrecto.

## 7. QA sitemap

- Sitemap index: 200, 29 sitemaps.
- Sitemap páginas ES: 200, 41 URLs; contiene España y Francia base.
- Sitemap páginas FR: 200, 41 URLs; contiene `/fr/pages/papier-peint-en-france`.
- La URL incorrecta `/fr/pages/papier-peint-france` no aparece.

## 8. Incidencias y deuda pendiente

No hay fallo crítico dentro del alcance aprobado.

Deuda pendiente:

- La traducción FR de la página España queda `outdated=true`.
- Traducciones EN/DE/NL de estas páginas siguen pendientes de revisión y actualización.
- Alicante queda `REQUIERE DECISION HUMANA` por `noindex,nofollow`.
- SEO meta title/meta description específicos no se tocaron porque `PageUpdateInput` no expone campos SEO directos; se debe tratar con Shopify UI/LangShop/metafields si procede en lote separado.

## 9. Método de reversión

Si se requiere rollback:

1. Usar `backup-pre-MW-GEO-LANDINGS-SPAIN-FRANCE-PAGE-UPDATE-012F-2026-07-03.md`.
2. Restaurar `title` y `body` de ambas páginas con `pageUpdate`.
3. Restaurar traducción FR de Francia con `translationsRegister` o Shopify Translate/LangShop.
4. Repetir QA público y Admin.

## 10. Evidencias

- `backup-pre-MW-GEO-LANDINGS-SPAIN-FRANCE-PAGE-UPDATE-012F-2026-07-03.md`
- `mutation-results-MW-GEO-LANDINGS-SPAIN-FRANCE-PAGE-UPDATE-012F-2026-07-03.csv`
- `admin-post-MW-GEO-LANDINGS-SPAIN-FRANCE-PAGE-UPDATE-012F-2026-07-03.csv`
- `qa-publico-post-MW-GEO-LANDINGS-SPAIN-FRANCE-PAGE-UPDATE-012F-2026-07-03.csv`
- `qa-sitemap-post-MW-GEO-LANDINGS-SPAIN-FRANCE-PAGE-UPDATE-012F-2026-07-03.csv`

