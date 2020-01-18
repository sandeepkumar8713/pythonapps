# https://www.geeksforgeeks.org/print-all-interleavings-of-given-two-strings/
# Question : Given two strings str1 and str2, write a function that prints all inter leavings of the given
# two strings. You may assume that all characters in both strings are different.
# 
# Input: str1 = "AB",  str2 = "CD"
# Output:
#     ABCD
#     ACBD
#     ACDB
#     CABD
#     CADB
#     CDAB
#
# Used : Use recursion, 2 ways choose either from s1 or s2
# Complexity : O((m+n)!)


def toString(List):
    return "".join(List)


def printIlsRecur(str1, str2, iStr, m, n, i):
    if m == 0 and n == 0:
        print toString(iStr)

    if m != 0:
        iStr[i] = str1[0]
        printIlsRecur(str1[1:], str2, iStr, m - 1, n, i + 1)

    if n != 0:
        iStr[i] = str2[0]
        printIlsRecur(str1, str2[1:], iStr, m, n - 1, i + 1)


def printIls(str1, str2, m, n):
    iStr = [''] * (m + n)
    printIlsRecur(str1, str2, iStr, m, n, 0)


if __name__ == "__main__":
    str1 = "AB"
    str2 = "CD"
    printIls(str1, str2, len(str1), len(str2))
