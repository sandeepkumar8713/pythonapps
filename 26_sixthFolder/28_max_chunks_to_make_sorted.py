# https://leetcode.com/problems/max-chunks-to-make-sorted-ii/
# Question : You are given an integer array arr. We split arr into some number of chunks (i.e., partitions),
# and individually sort each chunk. After concatenating them, the result should equal the sorted array.
# Return the largest number of chunks we can make to sort the array.
#
# Example : Input: arr = [2,1,3,4,4]
# Output: 4
# Explanation: We can split into two chunks, such as [2, 1], [3, 4, 4].
# However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks possible.
#
# Question Type : Generic
# Used : Make a right min array.
#        Now loop the given array, while doing so maintain left max also.
#        if left max is less than right min, increment count.
#        After the loop, return count
#        Logic :
#        cut, leftMax = 0, -1
#        for i in range(len(inpArr) - 1):
#           leftMax = max(leftMax, inpArr[i])
#           if leftMax <= right_min[i]: cut += 1
#        return cut + 1
# Complexity : O(n)

import sys


def maxChunksToSorted(inpArr):
    right_min = [sys.maxsize]

    for i in range(len(inpArr) - 1, 0, -1):
        right_min.append(min(inpArr[i], right_min[-1]))

    right_min.reverse()
    cut, leftMax = 0, -1

    for i in range(len(inpArr) - 1):
        leftMax = max(leftMax, inpArr[i])
        if leftMax <= right_min[i]:
            cut += 1

    return cut + 1


if __name__ == "__main__":
    arr = [2, 1, 3, 4, 4]
    print(maxChunksToSorted(arr))
