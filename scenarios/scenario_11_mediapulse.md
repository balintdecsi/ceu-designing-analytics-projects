# Scenario 11: MediaPulse

## Company Overview

**MediaPulse** is a digital news publisher covering technology, business, and culture. They operate three brands: TechInsider (technology news), BusinessBeat (finance and markets), and CultureDrop (entertainment and lifestyle). Founded in 2016, they've grown to become a significant mid-tier publisher.

**Business Model:**
- Advertising revenue (programmatic + direct): 70% of revenue
- Subscription (MediaPulse Pro): $9.99/month for ad-free experience + exclusive content
- Sponsored content: Native advertising partnerships
- Events: Annual conference series

**Current Metrics:**
- 45 million monthly unique visitors (across all brands)
- 180,000 Pro subscribers
- Average pages per session: 2.3
- Time on site: 3.2 minutes
- Ad revenue per 1,000 pageviews (RPM): $12.40
- Newsletter subscribers: 2.1 million

---

## The Situation

MediaPulse is caught in the broader media industry crisis. Advertising revenue dropped 22% year-over-year as programmatic rates collapsed and Google/Meta captured more market share. The subscription business is growing but not fast enough to offset ad declines.

The editorial team is divided on strategy:

**Team A (Led by TechInsider editor)**: Focus on "hard news"—breaking stories, investigative journalism. Claims these drive social sharing and brand reputation.

**Team B (Led by CultureDrop editor)**: Focus on "evergreen content"—guides, reviews, explainers. Claims these drive search traffic and have longer shelf life.

Data tells a mixed story:
- Breaking news: High social traffic, low search, 90% of traffic in first 48 hours
- Evergreen content: Low social, high search, traffic spreads over 18+ months
- Subscriber conversion: 0.8% for breaking news readers, 1.2% for evergreen readers

Meanwhile, newsletter engagement is declining. Open rates dropped from 28% to 19% over the past year. The VP of Audience Development, Christina Lee, believes email is dying. The CEO disagrees—she thinks the content mix is wrong.

---

## Available Data

You have access to:

1. **Articles table**: article_id, brand, author, category, publish_date, content_type (breaking/evergreen/opinion), word_count
2. **Pageviews table**: pageview_id, article_id, user_id (null if anonymous), timestamp, source (direct/search/social/email/referral), device
3. **Users table**: user_id, first_seen, subscription_status, subscription_start, newsletter_subscribed
4. **Newsletter sends**: send_id, user_id, send_date, campaign_name, subject_line, opened, clicked
5. **Ad impressions**: impression_id, article_id, ad_unit, timestamp, revenue
6. **Subscriptions table**: user_id, start_date, end_date, cancellation_reason

**Data quality notes:**
- 60% of pageviews are from anonymous users (can't link behavior)
- Social referrer data is degraded (shows as "direct" increasingly)
- Newsletter opened tracking affected by iOS privacy changes
- Ad revenue attribution to specific articles is imperfect

---

## Key Stakeholders

- **TechInsider Editor**: Believes breaking news is core to brand identity. Worried evergreen focus will make them "just another content farm."

- **CultureDrop Editor**: Believes evergreen content is sustainable business model. Points to SEO traffic growth.

- **VP Audience Development (Christina Lee)**: Skeptical of email. Wants to invest in push notifications and app.

- **CFO**: Needs to cut costs. Questioning which editorial investments pay off.

- **CEO**: Believes content strategy should match business model. Wants data to settle internal debates.

---

## Constraints

- Cannot reduce editorial headcount until strategy is decided
- iOS privacy changes limit email open tracking accuracy
- Third-party cookie deprecation will affect ad revenue modeling
- SEO algorithm changes create uncertainty about evergreen value

---

## The Ask

The CEO wants a data-driven content strategy recommendation. Specifically:

1. What's the true ROI of breaking news vs. evergreen content when you factor in all revenue streams?
2. Is email actually dying, or is the content/frequency wrong?
3. Which content types drive subscription conversion? What's the LTV difference?
4. How should editorial investment be allocated across brands and content types?

The TechInsider editor has privately said: "CultureDrop just wants to write listicles. If we go that direction, I'm out."

**Your deliverable:** Create a complete Analytics Project Brief for this analysis.
