# https://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/
# Question : Given a set of integers, the task is to divide it into two sets S1 and S2 such
# that the absolute difference between their sums is minimum.
#
# Input:  arr[] = {1, 6, 11, 5}
# Output: 1
# Explanation:
# Subset1 = {1, 5, 6}, sum of Subset1 = 12
# Subset2 = {11}, sum of Subset2 = 11
#
# Question Type : Generic
# Used : (Knapsack) Let us suppose total sum is 100, so ideal division would be 50-50. If not possible
#        49-51, 48-52 and so on ... So to tell this, we should have array of boolean from 0
#        to 100, specifying whether it is possible to make those sums using the given input
#        elements by including or excluding.
#        To get the above mentioned array we have to make a memory table dp :
#        size (n+1) * (totalSum).
#        Mark all as false. Where dp[i][j] specify whether it is possible
#        to make sum j using i elements. Set first row as false. Set first column as true.
#        Loop over the elements of dp.
#           To exclude current element : dp[i][j] = dp[i - 1][j]. To include current element,
#           check if current element is less than or equal to j(sum), if yes :
#               dp[i][j] |= dp[i - 1][j - arr[i - 1]]
#        After the loop we will have dp[n][totalSum] array. Loop over this array from totalSum/2 to 0.
#           If dp[n][j] is true then set diff = (totalSum - 2 * j) and break.
#        return diff
# Logic: dp = []
#        for i in range(n+1):
#           dp.append([False] * (totalSum + 1))
#        for j in range(1, totalSum + 1):
#           dp[0][j] = False
#        for i in range(0, n + 1):
#           dp[i][0] = True
#        for i in range(1, n+1):
#           for j in range(1, totalSum):
#               dp[i][j] = dp[i - 1][j]
#               if arr[i - 1] <= j:
#                   dp[i][j] |= dp[i - 1][j - arr[i - 1]]
#        for j in range(totalSum // 2, -1, -1):
#           if dp[n][j]:
#               diff = totalSum - 2 * j
#               break
#        return diff
# Complexity : O(n * totalSum) same amount of auxiliary space.

import sys


def findMinDiff(arr):
    n = len(arr)
    totalSum = sum(arr)

    dp = []
    for i in range(n+1):
        dp.append([False] * (totalSum + 1))

    #  With 0 elements, no other sum except 0 is possible
    for j in range(1, totalSum + 1):
        dp[0][j] = False

    # 0 sum is possible with all elements
    for i in range(0, n + 1):
        dp[i][0] = True

    for i in range(1, n+1):
        for j in range(1, totalSum):
            # If i'th element is excluded
            dp[i][j] = dp[i - 1][j]

            # If i'th element is included
            if arr[i - 1] <= j:
                dp[i][j] |= dp[i - 1][j - arr[i - 1]]

    diff = sys.maxsize

    for j in range(totalSum // 2, -1, -1):
        if dp[n][j]:
            diff = totalSum - 2 * j
            break

    return diff


if __name__ == "__main__":
    arr = [1, 6, 11, 5]
    # arr = [3, 1, 4, 2, 2, 1]
    print("Minimum difference between 2 sets:", findMinDiff(arr))
