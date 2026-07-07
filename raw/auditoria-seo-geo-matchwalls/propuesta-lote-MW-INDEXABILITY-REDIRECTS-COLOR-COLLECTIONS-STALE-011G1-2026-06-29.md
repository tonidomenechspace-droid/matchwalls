# Propuesta de lote MW-INDEXABILITY-REDIRECTS-COLOR-COLLECTIONS-STALE-011G1

Fecha: 2026-06-29  
Estado: `REQUIERE DECISION HUMANA`  
Tipo: propuesta de escritura acotada en Shopify Admin  

## 1. Nombre y alcance exacto del lote

`MW-INDEXABILITY-REDIRECTS-COLOR-COLLECTIONS-STALE-011G1`

Alcance propuesto:

- Eliminar únicamente 14 objetos `UrlRedirect` de Shopify Admin.
- No tocar colecciones.
- No tocar handles.
- No tocar productos.
- No tocar páginas.
- No tocar sitemap manualmente.
- No tocar canonicals.
- No tocar tema Shopify.
- No tocar contenido visible.

Motivo: son redirects Admin obsoletos/inertes sobre colecciones ES de color que actualmente existen, cargan `200`, están en sitemap exacto y tienen canonical propio. Sus targets Admin, en cambio, devuelven `404`.

## 2. Recursos, IDs, URLs e idioma afectados

Idioma afectado: ES.

| ID Shopify | Path actual | Target actual |
|---|---|---|
| `gid://shopify/UrlRedirect/417542766819` | `/collections/papeles-pintados-color-blanco-y-negro` | `/collections/blanco-y-negro-murales` |
| `gid://shopify/UrlRedirect/417542799587` | `/collections/papeles-pintados-color-azul` | `/collections/murales-en-azul` |
| `gid://shopify/UrlRedirect/417542832355` | `/collections/papeles-pintados-color-amarillo` | `/collections/murales-en-amarillo` |
| `gid://shopify/UrlRedirect/417542865123` | `/collections/papeles-pintados-color-blanco` | `/collections/murales-en-blanco` |
| `gid://shopify/UrlRedirect/417542897891` | `/collections/papeles-pintados-color-beige` | `/collections/murales-en-beige` |
| `gid://shopify/UrlRedirect/417542930659` | `/collections/papeles-pintados-color-negro` | `/collections/murales-en-negro` |
| `gid://shopify/UrlRedirect/417542963427` | `/collections/papeles-pintados-color-gris` | `/collections/murales-en-gris` |
| `gid://shopify/UrlRedirect/417542996195` | `/collections/papeles-pintados-color-marron` | `/collections/murales-en-marron` |
| `gid://shopify/UrlRedirect/417543028963` | `/collections/papeles-pintados-color-rosa` | `/collections/murales-en-rosa` |
| `gid://shopify/UrlRedirect/417543061731` | `/collections/papeles-pintados-color-lila` | `/collections/murales-en-lila` |
| `gid://shopify/UrlRedirect/417543094499` | `/collections/papeles-pintados-color-verde` | `/collections/murales-en-verde` |
| `gid://shopify/UrlRedirect/417543127267` | `/collections/papeles-pintados-color-dorado` | `/collections/murales-en-dorado` |
| `gid://shopify/UrlRedirect/417543160035` | `/collections/papeles-pintados-color-plateado` | `/collections/murales-en-plateado` |
| `gid://shopify/UrlRedirect/417543192803` | `/collections/papeles-pintados-color-multicolor` | `/collections/murales-en-multicolor` |

## 3. Valores actuales

`VERIFICADO Y CORRECTO`

Consulta Admin Shopify de solo lectura:

- Los 14 redirects existen actualmente con los IDs, paths y targets indicados.
- Total redirects Admin actual: 634, precisión `EXACT`.

Archivo de respaldo previo:

- `backup-pre-MW-INDEXABILITY-REDIRECTS-COLOR-COLLECTIONS-STALE-011G1-2026-06-29.csv`

## 4. Valores propuestos

`REQUIERE DECISION HUMANA`

Eliminar los 14 objetos `UrlRedirect`.

Resultado Admin esperado:

- Cada `urlRedirect(id)` eliminado debe devolver `null` en postcheck.
- Cada `path:/collections/papeles-pintados-color-*` correspondiente debe quedar sin redirect Admin.
- Total redirects esperado si no hay otros cambios simultáneos: 620.

Resultado público esperado:

- Las 14 URLs fuente deben seguir cargando `200` porque son colecciones reales.
- Deben conservar canonical propio.
- Deben seguir presentes en sitemap exacto si Shopify mantiene esas colecciones publicadas.
- No se espera cambio visual público inmediato, porque los redirects están inertes mientras las colecciones fuente existen.

## 5. Evidencia y motivo técnico

`RIESGO CRITICO`

Evidencias:

