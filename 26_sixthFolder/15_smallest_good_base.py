# https://leetcode.com/problems/smallest-good-base/
# Question : Given an integer n represented as a string, return the smallest good base of n.
# We call k >= 2 a good base of n, if all digits of n base k are 1's.
#
# Example : Input: n = "13"
# Output: "3" (3 digit number system)
# Explanation: 13 base 3 is 111.
#
# Question Type : OddOne
# Used : ans^0 + ans^1 + ans^2 + ... + ans^N-1 = n
#        As the base increases - from 2 to 8 to 16 the length of the string decreases.
#        From this we can infer that N(no. of digits) must be less than or equal to len(bin(n)) - 2.
#        Where the -2 is to ignore the prefix '0b'. i.e. bin(5) = '0b101'.
#        Now we should do binary search from 2 to n - 1 base, with number of digits as N to 0.
#        Logic:
#        N = len(bin(n)[2:])
#        for length in range(N, 0, -1):
#           low = 2, high = n - 1
#           while low <= high:
#               guessBase = (low + high) // 2
#               v = is_valid(guessBase, length, n)
#               if v < 0: high = guessBase - 1
#               elif v > 0: low = guessBase + 1
#               else: return str(guessBase)
# Complexity : O(log n * log n)


def is_valid(base, length, n):
    """returns 0 if total == n, pos if n > total and neg if n < total"""
    total = 0
    for i in range(length):
        total += base ** i
    return n - total


def smallestGoodBase(n):
    n = int(n)
    N = len(bin(n)[2:])
    for length in range(N, 0, -1):
        low = 2
        high = n - 1
        while low <= high:
            guessBase = (low + high) // 2
            v = is_valid(guessBase, length, n)
            if v < 0:
                high = guessBase - 1
            elif v > 0:
                low = guessBase + 1
            else:
                return str(guessBase)


if __name__ == "__main__":
    n = 13
    print(smallestGoodBase(n))
