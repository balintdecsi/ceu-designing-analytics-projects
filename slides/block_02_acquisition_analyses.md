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

<!--
INSTRUCTOR NOTE:

**Background:** Students often panic when they see 9 analyses to cover in one day. This slide reframes expectations. The goal isn't memorization — it's pattern recognition. They need to know WHAT each analysis does, not HOW to execute it perfectly from memory.

**Key point:** Know what each analysis answers, not how to execute every detail.

**Say something like:**
"I want to set expectations for this block and the next one. We're going to cover 9 foundational analyses today. That sounds like a lot — and it is. But here's what I don't want you to do: don't try to memorize everything.

These analyses are a reference library. When you encounter a problem in the real world, you'll think: 'This looks like a funnel problem,' or 'This is a retention question.' Then you'll look up the details.

Your goal today is threefold. One: know what each analysis answers conceptually. Two: recognize which one applies when you see a business problem. Three: know where to find the detailed examples when you need them.

The template folder has complete Brief examples for each analysis. When you're working on your assignment, use them. Copy the structure. Adapt the content. That's how professionals work — nobody starts from a blank page."

**If asked:** "Will we need to memorize the formulas?"
A: For the exam, you'll need to know core concepts and when to use each analysis. The Brief template will be provided as reference.

**Transition:** "Let's dive into the first acquisition analysis — funnel analysis..."
-->

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

<!--
INSTRUCTOR NOTE:

**Background:** Funnel analysis is usually the first analysis new analysts learn, but it's often done poorly. The common mistake is calculating overall conversion without understanding step-by-step drop-off. The "why" is crucial — you can identify WHERE users drop but understanding WHY requires segmentation and often qualitative research.

**Key point:** Funnel analysis tells you WHERE users drop. The "why" requires digging deeper.

**Say something like:**
"Funnel analysis is one of the most common analytics tasks you'll encounter. Every conversion process has steps, and most users don't make it to the end. Your job is to find where they leave — and more importantly, why.

I want to emphasize that second part. Funnel analysis is very good at telling you WHERE users drop off. It's much harder to tell you WHY. If you see a 40% drop at the payment step, you know there's a problem. But is it because the page is slow? The form is confusing? They're comparison shopping? They don't have their credit card handy? The funnel doesn't tell you that.

So when you do funnel analysis, you're usually generating hypotheses, not proving conclusions. You identify the biggest drops, then segment to narrow down causes, then often need qualitative research — user interviews, session recordings — to understand the 'why'."

**If asked:** "How do I know if a drop-off rate is bad?"
A: Compare to benchmarks (industry averages), your historical data, or segment by segment. A 60% checkout completion might be great for luxury goods and terrible for commodities.

**Transition:** "Let me show you just how universal funnel thinking is..."
-->

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

<!--
INSTRUCTOR NOTE:

**Background:** Students sometimes think funnels only apply to e-commerce checkout. This table shows that funnel thinking is universal — any multi-step process can be analyzed as a funnel. The key insight is that YOUR business defines what the stages are; there's no universal template.

**Key point:** Funnels apply to any multi-step conversion process. Your business defines the stages.

**Say something like:**
"I want to show you that funnel thinking isn't just for e-commerce checkout. It's a universal framework.

E-commerce: Browse, Cart, Purchase — that's obvious. But look at SaaS: Visit, Sign up, Subscribe. Same structure. B2B sales: Lead, Sales Qualified Lead, Closed Won. Mobile app: Install, Register, First meaningful action.

Even content marketing is a funnel: Impression, Click, Share.

The point is: YOUR business defines what the stages are. There's no universal template. Your first job in any funnel analysis is to define the stages explicitly. What are the steps a user goes through? What events mark each transition?"

**If asked:** "How many stages should a funnel have?"
A: Typically 3-7. Too few and you miss important drops. Too many and you're just tracking every click. Focus on stages where users make meaningful decisions.

**Transition:** "Let me show you what data you need to do this analysis..."
-->

---

