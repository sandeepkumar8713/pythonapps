# https://leetcode.com/problems/strange-printer/
# Question : There is a strange printer with the following two special properties:
# The printer can only print a sequence of the same character each time.
# At each turn, the printer can print new characters starting from and ending at
# any place and will cover the original existing characters.
# Given a string s, return the minimum number of turns the printer needed to print it.
#
# Question type : Generic
# Used : 1. Make a dp matrix where cell dp[i][j] represents the minimum number of turns the printer needs
#        to print the substring from i to j.
#        2. We initialize the diagonal of the DP table with 1s because the printer only needs one turn
#        to print a single character.
#        3. Note to run i from right hand side. j with i+1 to n-1. Consider cost of not matching.
#        4. Now run a loop k from i to j,
#               if s[k] == s[j]:
#                   then there is overlap.
#                   We can break the substring i to j at k.
#                   We already know the count of dp[i][k]
#                   For other half we take dp[k + 1][j - 1], as ele at j is already printed.
#               keep track of min value among all position of k
#         5. return dp[0][n - 1]
# Logic: for i in range(n - 1, -1, -1):
#           dp[i][i] = 1
#           for j in range(i + 1, n):
#               dp[i][j] = dp[i][j - 1] + 1
#               for k in range(i, j):
#                   if s[k] == s[j]:
#                       tmp = dp[i][k]
#                       if k + 1 <= j - 1:
#                           tmp += dp[k + 1][j - 1]
#                   dp[i][j] = min(dp[i][j], tmp)
#        return dp[0][n - 1]
# Complexity : O(n^3)

def strangePrinter(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for i in range(n - 1, -1, -1):
        dp[i][i] = 1
        for j in range(i + 1, n):
            dp[i][j] = dp[i][j - 1] + 1
            for k in range(i, j):
                if s[k] == s[j]:
                    tmp = dp[i][k]
                    if k + 1 <= j - 1:
                        tmp += dp[k + 1][j - 1]
                    dp[i][j] = min(dp[i][j], tmp)

    return dp[0][n - 1]


if __name__ == "__main__":
    s = "aba"
    print(strangePrinter(s))

    s = "abababababa"  # Print 'a' once and 'b' 5 times
    print(strangePrinter(s))
