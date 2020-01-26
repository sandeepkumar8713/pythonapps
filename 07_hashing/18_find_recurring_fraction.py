# https://www.geeksforgeeks.org/find-recurring-sequence-fraction/
# Question : Given a fraction, find recurring sequence of digits if exists, otherwise print "No recurring sequence".
#
# Input  : Numerator = 8, Denominator = 3
# Output : Recurring sequence is 6
# Explanation : 8/3 = 2.66666666.......
#
# Input : Numerator = 50, Denominator = 22
# Output : Recurring sequence is 27
# Explanation : 50/22 = 2.272727272.....
#
# Question Type : ShouldSee
# Used : Let us look at the part where we have already figured out the integer part which is
#        floor(numerator/denominator). Now we are left with ( remainder = numerator%denominator ) / denominator.
#        At each step we do the following :
#           Multiply the remainder by 10.
#           Append remainder / denominator to result.
#           Remainder = remainder % denominator.
#       At any moment, if remainder becomes 0, we are done. If we start with remainder 'rem' and if the remainder
#       repeats at any point of time, the digits between the two occurrence of 'rem' keep repeating.
# Complexity : O(n) where n is denominator. As remainder will range from 0 to denominator - 1.


def fractionToDecimal(numerator, denominator):
    res = ""
    hashMap = dict()
    rem = numerator % denominator
    while rem != 0 and rem not in hashMap.keys():
        hashMap[rem] = len(res)
        rem = rem*10
        resPart = rem // denominator
        res += str(resPart)
        rem = rem % denominator

    if rem == 0:
        print("")
    else:
        startIndex = hashMap[rem]
        print(res[startIndex::])


if __name__ == "__main__":
    numerator = 50
    denominator = 22
    fractionToDecimal(numerator, denominator)
