# https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/discuss/429880/Simple-Python-5-lines-O(N)-time-O(1)-space
# https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/
# Question : Given an array of integers, return the maximum sum for a non-empty sub-array
# (contiguous elements) with at most one element deletion. In other words, you want to choose
# a sub-array and optionally delete one element from it so that there is still at least one
# element left and the sum of the remaining elements is maximum possible.
# Note that the sub-array needs to be non-empty after deleting one element.
#
# Example : Input: arr = [1, -2, 0, 3]
# Output: 4
# Explanation: Because we can choose [1, -2, 0, 3] and drop -2, thus the sub-array [1, 0, 3] becomes the maximum value.
#
# Question Type : ShouldSee
# Used : We only need to track two variables: the maximum sum we can get (with / without) a deletion.
#        For the maximum without a deletion, it is purely Kadane's algorithm.
#        For the maximum with a deletion, we can either discard current number, or, add current number to previous
#        maximum with a deletion.
# Logic: maxi = modified = unmodified = -sys.maxsize
#        for n in arr:
#           modified, unmodified = max(unmodified, modified + n), max(0, unmodified) + n
#           maxi = max(maxi, modified, unmodified)
#        return maxi
# Complexity : O(n)

import sys


def maximumSum(arr):
    maxi = modified = unmodified = -sys.maxsize

    for n in arr:
        modified, unmodified = max(unmodified, modified + n), max(0, unmodified) + n
        maxi = max(maxi, modified, unmodified)
    return maxi


if __name__ == "__main__":
    inpArr = [1, -2, 0, 3]
    print(maximumSum(inpArr))
