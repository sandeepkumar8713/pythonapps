# https://leetcode.com/problems/arithmetic-slices-ii-subsequence/
# Similar : 23_thirdFolder/28_longest_arithmetic_progression.py
# Question : Given an integer array nums, return the number of all the arithmetic subsequences
# of nums. A sequence of numbers is called arithmetic if it consists of at least three elements
# and if the difference between any two consecutive elements is the same.
# For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are arithmetic sequences.
# For example, [1, 1, 2, 5, 7] is not an arithmetic sequence.
# A subsequence of an array is a sequence that can be formed by removing some elements
# (possibly none) of the array.
# For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].
#
# Question Type : Generic, Similar Added
# Used : DP with Box stacking
#        The main idea is to maintain a map of differences seen at each index. We iteratively
#        build the map for a new index i, by considering all elements to the left one-by-one.
#        For each pair of indices (i,j) and difference d = A[i]-A[j] considered, we check if
#        there was an existing chain at the index j with difference d already.
# Logic : res = 0
#         dp = [defaultdict(int) for _ in range(len(nums))]
#         for i in range(1, len(nums)):
#           for j in range(i):
#               diff = nums[i] - nums[j]
#               dp[i][diff] += 1
#               if diff in dp[j]:
#                   dp[i][diff] += dp[j][diff]
#                   res += dp[j][diff]
#         return res
# Complexity : O(n*m)

from collections import defaultdict


def number_of_arithmetic_slices(nums) -> int:
    res = 0
    dp = [defaultdict(int) for _ in range(len(nums))]

    for i in range(1, len(nums)):
        for j in range(i):
            diff = nums[i] - nums[j]
            dp[i][diff] += 1
            # 3 elements formed here
            if diff in dp[j]:
                dp[i][diff] += dp[j][diff]
                res += dp[j][diff]
    return res


if __name__ == "__main__":
    inpArr = [1, 3, 5, 7, 9]
    print(number_of_arithmetic_slices(inpArr))

    inpArr = [7, 7, 7, 7]
    print(number_of_arithmetic_slices(inpArr))

    inpArr = [3, -1, -5, -9]
    print(number_of_arithmetic_slices(inpArr))
