# http://www.geeksforgeeks.org/dynamic-programming-set-5-edit-distance/
# Question : Given two strings str1 and str2 and below operations that can performed on str1. Find minimum number
# of edits (operations) required to convert 'str1' into 'str2'.
# Insert
# Remove
# Replace
#
# Question Type : Generic
# Used : Here we are maintaining a memory table. dp : size (m+1) * (n+1). Initialize all as 0.
#        Now loop over each element of the table dp. If it is in first row or col set as 0.
#           If two characters of two strings are same, nothing much to do. Ignore these 2 characters and get count for
#               remaining strings. dp[i][j] = dp[i - 1][j - 1]
#           Else we consider all operations on 'str1',
#               Insert: dp[i][j - 1]
#               Remove: dp[i - 1][j]
#               Replace: dp[i - 1][j - 1]
#               dp[i][j] = 1 + min(dp(insert),dp(remove),dp(replace))
#         return dp[m][n]
# Complexity : O(mn) so O(n^2)


def editDist(str1, str2, m, n):
    dp = []
    for i in range(0, m+1):
        row = [0] * (n + 1)
        dp.append(row)

    # Fill d[][] in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):

            if i == 0:
                dp[i][j] = j  # Min. operations = j

            elif j == 0:
                dp[i][j] = i  # Min. operations = i

            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            else:
                dp[i][j] = 1 + min(dp[i][j - 1],  # Insert
                                   dp[i - 1][j],  # Remove
                                   dp[i - 1][j - 1])  # Replace

    return dp[m][n]


if __name__ == "__main__":
    str1 = "sunday"
    str2 = "saturday"
    print("Minimum operations:", editDist(str1, str2, len(str1), len(str2)))
