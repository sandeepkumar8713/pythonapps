# https://leetcode.com/problems/maximum-subarray/
# Question : Given an integer array nums, find the contiguous subarray
# (containing at least one number) which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.
#
# Question Type : Easy
# Used : We will use Kadane algo here.
#        Logic :
#        max_ending_here = inpArr[0]
#        for i in range(1, len(inpArr)):
#           max_ending_here = max_ending_here + inpArr[i]
#           if max_ending_here < 0:
#               max_ending_here = 0
#           if max_so_far < max_ending_here:
#               max_so_far = max_ending_here
# Complexity : O(n)

import sys


def kadaneAlgo(inpArr):
    max_so_far = -sys.maxsize

    max_ending_here = inpArr[0]
    for i in range(1, len(inpArr)):
        max_ending_here = max_ending_here + inpArr[i]
        if max_ending_here < 0:
            max_ending_here = 0

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

    return max_so_far


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(kadaneAlgo(nums))
