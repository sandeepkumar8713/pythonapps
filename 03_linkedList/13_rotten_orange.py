# Question : Given a matrix of dimension m*n where each cell in the matrix can have values 0, 1 or 2 which has the
# following meaning:
# 0: Empty cell
# 1: Cells have fresh oranges
# 2: Cells have rotten oranges
# So we have to determine what is the minimum time required so that all the oranges become rotten. A rotten orange at
# index [i,j] can rot other fresh orange at indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1] (up, down, left and right). If
# it is impossible to rot every orange then simply return -1.
#
# Used : Push all the rotten oranges in the queue with time taken 0. Now loop through the queue and pop 1 element from
#        rear and check its surrounding if there are fresh oranges make them rotten and push them in queue while
#        incrementing the time by 1. Also keep track of maxTime taken so far.
#        Once the queue is empty, check if any fresh orange is left or not. If not left return maxTime else return -1
# Complexity : O(m*n)

possiblePaths = [[-1, 0], [1, 0], [0, -1], [0, 1]]


class Cell:
    def __init__(self, i, j, time):
        self.i = i
        self.j = j
        self.time = time


def rotTheMatrix(matrix):
    queue = []
    m = len(matrix)
    n = len(matrix[0])
    for i in range(0, m):
        for j in range(0, n):
            if matrix[i][j] == 2:
                c = Cell(i, j, 0)
                queue.append(c)

    maxTime = -9999

    while len(queue) > 0:
        frontCell = queue[0]
        del queue[0]

        if frontCell.time > maxTime:
            maxTime = frontCell.time

        for item in possiblePaths:
            nextI = frontCell.i + item[0]
            nextJ = frontCell.j + item[1]
            if 0 <= nextI < m and 0 <= nextJ < n:
                if matrix[nextI][nextJ] == 1:
                    matrix[nextI][nextJ] = 2
                    c = Cell(nextI, nextJ, frontCell.time + 1)
                    queue.append(c)

    for row in matrix:
        for item in row:
            if item == 1:
                return -1

    return maxTime


if __name__ == "__main__":
    matrix = [[2, 1, 0, 2, 1],
              [1, 0, 1, 2, 1],
              [1, 0, 0, 2, 1]]

    # matrix = [[2, 1, 0, 2, 1],
    #           [0, 0, 1, 2, 1],
    #           [1, 0, 0, 2, 1]]
    print rotTheMatrix(matrix)

