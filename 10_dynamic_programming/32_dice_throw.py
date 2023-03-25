# https://www.geeksforgeeks.org/dice-throw-dp-30/
# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
# Question : https://www.geeksforgeeks.org/dice-throw-dp-30/
# Given n dice each with m faces, numbered from 1 to m, find the number of ways to get sum X.
# X is the summation of values on each face when all the dice are thrown.
#
# Explanation : Let the function to find X from n dice is: Sum(m, n, X)
# The function can be represented as:
# Sum(m, n, X) = Finding Sum (X - 1) from (n - 1) dice plus 1 from nth dice
#                + Finding Sum (X - 2) from (n - 1) dice plus 2 from nth dice
#                + Finding Sum (X - 3) from (n - 1) dice plus 3 from nth dice
#                   ...................................................
#                   ...................................................
#                   ...................................................
#               + Finding Sum (X - m) from (n - 1) dice plus m from nth dice
#
# So we can recursively write Sum(m, n, x) as following
# Sum(m, n, X) = Sum(m, n - 1, X - 1) +
#                Sum(m, n - 1, X - 2) +
#                .................... +
#                Sum(m, n - 1, X - m)
#
# Question Type : ShouldSee
# Used : Make a dp matrix : (dices + 1) * (targetSum + 1)
#        Now run 2 loops on dp, current value can be find by adding, combination of dices : targetSum - 1 and
#        combination of dices-1 and targetSum - 1. We have take care of overlapping combination if j - faces - 1 >= 0.
#        Logic : dp[0][0] = 1
#        for i in range(1, diceCount+1):
#           for j in range(1, targetSum+1):
#               dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
#               if j - faces - 1 >= 0: dp[i][j] -= dp[i - 1][j - faces - 1]
#        return dp[diceCount][targetSum]
# Complexity : O(dices * targetSum)


def findWays(faces, diceCount, targetSum):
    dp = []
    for i in range(diceCount+1):
        dp.append([0] * (targetSum + 1))

    dp[0][0] = 1

    for i in range(1, diceCount+1):
        for j in range(1, targetSum+1):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
            if j - faces - 1 >= 0:
                dp[i][j] -= dp[i - 1][j - faces - 1]
    return dp[diceCount][targetSum]


if __name__ == "__main__":
    print(findWays(4, 2, 1))
    print(findWays(2, 2, 3))
    print(findWays(6, 3, 8))
    print(findWays(4, 2, 5))
    print(findWays(4, 3, 5))
