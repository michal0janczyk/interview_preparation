import numpy as np
import matplotlib.pyplot as plt

import random
import threading
import time

pEndLine = 1000
pNRunners = 5

# 0 -> task1 (no synchro)
# 1 -> task2 (cyclic barrier)
# 2 -> task3 (critical section)
# 3 -> task4 (semaphore)
mode = 0

class Counter:
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()

    def reset(self):
        self.lock.acquire()
        self.count = 0
        self.lock.release()

    def increment(self):
        self.lock.acquire()
        self.count += 1
        self.lock.release()

    def getCount(self):
        return self.count

class Runner:
    def __init__(self, idName, nRunners):
        self.idName = idName
        self.meters = 0
        self.finished = False
        self.nRunners = nRunners
        self.lock = threading.Lock()


    def run(self):
        while self.meters < pEndLine:
            time.sleep(random.randint(1, 30) / 1000.0) # [1, 5] ms
            self.meters += 1

        self.finished = True

    def runCB(self):
        while self.meters < pEndLine:
            time.sleep(random.randint(1, 30) / 1000.0) # [1, 5] ms
            self.meters += 1

            # print "{0}) {1}".format(self.idName, self.meters)

            if self.meters == 250:
                print "Barrier start"
                self.counter.increment()

                # Warning: do not reuse this semaphore.
                # Problematic if threads are scheduled out in this line (semaphore released more than nRunners times).
                if self.counter.getCount() == self.nRunners:
                    print "Last Runner"
                    for i in xrange(self.nRunners - 1):
                        self.sem.release()
                else:
                    self.sem.acquire()
                    print "Release all"

        self.finished = True

    def runCS(self):
        self.isBusy = False
        while self.meters < pEndLine:
            time.sleep(random.randint(1, 5) / 1000.0) # [1, 5] ms
            self.meters += 1

            if self.meters == 500:
                self.lock.acquire(True)
                print "500m Start CS"
                print "{0}) {1}".format(self.idName, self.meters)
            elif self.meters == 750:
                self.lock.release()
                print "750m Release CS"
                print "{0}) {1}".format(self.idName, self.meters)

            # if self.meters == 500:
            #     if self.isBusy == False:
            #         self.counter.increment()
            #         self.lock.release()
            #         self.isBusy = True
            #         print "{0})".format(self.idName)
            #     else:
            #         self.lock.acquire()
            #         print "Stay na 500m"
            # elif self.meters == 750:
            #     self.lock.release()
            #     self.isBusy = False
            #     print "3rd lap 750m"

    def runSM(self):
        while self.meters < pEndLine:
            time.sleep(random.randint(1, 5) / 1000.0) # [1, 5] ms
            self.meters += 1

        if self.counter.getCount == 1:
            self.counter.reset()
            print "if getCount = 1"
            print "{0}) {1}".format(self.idName, self.meters)
        else:
            self.counter.increment()
            print "else"
            print "{0}) {1}".format(self.idName, self.meters)

    def getMeters(self):
        return self.meters

    def isFinished(self):
        return self.finished

    def setState(self, sem, counter):
        self.sem = sem
        self.counter = counter

def task1(runners):
    threads = []

    for i in xrange(pNRunners):
        t = threading.Thread(target = runners[i].run)
        threads += [t]

    for iA in xrange(pNRunners):
        threads[iA].start()

    nSteps = 0
    Y = [[] for _ in xrange(len(runners))]

    plt.ion()

    nXSteps = 1
    plt.xlim(1, nXSteps)

    plt.ylim(0, 1000)

    while True:
        nSteps += 1

        # time.sleep(0.5)
        nFinished = 0

        for runner in runners:
            print "{0}) {1}".format(runner.idName, runner.getMeters())

            if runner.isFinished():
                nFinished += 1

        for i in xrange(len(runners)):
            Y[i] += [runners[i].getMeters()]

        x = [i for i in xrange(1, nSteps + 1, 1)]

        for i in xrange(len(Y)):
            plt.plot(x, Y[i])

        if nSteps >= nXSteps:
            nXSteps *= 2
            plt.xlim(1, nXSteps)

        # plt.xlim(1, nSteps)

        # plt.pause(0.00000001)
        time.sleep(0.5)
        # plt.pause(1.0)

        if nFinished == pNRunners:
            print "All finished #Task1"
            break

    plt.show()


def task2(runners):
    threads = []

    sem = threading.Semaphore(0)
    counter = Counter()

    for i in xrange(pNRunners):
        t = threading.Thread(target = runners[i].runCB)
        threads += [t]

        runners[i].setState(sem, counter)

    for iA in xrange(pNRunners):
        threads[iA].start()

    print "All finished #Task2"

def task3(runners):
    threads = []

    for i in xrange(pNRunners):
        t = threading.Thread(target = runners[i].runCS)
        threads += [t]

    for iA in xrange(pNRunners):
        threads[iA].start()

    print "All finished #Task3"

def task4(runners):
    threads = []

    sem = threading.Semaphore(2)
    counter = Counter()

    for i in xrange(pNRunners):
        t = threading.Thread(target = runners[i].runSM)
        threads += [t]

        runners[i].setState(sem, counter)

    for iA in xrange(pNRunners):
        threads[iA].start()

    print "All finished #Task4"

def main():
    runners = []
    # plt.ion()

    for i in xrange(pNRunners):
        runners += [Runner(i, pNRunners)]

    if mode == 0:
        print "#Task1 - No synchronization"
        task1(runners)
    elif mode == 1:
        print "#Task2 - Cyclic barrier"
        task2(runners)
    elif mode == 2:
        print "#Task3 - Promotion"
        task3(runners)
    elif mode == 3:
        print "#Task4 - Promotion"
        task4(runners)
    else:
        print "Bad mode = {0}".format(mode)

if __name__ == "__main__":
    main()
