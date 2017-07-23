"""
    Depth-first search
    DFS is an algorithm for traversing or searching tree or graph data structures.
    One starts at the root (selecting some arbitrary node as the root in the case of a graph) and explores as far as possible along each branch before backtracking.
    Breadth-first search
    BFS is an algorithm for traversing or searching tree or graph data structures.
    It starts at the tree root (or some arbitrary node of a graph, sometimes referred to as a 'search key') and explores the neighbor nodes first,
    before moving to the next level neighbors.
    A* search algorithm
    A* is a computer algorithm that is widely used in pathfinding and graph traversal,
    the process of plotting an efficiently directed path between multiple points, called nodes.
    It enjoys widespread use due to its performance and accuracy.
    However, in practical travel-routing systems, it is generally outperformed by algorithms which can pre-process the graph to attain better performance,
    although other work has found A* to be superior to other approaches
"""

import heapq
import random
import sys

class Node:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

        self.x = 0
        self.n = [] # Indices of neighbors

        self.cost = None
        self.cameFrom = None

class Graph:
    def __init__(self):
        self.nodes = []

    def addNode(self, x, X, Y):
        n = Node(X, Y)
        n.x = x

        self.nodes += [n]
        return len(self.nodes) - 1

    def addEdge(self, i1, i2):
        self.nodes[i1].n += [i2]

    def DFS(self, iNode, visited = set()):
        for iNeigh in self.nodes[iNode].n:
            if iNeigh in visited:
                continue

            print self.nodes[iNeigh].x
            visited.add(iNeigh)
            self.DFS(iNeigh, visited)

    def BFS(self, iNode, depth = 1, pQ = [], visited = set()):
        for iNeigh in self.nodes[iNode].n:
            if iNeigh in visited:
                continue

            pQ += [(depth, iNeigh)]

        if not pQ or pQ is None:
            return

        pQ.sort()

        iNode = pQ[0][1]
        print self.nodes[iNode].x

        visited.add(iNode)
        pQ = pQ[1 : ]
        self.BFS(iNode, depth + 1, pQ, visited)

    def clear(self):
        for node in self.nodes:
            node.cost = sys.maxint
            node.cameFrom = None

    def reconPath(self, iStart, iEnd):
        res = [iEnd]
        curNode = iEnd

        while curNode:
            res += [self.nodes[curNode].cameFrom]
            curNode = res[-1]

            if curNode == iStart:
                break

        return list(reversed(res))

    def addSorted(self, iCur, openS):
        for i in xrange(len(openS)):
            # Znalezlismy miejsce w srodku.
            if self.nodes[openS[i]].cost >= self.nodes[iCur].cost:
                openS.insert(i, iCur)
                return

        openS.append(iCur)

    def heuristicCost(self, iStart, iEnd):
        (x1, y1) = iStart
        (x2, y2) = iEnd
        return (abs(x1 - x2) + abs(y1 - y2))

    def aStar(self, iStart, iEnd):
        closedS = set()

        openS = [iStart]
        openSSet = set([iStart])

        self.clear()
        self.nodes[iStart].cost = 0

        while openS:
            cur = heapq.heappop(openS)[1]
            openSSet.remove(cur) # chyba niepotrzebne

            if cur == iEnd:
                return self.reconPath(iStart, iEnd)

            closedS.add(cur)

            # Patrzymy na sasiadow
            for iNeigh in self.nodes[cur].n:
                if iNeigh in closedS:
                    continue

                if iNeigh not in openSSet:
                    # self.addSorted(iNeigh, openS)
                    # print openS
                    heapq.heappush(openS, (self.nodes[iNeigh].cost, iNeigh))
                    openSSet.add(iNeigh)

                # Zmieniamy odleglosci / cameFrom jesli znalelismy lepsza sciezke
                curCost = self.nodes[cur].cost + 1
                if curCost < self.nodes[iNeigh].cost:
                    self.nodes[iNeigh].cost = curCost
                    self.nodes[iNeigh].cameFrom = cur
                    newNode = (self.nodes[iNeigh.cost + heuristicCost])

def main():
    g = Graph()

    nNodes = 5
    idList = []

    for i in xrange(nNodes):
        X = random.randint(0, 10)
        Y = random.randint(0, 10)

        g.addNode(i, X, Y)
        idList += [i]

    g.addEdge(idList[0], idList[1])

    # print "DFS"
    # g.DFS(i1)

    # print "BFS"
    # g.BFS(i1)

    print "Result =",g.aStar(i1, i3)
    print "Result =",g.aStar(i1, i4)

    print("Finish")

if __name__ == "__main__":
    main()

    # for iNeigh in self.nodes[iNode].n:
        #     if iNeigh in visited:
        #         continue

        #     print self.nodes[iNeigh].x

        # for iNeigh in self.nodes[iNode].n:
        #     if iNeigh in visited:
        #         continue

        #     visited.add(iNeigh)
        #     self.BFS(iNeigh)
