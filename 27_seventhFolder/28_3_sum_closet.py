# https://leetcode.com/problems/3sum-closest/
# Qeustion : Given an integer array nums of length n and an integer target,
# find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers. You may assume that each input
# would have exactly one solution.
#
# Example : Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#
# Question Type : Generic
# Used : Sort the given input array.
#        Run a loop over the array.
#           Fix the first element, for remaining elements choose leftmost and rightmost.
#           Run a loop to find the closet sum.
#           Now fix the second element, and repeat the above process.
# Complexity : O(n log n) + O(n^2)

import sys


def find_closest(nums, target):
    closest = sys.maxsize
    nums.sort()
    for i in range(len(nums)-2):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]
            if abs(target - curr_sum) < abs(target - closest):
                closest = curr_sum
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
    return closest


if __name__ == "__main__":
    nums = [-1, 2, 1, -4]
    target = 1
    print(find_closest(nums, target))

    nums = [0, 0, 0]
    target = 1
    print(find_closest(nums, target))
