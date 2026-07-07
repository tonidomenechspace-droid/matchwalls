# MW-CRAWLERS-WAF-CDN-BOT-ALLOWLIST-DIAG-013F

Fecha: 2026-07-05  
Hora de registro: 12:58 Europe/Madrid  
Modo: solo lectura  
Estado final: `VERIFICADO PERO MEJORABLE`

## Objetivo

Comprobar si Shopify/CDN/WAF/app de seguridad está bloqueando, degradando o alterando respuestas públicas para bots legítimos de buscadores e IA:

- Googlebot
- Bingbot
- OAI-SearchBot
- GPTBot
- ClaudeBot / Claude-SearchBot
- PerplexityBot / Perplexity-User
- Applebot
- Navegador Chrome como control

Este lote no modifica Shopify, `robots.txt`, Bing Webmaster Tools, IndexNow, temas, apps, URLs, handles ni configuración.

## Documentos revisados

`VERIFICADO Y CORRECTO`

- `registro-cambios-ejecutados.md`
- `diagnostico-MW-CRAWLERS-BING-COPILOT-AI-ROBOTS-DIAG-013B-2026-07-04.md`
- `propuesta-MW-CRAWLERS-SEARCH-AI-POLICY-PROPOSAL-013C-2026-07-04.md`
- `review-MW-CRAWLERS-SEARCH-AI-POLICY-PROPOSAL-013C-REVIEW-2026-07-05.md`
- `policy-review-matrix-MW-CRAWLERS-SEARCH-AI-POLICY-PROPOSAL-013C-REVIEW-2026-07-05.csv`

Fuentes oficiales revisadas:

- OpenAI Crawlers
- Anthropic Crawlers
- Perplexity Crawlers
- Google AI features
- Applebot
- Bing Chat / Copilot controls

## Alcance de pruebas públicas

`VERIFICADO Y CORRECTO`

URLs probadas:

- `https://www.matchwalls.com/`
- `https://www.matchwalls.com/robots.txt`
- `https://www.matchwalls.com/sitemap.xml`
- `https://www.matchwalls.com/llms.txt`
- `https://www.matchwalls.com/agents.md`
- `https://www.matchwalls.com/pages/papel-pintado-espana`
- `https://www.matchwalls.com/en/collections/`

User-agents probados:

- Chrome
- Googlebot
- Bingbot
- OAI-SearchBot
- GPTBot
- Claude-SearchBot
- ClaudeBot
- PerplexityBot
- Perplexity-User
- Applebot

Limitación importante:

`NO ACCESIBLE`

Desde este entorno no se puede simular IP oficial real de Google, Bing, OpenAI, Anthropic, Perplexity o Apple. Por tanto, este diagnóstico valida respuesta por `User-Agent`, no validación completa por IP/reverse DNS.

## Resultado técnico

### 1. Archivos técnicos públicos

`VERIFICADO Y CORRECTO`

Los siguientes archivos respondieron `200 OK` para todos los user-agents probados:

- `robots.txt`
- `sitemap.xml`
- `llms.txt`
- `agents.md`

No se observó bloqueo WAF/CDN en estos recursos.

### 2. Páginas internas / landings

`VERIFICADO Y CORRECTO`

Las siguientes URLs respondieron `200 OK` para los user-agents probados:

- `https://www.matchwalls.com/pages/papel-pintado-espana`
- `https://www.matchwalls.com/en/collections/`

No se observó bloqueo WAF/CDN global sobre páginas internas en esta muestra.

### 3. Home pública

`RIESGO CRITICO`

La home `https://www.matchwalls.com/` devolvió errores `500` intermitentes con página genérica Shopify.

Marcador del cuerpo devuelto en error:

```txt
<!-- The source of truth for this generic error page
```

En el recheck focalizado de home:

- Chrome: 2/5 respuestas `200`, 3/5 respuestas `500`
- Googlebot: 1/5 respuestas `200`, 4/5 respuestas `500`
- Bingbot: 0/5 respuestas `200`, 5/5 respuestas `500`
- OAI-SearchBot: 0/5 respuestas `200`, 5/5 respuestas `500`
- PerplexityBot: 0/5 respuestas `200`, 5/5 respuestas `500`

Total de la muestra focalizada: 22 fallos `500` sobre 25 solicitudes.

Esto no se comporta como un bloqueo WAF típico (`403`, `401`, captcha, `429`). Se comporta como error interno/intermitente de renderizado Shopify/CDN/shard en la home.

## Request IDs relevantes

`VERIFICADO Y CORRECTO`

Ejemplos de request IDs con `500` en home:

