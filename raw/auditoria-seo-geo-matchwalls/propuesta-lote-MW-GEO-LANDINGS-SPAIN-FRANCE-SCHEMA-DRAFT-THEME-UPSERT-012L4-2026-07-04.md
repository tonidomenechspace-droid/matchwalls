# Propuesta de lote - MW-GEO-LANDINGS-SPAIN-FRANCE-SCHEMA-DRAFT-THEME-UPSERT-012L4

Fecha propuesta: 2026-07-04  
Tipo: escritura acotada en tema no publicado.  
Estado: `REQUIERE DECISION HUMANA`

## 1. Objetivo

Aplicar el prototipo schema validado en 012L2 a un tema no publicado para poder hacer QA real de preview antes de decidir cualquier publicacion.

## 2. Aprobacion necesaria

No ejecutar hasta que Daniel apruebe exactamente:

`APROBADO LOTE MW-GEO-LANDINGS-SPAIN-FRANCE-SCHEMA-DRAFT-THEME-UPSERT-012L4`

## 3. Tema destino propuesto

- ID: `gid://shopify/OnlineStoreTheme/178396463480`.
- Nombre: `MW-THEME-PAGE-H1-SEMANTIC-008E - ISOLATED QA - ...`.
- Rol actual verificado en 012L3: `UNPUBLISHED`.
- Prefix: `/t/45`.
- `processing`: `false`.
- `processingFailed`: `false`.

Condicion de seguridad:

- Antes de escribir, se debe releer el tema.
- Si el rol no es `UNPUBLISHED`, abortar.
- Si `processing` o `processingFailed` no son seguros, abortar.

## 4. Recursos afectados

Solo en el tema `178396463480`:

1. `snippets/geo-landing-schema.liquid`
   - Estado actual: no existe en lectura 012L3.
   - Estado propuesto: crear con contenido validado en 012L2.
   - MD5 local propuesto: `9033b2bfa89dc435b9811b3d897e07c1`.
   - Tamano: `11723` bytes.

2. `snippets/microdata-schema.liquid`
   - Estado actual checksum: `58417e4825aa3d4570a6646f292aaedc`.
   - Estado propuesto checksum local: `a3d8e23b4979219149a9c5b5f76723ec`.
   - Cambio: insertar una sola llamada render.

Linea propuesta:

```liquid
{%- render 'geo-landing-schema' -%}
```

Ubicacion:

- Despues del bloque `BreadcrumbList`.
- Antes de `{%- if request.page_type == 'index' -%}`.

## 5. Lo que NO incluye

- No publicar tema.
- No tocar MAIN `178399019384`.
- No tocar `178383749496` ni otros temas de reversion.
- No tocar LangShop.
- No tocar paginas, handles, URLs, canonicals, hreflang ni metas.
- No cambiar `config/settings_data.json`.
- No activar schema para IT/PT.

## 6. Pruebas posteriores obligatorias

Sobre preview del tema `178396463480`:

- 10 URLs landings pais:
  - Espana ES/EN/FR/DE/NL.
  - Francia ES/EN/FR/DE/NL.
- Comprobar:
  - HTTP 200.
  - canonical sin regresion.
  - hreflang sin regresion.
  - `noindex` ausente.
  - `BreadcrumbList` sigue presente.
  - Nuevo `WebPage` presente.
  - Nuevo `FAQPage` presente.
  - 3 FAQs por URL.
  - JSON-LD parsea sin errores.
  - IT/PT no reciben el nuevo schema.

## 7. Reversion

Reversion minima:

1. Retirar la linea:

```liquid
{%- render 'geo-landing-schema' -%}
```

2. Verificar que el tema vuelve a emitir solo el schema previo en landings.

Si Shopify permite borrar archivos:

- Eliminar `snippets/geo-landing-schema.liquid`.

Si Shopify bloquea borrado:

- Dejar el snippet inerte. Sin render, no afecta a la web.

## 8. Riesgos

| Riesgo | Estado | Mitigacion |
| --- | --- | --- |
| Escribir en MAIN | `RIESGO CRITICO` | Releer rol antes de escribir; la herramienta bloquea writes al MAIN, pero no se debe depender solo de eso. |
| Publicar por error | `RIESGO CRITICO` | El lote no incluye publicacion. |
| Tema candidato desfasado frente a MAIN | `VERIFICADO PERO MEJORABLE` | Uso exclusivo para QA schema, no publicacion. |
| Divergencia FAQ visible/schema | `VERIFICADO PERO MEJORABLE` | QA sobre 10 URLs despues de escritura. |
| Dejar archivo extra si no se puede borrar | `VERIFICADO PERO MEJORABLE` | Retirar render basta para desactivar. |

## 9. Decision recomendada

Ejecutar 012L4 solo si Daniel acepta que:

- Es una prueba en tema no publicado.
- No equivale a publicacion.
- No convierte el tema `178396463480` en publicable.
- La decision de publicar, si llega, requerira otro lote posterior con QA completa.

