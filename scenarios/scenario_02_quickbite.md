# Scenario 02: QuickBite

## Company Overview

**QuickBite** is a ghost kitchen company operating in 12 US cities. They operate 45 "dark kitchens"—commercial kitchens with no dine-in service—that prepare food for delivery through third-party apps (DoorDash, Uber Eats, Grubhub) and their own app.

**Business Model:**
- Multiple virtual brands per kitchen (Italian, Asian, American, Mexican)
- Orders via third-party apps (65%) and owned app (35%)
- Average order value: $28 (third-party) vs. $34 (owned app)
- Take rate: Keep 70% on owned app, 55% on third-party after fees

**Current Metrics:**
- 180,000 orders/month across all kitchens
- $5.1M monthly GMV (gross merchandise value)
- Owned app: 45,000 registered users, 12,000 monthly orderers
- Customer acquisition cost (owned app): $18
- Repeat order rate (within 30 days): 22%

---

## The Situation

QuickBite's unit economics are barely profitable. The CEO, James Whitmore, believes the path to profitability is shifting more volume to the owned app (higher margins) and increasing order frequency.

Three months ago, they launched a loyalty program on the owned app:
- Earn 1 point per $1 spent
- 100 points = $5 off next order
- Free delivery for orders over $25

Early results are mixed. Loyalty program members order 40% more frequently than non-members, but the CFO, Angela Martinez, is concerned that the program is cannibalizing margin without driving incremental orders.

Meanwhile, the Operations team is struggling with quality consistency. Negative reviews mentioning "cold food" or "long wait times" have increased 35% in the past quarter. The Head of Operations, David Park, insists the problems are isolated to 5-6 kitchens and shouldn't affect company-wide strategy.

---

## Available Data

You have access to:

1. **Orders table**: order_id, user_id, kitchen_id, order_timestamp, platform (owned/doordash/ubereats/grubhub), brand, subtotal, discount_amount, delivery_fee, tip
2. **Users table**: user_id, signup_date, signup_source, loyalty_member (boolean), loyalty_points_balance, city
3. **Kitchen table**: kitchen_id, city, open_date, capacity_orders_per_hour, brands_offered
4. **Reviews table**: order_id, platform, rating (1-5), review_text, review_timestamp
5. **Loyalty transactions**: user_id, transaction_date, points_earned, points_redeemed, order_id

**Data quality notes:**
- Third-party platform orders don't have user_id (can only be matched if they also use owned app)
- Reviews are only available for ~30% of orders
- Kitchen operational metrics (prep time, delivery time) are logged but inconsistent

---

## Key Stakeholders

- **James Whitmore (CEO)**: Wants to prove owned-app strategy is working. Optimistic about loyalty program. Presenting to the board in 5 weeks.

- **Angela Martinez (CFO)**: Skeptical of loyalty program economics. Wants to see proof it drives incremental revenue, not just rewards existing behavior.

- **David Park (Head of Operations)**: Defensive about quality issues. Claims the "bad kitchens" are being fixed and shouldn't affect strategic decisions.

- **Sarah Liu (VP Marketing)**: Owns the loyalty program. Her team spent 6 months building it. She believes the 40% frequency lift proves it works.

- **Board of Directors**: Questioning path to profitability. Comparing QuickBite unfavorably to competitors with stronger repeat rates.

---

## Constraints

- Cannot access individual-level data from third-party platforms (only aggregate)
- Loyalty program has only been live for 3 months—limited data history
- Cannot change loyalty program structure during analysis period
- Kitchen-level operational data is messy and requires significant cleaning

---

## The Ask

The CEO wants a comprehensive analysis to present at the board meeting. Specifically:

1. Is the loyalty program driving incremental revenue, or just rewarding behavior that would have happened anyway?
2. Which kitchens are underperforming, and what's the financial impact of quality issues?
3. What's the true customer lifetime value on the owned app vs. third-party platforms?

Angela has privately told you: "James loves this loyalty program. I need an objective analysis, even if the answer isn't what he wants to hear."

**Your deliverable:** Create a complete Analytics Project Brief for this analysis.
