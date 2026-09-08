"""Results: index plus four deployment case studies."""

from build import Page, SITE

CRUMB = [("Results", "/results/")]

DISCLOSURE = (
    '<p class="note">These figures are as published by the operating authority. '
    'They document a deployment of the sensor and software platform that Britannia IoT '
    'Solutions supplies in the United Kingdom, and are presented as evidence for the '
    'technology rather than as a Britannia IoT Solutions client engagement. '
    'Outcomes in any given operation depend on current collection frequency, bin density '
    'and round geography &mdash; which is what a pilot measures.</p>'
)


def article_schema(path, headline, desc, keywords, about):
    url = SITE["url"] + path
    return {
        "@type": "Article",
        "@id": url + "#article",
        "headline": headline,
        "description": desc,
        "keywords": keywords,
        "about": about,
        "author": {"@id": SITE["url"] + "/#organization"},
        "publisher": {"@id": SITE["url"] + "/#organization"},
        "datePublished": "2026-09-05",
        "dateModified": SITE["updated"],
        "isPartOf": {"@id": SITE["url"] + "/#website"},
        "mainEntityOfPage": {"@id": url + "#webpage"},
        "inLanguage": "en-GB",
    }


# --------------------------------------------------------------- index ----

INDEX_BODY = """
<section class="section">
  <div class="wrap">
    <div class="answer-box">
      <p><strong>Four public bodies, four different waste problems, four sets of published numbers. Stralsund cut street-bin collections by 71% and mileage by 54%. Vejle moved from twice-weekly to fortnightly collection across 547 instrumented bins. Fan&oslash; reduced emptyings by 20% within two months. Langeland removed a collection vehicle from service and eliminated a 176&nbsp;km manual inspection round.</strong></p>
      <p class="mt-1">All four are live deployments of the sensor and software platform Britannia IoT Solutions supplies in the UK. They are in Denmark and Germany, and we present them as the technology's track record &mdash; not as our own client list.</p>
    </div>
  </div>
</section>

<section class="section-tight">
  <div class="wrap">
    <div class="stat-band">
      <div class="stat"><span class="stat-num">71%</span><span class="stat-label">fewer weekly collections &mdash; 1,548 down to 445</span><span class="stat-src">Stralsund, Germany</span></div>
      <div class="stat"><span class="stat-num">54%</span><span class="stat-label">fewer weekly kilometres &mdash; 1,677 down to 779</span><span class="stat-src">Stralsund, Germany</span></div>
      <div class="stat"><span class="stat-num">30%</span><span class="stat-label">reduction in working hours on the task</span><span class="stat-src">Stralsund, Germany</span></div>
      <div class="stat"><span class="stat-num">20%</span><span class="stat-label">fewer emptyings within two months</span><span class="stat-src">Fan&oslash;, Denmark</span></div>
      <div class="stat"><span class="stat-num">2.0&rarr;1.5</span><span class="stat-label">full-time staff on bin emptying</span><span class="stat-src">Vejle, Denmark</span></div>
      <div class="stat"><span class="stat-num">1</span><span class="stat-label">collection vehicle removed from the fleet</span><span class="stat-src">Langeland, Denmark</span></div>
      <div class="stat"><span class="stat-num">1 / 220</span><span class="stat-label">sensor faults in the first four months</span><span class="stat-src">Langeland, Denmark</span></div>
      <div class="stat"><span class="stat-num">&lt;12</span><span class="stat-label">months for the pilot to pay for itself</span><span class="stat-src">Stralsund, Germany</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="eyebrow">Case studies</p>
    <h2 class="measure">Read them in full</h2>
    <div class="grid grid-2 mt-3">
      <a class="card case-card" href="/results/stralsund-smart-street-bins/">
        <span class="case-flag">Stralsund, Germany</span>
        <p class="case-headline">71% fewer collections</p>
        <h3>Town-centre street bins</h3>
        <p>A city of 55,000 collecting 180 tonnes a year from public bins fitted radar sensors to 35 town-centre 60-litre bins. Collections fell from twice a week to only when needed. The pilot paid back inside a year and was extended by 100 more sensors.</p>
        <span class="arrow-link">Read the Stralsund case study</span>
      </a>
      <a class="card case-card" href="/results/vejle-dynamic-round-planning/">
        <span class="case-flag">Vejle, Denmark</span>
        <p class="case-headline">Twice weekly &rarr; fortnightly</p>
        <h3>Municipality-wide rollout</h3>
        <p>547 of 875 public bins along 2,000&nbsp;km of roads, with an optimised round calculated automatically at 05:00 daily. A funded pilot on one trial route led to a council decision to roll out across the municipality.</p>
        <span class="arrow-link">Read the Vejle case study</span>
      </a>
      <a class="card case-card" href="/results/fano-seasonal-recycling-sites/">
        <span class="case-flag">Fan&oslash;, Denmark</span>
        <p class="case-headline">20% fewer emptyings</p>
        <h3>Seasonal recycling sites</h3>
        <p>An island whose population runs between 3,000 and 50,000 across the year, with 82 semi-buried containers across 14 sites. Emptying had been done, in the authority's own words, by gut feeling.</p>
        <span class="arrow-link">Read the Fan&oslash; case study</span>
      </a>
      <a class="card case-card" href="/results/langeland-island-recycling-network/">
        <span class="case-flag">Langeland, Denmark</span>
        <p class="case-headline">One vehicle removed</p>
        <h3>Rural bring-site network</h3>
        <p>220 sensors across roughly 30 collection points serving 2,300 holiday households, replacing a 176&nbsp;km manual inspection round that took a day and a half and produced a paper report.</p>
        <span class="arrow-link">Read the Langeland case study</span>
      </a>
    </div>
  </div>
</section>

<section class="section section-alt section-line">
  <div class="wrap">
    <p class="eyebrow">Comparison</p>
    <h2 class="measure">The four deployments side by side</h2>
    <div class="table-scroll mt-2">
      <table>
        <caption class="visually-hidden">Comparison of four published fill-level sensor deployments</caption>
        <thead><tr><th scope="col">Deployment</th><th scope="col">Setting</th><th scope="col">Scale</th><th scope="col">Headline outcome</th></tr></thead>
        <tbody>
          <tr><td><a href="/results/stralsund-smart-street-bins/">Stralsund</a></td><td>Historic town centre, 55,000 residents</td><td>35 bins of 60 litres, rising by 100+</td><td>71% fewer collections, 54% fewer km, 30% fewer working hours, payback under a year</td></tr>
          <tr><td><a href="/results/vejle-dynamic-round-planning/">Vejle</a></td><td>Municipality-wide, 2,000&nbsp;km of roads</td><td>547 of 875 public bins</td><td>Twice weekly to fortnightly; 2.0 to 1.5 FTE; targets of 30% less travel, 40% economic gain, 5.5 t CO&#8322;/yr</td></tr>
          <tr><td><a href="/results/fano-seasonal-recycling-sites/">Fan&oslash;</a></td><td>Island, population 3,000&ndash;50,000 by season</td><td>82 semi-buried containers, 14 sites</td><td>20% fewer emptyings in two months against a 25% target</td></tr>
          <tr><td><a href="/results/langeland-island-recycling-network/">Langeland</a></td><td>Rural island, ~30 collection points</td><td>220 sensors, 10 waste fractions</td><td>One vehicle removed; 176&nbsp;km inspection round eliminated; 1 fault in 220 units</td></tr>
        </tbody>
      </table>
    </div>
    <p class="note">Figures as published by the operating authorities. Britannia IoT Solutions supplies the same sensor and software platform in the United Kingdom.</p>
  </div>
</section>
"""

