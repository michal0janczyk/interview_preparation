"""
    A binary heap is a heap data structure that takes the form of a binary tree. Binary heaps are a common way of implementing priority queues.
    A binary heap is defined as a binary tree with two additional constraints:
    Shape property: a binary heap is a complete binary tree; that is, all levels of the tree, except possibly the last one (deepest) are fully filled,
    and, if the last level of the tree is not complete, the nodes of that level are filled from left to right.
    Heap property: the key stored in each node is either greater than or equal to (≥) or less than or equal to (≤) the keys in the node's children, according to some total order.
    Heaps where the parent key is greater than or equal to (≥) the child keys are called max-heaps; those where it is less than or equal to (≤) are called min-heaps.
    Efficient (logarithmic time) algorithms are known for the two operations needed to implement a priority queue on a binary heap:
    inserting an element, and removing the smallest (largest) element from a min-heap (max-heap).
    Binary heaps are also commonly employed in the heapsort sorting algorithm, which is an in-place algorithm owing to the fact that
    binary heaps can be implemented as an implicit data structure, storing keys in an array and using their relative positions within that array to represent child-parent relationships.
"""

import random

class Node:
    def __init__(self, val, p, l = None, r = None):
        self.val = val
        self.parent = p

        self.left = l
        self.right = r

# MAX HEAP
class Heap:
    def __init__(self):
        self.root = None
        self.currentSize = 0

    def insert(self, val):
        self.currentSize += 1

        if self.root is None:
            self.root = Node(val)
            return

        curNode = Node(val)
        curParent = getLastNode()

        if curParent.left is None:
            curParent.left = curNode
        else:
            curParent.right = curNode

        curNode.parent = curParent

        while curNode.val > curParent.val:
            # Swap
            curNode.val, curParent.val = curParent.val, curNode.val

            curNode = curParent
            curParent = curParent.parent

    # Wyjmujemy najwiekszy element (czyli ten w korzeniu).
    def extract(self):
        res = self.root.val
        last = self.getLastNode()

        self.root.val = last.val

        if last.parent.left == last:
            last.parent.left = None
        else:
            last.parent.right = None

        return res

    # Znajdujemy BFS-em ostatni wezel na ostatnim poziomie.
    def getLastNode():
        pass

    def heapify(vals):
        pass

def main():
    h = Heap()

    for _ in xrange(10):
        val = random.randint(0, 10)
        h.insert(val)

if __name__ == "__main__":
    main()
