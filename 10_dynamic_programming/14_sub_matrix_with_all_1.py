# https://www.geeksforgeeks.org/maximum-size-sub-matrix-with-all-1s-in-a-binary-matrix/
# https://leetcode.com/problems/maximal-square/
# https://leetcode.com/discuss/interview-question/416012/
# Question : Given a binary matrix, find out the maximum size square sub-matrix with all 1s.
# Similar question : Count the number of squares in the matrix of zeros and ones, which consist only of zeros.
#
# Used : The idea of the algorithm is to construct an auxiliary size matrix dp[][] in which each entry d[[i][j]
#        represents size of the square sub-matrix with all 1s including mat[i][j] where mat[i][j] is the rightmost
#        and bottommost entry in sub-matrix.
#        We have to make a memory table count : dp (m) * (n). Mark all as 0.
#        Set first row and col of dp same as inpMat(Single cell is also a square).
#        Loop over each of the elements in mat.
#           If mat[i][j] == 1: set dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
#           else set dp[i][j] = 0
#        Find the cell in dp which has max value and save its index.
#        Print mat for rows : [maxI - maxSize + 1: maxI + 1] cols : [maxJ - maxSize + 1: maxJ + 1]
#        Similar question : Square count. We will simply take sum of our dp array. Why sum? Because if at i,j
#        there is a matrix of size K x K then it should also include (K-1) x (K-1)
# Complexity : O(n*n)


def printMaxSubSquare(mat):
    row = len(M)
    col = len(M[0])

    dp = []
    for i in range(row):
        dp.append([0] * col)

    for j in range(col):
        dp[0][j] = mat[0][j]

    for i in range(row):
        dp[i][0] = mat[i][0]

    for i in range(1, row):
        for j in range(1, col):
            if mat[i][j] == 1:
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
            else:
                dp[i][j] = 0

    maxSize = dp[0][0]
    maxI = 0
    maxJ = 0
    for i in range(row):
        rowMax = max(dp[i])
        if maxSize < rowMax:
            maxSize = rowMax
            maxJ = dp[i].index(rowMax)
            maxI = i

    squareCount = 0
    for row in dp:
        squareCount += sum(row)
    print "squareCount :", squareCount
    print "Max square :"

    for thisRow in mat[maxI - maxSize + 1: maxI + 1]:
        print thisRow[maxJ - maxSize + 1: maxJ + 1]

    print ""


if __name__ == "__main__":
    M = [[0, 1, 1, 0, 1],
         [1, 1, 0, 1, 0],
         [0, 1, 1, 1, 0],
         [1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0]]
    printMaxSubSquare(M)

    M = [[1, 1, 1],
         [1, 1, 1],
         [1, 1, 0]]
    printMaxSubSquare(M)

    M = [[1, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
    printMaxSubSquare(M)

