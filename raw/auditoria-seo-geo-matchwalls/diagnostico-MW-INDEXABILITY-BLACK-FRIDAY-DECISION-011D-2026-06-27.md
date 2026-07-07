# 2026-06-27 - Diagnóstico y decisión Black Friday

Lote de lectura: `MW-INDEXABILITY-BLACK-FRIDAY-DECISION-011D`

Estado global: `REQUIERE DECISION HUMANA`

No se ha modificado Shopify.

## Documentos y artefactos revisados

- `AGENTS.md`
- `registro-cambios-ejecutados.md`
- `diagnostico-MW-INDEXABILITY-REMAINING-CLASSIFICATION-DIAG-011C-2026-06-27.md`
- `flag-black_friday-MW-INDEXABILITY-REMAINING-CLASSIFICATION-DIAG-011C-2026-06-27.csv`
- sitemaps públicos localizados
- colección Shopify Admin `gid://shopify/Collection/646234440056`
- plantilla local `templates/collection.black-friday.json`, contrastada con HTML público

## Estado real comprobado

`INCORRECTO`

La landing Black Friday está publicada, indexable y en sitemap cuando el contenido visible sigue siendo de Black Friday 2024.

Fecha actual del diagnóstico: 27 de junio de 2026.

## Recurso Shopify real

`VERIFICADO PERO MEJORABLE`

- Recurso: `Collection`
- ID: `gid://shopify/Collection/646234440056`
- Legacy ID: `646234440056`
- Título base: `Papel Pintado Black Friday`
- Handle base: `papel-pintado-black-friday`
- Template suffix: `black-friday`
- UpdatedAt: `2026-04-20T15:23:00Z`
- ProductsCount Admin: `0`
- Publicaciones: `9`
- `seo.hidden`: `null`

Nota: aunque Admin indica `productsCount=0`, el HTML público contiene marcadores/enlaces de producto por plantilla. No se declara página vacía sin QA visual adicional.

## URLs públicas detectadas

`INCORRECTO`

El inventario 011C detectó 5 URLs por patrón `black-friday`; el diagnóstico 011D amplía a 7 porque DE y PT usan handles traducidos.

| Idioma | URL | Estado público | Sitemap | Indexable |
|---|---|---:|---:|---:|
| ES | `https://www.matchwalls.com/collections/papel-pintado-black-friday` | 200 | sí | sí |
| EN | `https://www.matchwalls.com/en/collections/wallpapers-black-friday` | 200 | sí | sí |
| FR | `https://www.matchwalls.com/fr/collections/papiers-peints-black-friday` | 200 | sí | sí |
| NL | `https://www.matchwalls.com/nl/collections/black-friday-wallpaper` | 200 | sí | sí |
| IT | `https://www.matchwalls.com/it/collections/sfondi-del-black-friday` | 200 | sí | sí |
| DE | `https://www.matchwalls.com/de/collections/schwarzer-freitag-wallpaper` | 200 | sí | sí |
| PT | `https://www.matchwalls.com/pt/collections/papel-de-parede-de-sexta-feira-negra` | 200 | sí | sí |

## Señales obsoletas verificadas en público

`INCORRECTO`

En los 7 idiomas:

- `Black Friday 2024` aparece en HTML público.
- El contador apunta a `Nov 29, 2024`.
- Aparece el mensaje `La oferta ha finalizado`.
- La página no tiene `noindex`.
- El canonical es self.

En EN:

- Meta title: `Wallpaper Black Friday  2025 - Wallpaper Sale`.
- H1 visible: `Black Friday 2024`.

En FR:

- Traducción `body_html`: `Acheter du papier peint Toulouse - MatchWalls`.
- Estado: `INCORRECTO`, porque mezcla una intención geográfica no relacionada con Black Friday.

## Redirecciones

`VERIFICADO PERO MEJORABLE`

- Búsqueda Admin `black-friday`: 0 redirecciones.
- Búsqueda Admin `black`: 2 redirecciones no relacionadas con estas URLs.
- No existe cobertura 301 para retirar estas URLs.

## Opciones evaluadas

### Opción A - Mantener indexable

Estado: `INCORRECTO`

No recomendada. La página comunica ofertas 2024 en 2026 y contiene señales contradictorias.

### Opción B - Redirigir a ofertas actuales

Estado: `REQUIERE DECISION HUMANA`

No recomendada todavía porque no se ha aprobado un destino comercial permanente y porque Black Friday puede reutilizarse como landing estacional futura.

### Opción C - Borrar/despublicar colección

Estado: `REQUIERE DECISION HUMANA`

No recomendada. Es más invasiva, puede afectar enlaces internos/externos y no es necesaria para retirar indexabilidad.

### Opción D - Noindex reversible ahora

Estado: `VERIFICADO PERO MEJORABLE`

Recomendada.

Consiste en aplicar `seo.hidden=1` a la colección base `gid://shopify/Collection/646234440056`.

Ventajas:

- retira la landing de indexación/sitemap;
- conserva URLs para campañas futuras;
- no cambia handles;
- no toca redirecciones;
- no toca plantilla ni contenido;
- reversible eliminando el metafield `seo.hidden`.

## Recomendación

`REQUIERE DECISION HUMANA`

Ejecutar un lote separado:

`MW-INDEXABILITY-BLACK-FRIDAY-NOINDEX-011D1`

Alcance exacto:

- crear metafield en la colección:
  - ownerId: `gid://shopify/Collection/646234440056`
  - namespace: `seo`
  - key: `hidden`
  - type: `number_integer`
  - value: `1`

No tocar:

- handles;
- redirecciones;
- traducciones;
- plantilla;
- productos;
- navegación;
- contenido visible.

## Mutaciones validadas pero no ejecutadas

Noindex:

```json
{
  "metafields": [
    {
      "ownerId": "gid://shopify/Collection/646234440056",
      "namespace": "seo",
      "key": "hidden",
      "type": "number_integer",
      "value": "1"
    }
  ]
}
```

Rollback:

```json
{
  "metafields": [
    {
      "ownerId": "gid://shopify/Collection/646234440056",
      "namespace": "seo",
      "key": "hidden"
    }
  ]
}
```

## QA posterior requerido si se aprueba 011D1

1. Admin:
   - verificar `seo.hidden = 1`.
2. Público:
   - comprobar 7 URLs;
   - verificar `noindex`/robots equivalente.
3. Sitemap:
   - comprobar que las 7 URLs desaparecen.
4. Control:
   - no tocar redirecciones;
   - no tocar handles;
   - verificar que colección sigue accesible si se visita directamente.

