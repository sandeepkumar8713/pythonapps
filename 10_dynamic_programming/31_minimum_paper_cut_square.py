# https://www.geeksforgeeks.org/paper-cut-minimum-number-squares-set-2/
# Question : Given a paper of size A x B. Task is to cut the paper into squares of any size. Find the minimum
# number of squares that can be cut from the paper.
#
# Examples:
# Input  : 36 x 30
# Output : 5
# Explanation : 3 (squares of size 12x12) +  2 (squares of size 18x18)
#
# Question Type : Generic
# Used : Assuming we have a rectangle with width is N and height is M.
#        if (N == M), so it is a square and nothing need to be done.
#        Otherwise, we can divide the rectangle into two other smaller one (N - x, M) and (x, M), so it can
#        be solved recursively. Similarly, we can also divide it into (N, M - x) and (N, x).
#        def minimumSquare(m, n):
#           if m == n: return 1
#           if dp[m][n] != 0: return dp[m][n]
#           for i in range(1, m // 2 + 1): horizontal_min = min(minimumSquare(i, n) +
#                minimumSquare(m - i, n), horizontal_min)
#           for j in range(1, n // 2 + 1): vertical_min = min(minimumSquare(m, j) +
#                            minimumSquare(m, n - j), vertical_min)
#           dp[m][n] = min(vertical_min, horizontal_min)
#           return dp[m][n]
# Complexity : O(n * m)

import sys

MAX = 300
dp = [[0 for i in range(MAX)] for i in range(MAX)]


def minimumSquare(m, n):
    vertical_min = sys.maxsize
    horizontal_min = sys.maxsize

    if m == n:
        return 1

    if dp[m][n] != 0:
        return dp[m][n]

    # Horizontal cuts
    for i in range(1, m // 2 + 1):
        horizontal_min = min(minimumSquare(i, n) +
                             minimumSquare(m - i, n), horizontal_min)
    # Vertical cuts
    for j in range(1, n // 2 + 1):
        vertical_min = min(minimumSquare(m, j) +
                           minimumSquare(m, n - j), vertical_min)
    dp[m][n] = min(vertical_min, horizontal_min)
    return dp[m][n]


if __name__ == '__main__':
    m = 30
    n = 35
    print(minimumSquare(m, n))
