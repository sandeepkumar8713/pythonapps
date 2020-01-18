# https://leetcode.com/discuss/interview-question/352743/Google-or-Onsite-or-Binary-Searchable-Numbers
# Question : Binary search is a search algorithm usually used on a sorted sequence to quickly find an
# element with a given value. In this problem we will evaluate how binary search performs on data that isn't
# necessarily sorted. An element is said to be binary searchable if, regardless of how the pivot is chosen the
# algorithm returns true. In other words, the problems asks how many elements are larger than all elements to
# their left, and smaller than all elements to their right.
# Similar Question: given a unsorted array, give the count of elements which are already at correct position in sorted
# array.
#
# Example : Input: [1, 3, 2]
# Output: 1
# Explanation: However we choose the pivots, we will always find the number 1 when looking for it. This does
# not hold for 3 and 2.
#
# Example : Input: [2, 1, 3, 5, 4, 6]
# Output: 2
# Explanation: 3 and 6 are the numbers guaranteed to be found.
#
# Used : Run a loop over the input array. If the element is higher than max left and lower than min Right increase
#        the count.
#        Logic : def binarySearchable(inpArr):
#        n = len(inpArr), count = 0
#        maxLeft = [0] * n
#        maxLeft[0] = inpArr[0]
#        for i in range(1, n):
#           maxLeft[i] = max(maxLeft[i-1], inpArr[i])
#        minRight = sys.maxint
#        for i in range(n-1,-1,-1):
#           minRight = min(minRight, inpArr[i])
#           if inpArr[i] <= minRight and inpArr[i] >= maxLeft[i]:
#               count += 1
#        return count
# Complexity : O(n)

import sys


def binarySearchable(inpArr):
    n = len(inpArr)
    count = 0

    maxLeft = [0] * n
    maxLeft[0] = inpArr[0]
    for i in range(1, n):
        maxLeft[i] = max(maxLeft[i-1], inpArr[i])

    minRight = sys.maxint
    for i in range(n-1,-1,-1):
        minRight = min(minRight, inpArr[i])
        if inpArr[i] <= minRight and inpArr[i] >= maxLeft[i]:
            count += 1

    return count


if __name__ == "__main__":
    inpArr = [2, 1, 3, 5, 4, 6]
    print binarySearchable(inpArr)

    inpArr = [1, 2, 3, 4, 6]
    print binarySearchable(inpArr)

