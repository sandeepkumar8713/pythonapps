# https://www.geeksforgeeks.org/google-interview-experience-for-sde-1/
# Question : One grid is given. It contains characters in each cell. You have to find out the smallest
# hamilton distance between x to y.
# Hamilton Distance: |row_index_x - row_index_y| + |column_index_x - column_index_y|
#
# Example :
# Input :
# [ x, 0, 0, 0 ]
# [ 0, y, 0, y ]
# [ x, x, 0, 0 ]
# [ 0, y, 0, 0 ]
# Output : 1
#
# Used : Maintain a table dp of size m * n. Loop over the each and every element of input matrix. but from right side
#        and column wise. col : n-1 to 0 and row : n -1  to 0
#            The idea is to choose min distance out of 3 option right, down and right down
#            right = dp[row][col + 1]
#            down = dp[row][col + 1]
#            right_down = dp[row + 1][col + 1]
#            dp[row][col] = valueFound(mat[row][col], right, down, rightDown) (
#            if mat[row][col] == 'x':
#                if dp[row][col][1] < minDist:
#                    minDist = dp[row][col][1]
#        return minDist
#        Note valueFound gives, minimum distance of x and y, from current cell
# Complexity : O(m * n)

maxNumber = 100


def valueFound(thisCell, right, down, rightDown):
    dist = [-1,  -1]

    if 'x' == thisCell:
        dist[0] = 0
    else:
        dist[0] = min(right[0] + 1, down[0] + 1, rightDown[0] + 2)

    if 'y' == thisCell:
        dist[1] = 0
    else:
        dist[1] = min(right[1] + 1, down[1] + 1, rightDown[1] + 2)

    return dist


def hamiltonDistance(mat, m, n):
    dp = []
    for i in range(m):
        dp.append([[maxNumber, maxNumber]] * n)

    minDist = maxNumber

    for col in range(n - 1, -1, -1):
        for row in range(m-1, -1, -1):
            # if take right
            if col == n - 1:
                right = [maxNumber,  maxNumber]
            else:
                right = dp[row][col + 1]

            # if take down
            if row == m - 1:
                down = [maxNumber,  maxNumber]
            else:
                down = dp[row + 1][col]

            # if take right down
            if row == m - 1 or col == n - 1:
                rightDown = [maxNumber, maxNumber]
            else:
                rightDown = dp[row + 1][col + 1]

            dp[row][col] = valueFound(mat[row][col], right, down, rightDown)

            if mat[row][col] == 'x':
                if dp[row][col][1] < minDist:
                    minDist = dp[row][col][1]

            if mat[row][col] == 'y':
                if dp[row][col][0] < minDist:
                    minDist = dp[row][col][0]

    return minDist


if __name__ == "__main__":
    inpMatrix = [['x', '0', '0'],
                 ['0', '0', '0'],
                 ['x', '0', 'y']]

    m = len(inpMatrix)
    n = len(inpMatrix[0])
    print (hamiltonDistance(inpMatrix,m,n))

