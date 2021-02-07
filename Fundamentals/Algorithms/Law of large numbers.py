"""
    In probability theory, the law of large numbers (LLN) is a theorem that describes the result of performing the same experiment a large number of times.
    According to the law, the average of the results obtained from a large number of trials should be close to the expected value,
    and will tend to become closer as more trials are performed.
    The LLN is important because it "guarantees" stable long-term results for the averages of some random events.
    For example, while a casino may lose money in a single spin of the roulette wheel, its earnings will tend towards a predictable percentage over a large number of spins.
    Any winning streak by a player will eventually be overcome by the parameters of the game.
    It is important to remember that the LLN only applies (as the name indicates) when a large number of observations is considered.
    There is no principle that a small number of observations will coincide with the expected value or that a streak of one value will immediately be "balanced" by the others.
"""

import math
import random
import sys

hunThousand = 100000
million = 1000000

perfAvg = 3.5
diff = []

# losujemy n razy rzut koscia
for x in xrange(hunThousand, million, hunThousand):
    sys.stdout.write("{0}...".format(x))

    l = 0.0
    for i in xrange(x):
        n = random.randint(1,6)
        l += n
    l /= x
    print(" {0}".format(l))

    l -= perfAvg
    l = math.fabs(l)
    diff += [l]

diffAvg = sum(diff) / len(diff)

std = 0.0

for d in diff:
    std += (diffAvg - d) ** 2

print diffAvg, std
