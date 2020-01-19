# https://www.geeksforgeeks.org/stock-buy-sell/
# Question : The cost of a stock on each day is given in an array, find the max profit that you can make by buying and
# selling in those days. For example, if the given array is {100, 180, 260, 310, 40, 535, 695}, the maximum
# profit can earned by buying on day 0, selling on day 3. Again buy on day 4 and sell on day 6. If the given
# array of prices is sorted in decreasing order, then profit cannot be earned at all.
#
# Question Type : ShouldSee
# Used : Run a loop over given array from 0 to n-2.
#           move ahead i++ while current is higher than next. (let the price fall)
#           then buy current stock          (buy at the point where price start increasing)
#           move ahead i++ while current is higher than previous (let the price increase)
#           then sell previous stock        (sell at the point where price start falling)
#        Print the dict in which buy and sell stock were stored
# Complexity : O(n)


def stockBuySell(arr):
    n = len(arr)

    sol = []
    if n == 1:
        return sol

    i = 0
    while i < n-1:
        # move while current is higher than next
        while i < n-1 and arr[i] >= arr[i+1]:
            i += 1

        if i == n-1:
            break

        # buy current stock
        tempDict = {'buy': i}
        i += 1

        # move while current is higher than previous
        while i < n and arr[i] >= arr[i-1]:
            i += 1

        # sell previous stock
        tempDict['sell'] = i-1
        sol.append(tempDict)

    return sol


if __name__ == "__main__":
    arr = [100, 180, 260, 310, 40, 535, 695]
    print(stockBuySell(arr))

