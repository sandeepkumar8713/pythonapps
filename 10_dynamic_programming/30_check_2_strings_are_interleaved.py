# https://www.geeksforgeeks.org/find-if-a-string-is-interleaved-of-two-other-strings-dp-33/
# Question : Given three strings A, B and C. Write a function that checks whether C is an interleaving of A and B.
# C is said to be interleaving A and B, if it contains all characters of A and B and order of all characters in
# individual strings is preserved.
#
# Question Type : Generic
# Used : Make a dp 2 array of size m+1 * n+1
#        Run two loops over A and B, and check if either of the character is present in C. If true set value using
#        previous dp value of matching character.
#        for i in range(m+1):
#           for j in range(n+1):
#               if i == 0 and j == 0: dp[i][j] = True
#               elif i == 0 and B[j - 1] == C[j - 1]: dp[i][j] = dp[i][j - 1]
#               elif j == 0 and A[i - 1] == C[i - 1]: dp[i][j] = dp[i - 1][j]
#               elif A[i - 1] == C[i + j - 1] and B[j - 1] != C[i + j - 1]: dp[i][j] = dp[i - 1][j]
#               elif A[i - 1] != C[i + j - 1] and B[j - 1] == C[i + j - 1]: dp[i][j] = dp[i][j - 1]
#               elif A[i - 1] == C[i + j - 1] and B[j - 1] == C[i + j - 1]: dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
# Complexity : O(m * n)


def isInterleaved(A, B, C):
    m = len(A)
    n = len(B)

    dp = []
    for i in range(m+1):
        dp.append([False] * (n+1))

    if m+n != len(C):
        return False

    for i in range(m+1):
        for j in range(n+1):

            # If both are empty
            if i == 0 and j == 0:
                dp[i][j] = True

            # A is empty
            elif i == 0 and B[j - 1] == C[j - 1]:
                dp[i][j] = dp[i][j - 1]

            # B is empty
            elif j == 0 and A[i - 1] == C[i - 1]:
                dp[i][j] = dp[i - 1][j]

            elif A[i - 1] == C[i + j - 1] and B[j - 1] != C[i + j - 1]:
                dp[i][j] = dp[i - 1][j]

            elif A[i - 1] != C[i + j - 1] and B[j - 1] == C[i + j - 1]:
                dp[i][j] = dp[i][j - 1]

            elif A[i - 1] == C[i + j - 1] and B[j - 1] == C[i + j - 1]:
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

    return dp[m][n]


if __name__ == "__main__":
    A = "XXY"
    B = "XXZ"
    C = "XXZXXXY"
    print(isInterleaved(A, B, C))
    print(isInterleaved("XY", "WZ", "WZXY"))
