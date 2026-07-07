from pathlib import Path
import hashlib
root = Path(r'C:\Users\d.bermejo\OneDrive - Matchwalls\Documentos\Matchwalls Shopify')
src = root / 'theme-work-MW-THEME-PAGE-H1-SEMANTIC-008E' / 'snippets'
out = root / 'tmp-matchwalls-010a2b' / 'snippets'
out.mkdir(parents=True, exist_ok=True)
external_bytes = (src / 'external-selectors.liquid').read_bytes()
srolling_bytes = (src / 'srolling_bar_menu.liquid').read_bytes()
external = external_bytes.decode('utf-8')
srolling = srolling_bytes.decode('utf-8')
expected_ext = '8a9c233bca52da58ce59fffc3aee8359'
expected_srolling_original = 'c254cf711a7706dc21ece2f2ad31acea'
if hashlib.md5(external_bytes).hexdigest() != expected_ext:
    raise SystemExit(f'external source MD5 mismatch {hashlib.md5(external_bytes).hexdigest()}')
if hashlib.md5(srolling_bytes).hexdigest() != expected_srolling_original:
    raise SystemExit(f'srolling source MD5 mismatch {hashlib.md5(srolling_bytes).hexdigest()}')
nl = '\r\n' if '\r\n' in external else '\n'
insert_after = f"    const ftToMeter = 0.3048;{nl}"
insert_block = (
    f"{nl}"
    f"    function debounceTracking(func, delay) {{{nl}"
    f"      let timeout;{nl}"
    f"      return function (...args) {{{nl}"
    f"        clearTimeout(timeout);{nl}"
    f"        timeout = setTimeout(() => func.apply(this, args), delay);{nl}"
    f"      }};{nl}"
    f"    }}{nl}"
    f"{nl}"
    f"    function pushInputMuralOutsideEvent(dimension, value) {{{nl}"
    f"      window.dataLayer = window.dataLayer || [];{nl}"
    f"      window.dataLayer.push({{{nl}"
    f"        event: 'input_mural_outside',{nl}"
    f"        dimension: dimension,{nl}"
    f"        value: value,{nl}"
    f"      }});{nl}"
    f"    }}{nl}"
    f"{nl}"
    f"    const pushExternalWidthTracking = debounceTracking(function () {{{nl}"
    f"      pushInputMuralOutsideEvent('width', externalWidthInput.value);{nl}"
    f"    }}, 300);{nl}"
    f"{nl}"
    f"    const pushExternalHeightTracking = debounceTracking(function () {{{nl}"
    f"      pushInputMuralOutsideEvent('height', externalHeightInput.value);{nl}"
    f"    }}, 300);{nl}"
)
if insert_block.strip() in external:
    raise SystemExit('external already patched')
external2 = external.replace(insert_after, insert_after + insert_block, 1)
old_width = (
    f"    externalWidthInput.addEventListener('input', function () {{{nl}"
    f"      updateFormSurfaceInputs(); // Sync form-surface inputs{nl}"
    f"      updateProductCustomizer(); // Update logic for customizer{nl}"
    f"      calculateValues(); // Recalculate values{nl}"
    f"      saveDimensionsToLocalStorage();{nl}"
    f"    }});{nl}"
)
new_width = (
    f"    externalWidthInput.addEventListener('input', function () {{{nl}"
    f"      updateFormSurfaceInputs(); // Sync form-surface inputs{nl}"
    f"      updateProductCustomizer(); // Update logic for customizer{nl}"
    f"      calculateValues(); // Recalculate values{nl}"
    f"      saveDimensionsToLocalStorage();{nl}"
    f"      pushExternalWidthTracking();{nl}"
    f"    }});{nl}"
)
old_height = (
    f"    externalHeightInput.addEventListener('input', function () {{{nl}"
    f"      updateFormSurfaceInputs(); // Sync form-surface inputs{nl}"
    f"      updateProductCustomizer();{nl}"
    f"      calculateValues(); // Recalculate values{nl}"
    f"      saveDimensionsToLocalStorage();{nl}"
    f"    }});{nl}"
)
new_height = (
    f"    externalHeightInput.addEventListener('input', function () {{{nl}"
    f"      updateFormSurfaceInputs(); // Sync form-surface inputs{nl}"
    f"      updateProductCustomizer();{nl}"
    f"      calculateValues(); // Recalculate values{nl}"
    f"      saveDimensionsToLocalStorage();{nl}"
    f"      pushExternalHeightTracking();{nl}"
    f"    }});{nl}"
)
if old_width not in external2:
    raise SystemExit('width listener block not found')
if old_height not in external2:
    raise SystemExit('height listener block not found')
external2 = external2.replace(old_width, new_width, 1).replace(old_height, new_height, 1)
nl_s = '\r\n' if '\r\n' in srolling else '\n'
start_marker = f"{nl_s}{nl_s}    // Select the width and height input fields"
end_marker = f"{nl_s}  }});{nl_s}</script>"
start = srolling.find(start_marker)
end = srolling.find(end_marker, start)
if start == -1 or end == -1:
    raise SystemExit('srolling measurement block markers not found')
srolling2 = srolling[:start] + end_marker + srolling[end + len(end_marker):]
(out / 'external-selectors.liquid').write_bytes(external2.encode('utf-8'))
(out / 'srolling_bar_menu.liquid').write_bytes(srolling2.encode('utf-8'))
for name, text in [('external-selectors.liquid', external2), ('srolling_bar_menu.liquid', srolling2)]:
    data = text.encode('utf-8')
    print(name, hashlib.md5(data).hexdigest(), len(data))
print('external_input_mural_count', external2.count('input_mural_outside'))
print('srolling_input_mural_count', srolling2.count('input_mural_outside'))
print('srolling_collection_click_count', srolling2.count('collection_submenu_click'))
