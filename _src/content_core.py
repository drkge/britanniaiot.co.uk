"""Home, how-it-works, about, FAQ, contact, privacy, 404."""

from build import Page, SITE

# ---------------------------------------------------------------- shared --

ICON = {
    "radar": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M12 12v9"/><path d="M5 20h14"/><circle cx="12" cy="9" r="1.6"/><path d="M8.8 12.2a4.5 4.5 0 0 1 0-6.4"/><path d="M15.2 5.8a4.5 4.5 0 0 1 0 6.4"/><path d="M6.2 14.8a8.2 8.2 0 0 1 0-11.6"/><path d="M17.8 3.2a8.2 8.2 0 0 1 0 11.6"/></svg>',
    "route": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><circle cx="5" cy="5" r="2.4"/><circle cx="19" cy="19" r="2.4"/><path d="M5 7.4v4.1A4.5 4.5 0 0 0 9.5 16h5A4.5 4.5 0 0 1 19 20.5v-4"/><path d="M16.4 13.2 19 16l2.6-2.8"/></svg>',
    "chart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M3 21h18"/><rect x="4" y="12" width="3.6" height="6" rx="1"/><rect x="10.2" y="7" width="3.6" height="11" rx="1"/><rect x="16.4" y="3.5" width="3.6" height="14.5" rx="1"/></svg>',
    "truck": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M2 6.5h11.5v9.5H2z"/><path d="M13.5 10h4l3.5 3.3V16h-7.5"/><circle cx="6.5" cy="18.5" r="2"/><circle cx="17" cy="18.5" r="2"/></svg>',
    "leaf": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20c0-8 5-13 16-14 0 11-5 15-11 15-2.8 0-5-1.2-5-1z"/><path d="M9.5 14.5C12 12 14.5 10.8 17 10.2"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l7.5 3v5.6c0 4.6-3.1 8.3-7.5 9.4-4.4-1.1-7.5-4.8-7.5-9.4V6z"/><path d="M9 12.2l2.1 2.1L15.3 10"/></svg>',
    "signal": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M4.5 19.5v-4"/><path d="M9.5 19.5v-8"/><path d="M14.5 19.5v-12"/><path d="M19.5 19.5v-16"/></svg>',
    "people": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="8" r="3.2"/><path d="M2.8 20a6.4 6.4 0 0 1 12.4 0"/><path d="M16.5 5.3a3.2 3.2 0 0 1 0 5.6"/><path d="M18 14.4A6.4 6.4 0 0 1 21.4 20"/></svg>',
    "clipboard": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="4.5" width="14" height="16" rx="2.2"/><path d="M9 4.5V3.4A1.4 1.4 0 0 1 10.4 2h3.2A1.4 1.4 0 0 1 15 3.4v1.1z"/><path d="M9 11h6M9 15h4"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><rect x="2.8" y="5" width="18.4" height="14" rx="2.6"/><path d="m3.6 6.8 7.3 5.4a2 2 0 0 0 2.2 0l7.3-5.4"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M8.1 3.3 9.9 7 8 9a12.5 12.5 0 0 0 7 7l2-1.9 3.7 1.8v3a2 2 0 0 1-2.2 2A17.6 17.6 0 0 1 3.1 5.5a2 2 0 0 1 2-2.2z"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5.3l3.4 2"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21.5c4.4-4.6 6.6-8 6.6-10.6a6.6 6.6 0 1 0-13.2 0c0 2.6 2.2 6 6.6 10.6z"/><circle cx="12" cy="10.7" r="2.5"/></svg>',
    "pound": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M15.5 6.4A3.9 3.9 0 0 0 9 9.2V13c0 2.2-1 3.6-2.5 4.4h11"/><path d="M6.5 12.4h6.8"/></svg>',
}


def icon_card(key, title, body, href=None, cta=None):
    tag = "a" if href else "div"
    attrs = f' href="{href}"' if href else ""
    foot = f'<span class="arrow-link">{cta}</span>' if href and cta else ""
    return (f'<{tag} class="card"{attrs}><span class="card-icon">{ICON[key]}</span>'
            f"<h3>{title}</h3><p>{body}</p>{foot}</{tag}>")


# ------------------------------------------------------------------ home --

HOME_HERO = """<section class="hero hero-center">
  <div class="wrap">
    <p class="hero-pill"><span class="dot"></span> Radar fill-level sensors &middot; NB-IoT &middot; UK deployment</p>
    <h1>Collect the bins that are full. Skip the ones that aren't.</h1>
    <p class="lede">Britannia IoT Solutions fits radar fill-level sensors to street bins, communal containers and bring sites across the UK, then rebuilds your collection rounds around what the data actually says. Public bodies already running this platform in Europe have cut collections by up to 71% and vehicle mileage by more than half.</p>
    <div class="btn-row mt-2">
      <a class="btn btn-primary btn-lg" href="/contact/">Talk to us</a>
      <a class="btn btn-ghost btn-lg" href="/results/">See the measured results</a>
    </div>
  </div>
  <div class="wrap mt-3">
    <div class="stat-band">
      <div class="stat"><span class="stat-num">71%</span><span class="stat-label">fewer street-bin collections per week</span><span class="stat-src">Stralsund, Germany</span></div>
      <div class="stat"><span class="stat-num">54%</span><span class="stat-label">fewer kilometres driven per week</span><span class="stat-src">Stralsund, Germany</span></div>
      <div class="stat"><span class="stat-num">&lt;12</span><span class="stat-label">months to pay back the investment</span><span class="stat-src">Stralsund, Germany</span></div>
      <div class="stat"><span class="stat-num">8 yrs</span><span class="stat-label">sensor battery life at six readings a day</span><span class="stat-src">Manufacturer specification</span></div>
    </div>
  </div>
</section>"""

