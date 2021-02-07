"""
    A martingale is any of a class of betting strategies that originated from and were popular in 18th century France.
    The simplest of these strategies was designed for a game in which the gambler wins his stake if a coin comes up heads and loses it if the coin comes up tails.
    The strategy had the gambler double his bet after every loss, so that the first win would recover all previous losses plus win a profit equal to the original stake.
    The martingale strategy has been applied to roulette as well, as the probability of hitting either red or black is close to 50%.
    Since a gambler with infinite wealth will, almost surely, eventually flip heads, the martingale betting strategy was seen as a sure thing by those who advocated it.
    Of course, none of the gamblers in fact possessed infinite wealth, and the exponential growth of the bets would eventually bankrupt "unlucky" gamblers who chose to use the martingale.
    The gambler usually wins a small net reward, thus appearing to have a sound strategy. However, the gambler's expected value does indeed remain zero (or less than zero)
    because the small probability that he will suffer a catastrophic loss exactly balances with his expected gain.
    (In a casino, the expected value is negative, due to the house's edge.)
    The likelihood of catastrophic loss may not even be very small. The bet size rises exponentially.
    This, combined with the fact that strings of consecutive losses actually occur more often than common intuition suggests, can bankrupt a gambler quickly.
"""

import random
import matplotlib.pyplot as plt

def won():
    return random.random() < 0.5 # [0.0, 1.0)

acc = 10
curBet = 1

series = []
nWins = 0

nCurLosses = 0
longestLosing = 0

while True:
    print(acc, nWins)

    series += [acc]
    acc -= curBet

    if won():
        acc += 2 * curBet
        curBet = 1

        nWins += 1

        if nCurLosses > longestLosing:
            longestLosing = nCurLosses

        nCurLosses = 0
    else:
        curBet += 1
        nCurLosses += 1

    if acc <= 0:
        break

plt.plot(series)
plt.show()

print("losing streak = {0}".format(longestLosing))
