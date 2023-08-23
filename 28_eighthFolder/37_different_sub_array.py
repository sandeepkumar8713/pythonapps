# https://leetcode.com/problems/subarrays-with-k-different-integers/
# Question : Given an integer array nums and an integer k, return the number of good subarrays of nums.
# A good array is an array where the number of different integers in that array is exactly k.
# For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
# A subarray is a contiguous part of an array.
#
# Example : Input: nums = [1,2,1,2,3], k = 2
# Output: 7
# Explanation: Subarrays formed with exactly 2 different integers:
# [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
#
# Question Type : OddOne
# TODO :: add code

if __name__ == "__main__":
    nums = [1, 2, 1, 2, 3]
    k = 2
