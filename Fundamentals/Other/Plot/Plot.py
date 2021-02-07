import matplotlib.pyplot as plt
import numpy as np
import random
import sys

def calc(nIter):
    s = 0.0

    for i in xrange(nIter):
        cur = random.randint(1, 6)
        s += cur

    avg = s / nIter
    return avg

def present(avgs):
    xList = [i for i in xrange(1, len(avgs) + 1, 1)]
    stdevs = []
    line = [3.5 for _ in xList]

    for i in xrange(1, len(avgs) + 1, 1):
        cur = np.std(avgs[ : i])
        stdevs += [cur]

    plt.plot(xList, avgs, 'k-', label = "value")
    plt.plot(xList, stdevs, 'b-', label = "stdevs")
    plt.plot(xList, line, 'r--')

    plt.legend(loc = 2)
    plt.xlabel("#iterations")
    plt.ylabel("avg value")

    plt.title("Die roll")
    plt.show()

separator=","

def dump(avgs):
    with open("data.dat", 'w') as f:
        for n in avgs:
            f.write(str(n) + separator)

def main1():
    if len(sys.argv) != 2:
        print "Usage: numbers.py [#iterations]"
        sys.exit(1)

    avgs = []

    maxNIter = int(sys.argv[1])
    for i in xrange(1, maxNIter + 1, 1):
        print("{0}/{1}".format(i, maxNIter))

        cur = calc(i)
        avgs += [cur]

    assert len(avgs) == maxNIter

    # present(avgs)
    # dump(avgs)

def readData(fName):
    with open(fName, 'r') as f:
        s = f.read()
    return [float(n) for n in s.split(separator) if n]

def main2():
    # We read the data from file.
    avgs = readData("data.csv")
    present(avgs)

if __name__ == "__main__":
    # main1()
    main2()
