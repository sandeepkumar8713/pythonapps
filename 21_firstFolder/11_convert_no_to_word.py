# CTCI : Q16_08_English_Int
# https://www.geeksforgeeks.org/convert-number-to-words/
# Question : Write a method to convert a number (range : 0 to 9 billion) to a String literal,
# e.g. sample input : 12345,  sample output : Twelve Thousand Three Hundred Forty Five.
#
# Question Type : Easy
# Used : Take care to represent values between 0-999. After that break the numbers into hundreds,
#        millions and billions.
#        Now call the above function again.
# Complexity : O(n)

singleDigits = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
                5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}

twoDigits = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
             15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}

tensMultiple = {20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
                60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}

tensPower = {100: "hundred", 1000: "thousand", 1000000: "million", 1000000000: "billion"}


def convertNumber(resStr,inpNum):
    hundred = 100
    if inpNum / hundred > 0:
        resStr += singleDigits[inpNum/hundred] + ' ' + tensPower[hundred] + ' '
        inpNum %= hundred
    if inpNum >= 20:
        if inpNum in tensMultiple:
            resStr += tensMultiple[inpNum] + ' '
        else:
            ones = inpNum % 10
            tens = inpNum - ones
            resStr += tensMultiple[tens] + ' ' + singleDigits[ones] + ' '
    elif inpNum in twoDigits:
        resStr += twoDigits[inpNum] + ' '
    elif inpNum in singleDigits:
        resStr += singleDigits[inpNum] + ' '

    return resStr


def convertBigNumber(inpNum):
    resStr = ''

    if inpNum < 0:
        resStr = 'Negative '
        inpNum *= -1

    thousand = 1000
    million = thousand * thousand
    billion = million * thousand
    if inpNum >= billion:
        resStr = convertNumber(resStr, inpNum/billion) + tensPower[billion] + ' '
        inpNum %= billion
    if inpNum >= million:
        resStr = convertNumber(resStr, inpNum/million) + tensPower[million] + ' '
        inpNum %= million
    if inpNum >= thousand:
        resStr = convertNumber(resStr, inpNum/thousand) + tensPower[thousand] + ' '
        inpNum %= thousand
    return convertNumber(resStr, inpNum) + 'only'


if __name__ == "__main__":
    inpNum = -1954
    inpNum = 0
    # inpNum = 9999
    # inpNum = 2222222
    # inpNum = 222222222222
    print(convertBigNumber(inpNum))
