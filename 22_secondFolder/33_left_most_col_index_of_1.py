# https://leetcode.com/discuss/interview-question/341247/Facebook-and-Google-or-Phone-screen-or-Leftmost-column-index-of-1
# Question : In a binary matrix (all elements are 0 and 1), every row is sorted in ascending order (0 to the left of
# 1). Find the leftmost column index with a 1 in it.
#
# Example : Input:
# [[0, 0, 0, 1],
#  [0, 0, 1, 1],
#  [0, 1, 1, 1],
#  [0, 0, 0, 0]]
# Output: 1
#
# Question Type : ShouldSee
# Used : We start from first row and last col. If 1 is found, we reduce col else inc row. Since it is sorted in
#        ascending order we use this logic. We need to find first 1.
#        Logic : def findLeftMostIndexOfOne(inpMat):
#        rows = len(inpMat)
#        cols = len(inpMat[0])
#        i = 0, j = cols - 1
#        candidate = -1
#        while i < rows and j >= 0:
#           if inpMat[i][j] == 1:
#               candidate = j
#               j -= 1
#           else:
#               i += 1
#        return candidate
# Complexity : O(r + c)


def findLeftMostIndexOfOne(inpMat):
    rows = len(inpMat)
    cols = len(inpMat[0])
    i = 0
    j = cols - 1
    candidate = -1
    while i < rows and j >= 0:
        if inpMat[i][j] == 1:
            candidate = j
            j -= 1
        else:
            i += 1
    return candidate


if __name__ == "__main__":
    inpMat = [[0, 0, 0, 1],
              [0, 0, 1, 1],
              [0, 1, 1, 1],
              [0, 0, 0, 0]]

    print(findLeftMostIndexOfOne(inpMat))
