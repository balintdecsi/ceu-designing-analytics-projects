# Analytics Project Brief

**Project Name:** Subscriber Unit Economics Analysis **Date:** January 2026

**Prepared by:** Growth Analytics, MindfulApp (Meditation & Wellness App)

---

## 1. Problem & Decision

**What business question or decision will this analysis inform?**

MindfulApp is growing subscribers 40% YoY but burning $8M/quarter. The board wants to know: Are we acquiring customers profitably? Should we scale acquisition spend or fix unit economics first?

**Who is asking, and why now?**

Series B investors asking for path to profitability. CEO needs to show either (a) unit economics are healthy and we should spend more, or (b) we need to fix economics before scaling. Next board meeting: 6 weeks.

**Who is the ultimate decision maker?**

Board of Directors, with CEO presenting the recommendation.

**Hypothesis**

_We believe organic and referral users are highly profitable (LTV:CAC > 5x) while paid social users are marginal (LTV:CAC ~ 1.2x), and we should shift investment toward referral programs._

---

## 2. Metrics

**Primary Metric**

| Metric name | Definition | Baseline | Target |
|-------------|------------|----------|--------|
| LTV:CAC Ratio by Channel | (12-month projected LTV from `subscription_revenue`) / (Fully-loaded CAC including media, labor, tools), by acquisition source from Adjust | Unknown | Identify channels >3x; understand payback periods |

**Counter-Metrics** _(2-3 max — what breaks if we optimize the primary metric?)_

| Counter-metric | Type | Why it could break | How we'll measure |
|----------------|------|-------------------|-------------------|
| 1. Growth rate | Tradeoff | Cutting unprofitable channels may slow growth significantly | Monthly subscriber growth rate |
| 2. Engagement quality | Guardrail | Cheap users may convert but not engage (churn risk) | DAU/MAU ratio by acquisition cohort |
| 3. Brand awareness | Tradeoff | Paid builds awareness even when direct ROI is low | Branded search volume, aided awareness |

_Guardrail = must not worsen. Tradeoff = may worsen within acceptable bounds._

---

## 3. Stakeholder Map

| | High Interest | Low Interest |
|---|---|---|
| **High Power** | CEO, CFO, Board | CTO |
| **Low Power** | Head of Growth, Paid acquisition team | Product, Engineering |

**Champions:** CEO (needs this for board), Head of Growth (wants data to restructure budget)

**Blockers:** Paid acquisition team (if paid social looks bad, their team of 4 shrinks to 2 — jobs are on the line), Board members (one investor previously ran a consumer app and has strong priors about "acceptable" LTV:CAC ratios that may not fit our business)

_Strategy: Present scenarios, not just one answer. "If we optimize for profitability, growth slows to X. If we optimize for growth, burn is Y." Let leadership choose the tradeoff explicitly._

---

## 4. Methodology

| Method | Hypothesis being tested | Data required |
|--------|------------------------|---------------|
| 1. Cohort-based LTV modeling | Can we predict lifetime value from early behavior? | User-level subscription history |
| 2. Fully-loaded CAC by channel | What's true acquisition cost including labor, tools, creative? | Marketing spend, team allocation |
| 3. Payback period analysis | How many months to recover CAC by channel? | Monthly revenue by user by cohort |

**Data Availability**

| Data needed | Available? | If no, fallback |
|-------------|-----------|-----------------|
| User-level acquisition source | Yes (Adjust) | — |
| Subscription history by user | Yes (billing) | — |
| Detailed marketing spend by channel | Partial | Work with finance to allocate overhead |

**Data Validity Checks (Stop/Go)**

| Check | How to validate | Stop if... |
|-------|-----------------|------------|
| Adjust attribution coverage | % of paid users with valid source | <90% attributed |
| Subscription events complete | Compare billing revenue to event-based revenue | >5% discrepancy |

---

## 5. Scope & Deliverables

**In Scope**
- 5 channels: Paid Social, Paid Search, Organic/SEO, Referral, Influencer
- Cohorts from last 18 months
- Monthly and annual subscribers

**Out of Scope**
- Free tier users — paid subscriber economics only
- B2B/enterprise partnerships — different economics
- Reactivated churned users — new acquisition only

**Final Deliverables**

- [x] Slide deck / Executive summary
- [x] Written report
- [x] Dashboard (Tableau / PowerBI / other)
- [x] Code / Reproducible pipeline
- [ ] Cleaned dataset

---

## 6. Success & Decision Criteria

**Analytical Success**
- LTV estimates with <20% confidence interval
- CAC reconciles to finance's total spend (±5%)
- Clear segmentation by channel and subscription type

**Business Success**
- Board accepts methodology and findings
- Clear budget recommendation with projected impact

**Decision Forum:** Board Meeting (Feb) **Action Owner:** CEO

**Decision Criteria**

| If we find... | We will... |
|---------------|------------|
| All channels LTV:CAC > 3x | Increase spend aggressively across all channels |
| Mixed (some >3x, some <2x) | Reallocate from low to high performers |
| Most channels < 2x | Reduce spend, fix retention before scaling |
| Referral is 5x+ but tiny volume | Invest heavily in referral program ($500K) |
| _(inconclusive / null result)_ | Extend LTV observation window to 18 months, revisit in 6 months |

**Action Thresholds**
- We will only recommend channel cuts if: LTV:CAC <1.5x AND CI upper bound <2x
- We will not act if: cohorts are <6 months old (insufficient LTV data)

---

## 7. Timeline

| Milestone | Date |
|-----------|------|
| Data access secured | Jan 8 |
| Initial findings review | Jan 22 |
| Final delivery (board-ready) | Feb 5 |

---

## 8. Risks & Assumptions

**Key Assumptions**
1. Past retention predicts future retention (no major product changes)
2. Attribution data accurately assigns users to channels
3. Pricing stays constant (no major plan changes)

**Data Quality Assumptions**
- Adjust attribution is reliable for >90% of paid users
- Subscription events are logged without gaps

**Risks**

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| LTV projections too optimistic | H | H | Use conservative retention curves, show sensitivity |
| Attribution is messy (multi-touch) | M | M | Acknowledge uncertainty, show ranges |
| Board has different LTV:CAC expectations | M | M | Research SaaS benchmarks, contextualize |

---

## 9. Ethics & Privacy

| | Yes | No | Notes |
|---|---|---|---|
| Requires PII? | [x] | [ ] | User-level data, anonymized for analysis |
| Risk of bias against protected groups? | [ ] | [x] | |
| GDPR / Privacy compliance reviewed? | [x] | [ ] | Using existing consented data |

_Mitigation: All outputs aggregated to cohort level. No individual user data in deliverables._

---

## 10. Pre-Mortem

_It's 3 months from now and this project failed. What happened?_

We showed paid social had 1.5x LTV:CAC and recommended cutting 60% of spend. Growth slowed from 40% to 15%. Turns out paid social drove awareness that boosted organic and referral — channels weren't independent. We should have run a holdout test before making major cuts to understand channel interactions.

---

_"Your job is never to optimize a metric; it's to improve the experience that the metric measures."_
