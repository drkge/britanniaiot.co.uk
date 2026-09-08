"""Sector discovery pages: councils, contractors, estates, tourism/parks."""

from build import Page, SITE
from content_core import ICON, icon_card

CRUMB = [("Sectors", "/sectors/")]


def audience_service(url, name, desc, audience):
    return {
        "@type": "Service",
        "@id": SITE["url"] + url + "#service",
        "name": name,
        "description": desc,
        "provider": {"@id": SITE["url"] + "/#organization"},
        "areaServed": {"@type": "Country", "name": "United Kingdom"},
        "serviceType": "Sensor-led waste collection",
        "audience": {"@type": "Audience", "audienceType": audience},
    }


# ------------------------------------------------------------- overview ----

OVERVIEW_BODY = f"""
<section class="section">
  <div class="wrap">
    <div class="answer-box">
      <p><strong>Britannia IoT Solutions works with four kinds of UK organisation: local authorities, waste management contractors, universities and NHS and large estates, and tourism, coastal and parks authorities. The technology is the same in each case; the business case, the buying process and the person who cares are completely different.</strong></p>
    </div>
    <div class="grid grid-2 mt-3">
      <a class="card" href="/sectors/local-authorities/"><span class="card-icon">{ICON["clipboard"]}</span><h3>District &amp; unitary councils</h3><p>Street bins, bring sites, HWRCs and communal housing containers, on rounds set years ago. The pressure is a service budget that has to fall while resident expectations do not &mdash; plus an evidence gap every time a complaint reaches a councillor.</p><span class="arrow-link">Sensor-led collection for councils</span></a>
      <a class="card" href="/sectors/waste-contractors/"><span class="card-icon">{ICON["truck"]}</span><h3>Waste management contractors</h3><p>On a fixed-price contract, every avoided lift is margin. On a per-lift contract, fill data is how you prove the frequency is wrong. Either way it is evidence nobody else brings to the next tender.</p><span class="arrow-link">Sensor-led collection for contractors</span></a>
      <a class="card" href="/sectors/universities-nhs-estates/"><span class="card-icon">{ICON["people"]}</span><h3>Universities, NHS &amp; large estates</h3><p>Dense bin estates inside one boundary, one decision-maker, and demand that swings wildly with terms, shifts and clinic timetables. Often the fastest deployments we can do, because there is no procurement framework in the way.</p><span class="arrow-link">Sensor-led collection for estates</span></a>
      <a class="card" href="/sectors/tourism-coastal-parks/"><span class="card-icon">{ICON["leaf"]}</span><h3>Tourism, coastal &amp; parks authorities</h3><p>Where the population multiplies in July, the seafront bin overflows by Saturday lunchtime, and the photograph is on social media by Sunday. Seasonality is the condition sensors were built for.</p><span class="arrow-link">Sensor-led collection for visitor destinations</span></a>
    </div>
  </div>
</section>

<section class="section section-alt section-line">
  <div class="wrap">
    <p class="eyebrow">Also relevant</p>
    <h2 class="measure">Other operations we can instrument</h2>
    <p class="lede">The requirement is simply that something has to travel to a container to empty it, and that at least some of those journeys are currently wasted.</p>
    <div class="grid grid-3 mt-3">
      <div class="card no-push"><h3>Housing associations &amp; managing agents</h3><p>Communal bin stores and chute-fed containers where overflow becomes a health and safety issue, a fire risk and a resident satisfaction score all at once.</p></div>
      <div class="card no-push"><h3>Retail parks, shopping centres &amp; leisure</h3><p>Trade waste under a service charge that tenants scrutinise line by line, with demand driven by footfall nobody is currently measuring at the bin.</p></div>
      <div class="card no-push"><h3>Ports, airports &amp; transport operators</h3><p>Dispersed bins across large secure sites where access is time-consuming and a wasted trip costs more than it does on a high street.</p></div>
      <div class="card no-push"><h3>Business improvement districts</h3><p>A defined area, a levy to justify, and an immediate need to show members what the money bought &mdash; which is exactly what lift and mileage data does.</p></div>
      <div class="card no-push"><h3>Event venues &amp; festivals</h3><p>Extreme, short-lived demand where the whole problem is knowing which bins have gone in the last hour, not last week.</p></div>
      <div class="card no-push"><h3>Waste transfer &amp; recycling operators</h3><p>Inbound container monitoring at satellite sites, so a vehicle is dispatched to a full container rather than on a schedule.</p></div>
    </div>
  </div>
</section>
"""


# ----------------------------------------------------------- authorities ---

