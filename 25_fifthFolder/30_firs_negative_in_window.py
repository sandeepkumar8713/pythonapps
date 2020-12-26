# https://www.geeksforgeeks.org/first-negative-integer-every-window-size-k/
# Question : Given an array and a positive integer k, find the first negative integer for each window(contiguous
# subarray) of size k. If a window does not contain a negative integer, then print 0 for that window.
#
# Question Type : ShouldSee
# Used : Start firstNegativeIndex as 0.
#        Loop over the give inpArr.
#        If i is outside the window or element is positive increment firstNegativeIndex.
#        If ele at firstNegativeIndex is negative print element else print 0.
#        printFirstNegativeInteger(arr, k):
#        firstNegativeIndex = 0
#        for i in range(k - 1, len(arr)):
#        while firstNegativeIndex < i and (firstNegativeIndex <= i - k or arr[firstNegativeIndex] > 0):
#           firstNegativeIndex += 1
#        if arr[firstNegativeIndex] < 0:
#           firstNegativeElement = arr[firstNegativeIndex]
#        else:
#           firstNegativeElement = 0
#        print(firstNegativeElement, end=' ')
# Complexity : O(n)


def printFirstNegativeInteger(arr, k):
    firstNegativeIndex = 0

    for i in range(k - 1, len(arr)):

        # skip out of window and positive elements
        while firstNegativeIndex < i and (firstNegativeIndex <= i - k or arr[firstNegativeIndex] > 0):
            firstNegativeIndex += 1

        # check if a negative element is found, otherwise use 0
        if arr[firstNegativeIndex] < 0:
            firstNegativeElement = arr[firstNegativeIndex]
        else:
            firstNegativeElement = 0
        print(firstNegativeElement, end=' ')


if __name__ == "__main__":
    arr = [12, -1, -7, 8, -15, 30, 16, 28]
    k = 3
    printFirstNegativeInteger(arr, k)