- `diagnostico-MW-INDEXABILITY-REDIRECTS-GLOBAL-REMAINING-DIAG-011G-2026-06-29.md`
- `qa-sitemap-exact-MW-INDEXABILITY-REDIRECTS-GLOBAL-REMAINING-DIAG-011G-2026-06-29.csv`
- `qa-publico-sitemap-sources-MW-INDEXABILITY-REDIRECTS-GLOBAL-REMAINING-DIAG-011G-2026-06-29.csv`
- `backup-pre-MW-INDEXABILITY-REDIRECTS-COLOR-COLLECTIONS-STALE-011G1-2026-06-29.csv`
- `qa-publico-pre-MW-INDEXABILITY-REDIRECTS-COLOR-COLLECTIONS-STALE-011G1-2026-06-29.csv`
- `qa-sitemap-exact-pre-MW-INDEXABILITY-REDIRECTS-COLOR-COLLECTIONS-STALE-011G1-2026-06-29.csv`
- `qa-publico-recheck-murales-en-dorado-MW-INDEXABILITY-REDIRECTS-COLOR-COLLECTIONS-STALE-011G1-2026-06-29.csv`

Hechos verificados:

- Las 14 fuentes `/collections/papeles-pintados-color-*` cargan `200`.
- Las 14 fuentes aparecen en sitemap exacto.
- Las 14 fuentes son colecciones reales visibles, no redirects públicos activos.
- Los 14 targets Admin devuelven `404`.
- Los redirects Admin son inertes ahora, pero son deuda peligrosa porque si una colección fuente desaparece o cambia, Shopify podría empezar a aplicar un redirect hacia un destino muerto.

## 6. Riesgos y efectos secundarios

`VERIFICADO PERO MEJORABLE`

Riesgo bajo-medio, acotado.

Riesgos:

- Si alguna URL fuente dejara de existir en el futuro, ya no tendría este redirect legacy como fallback.
- Si hubiera una dependencia interna desconocida del redirect Admin, se perdería. No se ha observado dependencia pública porque las fuentes responden `200` directo.
- `0 userErrors` en la mutación solo confirmaría aceptación por Shopify; no demostraría que el resultado público sea correcto. Por eso se exige postcheck público.

Mitigación:

- Ejecutar eliminación una a una, no en bulk async.
- Parar ante cualquier `userErrors`.
- Verificar Admin y storefront inmediatamente después.
- Conservar backup CSV para recreación exacta.

## 7. Respaldo disponible

`VERIFICADO Y CORRECTO`

Archivo:

- `backup-pre-MW-INDEXABILITY-REDIRECTS-COLOR-COLLECTIONS-STALE-011G1-2026-06-29.csv`

Contiene:

- ID original.
- Path original.
- Target original.

## 8. Método exacto de ejecución

`REQUIERE DECISION HUMANA`

Mutación validada contra schema, no ejecutada:

```graphql
mutation DeleteOneUrlRedirect011G1($id: ID!) {
  urlRedirectDelete(id: $id) {
    deletedUrlRedirectId
    userErrors {
      field
      message
    }
  }
}
```

Ejecución propuesta:

- Ejecutar `urlRedirectDelete` secuencialmente sobre los 14 IDs.
- Registrar `deletedUrlRedirectId`.
- Si aparece cualquier `userErrors`, detener el lote y no continuar.

## 9. Método exacto de reversión

`VERIFICADO Y CORRECTO`

Mutación validada contra schema, no ejecutada:

```graphql
mutation RestoreOneUrlRedirect011G1($path: String!, $target: String!) {
  urlRedirectCreate(urlRedirect: {path: $path, target: $target}) {
    urlRedirect {
      id
      path
      target
    }
    userErrors {
      field
      message
    }
  }
}
```

Reversión:

- Recrear los redirects eliminados usando `path` y `target` del backup.
- Los IDs nuevos no serían necesariamente iguales a los IDs eliminados.
- Verificar después que cada path/target vuelve a existir.

## 10. Pruebas posteriores obligatorias

`REQUIERE DECISION HUMANA`

Postcheck Admin:

- Confirmar que los 14 IDs eliminados devuelven `null`.
- Confirmar que no queda redirect Admin para cada path fuente.
- Confirmar total redirects esperado: 620 si no hubo cambios simultáneos externos.

Postcheck público:

- Revalidar las 14 URLs fuente:
  - status `200`;
  - `0` saltos;
  - canonical propio;
  - H1 visible;
  - sin `noindex` visible salvo cambio externo no previsto.

Postcheck sitemap:

- Confirmar que las 14 fuentes siguen en sitemap exacto.
- Confirmar que los 14 targets `404` no están en sitemap exacto.

Registro:

- Crear archivo de ejecución.
- Crear CSV post Admin.
- Crear CSV post público.
- Actualizar `registro-cambios-ejecutados.md`.

## 11. Aprobación requerida

No autorizado todavía.

Para ejecutar este lote, Daniel debe responder exactamente:

`APROBADO LOTE MW-INDEXABILITY-REDIRECTS-COLOR-COLLECTIONS-STALE-011G1`