HOME_BODY = f"""
<section class="section">
  <div class="wrap">
    <div class="split">
      <div>
        <p class="eyebrow">What we do</p>
        <h2>Sensor-led collection, in one sentence</h2>
        <p>No jargon, no smart-city framing. A bin reports how full it is; the round goes to the ones that are.</p>
      </div>
      <div>
        <div class="answer-box">
          <p><strong>Britannia IoT Solutions is a UK company that fits radar fill-level sensors inside bins and waste containers, streams the readings over the NB-IoT mobile network, and uses them to generate a daily collection round that visits only the containers actually approaching full.</strong></p>
          <p class="mt-1">The result is fewer collections, fewer miles, fewer complaints about overflowing bins, and a documented record of every emptying. Councils, waste contractors, universities, NHS trusts and parks authorities all buy it for the same reason: fixed-frequency rounds send crews to bins nobody used.</p>
        </div>
        <a class="arrow-link" href="/how-it-works/">See the five stages from survey to live rounds</a>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt section-line">
  <div class="wrap">
    <p class="eyebrow">The problem</p>
    <h2 class="measure">Fixed rounds are a guess, and the guess is expensive</h2>
    <p class="lede">Almost every public bin in Britain is emptied on a timetable set years ago, by someone estimating how busy each location would be. Usage has moved since. The timetable hasn't.</p>
    <div class="grid grid-3 mt-3">
      <div class="card no-push">
        <span class="card-num">01</span>
        <h3>You pay to lift empty bins</h3>
        <p>When Stralsund instrumented 35 town-centre bins, the data showed some sat virtually empty between twice-weekly visits while others filled far faster than anyone expected. Every visit to the first group was cost with no output.</p>
      </div>
      <div class="card no-push">
        <span class="card-num">02</span>
        <h3>And the busy ones still overflow</h3>
        <p>A timetable cannot respond to a heatwave, a bank holiday, a festival or a coach party. The bins that generate complaints, photographs and councillor emails are precisely the ones a fixed frequency under-serves.</p>
      </div>
      <div class="card no-push">
        <span class="card-num">03</span>
        <h3>Nobody can prove what happened</h3>
        <p>When a resident says a bin has not been emptied for a fortnight, most operations have no record to check. Sensor history turns that argument into a timestamped answer you can send back the same day.</p>
      </div>
    </div>
    <div class="pullquote mt-3">
      <blockquote>We simply cannot plan our emptyings, because a few days of sunshine can change the picture completely. So far the emptying has taken place by gut feeling.</blockquote>
      <cite><b>Senior engineer, technical administration</b> &mdash; Fan&oslash; Municipality, Denmark, before deployment</cite>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="eyebrow">Solutions</p>
    <h2 class="measure">Three parts, sold as one managed service</h2>
    <p class="lede">You are not buying hardware and then working out what to do with it. Sensors, connectivity, planning software, the driver app and the reporting arrive together on a single subscription.</p>
    <div class="grid grid-3 mt-3">
      {icon_card("radar", "Radar fill-level sensors", "Lid-mounted or container-mounted radar that measures the real fill level of the waste beneath it &mdash; including awkward materials like cardboard, paper and film plastic that defeat older ultrasonic units. Around ten minutes to install. No wiring, no drilling into the shell.", "/solutions/fill-level-sensors/", "Sensors and connectivity")}
      {icon_card("route", "Dynamic round planning", "Every morning the platform builds an optimised round from overnight readings, then pushes it to the driver's tablet with live fill percentages, locations and navigation. Drivers confirm each lift and report damage on the spot.", "/solutions/route-optimisation/", "Rounds and the driver app")}
      {icon_card("chart", "Analytics &amp; reporting", "Fill history for every container, heat maps of genuine demand, evidence for complaint responses, mileage and CO&#8322; reporting for your climate commitments, and the data to rationalise a bin estate that has grown by accretion.", "/solutions/analytics-reporting/", "Reporting and forecasting")}
    </div>
  </div>
</section>

<section class="section section-dark">
  <div class="wrap">
    <p class="eyebrow">Evidence</p>
    <h2 class="measure">Four public bodies, four different problems, measured outcomes</h2>
    <p class="lede">These are live deployments of the sensor and software platform we bring to the UK. They are published municipal case studies from Denmark and Germany &mdash; the technology's track record, honestly labelled, rather than a client list of our own.</p>
    <div class="grid grid-2 mt-3">
      <a class="card case-card" href="/results/stralsund-smart-street-bins/">
        <span class="case-flag">Stralsund, Germany &middot; 55,000 residents</span>
        <p class="case-headline">71% fewer collections</p>
        <h3>Town-centre street bins</h3>
        <p>Weekly collections fell from 1,548 to 445 and weekly mileage from 1,677&nbsp;km to 779&nbsp;km across 35 instrumented 60-litre bins. Working hours down 30%. The pilot paid for itself inside a year and was extended by a further 100 sensors.</p>
        <span class="arrow-link">Read the Stralsund result</span>
      </a>
      <a class="card case-card" href="/results/vejle-dynamic-round-planning/">
        <span class="case-flag">Vejle, Denmark &middot; 875 public bins</span>
        <p class="case-headline">Twice weekly &rarr; fortnightly</p>
        <h3>Municipality-wide rollout</h3>
        <p>547 bins across 2,000&nbsp;km of roads now generate an optimised round automatically at 05:00 each day. Crewing fell from 2.0 to 1.5 full-time staff, with targets of 30% less travel, a 40% economic gain and 5.5 tonnes of CO&#8322; saved a year.</p>
        <span class="arrow-link">Read the Vejle result</span>
      </a>
      <a class="card case-card" href="/results/fano-seasonal-recycling-sites/">
        <span class="case-flag">Fan&oslash;, Denmark &middot; population 3,000&ndash;50,000 by season</span>
        <p class="case-headline">20% fewer emptyings in 8 weeks</p>
        <h3>Seasonal recycling sites</h3>
        <p>82 semi-buried containers across 14 sites on an island whose population multiplies sixteenfold in summer. Within two months of switching on, emptyings were down 20% against a 25% target &mdash; and residents stopped finding overflowing containers.</p>
        <span class="arrow-link">Read the Fan&oslash; result</span>
      </a>
      <a class="card case-card" href="/results/langeland-island-recycling-network/">
        <span class="case-flag">Langeland, Denmark &middot; 220 sensors</span>
        <p class="case-headline">One vehicle removed</p>
        <h3>Rural bring-site network</h3>
        <p>A 176&nbsp;km manual inspection round that consumed a day and a half every cycle was replaced by readings updated every six hours. The utility took a collection vehicle off the road and has had one sensor fault in 220 units.</p>
        <span class="arrow-link">Read the Langeland result</span>
      </a>
    </div>
    <p class="note" style="border-color:rgba(255,255,255,.14);color:#8FADCA">Figures as published by the operating authorities. Britannia IoT Solutions supplies the same sensor and software platform in the United Kingdom. Your own results will depend on your bin density, current collection frequency and round geography &mdash; which is exactly what a pilot is for.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="eyebrow">Who we work with</p>
    <h2 class="measure">Built for the way British waste operations are actually run</h2>
    <p class="lede">Different buyers, different maths. A unitary authority is protecting a service budget; a contractor is protecting a margin; an estates team just wants the overflowing bin outside the library to stop being a problem.</p>
    <div class="grid grid-4 mt-3">
      <a class="card" href="/sectors/local-authorities/"><span class="card-icon">{ICON["clipboard"]}</span><h3>District &amp; unitary councils</h3><p>Street bins, bring sites, HWRCs and communal housing containers &mdash; with the audit trail your members and complaints team keep asking for.</p><span class="arrow-link">For councils</span></a>
      <a class="card" href="/sectors/waste-contractors/"><span class="card-icon">{ICON["truck"]}</span><h3>Waste management contractors</h3><p>Protect margin on fixed-price contracts, evidence SLA performance, and go into the next tender with data nobody else in the room has.</p><span class="arrow-link">For contractors</span></a>
      <a class="card" href="/sectors/universities-nhs-estates/"><span class="card-icon">{ICON["people"]}</span><h3>Universities, NHS &amp; estates</h3><p>Dense bin estates, one decision-maker, no procurement framework friction. Term-time and shift patterns make demand wildly uneven &mdash; and predictable.</p><span class="arrow-link">For estates teams</span></a>
      <a class="card" href="/sectors/tourism-coastal-parks/"><span class="card-icon">{ICON["leaf"]}</span><h3>Tourism, coastal &amp; parks</h3><p>Where the population multiplies in July and the beach car park bin overflows by Saturday lunchtime. Seasonality is where sensors earn most.</p><span class="arrow-link">For visitor destinations</span></a>
    </div>
  </div>
</section>

<section class="section section-alt section-line">
  <div class="wrap">
    <div class="split split-top">
      <div>
        <p class="eyebrow">Why us</p>
        <h2>What you should expect from a supplier</h2>
        <p class="lede">There are cheap sensors and there is a working service. The difference shows up in year two, when the batteries need changing and nobody can remember which bin has which unit.</p>
        <div class="btn-row mt-2">
          <a class="btn btn-ghost" href="/about/">More about how we work</a>
        </div>
      </div>
      <div>
        <ul class="feature-list">
          <li><strong>Radar, not ultrasonic.</strong> Ultrasonic sensors misread cardboard, paper and film plastic, and produce the false readings that kill pilots. Vejle switched suppliers after an earlier trial produced error reports on up to 30% of readings.</li>
          <li><strong>One accountable service.</strong> Sensors, SIMs, connectivity, software, driver app and support on a single subscription. No integration project you have to run yourself.</li>
          <li><strong>A pilot with a real answer at the end.</strong> 90 days on one round, with a baseline taken before we start, so the business case is arithmetic rather than a brochure claim.</li>
          <li><strong>Designed for the people doing the job.</strong> If drivers do not trust the round, the project fails. The app shows them why each stop is on the list and lets them push back.</li>
          <li><strong>Data that stays yours.</strong> Full export, open API, UK-hosted. If you ever leave, you leave with your history.</li>
        </ul>
      </div>
    </div>
  </div>
</section>
"""