INDEX_FAQS = [
    ("Are these your customers?",
     "<p>No, and we would rather say so plainly. These are published deployments by European public bodies of the sensor and software platform we supply in the UK. We present them as evidence that the technology works in daily municipal service, with attributable numbers behind it, because that is a more useful thing for a prospective customer to assess than an unverifiable claim. Britannia IoT Solutions is a young company and our own UK deployments are at an early stage.</p>"),
    ("Why are all the examples European rather than British?",
     "<p>Because Denmark and Germany adopted this technology at municipal scale several years before the UK did, so that is where the multi-year operating evidence exists. The underlying situation is not materially different: a district council emptying street bins twice a week to a fixed timetable faces the same problem as Stralsund did, and a coastal authority with a summer population spike faces Fan&oslash;'s problem almost exactly.</p>"),
    ("Would we get the same results?",
     "<p>Possibly better, possibly worse, and nobody can tell you which before measuring. The gains depend on how over-serviced your current rounds are and how much driving sits between your stops. An authority emptying rural bring sites on a fixed fortnightly cycle has a great deal of slack to recover; a dense urban round where every bin genuinely fills daily has very little. That is exactly what a 90-day pilot against your own baseline establishes, at small cost, before any significant commitment.</p>"),
]


# ----------------------------------------------------------- Stralsund ----

