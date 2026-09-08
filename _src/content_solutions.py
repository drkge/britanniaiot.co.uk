"""Solutions: overview, fill-level sensors, route optimisation, analytics."""

from build import Page, SITE
from content_core import ICON, icon_card

CRUMB = [("Solutions", "/solutions/")]


def service_schema(url, name, desc, terms):
    return {
        "@type": "Service",
        "@id": SITE["url"] + url + "#service",
        "name": name,
        "description": desc,
        "serviceType": terms,
        "provider": {"@id": SITE["url"] + "/#organization"},
        "areaServed": {"@type": "Country", "name": "United Kingdom"},
        "audience": {"@type": "BusinessAudience",
                     "name": "UK local authorities, waste contractors and large estates"},
    }


# ----------------------------------------------------------- overview ----

OVERVIEW_BODY = f"""
<section class="section">
  <div class="wrap">
    <div class="answer-box">
      <p><strong>Britannia IoT Solutions supplies three things as one managed subscription: radar fill-level sensors with NB-IoT connectivity, software that builds an optimised collection round from the readings every morning and pushes it to a driver app, and reporting that turns months of fill history into evidence for complaints, climate targets and contract negotiations.</strong></p>
      <p class="mt-1">You cannot buy the parts separately from us, and that is deliberate. Sensors without planning software produce a dashboard nobody has time to read; planning software without accurate measurement produces rounds crews stop trusting.</p>
    </div>

    <div class="grid grid-3 mt-3">
      {icon_card("radar", "Fill-level sensors &amp; connectivity", "Radar measurement inside the lid, sealed, battery-powered, around eight years of life at six readings a day, connected over the NB-IoT mobile network. Ten minutes to fit, no wiring, no bin modification.", "/solutions/fill-level-sensors/", "Sensors in detail")}
      {icon_card("route", "Dynamic round planning &amp; driver app", "An optimised round generated automatically each morning from overnight readings, delivered to the driver's tablet with live fill percentages, locations, navigation and one-tap lift confirmation.", "/solutions/route-optimisation/", "Round planning in detail")}
      {icon_card("chart", "Analytics, forecasting &amp; reporting", "Fill history per container, AI emptying forecasts, demand heat maps, complaint evidence, mileage and CO&#8322; reporting, and the data to remove bins that were never needed.", "/solutions/analytics-reporting/", "Reporting in detail")}
    </div>
  </div>
</section>

<section class="section section-alt section-line">
  <div class="wrap">
    <p class="eyebrow">What is included</p>
    <h2 class="measure">One subscription, one accountable supplier</h2>
    <p class="lede">Smart waste projects usually fail at the seams &mdash; between the hardware vendor, the connectivity provider and the software licence. We removed the seams.</p>
    <div class="table-scroll mt-3">
      <table>
        <caption class="visually-hidden">What is included in a Britannia IoT Solutions subscription</caption>
        <thead><tr><th scope="col">Component</th><th scope="col">Included</th><th scope="col">Notes</th></tr></thead>
        <tbody>
          <tr><td>Radar fill-level sensor</td><td>Yes</td><td>Per container. Replacement hardware for faults and end-of-life batteries included.</td></tr>
          <tr><td>SIM and NB-IoT connectivity</td><td>Yes</td><td>Runs on existing UK mobile infrastructure. No network for you to build or maintain.</td></tr>
          <tr><td>Software platform</td><td>Yes</td><td>Unlimited users. Dashboard, round planning, thresholds, alerts and reporting.</td></tr>
          <tr><td>Driver app</td><td>Yes</td><td>Android and iOS. Usable by in-house crews or your contractor.</td></tr>
          <tr><td>Installation</td><td>Optional</td><td>We install, or we train your team &mdash; it is a ten-minute job per bin and most customers take it in-house after the first tranche.</td></tr>
          <tr><td>Bin register survey</td><td>Optional</td><td>Fixed-price if your container data is incomplete. Worth doing properly; it is the usual cause of trouble later.</td></tr>
          <tr><td>API and data export</td><td>Yes</td><td>Open API and full export at any time. Your history remains yours.</td></tr>
          <tr><td>Support</td><td>Yes</td><td>UK business hours, with sensor health monitored centrally so failures surface before they cause a missed lift.</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="eyebrow">Container types</p>
    <h2 class="measure">What we can instrument</h2>
    <p class="lede">If it holds waste and something has to come and empty it, it can usually be measured.</p>
    <div class="grid grid-4 mt-3">
      <div class="card no-push"><h3>Street &amp; park bins</h3><p>Typically 60&ndash;240 litres, on high streets, promenades, parks and transport interchanges. The highest-frequency, lowest-yield collections in most operations &mdash; and therefore the biggest saving.</p></div>
      <div class="card no-push"><h3>Semi-buried &amp; underground</h3><p>Up to around three cubic metres, with no way to judge fill level from the street. One of the strongest cases for sensors, and one NB-IoT was chosen to serve.</p></div>
      <div class="card no-push"><h3>Bring sites &amp; recycling points</h3><p>Glass, cans, paper, card, textiles. Frequently in rural or edge-of-town locations where a wasted visit costs a long drive.</p></div>
      <div class="card no-push"><h3>Communal &amp; trade containers</h3><p>Eurobins and communal housing containers, plus commercial waste at business parks, retail sites, universities and hospital estates.</p></div>
    </div>
    <div class="tag-row">
      <span class="tag">Residual waste</span><span class="tag">Mixed recycling</span><span class="tag">Glass</span>
      <span class="tag">Paper &amp; card</span><span class="tag">Food waste</span><span class="tag">Textiles</span>
      <span class="tag">Litter bins</span><span class="tag">Dog waste bins</span>
    </div>
  </div>
</section>
"""

