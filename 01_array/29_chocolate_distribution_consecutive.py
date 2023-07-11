# https://www.geeksforgeeks.org/maximum-number-chocolates-distributed-equally-among-k-students/
# https://leetcode.com/problems/maximum-average-subarray-i/
# Question : The problem is to find maximum sum sub-array divisible by k and then return (sum / k).
# Given n boxes containing some chocolates arranged in a row. There are k number of students.
# The problem is to distribute maximum number of chocolates equally among k students by selecting
# a consecutive sequence of boxes from the given lot. Consider the boxes are arranged in a row with
# numbers from 1 to n from left to right. We have to select a group of boxes which are in consecutive
# order that could provide maximum number of chocolates equally to all the k students. An array arr[]
# is given representing the row arrangement of the boxes and arr[i]
# represents number of chocolates in that box at position 'i'.
#
# Input : arr[] = {2, 7, 6, 1, 4, 5}, k = 3
# Output : 6
# The sub-array is {7, 6, 1, 4} with sum 18.
# Equal distribution of 18 chocolates among 3 students is 6.
# Note that the selected boxes are in consecutive order with indexes {1, 2, 3, 4}.
#
# Question Type : Generic
# Used : Maintain a cumulative Sum Array for input array. Maintain a dict of remainders.
#        (Keep in mind that over a cumulative sum array, if the reminder of two elements
#        are same, then sum b/w them is divisible by k)
#        Run a loop for i : 0 to n-1. Calculate reminder: curr_rem = cumulativeSum[i] % k
#        Three Conditions :
#        1. if currRem is 0. update maxSum.
#        2. else if currRem is not in dict. Insert in dict.
#        3. if currRem is in dict. Check for mentioned diff and update maxSum if required.
#        return maxSum / k
# Logic: for i in range(n):
#        curr_rem = cumulativeSum[i] % k
#        if curr_rem == 0 and maxSum < cumulativeSum[i]:
#           maxSum = cumulativeSum[i]
#        elif not curr_rem in remDict:
#           remDict[curr_rem] = i
#        elif maxSum < cumulativeSum[i] - cumulativeSum[remDict[curr_rem]]:
#           maxSum = cumulativeSum[i] - cumulativeSum[remDict[curr_rem]]
#        return maxSum // k
# Complexity : O(n)


def maxNumOfChocolates(arr, n, k):
    remDict = {}
    curr_rem = 0
    maxSum = 0

    cumulativeSum = [0] * n
    cumulativeSum[0] = arr[0]

    for i in range(1, n):
        cumulativeSum[i] = cumulativeSum[i - 1] + arr[i]

    for i in range(n):
        curr_rem = cumulativeSum[i] % k

        if curr_rem == 0 and maxSum < cumulativeSum[i]:
            maxSum = cumulativeSum[i]
        elif not curr_rem in remDict:
            remDict[curr_rem] = i
        elif maxSum < cumulativeSum[i] - cumulativeSum[remDict[curr_rem]]:
            maxSum = cumulativeSum[i] - cumulativeSum[remDict[curr_rem]]

    return maxSum // k


if __name__ == "__main__":
    arr = [2, 7, 6, 1, 4, 5]
    n = len(arr)
    k = 3
    print("Maximum number of chocolates: ", maxNumOfChocolates(arr, n, k))
