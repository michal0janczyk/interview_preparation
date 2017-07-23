"""
A race condition or race hazard is the behavior of an electronic, software, or other system where the output is dependent on the sequence or 
timing of other uncontrollable events. It becomes a bug when events do not happen in the order the programmer intended. The term originates 
with the idea of two signals racing each other to influence the output first.
"""

import numpy as np
import random
import threading
import time

# 0 -> firstRun (no synchro)
# 1 -> secondRun (cyclic barrier)
mode = 0

class Car(object):
    def __init__(self, name):
        self.lock = threading.Lock()
        self.cycleTime = 0
        self.distance = 0
        self.curDist = 0
        self.nCycles = 0
        self.name = name
        self.finished = False

    def drive(self, raceLength):
        while self.distance < raceLength:
            self.cycleTime = time.sleep(random.randint(1, 5) / 1000.0)
            self.distance += 1
            self.curDist += 1
            self.nCycles += 1

        self.finished = True

    def getNCycles(self):
        return self.nCycles

    def getNDistance(self):
        return self.distance

    def isFinished(self):
        # Blokujemy az bedzie finished (np. lock)
        return self.finished

    def setStateSem(self, sem):
        self.sem = sem

class RaceCar(Car):
    def __init__(self, name):
        super(RaceCar, self).__init__(name)
        # Car.__init__(self, name)
        self.cycleTime = random.randint(10, 20)
        self.distance = random.randint(200, 500)

class Truck(Car):
    def __init__(self, name):
        super(Truck, self).__init__(name)
        # Car.__init__(self, name)
        self.cycleTime = random.randint(20, 30)
        self.distance = random.randint(100, 300)

def addToTable(raceCar, truck):
    tab = []

    for i in xrange(raceCar):
        tab += [RaceCar("RaceCar")]

    for i in xrange(truck):
        tab += [Truck("Truck")]

    return tab

def firstRun(cars):
    threads = []
    sem = threading.Semaphore(0)

    for i in xrange(len(cars)):
        t = threading.Thread(target = cars[i].drive, args=(5000,))
        print "Drive"
        threads += [t]

        cars[i].setStateSem(sem)

    for iC in xrange(len(cars)):
        threads[iC].start()

    while True:
        time.sleep(1.0) # zamienic na metode synchronizacji (np. lock)
        nFinished = 0

        for car in cars:
            print "%10s %10s" % (car.name, car.getNCycles())

            if car.isFinished():
                nFinished += 1

        if nFinished == len(cars):
            print "All cars finished #firstRun"
            break

def main():
    pNCars = addToTable(raceCar = 5, truck = 5)

    if mode == 0:
        print "#Task1"
        firstRun(pNCars)
    elif mode == 1:
        print "#Task2"
        secondRun()
    else:
        print "Bad mode = {0}".format(mode)

if __name__ == "__main__":
    main()
