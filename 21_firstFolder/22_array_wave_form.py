# CTCI : Q10_11_Peaks_and_Valleys
# https://www.geeksforgeeks.org/sort-array-wave-form-2/
# Question : Given an unsorted array of integers, sort the array into a wave like array.
# Given an int array, arrange the elements in increasing decreasing order i.e.
# one element bigger than a smaller element then bigger and so on.
#
# Question Type : ShouldSee
# Used : Check only even condition for i-1 > i < i + 1; else swap
# Complexity : O(n)


def sortInWave(arr, n):
    for i in range(0, n, 2):
        # for i (only even), i-1 should be more and i+1 should be less, 8 6 7

        # If current even element is smaller than previous
        if i > 0 and arr[i - 1] > arr[i]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]

        # If current even element is smaller than next
        if i < n - 1 and arr[i] < arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]


if __name__ == "__main__":
    arr = [10, 90, 49, 2, 1, 5, 23]
    sortInWave(arr, len(arr))
    print(arr)