## The Data You Need

Funnel analysis requires **event-level data** with three things:

| Field | Example | Why |
|-------|---------|-----|
| `user_id` | `u_12345` | Track same user across steps |
| `timestamp` | `2026-01-08 14:32:07` | Sequence events in order |
| `event_type` | `checkout_started` | Identify which step occurred |

Optional but valuable: device, source, session_id, properties (like cart value)

<!--
INSTRUCTOR NOTE:

**Background:** Students often jump to analysis before understanding data requirements. The three required fields — user_id, timestamp, event_type — are non-negotiable for funnel analysis. Without user_id, you can't track the same person. Without timestamp, you can't sequence events. Without event_type, you can't define stages. Many analytics failures start with "we don't have that field."

**Key point:** Three fields are non-negotiable: user_id, timestamp, event_type. Check data availability BEFORE committing to the analysis.

**Say something like:**
"Before you do any funnel analysis, you need three things in your data.

User ID — some way to track the same person across steps. This could be a logged-in user ID, a device ID, a cookie. But you need something.

Timestamp — when did each event happen? You need this to sequence the journey. Did they add to cart before or after viewing shipping costs?

Event type — what happened? You need distinct events for each stage. 'checkout_started', 'payment_submitted', 'order_confirmed' — whatever your company calls them.

Without any one of these three, you cannot do funnel analysis. Full stop.

The optional fields — device, source, session_id — are what let you do the really valuable work: segmentation. But the core three are required.

Here's a tip: before you commit to a funnel analysis in your Brief, verify that these fields exist and are reliable. Many projects fail because someone assumed the data existed."

**If asked:** "What if we have page views but not events?"
A: Page views can work if URLs are unique per stage. But events are more reliable — page views can fire multiple times, have bot traffic, etc.

**Transition:** "Now let's talk about defining stages precisely..."
-->

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

<!--
INSTRUCTOR NOTE:

**Background:** Vague stage definitions are one of the most common sources of analytics confusion. When someone says "checkout started," five people might interpret it five different ways. The SQL test forces precision: if you can't write WHERE event_type = 'something', you haven't defined it. This connects directly to the Brief's metric precision requirements.

**Key point:** If you can't write the SQL WHERE clause, you haven't defined the stage.

**Say something like:**
"This is a rule I want you to internalize: if you can't write the SQL WHERE clause, you haven't defined it.

'User started checkout' — what does that mean? Did they click the checkout button? Did the checkout page load? Did they enter their email? Five people might interpret this five different ways.

'checkout_start event fired' — now I can write SQL. WHERE event_type = 'checkout_start'. No ambiguity.

[Point to table]

Look at these definitions. Cart: cart_page_loaded event. Payment: payment_form_submitted event. Complete: order_confirmation event with order_id.

Each one is precise enough to query. That's the standard.

When you write your Brief's metrics section, apply this test. Can you write the SQL? If not, keep refining until you can."

**If asked:** "What if my company doesn't have consistent event naming?"
A: That's a common problem. You'll need to figure out what events exist and what they mean. Check with engineering or look at the raw data. Document your definitions explicitly.

**Transition:** "Now let's calculate conversion rates..."
-->

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

<!--
INSTRUCTOR NOTE:

**Background:** This is one of the most important slides in the funnel section. The aggregate funnel (say, 61% overall conversion) hides all the interesting variation. When you segment, you discover that mobile web is 54% while iOS app is 72% — that's an 18 percentage point gap! Segmentation is where insights live.

**Key point:** The insight is usually in the segments, not the aggregate.

**Say something like:**
"This is where funnel analysis gets interesting. The overall number — 61% checkout completion — is not that useful. It's an average that hides everything important.

Look at this table. Desktop is 68%. Mobile web is 54%. That's a 14 percentage point gap. iOS app is 72% — even better than desktop. New users are 51%, returning users are 74%.

Do you see the insights now? Mobile web has a problem. New users struggle more than returning users. These are actionable findings. 'Overall conversion is 61%' is not actionable.

