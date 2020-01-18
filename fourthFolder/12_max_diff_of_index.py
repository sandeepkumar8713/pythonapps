# https://www.geeksforgeeks.org/given-an-array-arr-find-the-maximum-j-i-such-that-arrj-arri/
# Question : Given an array arr[], find the maximum j - i such that arr[j] > arr[i].
#
# Examples :
# Input: {34, 8, 10, 3, 2, 80, 30, 33, 1}
# Output: 6  (j = 7, i = 1)
#
# Used : Compute leftMin array, i.e. minimum array that starts from 0.
#        Compute rightMin array, i.e. maximum array that starts from n-1.
#        Run loop over these two array to find max difference of j-i
#        while j < n and i < n:
#           if LMin[i] < RMax[j]:
#               maxDiff = max(maxDiff, j - i)
#               j = j + 1
#           else:
#               i = i + 1
#        return maxDiff
# Complexity : O(n)


def maxIndexDiff(arr, n):
    LMin = [0] * n
    RMax = [0] * n

    LMin[0] = arr[0]
    for i in range(1, n):
        LMin[i] = min(arr[i], LMin[i - 1])

    RMax[n - 1] = arr[n - 1]
    for j in range(n - 2, -1, -1):
        RMax[j] = max(arr[j], RMax[j + 1]);

    i, j = 0, 0
    maxDiff = -1
    while j < n and i < n:
        if LMin[i] < RMax[j]:
            maxDiff = max(maxDiff, j - i)
            j = j + 1
        else:
            i = i + 1
    return maxDiff


if __name__ == '__main__':
    arr = [9, 2, 3, 4, 5, 6, 7, 8, 18, 0]
    n = len(arr)
    maxDiff = maxIndexDiff(arr, n)
    print (maxDiff)
