# MW-INDEXNOW-APP-I18N-LANGUAGES-DECISION-013I2

Fecha: 2026-07-05  
Modo: solo lectura / decisión.  
Estado final: `REQUIERE DECISION HUMANA`.

## Documentos leídos

`VERIFICADO Y CORRECTO`

- `settings-logs-MW-INDEXNOW-APP-POSTINSTALL-SETTINGS-LOGS-QA-013I1-2026-07-05.md`
- `settings-state-MW-INDEXNOW-APP-POSTINSTALL-SETTINGS-LOGS-QA-013I1-2026-07-05.csv`
- `postinstall-MW-INDEXNOW-APP-PILOT-INSTALL-CONFIG-013I-STORESpark-PREMIUM-2026-07-05.md`
- `preflight-MW-INDEXNOW-APP-PILOT-INSTALL-CONFIG-013I-2026-07-05.md`
- `registro-cambios-ejecutados.md`

## Estado real comprobado

`VERIFICADO PERO MEJORABLE`

Pantalla actual:

- `https://admin.shopify.com/store/matchwalls/apps/indexnow-18/plans`
- Título: `Matchwalls · IndexNow · Shopify`
- Resultado visible en iframe: `404 Not Found`

Conclusión: la pantalla de planes no permite verificar el plan mensual desde esa ruta. El plan mensual queda como `DECLARADO PERO NO VERIFICADO` por confirmación de Daniel, pendiente de comprobar en Shopify Admin > Facturación.

## Estado de idiomas heredado de 013I1

`VERIFICADO PERO MEJORABLE`

Idiomas prioritarios MatchWalls:

- ES / Spanish default: activo.
- EN / English: inactivo.
- FR / French: inactivo.
- DE / German: inactivo.
- NL / Dutch: inactivo.

Idiomas no prioritarios:

- IT / Italian: inactivo.
- PT-PT / European Portuguese: inactivo.
- Otros idiomas: inactivos.

## Decisión SEO/GEO

`REQUIERE DECISION HUMANA`

Para la estrategia SEO/GEO/AEO de MatchWalls, la app IndexNow debería cubrir los cinco idiomas prioritarios:

- ES
- EN
- FR
- DE
- NL

Sin embargo, activar EN/FR/DE/NL es una escritura en una app externa y puede afectar envíos automáticos. No debe hacerse dentro de este lote de decisión.

## Riesgo principal

`VERIFICADO PERO MEJORABLE`

La app tiene auto-submit activo para:

- Products
- Collections
- Pages
- Blog posts

No se ha verificado si activar un idioma:

1. solo afecta a cambios futuros;
2. genera envíos retroactivos de URLs existentes;
3. envía automáticamente todas las variantes traducidas;
4. permite excluir muestras noindex, URLs de prueba, IT/PT o URLs sin valor.

## Decisión recomendada

`REQUIERE DECISION HUMANA`

Activar EN, FR, DE y NL, pero solo en un lote controlado con estas condiciones:

1. No tocar IT ni PT-PT.
2. No tocar otros idiomas.
3. No usar Manual submissions.
4. No usar bulk submit / submit all / sync all.
5. Tras activar, revisar logs inmediatamente.
6. Si aparecen envíos masivos no controlados, revertir desactivando EN/FR/DE/NL y registrar incidencia.

## Próximo lote recomendado

`MW-INDEXNOW-APP-I18N-LANGUAGES-ACTIVATION-013I3`

Alcance propuesto:

- Activar solo:
  - English
  - French
  - German
  - Dutch
- Mantener activos:
  - Spanish default
- Mantener inactivos:
  - Italian
  - European Portuguese
  - resto de idiomas
- No tocar:
  - Products
  - Collections
  - Pages
  - Blog posts
  - API Key
  - Manual submissions
  - Pricing

Texto de aprobación requerido:

`APROBADO LOTE MW-INDEXNOW-APP-I18N-LANGUAGES-ACTIVATION-013I3`

## Pruebas posteriores del lote 013I3

`VERIFICADO Y CORRECTO`

Tras activar:

1. Verificar en Settings que ES, EN, FR, DE y NL están activos.
2. Verificar que IT/PT y otros idiomas siguen inactivos.
3. Verificar logs de la app.
4. Confirmar si se generaron envíos nuevos.
5. Si se generaron envíos nuevos, registrar URL, idioma, evento, hora y estado.
6. No enviar manualmente URLs todavía.

## Exclusiones respetadas en 013I2

`VERIFICADO Y CORRECTO`

No se modificó la app. No se pulsó Save, Discard, Manual submissions, Pricing actions, toggles de idiomas ni tipos de contenido.