This is why your first move after building the overall funnel should be: segment. By device, by traffic source, by new vs. returning, by geography, by time period.

The insight is almost never in the aggregate. It's in the segments."

**If asked:** "How many segments should I look at?"
A: Start with the obvious ones: device, new/returning, traffic source. Then let hypotheses guide you. Don't segment randomly — each segment should answer a question.

**Transition:** "Before we move on, let me warn you about common data issues..."
-->

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

<!--
INSTRUCTOR NOTE:

**Background:** This is the first complete scenario application in the course. Walk through how the Brief framework connects to funnel analysis. Note the specific elements: measurable problem (68% to 61%), quantified stakes ($4.2M), and a testable hypothesis (payment step, mobile, October launch). This is what "good scoping" looks like.

**Key point:** Notice how the hypothesis is specific and testable: payment step, mobile, October launch.

**Say something like:**
"Let me walk you through how funnel analysis connects to the Brief framework.

Quickcart is an e-commerce company. Their checkout completion dropped from 68% to 61%. That's 7 percentage points — and they've calculated it costs them about $4.2M per quarter.

Now look at the hypothesis: 'Drop concentrated in payment step on mobile, new UI launched October.'

This hypothesis is specific and testable. We can segment the funnel by device and look at the payment step. We can compare October and after to before October. If the hypothesis is right, we'll see mobile payment drop concentrated after the October launch.

That's what good scoping looks like. Not 'checkout is bad' — that's too vague. Not 'maybe the whole thing is slow' — that's not testable. A specific hypothesis about where, when, and what changed."

**If asked:** "What if the hypothesis is wrong?"
A: Great! That's a result. You eliminate one explanation and move to the next. Hypotheses are meant to be tested, not confirmed.

**Transition:** "Let's see how the Brief sections fill out for this scenario..."
-->

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

<!--
INSTRUCTOR NOTE:

**Background:** Attribution is one of the most contentious topics in marketing analytics. Billions of dollars are allocated based on attribution models, yet there's no objectively "correct" answer — just different ways of assigning credit. This is fundamentally different from funnel analysis, where conversion rates are facts. Attribution is a modeling choice.

**Key point:** Attribution is about assigning credit, not measuring truth. There's no objectively correct answer.

**Say something like:**
"Let me be clear upfront: attribution is different from the other analyses we'll cover.

In funnel analysis, conversion rates are facts. 61% of users completed checkout — that's a number you can calculate precisely.

In attribution, we're making modeling choices. A user saw a LinkedIn ad on Monday, clicked a Google ad on Friday, and bought on Sunday. Who gets credit for the sale?

There's no objectively correct answer. LinkedIn introduced them. Google reminded them. The product convinced them. All three contributed.

Attribution models are different ways of assigning credit. Last-touch gives all credit to Google. First-touch gives all credit to LinkedIn. Linear splits it evenly.

None of these is 'right.' They're different lenses. The question is: which lens is most useful for the decision you're making?"

**If asked:** "So which model should we use?"
A: Depends on the decision. For budget allocation, I recommend comparing multiple models and looking for channels where they disagree dramatically. That's where investigation is needed.

**Transition:** "First, let's define what a touchpoint is..."
-->

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

<!--
INSTRUCTOR NOTE:

**Background:** Last-touch is the default attribution model at most companies because it's simple to implement and explain. But it systematically overvalues "closer" channels (branded search, retargeting, direct) and undervalues awareness channels (display, social, content). This creates perverse incentives — cutting awareness channels looks good under last-touch but may hurt overall acquisition.

**Key point:** Last-touch is the default, but it systematically undervalues awareness channels. Be aware of the bias.

**Say something like:**
"Last-touch is what most companies use by default. It's simple: whoever touched the customer last before they converted gets 100% credit.

The SQL is straightforward — MAX timestamp grouped by user.

But here's the problem. Last-touch systematically overvalues closers. Who's typically the last touch? Branded search — someone types your company name into Google. Direct — they type your URL. Retargeting — they already visited, you reminded them.

