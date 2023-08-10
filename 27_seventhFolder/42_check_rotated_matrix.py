# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/
# Question : Given two n x n binary matrices mat and target, return true if it is possible to make
# mat equal to target by rotating mat in 90-degree increments, or false otherwise.
#
# Question Type : Generic
# Used : Run a 2d loop.
#        In each iteration check if current element is matching with, 4 elements in the target matrix.
#        If the target is rotation of input matrix one of the element will match.
#        After the loop, check if any one boolean variables is True.
# Logic: p = True, q = True, r = True, s = True
#        for i in range(n):
#           for j in range(n):
#               ele = mat[i][j]
#               if ele != target[i][j]:  # Same
#                   p = False
#               if ele != target[j][n-1-i]: # 90 degree
#                   q = False
#               if ele != target[n-1-i][n-1-j]: # 180 degree
#                   r = False
#               if ele != target[n-1-j][i]: # 270 degree
#                   s = False
#        return p or q or r or s
# Complexity : O(n^2)

def check_if_rotated(mat, target):
    n = len(mat)
    p= True
    q= True
    r= True
    s= True

    for i in range(n):
        for j in range(n):
            ele = mat[i][j]
            if ele != target[i][j]:  # Same
                p = False
            if ele != target[j][n-1-i]: # 90 degree
                q = False
            if ele != target[n-1-i][n-1-j]: # 180 degree
                r = False
            if ele != target[n-1-j][i]: # 270 degree
                s = False

    return p or q or r or s
    # if any of them is true, means we have find one rotation which equals target


if __name__ == "__main__":
    mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    target = [[1, 1, 1], [0, 1, 0], [0, 0, 0]]
    print (check_if_rotated(mat, target))
