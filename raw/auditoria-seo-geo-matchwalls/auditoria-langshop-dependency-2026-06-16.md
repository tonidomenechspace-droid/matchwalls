# Auditoria dependencia LangShop - 2026-06-16

Fecha: 2026-06-16 11:37:39 +02:00

Modo: solo lectura. No se ha modificado Shopify, apps, temas, traducciones, mercados, URLs, productos, colecciones, paginas, menus, precios, inventario, imagenes ni variantes.

## Objetivo

Responder si MatchWalls puede eliminar LangShop o reducir su plan sin poner en riesgo SEO internacional, GEO/LLMO, traducciones, URLs localizadas, checkout, contenido dinamico y gestion editorial multilingue.

## Fuentes revisadas

- `AGENTS.md`.
- `registro-cambios-ejecutados.md`.
- `auditoria-contenido-i18n-geo-2026-06-16.md`.
- `inventario-problemas-contenido-i18n-geo-2026-06-16.csv`.
- `textos-fijos-plantilla-bloqueantes-2026-06-16.csv`.
- `qa-post-publicacion-hotfix-2026-06-16-MW-PUBLISH-HOTFIX-001.md`.
- Shopify Admin GraphQL en modo lectura.
- Tema MAIN `SEO schema hotfix - 2026-06-15`.
- Shopify App Store: `https://apps.shopify.com/langshop`.
- LangShop pricing: `https://langshop.io/pricing`.
- Shopify docs sobre traducciones: `https://shopify.dev/docs/apps/build/markets/manage-translated-content`.
- Shopify Help Center sobre idiomas/localizacion: `https://help.shopify.com/en/manual/international/localization-and-translation`.

## Estado verificado de Shopify

| Elemento | Evidencia | Estado |
|---|---|---|
| Tienda | `Matchwalls`, dominio primario `https://www.matchwalls.com`, myshopify `matchwalls.myshopify.com` | `VERIFICADO Y CORRECTO` |
| Tema MAIN | `SEO schema hotfix - 2026-06-15`, `gid://shopify/OnlineStoreTheme/178383749496` | `VERIFICADO Y CORRECTO` |
| Productos | `productsCount.count = 3022` | `VERIFICADO Y CORRECTO` |
| Colecciones | `collectionsCount.count = 109` | `VERIFICADO Y CORRECTO` |
| Idiomas publicados | `es` primario; `en`, `fr`, `de`, `nl`, `it`, `pt-PT` publicados | `VERIFICADO Y CORRECTO` |
| Idiomas prioritarios SEO/GEO | ES, EN, FR, DE, NL | `VERIFICADO Y CORRECTO` |
| Presencia web | Dominio unico `www.matchwalls.com` con subcarpetas por idioma: `/en/`, `/fr/`, `/de/`, `/nl/`, `/it/`, `/pt/` | `VERIFICADO Y CORRECTO` |
| Selector de idioma del tema | `snippets/localization-selector.liquid` usa formulario nativo `{% form 'localization' %}` y `localization.available_languages` | `VERIFICADO Y CORRECTO` |
| LangShop en tema MAIN | `config/settings_data.json` contiene bloque activo `shopify://apps/langshop/blocks/sdk/...`, `disabled:false` | `VERIFICADO PERO MEJORABLE` |
| Instalacion/suscripcion LangShop | `appInstallations` devuelve `access denied`; `appByHandle(handle:"langshop")` devuelve app publica pero `installation:null` | `NO ACCESIBLE` / `REQUIERE DECISION HUMANA` |

## Evidencia de dependencias

### 1. LangShop aparece como App Embed activo en el tema

En `config/settings_data.json` del MAIN:

- Bloque: `18146506648094396618`.
- Tipo: `shopify://apps/langshop/blocks/sdk/84899e01-2b29-42af-99d6-46d16daa2111`.
- `disabled: false`.

Interpretacion:

- Hay una referencia activa a LangShop en el tema publicado.
- No se ha verificado que el script este cargando publicamente en este turno porque el acceso HTML publico desde el entorno devolvio 403/TLS.
- En el QA post-hotfix previo si se documento deteccion publica de LangShop.

Estado: `VERIFICADO PERO MEJORABLE`.

