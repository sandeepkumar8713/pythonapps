# https://leetcode.com/problems/wiggle-subsequence/
# Question :  Wiggle sequence is a sequence where the differences between successive numbers
# strictly alternate between positive and negative. The first difference (if one exists) may
# be either positive or negative. A sequence with one element and a sequence with two non-equal
# elements are trivially wiggle sequences.
# For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3)
# alternate between positive and negative.
# In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences. The first is not
# because its first two differences are positive, and the second is not because its last difference
# is zero.
# A subsequence is obtained by deleting some elements (possibly zero) from the original sequence,
# leaving the remaining elements in their original order.
# Given an integer array nums, return the length of the longest wiggle subsequence of nums.
#
# Question Type : Easy
# Used : We have to count number of peaks and valley.
#        When current is increasing, set its value as decreasing + 1.
#        And do vice versa
# Logic: def wiggle_max_length(nums):
#        inc = 1, dec = 1
#        for i in range(1, len(nums)):
#           if nums[i - 1] < nums[i]:
#               inc = dec + 1
#           elif nums[i] < nums[i - 1]:
#               dec = inc + 1
#        res = max(inc, dec)
#        return res
# Complexity : O(n)

def wiggle_max_length(nums):
    inc = 1
    dec = 1
    for i in range(1, len(nums)):
        if nums[i - 1] < nums[i]:
            inc = dec + 1
        elif nums[i] < nums[i - 1]:
            dec = inc + 1
    res = max(inc, dec)
    return res


if __name__ == "__main__":
    nums = [1, 7, 4, 9, 2, 5]
    print(wiggle_max_length(nums))
