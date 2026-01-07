# Analytics Project Brief

**Project Name:** Marketing Channel Attribution & Budget Reallocation **Date:** January 2026

**Prepared by:** Marketing Analytics, DataDash (B2B Analytics Platform)

---

## 1. Problem & Decision

**What business question or decision will this analysis inform?**

DataDash spends $2.4M/quarter across 6 marketing channels. Current budget allocation uses last-touch attribution, which heavily favors Google Search. The CMO suspects we're undervaluing awareness channels (LinkedIn, content marketing) that create demand but don't get conversion credit.

**Who is asking, and why now?**

CMO is preparing Q2 budget proposal for the board. Need to prove (or disprove) that reallocation can improve CAC efficiency. Decision deadline: March 15.

**Who is the ultimate decision maker?**

CMO owns marketing budget. CFO has veto power on major reallocations (>$500K shift).

**Hypothesis**

_We believe LinkedIn and content marketing are undervalued because they appear in >50% of closed-won deals as first-touch but receive <5% of last-touch credit._

---

## 2. Metrics

**Primary Metric**

| Metric name | Definition | Baseline | Target |
|-------------|------------|----------|--------|
| Channel-attributed pipeline value | `opportunity.value` × attribution weight, closed-won deals, 12-month lookback, US accounts | Last-touch model only | Multi-touch model revealing >20% reallocation opportunity |

**Counter-Metrics** _(2-3 max — what breaks if we optimize the primary metric?)_

| Counter-metric | Type | Why it could break | How we'll measure |
|----------------|------|-------------------|-------------------|
| 1. Brand awareness | Guardrail | Cutting awareness channels may hurt long-term pipeline | Quarterly brand survey, direct traffic trends |
| 2. Lead quality | Guardrail | Some channels bring volume but low close rates | Win rate and deal size by attributed channel |
| 3. Partner relationships | Tradeoff | Sudden budget cuts damage platform relationships | Qualitative check with channel managers |

_Guardrail = must not worsen. Tradeoff = may worsen within acceptable bounds._

---

## 3. Stakeholder Map

| | High Interest | Low Interest |
|---|---|---|
| **High Power** | CMO, CFO, VP Sales | CEO |
| **Low Power** | Paid Search manager, Content lead, LinkedIn ads manager | Product, Engineering |

**Champions:** CMO (initiated analysis), Content marketing lead (believes their channel is undervalued)

**Blockers:** Paid Search manager (last-touch model favors them — reallocation = budget cut; also recently promoted based on "Search ROI" narrative, so findings threaten their credibility), VP Sales (skeptical of "marketing math" after a prior attribution model led to bad territory planning two years ago)

_Strategy: Include lead quality metrics to address Sales concerns. Private conversation with Paid Search manager about findings before broad share. Acknowledge their past success while reframing as "evolving our measurement."_

---

## 4. Methodology

| Method | Hypothesis being tested | Data required |
|--------|------------------------|---------------|
| 1. Multi-touch attribution modeling | Which channels are over/undervalued vs. last-touch? | All marketing touchpoints per account |
| 2. Channel LTV analysis | Which channels bring high-value customers? | Deal outcomes and values |
| 3. Path analysis | How do channels work together in winning deals? | Touchpoint sequences with timestamps |

**Data Availability**

| Data needed | Available? | If no, fallback |
|-------------|-----------|-----------------|
| Marketing touchpoints per account | Yes (CRM + marketing automation) | — |
| Deal outcomes and values | Yes (Salesforce) | — |
| Touchpoint timestamps | Partial | Use best available, note uncertainty |

**Data Validity Checks (Stop/Go)**

| Check | How to validate | Stop if... |
|-------|-----------------|------------|
| UTM parameters present on touchpoints | Query for NULL UTMs | >10% missing UTMs |
| Touchpoint-to-deal join rate | Compare touchpoint accounts to SF accounts | <80% of deals have ≥1 touchpoint |

---

## 5. Scope & Deliverables

**In Scope**
- 6 channels: Google Search, LinkedIn Ads, Content/SEO, Email, Events, Paid Social
- Last 12 months of closed deals (won and lost)
- Comparison of 4 attribution models (first, last, linear, time-decay)

**Out of Scope**
- Channel creative optimization — this is budget allocation, not campaign optimization
- New channel evaluation (podcast, etc.) — existing channels only
- Sales-assisted vs. self-serve segmentation — future analysis

**Final Deliverables**

- [x] Slide deck / Executive summary
- [x] Written report
- [ ] Dashboard (Tableau / PowerBI / other)
- [x] Code / Reproducible pipeline
- [ ] Cleaned dataset

---

## 6. Success & Decision Criteria

**Analytical Success**
- Clear channel ranking under multiple attribution models
- Confidence intervals on attribution weights (±10% or tighter)
- Path analysis showing common multi-touch journeys

**Business Success**
- CMO has defensible budget proposal for board
- Clear reallocation recommendation with projected CAC impact

**Decision Forum:** Marketing Leadership Weekly **Action Owner:** CMO

**Decision Criteria**

| If we find... | We will... |
|---------------|------------|
| LinkedIn/content undervalued by >30% | Recommend 20-30% shift from Search to awareness ($400-600K) |
| Models roughly agree with last-touch | Maintain allocation, focus on channel-level optimization |
| Data quality too poor to trust | Invest in attribution infrastructure before reallocating |
| _(inconclusive / null result)_ | Run controlled geo-holdout test (2 markets, 8 weeks) to validate |

**Action Thresholds**
- We will only recommend reallocation if: attribution gap ≥20% AND CI excludes zero
- We will not act if: gap <10% or sample size <100 closed deals per channel

---

## 7. Timeline

| Milestone | Date |
|-----------|------|
| Data access secured | Jan 10 |
| Initial findings review | Feb 1 |
| Final delivery | Feb 15 |

---

## 8. Risks & Assumptions

**Key Assumptions**
1. CRM touchpoint data is reasonably complete
2. 12 months is sufficient to observe channel effects
3. Past channel performance predicts future value

**Data Quality Assumptions**
- UTM parameters are consistently applied across channels
- Deal attribution in Salesforce is accurate

**Risks**

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Paid Search manager undermines findings | M | M | Early involvement, acknowledge expertise |
| Model choice drives conclusion | M | H | Present all 4 models transparently |
| Board rejects methodology | L | H | Include case studies, conservative estimates |

---

## 9. Ethics & Privacy

| | Yes | No | Notes |
|---|---|---|---|
| Requires PII? | [ ] | [x] | Account-level, not individual |
| Risk of bias against protected groups? | [ ] | [x] | B2B context, company-level analysis |
| GDPR / Privacy compliance reviewed? | [x] | [ ] | Using existing CRM data per policy |

---

## 10. Pre-Mortem

_It's 3 months from now and this project failed. What happened?_

We recommended shifting $600K from Paid Search to LinkedIn. Three months later, pipeline dropped 25%. Our touchpoint tracking missed that Paid Search was the "closer" for deals that LinkedIn "started" — we double-counted LinkedIn's influence and cut the channel that actually closed. We should have run a geo-holdout test before major budget shifts.

---

_"Your job is never to optimize a metric; it's to improve the experience that the metric measures."_
