# CTCI : Q5_06_Conversion
# Question : Write a function to determine the number of bits you would need to flip to convert
# integer A to integer B.
#
# Example :
# Input: 29 (or: 11101), 15 (or: 01111)
# Output: 2
#
# Question Type : Easy
# Used : Each 1 in the XOR represents a bit that is different between A and B. Therefore,
#        to check the number of bits that are different between A and B, we simply need to count
#        the number of bits in A ^ B that are 1.
# Complexity : O(1)


# Python follows 1's complement notation


def bitSwapRequired(a, b):
    count = 0
    c = a ^ b  # XOR
    print(bin(a))
    print(bin(b))
    print(bin(c))
    binary = bin(c)

    # now separate out all 1's from binary string, we need to skip starting two characters
    # of binary string i.e; 0b
    setBits = [ones for ones in binary[2:] if ones == '1']
    return len(setBits)


if __name__ == "__main__":
    a = -23432
    b = 512132
    print(bitSwapRequired(a, b))
