# Ejecucion lote MW-LANGSHOP-LEGACY-MENU-CLEANUP-006

Fecha: 2026-06-17  
Hora de cierre: 15:22 +02:00  
Lote aprobado por Daniel: `APROBADO LOTE MW-LANGSHOP-LEGACY-MENU-CLEANUP-006`  
Estado final del alcance aprobado: `CORREGIDO Y VERIFICADO` para el menu legacy `footer-matchwalls` en Shopify Admin.  
Estado global tras QA publico: `INCOMPLETO`, porque el HTML publico externo sigue mostrando residuos antiguos que no quedan explicados por el menu legacy limpiado.

## 1. Alcance ejecutado

Se ejecuto exclusivamente la limpieza del menu legacy:

- Menu: `gid://shopify/Menu/210969952483`.
- Handle: `footer-matchwalls`.
- Titulo anterior: `Footer matchwalls`.
- Titulo nuevo: `ZZ LEGACY - NO USAR - footer-matchwalls`.
- Items anteriores: arbol legacy completo respaldado en `respaldo-MW-LANGSHOP-LEGACY-MENU-CLEANUP-006-2026-06-17.md`.
- Items nuevos: lista vacia `[]`.

No se modificaron:

- Tema MAIN.
- Archivos Liquid o JSON del tema.
- Menus activos `footer`, `footer-profesional`, `footer-brand`, `footer-legal`.
- LangShop.
- Traducciones.
- Productos, paginas, colecciones, blogs, inventario, precios, handles, canonicals, redirecciones ni App Embeds.

## 2. Respaldo previo

Archivo de respaldo:

- `auditoria-seo-geo-matchwalls/respaldo-MW-LANGSHOP-LEGACY-MENU-CLEANUP-006-2026-06-17.md`.

El respaldo contiene:

- ID, handle, titulo e `isDefault`.
- Arbol anterior completo del menu legacy.
- IDs de MenuItem.
- URLs y `resourceId`.
- Metodo de reversion.

Estado del respaldo: `VERIFICADO Y CORRECTO`.

## 3. Mutacion ejecutada

Mutacion Shopify Admin GraphQL:

```graphql
mutation CleanupLegacyFooterMenu($id: ID!, $title: String!, $items: [MenuItemUpdateInput!]!) {
  menuUpdate(id: $id, title: $title, items: $items) {
    menu {
      id
      handle
      title
      items(limit: 80) {
        id
        title
        type
        url
        resourceId
        items {
          id
          title
          type
          url
          resourceId
        }
      }
    }
    userErrors {
      field
      message
    }
  }
}
```

Variables ejecutadas:

```json
{
  "id": "gid://shopify/Menu/210969952483",
  "title": "ZZ LEGACY - NO USAR - footer-matchwalls",
  "items": []
}
```

Resultado Shopify:

- `userErrors`: `[]`.
- Menu devuelto:
  - ID: `gid://shopify/Menu/210969952483`.
  - Handle: `footer-matchwalls`.
  - Titulo: `ZZ LEGACY - NO USAR - footer-matchwalls`.
  - Items: `[]`.

Nota: `0 userErrors` confirma que Shopify acepto la operacion. No demuestra por si solo que el resultado publico, editorial, SEO o visual sea correcto.

## 4. Verificacion Shopify Admin posterior

### Menu legacy

Lectura posterior del menu:

- ID: `gid://shopify/Menu/210969952483`.
- Handle: `footer-matchwalls`.
- Titulo: `ZZ LEGACY - NO USAR - footer-matchwalls`.
- `isDefault`: `false`.
- Items: lista vacia.

Estado: `CORREGIDO Y VERIFICADO`.

### Menus activos de footer

Se verifico que los menus activos no fueron modificados:

- `gid://shopify/Menu/210266325219`, handle `footer`, titulo `AYUDA Y SOPORTE`.
- `gid://shopify/Menu/210972311779`, handle `footer-profesional`, titulo `PROFESIONALES`.
- `gid://shopify/Menu/210972344547`, handle `footer-brand`, titulo `EMPRESA`.
- `gid://shopify/Menu/210972410083`, handle `footer-legal`, titulo `LEGAL`.

Estado: `VERIFICADO Y CORRECTO`.

