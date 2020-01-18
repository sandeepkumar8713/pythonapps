# CTCI : Q8_11_Coins
# Question : Given a value N, if we want to make change for N cents, and we have infinite supply of each of
# S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change? The order of coins doesn't matter.
#
# For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}.
#
# Used : Here we are maintaining a memory table. table : size (targetSum+1). Initialize all as 0.
#        table[i] will be storing the number of solutions for targetSum i.
#        Run a loop over coin value in coinList
#           Run a loop from coin value to targetSum
#               Consider this coin as chosen, then take possible counts from table[j - coinValue] and add to table[j].
#               table[j] += table[j - coinValue]
# Complexity : O(n^2)


def count(coinList, targetSum):
    # table[i] will be storing the number of solutions for targetSum i.
    table = [0] * (targetSum + 1)
    table[0] = 1

    # Pick all coins one by one and update the table[] values after the index greater than or equal to the value of the
    # picked coin
    for coinValue in coinList:
        for j in range(coinValue, targetSum + 1):
            table[j] += table[j - coinValue]

    return table[targetSum]


if __name__ == "__main__":
    coinList = [1, 2, 3]
    targetSum = 4

    # coinList = {2, 5, 3, 6}
    # targetSum = 10
    print ("Possible ways to make change : " + str(count(coinList, targetSum)))
