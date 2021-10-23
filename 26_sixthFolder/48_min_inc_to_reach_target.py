# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/
# Question : Given an array of positive integers target and an array initial of same size with
# all zeros. Return the minimum number of operations to form a target array from initial if
# you are allowed to do the following operation: Choose any subarray from initial and
# increment each value by one. The answer is guaranteed to fit within the range of a
# 32-bit signed integer.
#
# Example : Input: target = [3,1,1,2]
# Output: 4
# Explanation: (initial)[0,0,0,0] -> [1,1,1,1] -> [1,1,1,2] -> [2,1,1,2] -> [3,1,1,2] (target).
#
# Question Type : Generic
# Used : Since we increment ele only by 1,ans is dependent on diff of max and min elements.
#        Initialize the ans with first ele.
#        Loop over the remaining ele, if the diff b/w adjacent elements is more than 0 add to ans.
#        Logic :
#        def minNumberOperations(target):
#        diffSum = target[0]
#        for i in range(1, len(target)):
#           diffSum += max(0, target[i] - target[i - 1])
#        return diffSum
# Complexity : O(n)


def minNumberOperations(target):
    diffSum = target[0]
    for i in range(1, len(target)):
        diffSum += max(0, target[i] - target[i - 1])

    return diffSum


if __name__ == "__main__":
    target = [1, 2, 3, 2, 1]
    print(minNumberOperations(target))

    target = [3, 1, 1, 2]
    print(minNumberOperations(target))

    target = [3, 1, 5, 4, 2]
    print(minNumberOperations(target))

    target = [1, 1, 1, 1]
    print(minNumberOperations(target))
