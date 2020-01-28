# https://leetcode.com/problems/find-k-th-smallest-pair-distance/solution/
# Question : Given an integer array, return the k-th smallest distance among all the pairs.
# The distance of a pair (A, B) is defined as the absolute difference between A and B.
#
# Example: Input: nums = [1,3,1]
# k = 1
# Output: 0
# Explanation: Here are all the pairs:
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# Then the 1st smallest distance pair is (1,1), and its distance is 0.
#
# Question Type : ShouldSee
# Used : Here we find min and max value of inpArr. We do binary search over it, take a mid value, then check if there
#        are k pairs or more whose distance is less than mid. After the binary search low is our answer.
#        Let's binary search for the answer. It's definitely in the range [0, W], where W = max(nums) - min(nums)].
#        Let possible(guess) be true if and only if there are k or more pairs with distance less than or equal to
#        guess. We will focus on evaluating our possible function quickly. We will use a sliding window approach
#        to count the number of pairs with distance <= guess.
#        Logic :
#        smallestDistancePair(nums, k):
#           nums.sort()
#           lo = 0, hi = nums[-1] - nums[0]
#           while lo < hi:
#               mi = (lo + hi) / 2
#               if possible(mi, nums, k): hi = mi
#               else: lo = mi + 1
#           return lo
#        possible(guess, nums, k):
#           count = left = 0
#           for right in range(len(nums)):
#               while nums[right] - nums[left] > guess: left += 1
#               count += right - left
#           return count >= k
# Complexity : O(N log W + N log N), where NN is the length of nums, and WW is equal to nums[nums.length - 1] - nums[0]


def possible(guess, nums, k):
    # Is there k or more pairs with distance <= guess?
    count = left = 0
    for right in range(len(nums)):
        while nums[right] - nums[left] > guess:
            left += 1
        count += right - left
    return count >= k


def smallestDistancePair(nums, k):
        nums.sort()
        lo = 0
        hi = nums[-1] - nums[0]
        while lo < hi:
            mi = (lo + hi) / 2
            if possible(mi, nums, k):
                hi = mi
            else:
                lo = mi + 1
        return lo


if __name__ == "__main__":
    nums = [1, 3, 1]
    k = 1
    print(smallestDistancePair(nums, k))
