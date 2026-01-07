---
marp: true
theme: default
paginate: true
header: 'ECBS5228A: Designing Analytics Projects'
footer: 'Block 3: Retention & Growth Analyses'
---

<!-- _class: lead -->
<!-- _paginate: false -->
<!-- _header: '' -->
<!-- _footer: '' -->

# Designing Analytics Projects

## Block 3: Retention & Growth Analyses

**Eduardo Arino de la Rubia**
January 8, 2026

---

## Block 3 Overview

| Section | Time |
|---------|------|
| Retention Analysis | 20 min |
| Power User Analysis | 13 min |
| Mini-Case Exercise | 10 min |
| Failure Analysis | 13 min |
| Expansion & Monetization | 10 min |
| Ecosystem Analysis | 12 min |
| Day 1 Wrap-up | 8 min |

---

## The Retention & Growth Questions

Block 2 was about **getting** customers.
Block 3 is about **keeping** and **growing** them.

> Acquisition without retention is a leaky bucket.

The analyses in this block answer:
- Why do they leave? (Retention)
- Who matters most? (Power User)
- What's broken? (Failure)
- How do they grow? (Expansion)

---

<!-- _class: lead -->

# Part 1: Retention Analysis
### *(22 minutes)*

---

## What is Retention Analysis?

**Measuring whether users come back after their first interaction.**

The fundamental question:

> Of the users who signed up on Day 0, what percentage are still active on Day N?

This tells you if your product has lasting value — or if people try it and leave.

<!--
INSTRUCTOR NOTE:

**Background:** Retention is often called "the silent killer" — companies can grow quickly with poor retention by pouring money into acquisition, but it's not sustainable. The D7 and D30 retention benchmarks vary dramatically by industry: gaming apps often have 20% D30, productivity apps 40%+, social apps in between.

**Key point:** Retention tells you if your product has lasting value.

**Say something like:**
"Retention analysis answers a simple but crucial question: do people come back?

Of the users who signed up on a given day — call it Day 0 — what percentage are still active on Day 7? Day 30? Day 90?

This is the single best indicator of whether your product has lasting value. If people try it and never return, it doesn't matter how many you acquire — you're filling a leaky bucket.

I like to think of retention as the truth-teller. Marketing can get people in the door. A clever onboarding flow can get them to complete signup. But if they don't come back the next week? The product didn't deliver value. Retention is the metric you can't fake."

**If asked:** "What's a good retention rate?"
A: It depends on the product category. Gaming apps: 20-30% D30 is solid. Productivity SaaS: 40%+ D30. Social apps: 30-40% D30. The trend matters as much as the absolute number — is it improving or declining?

**Transition:** "Let me show you why retention matters more than most people realize..."
-->

---

<!-- _header: '' -->
<!-- _footer: '' -->

![bg contain](../figures/images/block_03_retention_vs_acquisition.png)

---

## Why Retention Matters More Than Acquisition

**Acquisition is expensive. Retention compounds.**

- Improving acquisition 20% → 20% more users
- Improving retention 20% → 20% more users **every cohort, forever**

Small retention improvements have massive long-term impact.

<!--
INSTRUCTOR NOTE:

**Background:** This is one of the most important slides for students to internalize. Companies often over-invest in acquisition and under-invest in retention. The math is simple but powerful: acquisition improvements are additive (one-time gain), retention improvements are multiplicative (compound over every future cohort).

**Key point:** Retention improvements compound. Acquisition improvements don't.

**Say something like:**
"I want you to understand the math of retention vs. acquisition.

If you improve acquisition 20%, you get 20% more users this period. Great. But that's a one-time gain.

If you improve retention 20%, you get 20% more users retained from this cohort. And 20% more from next month's cohort. And 20% more from every cohort forever.

Retention compounds. Acquisition doesn't.

A 5 percentage point improvement in D30 retention might sound small. But apply it to every cohort over 3 years and you've potentially doubled your active user base compared to where you'd be otherwise.

This is why smart companies obsess about retention. It's not as glamorous as growth — nobody writes headlines about 'retention improved 3 percentage points' — but the long-term math is overwhelmingly in favor of retention investment."

**If asked:** "Then why do companies focus so much on acquisition?"
A: Several reasons. Acquisition is more visible. Executives can see ads running. Growth numbers look good in board decks. Retention is quiet — you're preventing something bad, not creating something visible. Also, many companies have short time horizons.

**Transition:** "Let me show you what data you need for retention analysis..."
-->

---

## The Data You Need

| Field | Example | Why |
|-------|---------|-----|
| `user_id` | `u_12345` | Track individual users |
| `signup_date` | `2026-01-01` | Define cohort (Day 0) |
| `activity_date` | `2026-01-08` | When they came back |
| `activity_type` | `app_open` | What counts as "active" |

