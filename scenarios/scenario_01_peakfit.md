# Scenario 01: PeakFit

## Company Overview

**PeakFit** is a fitness app that offers personalized workout plans and nutrition tracking. Founded in 2021, the company has grown to 2.8 million monthly active users across 40 countries. The app offers a freemium model: basic features are free, with a Premium tier at $14.99/month or $99.99/year.

**Business Model:**
- Free tier: Basic workout library, manual food logging
- Premium: AI-personalized plans, barcode scanner, wearable integrations, live classes

**Current Metrics:**
- 2.8M MAU (monthly active users)
- 340,000 paying subscribers (12% conversion rate)
- $42M ARR (annual recurring revenue)
- Monthly churn: 6.2% for monthly subscribers, 2.1% for annual
- D7 retention (free users): 28%
- D30 retention (free users): 12%

---

## The Situation

PeakFit just closed a Series B round of $35M. The board has set an aggressive growth target: reach 500,000 paying subscribers within 18 months while maintaining or improving unit economics.

The VP of Growth, Marcus Chen, has been experimenting with different acquisition channels. Currently, the marketing budget is allocated as follows:

| Channel | Monthly Spend | New Users/Month | Paid Conversions/Month |
|---------|--------------|-----------------|------------------------|
| Instagram Ads | $180,000 | 95,000 | 3,200 |
| Google Search | $120,000 | 45,000 | 2,800 |
| TikTok Influencers | $80,000 | 120,000 | 1,100 |
| Apple Search Ads | $60,000 | 22,000 | 1,800 |
| Referral Program | $40,000 | 18,000 | 2,400 |

Marcus is under pressure to justify his budget allocation. The CFO, Diana Okonkwo, has questioned why TikTok gets $80K/month when it has the lowest conversion rate. Marcus believes TikTok users just take longer to convert and that the current attribution model undercounts them.

---

## Available Data

You have access to:

1. **User table**: user_id, signup_date, signup_channel, country, age_bucket, gender, device_type
2. **Subscriptions table**: user_id, subscription_start, subscription_end (null if active), plan_type (monthly/annual), price_paid, cancellation_reason
3. **Events table**: user_id, event_timestamp, event_type (workout_complete, food_logged, class_joined, feature_used, etc.)
4. **Marketing spend table**: date, channel, spend_amount, impressions, clicks
5. **Attribution table**: user_id, touchpoint_timestamp, channel, touchpoint_type (impression/click)

**Data quality notes:**
- Attribution tracking was only implemented 8 months ago
- iOS users have limited attribution due to ATT (App Tracking Transparency)
- Referral program data is clean and complete
- Some users have multiple attribution touchpoints

---

## Key Stakeholders

- **Marcus Chen (VP Growth)**: Owns marketing budget. Believes current attribution undervalues TikTok and awareness channels. His bonus is tied to new subscriber growth.

- **Diana Okonkwo (CFO)**: Skeptical of "brand awareness" arguments. Wants clear ROI metrics. Recently questioned the $80K TikTok spend in a board meeting.

- **Priya Sharma (Head of Product)**: Concerned that chasing acquisition is hurting retention investment. Wants to understand which users are highest quality, not just cheapest.

- **Board of Directors**: Want to see a path to 500K subscribers. Expecting quarterly updates on CAC trends.

---

## Constraints

- The analysis must be completed within 3 weeks to inform Q2 budget planning
- iOS attribution gaps cannot be fully solved (industry-wide limitation)
- You cannot run new A/B tests for this analysis—must use historical data
- TikTok influencer campaigns are managed by an external agency; detailed per-post data is available but messy

**Note on iOS ATT:** Apple's App Tracking Transparency means some attribution data is fundamentally incomplete. Your analysis should acknowledge this limitation and propose how to work around it (e.g., focus on Android data, use proxy metrics, model the gap) rather than attempt to fully solve it. This is a real-world constraint that all mobile analysts face.

---

## The Ask

Diana has requested a comprehensive analysis of customer acquisition performance by channel. Specifically:

1. What is the true CAC and projected LTV by channel?
2. Which channels should receive more/less budget in Q2?
3. How should we account for multi-touch attribution and awareness effects?

Marcus has privately asked you to "make sure the analysis captures the full value of awareness channels, not just last-click."

**Your deliverable:** Create a complete Analytics Project Brief for this analysis.
