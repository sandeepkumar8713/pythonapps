# https://leetcode.com/articles/toeplitz-matrix/
# Question : A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.
# Now given an M x N matrix, return True if and only if the matrix is Toeplitz. Follow up:
# What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row
# of the matrix into the memory at once? What if the matrix is so large that you can only load up a partial row
# into the memory at once?
#
# Example : Input: matrix =
#   [[1,2,3,4],
#   [5,1,2,3],
#   [9,5,1,2]]
# Output: True
#
# Question Type : ShouldSee
# Used : We ask what feature makes two coordinates (r1, c1) and (r2, c2) belong to the same diagonal?
#        It turns out two coordinates are on the same diagonal if and only if r1 - c1 == r2 - c2.
#        This leads to the following idea: remember the value of that diagonal as groups[r-c]. If we see a mismatch,
#        the matrix is not Toeplitz otherwise it is.
#        Logic :
#        for i in range(len(inpMat)):
#           row = inpMat[i]
#           for j in range(len(row)):
#               val = row[j], diff = i - j
#               if diff not in map.keys(): map[diff] = val
#               elif map[diff] != val: return False
#        return True
# Complexity : O(N * M) space O(N + M) diagonal count


def isToeplitzMatrix(inpMat):
    map = dict()
    for i in range(len(inpMat)):
        row = inpMat[i]
        for j in range(len(row)):
            val = row[j]
            diff = i - j
            if diff not in map.keys():
                map[diff] = val
            elif map[diff] != val:
                return False

    return True


if __name__ == "__main__":
    inpMat = [[1, 2, 3, 4],
              [5, 1, 2, 3],
              [9, 5, 1, 2]]
    print(isToeplitzMatrix(inpMat))