These channels look amazing under last-touch. But think about it: if someone types your brand name into Google, they already knew about you. Who told them? Probably an awareness channel — a LinkedIn ad, a podcast mention, a friend's recommendation — that happened weeks earlier and doesn't get credit.

Last-touch tells you who closed the deal. It doesn't tell you who introduced the customer in the first place. If you cut all your awareness channels based on last-touch data, you might find that eventually nobody knows who you are and branded search volume drops."

**If asked:** "If it's so biased, why do companies use it?"
A: Convenience. It's easy to implement, easy to explain, and channels like Google Ads report last-touch by default. It takes deliberate effort to look at multi-touch.

**Transition:** "Let's look at a model that spreads credit more evenly..."
-->

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

<!--
INSTRUCTOR NOTE:

**Background:** This scenario illustrates a common B2B problem: long sales cycles where attribution is especially tricky. Someone reads a blog post in January, downloads a whitepaper in March, gets a sales call in May, and closes in June. Last-touch credits the sales call, but the content did the initial work.

**Key point:** B2B has long sales cycles where awareness channels contribute early and get no credit under last-touch.

**Say something like:**
"Let's look at a B2B scenario where attribution is especially tricky.

DataDash is a B2B analytics platform. They spend $2.4M per quarter across 6 channels. They use last-touch attribution — whatever most companies use by default.

The CMO suspects something's off. LinkedIn and content marketing don't get much credit, but qualitatively, customers keep saying 'I first heard about you from a blog post' or 'I saw you on LinkedIn.'

The hypothesis: LinkedIn and content are in more than 50% of deals as the first touch, but less than 5% of deals as the last touch. They're starting journeys that search and sales are closing.

This is classic B2B. Someone reads your blog post in January. Three months later, they search for your product category, click a branded search ad, and buy. Last-touch says 'Search gets all credit.' But search only worked because content built awareness months earlier."

**If asked:** "How long are typical B2B attribution windows?"
A: Often 90 days for enterprise sales, sometimes longer. The longer the window, the more you see awareness channels contributing.

**Transition:** "Let's look at the counter-metrics for this analysis..."
-->

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

<!--
INSTRUCTOR NOTE:

**Background:** This is the philosophical foundation for campaign effectiveness analysis. Many students (and professionals) conflate correlation with causation. The medicine example is intuitive and non-threatening — it's not about their work, so they can think clearly about the logic before applying it to marketing.

**Key point:** Correlation is not causation. To claim causation, you need a counterfactual.

**Say something like:**
"Before we talk about measuring campaign effectiveness, I need to introduce a concept that underpins everything: the 'What If' problem.

Here's a simple example. You have a headache. You take medicine. The headache goes away. Question: how do you know the medicine worked?

[Pause for answers]

The honest answer is: you don't. Maybe the medicine worked. Maybe the headache would have gone away on its own. Maybe you also drank water and that helped. Maybe you were stressed and then relaxed. You observed ONE outcome — headache gone — but you needed to compare it to a world where you didn't take the medicine. That world doesn't exist. You can't observe it.

This is the fundamental challenge of causal inference. In marketing: you ran a campaign and sales went up. Did the campaign cause the sales increase? Or would sales have gone up anyway? You can't directly observe the world where you didn't run the campaign."

**If asked:** "Can't we just compare to last year?"
A: That's one approach, but it assumes this year would have looked like last year without the campaign. New stores, economy, competitors — lots of things change. Year-over-year comparisons are a rough proxy, not a true counterfactual.

**Transition:** "Let me be more precise about what I mean by counterfactual..."
-->

---

## What is a Counterfactual?

A **counterfactual** is: *"What would have happened if we hadn't done X?"*

**The Twin Study Analogy:**
- Twin A takes drug → better in 3 days
- Twin B takes placebo → better in 5 days
- Difference (2 days) = **causal effect**

**The problem in marketing:** We don't have twins. We must *construct* a comparison group.

