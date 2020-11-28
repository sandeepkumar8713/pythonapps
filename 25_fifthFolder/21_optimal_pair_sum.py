# https://leetcode.com/discuss/interview-question/373202
# Similar : 07_hashing/07_find_all_pair_for_sum
# Question : Given 2 lists a and b. Each element is a pair of integers where the first integer represents the
# unique id and the second integer represents a value. Your task is to find an element from a and an element form
# b such that the sum of their values is less or equal to target and as close to target as possible.
# Return a list of ids of selected elements. If no pair is possible, return an empty list.
#
# Example :
# Input: a = [[1, 2], [2, 4], [3, 6]]
# b = [[1, 2]]
# target = 7
# Output: [[2, 1]]
# Explanation:
# There are only three combinations [1, 1], [2, 1], and [3, 1], which have a total sum of 4, 6 and 8, respectively.
# Since 6 is the largest sum that does not exceed 7, [2, 1] is the optimal pair.
#
# Question Type : Easy
# Used : Loop over the smaller array, add elements to the dict along with its value.
#        Loop over the larger array, check if target - element is present in dict. Append in result if present.
#        Repeat the above loop if result list is empty with target - 1.
#        findAllPair(largerArr, hashDict, x, result, flipped):
#        for ele in largerArr:
#           if x - ele[1] in hashDict:
#               result.append([ele[0], hashDict[x - ele[1]]])
#
#        findOptimalPairs(arr1, arr2, target):
#        result = []
#        for x in range(target, minTarget - 1, -1):
#           if len(result) == 0:
#               findAllPair(largeArr, hashDict, x, result, flipped)
#           else:
#               break
#        result result
# Complexity : O(n) * O(target)

import sys


def findAllPair(largerArr, hashDict, x, result, flipped):
    for ele in largerArr:
        if x - ele[1] in hashDict:
            if flipped:
                result.append([ele[0], hashDict[x - ele[1]]])
            else:
                result.append([hashDict[x - ele[1]], ele[0]])


def getMinValue(inpArr):
    minVal = sys.maxsize
    for item in inpArr:
        if minVal > item[1]:
            minVal = item[1]
    return minVal


def findOptimalPairs(arr1, arr2, target):
    hashDict = dict()
    result = []
    flipped = False

    if len(arr1) <= len(arr2):
        smallArr = arr1
        largeArr = arr2
    else:
        smallArr = arr2
        largeArr = arr1
        flipped = True

    for ele in smallArr:
        hashDict[ele[1]] = ele[0]

    minTarget = getMinValue(arr1) + getMinValue(arr2)

    for x in range(target, minTarget - 1, -1):
        if len(result) == 0:
            findAllPair(largeArr, hashDict, x, result, flipped)
        else:
            break
    print(result)


if __name__ == "__main__":
    a = [[1, 2], [2, 4], [3, 6]]
    b = [[1, 2]]
    target = 70
    findOptimalPairs(a, b, target)

    a = [[1, 3], [2, 5], [3, 7], [4, 10]]
    b = [[1, 2], [2, 3], [3, 4], [4, 5]]
    target = 10
    findOptimalPairs(a, b, target)

    a = [[1, 8], [2, 15], [3, 9]]
    b = [[1, 8], [2, 11], [3, 12]]
    target = 20
    findOptimalPairs(a, b, target)

    a = [[1, 8], [2, 7], [3, 14]]
    b = [[1, 5], [2, 10], [3, 14]]
    target = 20
    findOptimalPairs(a, b, target)
