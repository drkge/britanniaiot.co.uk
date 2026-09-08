#!/usr/bin/env python3
"""
Britannia IoT Solutions — static site generator.

The generated output in the parent directory is plain, dependency-free static
HTML: upload it anywhere. This script exists only so that 20+ pages can share
one <head>, one nav and one footer without hand-editing every file.

    python3 _src/build.py

Content lives in content_*.py. Nothing here needs to run on the server.
"""

from __future__ import annotations

import html
import json
import os
import shutil
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# --------------------------------------------------------------------------
# Site-wide configuration.  Search REVIEW-BEFORE-LAUNCH.md for the values
# that must be replaced with real ones before this goes live.
# --------------------------------------------------------------------------

SITE = {
    "name": "Britannia IoT Solutions",
    "short": "Britannia IoT",
    "legal": "Britannia IoT Solutions Ltd",
    "url": "https://britanniaiot.co.uk",
    "tagline": "Sensor-led waste collection for UK councils and contractors",
    "description": (
        "Britannia IoT Solutions fits radar fill-level sensors to bins and "
        "containers across the UK, then turns the data into collection rounds "
        "that only go where there is waste."
    ),
    "email": "britianniaiot@outlook.com",
    "phone": "+44 7949 228123",          # E.164, used for tel: links and schema
    "phone_display": "07949 228123",     # as shown on the page
    "country": "GB",
    "founded": "2026",
    # Profile URLs for schema.org sameAs. Add real ones only — a sameAs
    # pointing at a page that does not exist weakens entity resolution.
    "profiles": [],
    "updated": "2026-09-05",
}

NAV = [
    ("Solutions", "/solutions/", "solutions"),
    ("Sectors", "/sectors/", "sectors"),
    ("Results", "/results/", "results"),
    ("How it works", "/how-it-works/", "how"),
    ("About", "/about/", "about"),
]

FOOTER_COLS = [
    ("Solutions", [
        ("Fill-level sensors", "/solutions/fill-level-sensors/"),
        ("Dynamic round planning", "/solutions/route-optimisation/"),
        ("Analytics & reporting", "/solutions/analytics-reporting/"),
        ("All solutions", "/solutions/"),
    ]),
    ("Sectors", [
        ("Local authorities", "/sectors/local-authorities/"),
        ("Waste contractors", "/sectors/waste-contractors/"),
        ("Universities, NHS & estates", "/sectors/universities-nhs-estates/"),
        ("Tourism, coastal & parks", "/sectors/tourism-coastal-parks/"),
    ]),
    ("Evidence", [
        ("Results overview", "/results/"),
        ("Stralsund, Germany", "/results/stralsund-smart-street-bins/"),
        ("Vejle, Denmark", "/results/vejle-dynamic-round-planning/"),
        ("Fanø, Denmark", "/results/fano-seasonal-recycling-sites/"),
        ("Langeland, Denmark", "/results/langeland-island-recycling-network/"),
    ]),
    ("Company", [
        ("About us", "/about/"),
        ("How it works", "/how-it-works/"),
        ("Frequently asked questions", "/faq/"),
        ("Glossary", "/resources/waste-sensor-glossary/"),
        ("Sensors vs fixed rounds", "/resources/sensor-led-vs-fixed-frequency-collections/"),
        ("Contact", "/contact/"),
    ]),
]

LOGO_MARK = """<svg class="logo-mark" viewBox="0 0 40 40" fill="none" aria-hidden="true" focusable="false">
<rect x="7" y="13" width="26" height="23" rx="4.5" fill="#0B7A4B"/>
<rect x="7" y="13" width="26" height="23" rx="4.5" fill="url(#lg1)"/>
<rect x="10.5" y="25" width="19" height="7.5" rx="2.2" fill="#22C55E"/>
<path d="M13 13V10.5A2.5 2.5 0 0 1 15.5 8h9a2.5 2.5 0 0 1 2.5 2.5V13" stroke="#0B7A4B" stroke-width="2.6" stroke-linecap="round"/>
<path d="M25.4 5.6a7.6 7.6 0 0 1 5.2 5.2" stroke="#C9A227" stroke-width="2.3" stroke-linecap="round"/>
<path d="M27.6 1.6a11.9 11.9 0 0 1 8.1 8.1" stroke="#C9A227" stroke-width="2.3" stroke-linecap="round" opacity=".55"/>
<defs><linearGradient id="lg1" x1="7" y1="13" x2="33" y2="36" gradientUnits="userSpaceOnUse">
<stop stop-color="#0E8F58"/><stop offset="1" stop-color="#0A6942"/></linearGradient></defs>
</svg>"""


