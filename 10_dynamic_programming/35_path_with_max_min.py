# https://leetcode.com/discuss/interview-question/383669/
# Similar : https://leetcode.com/problems/path-with-minimum-effort/
# Similar : 27_seventhFolder/02_swim_in_rising_water.py
# Similar : https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/
# Question : Given a matrix with r rows and c columns, find the maximum score of a path starting at [0, 0]
# and ending at [r-1, c-1]. The score of a path is the minimum value in that path. For example, the score of
# the path 8 → 4 → 5 → 9 is 4. Don’t include the first or final entry. You can only move either down or right
# at any point in time.
#
# Question Type : ShouldSee, SimilarAdded
# Used : Make a 2D dp matrix of size m*n. Initialize them as 0.
#        Set second row and col of dp, equal to inpMat as we are not support to consider entry point.
#        Run the 2 loops over dp while updating its value from left and up value with following condition.
# Logic: dp[i][j] = max( min(a[i][j], dp[i-1][j]), min(a[i][j], dp[i][j+1]))
#        maxScore2D(inpMat):
#        dp[0][0] = sys.maxsize
#        for i in range(1, m):
#           dp[i][0] = min(dp[i - 1][0], inpMat[i][0])
#        for j in range(1, n):
#           dp[0][j] = min(dp[0][j-1], inpMat[0][j])
#        for i in range(1, m):
#           for j in range(1, n):
#               if i == m - 1 or j == n - 1:
#                   dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
#               else:
#                   score1 = min(dp[i][j - 1], inpMat[i][j])
#                   score2 = min(dp[i - 1][j], inpMat[i][j])
#                   dp[i][j] = max(score1, score2)
#        return dp[m-1][n-1]
# Complexity : O(m * n)

import sys


def maxScore2D(inpMat):
    m = len(inpMat)
    n = len(inpMat[0])

    dp = []
    for i in range(m):
        dp.append([0] * n)

    # first entry is not considered
    dp[0][0] = sys.maxsize
    for i in range(1, m):
        dp[i][0] = min(dp[i - 1][0], inpMat[i][0])  # left

    for j in range(1, n):
        dp[0][j] = min(dp[0][j-1], inpMat[0][j])  # up

    for i in range(1, m):
        for j in range(1, n):
            if i == m - 1 or j == n - 1:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) # last entry is not considered
            else:
                score1 = min(dp[i][j - 1], inpMat[i][j])   # left
                score2 = min(dp[i - 1][j], inpMat[i][j])   # up
                dp[i][j] = max(score1, score2)

    return dp[m-1][n-1]


if __name__ == "__main__":
    inpMat = [[7, 10, 6],
              [8, 5, 11],
              [3, 4, 9]]
    print(maxScore2D(inpMat))

    inpMat = [[1, 2, 3],
              [4, 5, 1]]
    print(maxScore2D(inpMat))
