# Decision Model

This is the package's most explicit reconstruction of Nikita Bier's public product judgment. It is a hypothesis about recurring decision structure, not a claim of complete access to his mind. Use it to make an analysis falsifiable.

## State variables

Before recommending a change, describe the product using the variables that can block the next decision:

| Variable | Question | Typical failure |
| --- | --- | --- |
| **M — motivation** | What outcome already matters enough to change behavior? | Polite interest without action |
| **V — first value** | What observable event makes the product useful for the first time? | A signup or install with no meaningful payoff |
| **D — density / supply** | What people, content, or reliability must exist at that moment? | An empty graph, irrelevant feed, or unreachable peer |
| **E — execution fidelity** | Is the tested path coherent enough for users to consider the value? | Half-baked flow interpreted as demand failure |
| **A — acquisition** | How does the next suitable user arrive and reach V? | Sharing that creates visits but not first value |
| **R — repeat value** | Why would the user return at the product's natural frequency? | Calling a launch spike retention |
| **C — cost / speed** | What must be spent or built before the unknown becomes answerable? | Optimizing infrastructure before learning the key unknown |
| **S — system integrity** | How can the product be spammed, manipulated, or made unsafe? | Growth incentives that corrupt the environment |

## Causal order

The default chain is:

```text
M → V → D → E → A → R
       ↘ C     ↘ S
```

The arrows are dependencies, not a score. If V cannot occur, A is usually premature. If D is required and missing, a distribution test may only measure the ability to install users. If E is too weak, non-use is ambiguous. If A works but R is unknown, the result is viral or distributed, not durable. If S is ignored, a metric can improve while the product's value is degraded.

## Decision sequence

1. **Name the decision.** Examples: change onboarding, choose a launch shape, add messaging, or expand acquisition.
2. **Write the value event.** Use a behavioral event a user would recognize as useful; do not use install or account creation unless that is the product's actual value.
3. **Map the preconditions.** List the minimum peers, content, permissions, delivery reliability, manual work, or infrastructure needed for the event.
4. **Protect the signal.** Make the critical path credible enough to reach consideration. Keep scope small, but remove obvious execution confounds.
5. **Choose test geometry.** Use independent repeated communities when they are plentiful and comparable. Use bounded concentrated activation when one porous community must be dense at launch.
6. **Expose one acquisition mechanism.** Follow the next suitable user from source to first value. Do not count a share, impression, or invite as distribution success by itself.
7. **Measure repeat use separately.** Match the observation window to the product's natural cadence and keep denominators visible.
8. **Review integrity and decay.** Test foreseeable misuse and check whether a platform-dependent advantage is still available.
9. **Make the next decision conditional.** State what result supports continuing, changing the mechanism, or stopping.

## How to resolve apparent contradictions

| Tension | Resolution |
| --- | --- |
| “Get to value quickly” vs. “long onboarding can work” | Remove effort that does not create value; keep effort that creates the relevant graph, trust, or content, and measure first value rather than signup time. |
| “Keep the MVP small” vs. “half-baked products distort signal” | Minimize scope, not the quality of the one path being tested. Half-bake components that are outside the decision. |
| “Test small communities” vs. “launch big” | Inspect community supply, overlap, and density requirements. A mega-launch is a constraint response, not a default growth tactic. |
| “Build a social loop” vs. “private utilities can work” | Ask whether another person is part of the value event. If not, use the appropriate individual acquisition and retention mechanism. |
| “Growth is scientific” vs. “durable networks are rare” | Separate measurable distribution transitions from long-term habit formation. Do not use one as evidence for the other. |
| “Move fast” vs. “protect the signal” | Spend or polish only where it answers the current high-value unknown or prevents an interpretable test. |

## Evidence discipline

Every conclusion in a response should carry one of these labels internally:

- **Observed:** directly supported by a source passage or reported event.
- **Repeated:** appears in multiple contexts but still comes from one person's public material.
- **Inferred:** a mechanism reconstructed by this package.
- **Case advice:** a conditional recommendation for the user's product.
- **Unknown:** not supported by the supplied evidence.

Never use the phrase “Nikita would definitely...” for an inferred or case-specific conclusion. The safer form is “His public material repeatedly emphasizes X; for your case, that suggests testing Y, unless Z is true.”

## Stop conditions

- Stop scaling acquisition when the first-value event repeatedly fails or depends entirely on unmeasured manual work.
- Stop deleting setup when the setup creates relevant peers, trust, or content and the value event is strong after completion.
- Stop copying a distribution tactic when its platform condition has changed or the next user does not reach value.
- Stop calling a product durable until repeat use is measured for the product's natural cadence.
- Stop sharpening the tone when the mechanism, evidence, or uncertainty has been lost.
