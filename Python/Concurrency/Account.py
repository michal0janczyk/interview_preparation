import sys

from threading import Lock
from threading import Thread

from joblib import Parallel, delayed

class Account:
    def __init__(self):
        self.balance = 0
        self.mutex = Lock()

    def getBal(self):
        return self.balance

    # Synchronizacja lezy w gestii uzytkownika api
    def syncS(self):
        self.mutex.acquire()

    def syncE(self):
        self.mutex.release()

    def add(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def transfer(acc1, acc2, amount):
        acc1.syncS()
        acc2.syncS()

        acc1.withdraw(amount)
        acc2.add(amount)

        acc1.syncE()
        acc2.syncE()

def doTransfer(acc1, acc2):
    for i in xrange(10000):
        Account.transfer(acc1, acc2, 50)

def fun(n):
    return n + 5

def main():
    print "start"

    acc1 = Account()
    acc2 = Account()

    # t1 = Thread(target = doTransfer, args = (acc1, acc2))
    # t2 = Thread(target = doTransfer, args = (acc2, acc1))

    # # doTransfer(acc1, acc2)
    # # doTransfer(acc2, acc1)

    # t1.start()
    # t2.start()

    # t1.join()
    # t2.join()

    # print "{0} {1}".format(acc1.getBal(), acc2.getBal())

    l = [1,2,3,4,5,6,7,8]
    results = Parallel(n_jobs = -1)(delayed(fun)(i) for i in l)

    print results

if __name__ == "__main__":
    main()
