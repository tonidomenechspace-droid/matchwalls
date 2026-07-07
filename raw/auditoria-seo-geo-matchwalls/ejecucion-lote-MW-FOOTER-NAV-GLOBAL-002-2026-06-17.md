# Ejecución lote MW-FOOTER-NAV-GLOBAL-002 - 2026-06-17

Estado: EJECUTADO Y VERIFICADO PARCIALMENTE

## Aprobación

Daniel aprobó literalmente:

`APROBADO LOTE MW-FOOTER-NAV-GLOBAL-002`

## Objetivo

Reparar la navegación visible del footer publicada, retirando enlaces que Daniel confirmó que no deben aparecer:

- `Tarjeta regalo`
- `Black Friday 2024`
- `Envíos internacionales`

Además, corregir etiquetas fuente del footer en ES.

## Recursos modificados

Se modificaron exclusivamente menús globales de Shopify:

- `footer`: `gid://shopify/Menu/210266325219`
- `footer-profesional`: `gid://shopify/Menu/210972311779`
- `footer-brand`: `gid://shopify/Menu/210972344547`
- `footer-legal`: `gid://shopify/Menu/210972410083`

No se modificaron:

- temas;
- publicaciones;
- productos;
- colecciones;
- páginas;
- URLs;
- handles;
- redirecciones;
- precios;
- inventario;
- variantes;
- imágenes;
- App Embeds.

## Respaldo previo

Documento creado:

- `respaldo-MW-FOOTER-NAV-GLOBAL-002-2026-06-17.md`

Incluye títulos, IDs, tipos, URLs, resource IDs, orden original y método de reversión.

## Mutaciones ejecutadas

Mutación usada:

- `menuUpdate`

Validación previa:

- Operación GraphQL validada correctamente.
- Permisos requeridos por esquema: `write_online_store_navigation`, `read_online_store_navigation`.

Todas las mutaciones devolvieron:

- `userErrors: []`

Nota: `userErrors: []` solo confirma aceptación técnica por Shopify; no equivale por sí solo a QA editorial completa.

## Cambios ejecutados

### Menú `footer`

Título:

- Antes: `AYUDA & SOPORTE`
- Después: `AYUDA Y SOPORTE`

Ítems:

| Antes | Después |
| --- | --- |
| `FAQ´S - Envíos y devoluciones` | `FAQ - Envíos y devoluciones` |
| `Crea tu propio papel pintado rollo` | `Crea tu propio papel pintado` |
| `Crea tu papel pintado mural personalizado` | `Crea tu mural personalizado` |
| `Cómo tomar medidas de paredes` | sin cambio |
| `Cómo tomar medidas del techo` | sin cambio |
| `Envíos internacionales` | retirado del footer |
| `Black Friday 2024` | retirado del footer |
| `Your Privacy Choices` | sin cambio |

### Menú `footer-profesional`

Título:

- Antes: `PROFESIONALES & SOCIAL`
- Después: `PROFESIONALES`

Ítems:

| Antes | Después |
| --- | --- |
| `B2B Tiendas interiorismo` | `B2B tiendas de interiorismo` |
| `B2B Estudios interiorismo y arquitectura, hoteles y espacios púbicos.` | `B2B estudios de interiorismo y arquitectura, hoteles y espacios públicos` |
| `B2B Hoteles & Contact` | `B2B hoteles y contract` |
| `Social & Prensa y Afiliación` | `Social, prensa y afiliación` |
| `Artistas & Diseñadores` | `Artistas y diseñadores` |
| `Solicita tu muestra` | sin cambio |

### Menú `footer-brand`

Título:

- `EMPRESA` sin cambio.

Ítems:

| Antes | Después |
| --- | --- |
| `Sobre Nosotros` | `Sobre nosotros` |
| `Nuestros Productos` | `Nuestros productos` |
| `Sostenibilidad` | sin cambio |
| `Inspiración` | sin cambio |
| `Tarjeta regalo` | retirado del footer |

### Menú `footer-legal`

Título:

- Antes: `Legal`
- Después: `LEGAL`

Ítems:

