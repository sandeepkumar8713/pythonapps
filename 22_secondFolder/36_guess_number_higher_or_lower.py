# https://leetcode.com/problems/guess-number-higher-or-lower-ii/
# https://leetcode.com/problems/guess-number-higher-or-lower-ii/discuss/389172/Concise-DP-Python-code-with-clear-explanation
# Question : We are playing the Guess Game. The game is as follows:
# I pick a number from 1 to n. You have to guess which number I picked.
# Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.
# However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when you guess
# the number I picked.
#
# Example: n = 10, I pick 8.
# First round:  You guess 5, I tell you that it's higher. You pay $5.
# Second round: You guess 7, I tell you that it's higher. You pay $7.
# Third round:  You guess 9, I tell you that it's lower. You pay $9.
# Game over. 8 is the number I picked.
# You end up paying $5 + $7 + $9 = $21.
#
# Question Type : ShouldSee
# Used : We will do dp with this condition range(i,j) : return min(k + max(func(i, k-1), func(k+1, j))), for i<=k<j.
#        You choose a value k within the range.
#        2 scenarios are likely to happen: k is too high OR k is too low
#        To find the worse case scenario, find the max return value between these 2 scenarios
#        Then, find the best case scenario out of all your choices of k, and hence the min.
#        Note take we will be filling only upper part of matrix.
#        Logic :
#        for i in range(n + 1):
#           col = [0] * (n + 1)
#           dp.append(col)
#        for i in range(1, n + 1):
#           for j in range(1, n - i + 1):
#               res = sys.maxint
#               start = j
#               end = j + i
#               for k in range(start, end):
#                   res = min(res, k + max(dp[start][k - 1], dp[k + 1][end]))
#               dp[start][end] = res
#        return dp[1][n]
# Complexity : O(n^3)

import sys


def getMoneyAmount(n):
    dp = []

    # initialising 2-d DP-arr
    for i in range(n + 1):
        col = [0] * (n + 1)
        dp.append(col)

    # diagonally filling up DP-arr
    for i in range(1, n + 1):
        for j in range(1, n - i + 1):
            res = sys.maxsize
            start = j
            end = j + i
            for k in range(start, end):
                res = min(res, k + max(dp[start][k - 1], dp[k + 1][end]))
            dp[start][end] = res

    return dp[1][n]


if __name__ == "__main__":
    n = 10
    print(getMoneyAmount(n))
