from pathlib import Path
import base64, json, hashlib
root = Path(r'C:\Users\d.bermejo\OneDrive - Matchwalls\Documentos\Matchwalls Shopify\tmp-matchwalls-010a2b\snippets')
files=[]
for name in ['external-selectors.liquid','srolling_bar_menu.liquid']:
    data = (root/name).read_bytes()
    files.append({
        'filename': f'snippets/{name}',
        'body': {'type':'BASE64','value': base64.b64encode(data).decode('ascii')},
        '_md5': hashlib.md5(data).hexdigest(),
        '_size': len(data)
    })
print(json.dumps(files, separators=(',',':')))
