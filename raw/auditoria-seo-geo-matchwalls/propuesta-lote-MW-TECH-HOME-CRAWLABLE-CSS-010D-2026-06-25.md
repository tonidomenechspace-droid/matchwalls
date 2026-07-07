# Propuesta formal MW-TECH-HOME-CRAWLABLE-CSS-010D

Fecha: 2026-06-25  
Estado: `REQUIERE DECISION HUMANA`  
Ejecucion propuesta: no autorizada todavia  

## Aprobacion requerida

Para ejecutar, Daniel debe responder exactamente:

`APROBADO LOTE MW-TECH-HOME-CRAWLABLE-CSS-010D`

## Alcance exacto propuesto

Tema objetivo:

- `178399019384`
- Nombre: `MW-TECH-JS-ADD-EVENT-LISTENER-010A-QA-2026-06-18`
- Rol: `UNPUBLISHED`
- Preview: `/t/46`

Archivo objetivo:

- `sections/collection-logo-list.liquid`

Exclusiones:

- No modificar MAIN `178396463480`.
- No publicar tema.
- No modificar `templates/index.json`.
- No modificar textos, enlaces, handles, productos, precios, inventario, schema, redirecciones ni apps externas.

## Valores actuales

- MD5 actual del archivo en QA: `44d02156951a46f0147f3ee3de61f38e`.
- La home renderiza 8 enlaces `.logo-link`.
- Cada enlace contiene un `<style>` interno con reglas `.logo-link` y `.logo-list__image`.
- Resultado actual en preview auxiliar:
  - `<style>` problematicos dentro de `.logo-link`: 8.
  - CSS detectado en `body.textContent`: si.
  - CSS detectado en HTML bruto: si.
  - CSS visible en `body.innerText`: no.

## Cambio propuesto

Refactorizar solo `sections/collection-logo-list.liquid` en el tema auxiliar:

1. Retirar el bloque `<style>` que se imprime dentro de cada iteracion del bucle de logos.
2. Conservar las mismas reglas visuales una unica vez fuera del HTML repetido por bloque, preferiblemente mediante CSS de componente no rastreable como contenido editorial.
3. Mantener sin cambios:
   - clases existentes;
   - enlaces;
   - titulos de categoria;
   - imagenes;
   - `data-logo-title`;
   - script de `dataLayer`;
   - schema de la seccion;
   - orden visual.

## Criterio de salida

El lote solo se considerara `CORREGIDO Y VERIFICADO` si se cumple todo:

- MAIN no modificado.
- Tema de reversion no modificado.
- QA auxiliar guarda un nuevo checksum documentado.
- Home preview auxiliar:
  - 8 enlaces `.logo-link` conservados.
  - 0 bloques `<style>` dentro de `.logo-link`.
  - CSS `.logo-link/.logo-list__image` ausente del contenido textual rastreable de la home.
  - links de categorias sin cambios.
  - imagenes circulares, tamanos desktop/mobile y hover conservados.
- QA ES/EN/FR/DE/NL en desktop y mobile sin regresiones criticas.
- Si se detecta cambio visual no esperado, revertir.

## Pruebas posteriores

Pruebas minimas:

- Home ES/EN/FR/DE/NL en desktop.
- Home ES/EN/FR/DE/NL en mobile.
- Validacion de:
  - `badStyleNodeCount == 0` dentro de `.logo-link`;
  - `body.textContent` sin reglas `.logo-link/.logo-list__image` procedentes del bloque repetido;
  - 8 enlaces de categoria conservados;
  - canonical, hreflang prioritarios, `html lang`, noindex y errores criticos de consola.

Prueba ampliada recomendada si el cambio pasa los centinelas:

- Matriz estandar 170 pruebas para mantener coherencia con los sublotes tecnicos anteriores.

## Riesgos

- Riesgo visual: cambio accidental en logos de categoria, grid movil o hover.
- Riesgo de cascada CSS: las clases `.logo-link` y `.logo-list__image` pueden existir en otras secciones.
- Riesgo tecnico: si Shopify no acepta la forma CSS de componente elegida, se debe revertir y plantear alternativa en `assets/theme.css`.

## Reversion

Metodo exacto:

- Restaurar `sections/collection-logo-list.liquid` en el tema auxiliar al contenido original con MD5 `44d02156951a46f0147f3ee3de61f38e`.

Alternativa extrema:

- Descartar el tema auxiliar `178399019384` si se considera contaminado.

## Estado final de esta propuesta

`REQUIERE DECISION HUMANA`

No se ha modificado Shopify.
