# Instrucciones manuales - MW-THEME-LIBRARY-CLEANUP-SAFE-DELETE-016B

Eliminar solo un tema:

`Dev`

ID:

`141375406307`

## Pasos

1. En Shopify Admin, ve a **Tienda online > Temas**.
2. Baja hasta los temas borrador.
3. Busca exactamente el tema llamado:

   `Dev`

4. Comprueba que el enlace inferior o URL contiene:

   `themes/141375406307`

5. Abre el menú de tres puntos del tema `Dev`.
6. Elige **Remove / Eliminar**.
7. Confirma la eliminación.
8. No pulses `Publish` en ningún tema.
9. No elimines `Dev David`, `Staging`, `Production`, `SEO schema hotfix`, `MW-FOOTER`, `MW-THEME-PAGE-H1` ni el MAIN.

## Confirmación que debe devolver Daniel

Después de eliminar, responder:

`ELIMINADO 016B DEV 141375406307`

## Postcheck posterior

Tras la confirmación se debe ejecutar:

`MW-THEME-LIBRARY-CLEANUP-POSTCHECK-016B1`

Objetivo:

- Confirmar que Shopify pasa de 20 a 19 temas.
- Confirmar que MAIN sigue siendo `178399019384`.
- Confirmar que no se publicó ni eliminó otro tema.