STRALSUND_BODY = """
<section class="section">
  <div class="wrap">
    <div class="split split-article">
      <div class="prose">
        <div class="answer-box">
          <p><strong>The City of Stralsund fitted radar fill-level sensors to 35 town-centre public waste bins as a one-year trial. Weekly collections fell from 1,548 to 445 &mdash; a 71% reduction &mdash; and weekly distance driven fell from 1,677&nbsp;km to 779&nbsp;km, down 54%. Working hours on the task fell 30%. The investment paid for itself in under a year, and the city committed to installing at least 100 more sensors.</strong></p>
        </div>

        <h2>The situation</h2>
        <p>Stralsund is a Hanseatic city on Germany's Baltic coast with 55,000 residents and a UNESCO-listed old town. Its public bins &mdash; typically 60-litre units on streets and in parks &mdash; produce around 180 tonnes of waste a year, and were emptied twice a week regardless of use.</p>
        <p>The trial formed part of a wider Smart City programme in Mecklenburg-Western Pomerania. The stated aims were straightforward: reduce the number of refuse vehicle journeys, and with them staff costs, operating costs and CO&#8322; emissions.</p>

        <h2>What was deployed</h2>
        <p>Radar sensors were mounted in the lids of 35 bins in the old town. Each sensor uses radar waves to measure the volume of waste beneath it and therefore the current fill level, transmitting six times a day. The city's waste management team receives the readings continuously and empties bins as needed rather than on a schedule.</p>
        <p>The hardware itself drew unusual enthusiasm from the client. Stralsund's head of waste management described the radar sensor as a technical marvel &mdash; a small, lightweight, shock-resistant box containing the electronics, the power supply and the mini-radar, with a battery lasting eight years at six transmissions a day.</p>

        <h2>The results</h2>
        <p>After the first few months:</p>
        <ul>
          <li>Weekly collections fell from <strong>1,548 to 445</strong>, a reduction of <strong>71%</strong>.</li>
          <li>Weekly distance travelled by refuse vehicles fell from <strong>1,677&nbsp;km to 779&nbsp;km</strong>, a reduction of <strong>54%</strong>.</li>
          <li>Working hours on the task fell by <strong>30%</strong>, releasing staff for other urgent work.</li>
          <li>The investment <strong>paid for itself in under a year</strong>.</li>
        </ul>
        <p>The city noted that these results came from the quieter winter and spring months and still met expectations.</p>

        <div class="pullquote">
          <blockquote>We have saved over half the kilometres travelled by the refuse collection lorries, and we have been able to reduce working hours by 30 per cent compared to before. This has allowed us to deploy staff to other urgent tasks, and we have become more efficient overall.</blockquote>
          <cite><b>Head of waste management</b> &mdash; Stadt Stralsund</cite>
        </div>

        <h2>What the data revealed</h2>
        <p>The most instructive finding was not the aggregate saving but the variance underneath it. Usage differed enormously between individual bins: some remained virtually empty between the twice-weekly visits, while others filled far faster than anyone had expected. No amount of experience produces that map. Only measurement does &mdash; and it is the reason a uniform frequency is always wrong in both directions at once.</p>

        <h2>The crew's view</h2>
        <p>The driver was reported as equally positive. On a tablet he can see how full each bin is and its exact location, and plans his own route based on which bins are full and which are not. The city's account is explicit that this saves a lot of time &mdash; and it illustrates a pattern common to every successful deployment: the crew is given the data and the discretion, rather than a route to follow blindly.</p>

        <h2>What happened next</h2>
        <p>The pilot was scheduled to run for a year before a decision on continuation. It did not need the full year. On the evidence of the first months, the city committed to installing at least a further <strong>100 radar sensors</strong> that year, with expansion continuing in subsequent years.</p>
      </div>

      <div>
        <div class="keyfacts">
          <h2>Deployment at a glance</h2>
          <dl>
            <dt>Location</dt><dd>Stralsund, Mecklenburg-Western Pomerania, Germany</dd>
            <dt>Population</dt><dd>55,000</dd>
            <dt>Waste volume</dt><dd>180 tonnes a year from public bins</dd>
            <dt>Containers</dt><dd>35 public bins, typically 60 litres, in the old town</dd>
            <dt>Technology</dt><dd>Radar fill-level sensors mounted in the bin lid</dd>
            <dt>Reporting</dt><dd>6 readings per day</dd>
            <dt>Battery</dt><dd>8 years at that frequency</dd>
            <dt>Before</dt><dd>Collections twice weekly regardless of fill</dd>
            <dt>After</dt><dd>Collections only when sensors indicate bins are nearly full</dd>
            <dt>Collections</dt><dd>1,548 &rarr; 445 per week (&minus;71%)</dd>
            <dt>Distance</dt><dd>1,677&nbsp;km &rarr; 779&nbsp;km per week (&minus;54%)</dd>
            <dt>Working hours</dt><dd>&minus;30%</dd>
            <dt>Payback</dt><dd>Under 12 months</dd>
            <dt>Next phase</dt><dd>At least 100 further sensors, with continued expansion</dd>
            <dt>Context</dt><dd>Part of a regional Smart City programme</dd>
          </dl>
        </div>
        <p><a class="arrow-link" href="/sectors/local-authorities/">How this applies to a UK council</a></p>
      </div>
    </div>
    """ + DISCLOSURE + """
  </div>
</section>
"""

STRALSUND_FAQS = [
    ("Is a 71% reduction realistic for a UK town centre?",
     "<p>It is realistic where the starting point is the same: bins emptied on a fixed twice-weekly cycle regardless of use. That describes a great many UK street-bin rounds. The reduction was as large as it was precisely because the previous frequency was generous relative to actual demand &mdash; the data showed some bins virtually empty between visits. A round where bins genuinely fill every day has far less slack, and would show a much smaller figure. The only way to know which you have is to measure for a few weeks before changing anything, which is why we build an observation period into every pilot.</p>"),
    ("Only 35 bins &mdash; is that a large enough sample to trust?",
     "<p>For a decision about whether to expand, yes: 35 bins over several months produces thousands of readings and a clear picture of variance across a comparable set of locations. It is also the right size for a first commitment &mdash; small enough to abandon cheaply, large enough to be representative. Stralsund did not wait for the planned full year before extending by another 100 units, which is a reasonable indication of how clear the signal was.</p>"),
    ("Does it hold up outside winter and spring?",
     "<p>Stralsund made this caveat itself &mdash; that the early results came from quieter months. Higher demand narrows the gap between fixed and sensor-led collection at the busiest bins, since those genuinely need frequent emptying. But it widens it at the quiet ones, and it is at peak that a fixed timetable fails in the other direction by leaving busy bins overflowing. Fan&oslash;'s seasonal deployment, where summer population multiplies sixteenfold, is the better guide to peak-season behaviour.</p>"),
]


# --------------------------------------------------------------- Vejle ----

