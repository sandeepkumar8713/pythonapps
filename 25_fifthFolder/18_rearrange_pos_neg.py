# https://www.geeksforgeeks.org/rearrange-positive-and-negative-numbers-publish/
# Question : An array contains both positive and negative numbers in random order. Rearrange the array
# elements so that positive and negative numbers are placed alternatively. Number of positive and negative
# numbers need not be equal. If there are more positive numbers they appear at the end of the array.
# If there are more negative numbers, they too appear in the end of the array.
#
# Example : Input : [-1, 2, -3, 4, 5, 6, -7, 8, 9]
# Output : [9, -7, 8, -3, 5, -1, 2, 4, 6]
#
# Question Type : Easy
# Used : First of all move all the negative numbers to left and positive ones to right. To do this use, logic
#        similar to quicksort partition. The idea is to consider 0 as pivot and divide the array around it.
#        Now swap alternate negative numbers on left with positive ones in right.
#        rearrange(arr, n):
#        i = -1
#        for j in range(n):
#           if arr[j] < 0:
#               i += 1
#               arr[i], arr[j] = arr[j], arr[i]
#        pos, neg = i + 1, 0
#        while neg < pos < n and arr[neg] < 0:
#           arr[neg], arr[pos] = arr[pos], arr[neg]
#           pos += 1, neg += 2
# Complexity : O(n)


def rearrange(arr, n):
    # The following few lines are similar to partition process of QuickSort.
    # The idea is to consider 0 as pivot and divide the array around it.
    i = -1
    for j in range(n):
        if arr[j] < 0:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Now all positive numbers are at end and negative numbers at the beginning of array.
    pos, neg = i + 1, 0

    # Increment the negative index by 2 and positive index by 1,
    # i.e., swap every alternate negative number with next positive number
    while neg < pos < n and arr[neg] < 0:
        # swapping of arr
        arr[neg], arr[pos] = arr[pos], arr[neg]
        pos += 1
        neg += 2


if __name__ == "__main__":
    arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
    n = len(arr)
    rearrange(arr, n)
    print(arr)
