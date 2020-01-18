# Question : Given a string, your task is to count how many palindromic substrings in this string.
# The substrings with different start indexes or end indexes are counted as different substrings even they
# consist of same characters.
#
# Example : Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
#
# Example : Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
#
# Used : Call manachers function, which returns substring palindrome length array centered at i. Now sum array ele/2 to
#        get the result.
#        Logic : def manachers(inpStr):
#        expandedStr = '@#' + '#'.join(inpStr) + '#$'
#        palindromeLen = [0] * len(expandedStr)
#        center = right = 0
#        for i in xrange(1, len(expandedStr) - 1):
#           if i < right:
#               palindromeLen[i] = min(right - i, palindromeLen[2 * center - i])
#           while expandedStr[i + palindromeLen[i] + 1] == expandedStr[i - palindromeLen[i] - 1]:
#               palindromeLen[i] += 1
#           if i + palindromeLen[i] > right:
#               center, right = i, i + palindromeLen[i]
#        return palindromeLen
#        def countSubstrings(inpStr):
#        palindromeLen = manachers(inpStr)
#        for item in palindromeLen:
#           result += (item + 1)/2
#        return result
# Complexity : O(n)


def manachers(inpStr):
    expandedStr = '@#' + '#'.join(inpStr) + '#$'
    palindromeLen = [0] * len(expandedStr)
    center = right = 0

    # Here we try to use the fact that a substring palindrome has already been found at center i - 1, so use its small
    # part to skip some equality check.
    for i in xrange(1, len(expandedStr) - 1):
        if i < right:
            palindromeLen[i] = min(right - i, palindromeLen[2 * center - i])
        while expandedStr[i + palindromeLen[i] + 1] == expandedStr[i - palindromeLen[i] - 1]:
            palindromeLen[i] += 1
        if i + palindromeLen[i] > right:
            center, right = i, i + palindromeLen[i]

    return palindromeLen


def countSubstrings(inpStr):
    palindromeLen = manachers(inpStr)
    result = 0
    for item in palindromeLen:
        result += (item + 1)/2
    return result


if __name__ == "__main__":
    inpStr = "aaa"
    print countSubstrings(inpStr)
