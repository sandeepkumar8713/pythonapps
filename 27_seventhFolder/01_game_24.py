# https://leetcode.com/problems/24-game/
# Question : You are given an integer array cards of length 4. You have four cards,
# each containing a number in the range [1, 9]. You should arrange the numbers on
# these cards in a mathematical expression using the operators ['+', '-', '*', '/']
# and the parentheses '(' and ')' to get the value 24.
# You are restricted with the following rules:
# The division operator '/' represents real division, not integer division.
# For example, 4 / (1 - 2 / 3) = 4 / (1 / 3) = 12.
# Every operation done is between two numbers. In particular, we cannot use '-' as a unary operator.
# For example, if cards = [1, 1, 1, 1], the expression "-1 - 1 - 1 - 1" is not allowed.
# You cannot concatenate numbers together
# For example, if cards = [1, 2, 1, 2], the expression "12 + 12" is not valid.
# Return true if you can get such expression that evaluates to 24, and false otherwise.
#
#
# Question Type : ShouldSee
# Used : Make permutations of given sequence, pick first 2 operands, apply all operators and
#        recur for ans and remaining. At the end check if ans is 24 and return False.
#        Logic :
#        @lru_cache
#        def fn(*args):
#        if len(args) == 1: return args[0] == 24
#        for x, y, *rem in permutations(args):
#           for op in add, sub, mul, Fraction:
#               if (op != Fraction or y != 0) and fn(op(x, y), *rem):
#                   return True
#        return False
# Complexity : O(n!) where n is number of operands


from fractions import Fraction
from itertools import permutations
from functools import lru_cache


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x - y



def judgePoint24(cards):
    @lru_cache
    def fn(*args):
        """Return True if arguments can be combined into 24."""
        if len(args) == 1:
            return args[0] == 24

        for x, y, *rem in permutations(args):
            for op in add, sub, mul, Fraction:
                if (op != Fraction or y != 0) and fn(op(x, y), *rem):
                    return True

        return False

    return fn(*cards)


if __name__ == "__main__":
    cards = [4, 1, 8, 7]
    print(judgePoint24(cards))

    cards = [1, 2, 1, 2]
    print(judgePoint24(cards))
