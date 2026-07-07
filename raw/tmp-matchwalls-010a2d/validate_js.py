from pathlib import Path
import re, subprocess, tempfile, os, sys
p = Path('tmp-matchwalls-010a2d/snippets/external-selectors.liquid')
text = p.read_text(encoding='utf-8')
blocks = re.findall(r'<script>(.*?)</script>', text, flags=re.S)
print('SCRIPT_BLOCKS', len(blocks))
for i, block in enumerate(blocks, 1):
    js = block.strip()
    tmp = Path(tempfile.gettempdir()) / f'mw010a2d_script_{i}.js'
    tmp.write_text(js, encoding='utf-8')
    result = subprocess.run([r'C:\Users\d.bermejo\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe', '--check', str(tmp)], capture_output=True, text=True)
    print('SCRIPT', i, 'EXIT', result.returncode)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr)
    if result.returncode != 0:
        sys.exit(result.returncode)