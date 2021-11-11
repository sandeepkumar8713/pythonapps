# Question : Given an unsigned integer, swap all odd bits with even bits. For example, if the
# given number is 23 (00010111), it should be converted to 43 (00101011). Every even position
# bit is swapped with adjacent bit on right side, and every odd position bit is swapped
# with adjacent on left side.
#
# Question Type : Generic
# Used : First get even bits by doing and operation with 0xAAAAAAAA
#        Get odd bits by doing and operation with 0x55555555
#        Right shift even by 1. Left shift odd by 1.
#        return even | odd
# Complexity : O(1)


def swapBits(x):
    even_bits = x & 0xAAAAAAAA
    odd_bits = x & 0x55555555
    even_bits >>= 1
    odd_bits <<= 1
    return even_bits | odd_bits


if __name__ == "__main__":
    # 00010111
    x = 23
    # Output is 43 (00101011)
    print(swapBits(x))
