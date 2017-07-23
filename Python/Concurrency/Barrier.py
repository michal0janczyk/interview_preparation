import math
import threading

pNThreads = 3

class Counter:
    def __init__(self):
        self.counter = 0
        self.lock = threading.Lock()

    def getCounter(self):
        self.lock.acquire()
        value = self.counter
        self.lock.release()

        return value

    def addCounter(self):
        self.lock.acquire()
        self.counter += 1
        self.lock.release()

def fun(iT, sem, counter):
    for i in xrange(1000000): # 1m
        if i == 500000:
            print "{0}) 500k".format(iT)

            if counter.getCounter() == pNThreads - 1:
                for iP in xrange(pNThreads - 1):
                    sem.release()
            else:
                counter.addCounter()
                sem.acquire()

        math.sqrt(2)

    print "Finished"

threads = []

sem = threading.Semaphore(0)
counter = Counter()

for iP in xrange(pNThreads):
    t = threading.Thread(target = fun, args=(iP, sem, counter))
    threads += [t]

for iP in xrange(pNThreads):
    threads[iP].start()
