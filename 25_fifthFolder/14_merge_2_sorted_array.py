# https://www.geeksforgeeks.org/merge-two-sorted-arrays-in-o1-extra-space-using-quicksort-partition/
# Question : Given two sorted arrays, arr[], brr[] of size N, and M, the task is to merge the two
# given arrays such that they form a sorted sequence of integers combining elements of both the arrays.
#
# Examples: Input: arr[] = {10}, brr[] = {2, 3}
# Output: 2 3 10
# Explanation: The merged sorted array obtained by taking all the elements from the both
# the arrays is {2, 3, 10}. Therefore, the required output is 2 3 10.
#
# Question Type : Generic
# Used : The idea is to consider the (N + 1)th element of the final sorted array as a pivot element
#        and perform the quick sort partition around the pivot element.
#        Loop through both array to find lesser value to be set as pivot. Call Partition function
#        which makes sure that all the element on left side of pivot are smaller and vice versa
#        in right side. Now sort the elements on both sides.
#        Merge(arr, brr):
#        N = len(arr), M = len(brr)
#        l = 0, r = 0, index = -1, pivot = 0
#        while index < N and l < N and r < M:
#           if arr[l] < brr[r]:
#               pivot = arr[l], l += 1
#           else:
#               pivot = brr[r], r += 1
#           index += 1
#        while index < N and l < N:
#           pivot = arr[l]
#           l += 1, index += 1
#        while index < N and r < M:
#           pivot = brr[r]
#           r += 1, index += 1
#        partition(arr, N, brr, M, pivot)
#        arr = sorted(arr), brr = sorted(brr)
# Complexity : O((N + M)log(N + M)) space: O(1)

# Partition make sure that all the element on left side of pivot are smaller and vice versa in right side.
def partition(arr, N, brr, M, Pivot):
    l = N - 1
    r = 0

    # Find element in arr which is bigger than pivot
    # Find element in brr which is smaller than pivot, once found swap them
    while l >= 0 and r < M:
        if arr[l] < Pivot:
            l -= 1
        elif brr[r] > Pivot:
            r += 1
        else:
            arr[l], brr[r] = brr[r], arr[l]
            l -= 1
            r += 1


def Merge(arr, brr):
    N = len(arr)
    M = len(brr)

    l = 0
    r = 0
    index = -1
    pivot = 0

    # Loop through both array to find lesser value to be set as pivot
    while index < N and l < N and r < M:
        if arr[l] < brr[r]:
            pivot = arr[l]
            l += 1
        else:
            pivot = brr[r]
            r += 1

        index += 1

    # If pivot element is not found or index < N
    while index < N and l < N:
        pivot = arr[l]
        l += 1
        index += 1

    # If pivot element is not found or index < N
    while index < N and r < M:
        pivot = brr[r]
        r += 1
        index += 1

    partition(arr, N, brr, M, pivot)
    arr = sorted(arr)
    brr = sorted(brr)

    for i in range(N):
        print(arr[i], end=" ")
    for i in range(M):
        print(brr[i], end=" ")
    print("")


if __name__ == '__main__':
    arr = [1, 5, 9]
    brr = [2, 4, 7, 10]
    Merge(arr, brr)

    arr = [10]
    brr = [2, 3]
    Merge(arr, brr)
