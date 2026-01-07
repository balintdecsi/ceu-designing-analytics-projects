---
marp: true
theme: default
paginate: true
header: 'ECBS5228A: Designing Analytics Projects'
footer: 'Block 2: Acquisition Analyses'
---

<!-- _class: lead -->
<!-- _paginate: false -->
<!-- _header: '' -->
<!-- _footer: '' -->

# Designing Analytics Projects

## Block 2: Acquisition Analyses

**Eduardo Arino de la Rubia**
January 8, 2026

---

## Block 2 Overview

| Section | Time |
|---------|------|
| Funnel Analysis | 22 min |
| Channel Attribution | 22 min |
| Mini-Case Exercise | 10 min |
| Campaign Effectiveness | 22 min |
| CAC/LTV Analysis | 18 min |

All four analyses answer: **"How efficiently are we turning money into customers?"**

---

## How to Think About These Analyses

**This is a reference library, not a memorization exercise.**

Today we cover 9 foundational analyses. You won't memorize them all—and you shouldn't try.

**Your goal:**
1. Know what each analysis answers conceptually
2. Recognize which one applies to a given problem
3. Know where to find the detailed example when you need it

Each analysis has a complete Brief example in `templates/examples/`. Use them.

---

<!-- _class: lead -->

# Part 1: Funnel Analysis
### *(22 minutes)*

---

<!-- _header: '' -->
<!-- _footer: '' -->

![bg contain](../figures/images/block_02_funnel_basic.png)

---

## Funnel Analysis: The Core Question

Every conversion process has steps. Most users don't finish.

Your job: **Find where they leave, and why.**

**The core question:** At which step are we losing the most users, and why?

---

## Funnels Are Everywhere

| Business | Typical Stages |
|----------|---------------|
| **E-commerce** | Browse → Cart → Purchase |
| **SaaS** | Visit → Sign up → Subscribe |
| **B2B Sales** | Lead → SQL → Closed Won |
| **Mobile App** | Install → Register → First Action |
| **Content** | Impression → Click → Share |

The stages depend on your business. Define them explicitly.

---

## The Data You Need

Funnel analysis requires **event-level data** with three things:

| Field | Example | Why |
|-------|---------|-----|
| `user_id` | `u_12345` | Track same user across steps |
| `timestamp` | `2026-01-08 14:32:07` | Sequence events in order |
| `event_type` | `checkout_started` | Identify which step occurred |

Optional but valuable: device, source, session_id, properties (like cart value)

---

## Defining Stages: Be Precise

**Vague:** "User started checkout"
**Precise:** "`checkout_start` event fired"

| Stage | Good Definition |
|-------|-----------------|
| Cart | `cart_page_loaded` event |
| Payment | `payment_form_submitted` event |
| Complete | `order_confirmation` event with `order_id` |

**Rule:** If you can't write the SQL WHERE clause, you haven't defined it.

---

## How to Calculate Conversion Rates

**Conversion Rate** = Users at Step N+1 / Users at Step N

**Example:**

| Stage | Users | Conv. Rate |
|-------|-------|------------|
| Cart | 10,000 | 85% → |
| Shipping | 7,820 | 88% → |
| Payment | 6,882 | 89% → |
| Confirm | 6,125 | — |

**Overall:** 61.3% cart-to-confirm

---

<!-- _header: '' -->
<!-- _footer: '' -->

![bg contain](../figures/images/block_02_funnel_output.png)

---

## Reading Funnel Output

Two ways to view:
- **Percentage view:** Which step has the worst conversion rate?
- **Absolute view:** Which step loses the most users?

Sometimes they're different. A 5% drop from 100K users (5K lost) matters more than a 20% drop from 1K users (200 lost).

---

## Segmentation: The Real Power

Overall funnel hides important variation.

| Segment | Cart-to-Confirm |
|---------|-----------------|
| **Desktop** | 68% |
| **Mobile Web** | 54% |
| **iOS App** | 72% |
| **New Users** | 51% |
| **Returning Users** | 74% |

**Segment by:** Device, traffic source, new vs. returning, geography, time period.

The insight is usually in the segments, not the aggregate.

---

## Common Funnel Data Issues

- **Missing events** — Event counts << page views → undercounts
- **Duplicate events** — Same user/timestamp → overcounts
- **Bot traffic** — Unusual patterns, data center IPs → inflates top
- **Cross-device** — User appears twice → undercounts
- **Session stitching** — Gaps in journey → breaks logic

**Always validate data before analyzing.**

---

