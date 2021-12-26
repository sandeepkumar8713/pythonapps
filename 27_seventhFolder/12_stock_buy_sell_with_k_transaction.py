# https://www.geeksforgeeks.org/best-time-to-buy-and-sell-stock/
# Question : Given an array price[] of length N which denotes the prices of the stocks
# on different days. The task is to find the maximum profit possible for buying and
# selling the stocks on different days using transactions where at most K transactions
# are allowed.
#
# Question Type : Generic
# Used : We will use DFS with DP here. Make a matrix of dp[n][2] where dp[i][1]
#        represents max profit b/w i to n considering ele at i is bought.
#        During DFS, check if we need to buy or sell.
#        From here we have either choose to do transaction or skip this element, based on which ever is max.
#        Logic :
#        def dfs(index, buy, count):
#        nonlocal dp, k, prices
#        if index >= len(prices) or count >= k:
#           return 0
#        if dp[index][buy] != -1:
#           return dp[index][buy]
#        togglebuy = buy ^ 1
#        if buy:
#           dp[index][buy] = max(-prices[index] + dfs(index + 1, togglebuy, count),
#                                  dfs(index + 1, buy, count))
#        else:
#           dp[index][buy] = max(prices[index] + dfs(index + 1, togglebuy, count + 1),
#                                  dfs(index + 1, buy, count))
#        return dp[index][buy]
#
#        call dfs(0, 1, 0) to get ans.
# Complexity : O(n)


def findMaxProfit(prices, k):
    n = len(prices)
    dp = []
    for i in range(n):
        dp.append([-1] * 2)

    def dfs(index, buy, count):
        nonlocal dp, k, prices

        if index >= len(prices) or count >= k:
            return 0

        if dp[index][buy] != -1:
            return dp[index][buy]

        togglebuy = buy ^ 1

        if buy:
            dp[index][buy] = max(-prices[index] + dfs(index + 1, togglebuy, count),
                                 dfs(index + 1, buy, count))
        else:
            dp[index][buy] = max(prices[index] + dfs(index + 1, togglebuy, count + 1),
                                 dfs(index + 1, buy, count))

        return dp[index][buy]

    return dfs(0, 1, 0)


if __name__ == "__main__":
    prices = [3, 2, 6, 5, 0, 3]
    k = 2
    print(findMaxProfit(prices, k))

    prices = [2, 4, 1]
    k = 2
    print(findMaxProfit(prices, k))

    prices = [2, 4, 6]
    k = 2
    print(findMaxProfit(prices, k))

    prices = [1, 2, 3, 4, 5]
    k = 2
    print(findMaxProfit(prices, k))
