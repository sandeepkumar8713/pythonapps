# CTCI : Q8_03_Magic_Index
# Question : Given an array of n integers sorted in ascending order, write a function that returns a Fixed Point
# in the array, if there is any Fixed Point present in array, else returns -1. Fixed Point in an array is an index i
# such that arr[i] is equal to i. Note that integers in array can be negative and elements can be repeated.
#
# Example : input : [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]
#           output : 7
#
# Used : We used binary search as the input array is already sorted. But here we know that some elements can be
#       repeated, so mid index calculation has changed. If element is not found in left side we search
#       in right side.
#       left = magicIndex(arr, start, min(midValue, midIndex - 1))
#       right = magicIndex(arr, max(midValue, midIndex + 1), end)
# Complexity : average O(log n) worst : O(n)


def magicIndex(arr, start, end):
    if start > end:
        return -1

    midIndex = (start + end) / 2
    midValue = arr[midIndex]

    if midIndex == midValue:
        return midIndex

    left = magicIndex(arr, start, min(midValue, midIndex - 1))

    if left >= 0:
        return left

    return magicIndex(arr, max(midValue, midIndex + 1), end)


if __name__ == "__main__":
    # arr = [-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13
    arr = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]
    n = len(arr)

    index = magicIndex(arr, 0, n - 1)

    if index == -1:
        print("No Magic Index")
    else:
        print("Magic Index is : " + str(index))
