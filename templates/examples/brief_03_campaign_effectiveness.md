# Analytics Project Brief

**Project Name:** Holiday Campaign Incrementality Analysis **Date:** January 2026

**Prepared by:** Marketing Science Team, BrightMart (National Retailer)

---

## 1. Problem & Decision

**What business question or decision will this analysis inform?**

BrightMart spent $18M on holiday marketing (Nov-Dec). Sales were up 12% YoY, but leadership questions whether marketing *caused* the lift or if we would have grown anyway due to economic tailwinds and new store openings.

**Who is asking, and why now?**

CFO is challenging marketing's budget request for next holiday season. CMO needs to prove incrementality, not just correlation. Decision: maintain, increase, or decrease holiday spend for next year.

**Who is the ultimate decision maker?**

CEO arbitrates between CFO (skeptical) and CMO (advocate). Board receives final recommendation.

**Hypothesis**

_We believe holiday marketing drove ~$45M in incremental revenue (2.5x ROI) because markets with heavier media weight showed disproportionate sales lifts after controlling for baseline trends._

---

## 2. Metrics

**Primary Metric**

| Metric name | Definition | Baseline | Target |
|-------------|------------|----------|--------|
| Incremental Revenue | (Actual revenue − Synthetic control revenue), daily POS, US markets, Nov 1-Dec 31 | $0 (null hypothesis) | Prove >2x ROI on $18M spend |

**Counter-Metrics** _(2-3 max — what breaks if we optimize the primary metric?)_

| Counter-metric | Type | Why it could break | How we'll measure |
|----------------|------|-------------------|-------------------|
| 1. Brand perception | Guardrail | Heavy promotional messaging may cheapen brand | Brand tracking survey (premium perception score) |
| 2. Gross margin | Tradeoff | Sales up but at lower margin due to promos | Margin % during campaign vs. baseline |
| 3. January sales | Guardrail | Pulling forward demand may hurt post-holiday | Jan YoY comparison |

_Guardrail = must not worsen. Tradeoff = may worsen within acceptable bounds._

---

## 3. Stakeholder Map

| | High Interest | Low Interest |
|---|---|---|
| **High Power** | CFO (skeptical), CMO (advocate), CEO (arbitrator) | Board |
| **Low Power** | Regional marketing managers, Agency partners | Store ops, HR |

**Champions:** CMO (most to gain from proving effectiveness), VP Digital (believes their channels outperformed TV)

**Blockers:** CFO (skeptical of marketing attribution after overspend on a failed brand campaign in 2023), Agency partners (low incrementality finding threatens their $5M contract renewal)

_Strategy: Involve CFO's team in methodology design upfront. Use conservative assumptions throughout. Present ranges, not point estimates. Address agency concern by framing as "optimization" not "cut."_

---

## 4. Methodology

| Method | Hypothesis being tested | Data required |
|--------|------------------------|---------------|
| 1. Geo-matched market test | High-spend vs. low-spend markets show different lifts? | Daily sales by market, media spend by market |
| 2. Synthetic control | What would have happened without campaign? | Pre-campaign trends by market |
| 3. Media mix modeling | Which tactics (TV, digital, print) drove most lift? | Spend by channel by week |

**Data Availability**

| Data needed | Available? | If no, fallback |
|-------------|-----------|-----------------|
| Daily sales by market (200+ markets) | Yes (POS) | — |
| Media spend by market by week | Yes (agency) | — |
| Competitor activity by market | Partial | Use national competitor spend as proxy |

**Data Validity Checks (Stop/Go)**

| Check | How to validate | Stop if... |
|-------|-----------------|------------|
| POS data complete across markets | Compare market count to expected 214 | >5% of markets missing data |
| Control markets are valid counterfactuals | Check for store openings/closings, competitor entry | Major confounds in >20% of control markets |

---

## 5. Scope & Deliverables

**In Scope**
- Nov 1 - Dec 31 campaign period
- All paid media (TV, digital, radio, OOH, print)
- US markets only
- Revenue and margin impact

**Out of Scope**
- Owned media (email, app) — analyzed separately
- Long-term brand effects — short-term incrementality only
- Store-level analysis — market level only
- Creative effectiveness — separate study

**Final Deliverables**

- [x] Slide deck / Executive summary
- [x] Written report
- [ ] Dashboard (Tableau / PowerBI / other)
- [x] Code / Reproducible pipeline
- [x] Cleaned dataset

---

## 6. Success & Decision Criteria

**Analytical Success**
- Incrementality estimate with confidence intervals
- Methodology passes CFO finance team review
- Channel-level breakdown with statistical significance

**Business Success**
- Budget decision made with data, not politics
- Clear guidance on which tactics to scale/cut

**Decision Forum:** Executive Committee Monthly **Action Owner:** CMO

**Decision Criteria**

| If we find... | We will... |
|---------------|------------|
| ROI > 3x | Recommend 15% budget increase, double down on top channels |
| ROI 2-3x | Maintain budget, reallocate from worst to best channels |
| ROI 1-2x | Maintain budget but restructure tactics significantly |
| ROI < 1x | Recommend budget cut, fundamental strategy rethink |
| _(inconclusive / null result)_ | Design cleaner holdout test for next year (5 markets, full dark) |

**Action Thresholds**
- We will only recommend budget increase if: ROI point estimate >2.5x AND lower CI bound >1.5x
- We will not act if: CI spans both positive and negative ROI

---

## 7. Timeline

| Milestone | Date |
|-----------|------|
| Data access secured | Jan 5 |
| Initial findings review | Jan 25 |
| Final delivery | Feb 10 |

---

## 8. Risks & Assumptions

**Key Assumptions**
1. Markets in holdout/low-spend groups are valid counterfactuals
2. No major competitor actions varied systematically by market
3. Economic conditions similar across test/control markets

**Data Quality Assumptions**
- POS data is complete and accurate across all markets
- Agency spend reports reconcile to finance actuals (±5%)

**Risks**

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| CFO rejects methodology | M | H | Involve finance in method design |
| Agency disputes findings | M | M | Share methodology early, invite input |
| Competitor confound in control markets | M | H | Validate market matching rigorously |

---

## 9. Ethics & Privacy

| | Yes | No | Notes |
|---|---|---|---|
| Requires PII? | [ ] | [x] | Market-level aggregates only |
| Risk of bias against protected groups? | [ ] | [x] | |
| GDPR / Privacy compliance reviewed? | [x] | [ ] | No individual data used |

---

## 10. Pre-Mortem

_It's 3 months from now and this project failed. What happened?_

We proved 2.8x ROI and CMO was thrilled. But CFO's team found that our "control" markets had a new competitor (ValueMart) enter during the campaign, artificially depressing their sales and inflating our incrementality estimate. When re-run with proper controls, ROI dropped to 1.4x. We should have validated market matching more rigorously before analysis.

---

_"Your job is never to optimize a metric; it's to improve the experience that the metric measures."_
