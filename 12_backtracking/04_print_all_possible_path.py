# https://www.geeksforgeeks.org/backttracking-set-2-rat-in-a-maze/
# Question : Consider a rat placed at (0, 0) in a square matrix m[][] of order n and has to
# reach the destination at (n-1, n-1). Your task is to complete the function which returns
# a sorted array of strings denoting all the possible directions which the rat can take to
# reach the destination at (n-1, n-1). The directions in which the rat can move are 'U'(up),
# 'D'(down), 'L' (left), 'R' (right).
#
# Similar Problem : https://www.geeksforgeeks.org/boggle-find-possible-words-board-characters/
# Given a dictionary, a method to do lookup in dictionary and a M x N board where every cell has one
# character. Find all possible words that can be formed by a sequence of adjacent characters. Note that we can move to
# any of 8 adjacent characters, but a word should not have multiple instances of same cell.
#
# Solution : Here call findPath() multiple times considering all the, cell as starting point, and compare path with
# words in dictionary in each call.
#
# Question Type : Asked
# Used : Make a call to recursive function findPath(grid, visited, path, m, n) with visited
#        matrix of size n*n, path empty list and start point as 0,0.
#        If m and n reach to target, print path.
#        Loop over the 4 possible direction. Check if nextI and nextJ are safe.
#           (Within the matrix, path not blocked and not yet visited.) If the next cell is
#           safe, mark it as visited, append the direction the path list and make a recursive
#           call to findPath once again.
#           Out of 4 direction at least 1 findPath function should return True.
#           res = findPath(grid, visited, path, nextI, nextJ) or res. Now to backtrack, pop
#           the last element from path and mark the current cell unvisited.
#        return res
#        If findPath returns False to the driver function it means that no path is possible.
# Complexity : O(N!)

dI = [0, 0, -1, 1]
dJ = [-1, 1, 0, 0]
dLabel = ["L", "R", "U", "D"]


def isSafe(grid, visited, m, n):
    row = len(grid)
    col = len(grid[0])

    if 0 <= m < row and 0 <= n < col:
        if grid[m][n] != 0 and visited[m][n] == 0:
            return True

    return False


def findPath(grid, visited, path, m, n):
    row = len(grid)
    col = len(grid[0])

    if row - 1 == m and col - 1 == n:
        print(''.join(path))
        return True

    res = False
    for i in range(len(dI)):
        nextI = m + dI[i]
        nextJ = n + dJ[i]
        nextDir = dLabel[i]
        if isSafe(grid, visited, nextI, nextJ):
            visited[nextI][nextJ] = 1
            path.append(nextDir)
            res = findPath(grid, visited, path, nextI, nextJ) or res
            # backtrack
            path.pop()
            visited[nextI][nextJ] = 0

    return res


def printAllPossiblePath(grid):
    row = len(grid)
    col = len(grid[0])

    visited = []
    for i in range(row):
        visited.append([0] * col)

    if not findPath(grid, visited, [], 0, 0):
        print("path not found")


if __name__ == "__main__":
    grid = [[1, 0, 0, 0],
            [1, 1, 0, 1],
            [1, 1, 0, 0],
            [0, 1, 1, 1]]
    # grid = [[1, 1, 1, 1],
    #         [1, 1, 0, 1],
    #         [0, 1, 1, 1],
    #         [1, 1, 1, 1]]
    #
    # grid = [[1, 1, 1, 1],
    #         [1, 1, 1, 1],
    #         [1, 1, 1, 1],
    #         [1, 1, 1, 1]]
    printAllPossiblePath(grid)
