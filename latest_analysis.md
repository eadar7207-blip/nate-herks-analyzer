# Nate Herk Analysis — September 09, 2026

## [I Turned GPT-6 Astra Into a 24/7 Stock Trader (tutorial)](https://www.youtube.com/watch?v=TLQLfa7yH4I)
*September 07 at 05:33 PM*

WHAT IT'S ABOUT

Nate walks through how he set up an AI system to trade stocks for him 24/7 using the newly released "GPT-6 Astra" (an advanced AI model). He previously ran a similar test with another AI called Claude and beat the stock market by 8%, so now he's repeating the experiment with a stronger AI, putting $10,000 of real money on the line. The main goal of the video is to show you exactly how he built the setup so you can copy it — while strongly warning you not to gamble real money before practicing first.

THE KEY POINTS

- **Nate strongly warns this is not financial advice and you should NOT hand an AI $10,000 to trade** — instead, start with "paper trading" (practice trading with fake money on real stock prices).
- He talked to Astra like a person, explained his challenge (make money in 7 days with a riskier strategy), and **the AI spun up about 10 "sub-agents" — smaller helper AIs that each research a piece of the problem — to do deep research and build a strategy.**
- There are two ways to use this: either let the AI think up a strategy for you, or, if you already trade every day, use AI just to speed up your work and make sure you don't forget things.
- Astra built a daily schedule where the AI "wakes up" six times a day at set times to read news, pick stocks, open trades, manage them, and close everything before the market shuts.
- **The single most important idea is "continuity" — because each time the AI wakes up it forgets everything, so it must leave a written progress log that the next wake-up reads to pick up where the last one left off.** Without this, Nate says, "you're just throwing darts at a wall."
- He planned for failures ahead of time (like the program crashing after placing an order or two sessions overlapping) so the system can recover safely without accidentally repeating a trade.
- Trades happen through "Alpaca," an online trading platform that gives you a free demo account (real stock prices, fake money) plus the option to trade real money later.
- You connect the AI to Alpaca using an "API key" (a secret password-like code that lets two programs talk to each other), which must be stored safely in an ".env file" (a hidden file for secret passwords) — never pasted into the chat window.
- Nate offers a free guide in his School community that you can hand straight to your AI to build the same system.

THE METHOD OR FRAMEWORK

Here's the step-by-step system Nate built:

1. **Talk it out first.** Explain your goal to the AI in plain language (Nate said: "I have 7 days, I want a riskier strategy, do thorough research").
2. **Let the AI research.** Astra created about 10 helper sub-agents that gathered information and wrote one big strategy document.
3. **Build a daily schedule.** The AI set six "wake-up" times through the trading day — read news and pick stocks in the morning, hunt for the first trade at market open (9:30), review positions midday, manage trades in the afternoon, then close everything and log results before close.
4. **Set up continuity.** Since the AI forgets between wake-ups, every session ends by writing a progress log. The next session starts by reading that log, checking the actual account, doing its job, then updating the log again — creating the illusion of one continuous trader instead of many separate ones.
5. **Plan for failures.** Write down what could go wrong (crashes, overlaps, corrupted data) so the system can recover without repeating trades.
6. **Connect to Alpaca.** Make an account, start with the free demo, grab your API key, and store it safely in an .env file — not in the chat.

HOW THIS APPLIES TO AI REAL ESTATE

The real lesson here isn't stocks — it's the "wake-up plus written handoff" pattern, and it maps perfectly onto real estate. Imagine an AI assistant for your consulting business that "wakes up" three times a day: at 7 a.m. it checks new property listings and price drops in your client's target neighborhood, at noon it reviews which leads replied to your emails, and at 5 p.m. it summarizes the day and drafts follow-ups. Just like Astra, each wake-up forgets the last one — so you build a shared progress log (for example, a simple database or document) where the AI records "Contacted the Johnsons about the 3-bed on Oak Street, waiting to hear back." When the next session runs, it reads that log first, so it never double-texts a client or forgets a hot lead. That continuity is what turns a bunch of forgetful one-off tasks into a reliable 24/7 assistant your clients can trust.

ACTION STEP THIS WEEK

Pick one repeating task in your real estate work (say, checking new listings for a client every morning) and build the continuity system for it. Concretely: (1) create one shared document or note that acts as the "progress log," (2) write a prompt that tells your AI to always read that log first, do the task, then write down what it did and what's next, and (3) run it manually two mornings in a row to confirm the second run correctly picks up where the first left off. You're not automating the whole business yet — you're just proving the handoff works.

BEST QUOTE

"Continuity is ensured by shared recordings, not by AI remembering the conversation."
