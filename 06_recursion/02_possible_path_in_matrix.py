# Question : The problem is to count all the possible paths from top left to bottom right of a mXn matrix with the
# constraints that from each cell you can either move only to right or down.
#
# Used: Solve this using sub problem. Path count to reach x,y is sum of path count to reach cell x-1,y and x,y-1. Use
#       this logic to loop over the input matrix. (Recursion return  numberOfPaths(m-1, n) + numberOfPaths(m, n-1) would
#       have more complexity, overlapping so memorization is used.
# Complexity : O(nm)


def numberOfPaths(m, n):
    # Create a 2D table to store results of subproblems
    count = [[0 for x in range(m)] for y in range(n)]

    for i in range(m):
        count[i][0] = 1

    for j in range(n):
        count[0][j] = 1

    for i in range(1, m):
        for j in range(n):
            count[i][j] = count[i - 1][j] + count[i][j - 1]
    return count[m - 1][n - 1]


if __name__ == "__main__":
    m = 3
    n = 3
    print numberOfPaths(m, n)