COUNCILS_BODY = """
<section class="section">
  <div class="wrap">
    <div class="answer-box">
      <p><strong>For a UK council, sensor-led collection does three things at once: it removes the lifts that go to bins nobody filled, it stops the specific bins that generate complaints from overflowing, and it produces a timestamped service record you can put in front of a resident, a councillor or an FOI request.</strong></p>
      <p class="mt-1">The first pays for the system. The second and third are usually why it survives the next budget round.</p>
    </div>

    <h2>Where the money actually is</h2>
    <p>Street and park bins are the most over-serviced part of most authorities' waste operation, because the frequency was set to protect against the worst case and never revisited. Stralsund &mdash; a town of 55,000 collecting 180 tonnes a year from public bins &mdash; was emptying its town-centre bins twice a week. After instrumenting 35 of them, weekly collections fell from <strong>1,548 to 445</strong>, a 71% reduction, and weekly mileage from 1,677&nbsp;km to 779&nbsp;km. Working hours on the task fell 30%, and staff moved to other work that had been waiting.</p>
    <p>Vejle Municipality, running 875 public bins along 2,000&nbsp;km of roads, went from emptying bins once or twice a week to <strong>an average of once a fortnight</strong> after fitting sensors to 547 of them. Crewing on the task fell from two full-time staff to one and a half, and the department expects the evaluation to confirm 30% less travel, a 40% economic gain and 5.5 tonnes less CO&#8322; a year.</p>
    <p>Neither authority reduced the service residents receive. Both stopped paying for journeys that produced nothing.</p>
  </div>
</section>

<section class="section section-alt section-line">
  <div class="wrap">
    <p class="eyebrow">Beyond the saving</p>
    <h2 class="measure">The three arguments that carry a committee</h2>
    <div class="grid grid-3 mt-3">
      <div class="card no-push">
        <span class="card-num">01</span>
        <h3>Evidence against complaints</h3>
        <p>Every reading and every lift is timestamped. When a resident reports a bin unemptied for a fortnight, you check and answer the same day. Fan&oslash; Municipality specifically cites being able to document whether containers were emptied &mdash; and Vejle's department head values being able to give elected members a straight answer when constituents ask.</p>
      </div>
      <div class="card no-push">
        <span class="card-num">02</span>
        <h3>A carbon number you can defend</h3>
        <p>Most council climate reporting on fleet is modelled. This is counted: journeys not made, kilometres not driven, fuel not burned. It contributes to a declared climate emergency commitment without asking residents to change anything, which is a rare combination.</p>
      </div>
      <div class="card no-push">
        <span class="card-num">03</span>
        <h3>Fewer bins, permanently</h3>
        <p>Bin estates grow by accretion &mdash; a complaint arrives, a bin is added, nobody reviews it. Fill history shows which containers overlap and which are barely used. Vejle began removing redundant bins on that evidence, taking a lift and a maintenance liability out of the estate for good.</p>
      </div>
    </div>
    <div class="pullquote mt-3">
      <blockquote>There is the little extra plus that we can quickly respond to our elected politicians when they get questions from concerned citizens about the waste bins. The politicians like that we do not make unnecessary trips, because it shows that we also consider the climate.</blockquote>
      <cite><b>Head of Roads &amp; Parks</b> &mdash; Vejle Municipality, Denmark</cite>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split split-top">
      <div>
        <p class="eyebrow">Procurement</p>
        <h2>Getting it bought</h2>
        <p>The procurement route is usually the slowest part, and there is a well-worn path through it.</p>
        <p>Most authorities start with a pilot small enough to sit under their delegated spend threshold. That gets sensors on real bins and real numbers in hand within a couple of months, without a tender. The pilot report &mdash; measured against a baseline recorded before anything changed &mdash; is then the evidence supporting the business case for a wider award, whether that goes out as a direct award, a framework call-off or a full tender.</p>
        <p>Vejle followed precisely this sequence: funds allocated for a pilot on a single trial route, a demonstrated optimisation potential and positive business case, then a council decision to roll out across the municipality.</p>
        <p>We are happy to provide the technical detail your procurement team needs to write an evaluable specification. The single most valuable line to include is <strong>radar</strong> rather than simply &ldquo;fill-level sensors&rdquo; &mdash; it is the difference between a pilot that convinces and one that produces arguments about false readings.</p>
      </div>
      <div>
        <div class="keyfacts" style="margin-bottom:0">
          <h3>Typical council deployment</h3>
          <dl>
            <dt>Start with</dt><dd>One round or one geographic cluster, 30&ndash;60 containers</dd>
            <dt>Pilot length</dt><dd>90 days, including 2&ndash;4 weeks observing before changing any collections</dd>
            <dt>Live in</dt><dd>4&ndash;6 weeks from go-ahead</dd>
            <dt>Threshold</dt><dd>Usually 80&ndash;90%, tuned in the first two months</dd>
            <dt>Who owns it</dt><dd>One named officer coordinating waste, highways, fleet and IT</dd>
            <dt>Prerequisite</dt><dd>An accurate container register &mdash; type, capacity and GPS position</dd>
            <dt>Deliverable</dt><dd>Measured before-and-after against your own baseline, and a costed rollout plan</dd>
          </dl>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section section-dark">
  <div class="wrap">
    <p class="eyebrow">The awkward question</p>
    <div class="split split-top">
      <div>
        <h2>What happens to the crews?</h2>
        <p>Ask it early, because your drivers will. A system that visibly reduces the number of lifts looks, from the cab, like a system that reduces the number of jobs &mdash; and a crew that believes that will find reasons the round plan is wrong.</p>
        <p>The deployments worth citing redeployed rather than cut. Stralsund reduced working hours on the task by 30% and moved staff to other urgent work. Vejle went from 2.0 to 1.5 full-time staff on bin emptying and used the freed capacity to start collecting waste along roads and at bridges &mdash; work that had never previously reached the top of the list. Most UK authorities have a comparable backlog of grounds, fly-tipping and street cleansing work that has been quietly deprioritised for a decade.</p>
      </div>
      <div>
        <ul class="feature-list">
          <li><strong>Decide the answer before the pilot starts</strong>, and say it plainly to the crews at the briefing.</li>
          <li><strong>Show drivers the fill data.</strong> The app tells them why each bin is on the round, which turns a directive into something they can check.</li>
          <li><strong>Let them plan the sequence.</strong> On several deployments drivers order their own stops from the flagged list and prefer it that way.</li>
          <li><strong>Expect contractor drivers to worry too</strong> &mdash; fewer lifts can look like less invoicing, when in practice it is less unpaid time spent checking half-empty containers.</li>
        </ul>
      </div>
    </div>
  </div>
</section>
"""

