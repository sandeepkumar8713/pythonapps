# https://www.geeksforgeeks.org/find-sum-of-all-elements-in-a-matrix-except-the-elements-in-given-row-andor-column-2/
# Question : Given a 2D matrix and a set of cell indexes e.g., an array of (i, j) where i indicates row and j column.
# For every given cell index (i, j), find sums of all matrix elements except the elements present in i'th row
# and/or j'th column.
#
# mat[][]  = { {1, 1, 2}
#              {3, 4, 6}
#              {5, 3, 2} }
# Array of Cell Indexes: {(0, 0), (1, 1), (0, 1)}
# Output:  15, 10, 16
#
# Question Type : Easy
# Used : Calculate sum of matrix, call it sum.
#        Calculate sum of individual rows and columns. (row[] and col[])
#        Loop over each element of input matrix : do this
#            colSum[j] += mat[i][j]
#            rowSum[i] += mat[i][j]
#        For a cell index (i, j), the desired sum will be
#        "sum - row[i] - col[j] + mat[i][j]"
# Complexity : O(m * n)


def printSums(mat, cells):
    totalSum = 0
    rowSum = [0] * len(mat)
    colSum = [0] * len(mat[0])

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            totalSum += mat[i][j]
            colSum[j] += mat[i][j]
            rowSum[i] += mat[i][j]

    for cell in cells:
        res = totalSum - rowSum[cell[0]] - colSum[cell[1]] + mat[cell[0]][cell[1]]
        print(res)


if __name__ == "__main__":
    mat = [[1, 1, 2],
           [3, 4, 6],
           [5, 3, 2]]
    cells = [[0, 0], [1, 1], [0, 1]]
    printSums(mat, cells)