VEJLE_BODY = """
<section class="section">
  <div class="wrap">
    <div class="split split-article">
      <div class="prose">
        <div class="answer-box">
          <p><strong>Vejle Municipality fitted fill-level sensors to 547 of its 875 public waste bins, spread along 2,000&nbsp;km of roads. An optimised collection round is now calculated automatically at 05:00 each morning. Average collection intervals moved from once or twice a week to once a fortnight, and staffing on the task fell from two full-time employees to one and a half.</strong></p>
        </div>

        <h2>From trial route to council decision</h2>
        <p>Vejle allocated funding for a pilot on a single trial route, with the objective of replacing estimated-frequency emptying with data-driven planning. The test was intended to establish three things: whether collection could be optimised, whether service to citizens improved, and whether waste management became more environmentally sound.</p>
        <p>It demonstrated clear optimisation potential and a positive business case, and the fill-level sensors were subsequently rolled out across the municipality following a council decision. This sequence &mdash; funded pilot, measured business case, political decision, phased rollout &mdash; is the one we recommend to UK authorities, for the same reasons.</p>

        <h2>The deployment</h2>
        <p>547 of the municipality's 875 public bins now carry radar sensors mounted on the inside of the lid. The remaining 328 sit in central locations in Vejle and the municipality's main towns, where they are emptied daily by staff as part of other routines &mdash; there is no wasted journey to eliminate, so there is nothing for a sensor to save.</p>
        <p>That distinction matters, and it is a point of discipline worth borrowing: instrument the containers where a vehicle travels specifically to reach them, not the ones already passed every day.</p>
        <p>Sensors flag a bin as ready for emptying at <strong>80% full</strong> and report six times a day over NB-IoT. The platform collects the readings and generates optimised rounds online for the municipality's internal contractor, the Materielg&aring;rden, which carries out the collections.</p>

        <h2>The results</h2>
        <ul>
          <li>Collection intervals moved from <strong>once or twice a week to an average of once a fortnight</strong>.</li>
          <li>Staffing on bin emptying fell from <strong>two full-time employees to one and a half</strong>, with scope for further reduction through ongoing optimisation.</li>
          <li>The freed capacity was redeployed &mdash; with the same staff, the team also now collects waste along roads and at road bridges.</li>
          <li>Programme targets: <strong>30% reduced travel</strong>, a <strong>40% economic gain</strong> and a reduction of <strong>5.5 tonnes of CO&#8322; per year</strong>.</li>
        </ul>

        <div class="pullquote">
          <blockquote>Previously we would drive out to the bins once or twice a week, but now we manage to empty them on average every fortnight.
          </blockquote>
          <cite><b>Operations assistant, Roads &amp; Parks</b> &mdash; Vejle Municipality</cite>
        </div>

        <h2>Why they changed sensor supplier</h2>
        <p>This is the most useful part of the Vejle story for anyone writing a specification. The original 2021 trial used non-radar fill-level sensors and produced error reports on <strong>up to 30% of readings</strong>. That level of false reporting is fatal: once operations staff have been sent to bins that turn out to be half empty, they stop acting on the data, and the project dies regardless of what the dashboard shows.</p>
        <p>Vejle switched supplier specifically to obtain radar-based measurement, and now experiences very few error reports &mdash; describing the radar sensors as performing clearly better than the goal set for the test period. Signal coverage over NB-IoT was also reported as very good, with fill levels updating six times a day.</p>
        <p>If you take one line from this case study into a procurement specification, make it <em>radar</em>.</p>

        <h2>The forecasting layer</h2>
        <p>Round planning uses an AI forecasting tool that improves over time at predicting when each individual container will next need emptying, combining current sensor measurements, historical fill patterns, drivers' reports and other data sources. The practical benefit is consolidation: a container approaching threshold can be collected while a vehicle is already in the area, rather than triggering its own journey days later.</p>

        <h2>What made it work</h2>
        <p>Vejle's team are unusually candid that the hard part was not the technology. Implementation required discipline and fixed routines in registering every bin with its type and GPS location in the municipality's database, and one person responsible for coordinating across the departments involved and for keeping that location data correct.</p>
        <p>The second requirement was driver buy-in. The operations assistant responsible for the rollout makes the point directly: it is important that drivers support the digital solution, and they do, because it is easy to use &mdash; including for substitutes. A system that only the regular driver can operate fails the first time someone is off sick.</p>

        <h2>The political dividend</h2>
        <p>An outcome the authority did not initially anticipate: the ability to answer elected members quickly when residents raise questions about bins. The head of Roads &amp; Parks notes that politicians like being able to show that unnecessary journeys are not being made, because it demonstrates that the climate has been considered. For a UK council with a declared climate emergency, that is a directly transferable argument.</p>
      </div>

      <div>
        <div class="keyfacts">
          <h2>Deployment at a glance</h2>
          <dl>
            <dt>Location</dt><dd>Vejle Municipality, Denmark</dd>
            <dt>Estate</dt><dd>875 public waste bins across 2,000&nbsp;km of roads</dd>
            <dt>Instrumented</dt><dd>547 bins</dd>
            <dt>Not instrumented</dt><dd>328 central bins already emptied daily as part of other routines</dd>
            <dt>Technology</dt><dd>Radar sensors mounted inside the bin lid, NB-IoT</dd>
            <dt>Reporting</dt><dd>6 readings per day</dd>
            <dt>Threshold</dt><dd>Flagged for emptying at 80% full</dd>
            <dt>Round generation</dt><dd>Automatic, calculated at 05:00 daily</dd>
            <dt>Collections by</dt><dd>Materielg&aring;rden, the municipality's internal contractor</dd>
            <dt>Interval before</dt><dd>Once or twice a week</dd>
            <dt>Interval after</dt><dd>Once a fortnight on average</dd>
            <dt>Staffing</dt><dd>2.0 &rarr; 1.5 full-time employees</dd>
            <dt>Targets</dt><dd>30% less travel, 40% economic gain, 5.5 t CO&#8322;/yr</dd>
            <dt>Earlier trial</dt><dd>2021, non-radar sensors, up to 30% error reports &mdash; supplier changed</dd>
            <dt>Fully implemented</dt><dd>2023</dd>
          </dl>
        </div>
        <p><a class="arrow-link" href="/solutions/fill-level-sensors/">Why radar rather than ultrasonic</a></p>
      </div>
    </div>
    """ + DISCLOSURE + """
  </div>
</section>
"""

