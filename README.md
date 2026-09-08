# Britannia IoT Solutions — website

A 24-page static marketing site. No runtime dependencies, no build step required to
deploy: upload the repository root to any static host and it works.

## Deploying

Everything at the top level is the site: plain static HTML, no build step on the server,
no runtime dependencies.

### GitHub Pages

Works as-is, with one hard requirement: **it must be served from a domain root.** Every
internal link and asset reference is root-relative (`/solutions/`, `/assets/css/style.css`)
— 999 of them. At a project-page subpath like `drkge.github.io/britannia-iot/` every one
of them breaks. So publish it either:

- at the custom domain — the `CNAME` file in this folder points Pages at
  `britanniaiot.co.uk`; add the DNS records on the registrar side (four A records to
  GitHub's apex IPs, or ALIAS/ANAME), then tick **Enforce HTTPS** in the repo's Pages
  settings once the certificate provisions; or
- from a repo named `<username>.github.io`, which also serves at a root.

Then: repo settings → Pages → deploy from branch, root folder. Clean URLs work (Pages
serves `<dir>/index.html` and redirects `/faq` → `/faq/`), and `404.html` is picked up
automatically.

Do **not** add a `.nojekyll` file. Jekyll's default behaviour is doing something useful
here: it skips `_src/` and `_headers`, so the generator source stays out of the published
site. Nothing in the built HTML uses Liquid syntax (`{{` / `{%`), so there is nothing for
Jekyll to mangle. If a Jekyll build error ever does appear, `.nojekyll` fixes it — at the
cost of publishing `_src/` publicly, which is harmless but untidy.

**What you lose on Pages:** `_headers` is a Netlify/Cloudflare file and does nothing on
GitHub Pages, so there are no security headers (HSTS, X-Frame-Options, Referrer-Policy)
and no immutable caching on `/assets/*`. Not fatal for a brochure site, but it is the one
real regression against Netlify. Putting Cloudflare in front of the domain restores the
headers if you ever want them.

### Netlify / Cloudflare Pages

Drag the folder in. `_headers` is read automatically, `404.html` is picked up, and clean
URLs work the same way.

## Local preview

```bash
./serve
```

Then http://localhost:4173 — or `./serve 8080` for a different port.

Open it through the server rather than double-clicking `index.html`: root-relative links
resolve against the filesystem root under `file://`, and browsers do not serve
`index.html` for a directory over `file://` either, so `/faq/` would not load. Any static
server works; this script is just `python3 -m http.server` with the right working
directory.

## Editing content

Page content lives in `_src/content_*.py` and is compiled to HTML by `_src/build.py`.
That indirection exists so 24 pages can share one `<head>`, one nav and one footer.

```bash
python3 _src/build.py
```

Regenerates every page plus `robots.txt`, `sitemap.xml`, `llms.txt`, `site.webmanifest`,
`favicon.svg` and `_headers`. No packages needed — standard library only.

**Edit the Python, not the generated HTML.** A direct HTML edit is silently overwritten on
the next build.

| File | Contains |
| --- | --- |
| `_src/build.py` | Page shell, nav, footer, JSON-LD, sitemap, robots.txt, llms.txt, site config |
| `_src/content_core.py` | Home, how it works, about, FAQ, contact, privacy, 404 |
| `_src/content_solutions.py` | Solutions overview, sensors, round planning, analytics |
| `_src/content_sectors.py` | Sectors overview and the four sector pages |
| `_src/content_results.py` | Results index and the four case studies |
| `_src/content_resources.py` | Glossary and the sensor-vs-fixed-frequency comparison |
| `_src/make_images.py` | Regenerates the OG card and icons (needs Pillow, macOS system fonts) |

Site-wide settings — domain, company name, email, telephone, LinkedIn — are the `SITE`
dict at the top of `_src/build.py`. Change them there and rebuild; they propagate to every
page, the structured data and `llms.txt`.

CSS is hand-written in `assets/css/style.css` and is not generated. The build stamps a
content hash onto the stylesheet URL (`style.css?v=…`) so `_headers` can cache
`/assets/*` immutably without stale-CSS problems.

## Search and AI-answer optimisation

Implemented across the build rather than bolted on:

- Unique `<title>` (≤60 chars) and meta description (130–158 chars) on every page,
  canonical URLs, Open Graph and Twitter cards, and a generated 1200×630 OG image.
- A single JSON-LD `@graph` per page linking `Organization`, `WebSite`, `WebPage`,
  `BreadcrumbList` and, where relevant, `Service`, `Product`, `Article`, `HowTo`,
  `FAQPage` and `DefinedTermSet` — all sharing one `@id` for the organisation entity.
- `robots.txt` explicitly allowing every named AI crawler (GPTBot, ClaudeBot,
  PerplexityBot, Google-Extended, Applebot-Extended and others) alongside conventional
  search bots.
- `/llms.txt` — a condensed machine-first index of the site and its key facts.
- Every page opens with a self-contained, quotable answer paragraph (`.answer-box`), which
  is what answer engines extract. Case studies and sector pages carry `.keyfacts`
  definition lists of atomic, citable facts.
- FAQ blocks phrased as real user questions, with matching `FAQPage` markup.
- Definitional (`/resources/waste-sensor-glossary/`) and comparison
  (`/resources/sensor-led-vs-fixed-frequency-collections/`) pages, the two content shapes
  that get cited most often in generated answers.
- All content is present in the raw HTML. Nothing depends on JavaScript, because most AI
  crawlers do not execute it. The only script on the site is the mobile nav toggle.
# britanniaiot.co.uk
