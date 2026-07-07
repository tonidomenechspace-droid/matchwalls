# Diagnostico — MW-GEO-LANDINGS-I18N-LANGSHOP-SEO-META-SAVE-FAIL-DIAG-012J1B

Fecha: 2026-07-04  
Tipo: diagnostico de fallo de guardado LangShop.  
Cambios Shopify: no.  
Cambios LangShop: no.  
Estado global: `VERIFICADO PERO MEJORABLE`

## 1. Documentos leidos

- `propuesta-MW-GEO-LANDINGS-I18N-LANGSHOP-SEO-META-PILOT-012J1-2026-07-04.md`
- `postcheck-MW-GEO-LANDINGS-I18N-LANGSHOP-SEO-META-PILOT-012J1-2026-07-04.md`
- `incidencia-MW-GEO-LANDINGS-I18N-LANGSHOP-SEO-META-SAVE-FAIL-012J1B-2026-07-04.md`
- `registro-cambios-ejecutados.md`

## 2. Estado real comprobado / evidencias

Recurso afectado:

- Pagina: Espana.
- Shopify Page GID: `gid://shopify/Page/687276622200`.
- Idioma: FR.
- Ruta LangShop: `admin.shopify.com/store/matchwalls/apps/langshop/translations/pages/687276622200/fr`.

Valores intentados:

- `Título de la página`: `Papier peint en Espagne | MatchWalls`.
- `Meta descripción`: `Papiers peints, panoramiques et solutions sur mesure en Espagne pour intérieurs résidentiels et projets professionnels. Commandez des échantillons.`

Evidencias visuales:

- `evidencias/captura-012J1-langshop-espana-fr-seo-meta-pendiente-guardar-2026-07-04.png`.
- `evidencias/captura-012J1B-langshop-guardar-no-persiste-sin-error-2026-07-04.png`.
- `evidencias/captura-012J1B-diag-langshop-guardar-piensa-no-persiste-2026-07-04.png`.

Evidencia observada:

- Los valores se pueden introducir en la columna traducida FR.
- La preview interna de LangShop se actualiza.
- Al pulsar `Guardar`, la interfaz parece procesar.
- El banner `Cambios no guardados` permanece.
- No aparece mensaje rojo ni error visible.
- El HTML publico no muestra los valores SEO propuestos.

## 3. Clasificacion

- Campos visibles: `VERIFICADO Y CORRECTO`.
- Valores cargados en formulario: `VERIFICADO Y CORRECTO`.
- Persistencia/guardado: `INCORRECTO`.
- Causa tecnica exacta: `NO ACCESIBLE`.
- HTML publico con nuevos valores: `INCORRECTO`.
- Riesgo de escalar: `RIESGO CRITICO`.

## 4. Inferencia tecnica, separada de hechos verificados

Inferencia principal:

LangShop muestra una capa UI/preview para SEO meta de pagina, pero no consigue persistir esos campos para esta pagina/idioma.

Motivo probable, no demostrado al 100%:

- Los campos SEO fuente/base aparecen vacios.
- 012I verifico previamente que Shopify Admin GraphQL no expone para estas paginas claves traducibles `seo_title`, `meta_title`, `meta_description` ni `description_tag`.
- Por tanto, LangShop puede estar intentando traducir una capa SEO que no existe realmente como recurso persistente de la pagina, o que requiere un valor fuente/base previo.

Hipotesis alternativas:

- fallo temporal de sesion/app;
- validacion silenciosa en LangShop;
- permiso/plan/limite de campo;
- error interno de LangShop;
- necesidad de sincronizacion del recurso antes de guardar.

Estas hipotesis no estan verificadas.

## 5. Decision operativa

No escalar a:

- Francia EN/DE/NL;
- Espana EN/DE/NL;
- Francia FR;
- otras paginas geograficas.

No seguir intentando guardar repetidamente.

No tocar:

- URL;
- `Título`;
- `Descripción`/body;
- metacampos;
- traduccion automatica;
- estadisticas globales de LangShop.

## 6. Accion inmediata recomendada en la pantalla viva

Como los valores no persisten y el piloto queda abortado, la accion segura es limpiar el estado local:

- Pulsar `Descartar` una sola vez.

Motivo:

- `Descartar` elimina cambios locales no guardados.
- No deberia publicar ni escribir nada.
- Evita dejar una pantalla con cambios no guardados que pueda provocar un guardado accidental posterior.

Clasificacion:

- Accion de limpieza UI: `VERIFICADO PERO MEJORABLE`.

## 7. Siguientes vias posibles

### Via recomendada A — no insistir en LangShop SEO meta

Estado:

- `VERIFICADO PERO MEJORABLE`.

Accion:

- Mantener los snippets automaticos actuales.
- Continuar con contenido visible, H1, body, enlaces internos y paginas pais.
- No escalar SEO meta en LangShop hasta tener soporte/evidencia.

Ventaja:

- Cero riesgo operativo.

### Via B — diagnostico de campos SEO fuente/base Shopify

Lote sugerido:

`MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-SOURCE-DIAG-012J2`

Objetivo:

- Revisar en Shopify Admin nativo si la pagina base ES tiene campos SEO title/meta description editables en el editor de pagina.
- No escribir.
- Confirmar si esos campos estan vacios o no existen.

Si existen y estan vacios:

- se podria plantear un piloto base ES separado, con aprobacion exacta, sabiendo que afecta a HTML publico ES.

### Via C — soporte LangShop

Accion:

- Enviar a soporte LangShop capturas y descripcion:
  - ruta `translations/pages/687276622200/fr`;
  - campos SEO meta aceptan texto;
  - preview cambia;
  - `Guardar` procesa pero `Cambios no guardados` permanece;
  - no hay error visible;
  - HTML publico no cambia.

Estado:

- `REQUIERE DECISION HUMANA`.

### Via D — solucion por tema/metafields

Estado:

- `RIESGO CRITICO` si se intenta sin diseno tecnico.

No recomendada ahora.

Implicaria:

- crear fuente SEO alternativa;
- modificar tema Liquid;
- manejar idiomas;
- garantizar canonicals/hreflang;
- QA completo.

## 8. Conclusion

El piloto ha cumplido su funcion: detectar que la via LangShop SEO meta no es fiable antes de escalar.

Estado final del diagnostico:

- `VERIFICADO PERO MEJORABLE`.

Decision:

- abortar escalado LangShop SEO meta;
- limpiar pantalla local con `Descartar`;
- continuar el plan SEO/GEO por vias de menor riesgo;
- si se desea optimizar meta manual, abrir antes el diagnostico de fuente Shopify nativa `012J2`.

