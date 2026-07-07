# Propuesta formal - MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-NATIVE-BASE-PILOT-012J3

Fecha: 2026-07-04  
Tipo: piloto controlado de escritura SEO nativa en Shopify Pages.  
Estado: `REQUIERE DECISION HUMANA`  
Cambios Shopify: no ejecutados.  
Cambios LangShop: no.  
Cambios Shopify Translate: no.

## 1. Documentos leidos

- `resultado-MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-NATIVE-MANUAL-CHECK-012J2A-2026-07-04.md`
- `diagnostico-MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-SOURCE-DIAG-012J2-2026-07-04.md`
- `seo-meta-copy-MW-GEO-LANDINGS-I18N-SEO-META-COPY-012I1-2026-07-03.md`
- `registro-cambios-ejecutados.md`

## 2. Estado real comprobado

Pagina base ES:

- Shopify Page GID historico: `gid://shopify/Page/687276622200`
- Admin nativo: `admin.shopify.com/store/matchwalls/pages/687276622200`
- URL publica: `https://www.matchwalls.com/pages/papel-pintado-espana`
- Handle: `papel-pintado-espana`

Valores actuales verificados en 012J2A:

- `Titulo de la pagina`: `Papel pintado en España para hogares y proyectos profesionales`
- `Metadescripcion`: `VACIO`
- `Identificador de URL`: `pages/papel-pintado-espana`

Estado actual:

- Campos SEO nativos visibles: `VERIFICADO Y CORRECTO`
- Metadescripcion ES nativa vacia: `VERIFICADO PERO MEJORABLE`
- HTML publico ES con meta autogenerada desde body: `VERIFICADO PERO MEJORABLE`

## 3. Alcance exacto propuesto

Editar manualmente en Shopify Admin nativo solo:

- Recurso: pagina `papel-pintado-espana`
- Campo: `Metadescripcion`
- Idioma/capa: ES base nativa

No modificar:

- Titulo de la pagina SEO.
- Titulo/H1 de la pagina.
- Body/contenido.
- URL handle.
- Canonical.
- Hreflang.
- LangShop.
- Shopify Translate.
- Pagina Francia.
- Idiomas FR/EN/DE/NL.
- Tema Shopify.

## 4. Valor actual

Campo `Metadescripcion`:

`VACIO`

## 5. Valor propuesto

Campo `Metadescripcion`:

`Papel pintado, murales y soluciones a medida para viviendas y proyectos profesionales en España. Pide muestras y personaliza tu mural.`

Longitud aproximada: 134 caracteres.

## 6. Motivo tecnico y SEO/GEO

El campo nativo vacio provoca que Shopify genere una meta description publica larga desde el contenido visible. Completar la metadescripcion base ES permite:

- dar una descripcion clara y controlada a buscadores;
- mejorar el snippet potencial de la landing de España;
- evitar una descripcion autogenerada excesivamente larga;
- probar si Shopify publica correctamente el campo SEO nativo antes de escalar.

No se afirma ni se garantiza mejora de ranking, indexacion, trafico o cita por IA.

## 7. Riesgos

- La escritura afecta la pagina publica ES.
- Si se toca accidentalmente el handle, se abriria riesgo critico de URL/redireccion. Por eso el handle queda prohibido.
- Si Shopify guarda otros campos modificados accidentalmente, podria alterar title/body. Por eso solo se debe tocar la metadescripcion.
- Puede tardar unos minutos en verse reflejado publicamente.
- No resuelve automaticamente las metas traducidas FR/EN/DE/NL; eso queda para lote posterior, porque LangShop SEO meta fallo en 012J1B.

## 8. Respaldo disponible

Valores previos:

- `Titulo de la pagina`: `Papel pintado en España para hogares y proyectos profesionales`
- `Metadescripcion`: `VACIO`
- `Identificador de URL`: `pages/papel-pintado-espana`

Evidencia de respaldo:

- `evidencias/captura-012J2A-shopify-nativo-espana-seo-fields-2026-07-04.png`
- `resultado-MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-NATIVE-MANUAL-CHECK-012J2A-2026-07-04.md`

## 9. Metodo exacto de reversion

Si el resultado no es correcto:

1. Volver a Shopify Admin nativo > `Tienda online` > `Paginas` > `papel-pintado-espana`.
2. Abrir `Publicacion en motores de busqueda`.
3. Borrar solo el campo `Metadescripcion`.
4. Confirmar que queda `VACIO`.
5. No tocar `Titulo de la pagina` ni `Identificador de URL`.
6. Guardar.
7. Repetir QA publico.

## 10. Pruebas posteriores obligatorias

Tras guardar, verificar:

- Admin nativo:
  - `Metadescripcion` contiene exactamente el valor propuesto.
  - `Titulo de la pagina` no ha cambiado.
  - `Identificador de URL` sigue siendo `pages/papel-pintado-espana`.
- Publico ES:
  - HTTP 200.
  - `<title>` no cambia inesperadamente.
  - `<meta name="description">` muestra el valor propuesto o, si Shopify tarda, queda documentado como pendiente de propagacion.
  - canonical propio.
  - sin `noindex`.
  - H1 correcto.
  - hreflang presente.

## 11. Criterio de salida

`CORREGIDO Y VERIFICADO` si:

- el campo se guarda en Shopify nativo;
- el HTML publico ES muestra la meta description propuesta;
- URL/title/body permanecen intactos.

`INCORRECTO` si:

- Shopify no guarda el campo;
- el HTML publico no cambia tras espera razonable;
- cambia cualquier campo fuera de alcance.

`REQUIERE DECISION HUMANA` si:

- aparece advertencia inesperada de Shopify;
- el campo no se puede guardar;
- el valor afecta negativamente a traducciones o URLs.

## 12. Aprobacion necesaria

Para ejecutar este lote, Daniel debe responder exactamente:

`APROBADO LOTE MW-GEO-LANDINGS-SHOPIFY-PAGE-SEO-NATIVE-BASE-PILOT-012J3`

