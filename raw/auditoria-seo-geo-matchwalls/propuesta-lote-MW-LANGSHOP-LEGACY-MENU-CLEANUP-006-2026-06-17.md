# Propuesta lote MW-LANGSHOP-LEGACY-MENU-CLEANUP-006

Fecha: 2026-06-17
Estado: `REQUIERE DECISION HUMANA`

## 1. Nombre y alcance exacto

Lote: `MW-LANGSHOP-LEGACY-MENU-CLEANUP-006`.

Objetivo: retirar del inventario operativo de Shopify un menu legacy de footer que LangShop sigue detectando/exportando, aunque no forma parte del footer publico actual.

Accion propuesta: actualizar el menu `footer-matchwalls` para dejarlo sin items y marcarlo claramente como legacy/no usar.

No se propone:

- No borrar el menu.
- No modificar el tema MAIN.
- No modificar `footer-profesional`, `footer-brand`, `footer`, `footer-legal`.
- No modificar productos, paginas, colecciones, blogs, inventario, precios, redirecciones, handles, App Embeds ni configuracion LangShop.
- No importar ni exportar CSV desde LangShop.
- No ejecutar traducciones automaticas.

## 2. Recursos, IDs, URLs e idiomas afectados

Recurso directo:

- Menu: `gid://shopify/Menu/210969952483`.
- Handle: `footer-matchwalls`.
- Titulo actual: `Footer matchwalls`.
- Idioma fuente del menu: ES.

Items legacy que quedarian retirados del menu:

- `Tarjeta regalo` - `gid://shopify/MenuItem/493550371043` - `/products/tarjeta-regalo`.
- `B2B Interiorismo` - `gid://shopify/MenuItem/493550239971` - `/pages/horeca`.
- Resto de items del menu legacy `footer-matchwalls`.

Idiomas indirectos:

- EN, FR, DE y NL pueden quedar afectados solo en LangShop como recursos traducibles obsoletos que dejarian de venir del menu fuente.
- No se modificaran traducciones publicadas directamente en este lote.

## 3. Valores actuales verificados

Tema MAIN:

- `gid://shopify/OnlineStoreTheme/178383749496`.
- Nombre: `SEO schema hotfix - 2026-06-15`.
- `sections/footer-group.json` usa:
  - `footer-profesional`.
  - `footer-brand`.
  - `footer`.
  - `footer-legal`.
- `sections/footer-group.json` no usa `footer-matchwalls`.
- `sections/footer.liquid` no hardcodea `footer-matchwalls`.

Menu legacy:

- ID: `gid://shopify/Menu/210969952483`.
- Handle: `footer-matchwalls`.
- Titulo: `Footer matchwalls`.
- `isDefault`: `false`.
- Contiene `Tarjeta regalo`, `B2B Interiorismo` y otros elementos antiguos que LangShop muestra/exporta.

Estado:

- Footer publico actual: `CORREGIDO Y VERIFICADO` segun lote 005.
- Menu legacy `footer-matchwalls`: `VERIFICADO PERO MEJORABLE`.
- Residuo `Tarjeta regalo` en menu legacy: `INCORRECTO` como inventario operativo; no visible en footer publico.
- Configuracion interna LangShop: `NO ACCESIBLE`.

## 4. Valores propuestos

Actualizar el menu:

- Titulo nuevo: `ZZ LEGACY - NO USAR - footer-matchwalls`.
- Items nuevos: lista vacia `[]`.
- Handle: se mantiene `footer-matchwalls`.

Mutacion validada contra esquema, no ejecutada:

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

Variables propuestas:

```json
{
  "id": "gid://shopify/Menu/210969952483",
  "title": "ZZ LEGACY - NO USAR - footer-matchwalls",
  "items": []
}
```

## 5. Evidencia y motivo tecnico

Evidencia verificada:

- El footer MAIN no referencia `footer-matchwalls`.
- Los menus activos del footer son los cuatro menus separados creados/corregidos en lotes anteriores.
- Las exportaciones LangShop de navegacion siguen incluyendo recursos del menu legacy, incluyendo `Tarjeta regalo`.

Motivo:

- Reducir ruido y riesgo operativo en LangShop.
- Evitar que una importacion o revision futura tome como fuente un menu antiguo no publicado.
- Mantener el menu sin borrarlo para que exista un punto claro de reversion y trazabilidad.

## 6. Riesgos y efectos secundarios

- Si alguna app o integracion externa no visible usa `footer-matchwalls`, vera el menu vacio. Estado: `REQUIERE DECISION HUMANA`.
- LangShop podria conservar traducciones/cache de items antiguos hasta que se actualicen estadisticas o se reexporte. Estado LangShop interno: `NO ACCESIBLE`.
- La estructura se puede restaurar, pero si Shopify elimina definitivamente los MenuItem, los IDs exactos de items restaurados podrian cambiar. Estado: `VERIFICADO PERO MEJORABLE`.
- No deberia haber impacto publico en footer si la evidencia del tema MAIN es completa. Estado: `VERIFICADO Y CORRECTO`.

## 7. Respaldo disponible

Respaldo generado:

- `respaldo-MW-LANGSHOP-LEGACY-MENU-CLEANUP-006-2026-06-17.md`.

Incluye:

- Menu ID, handle, titulo e `isDefault`.
- Arbol completo actual.
- IDs de MenuItem.
- URLs.
- `resourceId`.
- Mutacion validada para limpieza.
- Metodo de reversion.

## 8. Metodo exacto de reversion

Si el lote produce un resultado no esperado:

1. Ejecutar `menuUpdate` sobre `gid://shopify/Menu/210969952483`.
2. Restaurar titulo `Footer matchwalls`.
3. Restaurar items originales desde el respaldo.
4. Verificar por lectura GraphQL que el arbol vuelve a existir.
5. Verificar que el footer publico sigue usando `footer-profesional`, `footer-brand`, `footer`, `footer-legal`.

Limitacion:

- Si los items fueron eliminados por Shopify, sus IDs podrian no ser reutilizables. En ese caso se restauraria estructura y enlaces, pero no necesariamente los mismos MenuItem IDs.

## 9. Pruebas posteriores

Despues de ejecutar, si se aprueba:

1. Consultar `gid://shopify/Menu/210969952483` y verificar:
   - Titulo `ZZ LEGACY - NO USAR - footer-matchwalls`.
   - `items` vacio.
   - `0 userErrors`.
2. Consultar `sections/footer-group.json` del tema MAIN y verificar que sigue usando:
   - `footer-profesional`.
   - `footer-brand`.
   - `footer`.
   - `footer-legal`.
3. Verificar que los menus activos no se modificaron.
4. Verificar footer publico ES, EN, FR, DE y NL cuando el entorno permita acceso.
5. Registrar resultado en `registro-cambios-ejecutados.md`.

## 10. Decision requerida

Para ejecutar este lote despues de esta propuesta, Daniel debe responder exactamente:

`APROBADO LOTE MW-LANGSHOP-LEGACY-MENU-CLEANUP-006`

Hasta recibir esa aprobacion posterior a la propuesta, no se ejecutara ninguna mutacion.