OVERVIEW_FAQS = [
    ("Can we buy just the sensors and use our own software?",
     "<p>We supply the platform as one service, because the two halves depend on each other and split responsibility is where these projects come unstuck. What we do support is integration: fill-level data can be pushed to an existing in-cab, route management or BI system through the API, so your crews and analysts keep the tools they already use while the measurement and health monitoring stay our responsibility.</p>"),
    ("Is there a minimum number of containers?",
     "<p>Pilots typically start around 30 to 50 containers &mdash; enough to be representative of a real round. Stralsund's trial ran on 35 bins and Langeland began with about ten before scaling to 220. Below roughly 30 the sample is too small to tell you anything reliable about your wider estate.</p>"),
    ("What happens at the end of the contract?",
     "<p>You export your full fill history and either renew, move to another supplier, or stop. Sensors remain our responsibility for removal or transfer depending on the terms agreed. We do not hold data as a retention mechanism &mdash; the export is available throughout the contract, not just at the end of it.</p>"),
]


# ------------------------------------------------------------- sensors ----

SENSORS_BODY = f"""
<section class="section">
  <div class="wrap">
    <div class="split split-article">
      <div>
        <div class="answer-box">
          <p><strong>A bin fill-level sensor is a sealed, battery-powered device fitted inside the lid or top of a waste container. It measures the distance down to the surface of the waste using radar, converts that to a percentage of capacity, and transmits the reading over the NB-IoT mobile network several times a day.</strong></p>
          <p class="mt-1">No wiring, no mains power, no modification to the container. Around ten minutes to fit and register. Battery life of roughly eight years at six readings a day.</p>
        </div>
        <h2>Why radar rather than ultrasonic</h2>
        <p>This is the single most consequential specification decision in a smart waste project, and it is the one most often got wrong.</p>
        <p>Ultrasonic sensors work by timing a sound pulse. They are cheap and they are fine against a flat, hard, reflective surface. Waste is none of those things. Flattened cardboard absorbs and scatters sound. Paper does the same. Film plastic flutters. A carrier bag hanging near the sensor returns a strong echo from nothing. The result is a stream of readings that look plausible and are wrong, and once a supervisor has been sent to two empty bins flagged as full, the system is finished politically whatever the dashboard says afterwards.</p>
        <p>Radar measures with millimetre-wave reflection instead. It is materially more tolerant of irregular, absorbent and light surfaces, which is precisely the profile of recycling waste. Vejle Municipality's original 2021 trial &mdash; using non-radar sensors &mdash; produced error reports on up to <strong>30% of readings</strong>. The authority changed supplier specifically to obtain radar measurement, and now reports very few faults, describing performance as clearly better than the target set for the test period.</p>
      </div>
      <div>
        <div class="keyfacts">
          <h2>Sensor specification at a glance</h2>
          <dl>
            <dt>Measurement</dt><dd>Millimetre-wave radar fill level</dd>
            <dt>Also reports</dt><dd>Temperature, GPS position, tilt, battery state, fault status</dd>
            <dt>Mounting</dt><dd>Inside the container lid or upper shell; no wiring or drilling of the shell</dd>
            <dt>Install time</dt><dd>About 10 minutes including software registration</dd>
            <dt>Battery life</dt><dd>Around 8 years at 6 readings per day</dd>
            <dt>Reporting rate</dt><dd>Typically 6 per day; up to 60 per day supported</dd>
            <dt>Connectivity</dt><dd>NB-IoT over existing UK mobile networks</dd>
            <dt>Enclosure</dt><dd>Sealed, lightweight, shock-resistant</dd>
            <dt>End of life</dt><dd>Components can be dismantled and recycled</dd>
            <dt>Suits</dt><dd>Street bins, semi-buried and underground containers, bring sites, communal and trade bins</dd>
          </dl>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt section-line">
  <div class="wrap">
    <p class="eyebrow">Connectivity</p>
    <div class="split split-top">
      <div>
        <h2>NB-IoT: why the signal reaches a buried container</h2>
        <p>NB-IoT &mdash; Narrowband Internet of Things &mdash; is a low-power mobile standard carried on the existing UK cellular network. You do not build anything, install any gateways, or maintain any infrastructure. Each sensor carries its own SIM, included in the subscription.</p>
        <p>It matters for three practical reasons. It reaches places ordinary mobile signal does not, including below ground level inside semi-buried containers and within metal enclosures. It consumes very little power, which is what makes an eight-year battery possible. And because it uses national infrastructure, coverage extends to rural bring sites without a local network of your own.</p>
        <p>Langeland's island network is the illustrative case: rolling terrain initially caused data transfer problems, and NB-IoT was the technology that delivered consistent, reliable reporting from containers spread across the island.</p>
      </div>
      <div>
        <ul class="feature-list">
          <li><strong>No infrastructure to build.</strong> No gateways, no mesh, no LoRaWAN network to plan, license and maintain.</li>
          <li><strong>Deep indoor and below-ground penetration.</strong> Designed for meters in basements; a semi-buried container is an easier problem.</li>
          <li><strong>Very low power draw.</strong> Small packets, infrequent transmission &mdash; the reason batteries last years rather than months.</li>
          <li><strong>Carrier-grade reliability.</strong> The network is somebody else's operational responsibility, and it is already there.</li>
          <li><strong>Scales without redesign.</strong> Adding the 400th sensor is the same job as adding the fourth.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="eyebrow">In service</p>
    <h2 class="measure">What reliability looks like in the field</h2>
    <div class="grid grid-3 mt-3">
      <div class="card no-push">
        <p class="case-headline">1 in 220</p>
        <h3>Sensor faults</h3>
        <p>Langelands Forsyning recorded one defective fill-level sensor out of 220 units in its first four months, and no battery replacements across a full year.</p>
      </div>
      <div class="card no-push">
        <p class="case-headline">10 min</p>
        <h3>To fit a replacement</h3>
        <p>Langeland's operations manager fits and configures new sensors himself while out on the road, rather than raising a job for anyone.</p>
      </div>
      <div class="card no-push">
        <p class="case-headline">8 years</p>
        <h3>Battery life</h3>
        <p>At six readings a day, in a sealed shock-resistant enclosure containing the electronics, power supply and mini-radar &mdash; as deployed in Stralsund's town-centre bins.</p>
      </div>
    </div>
    <div class="pullquote mt-3">
      <blockquote>It takes me ten minutes to install a new fill-level sensor and to set it up in our software.</blockquote>
      <cite><b>Operations manager</b> &mdash; Langelands Forsyning, Denmark</cite>
    </div>
  </div>
</section>

<section class="section section-dark">
  <div class="wrap">
    <p class="eyebrow">Installation</p>
    <h2 class="measure">Mounting position is not a detail</h2>
    <div class="split split-top mt-2">
      <div>
        <p>The most common cause of disappointing accuracy is not the sensor. It is where the sensor was put. A unit mounted where a hinge, a lid stay, a chute wall or a hanging bag sits inside its field of view will return a strong reflection from that object rather than from the waste, and will read high for ever.</p>
        <p>Fan&oslash; Municipality hit exactly this in its first weeks: initial accuracy was poor, and the fix was repositioning the sensor to avoid false returns. After that, when the sensor reported 90% full, it was 90% full.</p>
        <p>We set mounting position per container type during installation, and validate the first readings against physical checks before a container goes live in round planning. It is a small amount of extra work at the front that removes the main reason these projects lose credibility.</p>
      </div>
      <div>
        <ul class="feature-list">
          <li><strong>Position set per container type</strong>, not per site &mdash; a semi-buried three-cubic-metre container and a 60-litre street bin need different placement.</li>
          <li><strong>First readings validated physically</strong> before the container joins live round planning.</li>
          <li><strong>Self-learning calibration</strong> then refines each unit against its own container over the following weeks.</li>
          <li><strong>Health monitored centrally</strong> &mdash; units that stop reporting or drift are flagged, not discovered on a complaint.</li>
        </ul>
      </div>
    </div>
  </div>
</section>
"""

