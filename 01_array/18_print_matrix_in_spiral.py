# Question : Given a 2D array, print it in spiral form.
#
# Used : while thisRow < m and thisCol < n:
#           print first row, thisRow += 1,
#           print last col, dec n,
#           print last row, dec m,
#           print first col, thisCol += 1
# Complexity : O(m * n)


def printSpiral(mat):
    m = len(mat)
    n = len(mat[0])

    thisRow = 0
    thisCol = 0
    while thisRow < m and thisCol < n:

        # print first row
        for i in range(thisCol, n):
            print mat[thisRow][i],
        thisRow += 1

        # print last column
        for i in range(thisRow, m):
            print mat[i][n-1],
        n -= 1

        # print last row
        if thisRow < m:
            for i in range(n-1, thisCol-1, -1):
                print mat[m-1][i],
            m -= 1

        # print first column
        if thisCol < n:
            for i in range(m-1, thisRow-1, -1):
                print mat[i][thisCol],
            thisCol += 1


if __name__ == "__main__":
    mat = [[1, 2, 3, 4, 5, 6],
           [7, 8, 9, 10, 11, 12],
           [13, 14, 15, 16, 17, 18]]

    mat = [[1,   2,  3,  4,  5,  6],
           [7,   8,  9, 10, 11, 12],
           [13, 14, 15, 16, 17, 18],
           [19, 20, 21, 22, 23, 24],
           [25, 26, 27, 28, 29, 30],
           [31, 32, 33, 34, 35, 36]]
    printSpiral(mat)
