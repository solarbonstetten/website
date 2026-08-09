// Copies the pdf.js build files from node_modules into public/ so we can serve
// them from our own origin. Loading them from a CDN caused hard-to-debug
// failures for some users: the main module loaded, but the cross-origin module
// worker never started and the parse just hung forever.
//
// Runs automatically via the predev/prebuild npm scripts; the target directory
// is git-ignored.
import { copyFile, mkdir, readFile } from 'node:fs/promises';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const src = join(root, 'node_modules', 'pdfjs-dist', 'legacy', 'build');
const dest = join(root, 'public', 'leg', 'pdfjs');

// The "legacy" build is transpiled and polyfilled for older browsers – the
// modern build relies on very recent JS features (Promise.withResolvers etc.).
const FILES = ['pdf.min.mjs', 'pdf.worker.min.mjs'];

let pkg;
try {
  pkg = JSON.parse(await readFile(join(root, 'node_modules', 'pdfjs-dist', 'package.json'), 'utf8'));
} catch {
  console.error('vendor-pdfjs: pdfjs-dist is not installed – run `npm install` first.');
  process.exit(1);
}

await mkdir(dest, { recursive: true });
for (const file of FILES) {
  await copyFile(join(src, file), join(dest, file));
}
console.log(`vendor-pdfjs: copied pdf.js ${pkg.version} to public/leg/pdfjs/`);
