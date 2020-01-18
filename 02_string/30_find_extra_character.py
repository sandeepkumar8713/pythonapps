# https://www.geeksforgeeks.org/find-one-extra-character-string/
# Question : Given two strings which are of lengths n and n+1. The second string contains all the character
# of the first string, but there is one extra character. Your task to find the extra character in the second
# string.
#
# Used : Add the character of both strings. Their difference will give ascii of extra character.
# Complexity : O(n)


def charToIndex(ch):
    return ord(ch) - ord('a')


def indexToChar(index):
    return chr(index + ord('a'))


def findExtraChar(s1,s2):
    if len(s1) < len(s2):
        big = s2
        small = s1
    else:
        big = s1
        small = s2

    asciiSumBig = 0
    asciiSumSmall = 0

    for char in big:
        asciiSumBig += charToIndex(char)

    for char in small:
        asciiSumSmall += charToIndex(char)
    extraAsciiChar = asciiSumBig - asciiSumSmall

    return indexToChar(extraAsciiChar)


if __name__ == "__main__":
    s1 = "abcd"
    s2 = "cbdae"
    print (findExtraChar(s1,s2))
