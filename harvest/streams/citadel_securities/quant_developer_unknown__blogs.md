# Citadel Securities · quant developer unknown · blogs

- **Source family:** blogs
- **Items:** 2
- **Date range:** 2026-02-22 – 2026-02-22 (2/2 dated)
- **Tier mix:** B=2

---
### Q1 · Tier B · unknown · online_assessment (two coding questions, ninety minutes, large constraints)

Again, start and end times. Again, overlapping intervals. But this time the task changed subtly. Instead of asking for the global maximum number of simultaneous employees, they asked for the maximum number of direct overlaps centered around a single employee. ... If one employee ends at time 5 and another starts at time 5, do they overlap? In this problem, yes.

*Reported answer:* Sort the start times. Sort the end times. For each interval, determine how many intervals finish strictly before it starts. Then determine how many intervals begin strictly after it ends. Everything else overlaps. Binary search; O(n log n).

> Instead of asking for the global maximum number of simultaneous employees, they asked for the maximum number of direct overlaps centered around a single employee.
— blog · posted 2026-02-22 · full_text · [link](https://hiya31.medium.com/what-they-asked-me-in-the-citadel-securities-hackerrank-coding-round-ed3ceded3c04)
  1 attestation(s) across 1 domain(s) · doubt: Same source caveat as the first problem: stylised write-up, no role or level stated, and the second problem is described mainly by contrast with the first rather than reproduced as a prompt.

### Q2 · Tier B · unknown · online_assessment (two coding questions, ninety minutes, large constraints)

You’re given arrays of start times and end times for employees. Each pair represents when someone is active. The task: compute the maximum number of employees overlapping at any single moment. ... the constraint quietly says n can be as large as 2 x 10^5.

*Reported answer:* Sort the start times. Sort the end times. Sweep through them in order, tracking how many intervals are currently active. Increase when a new interval begins. Decrease when one ends. Track the maximum. O(n log n).

> You’re given arrays of start times and end times for employees. Each pair represents when someone is active. The task: compute the maximum number of employees overlapping at any single moment.
— blog · posted 2026-02-22 · full_text · [link](https://hiya31.medium.com/what-they-asked-me-in-the-citadel-securities-hackerrank-coding-round-ed3ceded3c04)
  1 attestation(s) across 1 domain(s) · doubt: The author's blog is general-interest tech content and the post is written in a heavily stylised, SEO-friendly voice, so it is possible the problems were reconstructed from a public source rather than from the sitting it
