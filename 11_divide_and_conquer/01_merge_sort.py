# Question : Implement merge Sort
#
# Used : MergeSort(arr[], l,  r)
#        If r > l
#      1. Find the middle point to divide the array into two halves:
#              middle m = (l+r)/2
#      2. Call mergeSort for first half:
#              Call mergeSort(arr, l, m)
#      3. Call mergeSort for second half:
#              Call mergeSort(arr, m+1, r)
#      4. Merge the two halves sorted in step 2 and 3:
#              Call merge(arr, l, m, r)
# Complexity : O(n log n)


def merge(arr, left, mid, right):
    leftRow = []
    for i in range(left, mid+1):
        leftRow.append(arr[i])

    rightRow = []
    for i in range(mid+1, right+1):
        rightRow.append(arr[i])

    i = 0
    j = 0
    while i < len(leftRow) and j < len(rightRow):
        if leftRow[i] <= rightRow[j]:
            arr[left] = leftRow[i]
            i += 1
        else:
            arr[left] = rightRow[j]
            j += 1
        left += 1

    while i < len(leftRow) and left <= right:
        arr[left] = leftRow[i]
        left += 1
        i += 1

    while j < len(rightRow) and left <= right:
        arr[left] = rightRow[j]
        left += 1
        j += 1


def mergeSort(arr, left, right):
    if left < right:
        mid = (left + right)/2
        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)


if __name__ == "__main__":
    arr = [13, 12, 11, 5, 6, 7]
    #arr = [7, 6, 5]
    left = 0
    right = len(arr) - 1
    mergeSort(arr, left, right)
    print arr
