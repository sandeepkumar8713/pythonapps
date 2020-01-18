# https://www.geeksforgeeks.org/rotate-ring-matrix-anticlockwise-k-elements/
# Question : Given a matrix of order M*N and a value K, the task is to rotate each ring of the matrix
# anticlockwise by K elements. If in any ring elements are less than and equal K then don't rotate it.
#
# Used : Make an auxiliary array temp[] of size M*N.
#        Start traversing matrix in spiral form and store elements of current ring in temp[] array. While storing the
#           elements in temp, keep track of starting and ending positions of current ring.
#        For every ring that is being stored in temp[], rotate that subarray temp[]
#        Repeat this process for each ring of matrix.
#       In last traverse matrix again spirally and copy elements of temp[] array to matrix.
# Array rotate by k : reverse(start, start+k)
#                     reverse(start+k, end)
#                     reverse(start, end)
# Complexity : O(m * n)


def fillMat(temp, mat):
    index = 0
    m = len(mat)
    n = len(mat[0])

    thisRow = 0
    thisCol = 0
    while thisRow < m and thisCol < n:

        # print first row
        for i in range(thisCol, n):
            mat[thisRow][i] = temp[index]
            index += 1
        thisRow += 1

        # print last column
        for i in range(thisRow, m):
            mat[i][n-1] = temp[index]
            index += 1
        n -= 1

        # print last row
        if thisRow < m:
            for i in range(n - 1, thisCol - 1, -1):
                mat[m - 1][i] = temp[index]
                index += 1
            m -= 1

        # print first column
        if thisCol < n:
            for i in range(m - 1, thisRow - 1, -1):
                mat[i][thisCol] = temp[index]
                index += 1
            thisCol += 1

    #print mat


def printSpiral(mat):
    m = len(mat)
    n = len(mat[0])
    temp = []
    startIndex = 0
    endIndex = 0

    thisRow = 0
    thisCol = 0
    while thisRow < m and thisCol < n:

        # print first row
        for i in range(thisCol, n):
            temp.append(mat[thisRow][i])
            endIndex += 1
        thisRow += 1

        # print last column
        for i in range(thisRow, m):
            temp.append(mat[i][n-1])
            endIndex += 1
        n -= 1

        # print last row
        if thisRow < m:
            for i in range(n-1, thisCol-1, -1):
                temp.append(mat[m-1][i])
                endIndex += 1
            m -= 1

        # print first column
        if thisCol < n:
            for i in range(m-1, thisRow-1, -1):
                temp.append(mat[i][thisCol])
                endIndex += 1
            thisCol += 1

        if endIndex - startIndex + 1 >= k:
            temp[startIndex:startIndex + k] = reversed(temp[startIndex: startIndex + k])
            temp[startIndex + k: endIndex] = reversed(temp[startIndex + k: endIndex])
            temp[startIndex: endIndex] = reversed(temp[startIndex: endIndex])

            startIndex = endIndex

    fillMat(temp, mat)


if __name__ == "__main__":
    k = 3
    mat = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15, 16]]
    printSpiral(mat)
    for row in mat:
        print row
