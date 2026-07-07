# Incidencia — MW-GEO-LANDINGS-I18N-LANGSHOP-SEO-META-SAVE-FAIL-012J1B

Fecha: 2026-07-04  
Lote origen: `MW-GEO-LANDINGS-I18N-LANGSHOP-SEO-META-PILOT-012J1`  
Estado: `DECLARADO PERO NO VERIFICADO`

## 1. Contexto

En el piloto 012J1 se intento guardar SEO title/meta description en LangShop para:

- Pagina: Espana.
- Shopify Page GID: `gid://shopify/Page/687276622200`.
- Idioma: FR.
- URL publica: `https://www.matchwalls.com/fr/pages/papier-peint-en-espagne`.

Valores introducidos:

- `Título de la página`: `Papier peint en Espagne | MatchWalls`.
- `Meta descripción`: `Papiers peints, panoramiques et solutions sur mesure en Espagne pour intérieurs résidentiels et projets professionnels. Commandez des échantillons.`

## 2. Evidencia previa

Captura recibida:

- `evidencias/captura-012J1-langshop-espana-fr-seo-meta-pendiente-guardar-2026-07-04.png`.

La captura mostraba:

- valores introducidos en los campos FR;
- preview interna de LangShop actualizada;
- banner `Cambios no guardados`;
- boton `Guardar` visible.

## 3. Incidencia declarada

Daniel informa:

```text
no me los guarda
```

Clasificacion:

- Fallo de guardado/persistencia: `DECLARADO PERO NO VERIFICADO`.
- HTML publico actualizado: no; ya verificado previamente que seguia usando title/meta automaticos.

## 3.1 Evidencia visual posterior

Daniel aporta captura adicional:

- `evidencias/captura-012J1B-langshop-guardar-no-persiste-sin-error-2026-07-04.png`.

La captura muestra:

- URL Admin: `admin.shopify.com/store/matchwalls/apps/langshop/translations/pages/687276622200/fr`.
- Banner superior `Cambios no guardados`.
- Botones `Descartar` y `Guardar`.
- No se observa mensaje rojo, toast de error ni validacion visible.

Daniel informa:

```text
no aparece nada en rojo, clico pero no guarda al pulsar guardar, piensa pero no guarda.
```

Clasificacion actualizada:

- Fallo de guardado/persistencia en UI: `VERIFICADO PERO MEJORABLE`.
- Causa tecnica: `NO ACCESIBLE`.

## 4. Decision operativa

No escalar a otros idiomas ni paginas.

No repetir guardados indefinidamente.

No tocar:

- URL.
- `Título`.
- `Descripción` / body.
- metacampos.
- traduccion automatica.

## 5. Siguiente diagnostico seguro

Lote recomendado:

`MW-GEO-LANDINGS-I18N-LANGSHOP-SEO-META-SAVE-FAIL-DIAG-012J1B`

Objetivo:

- Identificar si LangShop muestra error de validacion, permiso, limite de campo, problema de sesion o fallo de app.
- Verificar si el boton `Guardar` dispara algun mensaje.
- No modificar otros campos.
- No intentar alternativas masivas.

## 5.1 Acciones inmediatas seguras

- No seguir pulsando `Guardar` repetidamente.
- No pulsar `Descartar` hasta decidir si se abandona el piloto o se quiere conservar la pantalla para diagnostico.
- No tocar URL, `Título`, `Descripción`/body ni metacampos.
- Si se quiere diagnosticar sin riesgo, capturar consola/red o probar recarga controlada en lote separado.

## 6. Posibles causas, no verificadas

- Error temporal de LangShop o sesion Shopify.
- Campo SEO traducido visible en UI pero no persistente para paginas.
- Validacion oculta o fallo de permisos.
- Necesidad de recargar/sincronizar recurso antes de guardar.
- El campo puede ser solo preview interna o no estar conectado al objeto publico.

Estas causas son hipotesis, no hechos verificados.
