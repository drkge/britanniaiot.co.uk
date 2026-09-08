"""Reference pages built for definitional and comparison queries."""

from build import Page, SITE

CRUMB = [("Resources", "/resources/waste-sensor-glossary/")]

GLOSSARY = [
    ("Fill-level sensor",
     "A battery-powered device fitted inside the lid or top of a waste container that measures how full the container is and transmits the reading over a mobile network. Better units measure using radar; cheaper units use ultrasound. Alongside fill level they typically report temperature, GPS position, tilt, battery state and fault status."),
    ("Radar fill-level measurement",
     "Fill-level measurement using millimetre-wave radar reflection. Radar is substantially more tolerant than ultrasound of irregular, absorbent and lightweight materials &mdash; flattened cardboard, paper and film plastic in particular &mdash; which makes it the appropriate technology for recycling containers. Vejle Municipality switched supplier to obtain radar after a non-radar trial produced error reports on up to 30% of readings."),
    ("Ultrasonic fill-level measurement",
     "Fill-level measurement by timing a reflected sound pulse. Cheaper than radar and adequate against flat, hard, reflective surfaces, but prone to false readings against the soft and irregular materials that actually fill waste containers. The commonest cause of a smart waste pilot losing operational credibility."),
    ("NB-IoT",
     "Narrowband Internet of Things: a low-power wide-area mobile standard carried over existing cellular infrastructure. It offers deep penetration &mdash; including below ground level and inside metal enclosures &mdash; very low power consumption, high operational reliability and scalability. It requires no infrastructure of your own, which distinguishes it from LoRaWAN and Sigfox."),
    ("LoRaWAN",
     "A long-range, low-power radio protocol using unlicensed spectrum. Unlike NB-IoT it requires gateways you deploy and maintain yourself. Viable within a bounded estate such as a campus; less attractive for a dispersed council estate, where NB-IoT's use of national carrier infrastructure avoids building a network."),
    ("Fill threshold",
     "The percentage at which a container is flagged for collection. Typically set between 80% and 90%. Vejle flags at 80%; Langeland normally adds a container to the route at 80&ndash;90%. Lower thresholds suit locations reached infrequently or with long drive times; higher thresholds suit containers you can reach the same day."),
    ("Dynamic round planning",
     "Generating a collection round from current fill-level data rather than a fixed timetable, so that only containers at or approaching their threshold are visited. Vejle's round is calculated automatically at 05:00 each morning across 547 instrumented bins."),
    ("Fixed-frequency collection",
     "The conventional model: every container on a round is emptied on a set schedule regardless of how full it is. Simple to plan and simple to contract, but wrong in both directions simultaneously &mdash; wasteful at quiet locations, inadequate at busy ones."),
    ("Emptying forecast",
     "A prediction of when a specific container will reach its threshold, derived from its own fill history, current readings, driver reports and other data. Forecasts allow near-threshold containers to be collected while a vehicle is already in the area, rather than triggering a separate journey later."),
    ("Semi-buried container",
     "A waste container with the majority of its volume below ground level, commonly up to three cubic metres. Popular at bring sites and in holiday areas for capacity and appearance. Its fill level cannot be assessed from ground level at all, which makes it one of the strongest cases for sensors. Fanø Municipality monitors 82 of them."),
    ("Bring site",
     "An unstaffed public recycling point holding containers for several waste streams, often in a car park or at the edge of a settlement. Frequently a long drive from the depot, which is why a wasted journey to one is disproportionately expensive."),
    ("Waste fraction",
     "A separately collected waste stream &mdash; residual, mixed recycling, glass, paper and card, food, textiles. Langeland handles ten fractions across its network, combining glass and metal into one to improve collection efficiency."),
    ("Lift",
     "One emptying of one container. The standard unit of cost in a waste collection contract, and therefore the unit in which savings from sensor-led collection are usually expressed."),
    ("Side waste",
     "Waste left beside a container rather than in it, normally because the container was full. A leading indicator of an under-served location and a direct cause of litter, pest and fly-tipping problems in the surrounding area."),
    ("Bin estate rationalisation",
     "Reducing the number of containers by identifying, from fill history, those that overlap with others or are consistently under-used. Vejle began this once it had accurate location and fill data. Each container removed eliminates a lift, a sensor, a maintenance liability and a vandalism target permanently."),
    ("Baseline",
     "The record of current cost, lifts, working hours and mileage taken before any change, against which a pilot's results are measured. Without one, a pilot produces impressions rather than a business case, and cannot support a procurement decision."),
    ("HWRC",
     "Household Waste Recycling Centre &mdash; a staffed public site accepting bulky and separated household waste. Its containers are strong sensor candidates, because bulk container swaps are expensive and are typically scheduled rather than triggered by need."),
    ("Smart waste management",
     "The general term for using sensors, connectivity and data to plan waste collection according to measured demand rather than a fixed schedule. In practice it means three components: fill-level measurement, a planning system that acts on it, and reporting that makes the outcome visible."),
]

