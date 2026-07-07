# Respaldo MW-FOOTER-I18N-001 - 2026-06-17

Estado: RESPALDO PREVIO A EJECUCION

Fecha/hora de trabajo: 2026-06-17

Cambios en tema MAIN: ninguno.

Publicaciones: ninguna.

Menús modificados: ninguno.

## Tema MAIN de origen

- Tienda: `Matchwalls`
- Dominio principal: `https://www.matchwalls.com`
- Tema MAIN: `SEO schema hotfix - 2026-06-15`
- ID MAIN: `gid://shopify/OnlineStoreTheme/178383749496`
- Estado MAIN: `processing=false`, `processingFailed=false`

Archivos clave en MAIN:

| Archivo | Checksum MD5 | Tamaño | Actualizado |
| --- | --- | ---: | --- |
| `config/settings_data.json` | `a1192f2f698d277e0f69f7156a61a90c` | `10256` | `2026-06-15T12:34:14Z` |
| `sections/footer-group.json` | `e93af9228c8a97dce4ad91e203bf7e75` | `4210` | `2026-06-15T12:34:21Z` |
| `sections/header-group.json` | `671e993b0001e876d7a1bc51d8ccd44d` | `6939` | `2026-06-15T12:34:21Z` |
| `snippets/microdata-schema.liquid` | `58417e4825aa3d4570a6646f292aaedc` | `10787` | `2026-06-15T20:19:10Z` |

## Tema QA creado

- Nombre: `MW-FOOTER-I18N-001 - QA - 2026-06-17`
- ID: `gid://shopify/OnlineStoreTheme/178390401400`
- Estado: `UNPUBLISHED`
- Estado tras procesado: `processing=false`, `processingFailed=false`

Archivos clave tras duplicar MAIN:

| Archivo | Checksum MD5 | Tamaño | Actualizado |
| --- | --- | ---: | --- |
| `config/settings_data.json` | `a1192f2f698d277e0f69f7156a61a90c` | `10256` | `2026-06-17T08:13:08Z` |
| `sections/footer-group.json` | `e93af9228c8a97dce4ad91e203bf7e75` | `4210` | `2026-06-17T08:13:16Z` |
| `sections/header-group.json` | `671e993b0001e876d7a1bc51d8ccd44d` | `6939` | `2026-06-17T08:13:16Z` |
| `snippets/microdata-schema.liquid` | `58417e4825aa3d4570a6646f292aaedc` | `10787` | `2026-06-17T08:12:59Z` |

## `sections/footer-group.json` original

