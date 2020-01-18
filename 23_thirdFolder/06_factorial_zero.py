# CTCI : Q16_05_Factorial_Zeros
# Question : Given an integer n, write a function that returns count of trailing zeroes in n!.
#
# Used : A trailing zero is created with multiples of 10, and multiples of 10 are created with pairs of 5-multiples
#       and 2-multiples. Therefore, to count the number of zeros, we only need to count the pairs of multiples of 5
#       and 2. There will always be more multiples of 2 than 5, though, so simply counting the number of multiples
#       of 5 is sufficient.
#       i = 5; while (n/i >= 1): count += n / i; i *= 5
#           return count
# Complexity : O(n)


def findTrailingZeros(n):
    count = 0
    i = 5
    while n / i >= 1:
        count += n / i
        i *= 5

    return count


if __name__ == "__main__":
    n = 100
    print("Count of trailing 0s in " + str(n) + "! is", findTrailingZeros(n))
