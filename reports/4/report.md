---
title: "Week 4: Evaluating Project Opportunities"
author: "Bálint Décsi"
date: "February 13, 2026"
geometry: margin=0.75in
---

## 1. Search Update

Up to now, I've mostly been reaching out to people in my network. Honestly, a top experience for me regarding this is finding out how many managers and teams are open to collaboration, which has had a good effect on my confidence. Obviously, this is due to the fact that I offer to do the analysis for free, but either way I've talked with people I'd otherwise consider less approachable.\
Nonetheless, I find it difficult to close a possible opportunity or ask the *important* and often uncomfortable questions that shed light on red flags.\

## 2. Project Evaluation

### Potential Project 1: Climate Risk Classification for Budapest District Building Blocks

| Red Flag | Status |
|----------|--------|
| Can they articulate the business question? | Yes, classifying building blocks' climate risk towards their inhabitants |
| Is data available? When? | Yes, public and purchased, immediately |
| Is there a named sponsor? | Yes, team lead of Environmental Dept. |
| What decisions will this inform? | Partially defined -- long-term climate guidelines of district municipality. |
| Is the sponsor engaged or "too busy"? | Engaged. |

**Promise level:** This project will be promising if a clear business outcome is defined. Contact person and stakeholder relations are guaranteed. Analytics task is clear: create a *v2* classification model instead of the *v1* regression model.

### Potential Project 2: Building Roof Rainwater Capture Capacity Interpolation 

| Red Flag | Status |
|----------|--------|
| Can they articulate the business question? | Yes, assessing yearly rainwater that can be captured per building roof |
| Is data available? When? | Yes, public and purchased, immediately |
| Is there a named sponsor? | Yes, research group head at Budapest University of Technology and Economics |
| What decisions will this inform? | Size of water reservoir tanks that would be installed in the future |
| Is the sponsor engaged or "too busy"? | Engaged. |

**Promise level:** I'm possibly ruling this out because as far as I've understood, the dataset is small (around 1000 rows). The outcome decision is clear, maybe the clearest of all potential projects, but I fear it would be used for informative purposes as the analysis user is a research group, possibly lacking the actual executive power. I'm also worried about the level of analytics required, as it's been mentioned by the stakeholder researcher that in his opinion, an "interpolation would suffice".

### Potential Project 3: Car Traffic Incident Effect Ecosystem Analysis 

| Red Flag | Status |
|----------|--------|
| Can they articulate the business question? | Yes, classifying incidents that cause traffic jams and locating areas prone to be affected by it |
| Is data available? When? | Yes, public and purchased and own, immediately |
| Is there a named sponsor? | Yes, innovation project manager at BKK (the Budapest public transport company) |
| What decisions will this inform? | Fine-tuning of traffic lights and efficiently re-routing traffic in peak hours and in case of incidents |
| Is the sponsor engaged or "too busy"? | Somewhere between |

**Promise level:** The data is very promising both in size and quality. I've had a meeting with the stakeholder and analyst peer, and they are dedicated towards the project. They emphasized this project has been on the table for a year now and they're keen to get it done. The outcome of a POC would affect district municipalities, so they can be turned into sponsors. All in all, a promising outlook.


### Potential Project 4: Hungary's Biggest Online Real Estate and Used Car Marketplace Analysis 

| Red Flag | Status |
|----------|--------|
| Can they articulate the business question? | Not yet |
| Is data available? When? | Yes, own, immediately |
| Is there a named sponsor? | Yes, BI team manager at Ingatlan.com |
| What decisions will this inform? | Not yet defined |
| Is the sponsor engaged or "too busy"? | Too busy |

**Promise level:** The talks have started later than with the other projects, but the progress seems swift. After our meeting, they came back with a prospective project, which they haven't defined to me yet. Their team is rather busy, as one of their expectation was for me to be able to work individually, noting that they might be scarcely available. This could turn out to be a professionally interesting project with high-quality data. 

## 3. Scope Negotiations

I've had some interesting back-and-forths, especially with the BKK team. Initially, they were throwing everything at me—they wanted a comprehensive analysis of every single traffic incident across the whole city. I had to push back a bit and suggest we focus on a Proof of Concept (POC) for a few high-traffic "hotspots" first. It's more feasible for me to deliver something high-quality on a smaller scale than to get lost in a city-wide dataset that might be too noisy to handle in one semester.

With the Roof Rainwater project, the negotiation is more about the *scope of analysis*. The dataset is small (around 1000 rows), which limits the complexity of modeling approaches. The stakeholder expects a straightforward interpolation, but I need to clarify whether this will truly inform an executive decision on reservoir tank sizing or remain a research exercise. It's a tension between delivering what they think they need and ensuring the analysis actually drives actionable infrastructure decisions.

## 4. Plan B
If I don't have a signed-off scope by end of February, I'm just going to pick the most stable lead and run with it, even if it's not the most "exciting" one on paper. I can't afford to keep hunting into March.

## 5. Messy Situation Practice

> "The data is definitely available, we just need to work out access with IT. Should be ready in a few weeks, maybe a month. Let's not let that slow us down."

This is a huge red flag for me. "A few weeks" is the standard corporate polite way of saying "this isn't a priority for IT." I've seen projects die on the waiting for a simple database permission. 

My response would be: "I appreciate the support, but I've learned the hard way that IT access can be the biggest bottleneck. To make sure we don't waste time, could we at least get a CSV sample of the data schema by the end of this week? Also, who is our specific point of contact in IT?" If I don't get a sample or a name by next Friday, I'd walk away. I'm not going to build a project on a promise and then find out in April that the data is inaccessible or unusable.

## 6. Reflection

The biggest lesson I've learned is that being "polite" is actually a liability when you're project hunting. I spent the first week being unnecesarily careful and not asking the tough questions about data ownership and actual decision-making power. It's much better to have an awkward conversation now and find out a project is a dead end than to find that out halfway through the semester. I’m learning to look for the red flags on a project—if they've been trying to do it for a year but haven't, I need to know *exactly* why before I sign on.

---

**AI Declaration:** I've used AI for this task according to our MS program's [AI policy](https://gabors-data-analysis.com/aipolicy/). This document's structural skeleton (headings etc.) and typesetting were assisted by the Gemini CLI tool, using Gemini 3. The prompt used was: "Make a skeleton for the report based on Week 4 task in the task description. Stick to the outline of the task markdown file."
