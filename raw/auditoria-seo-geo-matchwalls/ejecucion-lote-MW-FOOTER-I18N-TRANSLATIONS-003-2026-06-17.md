# Ejecución lote MW-FOOTER-I18N-TRANSLATIONS-003 - 2026-06-17

Fecha y hora local de cierre: 2026-06-17 10:53:59 +02:00

## Aprobación

Daniel aprobó exactamente:

`APROBADO LOTE MW-FOOTER-I18N-TRANSLATIONS-003`

## Alcance ejecutado

Se registraron traducciones nativas Shopify para navegación del footer en:

- EN.
- FR.
- DE.
- NL.

Recursos:

- 4 títulos de menú `MENU`.
- 20 enlaces de navegación `LINK`.

No se modificaron:

- Tema MAIN.
- Archivos Liquid.
- Publicación de temas.
- Menús fuente ES.
- Productos, colecciones, páginas, handles, URLs, redirecciones, precios, inventario, variantes, imágenes, App Embeds ni configuración LangShop.

## Preflight realizado

### Recursos traducibles

Shopify expone:

- Títulos de menú como `gid://shopify/Menu/...`.
- Ítems/enlaces como `gid://shopify/Link/...`.

Los IDs `gid://shopify/MenuItem/...` no son válidos para `translatableResourcesByIds`; Shopify devolvió:

`Invalid id: gid://shopify/MenuItem/495449178339`

Se resolvió usando `gid://shopify/Link/...` con el mismo ID numérico.

### Respaldo

Se creó respaldo local:

- `respaldo-MW-FOOTER-I18N-TRANSLATIONS-003-2026-06-17.md`

Incluye:

- Recurso.
- Fuente ES.
- Digest vigente.
- Traducciones previas EN/FR/DE/NL.
- Estado `outdated` anterior.
- Método de reversión.

## Operación ejecutada

Mutación validada:

- `translationsRegister`

Permisos requeridos por validación:

- `write_translations`
- `read_translations`

Resultado:

- 24 llamadas `translationsRegister` dentro de una mutación GraphQL.
- 96 traducciones registradas o actualizadas.
- Todos los bloques devolvieron `userErrors: []`.

## Evidencia Admin posterior

Lectura posterior mediante `translatableResourcesByIds` confirmó:

- 4 menús con traducciones EN/FR/DE/NL actualizadas.
- 20 enlaces con traducciones EN/FR/DE/NL actualizadas.
- Todas las traducciones consultadas quedan `outdated:false`.

Lectura adicional de `Menu.translations` confirmó para títulos de menú:

| Menú | EN | FR | DE | NL | Estado |
| --- | --- | --- | --- | --- | --- |
| `footer` | `HELP AND SUPPORT` | `AIDE ET SUPPORT` | `HILFE UND SUPPORT` | `HULP EN SUPPORT` | `CORREGIDO Y VERIFICADO` por Admin |
| `footer-profesional` | `PROFESSIONALS` | `PROFESSIONNELS` | `FÜR FACHKUNDEN` | `PROFESSIONALS` | `CORREGIDO Y VERIFICADO` por Admin |
| `footer-brand` | `COMPANY` | `ENTREPRISE` | `UNTERNEHMEN` | `BEDRIJF` | `CORREGIDO Y VERIFICADO` por Admin |
| `footer-legal` | `LEGAL` | `LÉGAL` | `RECHTLICHES` | `JURIDISCH` | `CORREGIDO Y VERIFICADO` por Admin |

## Configuración de publicación verificada

Consulta de configuración Shopify confirmó:

| Elemento | Evidencia | Estado |
| --- | --- | --- |
| Tienda | `Matchwalls`, dominio primario `https://www.matchwalls.com`, SSL activo | `VERIFICADO Y CORRECTO` |
| Tema MAIN | `SEO schema hotfix - 2026-06-15`, `gid://shopify/OnlineStoreTheme/178383749496`, `role: MAIN`, `processing:false`, `processingFailed:false` | `VERIFICADO Y CORRECTO` |
| Idioma ES | `published:true`, `primary:true` | `VERIFICADO Y CORRECTO` |
| Idioma EN | `published:true`, URL raíz `https://www.matchwalls.com/en/` | `VERIFICADO Y CORRECTO` |
| Idioma FR | `published:true`, URL raíz `https://www.matchwalls.com/fr/` | `VERIFICADO Y CORRECTO` |
| Idioma DE | `published:true`, URL raíz `https://www.matchwalls.com/de/` | `VERIFICADO Y CORRECTO` |
| Idioma NL | `published:true`, URL raíz `https://www.matchwalls.com/nl/` | `VERIFICADO Y CORRECTO` |
| LangShop App Embed en MAIN | `config/settings_data.json` contiene `shopify://apps/langshop/blocks/sdk/...`, `disabled:false` | `VERIFICADO PERO MEJORABLE` |

