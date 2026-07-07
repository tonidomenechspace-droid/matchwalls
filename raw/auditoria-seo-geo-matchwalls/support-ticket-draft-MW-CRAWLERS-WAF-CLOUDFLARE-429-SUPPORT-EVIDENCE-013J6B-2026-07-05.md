# Borrador de mensaje de soporte - MW-CRAWLERS-WAF-CLOUDFLARE-429-SUPPORT-EVIDENCE-013J6B

Asunto sugerido:

`Intermittent/consistent Cloudflare 429 during controlled SEO crawler QA on matchwalls.com priority URLs`

Mensaje sugerido:

Hola,

Estamos realizando una auditoría SEO/GEO controlada de `https://www.matchwalls.com/` sobre URLs prioritarias detectadas en Bing Webmaster Tools.

Durante el lote de QA `MW-BING-SEO-GEO-PRIORITY-URL-PUBLIC-QA-013J6`, nuestro entorno recibió respuestas `429` de Cloudflare que impidieron completar la revisión HTML de varias URLs públicas.

Resumen de evidencia:

- 42 URLs priorizadas revisadas.
- 6 URLs respondieron `200` con user-agent browser-like y pasaron checks básicos de página.
- 36 URLs devolvieron `429` con user-agent browser-like.
- 42/42 URLs devolvieron `429` con user-agent Bingbot-like de prueba.
- Un mini recheck lento tras cooldown devolvió `429` en 3/3 URLs.
- En las respuestas `429` el servidor observado fue `cloudflare`.
- No vimos `x-request-id` de Shopify ni headers de render Shopify en esas respuestas `429`.

Interpretación:

No estamos afirmando que Bingbot real esté bloqueado, porque no hemos validado IPs oficiales ni logs internos. Tampoco estamos afirmando que las páginas afectadas estén mal a nivel SEO/editorial. Lo que necesitamos aclarar es si alguna regla WAF/rate-limit/bot-score/CDN puede estar bloqueando QA crawler controlado o user-agents crawler-like antes de llegar a Shopify/render HTML.

Preguntas:

1. ¿Existe alguna regla WAF, rate-limit, bot protection o CDN que pueda devolver `429` a user-agents crawler-like o a varias solicitudes SEO QA en poco tiempo?
2. ¿Podéis confirmar si los bots oficiales de búsqueda, especialmente Bingbot, se validan por IP oficial y no solo por user-agent?
3. ¿Existe una forma segura de permitir QA SEO controlado sin reducir la seguridad general de la tienda?
4. ¿Conviene revisar allowlist/rate-limit para bots oficiales: Bingbot, Googlebot, OAI-SearchBot, ChatGPT-User, Claude-SearchBot, PerplexityBot y Applebot/Safari crawler, siempre validando IP oficial cuando aplique?
5. ¿Debemos pausar nuevos crawls automatizados hasta que se revise esta capa?

Restricciones:

Por favor, no cambiéis contenido, tema, URLs, handles, redirecciones, traducciones, mercados, SEO fields, robots, sitemap, schema, apps ni configuración de IndexNow sin confirmación previa.

Archivos de evidencia disponibles:

- `public-url-qa-final-MW-BING-SEO-GEO-PRIORITY-URL-PUBLIC-QA-013J6-2026-07-05.csv`
- `crawler-access-risk-MW-BING-SEO-GEO-PRIORITY-URL-PUBLIC-QA-013J6-2026-07-05.csv`
- `summary-final-MW-BING-SEO-GEO-PRIORITY-URL-PUBLIC-QA-013J6-2026-07-05.csv`
- `support-evidence-MW-CRAWLERS-WAF-CLOUDFLARE-429-SUPPORT-EVIDENCE-013J6B-2026-07-05.md`

Gracias.
