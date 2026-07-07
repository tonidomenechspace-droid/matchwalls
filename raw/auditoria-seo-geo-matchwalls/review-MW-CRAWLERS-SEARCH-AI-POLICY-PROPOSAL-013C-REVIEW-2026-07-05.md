# MW-CRAWLERS-SEARCH-AI-POLICY-PROPOSAL-013C-REVIEW

Fecha: 2026-07-05  
Hora de registro: 12:37 Europe/Madrid  
Modo: solo lectura  
Estado final: `VERIFICADO Y CORRECTO`

## Objetivo

Revisar la propuesta `MW-CRAWLERS-SEARCH-AI-POLICY-PROPOSAL-013C` con el estado actualizado del proyecto:

- Bing Webmaster Tools ya está verificado para `matchwalls.com/`.
- El sitemap está reconocido por Bing.
- La app IndexNow está instalada y enviando URLs.
- Existen datos iniciales de Bing AI Performance.
- `robots.txt`, `sitemap.xml`, `llms.txt` y `agents.md` son accesibles públicamente.

Esta revisión no ejecuta cambios. Solo consolida política, riesgos y próximos lotes seguros.

## Documentos y evidencias revisadas

`VERIFICADO Y CORRECTO`

Documentos locales revisados:

- `registro-cambios-ejecutados.md`
- `diagnostico-MW-CRAWLERS-BING-COPILOT-AI-ROBOTS-DIAG-013B-2026-07-04.md`
- `propuesta-MW-CRAWLERS-SEARCH-AI-POLICY-PROPOSAL-013C-2026-07-04.md`
- Registros IndexNow/Bing recientes `013D`, `013E`, `013I`
- Archivos públicos capturados en `work-MW-CRAWLERS-SEARCH-AI-POLICY-PROPOSAL-013C-REVIEW`

Fuentes oficiales consultadas:

- OpenAI crawlers: `https://developers.openai.com/api/docs/bots`
- Anthropic crawlers: `https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler`
- Perplexity crawlers: `https://docs.perplexity.ai/docs/resources/perplexity-crawlers`
- Google AI features: `https://developers.google.com/search/docs/appearance/ai-features`
- Google common crawlers / Google-Extended: `https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers`
- Applebot: `https://support.apple.com/en-us/119829`
- Bing Chat / Copilot controls: `https://blogs.bing.com/webmaster/september-2023/Announcing-new-options-for-webmasters-to-control-usage-of-their-content-in-Bing-Chat`
- Yahoo submission via Bing: `https://help.yahoo.com/kb/SLN2217.html`
- IndexNow: `https://www.indexnow.org/documentation`

## Estado real comprobado

`VERIFICADO Y CORRECTO`

Lectura pública actual:

- `https://www.matchwalls.com/robots.txt`: `200 OK`
- `https://www.matchwalls.com/sitemap.xml`: `200 OK`
- `https://www.matchwalls.com/llms.txt`: `200 OK`
- `https://www.matchwalls.com/agents.md`: `200 OK`

Estado de `robots.txt`:

- Grupo general: `User-agent: *`
- Grupo específico: `User-agent: adsbot-google`
- Contenido público permitido por herencia general.
- Bloqueos privados/transaccionales presentes: checkout, cart, account, orders, endpoints internos, combinaciones de filtros, previews y trampas de rastreo.
- No hay grupos explícitos para bots IA.

Estado de `llms.txt` y `agents.md`:

- Accesibles.
- Contienen instrucciones de agente/UCP de Shopify.
- Son útiles para compatibilidad de agentes comerciales.
- No sustituyen contenido SEO/GEO factual, entidades, landings, schema ni páginas citables.

## Conclusión de política

`VERIFICADO Y CORRECTO`

La política recomendada en `013C` se mantiene, con actualización de contexto:

1. No modificar `robots.txt` ahora.
2. Mantener una política de visibilidad primero para buscadores y sistemas de cita.
3. No añadir grupos explícitos `Allow: /` para bots IA si no se duplican todos los bloqueos privados.
4. No aplicar `NOARCHIVE` ni `NOCACHE` globalmente.
5. Mantener `noindex` solo en URLs técnicas, sin valor o ya decididas por lote.
6. Separar bots de búsqueda/cita de bots de entrenamiento.
7. No inventar user-agents ni reglas para plataformas sin documentación oficial accesible.

## Motivo técnico principal

`VERIFICADO Y CORRECTO`