COUNCILS_FAQS = [
    ("We are under severe budget pressure. Is this affordable?",
     "<p>It is sold as an annual per-container subscription rather than a capital purchase, which usually makes it a revenue rather than a capital decision. On whether it pays back: Stralsund reported that its 35-bin pilot paid for itself in under a year purely through avoided collections and mileage, and extended the deployment by a further 100 sensors on that basis. The honest caveat is that the return depends on how over-serviced your current rounds are, which is unknown until measured &mdash; and the pilot exists to establish it at small cost.</p>"),
    ("Which bins should we start with?",
     "<p>Street and park bins on fixed frequencies, and rural or edge-of-town bring sites. Those are where the ratio of wasted journeys to useful ones is highest. Town-centre bins that genuinely fill daily have less slack to recover; a bin at the far end of a 20-minute drive that fills every three weeks has a great deal. A good pilot round mixes both so the report reflects your real estate rather than the best case.</p>"),
    ("Can we use this on kerbside household collections?",
     "<p>Not usefully. Kerbside rounds pass every property regardless, so there is no journey to avoid. Sensor-led collection applies to containers a vehicle travels specifically to reach: street and park bins, bring sites, communal housing containers, HWRC containers and trade waste. That is where the wasted mileage sits.</p>"),
    ("How does this fit a declared climate emergency commitment?",
     "<p>It reduces fleet emissions without reducing service or asking residents to change behaviour, which makes it unusually easy to defend politically. The numbers are counted rather than modelled: Stralsund's weekly mileage fell from 1,677&nbsp;km to 779&nbsp;km, and Vejle targets a 5.5 tonne annual CO&#8322; reduction alongside 30% less travel. Vejle's department head notes that members like being able to show that unnecessary journeys are not being made.</p>"),
    ("Our container records are incomplete. Is that a blocker?",
     "<p>It is the most common starting position and it is fixable, but it has to be fixed rather than worked around. Every successful deployment rests on an accurate register of container type, capacity and GPS position, maintained by one named person &mdash; Vejle's team are explicit that this discipline is the precondition for everything else. We offer a fixed-price survey where the data is patchy. It is far cheaper done deliberately at the start than discovered halfway through a rollout.</p>"),
    ("What if the service is delivered by an arm's-length company or a contractor?",
     "<p>It works either way. Contractors receive rounds directly in the driver app and confirm each lift, which also generates clean invoicing data &mdash; Fan&oslash; Municipality connected its contractor for exactly that reason. The authority keeps the dashboard, the history and the evidence, which matters at contract review whoever holds the vehicles.</p>"),
]


# ----------------------------------------------------------- contractors ---