GLOSSARY_BODY = (
    """
<section class="section">
  <div class="wrap wrap-narrow">
    <div class="answer-box">
      <p><strong>Definitions of the terms used in smart waste management and sensor-led collection &mdash; fill-level sensors, radar versus ultrasonic measurement, NB-IoT, fill thresholds, dynamic round planning and the rest &mdash; written for people specifying or procuring these systems in the UK.</strong></p>
    </div>
  </div>
</section>

<section class="section-tight">
  <div class="wrap wrap-narrow prose">
"""
    + "\n".join(
        f'    <h2 id="{t.lower().replace(" ", "-").replace("&mdash;", "")}">{t}</h2>\n    <p>{d}</p>'
        for t, d in GLOSSARY
    )
    + """
  </div>
</section>
"""
)


# --------------------------------------------------------- comparison ----

COMPARE_BODY = """
<section class="section">
  <div class="wrap">
    <div class="answer-box">
      <p><strong>Fixed-frequency collection empties every container on a set schedule regardless of how full it is. Sensor-led collection empties each container when it reaches a set fill threshold, usually 80&ndash;90%. Fixed frequency is simpler to plan and contract; sensor-led collection is cheaper to run, responds to demand spikes, and produces an audit trail. The gap between them widens with drive time between stops and with how variable demand is.</strong></p>
    </div>
  </div>
</section>

<section class="section-tight">
  <div class="wrap">
    <div class="table-scroll">
      <table>
        <caption class="visually-hidden">Comparison of fixed-frequency and sensor-led waste collection</caption>
        <thead><tr><th scope="col"></th><th scope="col">Fixed-frequency collection</th><th scope="col">Sensor-led collection</th></tr></thead>
        <tbody>
          <tr><td>What triggers a visit</td><td>The calendar</td><td>Measured fill level reaching a threshold you set</td></tr>
          <tr><td>Quiet locations</td><td>Emptied anyway &mdash; cost with no output</td><td>Skipped until they need it</td></tr>
          <tr><td>Busy locations</td><td>Overflow between scheduled visits</td><td>Collected when full, including outside the usual pattern</td></tr>
          <tr><td>Demand spikes</td><td>Cannot respond &mdash; heatwaves, events and bank holidays are absorbed as complaints</td><td>Round expands automatically; thresholds and reporting frequency can be tightened for a known peak</td></tr>
          <tr><td>Planning effort</td><td>Low, but the plan is never revisited</td><td>Automatic daily generation, with supervisor override</td></tr>
          <tr><td>Mileage</td><td>Fixed, regardless of need</td><td>Falls with the number of stops &mdash; Stralsund saw 54% less weekly distance</td></tr>
          <tr><td>Service evidence</td><td>None beyond crew recollection</td><td>Every reading and lift timestamped and queryable</td></tr>
          <tr><td>Carbon reporting</td><td>Modelled from scheduled journeys</td><td>Counted from journeys actually made</td></tr>
          <tr><td>Estate review</td><td>Effectively impossible &mdash; no utilisation data</td><td>Fill history identifies overlapping and under-used containers</td></tr>
          <tr><td>Contract negotiation</td><td>Frequency argued from opinion</td><td>Frequency argued from lift and fill data</td></tr>
          <tr><td>Upfront requirement</td><td>None</td><td>An accurate container register and a sensor per container</td></tr>
          <tr><td>Ongoing cost</td><td>Collection cost only</td><td>Collection cost plus a per-container subscription &mdash; offset by avoided lifts</td></tr>
          <tr><td>Best suited to</td><td>Dense urban rounds where every container genuinely fills daily</td><td>Anywhere demand varies, or where drive time between stops is significant</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="section section-alt section-line">
  <div class="wrap">
    <div class="split split-top">
      <div>
        <p class="eyebrow">When fixed frequency is fine</p>
        <h2>The honest case against sensors</h2>
        <p>Sensor-led collection is not universally worthwhile, and any supplier telling you otherwise is selling rather than advising.</p>
        <p>If every container on a round genuinely fills every day, there are no wasted journeys to remove, and a subscription buys you evidence and reporting rather than a saving. If the vehicle passes every container anyway &mdash; kerbside household rounds being the obvious case &mdash; there is no journey to avoid at all. Vejle applied this reasoning deliberately, leaving 328 of its 875 bins uninstrumented because they sit in central locations already emptied daily as part of other routines.</p>
        <p>The two questions worth asking before anything else: how many of last month's lifts went to containers that were less than half full, and how long does a vehicle spend driving between stops? If you cannot answer the first, that is itself the argument for measuring.</p>
      </div>
      <div>
        <div class="keyfacts" style="margin-bottom:0">
          <h3>Where the gap is widest</h3>
          <dl>
            <dt>Strongest case</dt><dd>Rural and edge-of-town bring sites with long drive times</dd>
            <dt>Strong case</dt><dd>Seasonal and visitor locations with volatile demand</dd>
            <dt>Strong case</dt><dd>Semi-buried containers whose fill level cannot be seen</dd>
            <dt>Good case</dt><dd>Street and park bins on generous fixed frequencies</dd>
            <dt>Moderate case</dt><dd>Campus and estate bins &mdash; less mileage, but real labour and appearance gains</dd>
            <dt>Weak case</dt><dd>Town-centre bins that genuinely fill every day</dd>
            <dt>No case</dt><dd>Kerbside household rounds that pass every property regardless</dd>
          </dl>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="eyebrow">Working it out</p>
    <h2 class="measure">How to size the opportunity before you spend anything</h2>
    <div class="grid grid-3 mt-3">
      <div class="card no-push">
        <span class="card-num">01</span>
        <h3>Count the lifts</h3>
        <p>How many container emptyings does your operation perform in a year, on containers a vehicle travels specifically to reach? Exclude kerbside. This is the denominator for everything else.</p>
      </div>
      <div class="card no-push">
        <span class="card-num">02</span>
        <h3>Estimate the waste</h3>
        <p>Ask supervisors what proportion of those containers are typically under half full at collection. The estimate will be wrong, but it establishes whether the potential is 10% or 60% &mdash; and it will almost certainly be understated.</p>
      </div>
      <div class="card no-push">
        <span class="card-num">03</span>
        <h3>Cost a lift properly</h3>
        <p>Include the drive to reach it, not just the emptying. On dispersed rural rounds the travel is the majority of the cost, which is why Langeland's saving came as much from eliminating an inspection round as from fewer collections.</p>
      </div>
    </div>
    <p class="lede mt-3">Multiply those three and you have an order of magnitude. Then measure a single round for 90 days and replace the estimate with a number. <a href="/contact/">We will help you build the model</a>, including the parts that argue against buying anything.</p>
  </div>
</section>
"""

