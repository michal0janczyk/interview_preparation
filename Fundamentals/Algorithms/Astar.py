"""
    A* is an informed search algorithm, or a best-first search, meaning that it solves problems by searching among all possible paths to the solution
    (goal) for the one that incurs the smallest cost (least distance travelled, shortest time, etc.),
    and among these paths it first considers the ones that appear to lead most quickly to the solution.
    It is formulated in terms of weighted graphs: starting from a specific node of a graph, it constructs a tree of paths starting from that node,
    expanding paths one step at a time, until one of its paths ends at the predetermined goal node.
    At each iteration of its main loop, A* needs to determine which of its partial paths to expand into one or more longer paths.
    It does so based on an estimate of the cost (total weight) still to go to the goal node. Specifically, A* selects the path that minimizes
    f(n)=g(n)+h(n)} f(n)=g(n)+h(n)
    where n is the last node on the path, g(n) is the cost of the path from the start node to n, and h(n) is a heuristic that estimates the cost of the cheapest path from n to the goal.
    The heuristic is problem-specific. For the algorithm to find the actual shortest path, the heuristic function must be admissible,
    meaning that it never overestimates the actual cost to get to the nearest goal node.
"""

from heapq import heappush, heappop
import math
import time
import random

class node:
    xPos = 0
    yPos = 0
    distance = 0  # total distance to node
    priority = 0  # priority = distance + remaining distance heuristic

    def __init__(self, xPos, yPos, distance, priority):
        self.xPos = xPos
        self.yPos = yPos
        self.distance = distance
        self.priority = priority

    def __que__(self, other):  # comparison priority queue
        return self.priority < other.priority

    def updatePriority(self, xDiv, yDiv):
        self.priority = self.distance + self.heuristic(xDiv, yDiv) * 10

    def nextMove(self, direct, d):
        if direct == 8 and d % 4 != 0:
            self.distance += 14
        else:
            self.distance += 10

    def heuristic(self, xDiv, yDiv):
        xd = xDiv - self.xPos
        yd = yDiv - self.yPos
        # Euclidian Distance
        d = math.sqrt(xd * xd + yd * yd)
        # Manhattan distance
        # d = abs(xd) + abs(yd)
        return (d)

def Astar(matrix, n, m, direct, dx, dy, xA, yA, xB, yB):
    visitedNode = []
    openNode = []
    directMat = []
    row = [0] * n
    for i in xrange(m):  # create 2d arrays
        visitedNode.append(list(row))
        openNode.append(list(row))
        directMat.append(list(row))

    nextNode = [[], []]             # priority queues of open (not-yet-tried) nodes
    index = 0                       # priority queue index
    root = node(xA, yA, 0, 0)       # start node and push into list of open nodes
    root.updatePriority(xB, yB)
    heappush(nextNode[index], root)
    openNode[yA][xA] = root.priority  # mark it on the open nodes map

    # A* search
    while len(nextNode[index]) > 0:     # get the current node with the highest priority
        topNode = nextNode[index][0]    # top node
        root = node(topNode.xPos, topNode.yPos, topNode.distance, topNode.priority)
        x = root.xPos
        y = root.yPos
        heappop(nextNode[index])  # remove the node from the open list
        openNode[y][x] = 0
        visitedNode[y][x] = 1       # mark it on the closed nodes matrix
        if x == xB and y == yB:     # quit searching when root.heuristic(xB, yB) == 0
            # generate the path from finish to start
            path = ''
            while not (x == xA and y == yA):
                z = directMat[y][x]
                se = str((z + direct / 2) % direct)
                path = se + path
                x += dx[z]
                y += dy[z]
            return path

        # generate moves (child nodes) in all possible directs
        for i in xrange(direct):
            xdx = x + dx[i]
            ydy = y + dy[i]
            if not (xdx < 0 or xdx > n - 1 or ydy < 0 or ydy > m - 1
                    or matrix[ydy][xdx] == 1 or visitedNode[ydy][xdx] == 1):
                # generate a child node
                childNode = node(xdx, ydy, root.distance, root.priority)
                childNode.nextMove(direct, i)
                childNode.updatePriority(xB, yB)
                # if it is not included in the open list of add
                if openNode[ydy][xdx] == 0:
                    openNode[ydy][xdx] = childNode.priority
                    heappush(nextNode[index], childNode)
                    # parent node direction
                    directMat[ydy][xdx] = (i + direct / 2) % direct
                elif openNode[ydy][xdx] > childNode.priority:
                    # update the priority
                    openNode[ydy][xdx] = childNode.priority
                    # update the parent direction
                    directMat[ydy][xdx] = (i + direct / 2) % direct
                    # we can replace the node by emptying one of the nextNode to the other one
                    # except that the node to be replaced will be ignored and the new node pushed in instead
                    while not (nextNode[index][0].xPos == xdx and nextNode[index][0].yPos == ydy):
                        heappush(nextNode[1 - index], nextNode[index][0])
                        heappop(nextNode[index])
                    heappop(nextNode[index])  # remove the target node
                    if len(nextNode[index]) > len(nextNode[1 - index]):
                        index = 1 - index
                    while len(nextNode[index]) > 0:
                        heappush(nextNode[1 - index], nextNode[index][0])
                        heappop(nextNode[index])
                    index = 1 - index
                    heappush(nextNode[index], childNode)  # add the better node instead
    return False  # if no route found

