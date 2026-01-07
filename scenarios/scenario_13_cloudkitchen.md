# Scenario 13: CloudKitchen Pro

## Company Overview

**CloudKitchen Pro** provides software for restaurant owners to manage their operations—POS (point of sale), inventory management, staff scheduling, and analytics. They serve 4,200 restaurants across the US, primarily independent and small-chain establishments.

**Business Model:**
- Monthly SaaS subscription: $199/month (Basic), $399/month (Pro), $699/month (Enterprise)
- Payment processing: 2.4% + $0.10 per transaction (optional, competes with Square/Toast)
- Hardware: POS terminals, kitchen displays, receipt printers (one-time purchase)
- Implementation services: $500-$2,000 setup fee

**Current Metrics:**
- 4,200 active restaurant clients
- MRR (monthly recurring revenue): $1.1M
- Payment processing volume: $28M/month
- Monthly churn: 2.8%
- NPS: 34 (industry average: 40)
- Average customer lifetime: 28 months

---

## The Situation

CloudKitchen Pro is losing ground to larger competitors (Toast, Square for Restaurants) who are bundling hardware, software, and payments with aggressive pricing. Three concerning trends emerged this quarter:

1. **Churn accelerating**: Monthly churn increased from 2.2% to 2.8%
2. **Payment adoption declining**: Only 22% of new customers adopt payment processing (down from 35% last year)
3. **Support burden increasing**: Average ticket resolution time up 40%

The VP of Product, Michelle Santos, believes the problem is feature parity. Competitors have mobile ordering integration, loyalty programs, and delivery platform connections. CloudKitchen Pro doesn't.

The VP of Sales, David Martinez, believes the problem is pricing. Competitors are offering first-year discounts that CloudKitchen Pro can't match without killing margins.

The Head of Customer Success, Jennifer Park, believes it's neither—it's onboarding. Restaurants that complete full onboarding retain at 97%. But only 45% complete onboarding.

---

## Available Data

You have access to:

1. **Restaurants table**: restaurant_id, restaurant_name, cuisine_type, location_city, signup_date, plan_tier, churned_date, churn_reason
2. **Onboarding table**: restaurant_id, onboarding_start, onboarding_complete (boolean), steps_completed, days_to_complete
3. **Feature usage**: restaurant_id, month, feature_name, usage_count
4. **Support tickets**: ticket_id, restaurant_id, ticket_date, category, resolution_time_hours, escalated
5. **Payment processing**: restaurant_id, month, transactions, volume, processing_revenue
6. **Competitor mentions**: restaurant_id, source (support ticket/exit survey/sales notes), competitor_named, context

**Data quality notes:**
- Churn reason is often missing or "Other" (only 40% useful)
- Feature usage tracking was updated 6 months ago—historical data inconsistent
- Exit surveys have 25% response rate
- Competitor mentions are manually tagged (subjective)

---

## Key Stakeholders

- **Michelle Santos (VP Product)**: Wants budget for feature development. Claims feature gap is existential threat.

- **David Martinez (VP Sales)**: Wants pricing flexibility. Claims sales team loses deals on price, not features.

- **Jennifer Park (Head of Customer Success)**: Wants investment in onboarding team. Claims onboarding is the highest-leverage intervention.

- **CFO**: Budget is limited. Can only fund one major initiative. Needs clear ROI projection.

- **Board of Directors**: Comparing metrics to Toast (public company). Concerned about competitive position.

---

## Constraints

- Cannot match competitor pricing without board approval (would reduce margins significantly)
- Feature development timeline is 6+ months for major features
- Customer Success team is at capacity—more onboarding investment requires hiring
- Cannot access competitor customer data directly

---

## The Ask

The CEO wants a data-driven recommendation for resource allocation. Specifically:

1. What's actually driving churn? Is it features, pricing, or onboarding?
2. Why is payment processing adoption declining? What's the revenue impact?
3. Which intervention (features, pricing, onboarding) has the highest ROI?
4. How do we compete against well-funded competitors without matching their spending?

David has privately said: "Michelle keeps asking for features that take forever to build. Price matching is immediate."

**Your deliverable:** Create a complete Analytics Project Brief for this analysis.
