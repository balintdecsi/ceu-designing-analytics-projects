---
title: "Week 6: Capstone Readiness Check"
author: "Bálint Décsi"
date: "February 27, 2026"
geometry: margin=0.75in
---

## 1. Search Journey Summary

I started the search on multiple threads in parallel, reaching out across my network. Luckily, several of these turned out to be promising leads. What worked well was applying the project brief framework early on---it helped me spot potential problems with data quality or scope before I got too invested. What didn't work as well was my communication. In some cases, I was too polite at the beginning and avoided asking the hard questions. I've learned that not sugarcoating things and asking directly about red flags creates a space where both parties are on the same page. If I had to start over, I'd stay more professional in the communication making clear what I'm looking for and what I can do in the framework of the cpastone project.

## 2. Key Lessons from Write-ups

- **Week 1 (Search Kickoff):** The biggest takeaway was learning to distinguish a "data project" from a "decision project"---I need to start every conversation with the business problem, not the architecture, to avoid technically perfect but useless solutions.

- **Week 2 (Counter-Metrics):** The lesson is that counter-metrics should proxy for *quality*, not just quantity. For any model I build, I need a metric that catches silent degradation.

- **Week 3 (Methodology Selection):** Never take a high-level metric at face value. The 45% lift exercise taught me that the most obvious "win" is often confounded by selection bias. Data validity checks as stop/go gates are non-negotiable.

- **Week 4 (Project Evaluation):** Being "polite" is actually a liability when you're project hunting. I spent the early weeks being unnecessarily careful instead of asking the tough questions about data ownership and actual decision-making power. It's much better to have an awkward conversation now than to find out halfway through the semester that a project is a dead end.

- **Week 5 (Pre-Mortem):** "Clean data" does not mean "accurate representation of reality." Data can be perfectly formatted, have no missing values, and still be completely wrong for the business question.

## 3. Your Capstone Brief Checklist

### Defining a Precise Primary Metric

I'll anchor the analysis to a concrete decision, not just a prediction task. From Week 1, I know I default to "improve accuracy" as a goal, so I'll force myself to define the specific *decision* that changes if the metric moves.

### Identifying Counter-Metrics

I'll define at least one tradeoff metric and one guardrail metric upfront, before any modeling begins. The Zillow use case study proved a point strongly here.

### Mapping Stakeholders (Especially Blockers)

I need to identify who has the actual executive power to act on my analysis. The Roof Rainwater project taught me that having an engaged stakeholder doesn't help if they lack decision-making authority---it risks the project becoming a research exercise. I've also learned that IT access is often the real bottleneck, so I'll get a named contact and a data sample in the first week.

### Writing Your Pre-Mortem

Prioritizing the pre-mortem is a real lesson here and I'll write it early, not as an afterthought. The key questions from Week 5: "What does the data *miss*? What happens in reality that isn't captured in these logs?" I'll specifically look for the gap between what the data *represents* and what I *assume* it represents---like listing prices vs. transaction prices.

## 4. Questions for Your Sponsor

*3--5 questions to ask your sponsor in your first meeting to help fill out your Brief.*

1. What specific decision will change based on the results of this analysis?
2. How will the model be evaluated and is there any benchmark it is expected to overperform?
3. Who else needs to approve or act on the results, and is anyone likely to push back?
4. Can I get a sample of the actual data (even a CSV export) by the end of this week, and who is my point of contact in IT for access?
5. Will you be available once a week for regular check-ins? If things get busy, what's the minimun amount of time per week you can commit to?

## 5. Confidence Check

- Understanding what makes a good capstone project? 5/5
- Defining metrics with precision? 4/5
- Identifying what could break? 4/5
- Navigating stakeholder dynamics? 2/5

Stakeholder dynamics is my weakest area. I've gotten better at asking tough questions, but I still tend to default to being overly polite when I sense pushback. My plan is to prepare my "uncomfortable questions" list *before* each meeting so I don't chicken out in the moment.

## 6. Reflection

*What are you most excited about? What are you most nervous about?*

I'm most excited about working on a real problem with real stakes in a field I don't have experience in. I really want to use the framework to see it holding up when I'm sitting across from a sponsor who has their own agenda and constraints.

On one hand, I'm most nervous about stakeholder management: keeping the sponsors engaged and getting the information and real answers at the appropriate time. On the other hand, I feel the reality of the "silent failure" scenario from my pre-mortem. Building something that runs fine, looks good in a presentation, but quietly produces garbage because I missed a fundamental assumption about the data.

---

**AI Declaration:** I've used AI for this task according to our MS program's [AI policy](https://gabors-data-analysis.com/aipolicy/). This document's structural skeleton (headings etc.) and typesetting were assisted by the Cursor CLI tool, using Claude Opus 4.6 (I know, a bit of an overkill for a skeleton synthesis, but this happens when companies throw free credits at students). The prompt used was: "Create the skeleton for report 6, based on the task description at reports/6/task_6.md. Write in markdown."