def main():
    direct = 8  # number of possible directions to move on the map
    if direct == 4:
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
    elif direct == 8:
        dx = [1, 1, 0, -1, -1, -1, 0, 1]
        dy = [0, 1, 1, 1, 0, -1, -1, -1]

    n = 30  # horizontal size of the map
    m = 30  # vertical size of the map
    matrix = []
    row = [0] * n
    for i in xrange(m):  # create empty map
        matrix.append(list(row))

    # fillout the map with a '+' pattern
    for x in xrange(n / 8, n * 7 / 8):
        matrix[m / 2][x] = 1
    for y in xrange(m / 8, m * 7 / 8):
        matrix[y][n / 2] = 1

    # randomly select start and finish locations from a list
    sf = []
    sf.append((0, 0, n - 1, m - 1))
    sf.append((0, m - 1, n - 1, 0))
    sf.append((n / 2 - 1, m / 2 - 1, n / 2 + 1, m / 2 + 1))
    sf.append((n / 2 - 1, m / 2 + 1, n / 2 + 1, m / 2 - 1))
    sf.append((n / 2 - 1, 0, n / 2 + 1, m - 1))
    sf.append((n / 2 + 1, m - 1, n / 2 - 1, 0))
    sf.append((0, m / 2 - 1, n - 1, m / 2 + 1))
    sf.append((n - 1, m / 2 + 1, 0, m / 2 - 1))
    (xA, yA, xB, yB) = random.choice(sf)

    print 'Size of map (X,Y): ', n, m
    print 'Start: ', xA, yA
    print 'Finish: ', xB, yB
    t = time.time()
    route = Astar(matrix, n, m, direct, dx, dy, xA, yA, xB, yB)
    print 'Time to generate the path (seconds): ', time.time() - t
    print 'Route:'
    print route

    # mark the route on the map
    if len(route) > 0:
        x = xA
        y = yA
        matrix[y][x] = 2
        for i in xrange(len(route)):
            j = int(route[i])
            x += dx[j]
            y += dy[j]
            matrix[y][x] = 3
        matrix[y][x] = 4

    # display the map with the route added
    print 'Map:'
    for y in xrange(m):
        for x in xrange(n):
            xy = matrix[y][x]
            if xy == 0:
                print '.',  # space
            elif xy == 1:
                print '#',  # obstacle
            elif xy == 2:
                print 'S',  # start
            elif xy == 3:
                print '*',  # route
            elif xy == 4:
                print 'F',  # finish
        print

if __name__ == "__main__":
    main()
