# https://leetcode.com/problems/stone-game-iii/
# Question : Alice and Bob continue their games with piles of stones. There are several stones
# arranged in a row, and each stone has an associated value which is an integer given in the
# array stoneValue. Alice and Bob take turns, with Alice starting first. On each player's turn,
# that player can take 1, 2 or 3 stones from the first remaining stones in the row. The score of
# each player is the sum of values of the stones taken. The score of each player is 0 initially.
# The objective of the game is to end with the highest score, and the winner is the player with
# the highest score and there could be a tie. The game continues until all the stones have been
# taken. Assume Alice and Bob play optimally. Return "Alice" if Alice will win, "Bob" if Bob
# will win or "Tie" if they end the game with the same score.
#
# Example : Input: values = [1,2,3,7]
# Output: "Bob"
# Explanation: Alice will always lose. Her best move will be to take three piles and the score
# become 6. Now the score of Bob is 7 and Bob wins.
#
# Question Type : ShouldSee
# Used : Make a dp dict, where key is index and value, is Alice's score from index to n.
#        Considering Alice makes first move, we do DFS from index 0.
#        During DFS, at each point Alice can choose 1, 2 or 3 stones fron start of array.
#        For the remaining array, call DFS again.
#        While doing DFS, keep updating dp dict.
#        After the DFS, return dp[0]
#        Alice's score should be +ve for her to win.
#        Logic :
#        def dfs(dp, stoneValue, index):
#        n = len(stoneValue)
#        if index >= n: return 0
#        if index in dp: return dp[index]
#        op1 = stoneValue[index] - dfs(dp, stoneValue, index + 1)
#        if index + 1 < n:
#           op2 = stoneValue[index] + stoneValue[index + 1] - dfs(dp, stoneValue, index + 2)
#        if index + 2 < n:
#           op3 = stoneValue[index] + stoneValue[index + 1] + stoneValue[index + 2] - dfs(dp, stoneValue, index + 3)
#        ans = max(ans, op1, op2, op3)
#        dp[index] = ans
#        return ans
#
#        dp = dict()
#        k = dfs(dp, stoneValue, 0)
#        if k > 0: return "Alice"
#        elif k < 0: return "Bob"
#        else: return "Tie"
# Complexity : O(n)

import sys


def dfs(dp, stoneValue, index):
    n = len(stoneValue)
    ans = -sys.maxsize
    op1 = op2 = op3 = ans

    if index >= n:
        return 0

    if index in dp:
        return dp[index]

    op1 = stoneValue[index] - dfs(dp, stoneValue, index + 1)
    if index + 1 < n:
        op2 = stoneValue[index] + stoneValue[index + 1] - dfs(dp, stoneValue, index + 2)
    if index + 2 < n:
        op3 = stoneValue[index] + stoneValue[index + 1] + stoneValue[index + 2] - dfs(dp, stoneValue, index + 3)

    ans = max(ans, op1, op2, op3)
    dp[index] = ans
    return ans


def stoneGameIII(stoneValue):
    dp = dict()
    k = dfs(dp, stoneValue, 0)

    if k > 0:
        return "Alice"
    elif k < 0:
        return "Bob"
    else:
        return "Tie"


if __name__ == "__main__":
    values = [1, 2, 3, 7]
    print(stoneGameIII(values))