| Antes | Después |
| --- | --- |
| `Aviso Legal` | `Aviso legal` |
| `Política de Cookies` | `Política de cookies` |
| `Condiciones de uso de la web` | sin cambio |
| `Condiciones de venta online` | sin cambio |

## Verificación Shopify Admin

Lectura posterior confirmada:

- `footer` ya no contiene `Envíos internacionales` ni `Black Friday 2024`.
- `footer-brand` ya no contiene `Tarjeta regalo`.
- `footer-profesional` contiene `espacios públicos`, no `espacios púbicos`.
- `FAQ´S` ya no aparece como etiqueta fuente en `footer`.
- `footer-legal` queda normalizado.

## QA pública

Se revisó el footer renderizado en:

- ES: `https://www.matchwalls.com/`
- EN: `https://www.matchwalls.com/en`
- FR: `https://www.matchwalls.com/fr`
- DE: `https://www.matchwalls.com/de`
- NL: `https://www.matchwalls.com/nl`

### Resultado por idioma

ES:

- `Tarjeta regalo`: no aparece.
- `Black Friday 2024`: no aparece.
- `Envíos internacionales`: no aparece.
- `FAQ´S`: no aparece.
- `espacios púbicos`: no aparece.
- Nuevas etiquetas fuente visibles correctamente.

EN:

- `Tarjeta regalo`: no aparece.
- `Black Friday 2024`: no aparece.
- `Envíos internacionales`: no aparece.
- Sigue apareciendo traducción antigua: `FAQ´S - Shipping and Returns`.
- Menú profesional mantiene traducciones antiguas: `Professional & social`, `B2B Hotels & Contact`, etc.

FR:

- `Tarjeta regalo`: no aparece.
- `Black Friday 2024`: no aparece.
- `Envíos internacionales`: no aparece.
- No aparece `FAQ´S`.
- Persisten cabeceras fuente españolas: `PROFESIONALES`, `EMPRESA`, `AYUDA Y SOPORTE`.
- Persisten traducciones mejorables: `Social & Press and Affiliation`, etc.

DE:

- `Tarjeta regalo`: no aparece.
- `Black Friday 2024`: no aparece.
- `Envíos internacionales`: no aparece.
- No aparece `FAQ´S` exacto.
- Persisten traducciones antiguas/mejorables.

NL:

- `Tarjeta regalo`: no aparece.
- `Black Friday 2024`: no aparece.
- `Envíos internacionales`: no aparece.
- No aparece `FAQ´S` exacto, pero aparece `FAQ´s - Verzending en retouren`.
- Persisten cabeceras fuente españolas: `PROFESIONALES`, `EMPRESA`, `AYUDA Y SOPORTE`.
- Persiste traducción incorrecta grave: `schaamruimtes` para espacios públicos.

## Estado final

Elementos retirados del footer publicado:

- `Tarjeta regalo`: `CORREGIDO Y VERIFICADO`
- `Black Friday 2024`: `CORREGIDO Y VERIFICADO`
- `Envíos internacionales`: `CORREGIDO Y VERIFICADO`

Fuente ES de menús:

- `CORREGIDO Y VERIFICADO`

Traducciones de navegación EN/FR/DE/NL:

- `INCOMPLETO`

Motivo:

- Shopify conserva traducciones publicadas antiguas de menús/ítems.
- Algunas traducciones no se actualizan automáticamente al modificar la fuente ES.
- No se escribieron traducciones porque el lote aprobado no incluía valores EN/FR/DE/NL exactos ni `digest` para `translationsRegister`.

## Reversión

Usar `respaldo-MW-FOOTER-NAV-GLOBAL-002-2026-06-17.md` para restaurar:

- títulos originales;
- ítems originales;
- orden original;
- enlaces retirados.

## Siguiente lote recomendado

`MW-FOOTER-I18N-TRANSLATIONS-003`

Objetivo:

- Inventariar claves/digest de traducciones de menús.
- Corregir footer EN, FR, DE y NL con textos humanos aprobados.
- Eliminar `FAQ´S`/`FAQ´s` y traducciones automáticas defectuosas.
- Corregir cabeceras españolas visibles en FR/NL.
