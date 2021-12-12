# https://leetcode.com/problems/bitwise-and-of-numbers-range/
# Question : Given two integers left and right that represent the range [left, right], return
# the bitwise AND of all numbers in this range, inclusive.
#
# Question Type : ShouldSee
# Used : If both the numbers are same, bitwise AND of them would give me the same number
#        since X & X = X. So, while the 2 numbers are not same we right shift the bits
#        of both the number by 1 and increase out shift counter by 1.
#        At the end we just need to multiple our smaller number by 2 ^ (shift counter)
#        since all those bits would give a bitwise AND of 0(zero) since there would be
#        always an odd and an even number between,
# Complexity : O(1)


def rangeBitwiseAnd(left, right):
    shift = 0

    while left != right:
        left >>= 1
        right >>= 1
        shift += 1

    return left << shift


if __name__ == "__main__":
    left = 5
    right = 7
    print(rangeBitwiseAnd(left, right))
