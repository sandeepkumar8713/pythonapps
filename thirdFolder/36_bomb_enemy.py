# https://massivealgorithms.blogspot.com/2016/06/leetcode-361-bomb-enemy.html
# Question : Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return
# the maximum enemies you can kill using one bomb. The bomb kills all the enemies in the same row and column from
# the planted point until it hits the wall since the wall is too strong to be destroyed. Note that you can only put
# the bomb at an empty cell.
#
# Example: Input :
# 0 E 0 0
# E 0 W E
# 0 E 0 0
# Output : 3 (Placing a bomb at (1,1) kills 3 enemies)
#
# Used : Run 2 loops in the matrix, from the current cell count the number of enemy hits until a wall hits (both row
#        and col). Also keep track of max enemy hit.
#        Logic : maxKilledEnemies(inpMat):
#        for i in range(m):
#           for j in range(n):
#               if j == 0 or inpMat[i][j - 1] == 'W':
#                   rowHits = 0, k = j
#                   while k < n and inpMat[i][k] != 'W':
#                       if inpMat[i][k] == 'E': rowHits += 1
#                       k += 1
#               if i == 0 or inpMat[i - 1][j] == 'W':
#                   colHits[j] = 0, k = i
#                   while k < m and inpMat[k][j] != 'W':
#                       if inpMat[k][j] == 'E': colHits[j] += 1
#                       k += 1
#               if inpMat[i][j] == '0':
#                   result = max(result, rowHits + colHits[j])
#        return result
# Complexity : O(m * n)


def maxKilledEnemies(inpMat):
    m = len(inpMat)
    n = len(inpMat[0])
    rowHits = 0
    colHits = [0] * n
    result = 0

    for i in range(m):
        for j in range(n):
            if j == 0 or inpMat[i][j - 1] == 'W':
                rowHits = 0
                k = j
                while k < n and inpMat[i][k] != 'W':
                    if inpMat[i][k] == 'E':
                        rowHits += 1
                    k += 1

            if i == 0 or inpMat[i - 1][j] == 'W':
                colHits[j] = 0
                k = i
                while k < m and inpMat[k][j] != 'W':
                    if inpMat[k][j] == 'E':
                        colHits[j] += 1
                    k += 1

            if inpMat[i][j] == '0':
                result = max(result, rowHits + colHits[j])

    return result


if __name__ == "__main__":
    inpMat = [['0', 'E', '0', '0'],
              ['E', '0', 'W', 'E'],
              ['0', 'E', '0', '0']]

    print maxKilledEnemies(inpMat)