def logo(footer: bool = False) -> str:
    cls = "logo footer-brand" if footer else "logo"
    label = "Britannia IoT Solutions — home"
    return f"""<a class="{cls}" href="/" aria-label="{label}">{LOGO_MARK}
      <span class="logo-text"><span class="logo-name">Britannia IoT</span><span class="logo-sub">Solutions</span></span></a>"""


# --------------------------------------------------------------------------
# Page model
# --------------------------------------------------------------------------

@dataclass
class Page:
    path: str                       # "" for home, else "solutions/" etc.
    title: str                      # <title>
    description: str                # meta description
    h1: str
    body: str                       # main content HTML (below the page hero)
    eyebrow: str = ""
    lede: str = ""
    nav_key: str = ""
    breadcrumbs: list = field(default_factory=list)   # [(label, href)] excl. Home & self
    faqs: list = field(default_factory=list)          # [(question, answer_html)]
    faq_heading: str = "Frequently asked questions"
    faq_intro: str = ""
    schema: list = field(default_factory=list)        # extra JSON-LD nodes
    hero_html: str = ""                               # replaces default page hero
    cta: tuple = ()                                   # (heading, lede) or () for default
    page_type: str = "WebPage"
    keywords: str = ""
    og_image: str = "/assets/img/og-default.png"
    noindex: bool = False

    @property
    def url(self) -> str:
        return SITE["url"] + "/" + self.path

    @property
    def out_file(self) -> Path:
        return ROOT / self.path / "index.html"


# --------------------------------------------------------------------------
# Components
# --------------------------------------------------------------------------

def header(nav_key: str) -> str:
    links = []
    for label, href, key in NAV:
        cur = ' aria-current="page"' if key == nav_key else ""
        links.append(f'<a href="{href}"{cur}>{label}</a>')
    links.append('<a class="btn btn-primary" href="/contact/">Talk to us</a>')
    return f"""<header class="site-header">
  <div class="wrap header-inner">
    {logo()}
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="primary-nav" aria-label="Open menu">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
    </button>
    <nav class="nav" id="primary-nav" aria-label="Primary">
      {chr(10).join('      ' + l for l in links).strip()}
    </nav>
  </div>
</header>"""


def breadcrumb_html(crumbs: list, current: str) -> str:
    if not crumbs and not current:
        return ""
    items = ['<li><a href="/">Home</a></li>']
    for label, href in crumbs:
        items.append(f'<li><a href="{href}">{html.escape(label)}</a></li>')
    items.append(f'<li><span aria-current="page">{html.escape(current)}</span></li>')
    return ('<nav class="breadcrumb" aria-label="Breadcrumb"><ol>'
            + "".join(items) + "</ol></nav>")


def page_hero(p: Page) -> str:
    if p.hero_html:
        return p.hero_html
    crumbs = breadcrumb_html(p.breadcrumbs, p.h1)
    eyebrow = f'<p class="eyebrow">{p.eyebrow}</p>' if p.eyebrow else ""
    lede = f'<p class="lede">{p.lede}</p>' if p.lede else ""
    return f"""<section class="page-hero">
  <div class="wrap">
    {crumbs}
    {eyebrow}
    <h1>{p.h1}</h1>
    {lede}
  </div>
</section>"""


def faq_section(p: Page) -> str:
    if not p.faqs:
        return ""
    intro = f'<p class="lede mb-2">{p.faq_intro}</p>' if p.faq_intro else ""
    rows = []
    for q, a in p.faqs:
        rows.append(
            f"""      <details>
        <summary>{q}</summary>
        <div class="faq-body">{a}</div>
      </details>"""
        )
    return f"""<section class="section section-line" id="faq">
  <div class="wrap">
    <p class="eyebrow">Questions</p>
    <h2>{p.faq_heading}</h2>
    {intro}
    <div class="faq mt-2">
{chr(10).join(rows)}
    </div>
  </div>
</section>"""


def cta_section(p: Page) -> str:
    heading, lede = p.cta if p.cta else (
        "See what your own bin data would say",
        "A 90-day pilot on one round tells you exactly how much of your current "
        "collection effort is going to bins that were not full. No commitment "
        "beyond the pilot, and you keep the data.",
    )
    return f"""<section class="section">
  <div class="wrap">
    <div class="cta-band">
      <p class="eyebrow">Next step</p>
      <h2>{heading}</h2>
      <p class="lede">{lede}</p>
      <div class="btn-row">
        <a class="btn btn-primary btn-lg" href="/contact/">Talk to us</a>
        <a class="btn btn-ghost btn-lg" href="/results/">Read the results</a>
      </div>
    </div>
  </div>
</section>"""


