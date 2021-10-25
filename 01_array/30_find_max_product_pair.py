# https://www.geeksforgeeks.org/return-a-pair-with-maximum-product-in-array-of-integers/
# Question : Given an array with both +ive and -ive integers, return a pair with highest product.
#
# Examples : Input: arr[] = {1, 4, 3, 6, 7, 0}
# Output: {6,7}
#
# Input: arr[] = {-1, -3, -4, 2, 0, -5}
# Output: {-4,-5}
#
# Question Type : Easy
# Used : The idea is to traverse the input array and keep track of following four values.
#       a) Maximum positive value
#       b) Second maximum positive value
#       c) Maximum negative value i.e., a negative value with maximum absolute value
#       d) Second maximum negative value.
#       At the end of the loop, compare the products of first two and last two and
#       print the maximum of two products.
# Complexity : O(n)

import sys


def maxProduct(inpArr):
    n = len(inpArr)

    if n < 2:
        print("not possible")
        return

    if n == 2:
        print(inpArr[0], inpArr[1])
        return

    maxPos = -sys.maxsize
    secondMaxPos = -sys.maxsize

    minNeg = 0
    secondMinNeg = 0

    for ele in inpArr:
        if ele >= 0:
            if ele > maxPos:
                secondMaxPos = maxPos
                maxPos = ele
            elif ele > secondMaxPos:
                secondMaxPos = ele
        else:
            if ele < minNeg:
                secondMinNeg = minNeg
                minNeg = ele
            elif ele < secondMinNeg:
                secondMinNeg = ele

    if maxPos * secondMaxPos > minNeg * secondMinNeg:
        print(maxPos, secondMaxPos)
    else:
        print(minNeg, secondMinNeg)


if __name__ == "__main__":
    inpArr = [1, 4, 3, 6, 7, 0]
    maxProduct(inpArr)

    inpArr = [-1, -3, -4, 2, 0, -5]
    maxProduct(inpArr)