<!--
INSTRUCTOR NOTE:

**Background:** The counterfactual is the central concept in causal inference. The twin study analogy makes it concrete: if you had an identical twin who did everything the same except take the medicine, you could measure the true causal effect. In marketing, we don't have twins — we have to construct comparison groups that approximate what would have happened without the treatment.

**Key point:** A counterfactual is the hypothetical outcome if we hadn't intervened. We can't observe it directly — we have to estimate it.

**Say something like:**
"Let me give you a mental model for counterfactuals: the twin study.

Imagine you have an identical twin. Same genetics, same life, same everything. You both get a headache at the same moment. You take medicine, your twin takes a placebo. You feel better in 3 days, your twin in 5 days.

The difference — 2 days — is the causal effect of the medicine. You know it's causal because your twin controlled for everything else.

Now here's the problem in marketing: we don't have twins. We ran a campaign in all markets. We can't observe the parallel universe where we didn't run it.

So we have to construct a comparison group — a 'control twin' — that approximates what would have happened without the campaign. That's what the next few slides are about: different methods for building your control twin."

**If asked:** "Isn't year-over-year comparison good enough?"
A: It's a rough proxy, but assumes this year would look like last year. In reality, economy, competition, your own growth rate, seasonality — many things change. YoY is convenient but not a true counterfactual.

**Transition:** "Let me show you three ways to build a control twin..."
-->

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

<!--
INSTRUCTOR NOTE:

**Background:** These three methods form a hierarchy of rigor. Randomized holdout is best but requires planning ahead. Geo-matching is common but risky — markets may differ in unobservable ways. Synthetic control is sophisticated but data-intensive. Students should understand when each is appropriate.

**Key point:** The quality of your causal estimate depends on how good your "control twin" is.

**Say something like:**
"There are three main ways to build a control twin, and they form a hierarchy of rigor.

Randomized holdout is the gold standard. Before the campaign, you randomly assign some markets to not receive it. Because assignment is random, any difference you see afterward is causal. But this requires advance planning — if the campaign already ran everywhere, it's too late.

Geo-matching is what you do when you didn't plan ahead. You find markets that look similar — maybe Phoenix and Tucson have similar demographics and growth trends — and use one as control. The risk: 'similar' on observables doesn't mean similar on unobservables.

Synthetic control is more sophisticated. When no single market is a good match, you create a weighted combination of multiple markets that together match your treated market's pre-campaign trajectory. It's powerful but requires more data and expertise.

All three answer the same question: what would have happened without the campaign? But they answer it with different levels of confidence.

The key insight: your causal estimate is only as good as your control twin. Garbage control = garbage estimate."

**If asked:** "Which method should I use?"
A: Randomized holdout if you can plan ahead. Geo-matching for quick analysis when holdout wasn't done. Synthetic control when you have data but no good single control market.

**Transition:** "Let me show you the fundamental question we're trying to answer..."
-->

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

<!--
INSTRUCTOR NOTE:

**Background:** Pull-forward is one of the most common traps in campaign analysis. A promotion causes a spike during the campaign period, but sales drop afterward as people who would have bought anyway already made their purchase. The "incremental" lift is actually just time-shifted demand, not new demand. Holiday campaigns and promotional periods are especially susceptible.

**Key point:** Measure beyond the campaign period. A spike followed by a drop is pull-forward, not true incrementality.

**Say something like:**
"Here's a trap that catches even experienced analysts: pull-forward.

You run a campaign. Sales spike 30% during the campaign period. Everyone celebrates. But then the next month, sales drop 20% below normal.

What happened? You didn't create new demand. You pulled forward demand that was going to happen anyway. People who would have bought next month bought this month instead because of the promotion.

From a campaign measurement perspective, your 'incremental' revenue is much smaller than it looked — maybe even negative once you factor in the discount you gave.

This is especially common with holiday promotions, sales, and limited-time offers.

