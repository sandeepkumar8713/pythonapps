# https://leetcode.com/problems/maximum-alternating-subarray-sum/
# https://leetcode.ca/2021-10-20-2036-Maximum-Alternating-Subarray-Sum/
# A subarray of a 0-indexed integer array is a contiguous non-empty sequence of elements within
# an array. The alternating subarray sum of a subarray that ranges from index i to j
# (inclusive, 0 <= i <= j < nums.length) is nums[i] - nums[i+1] + nums[i+2] - ... +/- nums[j].
# Given a 0-indexed integer array nums, return the maximum alternating subarray sum of any
# subarray of nums.
#
# Input: nums = [2,2,2,2,2]
# Output: 2
# Explanation:
# The subarrays [2], [2,2,2], and [2,2,2,2,2] have the largest alternating subarray sum.
# The alternating subarray sum of [2] is 2.
# The alternating subarray sum of [2,2,2] is 2 - 2 + 2 = 2.
# The alternating subarray sum of [2,2,2,2,2] is 2 - 2 + 2 - 2 + 2 = 2.
#
# Question Type : ShouldSee
# Used : Dp with sub problem
#        Make a 2d array DP. Where dp[i][j] denotes substring from i and j having max sum
# Logic: for i in range(n):
#           dp[i][i] = inp_arr[i]
#        max_res = max(inp_arr)
#        for i in range(n - 1):
#           for j in range(i, n - 1):
#               if ((j - i) % 2) == 0:
#                   dp[i][j + 1] = dp[i][j] - inp_arr[j + 1]
#               else:
#                   dp[i][j + 1] = dp[i][j] + inp_arr[j + 1]
#               max_res = max(max_res, dp[i][j + 1])
#        return max_res
# Complexity : O(n^2)

def find_max_subarray_sum(inp_arr):
    n = len(inp_arr)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = inp_arr[i]

    max_res = max(inp_arr)
    for i in range(n - 1):
        for j in range(i, n - 1):
            if ((j - i) % 2) == 0:
                dp[i][j + 1] = dp[i][j] - inp_arr[j + 1]
            else:
                dp[i][j + 1] = dp[i][j] + inp_arr[j + 1]
            max_res = max(max_res, dp[i][j + 1])

    return max_res


if __name__ == "__main__":
    inp_arr = [3, -1, 1, 2]
    print(find_max_subarray_sum(inp_arr))

    inp_arr = [2, 2, 2, 2, 2]
    print(find_max_subarray_sum(inp_arr))
