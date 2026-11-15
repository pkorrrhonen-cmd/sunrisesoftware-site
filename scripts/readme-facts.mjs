// Writes the profile README's product table from docs/facts.json (adr.sws.014).
//
//   node scripts/readme-facts.mjs --print                print the generated block
//   node scripts/readme-facts.mjs <README.md>            rewrite the block between the markers in place
//   node scripts/readme-facts.mjs <README.md> --check    exit 1 when the block differs from the facts
//
// The README lives in its own repository (pkorrrhonen-cmd/pkorrrhonen-cmd); give the path to its
// checkout. Only the block between the markers is written; the rest of the README is hand-written.
// check-site.mjs --readme <path> runs the same comparison in the session routine.
import { readFileSync, writeFileSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { loadFacts, validateFacts, renderReadmeBlock, readmeBlock } from './facts.mjs';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const args = process.argv.slice(2);
const facts = loadFacts(root);
const errors = validateFacts(facts);
if (errors.length) {
  console.error(errors.map((e) => `  - ${e}`).join('\n'));
  process.exit(1);
}

if (args.includes('--print')) {
  console.log(renderReadmeBlock(facts));
  process.exit(0);
}

const path = args.find((a) => !a.startsWith('--'));
if (!path) {
  console.error('usage: node scripts/readme-facts.mjs <README.md> [--check] | --print');
  process.exit(2);
}
const readme = readFileSync(path, 'utf8');
const eol = readme.includes('\r\n') ? '\r\n' : '\n';
const block = readmeBlock(readme);
if (!block) {
  console.error(`${path}: no "<!-- facts:start" ... "<!-- facts:end -->" markers; put them where the product table goes`);
  process.exit(1);
}
const fresh = renderReadmeBlock(facts, eol);
if (args.includes('--check')) {
  if (block.text !== fresh) {
    console.error(`${path}: the product table differs from docs/facts.json; run node scripts/readme-facts.mjs ${path}`);
    process.exit(1);
  }
  console.log(`${path}: the product table matches docs/facts.json`);
  process.exit(0);
}
if (block.text === fresh) {
  console.log(`${path}: already up to date`);
} else {
  writeFileSync(path, readme.slice(0, block.start) + fresh + readme.slice(block.end));
  console.log(`${path}: product table written from docs/facts.json`);
}
