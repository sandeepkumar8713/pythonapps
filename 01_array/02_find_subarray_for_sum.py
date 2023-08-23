# https://leetcode.com/problems/subarray-sum-equals-k/
# Question : Given an array of integers nums and an integer k, return the total number of subarrays whose sum
# equals to k.
# Similar : Given an unsorted array of integers, find a subarray which adds to a given number.
# If there are more than one sub arrays with sum as the given number, print any of them.
#
# Question Type : Generic
# Used : Do cumulative sum over the array and keep saving in dict as cumuSave and index.
#        Now while looping check if difference of current cumulative sum and target sum
# Logic: c_sum = 0
#        for i in range(n):
#           c_sum += arr[i]
#           if c_sum == targetSum: res.append((0, i))
#           diff = c_sum - targetSum
#           if diff in cumuSumMap:
#               for index in cumuSumMap[diff]:
#                   res.append((index + 1, i))
#           cumuSumMap[c_sum].append(i)
#        return res
# Complexity : 0(n)

from collections import defaultdict


def subArraySum(arr, targetSum):
    n = len(arr)
    cumuSum = [0] * n
    cumuSumMap = defaultdict(list)
    res = []

    c_sum = 0
    for i in range(n):
        c_sum += arr[i]
        if c_sum == targetSum:
            res.append((0, i))

        diff = c_sum - targetSum
        if diff in cumuSumMap:
            for index in cumuSumMap[diff]:
                res.append((index + 1, i))

        # Note that we only need to check prev index, so we are updating index while processing for desired range.
        cumuSumMap[c_sum].append(i)

    return res


if __name__ == "__main__":
    arr = [10, 2, -2, -20, 10]
    targetSum = -10
    print(subArraySum(arr, targetSum))

    arr = [1, 2, 3, 7, 5]
    targetSum = 12
    print(subArraySum(arr, targetSum))

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    targetSum = 15
    print(subArraySum(arr, targetSum))

    arr = [9, 4, 20, 3, 10, 5]
    targetSum = 33
    print(subArraySum(arr, targetSum))
