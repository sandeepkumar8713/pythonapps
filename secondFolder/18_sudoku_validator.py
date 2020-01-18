# https://stackoverflow.com/questions/5484629/check-if-sudoku-solution-is-valid
# Question : Write code for Sudoku Validator in most optimal time and space complexity.
#
# Used : Save sum and product of 1 to 9.
#        Run a loop over each row, col and sub matrix(3*3) to check that there sum and product are equal as above.
# Complexity : O(n^2)


CSUM = 45
CPROD = 362880


def validateBoard(mat):
    for i in range(len(mat)):
        tSum = 0
        tProduct = 1
        for j in range(len(mat[0])):
            tSum += mat[i][j]
            tProduct *= mat[i][j]
        if tSum != CSUM and tProduct != CPROD:
            return False

    for j in range(len(mat[0])):
        tSum = 0
        tProduct = 1
        for i in range(len(mat)):
            tSum += mat[i][j]
            tProduct *= mat[i][j]
        if tSum != CSUM and tProduct != CPROD:
            return False

    for i in range(0,9,3):
        for j in range(0,9,3):
            tSum = 0
            tProduct = 1
            for m in range(i, i+3):
                for n in range(j, j+3):
                    tSum += mat[m][n]
                    tProduct *= mat[m][n]
            if tSum != CSUM and tProduct != CPROD:
                return False

    return True


if __name__ == "__main__":
    mat = [[3, 1, 6, 5, 7, 8, 4, 9, 2],
           [5, 2, 9, 1, 3, 4, 7, 6, 8],
           [4, 8, 7, 6, 2, 9, 5, 3, 1],
           [2, 6, 3, 4, 1, 5, 9, 8, 7],
           [9, 7, 4, 8, 6, 3, 1, 2, 5],
           [8, 5, 1, 7, 9, 2, 6, 4, 3],
           [1, 3, 8, 9, 4, 7, 2, 5, 6],
           [6, 9, 2, 3, 5, 1, 8, 7, 4],
           [7, 4, 5, 2, 8, 6, 3, 1, 9]]
    print validateBoard(mat)
