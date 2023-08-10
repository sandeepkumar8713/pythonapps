# https://leetcode.com/problems/shopping-offers/
# Question : In LeetCode Store, there are n items to sell. Each item has a price. However, there are
# some special offers, and a special offer consists of one or more different kinds of items with a sale price.
# You are given an integer array price where price[i] is the price of the ith item, and an integer array
# needs where needs[i] is the number of pieces of the ith item you want to buy. You are also given an
# array special where special[i] is of size n + 1 where special[i][j] is the number of pieces of the
# jth item in the ith offer and special[i][n] (i.e., the last integer in the array) is the price of the ith offer.
# Return the lowest price you have to pay for exactly certain items as given, where you could make optimal
# use of the special offers. You are not allowed to buy more items than you want, even if that would lower
# the overall price. You could use any of the special offers as many times as you want.
#
# Example : Input: price = [2,5], special = [[3,0,5],[1,2,10]], needs = [3,2]
# Output: 14
# Explanation: There are two kinds of items, A and B. Their prices are $2 and $5 respectively.
# In special offer 1, you can pay $5 for 3A and 0B
# In special offer 2, you can pay $10 for 1A and 2B.
# You need to buy 3A and 2B, so you may pay $10 for 1A and 2B (special offer #2), and $4 for 2A.
#
# Question Type : ShouldSee
# Used : We do DFS using DP. DP's index will be tuple of needs array.
#        For each possible combination of need, check if special can be applied. If applied,
#        call DFS on remaining needs. While recursive calls, save the sub solution in dp.
# Logic: def dfs(dp, price, specials, needs):
#        if sum(needs) == 0: return 0
#        if tuple(needs) in dp: return dp[tuple(needs)]
#        for i in range(len(needs)):
#           actualPrice += price[i] * needs[i]
#        minPrice = sys.maxsize
#        for special in specials:
#           ok, remainingNeeds = canBuy(special, needs)
#           if ok:
#               specialPrice = dfs(dp, price, specials, remainingNeeds) + special[-1]
#               minPrice = min(minPrice, specialPrice)
#        dp[tuple(needs)] = min(minPrice, actualPrice)
#        return dp[tuple(needs)]
# Complexity : O(k^n) count of all possible combinations of needs.


import sys


def canBuy(special, needs):
    remainingNeeds = []
    for i in range(len(needs)):
        remaining = needs[i] - special[i]
        if remaining < 0:
            return False, needs
        remainingNeeds.append(remaining)
    return True, remainingNeeds


def dfs(dp, price, specials, needs):
    if sum(needs) == 0:
        return 0

    if tuple(needs) in dp:
        return dp[tuple(needs)]

    actualPrice = 0
    for i in range(len(needs)):
        actualPrice += price[i] * needs[i]

    minPrice = sys.maxsize
    for special in specials:
        ok, remainingNeeds = canBuy(special, needs)
        if ok:
            specialPrice = dfs(dp, price, specials, remainingNeeds) + special[-1]
            minPrice = min(minPrice, specialPrice)
            remainingNeeds.clear()

    dp[tuple(needs)] = min(minPrice, actualPrice)
    return dp[tuple(needs)]


def shoppingOffers(price, special, needs):
    dp = {}
    return dfs(dp, price, special, needs)


if __name__ == "__main__":
    price = [2, 5]
    specials = [[3, 0, 5], [1, 2, 10]]
    needs = [3, 2]
    print(shoppingOffers(price, specials, needs))

    price = [2, 3, 4]
    special = [[1, 1, 0, 4], [2, 2, 1, 9]]
    needs = [1, 2, 1]
    print(shoppingOffers(price, specials, needs))

