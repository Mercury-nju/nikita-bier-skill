# Reconstructed Casebook

This casebook is the evidence layer between public material and the package's decision model. Each case records a situation, constraint, choice, mechanism, observation, and transfer limit. It is a reconstruction of public evidence, not a transcript of private reasoning or a claim that Nikita would make the same choice today.

## Evidence tiers

- **A — direct first-person material:** an accessible original post or thread mirror that preserves the relevant context.
- **B — first-person material with incomplete access:** a retained local record or a short excerpt where the full context was not independently reviewed.
- **C — reported context:** an institutional report, interview summary, or independent profile.

Use a case to generate a hypothesis. Do not turn one case into a threshold, benchmark, or universal rule.

## C01 — TBH: concentrate the first network

- **Situation:** TBH was launched into a high-school network where the product's value depended on enough relevant peers being present.
- **Constraint:** a social product cannot reveal its value if the local graph is too sparse; a broad launch can create many installs without a usable network.
- **Choice reconstructed from public reporting:** start with a bounded school community, make participation and sharing compatible with that network, and use constrained prompts to reduce abuse.
- **Mechanism:** density creates the opportunity for a meaningful first interaction; constrained input reduces the cost of harmful behavior.
- **Observation:** the Berkeley event report describes rapid concentration and positive-only polling constraints. The report is evidence of the launch approach, not a complete experiment log.
- **Transfer limit:** this applies to products whose first value depends on local peers. It does not require every app to launch in a school or to remove expressive input.
- **Sources:** S12; S01.

## C02 — Gas: pay to answer the first real unknown