CONTRACTORS_BODY = """
<section class="section">
  <div class="wrap">
    <div class="answer-box">
      <p><strong>For a waste management contractor, fill-level data changes the economics of a contract in one of two directions. On fixed-price work, every lift you avoid without breaching the specification is margin recovered. On per-lift work, the same data is how you demonstrate to a client that the contracted frequency does not match reality &mdash; in either direction.</strong></p>
      <p class="mt-1">And in a tender, it is evidence about the client's own estate that nobody else in the room has.</p>
    </div>

    <h2>Margin on fixed-price contracts</h2>
    <p>If you are paid a fixed sum to service an estate of containers to a specified standard, every journey to a container that did not need emptying is cost with no revenue attached. Most contractors know this in principle and have no way to quantify it, because the only way to find out whether a bin needed emptying was to drive there and look.</p>
    <p>Stralsund's numbers show the scale of what is hiding in a typical street-bin round: weekly collections fell from 1,548 to 445 and weekly mileage from 1,677&nbsp;km to 779&nbsp;km once the bins could report their own fill level. Working hours on the task fell 30%. In a commercial operation those are not abstractions &mdash; they are vehicle hours, fuel, driver time and wear released back into the business or redeployed onto other customers.</p>
  </div>
</section>

<section class="section section-alt section-line">
  <div class="wrap">
    <p class="eyebrow">Commercial cases</p>
    <h2 class="measure">Four ways contractors use it</h2>
    <div class="grid grid-2 mt-3">
      <div class="card no-push">
        <h3>Recover margin on fixed-price work</h3>
        <p>Stop servicing containers that do not need it, within the terms of the specification, and redeploy the released capacity. This is the most direct case and the easiest to model &mdash; you already know your cost per lift and per kilometre.</p>
      </div>
      <div class="card no-push">
        <h3>Evidence a frequency change</h3>
        <p>On per-lift contracts, fill history is the only credible basis for renegotiating frequency &mdash; in either direction. It also protects you: where a client believes a frequency is too high, data showing containers genuinely at 90% is a stronger defence than assertion.</p>
      </div>
      <div class="card no-push">
        <h3>Prove SLA performance</h3>
        <p>Timestamped lift confirmations and threshold-breach records turn service level reporting from a spreadsheet you compile into a query you run. When a client raises a missed collection, you have the record rather than the argument.</p>
      </div>
      <div class="card no-push">
        <h3>Differentiate in a tender</h3>
        <p>Most bids compete on price against an identical specification. A bid that proposes instrumenting the estate, commits to a measured mileage and carbon reduction, and offers the authority a live evidence dashboard is competing on something else &mdash; and social value and carbon reduction are scored criteria in UK public procurement.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split split-top">
      <div>
        <p class="eyebrow">Operational fit</p>
        <h2>It sits inside your operation, not beside it</h2>
        <p>The practical concern for a contractor is usually integration: another portal, another login, another thing for drivers to ignore. Two routes avoid that.</p>
        <p>Either your crews work in the driver app directly &mdash; the round, live fill percentages, navigation, one-tap lift confirmation, on-the-spot fault reporting &mdash; which also produces clean lift records for invoicing. Fan&oslash; Municipality connected its contractor this way specifically so that emptying orders and invoicing data flowed through a single system, reducing the contractor's administrative burden as well as the authority's.</p>
        <p>Or fill-level data feeds your existing in-cab or route management platform through the API, so drivers keep the interface they know and the sensor layer sits underneath.</p>
      </div>
      <div>
        <ul class="feature-list">
          <li><strong>Multi-client, multi-site.</strong> Separate estates, separate thresholds, separate reporting.</li>
          <li><strong>Multi-fraction rounds.</strong> Vehicles collecting several streams in one pass are planned as such, not as several rounds.</li>
          <li><strong>Clean invoicing data.</strong> Confirmed lifts, timestamped, per container &mdash; the same record the client sees.</li>
          <li><strong>Client-facing transparency, on your terms.</strong> Giving a client a live view is a strong retention play when you are confident in the service.</li>
          <li><strong>Portable across contracts.</strong> Sensors move with the containers or come back with you, depending on how the contract is written.</li>
        </ul>
      </div>
    </div>
    <div class="pullquote mt-3">
      <blockquote>The lorry driver might be a little worried because he fears having to empty fewer containers, but he shouldn't be. He just avoids spending time checking containers that turn out to be only half full, and for which it makes no sense to empty and invoice. That time he could spend for another customer.</blockquote>
      <cite><b>Senior engineer, technical administration</b> &mdash; Fan&oslash; Municipality, Denmark</cite>
    </div>
  </div>
</section>
"""

CONTRACTORS_FAQS = [
    ("If we empty fewer containers, do we not earn less?",
     "<p>It depends on the contract, and being clear about that is the first thing to work out. On fixed-price work the arithmetic is straightforwardly in your favour: fewer lifts for the same fee is recovered margin. On per-lift work the immediate effect can be a reduction in billed lifts, offset by the time your crews stop spending driving to and checking containers that did not need servicing &mdash; time that is unbilled either way and can be sold to another customer. It also puts you in the strongest possible position at renewal, because you can evidence what the estate actually needs.</p>"),
    ("Can we deploy this on a client's containers?",
     "<p>Yes, subject to the client's agreement, and it is worth raising with them explicitly because most authorities will welcome it. Sensors are non-invasive &mdash; fitted inside the lid with no wiring or modification &mdash; and remove cleanly. How ownership and removal are handled at contract end is something we set out in the agreement up front, because it needs to be settled before the sensors go on rather than during a mobilisation dispute.</p>"),
    ("Does it integrate with our existing in-cab system?",
     "<p>Yes, through the API. Fill-level readings, container registers and lift records can be delivered to your route management or in-cab platform so drivers keep the interface they already use. Alternatively crews work in our driver app directly, which is often simpler for a specific contract or a mixed fleet. We work out which route makes sense during discovery.</p>"),
    ("Is this useful in a bid?",
     "<p>Materially, yes. UK public waste tenders are usually scored on price against a common specification, with social value and carbon reduction as differentiating criteria. A bid that commits to instrumenting the estate, offers a measured mileage and CO&#8322; reduction, and gives the authority a live evidence dashboard is answering those criteria with numbers rather than intent. We can supply the technical annexes and the reference figures from published deployments to support a submission.</p>"),
    ("What about commercial and trade waste customers?",
     "<p>Same technology, simpler commercial logic. For trade waste customers on a scheduled service, fill data lets you right-size both the container and the frequency &mdash; which either reduces your cost or lets you sell a service level that genuinely matches what the customer needs. It is also a straightforward upsell: customers with visibility of their own waste production tend to stay.</p>"),
]


