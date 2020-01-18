# https://leetcode.com/discuss/interview-question/353827
# Question : Given a 2D grid of size r * c. 0 is walkable, and 1 is a wall. You can move up, down, left or right at
# a time. Now you are allowed to break at most 1 wall, what is the minimum steps to walk from the upper left corner
# (0, 0) to the lower right corner (r-1, c-1)? Follow-up:
# What if you can break k walls?
#
# Example : Input: k = 2
# [[0, 1, 0, 0, 0],
#  [0, 0, 0, 1, 0],
#  [0, 1, 1, 1, 1],
#  [0, 1, 1, 1, 1],
#  [1, 1, 1, 1, 0]]
# Output: 10
# Explanation: Change (2, 4) and (3, 4) to `0`.
# Route (0, 0) -> (1, 0) -> (1, 1) -> (1, 2) -> (0, 2) -> (0, 3) -> (0, 4) -> (1, 4) -> (2, 4) -> (3, 4) -> (4, 4)
#
# Used : Do normal bfs, whenever we hit a wall, break it. Keep the count to walls broken and push it along with distance
#        in queue. Skip the nodes, where wall broken count is more than limit. If we reach target return length.
#        Logic : def shortestPathBreakWalls(inpMat, K):
#        m, n = len(inpMat), len(inpMat[0])
#        offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#        pq = [(0, 0, (0, 0))]
#        seen = {(0, (0, 0))}
#        while pq:
#           length, wallBroke, (r, c) = heappop(pq)
#           for dr, dc in offsets:
#               nextR, nextC = r + dr, c + dc
#               if not (0 <= nextR < m and 0 <= nextC < n): continue
#               if (nextR, nextC) == (m - 1, n - 1): return length + 1
#               nextWallBroke = wallBroke + inpMat[nextR][nextC]
#               if nextWallBroke > K or (nextWallBroke, (nextR, nextC)) in seen:
#                   continue
#               seen.add((nextWallBroke, (nextR, nextC)))
#               heappush(pq, (length + 1, nextWallBroke, (nextR, nextC)))
#        return -1
# Complexity : O(n*m)

from heapq import heappush, heappop


def shortestPathBreakWalls(inpMat, K):
    m, n = len(inpMat), len(inpMat[0])
    offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    # elements in form of: (path length, wall breaks, (row, column))
    pq = [(0, 0, (0, 0))]
    # store visited states: (wall breaks, (row, column))
    seen = {(0, (0, 0))}

    while pq:
        # pick the current shortest path
        # pick one with fewest wall breaks, if there is a tie
        length, wallBroke, (r, c) = heappop(pq)
        for dr, dc in offsets:
            nextR, nextC = r + dr, c + dc
            # skip if out of bound
            if not (0 <= nextR < m and 0 <= nextC < n):
                continue

            # reach target
            if (nextR, nextC) == (m - 1, n - 1):
                return length + 1

            nextWallBroke = wallBroke + inpMat[nextR][nextC]
            # skip if exceed wall break limit or state has been visited
            if nextWallBroke > K or (nextWallBroke, (nextR, nextC)) in seen:
                continue

            seen.add((nextWallBroke, (nextR, nextC)))
            heappush(pq, (length + 1, nextWallBroke, (nextR, nextC)))

    return -1


if __name__ == "__main__":
    A = [[0, 1, 0, 0, 0],
         [0, 0, 0, 1, 0],
         [1, 1, 0, 1, 0],
         [1, 1, 1, 1, 0]]
    K = 1
    print(shortestPathBreakWalls(A, K), 7)

    A = [[0, 1, 1],
         [1, 1, 0],
         [1, 1, 0]]
    K = 1
    print(shortestPathBreakWalls(A, K), -1)

    A = [[0, 1, 0, 0, 0],
         [0, 0, 0, 1, 0],
         [0, 1, 1, 1, 1],
         [0, 1, 1, 1, 1],
         [1, 1, 1, 1, 0]]
    K = 2
    print(shortestPathBreakWalls(A, K), 10)
