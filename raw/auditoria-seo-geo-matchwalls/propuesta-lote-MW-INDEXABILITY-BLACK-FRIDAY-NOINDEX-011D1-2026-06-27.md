# Propuesta formal - MW-INDEXABILITY-BLACK-FRIDAY-NOINDEX-011D1

Estado: `REQUIERE DECISION HUMANA`

Esta propuesta no ejecuta cambios. La ejecución queda bloqueada hasta recibir aprobación exacta:

`APROBADO LOTE MW-INDEXABILITY-BLACK-FRIDAY-NOINDEX-011D1`

## 1. Nombre y alcance exacto

Lote: `MW-INDEXABILITY-BLACK-FRIDAY-NOINDEX-011D1`

Objetivo: retirar temporalmente de indexación y sitemap la landing Black Friday obsoleta, sin borrar, redirigir ni cambiar handles.

Acción propuesta:

- aplicar `seo.hidden=1` a la colección base `gid://shopify/Collection/646234440056`.

## 2. Recursos, IDs, URLs e idiomas afectados

Recurso Shopify:

- Tipo: `Collection`
- ID: `gid://shopify/Collection/646234440056`
- Legacy ID: `646234440056`
- Título base: `Papel Pintado Black Friday`
- Handle base: `papel-pintado-black-friday`
- Template suffix: `black-friday`
- `seo.hidden` actual: `null`

URLs afectadas:

- ES: `https://www.matchwalls.com/collections/papel-pintado-black-friday`
- EN: `https://www.matchwalls.com/en/collections/wallpapers-black-friday`
- FR: `https://www.matchwalls.com/fr/collections/papiers-peints-black-friday`
- NL: `https://www.matchwalls.com/nl/collections/black-friday-wallpaper`
- IT: `https://www.matchwalls.com/it/collections/sfondi-del-black-friday`
- DE: `https://www.matchwalls.com/de/collections/schwarzer-freitag-wallpaper`
- PT: `https://www.matchwalls.com/pt/collections/papel-de-parede-de-sexta-feira-negra`

## 3. Valores actuales

`INCORRECTO`

- 7/7 URLs responden 200.
- 7/7 URLs están en sitemap.
- 7/7 URLs son indexables.
- 7/7 URLs conservan canonical self.
- 7/7 contienen señales Black Friday 2024.
- `seo.hidden = null`.

## 4. Valores propuestos

`CORREGIDO Y VERIFICADO` solo si el QA posterior confirma:

- `seo.hidden = 1`;
- 7/7 URLs con noindex;
- 7/7 URLs fuera de sitemap.

## 5. Evidencia y motivo técnico

La landing está obsoleta para indexación pública:

- fecha del diagnóstico: 27 de junio de 2026;
- H1/HTML: `Black Friday 2024`;
- contador: `Nov 29, 2024`;
- mensaje público: `La oferta ha finalizado`;
- EN mezcla title 2025 con H1 2024;
- FR tiene body translation de Toulouse, no Black Friday.

## 6. Riesgos y efectos secundarios

`VERIFICADO PERO MEJORABLE`

- Se retira una landing de indexación orgánica hasta nueva campaña.
- Puede reducir impresiones orgánicas de búsquedas Black Friday fuera de temporada.
- No afecta compras directas si alguien visita la URL.
- No afecta redirecciones.
- No afecta handles.
- No afecta plantilla.
- No afecta productos.

## 7. Respaldo disponible

`VERIFICADO Y CORRECTO`

Valor actual:

- `seo.hidden`: `null`.

Respaldo documental:

- `diagnostico-admin-MW-INDEXABILITY-BLACK-FRIDAY-DECISION-011D-2026-06-27.csv`
- `diagnostico-publico-ampliado-MW-INDEXABILITY-BLACK-FRIDAY-DECISION-011D-2026-06-27.csv`
- `diagnostico-sitemap-ampliado-MW-INDEXABILITY-BLACK-FRIDAY-DECISION-011D-2026-06-27.csv`

## 8. Método exacto de reversión

Eliminar el metafield:

- ownerId: `gid://shopify/Collection/646234440056`
- namespace: `seo`
- key: `hidden`

La mutación de rollback `metafieldsDelete` está validada pero no ejecutada.

## 9. Pruebas posteriores

Después de ejecutar:

1. Verificar Admin:
   - `seo.hidden = 1`.
2. Verificar público:
   - 7 URLs accesibles;
   - robots/noindex activo.
3. Verificar sitemap:
   - 7 URLs ausentes.
4. Verificar que no se han creado redirecciones.
5. Registrar resultado en `registro-cambios-ejecutados.md`.

