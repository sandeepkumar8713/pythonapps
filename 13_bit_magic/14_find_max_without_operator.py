# CTCI : Q16_07_Number_Max
# https://www.geeksforgeeks.org/compute-the-minimum-or-maximum-max-of-two-integers-without-branching/
# Question : Write a method that finds the maximum of two numbers. You should not use if-else
# or any other comparison operator.
#
# Question Type : ShouldSee
# Used : Minimum of x and y will be : y + ((x - y) & ((x - y) >> (sizeof(int) * CHAR_BIT - 1)))
#        This method right shifts the difference of x and y by 31.
#        If (x-y) is smaller than 0, then (x - y) >> 31 will be 1.
#        If (x-y) is greater than or equal to 0, then (x -y)>>31 will be 0.
#        So if x >= y, we get minimum as y + (x-y)&0 which is y.
#        If x < y, we get minimum as y + (x-y)&1 which is x.
# Complexity : O(1)

import sys

CHAR_BIT = 8
INT_BIT = sys.getsizeof(int())


def Min(x, y):
    return y + ((x - y) & ((x - y) >> (INT_BIT * CHAR_BIT - 1)))


def Max(x, y):
    return x - ((x - y) & ((x - y) >> (INT_BIT * CHAR_BIT - 1)))


if __name__ == "__main__":
    x = 15
    y = 6
    print("Minimum : " + str(Min(x, y)))
    print("Maximum : " + str(Max(x, y)))
