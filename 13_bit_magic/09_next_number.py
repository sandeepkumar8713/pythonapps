# CTCI : Q5_04_Next_Number
# https://www.geeksforgeeks.org/closest-next-smaller-greater-numbers-number-set-bits/
# Question : Given a positive integer n, print the next smallest and the previous largest
# number that have the same number of 1 bits in their binary representation
#
# Question Type : Generic
# Used : nextGreater:
#        p = Position of rightmost non-trailing 0. p = c1 + c0
#        c1 ==> Number of ones to the right of p
#        c0 ==> Number of zeros to the right of p
#        Flip rightmost non-trailing zero to one
#        Clear all bits to the right of p
#        Insert (c1 - 1) ones on the right and subtract 1
#
#        nextSmaller:
#        Compute c0 and c1.
#        Note that c1 is the number of trailing ones, and
#        c0 is the size of the block of zeros immediately to the left of the trailing ones.
#        Flip the rightmost non-trailing one to a zero. This will be at position p = c1 + c0.
#        Clear all bits to the right of bit p.
#        Insert (c0 + 1) ones immediately to the right of position p.
# Complexity : O(1)


def nextGreater(n):
    c = n
    c0 = 0
    c1 = 0

    while ((c & 1) == 0) and (c != 0):
        c0 += 1
        c >>= 1

    while (c & 1) == 1:
        c1 += 1
        c >>= 1

    # If there is no bigger number with
    # the same no. of 1's
    if c0 + c1 == 31 or c0 + c1 == 0:
        return -1

    print(c0, c1)
    # position of rightmost non-trailing zero
    p = c0 + c1
    # Flip rightmost non-trailing zero
    n |= (1 << p)
    # Clear all bits to the right of p
    n &= ~((1 << p) - 1)
    # Insert (c1-1) ones on the right.
    n |= (1 << (c1 - 1)) - 1

    return n


def previousSmaller(n):
    c = n
    c0 = 0
    c1 = 0

    if c == 0:
        return -1

    while (c & 1) == 1:
        c1 += 1
        c >>= 1

    while ((c & 1) == 0) and (c != 0):
        c0 += 1
        c >>= 1

    print(c0, c1)
    # position of rightmost non-trailing one
    p = c0 + c1
    # Flip rightmost non-trailing one
    n &= ~(1 << p)
    # Clear all bits to the right of p
    n &= ~((1 << p) - 1)

    # Insert (c1+1) ones on the right and shift left by c0-1

    # v = 0
    # for i in range(0, c1 + 1):
    #     v = (v << 1) + 1

    v = (1 << (c1 + 1)) - 1
    n |= (v << (c0 - 1))

    return n


if __name__ == "__main__":
    n = 10115
    print(bin(n))
    result = nextGreater(n)
    print(bin(result))
    print(result)

    print("")

    n = 10115
    print(bin(n))
    result = previousSmaller(n)
    print(bin(result))
    print(result)

    print("")

    n = 26
    print(bin(n))
    result = nextGreater(n)
    print(bin(result))
    print(result)

    print("")

    n = 26
    print(bin(n))
    result = previousSmaller(n)
    print(bin(result))
    print(result)

    print("")
