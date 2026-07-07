# QA MW-TECH-HOME-CRAWLABLE-CSS-010D

Fecha: 2026-06-25  
Estado final: `CORREGIDO Y VERIFICADO` en tema auxiliar  
Publicacion: no publicada  

## Aprobacion

Aprobacion exacta recibida:

`APROBADO LOTE MW-TECH-HOME-CRAWLABLE-CSS-010D`

## Alcance ejecutado

- Tema objetivo: `178399019384`
- Nombre: `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18`
- Rol: `UNPUBLISHED`
- Archivo modificado: `sections/collection-logo-list.liquid`
- MAIN `178396463480`: no modificado.
- Tema de reversion `178383749496`: no modificado.
- No se publicaron temas.
- No se modificaron URLs, handles, textos, productos, precios, inventario, schema, redirecciones ni apps externas.

## Valores anteriores y nuevos

| Recurso | Antes | Despues | Estado |
| --- | --- | --- | --- |
| QA `sections/collection-logo-list.liquid` | MD5 `44d02156951a46f0147f3ee3de61f38e`, size `6780` | MD5 `e246746230f64c88b529db9aa370f3e2`, size `5937` | `CORREGIDO Y VERIFICADO` |
| MAIN `sections/collection-logo-list.liquid` | MD5 `44d02156951a46f0147f3ee3de61f38e` | MD5 `44d02156951a46f0147f3ee3de61f38e` | `VERIFICADO Y CORRECTO` como no modificado |
| Reversion `sections/collection-logo-list.liquid` | MD5 `44d02156951a46f0147f3ee3de61f38e` | MD5 `44d02156951a46f0147f3ee3de61f38e` | `VERIFICADO Y CORRECTO` como no modificado |

## Cambio final

- Se retiro el `<style>` que se repetia dentro de cada enlace `.logo-link`.
- Se mantuvo el CSS estructural en `{% stylesheet %}`.
- Para evitar una regresion de cascada frente a `theme.css`, las medidas y forma critica de la imagen se fijaron con `style` en el `image_tag`:
  - `border-radius: 50%`
  - `object-fit: cover`
  - `width/height: clamp(70px, 18vw, 120px)`
  - `transition: transform 0.3s ease-in-out`
- Se conservaron clases, enlaces, titulos, imagenes, `data-logo-title`, script de `dataLayer` y schema de seccion.

## Incidencia durante la ejecucion

`VERIFICADO PERO MEJORABLE` como iteracion intermedia descartada.

- Primer guardado QA: MD5 `07e2ef27cb963166fa189ac4b8ae0f6b`, size `6038`, `0 userErrors`.
- Aunque eliminaba el CSS rastreable, en preview desktop la primera imagen quedaba a `190.583px` por cascada: el CSS compilado quedaba antes de `theme.css`.
- No se acepto ese candidato como final.
- Se corrigio dentro del mismo lote con el MD5 final `e246746230f64c88b529db9aa370f3e2`.

## Validaciones previas

- Consulta de documentacion Shopify sobre `{% stylesheet %}`: `VERIFICADO Y CORRECTO`.
- Consulta de documentacion Shopify sobre atributos de `image_tag`: `VERIFICADO Y CORRECTO`.
- Validacion GraphQL de `themeFilesUpsert`: `VERIFICADO Y CORRECTO`.
- Validador local Shopify Liquid: `NO ACCESIBLE` porque el bundle local no tenia la dependencia `@shopify/theme-check-common`. No se uso para declarar validez.
- Shopify acepto la escritura final con `0 userErrors`.

## QA renderizado

Preview verificado con assets del tema `/t/46`.

Cobertura home prioritaria:

| Idioma | Desktop | Mobile | Resultado |
| --- | --- | --- | --- |
| ES | OK | OK | `CORREGIDO Y VERIFICADO` |
| EN | OK tras retest con `/en/` | OK | `CORREGIDO Y VERIFICADO` |
| FR | OK tras retest con `/fr/` | OK | `CORREGIDO Y VERIFICADO` |
| DE | OK | OK | `CORREGIDO Y VERIFICADO` |
| NL | OK | OK | `CORREGIDO Y VERIFICADO` |

Comprobaciones cumplidas en las 10 vistas finales:

- 8 enlaces `.logo-link` conservados.
- 8 imagenes `.logo-list__image` conservadas.
- `styleInsideLogoLinkCount = 0`.
- `badBodyStyleCount = 0`.
- `body.textContent` no contiene reglas `.logo-link {` ni `.logo-list__image {`.
- `body.innerText` no contiene reglas `.logo-link {` ni `.logo-list__image {`.
- Desktop: primera imagen `120px x 120px`, circular, `object-fit: cover`.
- Mobile 390px: primera imagen aproximadamente `70.2px x 70.2px`, circular, `object-fit: cover`.
- Desktop: `reveal-items-collection` en `flex`, gap `24px`.
- Mobile: `reveal-items-collection` en `grid`, cuatro columnas, sin overflow horizontal.
- `noindex = false`.
- `hreflangCount = 8` en las vistas validas.
- `html lang` correcto en ES/EN/FR/DE/NL.
- Assets del tema preview: `46`.

Observacion de navegacion:

- Dos intentos iniciales desktop de EN/FR sin barra final devolvieron pantalla transitoria `Algo salio mal`; los retests con `/en/` y `/fr/` fueron correctos. No se atribuye al lote porque las vistas finales cargan correctamente y mobile EN/FR tambien fue correcto.

## Reversion

Metodo exacto de reversion:

- Restaurar `sections/collection-logo-list.liquid` en el tema auxiliar `178399019384` al contenido original con MD5 `44d02156951a46f0147f3ee3de61f38e`.

Fuente de reversion disponible:

- MAIN `178396463480` conserva MD5 `44d02156951a46f0147f3ee3de61f38e`.
- Tema `178383749496` conserva MD5 `44d02156951a46f0147f3ee3de61f38e`.

## Estado final

`CORREGIDO Y VERIFICADO` en tema auxiliar.

La produccion MAIN sigue sin este cambio hasta un lote de publicacion posterior.
