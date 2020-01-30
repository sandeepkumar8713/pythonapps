# Question : Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum
# total value in the knapsack.
#
# Question Type : Generic
# Used : Here we are maintaining a memory table. K : size (n+1) * (weightLimit+1). Initialize all as 0.
#        Now loop over each element of the table K. If it is in first row or col set as 0.
#           For this row i, check if current item i-1 can fit in the knapsack of j. If yes, choose the max of
#              previous row value, by ignoring this item : (K[i - 1][j]) or
#              put item in bag and check with remaining capacity: (itemValue[i - 1] + K[i - 1][j - itemWeight[i - 1]])
#           If it can't fit then set previous row value (K[i - 1][j])
#        return K[n][weightLimit] (Last item of table will give max value)
# Complexity : O(n * weightLimit) so O(n^2)


def knapSack(itemValue, itemWeight, weightLimit):
    n = len(itemValue)
    K = []
    for i in range(0, n+1):
        row = [0] * (weightLimit + 1)
        K.append(row)

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for j in range(weightLimit + 1):
            if i == 0 or j == 0:
                K[i][j] = 0
            elif itemWeight[i - 1] <= j:
                K[i][j] = max(itemValue[i - 1] + K[i - 1][j - itemWeight[i - 1]], K[i - 1][j])
            else:
                K[i][j] = K[i - 1][j]

    return K[n][weightLimit]


if __name__ == "__main__":
    itemValue = [60, 100, 120]
    itemWeight = [10, 20, 30]
    weightLimit = 50
    print(knapSack(itemValue, itemWeight, weightLimit))