**Critical decision:** What counts as "active"?
- App open? (low bar)
- Core action? (higher bar, more meaningful)
- Purchase? (highest bar)

---

## Defining Retention: DN vs. Rolling

**DN retention** — Active on Day N specifically?
`Active Day N / Signups Day 0`

**Rolling D7** — Active at any point in days 1-7?
`Active any day 1-7 / Signups Day 0`

**Example:** 1,000 signups Jan 1 → 420 active Jan 8 → D7 = 42%

**DN is stricter.** Rolling is more forgiving. Be explicit.

---

<!-- _header: '' -->
<!-- _footer: '' -->

![bg contain](../figures/images/block_03_retention_curve.png)

---

## Reading the Retention Curve

**Shape matters:**
- **Steep early drop** = First-time experience problem
- **Continued decline** = No habit formation
- **Flattens** = Found product-market fit for those users

Where the curve flattens = your "true" retention rate.

<!--
INSTRUCTOR NOTE:

**Background:** The shape of the retention curve tells a story. Most products have steep early drops (Day 1-7) as users who signed up but never engaged disappear. The curve then either continues declining (product doesn't form habits) or flattens (users who made it past the early drop have found value). The "true" retention rate is where the curve stabilizes.

**Key point:** A steep early drop is normal. What matters is whether the curve eventually flattens.

**Say something like:**
"When you look at a retention curve, the shape tells you a story.

A steep early drop — say, 50% by Day 7 — sounds bad, but it's actually normal. Many people sign up and never really try the product. They downloaded the app and forgot. They created an account and got distracted. That's expected.

What you care about is what happens after. If the curve keeps declining — 50% at D7, 30% at D30, 15% at D60, trending toward zero — you don't have habit formation. Users try it, use it a bit, and gradually drift away. Your product doesn't become part of their routine.

If the curve flattens — 50% at D7, 35% at D30, 30% at D60, stable around 28% — you have something. Those 28% found enough value to keep coming back. That's your 'true' retention rate.

The place where the curve flattens tells you what percentage of users you're really retaining long-term. Everything before that is the 'sorting' period."

**If asked:** "When does the curve typically flatten?"
A: Varies by product. Consumer apps often see stabilization by D30-D60. Enterprise software might take months. Gaming can stabilize in days.

**Transition:** "You shouldn't just look at one cohort though..."
-->

---

## Cohort Analysis: Comparing Over Time

Don't just look at one cohort. Compare them:

| Cohort | D1 | D7 | D30 |
|--------|----|----|-----|
| Jan 2025 | 65% | 42% | 28% |
| Apr 2025 | 62% | 38% | 24% |
| Jul 2025 | 58% | 35% | 22% |
| Oct 2025 | 55% | 35% | ??? |

**Trend is down.** Something changed — product? Acquisition source? Competition?

Cohort analysis reveals trends that aggregate metrics hide.

---

## Retention Driver Analysis

Beyond "what is retention?" → **"what drives retention?"**

**Method:** Compare users who retained vs. churned. What's different?

| Behavior in First Week | Retained D30 | Churned D30 |
|-----------------------|--------------|-------------|
| Added ≥3 friends | 52% | 18% |
| Completed profile | 45% | 22% |
| Posted content | 48% | 15% |
| Only browsed | 12% | 68% |

**Insight:** Friend-adding is the strongest predictor.

---

## The Driver Analysis Trap

**Correlation ≠ causation.**

Users who add 3+ friends retain better. But:
- Did friend-adding **cause** retention?
- Or do **naturally engaged users** both add friends AND retain?

If you force friend-adding on disengaged users, they might still churn.

**Always recommend A/B tests** before mandating changes based on driver analysis.

<!--
INSTRUCTOR NOTE:

**Background:** This is one of the most important cautions in the entire course. Every company does retention driver analysis and finds correlations like "users who do X retain better." The temptation is to force everyone to do X. This rarely works because it confuses correlation with causation. The Facebook "7 friends in 10 days" story is the canonical example — it's often misunderstood as "make everyone add 7 friends" when the insight was about identifying engaged users early.

**Key point:** Correlation is not causation. Recommend A/B tests before mandating changes.

**Say something like:**
"This slide is so important I want you to write it down. The driver analysis trap.

You do the analysis. You find that users who add 3+ friends in the first week retain at 2x the rate. The product team says: 'Great! Let's make everyone add 3 friends before they can use the app.'

Stop. Think about what you're assuming.

You're assuming that adding friends CAUSES retention. But what if engaged users — people who were always going to retain — naturally add friends because they're engaged? The adding didn't cause the engagement; they were both caused by underlying engagement.

If that's true, forcing friend-adding on disengaged users won't help. They'll add friends to get past the gate and then churn anyway. Or worse, they'll abandon during onboarding because you made it harder.

This is why your recommendation should always be: 'We found a correlation. We recommend an A/B test to establish causation before mandating the change.' That's what separates good analysts from dangerous ones."

**If asked:** "How do you run the A/B test?"
A: Test group gets prompted/encouraged to add friends but not forced. Control group gets normal experience. Measure D30 retention for both. If test retains better, there's likely a causal effect. If they're the same, the correlation was selection bias.

**Transition:** "Let me show you some common data quality issues to watch for..."
-->

---

## Common Retention Data Issues

**Inconsistent "active" definition** — Different teams use different events → metrics don't match

**Bot/fraud signups** — Unusual signup patterns → inflates D0, deflates retention

**Reactivation confusion** — Churned user returns after 90 days → is this D1 or new user?

**Platform differences** — iOS vs. Android tracking gaps → retention looks different

**Standardize your "active" event** across the company.

---

## The SnapGram Scenario

**Company:** SnapGram (photo sharing app)
**Problem:** D7 retention dropped from 42% to 35% over 6 months
**Stakes:** "Sugar diet growth" — high acquisition masking retention crisis

**Hypothesis:** Users who add ≥3 friends in first 48 hours retain at 2x the rate. Onboarding doesn't push friend-adding hard enough.

---

## SnapGram: Counter-Metrics

**Signup completion** (Guardrail) — Aggressive onboarding increases abandonment

**Engagement depth** (Guardrail) — "Zombie retention" = they return but don't engage

**Notification opt-out** (Tradeoff) — Pushy re-engagement causes fatigue

---

## SnapGram: Pre-Mortem

> We found friend-adding was the #1 predictor. Product added a mandatory "add 5 friends" step.
>
> Signup completion dropped 30%.
>
> The correlation was selection bias — engaged users organically add friends, but forcing it didn't make disengaged users engaged.
>
> **Lesson:** Recommend A/B tests, not mandates. Correlation ≠ causation.

---

## Retention Analysis: Key Takeaways

1. **Define "active" precisely** — same event across all analysis
2. **DN vs. rolling retention** — be explicit about which you're using
3. **Cohort comparisons reveal trends** — aggregates hide insights
4. **Driver analysis is correlational** — A/B test before mandating
5. **Counter-metrics matter** — don't break signup to fix D7

---

<!-- _class: lead -->

# Part 2: Power User Analysis
### *(13 minutes)*

---

## What is Power User Analysis?

**Understanding who your best users are and what they do differently.**

Most products have highly skewed engagement:

> A small percentage of users drive most of the value.

Power user analysis asks:
- How concentrated is engagement?
- Who are these users?
- What do they do differently?
- Should we optimize for them or broaden engagement?

<!--
INSTRUCTOR NOTE:

**Background:** Most products have highly skewed engagement — a small percentage of users drive a disproportionate share of value. This is the Pareto principle applied to user engagement. Power user analysis helps companies understand who these users are and decide whether to double down on them or try to create more of them.

**Key point:** Engagement is usually skewed. Understanding power users informs strategy.

**Say something like:**
"Most products have a dirty secret: a small percentage of users drive most of the value.

Think about any app you use. Some people check it 20 times a day. Most people open it once a week — if that. The daily users might be 10% of your base but 60% of your engagement.

Power user analysis asks four questions.

First: how concentrated is engagement? Is it 80/20? 90/10? 95/5?

Second: who are these power users? What do they have in common?

Third: what do they do differently? Features, behaviors, patterns?

Fourth — and this is the strategic question: should we optimize for power users, or try to create more of them?

This last question doesn't have a right answer. It's a strategy decision. Your job as an analyst is to provide the data that informs the decision."

**If asked:** "Shouldn't we always try to create more power users?"
A: Not necessarily. If your power users have fundamentally different needs or circumstances than casual users, trying to convert casual users may dilute the product for everyone. Sometimes serving power users better is the right call.

**Transition:** "Let me show you what data you need..."
-->

---

## The Data You Need

| Field | Example | Why |
|-------|---------|-----|
| `user_id` | `u_12345` | Identify individuals |
| `engagement_metric` | `viewing_hours` | What defines "power" |
| `time_period` | `Jan 2026` | Consistent measurement window |
| `user_attributes` | Tenure, source, demographics | Describe power users |
| `behaviors` | Features used, content consumed | What they do differently |

**Critical decision:** What metric defines "power"?
- Time spent? Actions taken? Revenue generated?

---

<!-- _header: '' -->
<!-- _footer: '' -->

![bg contain](../figures/images/block_03_pareto_curve.png)

---

## The 80/20 Rule (Pareto)

Often, engagement follows a power law:
- Top 10% of users → 50%+ of engagement
- Top 20% of users → 80%+ of engagement

The exact numbers vary, but skew is almost universal.

---

## Calculating Concentration

**Gini coefficient** or simple percentile analysis:

| User Percentile | % of Total Viewing Hours |
|-----------------|-------------------------|
| Top 1% | 15% |
| Top 5% | 35% |
| Top 10% | 52% |
| Top 20% | 72% |
| Bottom 50% | 8% |

**High concentration** = Small group matters a lot
**Low concentration** = Engagement is distributed

---

## Power User Behavioral Profile

Once you identify power users, describe them:

| Dimension | Power Users | Casual |
|-----------|------------|--------|
| Tenure | 18 mo avg | 4 mo |
| Sessions/week | 12 | 2 |
| Features used | 8 of 10 | 2 of 10 |
| Content type | Series | Movies |
| Time of day | Evening | Weekend |

**Insight:** Power users have formed a habit. Casual users haven't.

---

## Path to Power: How Users Become Power Users

Track user journeys over time:

| Months Active | % Became Power User |
|--------------|---------------------|
| 1 | 2% |
| 3 | 8% |
| 6 | 15% |
| 12 | 22% |

**Questions:** What triggers the transition? Can we accelerate it?

---

## The Strategic Question

**Two options:**

1. **Optimize for power users**
   - They drive most engagement
   - High retention, high value
   - Risk: Alienate casual users

2. **Broaden engagement**
   - More users become power users
   - Larger addressable base
   - Risk: Dilute product for core users

**This is a strategy decision, not an analytics one.** Your job is to inform it.

---

## The Streamflix Scenario

**Company:** Streamflix (streaming service, 45M subscribers)
**Problem:** Engagement is highly skewed. Small % drives most viewing.
**Question:** Optimize for power users or broaden engagement?

**Hypothesis:** Top 10% of users account for >50% of viewing hours and have distinct content preferences we're not explicitly designing for.

---

## Streamflix: Counter-Metrics

**Casual user satisfaction** (Guardrail) — Power user features may confuse casual users

**Content diversity** (Tradeoff) — Optimizing for power users may narrow content

**New user activation** (Guardrail) — Power user UX may overwhelm newcomers

---

## Streamflix: Pre-Mortem

> We redesigned homepage for power users (binge-watchers). Casual users saw engagement drop 20%, churn increased. We optimized for power users at the expense of everyone else.

**Lesson:** Serve both segments. Present a balanced strategy.

---

## Power User Analysis: Key Takeaways

1. **Engagement is usually skewed** — measure how much
2. **Define "power" with a clear metric** — time, actions, or revenue
3. **Profile power users behaviorally** — what do they do differently?
4. **Counter-metric: casual user health** — don't alienate the majority
5. **This informs strategy** — analysts provide data, leadership decides

---

<!-- _class: lead -->

# Mini-Case Exercise: Retention
### *(10 minutes)*

---

## Mini-Case: SocialApp Retention Drop

> **Situation:** SocialApp's D7 retention dropped from 42% to 34% after a major UI redesign.
>
> **Additional data:**
> - Power users (top 10%) seem unaffected — their D7 is still 68%
> - Casual users (bottom 50%) dropped from 28% to 18%
> - The new UI emphasizes "stories" over the feed

**Think (2 min):** What does this pattern tell you? Which foundational analysis would you use first?

---

## Mini-Case: Discussion

**Questions to consider:**

1. Why might power users be unaffected while casual users suffer?
2. Is this a Retention Analysis problem or a Power User Analysis problem?
3. What counter-metric should have been tracked during the redesign?
4. What's your hypothesis for the root cause?

<!--
INSTRUCTOR NOTE:
Cold call 2-3 students.
Looking for:
- Power users have habit formation, casual users don't
- The redesign catered to power user preferences
- Counter-metric: casual user engagement, feature adoption by segment
- Hypothesis: Stories are a power user feature; casual users wanted simple scrolling
-->

---

<!-- _class: lead -->

## ☕ Stretch Break
### 5 minutes

Stand up. Walk around. The last 30 minutes cover Failure and Expansion analyses.

---

<!-- _class: lead -->

# Part 3: Failure Analysis
### *(13 minutes)*

---

## What is Failure Analysis?

**Systematically investigating why something isn't working.**

Different from other analyses:
- **Funnel analysis** tells you *where* users drop off
- **Failure analysis** tells you *why*

Often **exploratory** — you don't have a hypothesis yet. You're categorizing problems.

<!--
INSTRUCTOR NOTE:

**Background:** Failure analysis is different from other analyses because it's explicitly exploratory. You don't start with a hypothesis — you start with a symptom ("searches are failing") and build a taxonomy of causes. This is qualitative work disguised as quantitative analysis. The manual sampling step is crucial and often skipped by analysts who want to stay in SQL.

**Key point:** Failure analysis is exploratory. You're categorizing problems, not testing hypotheses.

**Say something like:**
"Failure analysis is different from everything else we've covered. It's explicitly exploratory.

Here's the difference. Funnel analysis tells you WHERE users drop off — 40% abandon at the payment step. But it doesn't tell you WHY. Is the page slow? Confusing form? Missing payment method? You don't know.

Failure analysis answers the 'why' question. And here's the key: you usually don't have a hypothesis when you start. You have a symptom — searches are returning zero results, support tickets are spiking, error rates are up. Your job is to categorize the failures and size each category.

This is qualitative work. You can't stay in SQL for this. You have to look at actual examples — actual search queries that failed, actual error messages, actual support tickets. And then you build a taxonomy: 'These failures are spelling errors. These are inventory gaps. These are junk queries.' That taxonomy is the analytical output."

**If asked:** "Can't we automate this with machine learning?"
A: Eventually, maybe. But you need the taxonomy first. And ML classification is only as good as its training labels — which means a human had to categorize examples first. Start manual, automate later.

**Transition:** "Here's when you'd use failure analysis..."
-->

---

## When to Use Failure Analysis

| Symptom | Failure Analysis Approach |
|---------|--------------------------|
| Zero search results | Sample queries, categorize why they failed |
| High error rates | Sample errors, identify root causes |
| Support tickets | Categorize complaints, size each category |
| Abandonment | Review session recordings, identify patterns |

**Common thread:** Something is broken, but you don't know the mix of causes.

---

## The Method: Manual Sampling

**Step 1:** Pull a random sample (100-500 instances of failure)

**Step 2:** Manually review and categorize each one

**Step 3:** Develop a taxonomy (3-7 categories)

**Step 4:** Validate taxonomy at scale (can you apply it programmatically?)

**Step 5:** Size each category (volume and impact)

This is qualitative-first, quantitative-second.

---

## Example: Zero-Results Search

Sample 200 zero-result queries. Manually categorize:

| Category | Example | Count | % |
|----------|---------|-------|---|
| **Spelling error** | "ipone case" | 86 | 43% |
| **Synonym gap** | "sneakers" (we index "trainers") | 42 | 21% |
| **Inventory gap** | "vintage camera" (we don't sell) | 34 | 17% |
| **Junk/nonsense** | "asdfgh" | 24 | 12% |
| **Ambiguous** | "gift" (too broad) | 14 | 7% |

**Insight:** 43% is spelling. That's a clear priority.

---

## Opportunity Sizing

Not all failures are equal. Size by impact:

| Category | % | Value | Opportunity |
|----------|---|-------|-------------|
| Spelling | 43% | $50 | $5.4M/yr |
| Synonym | 21% | $75 | $3.9M/yr |
| Inventory | 17% | $120 | $5.1M/yr |
| Junk | 12% | $0 | $0 |

**Insight:** Spelling is highest volume, but inventory has high-value queries.

---

## Validation: Inter-Rater Reliability

Manual classification is subjective. Validate it:

**Method:** Have 2 people independently classify the same 50 samples.

| Agreement Level | Interpretation |
|-----------------|----------------|
| >80% | Taxonomy is clear, can proceed |
| 60-80% | Refine category definitions |
| <60% | Taxonomy is too subjective, rethink |

If classifiers disagree, the categories aren't crisp enough.

---

## The FindIt Scenario

**Company:** FindIt (e-commerce search engine)
**Problem:** 12% of searches return zero results (up from 9%)
**Stakes:** Each percentage point = ~$2M lost GMV

**Framing:** This is **exploratory**. We don't know why searches fail. Goal is to categorize and size before picking a solution.

---

## FindIt: Counter-Metrics

| Counter-metric | Type | Why it could break |
|----------------|------|-------------------|
| **Search relevance** | Guardrail | Returning bad results is worse than no results |
| **Query latency** | Guardrail | Complex spelling logic may slow search |
| **Inventory trust** | Tradeoff | Showing "similar" items may frustrate users |

**Key insight:** Aggressive spell-correction can break things. "Febreeze" → "Freeze" is wrong.

---

## FindIt: Pre-Mortem

> We found spelling errors were 45% of failures and recommended a spelling correction system.
>
> Engineering built it, but the speller was too aggressive — it "corrected" valid brand names and niche terms. Search relevance dropped 15%.
>
> **Lesson:** Exploratory work was valuable, but we skipped validation. Test edge cases before launch.

---

## Failure Analysis: Key Takeaways

1. **Start with manual sampling** — you need to see the failures
2. **Build a taxonomy** — 3-7 categories, mutually exclusive
3. **Validate with inter-rater reliability** — if classifiers disagree, refine
4. **Size by impact, not just volume** — small category can have big $$$
5. **This is exploratory** — you're building hypotheses, not testing them
6. **Counter-metrics prevent over-correction** — fixing one thing can break another

---

<!-- _class: lead -->

# Part 4: Expansion & Monetization Analysis
### *(13 minutes)*

---

## What is Expansion Analysis?

**Understanding how customers grow their relationship with you.**

Questions:
- Why do free users upgrade to paid?
- Why do basic subscribers upgrade to premium?
- What triggers expansion (more seats, higher tier)?

This is about **extracting more value from existing customers** — often cheaper than acquisition.

---

<!-- _header: '' -->
<!-- _footer: '' -->

![bg contain](../figures/images/block_03_freemium_funnel.png)

---

## The Freemium Model

**Freemium math:**
- Free users: Large base, low/no revenue
- Paid users: Smaller base, meaningful revenue
- Premium: Smallest base, highest revenue

**The question:** What makes someone convert?

---

## The Data You Need

| Field | Example | Why |
|-------|---------|-----|
| `user_id` | `u_12345` | Track individual journeys |
| `subscription_status` | `free`, `basic`, `premium` | Current state |
| `status_change_date` | `2026-01-15` | When they upgraded |
| `usage_metrics` | Storage used, features used | What might trigger upgrade |
| `limit_hit_events` | `storage_limit_reached` | Friction points |

---

## Conversion Driver Analysis

Compare users who upgraded vs. stayed free:

| Behavior (Week Before Upgrade) | Upgraded | Stayed Free |
|-------------------------------|----------|-------------|
| Hit storage limit | 78% | 12% |
| Used premium feature (trial) | 65% | 8% |
| Invited team member | 45% | 5% |
| Heavy daily usage | 52% | 15% |

**Insight:** Hitting limits and trying premium features are strong triggers.

---

## Limit Analysis: The Conversion Trigger

Many freemium products use **limits** to drive conversion:

| Limit Type | % Who Hit It | Conversion Rate If Hit |
|-----------|--------------|------------------------|
| Storage (5GB) | 15% | 35% |
| Team members (3) | 8% | 52% |
| Projects (10) | 12% | 28% |
| API calls | 3% | 65% |

**Insight:** Few users hit limits, but those who do convert at high rates.

**Question:** Should we lower limits to force more conversions?

---

<!-- _header: '' -->
<!-- _footer: '' -->

![bg contain](../figures/images/block_03_limit_tradeoff.png)

---

## The Limit Dilemma

Lowering limits increases conversion, but:

- **Too high:** Few hit the limit, low conversion
- **Too low:** Users feel nickeled-and-dimed, churn

**Finding the sweet spot requires experimentation.**

<!--
INSTRUCTOR NOTE:

**Background:** The limit dilemma is central to freemium strategy. Limits are the most powerful conversion lever — when users hit a limit, conversion rates spike. But limits that are too aggressive damage user trust and drive free users away. This is a classic tradeoff with no universal right answer.

**Key point:** Limits convert, but aggressive limits damage trust. Finding the right balance requires experimentation.

**Say something like:**
"This is the central tension in freemium: the limit dilemma.

Limits are incredibly powerful for conversion. When someone hits a storage limit or project limit, their conversion rate might be 10x higher than someone who hasn't hit a limit. They have an immediate need.

So there's a temptation: lower the limits. Make people hit them earlier. Convert more users.

But here's the problem. If limits feel too aggressive, users feel nickeled-and-dimed. They came for a 'free product' and immediately hit a paywall. They churn — often angrily, with bad reviews.

If limits are too generous, almost nobody hits them. You have millions of free users happily using your product forever, never converting.

The sweet spot is somewhere in the middle: limits that let users get genuine value from the free tier, encounter the limit naturally as they grow, and feel that paying is worth it.

Finding that sweet spot requires experimentation. There's no formula. You have to test different limits and measure both conversion AND free user retention."

**If asked:** "How do you test limit changes safely?"
A: Gradually and with holdbacks. Lower the limit for 10% of new users first. Measure conversion and churn for that cohort. If both metrics improve (or conversion goes up without killing churn), expand.

**Transition:** "Let's look at a real scenario..."
-->

---

## The NoteSpace Scenario

**Company:** NoteSpace (productivity SaaS)
**Problem:** 2M free users, 180K paid (9% conversion)
**Question:** Where should Product invest to drive upgrades — limits, feature discovery, or targeting?

**Hypothesis:** Users who hit the 5GB storage limit convert at 3x, but only 15% ever hit it.

---

## NoteSpace: Counter-Metrics

| Counter-metric | Type | Why it could break |
|----------------|------|-------------------|
| **Free user retention** | Guardrail | Aggressive prompts drive free users away |
| **Upgrade satisfaction** | Guardrail | Premature upgrades → regret → churn |
| **Brand perception** | Tradeoff | "Pushy" monetization damages trust |

---

## NoteSpace: Pre-Mortem

> We identified "high-value" free users (heavy usage, hit limits, tried premium features) and aggressively targeted them with upgrade prompts.
>
> Conversion increased 40%, but free user DAU dropped 25% as annoyed users left.
>
> Many "high-value" users were power free users who loved the free tier — they felt betrayed, not persuaded.
>
> **Lesson:** Looking valuable ≠ ready to convert. Use holdout tests. Monitor free retention as a hard guardrail.

---

## Expansion Analysis: Key Takeaways

1. **Conversion drivers are behavioral** — what triggers the upgrade moment?
2. **Limits are powerful but dangerous** — too aggressive alienates users
3. **Targeting requires validation** — holdout tests before aggressive prompts
4. **Counter-metric: free user health** — don't kill the funnel to boost conversion
5. **Selection bias is real** — engaged users ≠ incremental conversions

---

<!-- _class: lead -->

# Part 5: Ecosystem Analysis
### *(12 minutes)*

---

## What is Ecosystem Analysis?

**Understanding how multiple products or features interact.**

Questions:
- Do our products complement each other (1+1=3)?
- Or cannibalize each other (1+1=1.5)?
- Should we invest in cross-product features?

Relevant for: Multi-product companies, platform businesses, feature suites.

<!--
INSTRUCTOR NOTE:

**Background:** As companies grow, they often launch multiple products or features. The strategic question is whether these complement each other (using one increases value of another) or cannibalize each other (using one reduces need for another). This analysis is particularly relevant for platform businesses, multi-product companies, and feature-rich applications.

**Key point:** Products/features can complement (1+1=3) or cannibalize (1+1=1.5). Understanding which is crucial for strategy.

**Say something like:**
"Ecosystem analysis becomes important as companies grow and launch multiple products.

The core question: when users adopt multiple products, is the total value greater than the sum of parts — or less?

Complements: Think Slack and Google Drive. Using one makes the other more valuable. Integrations deepen engagement. 1+1=3.

Substitutes: Think iMessage and WhatsApp. Using one reduces need for the other. They compete for the same use case. 1+1=1.5.

If your products are complements, you want to encourage multi-product adoption — build bridges, promote cross-selling, reward multi-product users.

If your products are substitutes, you might be cannibalizing yourself. New product success comes at the expense of the old product. That might be okay strategically, but you need to know it's happening.

The analysis tells you which scenario you're in — and the strategy depends on the answer."

**If asked:** "How do I know if products are complements or substitutes?"
A: Look at user behavior. If users of Product A have higher engagement with Product B than non-users of A, they might be complements. If users of A rarely use B, they might be substitutes. But beware of selection bias — test causally.

**Transition:** "Let me define complements and substitutes more precisely..."
-->

---

## Complements vs. Substitutes

| Relationship | Definition | Example |
|-------------|------------|---------|
| **Complement** | Using A increases value of B | Slack + Google Drive |
| **Substitute** | Using A reduces need for B | iMessage vs. WhatsApp |
| **Independent** | No relationship | Spotify + banking app |

**Multi-product companies want complements.** Substitutes mean internal competition.

---

## The Selection Bias Problem

You observe: Users of both Product A and B retain 40% better than single-product users.

**But:** Is that because:
1. Using both products **causes** higher retention? (Complement)
2. Highly engaged users **naturally** use more products? (Selection bias)

If it's selection bias, pushing cross-product adoption won't help — and may annoy users.

<!--
INSTRUCTOR NOTE:

**Background:** This is the same selection bias problem we discussed in retention driver analysis, applied to ecosystem analysis. Multi-product users often look better on every metric — but that's often because engaged users naturally adopt more products, not because multi-product adoption causes engagement. This mistake leads to expensive "cross-product" investments that don't work.

**Key point:** Multi-product correlation almost always has selection bias. Engaged users do everything.

**Say something like:**
"This is the same trap we saw in retention driver analysis, applied to ecosystem analysis.

You look at the data. Users who use both Product A and Product B retain 40% better than single-product users. The product team says: 'Great! Let's invest in cross-product features to get more people using both!'

Stop. Same question as before. Is it that using both products CAUSES higher retention? Or is it that highly engaged users — the people who would have retained anyway — naturally explore and adopt more products?

If it's the second — and it usually is — pushing cross-product adoption on single-product users won't help. You're not creating engagement. You're just annoying people who were perfectly happy with one product.

This is why you can't just observe correlations. You need to test causally. Did the INTERVENTION of promoting cross-product adoption increase retention? Or did you just select for already-engaged users?"

**If asked:** "How can you tell the difference?"
A: A/B test. Show cross-product prompts to a treatment group, suppress them for a control group. Measure retention for both. If treatment retains better, there's a causal effect. If not, it was selection bias.

**Transition:** "Let me show you some methods to untangle this..."
-->

---

## Methods to Untangle Causation

| Method | How It Works | Strength |
|--------|-------------|----------|
| **Propensity matching** | Compare multi-product users to similar single-product users | Controls for observables |
| **Natural experiments** | When one product has outage, does the other suffer? | Reveals dependence |
| **Holdout tests** | Suppress cross-product prompts in some markets | Gold standard |

**Key insight:** Observational analysis alone cannot establish causation.

---

## The SocialSuite Scenario

**Company:** SocialSuite (FriendFeed, QuickChat, PicShare)
**Problem:** Products are siloed. Each PM optimizes their own metrics.
**Question:** Are products complements? Should we invest in "bridges"?

**Hypothesis:** Multi-product users retain 30% better, and cross-product features will increase stickiness.

---

## SocialSuite: Counter-Metrics & Pre-Mortem

**Counter-metrics:**
- Individual product focus (dilution risk)
- User overwhelm (too many cross-promos)
- Cannibalization (one product grows at another's expense)

**Pre-mortem:** We found 40% better retention for multi-product users and invested heavily in cross-product features. But it was selection bias — engaged users adopt everything naturally. Cross-product prompts annoyed single-product users, and FriendFeed DAU dropped 10%.

---

## Ecosystem Analysis: Key Takeaways

1. **Multi-product correlation ≠ causation** — selection bias is likely
2. **Use natural experiments** — outages reveal true dependence
3. **Holdout test before investing** — don't assume cross-product features help
4. **Watch for cannibalization** — products may compete internally
5. **This informs platform strategy** — big investment decisions

---

<!-- _class: lead -->

# Day 1 Summary & Wrap-up
### *(8 minutes)*

---

## The Retention & Growth Analyses

| Analysis | Question | Pitfall |
|----------|----------|---------|
| **Retention** | Do they come back? | Zombie retention |
| **Power User** | Who matters most? | Alienating casual users |
| **Failure** | What's broken? | Over-aggressive fixes |
| **Expansion** | How do they grow? | Annoying free users |
| **Ecosystem** | Products complement? | Selection bias |

---

## Common Thread: Selection Bias

**Multiple analyses today shared this trap:**

- Retention drivers: Engaged users do everything
- Power users: They were always going to be power users
- Expansion: High-propensity users would convert anyway

**Solution:** A/B test before major investments. Correlation ≠ causation.

<!--
INSTRUCTOR NOTE:

**Background:** This is the meta-lesson for Block 3, just as "interaction effects" was for Block 2. Selection bias is the single most common mistake in retention and growth analytics. It's related to the causal inference problem we introduced in Block 2, but here we're seeing it specifically in user-level analysis.

**Key point:** Selection bias causes most analytics failures in retention and growth work. Always ask: "Are we finding causation, or just selecting for engaged users?"

**Say something like:**
"I want you to notice a pattern that ran through every analysis we covered today.

Retention drivers: Users who add friends retain better. But maybe engaged users both add friends AND retain — selection bias.

Power users: Multi-product users have higher LTV. But maybe engaged users naturally adopt more products — selection bias.

Expansion: Users who hit limits convert. But maybe power users hit limits AND would have converted anyway — selection bias.

Do you see the pattern? In every case, we're observing a correlation and tempted to assume causation. But there's a hidden variable: underlying user engagement.

Here's the rule: whenever you find a behavioral correlation in user data, ask yourself: 'Would an A/B test validate this?' If you're not sure, recommend the test before the investment. The difference between correlation and causation can be millions of dollars of wasted effort.

Block 2's lesson was 'things interact.' Block 3's lesson is 'correlation isn't causation.' Both are the same underlying problem — observational data lies to you in predictable ways."

**If asked:** "Is there ever a case where we don't need to A/B test?"
A: If the intervention is cheap and reversible, sometimes you just try it. But for major investments — redesigns, forced onboarding changes, budget reallocation — always test.

**Transition:** "That wraps up Day 1..."
-->

---

## Day 1 Complete

You now know:
- **The Analytics Project Brief framework** (10 sections)
- **Counter-metrics and adversarial thinking**
- **9 foundational analyses** (4 acquisition + 5 retention/growth)

**Day 2:** Stakeholders & Influence, then Application & Capstone Preparation.

---

<!-- _class: lead -->
<!-- _paginate: false -->

# See you Monday!

**Day 2 starts at 10:50**

- Block 4: Application & Practice
- Block 5: Stakeholders & Influence

**Before then:** Review the Brief template. Questions: rubiae@ceu.edu
