"""
    Rosenbrock function is a non-convex function used as a performance test problem for optimization algorithms introduced by Howard H. Rosenbrock in 1960.
    It is also known as Rosenbrock's valley or Rosenbrock's banana function.
    The global minimum is inside a long, narrow, parabolic shaped flat valley. To find the valley is trivial.
    To converge to the global minimum, however, is difficult.
    The function is defined by f(x,y)=(a-x)^{2}+b(y-x^{2})^{2}}
"""

import random
import matplotlib.pyplot as plt
nIter = 100
popSize = 100

minV, maxV = -1000.0, 1000.0

def rosenbrock(x, y):
    return ((1.0 - x) ** 2) + 100.0 * ((y - x ** 2) ** 2)

def plot(fits):
    xFit = [x + 1 for x in xrange(len(fits))]

    plt.plot(xFit, fits, 'b--')
    plt.show()

def main():
    best = None
    bestFit = None
    bestFitList = []

    for iIter in xrange(nIter):
        # Tworzymy losowe rozwiazania
        pop = []

        for iP in xrange(popSize):
            inD = (random.randint(minV, maxV), random.randint(minV, maxV))
            pop += [inD]

        # Liczymy fitness (czyli rosenbrocka)
        fit = [rosenbrock(*t) for t in pop]

        # Wybieramy rozwiazanie, zapisujemy fitness
        curBestFit = min(fit)

        if bestFit is None or curBestFit < bestFit:
            bestFit = curBestFit

            iMin = fit.index(bestFit)
            best = pop[iMin]

        bestFitList += [bestFit]

        # Wypisujemy do pliku najlepsze rozwiazanie, poszczegolne fitness
        with open("fit.dat", "a") as f: # Append
            f.write("{0} {1}\n".format(iIter, bestFit))

    # Wykres zmieniajacego sie fitness (x - iteracja, y - fit)
    plot(bestFitList)

if __name__ == "__main__":
    main()
