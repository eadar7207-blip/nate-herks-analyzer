# Nate Herk Analysis — July 27, 2026

## [I Tested Opus 5 vs. Fable 5. What You Need to Know.](https://www.youtube.com/watch?v=2J3uX8iRNng)
*July 24 at 11:38 PM*

WHAT IT'S ABOUT

Nate tested two of Anthropic's newest AI models — Claude Opus 5 and Claude Fable 5 (Fable being the top-tier, most powerful one, and Opus being a cheaper option) — to see which actually works better for real tasks. The surprising thing he found is that Opus, even though it's cheaper, sometimes beats the expensive Fable model. He made this video to show real experiments instead of just trusting the official test scores, so you can figure out which model to use for your own work.

THE KEY POINTS

- **Opus 5 costs about half as much as Fable 5, yet on several benchmarks (standardized tests that measure AI performance) it actually scores higher.** This shocked Nate because usually the pricier model wins.
- Nate warns you to take benchmarks "with a grain of salt" and instead **run the models through your own real workflows to see what actually works for you.**
- In a diagram test (drawing a picture of how AI search works), Fable's looked more visual but Opus's was **more organized and detailed** — Nate would pick Opus's version to teach someone.
- In the first bug-fixing test, both models did well, but Fable's fix was slightly cleaner. Fable was faster (11 min) but more expensive; Opus was slower but cheaper.
- In the second bug-fixing test, **Opus clearly won — scoring 93 out of 95 versus Fable's 66 — while also being cheaper**, passing all four tests where Fable only passed two.
- Anthropic's biggest upgrade in Opus 5 is that it's **much better at "verifying" its own work — checking whether it actually finished the job correctly before stopping.**
- Nate's final takeaway: **the model you pick matters less than how you instruct it and feed it context** (the background information the AI needs to do the task right).

THE METHOD OR FRAMEWORK

Nate explains a practical way to test AI models for yourself:

1. **Pick real tasks you actually do** — not made-up tests. He used things like fixing bugs in a big pile of code and generating diagrams.
2. **Give both models the exact same prompt and the same materials** so the only thing changing is the model itself (this keeps the test fair).
3. **Track three things every time: cost (dollars spent), time (how long it took), and tokens (the chunks of text the AI reads and writes, which is what you're charged for).**
4. **Have a neutral third judge grade the results** — Nate used another AI called Codex to score which output was better, so it wasn't just his opinion.
5. **Build in verification** — tell the AI a clear "stopping condition," meaning don't quit until you pass this specific test. For fuzzy tasks, you can even spin up several "sub-agents" (mini AI helpers) that debate until they all agree.

HOW THIS APPLIES TO AI REAL ESTATE

If you run an AI real estate consulting business, this is directly about saving money without losing quality. Say you build an AI tool that reviews rental listings and flags problems, or one that drafts property descriptions and answers buyer questions. You don't automatically need the most expensive model. Instead, take a real task — like generating 50 property descriptions — and run it through both a cheaper model (Opus 5) and the top model (Fable 5), then compare the results side by side while tracking cost and quality. You might find the cheaper model does just as well, saving your client thousands of dollars per month. And for anything where accuracy matters — like an AI checking that a contract summary is correct — build in verification so the AI double-checks its own work before it hands anything to a client.

ACTION STEP THIS WEEK

Pick one real task your AI real estate system does often (for example, writing listing descriptions). Run the exact same prompt through two different models — one cheap, one expensive. Write down the cost, the time, and your honest rating of which output is better for all three of them. Then decide, based on real evidence, which model to use going forward for that specific task.

BEST QUOTE

"Yes, it's good to find the best model, but find the best model for your use case and then understand how to talk to it."
