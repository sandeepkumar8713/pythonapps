# Question : Given a 2D array, the task is to print matrix in anti spiral form:
#
# Question Type : Easy
# Used : Push in stack and print
#        1.first row
#        2.last column
#        3.last row
#        4.first column
#        Repeat
# Complexity : O(n*m)

stack = []


def moveInMatrix(matrix, firstRow, firstCol, lastRow, lastCol, elementCount):
    if firstRow > lastRow or firstCol > lastCol:
        return

    for j in range(firstCol, lastCol + 1):
        stack.append(matrix[firstRow][j])

    for i in range(firstRow + 1, lastRow + 1):
        stack.append(matrix[i][lastCol])

    if elementCount <= len(stack):
        return

    for j in range(lastCol - 1, firstCol - 1, -1):
        stack.append(matrix[lastRow][j])

    for i in range(lastRow - 1, firstRow, -1):
        stack.append(matrix[i][firstCol])

    moveInMatrix(matrix, firstRow + 1, firstCol + 1, lastRow - 1, lastCol - 1, elementCount)


def spiralPrint(matrix):
    row = len(matrix) - 1
    col = len(matrix[0]) - 1

    moveInMatrix(matrix, 0, 0, row, col, (row + 1) * (col + 1))


if __name__ == "__main__":
    # matrix = [[1,2,3],
    #           [4,5,6],
    #           [7,8,9]]

    # matrix = [[1,2,3,4],
    #           [5,6,7,8],
    #           [9,10,11,12]]

    # matrix = [[1,2,3,4],
    #           [5,6,7,8],
    #           [9,10,11,12],
    #           [13, 14, 15, 16]]

    matrix = [[1, 2, 3, 4, 5, 6],
              [7, 8, 9, 10, 11, 12],
              [13, 14, 15, 16, 17, 18]]

    spiralPrint(matrix)
    print(stack)
