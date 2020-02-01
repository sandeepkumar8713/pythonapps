# https://www.geeksforgeeks.org/gold-mine-problem/
# Question : Given a gold mine of n*m dimensions. Each field in this mine contains a positive integer which is
# the amount of gold in tons. Initially the miner is at first column but can be at any row. He can move only
# (right->,right up /,right down\) that is from a given cell, the miner can move to the cell diagonally up
# towards the right or right or diagonally down towards the right. Find out maximum amount of gold he can collect.
#
# Question Type : ShouldSee
# Used : Maintain a table dp of size m * n. Loop over the each and every element of input matrix. but from right side
#        and column wise. col : n-1 to 0 and row : 0 to n
#           The idea is to choose max out of 3 option right, right up and right down
#           right = dp[row][col + 1]
#           right_up = dp[row - 1][col + 1]
#           right_down = dp[row + 1][col + 1]
#           calculate dp[row][col] = gold[row][col] + max(right, right_up, right_down)
#       Now from the first column of dp choose the max and return
# Complexity : O(m * n)


def getMaxGold(gold, m, n):
    dp = []
    for i in range(m):
        dp.append([0] * n)

    for col in range(n - 1, -1, -1):
        for row in range(m):

            # if take right
            if col == n - 1:
                right = 0
            else:
                right = dp[row][col + 1]

            # if take right up
            if row == 0 or col == n - 1:
                right_up = 0
            else:
                right_up = dp[row - 1][col + 1]

            # if take right down
            if row == m - 1 or col == n - 1:
                right_down = 0
            else:
                right_down = dp[row + 1][col + 1]

            # Max gold collected from take either of the above 3 paths
            dp[row][col] = gold[row][col] + max(right, right_up, right_down)

    res = dp[0][0]
    for i in range(1, m):
        res = max(res, dp[i][0])

    return res


if __name__ == "__main__":
    mat = [[1, 3, 1, 5],
           [2, 2, 4, 1],
           [5, 0, 2, 3],
           [0, 6, 1, 2]]

    m = len(mat)
    n = len(mat[0])

    print (getMaxGold(mat, m, n))
