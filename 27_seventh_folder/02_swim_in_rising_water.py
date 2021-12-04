# https://leetcode.com/problems/swim-in-rising-water/
# Question : You are given an n x n integer matrix grid where each value grid[i][j] represents
# the elevation at that point (i, j). The rain starts to fall. At time t, the depth of the water
# everywhere is t. You can swim from a square to another 4-directionally adjacent square if
# and only if the elevation of both squares individually are at most t. You can swim infinite
# distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.
# Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start
# at the top left square (0, 0).
#
# Similar : 10_dynamic_programming/35_path_with_max_min.py
# Find max point in each path, that point is cost of that path in matrix.
#
# Question Type : Generic
# Used : We will use min heap to save all paths with cost as max value in path.
#        Keep looping over the min heap until it is empty.
#        Keep track of visited cells.
#        It is BFS with special condition that pop is done for min cost.
#        Return cost when target is reached.
#        Logic :
#        minHeap = [[grid[0][0], 0, 0]]
#        while minHeap:
#           h, i, j = heapq.heappop(minHeap)
#           if i == endIdx and j == endIdx:
#               return h
#           for d in directions:
#               ni, nj = i + d[0], j + d[1]
#               if ni < 0 or ni == length or nj < 0 or nj == length or (ni, nj) in visited:
#                   continue
#               visited.add((ni, nj))
#               heapq.heappush(minHeap, [max(h, grid[ni][nj]), ni, nj])
# Complexity : O(n log n) where n is number of cells

import heapq


def swimInWater(grid):
    visited = {(0, 0)}
    length = len(grid)
    endIdx = length - 1
    minHeap = [[grid[0][0], 0, 0]]
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    while minHeap:
        h, i, j = heapq.heappop(minHeap)
        if i == endIdx and j == endIdx:
            return h
        for d in directions:
            ni, nj = i + d[0], j + d[1]
            if ni < 0 or ni == length or nj < 0 or nj == length or (ni, nj) in visited:
                continue
            visited.add((ni, nj))
            heapq.heappush(minHeap, [max(h, grid[ni][nj]), ni, nj])


if __name__ == "__main__":
    grid = [[0, 2], [1, 3]]
    print(swimInWater(grid))

    grid = [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20],
            [10, 9, 8, 7, 6]]
    print(swimInWater(grid))
