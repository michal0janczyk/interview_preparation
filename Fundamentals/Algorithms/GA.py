"""
    In a genetic algorithm, a population of candidate solutions (called individuals, creatures, or phenotypes) to an optimization problem is evolved toward better solutions.
    Each candidate solution has a set of properties (its chromosomes or genotype) which can be mutated and altered; traditionally,
    solutions are represented in binary as strings of 0s and 1s, but other encodings are also possible.
    The evolution usually starts from a population of randomly generated individuals, and is an iterative process, with the population in each iteration called a generation.
    In each generation, the fitness of every individual in the population is evaluated;
    the fitness is usually the value of the objective function in the optimization problem being solved. 
    The more fit individuals are stochastically selected from the current population, and each individual's genome is modified (recombined and possibly randomly mutated)
    to form a new generation. The new generation of candidate solutions is then used in the next iteration of the algorithm.
    Commonly, the algorithm terminates when either a maximum number of generations has been produced, or a satisfactory fitness level has been reached for the population.
"""

import random
import matplotlib.pyplot as plt

nIter = 1000
popSize = 100

minV, maxV = -2.0, 2.0

mutProb = 0.1
cxProb = 0.9

def rosenbrock(x1, x2):
    return (10.0 * x1**4 - 20.0 * x1**2 * x2 + 10.0 * x2**2 + 1.0 * x1**2 - 2 * x1 + 5.0)

def plot(fits):
    xFit = [x + 1 for x in xrange(len(fits))]

    plt.plot(xFit, fits, 'b--')
    plt.show()

def genPop(size):
    pop = []

    for iP in xrange(size):
        inD = [random.uniform(minV, maxV), random.uniform(minV, maxV)]
        pop += [inD]

    return pop

def crossover(ind1, ind2):
    # Swapped part of first individual.
    iElem = random.randint(0, 1)

    if iElem == 0:
        temp = ind1[0]
        ind1[0] = ind2[1]
        ind2[1] = temp
    else:
        temp = ind1[1]
        ind1[1] = ind2[0]
        ind2[0] = temp

def main():
    best = None
    bestFit = None
    bestFitList = []

    # Tworzymy losowe rozwiazania
    pop = genPop(popSize)

    for iIter in xrange(nIter):
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
            msg = "{0} {1}\n".format(iIter, bestFit)
            f.write(msg)
        print msg

        # MUTACJE
        for t in pop:
            if random.random() < mutProb: # Losuje liczbe [0.0, 1.0)
                iF = random.randint(0, len(t) - 1)
                t[iF] = random.uniform(minV, maxV)

        # CROSSOVER
        for t in pop:
            if random.random() < cxProb:
                iP = random.randint(0, popSize - 1)
                crossover(t, pop[iP])

        fit = [rosenbrock(*t) for t in pop]

        # Zostawiamy najlepsze 50% populacji
        newPop = []

        while len(newPop) < (popSize / 2):
            assert len(fit) == len(pop)

            minIndex = fit.index(min(fit))
            curBest = pop[minIndex]

            newPop += [curBest]

            del pop[minIndex]
            del fit[minIndex]

        pop = newPop
        pop += genPop(popSize / 2)

        assert len(pop) == popSize
    # Wykres zmieniajacego sie fitness (x - iteracja, y - fit)
    plot(bestFitList)

if __name__ == "__main__":
    main()
