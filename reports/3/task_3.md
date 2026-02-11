## Week 3: Analysis Methodology Selection (Due: Feb 6)

### Prompt

Practice selecting and justifying foundational analyses for a real business problem.

**The Mini-Case: FreshMart Grocery Delivery**

> FreshMart is an online grocery delivery service operating in 8 cities. Last quarter, they noticed that first-order customers who receive their delivery within the 1-hour "Express" window have a 45% higher 30-day reorder rate than those who receive standard 3-hour delivery.
>
> The VP of Operations wants to invest $2M in expanding Express capacity.
>
> The CFO is skeptical: "Maybe Express customers are just wealthy professionals who would order anyway — they self-select into Express because they value their time, not because Express delivery makes them loyal."

**Available Data:**
- `orders`: order_id, customer_id, order_date, delivery_window_selected, actual_delivery_time, order_value
- `customers`: customer_id, signup_date, zip_code, first_order_date
- `census_data`: zip_code, median_income, population_density

**Your submission should include:**

1. **Analysis Selection (Choose 2-3)**
   - Which foundational analyses from class would help answer this question?
   - For each, explain:
     - What specific question does this analysis answer?
     - What would you learn from it?
     - What would it NOT tell you?

   *Reminder — The 9 Foundational Analyses:*
   - Acquisition: Funnel, Channel Attribution, Campaign Effectiveness, CAC/LTV
   - Retention: Retention Analysis, Power User Analysis, Failure Analysis
   - Growth: Expansion & Monetization, Ecosystem Analysis

2. **Data Validity Checks (Stop/Go Gates)**
   - What must be true about the data before you can draw conclusions?
   - For each check:
     - What are you validating?
     - How would you validate it?
     - What would make you stop the analysis?

3. **Causation vs. Correlation Challenge**
   - The CFO's concern is about selection bias. How would you address it?
   - What additional data or analysis design would help establish causation?
   - What would you tell stakeholders if you CAN'T establish causation?

4. **Counter-Metric**
   - If the VP is right and you recommend Express expansion, what could break?
   - Identify 1 counter-metric and explain why it matters

**Reflection:** What did this exercise reveal about the difficulty of analysis selection in ambiguous situations?

---

*Before submitting: What decision would this analysis drive? What could break if it succeeds?*

---
