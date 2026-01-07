# Scenario 09: CargoFlow

## Company Overview

**CargoFlow** is a freight logistics platform connecting shippers with trucking carriers. They operate a two-sided marketplace where companies can post loads and carriers can bid on them. Founded in 2018, they've grown to become a mid-sized player in the US freight market.

**Business Model:**
- Transaction fee: 12% of load value (split between shipper and carrier)
- Subscription tier for carriers: $199/month for priority matching and fuel discounts
- Subscription tier for shippers: $499/month for dedicated capacity guarantees
- Factoring services: Advance payment to carriers for 3% fee

**Current Metrics:**
- 8,500 active carriers (at least 1 load/month)
- 1,200 active shippers
- 42,000 loads/month
- Average load value: $1,850
- Gross merchandise value: $78M/month
- Take rate: 11.2% (after discounts)

---

## The Situation

CargoFlow is caught between two challenges: carrier churn and shipper concentration.

**Carrier problem**: Monthly carrier churn is 8.2%, meaning they need to recruit ~700 new carriers/month just to stay flat. Recruiting costs are $380/carrier. The top complaint from churning carriers: "Not enough loads in my region."

**Shipper problem**: The top 50 shippers (4% of accounts) represent 65% of load volume. When any top shipper reduces volume, the whole marketplace suffers. Last quarter, a major shipper moved 40% of their loads to a competitor, and regional carriers saw load availability drop 25%.

The VP of Supply (carriers), Marcus Williams, wants to invest in carrier retention: better app, fuel discounts, faster payment. The VP of Demand (shippers), Sarah Chen, wants to focus on shipper diversification: more mid-market shippers, even if they're lower volume.

The marketplace dynamics are complex. More carriers = more competition = lower prices for shippers. But if prices drop too much, carriers leave. Finding the balance is critical.

---

## Available Data

You have access to:

1. **Carriers table**: carrier_id, company_name, fleet_size, home_region, signup_date, subscription_status, churn_date
2. **Shippers table**: shipper_id, company_name, industry, signup_date, subscription_status
3. **Loads table**: load_id, shipper_id, carrier_id, origin_region, dest_region, post_date, accept_date, delivery_date, price
4. **Bids table**: bid_id, load_id, carrier_id, bid_amount, bid_time, accepted (boolean)
5. **Carrier activity**: carrier_id, date, loads_viewed, bids_placed, loads_completed
6. **Shipper activity**: shipper_id, date, loads_posted, loads_filled, avg_time_to_fill

**Data quality notes:**
- Carrier fleet size is self-reported and often outdated
- Churn reason is only captured for ~35% of churned carriers
- Some carriers operate under multiple accounts (estimated 5% duplication)
- Shipper industry classification is inconsistent

---

## Key Stakeholders

- **Marcus Williams (VP Supply)**: Owns carrier relationships. Believes carrier experience is the bottleneck. Wants budget for app improvements and financial products.

- **Sarah Chen (VP Demand)**: Owns shipper relationships. Believes diversification reduces platform risk. Wants sales team expansion.

- **CFO**: Concerned about CAC for both sides. Questions whether subscription tiers are priced correctly.

- **Carrier Advisory Council**: Group of top carriers who provide feedback. Vocal about payment speed and load availability.

- **Board of Directors**: Worried about concentration risk. Recent competitor fundraise increased pressure to grow faster.

---

## Constraints

- Cannot significantly change pricing without carrier council approval (political constraint)
- Sales team for mid-market shippers would take 6 months to build
- Carrier app redesign is 4 months out regardless of analysis
- Regional load data has privacy limitations (can show aggregates, not individual routes)

---

## The Ask

The CEO wants a strategic recommendation on marketplace investment priorities. Specifically:

1. What drives carrier churn? Is it load availability, pricing, experience, or something else?
2. How much risk does shipper concentration create? What's the impact if another top-50 shipper leaves?
3. Should we invest in carrier retention (Marcus) or shipper diversification (Sarah)?
4. Are our subscription tiers priced correctly for the value they deliver?

Marcus has privately said: "Sarah's team loses a big shipper and suddenly we all suffer. We need to fix the carrier side—that's what we control."

**Your deliverable:** Create a complete Analytics Project Brief for this analysis.
