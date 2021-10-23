# https://massivealgorithms.blogspot.com/2017/04/leetcode-562-longest-line-of.html
# https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/
# Question :  Given a 01 matrix M, find the longest line of consecutive one in the matrix.
# The line could be horizontal, vertical, diagonal or anti-diagonal.
#
# Example: Input:
# [[0,1,1,0],
#  [0,1,1,0],
#  [0,0,0,1]]
# Output: 3
#
# Question Type : ShouldSee
# Used : We make dp (dict) where key (i,j,k) holds line length for cell i and j passing in k direction
#        k can be Horizontal, Diagonal, Vertical, Anti Diagonal.
#        Iterate over matrix, For cell check in 4 for direction.
#        If the cell has value 1, add the line length coming from all the 4 directions and
#        choose max out of it.
#        After the loop, when we reach the last cell of matrix, return maxLen.
#        Logic:
#        dirs = [(0, -1), (-1, -1), (-1, 0), (-1, 1)]
#        for i in range(m):
#           for j in range(n):
#               if inpMat[i][j] == 0: continue
#               for k in range(4):
#                   dp[(i, j, k)] = 1
#                   x = i + dirs[k][0]
#                   y = j + dirs[k][1]
#                   if 0 <= x < m and 0 <= y < m:
#                       if inpMat[x][y] == 1:
#                           dp[(i, j, k)] += dp[(x, y, k)]
#                           res = max(res, dp[(i, j, k)])
#        return res
# Complexity : O(m * n) where m and n are row and col of matrix


import sys

# Horizontal, Diagonal, Vertical, Anti Diagonal
dirs = [(0, -1), (-1, -1), (-1, 0), (-1, 1)]


def straightLine(inpMat):
    m = len(inpMat)
    n = len(inpMat[0])
    dp = dict()

    res = -sys.maxsize
    for i in range(m):
        for j in range(n):
            if inpMat[i][j] == 0:
                continue

            for k in range(4):
                dp[(i, j, k)] = 1

                x = i + dirs[k][0]
                y = j + dirs[k][1]

                if 0 <= x < m and 0 <= y < m:
                    if inpMat[x][y] == 1:
                        dp[(i, j, k)] += dp[(x, y, k)]
                        res = max(res, dp[(i, j, k)])

    return res


if __name__ == "__main__":
    inpMat = [[0, 1, 1, 0],
              [0, 1, 1, 0],
              [0, 0, 0, 1]]
    print(straightLine(inpMat))
