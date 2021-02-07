"""
    The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells,
    each of which is in one of two possible states, alive or dead, or "populated" or "unpopulated".
    Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent.
    At each step in time, the following transitions occur:
    Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
    Any live cell with two or three live neighbours lives on to the next generation.
    Any live cell with more than three live neighbours dies, as if by overpopulation.
    Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
"""

import copy
import sys
import time

glider = {(2, 2),
          (1, 2),
          (0, 2),
          (2, 1),
          (1, 0),}

pStartingBoard = copy.deepcopy(glider)

pSize = 10
pSleepTime = 0.1
pNIter = 100

def printBoard(board, size):
    height = width = size or 0
    for iH in xrange(height + 1):
        for iW in xrange(width + 1):
            sys.stdout.write(' > ' if (iH, iW) in board else ' _ ')
        print

def neighborCell(cell, size, distance = 1):
    # print cell, type(cell)
    (x, y) = cell
    res = []

    # Range for neighboring cell, starting from the upper left corner.
    cellRange = xrange(0 - distance, 1 + distance)

    for iX in cellRange:
        for iY in cellRange:
            if (iX == iY == 0) == False: # Not in the center cell.
                if (x + iX >= 0 and x + iX < size) and (y + iY >= 0 and y + iY < size): # Still in map
                    res += [(x + iX, y + iY)]
    return res

def liveOrDead(board, size):
    return set(cell for cell in board if cell[0] <= size and cell[1] <= size)

def updateBoard(board):
    newBoard = set()
    for cell in board:
        newCell = set(neighborCell(cell, pSize))

        if len(board & newCell) in [2, 3]:
            newBoard.add(cell)
        for iC in newCell:
            if len(board & set(neighborCell(iC, pSize))) is 3:
                newBoard.add(iC)
    return newBoard


def main():
    board = pStartingBoard
    areCellsAlive = False

    while True:
        printBoard(board, pSize)
        time.sleep(pSleepTime)
        board = liveOrDead(updateBoard(board), pSize)


if __name__ == '__main__':
    main()
