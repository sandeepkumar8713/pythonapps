# https://leetcode.com/problems/minimum-falling-path-sum/
# Question : Given a square array of integers A, we want the minimum sum of a falling path
# through A. A falling path starts at any element in the first row, and chooses one element
# from each row.  The next row's choice must be in a column that is different from the
# previous row's column by at most one.
# 10_dynamic_programming/17_gold_mine, but this row wise.
#
# Example : Input: [[1,2,3],[4,5,6],[7,8,9]]
# Output: 12
# Explanation: The possible falling paths are:
# [1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
# [2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
# [3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
# The falling path with the smallest sum is [1,4,7], so the answer is 12
#
# Question Type : ShouldSee, SimilarAdded
# Used : dp(r, c) = A[r][c] + min(dp(r+1, c-1), dp(r+1, c), dp(r+1, c+1)), and the answer is min of dp(0, c)
# Logic: def minFallingPathSum(A):
#        while len(A) >= 2:
#           row = A.pop()
#           for i in xrange(len(row)):
#               A[-1][i] += min(row[max(0, i-1): min(len(row), i+2)])
#        return min(A[0])
# Complexity : O(n)


def minFallingPathSum(A):
    while len(A) >= 2:
        row = A.pop()
        for i in range(len(row)):
            A[-1][i] += min(row[max(0, i-1): min(len(row), i+2)])
    return min(A[0])


if __name__ == "__main__":
    inpMat = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    print(minFallingPathSum(inpMat))