### 2. La gestion de idioma visible del tema no depende exclusivamente de LangShop

El snippet `snippets/localization-selector.liquid` usa:

- formulario nativo de Shopify `localization`;
- `localization.available_languages`;
- `locale_code`;
- `localization.available_countries`.

Interpretacion:

- El selector basico de idioma/mercado parece nativo del tema/Shopify Markets.
- LangShop puede seguir aportando SDK, deteccion, traduccion dinamica, traducciones de apps, auto-sync, reglas/glosario o herramientas de gestion.

Estado: `VERIFICADO Y CORRECTO` para selector nativo; dependencia LangShop de funciones avanzadas: `REQUIERE DECISION HUMANA`.

### 3. Traducciones almacenadas en Shopify

Consultas `translatableResources` confirman traducciones nativas en Shopify para:

- `PAGE`.
- `PRODUCT`.
- `COLLECTION`.

Ejemplos verificados:

- Pagina Contacto: traducciones EN/FR/DE/NL vigentes (`outdated:false`) en titulo, cuerpo y metadatos.
- Productos de prueba: traducciones multilingues existentes, muchas con baja calidad, `Lorem ipsum`, `Pain`, `Nan`, y `outdated:true` en cuerpos.
- Colecciones: traducciones EN/FR/DE/NL/IT/PT existentes; varios handles defectuosos.

Interpretacion:

- Muchas traducciones estan guardadas en la capa nativa de Shopify, no solo renderizadas por una app en cliente.
- Esto no prueba que desinstalar LangShop sea seguro, porque el app puede gestionar historico, auto-sync, reglas, contenido dinamico, checkout o apps de terceros.

Estado: `VERIFICADO PERO MEJORABLE`.

### 4. Limites de plan LangShop frente a MatchWalls

Fuentes externas consultadas:

- Shopify App Store y LangShop pricing.

Planes publicos observados:

| Plan | Idiomas | Productos aproximados AI/gestion | Comentario para MatchWalls |
|---|---:|---:|---|
| Free | 1 | 50 | No encaja |
| Basic | 1 | 250 | No encaja |
| Standard | 3 | 2000 | No encaja con 3022 productos ni ES/EN/FR/DE/NL |
| Advanced | 5 | 5000 | Puede encajar para 5 idiomas prioritarios, pero riesgo si cuenta los 6 idiomas no primarios publicados |
| Pro | 10 | 10000 | Encaja mejor si se gestionan EN/FR/DE/NL/IT/PT-PT y 3022 productos |
| Enterprise/Unlimited | 20 | 50000 / ilimitado | Sobredimensionado salvo necesidad operativa |

Estado: `VERIFICADO PERO MEJORABLE`.

### 5. Deuda editorial detectada no se soluciona reduciendo/eliminando LangShop

La auditoria confirma problemas que requieren QA editorial y ejecucion controlada:

- DE/NL con traducciones automaticas deficientes.
- IT/PT publicados con traducciones `outdated:true` en recursos recientes.
- Productos de prueba publicados/traducidos con `Lorem ipsum`.
- Campos con `Nan`.
- Handles traducidos defectuosos: `matchwalswallpapers`, `matchwallsmurals`, typos y traducciones literales.
- Contenido fijo de plantillas que bloquea traducciones gobernadas.

Interpretacion:

- LangShop no debe considerarse garantia de calidad.
- Quitar LangShop ahora tampoco corrige la deuda; puede empeorar la capacidad de gestion masiva.

Estado: `INCORRECTO` para calidad editorial existente; decision app: `REQUIERE DECISION HUMANA`.

## Riesgos si se elimina LangShop ahora

| Riesgo | Impacto SEO | Impacto GEO/LLMO | Impacto comercial | Estado |
|---|---|---|---|---|
| Perder gestion masiva de traducciones y auto-sync | Alto | Alto | Alto | `RIESGO CRITICO` |
| Romper o dejar huerfano el App Embed activo | Medio | Medio | Medio | `VERIFICADO PERO MEJORABLE` |
| Perder traduccion dinamica de apps/checkout/metafields si se usa | Alto | Alto | Alto | `NO ACCESIBLE` |
| No poder mantener catalogo 3022 productos en 5-7 idiomas | Alto | Alto | Alto | `RIESGO CRITICO` |
| Confundir mejora de calidad con ahorro de app | Alto | Alto | Medio | `INCORRECTO` |
| Bajar a plan por debajo de idiomas/productos publicados | Alto | Alto | Alto | `RIESGO CRITICO` |

