REPO: SmthnNotTaken/Interns-IITM
PATH: Graviton/README.md
URL: https://github.com/SmthnNotTaken/Interns-IITM/blob/main/Graviton/README.md

# Role : Quant Researcher

# Test
3 challenging Probability puzzles. We had to give a descriptive answer.
I think they shortlisted people who solved 2 or more.

## Q1:
200 people in a firm, who trade in various markets. What is minimum number of markets that need to exist, such that for any 2 people A and B in the firm, there exists at least 1 market that A trades in and B does not, and vice versa.

<details hide>
  <summary>Answer</summary>
  10 markets.
  <details hide>
  <summary>Solution</summary>
 Logic: If there are N markets, we can give everyone a combination of N/2 markets to every person in the firm. Each combination will be unique, hence must satisfy the criteria mentioned above.
</details>
</details>

## Q2:
You are playing a game wherein you have 100 turns and 2 chests. Each turn you can choose to wait or stash. When you wait, one coin is randomly added to one of the chests with equal probability. When you stash, you collect the coins inside one of the 2 chests, with equal probability. 

Part A:
If you must stash exactly N times, derive a formula for the maximum expected returns from this game. 
<details hide>
  <summary>Solution</summary>
  Wait 100-N turns, stash the last N turns. Maximum expected returns is calculated using 2 cases. Case 1, where returns from only 1 chest is stashed in all N stashes. Case 2, where all coins are stashed. 
</details>
<br />
Part B:
What is the value of N, for which the expected returns from this game will be maximised.
<br />
<details hide>
  <summary>Answer</summary>
  6
</details>


# Interview
2 Rounds of Interview, first round was just probability puzzles which continuosuly increased in difficulty.
1. You are given an unfair coin, devise a 2 player game that is fair (Both players have equal chance of winning). If the coin was fair, the game of a single coin flip would be a fair game.
   <details hide>
     <summary>Solution</summary>
     The idea is that a fair game involves symmetry. When you flip 2 coins (one after the other), the probabilty of Tails followed by Heads is equal to Probabiltiy of Heads followed by Tails. Assign these as the winning outcome to the players. If both flips are heads or both are tails, they can repeat the game.
   </details>
2. Given a fair coin, how would you make a game which gives player 1 double the chance of winning as compared to player 2.
      <details hide>
     <summary>Solution</summary>
        Exploiting the idea from the previous game, we can flip 2 coins and assign the 4 possible outcomes : 2 outcomes are winning for player 1, 1 outcome is winning for player 2, and the last outcome is repeat game.
   </details>
3. Generalise the above question : given a coin and a fraction p/q, how can you make a game wherein player A has a p/q chance of winning and player B has a 1-p/q chance of winning.
   <details hide>
     <summary>Solution</summary>
     Choose $n = ceil({\log_2{(p+q)}})$. Perform n flips (one after the other). We have $2^n$ outcomes. Assign $p$ of them to player A , $q$ of them to player B and $2^n-p-q$ to repeat game. 
   </details>
4. What would you do if p/q is replaced by an irrational number.
