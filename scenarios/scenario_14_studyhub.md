# Scenario 14: StudyHub

## Company Overview

**StudyHub** is an online tutoring marketplace connecting students with tutors across academic subjects. They serve K-12 students, university students, and adult learners pursuing professional certifications. The platform facilitates video sessions, homework help, and test prep.

**Business Model:**
- Per-session fees: Students pay $40-120/hour depending on subject and tutor level
- Platform take rate: 20% of session fees
- Subscription (StudyHub+): $29/month for unlimited homework chat support
- Enterprise: B2B contracts with schools and learning centers

**Current Metrics:**
- 180,000 registered students (active in past 12 months)
- 12,000 active tutors
- 95,000 sessions/month
- Gross session value: $6.2M/month
- Platform revenue: $1.24M/month
- Tutor average rating: 4.7/5

---

## The Situation

StudyHub is facing a two-sided marketplace challenge. The platform is experiencing a "hollowing out":

**Student side**: Repeat session rate is declining. Students book 1-2 sessions, then either stop or take the relationship off-platform (paying tutors directly via Venmo).

**Tutor side**: Top tutors are leaving. The platform's 20% take rate is higher than competitors, and top tutors have full client rosters—they don't need discovery anymore.

The VP of Student Experience, Lauren Kim, wants to increase the "stickiness" through gamification, learning paths, and progress tracking. The VP of Tutor Experience, Mark Thompson, wants to reduce take rate for top tutors to retain them.

Recent data shows a troubling pattern: 35% of student-tutor matches that become "regular" (3+ sessions) eventually leave the platform. Lost revenue is estimated at $150K/month.

Additionally, StudyHub+ (subscription) has low adoption (8,000 subscribers) but high retention (94% monthly). Subscribers book 3x more sessions than non-subscribers.

---

## Available Data

You have access to:

1. **Students table**: student_id, signup_date, grade_level, primary_subject, subscription_status, last_session_date
2. **Tutors table**: tutor_id, signup_date, subjects_offered, hourly_rate, total_sessions, average_rating, verification_level
3. **Sessions table**: session_id, student_id, tutor_id, subject, session_date, duration_minutes, price, tutor_rating, student_rating
4. **Messages table**: message_id, sender_id, recipient_id, thread_id, message_date, content_length
5. **Subscriptions table**: student_id, subscription_start, subscription_end, cancellation_reason
6. **Off-platform signals**: student_id, tutor_id, flag_date, signal_type (contact info shared, regular scheduling mentioned, etc.)

**Data quality notes:**
- Off-platform signals are ML-detected from message content (false positive rate: ~20%)
- Tutor subjects are self-reported and not standardized
- Session cancellation data is incomplete
- Some tutors operate under multiple accounts

---

## Key Stakeholders

- **Lauren Kim (VP Student Experience)**: Wants product investment in engagement features. Believes sticky products reduce off-platform leakage.

- **Mark Thompson (VP Tutor Experience)**: Wants take rate reduction for retained tutors. Believes tutor satisfaction is the bottleneck.

- **CFO**: Concerned about take rate reduction impact on revenue. Wants proof it would increase volume enough to offset.

- **Top Tutors (Advisory Council)**: Vocal about take rate. Some have threatened to leave if nothing changes.

- **Investors**: Comparing to competitors. Pressing for marketplace efficiency metrics.

---

## Constraints

- Take rate changes affect all tutor contracts (legal review required)
- Gamification features would take 5 months to build
- Cannot directly prevent off-platform payments (would alienate tutors)
- StudyHub+ pricing is locked for current subscribers

---

## The Ask

The CEO wants a strategic recommendation on marketplace health. Specifically:

1. How much revenue is actually lost to off-platform relationships? Can we quantify it?
2. Would retaining top tutors (lower take rate) improve student metrics enough to offset revenue loss?
3. Is StudyHub+ the answer? What would happen if we offered it free to high-value students?
4. What's the optimal intervention: student stickiness (Lauren) or tutor retention (Mark)?

Mark has privately said: "Lauren wants to add bells and whistles, but tutors are the product. Fix tutor retention first."

**Your deliverable:** Create a complete Analytics Project Brief for this analysis.
