# https://www.geeksforgeeks.org/painters-partition-problem/
# https://www.geeksforgeeks.org/allocate-minimum-number-pages/
# Question : We have to paint n boards of length {A1, A2...An}. There are k painters available and each takes 1
# unit time to paint 1 unit of board. The problem is to find the minimum time to get
# this job done under the constraints that any painter will only paint continuous sections of boards, say
# board {2, 3, 4} or only board {1} or nothing but not board {2, 4, 5}.
#
# Used : Make a cumulative sum array, Make a dp array of size [k+1][n+1]. For each cell, try to separator from
#        p = i to j. Choose the minimum of maximum values (Remember this is our aim).
#        Steps :
#         for i in range(2, k+1):
#           for j in range(2, n+1):
#               minimum = sys.maxint
#               for p in range(1, j+1):
#                   minimum = min(minimum, max(dp[i - 1][p], subSum(p, j)))
#           dp[i][j] = minimum
#         return dp[k][n]
# Complexity : O(k* N^2)

import sys
cumulativeSum = []


def subSum(start, end):
    return cumulativeSum[end] - cumulativeSum[start]


def findMax(arr, k):
    global cumulativeSum
    n = len(arr)

    cumulativeSum = [0] * (n + 1)
    for i in range(n):
        cumulativeSum[i+1] = cumulativeSum[i] + arr[i]

    dp = []
    for i in range(k+1):
        dp.append([0] * (n + 1))

    # base casesCumulativeSum
    # k = 1
    for i in range(1, n+1):
        dp[1][i] = subSum(0, i)

    # n = 1
    for i in range(1, k+1):
        dp[i][1] = arr[0]

    # 2 to n boards
    for i in range(2, k+1):
        for j in range(2, n+1):
            minimum = sys.maxint
            # i-1 th separator before position arr[p=1..j]
            for p in range(1, j+1):
                minimum = min(minimum, max(dp[i - 1][p], subSum(p, j)))
            dp[i][j] = minimum

    return dp[k][n]


if __name__ == "__main__":
    arr = [10, 20, 60, 50, 30, 40]
    k = 3

    arr = [12, 34, 67, 90]
    k = 2

    arr = [1, 2, 4, 7, 3, 6, 9]
    k = 4

    print (findMax(arr, k))