VEJLE_FAQS = [
    ("Why did they only instrument 547 of 875 bins?",
     "<p>Because the other 328 are in central locations already emptied daily by staff as part of other routines. There is no journey to avoid at those bins, so a sensor would produce information nobody would act on. It is a good discipline to copy: instrument the containers a vehicle travels specifically to reach, and leave the ones already passed every day alone. It also keeps the subscription cost proportionate to the saving.</p>"),
    ("What does the 30% error rate on the earlier trial tell us?",
     "<p>That measurement technology is the whole ball game. Vejle's 2021 trial used non-radar sensors and produced error reports on up to 30% of readings, which is enough to destroy operational confidence entirely &mdash; a supervisor sent to two empty bins stops trusting the third flag. The authority changed supplier to obtain radar measurement and now reports very few faults. When writing a specification, the word to insist on is <em>radar</em>, not simply &ldquo;fill-level sensors&rdquo;.</p>"),
    ("How does a fortnightly interval not cause overflow?",
     "<p>Because it is an average outcome, not an imposed frequency. No bin is on a fortnightly schedule; each is collected when it reaches 80% full, and the fortnightly figure is simply what that works out to across the estate. A busy bin is still emptied often. What disappeared is the routine journey to bins that were nowhere near full &mdash; which is also why service to residents did not deteriorate.</p>"),
    ("Did Vejle reduce staff?",
     "<p>From 2.0 to 1.5 full-time employees on bin emptying, with the freed capacity redeployed rather than removed &mdash; the same team now also collects waste along roads and at road bridges, work that had not previously been getting done. The authority expects further optimisation to reduce the emptying requirement more. It is worth being straightforward with crews about this from the outset, because they will identify the implication immediately.</p>"),
]


# ---------------------------------------------------------------- Fanø ----

FANO_BODY = """
<section class="section">
  <div class="wrap">
    <div class="split split-article">
      <div class="prose">
        <div class="answer-box">
          <p><strong>Fan&oslash; Municipality is a Danish island whose population fluctuates between 3,000 and 50,000 across the year. It installed fill-level sensors on all 82 of its semi-buried waste containers across 14 recycling sites. Within two months, the number of emptyings had fallen by 20%, against a target of 25%.</strong></p>
        </div>

        <h2>Why fixed frequencies were impossible</h2>
        <p>Fan&oslash; has roughly 3,400 permanent residents and around 2,900 summer cottages. It operates six &ldquo;super&rdquo; recycling collection points and eight regular recycling stations. The regular stations mainly serve permanent residents and take cardboard, plastic and cans; the super points sit near the holiday cottages and also take organic and residual waste. All 82 containers are semi-buried and hold up to three cubic metres.</p>
        <p>In areas with permanent residents, containers typically take between two weeks and a month to fill. In the summer cottage areas, the same containers fill in anywhere between one or two days and several weeks, depending on the weather. The senior engineer responsible described planning efficient emptying in advance as almost impossible, and was blunt about the previous method: emptying happened by gut feeling.</p>
        <p>The pressure was compounding. Increased online shopping and greater environmental awareness among residents and visitors had pushed recycling volumes at the collection points roughly <strong>20% above the level assumed when the collection contract was tendered</strong>. The authority needed better operating economics and, simultaneously, to stop residents encountering overloaded containers.</p>

        <div class="pullquote">
          <blockquote>We simply cannot plan our emptyings because a few days of sunshine can change the picture completely. So far, the emptying has taken place by gut feeling, and that's how we usually do it.</blockquote>
          <cite><b>Senior engineer, technical administration</b> &mdash; Fan&oslash; Municipality</cite>
        </div>

        <h2>What was deployed</h2>
        <p>Sensors were installed on all 82 containers, measuring fill level and passing the data to the municipality via the cloud. Signals are sent up to 60 times a day, giving minimal battery consumption, low cost and good coverage.</p>
        <p>The workflow is simple and worth describing because it is what most UK authorities would actually run. On screen, the engineer sees every container with its fill level marked green, amber or red. He marks the containers to be emptied, creates a route plan, and sends it to the contractor, who receives it in the driver app. The contractor uses the same app to report when each container has been emptied. Fill history for each container is available, so he can judge how urgent an emptying is rather than treating every red flag identically.</p>

        <h2>An honest note about accuracy</h2>
        <p>Accuracy was not good at the beginning. Working with the supplier, the authority established that the sensor needed to be positioned slightly differently to avoid false signals. Once repositioned, when a sensor reported 90% full, it was 90% full. A built-in algorithm also learns continuously and becomes more accurate over time.</p>
        <p>We include this deliberately. Mounting position is the most common cause of early inaccuracy in a sensor deployment, and it is entirely avoidable &mdash; which is why we set position per container type at installation and validate first readings physically before a container joins live round planning.</p>

        <h2>The results</h2>
        <ul>
          <li>Emptyings reduced by <strong>20% within the first two months</strong>, against a target of 25%.</li>
          <li>The target reduction would bring the number of emptyings back down to the level assumed in the original tender, despite volumes having grown 20% since.</li>
          <li>The authority expected the investment to pay for itself within a manageable period.</li>
          <li>Complaints about missed emptying became documentable &mdash; the municipality can now show whether a container was emptied or not.</li>
        </ul>

        <h2>Bringing the contractor in</h2>
        <p>Fan&oslash;'s handling of its contractor is instructive, because the contractor's initial concern is universal. The lorry driver, the engineer noted, might worry about having fewer containers to empty &mdash; but he shouldn't. He stops spending time checking containers that turn out to be half full and which it makes no sense to empty and invoice, and that time can be sold to another customer. His administration also reduces, because invoicing data comes directly through the app.</p>
        <p>Connecting the contractor to the system was planned as the project's next step, so that emptying orders arrive directly from the platform rather than being passed on by the municipality.</p>
      </div>

      <div>
        <div class="keyfacts">
          <h2>Deployment at a glance</h2>
          <dl>
            <dt>Location</dt><dd>Fan&oslash; Municipality, Denmark (island)</dd>
            <dt>Population</dt><dd>3,000 to 50,000 depending on season</dd>
            <dt>Permanent residents</dt><dd>Approximately 3,400</dd>
            <dt>Summer cottages</dt><dd>Approximately 2,900</dd>
            <dt>Sites</dt><dd>6 super recycling points, 8 regular recycling stations</dd>
            <dt>Containers</dt><dd>82 semi-buried, up to 3 m&sup3; each</dd>
            <dt>Reporting</dt><dd>Up to 60 signals per day</dd>
            <dt>Fill pattern &mdash; resident areas</dt><dd>2 weeks to 1 month</dd>
            <dt>Fill pattern &mdash; cottage areas</dt><dd>1&ndash;2 days to several weeks</dd>
            <dt>Volume growth</dt><dd>~20% above the level assumed at tender</dd>
            <dt>Target</dt><dd>25% reduction in emptyings</dd>
            <dt>Achieved</dt><dd>20% reduction within two months</dd>
            <dt>Early issue</dt><dd>Sensor mounting position causing false signals &mdash; resolved by repositioning</dd>
            <dt>Contractor</dt><dd>Receives route plans and reports completion through the driver app</dd>
          </dl>
        </div>
        <p><a class="arrow-link" href="/sectors/tourism-coastal-parks/">How this applies to a UK coastal authority</a></p>
      </div>
    </div>
    """ + DISCLOSURE + """
  </div>
</section>
"""

