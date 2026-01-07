# Analytics Project Brief

**Project Name:** Freemium Upgrade Path Optimization **Date:** January 2026

**Prepared by:** Growth & Monetization, NoteSpace (Productivity SaaS)

---

## 1. Problem & Decision

**What business question or decision will this analysis inform?**

NoteSpace has 2M free users and 180K paid subscribers (9% conversion). We believe there's significant untapped revenue in the free base. We need to understand what triggers upgrades, which free users are most likely to convert, and what barriers prevent conversion.

**Who is asking, and why now?**

CFO is pushing for 20% revenue growth without proportional CAC increase. CEO wants to "monetize the base we've already built." The decision: Where should Product invest to drive upgrades — feature gating, usage limits, or premium feature discovery?

**Who is the ultimate decision maker?**

CEO sets revenue targets. VP Product decides implementation approach.

**Hypothesis**

_We believe users who hit the 5GB storage limit convert at 3x the rate of those who don't, but only 15% of free users ever hit the limit — we're leaving conversion on the table by not surfacing premium value earlier._

---

## 2. Metrics

**Primary Metric**

| Metric name | Definition | Baseline | Target |
|-------------|------------|----------|--------|
| Free-to-Paid Conversion Rate | Users with `subscription_status` changed from 'free' to 'paid' in month / Users with `subscription_status = 'free'` at month start, excluding trial users | 0.8%/month | Increase to 1.2%/month (+50%) |

**Counter-Metrics** _(2-3 max — what breaks if we optimize the primary metric?)_

| Counter-metric | Type | Why it could break | How we'll measure |
|----------------|------|-------------------|-------------------|
| 1. Free user retention | Guardrail | Aggressive upgrade prompts may drive free users away entirely | Free user D30 retention, free DAU trend |
| 2. Upgrade satisfaction | Guardrail | Premature upgrades may lead to regret and churn | 90-day paid retention, refund rate within 30 days |
| 3. Brand perception | Tradeoff | "Pushy" monetization damages trust and word-of-mouth | NPS score, App Store rating trend, support ticket volume |

_Guardrail = must not worsen. Tradeoff = may worsen within acceptable bounds._

---

## 3. Stakeholder Map

| | High Interest | Low Interest |
|---|---|---|
| **High Power** | CEO, CFO, VP Product | CTO |
| **Low Power** | Growth PM, Pricing team, Customer Success | Engineering, Marketing |

**Champions:** CFO (revenue focus), Growth PM (owns conversion funnel)

**Blockers:** Customer Success (worried about support load from confused upgrades — their team is already stretched, and premature conversions create "why am I paying for this?" tickets), VP Product (philosophically opposed to "aggressive" monetization that hurts UX — has killed similar proposals before)

_Strategy: Position as "right user, right time" not "monetize everyone." Show that premature upgrades hurt paid retention, so targeting is in everyone's interest. Involve VP Product in defining what "non-aggressive" looks like._

---

## 4. Methodology

| Method | Hypothesis being tested | Data required |
|--------|------------------------|---------------|
| 1. Conversion driver analysis | What behaviors precede upgrade? | User events, upgrade timestamps |
| 2. Limit-hit analysis | Do usage limits drive conversion or churn? | Storage/feature usage, limit events |
| 3. Propensity modeling | Can we predict who will convert? | User features, conversion outcomes |

**Data Availability**

| Data needed | Available? | If no, fallback |
|-------------|-----------|-----------------|
| Free user behavior logs | Yes | — |
| Upgrade events with timestamp | Yes | — |
| Usage limit hit events | Partial | Reconstruct from storage/usage data |

**Data Validity Checks (Stop/Go)**

| Check | How to validate | Stop if... |
|-------|-----------------|------------|
| Upgrade events accurate | Compare upgrade count to billing system records | >3% discrepancy |
| Free user tracking consistent | Compare event volume across iOS/Android/Web | Any platform has >20% different event rate |

---

## 5. Scope & Deliverables

**In Scope**
- Conversion drivers for free → paid
- Segment analysis: who converts vs. who doesn't
- Limit-hit behavior analysis
- Propensity model for targeting

**Out of Scope**
- Paid tier upsells (Basic → Pro → Enterprise) — separate analysis
- Pricing optimization — not changing price, just targeting
- Churn analysis for paid users — separate project

**Final Deliverables**

- [x] Slide deck / Executive summary
- [x] Written report
- [x] Dashboard (Tableau / PowerBI / other)
- [x] Code / Reproducible pipeline
- [x] Cleaned dataset (high-propensity user list)

---

## 6. Success & Decision Criteria

**Analytical Success**
- Identify 3-5 behavioral triggers that precede conversion
- Build propensity model with AUC >0.75
- Size the "high-propensity unconverted" segment

**Business Success**
- Product has clear roadmap for upgrade interventions
- Propensity list integrated into targeting system

**Decision Forum:** Growth Team Weekly **Action Owner:** Growth PM

**Decision Criteria**

| If we find... | We will... |
|---------------|------------|
| Storage limit is primary driver, but few hit it | Surface limit earlier or lower threshold (A/B test) |
| Premium feature discovery drives conversion | Improve premium feature trial/preview experience |
| High-propensity segment is large and untapped | Launch targeted upgrade campaign to that segment |
| Conversion appears random (no clear drivers) | Conduct user research on upgrade barriers before investing |
| _(inconclusive / null result)_ | A/B test top 2 hypotheses with small holdout to measure incrementality |

**Action Thresholds**
- We will only recommend targeting intervention if: propensity model AUC >0.70 AND target segment is >50K users
- We will not act if: top drivers explain <15% of conversion variance (model has no predictive power)

---

## 7. Timeline

| Milestone | Date |
|-----------|------|
| Data access secured | Jan 8 |
| Initial findings review | Jan 22 |
| Propensity model delivered | Feb 5 |
| Final delivery | Feb 12 |

---

## 8. Risks & Assumptions

**Key Assumptions**
1. Past conversion behavior predicts future conversion
2. Free users who convert are similar to current paid users
3. Behavioral signals are causal, not just correlated (selection bias risk)

**Data Quality Assumptions**
- Upgrade events accurately capture conversion moment
- Free user tracking is consistent across platforms

**Risks**

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Propensity model targets users who'd convert anyway | M | M | Use holdout group to measure incrementality |
| Aggressive targeting drives free user churn | M | H | Start with light-touch interventions, monitor D30 retention weekly |
| VP Product blocks "pushy" monetization | M | M | Involve VP Product in defining acceptable intervention types upfront |

---

## 9. Ethics & Privacy

| | Yes | No | Notes |
|---|---|---|---|
| Requires PII? | [x] | [ ] | User-level behavior data |
| Risk of bias against protected groups? | [ ] | [x] | Targeting based on behavior, not demographics |
| GDPR / Privacy compliance reviewed? | [x] | [ ] | Using consented product data |

_Mitigation: Propensity scores based on behavior only. No demographic targeting. All outputs aggregated in reports._

---

## 10. Pre-Mortem

_It's 3 months from now and this project failed. What happened?_

We built a propensity model and aggressively targeted high-propensity free users with upgrade prompts. Conversion increased 40%, but free user DAU dropped 25% as annoyed users left. It turned out many "high propensity" users were power free users who valued the free tier — they felt betrayed by constant upsell pressure. We should have tested messaging gentleness, used a holdout group, and monitored free retention as a hard guardrail from day one.

---

_"Your job is never to optimize a metric; it's to improve the experience that the metric measures."_
