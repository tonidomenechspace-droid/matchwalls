from pathlib import Path
import hashlib
root = Path.cwd()
base = root / 'theme-work-MW-THEME-PAGE-H1-SEMANTIC-008E' / 'snippets' / 'external-selectors.liquid'
outdir = root / 'tmp-matchwalls-010a2d'
outdir.mkdir(exist_ok=True)
backup = outdir / 'external-selectors.rollback.liquid'
candidate = outdir / 'external-selectors.010a2d.liquid'
raw = base.read_bytes()
md5 = hashlib.md5(raw).hexdigest()
expected = '8a9c233bca52da58ce59fffc3aee8359'
if md5 != expected:
    raise SystemExit(f'Base raw MD5 mismatch: {md5} != {expected}')
text = raw.decode('utf-8')
nl = '\r\n' if '\r\n' in text else '\n'
insert_after = f"    const ftToMeter = 0.3048;{nl}"
insert = f"""{nl}    function updateMeasureTrackingQa(payload) {{{nl}      if (window.location.search.indexOf('mwqa=010a2d') === -1) return;{nl}{nl}      const currentCount = parseInt(document.documentElement.getAttribute('data-mw010a2d-count') || '0', 10) + 1;{nl}      document.documentElement.setAttribute('data-mw010a2d-count', String(currentCount));{nl}      document.documentElement.setAttribute('data-mw010a2d-last-event', JSON.stringify(payload));{nl}    }}{nl}{nl}    function pushInputMuralOutsideEvent(dimension, value) {{{nl}      const payload = {{{nl}        event: 'input_mural_outside',{nl}        dimension: dimension,{nl}        value: value,{nl}      }};{nl}{nl}      window.dataLayer = window.dataLayer || [];{nl}      window.dataLayer.push(payload);{nl}      updateMeasureTrackingQa(payload);{nl}    }}{nl}"""
if insert_after not in text:
    raise SystemExit('Insertion anchor not found')
text2 = text.replace(insert_after, insert_after + insert, 1)
old_width = f"""    externalWidthInput.addEventListener('input', function () {{{nl}      updateFormSurfaceInputs(); // Sync form-surface inputs{nl}      updateProductCustomizer(); // Update logic for customizer{nl}      calculateValues(); // Recalculate values{nl}      saveDimensionsToLocalStorage();{nl}    }});{nl}"""
new_width = f"""    externalWidthInput.addEventListener('input', function () {{{nl}      updateFormSurfaceInputs(); // Sync form-surface inputs{nl}      updateProductCustomizer(); // Update logic for customizer{nl}      calculateValues(); // Recalculate values{nl}      saveDimensionsToLocalStorage();{nl}      pushInputMuralOutsideEvent('width', externalWidthInput.value);{nl}    }});{nl}"""
old_height = f"""    externalHeightInput.addEventListener('input', function () {{{nl}      updateFormSurfaceInputs(); // Sync form-surface inputs{nl}      updateProductCustomizer();{nl}      calculateValues(); // Recalculate values{nl}      saveDimensionsToLocalStorage();{nl}    }});{nl}"""
new_height = f"""    externalHeightInput.addEventListener('input', function () {{{nl}      updateFormSurfaceInputs(); // Sync form-surface inputs{nl}      updateProductCustomizer();{nl}      calculateValues(); // Recalculate values{nl}      saveDimensionsToLocalStorage();{nl}      pushInputMuralOutsideEvent('height', externalHeightInput.value);{nl}    }});{nl}"""
if text2.count(old_width) != 1:
    raise SystemExit(f'Width block count not 1: {text2.count(old_width)}')
if text2.count(old_height) != 1:
    raise SystemExit(f'Height block count not 1: {text2.count(old_height)}')
text2 = text2.replace(old_width, new_width, 1).replace(old_height, new_height, 1)
backup.write_bytes(raw)
candidate.write_bytes(text2.encode('utf-8'))
print('BASE_MD5', md5)
print('CANDIDATE_MD5', hashlib.md5(text2.encode('utf-8')).hexdigest())
print('BASE_BYTES', len(raw))
print('CANDIDATE_BYTES', len(text2.encode('utf-8')))
print('FUNCTION_COUNT', text2.count('function pushInputMuralOutsideEvent'))
print('QA_SIGNAL_COUNT', text2.count('data-mw010a2d'))
print('WIDTH_CALL_COUNT', text2.count("pushInputMuralOutsideEvent('width'"))
print('HEIGHT_CALL_COUNT', text2.count("pushInputMuralOutsideEvent('height'"))
print('NEWLINE', repr(nl))