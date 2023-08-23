# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/412736/Much-easier-to-understand.-Beats-99-python-O(n)
# Similar : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
# Question : Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of
# the stock), design an algorithm to find the maximum profit. Note that you cannot sell a stock before
# you buy one. Followup : If you were only permitted to complete at most one transaction.
#
# Question Type : Generic
# Used : For first question, loop over the input array, find the min price then the max price and subtract.
#        The difference would give back the maxProfit.
#        For follow up question. Find the first max profit using above function get there start and end
#        index also. Now find max profit from index 0 to start - 1 and end + 1 to len. Return max of
#        two along with first max profit.
# Logic: def maxProfitTwoTranscation(prices):
#        firstProfit, index = maxProfit(prices, 0, len(prices) - 1)
#        if firstProfit == 0: return 0
#        leftProfit, leftIndex = maxProfit(prices, 0, index[0] - 1)
#        rightProfit, rightIndex = maxProfit(prices, index[1] + 1, len(prices) - 1)
#        return firstProfit + max(leftProfit, rightProfit)
#
#        def maxProfit(prices, left, right):
#        minPrice = sys.maxint, maxProfit = 0
#        sellIndex = -1, buyIndex = -1
#        for i in range(left, right + 1):
#           if prices[i] < minPrice:
#               minPrice = prices[i], buyIndex = i
#           elif prices[i] - minPrice > maxProfit:
#               maxProfit = prices[i] - minPrice
#               sellIndex = i
#        if maxProfit == 0: return 0, [-1, -1]
#        return maxProfit, [buyIndex, sellIndex]
# Complexity : O(n)

import sys


def maxProfit(prices, left, right):
    minPrice = sys.maxsize
    maxProfit = 0
    sellIndex = -1
    buyIndex = -1
    for i in range(left, right + 1):
        if prices[i] < minPrice:
            minPrice = prices[i]
            buyIndex = i
        elif prices[i] - minPrice > maxProfit:
            maxProfit = prices[i] - minPrice
            sellIndex = i

    if maxProfit == 0:
        return 0, [-1, -1]

    return maxProfit, [buyIndex, sellIndex]


def maxProfitTwoTranscation(prices):
    firstProfit, index = maxProfit(prices, 0, len(prices) - 1)
    if firstProfit == 0:
        return 0
    leftProfit, leftIndex = maxProfit(prices, 0, index[0] - 1)
    rightProfit, rightIndex = maxProfit(prices, index[1] + 1, len(prices) - 1)

    return firstProfit + max(leftProfit, rightProfit)


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(maxProfit(prices, 0, len(prices) - 1))

    prices = [7, 6, 4, 3, 1]
    print(maxProfit(prices, 0, len(prices) - 1))

    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    print(maxProfitTwoTranscation(prices))

    prices = [1, 2, 3, 4, 5]
    print(maxProfitTwoTranscation(prices))