El estado actual ya permite el rastreo público mediante `User-agent: *`.

Añadir grupos específicos para bots IA con solo:

```txt
User-agent: OAI-SearchBot
Allow: /
```

podría ser peor que no hacer nada, porque algunos rastreadores aplican el grupo más específico y podrían dejar de heredar los bloqueos privados del grupo general.

Si algún día se añade un grupo específico, debe duplicar también los `Disallow` privados/transaccionales. Por tanto, hoy el camino más seguro es no tocar `robots.txt`.

## Matriz de decisión resumida

| Plataforma / bot | Estado recomendado | Clasificación |
|---|---:|---|
| Google Search / Googlebot | Permitido por `User-agent: *` | `VERIFICADO Y CORRECTO` |
| Bing Search / Bingbot / Copilot / Yahoo / Edge | Permitido por `User-agent: *`; Bing verificado | `VERIFICADO Y CORRECTO` |
| OAI-SearchBot | Permitido por `User-agent: *` | `VERIFICADO Y CORRECTO` |
| ChatGPT-User | No bloquear; user-initiated | `VERIFICADO Y CORRECTO` |
| Claude-SearchBot / Claude-User | Permitido por `User-agent: *` | `VERIFICADO Y CORRECTO` |
| PerplexityBot / Perplexity-User / Comet | Permitido por `User-agent: *` | `VERIFICADO Y CORRECTO` |
| Applebot | Permitido por `User-agent: *` | `VERIFICADO Y CORRECTO` |
| Google-Extended | No bloquear por ahora; decisión separada de entrenamiento | `REQUIERE DECISION HUMANA` |
| GPTBot | No bloquear por ahora; decisión separada de entrenamiento | `REQUIERE DECISION HUMANA` |
| ClaudeBot | No bloquear por ahora; decisión separada de entrenamiento | `REQUIERE DECISION HUMANA` |
| Applebot-Extended | No bloquear por ahora; decisión separada de entrenamiento | `REQUIERE DECISION HUMANA` |
| Meta crawlers IA | Fuente oficial no completamente accesible en esta revisión | `DECLARADO PERO NO VERIFICADO` |
| Grok / xAI crawler | Sin fuente oficial verificada | `NO ACCESIBLE` |
| Ollama | No es crawler público; sin acción robots | `VERIFICADO Y CORRECTO` |

## Bots de entrenamiento: decisión pendiente

`REQUIERE DECISION HUMANA`

Para el objetivo declarado de MatchWalls —maximizar impresiones, comprensión, citabilidad y presencia en buscadores e IA— la recomendación operativa es:

- No bloquear bots de entrenamiento todavía.
- No mezclar esa decisión con el lote de rastreo/citación.
- Tratarlo como decisión legal, reputacional, de propiedad intelectual y estrategia de datos.

Si Daniel decide separar claramente “cita sí, entrenamiento no”, debe abrirse un lote específico:

`MW-CRAWLERS-AI-TRAINING-OPT-OUT-DECISION-013C2`

Ese lote deberá presentar reglas exactas, efectos esperados y riesgo de pérdida de visibilidad indirecta.

## Bing, Copilot, Edge y Yahoo

`VERIFICADO Y CORRECTO`

Bing Webmaster Tools está activo para `matchwalls.com/` y el sitemap fue importado correctamente desde Google Search Console. Yahoo se apoya en Bing Webmaster Tools para envío de sitios. Edge/Copilot quedan cubiertos por la capa Bing, no por una optimización independiente de navegador.

Acciones ya encaminadas:

- Sitemap reconocido por Bing.
- IndexNow instalado mediante app.
- Envíos visibles en Bing Webmaster Tools.
- Datos iniciales de AI Performance disponibles.

Pendiente:

- Resolver discrepancia visual de IndexNow: `Submitted URLs = 13` frente a tabla/export de 3 URLs.
- Monitorizar recepción durante 24-72 horas con nuevos eventos reales.

## Google, Gemini y Chrome

`VERIFICADO Y CORRECTO`

Google indica que las funciones de IA en Search no requieren archivos especiales para IA ni schema exclusivo. La prioridad sigue siendo:

- contenido textual visible;
- indexabilidad;
- enlaces internos;
- experiencia de página;
- structured data coherente con contenido visible.

Chrome no requiere SEO propio. Es navegador. La prioridad para navegadores es compatibilidad técnica, accesibilidad, rendimiento y HTML rastreable.

## ChatGPT, Claude, Perplexity y Comet

