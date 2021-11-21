# CTCI : Q8_05_Recursive_Multiply
# https://www.geeksforgeeks.org/russian-peasant-multiply-two-numbers-using-bitwise-operators/
# Question : Write a recursive function to multiply two positive integers without using
# the * operator (or / operator). You can use addition, subtraction, and bit shifting, but you should
# minimize the number of those operations.
#
# Question Type : ShouldSee
# Used :  The idea is to double the first number and halve the second number repeatedly till
#         the second number doesn't become 1. In the process, whenever the second number
#         become odd, we add the first number to result (result is initialized as 0).
#         The value of a*b is same as (a*2)*(b/2) if b is even,
#         otherwise the value is same as ((a*2)*(b/2) + a).
#         Logic :
#         def russianPeasant(a, b):
#         a, b = makeSecondSmaller(a, b)
#         res = 0
#         while b > 0:
#           if b & 1: res = res + a
#           a <<= 1
#           b >>= 1
#         return res
# Complexity : O(log m) m is smaller of the two


def makeSecondSmaller(a,b):
    if a > b:
        return a, b
    else:
        return b, a


def russianPeasant(a, b):
    a, b = makeSecondSmaller(a, b)
    res = 0

    while b > 0:
        if b & 1:
            res = res + a

        a <<= 1
        b >>= 1

    return res


if __name__ == "__main__":
    print(russianPeasant(18, 1))
    print(russianPeasant(12, 20))