The fix: always measure beyond the campaign period. Compare campaign period PLUS post-period to the same timeframe last year. If the total is the same but it shifted earlier, that's pull-forward."

**If asked:** "How long should the post-period be?"
A: Depends on purchase frequency. For consumer goods bought monthly, measure at least 2-3 months after. For annual purchases, you might need to wait a full year.

**Transition:** "Let me show you a realistic scenario..."
-->

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

<!--
INSTRUCTOR NOTE:

**Background:** Unit economics became prominent during the 2010s tech boom when many startups grew at all costs, only to discover their customers weren't profitable. WeWork, Uber, and many others had terrible unit economics masked by growth. The 2022 market correction made CAC/LTV analysis suddenly important to investors and executives.

**Key point:** Growth without profitable unit economics is just burning money faster.

**Say something like:**
"This might be the most important question in business analytics: Does a customer generate more value than they cost to acquire?

If the answer is yes — LTV greater than CAC — you can scale profitably. Spend more on acquisition, get more customers, make more money. A virtuous cycle.

If the answer is no — LTV less than CAC — growth makes you poorer. Every new customer loses money. The more you grow, the more you lose.

And if they're roughly equal — you're on a treadmill. Running hard, going nowhere.

A lot of tech companies learned this the hard way in 2021-2022. They'd grown at all costs, raised funding based on growth rates, and then discovered their customers weren't actually profitable. [Pause] Some of those companies don't exist anymore.

Your job as an analyst is to answer this question honestly — even when the answer is uncomfortable."

**If asked:** "What's a good LTV:CAC ratio?"
A: Depends on the business. SaaS benchmarks are 3:1 or higher. E-commerce is often 2:1 to 3:1. The 'good' number depends on your cash flow needs and competitive dynamics.

**Transition:** "Let me define these terms precisely..."
-->

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

<!--
INSTRUCTOR NOTE:

**Background:** Most companies understate CAC by only counting media spend. "Fully loaded" CAC includes all costs of acquiring customers: media, creative, agency fees, team salaries, tools. The difference can be dramatic — in this example, $880 fully loaded vs. $500 media-only. This matters for unit economics and profitability analysis.

**Key point:** Fully loaded CAC includes all costs, not just media spend. The difference can be 50%+ higher than naive calculations.

**Say something like:**
"When you calculate CAC, don't just count media spend. That's the most common mistake.

Look at this table. Media spend is $500K — that's what shows up in Google Ads or Meta's dashboard. But what else did you pay for?

Creative production: the video shoot cost $50K. Agency fees: you pay a retainer. Team salaries: you have 4 people working on paid acquisition — some portion of their salary is acquisition cost. Tools: that attribution software isn't free.

Add it all up: $880K total for 1,000 customers = $880 CAC.

If you only counted media spend: $500K / 1,000 = $500 CAC.

That's a 76% difference! If your LTV is $750, you think you're profitable at $500 CAC but you're actually underwater at $880.

When your Brief asks for CAC, specify 'fully loaded.' And when you read someone else's CAC claims, ask what's included."

**If asked:** "How do I allocate team salaries to acquisition?"
A: Estimate the percentage of time spent on acquisition activities. If 50% of the marketing team's time is acquisition, allocate 50% of salaries. It's imprecise but better than ignoring it.

**Transition:** "Let's break this down by channel..."
-->

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

<!--
INSTRUCTOR NOTE:

**Background:** Cohort-based LTV tracking is more accurate than simple formulas because it measures actual user behavior over time. But it requires patience — you can only observe data you have. For newer cohorts, you extrapolate based on older cohorts' trajectories. This extrapolation is the source of most LTV calculation errors.

**Key point:** Cohort tracking is more accurate, but extrapolation is guessing. Always be conservative when projecting future LTV.

**Say something like:**
"Cohort-based LTV tracking is more accurate than simple formulas because you're measuring what users actually do, not what a formula predicts.

Look at this table. The January 2025 cohort has been around for 12 months, so we know their 12-month LTV: $480. The April cohort has only been around 6 months — we can see $235, but month 12 is a question mark.