HOME_FAQS = [
    ("What does Britannia IoT Solutions actually do?",
     "<p>We fit radar fill-level sensors to bins, containers and bring sites, connect them to the NB-IoT mobile network, and provide the software that turns those readings into a daily collection round, a driver app and a reporting dashboard. It is sold as one managed subscription covering hardware, connectivity, software and support, so there is no separate integration project for your team to run.</p>"),
    ("How much can a council realistically save?",
     "<p>The honest answer is that it depends entirely on how over-serviced your current rounds are, and no supplier can tell you before measuring. Published municipal deployments of this platform give a range: Stralsund cut weekly street-bin collections by 71% and mileage by 54%; Fan&oslash; reduced emptyings by 20% within two months against a 25% target; Vejle moved from twice-weekly to fortnightly collection and reduced crewing from 2.0 to 1.5 full-time staff. The largest gains come where bins are currently emptied on a fixed frequency regardless of use, and where round geography involves long drives between stops.</p>"),
    ("How accurate are the sensors, and what about cardboard and plastic?",
     "<p>The sensors use radar rather than ultrasound. That matters because ultrasonic sensors scatter badly off irregular, sound-absorbing materials &mdash; flattened cardboard, paper and film plastic in particular &mdash; which is the usual cause of false readings in recycling containers. Vejle Municipality moved to radar after an earlier non-radar trial produced error reports on up to 30% of readings, and now reports very few faults. A learning algorithm also improves per-container accuracy over the first weeks as it builds a profile of that specific bin.</p>"),
    ("Do the bins need power, wiring or modification?",
     "<p>No. Each sensor is a self-contained sealed unit with its own battery, mounted inside the lid or the top of the container. Battery life is around eight years at six readings a day. Installation takes roughly ten minutes per bin, and operations staff routinely fit replacements themselves while out on a round. There is no cabling, no mains supply and no structural modification to the container.</p>"),
    ("How long does a rollout take?",
     "<p>A typical pilot is live within four to six weeks of go-ahead: a week to survey and confirm the bin register, two to three weeks for hardware and SIM provisioning, and a few days to install and calibrate. We recommend running the pilot for 90 days so the data covers more than one demand pattern. Full rollouts are usually phased round by round rather than done in one weekend, which keeps the service stable and lets the round plans settle.</p>"),
    ("Will it work alongside our existing contractor or in-cab system?",
     "<p>Yes. Contractors can be given their own login and receive rounds directly in the driver app, confirming each lift as they go &mdash; which is how Fan&oslash; runs it, and it also produces clean invoicing data. Where you already run an in-cab or route management system, fill-level data can be fed to it through the API instead, so crews keep the interface they know. Which route makes sense is one of the first things we work out when we talk.</p>"),
]


# ------------------------------------------------------- how it works -----

