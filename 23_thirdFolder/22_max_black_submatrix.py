# CTCI : Q17_23_Max_Black_Square
# Question : Imagine you have a square matrix, where each cell (pixel) is either black or
# white. Design an algorithm to find the maximum sub square such that all four borders
# are filled with black pixels.
#
# Question Type : Generic
# Used : For the given matrix make a processed matrix whose cell contains a object squareCell
#        whose members are rightZeros and downZeros from the current cell.
#        Now run one more loop from N to 1 (possible square size) and call findSqaureWithSize()
#        to check if sub square of given size is possible.
#        def findSqaureWithSize(processed, squareSize):
#           count = len(processed) - squareSize + 1
#           for row in range(0, count):
#               for col in range(0, count):
#                   if isSquare(processed, row, col, squareSize):
#                       return row, col, squareSize
#            return None
#         Note that isSquare checks if processed has equal or more 0's than squareSize,
#         from position (row,col)
# Complexity : O(N ^ 3)


class SquareCell:
    def __init__(self, rightZeros, downZeros):
        self.rightZeros = rightZeros
        self.downZeros = downZeros


def processSquare(matrix):
    processed = []
    for i in range(len(matrix)):
        row = [None] * len(matrix[0])
        processed.append(row)

    for r in range(len(matrix)-1, -1, -1):
        for c in range(len(matrix)-1, -1, -1):
            rightZeros = 0
            downZeros = 0
            if matrix[r][c] is 0:
                rightZeros = 1
                downZeros = 1
                if c + 1 < len(matrix):
                    previous = processed[r][c+1]
                    rightZeros += previous.rightZeros

                if r + 1 < len(matrix):
                    previous = processed[r+1][c]
                    downZeros += previous.downZeros

            processed[r][c] = SquareCell(rightZeros, downZeros)

    return processed


def findSqaure(matrix):
    processed = processSquare(matrix)

    for i in range(len(matrix), 0, -1):
        square = findSqaureWithSize(processed, i)
        if square is not None:
            return square
    return None


def isSquare(processed, row, col, squareSize):
    topLeft = processed[row][col]
    topRight = processed[row][col + squareSize - 1]
    bottomLeft = processed[row + squareSize - 1][col]

    if topLeft.rightZeros < squareSize: return False
    if topLeft.downZeros < squareSize: return False
    if topRight.downZeros < squareSize: return False
    if bottomLeft.rightZeros < squareSize: return False

    return True


def findSqaureWithSize(processed, squareSize):
    count = len(processed) - squareSize + 1

    for row in range(0, count):
        for col in range(0, count):
            if isSquare(processed, row, col, squareSize):
                return row, col, squareSize
    return None


if __name__ == "__main__":
    matrix = [[0, 0, 1],
              [0, 0, 1],
              [1, 0, 1]]
    print("row, col, length :"),
    print(findSqaure(matrix))
