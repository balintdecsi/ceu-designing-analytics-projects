# Scenario 05: PetPal

## Company Overview

**PetPal** is a subscription box service for pet owners, delivering monthly boxes of toys, treats, and supplies. Founded in 2018, they've grown to serve 280,000 active subscribers across the US and Canada.

**Business Model:**
- Dog box: $35/month or $29/month annual plan
- Cat box: $32/month or $26/month annual plan
- Premium box (larger dogs, premium brands): $55/month
- Add-on marketplace: One-time purchases of items from past boxes

**Current Metrics:**
- 280,000 active subscribers (240,000 dogs, 40,000 cats)
- Monthly churn: 5.8% (monthly plans), 1.9% (annual plans)
- Average subscription length: 8.2 months
- Add-on marketplace: 22% of subscribers make additional purchases
- NPS: 52 (industry benchmark: 45)

---

## The Situation

PetPal's growth has plateaued. New subscriber acquisition costs have risen 40% in the past year due to increased competition (BarkBox, Chewy's subscription, Amazon Subscribe & Save).

The VP of Marketing, Jennifer Walsh, ran an experiment last quarter: a "Super Chewer" box variant for dogs who destroy toys quickly. The initial results were promising:
- 15,000 subscribers opted into Super Chewer
- Super Chewer monthly churn: 3.2% vs. 5.8% regular
- Super Chewer NPS: 68 vs. 52 regular

Jennifer wants to expand Super Chewer aggressively and create similar variants for other pet profiles. However, the Head of Operations, Carlos Mendez, is concerned. Super Chewer boxes cost 35% more to source and fulfill, but pricing is only 20% higher. He claims the economics don't work.

Meanwhile, customer support tickets have increased 25% in the past 6 months, primarily complaints about:
- Repeated items in boxes
- Items inappropriate for pet size
- Allergies not being considered

---

## Available Data

You have access to:

1. **Subscribers table**: subscriber_id, pet_type, pet_name, pet_size, pet_age, signup_date, plan_type, subscription_status, churn_date, churn_reason
2. **Boxes table**: box_id, subscriber_id, ship_date, box_type, items_included (JSON), fulfillment_cost
3. **Items table**: item_id, item_name, category (toy/treat/supply), brand, cost, size_appropriate (S/M/L/XL)
4. **Surveys table**: subscriber_id, survey_date, nps_score, item_ratings (JSON), comments
5. **Support tickets**: ticket_id, subscriber_id, ticket_date, category, resolution, resolution_time
6. **Add-on purchases**: purchase_id, subscriber_id, item_id, purchase_date, revenue

**Data quality notes:**
- Pet allergy information is only captured for ~40% of subscribers
- Churn reason is often missing or "Other"
- Item ratings in surveys are sparse (most people skip them)
- Fulfillment costs are estimates, not actuals

---

## Key Stakeholders

- **Jennifer Walsh (VP Marketing)**: Champions Super Chewer. Believes personalization is the future. Her budget depends on proving Super Chewer works.

- **Carlos Mendez (Head of Operations)**: Skeptical of Super Chewer economics. Concerned about supply chain complexity of multiple box variants.

- **Rachel Kim (Head of Product)**: Wants to understand personalization value. Proposing an AI-driven "perfect box" algorithm.

- **Customer Support Lead**: Frustrated by preventable complaints. Wants better data integration to avoid sending inappropriate items.

- **CEO**: Wants a clear strategy for differentiation against well-funded competitors. Preparing board presentation.

---

## Constraints

- Cannot change pricing during analysis (already communicated to customers)
- Supply chain commitments for next 3 months are locked
- Cannot survey churned customers (email opt-outs)
- Allergy data improvement requires product changes—out of scope for this analysis

---

## The Ask

The CEO wants a comprehensive analysis to inform product strategy. Specifically:

1. Is Super Chewer actually more profitable despite higher costs? What's the true LTV?
2. What percentage of churn is driven by personalization failures (wrong items, repeats, allergies)?
3. Should we invest in more box variants, better personalization algorithm, or focus elsewhere?

Carlos has privately said: "Jennifer's Super Chewer numbers look good because she's not accounting for the operational chaos it causes."

**Your deliverable:** Create a complete Analytics Project Brief for this analysis.
