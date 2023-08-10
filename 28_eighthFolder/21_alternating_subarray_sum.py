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
