# https://www.geeksforgeeks.org/3-way-quicksort-dutch-national-flag/
# Question : In simple QuickSort algorithm, we select an element as pivot, partition the array around pivot
# and recur for subarrays on left and right of pivot.
#
# Consider an array which has many redundant elements. For example,
# {1, 4, 2, 4, 2, 4, 1, 2, 4, 1, 2, 2, 2, 2, 4, 1, 4, 4, 4}. If 4 is picked as pivot in Simple QuickSort, we fix
#  only one 4 and recursively process remaining occurrences.
#
# Used : In partition function. After finding pivot position. Run a loop from 0 to pivotPosition-1 and keep swapping
#        pivot to middle. Similarly run a loop from pivotPosition+1 to n-1 and keep swapping pivot to middle. Now
#        partition would return left and right pivot position. Use these two position to do quicksort further.
#        quickSort(array, start, pivotLeft[0] - 1)
#        quickSort(array, pivotRight[0] + 1, end)
# Complexity : O(n log n)


def quickSort(array, start, end):
    if start < end:
        pivotLeft = [0]
        pivotRight = [0]
        partition(array, start, end, pivotLeft, pivotRight)
        quickSort(array, start, pivotLeft[0] - 1)
        quickSort(array, pivotRight[0] + 1, end)


def partition(arr, left, right, pivotLeft, pivotRight):
    i = (left - 1)  # index of smaller element
    pivot = arr[right]  # pivot

    for j in range(left, right):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = arr[right], arr[i + 1]

    pivotPosition = i + 1
    pivot = arr[i + 1]

    m = 0
    leftCount = 0
    leftPivotPosition = pivotPosition - 1
    while m <= leftPivotPosition:
        if arr[m] == pivot:
            arr[m], arr[leftPivotPosition] = arr[leftPivotPosition], arr[m]
            leftPivotPosition -= 1
            leftCount += 1
        m += 1

    n = right
    rightCount = 0
    rightPivotPosition = pivotPosition + 1
    while rightPivotPosition <= n:
        if arr[n] == pivot:
            arr[n], arr[rightPivotPosition] = arr[rightPivotPosition], arr[n]
            rightPivotPosition += 1
            rightCount += 1
        n -= 1

    pivotLeft[0] = pivotPosition - leftCount
    pivotRight[0] = pivotPosition + rightCount


if __name__ == '__main__':
    array = [1, 4, 45, 6, 10, -8]
    array = [4, 9, 4, 4, 1, 9, 4, 4, 9, 4, 4, 1, 4]
    quickSort(array, 0, len(array) - 1)
    print array