SENSORS_FAQS = [
    ("What exactly does the sensor measure?",
     "<p>Fill level as a percentage of the container's usable capacity, derived from the radar distance between the sensor and the surface of the waste below it. Units also report temperature where fitted, GPS position, tilt, battery state and fault status. Temperature is genuinely useful in town-centre and transport locations, because a rising reading gives early warning of a bin fire.</p>"),
    ("How long does the battery last, and can it be replaced?",
     "<p>Around eight years at six readings a day. Reporting more often shortens that roughly proportionally, so the frequency is a decision rather than a fixed setting &mdash; six a day suits most rounds; up to 60 a day is supported where a location genuinely warrants it. Battery state is monitored centrally so units are flagged before they go dark, and replacement is a ten-minute job covered by the subscription.</p>"),
    ("Do sensors work in semi-buried and underground containers?",
     "<p>Yes, and it is one of their strongest applications, because the fill level of a semi-buried container cannot be judged from street level at all. Fan&oslash; Municipality runs 82 semi-buried containers of up to three cubic metres this way. NB-IoT was selected in part for its ability to hold a signal below ground level and inside metal enclosures.</p>"),
    ("Is the sensor a target for vandalism or theft?",
     "<p>Rarely. It sits inside the container in a small sealed enclosure with no external cabling, no display and negligible resale value. If a unit is damaged or removed it stops reporting, which raises a flag automatically &mdash; so you find out promptly rather than at the next inspection.</p>"),
    ("What happens to the sensors at end of life?",
     "<p>The components can be dismantled and recycled. For an authority with a circular economy commitment this is worth confirming in the specification, because not all sensors on the market are designed for disassembly.</p>"),
    ("Can we install them ourselves?",
     "<p>Yes, and most customers do after the first tranche. It is a ten-minute job per container: mount the unit in the specified position, scan it against the right container in the software, done. We install the pilot and train your team alongside, so the skill stays in-house. Operations managers on existing deployments routinely fit replacements themselves while already out on a round.</p>"),
]