HOW_BODY = """
<section class="section">
  <div class="wrap wrap-narrow">
    <div class="answer-box">
      <p><strong>Getting from a fixed timetable to sensor-led collection takes about four to six weeks to pilot and runs in five stages: survey the bin estate and take a baseline, install the sensors, connect and calibrate them, switch round planning over to live data, then measure and rationalise.</strong></p>
      <p class="mt-1">Nothing here requires you to change vehicles, depots or crews. The change is which bins the round visits, and on which day.</p>
    </div>
  </div>
</section>

<section class="section-tight">
  <div class="wrap wrap-narrow">
    <div class="steps">
      <div class="step">
        <h3>Survey the estate and take a baseline</h3>
        <p>We work through your bin register with you: container type, capacity, GPS position, current collection frequency and who does the lifting. This stage is unglamorous and it is the one that decides whether the project works. Vejle's operations team are explicit that a clean location database, owned by one named person, is the precondition for everything downstream. At the same time we record what you spend today &mdash; lifts, hours, mileage, fuel &mdash; because without a baseline there is no business case at the end, only anecdote.</p>
      </div>
      <div class="step">
        <h3>Install the sensors</h3>
        <p>Each radar sensor is a sealed, shock-resistant unit that mounts inside the lid or in the top of the container. No wiring, no mains power, no modification to the bin. Around ten minutes per unit including registering it against the right container in the software &mdash; operations managers on existing deployments fit their own replacements while out on the road. For semi-buried and communal containers, mounting position matters, and we set it during install: Fan&oslash;'s early accuracy problems were solved by repositioning the sensor to avoid false returns.</p>
      </div>
      <div class="step">
        <h3>Connect and calibrate</h3>
        <p>Sensors report over NB-IoT, a low-power mobile network that runs on existing UK telecoms infrastructure and holds a signal in the places that defeat ordinary connectivity &mdash; below ground level in semi-buried containers, inside metal housings, in rural bring sites. Typical reporting is six readings a day; the hardware supports up to 60 where demand justifies it. Over the first few weeks a learning algorithm tunes each sensor to the specific geometry of its container, so accuracy at the critical 80&ndash;90% threshold improves as it goes.</p>
      </div>
      <div class="step">
        <h3>Switch round planning to live data</h3>
        <p>The platform generates the round automatically &mdash; Vejle's is calculated at 05:00 every morning &mdash; picking up every container over its threshold and sequencing them into an efficient route. Thresholds are yours to set, and 80&ndash;90% is the usual starting point. Drivers get the round on a tablet with live fill percentages, locations and navigation, confirm each lift, and flag damage or contamination where they stand. Crucially they can see <em>why</em> a bin is on the list, which is what makes them trust it.</p>
      </div>
      <div class="step">
        <h3>Measure, report and rationalise</h3>
        <p>Once you have a few months of history, the interesting work starts. Fill curves show which locations are genuinely busy and which have been over-served for years. Some bins turn out to be redundant &mdash; Vejle began removing overlapping bins on the evidence, without reducing the service residents actually experience. Complaint responses become a timestamped record rather than a guess. Mileage and CO&#8322; reductions become a number you can put in a climate report, and lift counts become the number you take into the next contract negotiation.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt section-line">
  <div class="wrap">
    <p class="eyebrow">Timeline</p>
    <h2>What a first 90 days looks like</h2>
    <p class="lede">A pilot is deliberately small: one round, or one geographic cluster, big enough to be representative and small enough to be reversible.</p>
    <div class="table-scroll mt-2">
      <table>
        <caption class="visually-hidden">Indicative pilot timeline for a sensor-led waste collection deployment</caption>
        <thead><tr><th scope="col">Stage</th><th scope="col">Typical duration</th><th scope="col">What you get at the end</th></tr></thead>
        <tbody>
          <tr><td>Discovery &amp; scoping</td><td>1&ndash;2 weeks</td><td>An agreed pilot round, a bin register we both trust, and a written baseline of current cost, lifts, hours and mileage.</td></tr>
          <tr><td>Provisioning</td><td>2&ndash;3 weeks</td><td>Sensors configured and SIMs activated against your specific container list before anything leaves the box.</td></tr>
          <tr><td>Installation</td><td>1&ndash;3 days</td><td>All pilot containers instrumented and reporting, with mounting positions set per container type.</td></tr>
          <tr><td>Observation</td><td>2&ndash;4 weeks</td><td>Live fill data with collections unchanged &mdash; so you can see the gap between the timetable and reality before changing anything.</td></tr>
          <tr><td>Live sensor-led rounds</td><td>Remaining 6&ndash;8 weeks</td><td>Dynamic rounds in the driver app, with weekly reporting on lifts avoided, mileage saved and threshold breaches.</td></tr>
          <tr><td>Review</td><td>1 week</td><td>Measured before-and-after against your own baseline, and a costed rollout plan &mdash; or a clear answer that it is not worth it here.</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split split-top">
      <div>
        <p class="eyebrow">What we need from you</p>
        <h2>Three things decide whether this works</h2>
        <p class="lede">Deployments that struggle almost always struggle for the same reasons, and none of them are technical.</p>
      </div>
      <div>
        <ul class="feature-list">
          <li><strong>An accurate bin register.</strong> Type, capacity and GPS position for every container. If your data is patchy, say so early &mdash; surveying it properly is a fixed, one-off cost and far cheaper than discovering the gaps mid-rollout.</li>
          <li><strong>One named owner.</strong> Somebody who can coordinate across highways, waste, fleet and IT, and who owns the location database. Every successful deployment we can point to has this person.</li>
          <li><strong>Drivers brought in early.</strong> Crews are quick to spot that fewer lifts might mean fewer hours, and they need a straight answer about what the freed-up time is for. Where it has gone well, that time was redeployed to litter picking, fly-tipping and grounds work that was already overdue.</li>
        </ul>
      </div>
    </div>
  </div>
</section>
"""

HOW_FAQS = [
    ("Do we have to change our vehicles or depot arrangements?",
     "<p>No. Sensor-led collection changes which containers a round visits and in what order, not what lifts them. Existing vehicles, crews, depots and lifting equipment all stay as they are. The driver receives the round on a tablet or phone instead of a printed sheet or a memorised route.</p>"),
    ("What fill threshold should we set?",
     "<p>Most deployments start at 80&ndash;90%. Vejle flags bins at 80%; Langeland typically adds a container to the round at 80&ndash;90%. The right number depends on how much headroom you need between the reading and the visit: a rural site collected every few days needs a lower threshold than a town-centre bin you can reach the same afternoon. Langeland also runs an extra data check every Wednesday to catch containers likely to become critical over the weekend, which is the kind of local rule the platform is designed to accommodate.</p>"),
    ("How do you handle bins that fill unpredictably or seasonally?",
     "<p>That is the case sensors handle best, because a fixed timetable cannot. Fan&oslash;'s population swings between 3,000 and 50,000 across the year and its containers fill anywhere between one day and several weeks; forecasting uses each container's own history alongside live readings, so it adapts rather than assuming last month's pattern holds. For known events &mdash; a festival, a bank holiday weekend, a match day &mdash; you can raise reporting frequency and tighten thresholds for the period.</p>"),
    ("What happens if a sensor fails?",
     "<p>The platform monitors sensor health centrally and flags units that stop reporting or are running low on battery, so failures surface before they cause a missed collection rather than after. Reliability in the field has been high: Langeland reported one defective unit out of 220 in the first four months and no battery replacements in a year. Replacement is a ten-minute job and is covered under the subscription.</p>"),
    ("Can we start with one round rather than the whole authority?",
     "<p>Yes, and we recommend it. Every deployment worth citing started small: Stralsund began with 35 bins, Langeland with about ten sensors before scaling to 220, and Vejle ran a single trial route before a council decision to roll out across the municipality. A pilot on one representative round gives you real numbers from your own operation to take to a committee, which is a far stronger paper than any supplier's brochure.</p>"),
]


# ----------------------------------------------------------------- about --