## Decision recomendada

No eliminar LangShop ahora.

No reducir plan ahora si el plan actual es Advanced, Pro o superior hasta comprobar desde el Admin de LangShop:

1. Plan contratado real.
2. Numero de idiomas que LangShop considera activos o gestionados.
3. Si cuenta ES como idioma o solo idiomas traducidos.
4. Si IT y PT-PT consumen cupo.
5. Uso de traduccion dinamica de apps.
6. Uso de auto-sync para nuevos productos/colecciones.
7. Uso de glosario, reglas y exclusiones.
8. Exportacion completa disponible.
9. Historico/versionado recuperable.
10. Dependencia de checkout, metafields, metaobjects, menus y contenido de tema.

## Escenarios seguros

### Escenario A: mantener LangShop temporalmente

Recomendado ahora.

Condiciones:

- Completar auditoria de dependencia.
- Exportar traducciones.
- Sanear ES/EN/FR/DE/NL.
- Decidir si IT/PT-PT siguen publicados.
- Crear proceso editorial con glosario.

Estado: `RECOMENDADO`.

### Escenario B: bajar a Advanced

Solo posible si:

- LangShop cuenta 5 idiomas como limite y MatchWalls gestiona exactamente 5 idiomas dentro del plan.
- IT/PT-PT quedan fuera del uso real o se despublican con estrategia SEO/301/404 controlada.
- 3022 productos quedan dentro del limite de 5000.
- No se pierden funciones necesarias de Pro/API.

Estado: `REQUIERE DECISION HUMANA`.

### Escenario C: bajar a Standard

No recomendado.

Motivo:

- Standard declara 3 idiomas y 2000 productos.
- MatchWalls tiene 3022 productos y 5 idiomas prioritarios, mas IT/PT-PT publicados.

Estado: `RIESGO CRITICO`.

### Escenario D: eliminar LangShop

No recomendado ahora.

Solo podria plantearse tras:

- Export completo de traducciones.
- Backup de tema y `settings_data`.
- QA de selector de idioma y mercados sin SDK.
- Desactivar primero App Embed en tema auxiliar, nunca directamente en MAIN.
- Test publico ES/EN/FR/DE/NL/IT/PT-PT.
- Confirmar checkout, formularios, apps, metafields, menus, sitemap, hreflang y schema.
- Plan alternativo: Shopify Translate & Adapt, CSV nativo, app alternativa o flujo propio via Admin API.

Estado: `RIESGO CRITICO`.

## Siguiente lote recomendado

`MW-LANGSHOP-DEPENDENCY-AUDIT-001`

Modo: solo lectura.

Alcance:

- Entrar al Admin de LangShop y documentar plan real, idiomas activos, productos contabilizados, auto-sync, glosarios, reglas, exclusiones, export/import, traduccion dinamica, apps conectadas, checkout y metafields.
- Exportar o solicitar export de traducciones antes de cualquier cambio de plan.
- No cambiar plan, no desinstalar, no desactivar App Embed y no ejecutar traducciones automaticas.

Decision tras ese lote:

- Mantener plan.
- Bajar plan con riesgo controlado.
- Preparar migracion fuera de LangShop.
- Mantener LangShop solo hasta terminar saneamiento editorial.

## Estado final de esta auditoria

`REQUIERE DECISION HUMANA`

Conclusion ejecutiva:

LangShop no debe eliminarse ni rebajarse todavia. MatchWalls tiene 3022 productos, 7 idiomas publicados contando ES, y una deuda editorial multilingue activa. La tienda ya almacena traducciones nativas en Shopify, pero LangShop sigue referenciado como App Embed activo y puede estar sosteniendo funciones de gestion, auto-sync o traduccion dinamica. El primer paso seguro es auditar el panel de LangShop y hacer export/backup antes de tocar el plan.
