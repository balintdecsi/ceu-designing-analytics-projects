---
title: "Week 5: Pre-Mortem on a Hypothetical"
author: "Bálint Décsi"
date: "February 20, 2026"
geometry: margin=0.75in
---

## 1. Project Summary

**Project:** Real Estate Price Prediction Model for Hungary's largest online marketplace.\
**Sponsor:** BI Team Manager.\
**Goal:** Build a regression model to suggest "optimal rental prices" to landlords when they upload a new flat listing, helping them price competitively to reduce time-on-market.

## 2. The Pre-Mortem Narrative

It is six months later, and the project has been shelved. The failure started quietly but ended up making the tool unusable. I spent the first two months building a complex regression model on the entire national dataset. The validation metrics looked great—low RMSE, high R-squared. We launched the beta to a small group of landlords, and the complaints started immediately. Landlords in rural areas said the suggested prices were laughably high, while Budapest landlords said they were leaving money on the table.

The root cause was a fatal **Data Quality Issue** that we treated as a "feature." My model was trained on *listing prices* (what people ask for), not *transaction prices* (what people actually pay). In the current cooling market in Hungary, the gap between the two had widened significantly. Because I was working in a silo and the sponsor was "too busy" to give regular feedback, I didn't realize that listing prices were effectively "wishful thinking" data, not market reality.

Additionally, we fell into a **Scope Creep** trap. By trying to model the *whole country* at once, the model couldn't capture the nuances of specific neighborhoods. A 50sqm flat in District 5 behaves totally differently from a 50sqm flat in a rural village, but my national model smoothed over these differences, resulting in a tool that was "average everywhere" but "accurate nowhere." The sponsor eventually stopped replying to my emails because fixing the model would require a total rebuild they didn't have time to supervise.

## 3. What Should Have Been Done Differently?

*   **Validated the Target Variable:** I should have asked the "dumb" question in Week 1: "Does this price represent what people actually pay?" We could have adjusted the target variable using a "bargaining coefficient" derived from historical transaction data, or at least flagged this as a major risk.\
*   **Reduced Scope:** Instead of modeling the whole country, I should have insisted on a **Pilot for Budapest only**. This would have allowed us to spot the data discrepancies faster and iterate without the noise of national variance.\
*   **Forced Sponsor Engagement:** Since I knew the sponsor was busy, I should have set up strict "Go/No-Go" checkpoints. If they couldn't review the initial error analysis in Week 3, I should have paused the project rather than drifting into a vacuum.
*   **Study Famous Failures** Real estate predictions have been around for a while and there are many use case studies about things that go wrong. I should read these.

## 4. How This Informs Your Capstone

I will explicitly ask my sponsor: "What does the data *miss*? What happens in reality that isn't captured in these logs?". I will be hyper-aware of "silent failure"—where the model runs without errors but produces garbage output. I’ll prioritize getting a "sanity check" from a domain expert early on, rather than trusting the summary statistics blindly.

## 5. Reflection

I realized that I usually assume "clean data" means "accurate representation of reality." It’s not. Data can be perfectly formatted, have no missing values, and still be completely wrong for the business question (like listing prices vs. transaction prices). This pre-mortem forced me to look for logical flaws in the *premise* of the project, not just technical flaws in the execution.

---

**AI Declaration:** I've used AI for this task according to our MS program's [AI policy](https://gabors-data-analysis.com/aipolicy/). This document's structural skeleton (headings etc.) and typesetting were assisted by the Gemini CLI tool, using Gemini 3. The prompt used was: "Make a skeleton for the report based on Week 5 task in the task description. Stick to the outline of the task markdown file." 
