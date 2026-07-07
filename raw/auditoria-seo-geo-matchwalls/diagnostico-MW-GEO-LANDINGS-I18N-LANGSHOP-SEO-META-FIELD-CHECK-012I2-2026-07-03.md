# Diagnostico — MW-GEO-LANDINGS-I18N-LANGSHOP-SEO-META-FIELD-CHECK-012I2

Fecha: 2026-07-03 19:24 +02:00  
Tipo: diagnostico de solo lectura en LangShop / Shopify Admin.  
Cambios Shopify: no.  
Cambios LangShop: no.  
Estado global: `VERIFICADO PERO MEJORABLE`

## 1. Documentos leidos

- `diagnostico-MW-GEO-LANDINGS-I18N-SEO-META-DIAG-012I-2026-07-03.md`
- `seo-meta-copy-MW-GEO-LANDINGS-I18N-SEO-META-COPY-012I1-2026-07-03.md`
- `ejecucion-MW-GEO-LANDINGS-I18N-LANGSHOP-UPDATE-SPAIN-FRANCE-012H-2026-07-03.md`
- `registro-cambios-ejecutados.md`

## 2. Alcance

Objetivo:

- Comprobar si LangShop muestra campos SEO meta editables para paginas.
- Diferenciar campo real de preview interna.
- No guardar ni modificar nada.

Paginas objetivo posteriores:

- Espana: `gid://shopify/Page/687276622200`, `papel-pintado-espana`.
- Francia: `gid://shopify/Page/687276654968`, `papel-pintado-francia`.

Idiomas objetivo posteriores:

- ES
- FR
- EN
- DE
- NL

## 3. Acciones realizadas

Se abrio en Shopify Admin:

- `https://admin.shopify.com/store/matchwalls/apps/langshop/translations`

Acciones de solo lectura:

- Lectura de pantalla principal de traducciones.
- Apertura del recurso `Páginas`.
- Apertura de detalle de pagina pais Espana dentro de LangShop.
- Apertura del bloque `Editar SEO del sitio web`.
- Lectura de campos visibles.

Acciones no realizadas:

- No se pulso `Save`.
- No se pulso `Discard`.
- No se pulso `Traducir`.
- No se pulso `Actualización`.
- No se pulso `Actualizar todas las estadísticas`.
- No se escribio en ningun campo.

## 4. Hallazgos verificados

### Pantalla principal LangShop

Estado observado:

- Recurso `Páginas`: 55 recursos, 41 traducidos, estado `Desactualizado`.
- Recurso `Metaetiquetas`: 0 recursos, 0 traducidos, estado `Sin artículos`.

Clasificacion:

- `Páginas`: `VERIFICADO PERO MEJORABLE`
- `Metaetiquetas` como recurso separado: `VERIFICADO Y CORRECTO` que no contiene articulos disponibles en esta pantalla.

Interpretacion:

- La optimizacion SEO meta de paginas no parece estar en un recurso separado llamado `Metaetiquetas`.
- La capa SEO aparece dentro del detalle de cada pagina.

### Detalle de pagina en LangShop

Pagina abierta:

- Espana: `gid://shopify/Page/687276622200`.

Nota de alcance:

- La app cargo de forma fiable el detalle en idioma `Árabe`, no en los idiomas prioritarios.
- Esta vista se uso para confirmar estructura de campos, no para preparar ejecucion editorial en arabe.

Campos y bloques observados antes de abrir SEO:

- `Título`
- `Descripción`
- `URL`
- `Vista previa del listado del motor de búsqueda`
- `Editar SEO del sitio web`

Campos observados despues de abrir `Editar SEO del sitio web`:

- `Título de la página`
- `Meta descripción`

Elementos editables detectados:

- 10 campos editables en total.

Inferencia estructural a partir del orden visible:

1. Titulo fuente.
2. Titulo traducido.
3. Descripcion/body fuente.
4. Descripcion/body traducida.
5. URL fuente.
6. URL traducida.
7. SEO title / titulo de pagina fuente.
8. SEO title / titulo de pagina traducido.
9. Meta description fuente.
10. Meta description traducida.

Clasificacion:

- Existencia de bloque SEO dentro de pagina LangShop: `VERIFICADO Y CORRECTO`.
- Existencia de campos `Título de la página` y `Meta descripción` dentro del bloque SEO: `VERIFICADO Y CORRECTO`.
- Verificacion especifica en FR/EN/DE/NL por automatizacion: `NO ACCESIBLE`.

## 5. Elementos no accesibles o no concluyentes

La ruta directa al detalle FR:

- `pages/687276622200/fr`

no renderizo contenido de LangShop de forma fiable dentro del navegador integrado. Solo quedo visible el contenedor basico del iframe.

Por tanto:

- No se puede afirmar todavia que los campos esten poblados/editables correctamente en FR, EN, DE y NL desde la automatizacion.
- No se puede afirmar todavia que guardar esos campos modifique el HTML publico.
- No se puede afirmar todavia que el valor actual exacto de SEO title/meta description por idioma este capturado.

Clasificacion:

- Prioritarios FR/EN/DE/NL en UI LangShop: `NO ACCESIBLE` desde automatizacion en 012I2.
- Publicacion efectiva en HTML tras guardar: `DECLARADO PERO NO VERIFICADO`.

## 6. Riesgos

- LangShop puede mostrar una preview SEO basada en fallback de `title`/`body_html`.
- Los campos SEO pueden existir pero estar vacios y usar fallback publico.
- Guardar SEO meta podria activar botones `Save`/`Discard` y generar cambios no deseados si se manipula fuera de un lote aprobado.
- La vista directa por idioma no fue estable en automatizacion, por lo que la ejecucion debe ser manual y campo a campo si se aprueba.

## 7. Decision operativa

No ejecutar 012J todavia.

Antes de escribir, Daniel debe abrir manualmente una pagina objetivo en LangShop en uno de los idiomas prioritarios y confirmar:

1. Que ve `Editar SEO del sitio web`.
2. Que al abrirlo aparecen `Título de la página` y `Meta descripción`.
3. Que los campos pertenecen al idioma correcto.
4. Que no se va a tocar `URL`.

Si esa comprobacion manual se confirma, se puede preparar lote de escritura:

`MW-GEO-LANDINGS-I18N-LANGSHOP-SEO-META-UPDATE-012J`

## 8. Siguiente paso seguro

Siguiente paso recomendado:

`MW-GEO-LANDINGS-I18N-LANGSHOP-SEO-META-MANUAL-CHECK-012I3`

Objetivo:

- Daniel verifica en pantalla una pagina objetivo en FR/EN/DE/NL.
- Codex guia sin escribir.
- Se capturan los valores actuales exactos antes de cualquier aprobacion de escritura.

Alternativa si Daniel ya confirma que ve esos campos en los idiomas prioritarios:

- Preparar propuesta formal de ejecucion `012J` con:
  - recursos e idiomas;
  - valores actuales;
  - valores nuevos desde 012I1;
  - riesgos;
  - reversion;
  - pruebas publicas posteriores.

