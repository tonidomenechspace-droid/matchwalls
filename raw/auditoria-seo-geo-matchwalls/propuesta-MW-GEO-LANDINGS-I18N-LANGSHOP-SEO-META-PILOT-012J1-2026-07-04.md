# Propuesta formal — MW-GEO-LANDINGS-I18N-LANGSHOP-SEO-META-PILOT-012J1

Fecha: 2026-07-04  
Tipo: piloto controlado de escritura manual en LangShop.  
Estado: `REQUIERE DECISION HUMANA`  
Cambios Shopify/LangShop propuestos: si, solo si Daniel aprueba exactamente el lote.

## 1. Documentos leidos

- `seo-meta-copy-MW-GEO-LANDINGS-I18N-SEO-META-COPY-012I1-2026-07-03.md`
- `matriz-MW-GEO-LANDINGS-I18N-SEO-META-COPY-012I1-2026-07-03.csv`
- `protocolo-MW-GEO-LANDINGS-I18N-LANGSHOP-SEO-META-MANUAL-CHECK-012I3-2026-07-04.md`
- `matriz-MW-GEO-LANDINGS-I18N-LANGSHOP-SEO-META-MANUAL-CHECK-012I3-2026-07-04.csv`
- `registro-cambios-ejecutados.md`

## 2. Estado real comprobado

Recurso:

- Pais: Espana.
- Idioma: FR.
- Shopify Page GID: `gid://shopify/Page/687276622200`.
- Handle base: `papel-pintado-espana`.
- URL publica localizada: `https://www.matchwalls.com/fr/pages/papier-peint-en-espagne`.
- Ruta LangShop observada: `admin.shopify.com/store/matchwalls/apps/langshop/translations/pages/687276622200/fr`.

Estado verificado en 012I3:

- Campos SEO visibles: si.
- Campo `Título de la página`: visible.
- Campo `Meta descripción`: visible.
- Valor actual SEO title FR: `VACIO`.
- Valor actual meta description FR: `VACIO`.
- URL tocada: no.
- Guardado: no.

Evidencia:

- `evidencias/captura-012I3-langshop-espana-fr-seo-meta-visible-2026-07-04.png`.

## 3. Alcance exacto del piloto

Actualizar solo estos dos campos en LangShop:

| Recurso | Idioma | Campo | Valor actual | Valor propuesto |
|---|---:|---|---|---|
| Espana page `687276622200` | FR | `Título de la página` | `VACIO` | `Papier peint en Espagne \| MatchWalls` |
| Espana page `687276622200` | FR | `Meta descripción` | `VACIO` | `Papiers peints, panoramiques et solutions sur mesure en Espagne pour intérieurs résidentiels et projets professionnels. Commandez des échantillons.` |

Longitudes:

- SEO title propuesto: 36 caracteres.
- Meta description propuesta: 147 caracteres.

## 4. Fuera de alcance

No tocar:

- `Título`.
- `Descripción` / body.
- `URL`.
- Handles.
- Traduccion automatica.
- Botones de flecha de autotraduccion.
- `Traducir`.
- `Actualización`.
- `Actualizar todas las estadísticas`.
- Metacampos.
- Otras paginas.
- Otros idiomas.
- Shopify theme / Liquid.
- Canonicals, hreflang, redirecciones, productos, colecciones, inventario o precios.

## 5. Motivo tecnico

012I verifico que el HTML publico ya esta en idioma correcto, pero los snippets SEO son mejorables.  
012I2 verifico que LangShop tiene bloque SEO dentro de paginas.  
012I3 verifico manualmente que Espana FR tiene campos SEO vacios y visibles.

Este piloto sirve para comprobar si escribir esos campos:

1. se guarda correctamente en LangShop;
2. no altera URL/title/body;
3. modifica el HTML publico real;
4. puede escalarse despues al resto de idiomas/paginas.

## 6. Riesgos

- LangShop puede guardar el campo pero no publicarlo en HTML publico inmediatamente.
- Puede haber cache de Shopify/LangShop.
- El SEO title podria afectar el `<title>` publico o solo la preview interna.
- Tocar por error `URL`, `Título` o `Descripción` afectaria contenido ya corregido en 012H.
- Pulsar traduccion automatica podria sobrescribir valores aprobados.

Riesgo controlado:

- Piloto de una sola pagina/idioma.
- Valores actuales vacios; reversion sencilla.
- No se tocan URL/title/body.

## 7. Respaldo disponible

Valores previos exactos:

- SEO title FR previo: `VACIO`.
- Meta description FR previa: `VACIO`.

Evidencia visual:

- `evidencias/captura-012I3-langshop-espana-fr-seo-meta-visible-2026-07-04.png`.

## 8. Metodo exacto de reversion

Si el piloto falla o produce resultado no deseado:

1. Volver a LangShop > Paginas > Espana > FR.
2. Abrir `Editar SEO del sitio web`.
3. Vaciar `Título de la página`.
4. Vaciar `Meta descripción`.
5. Guardar.
6. Verificar HTML publico de nuevo.

Estado esperado tras reversion:

- SEO title FR: `VACIO`.
- Meta description FR: `VACIO`.

## 9. Ejecucion manual propuesta

Solo despues de aprobacion exacta:

`APROBADO LOTE MW-GEO-LANDINGS-I18N-LANGSHOP-SEO-META-PILOT-012J1`

Pasos:

1. En la pantalla ya abierta de LangShop FR, mantener visible el bloque SEO.
2. En la columna traducida FR, campo `Título de la página`, pegar:

```text
Papier peint en Espagne | MatchWalls
```

3. En la columna traducida FR, campo `Meta descripción`, pegar:

```text
Papiers peints, panoramiques et solutions sur mesure en Espagne pour intérieurs résidentiels et projets professionnels. Commandez des échantillons.
```

4. No tocar `URL`.
5. No tocar `Título` ni `Descripción`.
6. Pulsar `Save` / `Guardar` una sola vez.
7. Informar a Codex:

```text
GUARDADO 012J1 ESPAÑA FR
URL tocada: no
Título/body tocados: no
```

## 10. Pruebas posteriores

Tras el guardado:

1. Verificar en LangShop que los campos siguen poblados.
2. Verificar URL publica:
   - `https://www.matchwalls.com/fr/pages/papier-peint-en-espagne?mwqa=012j1`
3. Comprobar:
   - HTTP 200.
   - canonical propio.
   - no `noindex`.
   - hreflang presente.
   - `<title>` publico.
   - `meta name="description"` publico.
   - `og:title`.
   - `og:description`.
   - que no se haya alterado H1/body.

Estados posibles:

- Si el HTML publico cambia al valor propuesto: `CORREGIDO Y VERIFICADO`.
- Si LangShop guarda pero el HTML publico no cambia aun: `VERIFICADO PERO MEJORABLE` con posible cache/retardo.
- Si se altera URL/title/body: `RIESGO CRITICO` y aplicar reversion.

## 11. Aprobacion requerida

Para ejecutar este piloto, Daniel debe responder exactamente:

```text
APROBADO LOTE MW-GEO-LANDINGS-I18N-LANGSHOP-SEO-META-PILOT-012J1
```

Sin esa frase exacta, no se debe escribir ni guardar nada.

