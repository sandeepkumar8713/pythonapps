# https://www.geeksforgeeks.org/wildcard-pattern-matching/
# Question : Given a text and a wildcard pattern, implement wildcard pattern matching algorithm that finds if
# wildcard pattern is matched with text. The matching should cover the entire text (not partial text).
# The wildcard pattern can include the characters '?' and '*'
# '?' - matches any single character
# '*' - Matches any sequence of characters (including the empty sequence)
#
# Text = "baaabab",
# Pattern = "*****ba*****ab", output : true
# Pattern = "baaa?ab", output : true
#
# Question Type : ShouldSee
# Used : Here we are maintaining a memory table. dp : size (n+1) * (m+1). Initialize all as False.
#        dp[0][0] = True
#        Only '*' can match with empty string
#        for j in range(1, ptrLen + 1): if pattern[j - 1] == '*': dp[0][j] = dp[0][j - 1]
#        Now Loop
#        for i in range(1, strLen + 1):
#           for j in range(1, ptrLen + 1):
#                 if pattern[j - 1] == '*': dp[i][j] = dp[i][j-1] or dp[i-1][j]
#                 elif pattern[j - 1] == '?' or inpStr[i - 1] == pattern[j - 1]: dp[i][j] = dp[i-1][j-1]
#                 else: dp[i][j] = False
#        return dp[strLen][ptrLen]
# Complexity : O(m*n) m : length of pattern and n : length of string


def strMatch(pattern, inpStr):
    ptrLen = len(pattern)
    strLen = len(inpStr)

    if ptrLen == 0:
        return strLen == 0

    dp = []
    for i in range(strLen+1):
        dp.append([False] * (ptrLen+1))

    dp[0][0] = True

    # Only '*' can match with empty string
    for j in range(1, ptrLen + 1):
        if pattern[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    for i in range(1, strLen + 1):
        for j in range(1, ptrLen + 1):
            #  Two cases if we see a '*'
            #  a) We ignore '*' character and move to next character in the pattern, i.e., '*' indicates an empty
            #     sequence.
            #  b) '*' character matches with ith character in input
            if pattern[j - 1] == '*':
                dp[i][j] = dp[i][j-1] or dp[i-1][j]

            # Current characters are considered as matching in two cases
            # a) current character of pattern is '?'
            # b) characters actually match
            elif pattern[j - 1] == '?' or inpStr[i - 1] == pattern[j - 1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = False

    return dp[strLen][ptrLen]


if __name__ == "__main__":
    inpStr = "baaabab"
    pattern = "*****ba*****ab"
    # pattern = "baaa?ab"
    print(strMatch(pattern, inpStr))
