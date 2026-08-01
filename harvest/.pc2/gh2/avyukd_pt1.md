---
title: "Recruiting, Internships, and Reflections Pt. 1"
date: 2024-06-28
type: post
tags:
  - recruiting
  - career
  - reflection
  - software-engineering
summary: "How I went from a barely-passed-the-bar Amazon offer to an Optiver offer and a surprise winter internship at Madison Avenue Partners"
---

<!-- import-meta: date=2024-06-28 | title=Recruiting, Internships, and Reflections Pt. 1 | slug=2024-06-28-recruiting-internships-and-reflections-pt-1 -->

*<u>Recruiting Season</u>*

After my summer internship at [[amazon|Amazon]], I decided to begin taking recruiting seriously before junior year began. The prior year, I had arrogantly overestimated my interviewing abilities and lucked out with an Amazon offer. During the Amazon interview, I was asked Insert Interval, a common Leetcode Medium question – I had done this question before but still fumbled during the interview, coming up with a less-than-optimal solution. I correctly explained what an optimal solution would look like and gave convincing responses in the behavioral portion of the interview, leading to what I think was a “barely passed the bar” ZIRP-phenomenon offer (i.e., in a normal year, were interest rates not zero and FAANG not hiring aggressively, I would not have received an offer).

The next summer, to avoid such embarrassment, I decided to start from scratch. I curbed my ego and began Leetcoding with Two Sum. I failed on LC Easys but was sufficiently honest to truly understand the solution before moving on – no “oh yea, this is trivial, let’s brush it aside and move on”; I strived for mastery. Over the course of a few months, I completed ~300 LC problems, going from “exists a possibility I will fail this Easy” to “I think I can maybe solve that Hard…”. I began optimizing for speed, learning to interview in Python (I already knew the language, but data structures and “competitive” programming in Python requires learning a decent number of tricks). Let me clarify some things that I did in my interview prep that may be unusual or different:

- **Go to failure:** Many people set a goal to do 1-2 Leetcode problems per day. This is arbitrary and stupid – why artificially limit yourself? You should do Leetcode until you reach your exhaustion point, similar to how one exercises to failure. When I started going to the gym, I would bench 85 pounds. Three or four sets of this and I could do no more. Now, I bench 185. I don’t go to the gym and continue to bench 85 for three or four sets – that would be useless. If you are only doing 1-2 Leetcode easys/mediums a day when you know your capacity is to do 4 or 5 mediums/hards for 2 hours/day, you are engaging in frivolous discipline and hurting yourself.