To fill in that question mark, we extrapolate. If January cohort went from $270 at month 6 to $480 at month 12, that's a 78% increase. We might assume April cohort follows a similar curve: $235 × 1.78 = ~$418.

But here's the danger: extrapolation is guessing. Maybe April cohort came from a different marketing channel. Maybe the product changed. Maybe the economy shifted. Any number of things could make the future different from the past.

Rule of thumb: when projecting LTV, be conservative. If your optimistic projection says 3:1 LTV:CAC and your conservative projection says 1.8:1, plan for 1.8:1."

**If asked:** "How far out can we reasonably project?"
A: Depends on how much historical data you have and how stable the business is. Projecting 12 months from 6 months of data is reasonable. Projecting 36 months from 6 months is dangerous.

**Transition:** "Let me show you what these curves look like visually..."
-->

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

<!--
INSTRUCTOR NOTE:

**Background:** This is one of the most common mistakes in channel analysis — treating channels as independent when they're interconnected. It's the same causal inference problem we discussed earlier, but applied to channel relationships. The "halo effect" of awareness channels is real but hard to measure directly.

**Key point:** Channels interact. Cutting one may hurt others in ways that attribution doesn't capture.

**Say something like:**
"This is crucial. Channels don't work in isolation.

Let me give you a scenario. You analyze your channel economics and find paid social has a 0.9x LTV:CAC ratio — every dollar you spend, you lose 10 cents. Seems like an easy call: cut paid social.

So you cut it. What happens?

Brand awareness drops — fewer people see your ads, fewer people know you exist. Organic search volume decreases — people search for brands they've heard of. Referral slows — people don't recommend products they haven't heard of. Overall growth drops 40%.

What happened? Paid social wasn't just acquiring customers directly. It was building awareness that fed your other channels. The attribution system couldn't see this because it only measured direct conversions.

This is why the pre-mortem for MindfulApp is so important. They cut paid social based on channel economics and killed their growth. The analysis was correct — paid social's direct LTV:CAC was low — but it missed the indirect effects.

Before you make major channel cuts, run holdout tests. Turn off the channel in some markets and see what happens to OVERALL growth, not just that channel's attributed conversions."

**If asked:** "How do you measure the 'halo effect'?"
A: Holdout tests or market experiments. Turn off a channel in some geos and measure total outcome, not just attributed outcome. It's more work but it's the only way to know for sure.

**Transition:** "Let me show you a real scenario where this goes wrong..."
-->

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

<!--
INSTRUCTOR NOTE:

**Background:** This summary slide ties together the meta-lesson of Block 2: interaction effects are everywhere, and they're the most common source of analytics mistakes. Each pre-mortem in this block illustrated a different version of the same problem.

**Key point:** The common failure mode in acquisition analytics is treating things as independent when they interact.

**Say something like:**
"Before we break, I want you to notice a pattern. Look at the pre-mortems from this block.

Funnel analysis: We saw mobile conversion drop and 'fixed' mobile checkout, but users were browsing on mobile and buying on desktop. The devices interacted.

Attribution: We credited last-touch and undervalued LinkedIn, but LinkedIn was starting journeys that search was closing. The channels interacted.

Campaign effectiveness: We found great ROI but our control markets had a competitor enter. Treatment and control interacted with external factors.

CAC/LTV: We cut paid social and growth collapsed because paid social was feeding awareness that drove other channels. The channels interacted.

Every single failure was about interaction effects. Things don't work in isolation. This is why I keep emphasizing causal testing. Run holdouts. Do experiments. Don't make major decisions based on attribution alone — attribution is correlation, not causation."

**If asked:** "Is there a way to model all these interactions?"
A: Marketing mix modeling (MMM) tries to. But it's complex and requires a lot of data. For most decisions, simpler holdout tests work better.

**Transition:** "After break, we'll cover retention and growth analyses. Same pattern — we'll look at how things interact."
-->

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

