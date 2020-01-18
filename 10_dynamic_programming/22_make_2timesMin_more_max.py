# https://www.geeksforgeeks.org/remove-minimum-elements-either-side-2min-max/
# Question : Given an unsorted array, trim the array such that twice of minimum is greater than maximum in the
# trimmed array. Elements should be removed either end of the array. Number of removals should be minimum.
#
# arr[] = {4, 5, 100, 9, 10, 11, 12, 15, 200}
# Output: 4
# We need to remove 4 elements (4, 5, 100, 200) so that 2*min becomes more than max.
#
# Used : initialize longestStart = -1 longestEnd = 0
#        The idea is to take sub array of variable length, check if it satisfies the condition and take the longest
#           sub array length.
#        Run two loops i : 0 to n-1 and j : i to n-1. For array[i to n] keep maintaining min and max value and keep
#           checking this condition if 2 * minVal < maxVal : break from inner loop.
#           (If the property is violated, then no point to continue for a bigger array)
#           Compare diff b/w i & j and longestStart & longestEnd. Update if required
#        After the loop, If condition not satisfied at all, if longestStart == -1: return n
#        Else return number of elements to be removed to satisfy : return n - (longestEnd - longestStart + 1)
# Complexity : O(n^2)

import sys


def minRemovalsDP(inpArr):
    longestStart = -1
    longestEnd = 0
    n = len(inpArr)

    for i in range(n):
        minVal = sys.maxint
        maxVal = -sys.maxint
        for j in range(i, n):
            if inpArr[j] > maxVal:
                maxVal = inpArr[j]
            if inpArr[j] < minVal:
                minVal = inpArr[j]

            # If the property is violated, then no point to continue for a bigger array
            if 2 * minVal < maxVal:
                break

            if j - i > longestEnd - longestStart or longestStart == -1:
                longestStart = i
                longestEnd = j

    # If not even a single element follow the property then return n
    if longestStart == -1:
        return n

    # print inpArr[longestStart:longestEnd+1]
    return n - (longestEnd - longestStart + 1)


if __name__ == "__main__":
    inpArr = [4, 5, 100, 9, 10, 11, 12, 15, 200]
    # inpArr = [4, 7, 5, 6]
    # inpArr = [20, 7, 5, 6]
    # inpArr = [20, 4, 1, 3]
    print minRemovalsDP(inpArr)
