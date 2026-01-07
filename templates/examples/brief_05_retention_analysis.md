# Analytics Project Brief

**Project Name:** New User Retention Driver Analysis **Date:** January 2026

**Prepared by:** Product Analytics, SnapGram (Photo Sharing App)

---

## 1. Problem & Decision

**What business question or decision will this analysis inform?**

SnapGram's D7 retention (users active 7 days after signup) dropped from 42% to 35% over six months. We're acquiring more users than ever, but they're not sticking. We need to identify what drives retention and which product levers can recover the lost 7 points.

**Who is asking, and why now?**

VP Product escalated after MAU growth flattened despite record signups. This is "sugar diet growth" — big acquisition masking a retention crisis. If we don't fix it, we plateau.

**Who is the ultimate decision maker?**

VP Product owns the roadmap. CEO monitors MAU as a board metric.

**Hypothesis**

_We believe users who add at least 3 friends in their first 48 hours retain at 2x the rate of those who don't, and our onboarding doesn't push friend-adding hard enough._

---

## 2. Metrics

**Primary Metric**

| Metric name | Definition | Baseline | Target |
|-------------|------------|----------|--------|
| D7 Retention Rate | Users with ≥1 `app_open` event on calendar day 7 / Users with `signup_complete` on day 0 | 35% | Return to 42% within 2 quarters |

**Counter-Metrics** _(2-3 max — what breaks if we optimize the primary metric?)_

| Counter-metric | Type | Why it could break | How we'll measure |
|----------------|------|-------------------|-------------------|
| 1. Signup completion rate | Guardrail | Aggressive onboarding may increase abandonment | Signup funnel completion % |
| 2. Engagement depth | Guardrail | Users might return but not engage ("zombie retention") | Time spent per DAU, actions per session |
| 3. Notification opt-out | Tradeoff | Pushy re-engagement causes fatigue | Notification permission rate over time |

_Guardrail = must not worsen. Tradeoff = may worsen within acceptable bounds._

---

## 3. Stakeholder Map

| | High Interest | Low Interest |
|---|---|---|
| **High Power** | VP Product, CEO, Head of Growth | CFO |
| **Low Power** | Onboarding PM, Notifications PM, Data Science | Marketing |

**Champions:** VP Product (owns the problem), Onboarding PM (wants evidence to improve their flow)

**Blockers:** Head of Growth (worried onboarding friction will hurt their signup KPIs — their bonus is tied to signup volume, not retention), Notifications PM (defensive because "more notifications" is often the lazy answer, and they've been burned before by aggressive push strategies)

_Strategy: Frame as "high-impact, low-friction changes." Show that retention improvements compound into Growth's signup ROI. Commit to testing, not mandating._

---

## 4. Methodology

| Method | Hypothesis being tested | Data required |
|--------|------------------------|---------------|
| 1. Retention driver analysis (logistic regression) | Which first-week behaviors predict D7 return? | Behavioral events, D7 activity flag |
| 2. Cohort-over-cohort comparison | What changed between high and low retention cohorts? | Signup dates, product changes log |
| 3. User journey mapping | Where do churned users diverge from retained? | Session-level event sequences |

**Data Availability**

| Data needed | Available? | If no, fallback |
|-------------|-----------|-----------------|
| User signups with D7 activity flag | Yes | — |
| First-week behavioral events | Yes | — |
| Product changes log by date | Partial | Reconstruct from release notes |

**Data Validity Checks (Stop/Go)**

| Check | How to validate | Stop if... |
|-------|-----------------|------------|
| D7 flag is accurate | Spot-check 100 users manually | >2% error rate |
| Event logging consistent across app versions | Compare event volume by app version | Major version has >20% different event rates |

---

## 5. Scope & Deliverables

**In Scope**
- New users from last 6 months
- D7 retention (primary), D1 and D30 as supporting
- Behavioral drivers in first 7 days
- Segmentation by acquisition source, device, geography

**Out of Scope**
- Existing user churn — new user focus only
- Win-back campaigns — separate project
- Engagement depth analysis — this is return rate, not session quality

**Final Deliverables**

- [x] Slide deck / Executive summary
- [x] Written report
- [ ] Dashboard (Tableau / PowerBI / other)
- [x] Code / Reproducible pipeline
- [ ] Cleaned dataset

---

## 6. Success & Decision Criteria

**Analytical Success**
- Identify 3-5 statistically significant retention drivers
- Quantify: "Users who do X retain at Y% vs. Z%"
- Explain >50% of the 7-point retention drop

**Business Success**
- Product team has prioritized roadmap for Q2
- Clear A/B test hypotheses for top 2 drivers

**Decision Forum:** Product Review (Fridays) **Action Owner:** Onboarding PM

**Decision Criteria**

| If we find... | We will... |
|---------------|------------|
| Friend-adding is top driver | Redesign onboarding to prioritize friend connections (A/B test) |
| Content consumption is top driver | Improve recommendations for new users |
| Notification engagement is key | Optimize notification timing and content |
| Drop caused by acquisition source shift | Reallocate marketing to higher-quality channels |
| _(inconclusive / null result)_ | Run qualitative user research (15 interviews) to generate new hypotheses |

**Action Thresholds**
- We will only recommend product changes if: effect size ≥5pp retention difference AND p<0.05
- We will not act if: driver explains <10% of variance or sample <10K users

---

## 7. Timeline

| Milestone | Date |
|-----------|------|
| Data access secured | Jan 6 |
| Initial findings review | Jan 18 |
| Final delivery | Jan 28 |

---

## 8. Risks & Assumptions

**Key Assumptions**
1. Behavioral drivers are causal, not just correlated (selection bias risk)
2. First-week is the right window (not first day or month)
3. D7 is a valid proxy for long-term retention

**Data Quality Assumptions**
- Event logging is consistent across app versions
- Attribution to signup source is accurate

**Risks**

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Correlation ≠ causation (selection bias) | H | H | Recommend A/B tests before mandating changes |
| Product changes confound cohort analysis | M | M | Control for signup date, note major releases |
| Growth blocks onboarding friction | M | M | Show ROI of retention on their metrics |

---

## 9. Ethics & Privacy

| | Yes | No | Notes |
|---|---|---|---|
| Requires PII? | [x] | [ ] | User-level behavioral data |
| Risk of bias against protected groups? | [ ] | [x] | |
| GDPR / Privacy compliance reviewed? | [x] | [ ] | Using consented analytics data |

_Mitigation: All outputs aggregated. No individual data in reports._

---

## 10. Pre-Mortem

_It's 3 months from now and this project failed. What happened?_

We found friend-adding was the #1 predictor. Product added a mandatory "add 5 friends" step. Signup completion dropped 30%. The correlation was selection bias — engaged users organically add friends, but forcing it didn't make disengaged users engaged. We should have recommended an A/B test, not a mandate.

---

_"Your job is never to optimize a metric; it's to improve the experience that the metric measures."_
