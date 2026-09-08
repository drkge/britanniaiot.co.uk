# Before this goes live

Everything below is a placeholder, an unverified claim, or a decision only you can make.
Work top-down; the first section will stop the site being usable if it ships as-is.

## 1. Confirmed

- **Domain:** `britanniaiot.co.uk` — confirmed. It is the canonical URL on every
  page and the entity `@id` throughout the structured data.
- **Email:** `britianniaiot@outlook.com` — confirmed as registered, including the
  `britiannia` spelling, which deliberately differs from the *Britannia* brand name
  used everywhere else on the site. Do not "correct" it in a later edit.

One thing worth doing when you have a moment: you own the domain, so a mailbox at it
(`hello@britanniaiot.co.uk`, forwarding to the Outlook account) would cost nothing and
reads better on a tender return than a free webmail address. Purely cosmetic — the site
works exactly as it is.

## 2. Placeholders that must be replaced

All of these live in the `SITE` dict at the top of `_src/build.py`. Change them there and
run `python3 _src/build.py` — they propagate to every page, the structured data, the
footer and `llms.txt`.

| Field | Current value | Note |
| --- | --- | --- |
| `phone` / `phone_display` | `+44 20 7946 0421` | **Ofcom's reserved drama range.** It cannot ring a real line, which is why it is safe as a placeholder — and why it must be replaced before launch. |
| `locality` | `London` | Used in `PostalAddress`. Change or drop for the real registered location. |
| `linkedin` | speculative URL | Remove from `sameAs` until the page actually exists — a dead `sameAs` weakens entity resolution rather than helping it. |
| `legal` | `Britannia IoT Solutions Ltd` | Confirm the exact registered name. |

Also add, once you have them: company registration number and registered office in the
footer (a legal requirement for a UK limited company's website), VAT number if registered,
and the ICO registration number in the privacy notice.

## 3. The mailbox is the only way in

There is no contact form by design, so `/contact/` is entirely `mailto:` and `tel:` links.
That removes a whole class of launch problems — nothing to configure, no form spam, no
third-party processor in the privacy notice — but it does mean **an unmonitored inbox is a
dead site**. `britianniaiot@outlook.com` needs to be somewhere it will actually be seen,
and whoever answers it needs to know about the one-working-day commitment the site makes.

The phone number is still the placeholder from section 2. A visitor calling it gets nothing.

## 4. Claims I made that you need to be able to stand behind

I have avoided inventing certifications, client counts, framework listings or staff. But
the copy does commit you to a service model. Confirm each of these is what you intend to
sell, or change the wording:

- **Subscription pricing.** The site says the service is sold as an annual per-container
  subscription covering sensor, SIM, connectivity, software, driver app, support and
  replacement hardware — not a capital purchase plus licence. This appears on
  `/solutions/`, `/faq/` and several sector pages.
- **A paid 90-day pilot on one round, measured against a pre-recorded baseline.** This is
  the offer the whole site funnels toward, and the entry point on every CTA.
- **UK-hosted data, full export, open API, no lock-in.** Stated on `/solutions/analytics-reporting/`,
  `/about/` and `/faq/`. Make sure your platform agreement actually permits all three.
- **Response within one working day** and **Monday–Friday 08:30–17:30** on `/contact/`.
- **UK-only coverage.** `/about/` states plainly that you do not work outside the UK.
- **Installation training** so customers can fit their own sensors after the first tranche.
- **API integration with third-party in-cab and CAFM systems.** Referenced on the
  contractor and estates pages. Confirm what the platform genuinely exposes.

## 5. How the case studies are framed — read this bit

Every performance figure on the site comes from the four PDFs you supplied. They are
deployments by Danish and German public bodies of the vendor's platform, not your
customers. The site handles that as follows:

- The vendor and the hardware brand are **never named** anywhere on the site.
- The four case studies are labelled as *"live deployments of the sensor and software
  platform we bring to the UK"*, with a disclosure note at the foot of each one.
- `/results/` carries an explicit FAQ, *"Are these your customers?"*, answered "No".
- `/about/` says openly that you are a young company and that these are the technology's
  track record rather than your delivery record.
- `/llms.txt` repeats the distinction so AI assistants summarising the site inherit it.

This is deliberate, and I would push back on softening it. Specific, attributable,
honestly-labelled third-party evidence is more persuasive to a council procurement team
than vague first-person claims — and it cannot blow up later in a tender clarification.

Two things worth checking with your supplier before launch:

1. **Whether they mind.** You are quoting their published marketing material. Most vendors
   are delighted; some have reseller rules about it. A one-line email now is cheaper than
   a takedown later.
2. **Your right to resell.** Everything on this site assumes you can supply this platform
   in the UK.

## 6. Legal and compliance

- **The privacy notice is a working draft.** It is flagged as such at the top of the page
  and needs a qualified review, plus your ICO registration number.
- No cookie banner is present, and none is currently needed: the site sets no cookies and
  runs no analytics. **This changes the moment you add analytics** — anything beyond
  strictly-necessary storage needs consent under PECR. If you add analytics, prefer a
  cookieless option (Plausible, Fathom) and you can keep the site banner-free.
- **Google Fonts is the one third-party request.** It sends visitor IP addresses to Google,
  which is noted in the privacy notice. Some public-sector buyers ask about this. To remove
  it entirely, self-host Inter and Newsreader in `assets/fonts/` and swap the `<link>` in
  `_src/build.py` for `@font-face` rules — about twenty minutes of work.
- Add terms of business and an accessibility statement. **Accessibility matters
  commercially here**: public sector buyers will ask, and WCAG 2.2 AA is a standard
  procurement requirement. The site is built to meet it — semantic landmarks, one `h1` per
  page, visible focus rings, `prefers-reduced-motion` honoured, keyboard-operable nav and
  accordions, and all text at or above 4.5:1 contrast — but an accessibility statement is a
  document you publish, not a property of the code.

## 7. Post-launch, in order of value

1. **Google Search Console and Bing Webmaster Tools** — verify the domain and submit
   `https://britanniaiot.co.uk/sitemap.xml`. Bing matters more than usual here: it feeds ChatGPT search.
2. **Google Business Profile** — add `sameAs` to the `Organization` JSON-LD once live.
3. **A LinkedIn company page**, then add the real URL to `SITE["linkedin"]`.
4. **Get cited off-site.** AI answer engines weight third-party mentions heavily. The
   highest-value targets are LinkedIn, LetsRecycle, MRW, Resource Magazine, the local
   authority trade press, and supplier directories such as APSE and the ESPO/YPO
   frameworks. One trade-press piece is worth more than a month of on-site tuning.
5. **Publish your own UK pilot as a fifth case study** the moment you have one. It
   immediately becomes the most valuable page on the site, and it removes the only real
   objection to the current evidence framing.
6. **Watch the AI answers directly.** Ask ChatGPT, Claude, Gemini and Perplexity things
   like *"bin fill level sensors UK suppliers"*, *"how to reduce council waste collection
   costs"*, *"radar vs ultrasonic bin sensors"* once a month, and note what they cite. That
   is your ranking report for this channel; there is no console for it yet.
