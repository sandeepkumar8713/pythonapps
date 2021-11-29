# https://leetcode.com/problems/nth-digit/
# Question : Given an integer n, return the nth digit of the infinite integer sequence
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...].
#
# Example : Input: n = 11
# Output: 0
# Explanation: The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0,
# which is part of the number 10.
#
# Question Type : ShouldSee
# Used : Remember this : 1 * 9 [1, 9], 2 * 90 [10, 99], 3 * 900 [100, 999], 4 * 9000 [1000, 9999]
#        Here n is target digits to be used.
#        Following, run a loop of levels to find out n lies b/w which level.
#        While looping also keep track of numberUsed and digitUsed.
#        After the loop, find the digitsRemaining. Divide it by levelNumber to get secondLastNumber
#        If remainder is 0, return last digit of secondLastNumber.
#        else return digit at remainder place of last number.
#        Logic :
#        if n < 10: return n
#        levelCount = 1, digitsUsed = 0, numberUsed = 0
#        thisLevel = 9
#        while True:
#           digitsUsed += thisLevel * levelCount
#           numberUsed += thisLevel
#           nextLevel = thisLevel * 10
#           if thisLevel < n <= nextLevel: break
#           levelCount += 1
#           thisLevel = nextLevel
#        levelCount += 1
#        digitsRemaining = n - digitsUsed
#        secondLastNumber = numberUsed + (digitsRemaining // levelCount)
#        remainder = digitsRemaining % levelCount
# Complexity : O(log10 n) where n in number of digits


def findNthDigit(n):
    # 1 * 9 [1, 9]
    # 2 * 90 [10, 99]
    # 3 * 900 [100, 999]
    # 4 * 9000 [1000, 9999]
    # ...

    if n < 10:
        return n
    levelCount = 1
    digitsUsed = 0
    numberUsed = 0

    thisLevel = 9
    while True:
        digitsUsed += thisLevel * levelCount
        numberUsed += thisLevel

        nextLevel = thisLevel * 10

        if thisLevel < n <= nextLevel:
            break

        levelCount += 1
        thisLevel = nextLevel

    levelCount += 1
    digitsRemaining = n - digitsUsed
    secondLastNumber = numberUsed + (digitsRemaining // levelCount)
    remainder = digitsRemaining % levelCount

    if remainder == 0:
        return secondLastNumber % 10
    else:
        digitsPlace = (levelCount - remainder) + 1
        lastNumber = secondLastNumber + 1
        while digitsPlace > 0:
            rem = lastNumber % 10
            lastNumber //= 10
            digitsPlace -= 1
        return rem


if __name__ == "__main__":
    n = 5000
    print(findNthDigit(n))

    n = 3
    print(findNthDigit(n))

    n = 11
    print(findNthDigit(n))
