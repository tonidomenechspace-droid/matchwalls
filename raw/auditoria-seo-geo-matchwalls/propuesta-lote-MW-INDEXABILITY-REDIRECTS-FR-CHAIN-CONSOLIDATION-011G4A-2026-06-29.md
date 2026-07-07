# Propuesta de lote: MW-INDEXABILITY-REDIRECTS-FR-CHAIN-CONSOLIDATION-011G4A

Fecha: 2026-06-29  
Estado: REQUIERE DECISION HUMANA  
Tipo: propuesta de escritura acotada en Shopify Admin  

## 1. Alcance exacto propuesto

Actualizar exclusivamente 12 redirects FR que hoy hacen cadena `301 -> 301 -> 200`, cambiando su target actual por el destino final 200 ya verificado.

No se propone:

- Eliminar redirects.
- Crear redirects.
- Cambiar handles.
- Renombrar colecciones.
- Modificar contenido visible.
- Modificar sitemap.
- Modificar canonicals.
- Modificar tema Shopify.
- Tocar EN, AR, ES, DE, NL, IT o PT.
- Tocar el caso FR que termina en 404.

## 2. Estado real comprobado

Diagnostico previo:

- `MW-INDEXABILITY-REDIRECTS-FR-CHAINS-DIAG-011G4`

Estado actual:

- Total redirects Shopify: 614 EXACT.
- FR: 23 redirects.
- 12 redirects FR hacen `301 -> 301 -> 200`.
- 1 redirect FR termina en `404` y queda excluido.
- 10 redirects FR hacen `301 -> 200` y quedan sin cambios.

## 3. Recursos afectados y valores propuestos

| ID Shopify | Path | Target actual | Target propuesto |
|---|---|---|---|
| `gid://shopify/UrlRedirect/417580974307` | `/fr/collections/floral-painted-papers-matchwallswallspapers` | `/fr/collections/floral-murals-matchwallsmurals` | `/fr/collections/peintures-murales-florales-matchwallsmurals` |
| `gid://shopify/UrlRedirect/417581007075` | `/fr/collections/painted-papers-graphic-matchwallswallpapers-1` | `/fr/collections/graphical-murals-matchwallsmurals` | `/fr/collections/peintures-murales-graphiques-matchwallsmurals` |
| `gid://shopify/UrlRedirect/417581039843` | `/fr/collections/geometric-paints-matchwalswallpapers` | `/fr/collections/geometric-murals-matchwallsmurs` | `/fr/collections/peintures-murales-geometriques-matchwallsmurs` |
| `gid://shopify/UrlRedirect/417581072611` | `/fr/collections/nature-painted-papers-matchwallswallpapers` | `/fr/collections/nature-murals-matchwallsmurals` | `/fr/collections/peintures-murales-de-la-nature-matchwallsmurals` |
| `gid://shopify/UrlRedirect/417581105379` | `/fr/collections/wall-paper-matchwallswallpapers` | `/fr/collections/rays-mural-matchwallsmurals-1` | `/fr/collections/rayons-muraux-matchwallsmurals` |
| `gid://shopify/UrlRedirect/417581138147` | `/fr/collections/japanese-painted-papers-matchwallswallpapers` | `/fr/collections/japanese-murals-matchwallsmurals` | `/fr/collections/peintures-murales-japonaises-matchwallsmurals` |
| `gid://shopify/UrlRedirect/417581170915` | `/fr/collections/painted-papeles-marble-matchwallswallpa` | `/fr/collections/mural-mural-matchwallsmurals` | `/fr/collections/murale-murale-matchwallsmurals` |
| `gid://shopify/UrlRedirect/417581236451` | `/fr/collections/painted-papers-matchwallswallpapers` | `/fr/collections/murals-for-the-matchwallsmurals-room` | `/fr/collections/peintures-murales-pour-la-salle-matchwallsmurals` |
| `gid://shopify/UrlRedirect/417581269219` | `/fr/collections/painted-dining-papers-matchwallswallpapers` | `/fr/collections/mural-for-the-matchwallsmurals-dining-room` | `/fr/collections/murale-pour-la-salle-a-manger-matchwallsmurals` |
| `gid://shopify/UrlRedirect/417581301987` | `/fr/collections/painted-papers-kitchen-matchwallswallpapers` | `/fr/collections/kitchen-murals-matchwallsmurals` | `/fr/collections/mindicules-de-cuisine-matchwallsmurals` |
| `gid://shopify/UrlRedirect/417581334755` | `/fr/collections/bedroom-painted-papers-matchwallswallpa` | `/fr/collections/bedroom-murals-matchwallsmurals` | `/fr/collections/peintures-murales-de-chambre-matchwallsmurals` |
| `gid://shopify/UrlRedirect/417581400291` | `/fr/collections/painted-adolescents-matchwallswallpapers` | `/fr/collections/mural-for-teenage-rooms-matchwallsmurals` | `/fr/collections/peinture-murale-pour-les-salles-dadolescents-matchwallsmurals` |