# --------------------------------------------------------------- estates ---

ESTATES_BODY = """
<section class="section">
  <div class="wrap">
    <div class="answer-box">
      <p><strong>Universities, NHS trusts and large estates are often the fastest sensor deployments available, because everything that slows a council down is absent: one landowner, one budget holder, one boundary, no framework procurement, and internal or single-contract collection.</strong></p>
      <p class="mt-1">They also have unusually uneven demand &mdash; term dates, shift changes, clinic timetables, exam periods, vacation shutdowns &mdash; which is exactly the pattern a fixed collection timetable serves badly.</p>
    </div>

    <h2>Why estates get more from it than they expect</h2>
    <p>A campus or hospital site typically has a few hundred containers inside a walkable boundary, serviced by an internal team or a single contractor on a frequency set when the site was smaller. Demand across those containers is wildly uneven: the bins outside the students' union and the main entrance are emptied daily and still overflow, while those behind the estates workshop and in the far car park are emptied on the same round and are rarely half full.</p>
    <p>Because the whole estate sits inside one boundary, the drive time per stop is small &mdash; which means the saving is less about mileage and more about labour hours, complaints, and the appearance of the site. For a university competing on open days, or a hospital being inspected, an overflowing bin outside the main entrance is a disproportionate problem, and it is precisely the bin a fixed timetable underserves.</p>
  </div>
</section>

<section class="section section-alt section-line">
  <div class="wrap">
    <p class="eyebrow">By setting</p>
    <h2 class="measure">What it looks like on different estates</h2>
    <div class="grid grid-3 mt-3">
      <div class="card no-push">
        <h3>Universities &amp; colleges</h3>
        <p>Demand that collapses in vacation and spikes at freshers, exams and graduation, plus a sustainability commitment students actively scrutinise. Fill data by waste stream also evidences recycling performance for reporting obligations and league table submissions.</p>
      </div>
      <div class="card no-push">
        <h3>NHS trusts &amp; hospital sites</h3>
        <p>Large dispersed sites with tight access windows, high-visibility public entrances, and a strong incentive to keep external areas presentable. Domestic and recycling waste is the practical starting point; clinical streams stay on their own compliance-driven regime.</p>
      </div>
      <div class="card no-push">
        <h3>Business &amp; science parks</h3>
        <p>Shared trade waste recharged through a service charge that tenants examine closely. Fill data lets you right-size containers and frequency, and evidence the charge rather than defend it.</p>
      </div>
      <div class="card no-push">
        <h3>Schools &amp; multi-academy trusts</h3>
        <p>Predictable term-time and holiday patterns that fixed contracts rarely reflect. Trusts running collections across several sites can consolidate rounds instead of scheduling each site separately.</p>
      </div>
      <div class="card no-push">
        <h3>Shopping centres &amp; leisure</h3>
        <p>Footfall-driven demand nobody currently measures at the bin. Sensor data links waste production to trading patterns, which changes how the contract is specified at renewal.</p>
      </div>
      <div class="card no-push">
        <h3>Housing &amp; managed residential</h3>
        <p>Communal bin stores and chute-fed containers where overflow is simultaneously a fire risk, a health and safety issue and a resident satisfaction score. Early warning is worth more than the collection saving.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split split-top">
      <div>
        <p class="eyebrow">Why it moves quickly</p>
        <h2>No framework, no committee cycle</h2>
        <p>The practical advantage of an estate is that the person who owns the problem usually also owns the budget. A head of estates or facilities can commission a pilot on delegated authority, see results inside a term, and expand without a council decision or an OJEU-scale process.</p>
        <p>The container register also tends to be better than a council's, because the estate is bounded, mapped and already managed by a CAFM system. That removes the single most common cause of delay.</p>
      </div>
      <div>
        <div class="keyfacts" style="margin-bottom:0">
          <h3>Typical estate deployment</h3>
          <dl>
            <dt>Scale</dt><dd>50&ndash;500 containers within one boundary</dd>
            <dt>Live in</dt><dd>3&ndash;5 weeks from go-ahead &mdash; usually faster than a council, because the register already exists</dd>
            <dt>Best first target</dt><dd>External bins on fixed daily or twice-weekly rounds, plus communal and trade containers</dd>
            <dt>Primary gain</dt><dd>Labour hours and site appearance, more than vehicle mileage</dd>
            <dt>Secondary gain</dt><dd>Waste-stream data for sustainability and recycling reporting</dd>
            <dt>Decision-maker</dt><dd>Head of estates, facilities or sustainability &mdash; usually on delegated authority</dd>
            <dt>Integration</dt><dd>API feed into an existing CAFM or helpdesk system where wanted</dd>
          </dl>
        </div>
      </div>
    </div>
  </div>
</section>
"""

