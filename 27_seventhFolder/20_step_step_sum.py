# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/
# Question : Given an array of integers nums, you start with an initial positive value
# startValue. In each iteration, you calculate the step by step sum of startValue plus
# elements in nums (from left to right). Return the minimum positive value of startValue
# such that the step by step sum is never less than 1.
#
# Example : Input: nums = [-3,2,-3,4,2]
# Output: 5
# Explanation: If you choose startValue = 4, in the third iteration your step by step sum
# is less than 1. step by step sum
# startValue = 4 | startValue = 5 | nums
#   (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
#   (1 +2 ) = 3  | (2 +2 ) = 4    |   2
#   (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
#   (0 +4 ) = 4  | (1 +4 ) = 5    |   4
#   (4 +2 ) = 6  | (5 +2 ) = 7    |   2
#
# Question Type : Easy
# Used : Run a loop over the given input array. Maintain a runningSum and a minVal check.
#        To find minimum sum in array.
#        After the loop if minVal is positive return 1 else return absoulte(minVal) + 1
#        Logic :
#        for ele in inpArr:
#           runningSum += ele
#           minVal = min(minVal, runningSum)
#        if minVal > 1:
#           return minVal
#        return abs(minVal) + 1
# Complexity : O(n)


import sys


def minStartValue(inpArr):
    minVal = sys.maxsize
    runningSum = 0
    for ele in inpArr:
        runningSum += ele
        minVal = min(minVal, runningSum)

    if minVal > 1:
        return minVal

    return abs(minVal) + 1


if __name__ == "__main__":
    nums = [-3, 2, -3, 4, 2]
    print(minStartValue(nums))
