# Scenario 07: SoundWave

## Company Overview

**SoundWave** is a podcast hosting and monetization platform. They provide hosting, analytics, and advertising services to podcast creators. Founded in 2019, they've grown to host 85,000 active podcasts with 180 million monthly downloads.

**Business Model:**
- Free tier: Hosting up to 3 hours/month, basic analytics
- Creator tier ($15/month): Unlimited hosting, advanced analytics, custom website
- Pro tier ($45/month): Creator + monetization tools (dynamic ad insertion, sponsorship marketplace)
- Revenue share: 20% of ad revenue generated through their marketplace

**Current Metrics:**
- 85,000 active podcasts (at least 1 episode in past 90 days)
- 180M monthly downloads across all podcasts
- 12,000 Creator tier subscribers
- 3,200 Pro tier subscribers
- Monthly churn: 4.2% (Creator), 2.8% (Pro)
- Ad marketplace revenue: $2.8M/quarter

---

## The Situation

SoundWave is facing a strategic inflection point. The podcasting market is consolidating—Spotify and Apple are signing exclusive deals with top creators. SoundWave's largest podcasts are receiving acquisition offers.

The CEO, Maya Rodriguez, believes SoundWave's future is in the "middle class" of podcasting—creators too small for platform exclusives but large enough to monetize. However, this segment is underserved by current features.

Recent data shows troubling patterns:
- Podcasts with 10,000+ downloads/episode have 15% annual churn—they "graduate" to competitors
- Podcasts with <1,000 downloads/episode rarely convert to paid tiers
- The "middle" (1,000-10,000 downloads) has highest LTV but only 8% of podcasts

The VP of Product, Kevin Liu, wants to build features for the middle segment: better sponsorship matching, audience growth tools, and collaboration features. The Head of Sales, Diana Chen, wants to focus on the ad marketplace, claiming it's the real money-maker.

---

## Available Data

You have access to:

1. **Podcasts table**: podcast_id, creator_id, category, launch_date, tier, episodes_published, total_downloads
2. **Episodes table**: episode_id, podcast_id, publish_date, duration_minutes, downloads, completion_rate
3. **Creators table**: creator_id, signup_date, tier, tier_start_date, churn_date, email_domain
4. **Ad campaigns**: campaign_id, podcast_id, advertiser_id, start_date, end_date, impressions, revenue
5. **Analytics usage**: creator_id, date, features_used, time_in_dashboard
6. **Download geography**: episode_id, country, downloads

**Data quality notes:**
- Completion rate is estimated (not all podcast apps report this)
- Some podcasts have multiple creators (only primary is tracked)
- Ad campaign attribution to specific episodes is imperfect
- Category tags are self-reported and often inaccurate

---

## Key Stakeholders

- **Maya Rodriguez (CEO)**: Believes "middle class" strategy is existential. Wants data to prove or disprove this thesis.

- **Kevin Liu (VP Product)**: Wants to build for mid-tier creators. Proposing 6-month roadmap of growth tools.

- **Diana Chen (Head of Sales)**: Focused on ad marketplace revenue. Believes top 500 podcasts drive 80% of value.

- **Creator Community Team**: Hears constant feedback about needing better growth tools. Wants to justify investment in creator education.

- **Board of Directors**: Concerned about platform consolidation. Comparing SoundWave to competitors with stronger creator retention.

---

## Constraints

- Cannot access download data from external platforms (only SoundWave-hosted episodes)
- Cannot survey churned creators (most don't respond)
- 8 weeks until board strategy presentation
- Cannot commit engineering resources until after analysis is complete

---

## The Ask

The board wants a data-driven strategy recommendation. Specifically:

1. Is the "middle class" segment actually the highest LTV? What's the evidence?
2. Why do large podcasts churn? Is it preventable or inevitable graduation?
3. What features would most impact mid-tier creator retention and monetization?
4. Should we focus on creator tools (Kevin) or ad marketplace (Diana)?

Diana has privately said: "Kevin's 'middle class' thesis is romantic but not realistic. The data will show top creators are what matters."

**Your deliverable:** Create a complete Analytics Project Brief for this analysis.
