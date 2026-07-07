# Propuesta de lote — MW-TECH-PRODUCT-FILEINPUT-GUARD-010A3

Estado: `VERIFICADO PERO MEJORABLE`.

Este lote corrige una segunda excepción nula del producto en el tema auxiliar.
**No publica ni modifica el MAIN.**

## 1. Nombre y alcance exacto

Modificar una única llamada en `snippets/product-customizer.liquid` del tema
auxiliar `178399019384` para que el listener del selector opcional
`#customImage` solo se registre cuando el campo exista.

## 2. Recursos, IDs, URLs e idiomas afectados

- Tema: `gid://shopify/OnlineStoreTheme/178399019384`.
- Rol/prefijo: `UNPUBLISHED`, `/t/46`.
- Archivo: `snippets/product-customizer.liquid`.
- Ruta principal de prueba:
  `/products/lineas-noridcas-marron` en ES, EN, FR, DE y NL.
- Ruta funcional del campo opcional: `/products/custom-file-uploader`.
- MAIN `178396463480`: excluido.

## 3. Valores actuales

`INCORRECTO`

- MD5: `3878a24a9bb6cb134247ac6aff707a58`.
- El producto estándar contiene 0 elementos `#customImage`.
- El archivo ejecuta una llamada directa sobre `fileInput` nulo.
- La consola registra la excepción `addEventListener` en el producto.

Código actual:

```javascript
fileInput.addEventListener('change', function () {
```

## 4. Valor propuesto

```javascript
fileInput?.addEventListener('change', function () {
```

No se cambiará el cuerpo del callback ni ninguna otra línea.

## 5. Evidencia y motivo técnico

- HTML del producto: `#customImage` ausente.
- Archivo real de Shopify: una única ocurrencia de la llamada.
- Consola: excepción nula reproducida en `/t/46`.
- El tema ya utiliza sintaxis opcional compatible en otros bloques.
- Evidencia: `qa-MW-TECH-DYNAMIC-MEASURE-TRACKING-010A2-2026-06-18.md`.

## 6. Riesgos y efectos secundarios

- Riesgo bajo de sintaxis si se alterase algo más que el operador opcional; se
  verificará el contenido almacenado exacto.
- En la plantilla con `#customImage`, el callback debe conservarse sin cambios.
- El error `convertToInches`, el tracking de medidas y el overflow permanecen
  fuera del alcance.

## 7. Respaldo disponible

- Copia local exacta en
  `theme-work-MW-THEME-PAGE-H1-SEMANTIC-008E/snippets/product-customizer.liquid`.
- MD5 local y remoto: `3878a24a9bb6cb134247ac6aff707a58`.
- MAIN y reversión intactos.

## 8. Método exacto de reversión

Restaurar `fileInput.addEventListener` sin `?.` y comprobar que el checksum
vuelve a `3878a24a9bb6cb134247ac6aff707a58`.

## 9. Pruebas posteriores

- Verificar que solo difiere el archivo y la llamada autorizados.
- Confirmar ausencia de la excepción en el producto estándar ES/EN/FR/DE/NL,
  escritorio y móvil.
- Confirmar que `/products/custom-file-uploader` conserva `#customImage` y
  carga sin la excepción.
- Repetir la matriz de 170 pruebas antes de cualquier propuesta de publicación.
- Registrar por separado `convertToInches` y tracking de medidas.

## Aprobación requerida

Para modificar únicamente el tema auxiliar, responde exactamente:

`APROBADO LOTE MW-TECH-PRODUCT-FILEINPUT-GUARD-010A3`

Esta aprobación no autoriza publicar el tema ni modificar el MAIN.

## Estado de ejecución

- Aprobación exacta recibida el 18/06/2026.
- Preflight correcto: auxiliar `178399019384` `UNPUBLISHED`, checksum
  `3878a24a9bb6cb134247ac6aff707a58`, MAIN y reversión intactos.
- Dos escrituras por el conector quedaron bloqueadas y se cancelaron.
- Lectura posterior: archivo sin cambios; la llamada directa permanece.
- Shopify CLI no está instalado y no se instaló software.
- El editor administrativo no fue controlable mediante el navegador integrado.
- Pendiente: guardar manualmente el único carácter `?` autorizado y verificar.
- Verificación posterior a `GUARDADO 010A3`: Shopify sigue mostrando checksum
  `3878a24a9bb6cb134247ac6aff707a58`, una llamada directa y cero llamadas
  opcionales. La modificación no quedó almacenada en el tema objetivo.

## Resultado final almacenado

- Tras la corrección manual confirmada, Shopify almacena exactamente el único
  carácter propuesto.
- MD5 final `8f8a7d213f04ace77c4003647053f763`.
- Producto estándar: 0/10 errores `addEventListener`.
- Cargador: 10/10 errores por el siguiente selector nulo
  `openModalButton`; requiere 010A4.
- Tema auxiliar continúa `UNPUBLISHED`; MAIN intacto.
