# https://www.geeksforgeeks.org/printing-brackets-matrix-chain-multiplication-problem/
# Question : Given a sequence of matrices, find the most efficient way to multiply these matrices together.
# The problem is not actually to perform the multiplications, but merely to decide in which order to perform the
# multiplications.
#
# Question Type : Generic
# Used : L is chain length. Here we are taking variable length and start at different i. Place parenthesis at different
#        places between first and last matrix(i,j), recursively calculate count of multiplications for each parenthesis
#        placement and return the minimum count.
#        We have to run 3 loops.
#
#         for L in range(2, n):
#           for i in range(1, n-L+1):
#               j = i + L - 1
#               for k in range(i, j):
#                   q = dp[i][k] + dp[k+1][j] + matrixSize[i-1] * matrixSize[k] * matrixSize[j]
#               Update dp[i][j], if q is lesser and set bracket[i][j] = k
#
#        minCost = dp[1][n-1]
#        Call recursive function printParenthesis(1, n-1, bracket, [ord('A')])
# printParenthesis() : if i == j : print name, increment name, return
#                       print "(",
#                       printParenthesis(i, bracket[i][j], bracket, matrixNameAscii)
#                       printParenthesis(bracket[i][j] + 1, j, bracket, matrixNameAscii)
#                       print ")",
# Complexity : O(n^3)

import sys


def printParenthesis(i, j, bracket, matrixNameAscii):
    if i == j:
        print(chr(matrixNameAscii[0]),end=" ")
        matrixNameAscii[0] += 1
        return

    print("(",end=" ")
    printParenthesis(i, bracket[i][j], bracket, matrixNameAscii)
    printParenthesis(bracket[i][j] + 1, j, bracket, matrixNameAscii)
    print(")",end=" ")


def matrixChainOrder(matrixSize):
    n = len(matrixSize)
    # Multiplication Size
    dp = []
    for i in range(n):
        dp.append([sys.maxsize] * n)

    for i in range(n):
        dp[i][i] = 0

    bracket = []
    for i in range(n):
        bracket.append([0] * n)

    # L is chain length
    # Here we are taking variable length and start at different i.
    for L in range(2, n):
        for i in range(1, n-L+1):
            j = i + L - 1
            # Place parenthesis at different places between first and last matrix, recursively calculate count of
            # multiplications for each parenthesis placement and return the minimum count
            for k in range(i, j):
                # We are placing k(bracket) in middle and calculating assuming matrices i to k and k + 1 to j are
                # already multiplied
                q = dp[i][k] + dp[k+1][j] + matrixSize[i-1] * matrixSize[k] * matrixSize[j] # matrix multiplication cost
                if q < dp[i][j]:
                    dp[i][j] = q
                    bracket[i][j] = k

    matrixNameAscii = ord('A')
    printParenthesis(1, n-1, bracket, [matrixNameAscii])
    print("")
    print(dp[1][n-1])


if __name__ == "__main__":
    # take care that here array is n + 1
    matrixSize = [40, 20, 30, 10, 30]
    matrixChainOrder(matrixSize)
