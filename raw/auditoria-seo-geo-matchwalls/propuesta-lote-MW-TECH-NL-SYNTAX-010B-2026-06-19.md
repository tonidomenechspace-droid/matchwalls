# Propuesta — MW-TECH-NL-SYNTAX-010B

Estado: `INCOMPLETO` — pendiente de aprobación.

## Alcance exacto

- Tema auxiliar `178399019384`, `UNPUBLISHED`, `/t/46`.
- Único archivo: `snippets/ultimate-datalayer.liquid`.
- Idiomas y URLs afectadas: ES, EN, FR, DE y NL en la página localizada
  «Nuestros productos».
- Se excluyen el tema MAIN `178396463480`, la reversión `178383749496`, la
  publicación del tema y cualquier plataforma externa.

## Estado real y valor actual

- Shopify confirma en auxiliar, MAIN y reversión el mismo archivo:
  MD5 `449db7505f61b2f81c835cc32669c37c`; 57168 bytes.
- El error se reproduce en las cinco URLs afectadas, no solo en NL:
  `SyntaxError: Unexpected token ','`.
- El JavaScript renderizado contiene:
  `variant_id: ,`.
- La causa está localizada en tres condiciones Liquid demasiado amplias:

```liquid
{% if template contains 'product' %}
```

dos veces, y:

```liquid
{% unless template contains 'product' %}
```

una vez.

La plantilla `page.nuestros-productos` contiene la cadena `product`; por eso
ejecuta lógica reservada a fichas de producto aunque el objeto `product` no
existe en una página normal.

## Cambio propuesto

Sustituir exactamente las dos condiciones `if` por:

```liquid
{% if request.page_type == 'product' %}
```

y la única condición `unless` por:

```liquid
{% unless request.page_type == 'product' %}
```

Shopify documenta que `request.page_type` devuelve el tipo exacto de la página
y que `product` es uno de sus valores admitidos. El candidato elimina las tres
coincidencias parciales y conserva dos `if` y un `unless` estrictos.

## Valores propuestos y respaldo

- MD5 candidato calculado: `792a7f2c37022db342e1d7a82a8d3679`.
- Tamaño candidato: 57177 bytes.
- Respaldo exacto: contenido Shopify actual y MD5
  `449db7505f61b2f81c835cc32669c37c`.
- MAIN y reversión contienen además una copia idéntica del archivo original.

## Riesgos y efectos secundarios

- Riesgo principal: alterar `view_item`, datos de variante o el seguimiento del
  botón de compra directa en fichas de producto.
- Riesgo secundario: que aparezca un error posterior actualmente oculto por el
  primer `SyntaxError`.
- El validador Liquid empaquetado no está operativo en este entorno por una
  dependencia ausente: `NO ACCESIBLE`. La sintaxis propuesta está respaldada
  por la referencia oficial, pero no se declarará correcta hasta verificar el
  render real del tema auxiliar.

## Reversión exacta

1. Restaurar las tres condiciones originales.
2. Confirmar MD5 `449db7505f61b2f81c835cc32669c37c` y 57168 bytes.
3. Repetir las pruebas críticas.
4. Si la reversión no coincide exactamente, detener el lote y descartar el
   tema auxiliar; MAIN permanece intacto.

## QA posterior obligatoria

- Las cinco páginas «Nuestros productos» × escritorio/móvil: 10 pruebas.
- Una ficha de producto representativa en ES/EN/FR/DE/NL ×
  escritorio/móvil: 10 pruebas.
- En páginas normales: ausencia de `SyntaxError` y de `variant_id: ,`.
- En productos: JavaScript válido, `variant_id` informado, evento `view_item`,
  variante, precio y compra sin regresiones.
- Comprobar home, colección y carrito por la rama de compra directa.
- Repetir después la matriz global de 170 pruebas.
- Detener y revertir ante cualquier diferencia comercial, de carrito o de
  medición.

## Aprobación requerida

`APROBADO LOTE MW-TECH-NL-SYNTAX-010B`

Esta aprobación no autoriza publicar, modificar MAIN ni realizar otros cambios.

## Ejecución y cierre — 2026-06-20

- Aprobación exacta recibida.
- Cambio aplicado únicamente en `178399019384`, que continúa `UNPUBLISHED`.
- MD5 final `792a7f2c37022db342e1d7a82a8d3679`; 57177 bytes.
- MAIN y reversión conservan MD5 `449db7505f61b2f81c835cc32669c37c`.
- QA específica: 20/20.
- Regresión: 170/170.
- Estado final: `CORREGIDO Y VERIFICADO`.
- Evidencia: `qa-MW-TECH-NL-SYNTAX-010B-2026-06-20.md`.