```json
/*
 * ------------------------------------------------------------
 * IMPORTANT: The contents of this file are auto-generated.
 *
 * This file may be updated by the Shopify admin theme editor
 * or related systems. Please exercise caution as any changes
 * made to this file may be overwritten.
 * ------------------------------------------------------------
 */
{
  "type": "footer",
  "name": "Footer group",
  "sections": {
    "newsletter_3KJrzh": {
      "type": "newsletter",
      "settings": {
        "full_width": true,
        "klaviyo_newsletter": "<div class=\"klaviyo-form-U2ngKt\"></div>",
        "show_icon": false,
        "title": "NOTICIAS, INSPIRACIÓN, REGALOS Y NOVEDADES",
        "content": "<p>¡Suscríbete a nuestras noticias! Se el primero en enterarte de las últimas tendencias, novedades de nuestros papeles pintados y art prints además de divertidos tips que te ayudarán a decorar tu espacio particular o residencial. #BeMatchWalls</p>",
        "button_text": "",
        "subtext": "#JoinTheMatch",
        "background": "#f2f2f2",
        "background_gradient": "",
        "text_color": "",
        "button_background": "",
        "button_text_color": ""
      }
    },
    "text-with-icons": {
      "type": "text-with-icons",
      "blocks": {
        "item_A8zFya": {
          "type": "item",
          "settings": {
            "icon": "picto-box",
            "custom_icon": "shopify://shop_images/Caja_1ec22c37-ba87-4497-b3f2-8ea902c4a67e.webp",
            "mobile_icon_width": 24,
            "icon_width": 36,
            "icon_background_type": "none",
            "icon_background": "#f8e1e7",
            "icon_color": "#504746",
            "title": "Envío gratuito",
            "content": "Worldwide."
          }
        },
        "item_QgtB3M": {
          "type": "item",
          "settings": {
            "icon": "picto-credit-card",
            "custom_icon": "shopify://shop_images/Cell.webp",
            "mobile_icon_width": 24,
            "icon_width": 36,
            "icon_background_type": "none",
            "icon_background": "#f8e1e7",
            "icon_color": "#504746",
            "title": "Pago seguro",
            "content": "Metodos de pago seguros y financiación."
          }
        },
        "item_DEWgDL": {
          "type": "item",
          "settings": {
            "icon": "picto-star",
            "custom_icon": "shopify://shop_images/Carita.webp",
            "mobile_icon_width": 24,
            "icon_width": 36,
            "icon_background_type": "none",
            "icon_background": "#f8e1e7",
            "icon_color": "#504746",
            "title": "Garantía de satisfacción",
            "content": "Nuestro compromiso tu tranquilidad."
          }
        },
        "customer-support": {
          "type": "item",
          "settings": {
            "icon": "picto-printer",
            "custom_icon": "shopify://shop_images/Pintura_8e0c8284-761d-46a1-9333-57752703bfc2.webp",
            "mobile_icon_width": 36,
            "icon_width": 48,
            "icon_background_type": "none",
            "icon_background": "#f8e1e7",
            "icon_color": "#504746",
            "title": "Personalización",
            "content": "Te ayudamos a crear tu diseño Matchwalls."
          }
        },
        "item_gm7PTn": {
          "type": "item",
          "settings": {
            "icon": "picto-customer-support",
            "custom_icon": "shopify://shop_images/Engranaje.webp",
            "mobile_icon_width": 36,
            "icon_width": 36,
            "icon_background_type": "none",
            "icon_background": "#f8e1e7",
            "icon_color": "#504746",
            "title": "Fácil instalación",
            "content": "Descargate nuestras guías de fácil instlacióon."
          }
        }
      },
      "block_order": [
        "item_A8zFya",
        "item_QgtB3M",
        "item_DEWgDL",
        "customer-support",
        "item_gm7PTn"
      ],
      "custom_css": [],
      "settings": {
        "full_width": true,
        "stack_on_mobile": false,
        "title": "",
        "heading_tag": "h6",
        "text_alignment": "center",
        "icon_spacing": "small",
        "background": "rgba(0,0,0,0)",
        "background_gradient": "",
        "text_color": ""
      }
    },
    "footer": {
      "type": "footer",
      "blocks": {
        "links_hFcP7H": {
          "type": "links",
          "settings": {
            "menu": "footer-profesional",
            "show_menu_title": true,
            "menu_title": ""
          }
        },
        "links_X4Yg8z": {
          "type": "links",
          "settings": {
            "menu": "footer-brand",
            "show_menu_title": true,
            "menu_title": ""
          }
        },
        "links_Qp4ir6": {
          "type": "links",
          "settings": {
            "menu": "footer",
            "show_menu_title": true,
            "menu_title": ""
          }
        },
        "newsletter_rYyiKC": {
          "type": "newsletter",
          "settings": {
            "store_title": "",
            "icon": "shopify://shop_images/Logo_MatchWalls-02.png",
            "additional_text": "",
            "image_width": 50,
            "heading_size": "h3",
            "title": "#Bematchwalls",
            "content": "<p><strong>Lunes a Jueves:</strong> 9-17H (GMT +1)<br/><strong>Viernes:</strong> 9 - 14H (GMT +1)<br/>Cerrado para el almuerzo de 13H a 14H<strong><br/></strong><a href=\"mailto:help@matchwalls.com\" target=\"_blank\">help@matchwalls.com<br/></a>Av Diagonal 508 Principal 2ª, 08006, Barcelona, Spain</p>",
            "content_2": "",
            "content_3": "",
            "show_newsletter": false
          }
        },
        "links_fJFVfP": {
          "type": "links",
          "settings": {
            "menu": "footer-legal",
            "show_menu_title": true,
            "menu_title": ""
          }
        }
      },
      "block_order": [
        "links_hFcP7H",
        "links_X4Yg8z",
        "links_Qp4ir6",
        "newsletter_rYyiKC",
        "links_fJFVfP"
      ],
      "custom_css": [
        ".bold {font-weight: 900; font-size: large;}",
        ".social-media {color: #f1b6c9; margin-block: 3%;}"
      ],
      "settings": {
        "show_social_media": true,
        "show_payment_icons": true,
        "show_country_selector": false,
        "show_country_flag": false,
        "show_country_name": false,
        "show_locale_selector": false
      }
    }
  },
  "order": [
    "newsletter_3KJrzh",
    "text-with-icons",
    "footer"
  ]
}
```

