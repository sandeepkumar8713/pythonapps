# https://www.geeksforgeeks.org/count-all-square-sub-matrix-with-sum-greater-than-the-given-number-s/
# Question : Given a matrix mat[][] and two integers K and S, the task is to count all K x K sub-matrix such that the
# sum of all the elements in the sub-matrix is greater than or equal to S.
#
# Example : Input: K = 2, S = 15
# mat[][] = {{1, 2, 3},
#            {4, 5, 6},
#            {7, 8, 9}}
# Output: 3
# Explanation:
# In the given matrix there are 3 sub-matrix
# Sub-Matrix 1: (0, 1) to (1, 2)
# Sum = 2 + 3 + 5 + 6 = 16
# Sub-matrix 2: (1, 0) to (2, 1)
# Sum = 4 + 5 + 7 + 8 = 24
# Sub-matrix 3: (1, 1) to (2, 2)
# Sum = 5 + 6 + 8 + 9 = 28
#
# Question Type : Generic
# Used : Make a dp matrix : m * n
#        Set dp's value as cumulative sum of given input matrix
#        Run 2 loop on dp,for row and col, checking all the possible submatrix of size k
#        Use the already computed cumulative sum to compare with target sum and keep incrementing count
#        Return count at the end of loop
#        Logic : createTable(mat, k, p, dp):
#        dp[0][0] = mat[0][0]
#        for j in range(1, dim): dp[0][j] = mat[0][j] + dp[0][j - 1]
#        for i in range(1, dim): dp[i][0] = mat[i][0] + dp[i - 1][0]
#        for i in range(1, dim):
#           for j in range(1, dim):
#             dp[i][j] = (mat[i][j] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1])
#
#        countSubMatrixUtil(dp, k, target):
#        for i in range(k - 1, dim):
#           for j in range(k - 1, dim, 1):
#             subMatSum = dp[i][j] - subMatrixSum(dp, i - k, j) -\
#             subMatrixSum(dp, i, j - k) + subMatrixSum(dp, i - k, j - k)
#             if subMatSum >= target:
#                 count += 1
#        return count
# Complexity : O(M * N)

dim = 5


# Function to create a cumulative matrix
def createTable(mat, k, p, dp):
    dp[0][0] = mat[0][0]

    for j in range(1, dim):
        dp[0][j] = mat[0][j] + dp[0][j - 1]

    for i in range(1, dim):
        dp[i][0] = mat[i][0] + dp[i - 1][0]

    for i in range(1, dim):
        for j in range(1, dim):
            dp[i][j] = (mat[i][j] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1])


def subMatrixSum(dp, x, y):
    if x < 0 or y < 0:
        return 0
    return dp[x][y]


def countSubMatrixUtil(dp, k, target):
    count = 0
    subMatSum = 0

    for i in range(k - 1, dim):
        for j in range(k - 1, dim, 1):
            subMatSum = dp[i][j] - subMatrixSum(dp, i - k, j) -\
            subMatrixSum(dp, i, j - k) + subMatrixSum(dp, i - k, j - k)
            if subMatSum >= target:
                count += 1
    return count


def countSubMatrix(mtrx, k, target):
    dp = [[0] * dim for i in range(dim)]
    createTable(mtrx, k, target, dp)
    return countSubMatrixUtil(dp, k, target)


if __name__ == '__main__':
    mtrx = [[1, 7, 1, 1, 1],
            [2, 2, 2, 2, 2],
            [3, 9, 6, 7, 3],
            [4, 3, 2, 4, 5],
            [5, 1, 5, 3, 1]]
    k = 3
    target = 35
    print(countSubMatrix(mtrx, k, target))
