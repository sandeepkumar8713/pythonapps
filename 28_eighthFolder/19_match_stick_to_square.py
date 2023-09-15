# https://leetcode.com/problems/matchsticks-to-square/
# Similar : https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
# Question : You are given an integer array matchsticks where matchsticks[i] is the length of the ith
# matchstick. You want to use all the matchsticks to make one square. You should not break any stick,
# but you can link them up, and each matchstick must be used exactly one time.
# Return true if you can make this square and false otherwise.
#
# Question Type : Generic
# Used : We'll use DP to find whether the array can be partitioned into k subsets of equal sum.
#        dp size = power set of array elements. why? because, we need to consider all sum subsets.
#        dp[i] indicates whether array of length i can partitioned into k subsets of equal sum. Using this technique,
#        the last index of this dp array will tell whether the whole array can be partitioned into k subsets of equal
#        sum.
# Logic: target = sum(inp_arr) // k
#        dp = dict(), dp[0] = 0
#        for mask in range(1 << n):
#           if mask not in dp.keys(): continue
#           for i in range(n):
#               ele = inp_arr[i]
#               if not (mask & (1 << i)) and dp[mask] + ele <= target:
#                   dp[mask | (1 << i)] = (dp[mask] + ele) % target
#        if (1 << n) - 1 in dp.keys():
#           return dp[(1 << n) - 1] == 0
#        else:
#           return False
# Complexity : O(n)

def is_possible(inp_arr, k):
    n = len(inp_arr)
    if (sum(inp_arr) % k) != 0:
        return False
    target = sum(inp_arr) // k

    dp = dict()
    dp[0] = 0
    for mask in range(1 << n):
        if mask not in dp.keys():
            continue

        for i in range(n):
            ele = inp_arr[i]
            # i is not selected and sum is less than or equal to target
            if not (mask & (1 << i)) and dp[mask] + ele <= target:
                dp[mask | (1 << i)] = (dp[mask] + ele) % target

    if (1 << n) - 1 in dp.keys():
        # All elements selected
        return dp[(1 << n) - 1] == 0
    else:
        return False


if __name__ == "__main__":
    inp_arr = [1, 1, 2, 2, 2]
    k = 4
    print(is_possible(inp_arr, k))

    inp_arr = [3, 3, 3, 3, 4]
    k = 4
    print(is_possible(inp_arr, k))

    inp_arr = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    print(is_possible(inp_arr, k))

    inp_arr = [1, 2, 3, 4, 5]
    k = 3
    print(is_possible(inp_arr, k))
