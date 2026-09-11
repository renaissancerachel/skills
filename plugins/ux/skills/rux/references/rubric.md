# RUX Rubric - the scoring engine

The Rapid UX rubric. 10 categories, 3 criteria each, 30 criteria total. Each criterion is scored 0-3. Categories total `/9`, the page totals `/90`.

Load this for any `evaluate`. The scoring procedure, quick-mode crosswalk, and report format live in `evaluate.md`; this file is the criteria and the math.

## The 0-3 scale

Apply the same anchors to every criterion. Score the page as it is, not as it could be.

| Score | Meaning |
|---|---|
| 0 | Missing, or actively harmful to the user |
| 1 | Present but poorly executed or inconsistent |
| 2 | Adequate and functional |
| 3 | Excellent and fully aligned with UX best practice |

Use `N/A` when the input does not let you judge a criterion (for example, judging responsiveness from pasted copy). Note it; do not score it as 0, and exclude it from the category max so the percentage stays honest.

## Categories

Each category below carries its guiding question, its three criteria, and the principles it draws from. Show the source line in pro-mode reports; it is what separates RUX from an opinion.

### I. Clarity & Visibility  `/9`
Is the user always aware of where they are, what is happening, and what to do next?
1. Navigation is clear and consistent across pages.
2. Users can quickly understand the site's purpose.
3. System status or progress indicators are present when needed.

*Grounded in: Nielsen (Visibility of System Status), ISO 9241 (Self-Descriptiveness), Rams (Clarity).*

### II. Consistency & Standards  `/9`
Does the site behave in predictable, familiar ways?
1. Components are visually and behaviorally consistent.
2. Terminology aligns with user expectations.
3. Icons and controls are familiar.

*Grounded in: Nielsen (Consistency & Standards), Shneiderman (Strive for Consistency), ISO 9241.*

### III. Feedback & Interaction  `/9`
Does the site respond appropriately to user actions?
1. Buttons and controls provide clear, immediate feedback.
2. Form errors and confirmations are well communicated.
3. Microinteractions enhance usability.

*Grounded in: Shneiderman (Offer Informative Feedback), Nielsen, ISO 9241.*

### IV. Control & Flexibility  `/9`
Can users move freely and correct mistakes easily?
1. Users can undo or change actions easily.
2. Clear exit points are available.
3. Shortcuts and power-user features are supported.

*Grounded in: Nielsen (User Control & Freedom), Shneiderman (Permit Easy Reversal of Actions).*

### V. Error Prevention & Recovery  `/9`
Does the site help users avoid and recover from mistakes?
1. Design prevents common user errors.
2. Error messages are helpful and actionable.
3. Form validation is user-friendly.

*Grounded in: Nielsen (Error Prevention; Help Users Recognize, Diagnose, and Recover from Errors), ISO 9241 (Error Tolerance).*

### VI. Aesthetic & Purposeful Design  `/9`
Is the visual design clean, meaningful, and free of distraction?
1. Visual hierarchy supports content understanding.
2. Design is free of clutter and unnecessary elements.
3. Typography, spacing, and colors are harmonious.

*Grounded in: Rams (Good Design Is Aesthetic; As Little Design As Possible), Nielsen (Aesthetic & Minimalist Design).*

### VII. Accessibility & Inclusivity  `/9`
Is the site usable by people of all abilities and contexts?
1. Meets basic WCAG 2.1 standards (contrast, keyboard navigation).
2. Media includes alt text or transcripts.
3. Responsive and functional on all screen sizes.

*Grounded in: ISO 9241 (Accessibility), Nielsen (Flexibility & Efficiency of Use), Inclusive Design Principles.*
*Note: RUX flags likely accessibility issues from inspection. A conformance claim needs a real WCAG audit; say so.*

### VIII. Motivation & Emotional Design  `/9`
Does the site engage users on an emotional level, in service of their goals?
1. Visuals and content create emotional engagement.
2. Calls-to-action are persuasive and well-placed.
3. Trust signals (testimonials, credentials, security) are present.

*Grounded in: Weinschenk & Barker (motivation, trust cues), Rams (Honest, emotionally engaging design), Nielsen.*
*Dual-use: reward persuasion that helps the visitor decide well. Flag dark patterns and manufactured urgency rather than scoring them as strengths.*

### IX. Learnability & Efficiency  `/9`
Can users learn the site quickly and complete tasks with ease?
1. Navigation and actions are intuitive for new users.
2. Task flows are streamlined.
3. Frequent actions are easily repeatable.

*Grounded in: ISO 9241 (Learnability, Suitability for the Task), Nielsen, Shneiderman (Reduce Short-Term Memory Load).*

### X. Relevance & Value  `/9`
Is the content valuable and tailored to user needs?
1. Content is timely, relevant, and useful.
2. Offerings are clearly articulated and benefit-driven.
3. Site provides reasons for return visits.

*Grounded in: Weinschenk (user motivation), Rams (Useful), ISO 9241 (Suitability for the Task).*

## Scoring the page

- Category score = sum of its three criteria (max 9), or scaled to `/9` if any criterion is `N/A`.
- Total = sum of the ten categories, out of 90.
- Report each category `/9`, the total `/90`, and the band below.

### Interpretation bands

| Total `/90` | UX quality | Suggested action |
|---|---|---|
| 80-90 | Excellent | Maintain and evolve. Monitor performance. |
| 65-79 | Good, with areas to improve | Prioritize quick wins from the lowest-scoring criteria. |
| 50-64 | Fair | Test with real users, revise design and flows. |
| Below 50 | Poor | Consider a full redesign or re-architecture. |

### Optional weighting (off by default)

Teams may weight categories to their priorities (for example, accessibility or emotional design counted double). Weighting changes the total, so keep the canonical `/90` unweighted version in every report and present any weighted total beside it, clearly labeled. Do not silently reweight.
