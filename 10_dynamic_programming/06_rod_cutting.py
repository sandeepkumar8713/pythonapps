# https://www.geeksforgeeks.org/dynamic-programming-set-13-cutting-a-rod/
# Question : Given a rod of length n inches and an array of prices that contains prices of all pieces of size
# smaller than n. Determine the maximum value obtainable by cutting up the rod and selling the pieces.
# For example, if length of the rod is 8 and the values of different pieces are given as following, then the
# maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6)
#
# length   | 1   2   3   4   5   6   7   8
# --------------------------------------------
# price    | 1   5   8   9  10  17  17  20
#
# Used : Here we are maintaining a memory table. val : size (n+1). Initialize all as 0.
#        Loop over all the elements from 1 to n.
#           Loop over elements from 0 to i
#               Choose current value or cut at length j and add val for (i - j - 1) with prices[j]
#               val[i] = max(val[i], prices[j] + val[i - j - 1])
#        return val[n]
# Complexity : O(n^2)

import sys
INT_MIN = -sys.maxint


def cutRod(prices):
    n = len(prices)
    val = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i):
            val[i] = max(val[i], prices[j] + val[i - j - 1])

    return val[n]


if __name__ == "__main__":
    arr = [1, 5, 8, 9, 10, 17, 17, 20]
    # arr = [3, 5, 8, 9, 10, 17, 17, 20]
    size = len(arr)
    print "Maximum Obtainable Value is ", cutRod(arr)
