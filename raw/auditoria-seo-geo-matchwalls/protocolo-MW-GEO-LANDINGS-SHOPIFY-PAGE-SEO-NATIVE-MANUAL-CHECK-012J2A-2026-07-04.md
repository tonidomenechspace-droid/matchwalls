# Protocolo — MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-NATIVE-MANUAL-CHECK-012J2A

Fecha: 2026-07-04  
Tipo: comprobacion manual nativa de Shopify Pages.  
Cambios Shopify: no.  
Cambios LangShop: no.  
Estado: `VERIFICADO Y CORRECTO`

## 1. Documentos leidos

- `diagnostico-MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-SOURCE-DIAG-012J2-2026-07-04.md`
- `diagnostico-MW-GEO-LANDINGS-I18N-LANGSHOP-SEO-META-SAVE-FAIL-DIAG-012J1B-2026-07-04.md`
- `diagnostico-MW-GEO-LANDINGS-I18N-SEO-META-DIAG-012I-2026-07-03.md`
- `registro-cambios-ejecutados.md`

## 2. Estado real previo

- LangShop SEO meta para pagina Espana FR no persiste el guardado.
- La via LangShop SEO meta queda abortada para escalado.
- Shopify Help Center documenta que las paginas nativas permiten editar search engine listing con:
  - `Page title`;
  - `Meta description`;
  - `URL handle`.
- 012J2 no pudo leer la fuente exacta de MatchWalls desde API/GraphQL.
- El HTML publico ES y FR se comporta como fallback automatico desde titulo/body.

## 3. Objetivo de 012J2A

Leer sin modificar los campos SEO nativos de la pagina base ES:

- Pagina: `papel-pintado-espana`.
- Shopify Page GID historico: `gid://shopify/Page/687276622200`.
- URL publica: `https://www.matchwalls.com/pages/papel-pintado-espana`.

Campos a leer:

- `Page title` / titulo de pagina SEO.
- `Meta description` / descripcion SEO.
- `URL handle`.

## 4. Prohibido durante 012J2A

No modificar:

- Page title.
- Meta description.
- URL handle.
- Titulo de pagina.
- Body/contenido.
- Visibilidad.
- Plantilla.

No pulsar:

- `Save` / `Guardar`.
- Botones de generar texto.
- Cambios de URL/redirect.
- Acciones masivas.

## 5. Pasos manuales

1. En Shopify Admin, salir de LangShop si sigue abierto.
2. Ir a:
   - `Tienda online` > `Páginas`.
3. Buscar o abrir la pagina:
   - `papel-pintado-espana`
   - o titulo `Papel pintado en España para hogares y proyectos profesionales`.
4. En la pagina nativa, localizar:
   - `Vista previa del listado del motor de búsqueda`
   - o `Search engine listing preview`.
5. Pulsar solo:
   - `Editar SEO del sitio web`
   - o el icono/lapiz de edicion SEO.
6. Leer los campos, sin escribir:
   - `Título de la página` / `Page title`.
   - `Meta descripción` / `Meta description`.
   - `URL handle`.
7. No guardar.

## 6. Texto de respuesta esperado

Si los campos aparecen:

```text
CONFIRMADO 012J2A SHOPIFY NATIVO ESPAÑA:
Page title actual ES: "[valor exacto o VACIO]"
Meta description actual ES: "[valor exacto o VACIO]"
URL handle actual: "[valor exacto]"
URL tocada: no.
Guardado: no.
```

Si no aparecen:

```text
NO VISIBLE 012J2A SHOPIFY NATIVO ESPAÑA:
No aparecen Page title / Meta description en Shopify Pages.
URL tocada: no.
Guardado: no.
```

## 7. Criterio de salida

012J2A quedara `VERIFICADO Y CORRECTO` si:

- se ven los campos nativos;
- se capturan los valores exactos o se confirma `VACIO`;
- se confirma que no se toco URL;
- se confirma que no se guardo.

Quedara `NO ACCESIBLE` si:

- no se encuentran esos campos;
- la pagina no abre;
- Shopify impide leer sin entrar en modo edicion no seguro.

## 8. Decision posterior

Si Page title/meta description estan vacios:

- No escribir todavia.
- Preparar, si se decide, propuesta formal para piloto ES base:
  - `MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-NATIVE-BASE-PILOT-012J3`

Si estan poblados:

- Registrar valores.
- Comparar contra HTML publico.
- No escribir hasta diagnostico.

Si no existen:

- Cerrar via metas manuales para paginas por ahora.

## 9. Resultado comprobado

Resultado recibido por captura de Daniel en Shopify Admin nativo:

- URL admin visible: `admin.shopify.com/store/matchwalls/pages/687276622200`
- Campo `Titulo de la pagina`: visible.
- Valor actual: `Papel pintado en España para hogares y proyectos profesionales`
- Campo `Metadescripcion`: visible.
- Valor actual: `VACIO`
- Campo `Identificador de URL`: visible.
- Valor actual: `pages/papel-pintado-espana`
- URL tocada: no.
- Guardado: no.

Clasificacion del protocolo: `VERIFICADO Y CORRECTO`.

Clasificacion SEO del recurso: `VERIFICADO PERO MEJORABLE`, porque la metadescripcion nativa ES existe pero esta vacia.

Evidencia:

- `evidencias/captura-012J2A-shopify-nativo-espana-seo-fields-2026-07-04.png`
- `resultado-MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-NATIVE-MANUAL-CHECK-012J2A-2026-07-04.md`
