# Question : Find duplicate character in a String O(1n) time with no extra space
#
# Used : Maintain a mainRegister set to 0. Loop over the characters in input string. Covert the char to number i from
#           0 to 25. Do left shift of single bit 1(bitRepresent), for given value of i. Do & operation of bitRepresent
#           and mainRegister. If bitRepresent is already present print ch else do or operation :
#           mainRegister = mainRegister | bitRepresent
# Complexity : O(n)


def charToIndex(ch):
    return ord(ch) - ord('a')


def findDuplicate(inpStr):
    mainRegister = 0
    for ch in inpStr:
        bitRepresent = 1
        i = charToIndex(ch)
        bitRepresent = bitRepresent << i

        if (mainRegister & bitRepresent) == bitRepresent:
            print ch
        else:
            mainRegister = mainRegister | bitRepresent


if __name__ == "__main__":
    inpStr = "sandeepkumar"
    findDuplicate(inpStr)
