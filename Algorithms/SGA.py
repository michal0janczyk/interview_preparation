"""
    The algorithms for finding the functions’ maxima being typically a part of the optimization are
    generally limited for regular convex functions. However, many functions are multimodal, not continuous, and
    not-differentiable. Methods with stochastic selection are used to optimize these functions. While traditional
    searching techniques use the characteristics of the problem to define the next point of the chosen sampling (e.g.
    the gradient, hessian, linearity and continuity), the stochastic technique does not require such information,
    except the value of the function at the points being analyzed. Instead, the other sampling points are defined
    based more on the stochastic rules of selection or decision making than on several deterministic rules. Genetic
    algorithms are used to solve difficult problems that have as objective functions that do not possess “good”
    features such as continuity, derivability, fulfillment of Lipchitz conditions, etc.
"""

import math
import random
import struct

nIter = 100
popSize = 100
solutionFound = False
genesPerCh = 60

minV, maxV = 0.5, 2.5

mutProb = 0.1
cxProb = 0.6

elitism = 0.5
nBest = int(elitism * popSize)

def genPop(size):
    pop = []

    for iP in xrange(size):
        inD = random.uniform(minV, maxV)
        pop += [inD]

    return pop

def fitnessFun(x):
    assert minV <= x <= maxV

    res = (math.exp(x) * math.sin(10 * math.pi * x) + 1) / (x + 5)
    return float(res)

def toBytes(res):
    bits = list(bin(res))[2: ]
    return bits

def roulette(fits):
    sFits = sum(fits)
    normFits = [f / sFits for f in fits]

    r = random.random()
    cf = 0.0

    for cur in xrange(len(normFits)):
        cf += normFits[cur]

        if cf >= r:
            return cur

def floatToBits(f):
    s = struct.pack('>f', f)
    res = list(bin(struct.unpack('>L', s)[0])[2 : ])

    while len(res) < 32:
        res = ['0'] + res

    return res

def bitsToFloat(b):
    assert len(b) == 32
    # print b, len(b)

    s = struct.pack('>L', int(''.join(b), 2))
    return struct.unpack('>f', s)[0]

def crossover(val1, val2):
    bits1 = floatToBits(val1)
    bits2 = floatToBits(val2)

    # print val1, val2
    # print bits1, bits2
    # print len(bits1), len(bits2)

    assert len(bits1) == len(bits2)
    iCX = random.randint(0, len(bits1) - 1)

    newVal1 = bits1[ : iCX] + bits2[iCX : ]
    newVal2 = bits2[ : iCX] + bits1[iCX : ]

    return bitsToFloat(newVal1), bitsToFloat(newVal2)

def mutate(val):
    bits = floatToBits(val)
    i = random.randint(0, (len(bits) - 1))

    # We flip the bit.
    if bits[i] == '0':
        bits[i] = '1'
    else:
        bits[i] = '0'

    return bitsToFloat(bits)

def main():
    pop = genPop(popSize)
    bestFit = None

    for iIter in xrange(nIter):
        print("{0}/{1}".format(iIter + 1, nIter))

        fits = [fitnessFun(t) for t in pop]
        curBest = max(fits)

        if bestFit is None or curBest > bestFit:
            bestFit = curBest

        newPop = []
        i = 0

        while i < len(pop):
            genOp = random.random()

            if genOp <= cxProb and i != len(pop) - 1:
                ind1 = roulette(fits)
                ind2 = roulette(fits)

                val1, val2 = crossover(pop[ind1], pop[ind2])

                newPop += [val1]
                newPop += [val2]

                i += 2
            elif genOp > cxProb <= cxProb + mutProb:
                ind = roulette(fits)
                newPop += [mutate(pop[ind])]
                i += 1
            else:
                # Otherwise we do not modify the current individual
                # and it is retained in the current population (i.e. reproduced).
                ind = roulette(fits)
                newPop += [pop[ind]]
                i += 1

        assert len(newPop) == len(pop)

        for i in xrange(len(newPop)):
            if math.isnan(newPop[i]) or newPop[i] < minV or newPop[i] > maxV:
                newPop[i] = random.uniform(minV, maxV)

        pop = newPop
        # print pop

        print round(bestFit, 3), round(curBest, 3)

if __name__ == "__main__":
    main()