FANO_FAQS = [
    ("Accuracy was poor at first. Should that worry us?",
     "<p>It should inform how you run an installation rather than put you off. The cause was mounting position, not the sensor: a unit placed where a fixed object sits in its field of view reads the object instead of the waste. Repositioning fixed it, and afterwards a reported 90% meant 90%. We treat this as a solved problem by setting mounting position per container type during installation and physically validating first readings before a container enters live round planning &mdash; which is exactly the step that was missing at the start of Fan&oslash;'s deployment.</p>"),
    ("Does this apply to a UK coastal or tourist authority?",
     "<p>Almost line for line. Substitute a Cornish coastal parish, a Lake District village or a Norfolk broads settlement for Fan&oslash; and the description holds: a small permanent population, a large seasonal one, containers whose fill rate depends on the weather, and a collection contract priced against volumes that have since grown. The seasonal swing is precisely the condition a fixed timetable cannot serve, and it is where sensors deliver the most.</p>"),
    ("Why up to 60 readings a day when other deployments use six?",
     "<p>Because the fill rate is volatile. A container that can go from empty to full in a day during a hot spell needs closer monitoring than a street bin filling steadily over a fortnight. Higher reporting frequency shortens battery life proportionally, so it is a deliberate trade-off made per deployment &mdash; and it can be varied seasonally, running high in peak months and lower over winter.</p>"),
    ("Can semi-buried containers really be monitored reliably?",
     "<p>Yes, and they are among the best candidates, precisely because there is no way to judge their fill level from ground level. Fan&oslash; runs 82 of them at up to three cubic metres each. NB-IoT was chosen in part because it maintains a signal below ground level and inside metal enclosures where ordinary mobile connectivity degrades.</p>"),
]


# ------------------------------------------------------------ Langeland ---

