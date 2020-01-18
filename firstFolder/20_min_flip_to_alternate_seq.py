# https://www.geeksforgeeks.org/number-flips-make-binary-string-alternate/
# Question : Given a binary string, that is it contains only 0s and 1s. We need to make this string a
# sequence of alternate characters by flipping some of the bits, our goal is to minimize the number of
# bits to be flipped.
#
# Input : str = "0001010111"
# Output : 2
# Minimum number of flips required = 2
# We can flip 2nd bit from 0 to 1 and 9th bit from 1 to 0 to make alternate string "0101010101"
#
# Used : Count number of flips required if start with 0 and start with 1. Choose minimum of the two.
# Complexity : O(n)


def flip(ch):
    if ch == '0':
        return '1'
    else:
        return '0'


def getFlipCount(inpStr,expected):
    flipCount = 0
    for i in range(len(inpStr)):
        if inpStr[i] != expected:
            flipCount += 1
        expected = flip(expected)

    return flipCount


if __name__ == "__main__":
    inpStr = "0001010111"
    print "flip count:",min(getFlipCount(inpStr, '0'), getFlipCount(inpStr, '1'))
