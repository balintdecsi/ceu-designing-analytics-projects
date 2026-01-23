# Analytics Project Brief

**Project Name:** LearnLoop Product Strategy & Retention Analysis

**Date:** January 18, 2026

**Prepared by:** Bálint Décsi

---

## 1. Problem & Decision

**What business question or decision will this analysis inform?**

Growth has stalled, and the CEO wants to pivot strategy from acquisition to retention and expansion. The core decision is: **Which product features (Learning Paths, Cohort-based courses, or Skill Assessments) should I prioritize for investment in the next 12 months to drive retention and LTV?**

**Who is asking, and why now?**

*   **Rebecca Torres (CEO):** Asking because she needs to prove to the board that the new retention strategy is working and viable.
*   **Michael Chang (Head of Product):** Asking because he wants to validate his bet on "Learning Paths" and potentially make it the default experience.
*   **Enterprise Sales Team:** Asking because they need proof of "learning outcomes" to close deals.

**Who is the ultimate decision maker?**

**Rebecca Torres (CEO)** determines the strategic roadmap and budget allocation.

**Hypothesis**

I believe **Learning Paths and Cohort-based courses** drive significantly higher retention and skill acquisition than unstructured browsing because they provide guidance and accountability. I expect this lift to be high enough to justify the higher operational cost of Cohorts and the "tunneling" effect of Paths.

---

## 2. Metrics

**Primary Metric**

| Metric name | Definition | Baseline | Target |
|-------------|------------|----------|--------|
| **Pro Subscription Retention Rate (Month 3)** | **Event/Table:** `subscriptions` table<br>**Numerator:** Users with `status = 'active'` at Day 90<br>**Denominator:** Users with `signup_event` in Month 0<br>**Filters:** Exclude Enterprise, Free Trials<br>**Time Window:** Rolling 90 days | *Current Avg* | *+10% lift* |

**Counter-Metrics** _(2-3 max — what breaks if we optimize the primary metric?)_

