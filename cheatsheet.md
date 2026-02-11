# Designing Analytics Projects - Cheat Sheet

### 1. THE ANALYTICS PROJECT BRIEF
**Purpose:** Prevent failure (Wrong problem/metric/stakeholders/scope). **"Why Now":** Context/Urgency.

| # | Section | Key Question & Notes |
|:-:|---|---|
| **1** | **Problem** | Decision? Who asks & why now? **Ultimate decision maker**? |
| **2** | **Metrics** | **Primary:** Precise def (SQL-ready). **Counter:** Guardrails (Hard stop) vs Tradeoffs. |
| **3** | **Stakeholders** | Power-Interest Grid. **Champions** (Advocates) & **Blockers** (Resistance). |
| **4** | **Methodology** | Analyses? Data availability? **Validity Checks** (Stop/Go gates). |
| **5** | **Scope** | In Scope vs. **Out of Scope** (prevents scope creep). |
| **6** | **Success** | Analytical (Stat sig) vs Business (Action). **Decision Criteria Table** (Pre-commit). |
| **7** | **Timeline** | Key milestones. |
| **8** | **Risks** | Assumptions made. |
| **9** | **Ethics** | PII, Bias risks. |
| **10** | **Pre-Mortem** | **"It failed. What happened?"** Causal story from future. Surfaces hidden risks. |

### 2. STAKEHOLDER MANAGEMENT & INFLUENCE
**Power-Interest Grid:** Hi/Hi=**Manage Closely**; Hi/Lo=**Keep Satisfied**; Lo/Hi=**Keep Informed**; Lo/Lo=**Monitor**.
**Blockers:** Identify motivation (Budget, Ego, Workload). **Pre-brief privately** (No surprises).

**The Influence Compass (4 Strategies):**
*   **Authority (North):** Leverage hierarchy. *"The CEO asked..."* (For: Hierarchy-respecting).
*   **Credibility (South):** Leverage expertise. *"Data Science validated..."* (For: Technical/Skeptics).
*   **Social Proof (West):** Leverage data/peers. *"70% of peers do..."* (For: Risk-averse).
*   **Consistency (East):** Leverage alignment. *"Aligns with Q2 goals..."* (For: Strategy-focused).

### 3. KEY CONCEPTS & DEFINITIONS
*   **Goodhart's Law:** "When a measure becomes a target, it ceases to be a good measure."
*   **Counter-Metrics:** **Guardrail:** Hard stop (Fraud). **Tradeoff:** Acceptable cost (Short-term rev). **"What Breaks":** Direct neg, Quality, Segments.
*   **Selection Bias:** Sample != Population (e.g., analyzing only onboarded users).
*   **Processing Fluency:** Simple = Trustworthy (30s rule). **Message Theory:** "To **[Person]** about **[Topic]**, rec is **[Action]**."

### 4. ACQUISITION ANALYSES ("Getting Customers")

| Analysis | Core Question | Key Concepts & Notes | Common Pitfalls / Counter-Metrics |
|---|---|---|---|
| **Funnel** | Where do they drop? | **Events:** Define precisely. **Views:** Abs vs %. **Segment:** Device, Source. | **Pitfalls:** Missing events, cross-device.<br>**CM:** AOV, Fraud Rate, Support Tickets. |
| **Attribution** | Who gets credit? | **Models:** First (Aware), Last (Close), Linear, Time-Decay, U-Shaped. **Windows:** 7d vs 30d. | **Pitfalls:** No "right" model. Find disagreements.<br>**CM:** Brand Awareness, Lead Quality. |
| **Campaign** | Did X cause Y? | **Counterfactual:** What happened w/o campaign? **Methods:** Holdout (Gold), Geo-Match, Synthetic. | **Pitfalls:** **Corr != Causation**. Pull-forward. Contamination.<br>**Confounds:** Competitor actions. |
| **CAC / LTV** | Unit Economics | **CAC:** Cost/Acq. **LTV:** Rev * Margin * Life. **Ratio:** > 3:1 (SaaS). **Payback:** Months to recover. | **Pitfalls:** Blended CAC hides poor channels. LTV on rev not margin. |

### 5. RETENTION & GROWTH ANALYSES ("Keeping & Growing")

| Analysis | Core Question | Key Concepts & Notes | Common Pitfalls / Counter-Metrics |
|---|---|---|---|
| **Retention** | Do they return? | **Active:** Strict def. **DN** vs **Rolling**. **Curve:** Flattens = PMF. **Cohorts:** Compare trends. | **Pitfalls:** "Sugar Diet" (Growth masks churn). **Driver Trap:** Corr != Causation. Test mandates!<br>**CM:** Signup completion, "Zombie" retention. |
| **Power User** | Who matters? | **Pareto:** Top % drive value. **Conc:** Gini. **Strategy:** Optimize Power OR Broaden Base. | **Pitfalls:** Alienating casual majority.<br>**CM:** Casual user satisfaction, Content diversity. |
| **Failure** | What's broken? | **Exploratory.** Manual sample. **Taxonomy:** Categorize. **Size:** By **Impact ($)** not Vol. | **Pitfalls:** Skipping manual review. Bad taxonomy.<br>**CM:** Relevance (bad results < zero results). |
| **Expansion** | Why pay more? | **Freemium:** Limits=triggers. **Drivers:** Limits, Discovery. **Dilemma:** High limit (no conv) vs Low. | **Pitfalls:** "High-value" free != ready.<br>**CM:** Free user retention, Brand trust. |
| **Ecosystem** | 1+1 = 3 or 1.5? | **Complements:** A helps B. **Substitutes:** A hurts B. **Selection Bias:** Multi-prod users engaged. | **Pitfalls:** Assuming causation. Use holdouts/natural exp.<br>**CM:** Cannibalization. |

### 6. APPLIED SCENARIOS & TIPS
*   **Red Flags:** "Explore data", No decision, No hypothesis, "Why now?" undefined.
*   **B2B Attribution:** Long cycles. Last-touch undervalues content. Use Multi-touch/Time-Decay.
*   **Zero Results Search:** High impact ($). Counter-metric: Relevance (don't show junk).
*   **Pre-Mortem Strategy:** Write a **causal story** from the future. "We did X, Y happened, because Z."
*   **Validation:** Stop/Go gates, Inter-rater reliability (>80%), A/B Tests / Holdouts.