const fs = require('fs');
const vm = require('vm');
const files = [
  'tmp-matchwalls-010a2b/snippets/external-selectors.liquid',
  'tmp-matchwalls-010a2b/snippets/srolling_bar_menu.liquid'
];
for (const file of files) {
  const text = fs.readFileSync(file, 'utf8');
  const scripts = [...text.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m => m[1]);
  if (!scripts.length) throw new Error(`${file}: no script blocks found`);
  for (let i = 0; i < scripts.length; i++) {
    new vm.Script(scripts[i], { filename: `${file}#script${i}` });
  }
  console.log(file, 'scripts', scripts.length, 'js_parse_ok', true);
}
