# Question : Given a n*n matrix where all numbers are distinct, find the maximum length path (starting from any
# cell) such that all cells along the path are in increasing order with a difference of 1. We can move in 4
# directions from a given cell (i, j).
#
# Input:  mat[][] = {{1, 2, 9}
#                    {5, 3, 8}
#                    {4, 6, 7}}
# Output: 4
# The longest path is 6-7-8-9.
#
# Question Type : Generic, SimilarAdded
# Used : Here we are maintaining a memory table. table : dp row * col . Initialize all as -1. (-1 not yet computed)
#        Here the idea is to compute max possible path for each cell and return the largest value.
#        Set result as 1. Loop over each of the elements in the array and call(if not yet calculated) recursive function
#           findLongestFromACell which would set maxpathlength for this cell in dp[i][j]. See if it is more than result
#           and update accordingly.
#        return result
#
#        findLongestFromACell function: It takes current cells pos, mat and dp as input. Make a array of all possible
#           direction and loop over them. If the next position is within matrix and next cell's value is 1 higher than
#           current then dp[i][j] = 1 + findLongestFromACell(nextI, nextJ, mat, dp).
#        If the we can't move in either of 4 direction the set dp[i][j] = 1
#        return dp[i][j]
# Complexity : O(n^2)


def findLongestFromACell(i,j,mat,dp):
    row = len(mat)
    col = len(mat[0])

    atleastOneGreaterFound = False

    dI = [0, 0, -1, 1]
    dJ = [-1, 1, 0, 0]

    for k in range(len(dI)):
        nextI = i + dI[k]
        nextJ = j + dJ[k]

        if 0 <= nextI < row and 0 <= nextJ < col:
            if (mat[i][j] + 1) == mat[nextI][nextJ]:
                atleastOneGreaterFound = True
                dp[i][j] = 1 + findLongestFromACell(nextI, nextJ, mat, dp)

    if not atleastOneGreaterFound:
        dp[i][j] = 1

    return dp[i][j]


def finLongestOverAll(mat):
    result = 1

    row = len(mat)
    col = len(mat[0])

    dp = []   # -1 means not yet computed
    for i in range(row):
        dp.append([-1] * col)

    for i in range(row):
        for j in range(col):
            if dp[i][j] == -1:
                findLongestFromACell(i, j, mat, dp)
            result = max(result, dp[i][j])

    return result


if __name__ == "__main__":
    mat = [[1, 2, 9],
           [5, 3, 8],
           [4, 6, 7]]
    print("Longest path:", finLongestOverAll(mat))

