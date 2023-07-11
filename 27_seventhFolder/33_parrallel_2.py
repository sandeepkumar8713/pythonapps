# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/
# Question : Given a binary array nums, you should delete one element from it.
# Return the size of the longest non-empty subarray containing only 1's in the
# resulting array. Return 0 if there is no such subarray.
#
# Question Type : Easy
# Used : Loop through the given array. While doing so keep count of previous and current 1's found
#        b/w each zero. Find max sum of previous and current.
# Logic: for item in nums:
#           if item == 0:
#               zero_found = True
#               if prev + curr > max_value:
#                   max_value = prev + curr
#               prev = curr
#               curr = 0
#           else:
#               curr += 1
#        if zero_found is False:
#           return curr - 1
#        if prev + curr > max_value:
#           max_value = prev + curr
#        return max_value
# Complexity : O(n)


def longestSubarray(nums):
    max_value = 0
    curr = 0
    prev = 0
    zero_found = False
    for item in nums:
        if item == 0:
            zero_found = True
            if prev + curr > max_value:
                max_value = prev + curr
            prev = curr
            curr = 0
        else:
            curr += 1

    if zero_found is False:
        return curr - 1

    if prev + curr > max_value:
        max_value = prev + curr

    return max_value


if __name__ == "__main__":
    nums = [1, 1, 0, 1]
    print(longestSubarray(nums))

    nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
    print(longestSubarray(nums))

    nums = [1, 1, 1]
    print(longestSubarray(nums))