- Chrome: `b28ba463-9efe-47ac-a638-b153db8fa710-1783249035`
- Chrome: `ed355b04-e06e-4e99-aadc-459a8a2b1984-1783249044`
- Googlebot: `a75dba13-b5dc-4928-bd61-86908d9a76c8-1783249050`
- Googlebot: `44fe6cec-f154-4902-8f42-501f8f980d34-1783249055`
- Bingbot: `60df860b-52f7-49fb-8653-45e95c9126ec-1783249064`
- Bingbot: `0671c88a-895d-4584-8f69-edbf83374ce4-1783249067`
- OAI-SearchBot: `f2251646-9d32-428c-ada3-17edd2f96642-1783249080`
- OAI-SearchBot: `63a5262e-e04e-4850-8137-f0e6d4a702cc-1783249083`
- PerplexityBot: `7c58b0f9-1547-438b-b166-2f68aa6cb48a-1783249095`
- PerplexityBot: `361f2ec2-c66f-4c70-9da0-3cf5be383658-1783249098`

Ejemplos de request IDs con `200` en home:

- Chrome: `ddfa00fd-800d-43c0-ac9a-60400d2cb095-1783249038`
- Chrome: `9470c793-c7b2-4999-8126-d6c21233c408-1783249041`
- Googlebot: `111082d8-d668-4278-87ce-4006ed144197-1783249053`

## Interpretación

`VERIFICADO PERO MEJORABLE`

No hay evidencia de bloqueo global por `robots.txt`, ni bloqueo total de bots en CDN/WAF.

Sí hay evidencia de un problema grave de disponibilidad/renderizado en la home, visible con bots y también con navegador normal. Por tanto:

- No debe resolverse tocando `robots.txt`.
- No debe resolverse bloqueando o permitiendo user-agents concretos.
- No debe resolverse con IndexNow.
- No debe resolverse con cambios editoriales.
- Debe tratarse como incidencia de Shopify storefront/render/CDN o posible interacción de app/theme en la home.

## Riesgo SEO/GEO/AEO

`RIESGO CRITICO`

La home es una URL estratégica para:

- descubrimiento de marca;
- rastreo inicial;
- autoridad de entidad;
- buscadores generales;
- Bing/Copilot;
- ChatGPT Search;
- Perplexity/Comet;
- Claude Search;
- Applebot.

Si los bots reciben `500` de forma intermitente, se reduce la fiabilidad de rastreo y citabilidad, aunque páginas internas respondan correctamente.

## Relación con fuentes oficiales

`VERIFICADO Y CORRECTO`

- OpenAI recomienda permitir OAI-SearchBot y las solicitudes desde rangos IP publicados para aparecer en ChatGPT Search.
- Perplexity recomienda permitir PerplexityBot/Perplexity-User y combinar user-agent con rangos IP oficiales cuando exista WAF.
- Anthropic separa bots de entrenamiento, búsqueda y acceso iniciado por usuario.
- Google indica que la elegibilidad para funciones IA requiere SEO normal, rastreo permitido y que CDN/hosting no bloqueen.
- Bing advierte que `NOARCHIVE`/`NOCACHE` pueden limitar inclusión/citas en Bing Chat/Copilot.

Este diagnóstico confirma que la capa prioritaria ahora no es `robots.txt`, sino estabilidad de renderizado de la home.

## Acciones ejecutadas

`VERIFICADO Y CORRECTO`

Solo lectura:

- Peticiones HTTP públicas controladas.
- Comparación por URL y user-agent.
- Captura de códigos de estado.
- Captura de tamaños de respuesta.
- Captura de request IDs en errores `500`.
- Registro documental.

No se ejecutó:

- Escritura en Shopify.
- Cambios en tema.
- Cambios en `robots.txt`.
- Cambios en `llms.txt` o `agents.md`.
- Cambios en Bing.
- Cambios en IndexNow.
- Cambios en CDN/WAF.

## Estado final

`VERIFICADO PERO MEJORABLE`

Subestado:

- Archivos técnicos: `VERIFICADO Y CORRECTO`
- Páginas internas probadas: `VERIFICADO Y CORRECTO`
- Home: `RIESGO CRITICO`
- Validación IP real de bots: `NO ACCESIBLE`

## Próximo lote recomendado

`MW-CRAWLERS-HOME-500-SHOPIFY-INFRA-EVIDENCE-013F1`

Objetivo: preparar paquete quirúrgico para Shopify Support/infraestructura con request IDs, patrón de fallo y alcance exacto: home `https://www.matchwalls.com/` devuelve `500` intermitente para bots y navegador.

Alternativa si se quiere investigar desde tema antes de soporte:

`MW-HOME-RENDER-500-THEME-APP-DIAG-013F2`

Objetivo: diagnosticar en solo lectura si la home tiene secciones/apps/scripts que puedan provocar error de renderizado intermitente.

