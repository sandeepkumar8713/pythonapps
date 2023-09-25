# CTCI : Q16_18_Pattern_Matcher
# https://www.geeksforgeeks.org/match-a-pattern-and-string-without-using-regular-expressions/
# Question : Given a string, find out if string follows a given pattern or not without using
# any regular expressions.
#
# Input: string - GraphTreesGraph
#        pattern - aba
# Output: a->Graph
#         b->Trees
#
# Question Type : ShouldSee
# Used : Make a call to function patternMatch(inpStr, pat, n, m).
#        If n < m: return False
#        Maintain a map for key : character of pattern, value : subString from inpStr
#        Make a call to recursive function patternMatchUtil(inpStr, n, i, pat, m, j, myMap).
#        If it returns true, pattern is found, hence print the map.
# Logic: patternMatchUtil(inpStr, n, i, pat, m, j, myMap):
#        if i == n and j == m: return True
#        if i == n or j == m: return False
#        ch = pat[j]
#        if ch in myMap.keys():
#           alreadyTaggedString = myMap[ch]
#           nextSubString = inpStr[i: i + len(alreadyTaggedString)]
#           if nextSubString != alreadyTaggedString:
#               return False
#           return patternMatchUtil(inpStr, n, i + len(alreadyTaggedString), pat, m, j + 1, myMap)
#        for charLen in range(1, n-i+1):
#           myMap[ch] = inpStr[i: i + charLen]
#           if patternMatchUtil(inpStr, n, i + charLen, pat, m, j + 1, myMap):
#               return True
#           del myMap[ch]
#        return False
# Complexity : O(n!)


def patternMatchUtil(inpStr, n, i, pat, m, j, myMap):
    # If both string and pattern reach their end
    if i == n and j == m:
        return True

    # If either string or pattern reach their end
    if i == n or j == m:
        return False

    ch = pat[j]
    if ch in myMap.keys():
        alreadyTaggedString = myMap[ch]
        nextSubString = inpStr[i: i + len(alreadyTaggedString)]

        if nextSubString != alreadyTaggedString:
            return False
        return patternMatchUtil(inpStr, n, i + len(alreadyTaggedString), pat, m, j + 1, myMap)

    # n-i because i has moved ahead over inpStr
    for charLen in range(1, n-i+1):
        myMap[ch] = inpStr[i: i + charLen]

        if patternMatchUtil(inpStr, n, i + charLen, pat, m, j + 1, myMap):
            return True

        # backtracking
        del myMap[ch]

    return False


def patternMatch(inpStr, pat, n, m):
    if n < m:
        return False

    myMap = dict()
    res = patternMatchUtil(inpStr, n, 0, pat, m, 0, myMap)

    for char, words in myMap.items():
        print(char, words)

    return res


if __name__ == "__main__":
    # inpStr = "GeeksforGeeks"
    # pat = "GfG"

    # inpStr = "GraphTreesGraph"
    # pat = "GG"

    inpStr = "catcatgocatgo"
    pat = "aabab"

    n = len(inpStr)
    m = len(pat)
    print(patternMatch(inpStr, pat, n, m))
