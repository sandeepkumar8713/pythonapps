# Question : Given a simple expression tree, which is also a full binary tree consisting of basic
# binary operators i.e + - ,* and / and some integers, Your task is to evaluate the
# expression tree. You need to complete the function evalTree which takes the root of the
# tree as its only argument and returns an integer denoting the result obtained by simplifying
# the expression tree.
#
# Full binary tree (is a tree in which every node other than the leaves has two children)
# height of tree h = log(n+1)-1

# instead of switch use dictionary
# Question Type : ShouldSee
# TODO :: add used


def add(A, B):
    return A + B


def subtract(A, B):
    return A - B


def multiply(A, B):
    return A * B


def divide(A, B):
    return A / B


def make2DMatrix(expression, size):
    import math
    height = int(math.log(size + 1, 2)) - 1
    pointer = 0
    matrix = []
    for i in range(0, height + 1):
        rowLength = pow(2, i)
        thisRow = expression[pointer:pointer + rowLength]
        thisRow.insert(0, '')
        matrix.append(thisRow)
        pointer += rowLength

    # print matrix
    return matrix, height


def calculateMatrix(matrix, height):
    for i in range(height - 1, -1, -1):
        thisRow = matrix[i]
        nextRow = matrix[i + 1]
        for j in range(1, len(thisRow)):
            if thisRow[j] in ['+', '-', '*', '/']:
                result = operatorDict[thisRow[j]](int(nextRow[j * 2 - 1]), int(nextRow[j * 2]))

                # print result
                matrix[i][j] = result

    print('result =', matrix[0][1])


operatorDict = {'+': add,
                '-': subtract,
                '*': multiply,
                '/': divide}


if __name__ == "__main__":
    # 5 * 4 + 100 - 20 = + * - 5 4 100 20 (number of nodes 7)
    A = ['+', '*', '-', '5', '4', '100', '20']
    # A = ['-','4','7']
    print('given expression =', A)
    matrix, height = make2DMatrix(A, len(A))
    calculateMatrix(matrix, height)

    # make a in order expression
