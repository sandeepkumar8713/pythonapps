# https://leetcode.com/problems/target-sum/
# Question : You are given an integer array nums and an integer target.
# You want to build an expression out of nums by adding one of the symbols '+' and '-'
# before each integer in nums and then concatenate all the integers.
# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and
# concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.
#
# Question Type : ShouldSee
# Used : Make dp of size -total to +total
#        Run 2 loops, 1 for all elements and 1 for all possible total
#        After the loop, get result for target from dp.
#           Choose element and the next count.
#        Note that we are using 2 dp arrays here
# Logic: dp[-nums[0]] = 1
#        dp[nums[0]] += 1
#        for i in range(1, n):
#           next = defaultdict(int)
#           for k in range(-total, total + 1, 1):
#               next[k + nums[i]] += dp[k]
#               next[k - nums[i]] += dp[k]
#           dp = next
#        return dp.get(target, 0)
# Complexity : O(n*m) n is no of elements, m is sum of elements

from collections import defaultdict


def find_number(nums, target):
    total = sum(nums)
    n = len(nums)
    dp = defaultdict(int)

    dp[-nums[0]] = 1
    dp[nums[0]] += 1

    for i in range(1, n):
        next = defaultdict(int)
        for k in range(-total, total + 1, 1):
            next[k + nums[i]] += dp[k]
            next[k - nums[i]] += dp[k]
        dp = next

    return dp.get(target, 0)


if __name__ == "__main__":
    nums = [1, 1, 1, 1, 1]
    target = 3
    print(find_number(nums, target))

    nums = [2, 1]
    target = 1
    print(find_number(nums, target))

    nums = [0, 0, 0, 0, 0, 0, 0, 0, 1]
    target = 1
    print(find_number(nums, target))