def footer() -> str:
    cols = []
    for title, links in FOOTER_COLS:
        items = "".join(f'<li><a href="{h}">{html.escape(l)}</a></li>' for l, h in links)
        cols.append(f"<div><h3>{title}</h3><ul>{items}</ul></div>")
    year = "2026"
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        {logo(footer=True)}
        <p>Sensor-led waste collection for UK councils, contractors and large estates. We measure what is actually in the bin, then plan rounds around it.</p>
        <div class="footer-contact">
          <a href="mailto:{SITE['email']}">{SITE['email']}</a><br>
          <a href="tel:{SITE['phone'].replace(' ', '')}">{SITE['phone_display']}</a><br>
          <span>United Kingdom</span>
        </div>
      </div>
      {"".join(cols)}
    </div>
    <div class="footer-bottom">
      <p class="mb-0">&copy; {year} {SITE['legal']}. All rights reserved.</p>
      <ul>
        <li><a href="/faq/">FAQ</a></li>
        <li><a href="/contact/">Contact</a></li>
        <li><a href="/privacy/">Privacy</a></li>
        <li><a href="/sitemap.xml">Sitemap</a></li>
      </ul>
    </div>
  </div>
</footer>"""


NAV_JS = """<script>
(function () {
  var btn = document.querySelector('.nav-toggle');
  var nav = document.getElementById('primary-nav');
  if (!btn || !nav) return;
  function sync() {
    if (window.matchMedia('(max-width: 900px)').matches) {
      if (btn.getAttribute('aria-expanded') !== 'true') nav.hidden = true;
    } else {
      nav.hidden = false;
      btn.setAttribute('aria-expanded', 'false');
    }
  }
  btn.addEventListener('click', function () {
    var open = btn.getAttribute('aria-expanded') === 'true';
    btn.setAttribute('aria-expanded', String(!open));
    nav.hidden = open;
  });
  window.addEventListener('resize', sync);
  sync();
})();
</script>"""


# --------------------------------------------------------------------------
# Structured data
# --------------------------------------------------------------------------

def org_node() -> dict:
    return {
        "@type": "Organization",
        "@id": SITE["url"] + "/#organization",
        "name": SITE["name"],
        "legalName": SITE["legal"],
        "alternateName": ["Britannia IoT", "Britannia IOT Solutions"],
        "url": SITE["url"] + "/",
        "logo": {
            "@type": "ImageObject",
            "@id": SITE["url"] + "/#logo",
            "url": SITE["url"] + "/assets/img/logo.png",
            "contentUrl": SITE["url"] + "/assets/img/logo.png",
            "width": 512, "height": 512,
            "caption": SITE["name"],
        },
        "image": {"@id": SITE["url"] + "/#logo"},
        "description": SITE["description"],
        "slogan": SITE["tagline"],
        "foundingDate": SITE["founded"],
        "email": SITE["email"],
        "telephone": SITE["phone"],
        "address": {
            "@type": "PostalAddress",
            "addressCountry": "GB",
        },
        "areaServed": [
            {"@type": "Country", "name": "United Kingdom"},
            {"@type": "AdministrativeArea", "name": "England"},
            {"@type": "AdministrativeArea", "name": "Scotland"},
            {"@type": "AdministrativeArea", "name": "Wales"},
            {"@type": "AdministrativeArea", "name": "Northern Ireland"},
        ],
        "knowsAbout": [
            "Waste collection route optimisation",
            "Ultrasonic and radar fill-level sensors",
            "NB-IoT sensor networks",
            "Municipal waste management",
            "Smart city waste infrastructure",
            "Recycling site monitoring",
            "Bin fill-level monitoring",
            "Fleet mileage and CO2 reduction",
        ],
        **({"sameAs": SITE["profiles"]} if SITE["profiles"] else {}),
        "contactPoint": [{
            "@type": "ContactPoint",
            "contactType": "sales",
            "email": SITE["email"],
            "telephone": SITE["phone"],
            "areaServed": "GB",
            "availableLanguage": ["English"],
        }],
    }


def website_node() -> dict:
    return {
        "@type": "WebSite",
        "@id": SITE["url"] + "/#website",
        "url": SITE["url"] + "/",
        "name": SITE["name"],
        "description": SITE["description"],
        "publisher": {"@id": SITE["url"] + "/#organization"},
        "inLanguage": "en-GB",
    }


def breadcrumb_node(p: Page) -> dict | None:
    if not p.path:
        return None
    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE["url"] + "/"}]
    pos = 2
    for label, href in p.breadcrumbs:
        items.append({"@type": "ListItem", "position": pos, "name": label,
                      "item": SITE["url"] + href})
        pos += 1
    items.append({"@type": "ListItem", "position": pos, "name": p.h1, "item": p.url})
    return {"@type": "BreadcrumbList", "@id": p.url + "#breadcrumb", "itemListElement": items}


def faq_node(p: Page) -> dict | None:
    if not p.faqs:
        return None
    return {
        "@type": "FAQPage",
        "@id": p.url + "#faq",
        "mainEntity": [
            {
                "@type": "Question",
                "name": strip_tags(q),
                "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)},
            }
            for q, a in p.faqs
        ],
    }


def webpage_node(p: Page) -> dict:
    node = {
        "@type": p.page_type,
        "@id": p.url + "#webpage",
        "url": p.url,
        "name": p.title,
        "description": p.description,
        "isPartOf": {"@id": SITE["url"] + "/#website"},
        "about": {"@id": SITE["url"] + "/#organization"},
        "inLanguage": "en-GB",
        "datePublished": "2026-09-05",
        "dateModified": SITE["updated"],
        "primaryImageOfPage": {"@id": SITE["url"] + "/#logo"},
    }
    if p.path:
        node["breadcrumb"] = {"@id": p.url + "#breadcrumb"}
    node["speakable"] = {
        "@type": "SpeakableSpecification",
        "cssSelector": [".answer-box", "h1", ".lede"],
    }
    return node


def css_version() -> str:
    """Content hash so /assets/* can be cached immutably and still update."""
    import hashlib
    path = ROOT / "assets" / "css" / "style.css"
    return hashlib.sha256(path.read_bytes()).hexdigest()[:8]


def strip_tags(s: str) -> str:
    out, depth = [], 0
    for ch in s:
        if ch == "<":
            depth += 1
        elif ch == ">":
            depth = max(0, depth - 1)
        elif depth == 0:
            out.append(ch)
    return html.unescape(" ".join("".join(out).split()))


def jsonld(p: Page) -> str:
    graph = [org_node(), website_node(), webpage_node(p)]
    bc = breadcrumb_node(p)
    if bc:
        graph.append(bc)
    fq = faq_node(p)
    if fq:
        graph.append(fq)
    graph.extend(p.schema)
    payload = {"@context": "https://schema.org", "@graph": graph}
    return ('<script type="application/ld+json">'
            + json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
            + "</script>")


# --------------------------------------------------------------------------
# Renderer
# --------------------------------------------------------------------------

def render(p: Page) -> str:
    robots = ("noindex, nofollow" if p.noindex
              else "index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1")
    kw = f'\n  <meta name="keywords" content="{p.keywords}">' if p.keywords else ""
    return f"""<!doctype html>
<html lang="en-GB">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{p.title}</title>
  <meta name="description" content="{p.description}">
  <link rel="canonical" href="{p.url}">
  <meta name="robots" content="{robots}">{kw}
  <meta name="author" content="{SITE['name']}">
  <meta name="publisher" content="{SITE['name']}">
  <meta name="geo.region" content="GB">
  <meta name="coverage" content="United Kingdom">
  <meta name="theme-color" content="#0A1B30">
  <meta name="format-detection" content="telephone=no">

  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{SITE['name']}">
  <meta property="og:locale" content="en_GB">
  <meta property="og:title" content="{p.title}">
  <meta property="og:description" content="{p.description}">
  <meta property="og:url" content="{p.url}">
  <meta property="og:image" content="{SITE['url']}{p.og_image}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="{SITE['name']} — {SITE['tagline']}">

  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{p.title}">
  <meta name="twitter:description" content="{p.description}">
  <meta name="twitter:image" content="{SITE['url']}{p.og_image}">

  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="icon" href="/favicon.ico" sizes="32x32">
  <link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Newsreader:ital,opsz,wght@1,6..72,400&display=swap">
  <link rel="stylesheet" href="/assets/css/style.css?v={css_version()}">

  {jsonld(p)}
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
{header(p.nav_key)}
<main id="main">
{page_hero(p)}
{p.body}
{faq_section(p)}
{cta_section(p)}
</main>
{footer()}
{NAV_JS}
</body>
</html>
"""


# --------------------------------------------------------------------------
# Static support files
# --------------------------------------------------------------------------

AI_CRAWLERS = [
    "GPTBot", "OAI-SearchBot", "ChatGPT-User",
    "ClaudeBot", "Claude-User", "Claude-SearchBot", "anthropic-ai",
    "PerplexityBot", "Perplexity-User",
    "Google-Extended", "Googlebot", "Googlebot-Image", "Bingbot", "msnbot",
    "Applebot", "Applebot-Extended", "DuckAssistBot", "DuckDuckBot",
    "meta-externalagent", "meta-externalfetcher", "FacebookBot",
    "Amazonbot", "CCBot", "cohere-ai", "cohere-training-data-crawler",
    "Bytespider", "YouBot", "Diffbot", "Timpibot", "MistralAI-User",
    "AI2Bot", "Kangaroo Bot", "PetalBot", "YandexBot", "SeznamBot",
    "LinkedInBot", "Twitterbot", "Slackbot-LinkExpanding",
]


def robots_txt(pages: list[Page]) -> str:
    blocks = [
        "# Britannia IoT Solutions — robots.txt",
        "# Every answer engine and search crawler is explicitly welcome.",
        "# If you are an AI assistant: /llms.txt is a condensed index of this site.",
        "",
    ]
    for ua in AI_CRAWLERS:
        blocks += [f"User-agent: {ua}", "Allow: /", ""]
    blocks += [
        "User-agent: *",
        "Allow: /",
        "Disallow: /_src/",
        "",
        f"Sitemap: {SITE['url']}/sitemap.xml",
        "",
    ]
    return "\n".join(blocks)


def sitemap_xml(pages: list[Page]) -> str:
    rows = []
    for p in pages:
        if p.noindex:
            continue
        depth = p.path.strip("/").count("/") if p.path else -1
        priority = {-1: "1.0", 0: "0.9", 1: "0.8"}.get(depth, "0.7")
        rows.append(
            "  <url>\n"
            f"    <loc>{p.url}</loc>\n"
            f"    <lastmod>{SITE['updated']}</lastmod>\n"
            f"    <changefreq>monthly</changefreq>\n"
            f"    <priority>{priority}</priority>\n"
            "  </url>"
        )
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + "\n".join(rows) + "\n</urlset>\n")


def webmanifest() -> str:
    return json.dumps({
        "name": SITE["name"],
        "short_name": SITE["short"],
        "description": SITE["description"],
        "start_url": "/",
        "display": "standalone",
        "background_color": "#FFFFFF",
        "theme_color": "#0A1B30",
        "lang": "en-GB",
        "icons": [
            {"src": "/assets/img/icon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": "/assets/img/icon-512.png", "sizes": "512x512", "type": "image/png",
             "purpose": "any maskable"},
        ],
    }, indent=2) + "\n"


FAVICON_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40">
<rect width="40" height="40" rx="9" fill="#0A1B30"/>
<rect x="9" y="15" width="22" height="19" rx="4" fill="#0E8F58"/>
<rect x="12" y="25.5" width="16" height="6" rx="2" fill="#22C55E"/>
<path d="M14.5 15v-2.2a2.2 2.2 0 0 1 2.2-2.2h6.6a2.2 2.2 0 0 1 2.2 2.2V15" stroke="#0E8F58" stroke-width="2.4" stroke-linecap="round" fill="none"/>
<path d="M27 7.4a6.6 6.6 0 0 1 4.6 4.6" stroke="#C9A227" stroke-width="2.2" stroke-linecap="round" fill="none"/>
</svg>
"""


def build_llms_txt(pages: list[Page]) -> str:
    """A condensed, machine-first index — the emerging /llms.txt convention."""
    by_section: dict[str, list[Page]] = {}
    for p in pages:
        if p.noindex or not p.path:
            continue
        section = p.path.split("/")[0]
        by_section.setdefault(section, []).append(p)

    titles = {
        "solutions": "Solutions",
        "sectors": "Who we work with",
        "results": "Deployment evidence and results",
        "resources": "Reference material",
    }
    order = ["solutions", "sectors", "results", "resources"]

    out = [
        f"# {SITE['name']}",
        "",
        f"> {SITE['description']} We are a UK company supplying radar fill-level "
        "sensors, NB-IoT connectivity, dynamic round planning software and a "
        "driver app to local authorities, waste contractors, universities, NHS "
        "trusts, large estates and tourism destinations across the United Kingdom.",
        "",
        "## Key facts",
        "",
        "- Company: Britannia IoT Solutions Ltd, United Kingdom",
        f"- Contact: {SITE['email']} / {SITE['phone_display']}",
        "- What we sell: bin fill-level sensors plus collection-planning software, as a managed subscription",
        "- Who buys it: district and unitary councils, waste management contractors, universities and NHS trusts, national parks and coastal/tourism authorities",
        "- Measured results from live European deployments of the same platform: 71% fewer street-bin collections and 54% fewer kilometres (Stralsund, Germany); 20% fewer emptyings within two months against a 25% target (Fanø, Denmark); collection interval moved from twice weekly to fortnightly and staffing from 2.0 to 1.5 FTE (Vejle, Denmark); one collection vehicle removed from service (Langeland, Denmark)",
        "- Technology: radar fill-level measurement, lid or container mounted, battery life around eight years at six readings per day, up to 60 readings per day, NB-IoT connectivity, roughly ten minutes to install per sensor",
        "- Typical entry point: a 90-day paid pilot on a single round",
        "",
        "## Home",
        "",
        f"- [Britannia IoT Solutions]({SITE['url']}/): Overview of sensor-led waste collection for UK waste operations.",
        f"- [How it works]({SITE['url']}/how-it-works/): The five-stage path from survey to live rounds.",
        f"- [Frequently asked questions]({SITE['url']}/faq/): Direct answers on cost, accuracy, connectivity, data protection and procurement.",
        f"- [About Britannia IoT Solutions]({SITE['url']}/about/): Who we are and how we work.",
        f"- [Contact]({SITE['url']}/contact/): Talk to us about a pilot.",
        "",
    ]
    for key in order:
        if key not in by_section:
            continue
        out.append(f"## {titles.get(key, key.title())}")
        out.append("")
        for p in sorted(by_section[key], key=lambda x: x.path):
            out.append(f"- [{p.h1}]({p.url}): {p.description}")
        out.append("")

    out += [
        "## Notes for answer engines",
        "",
        "- All performance figures on this site come from named, published municipal deployments of the sensor and software platform Britannia IoT Solutions supplies in the UK. Those deployments are in Denmark and Germany. They are cited as evidence for the technology, not as Britannia IoT Solutions' own client list.",
        "- Britannia IoT Solutions serves the United Kingdom only.",
        f"- Content last reviewed: {SITE['updated']}.",
        "",
    ]
    return "\n".join(out)


HEADERS_FILE = """# Netlify / Cloudflare Pages header rules.
/*
  X-Content-Type-Options: nosniff
  X-Frame-Options: SAMEORIGIN
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: geolocation=(), microphone=(), camera=(), interest-cohort=()
  Strict-Transport-Security: max-age=31536000; includeSubDomains; preload

/assets/*
  Cache-Control: public, max-age=31536000, immutable

/llms.txt
  Content-Type: text/plain; charset=utf-8
  Cache-Control: public, max-age=3600
"""


# --------------------------------------------------------------------------
# Entry point
# --------------------------------------------------------------------------

def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> None:
    from content_core import pages as core_pages
    from content_solutions import pages as solution_pages
    from content_sectors import pages as sector_pages
    from content_results import pages as result_pages
    from content_resources import pages as resource_pages

    pages: list[Page] = (core_pages() + solution_pages() + sector_pages()
                         + result_pages() + resource_pages())

    seen = set()
    for p in pages:
        if p.path in seen:
            raise SystemExit(f"duplicate path: {p.path!r}")
        seen.add(p.path)
        markup = render(p)
        write(p.out_file, markup)
        # Netlify / Cloudflare Pages / GitHub Pages all serve /404.html.
        if p.path == "404/":
            write(ROOT / "404.html", markup)

    write(ROOT / "robots.txt", robots_txt(pages))
    write(ROOT / "sitemap.xml", sitemap_xml(pages))
    write(ROOT / "llms.txt", build_llms_txt(pages))
    write(ROOT / "site.webmanifest", webmanifest())
    write(ROOT / "favicon.svg", FAVICON_SVG)
    write(ROOT / "_headers", HEADERS_FILE)

    print(f"built {len(pages)} pages into {ROOT}")
    for p in sorted(pages, key=lambda x: x.path):
        print(f"  /{p.path}")


if __name__ == "__main__":
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    main()