`VERIFICADO Y CORRECTO`

El enfoque correcto es permitir rastreo de búsqueda/citación y construir contenido factual, claro y citable. Los bots de búsqueda/cita quedan permitidos por la regla general actual.

Comet queda tratado como capa Perplexity.

## Meta, Grok y Ollama

`VERIFICADO PERO MEJORABLE`

Meta:

- Existe documentación oficial de Meta sobre web crawlers, pero el contenido completo no fue accesible de forma fiable en esta revisión.
- No se recomienda añadir reglas hasta verificar documentación oficial completa.

Grok / xAI:

- No se ha verificado una fuente oficial estable de user-agent o política robots.
- No se deben inventar reglas.

Ollama:

- No es un buscador/crawler público.
- No requiere acción en `robots.txt`.

## Riesgos detectados

`VERIFICADO PERO MEJORABLE`

1. **Riesgo de grupos específicos mal definidos**  
   Añadir `User-agent` IA con solo `Allow: /` puede saltarse bloqueos privados.

2. **Riesgo de `NOARCHIVE` / `NOCACHE`**  
   Bing advierte que estos controles pueden limitar respuestas/citas en Bing Chat/Copilot.

3. **Riesgo WAF/CDN**  
   En una captura técnica con user-agent no estándar se obtuvo una respuesta genérica de error Shopify, mientras que con user-agent navegador normal los archivos respondieron correctamente. Conviene auditar WAF/CDN/bot filtering antes de optimizar bots.

4. **Riesgo de falsa seguridad con `llms.txt`**  
   El archivo existe, pero es una instrucción UCP/Shopify; no sustituye contenidos citables, entidad factual ni schema.

5. **Riesgo de plataformas sin fuente oficial**  
   No deben añadirse reglas para Grok/xAI u otros bots sin documentación verificable.

## Acciones ejecutadas

`VERIFICADO Y CORRECTO`

Solo lectura:

- Lectura de registros locales.
- Lectura de propuesta `013C`.
- Lectura pública de `robots.txt`, `sitemap.xml`, `llms.txt`, `agents.md`.
- Consulta de documentación oficial de crawlers/buscadores.
- Consolidación de matriz de política.

No se ha modificado:

- Shopify.
- Tema MAIN o draft.
- `robots.txt`.
- `llms.txt`.
- `agents.md`.
- Bing Webmaster Tools.
- IndexNow.
- Sitemap.
- URLs, handles, canonicals, redirecciones.
- Traducciones.
- App embeds.

## Resultado final

`VERIFICADO Y CORRECTO`

El lote `MW-CRAWLERS-SEARCH-AI-POLICY-PROPOSAL-013C-REVIEW` queda cerrado como revisión.

Decisión vigente:

- Mantener `robots.txt` actual.
- Mantener visibilidad para buscadores e IA de búsqueda/citación.
- No bloquear entrenamiento por defecto sin decisión humana.
- No añadir user-agents IA explícitos todavía.
- Seguir trabajando la elegibilidad real mediante contenido, indexabilidad, enlaces, schema, rendimiento y señales de confianza.

## Próximos lotes recomendados

### 1. `MW-CRAWLERS-WAF-CDN-BOT-ALLOWLIST-DIAG-013F`

Objetivo: verificar si Shopify/CDN/WAF/app de seguridad está bloqueando o alterando respuestas para bots legítimos: OpenAI, Anthropic, Perplexity, Bing, Google y Apple.

Tipo: solo lectura.  
Prioridad: alta.

### 2. `MW-CRAWLERS-AI-FILES-LLMS-AGENTS-FACTUAL-DIAG-013C1`

Objetivo: determinar si `llms.txt` y `agents.md` pueden o deben reforzarse con información factual de MatchWalls o si Shopify controla su contenido.

Tipo: diagnóstico.  
Prioridad: media.

### 3. `MW-BING-WEBMASTER-SEARCH-PERFORMANCE-BASELINE-013J`

Objetivo: registrar línea base Bing: impresiones, clics, CTR, keywords, páginas y AI Performance para panel CEO/CMO.

Tipo: solo lectura.  
Prioridad: alta.

### 4. `MW-CRAWLERS-AI-TRAINING-OPT-OUT-DECISION-013C2`

Objetivo: decidir si se bloquean o no bots de entrenamiento, separando búsqueda/citación de entrenamiento.

Tipo: decisión humana.  
Prioridad: media, solo si Daniel quiere tratar propiedad intelectual/datos.

