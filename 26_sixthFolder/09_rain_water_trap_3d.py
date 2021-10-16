# https://leetcode.com/problems/trapping-rain-water-ii/
# Question : Given an m x n integer matrix heightMap representing the height of each unit cell in
# a 2D elevation map, return the volume of water it can trap after raining.
#
# Example : Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
# Output: 4
#
# Question Type : Generic
# Used : Note that, a cell's water capacity depends on minimum height of all 4 adjacent cells.
#        Loop over the input matrix and insert cells on edge in the minHeap and mark them as visited.
#        Run BFS on the minHeap. Pop top element from minHeap and its height as currH.
#        Loop over its adjacent cells. Skip if already visited, else mark as visited.
#        If cells height is less than currH, save the diff in res and push cell in minHeap with currH.
#        Else push cell in minHeap with its actual height.
#        After the loop, return res.
#        Loop :
#        while heap:
#           curh, i, j = heapq.heappop(heap)
#           for k in range(4):
#               x = i + dx[k], y = j + dy[k]
#               if x < 0 or y < 0 or x >= n or y >= m:
#                   continue
#               if grid[x][y] == 0:
#                   grid[x][y] = 1
#                   if curh > heightMap[x][y]:
#                       re += curh - heightMap[x][y]
#                       heapq.heappush(heap, (curh, x, y))
#                   else:
#                       heapq.heappush(heap, (heightMap[x][y], x, y))
#        return re
# Complexity : O(m * n) where m and n are row and col of input matrix


import heapq


def trapRainWater(heightMap):
    if not heightMap:
        return 0

    n = len(heightMap)
    m = len(heightMap[0])

    heap = []
    grid = [[0] * m for _ in range(n)]
    re = 0

    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0 or i == n - 1 or j == m - 1:
                grid[i][j] = 1
                heapq.heappush(heap, (heightMap[i][j], i, j))

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while heap:
        curh, i, j = heapq.heappop(heap)
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            if x < 0 or y < 0 or x >= n or y >= m:
                continue
            if grid[x][y] == 0:
                grid[x][y] = 1
                if curh > heightMap[x][y]:
                    re += curh - heightMap[x][y]
                    heapq.heappush(heap, (curh, x, y))
                else:
                    heapq.heappush(heap, (heightMap[x][y], x, y))

    return re
