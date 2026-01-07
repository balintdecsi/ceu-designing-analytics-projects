# Scenario 03: LearnLoop

## Company Overview

**LearnLoop** is an online education platform specializing in professional skills development. They offer courses in data science, product management, UX design, and digital marketing. Founded in 2019, the company has grown rapidly, especially during the pandemic.

**Business Model:**
- Individual courses: $79-$299 one-time purchase
- Pro subscription: $39/month or $299/year (access to all courses + certificates)
- Enterprise licenses: Custom pricing for company training programs

**Current Metrics:**
- 850,000 registered users
- 42,000 Pro subscribers
- 180 enterprise clients (avg. deal size: $45,000/year)
- Course completion rate: 18% (industry average: 15%)
- Net Promoter Score: 38

---

## The Situation

LearnLoop's growth has stalled. New user registrations dropped 25% year-over-year, and Pro subscription conversions are declining. The CEO, Rebecca Torres, believes the market is saturated with competitors and wants to focus on retention and expansion rather than acquisition.

The product team recently launched several new features:
- **Learning Paths**: Curated sequences of courses toward a skill goal
- **Cohort-based courses**: Live, scheduled courses with peer interaction
- **Skill Assessments**: Pre/post tests to measure learning outcomes

Early adoption varies significantly:
- Learning Paths: 35% of active users have started one
- Cohort courses: Only 3% have enrolled (but completion rate is 65%)
- Skill Assessments: 45% of course completers take the post-assessment

The Head of Product, Michael Chang, is proud of the Learning Paths feature and wants to make it the default experience. The Head of Content, Aisha Williams, is concerned that Learning Paths are surfacing her team's older courses and hiding newer, higher-quality content.

---

## Available Data

You have access to:

1. **Users table**: user_id, signup_date, signup_source, subscription_status, subscription_start, country, profession
2. **Enrollments table**: user_id, course_id, enrollment_date, completion_date (null if incomplete), certificate_issued
3. **Learning Paths table**: path_id, path_name, courses_in_path, target_skill
4. **User Path Progress**: user_id, path_id, start_date, current_course, completion_date
5. **Cohort Courses table**: cohort_id, course_id, start_date, instructor, enrolled_users, completed_users
6. **Assessment Scores**: user_id, course_id, pre_score, post_score, assessment_date
7. **Sessions table**: user_id, session_date, minutes_watched, courses_accessed

**Data quality notes:**
- Engagement data for mobile app is less complete than web
- Some users have multiple accounts (estimated 5-8% duplication)
- Enterprise user data is mixed with individual users (flag exists but not always accurate)

---

## Key Stakeholders

- **Rebecca Torres (CEO)**: Focused on proving LTV and reducing churn. Wants to show board that retention strategy is working.

- **Michael Chang (Head of Product)**: Championed Learning Paths. Believes it should be the default experience. His performance review hinges on Learning Paths adoption.

- **Aisha Williams (Head of Content)**: Concerned that product features are overriding content quality. Wants newer courses surfaced more prominently.

- **Enterprise Sales Team**: Needs data showing learning outcomes to close deals. Asking for "proof that people actually learn something."

- **CFO**: Wants to understand if cohort courses are worth the instructor costs (3x more expensive per user than self-paced).

---

## Constraints

- Cannot survey users directly—must use behavioral data
- Learning Paths feature is only 6 months old
- Cohort courses have small sample size (only 12 cohorts run so far)
- Enterprise data is sensitive and requires extra privacy precautions

---

## The Ask

Rebecca has asked for an analysis to inform the product roadmap. Specifically:

1. Which features (Learning Paths, Cohorts, Assessments) are driving retention and LTV?
2. Are users who engage with new features actually learning more (skill improvement)?
3. Where should product investment go in the next 12 months?

Michael has separately asked: "Can you make sure Learning Paths look good? They're the future of the platform."

**Your deliverable:** Create a complete Analytics Project Brief for this analysis.
