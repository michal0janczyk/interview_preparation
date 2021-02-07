"""
    The heap is one maximally efficient implementation of an abstract data type called a priority queue,
    and in fact priority queues are often referred to as "heaps", regardless of how they may be implemented.
    A common implementation of a heap is the binary heap, in which the tree is a complete binary tree (see figure).
    Heaps are also crucial in several efficient graph algorithms such as Dijkstra's algorithm. In a heap, the highest (or lowest) priority element is always stored at the root.
    A heap is not a sorted structure and can be regarded as partially ordered.
    As visible from the heap-diagram, there is no particular relationship among nodes on any given level, even among the siblings.
    When a heap is a complete binary tree, it has a smallest possible height—a heap with N nodes always has log N height.
    A heap is a useful data structure when you need to remove the object with the highest (or lowest) priority.
"""

import random

class Heap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def insert(self, val):
        l = len(self.heapList)
        self.heapList.append(val)
        self.currentSize += 1
        self.sortHeap(l)

    def sortHeap(self, pos):
        if pos == 0:
            return
        lastElem = self.getPos(pos)

        if self.heapList[pos] > self.heapList[lastElem]:
            self.swapPos(pos, lastElem)

    def getPos(self, pos):
        if pos == 1 or pos == 2:
            return 0
        # if pos = odd number => left child
        if pos % 2 == 0:
            return (pos - 2) / 2
        # if pos = even number => right child.
        else:
            return (pos - 1) / 2

    def swapPos(self, pos1, pos2):
        temp = self.heapList[pos1]
        self.heapList[pos1] = self.heapList[pos2]
        self.heapList[pos2] = temp

def main():
    h = Heap()

    for _ in xrange(10):
        val = random.randint(0, 10)
        h.instert(val)

if __name__ == "__main__":
    main()
