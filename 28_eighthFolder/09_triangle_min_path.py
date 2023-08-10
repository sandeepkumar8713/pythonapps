# https://leetcode.com/problems/triangle/
# Question : Given a triangle array, return the minimum path sum from top to bottom.
# For each step, you may move to an adjacent number of the row below. More formally,
# if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
#
# Question Type : Easy
# Used : Make a 2d Array of DP. We use DP with sub problem.
#        We should do bottom up approach.
# Logic: for i in range(m - 1, -1, -1):
#           for j in range(i + 1):
#               if i + 1 < m:
#                   dp[i][j] = triangle[i][j] + min(dp[i + 1][j], dp[i + 1][j + 1])
#               else:
#                   dp[i][j] = triangle[i][j]
#        return dp[0][0]
# Complexity : O(m*n)


def get_min_path(triangle):
    m = len(triangle)
    n = len(triangle[-1])
    dp = [[0] * n for _ in range(m)]
    for i in range(m - 1, -1, -1):
        for j in range(i + 1):
            if i + 1 < m:
                dp[i][j] = triangle[i][j] + min(dp[i + 1][j], dp[i + 1][j + 1])
            else:
                dp[i][j] = triangle[i][j]

    return dp[0][0]


if __name__ == "__main__":
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    print(get_min_path(triangle))

    triangle = [[-10]]
    print(get_min_path(triangle))
