# https://www.geeksforgeeks.org/quick-sort/
# Question : QuickSort is a sorting algorithm based on the Divide and Conquer algorithm that
# picks an element as a pivot and partitions the given array around the picked pivot by
# placing the pivot in its correct position in the sorted array.
#
# Used : For a given array, call quick sort on with left 0 and right n - 1.
#        While left < right call partition and call quick sort on left and right of pivot
#        In partition function, choose right most element as pivot.
#        Choose i = left - 1, to position before pivot element. Assuming element till i are sorted.
#        Run a loop from left to right for index j.
#           if ele in less than pivot:
#               increment i and swap ele at i and j.
#        After the loop, swap ele at i+1 and right.
#        return i + 1 which is position of pivot.
# Logic: def partition(array, left, right):
#        pivot = array[right]
#        i = left - 1
#        for j in range(left, right):
#           if array[j] <= pivot:
#               i = i + 1
#               (array[i], array[j]) = (array[j], array[i])
#        (array[i + 1], array[right]) = (array[right], array[i + 1])
#        return i + 1
#
#        def quicksort(array, left, right):
#        if left < right:
#           pivot = partition(array, left, right)
#           quicksort(array, left, pivot - 1)
#           quicksort(array, pivot + 1, right)
# Complexity : Best and average O(n log n), Best O(n^2)


def partition(array, left, right):
    # Choose the rightmost element as pivot
    pivot = array[right]
    # Pointer for greater element
    i = left - 1

    for j in range(left, right):
        if array[j] <= pivot:
            # If element smaller than pivot is found swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[right]) = (array[right], array[i + 1])

    # Return the position from where partition is done
    return i + 1


def quicksort(array, left, right):
    if left < right:
        pivot = partition(array, left, right)
        quicksort(array, left, pivot - 1)
        quicksort(array, pivot + 1, right)


if __name__ == '__main__':
    array = [10, 7, 8, 9, 1, 5]
    n = len(array)

    quicksort(array, 0, n - 1)
    print(array)
