# https://www.geeksforgeeks.org/minimum-insertions-to-form-a-palindrome-dp-28/
# Question : Given a string, find the minimum number of characters to be inserted to
# convert it to palindrome. Note that insertion can be in start, middle or end.
# ab: Number of insertions required is 1. bab
# aa: Number of insertions required is 0. aa
# abcd: Number of insertions required is 3. dcbabcd
# abcda: Number of insertions required is 2. adcbcda which is same as number of insertions in the substring bcd
# abcde: Number of insertions required is 4. edcbabcde
#
# Question Type : Generic
# Used : If we find out LCS of string and its reverse, we know how many maximum characters
#        can form a palindrome. We need to insert remaining characters. Find lcs length of
#        string and its reverse and subtract it from length of string.
#        lcs(X, Y, m, n):
#        if m == 0 or n == 0:
#           return 0
#        elif X[m - 1] == Y[n - 1]:
#           return 1 + lcs(X, Y, m - 1, n - 1)
#        else:
#           return max(lcs(X, Y, m, n - 1), lcs(X, Y, m - 1, n))
# Complexity : O(n^2) worst if there is no match in X and Y.


def lcs(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m - 1] == Y[n - 1]:
        return 1 + lcs(X, Y, m - 1, n - 1)
    else:
        return max(lcs(X, Y, m, n - 1), lcs(X, Y, m - 1, n))


def minInsertion(inpStr):
    n = len(inpStr)
    return n - lcs(inpStr, inpStr[::-1], len(inpStr), len(inpStr))


if __name__ == "__main__":
    inpStr = "geeks"
    print(minInsertion(inpStr))
