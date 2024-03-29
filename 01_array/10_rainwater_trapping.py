# CTCI : Q17_21_Volume_of_Histogram
# https://leetcode.com/problems/trapping-rain-water/
# Question : Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it is able to trap after raining.
#
# Input: arr[] = {3, 0, 0, 2, 0, 4}
# Output: 10
# Structure is like below
#      |
# |    |
# |  | |
# |__|_|
#
# Question Type : ShouldSee
# Used : Make two array of left max and right max, now loop through with min of left &
#        right and subtract current.
# Logic: def findWater(arr, n):
#        left[0] = arr[0]
#        for i in range(1, n):
#           left[i] = max(left[i - 1], arr[i])
#        right[n - 1] = arr[n - 1]
#        for i in range(n - 2, 0, -1):
#           right[i] = max(right[i + 1], arr[i])
#        for i in range(0, n):
#           water += min(left[i], right[i]) - arr[i]
#        return water
# Complexity : O(n)


def findWater(arr, n):
    left = [0] * n
    right = [0] * n
    water = 0

    left[0] = arr[0]
    for i in range(1, n):
        left[i] = max(left[i - 1], arr[i])

    right[n - 1] = arr[n - 1]
    for i in range(n - 2, 0, -1):
        right[i] = max(right[i + 1], arr[i])

    for i in range(0, n):
        water += min(left[i], right[i]) - arr[i]

    return water


if __name__ == "__main__":
    arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    n = len(arr)
    print("Maximum water that can be accumulated is: %s" % findWater(arr, n))