ABOUT_BODY = f"""
<section class="section">
  <div class="wrap wrap-narrow prose">
    <div class="answer-box">
      <p><strong>Britannia IoT Solutions is a United Kingdom company supplying radar fill-level sensors and collection-planning software to councils, waste contractors, universities, NHS trusts and parks authorities. We deploy a sensor and software platform already proven in municipal service across Denmark and Germany, and we are focused solely on the UK market.</strong></p>
    </div>

    <h2>Why we exist</h2>
    <p>Waste collection is one of the few council services that almost every resident notices, and one of the last still run largely on estimates. Rounds are set by frequency, not by need. Crews drive past bins nobody has used to reach bins that overflowed on Saturday. Everybody involved knows it, and until recently there was no affordable way to find out which was which.</p>
    <p>Cheap, long-life, low-power sensors changed that. A unit costing a fraction of a single wasted lift can now tell you the real fill level of a container six times a day for eight years, over a mobile network that already covers the country. The technology is settled. What has been missing in the UK is a supplier who takes responsibility for the whole thing working &mdash; hardware, connectivity, software, the driver's experience and the business case &mdash; rather than selling a box and wishing you luck.</p>

    <h2>What we are, and what we are not</h2>
    <p>We are a young company, and we would rather say so than imply a client list we do not yet have. What we bring is a platform with a genuine operational track record: municipalities and utilities running it in daily service, with published, attributable numbers behind them. Those deployments are documented on our <a href="/results/">results pages</a>, clearly labelled as what they are &mdash; evidence for the technology, gathered by the authorities operating it, not case studies of our own delivery.</p>
    <p>We think that distinction matters. Anyone can buy sensors. The reason Stralsund's pilot paid back inside a year and Vejle's rollout survived a council decision is that the underlying measurement was accurate enough for operations staff to act on without checking. That is a hardware and software question, and it is why we chose the platform we did.</p>

    <h2>How we work</h2>
    <div class="grid grid-2 mt-2">
      {icon_card("radar", "Radar first", "We only deploy radar fill-level measurement. Ultrasonic sensors are cheaper and they misread exactly the materials that fill recycling containers. A pilot undermined by false readings costs far more than the hardware saved.")}
      {icon_card("pound", "A pilot with a real answer", "Ninety days on one round, against a baseline recorded before we start. If the numbers do not justify a rollout in your operation, we will tell you, and you will have the data to prove it either way.")}
      {icon_card("people", "Operations, not just software", "The people who decide whether this succeeds are drivers and supervisors, not procurement. We plan for that from the first conversation, including the awkward one about what happens to the hours you free up.")}
      {icon_card("shield", "Your data stays yours", "UK-hosted, exportable in full, available through an open API. No lock-in through data hostage-taking. If you leave, your fill history leaves with you.")}
    </div>

    <h2>Where we work</h2>
    <p>The United Kingdom, exclusively &mdash; England, Scotland, Wales and Northern Ireland. That focus is deliberate. UK waste operations have their own procurement routes, their own contract structures, their own statutory reporting and their own arguments about who owns the bin outside the parade of shops. A supplier who understands a Danish utility's operating model is not automatically useful to a Yorkshire district council, and we would rather be genuinely good at one market.</p>

    <h2>Talk to us</h2>
    <p>The most useful first conversation is usually thirty minutes with whoever knows your current round frequencies and roughly what the service costs. We will tell you fairly quickly whether there is a case worth pursuing. <a href="/contact/">Talk to us</a> or email <a href="mailto:{SITE['email']}">{SITE['email']}</a>.</p>
  </div>
</section>
"""

ABOUT_FAQS = [
    ("Are you a manufacturer or a reseller?",
     "<p>We are a UK solutions provider. We deploy, configure, support and operate a proven European sensor and software platform for British customers, and we take single-point responsibility for the service working &mdash; hardware, connectivity, software, installation, training and support. We do not manufacture the sensors ourselves, and we would be sceptical of any young company claiming otherwise.</p>"),
    ("Why should we buy from a new company?",
     "<p>Fair question, and the honest answer is: because of what sits behind us, and because the commercial structure protects you. The platform has years of municipal service behind it with published results. The engagement starts with a paid 90-day pilot on a single round, measured against your own pre-recorded baseline, so the decision to expand is made on your numbers rather than our promises. And your data is exportable in full throughout, so you are never trapped by us.</p>"),
    ("Do you work outside the UK?",
     "<p>No. Britannia IoT Solutions serves the United Kingdom only. For deployments elsewhere in Europe we can point you to the appropriate partner.</p>"),
]


# ------------------------------------------------------------------- FAQ --

FAQ_BODY = """
<section class="section">
  <div class="wrap wrap-narrow">
    <div class="answer-box">
      <p><strong>Common questions about sensor-led waste collection: what it costs, how accurate radar fill-level sensors are, how they connect, what happens to the data, and how to buy it through UK public procurement.</strong> If your question is not here, ask us directly &mdash; we will add it.</p>
    </div>
  </div>
</section>
"""

