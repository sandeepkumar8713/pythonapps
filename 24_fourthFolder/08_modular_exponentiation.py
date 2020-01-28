# https://www.geeksforgeeks.org/modular-exponentiation-power-in-modular-arithmetic/
# Question : Given three numbers x, y and p, compute (xy) % p.
#
# Question Type : ShouldSee
# Used : (50 * 100) mod 13 = ( (50 mod 13) * (100 mod 13) ) mod 13
#        or (5000) mod 13 = ( 11 * 9 ) mod 13
#        or 8 = 8
#        so formula is : (ab) mod p = ( (a mod p) (b mod p) ) mod p
#        while y > 0:
#           if (y & 1) == 1: res = (res * x) % p
#           y = y >> 1  # y = y/2
#           x = (x * x) % p
# Complexity : O(log y)


def power(x, y, p):
    res = 1  # Initialize result

    # Update x if it is more than or equal to p
    x = x % p
    while y > 0:
        # If y is odd, multiply x with result
        if (y & 1) == 1:
            res = (res * x) % p

        # y must be even now
        y = y >> 1  # y = y/2
        x = (x * x) % p

    return res


if __name__ == "__main__":
    x = 2
    y = 5
    p = 13
    print("Power is ", power(x, y, p))