# --------------------------------------------------------------- routes ----

ROUTES_BODY = f"""
<section class="section">
  <div class="wrap">
    <div class="answer-box">
      <p><strong>Dynamic round planning replaces a fixed collection timetable with a round rebuilt every morning from overnight sensor readings. Containers over their fill threshold are selected automatically, sequenced into an efficient route, and pushed to the driver's tablet with live fill percentages, locations and navigation.</strong></p>
      <p class="mt-1">Vejle Municipality's round is calculated at 05:00 each day across 547 instrumented bins spread over 2,000&nbsp;km of roads. Nobody in the office builds it by hand.</p>
    </div>
  </div>
</section>

<section class="section-tight">
  <div class="wrap">
    <div class="split split-top">
      <div>
        <p class="eyebrow">The planner</p>
        <h2>What the office sees</h2>
        <p>A live map and list of every container, colour-coded green, amber and red against thresholds you set. You can accept the generated round, adjust it, add a container that is not over threshold but is on the way, or hold one back.</p>
        <p>Nobody in the office builds a round by hand any more, and nobody drives out to check a bin before deciding.</p>
      </div>
      <div>
        <ul class="feature-list" style="margin-top:0">
          <li><strong>Thresholds you control.</strong> 80&ndash;90% is the usual starting point, and it can differ by container type, waste stream, location or season.</li>
          <li><strong>Local rules.</strong> Langeland runs an extra data check every Wednesday to catch containers likely to become critical over the weekend in holiday-home areas. Rules like that are configuration, not a special request.</li>
          <li><strong>Multi-stream rounds.</strong> A vehicle handling several fractions in one pass can be planned as such &mdash; Langeland's service truck and trailer covers four fractions at a time.</li>
          <li><strong>Manual override, always.</strong> Events, road closures, complaints and reported access problems all sit outside the data. The planner assists the supervisor; it does not replace them.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt section-line">
  <div class="wrap">
    <div class="split split-top">
      <div>
        <p class="eyebrow">The driver app</p>
        <h2>What the crew sees</h2>
        <p>If drivers do not trust the round, the project fails &mdash; regardless of how good the analytics are. So the app is built for the cab, not the office.</p>
        <p>The day's stops, each with a live fill percentage and an exact location. Navigation between them. One tap to confirm a lift. A field to report damage, contamination or an access problem while standing in front of it. And, importantly, the reason each stop is on the list, so nobody is following instructions they cannot interrogate.</p>
        <p>On several deployments drivers plan their own sequence from the flagged list rather than following a fixed order, and prefer it that way. Langeland's operations manager handed round planning to the driver entirely once the data proved itself.</p>
        <div class="pullquote">
          <blockquote>It is easy to use and provides an overview, so we are able to delegate the planning of the service route to our driver &mdash; he is now fully in charge of the process.</blockquote>
          <cite><b>Operations manager</b> &mdash; Langelands Forsyning, Denmark</cite>
        </div>
      </div>
      <div>
        <ul class="feature-list">
          <li><strong>Android and iOS.</strong> Runs on a standard tablet or phone; no proprietary in-cab hardware.</li>
          <li><strong>Usable by contractors.</strong> Fan&oslash; connected its contractor to the same app so emptying orders arrive directly and completion is reported back &mdash; which also produces clean invoicing data.</li>
          <li><strong>Fault reporting at the bin.</strong> Vejle's drivers register emptyings and report repair needs on the spot rather than remembering them until the depot.</li>
          <li><strong>Straightforward enough for cover staff.</strong> Vejle's operations assistant makes the point that substitutes pick it up without difficulty, which matters more than it sounds when someone is off sick.</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="eyebrow">Forecasting</p>
    <div class="split split-top">
      <div>
        <h2>Planning ahead of the threshold, not behind it</h2>
        <p>A live reading tells you a container is full now. A forecast tells you which containers will be full on Thursday, which is the more useful number when you are deciding what Thursday's round should look like.</p>
        <p>The platform's forecasting draws on each container's own fill history, current readings, driver reports and other data sources, and improves at predicting individual containers over time &mdash; Vejle describes the route planning system as continuously getting better at anticipating when each container needs emptying next.</p>
        <p>In practice this is what lets you consolidate: instead of a container tipping over threshold on its own and forcing a special trip, it can be picked up on the day the vehicle is already in that area.</p>
      </div>
      <div>
        <ul class="feature-list">
          <li><strong>Fewer one-container detours</strong> by pulling near-threshold stops into a round already passing.</li>
          <li><strong>Weekend and bank holiday cover</strong> planned from predicted fill rather than a guess about how busy Saturday will be.</li>
          <li><strong>Seasonal adaptation</strong> for locations whose demand curve changes completely between February and August.</li>
          <li><strong>Event handling</strong> &mdash; raise reporting frequency and tighten thresholds around a festival, match day or bank holiday weekend.</li>
        </ul>
      </div>
    </div>
  </div>
</section>
"""

