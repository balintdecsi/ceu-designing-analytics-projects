# Scenario 10: NeonBank

## Company Overview

**NeonBank** is a digital-only neobank targeting millennials and Gen Z. They offer checking accounts, savings, debit cards, and recently launched personal loans and crypto trading. The bank is fully mobile—no branches, no paper.

**Business Model:**
- Free checking account with debit card
- Premium account ($9.99/month): Higher ATM limits, cashback, priority support
- Revenue from interchange fees, interest spread, loan origination, crypto trading fees
- 2.5% APY on savings (competitive for the market)

**Current Metrics:**
- 1.8 million customers
- 320,000 Premium subscribers
- Average deposits: $4,200 (checking), $8,100 (savings)
- Personal loans outstanding: $180M
- Crypto trading monthly volume: $45M
- Customer acquisition cost: $85
- Monthly active users: 72%

---

## The Situation

NeonBank's board is concerned about profitability path. The unit economics are challenging:

- Interchange revenue per customer: $42/year
- Premium subscription revenue: $120/year (but only 18% convert)
- Interest income per customer: $28/year (low balances)
- Personal loan revenue per borrower: $380/year (but only 4% of customers have loans)

The Head of Product, Alex Tran, believes the answer is "product stacking"—getting customers to use multiple products. Data shows that customers using 3+ products have 5x higher revenue and 70% lower churn. But correlation isn't causation: are engaged users just naturally multi-product, or does adding products drive engagement?

Meanwhile, the personal loans product is underperforming. Approval rates are 18% (too low, frustrating applicants), but default rates for approved loans are 6.2% (higher than target of 4%). The credit model may be miscalibrated.

Crypto trading launched 8 months ago and adoption has been volatile—literally tracking Bitcoin price movements.

---

## Available Data

You have access to:

1. **Customers table**: customer_id, signup_date, signup_source, premium_status, age, income_bucket (self-reported), zip_code
2. **Accounts table**: customer_id, account_type (checking/savings), balance, last_activity_date
3. **Transactions table**: customer_id, transaction_date, transaction_type, amount, merchant_category
4. **Loans table**: loan_id, customer_id, loan_amount, origination_date, interest_rate, status (current/delinquent/default/paid_off)
5. **Crypto trades**: customer_id, trade_date, crypto_symbol, trade_type (buy/sell), amount
6. **App sessions**: customer_id, session_date, features_used, session_duration

**Data quality notes:**
- Income is self-reported and often missing (~40% null)
- Transaction merchant categories are inconsistent
- Crypto prices are available but need external API for historical
- Loan application data (denials) requires separate approval to access

---

## Key Stakeholders

- **Alex Tran (Head of Product)**: Champions product stacking thesis. Wants to invest in cross-sell flows.

- **Credit Risk Team**: Owns loan model. Defensive about current calibration. Claims underperformance is due to economic conditions, not model.

- **CFO**: Needs clear path to profitability. Skeptical that "engagement" translates to revenue.

- **Compliance Officer**: Concerned about fair lending if credit model is adjusted. Requires disparate impact analysis.

- **Board of Directors**: Comparing NeonBank unfavorably to competitors. Questioning crypto investment.

---

## Constraints

- Cannot share individual customer data externally (regulatory)
- Fair lending analysis required before any credit model changes
- Crypto product has regulatory uncertainty—cannot expand features currently
- Premium pricing change would require 90-day notice to customers

---

## The Ask

The CEO wants analysis to support the board's profitability review. Specifically:

1. Does product stacking actually drive revenue, or is it just correlation with engaged users?
2. What's wrong with the personal loans product? Should we loosen approval (more volume, more risk) or tighten (less volume, better performance)?
3. Is crypto trading worth the investment? What's the actual customer economics?
4. What's the path to profitability for the average NeonBank customer?

Alex has privately said: "The CFO only cares about short-term revenue. Product stacking is about long-term LTV—make sure that comes through."

**Your deliverable:** Create a complete Analytics Project Brief for this analysis.
