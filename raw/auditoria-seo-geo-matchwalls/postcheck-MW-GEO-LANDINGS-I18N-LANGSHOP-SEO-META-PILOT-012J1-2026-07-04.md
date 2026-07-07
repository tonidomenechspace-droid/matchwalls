# Postcheck — MW-GEO-LANDINGS-I18N-LANGSHOP-SEO-META-PILOT-012J1

Fecha: 2026-07-04  
Estado: `VERIFICADO PERO MEJORABLE`  
Cambios LangShop: declarados por Daniel, no verificados por lectura interna posterior.  
HTML publico: verificado, pero no refleja todavia los valores SEO propuestos.

## 1. Confirmacion de guardado recibida

Daniel confirmo:

```text
GUARDADO 012J1 ESPAÑA FR
URL tocada: no
Título/body tocados: no
```

Clasificacion:

- Guardado en LangShop: `DECLARADO PERO NO VERIFICADO`.
- URL/title/body no tocados: `DECLARADO PERO NO VERIFICADO`.

## 2. Valores aprobados

Campo `Título de la página`:

```text
Papier peint en Espagne | MatchWalls
```

Campo `Meta descripción`:

```text
Papiers peints, panoramiques et solutions sur mesure en Espagne pour intérieurs résidentiels et projets professionnels. Commandez des échantillons.
```

## 3. QA publico realizado

URL comprobada:

- `https://www.matchwalls.com/fr/pages/papier-peint-en-espagne?mwqa=012j1`

Segundo control con cache evitada:

- parametro unico `mwqa=012j1b_[timestamp]`.
- cabeceras `Cache-Control: no-cache` y `Pragma: no-cache`.

Resultado tecnico:

- HTTP 200.
- Canonical: `https://www.matchwalls.com/fr/pages/papier-peint-en-espagne`.
- No `noindex`.
- 8 hreflang detectados.
- H1 correcto:
  - `Papier peint en Espagne pour intérieurs résidentiels et projets professionnels`.

## 4. Resultado de title/meta publico

`<title>` observado:

```text
Papier peint en Espagne pour intérieurs résidentiels et projets profes
```

Meta description observada:

```text
Papiers peints, panoramiques et solutions sur mesure en Espagne Chez MatchWalls, nous concevons des papiers peints, des panoramiques décoratifs et des solutions murales sur mesure pour les intérieurs résidentiels, hôtels, restaurants, bureaux, boutiques et espaces professionnels en Espagne. Vous pouvez explorer des des
```

Comparacion:

- SEO title esperado en HTML: no aparece.
- Meta description esperada en HTML: no aparece.
- Los valores propuestos tampoco aparecen como texto dentro del HTML descargado.

Archivo QA:

- `qa-publico-post-MW-GEO-LANDINGS-I18N-LANGSHOP-SEO-META-PILOT-012J1-2026-07-04.csv`.

## 5. Interpretacion

No se puede considerar el piloto como `CORREGIDO Y VERIFICADO`.

Con la evidencia actual, hay tres posibilidades:

1. LangShop guardo el valor, pero todavia no lo ha propagado al HTML publico.
2. LangShop guardo el valor para preview interna, pero el tema/Shopify no lo usa en el HTML publico.
3. El valor no quedo almacenado en la columna traducida FR tras guardar.

No hay evidencia de rotura tecnica publica:

- la pagina sigue 200;
- sigue indexable;
- canonical y hreflang se mantienen;
- H1/body no parecen alterados en el HTML publico.

## 6. Decision operativa

No extender a otros idiomas ni paginas.

Siguiente paso seguro:

`MW-GEO-LANDINGS-I18N-LANGSHOP-SEO-META-STORAGE-CHECK-012J1A`

Objetivo:

- Recargar LangShop en Espana FR.
- Confirmar si los campos `Título de la página` y `Meta descripción` conservan los valores pegados.
- No escribir.
- No guardar.

Si los valores siguen ahi:

- esperar/cache o investigar si el tema no consume esos campos.

Si los valores no estan:

- el guardado no persistio y no debe escalarse.

## 7. Reversion

No se ejecuta reversion ahora porque:

- los valores previos eran `VACIO`;
- el HTML publico no muestra los valores nuevos;
- no hay evidencia de impacto publico negativo.

Si se detecta impacto posterior no deseado:

- vaciar `Título de la página`;
- vaciar `Meta descripción`;
- guardar;
- repetir QA publico.

## 8. Evidencia posterior de estado no guardado

Daniel envio captura posterior de LangShop:

- `evidencias/captura-012J1-langshop-espana-fr-seo-meta-pendiente-guardar-2026-07-04.png`.

La captura muestra:

- valores propuestos presentes en la columna traducida FR;
- preview interna de LangShop actualizada;
- banner superior `Cambios no guardados`;
- boton `Guardar` visible.

Interpretacion actualizada:

- Los valores estan cargados en el formulario de LangShop.
- No se puede considerar persistido hasta pulsar `Guardar` y comprobar que desaparece el aviso de cambios no guardados.
- El QA publico anterior sigue siendo valido como evidencia de que, antes del guardado efectivo, el HTML publico no habia cambiado.

## 9. Incidencia declarada de guardado

Daniel informa posteriormente:

```text
no me los guarda
```

Estado:

- Guardado/persistencia: `DECLARADO PERO NO VERIFICADO`.
- No se debe escalar a mas idiomas/paginas.
- Debe abrirse diagnostico especifico de fallo de guardado antes de cualquier alternativa.

Documento de incidencia:

- `incidencia-MW-GEO-LANDINGS-I18N-LANGSHOP-SEO-META-SAVE-FAIL-012J1B-2026-07-04.md`.

Evidencia adicional:

- `evidencias/captura-012J1B-langshop-guardar-no-persiste-sin-error-2026-07-04.png`.

Conclusion actualizada:

- El piloto 012J1 no debe continuar hacia escalado.
- El guardado de campos SEO meta en LangShop no persiste visualmente y no muestra error visible.
- La causa queda `NO ACCESIBLE` hasta diagnostico especifico.