ROUTES_FAQS = [
    ("Does the system decide the round, or do we?",
     "<p>It proposes; you dispose. The platform generates an optimised round automatically from the readings, and a supervisor can accept it, add stops, remove stops or reorder it. There are always factors outside the data &mdash; a road closure, an event, a complaint, a container someone reported as damaged &mdash; and the planner is built on the assumption that a human is applying them.</p>"),
    ("What fill threshold should we set?",
     "<p>80&ndash;90% is the standard starting point: Vejle flags at 80%, Langeland typically adds a container at 80&ndash;90%. The right figure depends on your headroom between reading and visit. A rural bring site you reach twice a week needs a lower threshold than a town-centre bin you can reach the same afternoon. Thresholds can vary by container type, waste stream, location and season, and most customers tune them in the first couple of months.</p>"),
    ("Will our drivers accept it?",
     "<p>Generally yes, once two things are true: the readings are accurate enough that they are not sent to bins that turn out to be half empty, and somebody has given them a straight answer about what the freed-up hours are for. Drivers on existing deployments report liking the visibility &mdash; being able to see fill levels and exact locations and plan their own sequence saves them time and arguments. What loses them is a system that flags full bins that are not, which is why the sensor specification matters as much as the software.</p>"),
    ("Does this work if our collections are done by a contractor?",
     "<p>Yes. Contractors get their own access and receive the round directly in the driver app, confirming each lift as they go. Fan&oslash; Municipality connected its contractor precisely this way so that emptying orders arrive through the system and invoicing data comes back through it &mdash; which reduces the contractor's administration as well as the authority's. Where a contractor prefers to keep its own in-cab system, fill data can be delivered to it through the API instead.</p>"),
    ("Can it plan rounds for vehicles collecting several waste streams at once?",
     "<p>Yes. Multi-fraction rounds are a normal case, not an exception &mdash; Langelands Forsyning runs a service truck and trailer that handles four fractions in a single pass, alongside three vehicles on daily collection. Round generation accounts for which streams each vehicle can take and the capacity available.</p>"),
    ("What happens on a day when nothing is over threshold?",
     "<p>You do not send a vehicle out, which is the point. In practice most operations find a lower-priority backlog absorbs that capacity quickly &mdash; litter picking, fly-tipping, grounds maintenance, bin repairs. Vejle used its freed capacity to start collecting waste along roads and at bridges, work that had previously never made it to the top of the list.</p>"),
]


