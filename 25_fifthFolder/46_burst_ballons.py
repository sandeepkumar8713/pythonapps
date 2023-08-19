# https://leetcode.com/problems/burst-balloons/
# Question : You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number
# on it represented by an array nums. You are asked to burst all the balloons.
# If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1
# or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.
# Return the maximum coins you can collect by bursting the balloons wisely.
#
# Example: Input: nums = [3,1,5,8]
# Output: 167
# Explanation:
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
#
# Question Type : ShouldSee
# Used : DP with DFS is used.
#        Call recursive function dfs, with start and end, which calculate max value using intermediate
#        value of dfs().
# Logic: nums = [1] + nums + [1]
#        dp = dict()
#        def dfs(l, r):
#           if l > r: return 0
#           if (l, r) not in dp:
#               maximum = float("-inf")
#               for i in range(l, 1 + r):
#                   left and right sub array is already brust
#                   maximum = max(maximum, nums[i] * nums[l - 1] * nums[r + 1] +
#                      dfs(l, i - 1) + dfs(i + 1, r))
#               dp[(l, r)] = maximum
#           return dp[(l, r)]
#
#        return dfs(1, len(nums) - 2)
# Complexity : O(n^2)


def maxCoins(nums):
    nums = [1] + nums + [1]
    dp = dict()

    def dfs(l, r):
        if l > r:
            return 0
        if (l, r) not in dp:
            maximum = float("-inf")
            for i in range(l, 1 + r):
                maximum = max(maximum, nums[i] * nums[l - 1] * nums[r + 1] + dfs(l, i - 1) + dfs(i + 1, r))
            dp[(l, r)] = maximum
        return dp[(l, r)]

    return dfs(1, len(nums) - 2)


if __name__ == "__main__":
    nums = [3, 1, 5, 8]
    print(maxCoins(nums))

    nums = [8, 8]
    print(maxCoins(nums))

    nums = [1, 5]
    print(maxCoins(nums))
