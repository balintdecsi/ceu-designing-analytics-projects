# Scenario 15: HomeValue AI

## Company Overview

**HomeValue AI** provides automated property valuation models to mortgage lenders, real estate investors, and insurance companies. Their machine learning models estimate property values using public records, satellite imagery, and market data. Founded in 2020, they've grown to serve 45 financial institution clients.

**Business Model:**
- API-based pricing: $2-15 per valuation depending on volume and data depth
- Annual contracts: Minimum commitments with usage tiers
- Custom models: Premium pricing for client-specific model tuning
- Data licensing: Historical valuation data for research purposes

**Current Metrics:**
- 45 active clients
- 8.2 million valuations/month
- Annual contract value (ACV) range: $50K - $2.4M
- Median ACV: $185K
- Gross retention: 88%
- Net retention: 105%

---

## The Situation

HomeValue AI's valuation accuracy is being questioned. A major mortgage lender client ran an internal audit and found that HomeValue predictions deviated from eventual sale prices by more than 10% in 18% of cases. The industry standard is <10% deviation in 90% of cases.

The VP of Data Science, Dr. Sarah Chen, believes the problem is geographic. The model performs well in data-rich markets (California, Texas, Florida) but poorly in rural and tertiary markets where training data is sparse.

The VP of Sales, Robert Garcia, is worried. Two clients have raised concerns after seeing similar audits. If HomeValue can't demonstrate improvement, $1.8M in renewals (3 clients) are at risk in the next quarter.

Meanwhile, a competitor launched a hybrid model that combines AI with human appraisers for edge cases. The CEO, Amanda Wright, wonders if HomeValue should do the same, but it would dramatically increase costs and slow down the core value proposition (instant valuations).

---

## Available Data

You have access to:

1. **Valuations table**: valuation_id, property_id, client_id, valuation_date, predicted_value, confidence_score, model_version
2. **Properties table**: property_id, address, property_type, square_feet, lot_size, year_built, bedrooms, bathrooms, county, state
3. **Sale outcomes**: property_id, sale_date, sale_price (available for subset that eventually sold)
4. **Client usage**: client_id, month, valuations_requested, use_case (mortgage/investment/insurance)
5. **Model performance**: model_version, region, property_type, mean_absolute_error, percent_within_10pct
6. **Client health**: client_id, month, health_score, risk_flag, notes

**Data quality notes:**
- Sale outcomes only available for 22% of valued properties (most never sell)
- Public records have lag (2-6 months depending on county)
- Property features may be outdated (renovations not captured)
- Client-specific model tuning makes cross-client comparison difficult

---

## Key Stakeholders

- **Dr. Sarah Chen (VP Data Science)**: Wants investment in data acquisition and model improvements. Believes accuracy is a solvable technical problem.

- **Robert Garcia (VP Sales)**: Wants fast solution for at-risk clients. Considering custom model tuning or pricing concessions.

- **Amanda Wright (CEO)**: Weighing hybrid model option. Concerned about competitive positioning.

- **At-risk clients**: Three lenders with 75+ accuracy complaints. Need reassurance or will churn.

- **Board of Directors**: AI company with accuracy problems = existential risk narrative. Want this resolved.

---

## Constraints

- Cannot access ground truth for most valuations (properties don't sell)
- Custom model tuning is labor-intensive (3-4 weeks per client)
- Hybrid model would require hiring appraisers (6-month ramp)
- Some clients share data back; others don't (inconsistent feedback loop)

---

## The Ask

The CEO wants an analytical framework to address the accuracy crisis. Specifically:

1. Where does the model actually underperform? Is it geography, property type, or something else?
2. What's the true accuracy when measured properly? Is the client's audit methodology fair?
3. Should we invest in model improvement, hybrid approach, or something else?
4. How do we save the at-risk clients in the next 60 days?

Robert has privately said: "Sarah's team keeps saying 'we need more data.' But we're losing clients now. We need a solution, not a research project."

**Your deliverable:** Create a complete Analytics Project Brief for this analysis.
