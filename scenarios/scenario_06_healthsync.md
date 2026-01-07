# Scenario 06: HealthSync

## Company Overview

**HealthSync** is a B2B healthcare technology company providing patient engagement platforms to hospitals and health systems. Their software helps healthcare providers communicate with patients through appointment reminders, post-visit follow-ups, and chronic disease management programs.

**Business Model:**
- Annual contracts with hospitals/health systems
- Pricing based on covered patient population (per-member-per-month)
- Implementation fees for onboarding new clients
- Premium modules (telehealth integration, AI triage) sold separately

**Current Metrics:**
- 45 health system clients covering 8.2 million patients
- $38M ARR (annual recurring revenue)
- Gross retention: 92% (logos retained)
- Net retention: 108% (including upsells)
- Average contract value: $844,000/year
- Implementation timeline: 6-9 months

---

## The Situation

HealthSync is preparing for a Series C fundraise. The board wants to demonstrate strong product-market fit through engagement metrics, but the data tells a complicated story.

Overall platform engagement (patients who interact with at least one message/month) is 62%. However, engagement varies dramatically:
- Top quartile clients: 78% engagement
- Bottom quartile clients: 34% engagement

The VP of Customer Success, Amanda Foster, believes the difference is implementation quality. Clients with dedicated IT resources and executive sponsorship engage more. The VP of Product, Robert Chang, disagrees—he thinks it's about which features clients use. Clients using the mobile app (vs. SMS-only) have 2x higher engagement.

Two major clients are at risk of non-renewal next quarter:
- **Metro Health System** (1.2M patients): Engagement dropped from 58% to 41% after they switched EMR vendors
- **Coastal Medical Group** (400K patients): New CMO is skeptical of the ROI and demanding proof

---

## Available Data

You have access to:

1. **Clients table**: client_id, client_name, contract_start, contract_end, contract_value, patient_population, client_tier, account_manager
2. **Patient engagement**: patient_id, client_id, month, messages_sent, messages_opened, actions_taken (appointment confirmed, form completed, etc.)
3. **Feature usage**: client_id, month, feature_name, usage_count
4. **Implementation log**: client_id, implementation_start, go_live_date, implementation_score, notes
5. **Client health scores**: client_id, month, health_score (1-100), risk_flag, notes
6. **Upsell history**: client_id, module_name, upsell_date, incremental_revenue

**Data quality notes:**
- Patient-level data cannot be exported or used in aggregate reporting (HIPAA)
- Implementation notes are unstructured text
- Health scores are subjective (assigned by account managers)
- Some clients opted out of detailed usage tracking

---

## Key Stakeholders

- **Amanda Foster (VP Customer Success)**: Owns client retention. Believes implementation quality is the key driver. Her team's bonus depends on gross retention.

- **Robert Chang (VP Product)**: Wants to prove that product features (esp. mobile app) drive engagement. Proposing a mandatory mobile app rollout.

- **Sales Team**: Wants engagement benchmarks to use in sales conversations. Worried about bottom-quartile stats becoming public.

- **At-risk client CMOs**: Metro Health and Coastal Medical—need convincing data to renew.

- **Board/Investors**: Want clear metrics for Series C deck. Comparing HealthSync to competitors with higher reported engagement.

---

## Constraints

- Cannot share client-specific data between clients (confidentiality agreements)
- HIPAA limits what patient-level analysis can be reported externally
- Only 6 weeks until Series C kickoff—analysis must be complete
- Cannot delay at-risk client renewals—decisions needed in 4 weeks

---

## The Ask

The CEO wants analysis to support both the Series C narrative and client retention. Specifically:

1. What drives engagement differences between top and bottom quartile clients?
2. Is the driver implementation quality (fixable with services) or product features (fixable with product)?
3. What story can we credibly tell in the Series C deck about engagement and outcomes?
4. How do we save Metro Health and Coastal Medical?

Amanda has warned: "If we blame implementation, my team looks bad. If we blame product, Robert's team looks bad. Be careful how you frame this."

**Your deliverable:** Create a complete Analytics Project Brief for this analysis.
