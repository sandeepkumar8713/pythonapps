# https://leetcode.com/problems/longest-mountain-in-array/
# Similar : https://leetcode.com/problems/peak-index-in-a-mountain-array/
# You may recall that an array arr is a mountain array if and only if:
# arr.length >= 3
# There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
#   arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
#   arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given an integer array arr, return the length of the longest subarray, which is a mountain.
# Return 0 if there is no mountain subarray.
#
# Question Type : Generic
# Used : Find left min and right min array. Break will happen even if values are same.
#        as we need strictly increasing. Also keep track of index
# Logic: max_len = 0
#        for i in range(1, n - 1):
#           if left_min_array[i - 1] < arr[i] and arr[i] > right_min_array[i + 1] and \
#               arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
#                   this_len = (index_right[i + 1] - index_left[i - 1]) + 1
#                   max_len = max(this_len, max_len)
#        return max_len
# Complexity : O(n)

def longest_mountain(arr):
    n = len(arr)

    left_min_array = arr[::]
    index_left = [0] * n
    left_min_array[0] = arr[0]

    for i in range(1, n):
        if left_min_array[i - 1] > arr[i] or arr[i - 1] >= arr[i]:
            left_min_array[i] = arr[i]
            index_left[i] = i
        else:
            left_min_array[i] = left_min_array[i - 1]
            index_left[i] = index_left[i - 1]

    right_min_array = arr[::]
    index_right = [n - 1] * n
    right_min_array[n - 1] = arr[n - 1]

    for i in range(n - 2, -1, -1):
        if right_min_array[i + 1] > arr[i] or arr[i] <= arr[i + 1]:
            right_min_array[i] = arr[i]
            index_right[i] = i
        else:
            right_min_array[i] = right_min_array[i + 1]
            index_right[i] = index_right[i + 1]

    max_len = 0
    for i in range(1, n - 1):
        if left_min_array[i - 1] < arr[i] and arr[i] > right_min_array[i + 1] and \
                arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
            this_len = (index_right[i + 1] - index_left[i - 1]) + 1
            max_len = max(this_len, max_len)

    return max_len


if __name__ == "__main__":
    print(longest_mountain([1, 2, 2, 2]))

    arr = [0, 2, 0, 2, 1, 2, 3, 4, 4, 1]
    print(longest_mountain(arr))

    arr = [3, 6, 5, 6, 3, 9]
    print(longest_mountain(arr))
