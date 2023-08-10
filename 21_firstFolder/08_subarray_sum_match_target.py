# https://www.geeksforgeeks.org/minimum-length-subarray-sum-greater-given-value/
# Similar : https://leetcode.com/problems/minimum-size-subarray-sum/
# Question : Given an array of integers and a number x, find the smallest sub array with sum greater
# than the given value.
#
# Question Type : Generic
# Used : Sliding window problem. Keep adding the elements from the start until the sum is equal to
#        target. Now start removing elements from start until sum is still equal to target. Update
#        the minimum length. Repeat the above process till end.
# Logic: smallestSubWithSum(arr,x):
#        n = len(arr), currSum = 0, minLen = n+1
#        start = 0, end = 0
#        while end < n:
#           while currSum <= x and end < n:
#               if currSum <= 0 and x > 0:
#                   start = end
#                   currSum = 0
#               currSum += arr[end]
#               end += 1
#           while currSum > x and start < n:
#               if end - start < minLen:
#                   minLen = end - start
#               currSum -= arr[start]
#               start += 1
#        return minLen
# Complexity : O(n)


def smallestSubWithSum(arr,x):
    n = len(arr)
    currSum = 0
    minLen = n+1

    start = 0
    end = 0
    while end < n:
        while currSum <= x and end < n:
            #  Ignore subarrays with negative sum if x is positive.
            if currSum <= 0 and x > 0:
                start = end
                currSum = 0

            currSum += arr[end]
            end += 1

        while currSum > x and start < n:
            if end - start < minLen:
                minLen = end - start
            # remove starting elements.
            currSum -= arr[start]
            start += 1

    return minLen


if __name__ == "__main__":
    arr = [- 8, 1, 4, 2, -6]
    x = 6
    print("Smallest sub array length :", smallestSubWithSum(arr, x))