## Menús globales afectados, sin cambios

### `footer`

- ID: `gid://shopify/Menu/210266325219`
- Handle: `footer`
- Título: `AYUDA & SOPORTE`
- Default: `true`

Elementos:

| ID | Título | Tipo | URL | Recurso |
| --- | --- | --- | --- | --- |
| `gid://shopify/MenuItem/495449178339` | `FAQ´S - Envíos y devoluciones` | `PAGE` | `/pages/preguntas-frecuentes` | `gid://shopify/Page/106205020387` |
| `gid://shopify/MenuItem/495449211107` | `Crea tu propio papel pintado rollo` | `PAGE` | `/pages/crea-tu-papel-pintado-rollo` | `gid://shopify/Page/106205151459` |
| `gid://shopify/MenuItem/495449243875` | `Crea tu papel pintado mural personalizado` | `PAGE` | `/pages/crea-tu-mural` | `gid://shopify/Page/106205118691` |
| `gid://shopify/MenuItem/497161568483` | `Cómo tomar medidas de paredes` | `PAGE` | `/pages/medidas-paredes` | `gid://shopify/Page/106229170403` |
| `gid://shopify/MenuItem/497161601251` | `Cómo tomar medidas del techo` | `PAGE` | `/pages/medidas-techo` | `gid://shopify/Page/106229203171` |
| `gid://shopify/MenuItem/712964669816` | `Envíos internacionales` | `PAGE` | `/pages/envios-internacionales` | `gid://shopify/Page/687276589432` |
| `gid://shopify/MenuItem/713032991096` | `Black Friday 2024` | `COLLECTION` | `/collections/papel-pintado-black-friday` | `gid://shopify/Collection/646234440056` |
| `gid://shopify/MenuItem/713118876024` | `Your Privacy Choices` | `PAGE` | `/pages/data-sharing-opt-out` | `gid://shopify/Page/687313092984` |

Traducciones título menú:

- EN: `Help &amp; support`, `outdated=true`, actualizado `2024-07-25T11:48:16Z`
- FR: sin traducción leída
- DE: `Hilfe Unterstützung`, `outdated=true`, actualizado `2024-07-25T11:48:16Z`
- NL: sin traducción leída

### `footer-profesional`

- ID: `gid://shopify/Menu/210972311779`
- Handle: `footer-profesional`
- Título: `PROFESIONALES & SOCIAL`
- Default: `false`

Elementos:

| ID | Título | Tipo | URL | Recurso |
| --- | --- | --- | --- | --- |
| `gid://shopify/MenuItem/493556531427` | `B2B Tiendas interiorismo` | `PAGE` | `/pages/tiendas` | `gid://shopify/Page/105958342883` |
| `gid://shopify/MenuItem/493556564195` | `B2B Estudios interiorismo y arquitectura, hoteles y espacios púbicos.` | `PAGE` | `/pages/estudios-profesionales` | `gid://shopify/Page/106279141603` |
| `gid://shopify/MenuItem/503255138531` | `B2B Hoteles & Contact` | `PAGE` | `/pages/horeca` | `gid://shopify/Page/105958375651` |
| `gid://shopify/MenuItem/493556596963` | `Social & Prensa y Afiliación` | `PAGE` | `/pages/social-prensa-y-afiliacion` | `gid://shopify/Page/106205216995` |
| `gid://shopify/MenuItem/493556629731` | `Artistas & Diseñadores` | `PAGE` | `/pages/artistas` | `gid://shopify/Page/106205315299` |
| `gid://shopify/MenuItem/495008121059` | `Solicita tu muestra` | `PAGE` | `/pages/muestras` | `gid://shopify/Page/106299195619` |

