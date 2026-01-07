# Scenario 12: UrbanMove

## Company Overview

**UrbanMove** operates electric bike and scooter sharing in 15 European cities. Users unlock vehicles via app, ride to their destination, and end the ride anywhere in the service zone. Founded in 2019, they survived the micromobility shakeout and are now focused on profitability.

**Business Model:**
- Per-ride pricing: €1 unlock + €0.25/minute
- Monthly pass: €29 for unlimited unlocks (still pay per-minute)
- Seasonal pass: €99 for 4 months (popular with students)
- B2B partnerships: Corporate accounts for employee commuting

**Current Metrics:**
- 45,000 vehicles deployed (28,000 scooters, 17,000 bikes)
- 2.1 million registered users
- 85,000 monthly pass holders
- 3.2 million rides/month
- Average ride: 12 minutes, €4.80
- Vehicle utilization: 3.8 rides/vehicle/day

---

## The Situation

UrbanMove's path to profitability depends on one thing: vehicle utilization. The economics are brutal:

| Utilization | Contribution Margin |
|-------------|---------------------|
| <2 rides/day | -€180/month/vehicle |
| 2-4 rides/day | Breakeven |
| >4 rides/day | +€120/month/vehicle |

Currently, only 35% of vehicles average >4 rides/day. The fleet team spends enormous effort repositioning vehicles from low-demand to high-demand areas, but it's expensive (€8 per reposition).

The VP of Operations, Henrik Larsson, wants to invest in predictive repositioning—using AI to move vehicles before they're needed. The VP of Growth, Anna Kowalski, believes the problem is user acquisition in underserved areas. If more people used the service, utilization would naturally improve.

Recent analysis also revealed that monthly pass holders are actually less profitable than per-ride users. Pass holders take short trips during peak times, contributing less revenue while using prime vehicles.

---

## Available Data

You have access to:

1. **Vehicles table**: vehicle_id, vehicle_type (scooter/bike), city, deployment_date, current_zone, status
2. **Rides table**: ride_id, user_id, vehicle_id, start_time, end_time, start_zone, end_zone, distance_km, revenue
3. **Users table**: user_id, signup_date, city, pass_type (none/monthly/seasonal/corporate), age_bucket
4. **Repositioning log**: vehicle_id, move_date, from_zone, to_zone, cost
5. **Zone metrics**: zone_id, city, zone_type (commercial/residential/mixed), avg_rides_per_day, supply_score, demand_score
6. **Weather data**: city, date, temperature, precipitation, conditions

**Data quality notes:**
- GPS can be inaccurate in urban canyons (zone assignment may be wrong near boundaries)
- Repositioning costs are estimates (actual labor time varies)
- Corporate accounts are grouped—no individual user data
- Some rides have missing end location (user left service zone)

---

## Key Stakeholders

- **Henrik Larsson (VP Operations)**: Believes AI repositioning can save €2M/year. Requesting budget for data science team.

- **Anna Kowalski (VP Growth)**: Believes geographic expansion within cities (more coverage) drives network effects.

- **CFO**: Skeptical of both proposals. Wants proof before major investment.

- **City Governments**: Some cities threatening to revoke permits if vehicles block sidewalks or have low utilization.

- **Monthly Pass Holders**: Vocal on social media. Any negative changes would cause backlash.

---

## Constraints

- Cannot increase prices in cities with regulated caps
- Monthly pass pricing is locked for existing subscribers until next year
- AI repositioning model would take 4 months to build and validate
- Some cities limit total vehicle counts (can't just add more vehicles)

---

## The Ask

The CEO wants a clear recommendation on profitability levers. Specifically:

1. What's the real driver of vehicle utilization? Is it supply (positioning) or demand (user base)?
2. Are monthly passes actually unprofitable? What would happen if we changed pricing or terms?
3. Is AI repositioning worth the investment? What's the realistic improvement potential?
4. Which cities should we prioritize for profitability vs. growth?

Henrik has privately said: "Anna keeps throwing more vehicles at the problem without thinking about where they should go."

**Your deliverable:** Create a complete Analytics Project Brief for this analysis.
