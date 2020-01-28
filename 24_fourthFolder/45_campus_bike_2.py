# https://algorithm-notes-allinone.blogspot.com/2019/09/leetcode-1066-campus-bikes-ii.html
# Question : campus represented as a 2D grid, there are N workers and M bikes, with N <= M. Each worker and bike
# is a 2D coordinate on this grid. We assign one unique bike to each worker so that the sum of the Manhattan distances
# between each worker and their assigned bike is minimized. The Manhattan distance between two points p1 and p2
# is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|. Return the minimum possible sum of Manhattan distances
# between each worker and their assigned bike.
# 0 <= workers[i][0], workers[i][1], bikes[i][0], bikes[i][1] < 1000
# All worker and bike locations are distinct.
# 1 <= workers.length <= bikes.length <= 10
#
# Question Type : Generic
# Used : The naive method is that we try all the possible combinations using backtracking, but apparently we
#        re-calculate a lot of sub-states. In order to better see this, let us consider two cases. One is that we
#        let worker 1 choose bike 1, and worker 2 pick bike 2, then the rest workers choose the rest bikes
#        (sub-state 1). The other case is that, worker 1 chooses bike 2, and worker 2 chooses bike 1, then the rest
#        workers choose the rest bikes (sub-state 2). Apparently, sub-state 1 is the same as sub-state 2, so we just
#        need to calculate it once, and then re-use the result directly if need it again. To this question, bit mapping
#        is a naturally choice to label the state. 0 represents un-used and 1 represents used. (The very small values
#        of the number of both workers and bikes are good indicators to this.) Since both the number of the workers
#        and bikes are no larger than 10, an integer (32 bits) should be enough to record it. Thus, we can use two
#        integers to memorize the combination conditions between workers and bikes. In the following code, integer
#        workersState is for workers, and integer bikesState for bikes.
#        Logic : def dfs(i, workers, workersState, bikes, bikesState, dp):
#        if i == len(workers): return 0
#        if dp[workersState][bikesState] != -1: return dp[workersState][bikesState]
#        minDis = sys.maxint
#        for j in range(len(bikes)):            # try all the bikes
#           if (bikesState >> j) & 1: continue  # if the bike is used;
#           oneDis = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
#           oneDis += dfs(i + 1, workers, workersState | (1 << i), bikes, bikesState | (1 << j), dp)
#           minDis = min(minDis, oneDis)
#        dp[workersState][bikesState] = minDis
#        return dp[workersState][bikesState]
#        Calls as :  dfs(0, workers, 0, bikes, 0, dp) where dp size is 2^m and 2^m
# Complexity : O(n * m * 2^n * 2^m)

import sys


def minManhattanDist(workers, bikes):
    m = len(workers)
    n = len(bikes)
    dp = []
    for i in range(1 << m):
        dp.append([-1] * (1 << n))
    workersState = 0
    bikesState = 0
    return dfs(0, workers, workersState, bikes, bikesState, dp)


def dfs(i, workers, workersState, bikes, bikesState, dp):
    if i == len(workers):
        return 0

    if dp[workersState][bikesState] != -1:
        return dp[workersState][bikesState]

    minDis = sys.maxsize
    for j in range(len(bikes)):     # try all the bikes
        if (bikesState >> j) & 1:   # if the bike is used;
            continue
        oneDis = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
        # We have assigned bike j to worker i, now see how remaining will be assigned
        oneDis += dfs(i + 1, workers, workersState | (1 << i), bikes, bikesState | (1 << j), dp)
        minDis = min(minDis, oneDis)

    dp[workersState][bikesState] = minDis
    return dp[workersState][bikesState]


if __name__ == "__main__":
    workers = [[0, 0], [2, 1]]
    bikes = [[1, 2], [3, 3]]
    print(minManhattanDist(workers, bikes))

    workers = [[0, 0], [1, 1], [2, 0]]
    bikes = [[1, 0], [2, 2], [2, 1]]
    print(minManhattanDist(workers, bikes))
