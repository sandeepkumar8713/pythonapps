# https://www.geeksforgeeks.org/the-stock-span-problem/
# Similar : https://leetcode.com/problems/daily-temperatures/
# Question : The stock span problem is a financial problem where we have a series of n daily price
# quotes for a stock and we need to calculate span of stock’s price for all n days.The span Si
# of the stock’s price on a given day i is defined as the maximum number of consecutive days
# just before the given day, for which the price of the stock on the current day is less than
# or equal to its price on the given day.
#
# Example : Input : {100, 80, 60, 70, 60, 75, 85}
# Output : {1, 1, 1, 2, 1, 4, 6}
#
# Question Type : Generic
# Used : Loop over the given inpArr. If current element is higher than previous element,
#        add its span to current span. Jump in left by current span value.
#        Repeat the above process.
#        calculateSpan(inpArr):
#        n = len(inpArr), span = [0] * n
#        span[0] = 1
#        for i in range(1, n):
#           counter = 1
#           while (i - counter) >= 0 and inpArr[i] >= inpArr[i - counter]:
#               counter += span[i - counter]
#           span[i] = counter
#        return span
# Complexity : O(2n)


def calculateSpan(inpArr):
    n = len(inpArr)
    span = [0] * n
    # Span value of first element is always 1
    span[0] = 1

    # Calculate span values for rest of the elements
    for i in range(1, n):
        counter = 1
        while (i - counter) >= 0 and inpArr[i] >= inpArr[i - counter]:
            counter += span[i - counter]
        span[i] = counter
    return span


if __name__ == "__main__":
    price = [10, 4, 5, 90, 120, 80]
    print(calculateSpan(price))

    price = [100, 80, 60, 70, 60, 75, 85]
    print(calculateSpan(price))
