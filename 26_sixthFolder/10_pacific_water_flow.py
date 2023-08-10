# https://leetcode.com/problems/pacific-atlantic-water-flow/
# Question : There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean.
# The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's
# right and bottom edges. The island is partitioned into a grid of square cells. You are given an m x n
# integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south,
# east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water
# can flow from any cell adjacent to an ocean into the ocean. Return a 2D list of grid coordinates result
# where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and
# Atlantic oceans.
#
# Example : Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
#
# Question Type : ShouldSee
# Used : We should run 2 bfs (i.e for atlantic and pacific)
#        Start bfs by pushing cells on edge in queue. During BFS, push the next cell in queue
#        only if its height higher than or equal to current cell's height.
#        While doing so keep track of cells visited in two separate matrix.
#        Our ans is intersection of these two visited matrix.
# Logic: def BFS(inputMat, m, n, queue, visited):
#        for i, j in queue: visited[i][j] = 1
#        while queue:
#           x, y = queue.pop()
#           for k in range(4):
#               i = x + dx[k], j = y + dy[k]
#               if 0 <= i < m and 0 <= j < n and visited[i][j] == 0:
#                   if inputMat[i][j] >= inputMat[x][y]:
#                       visited[i][j] = 1, queue.append([i, j])
#        def pacificAtlantic(heights):
#        atlanticQ = [[i, n - 1] for i in range(m)]  # right side
#        atlanticQ += [[m - 1, j] for j in range(n)]  # bottom side
#        BFS(heights, m, n, atlanticQ, atVis)
#        BFS(heights, m, n, pacificQ, pcVis)
#        return atVis intersection pcVis
# Complexity : O(m * n) where m and n are row and col of input matrix.

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def BFS(inputMat, m, n, queue, visited):
    for i, j in queue:
        visited[i][j] = 1

    while queue:
        x, y = queue.pop()
        for k in range(4):
            i = x + dx[k]
            j = y + dy[k]
            if 0 <= i < m and 0 <= j < n and visited[i][j] == 0:
                if inputMat[i][j] >= inputMat[x][y]:
                    visited[i][j] = 1
                    queue.append([i, j])


def pacificAtlantic(heights):
    # intersection of
    # 1)cells that flow into pacific
    # 2)cells that flow into atlantic

    m, n = len(heights), len(heights[0])
    atlanticQ = [[i, n - 1] for i in range(m)]  # right side
    atlanticQ += [[m - 1, j] for j in range(n)]  # bottom side

    pacificQ = [[0, j] for j in range(n)]  # left side
    pacificQ += [[i, 0] for i in range(m)]  # top side

    result = []

    # 0,1,2 = notVisited, visited
    atVis = [[0] * n for i in range(m)]
    pcVis = [[0] * n for i in range(m)]

    BFS(heights, m, n, atlanticQ, atVis)
    BFS(heights, m, n, pacificQ, pcVis)

    print ("Atlantic")
    for row in atVis:
        print (row)

    print("Pacific")
    for row in pcVis:
        print (row)

    for i in range(m):
        for j in range(n):
            if atVis[i][j] == pcVis[i][j] == 1:
                result.append([i, j])

    return result


if __name__ == "__main__":
    heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    print(pacificAtlantic(heights))
