# Respaldo previo - MW-LANGSHOP-LEGACY-MENU-CLEANUP-006

Fecha: 2026-06-17
Estado: respaldo previo, sin ejecucion de cambios

## Fuente verificada

Lectura directa Shopify Admin GraphQL, solo lectura.

## Recurso afectado si el lote se ejecuta

- Tipo: Menu Shopify / Online Store Navigation.
- ID: `gid://shopify/Menu/210969952483`.
- Handle: `footer-matchwalls`.
- Titulo actual: `Footer matchwalls`.
- `isDefault`: `false`.

## Dependencia revisada en tema MAIN

- Tema MAIN: `SEO schema hotfix - 2026-06-15`.
- Theme ID: `gid://shopify/OnlineStoreTheme/178383749496`.
- Archivo revisado: `sections/footer-group.json`.
- Menus configurados en el footer MAIN:
  - `footer-profesional`.
  - `footer-brand`.
  - `footer`.
  - `footer-legal`.
- Resultado: `footer-matchwalls` no aparece como menu configurado en el footer MAIN.

Archivo revisado: `sections/footer.liquid`.

- Renderiza los bloques `links` mediante `block.settings.menu.links`.
- No contiene hardcode de `footer-matchwalls`.

Estado de dependencia visible: `VERIFICADO Y CORRECTO`.

## Arbol actual del menu legacy

### PROFESIONAL

- ID: `gid://shopify/MenuItem/493550174435`.
- Tipo: `FRONTPAGE`.
- URL: `/`.
- Hijos:
  - `gid://shopify/MenuItem/495453012195` - `B2B tienda interiorismo` - `PAGE` - `/pages/b2b-tienda-interiorismo` - `gid://shopify/Page/106436165859`.
  - `gid://shopify/MenuItem/493550239971` - `B2B Interiorismo` - `PAGE` - `/pages/horeca` - `gid://shopify/Page/105958375651`.
  - `gid://shopify/MenuItem/493550272739` - `Social, Prensa & Afiliación` - `PAGE` - `/pages/social-prensa-y-afiliacion` - `gid://shopify/Page/106205216995`.
  - `gid://shopify/MenuItem/493550305507` - `Artistas & Diseñadores` - `PAGE` - `/pages/artistas` - `gid://shopify/Page/106205315299`.

### BRAND

- ID: `gid://shopify/MenuItem/493550338275`.
- Tipo: `FRONTPAGE`.
- URL: `/`.
- Hijos:
  - `gid://shopify/MenuItem/493550371043` - `Tarjeta regalo` - `PRODUCT` - `/products/tarjeta-regalo` - `gid://shopify/Product/8296203518179`.
  - `gid://shopify/MenuItem/493550403811` - `Nuestros productos` - `PAGE` - `/pages/nuestros-productos` - `gid://shopify/Page/106278256867`.
  - `gid://shopify/MenuItem/494947631331` - `Sobre nosotros` - `PAGE` - `/pages/sobre-nosotros` - `gid://shopify/Page/106231464163`.
  - `gid://shopify/MenuItem/493550469347` - `Sostenibilidad` - `PAGE` - `/pages/sostenibilidad` - `gid://shopify/Page/106070999267`.

### AYUDA

- ID: `gid://shopify/MenuItem/493550502115`.
- Tipo: `FRONTPAGE`.
- URL: `/`.
- Hijos:
  - `gid://shopify/MenuItem/493550534883` - `Envíos y devoluciones` - `FRONTPAGE` - `/`.
  - `gid://shopify/MenuItem/493550567651` - `Financiación y métodos de pago` - `FRONTPAGE` - `/`.
  - `gid://shopify/MenuItem/493550600419` - `Preguntas frecuentes` - `PAGE` - `/pages/preguntas-frecuentes` - `gid://shopify/Page/106205020387`.
  - `gid://shopify/MenuItem/493550633187` - `Consejos instalación` - `FRONTPAGE` - `/`.
  - `gid://shopify/MenuItem/493550665955` - `Atención al cliente` - `PAGE` - `/pages/atencion-al-cliente` - `gid://shopify/Page/106852450531`.
  - `gid://shopify/MenuItem/493550698723` - `Contacto` - `PAGE` - `/pages/contact` - `gid://shopify/Page/105383657699`.

### LEGAL

- ID: `gid://shopify/MenuItem/493550731491`.
- Tipo: `FRONTPAGE`.
- URL: `/`.
- Hijos:
  - `gid://shopify/MenuItem/493550764259` - `Política de privacidad` - `PAGE` - `/pages/politica-de-privacidad` - `gid://shopify/Page/105703899363`.
  - `gid://shopify/MenuItem/493550797027` - `Política de cookies` - `PAGE` - `/pages/politica-de-cookies` - `gid://shopify/Page/105704063203`.
  - `gid://shopify/MenuItem/493550829795` - `Términos y condiciones` - `PAGE` - `/pages/terminos-y-condiciones` - `gid://shopify/Page/105703997667`.
  - `gid://shopify/MenuItem/493550862563` - `Aviso legal` - `PAGE` - `/pages/aviso-legal` - `gid://shopify/Page/105703932131`.

## Mutacion validada para limpieza propuesta

No ejecutada.

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

## Metodo de reversion

Revertir mediante `menuUpdate` sobre el mismo menu:

1. Restaurar titulo `Footer matchwalls`.
2. Restaurar el arbol anterior con los mismos titulos, tipos, URLs y `resourceId`.
3. Si Shopify no acepta IDs de items eliminados, repetir la restauracion sin los campos `id` para recrear la estructura. En ese caso, el contenido, URLs y recursos se recuperan, pero los IDs de MenuItem podrian cambiar.

Estado de reversibilidad: `VERIFICADO PERO MEJORABLE`, porque la estructura y los enlaces pueden restaurarse, pero la conservacion exacta de IDs tras eliminar items no puede garantizarse sin ejecutar y probar.