También se verificó que IT y PT-PT siguen publicados, pero quedan fuera del alcance prioritario de este lote.

## Permisos reales del conector

El conector actual es:

- `Shopify ChatGPT MCP App`
- `gid://shopify/AppInstallation/811026186616`

Permisos relevantes verificados:

- `write_translations`
- `read_translations`
- `read_locales`
- `write_locales`
- `read_markets`
- `write_markets`
- `read_themes`
- `write_themes`
- `read_online_store_navigation`
- `write_online_store_navigation`

Nota: que el conector tenga permisos amplios no autoriza su uso fuera de un lote aprobado. En este lote solo se usó `write_translations`.

## LangShop

Se tuvo en cuenta LangShop como capa activa.

Evidencia verificada:

- LangShop SDK está activo como App Embed en el tema MAIN.

Límite de acceso:

- `appInstallations` devuelve `access denied`.
- No se puede consultar desde este conector la configuración interna de LangShop, su plan, glosarios, auto-sync, reglas o cola de publicación.

Estado:

- App Embed: `VERIFICADO PERO MEJORABLE`.
- Configuración interna LangShop: `NO ACCESIBLE`.

Interpretación:

- Las traducciones nativas están correctamente almacenadas en Shopify.
- La configuración Shopify de idiomas y rutas permite que EN/FR/DE/NL sean visibles para compradores.
- No queda demostrado desde este entorno que LangShop no sobrescriba, cachee o interfiera en el render público.

## QA pública

Intentos:

- Navegador interno: `https://www.matchwalls.com/en/`
  - Resultado: página Shopify de error con título `Algo salió mal` y texto `Se ha producido un error al descargar el sitio`.
- `Invoke-WebRequest`: error `Se ha terminado la conexión: Error inesperado de recepción`.
- `curl.exe -I`: error de conexión a `www.matchwalls.com:443` vía `127.0.0.1`.

Estado:

- Render público EN/FR/DE/NL desde este entorno: `NO ACCESIBLE`.

No se puede afirmar que el footer público esté corregido visualmente hasta verlo en storefront real.

## Estado final por capa

| Capa | Estado |
| --- | --- |
| Traducciones almacenadas en Shopify Admin | `CORREGIDO Y VERIFICADO` |
| Títulos de menú publicados según `Menu.translations` | `CORREGIDO Y VERIFICADO` |
| Enlaces `LINK` almacenados y `outdated:false` | `CORREGIDO Y VERIFICADO` por Admin |
| Configuración de idiomas EN/FR/DE/NL visible para compradores | `VERIFICADO Y CORRECTO` |
| Tema MAIN real | `VERIFICADO Y CORRECTO` |
| LangShop App Embed activo | `VERIFICADO PERO MEJORABLE` |
| Configuración interna LangShop | `NO ACCESIBLE` |
| Render público storefront | `NO ACCESIBLE` |

## Reversión

Si se necesita revertir:

1. Consultar de nuevo `translatableResourcesByIds` para obtener `digest` vigente.
2. Ejecutar `translationsRegister` sobre los mismos recursos.
3. Usar los valores anteriores documentados en `respaldo-MW-FOOTER-I18N-TRANSLATIONS-003-2026-06-17.md`.
4. Verificar `userErrors: []`.
5. Leer Admin y storefront público.

## Próximo paso necesario

Verificación humana o desde un entorno con acceso público real a:

- `https://www.matchwalls.com/en/`
- `https://www.matchwalls.com/fr/`
- `https://www.matchwalls.com/de/`
- `https://www.matchwalls.com/nl/`

Comprobar footer visible:

- Que aparezcan las traducciones nuevas.
- Que no aparezcan `FAQ´S`, `FAQ´s`, `Professional & social`, `brand`, `PROFESIONALES`, `EMPRESA`, `AYUDA Y SOPORTE`, `schaamruimtes`, `B2B Hotels & Contact`.
- Que sigan ausentes `Tarjeta regalo`, `Black Friday 2024`, `Envíos internacionales`.

## Clasificación final del lote

`CORREGIDO Y VERIFICADO` en Shopify Admin.

`NO ACCESIBLE` en render público desde este entorno.
