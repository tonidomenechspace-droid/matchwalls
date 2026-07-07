# Ejecucion manual - MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-NATIVE-BASE-PILOT-012J3

Fecha: 2026-07-04  
Estado: `INCORRECTO`  
Tipo: escritura manual controlada en Shopify Pages nativo.  
Ejecucion Shopify: guardado declarado por Daniel; QA publico detecta efecto secundario.  
LangShop: no tocar.  
Shopify Translate: no tocar.

## 1. Aprobacion

Aprobacion exacta recibida:

`APROBADO LOTE MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-NATIVE-BASE-PILOT-012J3`

## 2. Respaldo previo

Valores previos verificados en 012J2A:

- Pagina: `papel-pintado-espana`
- Shopify Page GID historico: `gid://shopify/Page/687276622200`
- `Titulo de la pagina`: `Papel pintado en España para hogares y proyectos profesionales`
- `Metadescripcion`: `VACIO`
- `Identificador de URL`: `pages/papel-pintado-espana`

Evidencia:

- `evidencias/captura-012J2A-shopify-nativo-espana-seo-fields-2026-07-04.png`

## 3. Cambio autorizado

Completar solo el campo `Metadescripcion` con:

`Papel pintado, murales y soluciones a medida para viviendas y proyectos profesionales en España. Pide muestras y personaliza tu mural.`

## 4. Prohibido durante ejecucion

- No tocar `Titulo de la pagina`.
- No tocar `Identificador de URL`.
- No tocar title/H1/body.
- No tocar LangShop.
- No tocar Shopify Translate.
- No tocar pagina Francia ni idiomas FR/EN/DE/NL.

## 5. Estado actual

Pendiente de que Daniel confirme:

```text
GUARDADO 012J3 ESPAÑA ES
Title tocado: no
URL tocada: no
Body tocado: no
```

Despues de esa confirmacion se ejecuto QA publico.

## 6. QA publico post-guardado

Resultado ES:

- HTTP 200.
- Meta description publica coincide exactamente con el valor propuesto.
- Title, H1 y canonical intactos.
- Sin `noindex`.

Resultado multidioma:

- FR mantiene meta en frances/autogenerada.
- EN no concluyente por respuesta 503.
- DE hereda la metadescripcion ES.
- NL hereda la metadescripcion ES.

Clasificacion:

- ES: `VERIFICADO Y CORRECTO`.
- DE/NL: `INCORRECTO`.
- Estado del lote: `INCORRECTO`.

## 7. Decision operativa

El piloto no debe permanecer publicado como cambio aislado porque contamina metadescripciones de idiomas prioritarios.

Rollback recomendado inmediato:

- borrar solo la `Metadescripcion` nativa ES;
- dejarla en `VACIO`;
- no tocar `Titulo de la pagina`;
- no tocar `Identificador de URL`;
- guardar;
- repetir QA publico.

## 8. Evidencia

- `qa-publico-post-MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-NATIVE-BASE-PILOT-012J3-2026-07-04.csv`
- `incidencia-MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-NATIVE-BASE-PILOT-012J3-2026-07-04.md`
