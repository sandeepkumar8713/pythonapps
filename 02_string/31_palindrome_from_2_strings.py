# Question : Given two strings, A and B, of equal length, find whether it is possible to cut both strings at a common
# point such that the first part of A and the second part of B form a palindrome.
#
# Extension1. How would you change your solution if the strings could be cut at any point (not just a common point)?
# Extension2. Multiple cuts in the strings (substrings to form a palindrome)? Form a palindrome using a substring
# from both strings.
#
# Question Type : ShouldSee
# Used : 1st Question : Run a loop while characters match : Start from left of A and right of B.
#                       We have choose non-matching sub string either from A or B.
#                       Now check if either of the strings are palindrome.
#                       makeStrA = strA[:l] + strA[l:(n - l)] + strB[(r+1):]
#                       makeStrB = strA[:l] + strB[l:(n - l)] + strB[(r + 1):]
#       2nd Question : Run a loop similar to above.
#                      In case of substring (for both A and B), check if it is palindrome, if not remove characters
#                      from one end and repeat, until 1 character is left
#                      return longer of the two string
#                      makeStrA = strA[:l] + middleA + strB[(r+1):]
#                      makeStrB = strA[:l] + middleB + strB[(r + 1):]
#       3rd Question : Reverse the string B, Find longest common sub string between A and revB.
#                      Our palindrome is : commonString + middleChar + commonString[::-1]
#                      Where midChar is next char from A or previous char from B or ''
# Complexity : 1st Question : O(n)
#              2nd Question : O(n^2)
#              3rd Question : O(n^2)


def isPalindrome(inpstr):
    l = 0
    r = len(inpstr) - 1
    while l <= r:
        if inpstr[l] != inpstr[r]:
            return False
        l += 1
        r -= 1
    return True


def firstQuestion(strA,strB):
    if strA[0] != strB[-1]:
        if strB[0] == strA[-1]:
            strA, strB = strB, strA
        else:
            return None

    n = len(strA)
    l = 0
    r = len(strA) - 1
    while l < r:
        if strA[l] == strB[r]:
            pass
        else:
            break
        l += 1
        r -= 1

    makeStrA = strA[:l] + strA[l:(n - l)] + strB[(r+1):]
    makeStrB = strA[:l] + strB[l:(n - l)] + strB[(r + 1):]
    if isPalindrome(makeStrA):
        return makeStrA
    elif isPalindrome(makeStrB):
        return makeStrB
    else:
        None


def secondQuestion(strA,strB):
    if strA[0] != strB[-1]:
        if strB[0] == strA[-1]:
            strA, strB = strB, strA
        else:
            return None

    n = len(strA)
    l = 0
    r = len(strA) - 1
    while l < r:
        if strA[l] == strB[r]:
            pass
        else:
            break
        l += 1
        r -= 1

    middleA = strA[l:(n - l)]
    for i in range(1, len(middleA) + 1):
        if isPalindrome(middleA):
            break
        else:
            middleA = middleA[:-i]

    middleB = strB[l:(n - l)]
    for i in range(1, len(middleB) + 1):
        if isPalindrome(middleB):
            break
        else:
            middleB = middleB[-i:]

    makeStrA = strA[:l] + middleA + strB[(r+1):]
    makeStrB = strA[:l] + middleB + strB[(r + 1):]

    if len(makeStrA) < len(makeStrB):
        return makeStrB
    else:
        return makeStrA


def LCSubStr(X, Y, m, n):
    LCSuff = []
    for i in range(m+1):
        LCSuff.append([0]*(n+1))
    strLen = 0
    row = 0
    col = 0

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                LCSuff[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                LCSuff[i][j] = LCSuff[i - 1][j - 1] + 1
                if LCSuff[i][j] > strLen:
                    strLen = LCSuff[i][j]
                    row = i
                    col = j
            else:
                LCSuff[i][j] = 0

    commonString = ''
    while LCSuff[row][col] != 0:
        commonString = X[row-1] + commonString
        row -= 1
        col -= 1

    return commonString


def thirdQuestion(strA, strB):
    reverseB = strB[::-1]
    commonString = LCSubStr(strA, reverseB, len(strA), len(reverseB))

    nextCharIndexA = strA.find(commonString) + len(commonString)
    prevCharIndexB = strB.find(commonString[::-1]) - 1
    middleChar = ''

    if nextCharIndexA < len(strA):
        middleChar = strA[nextCharIndexA]
    elif prevCharIndexB >= 0:
        middleChar = strB[prevCharIndexB]

    palindrome = commonString + middleChar + commonString[::-1]

    return palindrome


if __name__ == "__main__":
    words = [["ABDE", "CFBA"],
             ["ABCCDE", "STYLBA"],
             ["ABCCEDE", "STYLZBA"],
             ["ABLDE", "CFXBA"],
             ["ABCTYZFY", "CDEFGCBA"],
             ["ABCTTCBL", "UVXYZCBA"]]

    print("\n1st Question:")
    for pair in words:
        print("%s %s : %s" % (pair[0], pair[1], firstQuestion(pair[0], pair[1])))

    words = [["ABCTYZFY", "CDEFGCBA"],
             ["ABCTYTZFY", "CDEFGFCBA"],
             ["ABCYYTZFY", "CDETGFCBA"],
             ["ABCYYTZFY", "CDEFGFCBA"]]

    print("\n2nd Question:")
    for pair in words:
        print("%s %s : %s" % (pair[0], pair[1], secondQuestion(pair[0], pair[1])))

    words = [["ABCVUXT", "FECBADS"],
             ["VUXTABC", "FECBADS"],
             ["VUXTABC", "CBADSFE"],
             ["WER", "ABC"]]

    print("\n3rd Question:")
    for pair in words:
        print("%s %s : %s" % (pair[0], pair[1], thirdQuestion(pair[0], pair[1])))
