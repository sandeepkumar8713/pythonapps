# https://leetcode.com/problems/split-array-largest-sum/
# https://leetcode.com/discuss/interview-question/350800/Google-or-Onsite-or-Chocolate-Sweetness
# Question : Given an array which consists of non-negative integers and an integer m, you can split the array into m
# non-empty continuous sub-arrays. Write an algorithm to minimize the largest sum among these m sub-arrays. We need
# minimum of the larger value.
# Same Question : Given an array chocolate of n non-negative integers, where the values are sweetness levels of
# the chocolate. You are also given a value k which denotes the number of friends you will share this chocolate
# with. Your friends are greedy so they will always take the highest sweetness chunk. Find out what is the maximum
# sweetness level you could get.
#
# It is similar to painter partition problem. But there output would be the larger value.
#
# Example : Input: chocolate = [6, 3, 2, 8, 7, 5], k = 3
# Output: 9
# Explanation: The values in array are sweetness level in each chunk of chocolate. Since k = 3, so you have to
# divide this array in 3 pieces, such that you would get maximum out of the minimum sweetness level. So, you should
# divide this array in
# [6, 3] -> 6 + 3 = 9
# [2, 8] -> 2 + 8 = 10
# [7, 5] -> 7 + 5 = 12
#
# Used : We are going to do binary search from 0 to maxInt, to check that each partition have minimum sum of mid.
#        Do this while low <= high and return high.
#        Logic : def splitArray(inpArr, k):
#        low = 0, high = sys.maxint
#        while low <= high:
#           mid = low + (high - low) / 2
#           if canSplit(inpArr, k, mid): low = mid + 1
#           else: high = mid - 1
#        maxTotal = [0]
#        canSplit(inpArr, k, high, maxTotal)
#        return high, maxTotal[0]
#        def canSplit(inpArr, k, minSum, maxTotal=None):
#           partitionCount = 0, total = 0
#           for i in range(len(inpArr)):
#               total += inpArr[i]
#               if total >= minSum:
#                   if maxTotal is not None:
#                       maxTotal[0] = max(maxTotal[0], total)
#                   total = 0
#                   partitionCount += 1
#           return partitionCount >= k
# Complexity : O(n * log (2^32))

import sys


def splitArray(inpArr, k):
    low = 0
    high = sys.maxint
    while low <= high:
        mid = low + (high - low) / 2
        # We try to increasing this mid as high as possible
        if canSplit(inpArr, k, mid):
            low = mid + 1
        else:
            high = mid - 1

    maxTotal = [0]
    canSplit(inpArr, k, high, maxTotal)
    return high, maxTotal[0]


def canSplit(inpArr, k, minSum, maxTotal=None):
    partitionCount = 0
    total = 0
    for i in range(len(inpArr)):
        total += inpArr[i]
        if total >= minSum:
            if maxTotal is not None:
                maxTotal[0] = max(maxTotal[0], total)
            total = 0
            partitionCount += 1
    return partitionCount >= k


if __name__ == "__main__":
    inpArr = [6, 3, 2, 8, 7, 5]
    k = 3
    print splitArray(inpArr, k)

    inpArr = [10, 20, 60, 50, 30, 40]
    k = 3
    print splitArray(inpArr, k)

    inpArr = [12, 34, 67, 90]
    k = 2
    print splitArray(inpArr, k)