### Tema MAIN

Tema MAIN verificado:

- ID: `gid://shopify/OnlineStoreTheme/178383749496`.
- Nombre: `SEO schema hotfix - 2026-06-15`.

`sections/footer-group.json` sigue usando:

- `footer-profesional`.
- `footer-brand`.
- `footer`.
- `footer-legal`.

No usa `footer-matchwalls`.

Estado: `VERIFICADO Y CORRECTO`.

## 5. Verificacion publica posterior

### Verificacion renderizada desde Codex

La comprobacion renderizada con navegador integrado no fue util: la pagina cargada devolvio pantalla de error de Shopify con titulo `Algo salio mal`.

Estado: `NO ACCESIBLE`.

### Verificacion HTML publica externa

La lectura externa del HTML publico detecto residuos antiguos en el footer HTML, especialmente en EN:

- `Gift Card`.
- `International shipments`.
- `Black Friday 2024`.

Tambien se detectaron residuos equivalentes en HTML publico ES:

- `Envios internacionales` / `Envíos internacionales`.
- `Black Friday 2024`.

Interpretacion:

- Esto contradice la lectura de Shopify Admin de los menus activos y del tema MAIN.
- Ya no puede atribuirse al menu legacy `footer-matchwalls`, porque ese menu quedo vacio y renombrado.
- Puede proceder de cache, traducciones publicadas residuales, HTML servido a fetch externo, otra capa del tema, app, CDN o configuracion no accesible todavia.
- No se debe afirmar que el footer publico esta totalmente resuelto hasta reconciliar esta diferencia.

Estado del HTML publico externo: `INCORRECTO`.

## 6. Recursos no accesibles o no resueltos

- Configuracion interna de LangShop: `NO ACCESIBLE`.
- Cola/cache interna de LangShop: `NO ACCESIBLE`.
- Render publico completo desde navegador integrado Codex: `NO ACCESIBLE`.
- Origen exacto del residuo en HTML publico externo: `REQUIERE DECISION HUMANA`.

## 7. Incidencias

Incidencia nueva:

- Tras limpiar `footer-matchwalls`, el HTML publico externo sigue mostrando enlaces antiguos.
- Esto queda fuera del alcance ejecutado en el lote 006.
- Requiere un lote nuevo, acotado y de investigacion/lectura antes de cualquier nueva escritura.

Estado: `INCORRECTO`.

## 8. Metodo de reversion

Si se decide revertir la limpieza del menu legacy:

1. Ejecutar `menuUpdate` sobre `gid://shopify/Menu/210969952483`.
2. Restaurar titulo `Footer matchwalls`.
3. Restaurar el arbol original desde `respaldo-MW-LANGSHOP-LEGACY-MENU-CLEANUP-006-2026-06-17.md`.
4. Verificar por lectura GraphQL que el arbol vuelve a existir.
5. Verificar que el tema MAIN sigue usando los menus activos correctos.

Limitacion:

- Si Shopify recrea los MenuItem, los IDs exactos podrian cambiar. La estructura, titulos, enlaces y recursos son reversibles; la identidad exacta de los MenuItem no esta garantizada.

Estado de reversion: `VERIFICADO PERO MEJORABLE`.

## 9. Estado final

- Limpieza del menu legacy `footer-matchwalls`: `CORREGIDO Y VERIFICADO`.
- Menus activos de footer en Shopify Admin: `VERIFICADO Y CORRECTO`.
- Configuracion del tema MAIN para footer: `VERIFICADO Y CORRECTO`.
- HTML publico externo: `INCORRECTO`.
- Render publico desde Codex: `NO ACCESIBLE`.
- Configuracion interna LangShop: `NO ACCESIBLE`.

Siguiente lote recomendado, no ejecutado:

- `MW-LANGSHOP-PUBLIC-FOOTER-RESIDUE-007`.

Objetivo del siguiente lote:

- Localizar el origen real de los residuos `Gift Card`, `International shipments`, `Black Friday 2024` y equivalentes en ES/EN/FR/DE/NL.
- Contrastar tema, traducciones publicadas, LangShop, cache/CDN y HTML servido.
- No ejecutar nuevas escrituras sin propuesta y aprobacion exacta.