# ------------------------------------------------------------ analytics ----

ANALYTICS_BODY = f"""
<section class="section">
  <div class="wrap">
    <div class="answer-box">
      <p><strong>Once containers have been reporting for a few months, the fill history answers questions no waste operation could previously answer: which bins are genuinely used, which have been over-served for years, which are redundant, what a collection actually costs, and whether a specific container was emptied on a specific day.</strong></p>
      <p class="mt-1">The savings pay for the system. The evidence is what makes it hard to remove.</p>
    </div>

    <div class="grid grid-2 mt-3">
      {icon_card("clipboard", "Complaint and enquiry evidence", "Every reading and every confirmed lift is timestamped. When a resident or a councillor says a container has not been emptied for a fortnight, you check rather than guess, and reply the same day with a record instead of an apology.")}
      {icon_card("chart", "Demand heat mapping", "Fill curves per container, per week, per season. Which locations are busy, which are quiet, and which have a pattern nobody in the office would have predicted &mdash; Stralsund found some bins virtually empty while others filled far faster than expected.")}
      {icon_card("truck", "Bin estate rationalisation", "Bin estates grow by accretion and are almost never reviewed. With precise locations and months of fill data you can identify overlapping and under-used containers and remove them on evidence &mdash; which is exactly what Vejle began doing.")}
      {icon_card("leaf", "Mileage and carbon reporting", "Kilometres avoided, lifts avoided, fuel not burned. Vejle's programme targets 5.5 tonnes of CO&#8322; saved a year and a 30% travel reduction; Stralsund cut weekly mileage by 54%. These are numbers a climate report can use.")}
      {icon_card("pound", "Contract and budget evidence", "Lift counts per container per period, against contracted frequency. Whether you are commissioning or delivering the service, this is the number the next negotiation turns on &mdash; and currently almost nobody has it.")}
      {icon_card("signal", "Service performance", "Threshold breaches, time from flag to lift, missed collections, sensor health. Ordinary operational KPIs, but measured rather than reported.")}
    </div>
  </div>
</section>

<section class="section section-alt section-line">
  <div class="wrap">
    <p class="eyebrow">The second-order win</p>
    <div class="split split-top">
      <div>
        <h2>Removing bins you never needed</h2>
        <p>Most bin estates are the accumulated residue of individual decisions. A complaint came in, a bin was added, and nobody ever went back to ask whether it was justified. Multiply that by twenty years and you have containers standing thirty metres apart, each collected on the same fixed frequency, each costing a lift.</p>
        <p>Fill history settles it. If two containers in sight of each other both sit at 30% between visits, one of them is unnecessary, and removing it is a permanent saving &mdash; a lift, a sensor, a maintenance liability and a graffiti target gone. Because the decision rests on months of measured data rather than an officer's impression, it survives the inevitable objection.</p>
        <p>Vejle began exactly this exercise once it had accurate location and fill-level history, trimming overlaps and reducing the number of bins without compromising the service residents actually experience.</p>
      </div>
      <div>
        <div class="keyfacts" style="margin-bottom:0">
          <h3>Questions the data answers</h3>
          <dl>
            <dt>Utilisation</dt><dd>What fill level does each container actually reach between visits?</dd>
            <dt>Frequency fit</dt><dd>How many of last month's lifts went to containers under 50%?</dd>
            <dt>Overlap</dt><dd>Which containers within 100&nbsp;m of each other are both under-used?</dd>
            <dt>Seasonality</dt><dd>How does demand at this location differ between February and August?</dd>
            <dt>Cost per lift</dt><dd>What does a collection at this container cost, including the drive to reach it?</dd>
            <dt>Service proof</dt><dd>Was container 4471 emptied on 14 August, and at what time?</dd>
            <dt>Carbon</dt><dd>How many kilometres and tonnes of CO&#8322; has the change avoided this year?</dd>
          </dl>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split split-top">
      <div>
        <p class="eyebrow">Access and integration</p>
        <h2>Your data, in your systems</h2>
        <p>Reporting is available in the platform, but nobody wants a twelfth dashboard to log into. Everything is exportable and accessible through an open API, so fill history and lift records can feed the systems your organisation already uses for performance reporting and financial analysis.</p>
      </div>
      <div>
        <ul class="feature-list">
          <li><strong>Open API</strong> for fill readings, lift confirmations, container registers and sensor health.</li>
          <li><strong>Full export</strong> at any time, in standard formats, throughout the contract rather than only at the end of it.</li>
          <li><strong>Feeds your BI tools</strong> &mdash; Power BI, Tableau or whatever your performance team already runs.</li>
          <li><strong>Push to existing route systems</strong> where crews should keep the in-cab interface they know.</li>
          <li><strong>UK-hosted</strong>, with the processing detail your information governance team will ask for.</li>
        </ul>
      </div>
    </div>
  </div>
</section>
"""