LANGELAND_BODY = """
<section class="section">
  <div class="wrap">
    <div class="split split-article">
      <div class="prose">
        <div class="answer-box">
          <p><strong>Langelands Forsyning, the utility for a Danish island, installed 220 fill-level sensors across roughly 30 collection points. A 176&nbsp;km manual inspection round that consumed a day and a half was eliminated entirely, the utility removed one collection vehicle from service, and overflowing containers in holiday-home areas stopped being a problem.</strong></p>
        </div>

        <h2>The round before</h2>
        <p>Every cycle, an employee drove a <strong>176&nbsp;km round trip</strong> across the island to check containers at 50 recycling stations. It took a day and a half and produced a paper report listing fill levels. A driver then used that report to plan which containers to empty.</p>
        <p>Two problems, beyond the obvious cost. The process was cumbersome, and the assessment varied depending on who made it. A container one inspector called nearly full was, to another, comfortably fine for another week. The operations manager's summary was that far too much time was being spent checking the municipality's environmental stations.</p>

        <h2>What was deployed</h2>
        <p>The utility approached it systematically, starting with about ten sensors and scaling to <strong>220</strong> &mdash; one for every container. The island now has around 30 collection points covering, among other areas, all holiday homes with 2,300 households. Each point holds six or seven containers and handles ten waste fractions in total. To make collection more efficient, glass and metal are collected as a single fraction.</p>
        <p>Alongside the sensors, the utility took the transport and logistics software that retrieves data from every container via the cloud, generates collection routes automatically, and gives drivers the service route and current fill levels through an app.</p>
        <p>Fill levels update automatically <strong>every six hours</strong>. A container is normally added to the service route at 80&ndash;90% full. Every Wednesday, an additional check is run for containers that might become critical over the weekend in holiday-home areas &mdash; a small local rule that prevents the failure mode most likely to generate complaints.</p>

        <h2>The results</h2>
        <ul>
          <li>The 176&nbsp;km manual inspection round was <strong>eliminated</strong>.</li>
          <li>Combined with a move to consolidated collection points, the utility reduced its fleet by <strong>one waste collection truck</strong>.</li>
          <li>Overflowing containers in the holiday-home areas <strong>ceased to be a problem</strong>.</li>
          <li>Reliability: <strong>one defective sensor out of 220</strong> in the first four months, and <strong>no battery replacements</strong> across the year.</li>
        </ul>
        <p>The operations manager's stated goal, delivered with some satisfaction, is no letters to the editor of the local newspaper about missed collections. It still holds.</p>

        <div class="pullquote">
          <blockquote>It is easy to use and provides an overview, so we are able to delegate the planning of the service route to our driver &mdash; he is now fully in charge of the process.</blockquote>
          <cite><b>Operations manager</b> &mdash; Langelands Forsyning</cite>
        </div>

        <h2>Connectivity on difficult terrain</h2>
        <p>Langeland is a beautiful island of rolling landscapes, and that initially caused problems transferring data from sensors distributed across it. NB-IoT was the technology that resolved it, providing consistent data transfer about container fill levels. For any UK authority servicing rural bring sites, upland car parks or coastal locations, this is the relevant precedent: NB-IoT reaches places ordinary connectivity does not, because it was designed to.</p>

        <h2>Expanding is a ten-minute job</h2>
        <p>The utility runs a subscription covering both the sensors and the software. When a sensor needs installing or replacing, the operations manager frequently does it himself while already out on the road &mdash; ten minutes to install a new fill-level sensor and set it up in the software.</p>
        <p>That figure matters more than it appears. A deployment where adding a container requires a supplier visit does not grow; one where a supervisor can do it from the cab does. Langeland went from ten sensors to 220 on that basis.</p>

        <h2>What they were planning next</h2>
        <p>Two things, both worth noting because they mark the maturity curve of a deployment. Moving to the next generation of radar fill-level sensors for greater precision on cardboard, paper and plastic &mdash; the materials that defeat older measurement technology. And beginning to use emptying forecasts rather than reacting to current fill levels alone.</p>
        <p>The operations manager recommends other waste handling companies install fill-level sensors, on the grounds that it creates obvious opportunities to optimise operations and that the more rational effort also makes good sense for the employees.</p>
      </div>

      <div>
        <div class="keyfacts">
          <h2>Deployment at a glance</h2>
          <dl>
            <dt>Operator</dt><dd>Langelands Forsyning A/S, Langeland, Denmark</dd>
            <dt>In service since</dt><dd>2019</dd>
            <dt>Sensors</dt><dd>220, starting from about 10</dd>
            <dt>Collection points</dt><dd>Approximately 30, with 6&ndash;7 containers each</dd>
            <dt>Households covered</dt><dd>All holiday homes &mdash; 2,300 households</dd>
            <dt>Waste fractions</dt><dd>10, with glass and metal combined for efficiency</dd>
            <dt>Reporting</dt><dd>Fill levels updated every 6 hours</dd>
            <dt>Threshold</dt><dd>Normally added to the route at 80&ndash;90% full</dd>
            <dt>Local rule</dt><dd>Extra Wednesday check for containers likely to become critical over the weekend</dd>
            <dt>Replaced</dt><dd>A 176&nbsp;km manual inspection round of 50 stations taking 1.5 days</dd>
            <dt>Fleet</dt><dd>One collection truck removed from service</dd>
            <dt>Vehicles</dt><dd>1 service truck with trailer handling 4 fractions at a time, plus 3 daily collection trucks</dd>
            <dt>Reliability</dt><dd>1 fault in 220 units over four months; no battery replacements in a year</dd>
            <dt>Install time</dt><dd>10 minutes per sensor, done in-house</dd>
            <dt>Connectivity</dt><dd>NB-IoT, adopted to overcome terrain-related data transfer problems</dd>
            <dt>Commercial model</dt><dd>Subscription covering sensors and software</dd>
          </dl>
        </div>
        <p><a class="arrow-link" href="/sectors/tourism-coastal-parks/">How this applies to rural and coastal UK operations</a></p>
      </div>
    </div>
    """ + DISCLOSURE + """
  </div>
</section>
"""

LANGELAND_FAQS = [
    ("How does eliminating an inspection round compare with reducing collections?",
     "<p>In a dispersed rural operation it is frequently the larger saving, and it is often overlooked. Langeland was spending a day and a half and 176&nbsp;km every cycle simply to find out what was in the containers &mdash; before any waste was collected at all. That entire activity disappeared. If your operation currently sends anyone to look at bring sites, that cost should be in the business case alongside the avoided lifts, because it goes to zero rather than merely reducing.</p>"),
    ("They removed a whole vehicle. Was that the sensors alone?",
     "<p>No, and the case study is clear about it: the reduction came from the sensors combined with a transition to consolidated collection points. That combination is common &mdash; better data makes rationalisation possible, and rationalisation is what releases a vehicle. It is worth planning for both together rather than treating sensors as a standalone measure.</p>"),
    ("One fault in 220 sensors &mdash; is that typical?",
     "<p>It is a strong result and it reflects the hardware: a sealed, shock-resistant enclosure with no moving parts and no external connections, in an application with very little to go wrong. The utility also reported no battery replacements across a full year. Sensor health is monitored centrally regardless, so units that stop reporting or run low are flagged before they cause a missed collection rather than discovered afterwards.</p>"),
    ("What is the Wednesday check about?",
     "<p>A local rule to catch containers likely to become critical over the weekend in holiday-home areas, when nobody is collecting and visitor numbers are highest. It is a good illustration of how these systems are actually configured in practice: the underlying automation is general, and the value comes from the operational knowledge layered on top of it. Rules of that kind are configuration, not custom development.</p>"),
]


