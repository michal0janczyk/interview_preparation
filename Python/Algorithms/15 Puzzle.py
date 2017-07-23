"""
    The 15-puzzle (also called Gem Puzzle, Boss Puzzle, Game of Fifteen, Mystic Square and many others)
    is a sliding puzzle that consists of a frame of numbered square tiles in random order with one tile missing.
    The puzzle also exists in other sizes, particularly the smaller 8-puzzle.
    If the size is 3×3 tiles, the puzzle is called the 8-puzzle or 9-puzzle, and if 4×4 tiles, the puzzle is called the 15-puzzle or 16-puzzle named, respectively,
    for the number of tiles and the number of spaces. The object of the puzzle is to place the tiles in order by making sliding moves that use the empty space.
    The n-puzzle is a classical problem for modelling algorithms involving heuristics.
    Commonly used heuristics for this problem include counting the number of misplaced tiles and finding the sum of the taxicab distances between each block and
    its position in the goal configuration. Note that both are admissible, i.e. they never overestimate the number of moves left,
    which ensures optimality for certain search algorithms such as A*.
"""

from heapq import heappush, heappop
import math
import time
import random
import pprint
pp = pprint.PrettyPrinter(indent=4)

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
            return pp.pprint(path)

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

def moves(mat):
    # Returns a list of all possible moves
    output = []

    m = eval(mat)
    i = 0
    while 0 not in m[i]: i += 1
    j = m[i].index(0);  # blank space (zero)

    if i > 0:
        m[i][j], m[i - 1][j] = m[i - 1][j], m[i][j]  # move up
        output.append(str(m))
        m[i][j], m[i - 1][j] = m[i - 1][j], m[i][j]

    if i < 3:
        m[i][j], m[i + 1][j] = m[i + 1][j], m[i][j]  # move down
        output.append(str(m))
        m[i][j], m[i + 1][j] = m[i + 1][j], m[i][j]

    if j > 0:
        m[i][j], m[i][j - 1] = m[i][j - 1], m[i][j]  # move left
        output.append(str(m))
        m[i][j], m[i][j - 1] = m[i][j - 1], m[i][j]

    if j < 3:
        m[i][j], m[i][j + 1] = m[i][j + 1], m[i][j]  # move right
        output.append(str(m))
        m[i][j], m[i][j + 1] = m[i][j + 1], m[i][j]

    return output

def heuristic(puzzle):
    # Manhattan distance
    distance = 0
    m = eval(puzzle)
    for i in range(4):
        for j in range(4):
            if m[i][j] == 0:
                continue
            distance += abs(i - (m[i][j] / 4)) + abs(j - (m[i][j] % 4))

    return distance

def main():

    puzzle = str([[1, 2, 6, 3], [4, 9, 5, 7], [8, 13, 11, 15], [12, 14, 0, 10]])
    end = str([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
    Astar(puzzle, end)

if __name__ == '__main__':
    main()
