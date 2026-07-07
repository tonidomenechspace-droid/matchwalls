# MW-THEME-LIBRARY-CLEANUP-SAFE-DELETE-016B

Fecha: 2026-07-06  
Tipo: decisión de limpieza segura de biblioteca de temas  
Estado: `REQUIERE DECISION HUMANA`

## Contexto

Shopify indica `Theme limit reached`: la tienda tiene el máximo de 20 temas.

Se ha ejecutado una consulta de solo lectura a Shopify Admin GraphQL. Resultado:

- Total de temas: 20
- Tema MAIN activo: `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18`
- Temas borrador: 19
- No se ha eliminado nada mediante Codex.

## Candidato único recomendado para eliminar

`CORREGIDO Y VERIFICADO` como candidato de bajo riesgo:

- Nombre: `Dev`
- ID: `gid://shopify/OnlineStoreTheme/141375406307`
- ID numérico visible en admin: `141375406307`
- Rol: `UNPUBLISHED`
- Prefijo: `/t/27`
- Creado: `2024-07-11T17:38:11Z`
- Última actualización: `2024-07-21T20:46:51Z`
- themeStoreId: vacío
- processing: `false`
- processingFailed: `false`

## Motivo

El tema `Dev` es un borrador antiguo, genérico, sin rol MAIN, sin actualización desde julio de 2024 y sin uso documentado en los lotes actuales SEO/GEO/AGEO.

Se prefiere frente a otros candidatos porque:

- No contiene `Production` en el nombre.
- No contiene `hotfix`.
- No contiene `schema`.
- No contiene `QA` reciente.
- No contiene `NO ELIMINAR`.
- No corresponde al MAIN actual.
- No forma parte visible de los lotes recientes 010, 012, 013, 014 o 015.

## Temas protegidos

No eliminar:

- `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18` — MAIN activo.
- `MatchWalls/Original/ NO ELIMINAR` — protegido por nombre.
- `Production - 24/08/2024` — posible reversión histórica.
- `Production` — actualizado en 2026, posible reversión.
- `Production - SEO fix AggregateRating (2026-06-12)` — hotfix SEO.
- `SEO schema hotfix - 2026-06-15` — referencia schema/hotfix.
- `MW-FOOTER-I18N-001 - QA - 2026-06-17` — QA i18n/footer.
- `MW-THEME-PAGE-H1-SEMANTIC-008E - ISOLATED QA - ...` — QA/H1 reciente.
- `SEO-GEO staging - 2026-06-15` — marcado incorrecto, pero conservar como evidencia hasta cierre documental.

## Riesgo

`VERIFICADO PERO MEJORABLE`

Eliminar un tema borrador no afecta al storefront público si no es MAIN. El riesgo principal es perder una referencia histórica no documentada. Por eso se recomienda eliminar solo un tema y elegir el borrador más genérico y antiguo.

## Reversión

`INCOMPLETO`

Shopify no ofrece reversión automática tras eliminar un tema desde Admin. La reversión real sería reimportar ZIP o restaurar desde repositorio/copia si existiera. Por eso solo se libera un hueco y se evita tocar temas con posible valor de rollback.

## Ejecución

`REQUIERE DECISION HUMANA`

La herramienta conectada de Shopify bloquea eliminación de temas por seguridad. La acción debe hacerla Daniel manualmente en Shopify Admin, eliminando exactamente:

`Dev` / `141375406307`