- **Attention to detail:** Ironically, as I’ll discuss later, attention to detail was a weakness pointed out to me at multiple internships. But as far as interview prep goes, I was very thorough – I would spend hours rereading data structures notes (absolutely goated: <https://ajzhou.gitlab.io/eecs281/notes/>) picking up small details I missed during my courses every time. I could talk about hashmaps and their design tradeoffs for 3-5 minutes in an interview. Knowing the basics like “O(1) linked list insertion” is sufficient for most interviews, but when you overprepare and get a chance to show your knowledge, the little details you picked up payoff: you distinguish yourself from hundreds of other candidates immediately. Every time an interviewer asked me about hashmaps that season, I would make a point of showing off my knowledge.

- **Don’t say no:** If you come across a piece of knowledge that seems only tangentially relevant to interview prep or too hard to learn, instead of ignoring it, throw it on a list to learn later. Eventually you will find yourself coming back to this list and learning the “tangential concepts”. Some of these may never show up in interviews, some of them inevitably will! An example: for some reason, I never took topological sort seriously in my first recruiting season. I never learned it in class, so I decided not to read about it. The next season, I put it on the list and came back to it. Over 50% of the companies I interviewed with asked a question about topological sort – my D.E. Shaw interviewer asked me a topological sort question and commented that I solved it the fastest he’s ever seen (\<3 minutes).

My interview prep paid off: I ended up getting an offer at [[optiver|Optiver]]. I didn’t cheat or try to game the system – I just put in the work. Despite my parents’ continued suggestions that I was a “gifted” student growing up, I assure you I am not a naturally cracked CS/math whiz – I wasn’t great at high school math, I don’t have any Olympiads under my belt, and the best college I got into was UMich. I am not a genius, but I put in hard work, got a little bit lucky, and broke into quant.

Some quick side-thoughts:

- The Optiver OA was 2 seemingly simple questions – one about graphs and another related to days between dates. You were given 2 hours to complete the OA. Most people I talked to said something along the lines of “that was easy, I solved it in 30 minutes.” I went the extra step: I solved it in 30, spent an additional 30 modularizing and prettyify-ing my code (they noted in the email that engineers review the OAs for style), and another 30 thinking about edge cases and testing them (Did you account for leap years in the second question? Even if you “accounted” for it, did you write tests for it to ensure it worked?). **Attention to detail** paid off.

- Cheating is paradoxical, especially with regards to recruiting. I have seen students put a lot of effort into cheating. Example: off-screen partner in an interview with a calculator to help with math questions (for trading interviews). These elaborate schemes may pay off and get you to the next stage in the interview process, but then what? How high can you build the house of cards? Eventually the cheater’s scheme will falter. You may have seen cheaters that succeed, but in my experience, the paradox is that these people are smart enough that they didn’t need to cheat to begin with – at which point, isn’t cheating just a time-waster detracting from them becoming… even smarter. It’s a video-game like addiction that doesn’t add any value. I’m not saying the occasional interview tip or Google search during an OA is wrong, just that a reliance on cheating will not work unless you are smart enough to not need to cheat and are just doing it for sport.

My intense, brief ~3 to 4-month prep spurt worked but did take a temporary toll on my mental health. I was generally moodier and “depressed” (not in the clinical sense but rather in the loose state college students throw the word around). After I received an offer from Optiver, my emotional state reversed sharply to “ecstatic” – I stopped recruiting.

*<u>A Profitable Hobby</u>*

In sophomore year of high school, I tried to imitate my friend’s penny stock trading success and opened a Robinhood account. I promptly lost most of my savings. The expensive lesson kept me away from the market, until COVID. Something (boredom?) compelled me to begin reading an investing book – *One Up on Wall Street* by [[peter-lynch|Peter Lynch]]. Lynch’s humorful prose kept me engaged, and I kept a reference *Value Investing for Dummies* book by my side to understand the technical terminologies in his book. I continued reading more investing books, slowly beginning to believe that there existed strategies to beat the market skillfully. Regretfully, I was timid and too skeptical of my investing skills to invest any of my own money during the “COVID” crash (the ensuing months would produce enormous returns).

I did, however, keep reading. And eventually by junior year of high school, I was managing small sums of money (some my own, some my parents). I published “investment memos” (a pitch to buy or sell a stock) and my thoughts on the market on my blog. After I got my offer from Optiver, I was itching to return to investing (I didn’t have time for hobbies during recruiting season – another lesson: don’t focus on too many things at once). I had a future memo I wanted to write on Whitehaven Coal, an Australian coal miner, and thought it would be fun to submit it to an upcoming stock pitch competition as a forcing function (I’m not a “productivity-optimizer” bro and don’t know the correct usage of this term, so my bad if it’s not correct, but I just mean the competition acted as a deadline holding me accountable for writing the memo). I submitted the pitch and won an honorable mention.

A few days later, I got an email from a hedge fund called [[madison|Madison Avenue Partners]] asking if I wanted to interview for an investment analyst intern role. I told them I already had an offer for the summer, but they encouraged me to interview anyways, and think about internship timelines later. The first interview was a mix of strange behavioral questions that seemed to be aimed at weeding out posers and liars. Example:

- Q: What are some books you have read?

- A: Mastering the Market Cycle by [[howard-marks|Howard Marks]], …, more books

- Q: Howard Marks is great. Have you read his memos?

- A: Yes, I have.

- Q: Describe your favorite one.

A poser/liar/cheat would have answered the first question, and be stuck by the last. Much easier to do the work and tell the truth than find a way to cheat the system.

The second interview was a case study – luckily, I had self-learned enough finance and I guess had good enough intuition to pass this with ease. While the case study only took 10-15 minutes, I spent another 30-45 minutes asking questions to my interviewer (the MP; managing partner of the fund). Another aside: **always** **ask questions during interviews!** And make them thoughtful and about the interviewer’s work. A good question: Can you talk more about how your work on convertible instrument pricing fits into the larger pipeline at D.E. Shaw? A bad question: What’s the work-life balance like here.

There weren’t any more interviews, but Madison asked for several writing samples (they seemingly read my entire blog), test scores, and reference checks (they made me give them a list of my friends, called my friends, and asked each one “why won’t \[the candidate\] succeed in life?”). Before giving me an offer, they did call me, tell me my friends said I don’t like to work hard on things I don’t like, and asked for “my thoughts”. A general word of advice on tricky behavioral questions like this: it’s always better to accept and talk about improving than to sound defensive. In another question, Madison said they thought I had an “arrogance” problem. In my mind, I heavily disagreed (maybe reflective of an “arrogance” problem in it of itself), but my response was “yes I do, I’ve been dealing with that. Here’s how I’m improving \[…some bullshit\]”. This worked great. A similar framework is useful for responding to more common questions like “what is your greatest weakness?”.

Madison called me and said they were willing to offer me a Winter internship – from mid-January all the way through Optiver began (almost 5 months!). At this point, I still knew very little about Madison – hedge funds prefer to operate in secrecy. On the offer call, I learned this is a \$1bn+ spin-out fund with very low headcount (5-10 FTEs), a strong LP base, and an exceptional track record. I also learned they were paying \$100/hr during the internship – I was stunned that I had stumbled into this opportunity! Excited to explore a new potential career path, I accepted the offer.
