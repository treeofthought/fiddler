# [Can you even the odds?](https://thefiddler.substack.com/p/can-you-even-the-odds)
## TLDR
My answer is 31/61, or roughly 50.8%.  Running `even_the_odds.py` will simulate three versions of turn order and report on A's win probability for each.

I don't have an analytic solution to thue morse, but `even_the_odds.py` has a function which computes A's win probability to arbitrary precision.  That yields a win rate of 50.159% for A.

## Basic alternation
As a warmup, let's solve the win probabilities for the alternating turn order.

The game has two states. State 1, "it is A's turn" and State 2 "it is B's turn"

Let "Pi" denote "probability that A wins, given the game is in state i"

The probability that A wins given either game state is

P1 = 1/6 + (5/6) * P2

P2 = (5/6) * P1

In other words, A will win with their roll 1/6 of the time...5/6 of the time, the game transitions to state 2.  In state 2, A's only chance for winning is the 5/6 probability of transitioning back to state 1.

We can solve this system of equations and learn that

P1 = 6/11

P2 = 5/11

My simulator agrees that A wins about 54.5% of the time! 

## Snake draft
The snake draft version of the game has three distinct states

S1 => A's first turn

S2 => B gets two turns in a row

S3 => A gets two turns in a row

We can set up a system just like for the basic case,

P1 = 1/6 + (5/6) * P2

P2 = (25/36) * P3

P3 = 1/6 + 5/36 + (25/36) * P2

Solving this system yields

P1 = 31/61

P2 = 25/61

P3 = 36/61

My simulator agrees that A wins about 50.8% of the time! 

## Thue Morse
I have not been able to reason out a good way to compute win probabilities as a function of current and future state.  The best I have been able to do here is simulate the outcome, and recognize that if we analyze the sequence of length N, we've computed A's win probability up to a maximum error of (5/6)^N (the probability the game continues after turn N), and thus we can calculate A's win probability to arbitrary precision.  Doing this yields a win rate of 50.159% for A.

My simulate came up with 50.20%, which is a bit futher from the truth than I like!