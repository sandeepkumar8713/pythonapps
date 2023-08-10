# https://leetcode.com/problems/scramble-string/
# Question : We can scramble a string s to get a string t using the following algorithm:
# 1. If the length of the string is 1, stop.
# 2. If the length of the string is > 1, do the following:
#    1. Split the string into two non-empty substrings at a random index, i.e.,
#      if the string is s, divide it to x and y where s = x + y.
#    2. Randomly decide to swap the two substrings or to keep them in the same order. i.e.,
#       after this step, s may become s = x + y or s = y + x.
#    3. Apply step 1 recursively on each of the two substrings x and y.
# Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1,
# otherwise, return false.
#
# Question Type : Generic
# Used : DP with sub problem used
#        dp[i][j][length] to represent whether s1[i:i+length] and s2[j:j+length] are scrambled versions of each other.
#        For each value of length, we can iterate through all possible starting indices i and j, and all possible
#        split points k such that 1 <= k < length.
#        if un_swap or swap is true, we set the value true.
# Logic: for i in range(n):
#           for j in range(n):
#               dp[i][j][1] = (s1[i] == s2[j])
#        for length in range(2, n + 1):
#           for i in range(n - length + 1):
#               for j in range(n - length + 1):
#                   for k in range(1, length):
#                       un_swap = dp[i][j][k] and dp[i + k][j + k][length - k]
#                       swap = dp[i][j + length - k][k] and dp[i + k][j][length - k]
#                       if un_swap or swap:
#                           dp[i][j][length] = True
#                           break
#        return dp[0][0][n]
# Complexity : time : O(n^4) space : O(n^3)


def isScramble(s1, s2):
    if s1 == s2:
        return True

    if sorted(s1) != sorted(s2):
        return False

    n = len(s1)
    # DP of size n * n * (n + 1)
    dp = [[[False] * (n + 1) for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            dp[i][j][1] = (s1[i] == s2[j])

    for length in range(2, n + 1):

        for i in range(n - length + 1):
            for j in range(n - length + 1):

                for k in range(1, length):
                    # ABCDEF k = 2
                    # GHIJKL
                    un_swap = dp[i][j][k] and dp[i + k][j + k][length - k]
                    swap = dp[i][j + length - k][k] and dp[i + k][j][length - k]

                    if un_swap or swap:
                        dp[i][j][length] = True
                        break

    return dp[0][0][n]


if __name__ == "__main__":
    print(isScramble("great", "rgeat"))
