# Lote prioritario de interfaz internacional DE/NL

Fecha: 15 de junio de 2026.

## Objetivo

Corregir primero las cadenas compartidas que aparecen en navegación, producto, carrito y mensajes comerciales. El trabajo debe ejecutarse en un tema aislado, con revisión editorial nativa y QA visual antes de publicar.

## Hechos verificados

- El archivo `locales/de.json` del tema principal tiene aproximadamente 230 KB y contiene numerosos textos traducidos automáticamente.
- La interfaz pública neerlandesa presenta problemas equivalentes.
- Las cadenas son compartidas y se repiten en muchas URLs; su impacto supera al de una descripción de producto individual.

## Prioridad 1: navegación y conversión

| Idioma | Texto actual | Corrección propuesta |
|---|---|---|
| DE | Offenes Auto | Warenkorb öffnen |
| DE | Account -Seite öffnen | Kontoseite öffnen |
| DE | Offene Suche | Suche öffnen |
| DE | 3 mit Klarna in 3 Amtszeiten bezahlen | In 3 Raten mit Klarna bezahlen |
| DE | Mindestanfrage | Mindestbestellwert |
| DE | Farbige Straßen | Verfügbare Farben |
| NL | Open auto | Winkelwagen openen |
| NL | Betaal in 3 termen met Klarna | Betaal in 3 termijnen met Klarna |
| NL | Spaties | Ruimtes |
| NL | Minimumverzoek | Minimale bestelwaarde |
| NL | Gekleurde wegen | Beschikbare kleuren |

## Prioridad 2: propuesta de valor y personalización

| Idioma | Texto actual | Corrección propuesta |
|---|---|---|
| DE | Haben Sie Ihre eigenen Designs? Wir werden wahr! | Haben Sie ein eigenes Design? Wir setzen es um! |
| DE | Laden Sie jetzt das Design hoch | Design jetzt hochladen |
| NL | Heeft u uw eigen ontwerpen? We komen uit! | Heb je een eigen ontwerp? Wij brengen het tot leven! |
| NL | Upload ontwerp nu | Ontwerp nu uploaden |
| NL | Transformeer je spaties met Matchwalls | Transformeer je ruimtes met Matchwalls |

## Prioridad 3: accesibilidad y microcopy

- Revisar textos de botones, estados de inventario, carrito, cuenta, formularios y búsqueda.
- Mantener variables Liquid como `{{ count }}`, `{{ price }}` y `{{ link }}` sin alterarlas.
- Evitar traducciones literales de términos de interfaz y comercio.

## Método de ejecución

1. Duplicar el tema principal en un tema aislado para UI internacional.
2. Exportar y revisar las claves realmente utilizadas en home, colección, producto, carrito, búsqueda y cuenta.
3. Corregir DE y NL con revisión humana; después revisar FR y EN.
4. Validar que el JSON siga siendo válido y que las variables Liquid se conserven.
5. Probar visualmente escritorio y móvil en cada idioma.
6. Publicar solo después de aprobar capturas y recorrido de compra.

## No ejecutar todavía

- No sustituir de forma masiva palabras sin contexto.
- No editar checkout o textos legales sin revisión específica.
- No publicar un tema que incluya cambios de diseño no aprobados.
