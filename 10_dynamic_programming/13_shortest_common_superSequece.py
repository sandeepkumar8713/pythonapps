# https://www.geeksforgeeks.org/shortest-common-supersequence/
# Question : Given two strings str1 and str2, find the shortest string that has both str1
# and str2 as sub sequences. We need to find length of a string that has both strings as
# sub sequences and is shortest such string.
#
# Input:   str1 = "geek",  str2 = "eke"
# Output: "geeke"
#
# Question Type : Generic
# Used : We have to make a memory table count : dp (m + 1) * (n + 1). Mark all as 0.
#        Loop over each of the elements in dp.
#           If i is 0, then set dp[i][j] = j, as we will have to add all the elements from array Y.
#           If j is 0, then set dp[i][j] = i.
#           If X[i-1] == Y[i-j]: dp[i][j] = 1 + dp[i - 1][j - 1]
#           add this same element once and check for remaining.
#           else dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
#           we will either add i or j and check for remaining and choose whichever gives lower value.
#        return dp[m][n]
#        Use this approach for LCS also as it is more efficient.
# Complexity : O(n^2)


def superSeq(X, Y):
    m = len(X)
    n = len(Y)

    dp = []
    for i in range(m+1):
        dp.append([0] * (n+1))

    # Fill table in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
                # dp[i][j] = 0 lcs

            elif j == 0:
                dp[i][j] = i
                # dp[i][j] = 0 lcs

            elif X[i - 1] == Y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]

            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
                # dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) lcs

    return dp[m][n]


if __name__ == "__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"
    print("Length of the shortest super sequence is:", superSeq(X, Y))
