---
marp: true
theme: default
paginate: true
header: 'ECBS5228A: Designing Analytics Projects'
footer: 'Block 4: Application & Practice'
---

<!-- _class: lead -->
<!-- _paginate: false -->
<!-- _header: '' -->
<!-- _footer: '' -->

# Designing Analytics Projects

## Block 4: Application & Practice

**Eduardo Arino de la Rubia**
January 12, 2026

---

## Welcome Back

Day 2 Agenda:

| Block | Time | Topic |
|-------|------|-------|
| **4** | 10:50–12:30 | Application & Practice *(you are here)* |
| | | *Lunch break* |
| **5** | 13:30–15:10 | Influence for Data Scientists |
| | | *Break* |
| **6** | 15:40–17:20 | Capstone Preparation & Closing |

Today is about **applying** what you learned on Day 1.

---

## Block 4 Overview

| Section | Time |
|---------|------|
| Q&A on Day 1 Content | 20 min |
| Deep Dive: A Complex Brief | 30 min |
| Group Exercise: Analysis Selection | 25 min |
| Timed Brief Practice | 10 min |
| Common Scoping Mistakes | 15 min |

---

<!-- _class: lead -->

# Part 1: Q&A on Day 1
### *(20 minutes)*

---

## Day 1 Recap: The Framework

**The Analytics Project Brief** — 10 sections:

| | |
|---|---|
| 1. Problem & Decision | 6. Success & Decision Criteria |
| 2. Metrics (Primary + Counter) | 7. Timeline |
| 3. Stakeholder Map | 8. Risks & Assumptions |
| 4. Methodology | 9. Ethics & Privacy |
| 5. Scope & Deliverables | 10. Pre-Mortem |

---

## Day 1 Recap: The Analyses

**Acquisition (Block 2):** Funnel (where lose them?) → Attribution (which channels?) → Campaign (did spend work?) → CAC/LTV (worth the cost?)

