# https://www.geeksforgeeks.org/counting-inversions/
# Question : Inversion Count for an array indicates - how far (or close) the array is from being
# sorted. If array is already sorted then inversion count is 0. If array is sorted in reverse order
# that inversion count is the maximum.
# Formally speaking, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j
#
# Example:
# The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).
#
# Question Type : Generic
# Used : We will do normal merge sort. While doing merge if second array has smaller element,
#        increase invCount by no. of elements left in first array.
# Logic: while i <= mid and j <= right:
#        if arr[i] <= arr[j]:
#           temp_arr[k] = arr[i], k += 1, i += 1
#        else:
#           inv_count += (mid - i + 1)
#        temp_arr[k] = arr[j], k += 1, j += 1
# Complexity : O(n log n)


def mergeSort(arr, n):
    temp_arr = [0] * n
    return mergeSortUtils(arr, temp_arr, 0, n - 1)


def mergeSortUtils(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count = mergeSortUtils(arr, temp_arr, left, mid)
        inv_count += mergeSortUtils(arr, temp_arr, mid + 1, right)
        inv_count += merge(arr, temp_arr, left, mid, right)
    return inv_count


def merge(arr, temp_arr, left, mid, right):
    i = left  # Starting index of left subarray
    j = mid + 1  # Starting index of right subarray
    k = left  # Starting index of to be sorted subarray
    inv_count = 0

    # Conditions are checked to make sure that i and j don't exceed their subarray limits.
    while i <= mid and j <= right:
        # There will be no inversion if arr[i] <= arr[j]
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            # Inversion will occur.
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            k += 1
            j += 1

    # Copy the remaining elements of left subarray into temporary array
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1

    # Copy the remaining elements of right subarray into temporary array
    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1

    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inv_count


if __name__ == "__main__":
    arr = [1, 20, 6, 4, 5]
    n = len(arr)
    result = mergeSort(arr, n)
    print("Number of inversions are", result)
