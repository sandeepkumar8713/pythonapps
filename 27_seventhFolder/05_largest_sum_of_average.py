# https://leetcode.com/problems/largest-sum-of-averages/
# Question : You are given an integer array nums and an integer k. You can partition the
# array into at most k non-empty adjacent subarrays. The score of a partition is the sum
# of the averages of each subarray. Note that the partition must use every integer in nums,
# and that the score is not necessarily an integer. Return the maximum score you can achieve
# of all the possible partitions. Answers within 10-6 of the actual answer will be accepted.
#
# largestSum(a[1]..a[n]) = avg(a[1]) + largestSum(a[2]...a[n]) or
# 								   avg(a[1]+a[2]) + largestSum(a[3]..a[n]) or
# 								   avg(a[1]+a[2]+a[3]) + largestSum(a[4]..a[n]) or
# 									...
# 								   avg(a[1]+..+a[n]) + largestSum([])
#
#
# Question Type : ShouldSee
# Used : Loop over the given inputArr. At each index we try to make a partition from 0 to i,
#        Calculate avg and recur for remaining ele with k-1 partition.
#        Return ans which is max in loop.
#        Logic :
#        def find(idx, k):
#        nonlocal nums
#        if idx == len(nums): return 0
#        if k == 1:
#           return sum(nums[idx:]) / len(nums[idx:])
#        s = 0, cur = 0
#        for i in range(idx, len(nums)):
#           cur += nums[i]
#           s = max(s, cur / (i - idx + 1) + find(i + 1, k - 1))
#        return s
# Complexity : O(n*k)

from functools import lru_cache


def largestSumOfAverages(nums, k):
    @lru_cache
    def find(idx, k):
        nonlocal nums
        if idx == len(nums):
            return 0
        if k == 1:
            return sum(nums[idx:]) / len(nums[idx:])
        s = 0
        cur = 0
        # try each partition index, get the best sum
        for i in range(idx, len(nums)):
            cur += nums[i]
            s = max(s, cur / (i - idx + 1) + find(i + 1, k - 1))
        return s

    return find(0, k)


if __name__ == "__main__":
    nums = [9, 1, 2, 3, 9]
    k = 3
    print(largestSumOfAverages(nums, k))
