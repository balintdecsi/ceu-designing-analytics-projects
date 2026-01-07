# ECBS5228A Slide Figures — Designer Brief Catalog

This document contains detailed briefs for a graphic designer to create infographics and visualizations for the course slides. Each entry specifies the filename, context, and design requirements.

**Instructions for Designer:**
- Save all images to `figures/images/` using the exact filenames specified
- Recommended format: PNG with transparent background where appropriate
- Recommended dimensions: 1920x1080 (16:9) unless otherwise noted
- Style: Clean, professional, suitable for business analytics education
- Color palette: Suggest using a consistent palette across all figures (blues, grays, with accent colors for emphasis)

---

## Table of Contents

1. [FIG-01: Basic Funnel Diagram](#fig-01-basic-funnel-diagram)
2. [FIG-02: Funnel Output Visualization](#fig-02-funnel-output-visualization)
3. [FIG-03: Counterfactual Line Chart](#fig-03-counterfactual-line-chart)
4. [FIG-04: Synthetic Control Visualization](#fig-04-synthetic-control-visualization)
5. [FIG-05: Pull-Forward Bar Chart](#fig-05-pull-forward-bar-chart)
6. [FIG-06: LTV Cohort Curve](#fig-06-ltv-cohort-curve)
7. [FIG-07: Retention vs Acquisition Comparison](#fig-07-retention-vs-acquisition-comparison)
8. [FIG-08: Classic Retention Curve](#fig-08-classic-retention-curve)
9. [FIG-09: Pareto/Lorenz Curve](#fig-09-paretolorenz-curve)
10. [FIG-10: Freemium Funnel](#fig-10-freemium-funnel)
11. [FIG-11: Limit Tradeoff Curve](#fig-11-limit-tradeoff-curve)
12. [FIG-12: Power-Interest Grid](#fig-12-power-interest-grid)
13. [FIG-13: Processing Fluency Comparison](#fig-13-processing-fluency-comparison)
14. [FIG-14: Influence Compass](#fig-14-influence-compass)

---

## FIG-01: Basic Funnel Diagram

**File:** `images/block_02_funnel_basic.png`
**Block:** 2 — Acquisition Analyses
**Slide:** "What is Funnel Analysis?"

### Context
This is the first introduction to funnel analysis. Students need to immediately grasp the concept of progressive narrowing through stages. The visual should make the "funnel" metaphor instantly clear.

### Design Brief
Create a classic funnel shape showing 4 stages narrowing from top to bottom:

| Stage | Percentage | Users |
|-------|------------|-------|
| Visit | 100% | (widest) |
| Sign Up | 40% | |
| Activate | 25% | |
| Subscribe | 10% | (narrowest) |

**Key elements:**
- Actual funnel shape (wide at top, narrow at bottom)
- Each stage clearly labeled on the left
- Percentages shown on the right
- Visual proportions should roughly match the percentages
- Use progressively darker/more saturated color as you go down (to show "concentration")

**Style notes:**
- Clean, minimal — this is a concept introduction
- No data clutter
- Should be understandable in 2 seconds

### Technical Notes
- Dimensions: 1920x1080 or 1200x800
- Labels must be legible at presentation scale
- Consider slight 3D effect for the funnel shape, but keep it subtle

---

## FIG-02: Funnel Output Visualization

**File:** `images/block_02_funnel_output.png`
**Block:** 2 — Acquisition Analyses
**Slide:** "What the Output Looks Like"

### Context
This shows students what a real funnel analysis deliverable looks like. The key insight is identifying where the biggest drop happens (not just the biggest percentage drop, but the biggest absolute user loss).

### Design Brief
Create a horizontal bar chart OR funnel visualization showing an e-commerce checkout funnel:

| Stage | Users |
|-------|-------|
| Cart | 10,000 |
| Address | 8,500 |
| Shipping | 7,800 |
| Payment | 6,900 |
| Confirm | 6,100 |

**Key elements:**
- Horizontal bars (or funnel stages) with user counts
- **Highlight the Cart → Address drop** (1,500 users lost) — this is the biggest absolute drop
- Show drop-off numbers between stages (e.g., "-1,500", "-700", "-900", "-800")
- Use a callout or annotation pointing to Cart → Address saying something like "Biggest drop: 1,500 users"

**Style notes:**
- More "data-y" than FIG-01 — this looks like actual output
- Could use a subtle red/warning color for the biggest drop
- Include light gridlines for readability

### Technical Notes
- Dimensions: 1920x1080
- Numbers must be clearly readable
- The "biggest drop" callout is the key teaching moment

---

## FIG-03: Counterfactual Line Chart

**File:** `images/block_02_counterfactual.png`
**Block:** 2 — Acquisition Analyses
**Slide:** "The Counterfactual Problem"

### Context
This is a conceptually important slide about causal inference. Students need to understand that we observe what happened, but the "what would have happened without the campaign" is estimated/hypothetical.

### Design Brief
Create a line chart with two lines:

**X-axis:** Time (show period before, during, and after a campaign)
**Y-axis:** Sales (or revenue)

**Elements:**
1. **Solid line:** "What happened" — shows sales going UP during the campaign period
2. **Dashed line:** "What would have happened" (the counterfactual) — shows the baseline trajectory without the campaign
3. **Shaded area** between the two lines during the campaign period = "Incremental effect"
4. **Vertical line or shaded region** marking the campaign period

**Labels:**
- "Observed" for the solid line
- "Counterfactual (estimated)" for the dashed line
- "Incremental lift" for the shaded area
- "Campaign period" for the vertical marker

**Style notes:**
- The dashed line should clearly look hypothetical/estimated
- The shaded "incremental" area is the key visual — make it prominent but not garish
- Use muted colors; this is a conceptual diagram, not flashy

### Technical Notes
- Dimensions: 1920x1080
- Include a small note/caption: "We observe the solid line. The dashed line is what we estimate."
- Time axis doesn't need specific dates — can be generic (Week 1, Week 2, etc.)

---

## FIG-04: Synthetic Control Visualization

**File:** `images/block_02_synthetic_control.png`
**Block:** 2 — Acquisition Analyses
**Slide:** "Synthetic Control Visualization"

### Context
This shows the synthetic control method — using a weighted combination of control markets to create a "synthetic" version of the treatment market. Students see how the synthetic tracks the actual pre-campaign, then diverges post-campaign.

### Design Brief
Create a line chart showing:

**X-axis:** Time (months, showing before and after campaign start)
**Y-axis:** Sales

**Elements:**
1. **Solid line:** "Phoenix (Actual)" — the real sales in the treatment market
2. **Dashed line:** "Synthetic Phoenix" — weighted combination of control markets
3. **Vertical line** at campaign start date
4. **Before campaign:** The two lines track closely together
5. **After campaign:** The lines diverge — actual Phoenix is higher than synthetic

**Labels:**
- "Phoenix (Actual)"
- "Synthetic Phoenix (weighted controls)"
- "Campaign starts" at the vertical line
- Optionally show the gap labeled as "Treatment effect"

**Style notes:**
- The close tracking pre-campaign is visually important — it shows the synthetic is a good match
- The divergence post-campaign is the key insight
- Clean, minimal — focus on the two lines and the divergence

### Technical Notes
- Dimensions: 1920x1080
- The pre-campaign fit should look tight; post-campaign divergence should be clear
- Consider subtle shading for pre vs. post periods

---

## FIG-05: Pull-Forward Bar Chart

**File:** `images/block_02_pull_forward.png`
**Block:** 2 — Acquisition Analyses
**Slide:** "Pull-Forward: The Hidden Trap"

### Context
This illustrates "pull-forward" — when a campaign doesn't create new demand, it just moves purchases earlier. The visual should make students immediately see the problem.

### Design Brief
Create a bar chart showing monthly sales:

| Month | This Year | Last Year (reference) |
|-------|-----------|----------------------|
| October | Normal | Normal |
| November | HIGH (campaign) | Normal |
| December | HIGH (campaign) | Normal |
| January | LOW | Normal |
| February | Normal | Normal |

**Key elements:**
- November and December show big spikes (the campaign period)
- January shows a dip BELOW last year's January
- Include a subtle reference line or ghost bars for "last year" to show January is actually down YoY
- Annotation: "Did the campaign create demand, or just move it earlier?"

**Style notes:**
- Use a bright/positive color for Nov-Dec spike
- Use a warning/red color for the January dip
- The visual story: "Look at that great campaign! ...wait, look at January"

### Technical Notes
- Dimensions: 1920x1080
- The January dip is the key insight — make sure it's visually prominent
- Caption/annotation is important for teaching moment

---

## FIG-06: LTV Cohort Curve

**File:** `images/block_02_ltv_curve.png`
**Block:** 2 — Acquisition Analyses
**Slide:** "LTV Visualization"

### Context
This shows how LTV is calculated from cohort data — observed retention/revenue that then gets projected forward. The uncertainty in the projection is a key teaching point.

### Design Brief
Create a cohort retention/revenue curve:

**X-axis:** Months since signup (0, 3, 6, 9, 12, 18, 24, 36)
**Y-axis:** % still active OR cumulative revenue per user

**Elements:**
1. **Solid line (observed):** Actual data for months 0-12
2. **Dashed line (projected):** Projection for months 12-36
3. **Shaded confidence band** around the projection showing uncertainty
4. **Curve shape:** Steep drop early (months 0-3), then gradually flattening

**Labels:**
- "Observed" for solid portion
- "Projected" for dashed portion
- "Uncertainty increases" annotation pointing to widening confidence band

**Style notes:**
- The curve should show classic retention shape (steep early, flattening)
- The uncertainty band should visibly widen as you go further into projection
- Professional, data-visualization style

### Technical Notes
- Dimensions: 1920x1080
- The observed/projected boundary is the key visual break
- Make the confidence band visually distinct but not overwhelming

---

## FIG-07: Retention vs Acquisition Comparison

**File:** `images/block_03_retention_vs_acquisition.png`
**Block:** 3 — Retention & Growth Analyses
**Slide:** "Why Retention Matters More Than Acquisition"

### Context
This shows why retention improvements compound while acquisition is linear. Two scenarios that look similar on acquisition end up very different on active users.

### Design Brief
Create a side-by-side comparison of two scenarios:

**Scenario A:**
- 1,000 signups/month
- 5% D30 retention
- Result: 50 active users after month 1

**Scenario B:**
- 500 signups/month
- 40% D30 retention
- Result: 200 active users after month 1

**Visual approach options:**
1. **Two funnels side by side** — A has wide top but tiny bottom; B has narrower top but much larger bottom
2. **Stacked bar or pictograph** — Show the dramatic difference in "active users" outcome
3. **Simple math visual** — Show the multiplication: 1000 × 5% = 50 vs 500 × 40% = 200

**Key message:** "Lower acquisition + higher retention wins"

**Style notes:**
- The contrast should be stark and immediate
- Scenario B should "win" visually despite lower acquisition
- Could use green/positive color for B's outcome

### Technical Notes
- Dimensions: 1920x1080
- The "200 vs 50" comparison is the punchline — make it visually dominant
- Include the calculation so students can verify

---

## FIG-08: Classic Retention Curve

**File:** `images/block_03_retention_curve.png`
**Block:** 3 — Retention & Growth Analyses
**Slide:** "The Retention Curve"

### Context
This is THE canonical retention curve shape. Students need to internalize: steep early drop, then gradual flattening. The flattening point represents "true" retention.

### Design Brief
Create a retention curve:

**X-axis:** Days since signup (0, 1, 7, 14, 30, 60, 90)
**Y-axis:** % retained (0-100%)

**Curve shape:**
- Day 0: 100%
- Day 1: ~65% (steep drop)
- Day 7: ~40%
- Day 14: ~32%
- Day 30: ~25%
- Day 60: ~22%
- Day 90: ~20% (flattening)

**Key elements:**
- The curve should show classic "steep then flat" shape
- Annotation pointing to the flattening region: "The flattening is where you find your core users"
- Optional: subtle shading or marker showing the "steep drop" phase vs "stable" phase

**Style notes:**
- Clean, textbook-quality visualization
- The shape itself is the lesson
- Make the flattening visually clear

### Technical Notes
- Dimensions: 1920x1080
- Use realistic-looking numbers
- The annotation about "core users" is important — include it in the image

---

## FIG-09: Pareto/Lorenz Curve

**File:** `images/block_03_pareto_curve.png`
**Block:** 3 — Retention & Growth Analyses
**Slide:** "The 80/20 Rule (Pareto)"

### Context
This shows engagement concentration — a small percentage of users drive most of the value. The Lorenz curve makes this inequality visible.

### Design Brief
Create a Lorenz curve (cumulative distribution):

**X-axis:** % of users (cumulative, sorted by engagement) — 0% to 100%
**Y-axis:** % of engagement/viewing hours (cumulative) — 0% to 100%

**Elements:**
1. **Diagonal line:** "Perfect equality" (if everyone contributed equally)
2. **Curved line below:** Actual distribution showing concentration
3. **Key annotation:** Mark where 20% of users = 80% of engagement
4. **Shaded "power user" segment:** Highlight the top 10-20% of users

**The curve should show:**
- At 20% of users → ~80% of engagement
- At 50% of users → ~92% of engagement
- Bottom 50% contribute very little

**Style notes:**
- Classic Lorenz curve style
- The gap between the diagonal and the curve shows inequality
- "Power user" segment should be visually called out

### Technical Notes
- Dimensions: 1920x1080
- Include axis labels clearly
- The "20% → 80%" point is the key teaching moment

---

## FIG-10: Freemium Funnel

**File:** `images/block_03_freemium_funnel.png`
**Block:** 3 — Retention & Growth Analyses
**Slide:** "The Freemium Model"

### Context
This shows the freemium business model structure — large free base, smaller paid tier, even smaller premium tier. Students should see the pyramid/funnel shape.

### Design Brief
Create a pyramid or inverted funnel showing three tiers:

| Tier | Users | Revenue |
|------|-------|---------|
| Free | 2,000,000 | $0 |
| Paid | 180,000 (9% conversion) | $$ |
| Premium | 25,000 | $$$ |

**Visual approach:**
- **Pyramid/triangle** with widest at bottom (Free), narrowest at top (Premium)
- OR **Inverted funnel** showing conversion flow
- Show user counts at each level
- Indicate the conversion percentages (9% free→paid)

**Key elements:**
- The massive free base should dominate visually
- The paid tier is much smaller
- Premium is tiny but high-value
- Arrows or flow lines showing "conversion" between tiers

**Style notes:**
- Could use different colors for each tier (gray for free, blue for paid, gold for premium)
- The size proportions should roughly match the user counts
- Clean, infographic style

### Technical Notes
- Dimensions: 1920x1080
- The visual proportions matter — free tier should look MUCH bigger
- Include the 9% conversion rate label

---

## FIG-11: Limit Tradeoff Curve

**File:** `images/block_03_limit_tradeoff.png`
**Block:** 3 — Retention & Growth Analyses
**Slide:** "The Limit Dilemma"

### Context
This shows the tradeoff when setting freemium limits — too low and you annoy users (they leave), too high and no one converts. There's a sweet spot.

### Design Brief
Create a dual-axis or two-line chart:

**X-axis:** Limit threshold (Low → High) — e.g., storage limit from 1GB to 20GB
**Y-axis:** Two metrics

**Line 1: Conversion rate** — High when limits are low, decreases as limits increase
**Line 2: Free user retention** — Low when limits are low (annoyed users leave), increases as limits increase

**Key elements:**
- The two lines cross or come close at the "sweet spot"
- Mark the sweet spot region: "Optimal range"
- Annotations:
  - Left side: "Too aggressive — users leave"
  - Right side: "Too generous — no one converts"
  - Middle: "Sweet spot"

**Style notes:**
- Classic tradeoff visualization
- The crossing/intersection point is the key insight
- Could shade the "optimal" region

### Technical Notes
- Dimensions: 1920x1080
- Both lines should be clearly distinguishable (different colors, one could be dashed)
- The sweet spot annotation is critical

---

## FIG-12: Power-Interest Grid (Mendelow Matrix)

**File:** `images/block_05_power_interest_grid.png`
**Block:** 5 — Stakeholders & Influence
**Slide:** "The Power-Interest Grid (Mendelow Matrix)"

### Context
This is a classic 2x2 stakeholder mapping framework. Students will use this to categorize stakeholders for their projects.

### Design Brief
Create a 2x2 matrix:

**X-axis:** Interest (Low → High)
**Y-axis:** Power (Low → High)

**Four quadrants with labels and actions:**

| Quadrant | Label | Action |
|----------|-------|--------|
| High Power, High Interest | "Key Players" | "Manage Closely" |
| High Power, Low Interest | "Keep Satisfied" | "Keep Satisfied" |
| Low Power, High Interest | "Keep Informed" | "Keep Informed" |
| Low Power, Low Interest | "Minimal Effort" | "Monitor" |

**Key elements:**
- Clear 2x2 grid structure
- Each quadrant labeled with both the stakeholder type AND the recommended action
- Axis labels clearly visible
- Could include small icons or example roles in each quadrant

**Style notes:**
- Classic consulting-style 2x2 matrix
- Clean, professional
- Could use color intensity to show importance (darker for "Manage Closely")

### Technical Notes
- Dimensions: 1920x1080 (or could be square 1080x1080)
- This is a reference diagram students will use repeatedly
- Make it clear enough to be useful as a standalone reference

---

## FIG-13: Processing Fluency Comparison

**File:** `images/block_05_fluency_comparison.png`
**Block:** 5 — Stakeholders & Influence
**Slide:** "Why Simple Beats Complex"

### Context
This demonstrates "processing fluency" — the same finding presented two ways. Students should immediately see why the simple version is more trustworthy/persuasive.

### Design Brief
Create a side-by-side comparison showing the SAME finding presented two ways:

**Version A (Bad - Dense/Jargon-Heavy):**
> "The coefficient on the interaction term between channel and cohort was statistically significant at p<0.05 (β=0.23, SE=0.08), controlling for demographic covariates, suggesting that the observed differential in retention metrics may be attributable to channel-specific selection effects, though further analysis is warranted to rule out confounding variables..."

**Version B (Good - Simple/Clear):**
> "Paid social users from Q3 retained 20% worse than Q2."

**Key elements:**
- Side-by-side or stacked comparison
- Version A should look dense, intimidating, academic
- Version B should look clean, scannable, trustworthy
- Caption: "Same finding. Different trust levels."
- Could use visual cues (red X vs green check, or frowning vs smiling face)

**Style notes:**
- The contrast should be stark and immediate
- Version A should feel exhausting to read
- Version B should feel obvious and clear

### Technical Notes
- Dimensions: 1920x1080
- The text in Version A can be slightly blurred or faded to emphasize "hard to process"
- Caption is important for the teaching moment

---

## FIG-14: Influence Compass

**File:** `images/block_05_influence_compass.png`
**Block:** 5 — Stakeholders & Influence
**Slide:** "The Influence Compass"

### Context
This introduces the four influence strategies. Students will use this framework to select the right approach for different stakeholders.

### Design Brief
Create a compass-style diagram with four directions:

**Layout:**
- **North:** Authority ("Because the expert says so")
- **East:** Consistency ("Because you already committed to this")
- **South:** Credibility ("Because the data proves it")
- **West:** Social Proof ("Because everyone else is doing it")
- **Center:** "Your Recommendation"

**Visual approach:**
- Actual compass shape with 4 cardinal directions
- OR 4-quadrant diagram with center point
- Each direction/strategy clearly labeled with its name and brief description
- Center shows this is about positioning your recommendation

**Key elements:**
- Four strategies equally weighted visually
- Brief descriptor for each (1-line explanation)
- Clear visual hierarchy with "Your Recommendation" at center
- Could use icons for each strategy (e.g., badge for Authority, checkmark for Consistency, graph for Credibility, people for Social Proof)

**Style notes:**
- Clean, memorable visual
- Students will reference this repeatedly
- Could use different colors for each quadrant

### Technical Notes
- Dimensions: 1920x1080 (or square 1080x1080)
- Should work as a standalone reference diagram
- Icons optional but helpful for memory

---

## Summary Checklist

| ID | Filename | Block | Ready? |
|----|----------|-------|--------|
| 01 | `block_02_funnel_basic.png` | 2 | ⬜ |
| 02 | `block_02_funnel_output.png` | 2 | ⬜ |
| 03 | `block_02_counterfactual.png` | 2 | ⬜ |
| 04 | `block_02_synthetic_control.png` | 2 | ⬜ |
| 05 | `block_02_pull_forward.png` | 2 | ⬜ |
| 06 | `block_02_ltv_curve.png` | 2 | ⬜ |
| 07 | `block_03_retention_vs_acquisition.png` | 3 | ⬜ |
| 08 | `block_03_retention_curve.png` | 3 | ⬜ |
| 09 | `block_03_pareto_curve.png` | 3 | ⬜ |
| 10 | `block_03_freemium_funnel.png` | 3 | ⬜ |
| 11 | `block_03_limit_tradeoff.png` | 3 | ⬜ |
| 12 | `block_05_power_interest_grid.png` | 5 | ⬜ |
| 13 | `block_05_fluency_comparison.png` | 5 | ⬜ |
| 14 | `block_05_influence_compass.png` | 5 | ⬜ |

---

## Delivery Instructions

1. Save all images to `figures/images/` with exact filenames listed above
2. Use PNG format with transparent backgrounds where appropriate
3. Check that filenames match exactly (case-sensitive)
4. Once images are in place, slides will automatically display them
