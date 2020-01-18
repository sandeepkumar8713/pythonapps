# https://www.geeksforgeeks.org/egg-dropping-puzzle-dp-11/
# Question : Suppose you have N eggs and you want to determine from which floor in a K-floor building you can
# drop an egg such that it doesn't break. You have to determine the minimum number of attempts you need in order
# find the critical floor in the worst case while using the best strategy.There are few rules given below.
#
# An egg that survives a fall can be used again.
# A broken egg must be discarded.
# The effect of a fall is the same for all eggs.
# If the egg doesn't break at a certain floor, it will not break at any floor below.
# If the eggs breaks at a certain floor, it will break at any floor above.
#
# Used : When we drop an egg from a floor x, there can be two cases (1) The egg breaks (2) The egg doesn't break.
#       1) We only need to check for floors lower than x with remaining eggs; so the problem reduces to
#          x-1 floors and n-1 eggs
#       2) We only need to check for floors higher than x; so the problem reduces to k-x floors and n eggs.
#
#        We have to make a memory table count : dp (eggCount+1) * (floorCount+1). Mark all as 0. Initialize base values
#        as following : We need 1 trial for 1 floor and 0 trials for 0 floors.
#                       We always need j trials for 1 egg and j floors.
#        Now loop over each of the element from in dp from : i = 2 to eggCount + 1 , j = 2, floorCount + 1
#           set  dp[i][j] = sys.maxint
#           Loop over from floor 1 to j + 1:
#               minTrail = 1 + max(dp[i - 1][x - 1], dp[i][j - x])
#               update dp[i][j] if minTrial is less.
#       return dp[eggCount][floorCount]
# Complexity : O(n * k * k)

import sys


def eggDrop(eggCount, floorCount):
    dp = []
    for i in range(eggCount+1):
        dp.append([0] * (floorCount+1))

    # We need one trial for one floor and 0 trials for 0 floors
    for i in range(1, eggCount+1):
        dp[i][1] = 1
        dp[i][0] = 0

    # We always need j trials for one egg and j floors.
    for j in range(1, floorCount + 1):
        dp[1][j] = j

    # Fill rest of the entries in table using optimal substructure property
    for i in range(2, eggCount + 1):
        for j in range(2, floorCount + 1):
            dp[i][j] = sys.maxint
            for x in range(1, j + 1):
                # max because we are considering for worst case
                minTrail = 1 + max(dp[i - 1][x - 1], dp[i][j - x])
                if minTrail < dp[i][j]:
                    dp[i][j] = minTrail

    return dp[n][k]


if __name__ == "__main__":
    n = 2
    k = 36

    # n = 2
    # k = 10
    print "Minimum number of trials in worst case with", n, "eggs and", k, "floors is", eggDrop(n, k)