ANALYTICS_FAQS = [
    ("How long before the data is useful?",
     "<p>Live fill levels are useful immediately &mdash; you can see which containers are full today from the first week. Pattern analysis needs longer: about four weeks before weekly rhythms are clear, and a full year before you can characterise seasonality properly. Fan&oslash; had a measurable 20% reduction in emptyings within two months, so the operational payoff arrives well before the analytical one.</p>"),
    ("Can we use this data to answer FOI requests and councillor enquiries?",
     "<p>Yes, and several authorities value it as highly as the cost saving. Every reading and confirmed lift is timestamped, so service history for any container over any period is a query rather than an investigation. Vejle's department head specifically cites being able to respond quickly to elected members fielding resident questions &mdash; and being able to show that unnecessary journeys are not being made, which is a political point as much as an operational one.</p>"),
    ("Does the reporting cover carbon and mileage?",
     "<p>Yes. Kilometres travelled, lifts performed and lifts avoided are all recorded, which is the basis for a fuel and CO&#8322; calculation against your fleet's emissions factors. Vejle's programme targets a 5.5 tonne annual CO&#8322; reduction alongside a 30% travel reduction; Stralsund measured weekly mileage falling from 1,677&nbsp;km to 779&nbsp;km. These figures are defensible in a climate report because they rest on counted journeys rather than modelled assumptions.</p>"),
    ("Who owns the data and where is it held?",
     "<p>You do. It is hosted in the United Kingdom, exportable in full at any time, and available through an open API. Fill-level readings are measurements of council or estate assets rather than personal data, so the data protection position is normally straightforward &mdash; but we will support your DPIA and provide the processing detail your information governance team needs. If you end the contract, your history leaves with you.</p>"),
]


