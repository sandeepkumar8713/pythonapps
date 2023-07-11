# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/
# Questions : You are given an integer array nums and two integers minK and maxK.
# A fixed-bound subarray of nums is a subarray that satisfies the following conditions:
#     The minimum value in the subarray is equal to minK.
#     The maximum value in the subarray is equal to maxK.
# Return the number of fixed-bound subarrays. A subarray is a contiguous part of an array.
#
# Example : Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
# Output: 2
# Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].
#
# Question Type : Generic
# Used : Loop over the given array.
#           If element is not in range, set start at this index.
#           Find a pair of minK and maxK.
#           The diff b/w start and min index of minK and maxK would give the count of subarray possible.
#        return sum of count.
# Complexity : O(n) n is node count and m is edge count


def countSubarrays(nums, minK, maxK):
    ans = 0
    start = -1
    prevMinKIndex = -1
    prevMaxKIndex = -1

    for i, num in enumerate(nums):
        if num < minK or num > maxK:
            j = i
        if num == minK:
            prevMinKIndex = i
        if num == maxK:
            prevMaxKIndex = i

        ans += max(0, min(prevMinKIndex, prevMaxKIndex) - start)

    return ans


if __name__ == "__main__":
    nums = [1, 3, 5, 2, 7, 5]
    minK = 1
    maxK = 5
    print (countSubarrays(nums, minK, maxK))

    nums = [1, 1, 1, 1]
    minK = 1
    maxK = 1
    print(countSubarrays(nums, minK, maxK))
