from pathlib import Path
import hashlib, base64, json
root = Path(r'C:\Users\d.bermejo\OneDrive - Matchwalls\Documentos\Matchwalls Shopify')
src = root / 'theme-work-MW-THEME-PAGE-H1-SEMANTIC-008E' / 'snippets'
out = root / 'tmp-matchwalls-010a2b' / 'rollback'
out.mkdir(parents=True, exist_ok=True)
external = (src / 'external-selectors.liquid').read_bytes().decode('utf-8')
srolling = (src / 'srolling_bar_menu.liquid').read_bytes().decode('utf-8')
nl = '\n'
old = """    // Debounced event handlers for width and height inputs
    const debouncedWidthEvent = debounce(() => {
      pushInputMuralOutsideEvent('width', widthInput.value);
    }, 300); // Delay of 300ms (adjustable)

    const debouncedHeightEvent = debounce(() => {
      pushInputMuralOutsideEvent('height', heightInput.value);
    }, 300); // Delay of 300ms (adjustable)

    // Add debounced event listeners to width and height inputs
    widthInput.addEventListener('input', debouncedWidthEvent);
    heightInput.addEventListener('input', debouncedHeightEvent);
"""
new = """    // Register only the controls that exist on the current template.
    if (widthInput) {
      const debouncedWidthEvent = debounce(() => {
        pushInputMuralOutsideEvent('width', widthInput.value);
      }, 300);

      widthInput.addEventListener('input', debouncedWidthEvent);
    }

    if (heightInput) {
      const debouncedHeightEvent = debounce(() => {
        pushInputMuralOutsideEvent('height', heightInput.value);
      }, 300);

      heightInput.addEventListener('input', debouncedHeightEvent);
    }
"""
if old not in srolling:
    raise SystemExit('original direct block not found')
srolling_rollback = srolling.replace(old, new, 1)
external_bytes = external.encode('utf-8')
srolling_bytes = srolling_rollback.encode('utf-8')
(out / 'external-selectors.liquid').write_bytes(external_bytes)
(out / 'srolling_bar_menu.liquid').write_bytes(srolling_bytes)
print('external', hashlib.md5(external_bytes).hexdigest(), len(external_bytes))
print('srolling', hashlib.md5(srolling_bytes).hexdigest(), len(srolling_bytes))
print(json.dumps([
 {'filename':'snippets/external-selectors.liquid','body':{'type':'BASE64','value':base64.b64encode(external_bytes).decode('ascii')}},
 {'filename':'snippets/srolling_bar_menu.liquid','body':{'type':'BASE64','value':base64.b64encode(srolling_bytes).decode('ascii')}}
], separators=(',',':')))