def pages():
    return [
        Page(
            path="results/",
            nav_key="results",
            title="Smart Waste Sensor Results | 71% Fewer Collections",
            description="Measured outcomes from four published municipal deployments: 71% fewer collections in Stralsund, 20% fewer emptyings in Fanø, fortnightly in Vejle.",
            keywords="smart bin case study, waste sensor results, fill level sensor ROI, smart waste savings",
            h1="Measured results",
            eyebrow="Evidence",
            lede="Four public bodies, four different waste problems, and published numbers behind each one.",
            body=INDEX_BODY,
            faqs=INDEX_FAQS,
            faq_heading="About this evidence",
            page_type="CollectionPage",
        ),
        Page(
            path="results/stralsund-smart-street-bins/",
            nav_key="results",
            breadcrumbs=CRUMB,
            title="Stralsund: 71% Fewer Street Bin Collections | Case Study",
            description="How Stralsund cut weekly public bin collections from 1,548 to 445 and weekly mileage from 1,677km to 779km using radar sensors on 35 town bins.",
            keywords="Stralsund smart bins, street bin sensors case study, reduce bin collections, smart city waste Germany",
            h1="Stralsund: 71% fewer street bin collections",
            eyebrow="Case study &middot; Germany",
            lede="A Baltic city of 55,000 instrumented 35 town-centre bins. Collections fell by 71%, mileage by 54%, and the pilot paid for itself in under a year.",
            body=STRALSUND_BODY,
            faqs=STRALSUND_FAQS,
            faq_heading="Reading the Stralsund numbers",
            schema=[article_schema(
                "/results/stralsund-smart-street-bins/",
                "Stralsund: 71% fewer street bin collections with radar fill-level sensors",
                "The City of Stralsund fitted radar fill-level sensors to 35 town-centre public bins, reducing weekly collections from 1,548 to 445 and weekly distance from 1,677km to 779km.",
                "Stralsund smart bins, street bin fill level sensors, waste collection reduction, smart city waste management",
                [{"@type": "Thing", "name": "Smart waste management"},
                 {"@type": "Place", "name": "Stralsund, Germany"}],
            )],
        ),
        Page(
            path="results/vejle-dynamic-round-planning/",
            nav_key="results",
            breadcrumbs=CRUMB,
            title="Vejle: 547 Bins on Automatic Daily Rounds | Case Study",
            description="How Vejle instrumented 547 of 875 public bins across 2,000km of roads, moved to fortnightly collection, and cut crewing from 2.0 to 1.5 full-time.",
            keywords="Vejle smart bins, municipal waste route optimisation, dynamic round planning case study, radar vs ultrasonic bin sensors",
            h1="Vejle: rounds that rebuild themselves at 05:00",
            eyebrow="Case study &middot; Denmark",
            lede="A municipality-wide rollout across 2,000km of roads &mdash; and the clearest published account of why radar measurement matters.",
            body=VEJLE_BODY,
            faqs=VEJLE_FAQS,
            faq_heading="Reading the Vejle deployment",
            schema=[article_schema(
                "/results/vejle-dynamic-round-planning/",
                "Vejle Municipality: dynamic waste collection round planning across 547 instrumented bins",
                "Vejle Municipality fitted radar fill-level sensors to 547 of 875 public bins, generating an optimised collection round automatically each morning and moving average collection intervals from twice weekly to fortnightly.",
                "Vejle waste management, dynamic route planning, radar fill level sensors, municipal waste digitisation",
                [{"@type": "Thing", "name": "Waste collection route optimisation"},
                 {"@type": "Place", "name": "Vejle, Denmark"}],
            )],
        ),
        Page(
            path="results/fano-seasonal-recycling-sites/",
            nav_key="results",
            breadcrumbs=CRUMB,
            title="Fanø: 20% Fewer Emptyings on Island Sites | Case Study",
            description="How Fanø, whose population swings from 3,000 to 50,000, cut emptyings 20% in two months with sensors on 82 semi-buried containers at 14 sites.",
            keywords="Fano smart waste, seasonal waste collection, semi-buried container sensors, island recycling sites",
            h1="Fan&oslash;: emptying by data instead of gut feeling",
            eyebrow="Case study &middot; Denmark",
            lede="An island whose population multiplies sixteenfold in summer, 82 semi-buried containers, and a 20% reduction in emptyings within two months.",
            body=FANO_BODY,
            faqs=FANO_FAQS,
            faq_heading="Reading the Fan&oslash; deployment",
            schema=[article_schema(
                "/results/fano-seasonal-recycling-sites/",
                "Fanø Municipality: 20% fewer emptyings on seasonal island recycling sites",
                "Fanø Municipality installed fill-level sensors on all 82 of its semi-buried waste containers, reducing emptyings by 20% within two months against a 25% target despite a 16-fold seasonal population swing.",
                "seasonal waste collection, semi-buried container monitoring, island waste management, recycling site sensors",
                [{"@type": "Thing", "name": "Seasonal waste collection"},
                 {"@type": "Place", "name": "Fanø, Denmark"}],
            )],
        ),
        Page(
            path="results/langeland-island-recycling-network/",
            nav_key="results",
            breadcrumbs=CRUMB,
            title="Langeland: 220 Sensors, One Less Vehicle | Case Study",
            description="How an island utility scrapped a 176km manual inspection round, removed a collection vehicle from service, and saw one sensor fault in 220 units.",
            keywords="Langeland waste sensors, rural bring site monitoring, recycling station fill level, NB-IoT rural waste",
            h1="Langeland: 220 sensors, one vehicle less",
            eyebrow="Case study &middot; Denmark",
            lede="A 176km manual inspection round that took a day and a half, replaced by readings every six hours.",
            body=LANGELAND_BODY,
            faqs=LANGELAND_FAQS,
            faq_heading="Reading the Langeland deployment",
            schema=[article_schema(
                "/results/langeland-island-recycling-network/",
                "Langeland: 220 fill-level sensors replace a 176km manual inspection round",
                "Langelands Forsyning installed 220 fill-level sensors across around 30 island collection points, eliminating a 176km manual inspection round, removing one collection vehicle from service and recording one sensor fault in 220 units.",
                "rural waste collection, bring site monitoring, NB-IoT waste sensors, island utility waste management",
                [{"@type": "Thing", "name": "Rural waste collection optimisation"},
                 {"@type": "Place", "name": "Langeland, Denmark"}],
            )],
        ),
    ]
