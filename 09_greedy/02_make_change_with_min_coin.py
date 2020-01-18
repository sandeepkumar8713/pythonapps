# Question : Given a value V, if we want to make change for V cents, and we have infinite supply of each of
# C = { C1, C2, .. , Cm} valued coins, what is the minimum number of coins to make the change?
#
# Input: coins[] = {25, 10, 5}, V = 30
# Output: Minimum 2 coins required
#
# Used : Try to solve the sub problem first. Make a array table of size V+1, which will be used to store sub result from
#        0 to V. Now loop over from 1 to V. Start one more loop that loops over all the coins of different denomination.
#           If a coins value is less than or equal to target value. Assume we have used it, find the sub result for
#           remaining value from the table.(subRes = table[i-coins[j]]). If subRes is not max int and (subRes + 1) is
#           less than current value in table, then update the table[i]
#        At the end of loop return table[targetValue]
# Complexity : O(mV) m : types of coin and V: target value


import sys


def minCoins(coins,targetValue):
    table = [sys.maxint] * (targetValue + 1)
    table[0] = 0

    for i in range(1, targetValue+1):
        for j in range(0, len(coins)):
            if coins[j] <= i:

                subRes = table[i-coins[j]]
                if subRes != sys.maxint and subRes + 1 < table[i]:
                    table[i] = subRes + 1

    return table[targetValue]


if __name__ == "__main__":
    coins = [9, 6, 5, 1]
    targetValue = 11
    print "Minimum coins required:", minCoins(coins,targetValue)
