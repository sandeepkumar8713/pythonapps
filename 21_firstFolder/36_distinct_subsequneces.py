# https://leetcode.com/problems/distinct-subsequences/
# https://leetcode.com/problems/distinct-subsequences/discuss/462463/Python-DP-Solution-beats-100-time-and-100-space.-Explanation-%2B-Example.
# Question : Given a string S and a string T, count the number of distinct subsequences of S
# which equals T.
#
# A subsequence of a string is a new string which is formed from the original string by deleting
# some (can be none) of the characters without disturbing the relative positions of the remaining
# characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
#
# Example : Input: S = "rabbbit", T = "rabbit"
# Output: 3
#
# Example ($ representing string termination, useful for overflow)
# s = "ababbc$"
# t = "abc$"
#       a  b  c  $
# dp = [0, 0, 0, 1]
# To start is s[5] == c, and increment dp by the count of the string terminator == 1:
#
#       a  b  c  $
# dp = [0, 0, 1, 1]
#
# Question Type : ShouldSee
# Used : We will use dp here. Make a indexDict of smallString.
#        For each char in bigString, loop over its indices from
#        the indexDict and increment the dp value at that index.
# Logic: def numDistinct(bigString, smallString):
#        dp = [0] * (len(smallString) + 1)
#        dp[-1] = 1  # String terminator count
#        for i in range(len(smallString)):
#           c = smallString[i]
#           if c in indexDict.keys():
#               indexDict[c].append(i)
#           else:
#               indexDict[c] = [i]
#        for c in reversed(bigString):
#           for i in indexDict[c]:
#               dp[i] += dp[i + 1]
#        return dp[0]
# Complexity : O(n * m)


def numDistinct(bigString, smallString):
    dp = [0] * (len(smallString) + 1)
    dp[-1] = 1  # String terminator count

    indexDict = dict()
    for i in range(len(smallString)):
        c = smallString[i]
        if c in indexDict.keys():
            indexDict[c].append(i)
        else:
            indexDict[c] = [i]

    for c in reversed(bigString):
        for i in indexDict[c]:
            dp[i] += dp[i + 1]

    return dp[0]


if __name__ == "__main__":
    bigString = "rabbbit"
    smallString = "rabbit"
    print(numDistinct(bigString, smallString))
