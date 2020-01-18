# https://tenderleo.gitbooks.io/leetcode-solutions-/GoogleHard/317.html
# Question : You want to build a house on an empty land which reaches all buildings in the shortest amount of
# distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:
# Each 0 marks an empty land which you can pass by freely.
# Each 1 marks a building which you cannot pass through.
# Each 2 marks an obstacle which you cannot pass through.
# If it is not possible to build such house according to the above rules, return -1.
#
# https://leetcode.com/discuss/interview-experience/389969/Google-or-L3-or-Seattle-or-Sep-2019-No-Offer
# Follow-ups: one was how would you scale it for parallel processing, my answers were, we can fire BFS in parallel
# but as each thread would try to update the distGrid, they run in to contention, so probably we need these many grids
# & then we can unify them later, another followup, that's costly in space, after some thinking I realised we don't need
# N copies of the distGrid, but all threads can share the same grid, but they would have contention on update a
# particular cell of the gird & one thread would have to wait. Several other followups on tests cases, general
# questions on google.
#
# Example : given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2):
# 1 - 0 - 2 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0
# The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal.
# So return 7.
#
# Used : Do BFS from each building. While doing so, if we find an empty space (x,y), update these two:
#        distMat[x][y] : distance sum of all building from x,y
#        reachableBuildingCount[x][y] : how many buildings can be reached from x,y
#        After BFS, loop over the inpMat again, if empty space is found, check if all the buildings can be reached from
#        it. If yes, get sum dist for all the buildings and update min.
#        Logic : def bfs(inpMat, distMat, reachableBuildingCount, x, y):
#        dist = 0
#        while len(queue) != 0:
#           dist += 1, size = len(queue)
#           for i in range(size):
#               top = queue.pop(0)
#               for j in range(4):
#                   nextX = top.x + neighbor[j][0], nextY = top.y + neighbor[j][1]
#                   if 0 <= nextX < row and 0 <= nextY < col:
#                       if inpMat[nextX][nextY] == 0 and not visited[nextX][nextY]:
#                           visited[nextX][nextY] = True
#                           distMat[nextX][nextY] += dist
#                           reachableBuildingCount[nextX][nextY] += 1
#                           queue.append(Cell(nextX, nextY))
#        def shortestDist(inpMat):
#        for i in range(row):
#           for j in range(col):
#               if inpMat[i][j] == 0 and distMat[i][j] != 0 and reachableBuildingCount[i][j] == buildingCount:
#                   if minDist > distMat[i][j]: minDist = distMat[i][j], emptySpace = [i, j]
# Complexity : O(n * m * k) where k is number of buildings, n & m are row and col of input matrix.


import sys


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def bfs(inpMat, distMat, reachableBuildingCount, x, y):
    row = len(inpMat)
    col = len(inpMat[0])
    neighbor = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    visited = []
    for i in range(row):
        visited.append([False] * col)
    queue = []
    queue.append(Cell(x, y))

    dist = 0
    while len(queue) != 0:
        dist += 1
        size = len(queue)
        for i in range(size):
            top = queue.pop(0)
            for j in range(4):
                nextX = top.x + neighbor[j][0]
                nextY = top.y + neighbor[j][1]
                if 0 <= nextX < row and 0 <= nextY < col:
                    if inpMat[nextX][nextY] == 0 and not visited[nextX][nextY]:  # We reached a empty space
                        visited[nextX][nextY] = True
                        distMat[nextX][nextY] += dist
                        reachableBuildingCount[nextX][nextY] += 1
                        queue.append(Cell(nextX, nextY))


def shortestDistance(inpMat):
    row = len(inpMat)
    col = len(inpMat[0])

    distMat = []
    for i in range(row):
        distMat.append([0] * col)

    # distance sum of all building from x,y : distMat[x][y]
    # how many buildings can be reached from x,y : reachableBuildingCount[x][y]

    reachableBuildingCount = []
    for i in range(row):
        reachableBuildingCount.append([0] * col)

    buildingCount = 0
    for i in range(row):
        for j in range(col):
            if inpMat[i][j] == 1:
                buildingCount += 1
                bfs(inpMat, distMat, reachableBuildingCount, i, j)

    minDist = sys.maxint
    emptySpace = []
    for i in range(row):
        for j in range(col):
            if inpMat[i][j] == 0 and distMat[i][j] != 0 and reachableBuildingCount[i][j] == buildingCount:
                if minDist > distMat[i][j]:
                    minDist = distMat[i][j]
                    emptySpace = [i, j]

    if minDist is sys.maxint:
        return -1, emptySpace

    return minDist, emptySpace


if __name__ == "__main__":
    inpMat = [[1, 0, 2, 0, 1],
              [0, 0, 0, 0, 0],
              [0, 0, 1, 0, 0]]
    print shortestDistance(inpMat)