FAQ_LIST = [
    ("What is a bin fill-level sensor?",
     "<p>A fill-level sensor is a small, battery-powered device fitted inside the lid or the top of a waste container. It measures the distance from itself down to the surface of the waste, converts that into a percentage of the container's capacity, and transmits the reading over a mobile network several times a day. Better units use radar rather than ultrasound, and also report temperature, GPS position, tilt and battery state. The whole unit is sealed and shock-resistant, and its components can be dismantled for recycling at end of life.</p>"),
    ("How much does sensor-led waste collection cost?",
     "<p>Britannia IoT Solutions sells the service as an annual per-container subscription covering the sensor, the SIM and connectivity, the software platform, the driver app, support and replacement hardware &mdash; rather than a large capital purchase followed by licence fees. Pricing depends on the number of containers, reporting frequency and contract length, and we will give you a firm figure at the discovery stage. For context on whether it is worth it: Stralsund reported that its pilot paid for itself in under a year, on 35 bins, purely through avoided collections and mileage.</p>"),
    ("How much will we actually save?",
     "<p>It depends on how over-serviced your current rounds are, and honest suppliers cannot tell you before measuring. Published results from live deployments of this platform give a realistic range. Stralsund cut weekly collections from 1,548 to 445 &mdash; 71% &mdash; and weekly mileage from 1,677&nbsp;km to 779&nbsp;km, a 54% reduction, with working hours down 30%. Fan&oslash; achieved a 20% reduction in emptyings within two months against a 25% target. Vejle moved from twice-weekly to fortnightly collection on average and reduced crewing from 2.0 to 1.5 full-time staff. Savings are largest where bins are currently emptied to a fixed timetable regardless of use, and where rounds involve long drives between stops.</p>"),
    ("How accurate are radar fill-level sensors?",
     "<p>Accurate enough that operations staff act on the readings without physically checking. Radar performs markedly better than ultrasound on the materials that actually fill recycling containers &mdash; flattened cardboard, paper and film plastic scatter and absorb ultrasound, producing false readings. Vejle Municipality switched to radar after an earlier non-radar trial produced error reports on up to 30% of readings, and now reports very few. Accuracy also improves over the first weeks: a learning algorithm builds a profile of each individual container. Mounting position matters, and getting it right is part of installation &mdash; Fan&oslash;'s early inaccuracies were resolved by repositioning the sensor.</p>"),
    ("How do the sensors connect? Do we need our own network?",
     "<p>No. Sensors use NB-IoT (Narrowband Internet of Things), a low-power standard that runs over existing UK mobile networks, so there is no infrastructure for you to install or maintain. NB-IoT is designed for exactly this job: it penetrates below ground level and inside metal enclosures where ordinary mobile signal fails, uses very little power, and carries tiny packets reliably. Langeland's network works across a hilly rural island where earlier connectivity had struggled. Each sensor carries its own SIM, included in the subscription.</p>"),
    ("How long do the batteries last, and who changes them?",
     "<p>Around eight years at six readings a day. Higher reporting frequencies shorten that proportionally; the hardware supports up to 60 readings a day where demand justifies it. Battery state is monitored centrally, so units are flagged before they go dark. Field reliability has been good &mdash; Langeland reported no battery replacements in a year across 220 sensors. Replacement is included in the subscription and takes about ten minutes.</p>"),
    ("Will this reduce our staff numbers?",
     "<p>It reduces the hours spent driving to bins that did not need emptying, and what you do with those hours is your decision. In practice the deployments we can point to redeployed rather than cut: Stralsund reduced working hours by 30% and moved staff to other urgent tasks; Vejle went from 2.0 to 1.5 full-time staff on bin emptying and used the freed capacity for litter collection along roads and at bridges. It is worth being straight with crews about this early, because they will work it out on day one, and a driver who thinks the system threatens their job will find reasons it does not work.</p>"),
    ("What does the driver see?",
     "<p>The day's round on a tablet or phone: which containers are on it, where they are, how full each one is, and navigation between stops. Drivers confirm each lift as they complete it and can report damage, contamination or access problems on the spot. On several deployments drivers plan their own sequence from the flagged list rather than following a fixed order, which they generally prefer. Langeland's operations manager delegated round planning to the driver entirely once the data was trusted.</p>"),
    ("Does it work with our existing route management or in-cab system?",
     "<p>Yes, through either route. Contractors and in-house teams can work directly in the driver app, which also produces clean lift records for invoicing &mdash; Fan&oslash; connected its contractor this way specifically so that emptying orders and invoicing data flowed through one system. Where you already run an in-cab or route optimisation platform, fill-level data can be delivered to it through the API so crews keep the interface they know. We work out which makes sense during discovery.</p>"),
    ("Who owns the data, and where is it hosted?",
     "<p>You own your data. It is hosted in the United Kingdom, exportable in full at any time, and available through an open API for your own reporting or BI tools. Fill-level readings are measurements of council assets rather than personal data, so the data protection position is usually straightforward, but we will support your DPIA and can provide the processing detail your information governance team needs. If you end the contract, you take your history with you.</p>"),
    ("How do we buy this within public procurement rules?",
     "<p>Most authorities start with a pilot small enough to sit under their own delegated spend threshold, which gets real evidence in hand before any substantial procurement. That evidence &mdash; measured against your own baseline &mdash; is then what supports the business case for a wider award. We are happy to work through your route with you, whether that is a direct award under threshold, a framework call-off or a full tender, and to supply the technical detail your procurement team needs for specification and evaluation. Vejle followed exactly this path: a funded pilot on a trial route, then a council decision to roll out.</p>"),
    ("What if the pilot shows it is not worth doing?",
     "<p>Then you have spent a small sum to avoid a large mistake, and you will have the numbers to close the question properly rather than revisiting it every budget round. We would rather tell you that than sell a rollout that underdelivers. Sensor-led collection is not universally worthwhile &mdash; a dense urban round where every bin genuinely fills every day has little slack to recover, and we will say so.</p>"),
    ("Can sensors help us reduce the number of bins we have?",
     "<p>Yes, and it is one of the more valuable second-order effects. Bin estates grow by accretion: a bin gets added after a complaint and is never reviewed. With months of fill history you can see which locations overlap and which are genuinely used, and remove the redundant ones on evidence rather than guesswork. Vejle began doing exactly this once it had precise location and fill history, without reducing the service residents actually experience. Every bin removed takes a lift, a sensor and a maintenance liability out of the estate permanently.</p>"),
    ("Do sensors work in semi-buried and underground containers?",
     "<p>Yes. Semi-buried containers are one of the strongest cases for them, because their fill level cannot be assessed from the street at all. Fan&oslash; runs 82 semi-buried containers of up to three cubic metres on sensors. NB-IoT was chosen partly because it holds a signal below ground level and inside metal enclosures where standard mobile connectivity does not.</p>"),
    ("What about vandalism, theft and bin fires?",
     "<p>The sensor sits inside the container, in a small shock-resistant enclosure with no external cabling and little resale value, so it is a poor target. Units that stop reporting are flagged automatically, which surfaces damage or theft quickly rather than at the next inspection. Sensors that report temperature also provide early warning of a fire in the container &mdash; useful in town-centre and transport locations where a bin fire can escalate.</p>"),
    ("Can we use this to answer complaints and FOI requests?",
     "<p>Yes, and several authorities rate it as highly as the cost saving. Every reading and every confirmed lift is timestamped, so when a resident or councillor says a container has not been emptied for a fortnight you can check rather than guess. Fan&oslash; specifically notes being able to document whether containers were emptied. Vejle's department head values being able to respond quickly to elected members fielding questions from residents &mdash; and to show that unnecessary journeys are not being made.</p>"),
]


# --------------------------------------------------------------- contact --

