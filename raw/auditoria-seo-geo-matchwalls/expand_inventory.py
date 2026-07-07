import csv
import re
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parent
source = ROOT / "inventario-urls.csv"
rows = list(csv.DictReader(source.open(encoding="utf-8-sig")))
by_url = {r["url"]: r for r in rows}
fields = list(rows[0].keys()) + ["estado_auditoria", "patron_muestra", "handle_sospechoso"]


def language(url):
    match = re.match(r"^/(en|fr|de|nl|it|pt)(/|$)", urlparse(url).path)
    return {"pt": "pt-PT"}.get(match.group(1), match.group(1)) if match else "es"


def kind(url):
    path = urlparse(url).path
    if "/products/" in path:
        return "product"
    if "/collections/" in path:
        return "collection"
    if "/blogs/" in path:
        return "article"
    if "/pages/" in path:
        return "page"
    if path.rstrip("/") in {"", "/en", "/fr", "/de", "/nl", "/it", "/pt"}:
        return "home"
    return "other"


sample_terms = ["sample", "muestra", "probe", "echantillon", "campione", "amostra", "steekproef"]
suspicious_terms = ["norid", "enchathed", "recoto", "suctan", "matchalls", "transfroma"]
expanded = []
for url in (ROOT / "sitemap-urls.txt").read_text(encoding="utf-8").splitlines():
    row = by_url.get(url, {f: "" for f in rows[0].keys()})
    row["url"] = url
    row["idioma_url"] = row.get("idioma_url") or language(url)
    row["tipo"] = row.get("tipo") or kind(url)
    status = str(row.get("estado_http", ""))
    if status == "200":
        audit = "verificada_http_200"
    elif status == "429":
        audit = "limitada_rate_limiting"
    elif status:
        audit = "verificada_con_error"
    else:
        audit = "no_rastreada"
    low = url.lower()
    row["estado_auditoria"] = audit
    row["patron_muestra"] = "sí" if "/products/" in low and any(x in low for x in sample_terms) else "no"
    row["handle_sospechoso"] = "sí" if any(x in low for x in suspicious_terms) or urlparse(url).path.endswith("-1") else "no"
    expanded.append(row)

with source.open("w", newline="", encoding="utf-8-sig") as out:
    writer = csv.DictWriter(out, fieldnames=fields)
    writer.writeheader()
    writer.writerows(expanded)
print(f"Inventory expanded to {len(expanded)} sitemap URLs")
