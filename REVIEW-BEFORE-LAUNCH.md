# Before this goes live

Everything below is a placeholder, an unverified claim, or a decision only you can make.
Work top-down; the first section will stop the site being usable if it ships as-is.

## 1. Confirmed

- **Domain:** `britanniaiot.co.uk` — confirmed. It is the canonical URL on every
  page and the entity `@id` throughout the structured data.
- **Email:** `britianniaiot@outlook.com` — confirmed as registered, including the
  `britiannia` spelling, which deliberately differs from the *Britannia* brand name
  used everywhere else on the site. Do not "correct" it in a later edit.
- **Telephone:** `07949 228123`, rendered as `tel:+447949228123` in links and
  `+44 7949 228123` in the structured data.
- **Company:** Britannia IoT Solutions Ltd, registered in England and Wales, company
  number **17399940**, incorporated 14 August 2026, status Active — verified against
  Companies House. Registered office 71-75 Shelton Street, Covent Garden, London
  WC2H 9JQ. This renders as the statutory footer line on every page, and as a `GB-COH`
  identifier plus a full `PostalAddress` in the Organization schema.
- **Location:** London, matching the registered office.

One thing worth doing when you have a moment: you own the domain, so a mailbox at it
(`hello@britanniaiot.co.uk`, forwarding to the Outlook account) would cost nothing and
reads better on a tender return than a free webmail address. Purely cosmetic — the site
works exactly as it is.

## 2. Still to add

These live in the `SITE` dict at the top of `_src/build.py`. Change them there and run
`python3 _src/build.py` — they propagate to every page, the structured data, the footer
and `llms.txt`.

- **VAT number** — `vat_number` is empty. Once registered, adding it appends a sentence to
  the footer disclosure and a `vatID` to the schema automatically.
- **Profile URLs** — `profiles` is empty, so no `sameAs` is emitted. Add a LinkedIn company
  page or Google Business Profile URL there once they genuinely exist.
- **ICO registration number** — needed in the privacy notice.

**71-75 Shelton Street is a formation agent's address.** Entirely legal and used by
thousands of companies, but it is well known as such, and council procurement teams do
occasionally look up suppliers. If you ever take a real trading address, update
`registered_office`, `street` and `postcode` in `SITE`. Not a problem, just worth knowing
someone might notice.

**The number is a mobile.** That is entirely workable and plenty of small suppliers run
this way, but council procurement teams do read a mobile-only contact as a sole-trader
signal. A cheap non-geographic or VoIP landline forwarding to it removes that impression
for a few pounds a month. Cosmetic, not urgent.

## 3. The mailbox is the only way in

There is no contact form by design, so `/contact/` is entirely `mailto:` and `tel:` links.
That removes a whole class of launch problems — nothing to configure, no form spam, no
third-party processor in the privacy notice — but it does mean **an unmonitored inbox is a
dead site**. `britianniaiot@outlook.com` needs to be somewhere it will actually be seen,
and whoever answers it needs to know about the one-working-day commitment the site makes.

The telephone number is real, so the site can now be shared without anyone reaching a dead line.

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

- **The privacy notice is now complete**, not a stub: controller identity with company
  number and registered office, what is collected, lawful basis, sharing, international
  transfers, retention periods, security, data subject rights and ICO complaint details.
  The public "draft" banner has been removed, because telling council buyers your privacy
  notice is unfinished is worse than the risk it was hedging.
  **It has still not been reviewed by a lawyer.** It was written to match how the site and
  business actually operate, which is most of the work, but that is not the same thing.
- **ICO registration.** Most UK organisations processing personal data must pay the annual
  data protection fee, though there is an exemption for processing limited to core purposes
  such as staff administration, marketing and accounts. Acting as a processor for customer
  data may take you outside it. Run the ICO's self-assessment at
  ico.org.uk/for-organisations/data-protection-fee, and if you are registrable, add the
  registration number to the privacy notice.
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
3. **A LinkedIn company page**, then add the real URL to the `profiles` list in `SITE`.
   The `sameAs` property is emitted only when that list is non-empty, so adding a URL
   there is all it takes — and leaving it empty is the correct state until the page
   genuinely exists. Same applies to a Google Business Profile or Companies House URL.
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
