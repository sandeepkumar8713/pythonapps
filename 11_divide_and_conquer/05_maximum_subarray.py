# CTCI : Q16_17_Contiguous_Sequence
# https://practice.geeksforgeeks.org/problems/maximum-sub-array5443/1
# Question : You are given a one dimensional array that may contain both positive and negative integers, find the
# sum of contiguous subarray of numbers which has the largest sum.
#
# Question Type : ShouldSee
# Used : 1) Divide the given array in two halves
#        2) Return the maximum of following three
#           a) Maximum subarray sum in left half (Make a recursive call)
#           b) Maximum subarray sum in right half (Make a recursive call)
#           c) Maximum subarray sum such that the subarray crosses the midpoint. maxCrossingSum()
#       maxCrossingSum():
#       The idea is simple, find the maximum sum starting from mid point and ending at some point
#       on left of mid, then find the maximum sum starting from mid + 1 and ending with sum point
#       on right of mid + 1. Finally, combine the two and return.
# Complexity : (n log n)


def maxCrossingSum(arr, l, m, h):
    # Include elements on left of mid.
    sm = 0
    left_sum = -10000

    for i in range(m, l - 1, -1):
        sm = sm + arr[i]

        if sm > left_sum:
            left_sum = sm

    # Include elements on right of mid
    sm = 0
    right_sum = -10000
    for i in range(m + 1, h + 1):
        sm = sm + arr[i]

        if sm > right_sum:
            right_sum = sm

    # Return sum of elements on left and right of mid
    return left_sum + right_sum


def maxSubArraySum(arr, l, h):
    # Base Case: Only one element
    if l == h:
        return arr[l]

    # Find middle point
    m = (l + h) // 2

    return max(maxSubArraySum(arr, l, m),
               maxSubArraySum(arr, m + 1, h),
               maxCrossingSum(arr, l, m, h))


if __name__ == "__main__":
    arr = [2, 3, 4, 5, 7]
    print(maxSubArraySum(arr, 0, len(arr) - 1))

    arr = [2, -8, 3, -2, 4, -10]
    print(maxSubArraySum(arr, 0, len(arr) - 1))

    arr = [1, 2, 5, -7, 2, 3]
    print(maxSubArraySum(arr, 0, len(arr) - 1))