| Counter-metric | Type | Why it could break | How I'll measure |
|----------------|------|-------------------|-------------------|
| **1. Content Consumption Diversity** | Tradeoff | If Paths are too rigid, users see fewer courses, potentially hiding new/diverse content (Aisha's concern). | Unique `course_id` accessed per active user / Month |
| **2. Gross Margin per User** | Guardrail | Cohorts are 3x more expensive. I cannot let retention gains come at an unsustainable cost. | (Revenue - Instructor Costs - Hosting) / Active Users |
| **3. New User Activation Rate** | Guardrail | If I force "Learning Paths" too early as the default, I might overwhelm casual users and drop activation. | % of signups who complete 1st lesson within 7 days |

_Guardrail = must not worsen. Tradeoff = may worsen within acceptable bounds._

---

## 3. Stakeholder Map

| | High Interest | Low Interest |
|---|---|---|
| **High Power** | **Rebecca Torres (CEO)** (Manage Closely) | **CFO** (Keep Satisfied - cares about margin) |
| **Low Power** | **Michael Chang (Product)**, **Aisha Williams (Content)**, **Sales** (Keep Informed) | **Engineering Team** (Monitor) |

**Champions:**
*   **Michael Chang:** Championing "Learning Paths". Will support any data proving their value.

**Blockers:**
*   **Aisha Williams (Head of Content):** Concerned that features hide her team's new content. *Why:* She fears quality degradation and that "older" content in paths will define the brand.
*   **CFO:** Potential blocker for "Cohort courses" due to high instructor costs.

---

## 4. Methodology

| Method | Hypothesis being tested | Data required |
|--------|------------------------|---------------|
| 1. **Retention Analysis (Cohort View)** | Users who engage with Learning Paths/Cohorts retain longer than those who don't. | Users, Enrollments, Path Progress, Subscription Status |
| 2. **Ecosystem Analysis (Propensity Matching)** | The retention lift is due to the *feature*, not just because "better" users choose the feature (Selection Bias). | User demographics, early behavior data |
| 3. **Outcome Analysis (Pre/Post Delta)** | Users in Cohorts/Paths show higher skill improvement scores. | Assessment Scores table |

**Data Availability**

| Data needed | Available? | If no, fallback |
|-------------|-----------|-----------------|
| Web Engagement Data | Yes | - |
| Mobile App Engagement | **Partial** | Flag as limitation; Exclude mobile-only users from deep behavioral analysis |
| Enterprise vs. Individual | **Mixed** | Use domain matching or heuristic to segment if flag is unreliable |

**Data Validity Checks (Stop/Go)**

_What must be true before analysis proceeds? List checks to validate before drawing conclusions._

| Check | How to validate | Stop if... |
|-------|-----------------|------------|
| **Mobile Data Completeness** | Compare `minutes_watched` distribution for mobile-primary vs web-primary users. | Mobile engagement is < 50% of Web (suggests broken tracking) |
| **Duplicate Accounts** | `COUNT(DISTINCT user_id)` vs `COUNT(*)` (or email hash check). | Duplicates > 10% of total user base |

---

## 5. Scope & Deliverables

**In Scope**
- Analysis of retention drivers: Learning Paths, Cohorts, Assessments.
- Impact on Skill Improvement (Assessment scores).
- Recommendations for 12-month product roadmap.
- Segmenting by Individual vs. Enterprise (where possible).

**Out of Scope**
- **UI/UX Redesign:** I will not address Michael's request to "make Learning Paths look good" (Design task, not analytics).
- **User Surveys:** I cannot survey users (constraint).
- **Acquisition Channel Analysis:** Focus is strictly on retention/expansion.

**Final Deliverables**

- [x] Slide deck / Executive summary (for Rebecca/Board)
- [x] Written report (Methodology & Details)
- [ ] Dashboard (Tableau / PowerBI / other)
- [ ] Code / Reproducible pipeline
- [ ] Cleaned dataset
- [ ] Other: _______________

---

## 6. Success & Decision Criteria

**Analytical Success** _(how do I know the analysis was sound?)_
- I can isolate the causal impact of features (via PSM or similar) with p<0.05.
- I identify at least one segment where "Cohorts" are ROI positive.

**Business Success** _(how do I know it drove impact?)_
- CEO adopts the roadmap recommendation.
- Sales team successfully uses "learning outcome" stats to close an Enterprise deal.

**Decision Forum:** Monthly Strategy Review **Action Owner:** Rebecca Torres

**Decision Criteria**

| If I find... | I will... |
|---------------|------------|
| Learning Paths lift retention > 10% | Recommend making Paths the default homepage experience. |
| Cohorts are ROI negative (even with high retention) | Recommend limiting Cohorts to Enterprise contracts only (high WTP). |
| No features drive significant retention | Recommend pivoting to qualitative research to understand churn reasons. |

**Action Thresholds**

_What minimum effect size or confidence level justifies action?_
- I will only recommend making Paths default if: **Retention lift > 5% AND User Activation does not drop.**
- I will not act if: **Results are not statistically significant (p > 0.10).**

---

## 7. Timeline

| Milestone | Date |
|-----------|------|
| Data access secured & validation | Jan 20 |
| Initial findings review (with Michael/Aisha) | Jan 25 |
| Final delivery (to CEO) | Jan 30 |

---

## 8. Risks & Assumptions

**Key Assumptions**
1. **Assessment Validity:** I assume pre/post scores accurately reflect *actual* learning, not just test-taking familiarity.
2. **Feature Stability:** I assume the "Learning Path" feature hasn't changed drastically in the last 6 months (polluting the data).

**Risks**

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| **Selection Bias** | High | High | Use Propensity Score Matching to control for "good user" bias. |
| **Privacy (Enterprise)** | Medium | High | Aggregate Enterprise data; do not report individual employee scores. |
| **Stakeholder Pushback** | Medium | Medium | Pre-brief Aisha if findings show "Older content" in Paths performs well. |

---

## 9. Ethics & Privacy

| | Yes | No | Notes |
|---|---|---|---|
| Requires PII? | [ ] | [x] | Analysis should be on pseudo-anonymized IDs. |
| Risk of bias against protected groups? | [x] | [ ] | Check if "Cohorts" (premium/expensive) exclude lower-income users. |
| GDPR / Privacy compliance reviewed? | [x] | [ ] | Ensure Enterprise data usage complies with client contracts. |

---

## 10. Pre-Mortem

_It's 3 months from now and this project failed. What happened?_

**The "Power User" Trap:**
I recommended making **Learning Paths** the default experience because my analysis showed a massive +20% retention lift for Path users.
Three months after rollout, site-wide retention **dropped**.
**Why?** My analysis failed to account for selection bias. The users who originally used Paths were my most motivated "power users" who would have retained anyway. By forcing the rigid Path structure on *all* users (including casual browsers), I increased friction and annoyance, causing casual users to churn. I confused correlation with causation.