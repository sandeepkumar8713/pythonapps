# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/
# Question : Given an integer array nums and an integer k, find three non-overlapping subarrays
# of length k with maximum sum and return them. Return the result as a list of indices representing
# the starting position of each interval (0-indexed). If there are multiple answers, return the
# lexicographically smallest one.
#
# Example : Input: nums = [1,2,1,2,6,7,5,1], k = 2
# Output: [0,3,5]
# Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
# We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
#
# Question Type : OddOne
# Used : We use DP, where key is tuple (i,subArrCount) i : 0 to n-1, subArrCount : 0 to 3
#        We do DFS here, keep saving the sub solution in dp.
#        DFS return the index list and its corresponding ele sum for given i and subArrCount.
#        At each iteration, we have 2 options
#        1. select current i and i + k elements.
#        2. Skip current i, call dfs for i + 1 index
#        We should compare sum returned by these 2 and update max in dp.
#        Logic :
#        dfs(dp, prefix_sum, i, subArrCount):
#        n = len(prefix_sum) - 1
#        if subArrCount == 0: return [], 0
#        if n - i < k * subArrCount: return None, -float("inf")
#        if (i, subArrCount) in dp: return dp[(i, subArrCount)]
#        indexInclude, cnt_in_sum = dfs(dp, prefix_sum, i + k, subArrCount - 1)
#        indexInclude, cnt_in_sum = [i] + indexInclude, cnt_in_sum + prefix_sum[i + k] - prefix_sum[i]
#        exclude, cnt_ex_sum = dfs(dp, prefix_sum, i + 1, subArrCount)
#        if cnt_in_sum >= cnt_ex_sum:
#           dp[(i, subArrCount)] = indexInclude, cnt_in_sum
#        else:
#           dp[(i, subArrCount)] = exclude, cnt_ex_sum
#        return dp[(i, subArrCount)]
#
#        res, resSum = dfs(dp, prefix_sum, 0, 3)
# Complexity : O(3 * n) where n is number of ele in input array.


def get_prefix_sum(inpArr):
    n = len(inpArr)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + inpArr[i]
    return prefix_sum


def dfs(dp, prefix_sum, i, subArrCount):  # (i: index in nums, subArrCount: numbers of sub arrays)
    n = len(prefix_sum) - 1

    if subArrCount == 0:
        return [], 0

    # Not feasible
    if n - i < k * subArrCount:
        return None, -float("inf")

    if (i, subArrCount) in dp:
        return dp[(i, subArrCount)]

    # 2 options: take k elements or skip current value
    indexInclude, cnt_in_sum = dfs(dp, prefix_sum, i + k, subArrCount - 1)  # take k elements

    # build array and sum during backtracking
    indexInclude, cnt_in_sum = [i] + indexInclude, cnt_in_sum + prefix_sum[i + k] - prefix_sum[i]

    exclude, cnt_ex_sum = dfs(dp, prefix_sum, i + 1, subArrCount)  # skip current value
    if cnt_in_sum >= cnt_ex_sum:  # to obtain the max sum.
        dp[(i, subArrCount)] = indexInclude, cnt_in_sum
    else:
        dp[(i, subArrCount)] = exclude, cnt_ex_sum

    return dp[(i, subArrCount)]


def maxSumOfThreeSubarrays(nums, k):
    dp = {}
    prefix_sum = get_prefix_sum(nums)
    res, resSum = dfs(dp, prefix_sum, 0, 3)
    return res


if __name__ == "__main__":
    nums = [1, 2, 1, 2, 6, 7, 5, 1]
    k = 2
    print(maxSumOfThreeSubarrays(nums, k))
