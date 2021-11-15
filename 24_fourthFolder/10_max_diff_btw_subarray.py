# https://www.geeksforgeeks.org/maximum-absolute-difference-between-sum-of-two-contiguous-sub-arrays/
# Question : Given an array of integers, find two non-overlapping contiguous sub-arrays
# such that the absolute difference between the sum of two sub-arrays is maximum.
#
# Example:
# Input: [-2, -3, 4, -1, -2, 1, 5, -3]
# Output: 12
# Two sub arrays are [-2, -3] and [4, -1, -2, 1, 5]
#
# Question Type : Generic
# Used : Using Kadane algorithm we can find left and right max sub array.
#        We can find min sub array by inverting the sign of input array.
#        Now use this logic:
#        for i in range(n - 1):
#           absValue = max(abs(leftMax[i] - rightMin[i + 1]), abs(leftMin[i] - rightMax[i + 1]))
#           if absValue > result: result = absValue
#        return result
#        Note : We are cutting the array at each index and checking its left and right sub array
#        for difference.
# Complexity : O(n)

import sys


def maxLeftSubArraySum(a, size, sum):
    max_so_far = a[0]
    curr_max = a[0]
    sum[0] = max_so_far

    for i in range(1, size):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far, curr_max)
        sum[i] = max_so_far

    return max_so_far


def maxRightSubArraySum(a, n, sum):
    max_so_far = a[n]
    curr_max = a[n]
    sum[n] = max_so_far

    for i in range(n - 1, -1, -1):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far, curr_max)
        sum[i] = max_so_far

    return max_so_far


def findMaxAbsDiff(arr, n):
    leftMax = [0] * n
    maxLeftSubArraySum(arr, n, leftMax)

    rightMax = [0] * n
    maxRightSubArraySum(arr, n - 1, rightMax)

    invertArr = [0] * n
    for i in range(n):
        invertArr[i] = -arr[i]

    leftMin = [0] * n
    maxLeftSubArraySum(invertArr, n, leftMin)
    for i in range(n):
        leftMin[i] = -leftMin[i]

    rightMin = [0] * n
    maxRightSubArraySum(invertArr, n - 1, rightMin)
    for i in range(n):
        rightMin[i] = -rightMin[i]

    result = -sys.maxsize
    for i in range(n - 1):
        absValue = max(abs(leftMax[i] - rightMin[i + 1]),
                       abs(leftMin[i] - rightMax[i + 1]))
        if absValue > result:
            result = absValue

    return result


if __name__ == "__main__":
    a = [-2, -3, 4, -1, -2, 1, 5, -3]
    n = len(a)
    print(findMaxAbsDiff(a, n))
