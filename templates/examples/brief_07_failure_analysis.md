# Analytics Project Brief

**Project Name:** Search Zero-Results Investigation **Date:** January 2026

**Prepared by:** Search Quality Team, FindIt (E-commerce Search Engine)

---

## 1. Problem & Decision

**What business question or decision will this analysis inform?**

12% of searches on FindIt return zero results. Users who hit zero-results pages have 3x higher bounce rates. We need to understand *why* searches fail and identify the highest-impact fixes — whether that's better spelling correction, synonym expansion, category mapping, or inventory gaps.

**Who is asking, and why now?**

VP Product flagged that zero-results rate has crept up from 9% to 12% over 6 months. Each percentage point represents ~$2M in lost annual GMV. Engineering has bandwidth for one major search improvement in Q2.

**Who is the ultimate decision maker?**

VP Product prioritizes the roadmap. VP Engineering allocates the team.

**Hypothesis**

_This is an exploratory analysis. We don't know why searches fail. The goal is to categorize failure modes and size each category before forming hypotheses about solutions._

---

## 2. Metrics

**Primary Metric**

| Metric name | Definition | Baseline | Target |
|-------------|------------|----------|--------|
| Zero-Results Rate | `search_executed` events with `result_count = 0` / total `search_executed` events, trailing 7 days, excluding bot traffic | 12% | Reduce to 8% (back to prior baseline) |

**Counter-Metrics** _(2-3 max — what breaks if we optimize the primary metric?)_

| Counter-metric | Type | Why it could break | How we'll measure |
|----------------|------|-------------------|-------------------|
| 1. Search relevance | Guardrail | Returning bad results is worse than no results — aggressive spellers may "correct" valid queries | Click-through rate, add-to-cart rate on search results |
| 2. Query latency | Guardrail | Complex spelling/synonym logic may slow search unacceptably | p95 search latency (must stay <300ms) |
| 3. Inventory trust | Tradeoff | Showing "similar" items for exact queries may frustrate users expecting exact match | Customer complaints, return rates |

_Guardrail = must not worsen. Tradeoff = may worsen within acceptable bounds._

---

## 3. Stakeholder Map

| | High Interest | Low Interest |
|---|---|---|
| **High Power** | VP Product, VP Engineering | CEO, CFO |
| **Low Power** | Search PM, ML team, Merchandising | Marketing, Support |

**Champions:** VP Product (owns the metric), Search PM (wants to fix their product)

**Blockers:** ML team (championing a sophisticated ML-based query understanding system — may resist "simple" fixes that undercut the case for their project), Merchandising (if inventory gaps are the problem, it's their issue and their budget — may dispute methodology to deflect blame)

_Strategy: Present data on root cause distribution objectively. If spelling is 40%+ of the problem, it's a quick win before investing in ML. Engage Merchandising early if inventory is significant — frame as "opportunity" not "blame."_

---

## 4. Methodology

| Method | Question being explored | Data required |
|--------|------------------------|---------------|
| 1. Manual query sampling (200 queries) | What are the categories of failure? (spelling, synonym, inventory, junk) | Random sample of zero-result queries |
| 2. Pattern classification at scale | Does the manual taxonomy hold at scale? | All zero-result queries (1 month) |
| 3. Opportunity sizing | Which category has highest GMV impact if fixed? | Query volume, estimated intent value |

**Data Availability**

| Data needed | Available? | If no, fallback |
|-------------|-----------|-----------------|
| Zero-result query logs | Yes | — |
| Inventory catalog for matching | Yes | — |
| Query → purchase intent mapping | Partial | Use category-level GMV estimates |

**Data Validity Checks (Stop/Go)**

| Check | How to validate | Stop if... |
|-------|-----------------|------------|
| Bot traffic filtered | Compare query patterns to known bot signatures | >15% suspected bot queries in sample |
| Query logs capture actual typed query | Spot-check 50 queries against UI session recordings | Queries are normalized/modified before logging |

---

## 5. Scope & Deliverables

**In Scope**
- Classification of zero-result queries into root causes
- Sizing each category by query volume and GMV impact
- Top 50 specific queries to fix immediately
- Recommendation for Q2 engineering investment

**Out of Scope**
- Implementing fixes — this analysis informs, engineering builds
- Low-result queries (results exist but are poor) — separate project
- Voice/image search — text queries only

**Final Deliverables**

- [x] Slide deck / Executive summary
- [x] Written report
- [ ] Dashboard (Tableau / PowerBI / other)
- [x] Code / Reproducible pipeline
- [x] Cleaned dataset (top queries to fix)

---

## 6. Success & Decision Criteria

**Analytical Success**
- Categorize >90% of zero-result queries into root causes
- Size each category by volume and GMV
- Identify "quick wins" vs. "infrastructure investments"

**Business Success**
- Engineering has clear priority for Q2
- Projected GMV recovery from top fix

**Decision Forum:** Search Quality Review (biweekly) **Action Owner:** Search PM

**Decision Criteria**

| If we find... | We will... |
|---------------|------------|
| Spelling/typos are >40% of failures | Prioritize spelling correction investment |
| Synonym gaps are >30% | Build synonym expansion system |
| Inventory gaps are dominant | Escalate to Merchandising for catalog expansion |
| Junk/nonsense queries are high (>30%) | Deprioritize this problem — not fixable |
| _(inconclusive / categories evenly split)_ | Expand sample size to 500, conduct user research to understand intent behind ambiguous queries |

**Action Thresholds**
- We will only recommend engineering investment if: category represents >25% of zero-results AND has clear technical solution
- We will not act if: manual classification inter-rater reliability <70% (methodology not trustworthy)

---

## 7. Timeline

| Milestone | Date |
|-----------|------|
| Data access secured | Jan 5 |
| Manual sample review complete | Jan 12 |
| Scale analysis complete | Jan 22 |
| Final delivery | Jan 28 |

---

## 8. Risks & Assumptions

**Key Assumptions**
1. Zero-result queries represent real user intent (not bots/junk)
2. Manual classification can be reliably scaled
3. Fixing zero-results will convert to revenue (users will retry)

**Data Quality Assumptions**
- Query logs capture the actual query as typed (not normalized)
- Bot traffic has been filtered from logs

**Risks**

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Manual classification is subjective | M | M | Have 2 people classify independently, measure agreement (require >70%) |
| ML team dismisses simple fixes | M | M | Show ROI of quick wins vs. time to ML solution |
| Inventory issues get blamed on search | M | M | Clearly separate "search can't find it" from "we don't sell it" — use catalog lookup |

---

## 9. Ethics & Privacy

| | Yes | No | Notes |
|---|---|---|---|
| Requires PII? | [ ] | [x] | Query-level only, no user data |
| Risk of bias against protected groups? | [ ] | [x] | |
| GDPR / Privacy compliance reviewed? | [x] | [ ] | Aggregate query logs, no personal data |

---

## 10. Pre-Mortem

_It's 3 months from now and this project failed. What happened?_

We found that spelling errors were 45% of failures and recommended a spelling correction system. Engineering built it, but the speller was too aggressive — it "corrected" valid brand names ("Febreeze" → "Freeze") and niche product terms ("açaí" → "acai" → wrong category). Search relevance dropped 15%. We should have tested with edge cases and set a guardrail for relevance before launch. The exploratory work was valuable, but we skipped the validation step.

---

_"Your job is never to optimize a metric; it's to improve the experience that the metric measures."_
