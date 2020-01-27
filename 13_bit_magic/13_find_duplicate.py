# CTCI : Q10_08_Find_Duplicates
# Question : You have an array with all the numbers from 1 to N, where N is at most 32,000. The
# array may have duplicate entries and you do not know what N is. With only 4 kilobytes of memory
# available, how would you print all duplicate elements in the array?
#
# Question Type : Easy
# Used : We have to use compact memory. make use of bit vector. 1 int have 32 bits. If there are 32000 integers,
#        we can use 1000 integers to make a bit map where each bit represents if a number is present.
#        Make a class which has array of 1000 elements. It should have set and get function.
#        Now loop over the given input array, using the class check if element is already present else set the bit.
# Complexity : O(n) space : O(n/32)


class BitSet:
    def __init__(self, size):
        self.bitset = [0] * ((size >> 5) + 1)

    def set(self, pos):
        wordNumber = pos >> 5  # divide by 32
        bitNumber = pos & 0x1F  # mod 32
        offset = 1 << bitNumber
        self.bitset[wordNumber] |= offset  # set bit at offset

    def get(self, pos):
        wordNumber = pos >> 5  # divide by 32
        bitNumber = pos & 0x1F  # mod 32
        slot = self.bitset[wordNumber]
        offset = 1 << bitNumber
        return slot & offset # check if that bit is set


def checkDuplicate(inpArr):
    bitSet = BitSet(32000)
    for ele in inpArr:
        if bitSet.get(ele-1):  # bitset starts at 0, numbers start at 1
            print (ele),
        else:
            bitSet.set(ele-1)


if __name__ == "__main__":
    arr = [30, 24, 30, 10, 18, 27, 15, 26, 27, 14, 12, 15, 29, 21, 4, 3, 10, 5, 15, 15, 28, 20, 12, 14,
           21, 10, 1, 10, 27, 20]
    checkDuplicate(arr)