def pages():
    return [
        Page(
            path="solutions/",
            nav_key="solutions",
            title="Smart Waste Solutions for UK Councils & Contractors",
            description="Radar bin fill-level sensors, NB-IoT connectivity, dynamic round planning, a driver app and waste analytics, as one managed UK subscription.",
            keywords="smart waste solutions UK, bin sensors and software, waste collection technology, IoT waste platform",
            h1="Solutions",
            eyebrow="Solutions",
            lede="Sensors, round planning and reporting &mdash; sold together, because the parts only work together.",
            body=OVERVIEW_BODY,
            faqs=OVERVIEW_FAQS,
            faq_heading="Buying questions",
            page_type="CollectionPage",
        ),
        Page(
            path="solutions/fill-level-sensors/",
            nav_key="solutions",
            breadcrumbs=CRUMB,
            title="Radar Bin Fill-Level Sensors | 8-Year Battery, NB-IoT",
            description="Radar fill-level sensors for street bins, semi-buried containers and bring sites. Eight-year battery, NB-IoT, ten-minute fit, no wiring or bin changes.",
            keywords="bin fill level sensor, radar waste sensor, ultrasonic vs radar bin sensor, NB-IoT bin sensor UK, smart bin sensor supplier",
            h1="Fill-level sensors and connectivity",
            eyebrow="Solutions",
            lede="Radar measurement, an eight-year battery, and a mobile network that already covers the country. The unglamorous half of the system, and the half that decides whether anyone trusts the other half.",
            body=SENSORS_BODY,
            faqs=SENSORS_FAQS,
            faq_heading="Sensor questions",
            schema=[service_schema(
                "/solutions/fill-level-sensors/",
                "Radar bin fill-level sensors with NB-IoT connectivity",
                "Supply, installation and support of radar fill-level sensors for waste containers in the UK, including SIMs and NB-IoT connectivity, mounting, calibration and central sensor health monitoring.",
                "Waste container fill-level monitoring",
            ), {
                "@type": "Product",
                "@id": SITE["url"] + "/solutions/fill-level-sensors/#product",
                "name": "Radar fill-level sensor for waste containers",
                "category": "IoT waste monitoring sensor",
                "brand": {"@id": SITE["url"] + "/#organization"},
                "description": "A sealed, battery-powered radar sensor fitted inside the lid or top of a waste container. Measures fill level, temperature, position, tilt and battery state, reporting over NB-IoT typically six times a day, with around eight years of battery life.",
                "additionalProperty": [
                    {"@type": "PropertyValue", "name": "Measurement technology", "value": "Millimetre-wave radar"},
                    {"@type": "PropertyValue", "name": "Battery life", "value": "Approximately 8 years at 6 readings per day"},
                    {"@type": "PropertyValue", "name": "Reporting frequency", "value": "6 per day typical, up to 60 per day supported"},
                    {"@type": "PropertyValue", "name": "Connectivity", "value": "NB-IoT over existing UK mobile networks"},
                    {"@type": "PropertyValue", "name": "Installation time", "value": "Approximately 10 minutes per container"},
                    {"@type": "PropertyValue", "name": "Power requirement", "value": "None — self-contained battery, no wiring"},
                ],
            }],
        ),
        Page(
            path="solutions/route-optimisation/",
            nav_key="solutions",
            breadcrumbs=CRUMB,
            title="Dynamic Waste Round Planning & Driver App | Britannia IoT",
            description="Collection rounds rebuilt each morning from live bin fill data, pushed to the driver's tablet with fill levels, navigation and one-tap lift capture.",
            keywords="waste collection route optimisation, dynamic round planning, refuse round software UK, bin collection driver app",
            h1="Dynamic round planning",
            eyebrow="Solutions",
            lede="A round that rebuilds itself from overnight readings, and a driver app the crew will actually use.",
            body=ROUTES_BODY,
            faqs=ROUTES_FAQS,
            faq_heading="Round planning questions",
            schema=[service_schema(
                "/solutions/route-optimisation/",
                "Dynamic waste collection round planning",
                "Software that generates an optimised daily waste collection round from live fill-level readings and delivers it to drivers through a mobile app, with configurable thresholds, multi-stream rounds, contractor access and manual override.",
                "Waste collection route optimisation software",
            )],
        ),
        Page(
            path="solutions/analytics-reporting/",
            nav_key="solutions",
            breadcrumbs=CRUMB,
            title="Waste Analytics, Forecasting & Reporting | Britannia IoT",
            description="Fill history per container, demand heat maps, emptying forecasts, complaint evidence and CO2 reporting, with an open API and full data export.",
            keywords="waste data analytics, bin fill history reporting, waste CO2 reporting, bin estate rationalisation",
            h1="Analytics, forecasting and reporting",
            eyebrow="Solutions",
            lede="The savings pay for the system. The evidence is what makes it permanent.",
            body=ANALYTICS_BODY,
            faqs=ANALYTICS_FAQS,
            faq_heading="Data and reporting questions",
            schema=[service_schema(
                "/solutions/analytics-reporting/",
                "Waste operation analytics, forecasting and reporting",
                "Reporting and forecasting built on fill-level history: container utilisation, demand heat mapping, bin estate rationalisation, complaint and FOI evidence, mileage and CO2 reduction reporting, delivered in-platform and through an open API.",
                "Waste management analytics and reporting",
            )],
        ),
    ]
