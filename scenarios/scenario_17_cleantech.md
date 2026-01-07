# Scenario 17: SolarSense

## Company Overview

**SolarSense** provides software for residential solar installation companies. Their platform handles lead management, proposal generation, permit automation, and project management. They serve 380 solar installers across the US, ranging from small local companies to regional chains.

**Business Model:**
- Per-project fee: $75-150 per completed installation (varies by deal size)
- Monthly subscription: $299-999/month for platform access (tiered by company size)
- Financing integration: Revenue share from solar loan originations
- Premium services: Permit expediting, utility interconnection support

**Current Metrics:**
- 380 active installer clients
- 12,000 installations processed/month
- Average installation value: $28,000
- Platform revenue: $1.8M/month
- Monthly churn: 3.1%
- Net Promoter Score: 41

---

## The Situation

The solar industry is in turmoil. California (40% of the market) changed net metering rules, making solar less economically attractive. Lead conversion rates dropped 25% industry-wide, and several SolarSense clients have gone out of business.

The Head of Product, Brian Walsh, wants to expand beyond solar—adding battery storage, EV chargers, and heat pump installation support. He believes diversification protects against policy risk.

The Head of Sales, Christina Martinez, wants to focus on geographic expansion. Many states are increasing solar incentives to meet clean energy goals. She believes SolarSense should help installers expand into growing markets.

The CFO, David Kim, is worried about customer health. He's tracking an alarming trend: clients with declining proposal volume don't churn immediately—they reduce usage, pay less in per-project fees, and eventually fail to renew. By the time churn happens, the revenue loss has already occurred.

---

## Available Data

You have access to:

1. **Installers table**: installer_id, company_name, signup_date, plan_tier, headquarters_state, employee_count, churned_date
2. **Projects table**: project_id, installer_id, homeowner_state, project_type (solar/battery/both), proposal_date, contract_date, install_date, project_value
3. **Proposals table**: proposal_id, installer_id, homeowner_zip, proposal_date, proposal_value, accepted (boolean)
4. **Usage table**: installer_id, month, logins, proposals_generated, permits_filed
5. **Market data**: state, month, permits_filed_market, avg_system_size_kw, utility_rates
6. **Financing table**: project_id, loan_amount, loan_provider, origination_date, solarSense_revenue_share

**Data quality notes:**
- Project outcome data depends on installer reporting (some don't update after contract)
- Battery storage was only added 6 months ago—limited data
- Market data is from public sources with 2-month lag
- Some installers operate across multiple states (headquarters may not reflect activity)

---

## Key Stakeholders

- **Brian Walsh (Head of Product)**: Wants to build battery/EV features. Believes diversification is existential for SolarSense.

- **Christina Martinez (Head of Sales)**: Wants geographic expansion team. Believes growing markets (Texas, Florida) need SolarSense.

- **David Kim (CFO)**: Focused on customer health metrics. Wants early warning system for failing installers.

- **Installer Advisory Board**: Mix of healthy and struggling companies. Divided on product direction.

- **Board of Directors**: Concerned about California exposure. Comparing SolarSense to competitors.

---

## Constraints

- Cannot build all product features at once—need to prioritize
- Battery/EV features would take 6+ months to build properly
- Geographic expansion requires local regulatory knowledge (varies by state)
- Some struggling installers are in default on payments—recovery uncertain

---

## The Ask

The CEO wants strategic guidance on navigating the industry shift. Specifically:

1. What's the real impact of California policy changes on our business?
2. Which installers are at risk of failure? Can we predict churn earlier?
3. Is diversification (battery/EV) or geographic expansion the better bet?
4. How should we price and package services for the new market reality?

Brian has privately said: "Christina wants to find more of the same customers. But the same customers are struggling. We need to evolve."

**Your deliverable:** Create a complete Analytics Project Brief for this analysis.
