# Analytics Project Brief

**Project Name:** Power User Behavior & Value Analysis **Date:** January 2026

**Prepared by:** Product Intelligence, Streamflix (Streaming Service)

---

## 1. Problem & Decision

**What business question or decision will this analysis inform?**

Streamflix has 45M subscribers, but engagement is highly skewed. We suspect a small percentage of users drive most of our viewing hours. We need to understand who power users are, what they do differently, and whether we should optimize for them or broaden engagement.

**Who is asking, and why now?**

CPO wants to inform the 2026 product roadmap. Should we build features for the hyper-engaged minority (who drive retention) or the casual majority (who might churn)? Content budget decisions also depend on understanding who watches what.

**Who is the ultimate decision maker?**

CPO for product roadmap. CFO weighs in on content investment implications.

**Hypothesis**

_We believe the top 10% of users account for >50% of viewing hours, and these power users have distinct content preferences and feature usage patterns that we're not explicitly designing for._

---

## 2. Metrics

**Primary Metric**

| Metric name | Definition | Baseline | Target |
|-------------|------------|----------|--------|
| Power User Concentration | % of total `viewing_minutes` from top 10% of users by monthly viewing, trailing 3 months | Unknown | Quantify concentration; identify behavioral markers |

**Counter-Metrics** _(2-3 max — what breaks if we optimize the primary metric?)_

| Counter-metric | Type | Why it could break | How we'll measure |
|----------------|------|-------------------|-------------------|
| 1. Casual user satisfaction | Guardrail | Power user features may confuse or alienate casual users | NPS by user segment, casual user churn rate |
| 2. Content diversity | Tradeoff | Optimizing for power users may narrow content investment | Genre diversity in top-viewed content |
| 3. New user activation | Guardrail | Power user-focused UX may overwhelm newcomers | D7 activation rate for new signups |

_Guardrail = must not worsen. Tradeoff = may worsen within acceptable bounds._

---

## 3. Stakeholder Map

| | High Interest | Low Interest |
|---|---|---|
| **High Power** | CPO, VP Content, CFO | CEO (high-level interest) |
| **Low Power** | Product managers, Content acquisition, UX research | Marketing, Engineering |

**Champions:** CPO (initiated analysis), VP Content (wants viewing data to inform licensing negotiations — power user preferences = negotiating leverage)

**Blockers:** VP Marketing (worried about messaging if findings suggest we're "only for binge-watchers" — conflicts with broad market positioning), UX Research lead (has existing personas that may be challenged; ego investment in prior work)

_Strategy: Frame as "understanding our full user base" not "choosing power users over everyone." Present as segmentation insight, not strategy prescription. Offer to collaborate with UX Research on persona updates._

---

## 4. Methodology

| Method | Hypothesis being tested | Data required |
|--------|------------------------|---------------|
| 1. Usage distribution analysis | How concentrated is viewing? (80/20 rule?) | Viewing hours per user per month |
| 2. Behavioral clustering | Do power users have distinct patterns? | Feature usage, content preferences, session patterns |
| 3. Path-to-power analysis | How do users become power users over time? | Longitudinal user behavior (12 months) |

**Data Availability**

| Data needed | Available? | If no, fallback |
|-------------|-----------|-----------------|
| Viewing hours per user (12 months) | Yes | — |
| Feature usage logs (downloads, lists, profiles) | Yes | — |
| Content metadata (genre, type) | Yes | — |

**Data Validity Checks (Stop/Go)**

| Check | How to validate | Stop if... |
|-------|-----------------|------------|
| Viewing data captures all devices | Compare to finance reported hours | >10% discrepancy |
| Multi-profile households handled | Check profile vs. account level | Analysis conflates profiles |

---

## 5. Scope & Deliverables

**In Scope**
- Define power user threshold (top 10%? 5%?)
- Behavioral profile of power users vs. casual
- Content preferences comparison
- Journey analysis: how users become power users

**Out of Scope**
- Revenue/LTV analysis — separate project with Finance
- Content recommendation algorithm changes — this informs, not implements
- International segmentation — US market only

**Final Deliverables**

- [x] Slide deck / Executive summary
- [x] Written report
- [x] Dashboard (Tableau / PowerBI / other)
- [x] Code / Reproducible pipeline
- [ ] Cleaned dataset

---

## 6. Success & Decision Criteria

**Analytical Success**
- Quantify power user concentration (% of hours from top X%)
- Identify 5+ statistically distinct behavioral markers
- Map the "path to power" journey with conversion rates

**Business Success**
- Product roadmap reflects segment insights
- Content team has data for licensing negotiations

**Decision Forum:** Product Strategy Quarterly **Action Owner:** CPO

**Decision Criteria**

| If we find... | We will... |
|---------------|------------|
| Power users are >50% of viewing and highly distinct | Create power user persona, prioritize their features |
| Power users valuable but small; casual users churn more | Balance: retain power users, activate casual |
| Path to power is predictable | Design interventions to accelerate casual → power |
| Power user content preferences are niche | Ensure content mix serves both segments |
| _(inconclusive / null result)_ | Conduct qualitative research with 10 power + 10 casual users |

**Action Thresholds**
- We will only recommend power user focus if: they drive >40% of viewing AND have distinct, actionable behaviors
- We will not act if: power users are just "people with more free time" with no replicable patterns

---

## 7. Timeline

| Milestone | Date |
|-----------|------|
| Data access secured | Jan 5 |
| Initial findings review | Jan 20 |
| Final delivery | Feb 1 |

---

## 8. Risks & Assumptions

**Key Assumptions**
1. Viewing hours is the right proxy for "power" (vs. breadth, recency)
2. Power user behavior is stable over time
3. Power users are more valuable (higher retention)

**Data Quality Assumptions**
- Viewing data captures all devices accurately
- Multi-profile households don't distort user-level analysis

**Risks**

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Shared accounts distort analysis | M | M | Use profile-level data where available |
| Power users are just "free time rich" | M | M | Segment by demographics, control for available time |
| Over-index on small segment | M | H | Always present casual user implications alongside |

---

## 9. Ethics & Privacy

| | Yes | No | Notes |
|---|---|---|---|
| Requires PII? | [x] | [ ] | User-level viewing data |
| Risk of bias against protected groups? | [x] | [ ] | Power users may skew demographically |
| GDPR / Privacy compliance reviewed? | [x] | [ ] | Using consented viewing data |

_Mitigation: Check demographic representation in power user segment. Ensure findings don't disadvantage any protected group in product decisions._

---

## 10. Pre-Mortem

_It's 3 months from now and this project failed. What happened?_

We identified power users as binge-watchers of serialized dramas. Product redesigned the homepage to prioritize "next episode" and long-form content. Casual users (who prefer movies and browsing) saw engagement drop 20%, and churn increased. We optimized for power users at the expense of everyone else. We should have presented a balanced strategy serving both segments.

---

_"Your job is never to optimize a metric; it's to improve the experience that the metric measures."_
