# Analytics Project Brief

**Project Name:** Cross-Product Engagement Effects Study **Date:** January 2026

**Prepared by:** Central Analytics, SocialSuite (Multi-Product Social Platform)

---

## 1. Problem & Decision

**What business question or decision will this analysis inform?**

SocialSuite operates three products: FriendFeed (social networking), QuickChat (messaging), and PicShare (photo sharing). Each product team optimizes their own metrics, but we suspect strong interdependencies. When PicShare engagement drops, does QuickChat suffer? Should we invest in "bridges" between products?

**Who is asking, and why now?**

Chief Product Officer observed that markets where FriendFeed is strong also show higher QuickChat retention — but can't tell if that's causal or selection. Strategy team is planning multi-year product investments and needs to know if products are complements or substitutes.

**Who is the ultimate decision maker?**

CPO for product strategy. CEO and board for major investment decisions.

**Hypothesis**

_We believe PicShare and QuickChat are complements (users of both retain 30% better than single-product users), and investment in cross-product features will increase overall platform stickiness._

---

## 2. Metrics

**Primary Metric**

| Metric name | Definition | Baseline | Target |
|-------------|------------|----------|--------|
| Multi-Product Retention Lift | D90 retention rate for users with `active_products >= 2` minus D90 retention for users with `active_products = 1`, where active = any session in prior 7 days | Unknown | Quantify lift; determine if >20% (actionable) |

**Counter-Metrics** _(2-3 max — what breaks if we optimize the primary metric?)_

| Counter-metric | Type | Why it could break | How we'll measure |
|----------------|------|-------------------|-------------------|
| 1. Individual product focus | Tradeoff | Cross-product investment may dilute each product's core value proposition | Product-specific NPS, core feature satisfaction scores |
| 2. User overwhelm | Guardrail | Pushing users across products may feel aggressive or confusing | Cross-promo opt-out rates, "too many notifications" complaints |
| 3. Cannibalization | Guardrail | One product may grow at another's expense (zero-sum) | Total platform DAU and time, not just per-product |

_Guardrail = must not worsen. Tradeoff = may worsen within acceptable bounds._

---

## 3. Stakeholder Map

| | High Interest | Low Interest |
|---|---|---|
| **High Power** | CPO, CEO, Strategy team | CFO (unless budget implications) |
| **Low Power** | FriendFeed PM, QuickChat PM, PicShare PM, Central Analytics | Engineering, Marketing |

**Champions:** CPO (initiated analysis), Strategy team (needs data for planning)

**Blockers:** Individual product PMs (may resist findings that deprioritize "their" product — each PM is measured on their product's metrics, so cross-product investment feels like a tax on their roadmap), FriendFeed PM specifically (largest product with most political capital — may not want to "subsidize" smaller products that they see as distractions)

_Strategy: Frame as "all boats rise" — show that ecosystem health benefits every product. Present in terms of total platform value, not product vs. product. Share draft findings privately with each PM before leadership presentation._

---

## 4. Methodology

| Method | Hypothesis being tested | Data required |
|--------|------------------------|---------------|
| 1. Multi-product user analysis | Do multi-product users retain better (controlling for engagement level)? | User-product engagement, retention |
| 2. Cross-product journey mapping | What are common paths across products? | Session-level product usage |
| 3. Natural experiment analysis | When one product has an outage/issue, do others suffer? | Product-level metrics, incident logs |

**Data Availability**

| Data needed | Available? | If no, fallback |
|-------------|-----------|-----------------|
| User engagement by product | Yes | — |
| Cross-product session data | Partial | Use daily active flags per product |
| Incident/outage logs | Yes | — |

**Data Validity Checks (Stop/Go)**

| Check | How to validate | Stop if... |
|-------|-----------------|------------|
| User identity consistent across products | Query for cross-product user ID overlap | <95% of users have unified ID |
| Engagement metrics comparable | Check for consistent event definitions | Products use different activity definitions |

---

## 5. Scope & Deliverables

**In Scope**
- Retention comparison: multi-product vs. single-product users
- Correlation analysis between product metrics
- Natural experiment: cross-product effects during incidents
- Recommendations for cross-product investment

**Out of Scope**
- Individual product deep-dives — each PM owns their product analysis
- Feature-level recommendations — this is strategic, not tactical
- Revenue/monetization effects — separate analysis with Finance

**Final Deliverables**

- [x] Slide deck / Executive summary
- [x] Written report
- [x] Dashboard (Tableau / PowerBI / other)
- [x] Code / Reproducible pipeline
- [ ] Cleaned dataset

---

## 6. Success & Decision Criteria

**Analytical Success**
- Quantify retention lift from multi-product usage (with confidence intervals)
- Establish (or refute) causal relationship between product engagement
- Map common cross-product journeys

**Business Success**
- Strategy team has data for multi-year product investment plan
- CPO can articulate platform strategy to board

**Decision Forum:** Product Strategy Quarterly **Action Owner:** CPO

**Decision Criteria**

| If we find... | We will... |
|---------------|------------|
| Strong complementarity (multi-product users 30%+ better retention, causal evidence) | Invest in cross-product features and bridges ($2M+ budget) |
| Weak or no relationship (selection bias explains correlation) | Let products optimize independently; no cross-product investment |
| Cannibalization (one product hurts another) | Reevaluate product portfolio strategy; possible sunset |
| Relationship varies by user segment | Target cross-product features to specific segments only |
| _(inconclusive / null result)_ | Design controlled experiment (holdout one product's cross-promo in 2 markets) |

**Action Thresholds**
- We will only recommend cross-product investment if: retention lift >20% AND causal evidence from natural experiments or propensity matching
- We will not act if: correlation exists but no causal support (selection bias likely)

---

## 7. Timeline

| Milestone | Date |
|-----------|------|
| Data access secured | Jan 10 |
| Initial findings review | Feb 1 |
| Final delivery | Feb 20 |

---

## 8. Risks & Assumptions

**Key Assumptions**
1. Multi-product usage is causal, not just a proxy for "engaged users do everything"
2. Cross-product data is joinable at user level
3. Historical patterns predict future ecosystem effects

**Data Quality Assumptions**
- User identity is consistent across products (single login)
- Engagement metrics are comparable across products

**Risks**

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Correlation ≠ causation (selection bias) | H | H | Use propensity matching, natural experiments; be explicit about what we can/can't claim |
| Product PMs dismiss "central" analysis | M | M | Involve PMs early, share methodology, solicit input on metrics |
| Findings threaten one product's resources | M | H | Frame as platform opportunity, not zero-sum; present total value created |

---

## 9. Ethics & Privacy

| | Yes | No | Notes |
|---|---|---|---|
| Requires PII? | [x] | [ ] | Cross-product user-level data |
| Risk of bias against protected groups? | [ ] | [x] | Platform-level analysis |
| GDPR / Privacy compliance reviewed? | [x] | [ ] | Using consented cross-product data per ToS |

_Mitigation: Analysis at aggregate level. No individual user data in deliverables._

---

## 10. Pre-Mortem

_It's 3 months from now and this project failed. What happened?_

We found that multi-product users retained 40% better and recommended heavy investment in cross-product features. But the correlation was selection bias — highly engaged users adopt multiple products naturally; the products didn't cause the engagement. When we pushed cross-product prompts to single-product users, it annoyed them, and FriendFeed saw a 10% DAU drop as users felt spammed. The product PMs blamed "central analytics" for the failure, damaging trust. We should have run a controlled holdout test before recommending investment, and been explicit about the limits of observational analysis.

---

_"Your job is never to optimize a metric; it's to improve the experience that the metric measures."_
