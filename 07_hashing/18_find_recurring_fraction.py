# https://www.geeksforgeeks.org/find-recurring-sequence-fraction/
# https://leetcode.com/problems/fraction-to-recurring-decimal/
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
# Used : Do normal division and keep track of remainder found with quotient index. If that remain is found again,
#        break and print from that index to end.
#       fractionToDecimal(numerator, denominator):
#       res = "", hashMap = dict()
#       rem = numerator % denominator
#       while rem != 0 and rem not in hashMap.keys():
#           hashMap[rem] = len(res)
#           rem = rem*10
#           resPart = rem // denominator
#           res += str(resPart)
#           rem = rem % denominator
#       if rem == 0: return ""
#       else:
#           startIndex = hashMap[rem]
#           return res[startIndex::]
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
