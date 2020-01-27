# https://www.geeksforgeeks.org/write-an-efficient-c-program-to-reverse-bits-of-a-number/
# Question : write an efficient c program to reverse bits of a number.
#
# Input : n = 1
# Output : 2147483648
# On a machine with size of unsigned
# bit as 32. Reverse of 0....001 is
# 100....0.
#
# Question Type : Easy
# Used : The idea is to keep putting set bits of the num in reverse_num until num becomes zero. After num becomes zero,
#        shift the remaining bits of reverse_num.
#        Logic :
#        reverseNum = 0
#        while num != 0:
#           reverseNum |= num & 1
#           num >>= 1
#           count -= 1
#           reverseNum <<= 1
#        reverseNum <<= count
#        return reverseNum
# Complexity : O(n)


def reverseBits(num):
    count = 32 - 1
    # Let num is stored using 8 bits and num be 00000110. After the loop you will get reverse_num as 00000011. Now you
    # need to left shift reverse_num 5 more times and you get the exact reverse 01100000.

    reverseNum = 0
    while num != 0:
        reverseNum |= num & 1
        num >>= 1
        count -= 1
        reverseNum <<= 1

    reverseNum <<= count
    return reverseNum


if __name__ == "__main__":
    x = 1
    # x = 2147483648
    print(reverseBits(x))
