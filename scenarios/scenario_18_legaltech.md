# Scenario 18: CaseFlow

## Company Overview

**CaseFlow** provides practice management software for small and mid-sized law firms. The platform handles case management, time tracking, billing, document management, and client communication. Founded in 2017, they've grown to serve 2,800 law firms across the US and Canada.

**Business Model:**
- Per-user pricing: $79/user/month (standard), $129/user/month (professional)
- Implementation fees: $1,000-5,000 based on firm size and data migration needs
- Document storage: Included up to 50GB, then $10/50GB/month
- Integrations: Premium connectors to court filing systems ($50/month)

**Current Metrics:**
- 2,800 law firms
- 18,500 active users (average 6.6 users per firm)
- MRR: $1.58M
- Annual churn: 14% (logos), 18% (revenue - due to seat reduction)
- NPS: 32 (industry average: 35)
- Implementation completion rate: 72%

---

## The Situation

CaseFlow is facing competitive pressure from both ends: Clio (the market leader) is moving downmarket with simplified pricing, while vertical specialists are targeting specific practice areas (immigration, personal injury, family law) with tailored features.

The VP of Product, Amy Richardson, believes the answer is vertical specialization. She wants to build practice-area-specific features, starting with personal injury (30% of CaseFlow's customer base). This would include settlement calculators, medical record management, and lien tracking.

The VP of Customer Success, John Park, disagrees. He believes churn is driven by poor implementation and low adoption, not feature gaps. Only 72% of firms complete implementation, and those that don't complete churn at 3x the rate.

Recent analysis revealed a "usage cliff": firms where <50% of licensed users log in monthly churn at 35% annually. Firms with >80% user engagement churn at only 8%.

---

## Available Data

You have access to:

1. **Firms table**: firm_id, firm_name, practice_area, signup_date, plan_tier, firm_size, churned_date, churn_reason
2. **Users table**: user_id, firm_id, role (attorney/paralegal/admin), user_start_date, last_login
3. **Usage table**: user_id, date, features_used, time_entries_logged, documents_created
4. **Implementation table**: firm_id, implementation_start, implementation_end, steps_completed, implementation_score
5. **Support tickets**: ticket_id, firm_id, user_id, ticket_date, category, resolution_time, satisfaction_score
6. **Billing table**: firm_id, month, users_billed, revenue, overages

**Data quality notes:**
- Practice area is self-reported and some firms do multiple areas
- Churn reason is only captured for 55% of churned firms
- Implementation "completion" definition changed 8 months ago
- Some firms have seasonal usage patterns (court calendars)

---

## Key Stakeholders

- **Amy Richardson (VP Product)**: Wants vertical features. Believes feature differentiation wins deals.

- **John Park (VP Customer Success)**: Wants implementation investment. Believes adoption drives retention.

- **Sales Team**: Split—some want vertical positioning, others want simpler pricing to compete with Clio.

- **Personal Injury Firm Advisory Group**: Vocal about wanting PI-specific features. Threaten to churn if not delivered.

- **Board of Directors**: Watching Clio's moves closely. Concerned about competitive moat.

---

## Constraints

- Engineering capacity limits building vertical features AND improving onboarding simultaneously
- Personal injury features would take 8+ months for full release
- Cannot significantly change pricing without full analysis (current model is embedded in sales compensation)
- Some implementation data is in legacy system (hard to query)

---

## The Ask

The CEO wants a clear strategic recommendation. Specifically:

1. What actually drives churn? Is it feature gaps, implementation failure, or something else?
2. Would vertical specialization (personal injury features) reduce churn in that segment?
3. Is the "usage cliff" real? Can we predict and prevent firms from falling off it?
4. Should we invest in vertical features (Amy) or implementation/adoption (John)?

Amy has privately said: "John wants to throw more onboarding at the problem. But firms don't churn because onboarding failed—they churn because we don't have what they need."

**Your deliverable:** Create a complete Analytics Project Brief for this analysis.
