# https://leetcode.com/problems/partition-equal-subset-sum/
# Question : Given a non-empty array nums containing only positive integers, find if the
# array can be partitioned into two subsets such that the sum of elements in both
# subsets is equal.
#
# Example : Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11]
#
# Question Type : Generic
# Used : Calculate sum of array ele and divide by 2. This is our target.
#        Do DP to find if this target can be achieved for choosing ele from array.
#        This similar to knapsack problem.
# Logic: target = total_sum // 2
#        dp = []
#        for i in range(n + 1):
#           dp.append([False] * (target + 1))
#        for i in range(n + 1):
#           dp[i][0] = True
#        for j in range(target + 1):
#           dp[0][j] = False
#        dp[0][0] = True
#        for i in range(1, n + 1):
#           for j in range(1, target + 1):
#               if j >= inpArr[i - 1]:
#                   dp[i][j] = dp[i - 1][j] or dp[i - 1][j - inpArr[i - 1]]
#              else:
#                   dp[i][j] = dp[i - 1][j]
#        return dp[n][target]
# Complexity : O(n)


def canPartition(inpArr):
    n = len(inpArr)
    total_sum = sum(inpArr)

    if total_sum % 2 == 1:
        return False

    target = total_sum // 2

    dp = []
    for i in range(n + 1):
        dp.append([False] * (target + 1))

    # We can always form a sum j = 0 by not including any number in the subset
    for i in range(n + 1):
        dp[i][0] = True

    # We can never form any sum 'j' with just 0 in our subset
    for j in range(target + 1):
        dp[0][j] = False

    dp[0][0] = True

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if j >= inpArr[i - 1]:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - inpArr[i - 1]]

            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][target]


if __name__ == "__main__":
    nums = [1, 5, 11, 5]
    print(canPartition(nums))
