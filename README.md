# britanniaiot.co.uk

The Britannia IoT Solutions website. Plain hand-written static HTML — no build step, no
dependencies, no generator. Edit the `.html` files directly and push.

Live at <https://britanniaiot.co.uk> via GitHub Pages.

## Layout

```
index.html                 home
404.html                   served automatically by GitHub Pages
about/          contact/          faq/          how-it-works/     privacy/
solutions/      + fill-level-sensors/  route-optimisation/  analytics-reporting/
sectors/        + local-authorities/   waste-contractors/
                  universities-nhs-estates/  tourism-coastal-parks/
results/        + stralsund-smart-street-bins/  vejle-dynamic-round-planning/
                  fano-seasonal-recycling-sites/  langeland-island-recycling-network/
resources/      + waste-sensor-glossary/  sensor-led-vs-fixed-frequency-collections/
assets/css/style.css       the only stylesheet, shared by every page
assets/img/                logo, icons, Open Graph card
```

Every page is `<dir>/index.html`, which is what gives the clean URLs (`/faq/`, not
`/faq.html`). Keep that pattern for new pages.

## Local preview

```bash
./serve
```

Then <http://localhost:4173> — or `./serve 8080` for another port.

Use the server rather than double-clicking `index.html`. Links are root-relative
(`/solutions/`, `/assets/css/style.css`), which resolve against your filesystem root under
`file://`, and browsers won't serve `index.html` for a directory over `file://` either.

## GitHub Pages

Settings → Pages → deploy from `main`, root folder. Already configured; pushing to `main`
publishes.

- `CNAME` holds the custom domain. **Don't delete it** — Pages reads it on every build.
  Removing and re-adding the domain in the UI rewrites this file and creates auto-commits.
- `.nojekyll` stops GitHub running the HTML through Jekyll. Nothing here uses Liquid, and
  skipping it makes builds faster and fully predictable.
- `404.html` at the root is picked up automatically.
- The site **must** be served from a domain root. All internal links are root-relative, so
  a project-page subpath (`drkge.github.io/britanniaiot.co.uk/`) breaks every one of them.
  The custom domain is what makes it work.

DNS at LCN: four A records to `185.199.108-111.153`, four AAAA to
`2606:50c0:8000-8003::153`, and `www` CNAME to `drkge.github.io`.

## Editing

**There is no template system.** The `<head>`, header nav and footer are duplicated in
all 22 pages. A change to any of them means changing every file — usually a scripted
find-and-replace rather than 22 manual edits:

```bash
# example: change a nav label everywhere
grep -rl 'How it works' --include='*.html' . | xargs sed -i '' 's|How it works|How it&nbsp;works|g'
```

Things that live in **every** page and must be kept consistent:

| What | Where |
| --- | --- |
| Header nav + "Talk to us" button | `<header class="site-header">` |
| Footer columns, contact details, statutory line | `<footer class="site-footer">` |
| Company number 17399940, registered office | footer `.footer-legal` |
| Email `britianniaiot@outlook.com`, phone `07949 228123` | footer, plus `/contact/` |
| Organization + WebSite structured data | the `application/ld+json` block in `<head>` |

Things that are **per page** and should differ:

`<title>` (≤60 chars), `<meta name="description">` (130–158 chars), `<link rel="canonical">`,
the Open Graph tags, and the page-specific JSON-LD nodes (`WebPage`, `BreadcrumbList`,
`FAQPage`, `Service`, `Article`).

**If you add or remove a page**, update `sitemap.xml` and `llms.txt` by hand — nothing
generates them any more.

The JSON-LD is pretty-printed specifically so it can be edited in place. Keep it valid;
a broken block is worse than none.

## SEO and AI-answer files

- `robots.txt` — explicitly allows every named AI crawler (GPTBot, ClaudeBot,
  PerplexityBot, Google-Extended, Applebot-Extended and others) as well as search bots.
- `sitemap.xml` — 22 URLs. Submit to Google Search Console and Bing Webmaster Tools.
- `llms.txt` — condensed machine-readable index of the site and its key facts, for
  answer engines.
- `site.webmanifest`, `favicon.svg`, `favicon.ico`, `assets/img/apple-touch-icon.png`.

Note there is no `_headers` file. It was a Netlify/Cloudflare feature and does nothing on
GitHub Pages, so security headers and asset cache-control aren't available here. Put
Cloudflare in front of the domain if you ever want them.

## Before sharing the site widely

See [REVIEW-BEFORE-LAUNCH.md](REVIEW-BEFORE-LAUNCH.md) — outstanding items are the VAT
number, an ICO registration number for the privacy notice, and a legal review of the
privacy notice itself.

## History

The site was originally generated from a small Python builder in `_src/`. That was removed
in favour of plain HTML; it remains in the git history if you ever want to look at it.
