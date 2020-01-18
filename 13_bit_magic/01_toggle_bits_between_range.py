# Question : Given a non-negative number n and two values l and r. The problem is to toggle the bits in the range
# l to r in the binary representation of n, i.e, to toggle bits from the rightmost lth bit to the rightmost
# rth bit. A toggle operation flips a bit 0 to 1 and a bit 1 to 0.
#
# Input : n = 17, l = 2, r = 3
# Output : 23
# (17)10 = (10001)2
# (23)10 = (10111)2
# The bits in the range 2 to 3 in the binary
# representation of 17 are toggled
#
# XOR: 0 XOR 0 = 0, 0 XOR 1 = 1, 1 XOR 0 = 1 and 1 XOR 1 = 0. For toggle do XOR with 1.
# Used : Calculate num = ((1 << r) - 1) ^ ((1 << (l-1)) - 1). This will produce a number num having r number of bits
#        and bits in the range l to r are the only set bits.
#        Now, perform n = n ^ num. This will toggle the bits in the range l to r in n.
# Complexity : O(1)


def toggleBitsFromLToR(n,l,r):
    # ^ = XOR
    num = ((1 << r) - 1) ^ ((1 << (l - 1)) - 1)
    print ("N : " + bin(n))
    print ("mask : " + bin(num))
    return n ^ num


if __name__ == "__main__":
    n = 50
    l = 2
    r = 5
    result = toggleBitsFromLToR(n, l, r)
    print ("result : " + bin(result))
    print result

