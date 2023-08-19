# https://leetcode.com/problems/minimum-window-subsequence/
# https://anshika-bhargava0202.medium.com/leetcode-727-minimum-window-subsequence-21c40baff689
# Question : Given strings S and T, find the minimum (contiguous) substring W of S, so that T
# is a subsequence of W. If there is no such window in S that covers all characters in T,
# return the empty string "". If there are multiple such minimum-length windows, return the
# one with the left-most starting index.
#
# Example : Input: S = "abcdebdde", T = "bde"
# Output: "bcde"
#
# Question Type : ShouldSee
# Used : We will use DP here. DP[i][j] saves start index in string[0..i] from where
#        match starts with pattern[0..j]. Now run 2d loop over string and pattern.
#        During loop, if pattern matches dp[i][j] = dp[i - 1][j - 1]
#           else dp[i][j] = dp[i - 1][j]
#        After 2d loop, find min len by running single loop on dp[0..i][p-1].
#        Return substring from minIndex to minLen.
# Logic: s = len(string)
#        p = len(pattern)
#        for i in range(s):
#           if string[i] == pattern[0]:
#               dp[i][0] = i
#           else:
#               if i != 0: dp[i][0] = dp[i - 1][0]
#        for i in range(1, s):
#           for j in range(1, p):
#               if string[i] == pattern[j]:
#                   dp[i][j] = dp[i - 1][j - 1]
#               else:
#                   dp[i][j] = dp[i - 1][j]
#
#        for i in range(s):
#           index = dp[i][p - 1]
#           if index != -1:
#               curLen = i - index + 1
#               if curLen < minLen:
#                   begin = index, minLen = curLen
#        return string[begin: begin + minLen]
# Complexity : O(n * m) where n and m are lengths of string and pattern

import sys


def minWindow(string, pattern):
    s = len(string)
    p = len(pattern)

    dp = []
    for i in range(s):
        dp.append([-1] * p)

    for i in range(s):
        if string[i] == pattern[0]:
            dp[i][0] = i
        else:
            if i != 0:
                dp[i][0] = dp[i - 1][0]

    for i in range(1, s):
        for j in range(1, p):
            if string[i] == pattern[j]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j]

    begin = -1
    minLen = sys.maxsize
    for i in range(s):
        index = dp[i][p - 1]
        if index != -1:
            curLen = i - index + 1
            if curLen < minLen:
                begin = index
                minLen = curLen

    if begin == -1:
        return ""

    return string[begin: begin + minLen]


if __name__ == "__main__":
    string = "abcdebdde"
    pattern = "bde"
    print(minWindow(string, pattern))
