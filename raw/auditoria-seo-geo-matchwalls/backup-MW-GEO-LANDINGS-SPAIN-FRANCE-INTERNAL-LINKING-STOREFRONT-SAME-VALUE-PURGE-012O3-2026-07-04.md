# Backup tecnico previo a `MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-SAME-VALUE-PURGE-012O3`

Fecha: 2026-07-04  
Tipo: respaldo de estado Admin antes de escritura tecnica same-value.

## Recursos

### Espana

- ID: `gid://shopify/Page/687276622200`
- Handle: `papel-pintado-espana`
- Title: `Papel pintado en España para hogares y proyectos profesionales`
- Publicada: `true`
- `updatedAt` previo a 012O3: `2026-07-04T13:29:58Z`
- Digest `body_html`: `1171b8996598abe8d2e3f5790fff27c2664bca44f34595a7517ad5d397dfe6e9`
- Traducciones `body_html` EN/FR/DE/NL: presentes, contienen bloque pais, `outdated:false`.

Bloque presente en ES:

```html
<h2>Papel pintado por país</h2><p>Estás consultando las soluciones para España. Si tu proyecto se desarrolla en Francia o quieres comparar opciones para otro mercado, consulta la guía de <a href="/pages/papel-pintado-francia">papel pintado en Francia</a>.</p>
```

### Francia

- ID: `gid://shopify/Page/687276654968`
- Handle: `papel-pintado-francia`
- Title: `Papel pintado en Francia para interiores y proyectos profesionales`
- Publicada: `true`
- `updatedAt` previo a 012O3: `2026-07-04T13:30:39Z`
- Digest `body_html`: `c610e2d374bd399794d96a4e9b43defb0d911a6e1db724e434ce5fbf43ca2b48`
- Traducciones `body_html` EN/FR/DE/NL: presentes, contienen bloque pais, `outdated:false`.

Bloque presente en ES:

```html
<h2>Papel pintado por país</h2><p>Estás consultando las soluciones para Francia. Si tu proyecto se desarrolla en España o quieres comparar opciones para otro mercado, consulta la guía de <a href="/pages/papel-pintado-espana">papel pintado en España</a>.</p>
```

## Valores completos

Los valores completos de `body` ES y traducciones `body_html` EN/FR/DE/NL fueron releidos via Shopify Admin GraphQL inmediatamente antes de la escritura y coinciden con el resultado registrado en `012O`.

Archivos base de respaldo relacionados:

- `backup-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-PAGE-BLOCK-012O-2026-07-04.md`
- `resultado-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-PAGE-BLOCK-012O-2026-07-04.md`
- `diagnostico-MW-GEO-LANDINGS-SPAIN-FRANCE-INTERNAL-LINKING-STOREFRONT-SYNC-DIAG-012O2-2026-07-04.md`

## Reversion prevista

Si la escritura same-value causa una regresion:

1. Reaplicar los cuerpos ES desde el estado previo registrado en `012O`.
2. Re-registrar traducciones `body_html` EN/FR/DE/NL con el digest vigente.
3. Verificar Admin y storefront publico en 10 URLs.
