# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/
# Question : Given an array nums, you are allowed to choose one element of nums and change it
# by any value in one move. Return the minimum difference between the largest and smallest
# value of nums after performing at most 3 moves.
#
# Question Type : Generic
# Used : We will use sliding window here. Sort the the inpArr.
#        windowlen = len(inpArr) - 3
#        Run loop over inpArr,
#           check min of [rightmost of the window] - [leftmost of the window]
#           slide over
#        Logic :
#        if len(inpArr) < 5: return 0
#        inpArr.sort()
#        window_len = len(inpArr) - 3
#        for i in range(0, len(inpArr) - window_len + 1):
#           res = min(res, inpArr[i + window_len - 1] - inpArr[i])
#        return res
# Complexity : O(n log n)


import sys


def minDifference(inpArr):
    if len(inpArr) < 5:
        return 0

    inpArr.sort()
    window_len = len(inpArr) - 3
    res = sys.maxsize
    for i in range(0, len(inpArr) - window_len + 1):
        res = min(res, inpArr[i + window_len - 1] - inpArr[i])

    return res


if __name__ == "__main__":
    inpArr = [5, 3, 2, 4]
    print (minDifference(inpArr))

    inpArr = [6, 6, 0, 1, 1, 4, 6]
    print(minDifference(inpArr))
