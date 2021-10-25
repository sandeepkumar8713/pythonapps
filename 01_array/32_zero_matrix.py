# CTCI : Q1_08_Zero_Matrix
# Question : Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0.
#
# Question Type : ShouldSee
# Used : Check if first row and column has zero, if yes set rowHasZero and colHasZero as true.
#        Now loop through the matrix, if you find 0, set its cell of first row and col to zero
#        (corresponding col or row). Make 2 function nullifyRow and nullifyCol which set 0
#        to given row and col. Run loop over first column and row, if a cell value is 0,
#        call nullifyRow and nullifyCol.
#        if rowHasZero is true, nullifyRow(matrix, 0)
#        if colHasZero is true, nullifyCol(matrix, 0)
# Complexity : O(n^2)


def nullifyRow(matrix, row):
    for j in range(len(matrix[0])):
        matrix[row][j] = 0


def nullifyCol(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0


def setZero(matrix):
    rowHasZero = False
    colHasZero = False

    for j in range(len(matrix[0])):
        if matrix[0][j] == 0:
            rowHasZero = True
            break

    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            colHasZero = True

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for j in range(len(matrix[0])):
        if matrix[0][j] == 0:
            nullifyCol(matrix, j)

    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            nullifyRow(matrix, i)

    if rowHasZero:
        nullifyRow(matrix, 0)

    if colHasZero:
        nullifyCol(matrix, 0)


if __name__ == "__main__":
    inpMat = [[1, 1, 1],
              [1, 0, 1],
              [1, 1, 1]]
    setZero(inpMat)
    for row in inpMat:
        print(row)