Traducciones título menú:

- EN: `Professional &amp; social`, `outdated=true`, actualizado `2024-07-25T11:35:19Z`
- FR: sin traducción leída
- DE: `Professionell und sozial`, `outdated=true`, actualizado `2024-07-25T11:35:19Z`
- NL: sin traducción leída

### `footer-brand`

- ID: `gid://shopify/Menu/210972344547`
- Handle: `footer-brand`
- Título: `EMPRESA`
- Default: `false`

Elementos:

| ID | Título | Tipo | URL | Recurso |
| --- | --- | --- | --- | --- |
| `gid://shopify/MenuItem/494947959011` | `Sobre Nosotros` | `PAGE` | `/pages/sobre-nosotros` | `gid://shopify/Page/106231464163` |
| `gid://shopify/MenuItem/494947926243` | `Nuestros Productos` | `PAGE` | `/pages/nuestros-productos` | `gid://shopify/Page/106278256867` |
| `gid://shopify/MenuItem/494947991779` | `Sostenibilidad` | `PAGE` | `/pages/sostenibilidad` | `gid://shopify/Page/106070999267` |
| `gid://shopify/MenuItem/494950613219` | `Inspiración` | `BLOG` | `/blogs/inspiracion` | `gid://shopify/Blog/91347550435` |
| `gid://shopify/MenuItem/493556662499` | `Tarjeta regalo` | `PRODUCT` | `/products/tarjeta-regalo` | `gid://shopify/Product/8296203518179` |

Traducciones título menú:

- EN: `brand`, `outdated=true`, actualizado `2024-07-25T11:47:38Z`
- FR: sin traducción leída
- DE: `Marke`, `outdated=true`, actualizado `2024-07-25T11:47:38Z`
- NL: sin traducción leída

### `footer-legal`

- ID: `gid://shopify/Menu/210972410083`
- Handle: `footer-legal`
- Título: `Legal`
- Default: `false`

Elementos:

| ID | Título | Tipo | URL | Recurso |
| --- | --- | --- | --- | --- |
| `gid://shopify/MenuItem/493557088483` | `Aviso Legal` | `PAGE` | `/pages/aviso-legal` | `gid://shopify/Page/105703932131` |
| `gid://shopify/MenuItem/493557022947` | `Política de Cookies` | `PAGE` | `/pages/politica-de-cookies` | `gid://shopify/Page/105704063203` |
| `gid://shopify/MenuItem/493557055715` | `Condiciones de uso de la web` | `PAGE` | `/pages/condiciones-de-uso` | `gid://shopify/Page/106604036323` |
| `gid://shopify/MenuItem/496053289187` | `Condiciones de venta online` | `PAGE` | `/pages/condiciones-de-venta-online` | `gid://shopify/Page/106604658915` |

Traducciones título menú:

- EN: sin traducción leída
- FR: sin traducción leída
- DE: sin traducción leída
- NL: sin traducción leída

## Nota sobre traducciones del tema

Se consultó el recurso traducible del tema MAIN con `translatableResource`.

Resultado operativo:

- La API devuelve una lista amplia de claves de todo el tema.
- Se confirmó que existen claves de `sections/footer-group.json`, por ejemplo:
  - `section.sections/footer-group.json.footer.newsletter_rYyiKC.icon:d3wbzb0bwd6g`
  - `section.sections/footer-group.json.text-with-icons.item_A8zFya.content:1e8vnqndgd6he`
- La respuesta completa es demasiado amplia para usarla como base manual segura sin filtrado por clave.

Decisión de seguridad:

- No se registrarán traducciones EN/FR/DE/NL en este paso sin inventario exacto de claves, digest y valores propuestos.
- No se modifican menús globales en este paso porque impactan el sitio publicado.
