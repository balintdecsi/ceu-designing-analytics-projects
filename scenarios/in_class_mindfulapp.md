# In-Class Scenario: MindfulApp

> **FOR CLASS DISCUSSION ONLY**
>
> This scenario is used during Block 4 for the deep dive exercise on CAC/LTV analysis.
> It is NOT a student assignment scenario. Student assignments use the numbered
> scenarios (scenario_01 through scenario_18).

---

## Company Overview

**MindfulApp** is a meditation and wellness app competing in the same space as Calm and Headspace. Founded in 2019, the company has grown rapidly and recently closed its Series B funding round.

**Business Model:**
- Free tier: Basic meditation library, limited sleep sounds, 7-day beginner course
- Premium ($12.99/month or $69.99/year): Full meditation library, personalized recommendations, multi-week guided programs, sleep stories, offline downloads, family sharing

**Current Metrics:**
- Subscriber growth: 40% year-over-year
- Quarterly burn rate: $8M/quarter
- Funding stage: Series B (just closed)
- Channels: Paid Social, Paid Search, Organic/SEO, Referral, Influencer

---

## The Situation

MindfulApp just closed its Series B round. The growth numbers look great—40% YoY subscriber growth—but the burn rate is concerning at $8M per quarter. The Series B investors are asking a pointed question: **Are we acquiring customers profitably, or are we buying growth that will never pay back?**

The CEO, Jamie Park, needs to present at the next board meeting in 6 weeks. The board wants to understand:

1. What is the LTV:CAC ratio by acquisition channel?
2. Should we scale acquisition spend aggressively, or fix unit economics first?

There's internal disagreement. The Head of Growth, Alex Rivera, believes organic and referral users are highly profitable (LTV:CAC > 5x) while paid social users are marginal (~1.2x). Alex wants to shift investment toward the referral program. But the paid acquisition team—currently 4 people—has a different view. They argue that paid social drives awareness that lifts organic and referral, even if direct attribution looks weak.

---

## Available Data

You have access to:

1. **Users table**: user_id, signup_date, acquisition_source (from Adjust), device_type, country
2. **Subscriptions table**: user_id, subscription_start, subscription_end (null if active), plan_type (monthly/annual), price_paid
3. **Marketing spend table**: date, channel, spend_amount
4. **Events table**: user_id, event_timestamp, event_type (meditation_complete, session_start, feature_used, etc.)

**Data quality notes:**
- Adjust attribution is reliable for ~90% of users
- Subscription events are logged without gaps (can reconcile to billing)
- Marketing spend by channel is available, but overhead allocation (salaries, tools, creative production) is partial—will need to work with finance
- Cohorts from the last 18 months are available

---

## Key Stakeholders

- **Jamie Park (CEO)**: Needs to present to the board. Champions this analysis—needs clear data to make the case either way. Success = board accepts the methodology and findings.

- **Morgan Chen (CFO)**: Cost-focused. Skeptical of "brand awareness" arguments without hard data. Wants to see fully-loaded CAC (not just media spend).

- **Board of Directors**: Decision makers. One board member previously ran a consumer app and has strong priors about "acceptable" LTV:CAC ratios (3:1 minimum). They'll push back if methodology seems soft.

- **Alex Rivera (Head of Growth)**: Champions this analysis. Believes organic/referral are underinvested. Wants data to restructure the marketing budget.

- **Paid Acquisition Team (4 people)**: Potential blockers. If paid social looks bad, their team of 4 shrinks to 2. Jobs are on the line. They'll argue that attribution doesn't capture awareness value.

---

## Constraints

- The analysis must be board-ready within **6 weeks**
- Overhead allocation data is partial—need to coordinate with finance
- You cannot run new experiments for this analysis—must use historical data
- Monthly and annual subscribers should both be included
- Free tier users are **out of scope**—this analysis is about paid subscriber economics only
- B2B partnerships and reactivated churned users are out of scope

---

## The Ask

The CEO has requested an analysis to answer:

1. **What is the true LTV:CAC ratio by channel?** (Using fully-loaded CAC, not just media spend)
2. **Which channels should receive more investment in Q2? Which should receive less?**
3. **Should we scale acquisition spend or fix unit economics first?**

The Head of Growth has privately noted: "Make sure the analysis considers that channels might not be independent. If we cut paid social and organic drops, we'll have made a very expensive mistake."

**Your deliverable:** Create a complete Analytics Project Brief for this analysis.

---

## Reference

See the completed Analytics Project Brief for this scenario:
[`templates/examples/brief_04_cac_ltv.md`](../templates/examples/brief_04_cac_ltv.md)