COMPARE_FAQS = [
    ("Is sensor-led collection always cheaper than fixed frequency?",
     "<p>No. It is cheaper wherever a meaningful share of current journeys go to containers that did not need emptying, which is most operations but not all. On a dense urban round where every bin genuinely fills daily there is little to recover, and the subscription buys evidence and reporting rather than a saving. On kerbside household rounds, where the vehicle passes every property anyway, there is no journey to avoid and no case at all.</p>"),
    ("What fill threshold gives the best balance?",
     "<p>80&ndash;90% is the established starting range. Vejle flags at 80%, Langeland typically adds a container at 80&ndash;90%. The variable is headroom: how long between the reading and the visit, and how bad an overflow would be at that location. A rural bring site reached twice a week needs a lower threshold than a town-centre bin you can reach the same afternoon. A promenade bin in August warrants a lower threshold than the same bin in November. Most operations tune thresholds during the first couple of months.</p>"),
    ("Can we run a hybrid model?",
     "<p>Yes, and most mature deployments do. Instrument the containers where the journey is discretionary; leave the ones already passed daily on a fixed routine. Vejle instrumented 547 of 875 bins on exactly this logic. Hybrid is not a compromise &mdash; it is the correct answer, because it puts the subscription only where it changes a decision.</p>"),
    ("How does this affect a waste collection contract?",
     "<p>It changes what the contract can be written against. Fixed-frequency contracts specify visits; sensor-led operation makes it possible to specify outcomes &mdash; containers not exceeding a fill threshold, response time from flag to lift, evidenced service history. That is a better contract for a commissioning authority and, for a contractor confident in its service, a better one to be measured by. It also removes most of the ambiguity that makes missed-collection disputes unresolvable.</p>"),
    ("Do the sensors pay for themselves?",
     "<p>Where there is genuine slack in the current schedule, quickly. Stralsund reported that its 35-bin pilot paid for itself in under a year on avoided collections and mileage alone, and extended the deployment on that basis. Fan&oslash; achieved a 20% reduction in emptyings within two months of switching on. Both had generous fixed frequencies to begin with. The point of a measured pilot is to find out whether yours does too, before committing to anything larger.</p>"),
]


