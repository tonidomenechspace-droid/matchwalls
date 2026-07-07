# Protocolo — MW-GEO-LANDINGS-I18N-LANGSHOP-SEO-META-MANUAL-CHECK-012I3

Fecha: 2026-07-04  
Tipo: comprobacion manual guiada en LangShop.  
Cambios Shopify: no.  
Cambios LangShop: no.  
Estado: `VERIFICADO Y CORRECTO`

## 1. Documentos leidos

- `diagnostico-MW-GEO-LANDINGS-I18N-SEO-META-DIAG-012I-2026-07-03.md`
- `seo-meta-copy-MW-GEO-LANDINGS-I18N-SEO-META-COPY-012I1-2026-07-03.md`
- `diagnostico-MW-GEO-LANDINGS-I18N-LANGSHOP-SEO-META-FIELD-CHECK-012I2-2026-07-03.md`
- `registro-cambios-ejecutados.md`

## 2. Estado real previo

- 012I: HTML publico de las paginas Espana/Francia en ES, FR, EN, DE y NL estaba en idioma correcto.
- 012I: no hay campo SEO/meta expuesto por Shopify Admin GraphQL ni metafield SEO detectable para estas paginas.
- 012I1: copy SEO meta preparado para 10 combinaciones pais/idioma.
- 012I2: LangShop mostro dentro de pagina el bloque `Vista previa del listado del motor de búsqueda`, el enlace `Editar SEO del sitio web` y los campos `Título de la página` y `Meta descripción`.
- 012I2: la comprobacion automatizada en idiomas prioritarios quedo `NO ACCESIBLE`; por eso se requiere comprobacion manual humana.

## 3. Objetivo de 012I3

Confirmar manualmente, sin guardar, que en al menos una pagina e idioma prioritario LangShop muestra:

1. `Editar SEO del sitio web`.
2. `Título de la página`.
3. `Meta descripción`.
4. Campos correspondientes al idioma prioritario correcto.
5. Valores actuales exactos o confirmacion de campo vacio.

Pagina recomendada para primera comprobacion:

- Espana FR: `papel-pintado-espana` / pagina traducida FR `Papier peint en Espagne...`

## 4. Prohibido durante 012I3

No pulsar:

- `Save`.
- `Guardar`.
- `Traducir`.
- `Actualización`.
- `Actualizar todas las estadísticas`.
- Cualquier boton de traduccion automatica.

No modificar:

- `Título`.
- `Descripción` / body.
- `URL`.
- `Título de la página`.
- `Meta descripción`.

## 5. Pasos manuales

1. Abrir Shopify Admin.
2. Entrar en Apps > LangShop > Traducciones.
3. Entrar en recurso `Páginas`.
4. Cambiar el idioma a `Francés` / `FR`.
5. Abrir la pagina de Espana:
   - buscar `Papier peint en Espagne` o la pagina equivalente de `papel-pintado-espana`.
6. En el detalle de la pagina, localizar:
   - `Vista previa del listado del motor de búsqueda`.
7. Pulsar solo:
   - `Editar SEO del sitio web`.
8. Comprobar si aparecen:
   - `Título de la página`.
   - `Meta descripción`.
9. Copiar los valores actuales exactos de los campos traducidos FR.
10. No guardar.

## 6. Texto de respuesta esperado

Si los campos aparecen:

```text
CONFIRMADO 012I3 ESPAÑA FR:
Campos SEO visibles: sí.
SEO title actual FR: "[valor exacto o VACIO]"
Meta description actual FR: "[valor exacto o VACIO]"
URL tocada: no.
Guardado: no.
```

Si no aparecen:

```text
NO VISIBLE 012I3 ESPAÑA FR:
No aparecen Título de la página / Meta descripción en LangShop FR.
URL tocada: no.
Guardado: no.
```

## 7. Criterio de salida

012I3 podra cerrarse como `VERIFICADO Y CORRECTO` si Daniel confirma que:

- los campos aparecen en FR;
- los valores actuales quedan capturados;
- no se ha guardado ni modificado nada.

Si no aparecen los campos:

- estado `REQUIERE DECISION HUMANA`;
- no se prepara 012J hasta decidir otra via.

## 8. Siguiente paso

Si 012I3 queda confirmado:

- preparar propuesta formal `MW-GEO-LANDINGS-I18N-LANGSHOP-SEO-META-UPDATE-012J`.

Antes de ejecutar 012J haran falta:

- valores actuales exactos;
- valores propuestos desde 012I1;
- respaldo;
- metodo de reversion;
- aprobacion exacta `APROBADO LOTE MW-GEO-LANDINGS-I18N-LANGSHOP-SEO-META-UPDATE-012J`.

## 9. Confirmacion recibida

Daniel confirmo:

```text
CONFIRMADO 012I3 ESPAÑA FR:
Campos SEO visibles: sí.
SEO title actual FR: "VACIO"
Meta description actual FR: "VACIO"
URL tocada: no.
Guardado: no.
```

Clasificacion:

- Campos SEO en idioma prioritario FR: `VERIFICADO Y CORRECTO`.
- Valores actuales España FR: `VERIFICADO Y CORRECTO`.
- Escritura ejecutada: no.

Decision:

- 012I3 queda cerrado.
- La ejecucion debe avanzar primero como piloto controlado, no masivo, para verificar si guardar esos campos modifica el HTML publico real.

Evidencia visual recibida:

- `evidencias/captura-012I3-langshop-espana-fr-seo-meta-visible-2026-07-04.png`

La captura muestra:

- URL Admin: `admin.shopify.com/store/matchwalls/apps/langshop/translations/pages/687276622200/fr`.
- Bloque SEO visible.
- Campos `Título de la página` y `Meta descripción`.
- Columna traducida FR visible.
- Campos vacios.
- No se observa accion de guardado ejecutada.
