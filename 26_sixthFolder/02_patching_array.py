# https://leetcode.com/problems/patching-array/
# Question : Given a sorted integer array nums and an integer n, add/patch elements to the array such
# that any number in the range [1, n] inclusive can be formed by the sum of some elements in the array.
# Return the minimum number of patches required.
#
# Example : Input: nums = [1,3], n = 6
# Output: 1
# Explanation: Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
# Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
# Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
#
# Question Type : ShouldSee
# Used : We initialize reach with 1. We loop until reach equals n.
#        While looping we keep adding elements to nums to reach.
#        If reach is less than next element in nums, then we need a patch.
#        Double reach and increment patch count.
#        After loop return patch count.
#        Logic :
#        while reach <= n:
#           if i < len(nums) and nums[i] <= reach:
#               reach += nums[i], i += 1
#           else:
#               reach *= 2, patches += 1
#        return patches
# Complexity : O(n)


def minPatches(nums, n):
    patches = 0
    reach = 1
    i = 0

    while reach <= n:
        if i < len(nums) and nums[i] <= reach:
            reach += nums[i]
            i += 1
        else:
            reach *= 2
            patches += 1

    return patches


if __name__ == "__main__":
    nums = [1, 3]
    n = 6
    print(minPatches(nums, n))

    nums = [1, 5, 10]
    n = 20
    print(minPatches(nums, n))

    nums = [1, 2, 2]
    n = 5
    print(minPatches(nums, n))
