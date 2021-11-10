# Question : Given a two dimensional grid, each cell of which contains integer cost which
# represents a cost to traverse through that cell, we need to find a path from top left cell
# to bottom right cell by which total cost incurred is minimum.
#
# Question Type : Generic, SimilarAdded
# Used : Make a class of cell with attributes: i and j. Make a dist matrix with all values set
#        as maxInt.
#        Make a queue and insert the source cell in it.
#        Initialize the source cell in dist with value in grid.
#        Now loop while the queue is not empty. Pop first cell from queue. Loop over the
#           possible directions it can go to. Check if it is safe to go to next cell.
#           Now check if sum of dist[currentCell] and grid[nextCell] is less than
#           dist[nextCell]. If true then if nextCell is already there in queue,
#           then remove its previous entry, as we got lesser cost to reach this cell.
#           Now append this cell in queue and update the dist[nextCell] with lower cost.
#        return dist[destination]
# Complexity : O(n^2)

import sys


class Cell:
    def __init__(self, i, j):
        self.i = i
        self.j = j


def isSafe(mat, i, j):
    row = len(mat)
    col = len(mat[0])
    if 0 <= i < row and 0 <= j < col:
            return True
    return False


def removePrevious(queue, i, j):
    indexToBeDeleted = -1
    index = 0
    for cell in queue:
        if cell.i is i and cell.j is j:
            indexToBeDeleted = index
        index += 1

    if indexToBeDeleted is not -1:
        queue.pop(indexToBeDeleted)


def shortestPath(grid, src, dest):
    row = len(grid)
    col = len(grid[0])

    # Possible direction left, right, up, down
    dJ = [-1, 1, 0, 0]
    dI = [0, 0, -1, 1]

    dist = []
    for i in range(row):
        defaultCol = [sys.maxsize] * col
        dist.append(defaultCol)
    queue = []
    queue.append(Cell(src["i"], src["j"]))
    dist[src["i"]][src["j"]] = grid[src["i"]][src["j"]]

    while len(queue) is not 0:
        cell = queue.pop(0)

        for i in range(len(dI)):
            nextI = cell.i + dI[i]
            nextJ = cell.j + dJ[i]

            if isSafe(grid, nextI, nextJ):
                if dist[nextI][nextJ] > dist[cell.i][cell.j] + grid[nextI][nextJ]:
                    # If cell is already there in set, then remove its previous entry, as we got lesser cost
                    if dist[nextI][nextJ] is not sys.maxsize:
                        removePrevious(queue, nextI, nextJ)

                    dist[nextI][nextJ] = dist[cell.i][cell.j] + grid[nextI][nextJ]
                    queue.append(Cell(nextI, nextJ))

    return dist[dest["i"]][dest["j"]]


if __name__ == "__main__":
    grid = [[31, 100, 65, 12, 18],
            [10, 13, 47, 157, 6],
            [100, 113, 174, 11, 33],
            [88, 124, 41, 20, 140],
            [99, 32, 111, 41, 20]]
    src = {"i": 0, "j": 0}
    dest = {"i": 4, "j": 4}

    # src = {"i": 4, "j": 3}
    # dest = {"i": 4, "j": 4}

    # src = {"i": 0, "j": 0}
    # dest = {"i": 0, "j": 0}
    print(shortestPath(grid, src, dest))
