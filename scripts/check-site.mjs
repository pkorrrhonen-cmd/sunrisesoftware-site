// Dependency-free checks for the static site. Run: node scripts/check-site.mjs [--links]
// CI runs it without --links (no network in the gate); --links HEAD-checks every external URL.
// Every page the sitemap names is checked: the front page and each sub-page (SEED v4.1.0, 5.8).
import { readFileSync, existsSync, readdirSync, statSync } from 'node:fs';
import { resolve, dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const SITE = 'https://sunrisesoftware.app';
const buildInfo = JSON.parse(readFileSync(resolve(root, 'docs/BUILD_INFO.json'), 'utf8'));
const failures = [];
const fail = (msg) => failures.push(msg);

// 0. The pages: every <url> in sitemap.xml, each with its own lastmod. A page's file is the
// address's path plus index.html, so /silent-context/ is silent-context/index.html.
const sitemap = readFileSync(resolve(root, 'sitemap.xml'), 'utf8');
const pages = [...sitemap.matchAll(/<url>\s*<loc>([^<]+)<\/loc>\s*(?:<lastmod>(\d{4}-\d{2}-\d{2})<\/lastmod>)?/g)]
  .map(([, loc, lastmod]) => {
    const path = loc.startsWith(SITE) ? loc.slice(SITE.length) : null;
    const file = path === null ? null : (path.replace(/^\//, '') + (path.endsWith('/') ? 'index.html' : ''));
    return { loc, lastmod, path, file: file || 'index.html' };
  });
if (!pages.some((p) => p.loc === `${SITE}/`)) fail('sitemap.xml does not name the canonical address');
for (const p of pages) {
  if (p.path === null) fail(`sitemap.xml names an address outside the site: ${p.loc}`);
  else if (!p.path.endsWith('/')) fail(`sitemap.xml address does not end in a slash: ${p.loc}`);
  if (!p.lastmod) fail(`sitemap.xml has no <lastmod> for ${p.loc}`);
  if (!existsSync(resolve(root, p.file))) fail(`sitemap.xml names ${p.loc}, but ${p.file} does not exist`);
}
// ...and every sub-page on disk is in the sitemap (a directory at the root holding an index.html).
const NOT_PAGES = new Set(['docs', 'scripts', 'images', 'media', 'scc', 'source-assets', 'node_modules', '.git', '.github', '.claude', '.wrangler']);
for (const d of readdirSync(root)) {
  if (NOT_PAGES.has(d) || !statSync(resolve(root, d)).isDirectory()) continue;
  if (existsSync(resolve(root, d, 'index.html')) && !pages.some((p) => p.file === `${d}/index.html`)) {
    fail(`${d}/index.html is a page but sitemap.xml does not name ${SITE}/${d}/`);
  }
}

// The version guard. The escapes in this pattern were eaten once (\b became a literal backspace and
// \d became "d"), so from 20.9. to 11.11.2026 the guard matched nothing at all.
// The self-test below keeps a broken pattern from passing silently again.
const VERSION_RE = /\bv\d+\.\d+(?:\.\d+)?\b|\b(?:MasterForge|Luviamo|Virustutka|Atlas|Somnus|SpectralForge|TilastoSilta|ReviewGlass)\s+\d+\.\d+/;
const mustHit = ['Luviamo v0.385', 'Atlas v0.9', 'MasterForge 4.44', 'SpectralForge v2.0'];
const mustMiss = ['1335.90 pts', 'version="1.0"', 'cubic-bezier(.22,1,.36,1)', 'Revised 20 Sep 2026'];
for (const s of mustHit) if (!VERSION_RE.test(s)) fail(`version guard broken: it does not catch "${s}"`);
for (const s of mustMiss) if (VERSION_RE.test(s)) fail(`version guard too wide: it catches "${s}"`);

// Forbidden strings: withheld names, corrected errors, relative-time copy (adr.sws.004, 006).
const forbidden = [
  'Premius',
  '2008&ndash;2016',
  '2008–2016',
  'Launching within the month',
  'coming soon',
  'within the month',
  'recently',
];

// A local reference: images/, media/ or source-assets/, written relative to the page, from the
// root (/media/...), or as the site's own absolute URL (og:image).
const REF_RE = /(?:src|href|content|poster)="((?:https:\/\/sunrisesoftware\.app)?\/?(?:images|media|source-assets)\/[^"]+)"/g;
let localCount = 0;
const allHtml = [];

for (const page of pages) {
  if (!existsSync(resolve(root, page.file))) continue;
  const name = page.file;
  const html = readFileSync(resolve(root, page.file), 'utf8');
  const front = page.file === 'index.html';
  allHtml.push(html);

  // 1. Every local image and media reference exists.
  const refs = new Set([...html.matchAll(REF_RE)].map((m) => m[1]));
  for (const ref of refs) {
    const fromRoot = ref.startsWith('/') || ref.startsWith(SITE);
    const rel = ref.replace(SITE, '').replace(/^\//, '');
    const target = fromRoot ? resolve(root, rel) : resolve(root, dirname(page.file), rel);
    if (!existsSync(target)) fail(`missing file referenced from ${name}: ${ref}`);
  }
  localCount += refs.size;

  // 2. Required head elements, and a canonical link to the page's own address.
  const required = [
    ['<meta name="description"', 'meta description'],
    ['<link rel="canonical"', 'canonical link'],
    ['property="og:title"', 'Open Graph title'],
    ['property="og:image"', 'Open Graph image'],
    ['property="og:image:alt"', 'Open Graph image alt'],
    ['type="application/ld+json"', 'JSON-LD structured data'],
    ['<link rel="icon"', 'favicon'],
  ];
  for (const [needle, what] of required) {
    if (!html.includes(needle)) fail(`missing ${what} in the <head> of ${name}`);
  }
  if (!html.includes(`<link rel="canonical" href="${page.loc}">`)) fail(`${name}: canonical is not ${page.loc}`);
  for (const block of html.matchAll(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/g)) {
    try { JSON.parse(block[1]); } catch (e) { fail(`${name}: JSON-LD does not parse (${e.message})`); }
  }

  // 3. No em dashes in on-page copy (style and script blocks excluded).
  const body = html.slice(html.indexOf('<body'), html.lastIndexOf('</body>'))
    .replace(/<script[\s\S]*?<\/script>/g, '')
    .replace(/<style[\s\S]*?<\/style>/g, '');
  if (/—|&mdash;/.test(body)) fail(`em dash in on-page copy of ${name} (use a comma, a colon, or restructure)`);

  // 3b. No product version numbers: they age silently (adr.sws.015). Statuses carry a date.
  // Checked over the whole file so the drawn instruments' card data is covered too.
  const versionHit = html.match(VERSION_RE);
  if (versionHit) fail(`product version number in ${name}: "${versionHit[0]}" (adr.sws.015: statuses carry a date, not a version)`);

  // 4. Forbidden strings.
  for (const s of forbidden) {
    if (html.toLowerCase().includes(s.toLowerCase())) fail(`forbidden string in ${name} (body, script or head): "${s}"`);
  }

  // 5. The footer revision date: the front page's equals BUILD_INFO.updated (adr.sws.004), and
  // every page's equals its own lastmod in the sitemap.
  const revised = html.match(/data-revised="(\d{4}-\d{2}-\d{2})"/);
  if (!revised) fail(`${name}: footer has no data-revised="YYYY-MM-DD" attribute`);
  else {
    if (front && revised[1] !== buildInfo.updated) {
      fail(`footer revision ${revised[1]} differs from docs/BUILD_INFO.json updated ${buildInfo.updated}`);
    }
    if (page.lastmod && revised[1] !== page.lastmod) {
      fail(`${name}: footer revision ${revised[1]} differs from its sitemap lastmod ${page.lastmod}`);
    }
  }

  if (front) {
    // 6. The GitHub profile link appears where adr.sws.007 says (nav, meta row, §05, JSON-LD).
    const github = (html.match(/https:\/\/github\.com\/pkorrrhonen-cmd(?!\/)/g) || []).length;
    if (github < 4) fail(`GitHub profile link appears ${github} times, expected at least 4 (adr.sws.007)`);
    // The front page links every sub-page.
    for (const p of pages) {
      if (p.path && p.path !== '/' && !html.includes(`href="${p.path}"`)) fail(`the front page does not link ${p.path}`);
    }
  } else {
    // 6b. A sub-page has the back button in the nav row and again at its foot (the SEED, 2.1).
    const back = (html.match(/href="\/"/g) || []).length;
    if (back < 3) fail(`${name}: links the front page ${back} times, expected the wordmark and the back button twice`);
    if (!/>[^<]*Back to the front page</.test(html)) fail(`${name}: no "Back to the front page" button`);
  }
}

// 7. The front page's lastmod equals BUILD_INFO.updated (SEED 5.3).
const frontPage = pages.find((p) => p.loc === `${SITE}/`);
if (frontPage && frontPage.lastmod !== buildInfo.updated) {
  fail(`sitemap.xml lastmod ${frontPage.lastmod} differs from docs/BUILD_INFO.json updated ${buildInfo.updated}`);
}

// 8. The files a crawler, a browser and a phone ask for by name must exist as
// files, not be answered by the front page (adr.sws.017).
for (const f of ['404.html', 'favicon.ico', 'icon-192.png', 'icon-512.png', 'icon-maskable-512.png', 'apple-touch-icon.png', 'site.webmanifest']) {
  if (!existsSync(resolve(root, f))) fail(`missing site file: ${f}`);
}

// 9. Optional: external links answer (2xx/3xx). Not run in CI.
if (process.argv.includes('--links')) {
  const urls = [...new Set(allHtml.flatMap((h) => [...h.matchAll(/href="(https?:\/\/[^"]+)"/g)].map((m) => m[1])))]
    .filter((u) => !u.startsWith('https://fonts.') && !u.startsWith(SITE));
  const results = await Promise.all(urls.map(async (u) => {
    try {
      let r = await fetch(u, { method: 'HEAD', redirect: 'follow', signal: AbortSignal.timeout(20000) });
      // Some hosts refuse HEAD (the Silent context demo answers 405); ask them with GET instead.
      if (r.status === 405 || r.status === 501) r = await fetch(u, { method: 'GET', redirect: 'follow', signal: AbortSignal.timeout(30000) });
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
console.log(`${pages.length} page(s) ok (${pages.map((p) => p.path).join(', ')}): ${localCount} local files, revision ${buildInfo.updated}, version ${buildInfo.version}`);
