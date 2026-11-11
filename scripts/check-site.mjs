// Dependency-free checks for the static site. Run: node scripts/check-site.mjs [--links]
// CI runs it without --links (no network in the gate); --links HEAD-checks every external URL.
import { readFileSync, existsSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const html = readFileSync(resolve(root, 'index.html'), 'utf8');
const buildInfo = JSON.parse(readFileSync(resolve(root, 'docs/BUILD_INFO.json'), 'utf8'));
const failures = [];
const fail = (msg) => failures.push(msg);

// 1. Every local image reference exists.
const localRefs = [...html.matchAll(/(?:src|href|content|poster)="((?:images|media|source-assets)\/[^"]+)"/g)].map((m) => m[1]);
for (const ref of new Set(localRefs)) {
  if (!existsSync(resolve(root, ref))) fail(`missing file referenced from index.html: ${ref}`);
}

// 2. Required head elements.
const required = [
  ['<meta name="description"', 'meta description'],
  ['<link rel="canonical"', 'canonical link'],
  ['property="og:title"', 'Open Graph title'],
  ['property="og:image"', 'Open Graph image'],
  ['type="application/ld+json"', 'JSON-LD structured data'],
  ['<link rel="icon"', 'favicon'],
];
for (const [needle, name] of required) {
  if (!html.includes(needle)) fail(`missing ${name} in <head>`);
}

// 3. No em dashes in on-page copy (style and script blocks excluded).
const body = html.slice(html.indexOf('<body'), html.lastIndexOf('</body>'))
  .replace(/<script[\s\S]*?<\/script>/g, '')
  .replace(/<style[\s\S]*?<\/style>/g, '');
if (/—|&mdash;/.test(body)) fail('em dash in on-page copy (use a comma, a colon, or restructure)');

// 3b. No product version numbers on the page: they age silently (adr.sws.015). Statuses carry a date.
// Checked over the whole file so the drawn instruments' card data is covered too.
// The escapes in this pattern were eaten once (\b became a literal backspace and
// \d became "d"), so from 20.9. to 11.11.2026 the guard matched nothing at all.
// The self-test below keeps a broken pattern from passing silently again.
const VERSION_RE = /\bv\d+\.\d+(?:\.\d+)?\b|\b(?:MasterForge|Luviamo|Virustutka|Atlas|Somnus|SpectralForge|TilastoSilta|ReviewGlass)\s+\d+\.\d+/;
const mustHit = ['Luviamo v0.385', 'Atlas v0.9', 'MasterForge 4.44', 'SpectralForge v2.0'];
const mustMiss = ['1335.90 pts', 'version="1.0"', 'cubic-bezier(.22,1,.36,1)', 'Revised 20 Sep 2026'];
for (const s of mustHit) if (!VERSION_RE.test(s)) fail(`version guard broken: it does not catch "${s}"`);
for (const s of mustMiss) if (VERSION_RE.test(s)) fail(`version guard too wide: it catches "${s}"`);
const versionHit = html.match(VERSION_RE);
if (versionHit) fail(`product version number on the page: "${versionHit[0]}" (adr.sws.015: statuses carry a date, not a version)`);

// 4. Forbidden strings: withheld names, corrected errors, relative-time copy (adr.sws.004, 006).
const forbidden = [
  'Premius',
  '2008&ndash;2016',
  '2008–2016',
  'Launching within the month',
  'coming soon',
  'within the month',
  'recently',
];
for (const s of forbidden) {
  if (html.toLowerCase().includes(s.toLowerCase())) fail(`forbidden string in index.html (body, script or head): "${s}"`);
}

// 5. The footer revision date equals BUILD_INFO.updated (adr.sws.004).
const revised = html.match(/data-revised="(\d{4}-\d{2}-\d{2})"/);
if (!revised) fail('footer has no data-revised="YYYY-MM-DD" attribute');
else if (revised[1] !== buildInfo.updated) {
  fail(`footer revision ${revised[1]} differs from docs/BUILD_INFO.json updated ${buildInfo.updated}`);
}

// 6. The GitHub profile link appears where adr.sws.007 says (nav, meta row, §05, JSON-LD).
const github = (html.match(/https:\/\/github\.com\/pkorrrhonen-cmd/g) || []).length;
if (github < 4) fail(`GitHub profile link appears ${github} times, expected at least 4 (adr.sws.007)`);

// 7. sitemap.xml lastmod equals the page revision (SEED 5.3), and the sitemap
// names the canonical address.
const sitemap = readFileSync(resolve(root, 'sitemap.xml'), 'utf8');
const lastmod = sitemap.match(/<lastmod>(\d{4}-\d{2}-\d{2})<\/lastmod>/);
if (!lastmod) fail('sitemap.xml has no <lastmod>');
else if (lastmod[1] !== buildInfo.updated) {
  fail(`sitemap.xml lastmod ${lastmod[1]} differs from docs/BUILD_INFO.json updated ${buildInfo.updated}`);
}
if (!sitemap.includes('<loc>https://sunrisesoftware.app/</loc>')) fail('sitemap.xml does not name the canonical address');

// 8. The files a crawler, a browser and a phone ask for by name must exist as
// files, not be answered by the front page (adr.sws.017).
for (const f of ['404.html', 'favicon.ico', 'icon-192.png', 'icon-512.png', 'icon-maskable-512.png', 'apple-touch-icon.png', 'site.webmanifest']) {
  if (!existsSync(resolve(root, f))) fail(`missing site file: ${f}`);
}

// 9. Optional: external links answer (2xx/3xx). Not run in CI.
if (process.argv.includes('--links')) {
  const urls = [...new Set([...html.matchAll(/href="(https?:\/\/[^"]+)"/g)].map((m) => m[1]))]
    .filter((u) => !u.startsWith('https://fonts.'));
  const results = await Promise.all(urls.map(async (u) => {
    try {
      const r = await fetch(u, { method: 'HEAD', redirect: 'follow', signal: AbortSignal.timeout(12000) });
      return [u, r.status];
    } catch (e) {
      return [u, `error: ${e.message}`];
    }
  }));
  for (const [u, status] of results) {
    const ok = typeof status === 'number' && status < 400;
    console.log(`${ok ? 'ok  ' : 'FAIL'} ${status} ${u}`);
    if (!ok) fail(`external link ${u} answered ${status}`);
  }
}

if (failures.length) {
  console.error(`\n${failures.length} check(s) failed:`);
  for (const f of failures) console.error(`  - ${f}`);
  process.exit(1);
}
console.log(`index.html ok: ${new Set(localRefs).size} local files, revision ${buildInfo.updated}, version ${buildInfo.version}`);
