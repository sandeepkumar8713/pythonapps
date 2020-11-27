# https://www.geeksforgeeks.org/optimal-strategy-for-a-game-dp-31/
# Question : Consider a row of n coins of values v1 ... vn, where n is even. We play a game against an
# opponent by alternating turns. In each turn, a player selects either the first or last coin from the row,
# removes it from the row permanently and receives the value of the coin. Determine the maximum possible
# amount of money we can definitely win if we move first.
#
# Input : 8, 15, 3, 7
# User chooses 8.
# Opponent chooses 15.
# User chooses 7.
# Opponent chooses 3.
# Total value collected by user is 15(8 + 7)
#
# Question Type : ShouldSee
# Used : We have to make a memory table count : dp n * n. Mark all as 0.
#        Run a loop from k: 0 to n-1
#           Run a loop from j: k to n-1, i: 0 to n-j-1 (Here we are increasing the array size.)
#               End pointers here are i and j. User can choose either i or j. If he choose i, opponent
#               while be left with i+1 to j to choose from. So opponent can choose either i+1 or j.
#               So user will be left with x or y.
#               x = dp[i + 2][j] if i+2 <= j else 0
#               y = dp[i + 1][j - 1] if i + 1 <= j - 1 else 0
#               z = dp[i][j - 2] if i <= j - 2 else 0
#               If user choose j, the is left with y or z.
#               So the current value should be:
#               dp[i][j] = max(arr[i] + min(x, y), arr[j] + min(y, z))
#        return dp[0][n-1]
#        optimalStrategyOfGame(arr):
#        n = len(arr), dp = []
#        for i in range(n):
#           dp.append([0] * n)
#        for k in range(n):
#           i = 0, j = k
#           while j < n:
#               x = dp[i + 2][j] if i+2 <= j else 0
#               y = dp[i + 1][j - 1] if i + 1 <= j - 1 else 0
#               z = dp[i][j - 2] if i <= j - 2 else 0
#               dp[i][j] = max(arr[i] + min(x, y), arr[j] + min(y, z))
#               i += 1, j += 1
#        return dp[0][n-1]
# Complexity : O(n * n)


def optimalStrategyOfGame(arr):
    n = len(arr)

    dp = []
    for i in range(n):
        dp.append([0] * n)

    # Note that the table is filled in diagonal fashion
    for k in range(n):
        i = 0
        j = k
        while j < n:
            x = dp[i + 2][j] if i+2 <= j else 0
            y = dp[i + 1][j - 1] if i + 1 <= j - 1 else 0
            z = dp[i][j - 2] if i <= j - 2 else 0
            # If user choose i, then he might get left with x or y
            # If user choose j, then he might get left with y or z
            # The opponent intends to choose the coin which leaves the user with minimum value.

            dp[i][j] = max(arr[i] + min(x, y), arr[j] + min(y, z))
            i += 1
            j += 1

    return dp[0][n-1]


if __name__ == "__main__":
    arr = [8, 15, 3, 7]
    print("Maximum value:", optimalStrategyOfGame(arr))
