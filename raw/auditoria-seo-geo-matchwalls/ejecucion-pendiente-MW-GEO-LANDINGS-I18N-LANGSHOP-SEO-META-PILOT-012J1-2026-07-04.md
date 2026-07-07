# Ejecucion pendiente — MW-GEO-LANDINGS-I18N-LANGSHOP-SEO-META-PILOT-012J1

Fecha: 2026-07-04  
Estado: `VERIFICADO PERO MEJORABLE`  
Cambios Shopify/LangShop: guardado declarado por Daniel; efecto publico no verificado como correcto.

## 1. Aprobacion recibida

Daniel aprobo exactamente:

```text
APROBADO LOTE MW-GEO-LANDINGS-I18N-LANGSHOP-SEO-META-PILOT-012J1
```

## 2. Respaldo previo

Recurso:

- Pagina: Espana.
- Shopify Page GID: `gid://shopify/Page/687276622200`.
- Idioma: FR.
- URL publica: `https://www.matchwalls.com/fr/pages/papier-peint-en-espagne`.

Valores previos verificados:

- `Título de la página`: `VACIO`.
- `Meta descripción`: `VACIO`.

Evidencia:

- `evidencias/captura-012I3-langshop-espana-fr-seo-meta-visible-2026-07-04.png`.

## 3. Valores aprobados para guardar

Campo `Título de la página`:

```text
Papier peint en Espagne | MatchWalls
```

Campo `Meta descripción`:

```text
Papiers peints, panoramiques et solutions sur mesure en Espagne pour intérieurs résidentiels et projets professionnels. Commandez des échantillons.
```

## 4. Instrucciones de ejecucion manual

En la pantalla de LangShop ya abierta:

1. Pegar el SEO title aprobado en el campo traducido FR `Título de la página`.
2. Pegar la meta description aprobada en el campo traducido FR `Meta descripción`.
3. No tocar `URL`.
4. No tocar `Título`.
5. No tocar `Descripción` / body.
6. No pulsar flechas de autotraduccion.
7. No pulsar `Traducir`.
8. Pulsar `Save` / `Guardar` una sola vez.

## 5. Confirmacion esperada de Daniel

Tras guardar, Daniel debe responder:

```text
GUARDADO 012J1 ESPAÑA FR
URL tocada: no
Título/body tocados: no
```

## 6. Verificacion posterior pendiente

Despues del guardado se verificara:

- HTML publico de `https://www.matchwalls.com/fr/pages/papier-peint-en-espagne?mwqa=012j1`.
- `<title>`.
- `meta name="description"`.
- `og:title`.
- `og:description`.
- canonical.
- hreflang.
- no `noindex`.
- H1/body sin alteraciones.

## 8. Confirmacion de guardado recibida

Daniel confirmo:

```text
GUARDADO 012J1 ESPAÑA FR
URL tocada: no
Título/body tocados: no
```

Clasificacion:

- Guardado LangShop: `DECLARADO PERO NO VERIFICADO`.
- URL no tocada: `DECLARADO PERO NO VERIFICADO`.
- Titulo/body no tocados: `DECLARADO PERO NO VERIFICADO`.

## 9. QA publico post-guardado

Archivo:

- `qa-publico-post-MW-GEO-LANDINGS-I18N-LANGSHOP-SEO-META-PILOT-012J1-2026-07-04.csv`.

Resultado:

- HTTP 200.
- Canonical correcto.
- Sin `noindex`.
- 8 hreflang.
- H1 correcto.
- El HTML publico no muestra todavia los valores SEO propuestos.

Title observado:

```text
Papier peint en Espagne pour intérieurs résidentiels et projets profes
```

Meta description observada:

```text
Papiers peints, panoramiques et solutions sur mesure en Espagne Chez MatchWalls, nous concevons des papiers peints, des panoramiques décoratifs et des solutions murales sur mesure pour les intérieurs résidentiels, hôtels, restaurants, bureaux, boutiques et espaces professionnels en Espagne. Vous pouvez explorer des des
```

Estado:

- `VERIFICADO PERO MEJORABLE`.

Siguiente paso:

- `MW-GEO-LANDINGS-I18N-LANGSHOP-SEO-META-STORAGE-CHECK-012J1A`.

## 10. Correccion de estado tras captura

Daniel envio captura posterior donde aparece el banner:

```text
Cambios no guardados
```

Evidencia:

- `evidencias/captura-012J1-langshop-espana-fr-seo-meta-pendiente-guardar-2026-07-04.png`.

Estado operativo actualizado:

- Valores en formulario: `VERIFICADO Y CORRECTO`.
- Guardado/persistencia: `INCOMPLETO`.
- Accion pendiente: pulsar `Guardar` una sola vez.

## 7. Reversion

Si falla el piloto:

1. Volver a los campos SEO FR.
2. Vaciar `Título de la página`.
3. Vaciar `Meta descripción`.
4. Guardar.
5. Repetir verificacion publica.
