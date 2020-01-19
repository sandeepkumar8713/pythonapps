# Question : Given two strings 'X' and 'Y', print the length of the longest common substring. If two or more
# substrings have the same value for longest common substring, then print any one of them.
# Input :  X = "GeeksforGeeks",
#          Y = "GeeksQuiz"
# Output : Geeks
#
# Question Type : Generic
# Used : The longest common suffix has following optimal substructure property
#        LCSuff(X, Y, m, n) = LCSuff(X, Y, m-1, n-1) + 1 if X[m-1] = Y[n-1]
#                        0  Otherwise (if X[m-1] != Y[n-1])
#        To print the substring, keep track of i,j for max length. Now traverse diagonally down from i,j till LCSuff
#        is not 0
#        Here we should have a memorization table to track.
# Complexity : O(m*n)


def LCSubStr(X, Y, m, n):
    # LCSuff is the table with zero value initially in each cell
    LCSuff = [[0 for k in range(n + 1)] for l in range(m + 1)]

    # To store the length of longest common substring
    result = 0
    row = 0
    col = 0

    # Following steps to build
    # LCSuff[m+1][n+1] in bottom up fashion
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                LCSuff[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                LCSuff[i][j] = LCSuff[i - 1][j - 1] + 1
                if LCSuff[i][j] > result:
                    result = LCSuff[i][j]
                    row = i
                    col = j
            else:
                LCSuff[i][j] = 0

    outputstring = ''
    while LCSuff[row][col] != 0:
        # append in reverse
        outputstring = X[row-1] + outputstring
        row -= 1
        col -= 1
    print(outputstring, result)


if __name__ == "__main__":
    X = 'OldSite:GeeksforGeeks.org'
    Y = 'NewSite:GeeksQuiz.com'
    m = len(X)
    n = len(Y)
    LCSubStr(X, Y, m, n)