ESTATES_FAQS = [
    ("Does this work for clinical or hazardous waste?",
     "<p>Fill-level monitoring applies to domestic, recycling and general trade waste containers. Clinical, cytotoxic and hazardous streams are governed by their own compliance regimes with mandated collection intervals that are not determined by how full the container is, so sensors do not change how they are collected &mdash; though fill data can still inform container sizing and identify where a stream is being over-provisioned.</p>"),
    ("Our collections are done in-house by the grounds team. Does that matter?",
     "<p>It usually makes things simpler. An in-house team means no contract renegotiation, no third-party integration and a shorter route from decision to deployment. The team uses the driver app on a phone or tablet, and because the estate is compact they often plan their own sequence from the flagged list rather than following a generated order.</p>"),
    ("Can we monitor recycling rates as well as fill levels?",
     "<p>Fill-level data gives you volume by stream and by location over time, which is the basis for a genuine recycling analysis: which buildings produce what, where contamination-driven residual volume is rising, and whether a new bin configuration actually changed behaviour. It measures volume rather than weight, so it complements weighbridge data rather than replacing it &mdash; but for identifying which parts of a campus are performing and which are not, it is considerably more granular than anything a weighbridge produces.</p>"),
    ("How do we handle vacation periods and shutdowns?",
     "<p>This is where sensors earn their place on a campus. Instead of maintaining a term-time frequency through a vacation, or manually rewriting the schedule twice a year, the round simply reflects what the containers report &mdash; which during a shutdown is very little. The same mechanism handles the reverse: freshers week, graduation and exam periods generate the round they need without anyone having to anticipate it.</p>"),
    ("Can it integrate with our CAFM or helpdesk system?",
     "<p>Yes. Fill readings, container records and lift confirmations are available through the API, so they can feed a CAFM platform, a helpdesk, or a sustainability dashboard. A common pattern is raising a task automatically in the existing helpdesk when a container passes threshold, so the estates team keeps one workflow rather than adding a second.</p>"),
]


# --------------------------------------------------------------- tourism ---

TOURISM_BODY = """
<section class="section">
  <div class="wrap">
    <div class="answer-box">
      <p><strong>Seasonal and visitor destinations get more from fill-level sensors than anyone else, because a fixed collection timetable is at its worst when demand swings by an order of magnitude. A frequency set for February is negligent in August; a frequency set for August is expensive for the other ten months.</strong></p>
      <p class="mt-1">Sensors remove the choice. The round follows the visitors.</p>
    </div>

    <h2>The Fan&oslash; problem, which is also the Cornwall problem</h2>
    <p>Fan&oslash; is a Danish island whose population moves between <strong>3,000 and 50,000</strong> across the year. It operates 82 semi-buried containers of up to three cubic metres across 14 recycling sites, most of them near roughly 2,900 holiday cottages. In areas with permanent residents, containers take between two weeks and a month to fill. In the holiday areas the same containers fill anywhere between one day and several weeks depending entirely on the weather.</p>
    <p>Before sensors, the authority described emptying as being done by gut feeling, and made the point that a few days of sunshine changed the picture completely. Growth in online shopping and recycling awareness had already pushed volumes about 20% above the level assumed when the collection contract was tendered.</p>
    <p>Within two months of installing sensors on all 82 containers, emptyings were down <strong>20%</strong> against a target of 25% &mdash; and residents stopped encountering overflowing containers. Any British coastal town, national park or lakeside village will recognise every part of that description.</p>
  </div>
</section>

<section class="section section-alt section-line">
  <div class="wrap">
    <p class="eyebrow">Where it applies</p>
    <h2 class="measure">British destinations with the same shape of problem</h2>
    <div class="grid grid-3 mt-3">
      <div class="card no-push"><h3>Coastal &amp; seaside towns</h3><p>Promenade, beach access and car park bins that fill within hours of a hot Saturday and barely move in November. The overflow photograph on social media is a reputational cost as much as an operational one.</p></div>
      <div class="card no-push"><h3>National parks &amp; AONBs</h3><p>Car parks and honeypot sites at the end of long single-track drives, where a wasted journey costs an hour and the overflow ends up as litter across a protected landscape.</p></div>
      <div class="card no-push"><h3>Holiday parks &amp; second-home areas</h3><p>Fan&oslash;'s exact case. Communal and semi-buried containers serving cottages occupied intensively for twelve weeks and empty for forty.</p></div>
      <div class="card no-push"><h3>Heritage sites &amp; visitor attractions</h3><p>Demand tracking opening hours, weather and events, on sites where an overflowing bin is directly in the photograph everyone takes.</p></div>
      <div class="card no-push"><h3>Market towns &amp; event venues</h3><p>Market days, festivals, fixtures and bank holidays &mdash; predictable spikes that fixed rounds handle by over-provisioning all year.</p></div>
      <div class="card no-push"><h3>Marinas, harbours &amp; country parks</h3><p>Dispersed containers over a wide site with long internal drive times, where the cost of checking a bin often exceeds the cost of emptying it.</p></div>
    </div>
    <div class="pullquote mt-3">
      <blockquote>In the holiday home areas there are no longer problems with overflowing waste containers.
      </blockquote>
      <cite><b>Operations manager</b> &mdash; Langelands Forsyning, Denmark, on its island collection network</cite>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split split-top">
      <div>
        <p class="eyebrow">Rural economics</p>
        <h2>When the drive costs more than the lift</h2>
        <p>In a dispersed rural or coastal operation, the expensive part is not emptying the container. It is getting to it.</p>
        <p>Langelands Forsyning used to send an employee on a <strong>176&nbsp;km round trip</strong> to inspect containers at 50 recycling sites. It took a day and a half, produced a paper report, and gave a different answer depending on who did the assessment. Only then could a driver plan which containers to empty.</p>
        <p>With 220 sensors reporting every six hours, that inspection round disappeared entirely. The utility reduced its fleet by <strong>one collection vehicle</strong>, and the operations manager delegated round planning to the driver, who now runs it himself.</p>
        <p>Any authority servicing bring sites 30&nbsp;km from the depot has a version of this problem, and the arithmetic works the same way.</p>
      </div>
      <div>
        <ul class="feature-list">
          <li><strong>Inspection rounds disappear.</strong> Nobody drives to look at a bin again.</li>
          <li><strong>Consistent judgement.</strong> A percentage means the same thing regardless of who is on shift.</li>
          <li><strong>Weekend and bank holiday cover</strong> planned from predicted fill &mdash; Langeland runs an extra Wednesday check specifically to catch containers likely to become critical over the weekend.</li>
          <li><strong>Deep rural connectivity.</strong> NB-IoT solved Langeland's data transfer problems across hilly terrain where earlier approaches had struggled.</li>
          <li><strong>Seasonal thresholds.</strong> Tighten in season, relax out of it, without rewriting the schedule twice a year.</li>
        </ul>
      </div>
    </div>
  </div>
</section>
"""

