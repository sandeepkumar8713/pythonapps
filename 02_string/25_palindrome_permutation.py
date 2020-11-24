# CTCI : Q1_04_Palindrome_Permutation
# Question : Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards.
# A permutation is a rearrangement of letters.
#
# Input : rats live on no evil star
# Output : True
#
# Question Type : ShouldSee
# Used : Here we have to make sure that frequency of each character is even. At most only one
#        character can have odd frequency. Use a bit vector and keep flipping its bits.
#        At end bit vector must be 0 as bits will be flipped even number of times.
#        For 1 odd use this logic : (bitVector & (bitVector - 1)) == 0
# Complexity : O(n)


def toggle(bitVector, index):
    if index < 0:
        return bitVector

    mask = 1 << index
    if (bitVector & mask) == 0:
        bitVector |= mask
    else:
        bitVector &= ~mask
    return bitVector


def createBitVector(phrase):
    bitVector = 0
    for char in phrase:
        x = ord(char)
        bitVector = toggle(bitVector, x)

    return bitVector


def checkAtMostOneBitSet(bitVector):
    return (bitVector & (bitVector - 1)) == 0


def isPermutationOfPalindrome(phrase):
    bitVector = createBitVector(phrase)
    return checkAtMostOneBitSet(bitVector)


if __name__ == "__main__":
    pali = "rats live on no evil star"
    print(isPermutationOfPalindrome(pali))