## 4. Recursos excluidos expresamente

FR 404 excluido:

- `gid://shopify/UrlRedirect/417581367523`
- `/fr/collections/painted-papers-baller-matchwallswallpapers`
- `/fr/collections/mural-murals-matchwallsmurals`
- Motivo: termina en 404; requiere decision separada, no consolidacion automatica.

EN:

- 2 redirects verificados como `301 -> 200`, sin accion.

AR:

- 4 redirects quedan en STANDBY por estar fuera de idiomas prioritarios actuales.

## 5. Evidencia

Archivos:

- `diagnostico-MW-INDEXABILITY-REDIRECTS-FR-CHAINS-DIAG-011G4-2026-06-29.md`
- `admin-fr-en-ar-MW-INDEXABILITY-REDIRECTS-FR-CHAINS-DIAG-011G4-2026-06-29.csv`
- `qa-publico-fr-en-ar-MW-INDEXABILITY-REDIRECTS-FR-CHAINS-DIAG-011G4-2026-06-29.csv`
- `qa-sitemap-fr-MW-INDEXABILITY-REDIRECTS-FR-CHAINS-DIAG-011G4-2026-06-29.csv`
- `clasificacion-MW-INDEXABILITY-REDIRECTS-FR-CHAINS-DIAG-011G4-2026-06-29.csv`
- `backup-pre-MW-INDEXABILITY-REDIRECTS-FR-CHAIN-CONSOLIDATION-011G4A-2026-06-29.csv`
- `propuesta-valores-MW-INDEXABILITY-REDIRECTS-FR-CHAIN-CONSOLIDATION-011G4A-2026-06-29.csv`

## 6. Motivo tecnico

La web ya resuelve estas 12 URLs antiguas hacia paginas finales 200, pero con dos saltos. La consolidacion propuesta mantiene la misma fuente antigua y apunta directamente al destino final actual.

Efecto esperado:

- Antes: `old FR URL -> target intermedio -> final 200`.
- Despues: `old FR URL -> final 200`.

## 7. Riesgos y efectos secundarios

Riesgo principal:

- Se cambia el target almacenado de 12 redirects, por lo que una configuracion incorrecta podria romper una URL antigua.

Control:

- Cada destino propuesto ya fue verificado como final 200 en la web publica.
- No se tocan handles ni colecciones.
- No se elimina ningun redirect.
- Hay backup de valores actuales.

Nota linguistica:

- Algunos handles finales FR pueden ser mejorables linguisticamente, por ejemplo `/fr/collections/mindicules-de-cuisine-matchwallsmurals`.
- Este lote no corrige nombres ni handles. Solo reduce cadenas existentes hacia el destino que la web ya usa hoy.

## 8. Respaldo disponible

Archivo:

- `backup-pre-MW-INDEXABILITY-REDIRECTS-FR-CHAIN-CONSOLIDATION-011G4A-2026-06-29.csv`

Contiene:

- ID.
- Path.
- Target actual.

## 9. Metodo exacto de ejecucion si se aprueba

Mutacion validada contra schema Shopify:

`urlRedirectUpdate(id: ID!, urlRedirect: UrlRedirectInput!)`

Para cada redirect:

- Mantener `path`.
- Sustituir `target` por el `proposed_target`.
- Ejecutar de uno en uno.
- Detener ante cualquier `userErrors`.

## 10. Metodo exacto de reversion

Usar `urlRedirectUpdate` con:

- Mismo `id`.
- Mismo `path`.
- `target` restaurado desde `backup-pre-MW-INDEXABILITY-REDIRECTS-FR-CHAIN-CONSOLIDATION-011G4A-2026-06-29.csv`.

## 11. Pruebas posteriores obligatorias

Admin:

- Confirmar que los 12 IDs siguen existiendo.
- Confirmar que los 12 `target` coinciden con `proposed_target`.
- Confirmar que el total de redirects sigue en 614, salvo cambios externos simultaneos.
- Confirmar que el FR 404 excluido sigue intacto.

Publico:

- Verificar 12/12 fuentes como `301 -> 200`.
- Confirmar 0 cadenas de mas de un salto en el lote.
- Confirmar 0 destinos 404 en el lote.

Sitemap:

- Verificar que las fuentes, targets anteriores y targets nuevos no generan exposicion inesperada en sitemap.

Registro:

- Actualizar `registro-cambios-ejecutados.md`.

## 12. Frase exacta necesaria para ejecutar

Para autorizar la escritura en Shopify, Daniel debe responder exactamente:

`APROBADO LOTE MW-INDEXABILITY-REDIRECTS-FR-CHAIN-CONSOLIDATION-011G4A`