CONTACT_BODY = f"""
<section class="section">
  <div class="wrap">
    <div class="split split-article">
      <div>
        <div class="answer-box">
          <p><strong>To talk to Britannia IoT Solutions about sensor-led waste collection, email <a href="mailto:{SITE['email']}">{SITE['email']}</a> or call <a href="tel:{SITE['phone'].replace(' ', '')}">{SITE['phone_display']}</a>. We reply to every enquiry within one working day.</strong></p>
        </div>

        <h2>What a first conversation covers</h2>
        <p>Thirty minutes, no slide deck. It is most useful with whoever knows your round frequencies and roughly what the service costs &mdash; usually an operations or waste services manager rather than procurement.</p>
        <ul class="feature-list">
          <li><strong>What you run today.</strong> How many containers, what type, what frequency, who lifts them.</li>
          <li><strong>Where the pain is.</strong> Overflow complaints, contract cost, mileage, CO&#8322; targets, crew capacity &mdash; the answer changes what we would propose.</li>
          <li><strong>Whether there is a case at all.</strong> We can usually tell within the call whether the numbers are likely to work, and we will say if they are not.</li>
          <li><strong>A pilot shape and an indicative price.</strong> Which round, how many sensors, what it costs, and what we would measure.</li>
        </ul>

        <h2>Useful to have to hand</h2>
        <p>None of this is required, and we will not send you a questionnaire before agreeing to talk. But if you know these figures the first conversation gets a lot further:</p>
        <ul class="feature-list">
          <li><strong>Roughly how many containers</strong> a vehicle travels specifically to reach &mdash; street and park bins, bring sites, communal and trade containers. Kerbside rounds do not count.</li>
          <li><strong>The current collection frequency</strong> on those, and whether it is the same everywhere.</li>
          <li><strong>Who does the lifting</strong> &mdash; an in-house team, an arm's-length company, or a contractor, and roughly when that contract next comes up.</li>
          <li><strong>What is driving the question</strong> &mdash; a budget line, an overflow problem, a carbon target, or a tender you are preparing.</li>
        </ul>
      </div>

      <div>
        <div class="contact-card">
          <h2>How to reach us</h2>
          <a class="contact-row" href="mailto:{SITE['email']}">
            <span class="contact-icon">{ICON["mail"]}</span>
            <span class="contact-text">
              <span class="contact-label">Email</span>
              <span class="contact-value">{SITE['email']}</span>
            </span>
          </a>
          <a class="contact-row" href="tel:{SITE['phone'].replace(' ', '')}">
            <span class="contact-icon">{ICON["phone"]}</span>
            <span class="contact-text">
              <span class="contact-label">Telephone</span>
              <span class="contact-value">{SITE['phone_display']}</span>
            </span>
          </a>
          <div class="contact-row is-static">
            <span class="contact-icon">{ICON["clock"]}</span>
            <span class="contact-text">
              <span class="contact-label">Office hours</span>
              <span class="contact-value">Monday to Friday, 08:30&ndash;17:30</span>
            </span>
          </div>
          <div class="contact-row is-static">
            <span class="contact-icon">{ICON["pin"]}</span>
            <span class="contact-text">
              <span class="contact-label">Coverage</span>
              <span class="contact-value">United Kingdom</span>
            </span>
          </div>
          <p class="contact-note">England, Scotland, Wales and Northern Ireland. We do not operate outside the UK.</p>
        </div>

        <div class="keyfacts mt-2" style="margin-bottom:0">
          <h3>Tenders, PQQs and specifications</h3>
          <dl>
            <dt>Documents</dt><dd>Email <a href="mailto:{SITE['email']}">{SITE['email']}</a>, marked for the bid team</dd>
            <dt>Specification help</dt><dd>We will supply the technical detail your procurement team needs, and we would rather do it early than respond to a specification that cannot be evaluated</dd>
            <dt>Turnaround</dt><dd>Acknowledged within one working day, with a named contact for the bid</dd>
          </dl>
        </div>
      </div>
    </div>
  </div>
</section>
"""

CONTACT_FAQS = [
    ("Can we see a demonstration before committing to anything?",
     "<p>Yes. We can walk through the live platform on a screen share &mdash; the dashboard, a generated round, the driver app and the reporting &mdash; using representative data. Where it is useful for a committee or a management team, we can also install a small number of sensors on your own containers so you are looking at your own bins rather than a demonstration dataset.</p>"),
    ("We are preparing a tender. Can you help with the specification?",
     "<p>Yes, and it is worth doing early. We can supply the technical detail needed to write a specification that is genuinely evaluable &mdash; measurement technology, accuracy under different waste streams, connectivity, battery life, API and export requirements, and support terms. Specifying <em>radar</em> rather than simply &ldquo;fill-level sensors&rdquo; is the single change that most reduces the risk of a disappointing award.</p>"),
    ("How quickly can you start?",
     "<p>A pilot is typically live four to six weeks after go-ahead: a week or two to scope and confirm the bin register, two to three weeks for hardware and SIM provisioning, and a day or three to install. The slowest step is usually confirming an accurate container list, so it helps to start pulling that together during the first conversation.</p>"),
]


# --------------------------------------------------------------- privacy --

PRIVACY_BODY = f"""
<section class="section">
  <div class="wrap wrap-narrow prose">
    <p class="note" style="margin-top:0;border-top:0;border-left:3px solid var(--sig-amber);padding:.8rem 0 .8rem 1rem">This notice is a working draft and must be reviewed by a qualified adviser, and completed with the company's registered details and ICO registration number, before the site goes live.</p>

    <h2>Who we are</h2>
    <p>{SITE['legal']} (&ldquo;we&rdquo;, &ldquo;us&rdquo;) is the data controller for personal data collected through this website. You can reach us at <a href="mailto:{SITE['email']}">{SITE['email']}</a> or {SITE['phone_display']}.</p>

    <h2>What we collect and why</h2>
    <p>This website has no enquiry form and collects nothing from you as you browse it. If you email or telephone us, we hold the contact details and the content of that correspondence. We use it solely to respond to your enquiry and, where relevant, to continue a commercial conversation you have started. The lawful basis is legitimate interests &mdash; responding to a business enquiry you have made of us.</p>
    <p>We do not run advertising trackers, third-party analytics profiling or cross-site cookies on this website. Web fonts are loaded from Google Fonts, which means Google receives the IP address of visitors' browsers as part of serving those files.</p>

    <h2>How long we keep it</h2>
    <p>Enquiry correspondence is retained for up to 24 months from our last contact with you, unless a contract is entered into, in which case records are retained for the period required by our contractual and statutory obligations.</p>

    <h2>Who we share it with</h2>
    <p>We do not sell personal data. We share it only with service providers who process it on our behalf &mdash; website hosting, form handling and email &mdash; under written terms, and where legally required.</p>

    <h2>Sensor data</h2>
    <p>Fill-level readings collected from customers' waste containers are measurements of physical assets, not personal data. Britannia IoT Solutions processes that data on behalf of the customer, who remains the controller. Contract terms, hosting location, retention and export rights are set out in the customer agreement, and we will support a customer's DPIA on request.</p>

    <h2>Your rights</h2>
    <p>You have the right to request access to the personal data we hold about you, to have it corrected or erased, to restrict or object to processing, and to data portability. To exercise any of these, email <a href="mailto:{SITE['email']}">{SITE['email']}</a>. If you are dissatisfied with our response you may complain to the Information Commissioner's Office at <a href="https://ico.org.uk" rel="noopener">ico.org.uk</a>.</p>

    <p class="note">Last updated {SITE['updated']}.</p>
  </div>
</section>
"""

NOTFOUND_BODY = """
<section class="section">
  <div class="wrap wrap-narrow">
    <p class="lede">That page does not exist, or it has moved. Try one of these instead:</p>
    <ul class="mt-2">
      <li><a href="/">Home</a></li>
      <li><a href="/solutions/">Solutions</a> &mdash; sensors, round planning and reporting</li>
      <li><a href="/sectors/">Sectors</a> &mdash; councils, contractors, estates and visitor destinations</li>
      <li><a href="/results/">Results</a> &mdash; measured outcomes from live deployments</li>
      <li><a href="/how-it-works/">How it works</a></li>
      <li><a href="/faq/">Frequently asked questions</a></li>
      <li><a href="/contact/">Contact us</a></li>
    </ul>
  </div>
</section>
"""


