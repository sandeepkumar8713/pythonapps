# https://leetcode.com/discuss/interview-question/3597465/Wayfair-or-SDE-2-(L2-4)-or-Bengaluru-or-OA
# An intern at HackerRank is assigned is finding the optimal middle subsequence.
# An optimal middle subsequence is the subsequence chosen[] of length 3 chosen from an array arr, such
# that chosen[0] < chosen[1] > chosen[2] and that the sum of its elements is the minimum possible.
# Given an array, return the sum of the values of the optimal middle subsequence. If there is none, return
# -1.
# Note: A subsequence of an array is obtained by deleting some (possibly 0) elements from the array
# without changing the order of the remaining elements. For example, [1, 3] is a subsequence of [1,
# 2, 3, 4] while [4, 2] is not.
#
# Example : Input : Consider n=7 arr=[3,4,5,1,2,3,1].
# Then, the subsequence [1, 2, 1] can be chosen as 1 <
# 2>1and sum=1+2+1=4, which is minimum
# possible. Thus, the answer is 4.
#
# Question type : Generic
# Used : Derive left and right min array.
#        Now check each possible combination, to find the min value.
#        left_min[i] + arr[i] + right_min[i]
# Logic: left[0] = arr[0]
#        for i in range(1, n):
#           left[i] = min(left[i - 1], arr[i])
#        right[n - 1] = arr[n - 1]
#        for i in range(n - 2, 0, -1):
#           right[i] = min(right[i + 1], arr[i])
#        for i in range(1,n-2):
#           result = min(result, left[i-1] + arr[i] + right[i+1])
#        return result
# Complexity : O(n)

import sys


def get_min_subsequence(arr):
    n = len(arr)
    left = [0] * n
    right = [0] * n

    left[0] = arr[0]
    for i in range(1, n):
        left[i] = min(left[i - 1], arr[i])

    right[n - 1] = arr[n - 1]
    for i in range(n - 2, 0, -1):
        right[i] = min(right[i + 1], arr[i])

    result = sys.maxsize
    for i in range(1, n - 2):
        result = min(result, left[i-1] + arr[i] + right[i+1])

    return result


if __name__ == "__main__":
    arr = [3, 4, 5, 1, 2, 3, 1]
    print(get_min_subsequence(arr))
