# https://leetcode.com/problems/maximal-rectangle/
# https://leetcode.com/problems/maximal-rectangle/discuss/452868/JavaScript-DP-O(n)-Time-and-Space
# Question : Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle
# containing only 1's and return its area.
#
# Example: Input:
#  [["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]]
# Output: 6
#
# Question Type : ShouldSee
# Used : We will do DP here. At each row, will try to find max subset with all 1.
# Logic: maximalRectangle(inpMat)
#        lefts = [0] * width
#        rights = [width] * width
#        heights = [0] * width
#        maxRes = 0
#        for row in range(height):
#           left = 0
#           right = width
#           for i in range(width):
#               if inpMat[row][i] == 1:
#                   lefts[i] = max(left, lefts[i])
#                   heights[i] += 1
#               else:
#                   lefts[i] = heights[i] = 0
#                   left = i + 1
#               rightIdx = width - 1 - i
#               if inpMat[row][rightIdx] == 1:
#                   rights[rightIdx] = min(right, rights[rightIdx])
#               else:
#                   rights[rightIdx] = width
#                   right = rightIdx
#           for i in range(width):
#               maxRes = max(maxRes, (rights[i] - lefts[i]) * heights[i])
#        return maxRes
# Complexity : O(m*n)


def maximalRectangle(inpMat):
    if len(inpMat) == 0 or len(inpMat[0]) == 0:
        return 0

    height = len(inpMat)
    width = len(inpMat[0])
    lefts = [0] * width
    rights = [width] * width
    heights = [0] * width
    maxRes = 0

    for row in range(height):
        left = 0
        right = width
        for i in range(width):
            if inpMat[row][i] == 1:
                lefts[i] = max(left, lefts[i])
                heights[i] += 1
            else:
                lefts[i] = heights[i] = 0
                left = i + 1

            rightIdx = width - 1 - i
            if inpMat[row][rightIdx] == 1:
                rights[rightIdx] = min(right, rights[rightIdx])
            else:
                rights[rightIdx] = width
                right = rightIdx

        for i in range(width):
            maxRes = max(maxRes, (rights[i] - lefts[i]) * heights[i])

    return maxRes


if __name__ == "__main__":
    inpMat = [[1, 0, 1, 0, 0],
              [1, 0, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 0, 0, 1, 0]]

    print(maximalRectangle(inpMat))
