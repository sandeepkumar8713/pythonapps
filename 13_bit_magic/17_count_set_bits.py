# https://www.geeksforgeeks.org/count-set-bits-in-an-integer/
# Question : Write an efficient program to count number of 1s in binary representation of an integer.
#
# Examples :
#
# Input : n = 6
# Output : 2
# Binary representation of 6 is 110 and has 2 set bits
#
# Question Type : Easy
# Used : We subtract a number by 1 and do bitwise & with itself (n & (n-1)), we unset the rightmost set bit.
#        If we do n & (n-1) in a loop and count the no of times loop executes we get the set bit count.
# Complexity : O(n)


def countSetBits(n):
    count = 0
    while n:
        n &= (n - 1)
        count += 1

    return count


if __name__ == "__main__":
    i = 10
    print(countSetBits(i))