- **Situation:** an early Gas prototype served roughly 800 people in one school but incurred a high daily infrastructure cost because of the friends-of-friends feature.
- **Constraint:** the team had limited time before the school year ended and needed to learn whether the concept resonated, could be monetized, and could grow.
- **Choice:** accept the temporary cost, create enough graph density to test the real experience, and use the resulting funnel signal to decide whether to invest in a longer build.
- **Mechanism:** spend is justified when it buys information about the highest-value unknown before a time window closes. The cost is part of the activation experiment, not a permanent unit-economics target.
- **Observation:** the post says the test produced benchmarks that guided later allocation of effort.
- **Transfer limit:** do not copy the dollar amount. Estimate the minimum network and the shortest window needed to answer the decision in the user's product.
- **Sources:** S16, [original post](https://x.com/nikitabier/status/1754896706880127185).

## C03 — Choose the geometry of the network test

- **Situation:** a network product can be tested in many comparable communities or in one central, porous community that must be saturated at once.
- **Constraint:** repeated tests require plentiful, similar, and sufficiently independent communities. A mega-launch gives little room to iterate and can make low density look like product failure.
- **Choice:** use repeated closed-community tests when the graph allows them; reserve a concentrated launch for products whose value requires one central community.
- **Mechanism:** test geometry controls both density and the amount of iteration available. Exposure leakage destroys the independence of repeated tests.
- **Observation:** the post explicitly calls the second route less preferred because the product must be right on day one.
- **Transfer limit:** “more than ten communities” is his example, not a sample-size theorem. Measure overlap, comparability, and supply-demand requirements directly.
- **Sources:** S04, [original post](https://x.com/nikitabier/status/1917931582670733394); S11.

## C04 — Gas: distribution advantages expire

- **Situation:** a new consumer app can appear to copy an old product while depending on a new set of distribution conditions.
- **Constraint:** platform surfaces, permissions, social norms, and ranking systems change; a tactic that worked for one generation may stop working.
- **Choice:** rediscover the growth mechanism for the current platform instead of importing an old playbook.
- **Mechanism:** distribution is a temporary arbitrage. The product must find a current path from one user's experience to the next qualified user's experience.
- **Observation:** Nikita says Gas required several months of independent experimentation and that only part of the tactics still worked a year later.
- **Transfer limit:** this supports testing current constraints, not offensive platform manipulation or a promise that every product needs a “hack.”
- **Sources:** S07, [original post](https://x.com/nikitabier/status/1757436313622479138).

## C05 — Dupe: make the most interesting thing the product

- **Situation:** a product can contain many possible benefits and still fail to give users a clear reason to care.
- **Constraint:** every extra surface competes with the one experience that might make the product memorable and shareable.
- **Choice reconstructed from the public posts:** identify the most interesting property of Dupe and make that the center of the experience; place the interaction inside an existing shopping journey rather than requiring a separate destination.
- **Mechanism:** focus increases the chance that a user reaches and can explain the value. Contextual placement reduces the distance between intent and use.
- **Observation:** the posts describe this as a lesson from helping Dupe and show the URL-prefix interaction as an experiment in fitting the existing journey.
- **Transfer limit:** a memorable property is not automatically product-market fit. Confirm repeat use, conversion, and the economics of the surrounding journey.
- **Sources:** [PMF focus post](https://x.com/nikitabier/status/1785401369375228376), [Dupe launch](https://x.com/nikitabier/status/1772012191379554452), [Dupe interaction](https://x.com/nikitabier/status/1772012194009374762).

## C06 — Test quality: prevent execution from corrupting the signal

- **Situation:** a team wants to test a narrow hypothesis with few features.
- **Constraint:** a half-baked critical path can cause users to abandon before considering the value, making non-use ambiguous.
- **Choice:** keep scope narrow but make the tested path coherent and credible; improve the component that stands between the user and the decision.
- **Mechanism:** execution quality is a measurement condition. It does not create demand, but poor execution can hide demand.
- **Observation:** two posts reject the idea that a thin core flow is automatically a valid MVP; one uses a physical-quality analogy and allows a small amount of polish when the top funnel is the uncertainty.
- **Transfer limit:** do not polish every edge case or delay learning indefinitely. Define the one value event whose signal must be protected.
- **Sources:** S14, S15; [quality post](https://x.com/nikitabier/status/1868429071140684175), [MVP post](https://x.com/nikitabier/status/1857896428317630893).

## C07 — Permission loss can corrupt the social graph

- **Situation:** a social app asks for contact access or another permission needed to construct its graph.
- **Constraint:** an extra step can reduce consent, leaving the app with an incomplete graph and a misleading view of demand.
- **Choice:** treat permission design as part of the product, research strong consent flows from other apps, and keep a fallback if the graph is incomplete.
- **Mechanism:** onboarding changes the state of the network, not only the conversion rate. A lower opt-in can change who is reachable and therefore change the product itself.
- **Observation:** the posts report a large opt-in drop after an additional step and recommend another plan for a corrupt graph; a separate post says he studies existing consent flows and improves them relentlessly.
- **Transfer limit:** the cited percentages are contextual observations, not universal conversion laws. Privacy, trust, and user control remain product requirements.
- **Sources:** [permission post](https://x.com/nikitabier/status/1824251869264482552), [consent-flow post](https://x.com/nikitabier/status/1784656165663920323).

## C08 — Interest graphs need relevance before distribution

- **Situation:** a text-based interest-graph app must create a useful first timeline for someone with no history.
- **Constraint:** contact import does not reveal interests, and sparse text interactions give the algorithm weak early signals.
- **Choice:** treat relevance construction as the activation problem; use richer entry points or better interest expression rather than assuming a generic feed will teach the system enough.
- **Mechanism:** the first-value state is relevant content, not account creation. Distribution cannot repair a feed that is empty or irrelevant.
- **Observation:** the post contrasts interest graphs with full-screen video systems and treats AI-assisted interest expression as a possible future improvement.
- **Transfer limit:** the AI claim is a forecast. Validate the quality and repeat use of the resulting feed rather than assuming the technology solves cold start.
- **Sources:** S10, [original post](https://x.com/nikitabier/status/1922864090277392756).

## C09 — Messaging competes with an existing inbox

- **Situation:** a team considers adding messaging to increase engagement or sharing.
- **Constraint:** users already rely on an inbox with reliability, reach, delivery, and feature expectations.
- **Choice:** treat messaging as a replacement problem unless the feature serves a narrow job that does not compete with the main inbox.
- **Mechanism:** a new message surface inherits the reliability standard of the old one and can reduce external distribution if conversations move inside the app.
- **Observation:** the post describes full delivery, feature parity, and contact reach as the burden of replacing existing chat.
- **Transfer limit:** this is not a prohibition on task-specific communication. Test the job, the reachable contacts, and the delivery standard.
- **Sources:** S09, [original post](https://x.com/nikitabier/status/1928847135216382109).

## C10 — Virality and durability are different bets

- **Situation:** a product gets a sharp acquisition spike but does not yet have evidence of repeat use.
- **Constraint:** a distribution funnel can be made more predictable than a durable social network; the latter depends on long-term habit and replacement of an existing behavior.
- **Choice:** measure spread and durability separately, and decide whether a temporary product can create value even without becoming a permanent network.
- **Mechanism:** acquisition is a sequence of observable transitions; durable retention is a rarer outcome with different causes.
- **Observation:** Nikita calls virality methodical and durable social networks unusually rare, while also describing temporary products as capable of real value.
- **Transfer limit:** do not use this distinction to excuse poor retention when durability is the product promise, or to demand daily use from a product with a different natural frequency.
- **Sources:** S01, S06, [original post](https://x.com/nikitabier/status/1824491565622104552).

## C11 — Manual validation is appeal, not repeatability

- **Situation:** a founder or team manually supplies content, matching, or prompts and sees strong first-value results.
- **Constraint:** removing the help may cause the result to collapse; the manual intervention may be the true product.
- **Choice:** use manual effort to expose the maximum possible appeal, then remove one dependency at a time and measure whether normal users can reproduce the experience.
- **Mechanism:** assisted demand and independent demand are separate hypotheses.
- **Observation:** the manual-validation thread explicitly recommends maximizing execution quality before testing whether the appeal survives removal of manual work.
- **Transfer limit:** a manual pilot can justify learning and iteration; it does not justify scaling by itself.
- **Sources:** S03, [thread mirror](https://threadreaderapp.com/thread/1820660351366738276.html).

## C12 — Product leadership: optimize for a human signal

- **Situation:** at X, product decisions involve ranking, spam, AI-generated content, platform integrity, and a large public conversation.
- **Constraint:** automation and growth incentives can adulterate the signal users came to read; policy and product choices have externalities beyond a funnel metric.
- **Choice reconstructed from public X-role posts:** treat authenticity, anti-spam, and the quality of the human signal as product requirements; use targeted controls and verification where incentives create abuse.
- **Mechanism:** a platform's value can be destroyed by optimizing the wrong proxy. Product quality includes the integrity of the environment in which users make judgments.
- **Observation:** these are public statements during his Head of Product tenure, not a complete internal strategy or proof that each intervention worked.
- **Transfer limit:** apply this as a defensive systems lens. Do not infer private motives, implementation details, or universal policy positions from public replies.
- **Sources:** [human-signal post](https://x.com/nikitabier/status/2025712861650305512), [anti-spam post](https://x.com/nikitabier/status/2011825522817270230), [crypto phishing post](https://x.com/nikitabier/status/2039341761156538644).

## Cross-case patterns

The strongest repeated structure is conditional rather than absolute:

1. **Start with the valuable human state.** A feature is irrelevant until a user reaches a meaningful outcome.
2. **Identify the state that must exist before that outcome.** It may be a peer graph, relevant content, reliable delivery, or a credible interface.
3. **Choose a test geometry that can create the state.** Closed communities enable iteration; porous communities may require concentration.
4. **Make the tested path credible enough to produce interpretable evidence.** Manual help and focused polish are allowed when they answer a specific unknown.
5. **Expose the route to the next qualified user.** Sharing, search, partnerships, or platform distribution are mechanisms, not virtues by themselves.
6. **Separate short-term spread from repeat value.** Call a result viral, durable, assisted, or unknown according to the measured transition.
7. **Re-check constraints as the platform changes.** A prior distribution advantage is a dated observation, not a reusable recipe.

This ordering is the package's reconstruction. It is supported by recurring cases, but it is not a published framework from Nikita Bier.
