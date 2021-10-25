# https://www.geeksforgeeks.org/closest-numbers-list-unsorted-integers/
# Question : Given a list of distinct unsorted integers, find the pair of elements
# that have the smallest absolute difference between them? If there are multiple pairs,
# find them all.
#
# Examples: Input : arr[] = {10, 50, 12, 100}
# Output : (10, 12)
# The closest elements are 10 and 12
#
# Question Type : Easy
# Used : Sort the given array and find min diff between values by running a loop
# Complexity : O(n log n)

import sys


def closestPair(inpArr):
    inpArr.sort()

    minDiff = sys.maxsize
    for i in range(1, len(inpArr)):
        if inpArr[i] - inpArr[i-1] < minDiff:
            minDiff = inpArr[i] - inpArr[i-1]
            first = inpArr[i-1]
            second = inpArr[i]

    print(first, second)


if __name__ == "__main__":
    arr = [5, 4, 3, 2]
    closestPair(arr)
