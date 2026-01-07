# Scenario 16: PlayForge Studios

## Company Overview

**PlayForge Studios** is a mobile gaming company with three active titles: a puzzle game (MindMerge), a strategy game (WarPath), and a casual game (CandyBlitz). Each game is free-to-play with in-app purchases and optional ad viewing for rewards.

**Business Model:**
- In-app purchases (IAP): Cosmetics, power-ups, virtual currency
- Advertising: Rewarded video ads (player chooses to watch)
- Battle Pass: $9.99/month recurring subscription in WarPath

**Current Metrics (Monthly):**
| Game | MAU | ARPU | IAP Revenue | Ad Revenue | D1 Retention |
|------|-----|------|-------------|------------|--------------|
| MindMerge | 2.8M | $0.42 | $580K | $600K | 42% |
| WarPath | 850K | $3.20 | $2.1M | $620K | 35% |
| CandyBlitz | 5.2M | $0.18 | $350K | $590K | 52% |

---

## The Situation

PlayForge's board is pushing for a "flagship focus" strategy. Instead of spreading resources across three games, they want to double down on one game and maximize its potential.

The Head of MindMerge, Jessica Lin, argues her game has the best balance of scale and monetization. The Head of WarPath, Michael Torres, argues his game has the highest ARPU and most committed players. The Head of CandyBlitz, Emily Park, argues casual games have lower development costs and more stable revenue.

But the analysis is complicated by recent changes:
- **MindMerge** added social features 4 months ago; engagement increased but monetization dropped
- **WarPath** launched in Japan last month; early results are mixed
- **CandyBlitz** is facing a clone that reached #3 on the app store

Meanwhile, the VP of Marketing, David Lee, is questioning acquisition spend. CPI (cost per install) is rising across all games, and he suspects the quality of acquired users is declining. He wants to shift from paid acquisition to organic/influencer channels.

---

## Available Data

You have access to:

1. **Users table**: user_id, game_id, install_date, install_source, country, device_type, churned_date
2. **Sessions table**: user_id, session_date, duration_minutes, levels_completed
3. **Purchases table**: purchase_id, user_id, purchase_date, item_type, price, currency
4. **Ad views table**: view_id, user_id, ad_date, ad_type, reward_type, completed
5. **Acquisition spend**: game_id, channel, date, spend, installs
6. **Social features (MindMerge only)**: user_id, friends_added, messages_sent, gifts_sent

**Data quality notes:**
- Attribution windows vary by channel (some 7-day, some 30-day)
- Japan launch data is only 4 weeks old
- CandyBlitz clone impact is hard to isolate
- IAP currency varies (need exchange rate conversion)

---

## Key Stakeholders

- **Jessica Lin (Head of MindMerge)**: Wants flagship investment in MindMerge. Believes social features will pay off long-term.

- **Michael Torres (Head of WarPath)**: Believes WarPath is the premium product. Argues ARPU > MAU for profitability.

- **Emily Park (Head of CandyBlitz)**: Defensive about clone competition. Claims CandyBlitz has lowest risk profile.

- **David Lee (VP Marketing)**: Wants acquisition strategy overhaul regardless of flagship choice.

- **Board of Directors**: Want clear recommendation. Tired of "balanced portfolio" approach.

---

## Constraints

- Cannot kill any game immediately (contractual obligations to players)
- Flagship investment would mean 60% of engineering to one game
- Japan expansion costs are sunk for next 6 months
- CandyBlitz team has already started clone counter-features

---

## The Ask

The CEO wants a data-driven flagship recommendation. Specifically:

1. Which game has the highest LTV potential when fully invested?
2. Are MindMerge's social features working? Are they worth the monetization dip?
3. Is WarPath's Japan expansion viable, or should we cut losses?
4. Is the acquisition quality decline real? Which channels should we shift to?
5. What's the flagship recommendation and why?

Michael has privately said: "Jessica's social features are a distraction. Nobody wants to chat in a puzzle game. WarPath players are actually committed."

**Your deliverable:** Create a complete Analytics Project Brief for this analysis.
