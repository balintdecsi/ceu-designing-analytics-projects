# Scenario 08: TrailBlaze

## Company Overview

**TrailBlaze** is an outdoor recreation app that provides hiking trail maps, GPS navigation, and community features. Users can discover trails, record their hikes, and share experiences. The app is particularly popular in North America and Western Europe.

**Business Model:**
- Free tier: Limited offline maps (1 region), basic trail info
- Pro ($35.99/year): Unlimited offline maps, real-time weather, safety features
- Pro+ ($59.99/year): Pro + 3D mapping, fitness tracking, lifetime statistics

**Current Metrics:**
- 4.2 million registered users
- 680,000 Pro/Pro+ subscribers (520,000 Pro, 160,000 Pro+)
- Annual churn: 28% (Pro), 18% (Pro+)
- DAU: 180,000 (summer peak), 45,000 (winter low)
- Avg. hikes recorded per active user: 3.2/month

---

## The Situation

TrailBlaze's subscription revenue is heavily seasonal. Summer months generate 60% of annual revenue as new users convert during peak hiking season. Winter months see subscription pauses and higher churn.

The product team launched three initiatives to reduce seasonality:

1. **Winter trails**: Added 5,000 snowshoeing and cross-country skiing trails
2. **Indoor integration**: Partnered with indoor climbing gyms for training logs
3. **Challenges**: Gamified monthly challenges with badges and leaderboards

Results after one winter season:
- Winter trail usage: 12,000 users (1.8% of subscribers)
- Indoor integration: 8,000 users (1.2% of subscribers)
- Challenges: 85,000 users engaged (12.5% of subscribers)

The VP of Product, Nina Kowalski, claims Challenges is the winner. The Head of Partnerships, James Morrison, insists indoor integration will grow as gym partnerships expand. The CEO, Erik Johansson, is unsure which bet to double down on.

Additionally, user-generated content quality has declined. The community feature was flooded with low-effort reviews, and top contributors are complaining about "noise."

---

## Available Data

You have access to:

1. **Users table**: user_id, signup_date, country, subscription_tier, subscription_start, subscription_status
2. **Activities table**: activity_id, user_id, activity_type (hike/snowshoe/climb/etc.), trail_id, start_time, duration, distance
3. **Trails table**: trail_id, trail_name, region, difficulty, activity_type, contributor_id
4. **Challenges table**: challenge_id, user_id, challenge_name, start_date, completed (boolean), badge_earned
5. **Reviews table**: review_id, user_id, trail_id, rating, review_text, review_date, helpful_votes
6. **Subscription events**: user_id, event_type (subscribe/pause/cancel/resume), event_date, plan

**Data quality notes:**
- Activity GPS data exists but is too large to query directly
- Indoor activities rely on manual logging (less reliable than GPS)
- Subscription pause is a new feature; historical data only covers 8 months
- Helpful votes on reviews are sparse

---

## Key Stakeholders

- **Erik Johansson (CEO)**: Focused on reducing seasonality. Wants clear recommendation on where to invest.

- **Nina Kowalski (VP Product)**: Champions gamification (Challenges). Believes engagement drives retention.

- **James Morrison (Head of Partnerships)**: Invested in gym partnerships. Believes long-term potential exceeds current adoption.

- **Community Team**: Concerned about content quality decline. Requesting features to promote high-quality contributors.

- **Board of Directors**: Questioning subscription pause feature—does it save customers or just delay churn?

---

## Constraints

- Gym partnership contracts are signed for 2 years—cannot exit early
- Winter data is only one season (small sample size)
- Cannot force users to complete surveys about seasonal behavior
- Engineering capacity is limited—can only pursue 1-2 major initiatives

---

## The Ask

The CEO wants a strategic recommendation before the next board meeting. Specifically:

1. Which winter initiative (Winter Trails, Indoor, Challenges) has the highest impact on retention?
2. Does subscription pause help retention or just delay inevitable churn?
3. Is the community content quality issue affecting retention? How should we address it?
4. Where should product investment go for the next year?

Nina has privately mentioned: "James's gym partnerships are going nowhere. The data should make that clear."

**Your deliverable:** Create a complete Analytics Project Brief for this analysis.
