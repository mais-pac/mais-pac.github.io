import katex from 'katex';
import fs from 'node:fs';
const input = JSON.parse(fs.readFileSync(0, 'utf8'));
const output = input.map(({tex,display}) => katex.renderToString(tex, {
  displayMode: display, throwOnError: true, strict: 'error', trust: false,
  output: 'htmlAndMathml', maxExpand: 1000
}));
process.stdout.write(JSON.stringify(output));
