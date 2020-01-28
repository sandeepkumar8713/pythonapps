# https://www.geeksforgeeks.org/submatrix-sum-queries/
# Question : Given a matrix of size M x N, there are large number of queries to find sub matrix sums. Inputs to
# queries are left top and right bottom indexes of sub matrix whose sum is to find out. How to pre-process the matrix
# so that sub matrix sum queries can be performed in O(1) time.
#
# Question Type : Generic
# Used : Make a auxiliary matrix which would be a cumulative sum of the input matrix. We will use this to find
#        result for the given query.
#        Build aux : 1. Copy first row of mat[][] to aux[][]
#                    2. Do column wise sum of the matrix and store it.
#                    3. Do the row wise sum of updated matrix aux[][] in step 2.
#        Query Computation : def sumQuery(aux, row1, col1, row2, col2):
#        res = aux[row2][col2]
#        if row1 > 0: res = res - aux[row1 - 1][col2]
#        if col1 > 0: res = res - aux[row2][col1 - 1]
#        if row1 > 0 and col1 > 0: res = res + aux[row1 - 1][col1 - 1]
#        return res
# Complexity : pre-process O(n^2) query O(n)


def preProcess(mat, aux):
    M = len(inpMat)
    N = len(inpMat[0])
    # Copy first row of mat[][] to aux[][]
    for i in range(0, N, 1):
        aux[0][i] = mat[0][i]

    # Do column wise sum
    for i in range(1, M, 1):
        for j in range(0, N, 1):
            aux[i][j] = mat[i][j] + aux[i - 1][j]

    # Do row wise sum
    for i in range(0, M, 1):
        for j in range(1, N, 1):
            aux[i][j] += aux[i][j - 1]


def sumQuery(aux, row1, col1, row2, col2):
    # result is now sum of elements between (0, 0) and (rbi, rbj)
    res = aux[row2][col2]

    # Remove elements between (0, 0) and (row1-1, col2)
    if row1 > 0:
        res = res - aux[row1 - 1][col2]

    # Remove elements between (0, 0) and (row2, col1-1)
    if col1 > 0:
        res = res - aux[row2][col1 - 1]

    # Add aux[tli-1][tlj-1] as elements between (0, 0) and (tli-1, tlj-1) are subtracted twice
    if row1 > 0 and col1 > 0:
        res = res + aux[row1 - 1][col1 - 1]

    return res


if __name__ == '__main__':
    inpMat = [[1, 2, 3, 4, 6],
              [5, 3, 8, 1, 2],
              [4, 6, 7, 5, 5],
              [2, 4, 8, 9, 4]]

    M = len(inpMat)
    N = len(inpMat[0])
    aux = [[0 for i in range(N)]
            for j in range(M)]

    preProcess(inpMat, aux)

    tli = 2
    tlj = 2
    rbi = 3
    rbj = 4
    print("Query1:", sumQuery(aux, tli, tlj, rbi, rbj))

    tli = 0
    tlj = 0
    rbi = 1
    rbj = 1
    print("Query2:", sumQuery(aux, tli, tlj, rbi, rbj))

    tli = 1
    tlj = 2
    rbi = 3
    rbj = 3
    print("Query3:", sumQuery(aux, tli, tlj, rbi, rbj))