def pages():
    return [
        Page(
            path="resources/waste-sensor-glossary/",
            nav_key="",
            breadcrumbs=[],
            title="Smart Waste Glossary | Fill-Level Sensors & NB-IoT Terms",
            description="Plain definitions of smart waste terms: fill-level sensors, radar vs ultrasonic, NB-IoT, LoRaWAN, fill thresholds, dynamic round planning, lifts.",
            keywords="what is a fill level sensor, NB-IoT definition, smart waste glossary, radar vs ultrasonic bin sensor, dynamic round planning meaning",
            h1="Smart waste glossary",
            eyebrow="Reference",
            lede="The terms that appear in specifications, tenders and supplier proposals, defined without the marketing.",
            body=GLOSSARY_BODY,
            page_type="WebPage",
            schema=[{
                "@type": "DefinedTermSet",
                "@id": SITE["url"] + "/resources/waste-sensor-glossary/#termset",
                "name": "Smart waste management glossary",
                "description": "Definitions of terms used in sensor-led waste collection and smart waste management in the United Kingdom.",
                "inLanguage": "en-GB",
                "publisher": {"@id": SITE["url"] + "/#organization"},
                "hasDefinedTerm": [
                    {
                        "@type": "DefinedTerm",
                        "@id": SITE["url"] + "/resources/waste-sensor-glossary/#" + t.lower().replace(" ", "-"),
                        "name": t,
                        "description": d.replace("&mdash;", "—").replace("&ndash;", "–").replace("&oslash;", "ø"),
                        "inDefinedTermSet": {"@id": SITE["url"] + "/resources/waste-sensor-glossary/#termset"},
                    }
                    for t, d in GLOSSARY
                ],
            }],
            cta=("Specifying a system?",
                 "We will supply the technical detail your procurement team needs to write a specification that can actually be evaluated &mdash; starting with why the word radar belongs in it."),
        ),
        Page(
            path="resources/sensor-led-vs-fixed-frequency-collections/",
            nav_key="",
            breadcrumbs=[("Glossary", "/resources/waste-sensor-glossary/")],
            title="Sensor-Led vs Fixed-Frequency Waste Collection Compared",
            description="Fixed-frequency vs sensor-led waste collection compared on cost, demand response, evidence and carbon, plus when sensors are not worth buying.",
            keywords="sensor led vs fixed frequency collection, dynamic vs scheduled waste collection, when are bin sensors worth it, waste collection frequency optimisation",
            h1="Sensor-led vs fixed-frequency collection",
            eyebrow="Comparison",
            lede="Where the two models differ, where the gap is widest, and the cases where fixed frequency is still the right answer.",
            body=COMPARE_BODY,
            faqs=COMPARE_FAQS,
            faq_heading="Choosing between the two",
            page_type="WebPage",
        ),
    ]
