# https://www.geeksforgeeks.org/highest-power-2-less-equal-given-number/
# Question : Given a number n, find the highest power of 2 that is smaller than or equal to n.
#
# Input : n = 10
# Output : 8
#
# Input : n = 19
# Output : 16
#
# Input : n = 32
# Output : 32
#
# Question Type : Easy
# Used : Take p = log of n and return pow(2, p)
# Complexity : O(1)


import math


def highestPowerOf2(n):
    p = int(math.log(n, 2))
    return pow(2, p)


if __name__ == "__main__":
    n = 10
    n = 1164
    print(highestPowerOf2(n))