TOURISM_FAQS = [
    ("Our demand changes completely between summer and winter. Can the system cope?",
     "<p>That is the scenario it handles best, and the scenario a fixed timetable handles worst. Rounds are generated from current readings, so they expand and contract with actual demand without anyone rewriting a schedule. Forecasting uses each container's own history, so it learns that a specific beach car park behaves one way in August and another in February. Thresholds and reporting frequency can also be varied seasonally &mdash; tighter and more frequent in peak, relaxed off-season to conserve battery.</p>"),
    ("Will it stop bins overflowing on a hot bank holiday?",
     "<p>It gives you the warning you currently do not have. A container heading for 90% by Saturday afternoon is visible on Friday morning, so it can be picked up before it becomes a photograph. Fan&oslash;'s stated objective was protecting citizens against overloaded containers, and Langeland reports that overflowing containers in its holiday-home areas are no longer a problem. For known peaks you can raise reporting frequency to as often as 60 readings a day and tighten thresholds for the period.</p>"),
    ("We service remote sites a long way from the depot. Does that change the case?",
     "<p>It strengthens it considerably. Where the drive dominates the cost, avoiding an unnecessary journey saves far more than avoiding an unnecessary lift. Langeland replaced a 176&nbsp;km, day-and-a-half manual inspection round with automatic readings every six hours, and took a collection vehicle out of service altogether. If your bring sites are 30&nbsp;km from the depot, the arithmetic is on your side.</p>"),
    ("Will sensors work in a rural area with patchy mobile coverage?",
     "<p>Generally yes. NB-IoT is designed for exactly this: it uses existing mobile infrastructure but penetrates far better than ordinary data connections, including below ground level and inside metal enclosures. Langeland's rolling island terrain initially caused problems with data transfer, and NB-IoT was the technology that produced consistent, reliable reporting. We check coverage at your specific locations during the survey rather than assuming it.</p>"),
    ("We have semi-buried and underground containers. Are those a problem?",
     "<p>No &mdash; they are one of the best applications, because there is no way to assess their fill level from ground level at all. Fan&oslash; runs 82 semi-buried containers of up to three cubic metres on sensors, and NB-IoT was selected partly for its ability to hold a signal below ground.</p>"),
    ("Can this help with the litter and fly-tipping that follows an overflowing bin?",
     "<p>Indirectly but meaningfully. A container that has overflowed generates litter across the surrounding area and invites side-waste, and clearing that costs far more than the collection would have. Preventing the overflow prevents most of the consequence. There is also a capacity effect: both Stralsund and Vejle redeployed the hours freed by fewer wasted journeys onto exactly this kind of work &mdash; Vejle used it to start collecting waste along roads and at bridges.</p>"),
]


