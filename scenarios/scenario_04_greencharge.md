# Scenario 04: GreenCharge

## Company Overview

**GreenCharge** operates a network of electric vehicle (EV) charging stations across Western Europe. Founded in 2020, they've grown to 2,400 charging points in 8 countries. The company focuses on "destination charging"—locations where drivers spend time anyway (shopping centers, hotels, office parks).

**Business Model:**
- Per-kWh charging fees (€0.35-0.55/kWh depending on location and speed)
- Monthly subscription: €12.99/month for 15% discount on all charging
- B2B partnerships: Revenue share with host locations (shopping centers, hotels)

**Current Metrics:**
- 2,400 charging points across 340 locations
- 185,000 registered app users
- 28,000 monthly subscribers
- 1.2M charging sessions/month
- Average session: 45 kWh, €19.80 revenue
- Station utilization: 18% average (varies widely by location)

---

## The Situation

GreenCharge is facing a critical decision. They have €15M allocated for expansion, but the board is divided on strategy:

**Option A**: Expand into 3 new countries (Poland, Czech Republic, Portugal)
**Option B**: Densify the network in existing countries (add more stations in proven locations)
**Option C**: Focus on improving utilization at existing underperforming stations

The CEO, Lars Bergström, favors Option A for growth narrative. The COO, Maria Santos, prefers Option B, arguing that network density drives user loyalty. The CFO, Thomas Mueller, is pushing Option C, claiming that 40% of stations are operating below breakeven utilization.

Recent data shows concerning patterns:
- 35% of stations have <10% utilization
- Users in areas with more GreenCharge stations use the network 2.5x more
- Subscriber churn increased from 4% to 7% monthly after a competitor entered the German market

---

## Available Data

You have access to:

1. **Stations table**: station_id, location_id, country, city, location_type (mall/hotel/office/other), charger_speed (kW), installation_date, monthly_rent_cost
2. **Sessions table**: session_id, station_id, user_id, start_time, end_time, kwh_delivered, revenue, payment_method
3. **Users table**: user_id, signup_date, country, car_model, subscription_status, subscription_start
4. **Locations table**: location_id, partner_name, revenue_share_pct, foot_traffic_estimate, parking_spaces
5. **Competitor stations**: latitude, longitude, operator, charger_speed (scraped from public APIs, updated monthly)

**Data quality notes:**
- Foot traffic estimates are provided by partners and may be inflated
- Competitor data has 2-3 week lag and may be incomplete
- Session data is clean but some sessions have missing user_id (guest charging)
- Subscription cancellation reasons are not captured

---

## Key Stakeholders

- **Lars Bergström (CEO)**: Wants aggressive growth story for next fundraise. Believes "be everywhere" is the winning strategy.

- **Maria Santos (COO)**: Focused on operational efficiency. Believes density in existing markets creates competitive moat.

- **Thomas Mueller (CFO)**: Concerned about cash burn. Wants to fix underperforming stations before building new ones.

- **Country Managers (8)**: Each wants expansion in their territory. May resist data showing their stations underperform.

- **Board of Directors**: Split between growth and efficiency. Expecting a data-driven recommendation.

---

## Constraints

- Expansion analysis must be ready for board meeting in 4 weeks
- Cannot get user-level data from competitors (only station locations)
- Country-specific regulations affect pricing and partnership structures
- €15M budget is fixed—cannot recommend "all of the above"

---

## The Ask

The board wants a data-driven recommendation for the €15M expansion budget. Specifically:

1. What drives station profitability? Which station types/locations should we prioritize?
2. Does network density actually improve user retention and usage? What's the evidence?
3. Where should the €15M go: new countries, densification, or fixing existing stations?

Thomas has privately noted: "Lars is emotionally attached to the expansion narrative. We need objective analysis."

**Your deliverable:** Create a complete Analytics Project Brief for this analysis.