## The Quickcart Scenario

**Company:** Quickcart (e-commerce)
**Problem:** Checkout completion dropped from 68% to 61%
**Stakes:** ~$4.2M in lost quarterly revenue

**Hypothesis:** Drop concentrated in payment step on mobile (new UI launched October)

---

## Quickcart: The Brief Application

| Brief Section | Quickcart |
|--------------|-----------|
| **Primary metric** | `order_complete` / `checkout_start`, per session, US users |
| **Counter-metrics** | AOV (tradeoff), Fraud rate (guardrail), Support tickets (guardrail) |
| **Blocker** | Mobile team lead — defensive about October launch |

**Pre-mortem:** We identified payment step as problem, but events weren't firing on iOS 17. Recommended UI fix when real issue was measurement.

---

## Funnel Analysis: Key Takeaways

1. **Define stages with event names** — not page names, not intentions
2. **Calculate both % and absolute drops** — they tell different stories
3. **Segment immediately** — the insight is in the segments
4. **Validate data first** — logging gaps will mislead you
5. **Counter-metrics matter** — conversion isn't the only goal (AOV, fraud)

---

<!-- _class: lead -->

# Part 2: Channel Attribution Analysis
### *(22 minutes)*

---

## What is Attribution?

**Assigning credit to marketing touchpoints for conversions.**

A user's journey: LinkedIn ad (day 1) → Google ad (day 5) → Direct purchase (day 8)

**Who gets credit for the sale?**

This is the attribution problem. There's no objectively "correct" answer.

---

## What is a Touchpoint?

A **touchpoint** is any recorded marketing interaction:

| Field | Example | Purpose |
|-------|---------|---------|
| `user_id` | `u_12345` | Link touchpoints to conversions |
| `timestamp` | `2026-01-05 09:14:22` | Sequence the journey |
| `channel` | `paid_search` | What marketing source |
| `campaign` | `winter_sale_2026` | Which specific effort |
| `action` | `click` or `impression` | What happened |

You need touchpoints joined to conversion events by user.

---

## The Data Structure

**Touchpoint Table:**

| user_id | timestamp | channel | action |
|---------|-----------|---------|--------|
| u_123 | Jan 1 | linkedin_ads | impression |
| u_123 | Jan 5 | paid_search | click |
| u_123 | Jan 8 | direct | click |

**Conversion Table:**

| user_id | timestamp | revenue |
|---------|-----------|---------|
| u_123 | Jan 8 | $150 |

**Join them** to see all touchpoints that preceded the conversion.

---

## Attribution Windows

**How far back should you look?**

