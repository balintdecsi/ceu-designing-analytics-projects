---
marp: true
theme: default
paginate: true
header: 'ECBS5228A: Designing Analytics Projects'
footer: 'Block 1: The Analytics Project Brief'
---

<!-- _class: lead -->
<!-- _paginate: false -->
<!-- _header: '' -->
<!-- _footer: '' -->

# Designing Analytics Projects

## Block 1: The Analytics Project Brief

**Eduardo Arino de la Rubia**
January 8, 2026

---

<!-- _class: lead -->

# Part 1: Course Overview
### *(15 minutes)*

---

## Welcome

Before we dive in:

- Grab coffee if you need it
- Phones away (you'll want to focus)
- We'll take breaks — this is a marathon, not a sprint

<!--
INSTRUCTOR NOTE:

**Background:** This is Day 1, first substantive block. Students just sat through syllabus logistics. Energy may be low or nervous. Your job in the first 5 minutes is to establish psychological safety and signal that this class will be different from their technical courses.

**Key point:** Set the tone that this is interactive, practical, and safe to make mistakes.

**Say something like:**
"Before we get into content, let me check in. By show of hands — who's excited to be here? [Pause, hands up] Now who's terrified? [Pause, fewer hands] Here's the thing: both is the right answer. If you're only excited, you might not be taking it seriously enough. If you're only terrified, you'll be too tense to learn. The best place to be is a little of both.

This class is going to be different from your technical courses. I'm going to ask you questions. I'm going to cold-call people. Not to embarrass anyone — but because this material only makes sense when you engage with it. The Brief framework we're learning today isn't something you memorize. It's something you practice."

**If asked:** "Will you really cold-call us?"
A: Yes. But I'm not trying to catch you out. I'm trying to get you thinking. If you don't know, say 'I don't know' — that's a valid answer and we'll work through it together.

**Transition:** "Alright, let's start with a question that might surprise you..."
-->

---

## A Question to Start

> **Think for 30 seconds:**
>
> What percentage of data science projects actually deliver business value?

<!--
INSTRUCTOR NOTE:

**Background:** The "60-85% failure rate" comes from multiple industry studies (Gartner, VentureBeat, IDC, academic papers) over the past decade. Exact numbers vary — some say 60%, others 85% — but the pattern is consistent. Crucially, when researchers investigate WHY projects fail, it's almost never the model or the code. It's scoping, stakeholder misalignment, solving the wrong problem, or scope creep.

**Key point:** Technical skills are necessary but not sufficient. This course exists because the failure mode is upstream of the code.

**Say something like:**
"I want you to think about this for 30 seconds. Don't answer yet — just think. Of all the data science and analytics projects out there — in companies, in research, in startups — what percentage do you think actually deliver the business value they promised?"

[PAUSE — let silence sit for 30 seconds. Silence is uncomfortable but necessary.]

"Okay, let me hear some guesses. [Point to student] What's your guess?"

[Take 2-3 guesses. Usually students guess 40-60%.]

"Those are reasonable guesses. Here's what the research actually says: somewhere between 60 and 85 percent of data science projects FAIL to deliver their intended value. Let that sink in. That's not 'partial success' — that's failure. The project didn't do what it was supposed to do.

Now here's the part that matters for this course: when researchers dig into WHY these projects failed, it's almost never the model. The algorithm worked. The code ran. The pipeline deployed. But nobody used it. Or it solved the wrong problem. Or the stakeholder who was supposed to act on it had already moved on to something else.

That's what this course is about — the 80% of the iceberg that's underwater. The work that happens BEFORE you write code."

**If asked:** "Where does that statistic come from?"
A: Multiple sources — Gartner, VentureBeat surveys, academic studies by researchers like Bessen and Righi. Numbers vary by methodology, but the pattern is extremely consistent. I can share links after class if you want to dig deeper.

**If asked:** "What about successful projects — what do they do differently?"
A: Great question. That's exactly what we're going to learn today. Spoiler: they fill out something like the Brief before they start.

**Transition:** "So if it's not technical failure, what IS causing these projects to fail? Let me show you the four most common failure modes..."
-->

---

## Why Most Analytics Projects Fail

It's rarely the model. It's usually:

- **Wrong problem** — solved something nobody needed
- **Wrong metric** — optimized the wrong thing
- **Wrong stakeholders** — built it, nobody used it
- **Wrong scope** — took too long, world moved on

This course is about avoiding those failures.

<!--
INSTRUCTOR NOTE:

**Background:** These four failure modes come up again and again in post-mortems. Each one maps directly to a section of the Brief we'll teach today. This slide is the "hook" — it creates the problem that the Brief solves.

**Key point:** Failures happen upstream of technical work. None of these are model failures.

**Say something like:**
"Look at these four failure modes. Notice what's NOT on this list: 'The model was inaccurate.' 'The code had bugs.' 'The algorithm was wrong.' Those things happen, but they're rarely why projects fail to deliver value.

Wrong problem — you built something beautiful that answers a question nobody actually had. Wrong metric — you optimized the hell out of something, and in doing so, broke something else that mattered more. Wrong stakeholders — you delivered insights to someone who couldn't or wouldn't act on them. Wrong scope — you took so long that by the time you finished, the business had moved on to different priorities.

Every single one of these is preventable. That's what this course is about."

**If asked:** "What if the problem is actually technical?"
A: Then you fix the technical problem. But in my experience, by the time you've scoped correctly and aligned stakeholders, the technical problems are solvable. The unsolvable problems are usually the ones on this list.

**Transition:** "So what does this mean for what we're going to teach you? Let me be clear about what this course is — and isn't..."
-->

---

## What This Course Is NOT

❌ How to build models
❌ How to write Python/SQL
❌ Statistical methods
❌ Machine learning techniques

You have other courses for those.

<!--
INSTRUCTOR NOTE:

**Background:** Students in MSBA programs often expect every course to be technical. They may feel anxious that this course "doesn't count" or isn't teaching "real skills." This slide preempts that concern by explicitly validating their technical courses AND positioning this as complementary.

**Key point:** Technical skills are covered elsewhere. This course is about the skills you DON'T get in those courses.

**Say something like:**
"I want to be very clear about what this course is NOT. We're not going to teach you how to build models — you have other courses for that. We're not going to write Python or SQL together — same thing. Statistics, machine learning, all of that — covered elsewhere in your program.

If you came here hoping to learn gradient boosting, I apologize in advance. [Light laughter expected]

But here's the thing: those skills are necessary but not sufficient. You can be the best model builder in the world, and if you're solving the wrong problem or you can't get stakeholders to act on your insights, none of it matters."

**Transition:** "So what IS this course? Let me tell you..."
-->

---

## What This Course IS

✅ The work that happens **before** you write code
✅ How to scope projects that actually matter
✅ How to navigate organizational dynamics
✅ How to avoid the most common failure modes

**One framework. Applied repeatedly.**

<!--
INSTRUCTOR NOTE:

**Background:** Students often wonder why "soft skills" courses exist in technical programs. The answer is that the gap between technical capability and business impact is filled by the skills this course teaches. This slide is the positive framing after the negative framing of the previous slide.

**Key point:** One framework (the Brief), applied repeatedly across different contexts. Simplicity is the point.

**Say something like:**
"This is what we're actually going to teach you. The work that happens before you write code. How to figure out which projects actually matter — because not all data science projects are created equal. How to navigate the political realities of organizations — because your analysis lives or dies based on whether stakeholders act on it. And how to avoid the four failure modes we just talked about.

Here's the good news: it's one framework. The Analytics Project Brief. You're going to learn it once, and then you're going to apply it over and over in different contexts. By the end of this course, filling out a Brief will be second nature."

**If asked:** "Will we use this in our capstone?"
A: Absolutely. The capstone project explicitly requires a Brief. This course is designed to prepare you for that.

**Transition:** "And all of this serves a single throughline — the reason data science exists at all..."
-->

---

## The Throughline

Your job — as a data scientist, analyst, or anyone working with data — is simple:

# Drive better decisions with data.

That's it. Everything else is in service of this.

<!--
INSTRUCTOR NOTE:

**Background:** This is the philosophical anchor of the course. Students often define their value as "building models" or "writing code." This reframes their purpose at a higher level of abstraction. This framing also helps when they encounter career uncertainty — job titles change, but this core purpose remains.

**Key point:** Your value is in decisions improved, not models deployed.

**Say something like:**
"I want you to remember this statement. Write it down if you want. Your job — as a data scientist, analyst, ML engineer, whatever title you end up with — is to drive better decisions with data.

Not to build models. Not to write code. Not to create dashboards. Those are all tools. The purpose — the reason anyone pays you money — is that decisions in the organization get better because of your work.

When you frame your work this way, everything changes. A beautiful model that nobody uses? Failure. A simple spreadsheet analysis that changes a $10M decision? Success. The output format doesn't matter. The decision quality matters."

**If asked:** "What if my job is just to maintain data pipelines?"
A: Even then, you're enabling better decisions by ensuring data quality. The decision-support chain has many links. But always ask yourself: 'What decisions am I enabling?'

**Transition:** "And when we look at failures through this lens, we see what goes wrong..."
-->

---

## Why Projects Fail (Revisited)

Every common failure maps to a missing piece:

| Failure | What Was Skipped |
|---------|------------------|
| "Solved something nobody needed" | No clear decision to drive |
| "Optimized the wrong thing" | No counter-metrics |
| "Built it, nobody used it" | No stakeholder mapping |
| "Didn't see the disaster coming" | No pre-mortem |

The Brief prevents all four.

---

## The Single Artifact

Everything in this course revolves around one thing:

# The Analytics Project Brief

A structured framework that forces clarity **before** you start analyzing.

---

## Learning Outcomes

By the end of this course, you will be able to:

1. **Use the Analytics Project Brief** to scope projects
2. **Identify counter-metrics** and stakeholder dynamics
3. **Recognize which analyses** apply to different problems
4. **Apply influence strategies** to gain buy-in

---

## Assessment Overview

| Component | Weight | When |
|-----------|--------|------|
| Scenario → Brief | 30% | Jan 16 |
| Pen & Paper Exam | 30% | Jan 27 |
| Weekly Write-ups | 30% | Feb 10 – Mar 17 |
| Participation | 10% | During class |

Each of you gets a **unique scenario** for the Brief assignment.
No two students have the same one.

---

## Today's Roadmap (Day 1)

| Block | Time | Topic |
|-------|------|-------|
| **1** | 10:50–12:30 | The Analytics Project Brief *(you are here)* |
| | | *Lunch break* |
| **2** | 13:30–15:10 | Acquisition Analyses |
| | | *Break* |
| **3** | 15:40–17:20 | Retention & Growth Analyses |

By end of day: You'll know the Brief framework and all 9 foundational analyses.

---

## Questions Before We Dive In?

<!--
INSTRUCTOR NOTE:
Take 2-3 questions max.
"Big picture questions only — details will become clear as we go."
-->

---

<!-- _class: lead -->

# Part 2: The Analytics Project Brief
### *(45 minutes)*

---

## Why a Structured Framework?

Without structure, scoping conversations go like this:

> **Exec:** "Can you look at why revenue is down?"
> **You:** "Sure!"
> *(3 weeks later)*
> **Exec:** "This isn't what I wanted at all."

The Brief forces the hard conversations **upfront**.

<!--
INSTRUCTOR NOTE:

**Background:** This scenario happens constantly in industry. An eager analyst takes a vague request, interprets it their way, works for weeks, and delivers something the requester didn't want. The exec isn't wrong — they had something specific in mind but didn't articulate it. The analyst isn't wrong — they tried their best with limited information. The problem is the process.

**Key point:** Hard conversations now prevent wasted work later.

**Say something like:**
"Let me tell you about a pattern I've seen dozens of times. An executive walks up to a data scientist and says, 'Can you look into why revenue is down?' The data scientist says 'Sure!' — because they want to be helpful, they want to show they can deliver.

Three weeks later, the data scientist comes back with a beautiful analysis of customer churn patterns. The exec looks at it and says, 'This isn't what I wanted. I already know we have churn. I wanted to know if the new pricing is causing it.'

Who's at fault? [Pause] Neither of them. The exec had something specific in mind but didn't say it. The analyst made reasonable assumptions but didn't verify them. The failure is the PROCESS.

The Brief exists to force those hard conversations upfront. Instead of 'Sure!', you say, 'Let me write up a one-page Brief so we're aligned on scope.' Takes 30 minutes. Saves 3 weeks."

**If asked:** "What if the exec doesn't want to spend time on alignment?"
A: Then you have important information: this isn't a real priority. If someone won't spend 15 minutes aligning on scope, they probably won't spend the time to act on your findings either.

**Transition:** "So let's look at what this framework actually contains..."
-->

---

## The Analytics Project Brief

10 sections. Each answers a critical question.

| # | Section | Key Question |
|---|---------|--------------|
| 1 | Problem & Decision | What decision will this inform? |
| 2 | Metrics | What are we optimizing? What breaks? |
| 3 | Stakeholders | Who has power? Who might block? |
| 4 | Methodology | What analyses? What data? |
| 5 | Scope | What's in? What's out? |

<!--
INSTRUCTOR NOTE:

**Background:** The Brief has 10 sections, but they're not all created equal. Sections 1-3 (Problem, Metrics, Stakeholders) are where most failures occur. Section 10 (Pre-Mortem) is the most under-utilized but high-value section. Students don't need to memorize the numbers — they need to internalize the questions.

**Key point:** The Brief is structured around questions, not answers.

**Say something like:**
"Ten sections might sound like a lot, but each one is just answering a question. And notice these are questions that any reasonable person would ask before starting a project.

What decision will this inform? — Because if there's no decision at stake, why are we doing this?
What are we optimizing? What breaks? — Because every optimization has tradeoffs.
Who has power? Who might block? — Because analysis is useless if the right people don't act on it.

We're going to go through each of these sections in detail. But I want you to notice: none of these are technical questions. They're strategic and political questions. That's deliberate."

**If asked:** "Do we have to fill out all 10 sections for every project?"
A: For the assignment, yes. In practice, some sections are lighter for smaller projects. But Problem, Metrics, and Stakeholders are always critical.

**Transition:** "Let me show you the second half of the framework..."
-->

---

## The Analytics Project Brief (cont.)

| # | Section | Key Question |
|---|---------|--------------|
| 6 | Success Criteria | How will we know this worked? |
| 7 | Timeline | Key milestones? |
| 8 | Risks & Assumptions | What could go wrong? |
| 9 | Ethics & Privacy | PII? Bias risks? |
| 10 | Pre-Mortem | It failed. What happened? |

---

## Section 1: Problem & Decision

The most important section. Everything flows from here.

**Three questions to answer:**
1. What business question will this analysis inform?
2. Who is asking, and why now?
3. Who is the ultimate decision maker?

<!--
INSTRUCTOR NOTE:

**Background:** This section is where most project failures are seeded. Students (and professionals) often skip to methodology because it's comfortable. The hard work of aligning on the decision is uncomfortable. "Who is asking and why now?" uncovers urgency and political context. "Ultimate decision maker" prevents building for the wrong audience.

**Key point:** If you can't answer these three questions, STOP. You're not ready to start.

**Say something like:**
"This is the most important section of the Brief. Everything else flows from here. Get this wrong, and nothing else matters.

Three questions. Write them down.

First: What business question will this analysis inform? Notice I didn't say 'what question will this analysis answer.' You inform decisions. Rarely do you answer questions definitively. But there has to be a decision at stake.

Second: Who is asking, and why now? [Pause] Why is this question important? [Cold call a student]

[Expected answer: urgency, priorities, context]

Exactly. 'Why now?' tells you a lot. Is this urgent because of a quarterly review? Because a competitor launched something? Because someone's job is on the line? That context shapes everything — your timeline, your framing, your stakeholder strategy.

Third: Who is the ultimate decision maker? Not 'who is sponsoring' — who will actually decide. Sometimes the same person. Often not. You need to know who you're ultimately serving."

**If asked:** "What if I don't know who the decision maker is?"
A: Then your first task is to find out. Ask your sponsor: 'Once this analysis is done, who decides what we do with it?' If they can't answer, that's a red flag.

**Transition:** "You should also include a hypothesis..."
-->

---

## Section 1: The Hypothesis

Also include a hypothesis:

> *We believe [X] because [Y], and this analysis will confirm or refute that.*

**Why?** Forces you to be specific about what you expect to find.

If you don't have a hypothesis, that's okay — mark it as **exploratory**.

<!--
INSTRUCTOR NOTE:

**Background:** The hypothesis forces pre-commitment and prevents fishing for results. Without a hypothesis, it's easy to analyze data, find any pattern, and present it as if you'd expected it. The "because [Y]" part is crucial — it surfaces your reasoning and makes the hypothesis testable.

**Key point:** A hypothesis isn't a prediction to be right about — it's a commitment to intellectual honesty.

**Say something like:**
"A hypothesis forces you to put a stake in the ground. 'We believe X because Y, and this analysis will confirm or refute that.'

The 'because Y' part is critical. It's not enough to say 'We believe mobile users convert less.' You have to say 'We believe mobile users convert less BECAUSE the checkout flow has 3 more steps on mobile than desktop.' Now you have a testable claim.

And here's the key thing: you're not trying to be right. You're trying to be honest about what you expect. If you have no hypothesis — you're genuinely exploring — that's fine. Just say so explicitly. Write 'This is exploratory. We don't have a hypothesis; we're looking for patterns.'

What you can't do is pretend to be exploratory, fish around in the data until you find something, and then act like you knew it all along. That's how bad analytics gets published."

**If asked:** "What if our hypothesis is wrong?"
A: Great! That's a result. You learned something. A refuted hypothesis is still valuable. What you can't accept is a vague question that can't be refuted.

**Transition:** "Let me check that we're all following..."
-->

---

## Check for Understanding

> **Quick check:**
> Why is "Who is asking and why now?" important?

<!--
INSTRUCTOR NOTE:
Cold call. Looking for answers like:
- Urgency/timeline implications
- Political context
- Whether this is a real priority or someone's pet project
-->

---

## Section 2: Metrics

Two parts:

### Primary Metric
What are you optimizing? **Be precise.**

❌ "Conversion rate"
✅ "Users who complete checkout / Users who reach cart page, excluding guest checkout, trailing 7 days"

---

## Section 2: Metric Definitions

A complete metric definition includes:

| Component | Example |
|-----------|---------|
| **Event/table** | `checkout_completed` events |
| **Numerator** | Users who completed checkout |
| **Denominator** | Users who viewed cart |
| **Filters** | Excluding guest checkout |
| **Time window** | Trailing 7 days |

If you can't write the SQL, you haven't defined it.

---

## Section 2: Counter-Metrics

We'll go deep on this in Part 3, but the key idea:

> **Counter-metrics** are what breaks if your primary metric succeeds.

You optimize checkout completion → Revenue per order drops (people buying cheaper stuff)

Always identify 2-3 counter-metrics.

---

## Discussion: Metric Precision

> **Think-Pair-Share (2 min):**
>
> Someone says their metric is "user engagement."
> What questions would you ask to make this precise?

<!--
INSTRUCTOR NOTE:
Give 30 sec to think, 1 min to discuss with neighbor, then share out.
Looking for: What counts as engagement? DAU? Time spent? Actions?
Which users? New? All? Time window?
-->

---

## Section 3: Stakeholders

Use the **Power-Interest Grid**:

|   | High Interest | Low Interest |
|---|---------------|--------------|
| **High Power** | Manage Closely | Keep Satisfied |
| **Low Power** | Keep Informed | Monitor |

<!--
INSTRUCTOR NOTE:

**Background:** The Power-Interest Grid (also called the Mendelow Matrix) is a classic stakeholder management tool from the 1990s. It's simple but effective: plot stakeholders by their power (ability to affect the project) and interest (motivation to do so). Different quadrants need different engagement strategies.

**Key point:** Not all stakeholders are equal. Spend energy proportional to their power and interest.

**Say something like:**
"The Power-Interest Grid is a simple tool that works. Two axes: power and interest.

Power means: can this person kill the project, starve it of resources, or block implementation? Interest means: do they care enough to get involved?

High power, high interest — manage closely. These are your sponsors and key stakeholders. Update them frequently. Get their input. Don't surprise them.

High power, low interest — keep satisfied. They can kill your project but don't care about details. Don't bother them with updates, but make sure they're not unhappy.

Low power, high interest — keep informed. They care a lot but can't really affect the outcome. Helpful as advocates but don't let them consume your time.

Low power, low interest — monitor. Check in occasionally but don't invest energy here.

When you fill out this grid, you should end up with specific names in each quadrant — not just roles."

**If asked:** "How do I know someone's power level?"
A: Ask: Can this person approve or deny budget? Block implementation? Fire or promote you? Influence someone who can? If yes to any of these, they have power.

**Transition:** "Beyond the grid, you need to identify champions and blockers..."
-->

---

## Section 3: Champions & Blockers

Beyond the grid, identify:

**Champions** — Who actively wants this to succeed?
**Blockers** — Who might resist? *Why* do they resist?

The "why" matters. People block for reasons:
- Threatens their budget
- Makes their past work look bad
- Creates work for their team

<!--
INSTRUCTOR NOTE:

**Background:** Students often think politics is dirty or that good work speaks for itself. It doesn't. Every project has blockers, and understanding WHY they block is the key to neutralizing resistance. The three reasons listed (budget, reputation, workload) cover most blocking behavior.

**Key point:** Blockers aren't irrational. They're protecting something. Understand what.

**Say something like:**
"Beyond the grid, you need to identify two specific roles: champions and blockers.

Champions are people who actively want your project to succeed. They'll advocate for you in meetings you're not in. They'll defend your timeline when someone wants to cut it. Identify them explicitly — you'll need their help.

Blockers are people who will resist. And here's the thing: every project has blockers. If you write 'no blockers' in your Brief, you haven't thought hard enough.

But the key isn't just identifying blockers — it's understanding WHY they block. Nobody thinks of themselves as a blocker. They have reasons that are rational from their perspective.

[Point to bullets]

Threatens their budget: Your project requires engineering resources that would come from their team's allocation.

Makes their past work look bad: You're analyzing why their previous initiative didn't work. If you find problems, their judgment looks poor.

Creates work for their team: Even if your findings are great, implementing them falls on their team. More work, same headcount.

When you understand the motivation, you can address it. Private pre-briefs. Reframing. Including them in the solution. You can't neutralize a blocker you don't understand."

**If asked:** "What if the blocker is my manager?"
A: Then you have a serious problem that the Brief just surfaced. Better to know now than after you've invested months.

**Transition:** "Let's move on to methodology..."
-->

---

## Section 4: Methodology

Two parts:

### Which Analyses?
Select from the foundational analyses (we'll cover these in Blocks 2-3)

### Data Availability
| Data needed | Available? | If no, fallback? |
|-------------|------------|------------------|
| User clicks | Yes | — |
| Purchase history | Partial | Use last 6 months only |

---

## Section 4: Data Validity Checks — Stop/Go Gates

**Before you analyze, verify your data is trustworthy:**

| Check | How to Validate | Stop If... |
|-------|-----------------|------------|
| Events fire on iOS | Compare iOS vs Android event counts | >10% discrepancy |
| No duplicate users | `SELECT COUNT(*) vs COUNT(DISTINCT user_id)` | >1% duplicates |
| Attribution window consistent | Check `first_touch` vs `last_touch` logic | Multiple conflicting windows |
| Historical data complete | Count events by month | Any month <80% of expected |

**Grading note:** Your Brief must include 2+ specific checks with validation method AND stop condition.

If data is broken, **stop**. Don't draw conclusions from bad data.

<!--
INSTRUCTOR NOTE:
Emphasize this is a grading criterion. Students who write generic "we'll check data quality"
without specific checks, validation methods, and stop conditions will lose points.
-->

---

<!-- _class: lead -->

## ☕ Stretch Break
### 5 minutes

Stand up. Move around. Refill coffee.

<!--
INSTRUCTOR NOTE:
Enforce this. Attention spans need it.
Resume at exactly 5 minutes.
-->

---

## Section 5: Scope & Deliverables

Be explicit about what's **in** and **out**:

**In Scope:**
- US market only
- Last 6 months of data
- Desktop and mobile web

**Out of Scope:**
- Native app (separate project)
- International markets
- Real-time implementation

---

## Section 6: Success & Decision Criteria

**Analytical success:** What makes the analysis itself good?
- Metric defined with <20% confidence interval
- 3+ statistically significant drivers identified

**Business success:** What makes it valuable?
- Product team changes roadmap based on findings
- Clear A/B test hypotheses generated

---

## Section 6: Decision Criteria Table

Pre-commit to decisions:

| If we find... | We will... |
|---------------|------------|
| Checkout friction is #1 driver | Prioritize UX redesign |
| Price sensitivity is #1 driver | Test promotional strategy |
| No clear driver found | Run qualitative user research |

**Including the null result.** What if you find nothing?

---

## Section 6: Action Thresholds

Be specific about magnitude:

> "We will only recommend action if effect size ≥5 percentage points AND p<0.05"

> "We will not act if sample size <1000 users per variant"

This prevents "statistically significant but meaningless" results driving decisions.

---

## Sections 7-9: Quick Overview

**Timeline:** Key milestones and dates. Keep it simple.

**Risks & Assumptions:** What are you assuming is true? What could invalidate the analysis?

**Ethics & Privacy:** Does this require PII? Any bias risks? GDPR considerations?

---

## Section 10: Pre-Mortem

The most valuable section.

> **Prompt:** It's 3 months from now. This project failed spectacularly. What happened?

Write it as a story. Be specific. Be pessimistic.

This surfaces risks you wouldn't otherwise consider.

<!--
INSTRUCTOR NOTE:

**Background:** The pre-mortem was popularized by psychologist Gary Klein. Research shows that "prospective hindsight" — imagining an event has already happened — increases ability to identify reasons for outcomes by 30%. It's psychologically easier to explain failure after imagining it happened than to abstractly list risks. The pre-mortem also creates psychological safety to name concerns.

**Key point:** A pre-mortem isn't pessimism — it's structured imagination that surfaces risks you'd otherwise miss.

**Say something like:**
"This might be the most valuable section of the Brief, and it's the one people skip most often. The pre-mortem.

Here's the prompt: It's three months from now. This project failed spectacularly. Write the story of what happened.

Not 'what might go wrong' — that's too abstract. What DID go wrong. Write it as if you're explaining to your manager why the project failed. Be specific. Be pessimistic. Be honest.

Why does this work? Psychology research shows that when you imagine something has already happened — psychologists call it 'prospective hindsight' — you're 30% better at identifying reasons than if you try to predict the future abstractly. It's easier to explain a failure than to predict one.

And there's a social benefit too. In a team setting, saying 'Here's what might go wrong' can feel like you're being negative. Saying 'Here's how this failed in my pre-mortem' is just... doing the exercise. It creates safety to name concerns."

**If asked:** "How long should a pre-mortem be?"
A: A paragraph to a page. Enough to tell a specific story with a causal chain. Not a bulleted list of risks — that's a different exercise.

**Transition:** "Let me show you what a good pre-mortem looks like..."
-->

---

## Example Pre-Mortem

> We found that mobile users converted 40% less than desktop. Product redesigned the mobile checkout flow.
>
> Three months later, mobile conversion was flat. Turns out mobile users were just *browsing* — they always completed purchases on desktop. We solved the wrong problem because we didn't segment by user journey, just by device.

<!--
INSTRUCTOR NOTE:

**Background:** This example illustrates a common failure mode: confusing correlation with causation and not understanding user behavior before optimizing. Mobile conversion rates are a classic analytics trap — the numbers look actionable but the causal story is often wrong.

**Key point:** A good pre-mortem has a causal chain: we did X → because of Y → which caused Z. The lesson is implicit in the story.

**Say something like:**
"Look at the structure of this pre-mortem. It's not just 'mobile conversion didn't improve.' It tells a causal story.

We found a data pattern: mobile users convert less. We acted on it: redesigned mobile checkout. We failed: conversion stayed flat. Here's why: mobile users weren't trying to convert — they were browsing. They always intended to buy on desktop.

The lesson is implicit: we should have segmented by user journey, not just by device. We would have seen that users who browse on mobile and buy on desktop are the same people.

This is what I want your pre-mortems to look like. A story with causation, not just a list of things that went wrong. When you write 'we didn't have good data' — that's not a pre-mortem. When you write 'we assumed the signup event fired on iOS the same way it did on Android, but iOS users appeared to have 40% lower signup rates because the event was misconfigured' — that's a pre-mortem."

**If asked:** "Is this example realistic?"
A: Very. Multi-device user journeys are one of the most common traps in analytics. People research on mobile, buy on desktop, or vice versa. If you don't track users across devices, you'll draw wrong conclusions.

**Transition:** "So let me summarize the key principle for using the Brief..."
-->

---

## The Brief in Practice

Key principle:

> **Fill out the Brief before you start analyzing.**

Not after. Not during. Before.

It will feel slow at first. It saves time overall.

---

## Questions on the Framework?

<!--
INSTRUCTOR NOTE:
Take 3-4 questions.
Common Q: "How long does this take?"
A: 30-60 min once you're practiced. First few times, longer.
-->

---

<!-- _class: lead -->

# Part 3: Counter-Metrics & Adversarial Thinking
### *(35 minutes)*

---

## Goodhart's Law

> "When a measure becomes a target, it ceases to be a good measure."
> — Charles Goodhart

Or more bluntly:

> "Tell me how you measure me, and I'll tell you how I'll behave."

<!--
INSTRUCTOR NOTE:

**Background:** Goodhart's Law is foundational to understanding counter-metrics. Charles Goodhart was a British economist who observed this pattern in monetary policy. The law applies everywhere: education, healthcare, tech, government. The second quote ("tell me how you measure me") is often attributed to Eli Goldratt and is more visceral.

**Key point:** Metrics change behavior, and not always in the direction you want.

**Say something like:**
"This is one of the most important ideas in analytics. Charles Goodhart was a British economist who noticed something troubling: the moment you use a measure to control behavior, it stops measuring what you think it measures.

[Read the quote on screen]

Here's the more visceral version: 'Tell me how you measure me, and I'll tell you how I'll behave.'

Think about that. It's not cynical — it's human nature. If you tell me my bonus depends on X, I'm going to optimize for X. And if X is imperfectly correlated with what you actually care about, I'm going to find the gap and exploit it. Not maliciously — just rationally.

This is why counter-metrics exist. You can't just set a target and walk away. You have to ask: 'What happens when people start gaming this?'"

**If asked:** "Is this the same as Campbell's Law?"
A: Yes, very similar. Campbell focused on social programs, Goodhart on economics. Same insight: measurement changes behavior.

**Transition:** "Let me show you some examples of this in practice..."
-->

---

## Goodhart's Law in Action

**Healthcare:** Hospitals measured on "length of stay"
→ Discharged patients early
→ Readmission rates spiked

**Education:** Schools measured on "test scores"
→ Taught to the test
→ Critical thinking declined

**Tech:** Social media measured on "engagement"
→ Optimized for outrage
→ Mental health crisis

<!--
INSTRUCTOR NOTE:

**Background:** These three examples span public sector (healthcare, education) and private sector (tech) to show the universality of the pattern. Students in a business analytics program will relate most to the tech example, but the healthcare and education examples are less politically charged.

**Key point:** This pattern is universal. It's not about bad actors — it's about rational responses to incentive structures.

**Say something like:**
"Let me walk through three examples. Healthcare: hospitals get measured on length of stay because payers don't want to pay for unnecessarily long hospitalizations. What happened? Hospitals discharged patients earlier. Length of stay went down — metric improved! But readmissions spiked because people were sent home before they were ready. The metric looked great. The outcome was worse.

Education: No Child Left Behind measured schools on test scores. Teachers started teaching to the test — because their jobs depended on it. Test scores went up. But ask any educator what happened to critical thinking, creativity, deep understanding. The metric went up; the thing the metric was supposed to measure went down.

Tech: social media companies measured engagement. What gets engagement? Outrage. Conflict. Emotional provocation. The algorithm optimized for what kept people scrolling, and what keeps people scrolling isn't what's good for them. We're still dealing with the consequences.

In none of these cases were the people involved evil. They responded rationally to the incentives they were given. That's Goodhart's Law."

**If asked:** "How do you prevent this?"
A: Counter-metrics. In healthcare, you'd track readmission rates alongside length of stay. In education, you'd measure critical thinking alongside test scores. In tech — well, some companies are starting to track 'regretted sessions.'

**Transition:** "So what does this mean for you, specifically?"
-->

---

## The Problem for Data Scientists

You're often asked to optimize a metric.

If you succeed, **something else gets worse**.

Your job is to figure out what that is **before** you start.

---

## Counter-Metrics Defined

> **Counter-metric:** A metric that could worsen if you optimize the primary metric.

Two types:

| Type | Definition | Example |
|------|------------|---------|
| **Guardrail** | Must not worsen | Data quality, fraud rate |
| **Tradeoff** | May worsen within bounds | Short-term revenue for LTV |

---

## The "What Breaks" Framework

Five questions to find counter-metrics:

1. **Direct negative:** What directly worsens when X improves?
2. **Quality degradation:** What quality suffers?
3. **User segments:** Which users are harmed?
4. **Temporal tradeoffs:** What long-term metrics suffer?
5. **Cross-functional:** Whose goals are threatened?

<!--
INSTRUCTOR NOTE:

**Background:** The "What Breaks" framework is a practical tool for finding counter-metrics. Each question targets a different failure mode. Students should use this systematically when identifying counter-metrics for their assignments.

**Key point:** These five questions are a checklist. Use all five for every project.

**Say something like:**
"Here's a practical framework for finding counter-metrics. Five questions. Write them down.

First: Direct negative. What directly gets worse when your metric improves? If you increase checkout completion, maybe revenue per order drops because people buy the minimum to finish quickly.

Second: Quality degradation. What quality suffers? If you increase content production, maybe content quality drops. If you speed up customer service, maybe resolution quality suffers.

Third: User segments. Which users are harmed? This is often the most overlooked. When you optimize for the average user, you often hurt edge cases. Power users. New users. Users with disabilities. International users. Someone usually gets worse treatment.

Fourth: Temporal tradeoffs. What long-term metrics suffer? Short-term revenue vs. LTV. Engagement today vs. retention next month. Shipping features fast vs. technical debt.

Fifth: Cross-functional. Whose goals are threatened? Your metric improves, but another team's metric gets worse. Sales vs. support. Growth vs. quality. These create organizational tension — often the source of blockers.

Use all five questions for every project. You won't always have answers for all five, but asking the questions is what matters."

**If asked:** "Do we need a counter-metric from each category?"
A: No. You need 2-3 total, from whichever categories are most relevant. But check all five categories.

**Transition:** "Let me show you what this looks like in practice..."
-->

---

## Example: Checkout Optimization

**Primary metric:** Checkout completion rate

**What breaks?**
1. Revenue per order (people buy cheaper stuff to "just finish")
2. Return rate (impulse purchases get returned)
3. Customer service load (confused customers)
4. Fraud rate (less friction = more fraud)

---

## Example: Notification Optimization

**Primary metric:** Click-through rate on notifications

**What breaks?**
1. Notification opt-out rate (annoy people → they disable)
2. App uninstalls (too many notifications → rage quit)
3. Session quality (clicked but didn't engage)
4. User trust (feels spammy → brand damage)

---

## Discussion: Find the Counter-Metrics

> **Think-Pair-Share (3 min):**
>
> Primary metric: "Increase free-to-paid conversion rate"
>
> What could break if you succeed?

<!--
INSTRUCTOR NOTE:
Give 1 min to think, 2 min to discuss.
Looking for: Premature conversions → churn, free user satisfaction drops,
brand perception as "pushy," support load from confused upgrades
-->

---

## How Many Counter-Metrics?

**2-3 is right.**

Too few: You're not thinking hard enough
Too many: Analysis paralysis, false positive problem

Every additional guardrail at p<0.05 adds ~5% false alarm rate.

---

## Guardrails vs. Tradeoffs

**Guardrail:** Hard stop. If this worsens, kill the project.
- Fraud rate
- Data quality
- Legal compliance

**Tradeoff:** Acceptable within bounds. Monitor but don't stop.
- Short-term revenue (if LTV improves)
- Complexity (if value justifies it)

Label each counter-metric as one or the other.

---

## The Pre-Mortem Exercise

Now let's practice.

> **Scenario:** You're tasked with increasing user signups by 50% in Q1.

**Exercise (5 min):**
1. Individually, write a pre-mortem (2-3 sentences)
2. What went wrong? Be specific.
3. What counter-metric would have caught this?

<!--
INSTRUCTOR NOTE:
Give them 5 minutes to write. Silence is okay.
Then cold-call 3-4 students to share.
-->

---

## Pre-Mortem Sharing

Let's hear some failure stories.

<!--
INSTRUCTOR NOTE:
Cold call 3-4 students. After each one, ask:
"What counter-metric would have caught this?"

Common pre-mortems:
- Signup quality dropped (counter: D7 retention)
- Fraud increased (counter: fraud rate)
- Support overwhelmed (counter: tickets per signup)
- Brand damaged (counter: NPS)
-->

---

## Why Pre-Mortems Work

Psychology research shows:

- **Prospective hindsight** increases ability to identify reasons for outcomes by 30%
- Easier to generate specific failures than abstract risks
- Creates psychological safety to name concerns

It's not pessimism. It's **preparation**.

---

## Key Takeaways: Counter-Metrics

1. **Every metric optimization breaks something else**
2. **Use the "What Breaks" framework** to find counter-metrics
3. **Identify 2-3** — not zero, not twenty
4. **Label as Guardrail or Tradeoff**
5. **Pre-mortem** surfaces risks you'd otherwise miss

---

<!-- _class: lead -->

# Block 1 Recap

---

## Block 1 Recap

| Part | Key Takeaway |
|------|--------------|
| **Course Overview** | One framework (the Brief), applied repeatedly |
| **The Brief** | 10 sections — fill it out *before* you analyze |
| **Counter-Metrics** | What breaks if you succeed? Always ask. |

<!--
INSTRUCTOR NOTE:

**Background:** Recaps help with retention. The three key takeaways map to the three parts of Block 1. Students should be able to repeat these by the end of the day.

**Key point:** If students remember nothing else, remember these three things.

**Say something like:**
"Let me summarize what we've covered. Three key takeaways.

First: One framework, applied repeatedly. The Analytics Project Brief. You're going to use this for your assignment, for the exam, and for your capstone. The framework itself is simple — the skill is in applying it well.

Second: 10 sections — fill it out BEFORE you analyze. Not during. Not after. Before. The Brief exists to prevent wasted work, not to document work you've already done.

Third: What breaks if you succeed? This is the counter-metrics question. Goodhart's Law. Every optimization creates unintended consequences. Your job is to anticipate them.

If you remember nothing else from this block, remember these three things. [Pause] Can someone repeat them back to me? [Cold call]"

**If asked:** "Will this be on the exam?"
A: Yes. The exam will ask you to complete Brief sections for a new scenario. Everything we covered today is fair game.

**Transition:** "Before lunch, let me preview what's coming in Block 2..."
-->

---

## Before Next Block

We'll cover the **9 foundational analyses** in Blocks 2-3.

Each one will be introduced through a completed Brief example.

**After lunch:** Funnel, Channel Attribution, Campaign Effectiveness, CAC/LTV

---

## Questions?

<!--
INSTRUCTOR NOTE:
Take 2-3 final questions.
End on time — lunch break matters.
-->

---

<!-- _class: lead -->
<!-- _paginate: false -->

# See you after lunch!

**Block 2 starts at 13:30**

Acquisition Analyses: Funnel → Attribution → Campaign → CAC/LTV
