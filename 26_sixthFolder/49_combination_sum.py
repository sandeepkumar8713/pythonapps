# https://leetcode.com/problems/combination-sum-iv/
# Qeustion : Given an array of distinct integers nums and a target integer target,
# return the number of possible combinations that add up to target. The answer is
# guaranteed to fit in a 32-bit integer.
#
# Question Type : ShouldSee
# Used : We will use recursion and dp here.
#        Loop over the given input array, call recursive function over diff of target and ele.
#        Save intermediate result in dp
#        Logic :
#        def combinations(target):
#        if target in dp:
#           return dp[target]
#        if target == 0: return 1
#        if target < 0: return 0
#        output = 0
#        for num in inpArr:
#           output += combinations(target - num)
#        dp[target] = output
#        return output
# Complexity : O(n) where n is target


def combinationSum4(inpArr, target):
    dp = dict()

    def combinations(target):
        if target in dp:
            return dp[target]

        if target == 0:
            return 1
        if target < 0:
            return 0

        output = 0
        for num in inpArr:
            output += combinations(target - num)
        dp[target] = output
        return output

    return combinations(target)


if __name__ == "__main__":
    inpArr = [1, 2, 3]
    target = 4
    print(combinationSum4(inpArr, target))