def pages():
    return [
        Page(
            path="sectors/",
            nav_key="sectors",
            title="Who We Work With | Smart Waste Sensors for UK Operations",
            description="Sensor-led waste collection for UK councils, waste contractors, universities, NHS trusts and large estates, and tourism, coastal and parks authorities.",
            keywords="smart waste for councils, waste sensors for contractors, campus waste management, coastal waste collection",
            h1="Who we work with",
            eyebrow="Sectors",
            lede="The technology is the same everywhere. The business case, the buying process and the person who cares about it are not.",
            body=OVERVIEW_BODY,
            page_type="CollectionPage",
        ),
        Page(
            path="sectors/local-authorities/",
            nav_key="sectors",
            breadcrumbs=CRUMB,
            title="Smart Bin Sensors for UK Councils | Cut Collection Costs",
            description="Sensor-led collection for district and unitary councils: fewer wasted lifts, no overflowing street bins, timestamped service evidence, less carbon.",
            keywords="smart bins for councils UK, local authority waste sensors, council bin fill level monitoring, reduce waste collection costs council",
            h1="Sensor-led collection for councils",
            eyebrow="Sectors",
            lede="Street bins, bring sites and communal containers on rounds set years ago &mdash; and the evidence gap every time a complaint reaches a member.",
            body=COUNCILS_BODY,
            faqs=COUNCILS_FAQS,
            faq_heading="Questions from local authorities",
            schema=[audience_service(
                "/sectors/local-authorities/",
                "Sensor-led waste collection for UK local authorities",
                "Radar fill-level sensors and dynamic round planning for district and unitary councils, covering street and park bins, bring sites, HWRC containers and communal housing waste, with service evidence and carbon reporting.",
                "District and unitary councils in the United Kingdom",
            )],
        ),
        Page(
            path="sectors/waste-contractors/",
            nav_key="sectors",
            breadcrumbs=CRUMB,
            title="Bin Sensors for Waste Contractors | Protect Your Margin",
            description="Fill-level data for UK waste contractors: recover margin on fixed-price work, evidence frequency and SLA performance, and win on carbon in tenders.",
            keywords="waste contractor route optimisation, commercial waste sensors UK, waste contract margin, SLA evidence waste collection",
            h1="Sensor-led collection for contractors",
            eyebrow="Sectors",
            lede="Every journey to a container that did not need emptying is cost with no revenue attached. Until now there was no way to know which ones those were.",
            body=CONTRACTORS_BODY,
            faqs=CONTRACTORS_FAQS,
            faq_heading="Questions from contractors",
            schema=[audience_service(
                "/sectors/waste-contractors/",
                "Fill-level monitoring for waste management contractors",
                "Radar fill-level sensors, dynamic round planning, driver app and API integration for UK waste management contractors, supporting margin recovery on fixed-price contracts, SLA evidence and tender differentiation.",
                "Waste management contractors operating in the United Kingdom",
            )],
        ),
        Page(
            path="sectors/universities-nhs-estates/",
            nav_key="sectors",
            breadcrumbs=CRUMB,
            title="Campus & Estate Waste Sensors | Universities and NHS",
            description="Fill-level sensors for universities, NHS trusts, business parks and large estates. Uneven term and shift demand, one decision-maker, live in weeks.",
            keywords="university waste management sensors, NHS estate waste, campus smart bins, business park waste monitoring",
            h1="Sensor-led collection for estates",
            eyebrow="Sectors",
            lede="One landowner, one budget holder, one boundary &mdash; and demand that swings with terms, shifts and clinic timetables.",
            body=ESTATES_BODY,
            faqs=ESTATES_FAQS,
            faq_heading="Questions from estates teams",
            schema=[audience_service(
                "/sectors/universities-nhs-estates/",
                "Waste fill-level monitoring for universities, NHS trusts and large estates",
                "Sensor-led waste collection for campuses, hospital sites, business and science parks, schools, shopping centres and managed residential estates, with CAFM and helpdesk integration and waste-stream reporting.",
                "Universities, NHS trusts, facilities and estates managers in the United Kingdom",
            )],
        ),
        Page(
            path="sectors/tourism-coastal-parks/",
            nav_key="sectors",
            breadcrumbs=CRUMB,
            title="Seasonal Waste Sensors | Coastal, Parks & Tourism Sites",
            description="Fill-level sensors for coastal towns, national parks, holiday areas and visitor attractions, where demand swings and fixed rounds fail both ways.",
            keywords="seasonal waste collection, coastal bin overflow, national park waste management, tourist area bin sensors",
            h1="Sensor-led collection for visitor destinations",
            eyebrow="Sectors",
            lede="A frequency set for February is negligent in August. A frequency set for August is expensive for the other ten months.",
            body=TOURISM_BODY,
            faqs=TOURISM_FAQS,
            faq_heading="Questions from visitor destinations",
            schema=[audience_service(
                "/sectors/tourism-coastal-parks/",
                "Seasonal waste collection monitoring for tourism, coastal and parks authorities",
                "Radar fill-level sensors and demand-led round planning for coastal towns, national parks, holiday areas, heritage sites, marinas and country parks, where waste volumes vary dramatically by season and weather.",
                "Coastal, tourism, national park and parks authorities in the United Kingdom",
            )],
        ),
    ]