**Retention & Growth (Block 3):** Retention (come back?) → Power User (who matters?) → Failure (what's broken?) → Expansion (how grow?) → Ecosystem (products interact?)

---

## Questions from the Long Weekend?

> **Open floor (15 min):**
>
> What questions came up as you reflected on Day 1?

<!--
INSTRUCTOR NOTE:
Take 4-5 questions. Common ones:
- "How do I choose between analyses?"
- "What if I don't have the data?"
- "How detailed should the Brief be?"
- "What's the difference between guardrail and tradeoff?"

If no questions, prompt: "What was most surprising about Day 1?"
-->

---

## Quick Clarifications

**Q: How long should a Brief take to complete?**
A: 30-60 minutes once practiced. First few times, longer.

**Q: What if I can't fill out a section?**
A: That's valuable information. "Unknown" or "To be determined" is honest. Blank is not.

**Q: Do I need all 9 analyses?**
A: No. Most projects use 2-3. The Brief's methodology section forces you to justify your choice.

---

<!-- _class: lead -->

# Part 2: Deep Dive — A Complex Brief
### *(35 minutes)*

---

## Why Deep Dive?

Day 1 showed you Brief sections in isolation.

Now let's see how they **connect** in a complete, realistic example.

We'll walk through one Brief end-to-end and discuss:
- What makes it strong?
- What would you change?
- How do sections reference each other?

---

## The Scenario: MindfulApp

**Company:** MindfulApp (meditation & wellness app)
**Problem:** Growing 40% YoY but burning $8M/quarter
**Question:** Are we acquiring customers profitably? Should we scale or fix?

Let's walk through their CAC/LTV Brief section by section.

---

## Section 1: Problem & Decision

| Element | MindfulApp |
|---------|------------|
| **Business question** | Are we acquiring customers profitably by channel? |
| **Who's asking** | Series B investors (path to profitability) |
| **Decision maker** | Board of Directors |
| **Hypothesis** | Organic/referral >5x LTV:CAC; paid social ~1.2x |

**Discussion:** Why does "who's asking" matter here?

<!--
INSTRUCTOR NOTE:
Looking for: Investors have specific expectations (benchmarks).
Board context means this is high-stakes.
Timeline is probably tied to fundraising.
-->

---

## Section 2: Metrics

**Primary Metric:**
> LTV:CAC Ratio by Channel — (12-month projected LTV) / (Fully-loaded CAC), by acquisition source

**Counter-Metrics:**

- **Growth rate** (Tradeoff) — Cutting unprofitable channels slows growth
- **Engagement quality** (Guardrail) — Cheap users may not engage
- **Brand awareness** (Tradeoff) — Paid builds awareness even with low direct ROI

**Discussion:** Why is growth rate a "tradeoff" not a "guardrail"?

---

## Section 3: Stakeholders

| | High Interest | Low Interest |
|---|---|---|
| **High Power** | CEO, CFO, Board | CTO |
| **Low Power** | Head of Growth, Paid team | Product, Engineering |

**Blocker:** Paid acquisition team — if paid social looks bad, their team shrinks from 4 to 2.

**Discussion:** How does knowing this blocker change how you present findings?

<!--
INSTRUCTOR NOTE:
Looking for: Present scenarios not verdicts.
Private conversation before broad share.
Frame as "tradeoffs leadership must decide" not "paid team failed."
-->

---

## Section 4: Methodology

**Cohort-based LTV modeling**
Predict lifetime value from early behavior. Needs: subscription history.

**Fully-loaded CAC by channel**
True acquisition cost. Needs: marketing spend, team allocation.

**Payback period analysis**
Months to recover CAC. Needs: monthly revenue by cohort.

**Discussion:** Why "fully-loaded" CAC? What gets missed if you just count media spend?

---

## Section 5: Scope

**In Scope:**
- 5 channels (Paid Social, Paid Search, Organic, Referral, Influencer)
- Cohorts from last 18 months
- Monthly and annual subscribers

**Out of Scope:**
- Free tier users
- B2B partnerships
- Reactivated churned users

**Discussion:** Why exclude free tier users? Is that the right call?

<!--
INSTRUCTOR NOTE:
Looking for: Free users have different economics.
Including them would muddy the paid subscriber analysis.
Could be a separate analysis.
-->

---

## Section 6: Success & Decision Criteria

**Decision Criteria:**

| If we find... | We will... |
|---------------|------------|
| All channels >3x | Scale aggressively |
| Mixed (some >3x, some <2x) | Reallocate from low to high |
| Most channels <2x | Fix retention before scaling |
| Referral is 5x+ but tiny | Invest $500K in referral program |

**Discussion:** Why include the "inconclusive" outcome?

---

## Section 7-9: Timeline, Risks, Ethics

**Timeline:** 4 weeks (data → findings → board-ready)

**Key Risk:** LTV projections too optimistic
**Mitigation:** Use conservative retention curves, show sensitivity

**Ethics:** PII required (user-level data), no bias risk, GDPR compliant

**Discussion:** What could invalidate the LTV projections?

<!--
INSTRUCTOR NOTE:
Looking for: Product changes, pricing changes, competitor entry,
economic shifts, cohort composition changes
-->

---

## Section 10: Pre-Mortem

> We showed paid social had 1.5x LTV:CAC and recommended cutting 60% of spend.
>
> Growth slowed from 40% to 15%.
>
> Turns out paid social drove awareness that boosted organic and referral — channels weren't independent.

**Discussion:** How could they have caught this before recommending the cut?

---

## How Sections Connect

The Brief isn't 10 independent sections. They reference each other:

- **Methodology** must answer the **Problem**
- **Counter-metrics** anticipate **Pre-mortem** scenarios
- **Stakeholder blockers** inform **how you present findings**
- **Decision criteria** prevent analysis-paralysis

---

## What Makes This Brief Strong?

1. **Specific metric definition** — Not just "LTV:CAC" but fully specified
2. **Counter-metrics with types** — Guardrail vs. tradeoff is clear
3. **Named blocker with motivation** — "Jobs on the line" is concrete
4. **Decision criteria include null result** — What if we find nothing?
5. **Pre-mortem is specific** — Not generic "something went wrong"

---

## What Would You Change?

> **Discussion (3 min):**
>
> Looking at this Brief, what's missing or could be stronger?

<!--
INSTRUCTOR NOTE:
Possible answers:
- No sensitivity analysis specified for LTV projections
- Doesn't address channel interaction explicitly in methodology
- Timeline might be aggressive for board-quality work
- Could specify action thresholds more precisely
-->

---

<!-- _class: lead -->

# Part 3: Group Exercise — Analysis Selection
### *(30 minutes)*

---

## The Exercise

You'll see 3 business scenarios.

For each one:
1. **Which foundational analyses apply?** (Pick 2-3)
2. **Why those analyses?** (Justify your choice)
3. **What's the primary metric?** (Be specific)

Work in groups of 3-4. You'll present and defend your choices.

---

## Scenario A: StreamBox

**Company:** StreamBox (music streaming service)
**Situation:** Premium subscriber growth is flat. Free tier is growing but not converting. Marketing spend is up 30% but results aren't scaling.

**The ask from the CMO:** "Help me understand what's working and what's not in our growth engine."

> **Your task:** Which 2-3 analyses? Why? What primary metric?

---

## Scenario A: Discussion

> **Groups share (5 min):**
>
> What analyses did you choose? Why?

<!--
INSTRUCTOR NOTE:
Reasonable answers:
- CAC/LTV (are we acquiring profitably?)
- Funnel (where are free users dropping off before premium?)
- Expansion/Monetization (what triggers free→paid conversion?)
- Attribution (which channels are working?)

Push back on any answer — "Why not [X] instead?"
-->

---

## Scenario B: QuickShip

**Company:** QuickShip (e-commerce logistics)
**Situation:** Customer complaints about delivery failures have tripled in 6 months. NPS dropped from 45 to 28. Operations says "it's not us, it's the carriers."

**The ask from the COO:** "Figure out what's actually going wrong and who's responsible."

> **Your task:** Which 2-3 analyses? Why? What primary metric?

---

## Scenario B: Discussion

> **Groups share (5 min):**
>
> What analyses did you choose? Why?

<!--
INSTRUCTOR NOTE:
Reasonable answers:
- Failure Analysis (categorize why deliveries fail — carrier? address? inventory?)
- Funnel (where in the delivery process do failures occur?)
- Retention (are affected customers churning?)

Key insight: This is exploratory — they don't know the root cause.
Failure Analysis is the right starting point.
-->

---

## Scenario C: FinTrack

**Company:** FinTrack (personal finance app)
**Situation:** App has 3 products: Budgeting, Investing, and Credit Score. Each team optimizes independently. CEO suspects "we're leaving money on the table by not connecting these."

**The ask from the CEO:** "Should we invest in cross-product features? Is there synergy?"

> **Your task:** Which 2-3 analyses? Why? What primary metric?

---

## Scenario C: Discussion

> **Groups share (5 min):**
>
> What analyses did you choose? Why?

<!--
INSTRUCTOR NOTE:
Reasonable answers:
- Ecosystem Analysis (complement vs. substitute?)
- Power User (are multi-product users more valuable?)
- Retention (do multi-product users retain better? Is it causal?)

Key pushback: Selection bias! Multi-product correlation ≠ causation.
-->

---

## Debrief: Why Reasonable People Disagree

There's no single "right" answer to analysis selection.

It depends on:
- **What data is available**
- **What decisions need to be made**
- **What's the timeline**
- **What's been tried before**

The Brief framework forces you to **justify** your choice, not just make it.

---

<!-- _class: lead -->

# Timed Brief Practice
### *(10 minutes)*

---

## Your Assignment Preview

On Thursday, you'll receive a unique 2-page scenario. You'll complete a full Brief.

Right now, you'll practice **under time pressure**. This is what Part C of the exam feels like.

**Ready?**

---

## Timed Exercise (10 minutes)

**Use the StreamBox scenario from the previous exercise.**

Write these sections:
1. **Primary Metric** — Full operational definition (2 min)
2. **One Counter-Metric** — Label as Guardrail or Tradeoff, explain why it could break (3 min)
3. **One Blocker** — Name the role, their motivation to resist, and your mitigation (3 min)

**Work alone. Timer starts now.**

<!--
INSTRUCTOR NOTE:
Set a visible 10-minute timer.
Walk around but don't answer questions — this simulates exam conditions.
After 10 min: "Pens down. How did that feel?"
-->

---

## Timed Exercise Debrief

> **Quick share (2 min):**
>
> How did that feel? What was hardest under time pressure?

<!--
INSTRUCTOR NOTE:
Common struggles:
- Metric precision takes longer than expected
- Hard to justify counter-metric quickly
- Blocker motivation requires scenario re-reading

Key message: "This is why you practice. Your assignment is Thursday."
-->

---

<!-- _class: lead -->

# Part 4: Common Scoping Mistakes
### *(15 minutes)*

---

## Mistake 1: Vague Metrics

❌ **Bad:** "Improve user engagement"

✅ **Good:** "Increase D7 retention (users with ≥1 `app_open` on day 7 / users who `signup_complete` on day 0) from 35% to 42%"

**The test:** Can you write the SQL? If not, it's not defined.

---

## Mistake 2: Missing Counter-Metrics

❌ **Bad:** Only tracking the primary metric

✅ **Good:** Identifying 2-3 things that could break

**Example:** You optimize checkout conversion. AOV drops 15%, fraud triples. You "won" on conversion but lost overall.

**The test:** What could go wrong if you succeed? If you can't answer, you haven't thought hard enough.

---

## Mistake 3: Stakeholder Blind Spots

❌ **Bad:** "We'll present to the leadership team"

✅ **Good:** Named stakeholders with power, interest, and motivation

**The killer:** The blocker you didn't identify who kills your project in a meeting you weren't invited to.

**The test:** Who has veto power? Who might resist? Why?

---

## Mistake 4: Scope Creep

❌ **Bad:** "We'll also look at [tangentially related thing]"

✅ **Good:** Explicit "Out of Scope" section

**Warning signs:**
- "While we're at it..."
- "It would be easy to also..."
- "Leadership asked if we could add..."

**The test:** Does adding this help the decision we're trying to inform? If not, it's out of scope.

---

## Mistake 5: No Decision Criteria

❌ **Bad:** "We'll analyze and see what we find"

✅ **Good:** "If we find X, we'll do Y. If we find Z, we'll do W."

**Including the null result:** What if you find nothing conclusive?

**The test:** Before you start, do you know what actions different findings would trigger?

---

## Mistake 6: Correlation as Causation

❌ **Bad:** "Users who do X retain better, so we should make everyone do X"

✅ **Good:** "Users who do X retain better. We recommend A/B testing whether forcing X improves retention."

**The trap:** Engaged users do everything. Forcing behavior on disengaged users rarely works.

**The test:** Is this correlation or causation? How would we know?

---

## The Meta-Mistake

All these mistakes share a root cause:

> **Starting analysis before finishing the Brief.**

The Brief exists to surface these issues **before** you waste time.

30 minutes of scoping saves 30 hours of wrong analysis.

---

## Block 4 Summary

| Section | Key Takeaway |
|---------|--------------|
| **Q&A** | Questions are valuable — gaps in understanding surface |
| **Deep Dive** | Brief sections connect; they're not independent |
| **Analysis Selection** | Reasonable people disagree; justify your choice |
| **Common Mistakes** | Brief prevents these; fill it out *before* you analyze |

---

## Questions Before Lunch?

<!--
INSTRUCTOR NOTE:
Take 2-3 questions max.
End on time — lunch break matters for afternoon energy.
-->

---

<!-- _class: lead -->
<!-- _paginate: false -->

# Lunch Break!

**Block 5 starts at 13:30**

Influence for Data Scientists

