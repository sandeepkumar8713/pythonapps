# CTCI : Q17_06_Count_of_2s
# https://www.geeksforgeeks.org/number-of-occurrences-of-2-as-a-digit-in-numbers-from-0-to-n/
# Question : Count the number of 2s as digit in all numbers from 0 to n
#
# Example : Input n = 573
# 1's place : Once in 10 numbers, 573 / 10 = 57 + 3 > 2 = 58
# 10's place : 10 in 100 numbers, 573 / 100 = 5 * 10 + 20 < 73 > 29 = 60
# 100's place : 100 in 1000 numbers, 573 / 1000 = 0 + 200 < 573 > 299 = 100
# Output = 218
#
# Question Type : ShouldSee
# Used : k = count of digit in number. Now call func k times and add its result, where d is 0...k-1
#        Logic :
#        count2sinRangeAtDigit(number,d):
#           powerOf10 = pow(10,d)
#           nextPowerOf10 = powerOf10 * 10
#           right = number % powerOf10
#           roundDown = number - (number % nextPowerOf10)
#           roundup = roundDown + nextPowerOf10
#           digit = (number // powerOf10) % 10
#           if digit < 2: return roundDown // 10
#           if digit == 2: return roundDown // 10 + right + 1
#           return roundup // 10
#
#         for unit in range(len(s)):
#           count += count2sinRangeAtDigit(number, unit)
#     return count
# Complexity : n(log n)


def count2sinRangeAtDigit(number, d):
    powerOf10 = int(pow(10, d))
    nextPowerOf10 = powerOf10 * 10
    right = number % powerOf10

    roundDown = number - (number % nextPowerOf10)
    roundup = roundDown + nextPowerOf10

    digit = (number // powerOf10) % 10
    if digit < 2:
        return roundDown // 10
    if digit == 2:
        return roundDown // 10 + right + 1
    return roundup // 10


def numberOf2sinRange(number):
    s = str(number)
    len1 = len(s)
    count = 0
    for unit in range(len1):
        print(count2sinRangeAtDigit(number, unit))
        count += count2sinRangeAtDigit(number, unit)
    return count


if __name__ == "__main__":
    # print(numberOf2sinRange(20))
    # print(numberOf2sinRange(22))
    # print(numberOf2sinRange(100))
    # print(numberOf2sinRange(130))
    print(numberOf2sinRange(573))
