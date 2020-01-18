# https://www.geeksforgeeks.org/find-length-of-the-longest-consecutive-path-in-a-character-matrix/
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
# Question : Given a matrix of characters. Find length of the longest path from a given character, such that
# all characters in the path are consecutive to each other, i.e., every character in path is next to previous
# in alphabetical order. It is allowed to move in all 8 directions from a cell.
# Given an integer matrix, find the length of the longest increasing path.
# From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or
# move outside of the boundary (i.e. wrap-around is not allowed).
#
# Used : Do Depth First Search (DFS) from each cell to find all consecutive paths. While doing DFS, we may encounter
#        many sub problems again and again. So we use dynamic programming to store results of sub problems.
#        maxLen = 0
#        for i in range(row):
#           for j in range(col):
#             if dp[i][j] == -1:
#                 thisCell = inpMat[i][j], ans = 0
#                 for k in range(8):
#                     ans = max(ans, 1 + getLenUtil(inpMat, dp, i + x[k], j + y[k], thisCell))
#                 dp[i][j] = ans
#             if maxLen < dp[i][j]: maxLen = dp[i][j]
# Complexity : O(n*m)


x = [0, 1, 1, -1, 1, 0, -1, -1]
y = [1, 0, 1, 1, -1, -1, 0, -1]

#x = [0, 1, 0, -1]
#y = [1, 0, -1, 0]

def isvalid(i, j, row, col):
    if i < 0 or j < 0 or i >= row or j >= col:
        return False
    return True


def isadjacent(prev, curr):
    if (ord(curr) - ord(prev)) == 1:
        return True
    return False


def isMore(prev, curr):
    if (ord(curr) - ord(prev)) > 0:
        return True
    return False


def getLenUtil(mat, dp, i, j, prev):
    row = len(mat)
    col = len(mat[0])
    if isvalid(i, j, row, col) is False or isadjacent(prev, mat[i][j]) is False:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    ans = 0  # DFS
    for k in range(len(x)):
        ans = max(ans, 1 + getLenUtil(mat, dp, i + x[k], j + y[k], mat[i][j]))

    dp[i][j] = ans
    return dp[i][j]


def getLen(inpMat):
    row = len(inpMat)
    col = len(inpMat[0])

    dp = []
    for i in range(row):
        dp.append([-1] * col)

    maxLen = 0
    for i in range(row):
        for j in range(col):
            if dp[i][j] == -1:
                thisCell = inpMat[i][j]
                ans = 0
                for k in range(len(x)):
                    ans = max(ans, 1 + getLenUtil(inpMat, dp, i + x[k], j + y[k], thisCell))
                dp[i][j] = ans
            if maxLen < dp[i][j]:
                maxLen = dp[i][j]

    return maxLen


if __name__ == "__main__":
    inpMat = ["ACD", "HBA", "IGF"]
    print getLen(inpMat)

    inpMat = ["ABE", "CFG", "BDH", "ABC"]
    print getLen(inpMat)

    inpMat = [['9', '9', '4'],
              ['6', '6', '8'],
              ['2', '1', '1']]
    print getLen(inpMat)
