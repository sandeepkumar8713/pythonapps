# Question : Bit Rotation: A rotation (or circular shift) is an operation similar to shift except that the
# bits that fall off at one end are put back to the other end.
# In left rotation, the bits that fall off at left end are put back at right end.
# In right rotation, the bits that fall off at right end are put back at left end.
#
# Question Type : Easy
# Used : For right rotate, A = right shift n by d, B = (left shift n by (32 - d)) & 0xFFFFFFFF. Ans = A | B
#        For left rotate, A = (left shift n by d) & 0xFFFFFFFF, B = right shift n by (32 - d). Ans = A | B
# Complexity : O(1)

INT_BITS = 32


def leftRotate(n, d):
    return ((n << d) & 0xFFFFFFFF) | (n >> (INT_BITS - d))


def rightRotate(n, d):
    return (n >> d) | ((n << (INT_BITS - d)) & 0xFFFFFFFF)


if __name__ == "__main__":
    n = 16
    d = 2
    print(leftRotate(n, d))
    print(rightRotate(n, d))
