# https://leetcode.com/problems/longest-palindromic-subsequence/
# Given a string s, find the longest palindromic subsequence's length in s.
# A subsequence is a sequence that can be derived from another sequence by deleting some or
# no elements without changing the order of the remaining elements.
#
# Input: s = "bbbab"
# Output: 4
# Explanation: One possible longest palindromic subsequence is "bbbb".
#
# Question Type : Generic
# Used : DP with sub problem
#        Make a 2d array DP where DP[i][j] tells longest palindrome length b/w i and j subsequence.
#        Run 2 loop, i from n-1 to 0, j from i + 1 to n
#           If first and last chars equal:
#               Add 2 and dp value of internal substring
#           else:
#               Find max b/w ignoring first char and last char
#        return dp[0][n-1]
# Logic: dp = [[0] * n for _ in range(n)]
#        for i in range(n - 1, -1, - 1):
#           dp[i][i] = 1
#           for j in range(i + 1, n):
#               if inp_str[i] == inp_str[j]:
#                   dp[i][j] += dp[i + 1][j - 1] + 2
#               else:
#                   dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
#        return dp[0][n - 1]
# Complexity : O(n^2)

def longest_palin_subsequence(inp_str):
    n = len(inp_str)
    dp = [[0] * n for _ in range(n)]

    for i in range(n - 1, -1, - 1):
        dp[i][i] = 1
        for j in range(i + 1, n):
            if inp_str[i] == inp_str[j]:
                dp[i][j] += dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]


if __name__ == "__main__":
    inp_str = "bbbab"
    print(longest_palin_subsequence(inp_str))

    inp_str = "cbbd"
    print(longest_palin_subsequence(inp_str))
