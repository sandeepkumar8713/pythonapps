# https://leetcode.com/problems/diagonal-traverse/
# Question : Given an m x n matrix mat, return an array of all the elements of the
# array in a diagonal order.
#
# Example : Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,4,7,5,3,6,8,9]
#
# Question Type : Generic
# Used : Remember the concept that sum for a diagonal, sum of its indices are equal.
#        Loop over matrix and update dict where
#        key : sum of indices, value : list of ele for that diagonal
#        Loop over the dict and print in the value list and alternatively reverse the list
#        Logic :
#        map = dict()
#        for i in range(len(inpMat)):
#           for j in range(len(inpMat[0])):
#               map[i + j] = map.get(i + j, []) + [inpMat[i][j]]
#        res = [], index = 0
#        for k, v in map.items():
#           if index % 2 == 0: res.extend(v[::-1])
#           else: res.extend(v)
#           index += 1
#        return res
# Complexity : O(n*m)


def findDiagonalOrder(inpMat):
    map = dict()
    for i in range(len(inpMat)):
        for j in range(len(inpMat[0])):
            map[i + j] = map.get(i + j, []) + [inpMat[i][j]]

    res = []
    index = 0
    for k, v in map.items():
        if index % 2 == 0:
            res.extend(v[::-1])
        else:
            res.extend(v)
        index += 1
    return res


if __name__ == "__main__":
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(findDiagonalOrder(mat))