| Window | Use Case |
|--------|----------|
| **7-day click** | Standard for lower-funnel (search, retargeting) |
| **30-day click** | B2B, considered purchases |
| **1-day view** | Display, video (saw ad but didn't click) |
| **90-day** | Enterprise sales, long cycles |

**The window changes the answer.** A 7-day window ignores a LinkedIn ad from 3 weeks ago. A 90-day window includes it.

Be explicit about your window choice.

---

## Attribution Model: First-Touch

**Rule:** 100% credit to the first touchpoint in the journey.

```
SELECT user_id, MIN(timestamp) as first_touch, channel
FROM touchpoints
WHERE timestamp <= conversion_time
  AND timestamp >= conversion_time - INTERVAL 30 DAY
GROUP BY user_id
```

**Bias:** Overvalues awareness channels (display, social, content)
**Undervalues:** Conversion channels (search, retargeting)

---

## Attribution Model: Last-Touch

**Rule:** 100% credit to the final touchpoint before conversion.

```
SELECT user_id, MAX(timestamp) as last_touch, channel
FROM touchpoints
WHERE timestamp <= conversion_time
  AND timestamp >= conversion_time - INTERVAL 30 DAY
GROUP BY user_id
```

**Bias:** Overvalues closers (branded search, direct, retargeting)
**Undervalues:** Awareness channels that started the journey

**This is what most companies use by default.** It's convenient but misleading.

---

## Attribution Model: Linear

**Rule:** Split credit equally among all touchpoints.

If user had 4 touchpoints before a $100 conversion:
- LinkedIn: $25
- Content: $25
- Email: $25
- Search: $25

**Bias:** Treats all touchpoints as equal, ignores timing
**Useful for:** Seeing full journey, identifying "assist" channels

---

## Attribution Model: Time-Decay

**Rule:** More credit to recent touchpoints, less to older ones.

Common approach: Half-life decay (e.g., 7-day half-life)

| Days Before Conversion | Weight |
|-----------------------|--------|
| 0 (same day) | 100% |
| 7 | 50% |
| 14 | 25% |
| 21 | 12.5% |

**Bias:** Still privileges closers, just less extremely than last-touch
**Useful for:** Compromise between first and last touch

---

## Attribution Model: Position-Based (U-Shaped)

**Rule:** Heavy credit to first and last, less to middle.

Typical: **40% first / 20% middle (split) / 40% last**

Recognizes that:
- First touch introduced the user (awareness)
- Last touch closed the deal (conversion)
- Middle touches helped but were less decisive

**Popular because it feels intuitively fair.**

---

## Attribution Output: Touch-Based Models

| Channel | Last-Touch | First-Touch |
|---------|-----------|-------------|
| Paid Search | $450K | $180K |
| LinkedIn | $80K | $310K |
| Content/SEO | $120K | $260K |
| Direct | $150K | $200K |

Last-touch favors closers. First-touch favors awareness.

---

## Attribution Output: Distributed Models

| Channel | Linear | Position-Based |
|---------|--------|----------------|
| Paid Search | $290K | $320K |
| LinkedIn | $220K | $195K |
| Content/SEO | $200K | $190K |
| Email | $140K | $145K |
| Direct | $150K | $150K |

Distributed models spread credit more evenly across the journey.

**Look for channels where models disagree dramatically.** LinkedIn: $80K (last-touch) vs. $310K (first-touch). That's worth investigating.

---

## Path Analysis: Common Journeys

Beyond credit allocation, look at **paths**:

| Path | Conversions | Avg Value |
|------|-------------|-----------|
| Search → Direct | 1,240 | $95 |
| LinkedIn → Content → Search | 890 | $180 |
| Direct only | 2,100 | $75 |

**Insight:** Multi-touch journeys have higher value. LinkedIn often starts valuable journeys.

---

## Data Quality Nightmares

- **Cross-device** — User on phone, converts on laptop → appears as two users
- **Cookie deletion** — Privacy browsers → touchpoints disappear
- **Walled gardens** — FB/Google limit data → can't see full journey
- **UTM inconsistency** — Different teams → channels miscategorized

Attribution is only as good as your tracking.

---

## The DataDash Scenario

**Company:** DataDash (B2B analytics platform)
**Problem:** $2.4M/quarter across 6 channels, using last-touch only
**Suspicion:** Undervaluing awareness channels (LinkedIn, content)

**Hypothesis:** LinkedIn/content in >50% of deals as first-touch but <5% of last-touch credit.

---

## DataDash: Counter-Metrics

| Counter-metric | Type | Why it could break |
|----------------|------|-------------------|
| **Brand awareness** | Guardrail | Cutting awareness hurts long-term |
| **Lead quality** | Guardrail | Volume ≠ close rate |

**Blocker:** Paid Search manager — recently promoted based on "Search ROI" narrative. Reallocation = budget cut = career threat.

**Pre-mortem:** We cut Search to fund LinkedIn. Pipeline dropped 25%. Search was the "closer" for journeys LinkedIn started. We double-counted LinkedIn's influence.

---

## Attribution: Key Takeaways

1. **Touchpoint = user_id + timestamp + channel** — you need all three
2. **No model is "right"** — present multiple, look for disagreements
3. **Attribution windows matter** — be explicit about your choice
4. **Path analysis reveals interactions** — channels don't work alone
5. **Data quality limits everything** — cross-device and cookies kill accuracy
6. **Validate with holdouts** — before major budget shifts, test causally

---

<!-- _class: lead -->

# Mini-Case Exercise: Acquisition
### *(10 minutes)*

---

## Mini-Case: TechStart E-commerce

> **Situation:** TechStart sees a 15% cart abandonment spike this month.
> At the same time, a new paid social campaign launched targeting first-time visitors.
>
> The VP of Marketing says: "The campaign is bringing in low-quality traffic."
> The VP of Product says: "The new checkout flow is broken on mobile."

**Think (3 min):** Which analysis would you use first — Funnel or Channel Attribution? Why?

---

## Mini-Case: Discussion

**Key questions to consider:**

1. How would Funnel Analysis help you here?
2. How would Channel Attribution help you here?
3. What if both are right — how do you untangle the effects?
4. What data would you need to decide?

<!--
INSTRUCTOR NOTE:
Cold call 2-3 students.
Looking for:
- Funnel Analysis FIRST: See if the drop is concentrated in specific steps
- THEN segment by traffic source to see if paid social behaves differently
- If mobile checkout drop-off is high across ALL channels, it's Product
- If only paid social traffic abandons, it's the campaign quality
- Need: user_id + timestamp + event_type + source + device
-->

---

## ☕ Quick Stretch
### 3 minutes

Stand up. Check your phone. Campaign Effectiveness is next — and it introduces some important statistical concepts.

---

<!-- _class: lead -->

# Part 3: Campaign Effectiveness Analysis
### *(22 minutes)*

---

## A Quick Prerequisite: The "What If" Problem

> You take medicine and your headache goes away. How do you know the medicine worked?

**The answer:** You can't — it might have gone away on its own.

This is the core challenge of **causal inference**.

---

## What is a Counterfactual?

A **counterfactual** is: *"What would have happened if we hadn't done X?"*

**The Twin Study Analogy:**
- Twin A takes drug → better in 3 days
- Twin B takes placebo → better in 5 days
- Difference (2 days) = **causal effect**

**The problem in marketing:** We don't have twins. We must *construct* a comparison group.

---

## Three Ways to Build a "Control Twin"

**Randomized Holdout** — Randomly assign some markets to get no campaign
*Gold standard. Requires advance planning.*

**Geo-Matching** — Find naturally similar markets
*When randomization wasn't possible.*

**Synthetic Control** — Build weighted "twin" from multiple markets
*When no single market is a good match.*

**All three answer:** What would have happened without the campaign?

**Key insight:** The quality of your causal estimate depends entirely on how good your "control twin" is.

---

## The Fundamental Question

> **Did the campaign cause the sales, or would they have happened anyway?**

Sales went up 12% during the campaign. But:
- Economy improved
- Competitor had a bad quarter
- It was holiday season
- New stores opened

**Correlation is easy. Causation is hard.**

---

## Why This Matters

**Scenario:** You spent $18M on holiday marketing. Sales were up $45M vs. last year.

**CMO says:** "We drove $45M! That's 2.5x ROI!"

**CFO asks:** "Would sales have been up $30M anyway due to new stores and economy? So marketing only drove $15M — less than 1x ROI."

**Who's right?** You need to estimate the **counterfactual** — what would have happened without the campaign.

---

<!-- _header: '' -->
<!-- _footer: '' -->

![bg contain](../figures/images/block_02_counterfactual.png)

---

## The Counterfactual Problem

You can never directly observe what would have happened if you hadn't run the campaign.

You have to **estimate** the counterfactual using control groups or statistical models.

---

## Method 1: Randomized Holdout Test

**Gold standard.** Randomly select some markets/users to NOT see the campaign.

| Group | What They See | Size |
|-------|--------------|------|
| **Treatment** | Full campaign | 90% of markets |
| **Control (Holdout)** | No campaign | 10% of markets |

**After campaign:**
```
Incremental Effect = Treatment Sales - Control Sales
```

**Why it works:** Random assignment ensures groups are comparable. Any difference is caused by the campaign.

---

## Method 2: Geo-Matched Markets

When you can't randomize, find markets that **look similar** before the campaign.

| Market | Pre-Campaign Trend | Campaign Spend |
|--------|-------------------|----------------|
| Phoenix | +5% YoY | $2M (heavy) |
| Tucson | +4% YoY | $0 (control) |

**Compare post-campaign:** Did Phoenix outperform Tucson more than expected?

**Risk:** "Similar" markets may differ in unobserved ways.

---

## Method 3: Synthetic Control

**Build a "fake" control from weighted combination of real controls.**

You're measuring Phoenix (treated). You have 10 other cities as potential controls.

Algorithm finds weights: Phoenix ≈ 0.4×Denver + 0.3×Austin + 0.2×Portland + 0.1×Salt Lake

The weighted combination matches Phoenix's pre-campaign trend.

**Post-campaign:** Compare Phoenix to the synthetic Phoenix.

---

<!-- _header: '' -->
<!-- _footer: '' -->

![bg contain](../figures/images/block_02_synthetic_control.png)

---

## Reading Synthetic Control

The lines track together before the campaign.
The gap after = causal effect estimate.

---

## The Data You Need

| Data | Granularity | Why |
|------|-------------|-----|
| **Sales** | Market × Day/Week | Outcome variable |
| **Marketing spend** | Market × Day/Week | Treatment variable |
| **Pre-period trend** | 6-12 months before | Match controls |
| **Market characteristics** | Demographics, stores | Improve matching |

**Key requirement:** You need variation in spend across markets. If all markets got the same campaign, you can't estimate incrementality.

---

## Interpreting Results

Output looks like:

| Metric | Estimate | 95% CI |
|--------|----------|--------|
| Incremental Revenue | $42M | $28M - $56M |
| Campaign Spend | $18M | — |
| Incremental ROI | 2.3x | 1.6x - 3.1x |

**Critical:** Report confidence intervals, not just point estimates.

If CI includes 1x (or below), you can't confidently say campaign was profitable.

---

## Common Pitfalls

- **Control contamination** — Control sees treatment ads → geographic buffers
- **Selection bias** — Best markets get campaign → randomize or match
- **Pull-forward** — Sales spike then drop → measure full period
- **Competitor confound** — Competitor enters control → validate matching

---

<!-- _header: '' -->
<!-- _footer: '' -->

![bg contain](../figures/images/block_02_pull_forward.png)

---

## Pull-Forward: The Hidden Trap

**The question:** Did the campaign create NEW customers, or convince existing customers to buy earlier?

**Always check:** Compare campaign period + post-period to same timeframe last year.

---

## The BrightMart Scenario

**Company:** BrightMart (national retailer)
**Problem:** Spent $18M on holiday marketing. Sales up 12% YoY.
**Question:** How much was marketing vs. external factors?

**Stakeholder complexity:**
- CFO: Skeptical (burned by past campaign overspend)
- CMO: Advocate (budget depends on proving effectiveness)
- Agency: Worried (low ROI threatens $5M contract)

---

## BrightMart: Pre-Mortem

> We proved 2.8x ROI and CMO was thrilled.
>
> But CFO's team found our "control" markets had a new competitor (ValueMart) enter during the campaign — artificially depressing their sales and inflating our incrementality.
>
> When re-run with proper controls, ROI dropped to 1.4x.
>
> **Lesson:** Validate control market selection rigorously before running analysis.

---

## Campaign Effectiveness: Key Takeaways

1. **Correlation ≠ causation** — "sales went up" doesn't mean campaign worked
2. **You need a counterfactual** — what would have happened without campaign
3. **Randomized holdouts are gold standard** — plan them into future campaigns
4. **Synthetic control for observational** — when you can't randomize
5. **Check for pull-forward** — measure beyond campaign period
6. **Report confidence intervals** — point estimates alone are misleading

---

<!-- _class: lead -->

# Part 4: CAC/LTV Analysis
### *(18 minutes)*

---

## The Unit Economics Question

> **"Does a customer generate more value than they cost to acquire?"**

This is the foundation of sustainable growth.

If LTV > CAC: You can scale profitably
If LTV < CAC: Growth makes you poorer
If LTV ≈ CAC: You're running on a treadmill

---

## Definitions

**CAC** = Total Acquisition Cost / Customers Acquired
*How much you pay per customer*

**LTV** = Revenue × Margin × Lifespan
*How much a customer is worth*

**LTV:CAC** = LTV / CAC → Profitability ratio

**Payback** = CAC / Monthly Revenue → Months to recover

**Benchmarks:** SaaS > 3:1, E-commerce > 2:1

---

## Calculating CAC: "Fully Loaded"

**Don't just count media spend.** Include everything:

| Cost Type | Example | Often Forgotten? |
|-----------|---------|-----------------|
| Media spend | $500K Google Ads | No |
| Creative production | $50K video shoot | Sometimes |
| Agency fees | $100K retainer | Sometimes |
| Team salaries | $200K (portion of 4 people) | **Often** |
| Tools & software | $30K attribution tool | **Often** |

**Fully loaded CAC = ($500K + $50K + $100K + $200K + $30K) / 1,000 customers = $880**
vs. just media: $500

---

## CAC by Channel

Break down by acquisition source:

| Channel | Spend | Customers | CAC |
|---------|-------|-----------|-----|
| Paid Social | $300K | 400 | $750 |
| Paid Search | $400K | 800 | $500 |
| Organic/SEO | $100K* | 600 | $167 |
| Referral | $50K | 300 | $167 |

*Content team salaries allocated

**Insight:** Organic and referral are 3-4x more efficient than paid.

---

## Calculating LTV: The Projection Problem

LTV requires predicting the future:
- How long will they stay? (Retention)
- What will they spend? (Revenue)
- What's your margin? (Profitability)

**Simple formula:**
```
LTV = ARPU × Gross Margin × Customer Lifespan
```

**Example:** $50/month × 70% margin × 24 months = **$840**

---

## Cohort-Based LTV: More Accurate

Track actual cohorts over time:

| Months Since Signup | Cohort Jan 2025 | Cohort Apr 2025 |
|--------------------|-----------------|-----------------|
| Month 1 | $50 | $45 |
| Month 3 | $145 | $130 |
| Month 6 | $270 | $235 |
| Month 12 | $480 | ??? |

For newer cohorts, **extrapolate** based on older cohort curves.

**Warning:** Extrapolation is guessing. Be conservative.

---

<!-- _header: '' -->
<!-- _footer: '' -->

![bg contain](../figures/images/block_02_ltv_curve.png)

---

## Reading LTV Curves

Early months are observed. Later months are projected.

The further you project, the more uncertain the estimate.

---

## Channel Economics: The Winners

| Channel | CAC | LTV | LTV:CAC | Payback |
|---------|-----|-----|---------|---------|
| Organic | $167 | $840 | **5.0x** | 3 mo |
| Referral | $167 | $920 | **5.5x** | 2 mo |

These channels are highly profitable. Low cost, high retention.

---

## Channel Economics: The Losers

| Channel | CAC | LTV | LTV:CAC | Payback |
|---------|-----|-----|---------|---------|
| Paid Search | $500 | $780 | 1.6x | 8 mo |
| Paid Social | $750 | $650 | **0.9x** | 14 mo |

Paid social is underwater (LTV < CAC over 12 months).

**But wait...** Are channels independent?

---

## The Channel Interaction Problem

Channels don't work in isolation.

**Scenario:** You cut paid social because LTV:CAC is 0.9x.

What happens?
- Brand awareness drops
- Organic search volume decreases
- Referral slows (fewer people know about you)
- Overall growth drops 40%

**Paid social was feeding the other channels.**

---

## The MindfulApp Scenario

**Company:** MindfulApp (meditation app)
**Problem:** 40% YoY growth, burning $8M/quarter
**Question:** Are we acquiring customers profitably?

**Hypothesis:** Organic/referral >5x LTV:CAC; paid social ~1.2x

**Blocker:** Paid acquisition team — if paid social looks bad, team of 4 becomes team of 2. Jobs literally on the line.

---

## MindfulApp: Pre-Mortem

> We showed paid social had 1.5x LTV:CAC and recommended cutting 60% of spend.
>
> Growth slowed from 40% to 15%.
>
> Turns out paid social drove awareness that boosted organic and referral — channels weren't independent.
>
> **Lesson:** Run holdout tests before major channel cuts to understand interactions.

---

## CAC/LTV: Key Takeaways

1. **Use fully-loaded CAC** — include salaries, tools, creative
2. **Project LTV conservatively** — extrapolation is guessing
3. **Use cohort-based analysis** — track real behavior over time
4. **Calculate by channel** — aggregate hides important variation
5. **Channels interact** — cutting one may hurt others
6. **Payback matters** — not just ratio (cash flow implications)

---

<!-- _class: lead -->

# Block 2 Summary

---

## The Four Acquisition Analyses

| Analysis | Core Question | Key Method |
|----------|--------------|------------|
| **Funnel** | Where do we lose them? | Step-by-step conversion rates |
| **Attribution** | Which channels brought them? | Multi-model comparison |
| **Campaign** | Did spend cause the lift? | Counterfactual estimation |
| **CAC/LTV** | Worth more than they cost? | Cohort-based unit economics |

---

## Common Thread: Interactions

**Every pre-mortem in this block shares a theme:**

Things don't work in isolation.
- **Funnel:** Device handoffs (mobile browse, desktop buy)
- **Attribution:** Multi-touch journeys
- **Campaign:** Control market confounds
- **CAC/LTV:** Channel awareness spillover

**Before major decisions, test causally.** Attribution and correlation lie.

---

## Coming Up: Block 3

After break, we cover **Retention & Growth Analyses:**

| Analysis | Question |
|----------|----------|
| **Retention** | Why do they leave? |
| **Power User** | Who are our best customers? |
| **Failure** | What's broken? |
| **Expansion** | How do they grow? |
| **Ecosystem** | How do products interact? |

---

## Questions?

<!--
INSTRUCTOR NOTE:
Take 2-3 questions max.
Common Q: "Which analysis should I start with?"
A: Depends on the problem. Funnel if conversion is the issue, Attribution if budget allocation, etc. The Brief's methodology section forces you to justify.
-->

---

<!-- _class: lead -->
<!-- _paginate: false -->

# Break Time!

**Block 3 starts at 15:40**

Retention & Growth Analyses

