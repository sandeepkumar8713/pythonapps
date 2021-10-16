# https://leetcode.com/problems/largest-divisible-subset/
# Question : Given a set of distinct positive integers nums, return the largest subset answer such that
# every pair (answer[i], answer[j]) of elements in this subset satisfies:
# answer[i] % answer[j] == 0, or answer[j] % answer[i] == 0
# If there are multiple solutions, return any of them.
#
# Example : Input: nums = [1,2,4,8]
# Output: [1,2,4,8]
#
# Question Type : ShouldSee
# Used : Initialize a dp array as dp = [1] * n. Where dp[i] represents subset max count from 0 to i.
#        Sort the given array. Run 2 loops to iterate over each possible pair
#        Check if divisibility constraint holds on the pair, if yes then check if dp value
#        can be update by merging with past values (like box stacking). Also keep track of
#        path(i.e previous index used to merge).
#        Also keep track of max dp value reached yet and its corresponding index.
#        After the loop, trace back the path from the index which had max dp value.
#        While tracing the path we will get our elements of answer.
#        Logic :
#        nums.sort(), dp = [1] * n
#        path = [-1] * n, iMax = 0, ans = []
#        for i in range(1, n):
#           for j in range(i):
#               if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
#                   dp[i] = dp[j] + 1
#                   path[i] = j
#           if dp[iMax] < dp[i]:
#               iMax = i
#        while iMax >= 0:
#           ans.append(nums[iMax])
#           iMax = path[iMax]
#        return ans[::-1]
# Complexity : O(n^2)


def largestDivisibleSubset(nums):
    nums.sort()
    n = len(nums)
    dp = [1] * n
    path = [-1] * n
    iMax = 0

    for i in range(1, n):
        for j in range(i):
            if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                path[i] = j

        if dp[iMax] < dp[i]:
            iMax = i

    ans = []
    while iMax >= 0:
        ans.append(nums[iMax])
        iMax = path[iMax]
    return ans[::-1]


if __name__ == "__main__":
    nums = [1, 2, 4, 8]
    print(largestDivisibleSubset(nums))

    nums = [1, 2, 3]
    print(largestDivisibleSubset(nums))
