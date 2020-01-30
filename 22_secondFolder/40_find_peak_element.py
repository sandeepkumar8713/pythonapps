# https://leetcode.com/problems/find-peak-element/
# Question : A peak element is an element that is greater than its neighbors.
# Given an input array nums, where nums[i] != nums[i+1], find a peak element and return its index.
# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
# You may imagine that nums[-1] = nums[n] = -infinite.
#
# Example : Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
#
# Question Type : Easy
# Used : Do binary search
#        Logic : def findPeakElement(nums):
#        l = 0
#        r = len(nums) - 1
#        while l < r:
#           mid = (l + r) / 2
#           if nums[mid] > nums[mid + 1]: r = mid
#           else: l = mid + 1
#        return l
# Complexity : O(log n)


def findPeakElement(nums):
    l = 0
    r = len(nums) - 1
    while l < r:
        mid = (l + r) / 2
        if nums[mid] > nums[mid + 1]:
            r = mid
        else:
            l = mid + 1
    return l


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    print(findPeakElement(nums))

    nums = [1, 2, 1, 3, 5, 6, 4]
    print(findPeakElement(nums))