def pages():
    return [
        Page(
            path="",
            nav_key="",
            title="Smart Bin Sensors & Waste Round Optimisation | Britannia IoT",
            description="UK supplier of radar bin fill-level sensors and dynamic collection round planning for councils, contractors and large estates. Cut lifts and mileage.",
            keywords="bin fill level sensors UK, smart waste management, waste collection route optimisation, smart bins for councils, IoT waste sensors, refuse round planning software",
            h1="Collect the bins that are full. Skip the ones that aren't.",
            hero_html=HOME_HERO,
            body=HOME_BODY,
            faqs=HOME_FAQS,
            faq_heading="Sensor-led waste collection: the short answers",
            faq_intro="The questions we are asked in almost every first conversation. There are more on the <a href=\"/faq/\">full FAQ page</a>.",
            page_type="WebPage",
            schema=[{
                "@type": "Service",
                "@id": SITE["url"] + "/#service",
                "name": "Sensor-led waste collection",
                "serviceType": "Smart waste management and collection route optimisation",
                "provider": {"@id": SITE["url"] + "/#organization"},
                "areaServed": {"@type": "Country", "name": "United Kingdom"},
                "description": (
                    "Radar fill-level sensors fitted to bins and waste containers, NB-IoT "
                    "connectivity, dynamic collection round planning, a driver app and "
                    "reporting, supplied to UK councils, waste contractors, universities, "
                    "NHS trusts and parks authorities as a single managed subscription."
                ),
                "audience": {
                    "@type": "BusinessAudience",
                    "name": "Local authorities, waste management contractors, universities and NHS trusts, parks and coastal authorities",
                },
                "hasOfferCatalog": {
                    "@type": "OfferCatalog",
                    "name": "Britannia IoT Solutions services",
                    "itemListElement": [
                        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Radar fill-level sensors and NB-IoT connectivity", "url": SITE["url"] + "/solutions/fill-level-sensors/"}},
                        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Dynamic collection round planning and driver app", "url": SITE["url"] + "/solutions/route-optimisation/"}},
                        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Waste analytics, forecasting and reporting", "url": SITE["url"] + "/solutions/analytics-reporting/"}},
                    ],
                },
            }],
        ),
        Page(
            path="how-it-works/",
            nav_key="how",
            title="How Sensor-Led Waste Collection Works | Britannia IoT",
            description="The five stages from bin survey to live sensor-led rounds, a 90-day pilot timeline, and the three non-technical things that decide if it succeeds.",
            keywords="how bin sensors work, smart waste deployment, fill level sensor installation, waste collection pilot",
            h1="How sensor-led collection works",
            eyebrow="How it works",
            lede="From an accurate bin register to a round that rebuilds itself every morning &mdash; and the honest version of what it takes to get there.",
            breadcrumbs=[],
            body=HOW_BODY,
            faqs=HOW_FAQS,
            faq_heading="Deployment questions",
            page_type="WebPage",
            schema=[{
                "@type": "HowTo",
                "@id": SITE["url"] + "/how-it-works/#howto",
                "name": "How to move from fixed-frequency to sensor-led waste collection",
                "description": "The five stages of deploying bin fill-level sensors and dynamic round planning in a UK waste operation.",
                "totalTime": "P90D",
                "step": [
                    {"@type": "HowToStep", "position": 1, "name": "Survey the estate and take a baseline",
                     "text": "Confirm container type, capacity, GPS position, current frequency and who lifts each bin, and record present cost, lifts, hours and mileage as a measurable baseline."},
                    {"@type": "HowToStep", "position": 2, "name": "Install the sensors",
                     "text": "Fit a sealed radar sensor inside the lid or top of each container. No wiring or mains power; roughly ten minutes per unit including registration in the software."},
                    {"@type": "HowToStep", "position": 3, "name": "Connect and calibrate",
                     "text": "Sensors report over the NB-IoT mobile network, typically six times a day and up to 60 where needed, while a learning algorithm tunes each unit to its container."},
                    {"@type": "HowToStep", "position": 4, "name": "Switch round planning to live data",
                     "text": "The platform generates an optimised daily round from overnight readings and pushes it to the driver app with live fill percentages and navigation."},
                    {"@type": "HowToStep", "position": 5, "name": "Measure, report and rationalise",
                     "text": "Use accumulated fill history to evidence complaint responses, report mileage and CO2 reductions, and remove redundant containers on data rather than guesswork."},
                ],
            }],
        ),
        Page(
            path="about/",
            nav_key="about",
            title="About Britannia IoT Solutions | UK Smart Waste Company",
            description="A UK company deploying radar fill-level sensors and round-planning software proven in Danish and German municipal service. Who we are and how we work.",
            keywords="smart waste company UK, IoT waste management supplier, bin sensor supplier Britain",
            h1="About Britannia IoT Solutions",
            eyebrow="About",
            lede="A UK company built around one idea: waste rounds should follow the waste, and you should be able to prove it did.",
            body=ABOUT_BODY,
            faqs=ABOUT_FAQS,
            faq_heading="About us",
            page_type="AboutPage",
        ),
        Page(
            path="faq/",
            title="Smart Waste Sensor FAQ | Cost, Accuracy & Procurement",
            description="Direct answers on bin fill-level sensors: cost, radar accuracy, NB-IoT connectivity, battery life, data ownership and UK public procurement routes.",
            keywords="bin sensor cost, fill level sensor accuracy, NB-IoT waste sensors, smart bin procurement UK",
            h1="Frequently asked questions",
            eyebrow="FAQ",
            lede="Everything we get asked about sensor-led waste collection, answered properly rather than in marketing language.",
            body=FAQ_BODY,
            faqs=FAQ_LIST,
            faq_heading="Questions and answers",
            page_type="FAQPage",
        ),
        Page(
            path="contact/",
            title="Contact Britannia IoT | Talk to Us About Bin Sensors",
            description="Talk to Britannia IoT Solutions about bin fill-level sensors and sensor-led collection rounds. Email or telephone us and we reply within one working day.",
            h1="Talk to us",
            eyebrow="Contact",
            lede="Thirty minutes with someone who knows your round frequencies is usually enough to tell whether there is a case worth pursuing.",
            body=CONTACT_BODY,
            faqs=CONTACT_FAQS,
            faq_heading="Before you get in touch",
            page_type="ContactPage",
            cta=("Prefer to see the numbers first?",
                 "Every performance figure on this site comes from a named, published municipal deployment. Read them, then decide whether a call is worth your time."),
        ),
        Page(
            path="privacy/",
            title="Privacy Notice | Britannia IoT Solutions",
            description="How Britannia IoT Solutions handles personal data submitted through this website, and how customer sensor data is treated under our contracts.",
            h1="Privacy notice",
            eyebrow="Legal",
            lede="What we collect, why, how long we keep it and what you can ask us to do about it.",
            body=PRIVACY_BODY,
            page_type="WebPage",
            cta=("Questions about data handling?",
                 "Our information governance detail, hosting arrangements and DPIA support material are available on request for any authority evaluating the service."),
        ),
        Page(
            path="404/",
            title="Page not found | Britannia IoT Solutions",
            description="The page you were looking for could not be found.",
            h1="Page not found",
            eyebrow="404",
            lede="We could not find that page.",
            body=NOTFOUND_BODY,
            noindex=True,
        ),
    ]
